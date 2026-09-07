#!/usr/bin/env python3
"""telemetry-extract.py — Portable Spawn Audit Block receipt reader (T1).

The ONE place that knows the Claude-Code jsonl envelope (design I1 / §5). All
harness-shape field names (`type`, `message.content`, `tool_use`/`tool_result`,
`tool_use_id`, `message.usage`) — and, since 2026-08-02, the async-spawn
`<task-notification>` envelope — live in `iter_receipts_from_jsonl` and its
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
per-writer temp file + os.replace). Fail-open: never raises out of main; exits 0.

ONE exception to fail-open, added 2026-08-02 (Wave A fix 2): WRITE mode takes a
single-writer lock (`<context-dir>/roi/.telemetry-write.lock`, O_EXCL, 30-min
stale takeover). If another live writer holds it this process writes NOTHING and
exits 9 — a second concurrent writer is the condition that permanently lost 85%
of appends under injection, so it must be loud, not degraded-quiet. A parent
that already holds the lock hands it down via $TELEMETRY_WRITE_LOCK.

Stdlib only. Python 3.8+.
"""

from __future__ import annotations

import argparse
import html
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
    parse_context_injected,
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

# Identity-line sentinel. RELAXED 2026-08-02 (round-3 audit F2, BLOCKER).
#
# The prior shape was `You are \*\*.+?\*\* (?:in|on)\b` — it demanded the literal
# word "in" or "on" immediately after the closing `**`, i.e. it keyed on the
# CONNECTIVE rather than on the identity line. Equally valid spawn prompts using
# any other continuation were invisible to PASS 1 and could therefore never yield
# a receipt, whatever they returned:
#     You are **⚖️ General Counsel** leading the Legal Team…
#     You are **🎙️ CMO** — Chief Marketing Officer, leading the Marketing Team…
#     You are **🛠️ Tech Lead** (Development Team ET; slug `tech-lead`). …
# The audit measured 11 of 32 spawns on 2026-08-02 dropped at this hop.
#
# What identifies an identity line is the SHAPE `You are **{emoji} {Name}**`, so
# that is what we anchor on. Strictness is preserved by bounding the bold span
# rather than by dictating the next word: single line, no nested `**`, ≤80 chars
# (longest real display name measured across 1,347 corpus spawns is 61). Verified
# strictly additive: over the whole transcript tree the relaxed pattern matches
# every prompt the old one matched (0 regressions) and 351 more.
IDENTITY_SENTINEL_RE = re.compile(r"You are \*\*[^*\n]{1,80}\*\*")
AGENT_ID_IN_DESC_RE = re.compile(r"^\[([a-z][a-z0-9-]*)\]")
# Relaxed in LOCKSTEP with the sentinel and for the same reason — this reads the
# SAME identity line, and leaving it tight would admit spawns PASS 1 could not
# name (43 of the 351 carry no `[agent-key]` description, so they would all key
# as "unknown-agent"). Bounding the bold span also FIXES a latent capture defect
# in the old `.+?`: with no `*` exclusion it could run past an intervening bold
# span to reach a later `** in`, yielding slugs like
# "chief-architect-running-the-third-audit-mode-b-pass-a-convergence-…".
# Measured blast radius on the live corpus: 1 pre-existing slug corrected, 43
# newly-admitted spawns correctly named, 0 slugs degraded.
DISPLAY_NAME_RE = re.compile(r"You are \*\*(?:[^\w\s]*\s*)?([^*\n]{1,80}?)\*\*")

