"""Audit Block Validator — schema-checks Spawn Audit Blocks emitted by agents.

Usage:
    # Validate all blocks in a single jsonl transcript:
    python audit-block-validator.py path/to/transcript.jsonl

    # Validate all blocks across a directory of transcripts:
    python audit-block-validator.py /path/to/transcripts/ --recursive

    # Validate text from stdin:
    cat block.txt | python audit-block-validator.py -

Schema (v2 spawn protocol, per agent-spawn-protocol.md):
    📋 Spawn Audit Block[ (Joint Authoring)]

    [Authors]                                       (joint authoring only)
    - {emoji} {Display Name} ({slug})
    - {emoji} {Display Name} ({slug})
    [...]

    [Pre-Execution Loads]
    - SKILL.md: ✓ {path}                            (or ✗ {reason})
    - Preload packs (N): {list}                     (N = digit)
    - Task-matched skills (M): {list}               (M = digit)
    - Conditional packs (K): {list}                 (K = digit)
    - Mandatory invocations (J): {list}             (J = digit)
    - Fallbacks: {description}                      ("none" if clean)

    [Decision Records — ...]                        (OS agents on deliverable tasks only)
    - Read pre-analysis (constraints honored): ...
    - Sniffed during work: ...
    - Drafted this run: ...
    - Updated this run: ...
    - Conflicts flagged (DR vs new evidence): ...
    - Open assumptions tracked: ...
    (or single line: "skipped — non-deliverable task")

    [Post-Execution ROI]
    - Time saved: ~X hrs (baseline: ...)
    - Elapsed: Ys
    - Tokens: Zk (~$C cost)
    - Value: ~$V (...)

Detects:
    - Old-format blocks (📋 Pre-Execution Self-Check)
    - Mode: field (removed in v2)
    - Template-placeholder leaks ({path}, {N}, {description}, etc.)
    - Missing required sections
    - Malformed count lines (no digit, no payload)
    - lightweight_spawn references in emitted blocks
"""

from __future__ import annotations

import io
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Block extraction + header/section/count-line regexes are defined ONCE in the
# portable core (audit_parse.py); the validator imports them back (the "lift").
# audit_parse.py uses an underscore so it imports cleanly as a sibling module.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_parse import (  # noqa: E402
    extract_blocks,
    NEW_HEADER_RE,
    OLD_HEADER_RE,
    SECTION_RE,
    COUNT_LINE_RES,
)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

SKILL_LINE_RE = re.compile(r"-\s*(@\S+\s+)?SKILL\.md:\s*([✓✗])\s*(.+)")
FALLBACKS_LINE_RE = re.compile(r"-\s*Fallbacks(?:\s*taken)?:\s*(.+)")

PLACEHOLDER_PATTERNS = [
    r"\{path\}",
    r"\{N\}",
    r"\{M\}",
    r"\{K\}",
    r"\{J\}",
    r"\{list\}",
    r"\{description\}",
    r"\{reason\}",
    r"\{comma-separated.*?\}",
    r"\{Glob fallback for X.*?\}",
    r"\{pack \(trigger:.*?\}",
    r"\{skill \(trigger:.*?\}",
    r"\[path\]",
]
PLACEHOLDER_RE = re.compile("|".join(PLACEHOLDER_PATTERNS))

MODE_LINE_RE = re.compile(r"-\s*Mode:\s*\S+", re.IGNORECASE)
LIGHTWEIGHT_REF_RE = re.compile(r"lightweight[-_]?spawn", re.IGNORECASE)

REQUIRED_SECTIONS_SINGLE = ["Pre-Execution Loads", "Post-Execution ROI"]
REQUIRED_SECTIONS_JOINT = ["Authors", "Pre-Execution Loads", "Post-Execution ROI"]


@dataclass
class Deviation:
    severity: str  # "error" | "warn"
    code: str
    detail: str
    line: int = 0


@dataclass
class BlockReport:
    source: str
    block_index: int
    is_joint: bool
    is_old_format: bool
    sections_found: list[str] = field(default_factory=list)
    deviations: list[Deviation] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not any(d.severity == "error" for d in self.deviations)


