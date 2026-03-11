#!/usr/bin/env python3
"""
Product Org OS — Context Tracker CLI

Standalone post-agent processing tool. Handles ROI logging, interaction logging,
document detection, session summaries, and pre-agent context injection.

Requirements: Python 3.8+ (stdlib only — no pip dependencies)
Design: Fail-open (never blocks the coding agent), append-only writes,
        idempotent (dedup by tool_use_id).

Usage:
  python os-tracker.py --hook                           # Claude Code PostToolUse (stdin JSON)
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
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VERSION = "1.2.0"
BASELINES_FILE = Path(__file__).parent / "baselines.json"

# Circuit breaker: after this many consecutive failures, disable for session
MAX_CONSECUTIVE_FAILURES = 3

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


def detect_complexity(text: str, baselines: dict) -> tuple:
    """Detect complexity from response length. Returns (label, multiplier)."""
    thresholds = baselines.get("complexityThresholds", {})
    multipliers = baselines.get("complexityMultipliers", {})

    length = len(text) if text else 0

    simple_t = thresholds.get("simple", 1000)
    standard_t = thresholds.get("standard", 3000)
    complex_t = thresholds.get("complex", 8000)

    if length < simple_t:
        return "simple", multipliers.get("simple", 0.5)
    elif length < standard_t:
        return "standard", multipliers.get("standard", 1.0)
    elif length < complex_t:
        return "complex", multipliers.get("complex", 1.5)
    else:
        return "enterprise", multipliers.get("enterprise", 2.0)


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


# ---------------------------------------------------------------------------
# ROI Calculation
# ---------------------------------------------------------------------------

def calculate_roi(agent_id: str, skill_id: str, response_text: str,
                  baselines: dict) -> dict:
    """Calculate ROI (minutes saved) from baselines."""
    complexity_label, multiplier = detect_complexity(response_text, baselines)

    base_minutes = 0
    manual_equiv = "general product work"
    source = "default"

    # Priority: skill > agent > default
    skills = baselines.get("skills", {})
    agents = baselines.get("agents", {})
    gateways = baselines.get("gateways", {})

    if skill_id and skill_id in skills:
        entry = skills[skill_id]
        base_minutes = entry.get("baseMinutes", 0)
        manual_equiv = entry.get("manualEquivalent", manual_equiv)
        source = f"skill:{skill_id}"
    elif agent_id in gateways:
        entry = gateways[agent_id]
        base_minutes = entry.get("baseMinutes", 0)
        manual_equiv = entry.get("manualEquivalent", manual_equiv)
        source = f"gateway:{agent_id}"
    elif agent_id in agents:
        entry = agents[agent_id]
        base_minutes = entry.get("baseMinutes", 0)
        manual_equiv = entry.get("manualEquivalent", manual_equiv)
        source = f"agent:{agent_id}"
    else:
        # Use defaults
        if skill_id:
            default = skills.get("_default", {})
        elif "leadership" in agent_id or "gateway" in agent_id:
            default = gateways.get("_default", {})
        else:
            default = agents.get("_default", {})
        base_minutes = default.get("baseMinutes", 60)
        manual_equiv = default.get("manualEquivalent", manual_equiv)
        source = "default"

    minutes_saved = int(base_minutes * multiplier)

    return {
        "minutesSaved": minutes_saved,
        "complexity": complexity_label,
        "multiplier": multiplier,
        "baseMinutes": base_minutes,
        "manualEquivalent": manual_equiv,
        "source": source,
    }


# ---------------------------------------------------------------------------
# Writers (append-only, fail-open)
# ---------------------------------------------------------------------------

def append_roi_log(context_dir: Path, agent_id: str, skill_id: str,
                   roi: dict, ix_id: str) -> None:
    """Append a row to context/roi/session-log.md."""
    roi_file = context_dir / "roi" / "session-log.md"
    roi_file.parent.mkdir(parents=True, exist_ok=True)

    # Create header if file doesn't exist or is empty
    if not roi_file.exists() or roi_file.stat().st_size == 0:
        header = (
            "# Session ROI Log\n\n"
            "| Time | Type | Operation | Agent | Complexity | Minutes Saved | IX-ID |\n"
            "|------|------|-----------|-------|------------|---------------|-------|\n"
        )
        with open(roi_file, "w", encoding="utf-8") as f:
            f.write(header)

    operation = skill_id if skill_id else "agent-work"
    op_type = "skill" if skill_id else "agent"
    minutes = roi["minutesSaved"]
    complexity = roi["complexity"]

    row = f"| {now_str()} | {op_type} | {operation} | {agent_id} | {complexity} | {minutes} | {ix_id} |\n"

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
    new_entry = f"- `{ix_id}` | **{operation}** | {request_summary[:80]} | ~{minutes} min saved"
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
        return  # Don't create if registry doesn't exist (run /setup first)

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
    """Process Claude Code PostToolUse stdin JSON."""
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return

        data = json.loads(raw)
    except (json.JSONDecodeError, Exception):
        return  # fail-open

    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})
    tool_response = data.get("tool_response", "")
    tool_use_id = data.get("tool_use_id", "")

    # Only process Agent tool calls
    if tool_name != "Agent":
        return

    # Find context dir — search upward from cwd
    context_dir = find_context_dir()
    if not context_dir:
        if verbose:
            print("No context/ dir found", file=sys.stderr)
        return

    run_tracking(tool_input, tool_response, tool_use_id, context_dir, verbose)


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

    # Detect documents and cross-references
    documents = detect_documents(response_text)
    cross_refs = detect_cross_refs(response_text)

    # --- Pipeline (each step independently try/except'd) ---

    try:
        append_roi_log(context_dir, agent_id, skill_id, roi, ix_id)
        if verbose:
            print(f"ROI logged: {roi['minutesSaved']} min", file=sys.stderr)
    except Exception as e:
        if verbose:
            print(f"ROI log failed: {e}", file=sys.stderr)

    try:
        append_interaction_log(
            context_dir, agent_id, skill_id,
            request_summary, response_summary, ix_id, cross_refs
        )
        if verbose:
            print(f"Interaction logged: {ix_id}", file=sys.stderr)
    except Exception as e:
        if verbose:
            print(f"Interaction log failed: {e}", file=sys.stderr)

    try:
        update_session_summary(
            context_dir, agent_id, skill_id,
            request_summary, roi, ix_id
        )
    except Exception as e:
        if verbose:
            print(f"Session summary failed: {e}", file=sys.stderr)

    try:
        append_document_registry(context_dir, documents)
    except Exception as e:
        if verbose:
            print(f"Document registry failed: {e}", file=sys.stderr)

    # Mark as processed (dedup)
    try:
        if tool_use_id:
            mark_processed(context_dir, tool_use_id)
    except Exception:
        pass

    if verbose:
        print(f"Tracking complete: {agent_id} | {ix_id} | {roi['minutesSaved']}min", file=sys.stderr)


# ---------------------------------------------------------------------------
# Pre-Inject: Context Recall Before Agent Spawning
# ---------------------------------------------------------------------------

# Directories to scan for context items, with their display category
CONTEXT_SOURCES = {
    "decisions": {
        "glob": "**/*.md",
        "category": "Related Decisions",
        "id_pattern": re.compile(r"^#+\s*(DR-\d{4}-\d{3})\b"),
    },
    "bets": {
        "glob": "**/*.md",
        "category": "Active Bets",
        "id_pattern": re.compile(r"^#+\s*(SB-\d{4}-\d{3})\b"),
    },
    "feedback": {
        "glob": "**/*.md",
        "category": "Related Feedback",
        "id_pattern": re.compile(r"^#+\s*(FB-\d{4}-\d{3})\b"),
    },
    "learnings": {
        "glob": "*.md",
        "category": "Relevant Learnings",
        "id_pattern": re.compile(r"^#+\s*(L-\d{3})\b"),
    },
}

# Max items per category in pre-inject output
PRE_INJECT_MAX_PER_CATEGORY = 3
PRE_INJECT_MAX_TOTAL = 5


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
    """Score a piece of content by keyword match density."""
    content_lower = content.lower()
    score = 0
    for kw in keywords:
        # Count occurrences, weight by keyword length (longer = more specific)
        count = content_lower.count(kw)
        score += count * max(1, len(kw) - 2)
    return score


def extract_entry_summary(content: str, entry_start: int, id_str: str) -> str:
    """Extract a brief summary around where the entry ID was found."""
    lines = content[entry_start:].split("\n")
    summary_parts = []
    title = ""

    for i, line in enumerate(lines[:15]):  # Look at first 15 lines of entry
        stripped = line.strip()
        if not stripped:
            continue

        # First heading line after ID is the title
        if not title and (stripped.startswith("#") or i == 0):
            # Clean the title
            title = re.sub(r"^#+\s*(?:DR|SB|FB|L)-[\d-]+\s*[|:—–-]*\s*", "", stripped).strip()
            if not title:
                title = stripped.lstrip("#").strip()
            continue

        # Look for status, date, owner, topics lines
        if any(k in stripped.lower() for k in ["status:", "date:", "owner:", "topic", "sentiment"]):
            summary_parts.append(stripped)

        if len(summary_parts) >= 3:
            break

    result = title if title else id_str
    if summary_parts:
        result += "\n  " + " | ".join(summary_parts[:3])
    return result


def scan_context_source(source_dir: Path, keywords: list,
                        source_config: dict) -> list:
    """Scan a context source directory for keyword matches. Returns scored entries."""
    if not source_dir.exists():
        return []

    entries = []
    id_pattern = source_config["id_pattern"]

    for md_file in source_dir.rglob("*.md"):
        # Skip index files — they contain all IDs and would match everything
        if md_file.name in ("index.md", "registry.md", "themes.md", "README.md"):
            continue

        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        # Score the whole file first
        file_score = score_content(content, keywords)
        if file_score == 0:
            continue

        # Find individual entries within the file
        for match in id_pattern.finditer(content):
            entry_id = match.group(1)
            entry_start = match.start()

            # Score the entry's local context (500 chars around it)
            local_text = content[max(0, entry_start - 200):entry_start + 1500]
            local_score = score_content(local_text, keywords)

            if local_score > 0:
                summary = extract_entry_summary(content, entry_start, entry_id)
                entries.append({
                    "id": entry_id,
                    "score": local_score,
                    "summary": summary,
                    "file": str(md_file.name),
                })

    # Sort by score descending
    entries.sort(key=lambda e: e["score"], reverse=True)
    return entries[:PRE_INJECT_MAX_PER_CATEGORY]


def scan_portfolio_bets(context_dir: Path, keywords: list) -> list:
    """Scan active-bets.md for keyword matches (these are always relevant)."""
    bets_file = context_dir / "portfolio" / "active-bets.md"
    if not bets_file.exists():
        return []

    try:
        content = bets_file.read_text(encoding="utf-8")
    except Exception:
        return []

    if score_content(content, keywords) == 0:
        return []

    # Extract bet references
    entries = []
    for match in re.finditer(r"\b(SB-\d{4}-\d{3})\b", content):
        bet_id = match.group(1)
        start = match.start()
        local = content[max(0, start - 50):start + 200]
        score = score_content(local, keywords)
        if score > 0:
            # Get the line containing the bet
            line_start = content.rfind("\n", 0, start) + 1
            line_end = content.find("\n", start)
            line = content[line_start:line_end].strip() if line_end > 0 else content[line_start:].strip()
            entries.append({
                "id": bet_id,
                "score": score,
                "summary": line[:200],
                "file": "active-bets.md",
            })

    entries.sort(key=lambda e: e["score"], reverse=True)
    return entries[:PRE_INJECT_MAX_PER_CATEGORY]


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
    """Scan context for items related to topic. Output markdown to stdout."""
    keywords = tokenize_topic(topic)

    if not keywords:
        return  # Empty topic, nothing to inject

    if verbose:
        print(f"Keywords: {keywords}", file=sys.stderr)

    all_results = {}
    total_count = 0

    # Scan each context source
    for source_name, config in CONTEXT_SOURCES.items():
        source_dir = context_dir / source_name
        entries = scan_context_source(source_dir, keywords, config)
        if entries:
            all_results[config["category"]] = entries
            total_count += len(entries)

    # Also scan portfolio for active bets
    portfolio_entries = scan_portfolio_bets(context_dir, keywords)
    if portfolio_entries:
        # Merge with existing bets category or create new
        category = "Active Bets"
        existing = all_results.get(category, [])
        # Dedup by ID
        existing_ids = {e["id"] for e in existing}
        for pe in portfolio_entries:
            if pe["id"] not in existing_ids:
                existing.append(pe)
        if existing:
            all_results[category] = existing[:PRE_INJECT_MAX_PER_CATEGORY]
            total_count = sum(len(v) for v in all_results.values())

    # Always load conventions (no keyword filtering — global context)
    conventions = load_conventions(context_dir)

    if total_count == 0 and not conventions:
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

    if total_count > 0:
        output.append(f"## Auto-Context: {total_count} related items found\n")

        items_shown = 0
        for category, entries in all_results.items():
            output.append(f"### {category}")
            for entry in entries:
                if items_shown >= PRE_INJECT_MAX_TOTAL:
                    break
                output.append(f"- **{entry['id']}**: {entry['summary']}")
                items_shown += 1
            output.append("")

            if items_shown >= PRE_INJECT_MAX_TOTAL:
                break

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
        "roi/session-log.md": "# Session ROI Log\n\n| Time | Type | Operation | Agent | Complexity | Minutes Saved | IX-ID |\n|------|------|-----------|-------|------------|---------------|-------|\n",
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
    # Pattern to match entry files by name: DR-2026-001.md, SB-2026-002.md, etc.
    file_id_pattern = re.compile(rf"^({id_prefix}-[\d-]+)\.md$")

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
                            help="Claude Code PostToolUse mode (reads stdin JSON)")
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

    # Resolve context directory
    if args.context_dir:
        context_dir = Path(args.context_dir)
    else:
        context_dir = find_context_dir()

    try:
        if args.hook:
            run_hook_mode(verbose=args.verbose)
        elif args.agent:
            if not context_dir:
                print("Error: no context/ directory found. Run /setup first.", file=sys.stderr)
                sys.exit(0)  # fail-open
            run_manual_mode(args.agent, args.skill, context_dir, verbose=args.verbose)
        elif args.pre_inject:
            if not context_dir:
                sys.exit(0)  # No context dir = nothing to inject, fail-open
            run_pre_inject_mode(args.pre_inject, context_dir, verbose=args.verbose)
        elif args.rollup:
            if not context_dir:
                print("Error: no context/ directory found.", file=sys.stderr)
                sys.exit(0)
            run_rollup_mode(context_dir, verbose=args.verbose)
        elif args.diagnose:
            if not context_dir:
                print("broken: no context/ directory found — fix: run /setup")
                sys.exit(0)
            run_diagnose_mode(context_dir, repair=args.repair, verbose=args.verbose)
    except Exception as e:
        if args.verbose:
            print(f"Fatal error (fail-open): {e}", file=sys.stderr)
        sys.exit(0)  # Always exit 0


if __name__ == "__main__":
    main()