# --- Async/background spawn notifications (round-3 audit F1, BLOCKER) --------
# Background spawns are the DEFAULT spawn mode. Their parent `tool_result` is a
# fixed ~1,068-byte "Async agent launched successfully" stub that contains no
# Audit Block; the agent's real final response arrives later as a USER-ROLE
# PLAIN-STRING message of this shape:
#
#   <task-notification>
#   <task-id>…</task-id>
#   <tool-use-id>toolu_…</tool-use-id>
#   <status>completed</status>
#   <result>📋 Spawn Audit Block …</result>
#   <usage><subagent_tokens>…</subagent_tokens>…</usage>
#   </task-notification>
#
# PASS 2 accepted blocks only from tool_results and gated assistant-text, and a
# user-role string is neither — so well-formed, correctly-keyed blocks were read
# past every day (29 emitted / 1 captured on the audited day). The notification
# is the RIGHT surface to fix this on rather than the subagent sidecar: it is
# ONE authoritative final block (measured: never more than one Audit Block header
# per `<result>` across 1,161 corpus notifications, where sidecars carry up to
# four because they contain everything the agent typed, including blocks quoted
# into fixtures), and it carries the `<tool-use-id>` the spawn-map join needs,
# which the sidecar sweep loses entirely.
TASK_NOTIFICATION_MARKER = "<task-notification>"
NOTIF_TOOL_USE_ID_RE = re.compile(r"<tool-use-id>\s*(toolu_[A-Za-z0-9_-]+)\s*</tool-use-id>")
NOTIF_STATUS_RE = re.compile(r"<status>\s*([A-Za-z_-]+)\s*</status>")
NOTIF_RESULT_RE = re.compile(r"<result>(.*?)</result>", re.S)
# A spawn the harness reports as failed or killed did not deliver a final
# response; anything block-shaped inside such a notification is not a completed
# agent's receipt. (Measured: 0 of the 16 non-`completed` notifications in the
# corpus carry a block at all, so this is a guard against a future shape, not a
# filter doing work today.)
NOTIF_REJECT_STATUSES = frozenset({"failed", "killed"})

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
    """Best-effort token usage (R7). Returns int total or None.

    INVARIANT (O6 part 2, 2026-08-01): this function is KEPT and stays the
    main-transcript-line usage reader. On real transcripts a tool_result line
    (user role) never carries message.usage — usage lives only on assistant
    lines (the join defect, gate-spec tech-lead.md section 2.1.1) — so for
    spawn candidates it is a null-returning fallback behind the sidecar
    reader below. It remains live (called as the fallback) and is exercised
    by the golden fixtures, which place usage on the tool_result line."""
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


# ---------------------------------------------------------------------------
# Sidecar join (O6 part 2, 2026-08-01) — the subagent's OWN usage
# ---------------------------------------------------------------------------
# A spawn's measured tokens are the SUBAGENT's consumption, recorded in the
# session's sidecar pair (`<session>/subagents/agent-*.meta.json` carrying
# toolUseId + sibling `agent-*.jsonl` carrying per-turn message.usage), not
# anywhere in the parent transcript. The component reader is pricing.py in
# this directory — ONE extraction rule, ONE implementation (request-as-
# billing-unit dedup, components preserved separately, <synthetic> excluded).
# Sidecar absent/unreadable -> fields stay null, loudly noted on stderr (O7);
# never fabricated. The append-only store is never rewritten — the sidecar
# fields appear on NEWLY-extracted receipts only.
try:
    import pricing as _pricing  # same-directory, stdlib-only module
except Exception as _pricing_err:  # loud degrade, never silent (O7)
    _pricing = None
    print(f"telemetry-extract: pricing module unavailable ({_pricing_err}); "
          f"sidecar-measured tokens will stay null", file=sys.stderr)

_SIDECAR_MAPS = {}


def _sidecar_map_for(subagents_dir: Path) -> dict:
    """{toolUseId: sidecar .jsonl Path} for one session's subagents dir.
    Cached per dir; fail-open (an unreadable meta is skipped)."""
    key = str(subagents_dir)
    if key in _SIDECAR_MAPS:
        return _SIDECAR_MAPS[key]
    m = {}
    try:
        if subagents_dir.is_dir():
            for meta in subagents_dir.glob("agent-*.meta.json"):
                try:
                    tid = json.loads(
                        meta.read_text(encoding="utf-8")).get("toolUseId")
                except Exception:
                    continue
                if tid:
                    m[tid] = meta.with_name(
                        meta.name[:-len(".meta.json")] + ".jsonl")
    except Exception:
        pass
    _SIDECAR_MAPS[key] = m
    return m


