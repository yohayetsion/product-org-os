#!/usr/bin/env python3
"""telemetry-extract.py — Portable Spawn Audit Block receipt reader (T1).

The ONE place that knows the Claude-Code jsonl envelope (design I1 / §5). All
harness-shape field names (`type`, `message.content`, `tool_use`/`tool_result`,
`tool_use_id`, `message.usage`) live in `iter_receipts_from_jsonl` and its
private helpers. `audit_parse.py` (the portable core) never sees them.

Modes (CLI):
  --from jsonl  --path <file>           extract from one Claude-Code transcript
  --from dir    --path <dir>            fan over *.jsonl ( --recursive for **/ )
  --from text   --path <file>           treat file as plain text (no join)
  --from stdin                          read plain text from stdin (no join)

Flags:
  --context-dir <ctx>                   where writers append (default: ./context)
  --summary                             print machine-readable JSON, NO writes
  --include-assistant-text              accept assistant-role text blocks (default OFF)
  --include-no-block-fallback           reserved escape hatch (default OFF; no-op here)
  --recursive                           dir mode: recurse into subdirs

Design contracts honored: D1 (manual run, no hooks), D2 (parse never re-derive),
R3 (does NOT call/modify os-tracker writers — owns its own richer writer),
R4 (separate unbounded .telemetry-dedup), R7 (token reconciliation best-effort),
R8 (line-by-line json.loads in try/except, errors='replace', ensure_ascii=True,
temp-file + os.replace). Fail-open: never raises out of main; exits 0.

Stdlib only. Python 3.8+.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys
from collections import namedtuple
from datetime import datetime, timezone
from pathlib import Path

# Import the PORTABLE core. Hyphenated sibling modules can't be imported, but
# audit_parse.py uses an underscore, so a normal import works once this file's
# directory is on sys.path (it is, when run as a script).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_parse import (  # noqa: E402
    extract_blocks,
    parse_block,
    block_hash,
    normalize_block,
    NEW_HEADER_RE,
    SECTION_RE,
)


def _has_section_line(block_text: str) -> bool:
    """A4: a captured block is a real receipt only if it contains at least one
    `[section]` line (e.g. `[Pre-Execution Loads]` / `[Post-Execution ROI]`).
    A genuine-spawn tool_result whose PROSE merely name-drops the header
    ("...the 📋 Spawn Audit Block earlier...") has no `[section]` line and is
    rejected here, so it can't inflate counts with an empty-loads junk receipt."""
    for line in block_text.split("\n"):
        if SECTION_RE.match(line.strip()):
            return True
    return False

def _ensure_utf8_stdout():
    """Make stdout surrogate-safe. Called only from main() — NEVER at import.

    Doing this at import time would rebind/wrap the stdout of any module that
    imports us (e.g. the validator's --role-aware path), and the wrapper closing
    on teardown breaks the importer's later prints ("I/O operation on closed
    file"). So it is strictly a __main__-time concern.
    """
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    except Exception:
        pass

# ---------------------------------------------------------------------------
# Harness-shape knowledge — CONFINED TO THIS MODULE (I1)
# ---------------------------------------------------------------------------

# Same shape os-tracker's AGENT_IDENTITY_PATTERN uses; matches OS ("in a
# simulated...") and ET ("on the {Team} Team").
IDENTITY_SENTINEL_RE = re.compile(r"You are \*\*.+?\*\* (?:in|on)\b")
AGENT_ID_IN_DESC_RE = re.compile(r"^\[([a-z][a-z0-9-]*)\]")
DISPLAY_NAME_RE = re.compile(r"You are \*\*(?:[^\w\s]*\s*)?(.+?)\*\* (?:in|on)\b")