def validate_block(block_text: str, source: str, block_index: int,
                   start_line: int, is_old_format: bool) -> BlockReport:
    report = BlockReport(source=source, block_index=block_index,
                         is_joint=False, is_old_format=is_old_format)

    if is_old_format:
        report.deviations.append(Deviation(
            severity="error", code="OLD_FORMAT",
            detail="Emits legacy 'Pre-Execution Self-Check' header — must use 'Spawn Audit Block' (v2)",
            line=start_line,
        ))
        return report

    # Joint authoring detection
    report.is_joint = bool(re.search(r"\(Joint Authoring\)", block_text, re.IGNORECASE))

    # Section detection
    for line_no, line in enumerate(block_text.split("\n"), start=start_line):
        m = SECTION_RE.match(line.strip())
        if m:
            report.sections_found.append(m.group(1).strip())

    # Required section check
    required = REQUIRED_SECTIONS_JOINT if report.is_joint else REQUIRED_SECTIONS_SINGLE
    section_names_norm = [s.split("—")[0].strip().lower() for s in report.sections_found]
    for req in required:
        if not any(req.lower() in s for s in section_names_norm):
            report.deviations.append(Deviation(
                severity="error", code="MISSING_SECTION",
                detail=f"Required section [{req}] not found",
                line=start_line,
            ))

    # Mode field check (must NOT exist in v2)
    for line_no, line in enumerate(block_text.split("\n"), start=start_line):
        if MODE_LINE_RE.match(line.strip()):
            report.deviations.append(Deviation(
                severity="error", code="MODE_FIELD_PRESENT",
                detail=f"'Mode:' line present (removed in v2): {line.strip()[:80]}",
                line=line_no,
            ))

    # lightweight_spawn references
    for line_no, line in enumerate(block_text.split("\n"), start=start_line):
        if LIGHTWEIGHT_REF_RE.search(line):
            report.deviations.append(Deviation(
                severity="error", code="LIGHTWEIGHT_REF",
                detail=f"References removed concept 'lightweight_spawn': {line.strip()[:80]}",
                line=line_no,
            ))

    # Placeholder leak check
    for line_no, line in enumerate(block_text.split("\n"), start=start_line):
        if PLACEHOLDER_RE.search(line):
            report.deviations.append(Deviation(
                severity="error", code="PLACEHOLDER_LEAK",
                detail=f"Template placeholder leaked into emitted block: {line.strip()[:100]}",
                line=line_no,
            ))

    # Count-line malformation check
    for line_no, line in enumerate(block_text.split("\n"), start=start_line):
        ls = line.strip()
        # Match the prefix of any count-bearing line to catch malformed ones
        for kind, regex in COUNT_LINE_RES.items():
            prefix_re = re.compile(rf"-\s*{kind.replace('_', '-').title()}", re.IGNORECASE)
            stripped_prefix = re.escape(kind.replace("_", " ").lower())
            if re.match(rf"-\s*{stripped_prefix}", ls, re.IGNORECASE):
                if not regex.match(ls):
                    report.deviations.append(Deviation(
                        severity="warn", code=f"MALFORMED_{kind.upper()}",
                        detail=f"Line matches {kind} prefix but doesn't fit schema: {ls[:100]}",
                        line=line_no,
                    ))

    # SKILL.md line check
    has_skill_line = any(SKILL_LINE_RE.match(line.strip())
                         for line in block_text.split("\n"))
    if not has_skill_line and "Pre-Execution Loads" in " ".join(report.sections_found):
        report.deviations.append(Deviation(
            severity="error", code="MISSING_SKILL_LINE",
            detail="Pre-Execution Loads section is missing SKILL.md: line",
            line=start_line,
        ))

    return report


def scan_jsonl(path: Path) -> list[BlockReport]:
    reports = []
    try:
        with path.open("r", encoding="utf-8", errors="replace") as f:
            block_counter = 0
            for raw_line_no, raw in enumerate(f, 1):
                raw = raw.strip()
                if not raw or "Audit Block" not in raw and "Self-Check" not in raw:
                    continue
                try:
                    obj = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                msg = obj.get("message") or {}
                content = msg.get("content")
                text = ""
                if isinstance(content, list):
                    for part in content:
                        if isinstance(part, dict) and part.get("type") == "text":
                            text += part.get("text", "") + "\n"
                elif isinstance(content, str):
                    text = content
                if not text:
                    continue
                for start_line, block, is_old in extract_blocks(text):
                    block_counter += 1
                    rpt = validate_block(block, str(path.name), block_counter,
                                         start_line, is_old)
                    reports.append(rpt)
    except Exception as e:
        print(f"  warn: {path.name}: {e}", file=sys.stderr)
    return reports


