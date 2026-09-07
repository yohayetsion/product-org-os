#!/usr/bin/env python3
"""
Product Org OS — Context Tracker CLI

Standalone post-agent processing tool. Handles ROI logging, interaction logging,
document detection, session summaries, and pre-agent context injection.

Requirements: Python 3.8+ (stdlib only — no pip dependencies)
Design: Per-mode exit-code contract (O7, 2026-08-01) — FAIL-CLOSED by default:
        an error in any mode exits non-zero with the error on stderr,
        unconditionally (never gated on --verbose). Only the FAIL_OPEN_MODES
        allow-list (--hook, --pre-inject) exits 0 on error — those run inside
        the harness/orchestrator spawn path and must never block a spawn —
        and even they MUST report the error on stderr. A newly-added mode is
        fail-closed by default, with no registration required anywhere.
        Append-only writes, idempotent (dedup by tool_use_id).
        Context reader (O4, 2026-08-01): --pre-inject scans ALL SIX context
        types (decisions, bets, assumptions, learnings, feedback, documents);
        for every type it reads BOTH the index/registry file AND the
        per-record files (never skip an index), dedupes by record ID
        (per-record content wins on conflict), and scores/summarizes each
        record against ITS OWN ROW or OWN FILE only (no char-window splicing
        across neighbouring records). Per-type caps are filled round-robin
        across types. The context dir resolves via resolve_context_dir():
        explicit --context-dir -> workspace root derived from the script's
        own location -> cwd upward, failing loud through this contract when
        none resolves. The reader is READ-ONLY against the stores. Per-file
        read failures are reported on stderr and skipped (visible partial
        result, never a silent skip, never a spawn-path failure).

Usage:
  python os-tracker.py --hook                           # DEPRECATED warn+no-op (telemetry v4.3/D1)
  python os-tracker.py --agent pm --context-dir ./ctx   # Manual invocation
  python os-tracker.py --pre-inject "pricing" --context-dir ./ctx  # Context injection
  python os-tracker.py --rollup --context-dir ./ctx     # Session-end summary
  python os-tracker.py --diagnose --context-dir ./ctx   # Health check
  python os-tracker.py --diagnose --repair --context-dir ./ctx  # Rebuild indexes
"""

import argparse
import hashlib
import json
import os
import re
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VERSION = "1.2.0"
BASELINES_FILE = Path(__file__).parent / "baselines.json"

# Circuit breaker: after this many consecutive failures, disable for session
MAX_CONSECUTIVE_FAILURES = 3


class ContextReadError(Exception):
    """A context read failed in a way the caller must see (O7).

    Raised for expected-but-fatal context conditions (e.g. no context/
    directory) by this file's modes and by future context readers (O4).
    Reported to stderr as a one-line message (no traceback); the per-mode
    exit-code contract below decides fail-open vs fail-closed.
    """


# --- O7 per-mode exit-code contract (audit-mechanism-repair, 2026-08-01) ----
# Default is FAIL-CLOSED: an error in ANY mode propagates to a non-zero exit
# with the error on stderr, unconditionally (never gated on --verbose). The
# ONLY fail-open modes are this explicit allow-list — they run inside the
# harness/orchestrator spawn path and must never block a spawn. Allow-listed
# modes may still exit 0 on error but MUST report the error on stderr.
# A newly-added mode is fail-closed by default: it does NOT need to be (and
# must not be) registered anywhere to get the safe behaviour.
FAIL_OPEN_MODES = frozenset({"hook", "pre-inject"})

# Strict ID patterns (require year prefix to avoid false positives)
ID_PATTERNS = {
    "DR": re.compile(r"\bDR-\d{4}-\d{3}\b"),
    "SB": re.compile(r"\bSB-\d{4}-\d{3}\b"),
    "FB": re.compile(r"\bFB-\d{4}-\d{3}\b"),
    "DOC": re.compile(r"\bDOC-\d{4}-\d{3}\b"),
    "L": re.compile(r"\bL-\d{3}\b"),
    "A": re.compile(r"\bA-\d{3}\b"),
}

# File path patterns in markdown (backtick-wrapped paths ending in .md)
FILE_PATH_PATTERN = re.compile(r"`([^`]+\.md)`")

# Agent identity pattern in prompt
AGENT_IDENTITY_PATTERN = re.compile(
    r"You are \*\*(.+?) (.+?)\*\* (?:in|on)"
)

# Agent ID in description: [agent-id] rest of description
AGENT_ID_IN_DESC_PATTERN = re.compile(r"^\[([a-z][a-z0-9-]*)\]")

