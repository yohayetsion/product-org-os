"""audit_parse.py — Portable Spawn Audit Block extraction + parsing core (T2).

THE PORTABILITY BOUNDARY (design note I1 / §5). This module receives ONLY plain
text + a source tag and NEVER READS Claude-Code-jsonl-envelope structure — there
are no `.get("tool_use"...)` / `tool_result` / `message` / `usage` envelope reads
anywhere in this file, and it imports nothing from the consumer modules. All
harness-shape knowledge lives in `telemetry-extract.py`'s
`iter_receipts_from_jsonl`. `JOIN_KEY` below is an OUTPUT field name (provenance
surfaced on the Receipt), not envelope-reading; parse_block sets it to a
placeholder and `build_receipt` overlays the real value in the adapter.
The portability gate tests envelope-READS + import isolation (not string
presence) — see `hooks/tests/run_tests.py`.

Contents:
  - `extract_blocks(text)`         — LIFTED VERBATIM from audit-block-validator.py.
                                      Returns every Spawn Audit Block (new + v1-legacy).
  - `NEW_HEADER_RE / OLD_HEADER_RE / SECTION_RE` — LIFTED VERBATIM (the validator
                                      imports these back from here; defined ONCE).
  - the shared count-line + ROI regexes (the validator imports the count-line
                                      shapes so the two never drift).
  - `parse_block(block_text, source_tag, *, start_line=0, is_old_format=False)`
                                      — NEW. TOTAL function, NEVER raises. Returns
                                      the `Receipt` dict (design §3.1) with
                                      `parse_warnings[]` on any miss.

Stdlib only. Python 3.8+.
"""

from __future__ import annotations

import hashlib
import re

# ---------------------------------------------------------------------------
# Header / section regexes — LIFTED VERBATIM from audit-block-validator.py.
# Defined ONCE here; the validator does `from audit_parse import ...`.
# ---------------------------------------------------------------------------

NEW_HEADER_RE = re.compile(r"📋\s*Spawn Audit Block(\s*\(Joint Authoring\))?", re.IGNORECASE)
OLD_HEADER_RE = re.compile(r"📋\s*Pre-Execution Self-Check", re.IGNORECASE)
SECTION_RE = re.compile(r"^\[([^\]]+)\]\s*$")

# Count-bearing lines — must have (digit) before the colon.
# LIFTED from the validator so the two never drift on what a "count line" is.
# `parse_block` reads the values; the validator checks schema legality. Same shapes.
COUNT_LINE_RES = {
    "preload": re.compile(r"-\s*Preload packs\s*(?:\(combined,\s*)?\((\d+)\)\s*:\s*(.+)$"),
    "task_skills": re.compile(r"-\s*Task-matched skills\s*\((\d+)\)\s*:\s*(.+)$"),
    "conditional": re.compile(r"-\s*Conditional packs\s*(?:triggered\s*)?\((\d+)\)\s*:\s*(.+)$"),
    "mandatory": re.compile(r"-\s*Mandatory invocations\s*(?:fired\s*)?\((\d+)\)\s*:\s*(.+)$"),
}

SKILL_LINE_RE = re.compile(r"-\s*(?:@\S+\s+)?SKILL\.md:\s*([✓✗])\s*(.+)")
FALLBACKS_LINE_RE = re.compile(r"-\s*Fallbacks(?:\s*taken)?:\s*(.+)")

# ---------------------------------------------------------------------------
# Decision-record / author / ROI regexes (NEW — for parse_block reads)
# ---------------------------------------------------------------------------

# Author lines in joint-authoring blocks: "- {emoji} {Display Name} ({slug}) — leads ..."
AUTHOR_LINE_RE = re.compile(r"-\s*.+?\(([a-z][a-z0-9-]*)\)")

# In-block slug recovery from a SKILL.md path: ".claude/skills/{slug}/SKILL.md"
SLUG_FROM_SKILL_PATH_RE = re.compile(r"skills[/\\]([a-z][a-z0-9-]+)[/\\]SKILL\.md", re.IGNORECASE)