def _sidecar_usage_for(transcript_path: Path, tool_use_id: str):
    """Resolve + read the spawn's sidecar. Returns (payload | None, reason).

    payload = {"measured_tokens": int, "components": {...}, "sidecar": name}
    measured_tokens = deduped input_tokens + output_tokens (the frozen
    drift-freeze v2 definition). components preserves all four token
    components separately (never pre-summed): input_tokens, output_tokens,
    cache_read_input_tokens, cache_write_5m_tokens."""
    if _pricing is None:
        return None, "pricing module unavailable"
    subagents_dir = transcript_path.with_suffix("") / "subagents"
    sc = _sidecar_map_for(subagents_dir).get(tool_use_id)
    if sc is None:
        return None, f"no surviving sidecar in {subagents_dir}"
    if not sc.exists():
        return None, f"sidecar meta present but jsonl missing ({sc.name})"
    try:
        turns = _pricing.extract_turns(sc)
    except Exception as e:
        return None, f"sidecar unreadable ({type(e).__name__}: {e})"
    comps = {k: 0 for k in _pricing.COMPONENTS}
    counted = 0
    for t in turns:
        if t.model == _pricing.SYNTHETIC_MODEL:
            continue  # sentinel, not a model; never counted (all-zero anyway)
        for k in _pricing.COMPONENTS:
            comps[k] += t.components[k]
        counted += 1
    return {
        "measured_tokens": comps["input_tokens"] + comps["output_tokens"],
        "components": comps,
        "sidecar": sc.name,
    }, None


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


def _parse_task_notification(text: str):
    """Parse an async-spawn `<task-notification>` string.

    Returns `(tool_use_id, result_body)` for a notification that could carry a
    receipt, or None to skip. Skips (in order): non-notifications; notifications
    whose `<status>` is in NOTIF_REJECT_STATUSES; notifications with no
    `<tool-use-id>` (10 in the corpus — with no join key they could never be
    attributed to a spawn, and an unkeyed receipt degrades dedup exactly the way
    the rejected sidecar sweep did); notifications with no `<result>`.

    The body is `html.unescape`d because the harness HTML-escapes it — 929 of
    1,161 corpus notifications carry `&amp;`/`&lt;`/`&gt;`/`&quot;`, so an
    un-unescaped Audit Block reaches the parser with mangled `Found &amp; fed`
    lines. Unescaping is unconditional (a body with no entities is unchanged),
    which is what the audit's named design specifies; the residual cost is that
    a literal `&amp;` an agent actually typed becomes `&` in the stored block
    text. That is cosmetic — it touches no `[section]` line, count, or ID — and
    it is deterministic, so `block_hash` and therefore dedup stay stable."""
    if TASK_NOTIFICATION_MARKER not in text:
        return None
    st = NOTIF_STATUS_RE.search(text)
    if st and st.group(1).strip().lower() in NOTIF_REJECT_STATUSES:
        return None
    tid_m = NOTIF_TOOL_USE_ID_RE.search(text)
    if not tid_m:
        return None
    res_m = NOTIF_RESULT_RE.search(text)
    if not res_m:
        return None
    return tid_m.group(1), html.unescape(res_m.group(1))


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