# Skip patterns — these indicate non-meaningful work
SKIP_KEYWORDS = [
    "context-recall", "context-save", "feedback-recall", "feedback-capture",
    "portfolio-status", "relevant-learnings", "handoff", "setup",
    "clear-demo", "reset-demo", "phase-check", "interaction-recall",
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def now_str() -> str:
    return now_utc().strftime("%Y-%m-%d %H:%M")


def today_str() -> str:
    return now_utc().strftime("%Y-%m-%d")


def year_str() -> str:
    return now_utc().strftime("%Y")


def generate_ix_id(agent: str, request: str) -> str:
    """Generate interaction ID from content hash (timestamp + agent + request[:50])."""
    seed = f"{now_str()}|{agent}|{request[:50]}"
    h = hashlib.sha256(seed.encode()).hexdigest()[:5]
    # Convert hex to 5-digit number
    num = int(h, 16) % 100000
    return f"IX-{year_str()}-{num:05d}"


def load_baselines() -> dict:
    """Load ROI baselines from JSON file."""
    try:
        with open(BASELINES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


_ALIAS_MERGES_CACHE = None


def load_alias_merges() -> dict:
    """Load the frozen canonical-slug map's `merges` (Wave A fix 9, 2026-08-02).

    The hours regime resolves an agent seat through the adjudicated alias map
    before looking it up in the activity table (DR-2026-181). This hook is
    PORTABLE plugin code, so the map is OPTIONAL: it lives in the operator's
    workspace (`<workspace>/audit-mechanism-repair/freeze/alias-map-*.json`),
    four levels up from this file. Absent map -> identity canon, which is the
    honest degradation (an unmapped slug simply prices on its literal key or
    stays unpriced) and never a fabricated number."""
    global _ALIAS_MERGES_CACHE
    if _ALIAS_MERGES_CACHE is not None:
        return _ALIAS_MERGES_CACHE
    _ALIAS_MERGES_CACHE = {}
    try:
        freeze = Path(__file__).resolve().parents[3] / "audit-mechanism-repair" / "freeze"
        maps = sorted(freeze.glob("alias-map-*.json"))
        if maps:
            with open(maps[-1], "r", encoding="utf-8") as f:
                _ALIAS_MERGES_CACHE = json.load(f).get("merges") or {}
    except Exception:
        _ALIAS_MERGES_CACHE = {}
    return _ALIAS_MERGES_CACHE


def canon_slug(slug: str) -> str:
    """strip/lower, then frozen-map lookup; identity otherwise (mirrors
    build-operator-dashboard.py::make_canon)."""
    s = (slug or "").strip().lower()
    return load_alias_merges().get(s, s)


def resolve_agent_id(tool_input: dict) -> str:
    """Resolve agent identity from tool input. Priority order:
    1. Structured [agent-id] in description field
    2. Parse identity block from prompt text
    3. Fall back to description text
    4. Default to 'unknown-agent'
    """
    # 1. Check description for [agent-id] pattern
    desc = tool_input.get("description", "")
    m = AGENT_ID_IN_DESC_PATTERN.match(desc)
    if m:
        return m.group(1)

    # 2. Parse prompt for identity block
    prompt = tool_input.get("prompt", "")
    m = AGENT_IDENTITY_PATTERN.search(prompt)
    if m:
        # Extract display name, convert to agent-key format
        display_name = m.group(2).strip()
        agent_key = display_name.lower().replace(" ", "-")
        return agent_key

    # 3. Fall back to description
    if desc:
        # Clean up description to make a reasonable ID
        clean = desc.lower().strip()
        clean = re.sub(r"[^a-z0-9\s-]", "", clean)
        clean = re.sub(r"\s+", "-", clean)
        return clean[:40] if clean else "unknown-agent"

    # 4. Default
    return "unknown-agent"


def resolve_skill_id(tool_input: dict) -> str:
    """Try to detect skill from prompt content."""
    prompt = tool_input.get("prompt", "")
    # Look for /skill-name patterns in the prompt
    m = re.search(r"/([a-z][a-z0-9-]+)", prompt)
    return m.group(1) if m else ""


def extract_request_summary(tool_input: dict) -> str:
    """Extract a short summary of the user's request from the prompt."""
    prompt = tool_input.get("prompt", "")
    # Look for a task section or use first meaningful line
    lines = prompt.strip().split("\n")
    for line in lines:
        line = line.strip()
        # Skip the identity block header lines
        if line.startswith("##") or line.startswith("You are **") or not line:
            continue
        if line.startswith("###"):
            continue
        # Skip short metadata lines
        if len(line) < 20:
            continue
        # Found a meaningful line — truncate
        return line[:200]
    return tool_input.get("description", "")[:200]


def is_meaningful_work(tool_input: dict, tool_response: str) -> bool:
    """Determine if this agent invocation represents meaningful work worth logging."""
    desc = tool_input.get("description", "").lower()
    prompt = tool_input.get("prompt", "").lower()

    # Check skip keywords
    for kw in SKIP_KEYWORDS:
        if kw in desc or kw in prompt[:500]:
            return False

    # Very short responses are probably not deliverables
    if tool_response and len(tool_response) < 100:
        return False

    return True


def detect_documents(text: str) -> list:
    """Detect file paths mentioned in the response text."""
    if not text:
        return []
    matches = FILE_PATH_PATTERN.findall(text)
    # Filter to likely real paths (contain / or \, not just a filename)
    docs = []
    for m in matches:
        if "/" in m or "\\" in m:
            docs.append(m)
    return docs


def detect_cross_refs(text: str) -> list:
    """Detect context IDs referenced in text."""
    if not text:
        return []
    refs = []
    for prefix, pattern in ID_PATTERNS.items():
        for match in pattern.findall(text):
            refs.append(match)
    return refs


# --- Structured Audit-Block extraction (M7/M29) ---------------------------------
# When a response carries the structured [Outputs] / [Context Records] sections,
# PREFER them over the blind backtick/ID scrape (which would re-count the same
# paths/ids and inflate the doc registry + cross-refs). Keyed on [Outputs] presence
# (M29) so an "[Outputs] none — non-deliverable" block still suppresses the scrape.
_AUDIT_SECTION_RE = re.compile(r"^\[([^\]]+)\]\s*$")
_OUTPUTS_PATH_RE = re.compile(r"-\s*(?:MD|Presentation):\s*(.+)$", re.IGNORECASE)
_NON_PATH_TOKENS = ("orchestrator will generate", "pending", "none", "non-deliverable",
                    "not applicable", "n/a")


def has_structured_outputs(text: str) -> bool:
    """True if the response contains an [Outputs] section header (the M29 key)."""
    if not text:
        return False
    return any(_AUDIT_SECTION_RE.match(line.strip()) and
               _AUDIT_SECTION_RE.match(line.strip()).group(1).strip().lower() == "outputs"
               for line in text.split("\n"))


def _audit_section_body(text: str, name_prefix: str) -> list:
    """Body lines under the first [Section] whose lowercased pre-em-dash name starts
    with name_prefix (until next header). [] if absent."""
    body, in_sec = [], False
    for line in text.split("\n"):
        m = _AUDIT_SECTION_RE.match(line.strip())
        if m:
            name = m.group(1).split("—")[0].split("--")[0].strip().lower()
            in_sec = name.startswith(name_prefix)
            continue
        if in_sec:
            body.append(line)
    return body


def detect_documents_structured(text: str) -> list:
    """Document paths from the [Outputs] section only (MD + real presentation paths)."""
    docs = []
    for line in _audit_section_body(text, "outputs"):
        m = _OUTPUTS_PATH_RE.match(line.strip())
        if not m:
            continue
        val = m.group(1).strip().strip("`")
        if any(tok in val.lower() for tok in _NON_PATH_TOKENS):
            continue
        if "/" in val or "\\" in val:
            docs.append(val)
    return docs


def detect_cross_refs_structured(text: str) -> list:
    """Context IDs from the [Context Records] + [Decision Records] sections only."""
    refs, seen = [], set()
    scoped = "\n".join(_audit_section_body(text, "context records")
                       + _audit_section_body(text, "decision records"))
    for prefix, pattern in ID_PATTERNS.items():
        for match in pattern.findall(scoped):
            if match not in seen:
                seen.add(match)
                refs.append(match)
    return refs


# ---------------------------------------------------------------------------
# ROI Calculation
# ---------------------------------------------------------------------------

def calculate_roi(agent_id: str, skill_id: str, response_text: str,
                  baselines: dict) -> dict:
    """Resolve this spawn's time basis under the HOURS-ONLY regime.

    Wave A fix 9 (round-2 product-operations §4, 2026-08-02). This arm never
    scraped the retired `[Post-Execution ROI]` self-report — it computed its OWN
    number, and that arm kept running after the 2026-08-01 switch: a live zombie
    writer appending legacy-format minutes (base x a complexity multiplier
    detected from RESPONSE LENGTH, with a `_default` 60-minute fallback) into
    `context/roi/session-log.md`. Both concepts are retired: the multiplier
    invents precision from prose length, and the `_default` fallback fabricates
    a time basis for a seat that has none. The published pipeline refuses both
    (build-operator-dashboard.py::load_hours_table).

    The regime now: canon(agent_slug) -> the `agents` activity table ->
    baseMinutes, unchanged and unmultiplied. NO skills/gateways priority chain
    (the activity table is a per-AGENT-SEAT instrument), NO `_default`, NO
    multiplier. A seat with no row is `unpriced` — reported as such, never
    estimated, exactly as a spawn with no table row is counted-not-priced on the
    dashboard. `minutesSaved` is None in that case, never 0 (0 would render as a
    measurement).

    `response_text` is now unused; the signature is kept so every call site and
    the hook contract are untouched."""
    del response_text  # retired input: complexity was detected from its length
    canon = canon_slug(agent_id)
    row = (baselines.get("agents") or {}).get(canon)
    base_minutes = row.get("baseMinutes") if isinstance(row, dict) else None

    # Same value-sanity gate as the published loaders (Wave A fix 1): a 0 or
    # negative or non-finite baseMinutes is not a time basis.
    if (canon == "_default" or isinstance(base_minutes, bool)
            or not isinstance(base_minutes, (int, float))
            or base_minutes != base_minutes            # NaN
            or base_minutes in (float("inf"), float("-inf"))
            or base_minutes <= 0):
        return {
            "minutesSaved": None,
            "basis": "unpriced",
            "canonSlug": canon,
            "manualEquivalent": None,
            "source": "no activity-table row",
        }

    return {
        "minutesSaved": int(base_minutes),
        "basis": "table",
        "canonSlug": canon,
        "manualEquivalent": row.get("manualEquivalent"),
        "source": f"agents:{canon}",
    }


# ---------------------------------------------------------------------------
# Writers (append-only, fail-open)
# ---------------------------------------------------------------------------

def append_roi_log(context_dir: Path, agent_id: str, skill_id: str,
                   roi: dict, ix_id: str) -> None:
    """Append a row to context/roi/session-log.md."""
    roi_file = context_dir / "roi" / "session-log.md"
    roi_file.parent.mkdir(parents=True, exist_ok=True)

    # Create header if file doesn't exist or is empty. Wave A fix 9: the
    # `Complexity` column is retired with the multiplier that produced it; the
    # column now carries the PRICING BASIS (`table` | `unpriced`). The live
    # file keeps its historical header — every row is self-describing either way.
    if not roi_file.exists() or roi_file.stat().st_size == 0:
        header = (
            "# Session ROI Log\n\n"
            "| Time | Type | Operation | Agent | Basis | Minutes (computed) | IX-ID |\n"
            "|------|------|-----------|-------|-------|--------------------|-------|\n"
        )
        with open(roi_file, "w", encoding="utf-8") as f:
            f.write(header)

    operation = skill_id if skill_id else "agent-work"
    op_type = "skill" if skill_id else "agent"
    basis = roi["basis"]
    # Never 0 for an unpriced seat — 0 reads as a measurement (the same
    # contract the dashboard renders as "no time basis yet").
    minutes = roi["minutesSaved"] if roi["minutesSaved"] is not None else "unpriced"

    row = f"| {now_str()} | {op_type} | {operation} | {agent_id} | {basis} | {minutes} | {ix_id} |\n"

    with open(roi_file, "a", encoding="utf-8") as f:
        f.write(row)


def append_interaction_log(context_dir: Path, agent_id: str, skill_id: str,
                           request_summary: str, response_summary: str,
                           ix_id: str, cross_refs: list) -> None:
    """Append an interaction entry to context/interactions/YYYY/YYYY-MM-DD.md."""
    year = year_str()
    date = today_str()
    int_dir = context_dir / "interactions" / year
    int_dir.mkdir(parents=True, exist_ok=True)

    int_file = int_dir / f"{date}.md"

    # Create header if file doesn't exist
    if not int_file.exists():
        header = f"# Interactions — {date}\n\n"
        with open(int_file, "w", encoding="utf-8") as f:
            f.write(header)

    related = ", ".join(cross_refs[:5]) if cross_refs else "—"
    op_type = "skill" if skill_id else "agent"
    skill_note = f" (`/{skill_id}`)" if skill_id else ""

    entry = (
        f"### {ix_id} | {agent_id}{skill_note} | {now_str()}\n\n"
        f"**Type**: {op_type}\n"
        f"**Agent**: {agent_id}\n"
        f"**Related**: {related}\n\n"
        f"#### User Request\n"
        f"> {request_summary[:300]}\n\n"
        f"#### Response\n"
        f"{response_summary[:500]}\n\n"
        f"---\n\n"
    )

    with open(int_file, "a", encoding="utf-8") as f:
        f.write(entry)


def update_session_summary(context_dir: Path, agent_id: str, skill_id: str,
                           request_summary: str, roi: dict, ix_id: str) -> None:
    """Update context/interactions/current-session.md with running list."""
    session_file = context_dir / "interactions" / "current-session.md"
    session_file.parent.mkdir(parents=True, exist_ok=True)

    # Read existing or create new
    entries = []
    if session_file.exists():
        content = session_file.read_text(encoding="utf-8")
        # Parse existing entries (lines starting with "- ")
        for line in content.split("\n"):
            if line.startswith("- "):
                entries.append(line)

    operation = f"/{skill_id}" if skill_id else agent_id
    minutes = roi["minutesSaved"]
    # Wave A fix 9: an unpriced seat contributes NO minutes to the running total
    # and says so. The priced phrasing is kept byte-identical so the existing
    # `~(\d+) min saved` reader below (and --diagnose) still totals correctly
    # across historical lines.
    tail = (f"~{minutes} min saved" if minutes is not None
            else "no time basis (unpriced)")
    new_entry = f"- `{ix_id}` | **{operation}** | {request_summary[:80]} | {tail}"
    entries.append(new_entry)

    # Write updated session file
    total_minutes = 0
    for e in entries:
        m = re.search(r"~(\d+) min saved", e)
        if m:
            total_minutes += int(m.group(1))

    content = (
        f"# Current Session\n\n"
        f"*Updated: {now_str()}*\n\n"
        f"**Session total: ~{total_minutes} min saved**\n\n"
    )
    content += "\n".join(entries) + "\n"

    with open(session_file, "w", encoding="utf-8") as f:
        f.write(content)


def append_document_registry(context_dir: Path, documents: list) -> None:
    """Append detected document paths to context/documents/registry.md."""
    if not documents:
        return

    # Accept either registry.md (canonical) or index.md (legacy)
    reg_file = context_dir / "documents" / "registry.md"
    if not reg_file.exists():
        reg_file = context_dir / "documents" / "index.md"
    if not reg_file.exists():
        return  # Don't create if the registry doesn't exist (the assistant creates
               # the context layer on install - see CLAUDE.md)

    existing = reg_file.read_text(encoding="utf-8")

    new_docs = []
    for doc_path in documents:
        if doc_path not in existing:
            new_docs.append(doc_path)

    if not new_docs:
        return

    with open(reg_file, "a", encoding="utf-8") as f:
        for doc in new_docs:
            f.write(f"\n| — | — | {Path(doc).stem} | `{doc}` | Active | — | — | {today_str()} |")


# ---------------------------------------------------------------------------
# Dedup
# ---------------------------------------------------------------------------

def check_dedup(context_dir: Path, tool_use_id: str) -> bool:
    """Check if this tool_use_id was already processed. Returns True if duplicate."""
    if not tool_use_id:
        return False

    dedup_file = context_dir / ".tracker-dedup"
    if dedup_file.exists():
        content = dedup_file.read_text(encoding="utf-8")
        if tool_use_id in content:
            return True

    return False


def mark_processed(context_dir: Path, tool_use_id: str) -> None:
    """Mark a tool_use_id as processed."""
    if not tool_use_id:
        return

    dedup_file = context_dir / ".tracker-dedup"
    dedup_file.parent.mkdir(parents=True, exist_ok=True)

    # Keep only last 200 IDs to prevent unbounded growth
    lines = []
    if dedup_file.exists():
        lines = dedup_file.read_text(encoding="utf-8").strip().split("\n")
        lines = lines[-199:]  # Keep last 199, we'll add 1

    lines.append(tool_use_id)

    with open(dedup_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ---------------------------------------------------------------------------
# Main Modes
# ---------------------------------------------------------------------------

def run_hook_mode(verbose: bool = False) -> None:
    """DEPRECATED (telemetry v4.3 / D1): warn + no-op shim.

    Under locked decision D1 (`cache/telemetry-portable-capture-plan-2026-05-30.md`)
    there is no Claude Code PostToolUse wiring — capture is a manual/on-demand run
    of the portable reader (`hooks/telemetry-extract.py`). The lossy re-derivation
    this hook performed (regex identity, length-based ROI, regex DRs) is replaced
    by parsing the agent's in-band Spawn Audit Block verbatim (D2).

    This shim drains stdin (so a piping PostToolUse caller doesn't get EPIPE),
    prints a one-line deprecation note to stderr, and exits 0 (fail-open). It does
    NOT process anything. `--pre-inject`, `--diagnose`, `--rollup` are unchanged.
    """
    try:
        # Drain stdin so an upstream pipe writer doesn't block / error.
        if not sys.stdin.isatty():
            sys.stdin.read()
    except Exception as e:
        # O7: even benign in-band failures are reported — never silent.
        print(f"os-tracker: --hook stdin drain failed: {e}", file=sys.stderr)
    print(
        "os-tracker --hook is DEPRECATED and no longer captures telemetry "
        "(telemetry v4.3 / decision D1: no PostToolUse hook). Run the portable "
        "reader instead: python hooks/telemetry-extract.py --from dir --path "
        "<transcripts> --context-dir <ctx>. This invocation did nothing.",
        file=sys.stderr,
    )
    return


def run_manual_mode(agent_id: str, skill_id: str, context_dir: Path,
                    verbose: bool = False) -> None:
    """Manual invocation with explicit agent/skill."""
    tool_input = {
        "description": f"[{agent_id}] manual invocation",
        "prompt": "",
    }
    run_tracking(tool_input, "", "", context_dir, verbose)


def run_tracking(tool_input: dict, tool_response: str, tool_use_id: str,
                 context_dir: Path, verbose: bool = False) -> None:
    """Core tracking pipeline."""
    # Dedup check
    if tool_use_id and check_dedup(context_dir, tool_use_id):
        if verbose:
            print(f"Skipping duplicate: {tool_use_id}", file=sys.stderr)
        return

    # Resolve identity
    agent_id = resolve_agent_id(tool_input)
    skill_id = resolve_skill_id(tool_input)

    # Check if meaningful work
    if not is_meaningful_work(tool_input, tool_response):
        if verbose:
            print(f"Skipping non-meaningful work: {agent_id}", file=sys.stderr)
        return

    # Extract data
    request_summary = extract_request_summary(tool_input)
    response_text = tool_response if isinstance(tool_response, str) else str(tool_response)
    response_summary = response_text[:500] if response_text else "Agent completed work."

    # Load baselines
    baselines = load_baselines()

    # Generate interaction ID
    ix_id = generate_ix_id(agent_id, request_summary)

    # Calculate ROI
    roi = calculate_roi(agent_id, skill_id, response_text, baselines)

    # Detect documents and cross-references. M7/M29: when the response carries a
    # structured [Outputs] section, PREFER the structured sections and SKIP the
    # blind backtick/ID scrape (which would re-count the same paths/ids and inflate
    # the registry). Keyed on [Outputs] presence so "[Outputs] none" also suppresses.
    if has_structured_outputs(response_text):
        documents = detect_documents_structured(response_text)
        cross_refs = detect_cross_refs_structured(response_text)
    else:
        documents = detect_documents(response_text)
        cross_refs = detect_cross_refs(response_text)

    # --- Pipeline (each step independently try/except'd) ---

    try:
        append_roi_log(context_dir, agent_id, skill_id, roi, ix_id)
        if verbose:
            print(f"ROI logged: {roi['minutesSaved']} min ({roi['basis']})",
                  file=sys.stderr)
    except Exception as e:
        # O7: step-failure reporting is unconditional (never gated on verbose).
        print(f"ROI log failed: {e}", file=sys.stderr)

    try:
        append_interaction_log(
            context_dir, agent_id, skill_id,
            request_summary, response_summary, ix_id, cross_refs
        )
        if verbose:
            print(f"Interaction logged: {ix_id}", file=sys.stderr)
    except Exception as e:
        print(f"Interaction log failed: {e}", file=sys.stderr)

    try:
        update_session_summary(
            context_dir, agent_id, skill_id,
            request_summary, roi, ix_id
        )
    except Exception as e:
        print(f"Session summary failed: {e}", file=sys.stderr)

    try:
        append_document_registry(context_dir, documents)
    except Exception as e:
        print(f"Document registry failed: {e}", file=sys.stderr)

    # Mark as processed (dedup)
    try:
        if tool_use_id:
            mark_processed(context_dir, tool_use_id)
    except Exception as e:
        print(f"Dedup mark failed: {e}", file=sys.stderr)

    if verbose:
        print(f"Tracking complete: {agent_id} | {ix_id} | "
              f"{roi['minutesSaved']}min ({roi['basis']})", file=sys.stderr)


# ---------------------------------------------------------------------------
# Pre-Inject: Context Recall Before Agent Spawning
# ---------------------------------------------------------------------------

# O4 reader (2026-08-01): ALL SIX context types are declared and scanned —
# documents and assumptions included (they were previously invisible). For
# every type the scan reads BOTH the index/registry file (row-form records,
# ID anchored at the row's FIRST cell) AND the per-record files (ID resolved
# from filename, then YAML frontmatter `id:`, then the first ID-bearing
# heading). Records dedupe by ID; per-record content wins on conflict.

_ID_CORES = {
    "DR": r"DR-\d{4}-\d{3}",
    "SB": r"SB-\d{4}-\d{3}",
    "FB": r"FB-\d{4}-\d{3}",
    "A": r"A-\d{3}",
    "L": r"L-\d{3}",
    "DOC": r"DOC-\d{4}-\d{3}",
}


def _type_patterns(core: str) -> dict:
    """Compile the anchored ID patterns for one record grammar."""
    return {
        # markdown TABLE ROW, ID anchored at the row's FIRST cell
        "row": re.compile(r"^\|\s*(" + core + r")\s*\|"),
        # per-record file heading (e.g. "# DR-2026-001: Title")
        "heading": re.compile(r"^#+\s*(" + core + r")\b"),
        # per-record YAML frontmatter (e.g. "id: FB-2026-018")
        "frontmatter": re.compile(r"^id:\s*(" + core + r")\s*$"),
        # per-record filename (e.g. "DR-2026-001-slug.md")
        "filename": re.compile(r"^(" + core + r")"),
    }


CONTEXT_TYPES = {
    "decisions": {
        "category": "Related Decisions",
        "index_files": ("index.md",),
        "patterns": _type_patterns(_ID_CORES["DR"]),
    },
    "bets": {
        "category": "Active Bets",
        "index_files": ("index.md",),
        "patterns": _type_patterns(_ID_CORES["SB"]),
    },
    "assumptions": {
        "category": "Relevant Assumptions",
        "index_files": ("registry.md", "index.md"),
        "patterns": _type_patterns(_ID_CORES["A"]),
    },
    "learnings": {
        "category": "Relevant Learnings",
        "index_files": ("index.md",),
        "patterns": _type_patterns(_ID_CORES["L"]),
    },
    "feedback": {
        "category": "Related Feedback",
        "index_files": ("index.md",),
        "patterns": _type_patterns(_ID_CORES["FB"]),
    },
    "documents": {
        "category": "Related Documents",
        "index_files": ("index.md", "registry.md"),
        "patterns": _type_patterns(_ID_CORES["DOC"]),
    },
}

# Index/aggregate filenames — scanned ONLY by the row-form index scan (they
# are records' rows, not record files); the per-record walk skips them.
_NON_RECORD_NAMES = {"index.md", "registry.md", "themes.md", "README.md"}

# O4: per-type cap + global round-robin budget. Replaces the flat total of 5
# (five items across six types is starvation). Every type surfaces its best
# item before any type gets a second.
PRE_INJECT_MAX_PER_TYPE = 3
PRE_INJECT_MAX_TOTAL = 12


def tokenize_topic(topic: str) -> list:
    """Split topic string into searchable keywords."""
    # Remove common stop words
    stop_words = {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
        "our", "my", "this", "that", "we", "should", "could", "would", "will",
    }
    words = re.findall(r"[a-zA-Z0-9][\w-]*", topic.lower())
    return [w for w in words if w not in stop_words and len(w) > 1]


def score_content(content: str, keywords: list) -> int:
    """Score text against keywords, COVERAGE-FIRST (O4): matching more
    DISTINCT keywords dominates matching one keyword many times. A record's
    own row/file contains every query term once; a long neighbour repeating a
    single term must not outrank it (linear occurrence counting was a
    measured recall failure: 4 of 748 own-row queries lost to term-repeat
    files). Within equal coverage, occurrence counts — damped at 5 per term,
    length-weighted (longer = more specific) — break ties. The damped
    tie-break maxes out well under the 1000-per-distinct-term coverage step."""
    content_lower = content.lower()
    matched = 0
    weight = 0
    for kw in keywords:
        count = content_lower.count(kw)
        if count:
            matched += 1
            weight += min(count, 5) * max(1, len(kw) - 2)
    if not matched:
        return 0
    return matched * 1000 + weight


def _iter_md_files(root: Path):
    """Yield .md files under root deterministically via os.walk with onerror
    RAISING — never a silent-on-error rglob; a walk failure must surface (O7)."""
    def _onerror(err):
        raise err
    for dirpath, dirnames, filenames in os.walk(root, onerror=_onerror):
        dirnames.sort()
        for fn in sorted(filenames):
            if fn.endswith(".md"):
                yield Path(dirpath) / fn


def _read_or_report_skip(path: Path) -> "str | None":
    """Read one store file. A real read failure is reported on stderr and the
    file is skipped — a VISIBLE partial result (O4), never a silent skip and
    never a spawn-path failure (--pre-inject stays fail-open per
    FAIL_OPEN_MODES). Anything that is not a read error propagates into the
    O7 per-mode contract."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as e:
        print(f"os-tracker: [pre-inject] skipped unreadable {path}: {e}",
              file=sys.stderr)
        return None


def _row_summary(row: str, rid: str) -> str:
    """Summary for an index/registry table row: its OWN cells only."""
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    cells = [c for c in cells if c and c != rid and c not in ("—", "-", "--")]
    return " | ".join(cells)[:220] or rid


def _record_summary(content: str, rid: str) -> str:
    """Summary for a per-record file: its OWN title/status lines only."""
    title = ""
    meta = []
    for line in content.split("\n")[:40]:
        stripped = line.strip()
        if not stripped or stripped == "---":
            continue
        if not title and stripped.startswith("#"):
            title = re.sub(
                r"^#+\s*(?:DR|SB|FB|L|A|DOC)-[\d-]+\s*[|:—–-]*\s*", "", stripped
            ).strip() or stripped.lstrip("#").strip()
            continue
        if not title and any(stripped.lower().startswith(k)
                             for k in ("topic:", "title:", "summary:")):
            title = stripped.split(":", 1)[1].strip()
            continue
        if any(k in stripped.lower() for k in ("status:", "date:", "owner:")):
            meta.append(stripped.strip("*").strip())
        if title and len(meta) >= 2:
            break
    out = title or rid
    if meta:
        out += " | " + " | ".join(meta[:2])
    return out[:220]


def scan_index_rows(index_file: Path, row_re, keywords: list) -> dict:
    """Scan ONE index/registry file for row-form records (ID anchored at the
    row's first cell). Each record is scored + summarized against ITS OWN ROW
    only. Returns {id: entry}."""
    content = _read_or_report_skip(index_file)
    if content is None:
        return {}
    found = {}
    for line in content.split("\n"):
        m = row_re.match(line)
        if not m:
            continue
        rid = m.group(1)
        score = score_content(line, keywords)
        prev = found.get(rid)
        if prev is None or score > prev["score"]:
            found[rid] = {
                "id": rid,
                "score": score,
                "summary": _row_summary(line, rid),
                "file": index_file.name,
            }
    return found


def _record_file_id(md_file: Path, content: str, patterns: dict) -> "str | None":
    """Resolve a per-record file's OWN record ID: filename first, then YAML
    frontmatter `id:`, then the first ID-bearing heading. None = not a record
    file of this type's grammar."""
    m = patterns["filename"].match(md_file.name)
    if m:
        return m.group(1)
    lines = content.split("\n")
    for line in lines[:30]:
        fm = patterns["frontmatter"].match(line.strip())
        if fm:
            return fm.group(1)
    for line in lines:
        hm = patterns["heading"].match(line)
        if hm:
            return hm.group(1)
    return None


def scan_record_files(source_dir: Path, patterns: dict, keywords: list) -> dict:
    """Scan a type's per-record files. Each record's scoring scope is ITS OWN
    FILE. Returns {id: entry}."""
    found = {}
    if not source_dir.is_dir():
        return found
    for md_file in _iter_md_files(source_dir):
        if md_file.name in _NON_RECORD_NAMES:
            continue
        content = _read_or_report_skip(md_file)
        if content is None:
            continue
        rid = _record_file_id(md_file, content, patterns)
        if rid is None:
            continue  # not a record file in this type's ID grammar
        score = score_content(content, keywords)
        prev = found.get(rid)
        if prev is None or score > prev["score"]:
            found[rid] = {
                "id": rid,
                "score": score,
                "summary": _record_summary(content, rid),
                "file": str(md_file.name),
            }
    return found


def scan_context_type(context_dir: Path, type_name: str, cfg: dict,
                      keywords: list) -> list:
    """Full scan of ONE context type: BOTH the index/registry file(s) AND the
    per-record files — never skip an index (index-only records must be
    reachable). Dedupe by ID: per-record content wins on conflict, keeping
    the MAX score across both surfaces (an index-row match must still surface
    a record whose file text differs from its row). Returns entries with
    score > 0, ranked, capped at PRE_INJECT_MAX_PER_TYPE."""
    source_dir = context_dir / type_name
    patterns = cfg["patterns"]

    index_entries = {}
    for idx_name in cfg["index_files"]:
        idx_file = source_dir / idx_name
        if not idx_file.is_file():
            continue
        for rid, entry in scan_index_rows(idx_file, patterns["row"],
                                          keywords).items():
            prev = index_entries.get(rid)
            if prev is None or entry["score"] > prev["score"]:
                index_entries[rid] = entry

    record_entries = scan_record_files(source_dir, patterns, keywords)

    merged = dict(index_entries)
    for rid, entry in record_entries.items():
        if rid in merged:
            entry = dict(entry)
            entry["score"] = max(entry["score"], merged[rid]["score"])
        merged[rid] = entry  # per-record content wins on conflict

    entries = [e for e in merged.values() if e["score"] > 0]
    entries.sort(key=lambda e: (-e["score"], e["id"]))
    return entries[:PRE_INJECT_MAX_PER_TYPE]


def scan_portfolio_bets(context_dir: Path, keywords: list) -> list:
    """Scan portfolio/active-bets.md for bet mentions, scored against each
    bet's OWN LINE only (row-scoped — no char-window splicing)."""
    bets_file = context_dir / "portfolio" / "active-bets.md"
    if not bets_file.is_file():
        return []
    content = _read_or_report_skip(bets_file)
    if content is None:
        return []

    entries = {}
    for line in content.split("\n"):
        for m in re.finditer(r"\b(SB-\d{4}-\d{3})\b", line):
            bet_id = m.group(1)
            score = score_content(line, keywords)
            if score <= 0:
                continue
            prev = entries.get(bet_id)
            if prev is None or score > prev["score"]:
                entries[bet_id] = {
                    "id": bet_id,
                    "score": score,
                    "summary": line.strip()[:200],
                    "file": "active-bets.md",
                }

    out = sorted(entries.values(), key=lambda e: (-e["score"], e["id"]))
    return out[:PRE_INJECT_MAX_PER_TYPE]


def load_conventions(context_dir: Path) -> str:
    """Load conventions file if it exists. Always included in pre-inject (no keyword filtering)."""
    conv_file = context_dir / "preferences" / "conventions.md"
    if not conv_file.exists():
        return ""
    try:
        content = conv_file.read_text(encoding="utf-8").strip()
        if not content or content == "# Organizational Conventions":
            return ""
        return content
    except Exception:
        return ""


def run_pre_inject_mode(topic: str, context_dir: Path,
                        verbose: bool = False) -> None:
    """Scan ALL SIX context types for items related to topic; output markdown
    to stdout (the shape the spawn protocol's `## Injected Context` assembly
    consumes). Per-type caps, filled ROUND-ROBIN across types so no type is
    starved by another's hits."""
    # Record summaries carry arbitrary Unicode (arrows, currency, Hebrew).
    # On a cp1252 console a raw print dies mid-injection; replace unencodable
    # characters instead — IDs and ASCII summaries stay intact.
    try:
        sys.stdout.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass  # non-reconfigurable stream (e.g. captured StringIO) — fine as-is
    keywords = tokenize_topic(topic)

    if not keywords:
        # O4/O7: an empty-token topic is visible, never a silent no-op.
        print("os-tracker: [pre-inject] topic yielded no searchable keywords "
              "— nothing to inject.", file=sys.stderr)
        return

    if verbose:
        print(f"Keywords: {keywords}", file=sys.stderr)

    # Scan every declared type (documents + assumptions included).
    per_type = {}  # type_name -> ranked entries (capped per type)
    for type_name, cfg in CONTEXT_TYPES.items():
        entries = scan_context_type(context_dir, type_name, cfg, keywords)
        if type_name == "bets":
            # Merge portfolio active-bets mentions into the bets type.
            existing_ids = {e["id"] for e in entries}
            for pe in scan_portfolio_bets(context_dir, keywords):
                if pe["id"] not in existing_ids:
                    entries.append(pe)
            entries.sort(key=lambda e: (-e["score"], e["id"]))
            entries = entries[:PRE_INJECT_MAX_PER_TYPE]
        if entries:
            per_type[type_name] = entries

    # Round-robin selection: rank 0 of every type, then rank 1, then rank 2,
    # within the global budget — every type surfaces its best item before any
    # type gets a second.
    selected = {t: [] for t in per_type}
    total_selected = 0
    for rank in range(PRE_INJECT_MAX_PER_TYPE):
        if total_selected >= PRE_INJECT_MAX_TOTAL:
            break
        for type_name in per_type:
            if total_selected >= PRE_INJECT_MAX_TOTAL:
                break
            entries = per_type[type_name]
            if rank < len(entries):
                selected[type_name].append(entries[rank])
                total_selected += 1

    # Always load conventions (no keyword filtering — global context)
    conventions = load_conventions(context_dir)

    if total_selected == 0 and not conventions:
        if verbose:
            print(f"No context found for: {topic}", file=sys.stderr)
        return  # Output nothing — no noise

    # Build markdown output
    output = []

    # Conventions go first (always-on organizational context)
    if conventions:
        # Strip the H1 header if present (we'll use our own H2)
        conv_body = re.sub(r"^#\s+Organizational Conventions\s*\n*", "", conventions).strip()
        if conv_body:
            output.append("## Organizational Conventions\n")
            output.append(conv_body)
            output.append("")

    if total_selected > 0:
        output.append(f"## Auto-Context: {total_selected} related items found\n")
        for type_name, cfg in CONTEXT_TYPES.items():
            picks = selected.get(type_name) or []
            if not picks:
                continue
            output.append(f"### {cfg['category']}")
            for entry in picks:
                output.append(f"- **{entry['id']}**: {entry['summary']}")
            output.append("")

    output.append("> Auto-injected by os-tracker. Use /context-recall for deeper queries.\n")

    print("\n".join(output))


def run_rollup_mode(context_dir: Path, verbose: bool = False) -> None:
    """Session-end rollup: summarize today's session."""
    session_file = context_dir / "interactions" / "current-session.md"
    if not session_file.exists():
        print("No session data to roll up.")
        return

    content = session_file.read_text(encoding="utf-8")
    print(content)

    # Also check ROI log for today's totals
    roi_file = context_dir / "roi" / "session-log.md"
    if roi_file.exists():
        today = today_str()
        total = 0
        count = 0
        for line in roi_file.read_text(encoding="utf-8").split("\n"):
            if today in line:
                m = re.search(r"\|\s*(\d+)\s*\|", line)
                if m:
                    total += int(m.group(1))
                    count += 1
        if count:
            print(f"\nToday's ROI: ~{total} min saved across {count} operations")


def run_diagnose_mode(context_dir: Path, repair: bool = False,
                      verbose: bool = False) -> None:
    """Health check and optional repair."""
    issues = []

    # Check context directory structure
    required_dirs = [
        "decisions", "bets", "assumptions", "portfolio", "learnings",
        "handoffs", "feedback", "documents", "roi", "roi/history",
        "interactions", "preferences",
    ]
    for d in required_dirs:
        path = context_dir / d
        if not path.exists():
            issues.append(f"missing directory: {d}")
            if repair:
                path.mkdir(parents=True, exist_ok=True)
                print(f"  repaired: created {d}/")

    # Check key files
    required_files = {
        "roi/session-log.md": "# Session ROI Log\n\n| Time | Type | Operation | Agent | Basis | Minutes (computed) | IX-ID |\n|------|------|-----------|-------|-------|--------------------|-------|\n",
        "interactions/current-session.md": "# Current Session\n\n*No active session*\n",
        # documents/registry.md OR documents/index.md (legacy name)
    }
    # Special check: documents registry can be either name
    doc_registry = context_dir / "documents" / "registry.md"
    doc_index = context_dir / "documents" / "index.md"
    if not doc_registry.exists() and not doc_index.exists():
        issues.append("missing file: documents/registry.md (or index.md)")

    for f, template in required_files.items():
        path = context_dir / f
        if not path.exists():
            issues.append(f"missing file: {f}")
            if repair and template:
                path.parent.mkdir(parents=True, exist_ok=True)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(template)
                print(f"  repaired: created {f}")

    # Check baselines
    if not BASELINES_FILE.exists():
        issues.append(f"missing baselines: {BASELINES_FILE}")
    else:
        try:
            baselines = load_baselines()
            if not baselines.get("skills"):
                issues.append("baselines.json has no skills entries")
        except Exception as e:
            issues.append(f"baselines.json parse error: {e}")

    # Rebuild JSON index from markdown sources (if repair)
    if repair:
        rebuild_index(context_dir, verbose)

    # Report
    if not issues:
        print("healthy")
    elif repair:
        # Issues were found but repair was attempted — check what remains
        remaining = []
        for issue in issues:
            # Re-check if the issue was actually fixed
            if issue.startswith("missing directory:"):
                d = issue.split(": ", 1)[1]
                if not (context_dir / d).exists():
                    remaining.append(issue)
            elif issue.startswith("missing file:"):
                f = issue.split(": ", 1)[1]
                if not (context_dir / f).exists():
                    remaining.append(issue)
            else:
                remaining.append(issue)
        if remaining:
            for issue in remaining:
                print(f"broken: {issue}")
        else:
            print("healthy (after repair)")
    else:
        for issue in issues:
            print(f"broken: {issue}")
        print("\nRun with --repair to fix these issues.")


def rebuild_directory_index(context_dir: Path, subdir: str, id_prefix: str,
                            id_pattern: re.Pattern, verbose: bool = False) -> int:
    """Rebuild a per-directory index.md from source entry files.
    Returns the number of entries found.
    Uses one entry per file (the primary ID), not every ID mention."""
    source_dir = context_dir / subdir
    if not source_dir.exists():
        return 0

    entries = []
    # Pattern to match entry files by name. Captures the numeric ID and tolerates
    # an optional `-slug` suffix: DR-2026-001.md AND DR-2026-010-pb-synthesis.md
    # both yield DR-2026-010. (Fix 2026-05-30: the old `-[\d-]+\.md$` dropped every
    # slug-suffixed file, which is why decisions/index.md was stale to DR-006.)
    file_id_pattern = re.compile(rf"^({id_prefix}-[\d]+(?:-[\d]+)*)(?:-[a-zA-Z].*)?\.md$")

    for md_file in sorted(source_dir.rglob("*.md")):
        if md_file.name in ("index.md", "registry.md", "themes.md", "README.md"):
            continue

        # Try to get the primary ID from the filename
        fm = file_id_pattern.match(md_file.name)
        if not fm:
            continue

        entry_id = fm.group(1)

        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        # Extract title, status, date from file content
        title = ""
        status = ""
        date = ""
        for line in content.split("\n")[:25]:
            stripped = line.strip()
            if not title and stripped.startswith("#"):
                # Clean heading to get title
                cleaned = re.sub(
                    rf"^#+\s*{re.escape(entry_id)}\s*[|:—–-]*\s*", "", stripped
                ).strip()
                if cleaned and cleaned != entry_id:
                    title = cleaned
            if not status and "status:" in stripped.lower():
                status = stripped.split(":", 1)[-1].strip().strip("*").strip()
            if not date and "date:" in stripped.lower():
                date = stripped.split(":", 1)[-1].strip().strip("*").strip()

        entries.append({
            "id": entry_id,
            "title": title or entry_id,
            "status": status,
            "date": date,
            "file": str(md_file.name),
        })

    if not entries:
        return 0

    # Write index.md
    index_file = source_dir / "index.md"
    header = f"# {subdir.title()} Index\n\n*Rebuilt: {now_str()}*\n\n"
    header += f"| ID | Title | Status | Date | File |\n"
    header += f"|-----|-------|--------|------|------|\n"

    rows = []
    for e in entries:
        rows.append(f"| {e['id']} | {e['title'][:60]} | {e['status']} | {e['date']} | {e['file']} |")

    with open(index_file, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(rows) + "\n")

    if verbose:
        print(f"  repaired: rebuilt {subdir}/index.md ({len(entries)} entries)", file=sys.stderr)

    return len(entries)


def rebuild_index(context_dir: Path, verbose: bool = False) -> None:
    """Rebuild all indexes: per-directory index.md files + interactions/index.json."""

    # --- Per-directory index.md rebuilds ---
    dir_configs = [
        ("decisions", "DR", re.compile(r"\b(DR-\d{4}-\d{3})\b")),
        ("bets", "SB", re.compile(r"\b(SB-\d{4}-\d{3})\b")),
        ("feedback", "FB", re.compile(r"\b(FB-\d{4}-\d{3})\b")),
        ("learnings", "L", re.compile(r"\b(L-\d{3})\b")),
    ]

    total_entries = 0
    for subdir, prefix, pattern in dir_configs:
        count = rebuild_directory_index(context_dir, subdir, prefix, pattern, verbose)
        total_entries += count

    print(f"  repaired: rebuilt per-directory indexes ({total_entries} total entries)")

    # --- Interactions index.json rebuild ---
    index_file = context_dir / "interactions" / "index.json"

    entries = []
    topic_index = {}
    agent_index = {}
    date_index = {}

    # Scan all interaction markdown files
    int_dir = context_dir / "interactions"
    for year_dir in sorted(int_dir.iterdir()) if int_dir.exists() else []:
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        for md_file in sorted(year_dir.glob("*.md")):
            try:
                content = md_file.read_text(encoding="utf-8")
                # Parse entries (### IX-YYYY-NNNNN | agent | date)
                for match in re.finditer(
                    r"### (IX-\d{4}-\d{5}) \| (.+?) \| (\d{4}-\d{2}-\d{2} \d{2}:\d{2})",
                    content,
                ):
                    ix_id = match.group(1)
                    agent = match.group(2).split(" (")[0].strip()
                    date = match.group(3)

                    entries.append({
                        "id": ix_id,
                        "agent": agent,
                        "date": date,
                        "file": str(md_file.relative_to(int_dir)),
                    })

                    # Build indexes
                    if agent not in agent_index:
                        agent_index[agent] = []
                    agent_index[agent].append(ix_id)

                    date_key = date[:10]
                    if date_key not in date_index:
                        date_index[date_key] = []
                    date_index[date_key].append(ix_id)
            except Exception as e:
                if verbose:
                    print(f"  skipped {md_file}: {e}", file=sys.stderr)

    index = {
        "version": "1.0",
        "lastUpdated": now_str(),
        "nextId": len(entries) + 1,
        "entries": entries,
        "topicIndex": topic_index,
        "agentIndex": agent_index,
        "dateIndex": date_index,
    }

    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"  repaired: rebuilt interactions/index.json ({len(entries)} entries)")


# ---------------------------------------------------------------------------
# Context directory resolution
# ---------------------------------------------------------------------------

def find_context_dir() -> Path | None:
    """Find the context/ directory by searching from cwd upward."""
    cwd = Path.cwd()

    # Check cwd/context/
    if (cwd / "context").is_dir():
        return cwd / "context"

    # Check parent directories (up to 5 levels)
    p = cwd
    for _ in range(5):
        p = p.parent
        if (p / "context").is_dir():
            return p / "context"
        if p == p.parent:
            break

    return None


def resolve_context_dir(explicit: str) -> Path:
    """O4 resolution chain — ships WITH the reader; no install layout is
    hard-coded:

      1. explicit --context-dir, if given. It must exist: a nonexistent
         explicit dir fails LOUD instead of yielding a plausible-looking
         empty answer.
      2. the workspace root's context/ derived from the SCRIPT'S OWN
         location: nearest ancestor ABOVE the plugin package that contains a
         context/ dir. The walk starts at the plugin root's parent (the
         script lives canonically at <plugin>/hooks/) because the plugin
         ships a scaffold context/ as a sibling of hooks/ — a fresh-install
         template whose indexes are empty; resolving to it would silently
         serve empty stores.
      3. cwd ./context, walking upward (find_context_dir) — this leg still
         reaches a scaffold-as-live-registry install when the caller works
         inside it.

    Raises ContextReadError when none resolves; the O7 per-mode contract
    decides fail-open vs fail-closed and reports on stderr."""
    if explicit:
        p = Path(explicit)
        if not p.is_dir():
            raise ContextReadError(f"--context-dir does not exist: {p}")
        return p

    here = Path(__file__).resolve()
    # here.parents[0] = hooks/, [1] = plugin root, [2] = plugin root's parent
    start = here.parents[2] if len(here.parents) > 2 else here.parents[-1]
    for anc in (start, *start.parents):
        cand = anc / "context"
        if cand.is_dir():
            return cand

    found = find_context_dir()
    if found is not None:
        return found

    raise ContextReadError(
        "no context/ directory found (checked --context-dir, the script's "
        "workspace ancestors, and cwd upward) — pass --context-dir or run "
        "the context layer has not been created yet."
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Product Org OS — Context Tracker CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("--hook", action="store_true",
                            help="DEPRECATED: warn+no-op shim (telemetry v4.3/D1; no PostToolUse). "
                                 "Use hooks/telemetry-extract.py instead.")
    mode_group.add_argument("--agent", type=str,
                            help="Manual mode: specify agent ID")
    mode_group.add_argument("--pre-inject", type=str, metavar="TOPIC",
                            help="Pre-agent context injection: returns related context for a topic")
    mode_group.add_argument("--rollup", action="store_true",
                            help="Session-end rollup summary")
    mode_group.add_argument("--diagnose", action="store_true",
                            help="Health check (add --repair to fix)")

    parser.add_argument("--skill", type=str, default="",
                        help="Skill ID (manual mode)")
    parser.add_argument("--context-dir", type=str, default="",
                        help="Path to context/ directory")
    parser.add_argument("--repair", action="store_true",
                        help="Repair issues found by --diagnose")
    parser.add_argument("--verbose", action="store_true",
                        help="Verbose output to stderr")
    parser.add_argument("--version", action="version",
                        version=f"os-tracker {VERSION}")

    args = parser.parse_args()

    # Store-derived text (record summaries, session logs) carries arbitrary
    # Unicode; on a cp1252 console a raw print dies mid-output. Replace
    # unencodable characters instead of failing — pre-existing latent bug
    # surfaced by the O7 loud contract (--rollup on real store content).
    try:
        sys.stdout.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass  # non-reconfigurable stream — fine as-is

    # O7: resolve the active mode flag generically over the mutually-exclusive
    # group, so any FUTURE mode added via mode_group.add_argument() is covered
    # by the exit-code contract WITHOUT being registered in any list.
    # (argparse keeps the group's actions on _group_actions; private but stable.)
    active_mode = "unknown"
    for action in mode_group._group_actions:
        val = getattr(args, action.dest, None)
        if val not in (None, False):
            active_mode = action.option_strings[0].lstrip("-")
            break

    try:
        if args.hook:
            run_hook_mode(verbose=args.verbose)
        elif args.agent or args.pre_inject or args.rollup or args.diagnose:
            # O4: every context-consuming mode resolves the context dir via
            # the resolution chain (explicit --context-dir → script-derived
            # workspace root → cwd upward). A failed resolution raises
            # ContextReadError into the O7 per-mode contract: loud on stderr,
            # exit 1 for fail-closed modes, exit 0 for the allow-listed
            # spawn-path modes (--pre-inject stays non-blocking but visible).
            try:
                context_dir = resolve_context_dir(args.context_dir)
            except ContextReadError:
                if args.diagnose:
                    # --diagnose keeps its stdout report line
                    print("broken: no context/ directory found — fix: create the context "
                          "layer per CLAUDE.md")
                raise
            if args.agent:
                run_manual_mode(args.agent, args.skill, context_dir,
                                verbose=args.verbose)
            elif args.pre_inject:
                run_pre_inject_mode(args.pre_inject, context_dir,
                                    verbose=args.verbose)
            elif args.rollup:
                run_rollup_mode(context_dir, verbose=args.verbose)
            else:
                run_diagnose_mode(context_dir, repair=args.repair,
                                  verbose=args.verbose)
        else:
            # A mode flag was parsed but matched no dispatch branch (empty
            # value, or a future flag whose branch was forgotten). O7: loud.
            raise ContextReadError(f"mode '--{active_mode}' matched no dispatch branch")
    except ContextReadError as e:
        # Expected fatal condition: one-line report (no traceback), then the
        # per-mode exit-code contract.
        print(f"os-tracker: [{active_mode}] {e}", file=sys.stderr)
        sys.exit(0 if active_mode in FAIL_OPEN_MODES else 1)
    except Exception:
        # O7 contract: nothing fails silently. Traceback on stderr
        # UNCONDITIONALLY (not gated on --verbose). Exit 0 only for the
        # allow-listed fail-open modes; non-zero for everything else —
        # including any newly-added mode not registered anywhere.
        traceback.print_exc(file=sys.stderr)
        fail_open = active_mode in FAIL_OPEN_MODES
        print(f"os-tracker: mode '--{active_mode}' failed "
              f"({'fail-open: exit 0' if fail_open else 'fail-closed: exit 1'})",
              file=sys.stderr)
        sys.exit(0 if fail_open else 1)


if __name__ == "__main__":
    main()
