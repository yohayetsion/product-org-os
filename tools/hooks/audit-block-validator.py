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
    - Empty/malformed [Post-Execution ROI] body — section header present but no
      parseable 'Time saved' or 'Value' line (and not marked non-applicable)
    - Missing [Context Injected] section (error MISSING_CONTEXT_INJECTED —
      always-present per protocol §2.5; DR-2026-178)
    - ID-shaped tokens in [Context Injected] that fail the context-ID grammar
      (error CONTEXT_INJECTED_ID_MALFORMED — grammar-only, no store dependency)
    - Grammar-valid [Context Injected] IDs no real context store resolves
      (warn CONTEXT_INJECTED_ID_UNRESOLVED, carrying the resolution method;
      requires --context-dir <path>; read-only against the stores)
"""

from __future__ import annotations

import io
import json
import os
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
    ROI_MINUTES_RE,
    ROI_VALUE_RE,
    OUTPUTS_MD_RE,
    OUTPUTS_PRES_RE,
    OUTPUTS_NON_APPLICABLE_TOKENS,
    ci_candidate_tokens,
    CI_STRICT_FULL_RE,
    CI_EMPTY_TOKENS,
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

# --- Ambient rule-stamp alarm (2026-08-02) ----------------------------------
# The agent reports, inside [Pre-Execution Loads], the first line of
# roi-display.md AS IT APPEARS IN ITS OWN CONTEXT. We compare that against the
# first line the file actually has ON DISK.
#
# THIS IS A ONE-SIDED ALARM AND MUST NEVER BE UPGRADED INTO A GREEN TICK.
# A MISMATCH is a loud failure naming both strings: it means the agent was
# reasoning over a stale snapshot of the rule text while the disk copy had
# already moved -- a defect that is structurally invisible from the disk side,
# because the disk is right. A MATCH IS RECORDED AND GRANTS NOTHING: it is not
# a pass, not a clearance, and proves nothing about any OTHER rule the agent
# received. Absence of the line is silence, not a pass either (warn).
AMBIENT_STAMP_RE = re.compile(
    r"^\s*-\s*Ambient rule stamp:.*?[\"“‘']"
    r"(?P<stamp>[^\"”’']+)[\"”’']"
)
RULES_DIR = None            # opt-in via --rules-dir; mirrors --check-files
_AMBIENT_DISK_STAMP = None  # first non-blank line of roi-display.md, read once

# [Post-Execution ROI] removed 2026-08-01 (O2 hours-only switch): ROI left the
# emit schema, so its absence is CONFORMANT. The roi_present-gated body check
# below stays — it validates the historical corpus and keeps the ROI_MINUTES_RE
# / ROI_VALUE_RE imports legitimate (see the invariant in audit_parse.py).
REQUIRED_SECTIONS_SINGLE = ["Pre-Execution Loads"]
REQUIRED_SECTIONS_JOINT = ["Authors", "Pre-Execution Loads"]


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
    # Ambient rule-stamp telemetry. `ambient_stamp` is what the block REPORTED
    # receiving (None = it reported nothing); `ambient_stamp_ok` is whether it
    # matched disk. RECORDED ONLY -- a True here confers nothing and is never
    # read as a pass. See AMBIENT_STAMP_RE above.
    ambient_stamp: str | None = None
    ambient_stamp_ok: bool | None = None

    @property
    def ok(self) -> bool:
        return not any(d.severity == "error" for d in self.deviations)


# ROI body whose presence exempts the block from the empty-ROI check. These are
# the blessed non-deliverable phrasings (roi-display.md: "non-deliverable; ROI
# not applicable").
ROI_NON_APPLICABLE_TOKENS = ("non-deliverable", "not applicable", "n/a")


# File-existence checking is OPT-IN (M2): the default validator is a pure
# text/schema checker (preserves the audit_parse portability boundary — it never
# reads the filesystem). Set via --check-files + --workspace-root.
CHECK_FILES = False
WORKSPACE_ROOT = None

# ---------------------------------------------------------------------------
# [Context Injected] context-store ID resolution (O5 — DR-2026-178).
# OPT-IN via --context-dir <path>, mirroring --check-files: the default
# validator stays a pure text/schema checker that never reads the filesystem.
# When set, grammar-valid [Context Injected] IDs resolve READ-ONLY against the
# real context stores (all six types reachable since O4): decisions, bets,
# assumptions, learnings, feedback, documents (+ feedback/themes.md for TH-).
# An ID no surface knows becomes a WARN carrying the resolution method — warns
# never flip BlockReport.ok. Grammar (malformed) checking needs no store and
# always runs.
# ---------------------------------------------------------------------------
CONTEXT_DIR = None
_CI_STORES = None  # lazy {family: {"ids": set, "method": str}}; loaded once

# family -> (subdir, index files scanned as rows, walk per-record filenames too)
_CI_STORE_SURFACES = {
    "DR": ("decisions", ("index.md",), True),
    "SB": ("bets", ("index.md",), False),
    "FB": ("feedback", ("index.md",), True),
    "A": ("assumptions", ("registry.md",), False),
    "L": ("learnings", ("index.md",), False),
    "DOC": ("documents", ("index.md", "registry.md"), False),
    "TH": ("feedback", ("index.md", "themes.md"), False),
}
_CI_FAMILY_RES = {
    fam: re.compile(r"\b" + fam + (r"-\d{4}-\d{3}\b" if fam in ("DR", "SB", "FB", "DOC")
                                   else r"-\d{3}\b"))
    for fam in _CI_STORE_SURFACES
}
# Per-record filenames carry slugs after the ID (DR-2026-177-assertions-....md);
# resolve by extracting the LEADING strict ID from the stem.
_CI_LEADING_ID_RE = re.compile(
    r"^((?:DR|SB|FB|DOC)-\d{4}-\d{3}|(?:A|L|TH)-\d{3})(?:$|[-.])")


def _ci_load_stores(context_dir):
    """READ-ONLY one-shot scan of the context stores. An unreadable or empty
    store disables resolution LOUDLY (stderr) rather than mass-warning against
    a comparand we do not actually have (DR-2026-177: findings ship where
    comparands can't — never gate against a plausible-looking empty answer)."""
    root = Path(context_dir)
    if not root.is_dir():
        print(f"  warn: --context-dir does not exist: {context_dir} — "
              f"[Context Injected] ID resolution disabled", file=sys.stderr)
        return {}
    stores = {}
    for fam, (sub, index_names, per_record) in _CI_STORE_SURFACES.items():
        ids: set = set()
        methods = []
        d = root / sub
        for iname in index_names:
            f = d / iname
            if f.is_file():
                try:
                    text = f.read_text(encoding="utf-8", errors="replace")
                except OSError as e:
                    print(f"  warn: unreadable store surface {f}: {e}", file=sys.stderr)
                    continue
                ids.update(_CI_FAMILY_RES[fam].findall(text))
                methods.append(f"{sub}/{iname} rows")
        if per_record and d.is_dir():
            def _loud(err, _sub=sub):
                print(f"  warn: store walk error under {_sub}/: {err}", file=sys.stderr)
            for _dirpath, _dirs, files in os.walk(d, onerror=_loud):
                for fn in files:
                    if not fn.endswith(".md"):
                        continue
                    m = _CI_LEADING_ID_RE.match(fn[:-3])
                    if m and m.group(1).startswith(fam + "-"):
                        ids.add(m.group(1))
            methods.append(f"{sub}/ per-record filenames")
        stores[fam] = {"ids": ids,
                       "method": " + ".join(methods) or f"{sub}/ (no readable surface)"}
    if not any(s["ids"] for s in stores.values()):
        print(f"  warn: context stores under {context_dir} yielded zero IDs — "
              f"[Context Injected] ID resolution disabled (empty comparand)",
              file=sys.stderr)
        return {}
    return stores


def _ci_resolve_ids(ids):
    """Return [(token, method)] for grammar-valid IDs no store surface resolves.
    Empty when resolution is disabled (no --context-dir / unusable store).
    recall:<slug> tokens are Layer-B recall memory, not context-store IDs."""
    global _CI_STORES
    if CONTEXT_DIR is None:
        return []
    if _CI_STORES is None:
        _CI_STORES = _ci_load_stores(CONTEXT_DIR)
    if not _CI_STORES:
        return []
    out = []
    for tok in ids:
        if tok.startswith("recall:"):
            continue
        entry = _CI_STORES.get(tok.split("-", 1)[0])
        if entry is not None and tok not in entry["ids"]:
            out.append((tok, entry["method"]))
    return out


def _section_body(block_text: str, name_prefix: str) -> str:
    """Return body lines under the first [Section] whose lowercased pre-em-dash
    name starts with name_prefix (until the next header / end). '' if absent.
    Header normalization mirrors audit_parse._section_map."""
    body: list[str] = []
    in_sec = False
    for line in block_text.split("\n"):
        m = SECTION_RE.match(line.strip())
        if m:
            name = m.group(1).split("—")[0].split("--")[0].strip().lower()
            in_sec = name.startswith(name_prefix)
            continue
        if in_sec:
            body.append(line)
    return "\n".join(body)


def _ambient_disk_stamp() -> str:
    """First non-blank line of roi-display.md AS IT IS ON DISK. Read once.

    Only ever called when RULES_DIR is set (--rules-dir), preserving the
    default validator's pure text/schema behaviour -- same opt-in idiom as
    --check-files and --context-dir.
    """
    global _AMBIENT_DISK_STAMP
    if _AMBIENT_DISK_STAMP is None:
        try:
            with open(Path(RULES_DIR) / "roi-display.md",
                      encoding="utf-8", errors="replace") as fh:
                _AMBIENT_DISK_STAMP = next(
                    (ln.strip() for ln in fh if ln.strip()), "")
        except OSError as exc:
            _AMBIENT_DISK_STAMP = f"<roi-display.md unreadable: {exc}>"
    return _AMBIENT_DISK_STAMP


def _check_ambient_stamp(block_text: str, report: "BlockReport", start_line: int) -> None:
    """Compare the block's self-reported ambient roi-display.md first line
    against the file on disk.

    ONE-SIDED ALARM -- IT CAN ONLY EVER RAISE. A mismatch is an error naming
    BOTH strings verbatim (so the reader never has to hunt for what moved). A
    MATCH IS RECORDED AND GRANTS NOTHING: it is not a pass, not a clearance,
    and must never be upgraded into a green tick by a later change to this
    function. There is deliberately no code path here that clears, downgrades,
    or satisfies any other check.
    """
    reported = None
    for line in block_text.split("\n"):
        m = AMBIENT_STAMP_RE.match(line)
        if m:
            reported = m.group("stamp").strip()
            break

    if reported is None:
        report.deviations.append(Deviation(
            severity="warn", code="AMBIENT_RULE_STAMP_ABSENT",
            detail="[Pre-Execution Loads] carries no '- Ambient rule stamp:' line, "
                   "so whether this agent received current or stale rule text is "
                   "unknown. Silence is not a pass.",
            line=start_line,
        ))
        return

    on_disk = _ambient_disk_stamp()
    report.ambient_stamp = reported
    report.ambient_stamp_ok = (reported == on_disk)
    if not report.ambient_stamp_ok:
        report.deviations.append(Deviation(
            severity="error", code="AMBIENT_RULE_STAMP_STALE",
            # Both strings lead: they are the actionable payload, and the
            # failure printer truncates the tail. Never reorder prose ahead
            # of them.
            detail=f"RECEIVED {reported!r} != ON DISK {on_disk!r} "
                   "— this agent reasoned over a stale snapshot of "
                   "roi-display.md; the disk copy is not evidence of what the "
                   "agent was actually given.",
            line=start_line,
        ))


def _roi_section_body(block_text: str) -> str:
    """Return the body lines under the [Post-Execution ROI] section (until the
    next [Section] header or end of block). Empty string when the header is
    absent. Header normalization (em-dash / double-dash split + lowercase)
    mirrors audit_parse._section_map so the two agree on section identity."""
    body: list[str] = []
    in_roi = False
    for line in block_text.split("\n"):
        m = SECTION_RE.match(line.strip())
        if m:
            name = m.group(1).split("—")[0].split("--")[0].strip().lower()
            in_roi = name.startswith("post-execution roi")
            continue
        if in_roi:
            body.append(line)
    return "\n".join(body)


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

    # Post-Execution ROI body check — symmetric to MISSING_SKILL_LINE above.
    # A fully-absent ROI section is already caught by MISSING_SECTION; THIS
    # catches the present-but-empty/garbage case (the content-strategist slip,
    # 2026-05-29) that the section-header check waves through. We reuse the
    # blessed ROI regexes imported from audit_parse so the validator and the
    # extractor never drift on what "parseable" means. Non-deliverable ROI
    # ("not applicable") is legitimately exempt.
    roi_present = any("post-execution roi" in s for s in section_names_norm)
    if roi_present:
        roi_body = _roi_section_body(block_text)
        roi_l = roi_body.lower()
        non_applicable = any(tok in roi_l for tok in ROI_NON_APPLICABLE_TOKENS)
        if not non_applicable:
            has_time = bool(ROI_MINUTES_RE.search(roi_body))
            has_value = bool(ROI_VALUE_RE.search(roi_body))
            if not has_time and not has_value:
                report.deviations.append(Deviation(
                    severity="error", code="EMPTY_ROI_SECTION",
                    detail=("[Post-Execution ROI] section present but contains no "
                            "parseable 'Time saved' or 'Value' line (and not marked "
                            "non-applicable)"),
                    line=start_line,
                ))
            else:
                # Partial: one core field missing → warn, not a hard fail.
                if not has_time:
                    report.deviations.append(Deviation(
                        severity="warn", code="MALFORMED_ROI_TIME",
                        detail="[Post-Execution ROI] missing a parseable 'Time saved' line",
                        line=start_line,
                    ))
                if not has_value:
                    report.deviations.append(Deviation(
                        severity="warn", code="MALFORMED_ROI_VALUE",
                        detail="[Post-Execution ROI] missing a parseable 'Value' line",
                        line=start_line,
                    ))

    # --- [Outputs] check (NEW — always-present on EVERY block; warn-first M13) ---
    outputs_present = any("outputs" == s for s in section_names_norm)
    if not outputs_present:
        report.deviations.append(Deviation(
            severity="warn", code="MISSING_OUTPUTS",
            detail="[Outputs] section absent (always-present per protocol §2.7; "
                   "use '- MD: <path>' or '- none — non-deliverable')",
            line=start_line,
        ))
    else:
        out_body = _section_body(block_text, "outputs")
        out_low = out_body.lower()
        # Match per-line (the `$` anchor is line-final; OUTPUTS_MD_RE has no MULTILINE).
        has_md = any(OUTPUTS_MD_RE.match(line.strip()) for line in out_body.split("\n"))
        non_applicable = any(tok in out_low for tok in OUTPUTS_NON_APPLICABLE_TOKENS)
        if not has_md and not non_applicable:
            report.deviations.append(Deviation(
                severity="warn", code="MISSING_OUTPUTS",
                detail="[Outputs] present but lists no '- MD:' path and no "
                       "non-deliverable token",
                line=start_line,
            ))
        # File-existence is OPT-IN and warn-only (M2 — never a hard error).
        if CHECK_FILES and WORKSPACE_ROOT and has_md and not non_applicable:
            for line in out_body.split("\n"):
                mm = OUTPUTS_MD_RE.match(line.strip())
                if not mm:
                    continue
                rel = mm.group(1).strip()
                low = rel.lower()
                if any(tok in low for tok in OUTPUTS_NON_APPLICABLE_TOKENS):
                    continue
                if low in ("orchestrator will generate", "pending"):
                    continue
                cand = Path(WORKSPACE_ROOT) / rel
                if not cand.exists() and not Path(rel).exists():
                    report.deviations.append(Deviation(
                        severity="warn", code="OUTPUTS_FILE_MISSING",
                        detail=f"[Outputs] MD path not found under workspace root: {rel[:100]}",
                        line=start_line,
                    ))

    # --- [Context Records] check (NEW — OS deliverable blocks only; warn-first) ---
    # OS-deliverable signal (M1): a [Decision Records] section present whose body
    # is NOT a 'skipped' line. Omitted blocks (non-OS / non-deliverable) are exempt.
    dr_present = any(s.startswith("decision records") for s in section_names_norm)
    if dr_present:
        dr_body = (_section_body(block_text, "decision records")).lower()
        # The skip reason often lives in the RAW header after the em-dash
        # ("[Decision Records — skipped, non-deliverable task]"), which the
        # normalized name drops — so check the un-normalized headers too.
        dr_header_raw = " ".join(s for s in report.sections_found
                                 if s.lower().startswith("decision records")).lower()
        is_os_deliverable = "skipped" not in dr_body and "skipped" not in dr_header_raw
        ctx_present = any(s.startswith("context records") for s in section_names_norm)
        if is_os_deliverable and not ctx_present:
            report.deviations.append(Deviation(
                severity="warn", code="MISSING_CONTEXT_RECORDS",
                detail="OS deliverable block has [Decision Records] but no "
                       "[Context Records] section (use '- none' if nothing created/updated)",
                line=start_line,
            ))

    # --- [Context Injected] checks (NEW — O5; DR-2026-176/178) ---
    # Exactly THREE codes ship (DR-2026-178, affirmed 2026-08-01):
    #   MISSING_CONTEXT_INJECTED       error — the always-present §2.5 section is absent
    #   CONTEXT_INJECTED_ID_MALFORMED  error — grammar-only, no store dependency;
    #                                  the only true fabrication signal
    #   CONTEXT_INJECTED_ID_UNRESOLVED warn  — grammar-valid ID no real store knows;
    #                                  carries its resolution method; warns never gate
    # The self-reported `Load-bearing` / `Coverage:` fields are parsed onto the
    # receipt and recorded as a distribution, NEVER gated — they are controlled
    # by the party being checked (DR-2026-178).
    ci_present = any(s.startswith("context injected") for s in section_names_norm)
    if not ci_present:
        report.deviations.append(Deviation(
            severity="error", code="MISSING_CONTEXT_INJECTED",
            detail="[Context Injected] section absent (always-present per protocol "
                   "§2.5; DR-2026-178 — declare the explicit empty token when "
                   "discovery found nothing or was skipped)",
            line=start_line,
        ))
    else:
        ci_body = _section_body(block_text, "context injected")
        ci_low = ci_body.lower()
        # Blessed empty declaration: MISSING cannot fire (section present) and
        # no ID codes fire.
        empty_declared = any(tok in ci_low for tok in CI_EMPTY_TOKENS)
        if not empty_declared:
            malformed: list[str] = []
            valid_ids: list[str] = []
            for line in ci_body.split("\n"):
                ls = line.strip()
                # The "Term-sets searched" line reports what was SEARCHED, not
                # what exists — ID-shaped search terms there are not claims.
                if ls.lower().lstrip("- ").startswith("term-sets"):
                    continue
                for tok in ci_candidate_tokens(ls):
                    if CI_STRICT_FULL_RE.fullmatch(tok):
                        if tok not in valid_ids:
                            valid_ids.append(tok)
                    elif tok not in malformed:
                        malformed.append(tok)
            if malformed:
                report.deviations.append(Deviation(
                    severity="error", code="CONTEXT_INJECTED_ID_MALFORMED",
                    detail="[Context Injected] carries ID-shaped tokens that fail "
                           "the context-ID grammar (fabrication signal, no store "
                           "needed): " + ", ".join(malformed[:10]),
                    line=start_line,
                ))
            for tok, method in _ci_resolve_ids(valid_ids):
                report.deviations.append(Deviation(
                    severity="warn", code="CONTEXT_INJECTED_ID_UNRESOLVED",
                    detail=f"[Context Injected] cites {tok} which no context store "
                           f"resolves (searched read-only: {method})",
                    line=start_line,
                ))

    # --- ambient rule-stamp alarm (opt-in, --rules-dir) ---
    if RULES_DIR:
        _check_ambient_stamp(block_text, report, start_line)

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
    global CHECK_FILES, WORKSPACE_ROOT, CONTEXT_DIR, RULES_DIR
    args = sys.argv[1:]
    recursive = "--recursive" in args
    args = [a for a in args if a != "--recursive"]
    # --role-aware is DEFAULT ON; --no-role-aware reproduces the legacy blind scan.
    role_aware = "--no-role-aware" not in args
    args = [a for a in args if a not in ("--role-aware", "--no-role-aware")]
    # --check-files (opt-in, M2) + --workspace-root <path>: enable warn-only MD
    # file-existence checks. Default stays a pure text/schema checker.
    if "--check-files" in args:
        CHECK_FILES = True
        args = [a for a in args if a != "--check-files"]
    if "--workspace-root" in args:
        i = args.index("--workspace-root")
        if i + 1 < len(args):
            WORKSPACE_ROOT = args[i + 1]
            del args[i:i + 2]
    # --context-dir <path> (opt-in, O5): enable READ-ONLY [Context Injected] ID
    # resolution against the real context stores (warn-only findings).
    if "--context-dir" in args:
        i = args.index("--context-dir")
        if i + 1 < len(args):
            CONTEXT_DIR = args[i + 1]
            del args[i:i + 2]
    # --rules-dir <path> (opt-in, 2026-08-02): enable the ambient rule-stamp
    # alarm -- compares each block's self-reported roi-display.md first line
    # against the file on disk. One-sided: it can only raise.
    if "--rules-dir" in args:
        i = args.index("--rules-dir")
        if i + 1 < len(args):
            RULES_DIR = args[i + 1]
            del args[i:i + 2]
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

    if RULES_DIR:
        reported = [r for r in all_reports if r.ambient_stamp is not None]
        matched = sum(1 for r in reported if r.ambient_stamp_ok)
        print(f"Ambient rule stamp (roi-display.md, on disk: "
              f"{_ambient_disk_stamp()!r}):")
        print(f"  {len(reported)}/{total} block(s) reported a stamp; "
              f"{matched} matched, {len(reported)-matched} STALE; "
              f"{total-len(reported)} reported none.")
        print("  Recorded only. A match grants nothing — this is a one-sided "
              "alarm, never a pass.\n")

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
            # 220, not 140 (2026-08-02): AMBIENT_RULE_STAMP_STALE's whole value
            # is naming BOTH the received and the on-disk rule heading, and two
            # headings do not fit in 140. Widening can only reveal more, never
            # hide a finding.
            print(f"    [{d.severity.upper()} {d.code}] line {d.line}: {d.detail[:220]}")

    sys.exit(0 if fail_count == 0 else 1)


if __name__ == "__main__":
    main()