# Context IDs
DR_ID_RE = re.compile(r"\bDR-\d{4}-\d{3}\b")
A_ID_RE = re.compile(r"\bA-\d{3}\b")

# The Receipt's join-key OUTPUT field name (provenance surfaced on every receipt).
# This is an output field name, NOT envelope-reading: parse_block sets it to a
# placeholder; build_receipt overlays the real value from the adapter. Spelled
# plainly — the portability gate tests envelope-READS + import isolation, not the
# presence of this string (see hooks/tests/run_tests.py).
JOIN_KEY = "tool_use_id"

# Decision Records section field-line prefixes (case-insensitive contains)

DR_READ_PREFIX = "read pre-analysis"
DR_DRAFTED_PREFIX = "drafted this run"
DR_UPDATED_PREFIX = "updated this run"
DR_CONFLICTS_PREFIX = "conflicts flagged"
DR_ASSUMPTIONS_PREFIX = "open assumptions"

# Free-text ROI parse contract (design §3.1 — blessed regexes only).
#
# Two alternation branches (FX-1 / A2) cover ALL mandated ROI phrasings:
#   (1) COLON form — "Time saved: ~3 hrs" and the sensitive-skill variant with
#       intervening words before the colon: "Time saved on drafting and triage: ~4 hrs".
#       The `(?:\s+on[^:]*)?` allows the intervening clause but is bounded by `[^:]*`
#       so it can NEVER bleed across a colon into a different ROI line.
#   (2) NUMBER-FIRST form (roi-display.md sensitive-skill worked example, which has
#       NO "Time saved:" token) — "~4 hrs saved on drafting and triage",
#       "~4 hrs saved producing structured ...". Anchored on `saved` so a bare
#       "~90s elapsed" can't match.
# Units accept hr/min families. Number tolerates a thousands comma ("~1,200 mins");
# `_parse_roi` strips commas before int().
#
# NEGATIVE guard: neither branch matches `Elapsed: ~90s`, `Tokens: ...`, or
# `Value: ...` lines — branch (1) requires the literal "Time saved" prefix;
# branch (2) requires a number IMMEDIATELY followed by an hr/min unit AND the
# word "saved" (Elapsed is seconds with no "saved"; Tokens/Value have no hr/min unit).
_ROI_NUM = r"([\d][\d,]*(?:\.\d+)?)"
_ROI_UNIT = r"(hr|hrs|hour|hours|min|mins|minute|minutes)"
ROI_MINUTES_RE = re.compile(
    r"Time saved(?:\s+on[^:]*)?:\s*~?\s*" + _ROI_NUM + r"\s*" + _ROI_UNIT
    + r"|"
    + r"~?\s*" + _ROI_NUM + r"\s*" + _ROI_UNIT + r"\s+saved\b",
    re.IGNORECASE,
)
ROI_TOKENS_RE = re.compile(r"Tokens?:\s*~?\s*([\d.]+)\s*([km]?)", re.IGNORECASE)
ROI_VALUE_RE = re.compile(r"Value:\s*~?\s*\$\s*([\d,]+)", re.IGNORECASE)


# ---------------------------------------------------------------------------
# extract_blocks — LIFTED VERBATIM from audit-block-validator.py (lines 125-174).
# Behavior MUST be unchanged: the validator's existing fixtures still pass.
# ---------------------------------------------------------------------------