def _accept_keyed_blocks(path, spawn_map, tid, text, source, ts, fallback_usage):
    """Yield RawCandidate for every acceptable block in `text`, keyed to `tid`.

    Shared by the two SPAWN-KEYED accept paths — SOURCE (a) tool_result (sync
    spawns) and SOURCE (c) task-notification (async spawns). Deliberately ONE
    implementation: both paths must apply the same A4 section guard, the same
    lazy once-per-payload sidecar resolution, and the same loud-on-failure
    stderr note, and a shared helper guarantees that where duplication would
    only promise it."""
    side_payload = None
    side_resolved = False
    for (ln, block, is_old) in extract_blocks(text):
        # A4: reject header-line-only prose (no [section] line). v1-legacy
        # blocks legitimately have no [section] markers, so the guard applies
        # to new-format blocks only.
        if not is_old and not _has_section_line(block):
            continue
        # O6 part 2: the spawn's measured usage lives in the subagent's
        # sidecar, not on the (user-role) line carrying the block. Resolve
        # lazily, once per accepted payload; on failure the fields stay null
        # and the reason is loud on stderr (O7) — never fabricated. The
        # sidecar is keyed on toolUseId, so it resolves identically for a
        # sync tool_result and an async notification.
        if not side_resolved:
            side_resolved = True
            side_payload, side_reason = _sidecar_usage_for(path, tid)
            if side_payload is None:
                print(
                    f"telemetry-extract: measured_tokens stays "
                    f"null for tool_use_id={tid} "
                    f"({path.name}): {side_reason}",
                    file=sys.stderr)
        yield RawCandidate(
            text=block, source_tag=path.name,
            tool_use_id=tid, agent_slug_hint=spawn_map[tid]["slug"],
            usage=(side_payload if side_payload is not None
                   else fallback_usage),
            start_line=ln, is_old=is_old,
            source=source, ts=ts,
        )