def scan_jsonl_role_aware(path: Path) -> list[BlockReport]:
    """Role-aware scan: candidate selection delegated to the structural join in
    telemetry-extract.iter_receipts_from_jsonl (the tool_use->tool_result join),
    then validate_block runs on the joined candidates only. Excludes decoys (audit
    blocks inside Read/Bash tool_results, prose narration) by construction.

    Import is lazy + guarded so the validator still runs if the extractor module
    is somehow absent (fail-open to the blind scan)."""
    reports = []
    try:
        import importlib.util
        ext_path = Path(__file__).resolve().parent / "telemetry-extract.py"
        spec = importlib.util.spec_from_file_location("telemetry_extract", ext_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for i, cand in enumerate(mod.iter_receipts_from_jsonl(path), 1):
            reports.append(validate_block(cand.text, str(path.name), i,
                                          cand.start_line, cand.is_old))
    except Exception as e:
        print(f"  warn: role-aware scan fell back to blind for {path.name}: {e}",
              file=sys.stderr)
        return scan_jsonl(path)
    return reports


def scan_text(text: str, source: str) -> list[BlockReport]:
    reports = []
    for i, (start_line, block, is_old) in enumerate(extract_blocks(text), 1):
        reports.append(validate_block(block, source, i, start_line, is_old))
    return reports


def main():
    args = sys.argv[1:]
    recursive = "--recursive" in args
    args = [a for a in args if a != "--recursive"]
    # --role-aware is DEFAULT ON; --no-role-aware reproduces the legacy blind scan.
    role_aware = "--no-role-aware" not in args
    args = [a for a in args if a not in ("--role-aware", "--no-role-aware")]
    _scan = scan_jsonl_role_aware if role_aware else scan_jsonl
    if not args:
        print(__doc__)
        sys.exit(2)

    target = args[0]
    all_reports: list[BlockReport] = []

    if target == "-":
        text = sys.stdin.read()
        all_reports = scan_text(text, "<stdin>")
    else:
        p = Path(target)
        if p.is_file():
            if p.suffix == ".jsonl":
                all_reports = _scan(p)
            else:
                all_reports = scan_text(p.read_text(encoding="utf-8", errors="replace"), p.name)
        elif p.is_dir():
            pattern = "**/*.jsonl" if recursive else "*.jsonl"
            for jsonl in sorted(p.glob(pattern)):
                all_reports.extend(_scan(jsonl))
        else:
            print(f"error: {target} not found", file=sys.stderr)
            sys.exit(1)

    total = len(all_reports)
    if total == 0:
        print("No Audit Blocks found.")
        return

    ok_count = sum(1 for r in all_reports if r.ok)
    fail_count = total - ok_count
    print(f"Audit Blocks: {total}  OK: {ok_count}  FAIL: {fail_count}")
    print(f"({100*ok_count/total:.1f}% pass rate)\n")

    if fail_count == 0:
        print("All Audit Blocks pass schema. ✓")
        return

    # Group by deviation code
    from collections import Counter
    code_counter = Counter()
    for r in all_reports:
        for d in r.deviations:
            code_counter[d.code] += 1
    print("Deviation breakdown:")
    for code, count in code_counter.most_common():
        print(f"  {count:4d}  {code}")

    print(f"\nFirst 10 failures (of {fail_count}):")
    shown = 0
    for r in all_reports:
        if r.ok:
            continue
        if shown >= 10:
            break
        shown += 1
        print(f"\n  Block #{r.block_index} in {r.source}")
        if r.is_joint:
            print(f"    (Joint Authoring)")
        for d in r.deviations:
            print(f"    [{d.severity.upper()} {d.code}] line {d.line}: {d.detail[:140]}")

    sys.exit(0 if fail_count == 0 else 1)


if __name__ == "__main__":
    main()