def extract_blocks(text: str) -> list:
    """Return list of (start_line, block_text, is_old_format)."""
    blocks = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        if NEW_HEADER_RE.search(lines[i]):
            start = i
            j = i + 1
            # Capture until 2 consecutive blank lines OR until next major header
            blank_count = 0
            while j < len(lines):
                line = lines[j]
                if not line.strip():
                    blank_count += 1
                    if blank_count >= 2:
                        break
                else:
                    blank_count = 0
                # Stop at typical "end of audit block" markers
                if line.startswith("**") and j > start + 3:
                    break
                if line.startswith("---") and j > start + 3:
                    break
                j += 1
            block = "\n".join(lines[start:j])
            blocks.append((start + 1, block, False))
            i = j
        elif OLD_HEADER_RE.search(lines[i]):
            start = i
            j = i + 1
            blank_count = 0
            while j < len(lines):
                if not lines[j].strip():
                    blank_count += 1
                    if blank_count >= 2:
                        break
                else:
                    blank_count = 0
                if lines[j].startswith("**") and j > start + 3:
                    break
                if lines[j].startswith("---") and j > start + 3:
                    break
                j += 1
            block = "\n".join(lines[start:j])
            blocks.append((start + 1, block, True))
            i = j
        else:
            i += 1
    return blocks


# ---------------------------------------------------------------------------
# Normalization + hashing (used for dedup fallback + provenance)
# ---------------------------------------------------------------------------

def normalize_block(block_text: str) -> str:
    """Collapse whitespace for a stable hash that ignores trivial reflow."""
    return re.sub(r"\s+", " ", block_text).strip()