RawCandidate = namedtuple(
    "RawCandidate",
    ["text", "source_tag", "tool_use_id", "agent_slug_hint", "usage", "start_line", "is_old", "source", "ts"],
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _iter_jsonl_objects(path: Path):
    """Yield parsed JSON objects, one per line. R8: never abort on a bad line.

    A5: opened with `utf-8-sig` so a UTF-8 BOM on line 1 is consumed by the
    decoder instead of being prepended to the first JSON object (which would make
    line 1's `json.loads` fail and silently drop the first transcript event).
    `utf-8-sig` strips a leading BOM if present and otherwise behaves as utf-8.
    A defensive per-line lstrip of a stray BOM char covers mid-stream BOMs too."""
    try:
        f = path.open("r", encoding="utf-8-sig", errors="replace")
    except Exception:
        return
    with f:
        for raw in f:
            raw = raw.lstrip("﻿").strip()
            if not raw:
                continue
            try:
                yield json.loads(raw)
            except Exception:
                continue  # skip bad line, keep going


def _content_parts(obj):
    """Normalize message.content (list | str) into a list of part-dicts."""
    msg = obj.get("message") or {}
    content = msg.get("content")
    if isinstance(content, list):
        return [p for p in content if isinstance(p, dict)]
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    return []


def _role(obj):
    msg = obj.get("message") or {}
    return msg.get("role") or obj.get("type")


def _timestamp_of(obj):
    return obj.get("timestamp") or (obj.get("message") or {}).get("timestamp")


def _usage_of(obj):
    """Best-effort token usage (R7). Returns int total or None."""
    usage = (obj.get("message") or {}).get("usage")
    if not isinstance(usage, dict):
        return None
    total = 0
    found = False
    for k in ("input_tokens", "output_tokens", "cache_read_input_tokens",
              "cache_creation_input_tokens"):
        v = usage.get(k)
        if isinstance(v, (int, float)):
            total += int(v)
            found = True
    return total if found else None


def _tool_result_text(part) -> str:
    """Flatten a tool_result's content into a single string."""
    c = part.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        out = []
        for x in c:
            if isinstance(x, dict) and x.get("type") == "text":
                out.append(x.get("text", ""))
            elif isinstance(x, str):
                out.append(x)
        return "\n".join(out)
    return ""


def _slug_from_prompt(prompt: str) -> str:
    """[agent-key] in description-equivalent header, else display-name->slug."""
    # In spawn prompts the agent-key convention lives in the Task description, not
    # the prompt body; but the prompt does carry "You are **{emoji} {Name}**".
    m = DISPLAY_NAME_RE.search(prompt)
    if m:
        name = m.group(1).strip()
        # strip any leading emoji/punctuation tokens
        name = re.sub(r"^[^A-Za-z]+", "", name).strip()
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        if slug:
            return slug
    return "unknown-agent"


# ---------------------------------------------------------------------------
# THE harness adapter — two-pass structural join (design §2)
# ---------------------------------------------------------------------------

def iter_receipts_from_jsonl(path, *, include_assistant_text=False):
    """Yield RawCandidate for every accepted Spawn Audit Block in a transcript.

    Two-pass: Pass 1 builds {tool_use_id: {slug, prompt}} from genuine Agent/Task
    spawns; Pass 2 accepts blocks ONLY from (a) tool_results whose tool_use_id is
    in the spawn map, or (b) gated assistant-text leading with the block header.
    """
    path = Path(path)

    # ---------- PASS 1: build the spawn map ----------
    spawn_map = {}
    for obj in _iter_jsonl_objects(path):
        for part in _content_parts(obj):
            if part.get("type") == "tool_use" and part.get("name") in ("Agent", "Task"):
                inp = part.get("input") or {}
                prompt = inp.get("prompt", "") or ""
                if IDENTITY_SENTINEL_RE.search(prompt):
                    tid = part.get("id")
                    if tid:
                        # description may carry [agent-key]; prefer it when present
                        slug = None
                        desc = inp.get("description", "") or ""
                        dm = AGENT_ID_IN_DESC_RE.match(desc.strip())
                        if dm:
                            slug = dm.group(1)
                        if not slug:
                            slug = _slug_from_prompt(prompt)
                        spawn_map[tid] = {"slug": slug, "prompt": prompt}

    # ---------- PASS 2: accept blocks from exactly two sources ----------
    seen_hashes = set()
    for obj in _iter_jsonl_objects(path):
        ts = _timestamp_of(obj)

        # SOURCE (a) — tool_result whose tool_use_id is a genuine spawn [PRIMARY]
        for part in _content_parts(obj):
            if part.get("type") == "tool_result":
                tid = part.get("tool_use_id")
                if tid in spawn_map:
                    text = _tool_result_text(part)
                    for (ln, block, is_old) in extract_blocks(text):
                        # A4: reject header-line-only prose (no [section] line).
                        # v1-legacy blocks legitimately have no [section] markers,
                        # so the guard applies to new-format blocks only.
                        if not is_old and not _has_section_line(block):
                            continue
                        yield RawCandidate(
                            text=block, source_tag=path.name,
                            tool_use_id=tid, agent_slug_hint=spawn_map[tid]["slug"],
                            usage=_usage_of(obj), start_line=ln, is_old=is_old,
                            source="tool_result", ts=ts,
                        )

        # SOURCE (b) — assistant-role text that LEADS with the block [GATED, OFF]
        if include_assistant_text and _role(obj) == "assistant":
            for part in _content_parts(obj):
                if part.get("type") == "text":
                    t = part.get("text", "")
                    head = t[:200]
                    if NEW_HEADER_RE.search(head) and "[Pre-Execution Loads]" in t:
                        for (ln, block, is_old) in extract_blocks(t):
                            # A4: same section-line guard as SOURCE (a).
                            if not is_old and not _has_section_line(block):
                                continue
                            h = block_hash(block)
                            if h in seen_hashes:
                                continue
                            seen_hashes.add(h)
                            yield RawCandidate(
                                text=block, source_tag=path.name,
                                tool_use_id=None, agent_slug_hint=None,
                                usage=None, start_line=ln, is_old=is_old,
                                source="assistant-text", ts=ts,
                            )
        # EXCLUDE BY CONSTRUCTION: every other tool_result + plain user/assistant
        # text. These are the decoy class that produced the misleading 22% rate.


def iter_receipts_from_text(text, source_tag):
    """Text/stdin mode: no envelope, no join. extract_blocks on raw text."""
    for (ln, block, is_old) in extract_blocks(text):
        yield RawCandidate(
            text=block, source_tag=source_tag,
            tool_use_id=None, agent_slug_hint=None,
            usage=None, start_line=ln, is_old=is_old,
            source="text-mode", ts=None,
        )


def iter_receipts_from_dir(path, *, recursive=False, include_assistant_text=False):
    """Glob *.jsonl (non-recursive) / **/*.jsonl (recursive); fan into jsonl."""
    path = Path(path)
    pattern = "**/*.jsonl" if recursive else "*.jsonl"
    for jsonl in sorted(path.glob(pattern)):
        for cand in iter_receipts_from_jsonl(
            jsonl, include_assistant_text=include_assistant_text
        ):
            yield cand


# ---------------------------------------------------------------------------
# build_receipt — overlay join-derived fields onto the parsed receipt
# ---------------------------------------------------------------------------

def build_receipt(candidate) -> dict:
    receipt = parse_block(
        candidate.text, candidate.source_tag,
        start_line=candidate.start_line, is_old_format=candidate.is_old,
    )
    receipt["source"] = candidate.source
    receipt["ts"] = candidate.ts or _now_iso()
    receipt["tool_use_id"] = candidate.tool_use_id

    # Join slug wins over in-block slug — the join is structurally trustworthy.
    if candidate.agent_slug_hint and candidate.agent_slug_hint != "unknown-agent":
        receipt["agent_slug"] = candidate.agent_slug_hint
        if not receipt["authors"] or receipt["authors"] == ["unknown-agent"]:
            receipt["authors"] = [candidate.agent_slug_hint]

    # Token reconciliation (R7): reported stays authoritative (I2/D2).
    if candidate.usage:
        receipt["roi"]["measured_tokens"] = candidate.usage
        rep = receipt["roi"].get("tokens")
        if rep:
            try:
                receipt["roi"]["drift"] = round(candidate.usage / rep, 2)
            except ZeroDivisionError:
                receipt["roi"]["drift"] = None
    return receipt


# ---------------------------------------------------------------------------
# Dedup — separate, per-run-unbounded .telemetry-dedup (R4)
# ---------------------------------------------------------------------------

def _dedup_key(receipt) -> str:
    """Dedup key (FX-5 / A1): COMPOSITE `tool_use_id:block_hash[:12]` so two
    DISTINCT blocks sharing one tool_use_id (e.g. a joint emission + a follow-up
    block in the same tool_result) both persist. Cross-file replays of the SAME
    block under the same id still collapse (the block_hash matches). Null
    tool_use_id (assistant-text / text-mode) falls back to block_hash only.
    Honors design §3.2 ("tool_use_id | block_hash")."""
    tid = receipt.get("tool_use_id")
    bh = receipt.get("block_hash") or ""
    if tid:
        return f"{tid}:{bh[:12]}"
    return "hash:" + bh


def _load_dedup(context_dir: Path) -> set:
    f = context_dir / ".telemetry-dedup"
    if not f.exists():
        return set()
    try:
        return set(x.strip() for x in f.read_text(encoding="utf-8").splitlines() if x.strip())
    except Exception:
        return set()


def _atomic_write(path: Path, text: str) -> None:
    """Temp-file + os.replace (R8). ensure_ascii handled by callers for jsonl."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.replace(tmp, path)


def _atomic_append(path: Path, text: str) -> None:
    """Append by read-modify-atomic-write (keeps fail-open + temp-file safety)."""
    existing = ""
    if path.exists():
        try:
            existing = path.read_text(encoding="utf-8")
        except Exception:
            existing = ""
    _atomic_write(path, existing + text)


# ---------------------------------------------------------------------------
# Writers — OWN richer writer + canonical jsonl (R3: never call os-tracker)
# ---------------------------------------------------------------------------

ROI_MD_HEADER = (
    "# Telemetry ROI Log (audit-block receipts)\n\n"
    "| Time | Source File | Agent | Format | Min Saved | Tokens | Value $ | "
    "Packs | DR Drafted | DR Updated | Drift | tool_use_id/hash |\n"
    "|------|-------------|-------|--------|-----------|--------|---------|"
    "-------|------------|------------|-------|------------------|\n"
)


def _roi_md_row(r) -> str:
    roi = r["roi"]
    loads = r["loads"]
    dr = r.get("decision_records") or {}
    mins = roi["minutes"] if roi["minutes"] is not None else "—"
    toks = roi["tokens"] if roi["tokens"] is not None else "—"
    val = roi["value_usd"] if roi["value_usd"] is not None else "—"
    drift = roi["drift"] if roi["drift"] is not None else "—"
    packs = loads["preload_packs"]["count"]
    packs = packs if packs is not None else "—"
    dr_drafted = len(dr.get("drafted", [])) if dr else 0
    dr_updated = len(dr.get("updated", [])) if dr else 0
    key = r.get("tool_use_id") or ("hash:" + (r.get("block_hash", "")[:12]))
    return (
        f"| {r['ts']} | {r['source_file']} | {r['agent_slug']} | {r['format']} | "
        f"{mins} | {toks} | {val} | {packs} | {dr_drafted} | {dr_updated} | "
        f"{drift} | {key} |\n"
    )


def _jsonl_line(r) -> str:
    return json.dumps(r, ensure_ascii=True) + "\n"


def _interaction_entry(r) -> str:
    dr = r.get("decision_records") or {}
    related = ", ".join((dr.get("drafted", []) + dr.get("updated", []))[:5]) or "—"
    return (
        f"### {r['ts']} | {r['agent_slug']} | {r['format']}\n\n"
        f"**Source**: {r['source']} ({r['source_file']})\n"
        f"**tool_use_id**: {r.get('tool_use_id') or '—'}\n"
        f"**Related DRs**: {related}\n"
        f"**Min saved**: {r['roi']['minutes'] if r['roi']['minutes'] is not None else '—'}\n\n"
        f"---\n\n"
    )


def write_receipts(receipts, context_dir):
    """Write all telemetry outputs. Dedup-gated (R4). Returns count written."""
    context_dir = Path(context_dir)
    dedup = _load_dedup(context_dir)

    roi_rows = []
    jsonl_lines = []
    interaction_lines = []
    dr_event_lines = []
    new_keys = []
    written = 0

    for r in receipts:
        key = _dedup_key(r)
        if key in dedup:
            continue
        dedup.add(key)
        new_keys.append(key)
        written += 1

        roi_rows.append(_roi_md_row(r))
        jsonl_lines.append(_jsonl_line(r))
        interaction_lines.append(_interaction_entry(r))

        dr = r.get("decision_records") or {}
        for drid in dr.get("drafted", []):
            dr_event_lines.append(f"- {r['ts']} | {drid} | drafted | {r['agent_slug']}\n")
        for drid in dr.get("updated", []):
            dr_event_lines.append(f"- {r['ts']} | {drid} | updated | {r['agent_slug']}\n")

    if written == 0:
        return 0

    # 1) canonical jsonl (system of record)
    receipts_file = context_dir / "roi" / "audit-receipts.jsonl"
    _atomic_append(receipts_file, "".join(jsonl_lines))

    # 2) richer ROI .md (projection)
    roi_md = context_dir / "roi" / "telemetry-roi-log.md"
    if not roi_md.exists() or roi_md.stat().st_size == 0:
        _atomic_write(roi_md, ROI_MD_HEADER)
    _atomic_append(roi_md, "".join(roi_rows))

    # 3) interactions day-log (same on-disk shape os-tracker uses, our own copy)
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    year = date[:4]
    int_file = context_dir / "interactions" / year / f"{date}.md"
    if not int_file.exists():
        _atomic_write(int_file, f"# Interactions — {date} (telemetry-extract)\n\n")
    _atomic_append(int_file, "".join(interaction_lines))

    # 4) DR events appended to decisions index
    if dr_event_lines:
        dr_index = context_dir / "decisions" / "index.md"
        if not dr_index.exists():
            _atomic_write(dr_index, "# Decisions Index\n\n## Telemetry DR events\n\n")
        _atomic_append(dr_index, "".join(dr_event_lines))

    # 5) dedup ledger (unbounded, R4)
    dedup_file = context_dir / ".telemetry-dedup"
    _atomic_append(dedup_file, "".join(k + "\n" for k in new_keys))

    return written


# ---------------------------------------------------------------------------
# Summary (no writes) — design §3.4
# ---------------------------------------------------------------------------

def summary(receipts, spawns_count) -> dict:
    receipts = list(receipts)
    total = len(receipts)
    v1 = sum(1 for r in receipts if r["format"] == "v1-legacy")
    non_legacy = total - v1
    value = sum(r["roi"]["value_usd"] or 0 for r in receipts)

    by_source = {"tool_result": 0, "assistant-text": 0, "text-mode": 0, "no-block-fallback": 0}
    for r in receipts:
        by_source[r["source"]] = by_source.get(r["source"], 0) + 1

    implausible = []
    for r in receipts:
        roi = r["roi"]
        if roi["drift"] is not None and roi["drift"] > 3:
            implausible.append({"source_file": r["source_file"],
                                "reason": "drift>3x", "tool_use_id": r.get("tool_use_id")})
        if roi["value_usd"] and roi["minutes"] is None:
            implausible.append({"source_file": r["source_file"],
                                "reason": "value-no-minutes", "tool_use_id": r.get("tool_use_id")})

    # v2_pass_rate proxy (A3): a block passes only if it is non-legacy, has a
    # SKILL.md path, has a [Post-Execution ROI] section (reported_raw non-empty)
    # AND that ROI is structurally parseable — at least one of minutes/tokens/
    # value_usd came through. Pure-garbage ROI (reported_raw present but nothing
    # parsed) no longer inflates the rate. Valid blocks (which parse at least one
    # field) keep passing, so existing pass-rate semantics for real blocks hold.
    def _passes(r):
        roi = r["roi"]
        roi_parsed = (roi["minutes"] is not None
                      or roi["tokens"] is not None
                      or roi["value_usd"] is not None)
        return (r["format"] != "v1-legacy"
                and bool(r["loads"]["skill_md"]["path"])
                and bool(roi["reported_raw"])
                and roi_parsed)
    passing = sum(1 for r in receipts if _passes(r))
    pass_rate = round(passing / non_legacy, 4) if non_legacy else 0.0

    return {
        "spawns": spawns_count,
        "receipts": total,
        "v1_legacy_count": v1,
        "v2_pass_rate": pass_rate,
        "value_usd": value,
        "implausible": implausible,
        "by_source": by_source,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _count_spawns_jsonl(path, *, recursive=False, is_dir=False):
    """Count genuine Agent/Task spawns (size of spawn_map) for --summary."""
    total = 0
    paths = []
    if is_dir:
        pattern = "**/*.jsonl" if recursive else "*.jsonl"
        paths = sorted(Path(path).glob(pattern))
    else:
        paths = [Path(path)]
    for p in paths:
        spawn_ids = set()
        for obj in _iter_jsonl_objects(p):
            for part in _content_parts(obj):
                if part.get("type") == "tool_use" and part.get("name") in ("Agent", "Task"):
                    inp = part.get("input") or {}
                    prompt = inp.get("prompt", "") or ""
                    if IDENTITY_SENTINEL_RE.search(prompt) and part.get("id"):
                        spawn_ids.add(part.get("id"))
        total += len(spawn_ids)
    return total


def _gather(args):
    """Return (receipts:list, spawns:int) for the chosen mode. Fail-open."""
    src = args.__dict__["from"]
    include_at = args.include_assistant_text

    if src == "stdin":
        text = sys.stdin.read()
        cands = iter_receipts_from_text(text, "<stdin>")
        return [build_receipt(c) for c in cands], 0

    if not args.path:
        print("error: --path required for --from %s" % src, file=sys.stderr)
        return [], 0
    p = Path(args.path)

    if src == "text":
        if not p.exists():
            return [], 0
        text = p.read_text(encoding="utf-8", errors="replace")
        cands = iter_receipts_from_text(text, p.name)
        return [build_receipt(c) for c in cands], 0

    if src == "dir":
        if not p.is_dir():
            return [], 0
        cands = iter_receipts_from_dir(
            p, recursive=args.recursive, include_assistant_text=include_at
        )
        receipts = [build_receipt(c) for c in cands]
        spawns = _count_spawns_jsonl(p, recursive=args.recursive, is_dir=True)
        return receipts, spawns

    # default: jsonl
    if not p.is_file():
        return [], 0
    cands = iter_receipts_from_jsonl(p, include_assistant_text=include_at)
    receipts = [build_receipt(c) for c in cands]
    spawns = _count_spawns_jsonl(p)
    return receipts, spawns


def main():
    _ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Portable Spawn Audit Block telemetry extractor")
    parser.add_argument("--from", dest="from", default="jsonl",
                        choices=["jsonl", "text", "stdin", "dir"],
                        help="input mode (default: jsonl)")
    parser.add_argument("--path", default="", help="file or directory")
    parser.add_argument("--context-dir", default="./context", help="context/ dir for writers")
    parser.add_argument("--summary", action="store_true", help="print JSON summary; NO writes")
    parser.add_argument("--include-assistant-text", action="store_true",
                        help="accept assistant-role text blocks (default OFF)")
    parser.add_argument("--include-no-block-fallback", action="store_true",
                        help="reserved escape hatch (default OFF; no-op)")
    parser.add_argument("--recursive", action="store_true", help="dir mode: recurse")
    args = parser.parse_args()

    try:
        receipts, spawns = _gather(args)

        if args.summary:
            print(json.dumps(summary(receipts, spawns), ensure_ascii=True, indent=2))
            sys.exit(0)

        written = write_receipts(receipts, args.context_dir)
        print(json.dumps(
            {"receipts_parsed": len(receipts), "written": written,
             "skipped_dedup": len(receipts) - written, "spawns": spawns},
            ensure_ascii=True,
        ))
    except Exception as e:  # fail-open (R8 / I3)
        print(f"telemetry-extract: fail-open ({e})", file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    main()