def iter_receipts_from_jsonl(path, *, include_assistant_text=False):
    """Yield RawCandidate for every accepted Spawn Audit Block in a transcript.

    Two-pass: Pass 1 builds {tool_use_id: {slug, prompt}} from genuine Agent/Task
    spawns; Pass 2 accepts blocks from (a) tool_results whose tool_use_id is in
    the spawn map [sync spawns], (b) gated assistant-text leading with the block
    header [OFF by default], or (c) user-role `<task-notification>` strings whose
    `<tool-use-id>` is in the spawn map [async/background spawns — the default
    spawn mode; added 2026-08-02 per round-3 audit F1].

    (a) and (c) are disjoint by construction and measured to be so: across the
    whole transcript tree, 428 tool_use_ids carry a block only in a tool_result,
    800 only in a notification, and ZERO in both — a spawn is either synchronous
    or backgrounded, never both. No block is therefore counted twice, and the
    write-layer composite dedup key (`tool_use_id:block_hash[:12]`) remains the
    backstop for replays across files.
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

        # SOURCE (a) — tool_result whose tool_use_id is a genuine spawn [PRIMARY,
        # synchronous spawns]. _usage_of(obj) remains the fallback behind the
        # sidecar (None on real transcripts; populated by the golden fixtures).
        for part in _content_parts(obj):
            if part.get("type") == "tool_result":
                tid = part.get("tool_use_id")
                if tid in spawn_map:
                    for cand in _accept_keyed_blocks(
                        path, spawn_map, tid, _tool_result_text(part),
                        "tool_result", ts, _usage_of(obj),
                    ):
                        yield cand

        # SOURCE (c) — user-role <task-notification> whose <tool-use-id> is a
        # genuine spawn [PRIMARY, async/background spawns — the default mode].
        # Role-gated: every one of the 1,161 notifications in the corpus is
        # user-role, and gating keeps an assistant that merely *quotes* a
        # notification out of the receipt stream. There is no message.usage on
        # this line, so the sidecar is the only usage source (fallback None).
        if _role(obj) == "user":
            for part in _content_parts(obj):
                if part.get("type") != "text":
                    continue
                notif = _parse_task_notification(part.get("text", "") or "")
                if notif is None:
                    continue
                tid, body = notif
                if tid not in spawn_map:
                    continue
                for cand in _accept_keyed_blocks(
                    path, spawn_map, tid, body, "task-notification", ts, None,
                ):
                    yield cand

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

    # [Context Injected] receipt field (O5 — DR-2026-176/178). Attached to
    # NEWLY-extracted receipts only: the append-only audit-receipts.jsonl store
    # is never backfilled or rewritten; historical lines keep their old shape.
    # load_bearing_ids/coverage are self-reported — recorded, never gated.
    receipt["context_injected"] = parse_context_injected(candidate.text)

    # roi.reporting_schema stamp (O2 hours-only switch, 2026-08-01):
    #   "v1-self-report"  — the block carries a [Post-Execution ROI] section
    #                       (the retired self-report emit schema; parsed for
    #                       history by _parse_roi, never published);
    #   "v2-hours-table"  — the block carries no ROI section (post-schema
    #                       receipts; hours are computed downstream from the
    #                       owner-affirmed activity table, never from the block).
    # Stamped on NEWLY-extracted receipts only; the store is never backfilled.
    receipt["roi"]["reporting_schema"] = (
        "v1-self-report" if receipt["roi"].get("reported_raw") else "v2-hours-table")

    # Join slug wins over in-block slug — the join is structurally trustworthy.
    if candidate.agent_slug_hint and candidate.agent_slug_hint != "unknown-agent":
        receipt["agent_slug"] = candidate.agent_slug_hint
        if not receipt["authors"] or receipt["authors"] == ["unknown-agent"]:
            receipt["authors"] = [candidate.agent_slug_hint]

    # Token reconciliation (R7): reported stays authoritative (I2/D2).
    # Two payload shapes (O6 part 2, 2026-08-01):
    #   dict — sidecar-derived: measured_tokens = deduped input+output (the
    #          frozen drift-freeze v2 definition); the four components are
    #          preserved separately on roi.measured_components (the scalar
    #          measured_tokens cannot carry them). New receipts only — the
    #          append-only store is never rewritten.
    #   int  — legacy transcript-line total from _usage_of, byte-identical
    #          behavior (exercised by the golden fixtures).
    if isinstance(candidate.usage, dict):
        measured = candidate.usage["measured_tokens"]
        receipt["roi"]["measured_tokens"] = measured
        receipt["roi"]["measured_components"] = candidate.usage["components"]
        receipt["roi"]["measured_source"] = "sidecar:" + candidate.usage["sidecar"]
        rep = receipt["roi"].get("tokens")
        if rep:
            try:
                receipt["roi"]["drift"] = round(measured / rep, 2)
            except ZeroDivisionError:
                receipt["roi"]["drift"] = None
    elif candidate.usage:
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
    """Temp-file + os.replace (R8). ensure_ascii handled by callers for jsonl.

    The temp name is PER-WRITER (pid + a monotonic counter). Wave A fix 2
    (round-2 data-architect BLOCKER F-2): the shared `.tmp` name meant two
    concurrent writers fought over one file — the injection produced 78
    sharing-violation errors on top of the lost appends. The single-writer lock
    in main() is the real fix; unique temp names are the belt to its braces, and
    they also stop a crashed run from leaving a temp file another run trips on."""
    path.parent.mkdir(parents=True, exist_ok=True)
    global _TMP_SEQ
    _TMP_SEQ += 1
    tmp = path.parent / f"{path.name}.tmp-{os.getpid()}-{_TMP_SEQ}"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.replace(tmp, path)


_TMP_SEQ = 0


# ---------------------------------------------------------------------------
# Single-writer lock (Wave A fix 2) — mirrors
# refresh-and-build-dashboard.py::acquire_write_lock. Deliberately a per-file
# copy, not a shared import: this module stays stdlib-only and portable, and
# the runner never import-executes it. Same path, same env var, same stale
# window — change them in lockstep.
# ---------------------------------------------------------------------------

LOCK_ENV = "TELEMETRY_WRITE_LOCK"
LOCK_STALE_SECONDS = 30 * 60


def _acquire_write_lock(context_dir: Path):
    """Serialize store writers behind one O_EXCL lockfile.

    Returns (token, acquired_here). `token` is None when another LIVE process
    holds it — the caller must NOT write. An inherited lock (LOCK_ENV set by a
    parent that already holds it, e.g. refresh-and-build-dashboard.py running
    this as a subprocess) returns ("inherited", False) so we never deadlock
    against our own parent. A lock older than LOCK_STALE_SECONDS is taken over
    with a loud stderr note."""
    import time as _time
    inherited = os.environ.get(LOCK_ENV)
    if inherited:
        return "inherited", False
    lock = Path(context_dir) / "roi" / ".telemetry-write.lock"
    lock.parent.mkdir(parents=True, exist_ok=True)
    token = f"{os.getpid()}@{datetime.now(timezone.utc).isoformat(timespec='seconds')}"
    for attempt in (1, 2):
        try:
            fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                fh.write(json.dumps({"pid": os.getpid(), "who": "telemetry-extract",
                                     "token": token,
                                     "acquired": datetime.now(timezone.utc)
                                     .isoformat(timespec="seconds")}))
            return token, True
        except FileExistsError:
            if attempt == 2:
                break
            try:
                age = _time.time() - lock.stat().st_mtime
                held = lock.read_text(encoding="utf-8").strip()
            except OSError:
                age, held = 0.0, "<unreadable>"
            if age > LOCK_STALE_SECONDS:
                print(f"telemetry-extract: STALE LOCK TAKEOVER — {lock} is "
                      f"{age/60:.1f} min old, holder {held}; taking over.",
                      file=sys.stderr)
                try:
                    lock.unlink()
                except OSError:
                    pass
                continue
            print(f"telemetry-extract: WRITE LOCK HELD by another run ({held}, age "
                  f"{age/60:.1f} min) — refusing to append as a second concurrent "
                  f"writer. Nothing was written.", file=sys.stderr)
            return None, False
    return None, False


def _release_write_lock(context_dir: Path, token, acquired_here: bool) -> None:
    if not acquired_here or not token:
        return
    lock = Path(context_dir) / "roi" / ".telemetry-write.lock"
    try:
        if lock.exists() and json.loads(lock.read_text(encoding="utf-8")).get("token") == token:
            lock.unlink()
    except (OSError, ValueError):
        pass


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

    by_source = {"tool_result": 0, "task-notification": 0, "assistant-text": 0,
                 "text-mode": 0, "no-block-fallback": 0}
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

    # v2_pass_rate proxy (A3, re-specified 2026-08-01 for the O2 hours-only
    # switch): a block passes if it is non-legacy, has a SKILL.md path, AND
    # satisfies its emit epoch's ROI contract:
    #   - v2-hours-table era (no ROI section; the block carries the
    #     always-present [Context Injected]): ROI absence is CONFORMANT — the
    #     receipt is NOT structurally failed for lacking ROI fields.
    #   - v1-self-report era (ROI section present): the historical contract
    #     holds — reported_raw non-empty and at least one of minutes/tokens/
    #     value_usd parseable. Pure-garbage ROI still fails.
    #   - a block with NEITHER an ROI section NOR [Context Injected] is a
    #     pre-schema truncation and keeps failing (history unchanged).
    def _passes(r):
        roi = r["roi"]
        structural = (r["format"] != "v1-legacy"
                      and bool(r["loads"]["skill_md"]["path"]))
        if not structural:
            return False
        if (roi.get("reporting_schema") == "v2-hours-table"
                and (r.get("context_injected") or {}).get("present")):
            return True
        roi_parsed = (roi["minutes"] is not None
                      or roi["tokens"] is not None
                      or roi["value_usd"] is not None)
        return bool(roi["reported_raw"]) and roi_parsed
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

    lock_token, lock_mine = None, False
    try:
        receipts, spawns = _gather(args)

        if args.summary:
            print(json.dumps(summary(receipts, spawns), ensure_ascii=True, indent=2))
            sys.exit(0)

        # Wave A fix 2: WRITE mode is lock-gated. Losing the race is NOT
        # fail-open — a second concurrent writer is exactly the condition that
        # permanently lost 85% of appends in the round-2 injection, so we exit
        # non-zero having written nothing rather than proceed quietly.
        lock_token, lock_mine = _acquire_write_lock(Path(args.context_dir))
        if lock_token is None:
            sys.exit(9)

        written = write_receipts(receipts, args.context_dir)
        print(json.dumps(
            {"receipts_parsed": len(receipts), "written": written,
             "skipped_dedup": len(receipts) - written, "spawns": spawns},
            ensure_ascii=True,
        ))
    except Exception as e:  # fail-open (R8 / I3)
        print(f"telemetry-extract: fail-open ({e})", file=sys.stderr)
    finally:
        _release_write_lock(Path(args.context_dir), lock_token, lock_mine)
    sys.exit(0)


if __name__ == "__main__":
    main()