def block_hash(block_text: str) -> str:
    return hashlib.sha256(normalize_block(block_text).encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Small parse helpers
# ---------------------------------------------------------------------------

def _split_items(payload: str) -> list:
    """Split a comma-separated item list from a count line into clean tokens."""
    payload = payload.strip()
    if not payload:
        return []
    low = payload.lower()
    # Common "nothing" phrasings → empty list
    if low in ("none", "0 declared on this agent", "n/a", "—", "-"):
        return []
    parts = [p.strip() for p in payload.split(",")]
    return [p for p in parts if p and p not in ("—", "-")]


def _parse_count_line(line: str, regex: re.Pattern) -> tuple:
    """Return (count:int|None, items:list). count=None when the line doesn't fit."""
    m = regex.match(line.strip())
    if not m:
        return None, []
    try:
        count = int(m.group(1))
    except (ValueError, IndexError):
        count = None
    items = _split_items(m.group(2)) if m.lastindex and m.lastindex >= 2 else []
    return count, items


def _collect_ids(text: str, pattern: re.Pattern) -> list:
    seen = []
    for m in pattern.findall(text):
        if m not in seen:
            seen.append(m)
    return seen


def _parse_roi(roi_text: str, warnings: list) -> dict:
    """Parse free-text ROI per the blessed regex table (design §3.1).

    NEVER re-derives from baselines. Unparseable → None + a parse_warnings entry.
    """
    roi = {
        "reported_raw": roi_text.strip(),
        "minutes": None,
        "tokens": None,
        "value_usd": None,
        "measured_tokens": None,  # filled by the harness adapter (R7), not here
        "drift": None,
    }

    m = ROI_MINUTES_RE.search(roi_text)
    if m:
        # Two alternation branches: colon form -> groups (1,2); number-first
        # form -> groups (3,4). Pick whichever side matched.
        num_raw = m.group(1) if m.group(1) is not None else m.group(3)
        unit_raw = m.group(2) if m.group(2) is not None else m.group(4)
        try:
            val = float((num_raw or "").replace(",", ""))  # strip thousands comma
            unit = (unit_raw or "").lower()
            if unit.startswith("hr") or unit.startswith("hour"):
                roi["minutes"] = int(round(val * 60))
            else:
                roi["minutes"] = int(round(val))
        except ValueError:
            warnings.append("roi.minutes: 'Time saved' value not numeric")
    else:
        warnings.append("roi.minutes: 'Time saved' line not parseable")

    m = ROI_TOKENS_RE.search(roi_text)
    if m:
        try:
            val = float(m.group(1))
            suffix = (m.group(2) or "").lower()
            if suffix == "k":
                val *= 1e3
            elif suffix == "m":
                val *= 1e6
            roi["tokens"] = int(round(val))
        except ValueError:
            warnings.append("roi.tokens: 'Tokens' value not numeric")
    else:
        warnings.append("roi.tokens: 'Tokens' line not parseable")

    m = ROI_VALUE_RE.search(roi_text)
    if m:
        try:
            roi["value_usd"] = int(m.group(1).replace(",", ""))
        except ValueError:
            warnings.append("roi.value_usd: 'Value' value not numeric")
    else:
        warnings.append("roi.value_usd: 'Value' line not parseable")

    return roi


def _section_map(block_text: str) -> dict:
    """Split a block into {section_header_lower: [lines]} keyed by [Section] markers.

    The header key is the lowercased text inside the brackets, truncated at the
    first em-dash (so "[Decision Records — deliverable task]" keys as
    "decision records").
    """
    sections = {}
    current = None
    for raw in block_text.split("\n"):
        m = SECTION_RE.match(raw.strip())
        if m:
            name = m.group(1).split("—")[0].split("--")[0].strip().lower()
            current = name
            sections[current] = []
        elif current is not None:
            sections[current].append(raw)
    return sections


# ---------------------------------------------------------------------------
# parse_block — NEW. TOTAL function, NEVER raises.
# ---------------------------------------------------------------------------

def parse_block(block_text, source_tag, *, start_line=0, is_old_format=False) -> dict:
    """Parse a Spawn Audit Block into a Receipt dict (design §3.1).

    Total function: any internal failure is captured as a `parse_warnings[]`
    entry; the function never raises. Reads verbatim — no baseline re-derivation
    (I2). Free-text ROI per the blessed regexes only.
    """
    warnings: list = []
    bhash = ""
    try:
        bhash = block_hash(block_text)
    except Exception:
        warnings.append("block_hash: hashing failed")

    receipt = {
        "ts": None,  # the harness adapter fills this from message.timestamp / run-time
        "source_file": source_tag,
        JOIN_KEY: None,  # overlaid by build_receipt from the join
        "block_hash": bhash,
        "agent_slug": "unknown-agent",
        "format": "v1-legacy" if is_old_format else "v2",
        "authors": [],
        "loads": {
            "skill_md": {"ok": False, "path": ""},
            "preload_packs": {"count": None, "items": []},
            "task_skills": {"count": None, "items": []},
            "conditional": {"count": None, "items": []},
            "mandatory": {"count": None, "items": []},
            "fallbacks": "none",
        },
        "decision_records": {},
        "roi": {
            "reported_raw": "",
            "minutes": None,
            "tokens": None,
            "value_usd": None,
            "measured_tokens": None,
            "drift": None,
        },
        "parse_warnings": warnings,
        "source": "text-mode",  # build_receipt / adapter overrides
    }

    # Legacy blocks: tag and stop. Their internal structure is the deleted v1
    # format; we capture the count, not the contents.
    if is_old_format:
        receipt["agent_slug"] = _slug_from_block(block_text) or "unknown-agent"
        warnings.append("format: v1-legacy 'Pre-Execution Self-Check' — captured for regression count")
        return receipt

    try:
        is_joint = bool(re.search(r"\(Joint Authoring\)", block_text, re.IGNORECASE))
        sections = _section_map(block_text)

        # --- Authors (joint) ---
        if is_joint:
            receipt["format"] = "joint"
            authors = []
            for raw in sections.get("authors", []):
                m = AUTHOR_LINE_RE.match(raw.strip())
                if m:
                    slug = m.group(1)
                    if slug not in authors:
                        authors.append(slug)
            receipt["authors"] = authors

        # --- Pre-Execution Loads ---
        loads_lines = sections.get("pre-execution loads", [])
        for raw in loads_lines:
            ls = raw.strip()
            sm = SKILL_LINE_RE.match(ls)
            if sm:
                receipt["loads"]["skill_md"] = {
                    "ok": sm.group(1) == "✓",
                    "path": sm.group(2).strip(),
                }
                continue
            c, items = _parse_count_line(ls, COUNT_LINE_RES["preload"])
            if c is not None or ls.lower().startswith("- preload"):
                receipt["loads"]["preload_packs"] = {"count": c, "items": items}
                continue
            c, items = _parse_count_line(ls, COUNT_LINE_RES["task_skills"])
            if c is not None or ls.lower().startswith("- task-matched"):
                receipt["loads"]["task_skills"] = {"count": c, "items": items}
                continue
            c, items = _parse_count_line(ls, COUNT_LINE_RES["conditional"])
            if c is not None or ls.lower().startswith("- conditional"):
                receipt["loads"]["conditional"] = {"count": c, "items": items}
                continue
            c, items = _parse_count_line(ls, COUNT_LINE_RES["mandatory"])
            if c is not None or ls.lower().startswith("- mandatory"):
                receipt["loads"]["mandatory"] = {"count": c, "items": items}
                continue
            fm = FALLBACKS_LINE_RE.match(ls)
            if fm:
                receipt["loads"]["fallbacks"] = fm.group(1).strip()

        # --- agent slug (join slug wins later in build_receipt) ---
        receipt["agent_slug"] = _slug_from_block(block_text) or "unknown-agent"
        if is_joint and receipt["authors"]:
            receipt["agent_slug"] = receipt["authors"][0]
        else:
            receipt["authors"] = [receipt["agent_slug"]]

        # --- Decision Records (OS deliverable blocks only) ---
        dr_key = None
        for k in sections:
            if k.startswith("decision records"):
                dr_key = k
                break
        if dr_key is not None:
            dr = {
                "present": True,
                "skipped_reason": None,
                "read_pre_analysis": [],
                "drafted": [],
                "updated": [],
                "conflicts": [],
                "assumptions": [],
            }
            # "skipped — non-deliverable task" can live in the header or a body line
            header_and_body = dr_key + " " + " ".join(sections[dr_key]).lower()
            if "skipped" in header_and_body:
                dr["present"] = False
                dr["skipped_reason"] = "skipped — non-deliverable task"
            for raw in sections[dr_key]:
                low = raw.lower()
                if DR_READ_PREFIX in low:
                    dr["read_pre_analysis"] = _collect_ids(raw, DR_ID_RE)
                elif DR_DRAFTED_PREFIX in low:
                    dr["drafted"] = _collect_ids(raw, DR_ID_RE)
                elif DR_UPDATED_PREFIX in low:
                    dr["updated"] = _collect_ids(raw, DR_ID_RE)
                elif DR_CONFLICTS_PREFIX in low:
                    dr["conflicts"] = _collect_ids(raw, DR_ID_RE)
                elif DR_ASSUMPTIONS_PREFIX in low:
                    dr["assumptions"] = _collect_ids(raw, A_ID_RE)
            receipt["decision_records"] = dr

        # --- Post-Execution ROI ---
        roi_key = None
        for k in sections:
            if k.startswith("post-execution roi"):
                roi_key = k
                break
        if roi_key is not None:
            roi_text = "\n".join(sections[roi_key])
            parsed = _parse_roi(roi_text, warnings)
            # preserve measured/drift placeholders (filled by adapter)
            parsed["measured_tokens"] = receipt["roi"]["measured_tokens"]
            parsed["drift"] = receipt["roi"]["drift"]
            receipt["roi"] = parsed
        else:
            warnings.append("roi: [Post-Execution ROI] section absent")

    except Exception as e:  # pragma: no cover - defensive; parse_block must never raise
        warnings.append("parse_block: unexpected error: %s" % e)

    return receipt


def _slug_from_block(block_text: str):
    """Best-effort in-block slug: from the SKILL.md path, else None."""
    m = SLUG_FROM_SKILL_PATH_RE.search(block_text)
    if m:
        return m.group(1).lower()
    return None
