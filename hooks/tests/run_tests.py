#!/usr/bin/env python3
"""run_tests.py — golden-fixture runner for the portable telemetry build.

Asserts the 11 design-§4 fixtures by diff against `expectations.py`, plus:
  - idempotency (re-run into a fresh temp --context-dir == byte-identical)
  - fail-open (malformed JSON / truncated block / missing path / zero-byte)
  - anti-regression (validator blind vs role-aware count)
  - full canonical receipt for fixture 1 (locks the whole schema shape)

No third-party deps. Run:
    python run_tests.py            # full suite
    python run_tests.py --rebuild  # regenerate fixtures first

Exit 0 iff every assertion passes.
"""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
HOOKS = HERE.parent
FX = HERE / "fixtures"

sys.path.insert(0, str(HERE))
import expectations as EXP  # noqa: E402


def _load_extractor():
    spec = importlib.util.spec_from_file_location(
        "telemetry_extract", HOOKS / "telemetry-extract.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["telemetry_extract"] = mod
    spec.loader.exec_module(mod)
    return mod


def _load_validator():
    spec = importlib.util.spec_from_file_location(
        "audit_block_validator", HOOKS / "audit-block-validator.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["audit_block_validator"] = mod
    spec.loader.exec_module(mod)
    return mod


TE = _load_extractor()


def _dotted(receipt, path):
    """Resolve a dotted field path against a receipt dict."""
    cur = receipt
    for key in path.split("."):
        if not isinstance(cur, dict):
            return "<NO-PARENT>"
        cur = cur.get(key, "<MISSING>")
    return cur


def _receipts_for(files, include_at):
    """Build receipts for a fixture (single file or list of files)."""
    if isinstance(files, str):
        files = [files]
    out = []
    for fn in files:
        p = FX / fn
        if not p.exists():
            continue
        cands = TE.iter_receipts_from_jsonl(p, include_assistant_text=include_at)
        out.extend(TE.build_receipt(c) for c in cands)
    return out


def _assert_case(case_name, files, include_at, count, receipt_specs, results):
    """Assert one (file, include_at) case. Appends a (name, ok, detail) tuple."""
    rs = _receipts_for(files, include_at)
    if len(rs) != count:
        results.append((case_name, False,
                        f"count: expected {count}, got {len(rs)}"))
        return
    for i, spec in enumerate(receipt_specs):
        if i >= len(rs):
            results.append((case_name, False, f"receipt[{i}] missing"))
            return
        for field, want in spec.items():
            got = _dotted(rs[i], field)
            if got != want:
                results.append((case_name, False,
                                f"receipt[{i}].{field}: expected {want!r}, got {got!r}"))
                return
    results.append((case_name, True, f"{count} receipt(s) match"))


def _assert_write_dedup(name, spec, results):
    """Write two files sharing a tool_use_id into one temp ctx; assert the writer
    persists exactly `expected_written_lines` (dedup gates the write — R4)."""
    script = HOOKS / "telemetry-extract.py"
    with tempfile.TemporaryDirectory() as ctx:
        for fn in spec["files"]:
            subprocess.run(
                [sys.executable, str(script), "--from", "jsonl",
                 "--path", str(FX / fn), "--context-dir", ctx],
                capture_output=True, text=True)
        rf = Path(ctx) / "roi" / "audit-receipts.jsonl"
        if not rf.exists():
            results.append((name, False, "receipts file not written"))
            return
        lines = rf.read_text(encoding="utf-8").strip().splitlines()
        dup_hits = sum(1 for ln in lines if spec["dup_key"] in ln)
        ok = (len(lines) == spec["expected_written_lines"] and dup_hits == 1)
        results.append((name, ok,
                        f"written lines={len(lines)} (expect "
                        f"{spec['expected_written_lines']}), "
                        f"dup-key occurrences={dup_hits} (expect 1)"))


def run_fx5_two_blocks(results):
    """FX-5 / A1: two DISTINCT blocks in one tool_result share a tool_use_id.
    The extractor must yield 2 raw receipts AND the writer must persist BOTH
    (composite dedup key tool_use_id:block_hash). A tool_use_id-only key would
    collapse them to one line = silent receipt loss."""
    spec = EXP.FX5_TWO_BLOCKS
    name = f"#12 {spec['file']} (FX-5 two blocks, one tool_use_id)"
    # (a) raw extraction yields 2
    rs = _receipts_for(spec["file"], False)
    if len(rs) != spec["raw_receipt_count"]:
        results.append((name, False,
                        f"raw receipts: expected {spec['raw_receipt_count']}, got {len(rs)}"))
        return
    # both carry the shared tool_use_id but have DISTINCT block hashes
    tids = {r["tool_use_id"] for r in rs}
    hashes = {r["block_hash"] for r in rs}
    if tids != {spec["shared_tool_use_id"]} or len(hashes) != 2:
        results.append((name, False,
                        f"expected shared tid + 2 distinct hashes; tids={tids}, "
                        f"distinct_hashes={len(hashes)}"))
        return
    # (b) writer persists BOTH lines
    script = HOOKS / "telemetry-extract.py"
    with tempfile.TemporaryDirectory() as ctx:
        subprocess.run(
            [sys.executable, str(script), "--from", "jsonl",
             "--path", str(FX / spec["file"]), "--context-dir", ctx],
            capture_output=True, text=True)
        rf = Path(ctx) / "roi" / "audit-receipts.jsonl"
        if not rf.exists():
            results.append((name, False, "receipts file not written"))
            return
        lines = rf.read_text(encoding="utf-8").strip().splitlines()
        ok = (len(lines) == spec["written_lines"])
        results.append((name, ok,
                        f"raw=2, distinct hashes=2, written lines={len(lines)} "
                        f"(expect {spec['written_lines']})"))


def run_fx1_roi_parse(results):
    """FX-1 / A2: the ROI minutes regex must parse every mandated phrasing and
    reject the negative lines. Direct unit assertions against _parse_roi."""
    import audit_parse as ap
    cases = [
        ("colon existing",        "- Time saved: ~3 hrs (baseline: x)",                 180),
        ("colon intervening",     "- Time saved on drafting and triage: ~4 hrs",        240),
        ("number-first 'on'",     "- ~4 hrs saved on drafting and triage",              240),
        ("number-first 'producing'", "- ~4 hrs saved producing structured extraction",  240),
        ("thousands comma",       "- ~1,200 mins saved on triage",                      1200),
        ("thousands colon",       "- Time saved: ~1,200 mins",                          1200),
    ]
    neg_section = ("- Elapsed: ~90s\n"
                   "- Tokens: 44k (~$0.3 cost)\n"
                   "- Value: ~$200 (2 hrs x $100/hr senior product professional rate)")
    detail = []
    ok = True
    for label, line, want in cases:
        w = []
        got = ap._parse_roi(line, w)["minutes"]
        if got != want:
            ok = False
            detail.append(f"{label}: expected {want}, got {got}")
    # NEGATIVE: a ROI section with ONLY Elapsed/Tokens/Value -> minutes None
    w = []
    neg = ap._parse_roi(neg_section, w)["minutes"]
    if neg is not None:
        ok = False
        detail.append(f"negative-over-match: expected None, got {neg}")
    results.append(("FX-1 ROI parse (6 phrasings + negative guard)", ok,
                    "; ".join(detail) or "all phrasings parse; negative section -> None"))


def run_fixture_suite(results):
    for c in EXP.EXPECTATIONS:
        name = f"#{c['id']} {c['name']}"
        if "write_dedup" in c:
            _assert_write_dedup(name, c["write_dedup"], results)
            continue
        _assert_case(name, c["file"], c["include_at"], c["count"],
                     c["receipts"], results)
        if "also" in c:
            a = c["also"]
            _assert_case(name + " [--include-assistant-text]", c["file"],
                         a["include_at"], a["count"], a["receipts"], results)


def run_canonical_receipt(results):
    """Lock the full schema shape of fixture 1 against a committed expected json."""
    rs = _receipts_for("01_subagent_tool_result.jsonl", False)
    if len(rs) != 1:
        results.append(("canonical receipt (fx1)", False, "expected exactly 1"))
        return
    got = rs[0]
    expected_path = FX / "01_subagent_tool_result.expected.json"
    if not expected_path.exists():
        results.append(("canonical receipt (fx1)", False,
                        f"missing committed expected: {expected_path.name}"))
        return
    want = json.loads(expected_path.read_text(encoding="utf-8"))
    if got == want:
        results.append(("canonical receipt (fx1)", True, "full schema byte-match"))
    else:
        # Surface the first divergent key for a useful failure.
        diffs = [k for k in set(got) | set(want) if got.get(k) != want.get(k)]
        results.append(("canonical receipt (fx1)", False,
                        f"diverges at: {', '.join(diffs)}"))


def run_idempotency(results):
    """Re-run into a fresh temp ctx; assert byte-identical receipts + dedup."""
    fixture = FX / "01_subagent_tool_result.jsonl"
    script = HOOKS / "telemetry-extract.py"
    with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
        def run(ctx):
            return subprocess.run(
                [sys.executable, str(script), "--from", "jsonl",
                 "--path", str(fixture), "--context-dir", ctx],
                capture_output=True, text=True)
        r1 = run(d1)
        r2 = run(d1)  # second run into SAME ctx -> must dedup
        r3 = run(d2)  # first run into a DIFFERENT fresh ctx
        rf1 = Path(d1) / "roi" / "audit-receipts.jsonl"
        rf2 = Path(d2) / "roi" / "audit-receipts.jsonl"
        ok = True
        detail = []
        # exit codes all 0
        if not (r1.returncode == r2.returncode == r3.returncode == 0):
            ok = False
            detail.append("non-zero exit")
        # run2 must have written 0 (dedup)
        try:
            j2 = json.loads(r2.stdout.strip().splitlines()[-1])
            if j2.get("written") != 0 or j2.get("skipped_dedup") != 1:
                ok = False
                detail.append(f"run2 not deduped: {j2}")
        except Exception as e:
            ok = False
            detail.append(f"run2 stdout unparseable: {e}")
        # receipts file unchanged after run2 (still 1 line)
        if rf1.exists():
            lines = rf1.read_text(encoding="utf-8").strip().splitlines()
            if len(lines) != 1:
                ok = False
                detail.append(f"ctx1 receipts has {len(lines)} lines after 2 runs")
        else:
            ok = False
            detail.append("ctx1 receipts file missing")
        # byte-identical across fresh ctxs
        if rf1.exists() and rf2.exists():
            if rf1.read_bytes() != rf2.read_bytes():
                ok = False
                detail.append("receipts NOT byte-identical across fresh ctxs")
        else:
            ok = False
            detail.append("a receipts file missing")
    results.append(("idempotency (re-run == no-op, byte-identical)", ok,
                    "; ".join(detail) or "deduped, byte-identical"))


def run_failopen(results):
    """Fail-open: exit 0 + no crash on malformed/truncated/missing/zero-byte."""
    script = HOOKS / "telemetry-extract.py"
    cases = [
        ("malformed JSON line", "09_malformed.jsonl"),
        ("truncated block", "08_truncated.jsonl"),
        ("missing path", "__DOES_NOT_EXIST__.jsonl"),
        ("zero-byte file", "zero_byte.jsonl"),
    ]
    all_ok = True
    detail = []
    for label, fn in cases:
        r = subprocess.run(
            [sys.executable, str(script), "--from", "jsonl",
             "--path", str(FX / fn), "--summary"],
            capture_output=True, text=True)
        if r.returncode != 0:
            all_ok = False
            detail.append(f"{label}: exit {r.returncode}")
    # truncated MUST still yield 1 receipt with roi.minutes None
    rs = _receipts_for("08_truncated.jsonl", False)
    if not (len(rs) == 1 and rs[0]["roi"]["minutes"] is None):
        all_ok = False
        detail.append("truncated did not yield 1 receipt w/ minutes None")
    # malformed MUST still yield 1
    rs = _receipts_for("09_malformed.jsonl", False)
    if len(rs) != 1:
        all_ok = False
        detail.append(f"malformed yielded {len(rs)} (expected 1)")
    results.append(("fail-open (4 bad inputs -> exit 0, partial output)", all_ok,
                    "; ".join(detail) or "all 4 exit 0, partial output preserved"))


def run_anti_regression(results):
    """Validator blind vs role-aware count divergence on a known fixture."""
    v = _load_validator()
    ar = EXP.ANTI_REGRESSION
    p = FX / ar["file"]
    blind = len(v.scan_jsonl(p))
    role = len(v.scan_jsonl_role_aware(p))
    ok = (blind == ar["blind_count"] and role == ar["role_aware_count"]
          and blind > role)
    results.append(("anti-regression (blind vs role-aware count)", ok,
                    f"blind={blind} (expect {ar['blind_count']}), "
                    f"role-aware={role} (expect {ar['role_aware_count']})"))


def run_anchors(results):
    """Re-establish the frozen anchors: pure-decoy -> 0, mixed -> exact genuine."""
    decoy = _receipts_for("04_pure_decoy.jsonl", False)
    mixed = _receipts_for("05_mixed.jsonl", False)
    ok = (len(decoy) == 0 and len(mixed) == 1)
    results.append(("anchors (pure-decoy->0, mixed->1 genuine)", ok,
                    f"pure-decoy={len(decoy)} (expect 0), "
                    f"mixed={len(mixed)} (expect 1)"))


import ast as _ast

# Envelope identifiers that, when READ structurally (not as an output literal),
# mean audit_parse has reached into harness-jsonl shape. The plain output field
# name JOIN_KEY = "tool_use_id" is a Constant assignment, never one of these reads.
_ENVELOPE_NAMES = {"tool_use", "tool_use_id", "tool_result", "usage", "content", "type"}
_ENVELOPE_ATTRS = {"content", "usage", "role"}  # e.g. message.content / message.usage
_CONSUMER_MODS = ("telemetry-extract", "telemetry_extract", "audit-block-validator",
                  "audit_block_validator")


def run_portability_gate(results):
    """Chief Architect's redefined portability gate (2026-05-30) — tests the REAL
    invariant via AST, not string presence (which a split literal could dodge and
    a docstring could false-trip):
      (a) import-isolation — audit_parse imports nothing from the consumer modules;
      (b) no envelope-READS — no `X.get("tool_use"...)`, `X["tool_result"]`, or
          `message.content/usage` accesses in executable code. Docstrings/comments
          and the output literal `JOIN_KEY = "tool_use_id"` are ignored because the
          AST sees them as Constants, not Call/Subscript/Attribute reads."""
    src = (HOOKS / "audit_parse.py").read_text(encoding="utf-8")
    tree = _ast.parse(src)

    bad_imports, reads = [], []
    for node in _ast.walk(tree):
        # (a) imports of consumer modules
        if isinstance(node, _ast.ImportFrom) and node.module and \
                any(m in node.module for m in _CONSUMER_MODS):
            bad_imports.append(node.module)
        if isinstance(node, _ast.Import):
            for n in node.names:
                if any(m in n.name for m in _CONSUMER_MODS):
                    bad_imports.append(n.name)
        # (b1) X.get("<envelope>") calls
        if isinstance(node, _ast.Call) and isinstance(node.func, _ast.Attribute) \
                and node.func.attr == "get" and node.args \
                and isinstance(node.args[0], _ast.Constant) \
                and node.args[0].value in _ENVELOPE_NAMES:
            reads.append(f'.get("{node.args[0].value}")')
        # (b2) X["<envelope>"] subscripts
        if isinstance(node, _ast.Subscript) and isinstance(node.slice, _ast.Constant) \
                and node.slice.value in _ENVELOPE_NAMES:
            reads.append(f'["{node.slice.value}"]')
        # (b3) <name>.content / .usage / .role attribute reads (e.g. message.content)
        if isinstance(node, _ast.Attribute) and node.attr in _ENVELOPE_ATTRS \
                and isinstance(node.value, _ast.Name):
            reads.append(f"{node.value.id}.{node.attr}")

    ok = not bad_imports and not reads
    detail = []
    if bad_imports:
        detail.append(f"consumer import in leaf: {bad_imports}")
    if reads:
        detail.append(f"envelope-read in leaf: {reads}")
    results.append(("portability gate (AST: import-isolation + no envelope-reads)", ok,
                    "; ".join(detail) or "leaf imports only stdlib; zero envelope reads"))


def main():
    if "--rebuild" in sys.argv:
        subprocess.run([sys.executable, str(HERE / "build_fixtures.py")], check=True)
        # ensure anti-regression + canonical-expected exist
        subprocess.run([sys.executable, str(HERE / "make_aux.py")], check=False)

    results = []
    run_fixture_suite(results)
    run_fx5_two_blocks(results)
    run_fx1_roi_parse(results)
    run_canonical_receipt(results)
    run_idempotency(results)
    run_failopen(results)
    run_anti_regression(results)
    run_anchors(results)
    run_portability_gate(results)

    passed = sum(1 for _, ok, _ in results if ok)
    total = len(results)
    print(f"\n{'='*72}\nTELEMETRY GOLDEN-FIXTURE SUITE — {passed}/{total} PASS\n{'='*72}")
    for name, ok, detail in results:
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {name}")
        if not ok:
            print(f"         -> {detail}")
        elif "--verbose" in sys.argv:
            print(f"         -> {detail}")
    print()
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
