# Portable Agent Telemetry — Technical Design Note

**Phase**: 0 (design ratification) of `cache/telemetry-portable-capture-plan-2026-05-30.md`
**Author**: 🏗️ Chief Architect (Architecture Team)
**Date**: 2026-05-30
**Status**: RATIFIED — buildable spec for backend-dev
**Builds on**: plan §2, §5 (two-pass join + module-boundary rule), §5.1 (R1–R9)
**Locked (do not relitigate)**: D1 manual-run (no Claude Code hooks); D2 self-reported numbers authoritative; D3 local Drive + `<clone>` clone → public GitHub only, NOT PMTK.

This is an engineering spec. It defines module boundaries, the join algorithm, data contracts, build order, and the portability assertion. backend-dev builds Phase 1 then Phase 2 from this note; qa-engineer's 11 fixtures gate each phase.

---

## 0. Design Invariants (the "why" behind every choice below)

| # | Invariant | Enforced by |
|---|-----------|-------------|
| I1 | **One harness-shape knower.** Only `iter_receipts_from_jsonl()` in `telemetry-extract.py` knows the Claude-Code jsonl envelope (`type`, `message.content`, `tool_use`/`tool_result`, `tool_use_id`, `message.usage`). | Module-boundary rule §5 + grep gate (Phase 1 verify) |
| I2 | **Parse, never re-derive (D2).** When a block exists, its self-reported Loads/DR/ROI numbers are authoritative. Baseline re-derivation runs ONLY for no-block spawns and only when explicitly opted in. | `audit_parse.parse_block` reads verbatim; no baselines import in the parse path |
| I3 | **Fail-open, append-only, idempotent.** Never raise on bad input; skip the bad line/block and continue; dedup gates every write. | `parse_block` is total; per-line try/except; `.telemetry-dedup` |
| I4 | **Structural join is the discriminator, not role.** Subagent receipts arrive in `tool_result` parts wrapped in `type=user` messages; a role filter drops 100% of them. Accept a block only via the `tool_use_id` join (or gated assistant-text). | Two-pass join §2 |
| I5 | **Reuse os-tracker's writers; do not touch its code paths.** Extractor owns its OWN richer writer + the canonical jsonl. os-tracker `append_roi_log`/`--diagnose`/`--rollup`/`--pre-inject` stay byte-identical (R3). | Separate writer functions in `telemetry-extract.py` |

---

## 1. Module Map

Three Python files in the plugin source's hooks/ (Drive) and mirrored to `<clone>/hooks/` (clone, flat). Stdlib only, Python 3.8+.

### 1.1 `audit_parse.py` — shared, PORTABLE core (T2) — NEW + one lift

The portability boundary. Receives **plain text + a source tag** only. Contains ZERO jsonl-envelope field names (`type`, `message`, `content`, `tool_use`, `tool_result`, `tool_use_id`, `usage` MUST NOT appear). This is the file `--from text|stdin|dir` and any future non-Claude harness feed.

| Symbol | Origin | Contract |
|--------|--------|----------|
| `extract_blocks(text) -> list[(start_line:int, block_text:str, is_old_format:bool)]` | **Lifted VERBATIM** from `audit-block-validator.py` (lines 125–174). Same function, moved here; validator imports it back. | Returns every Spawn Audit Block (new + v1-legacy) found in `text`, with 1-based start line and the old-format flag. Unchanged behavior — the validator's existing fixtures must still pass. |
| `parse_block(block_text, source_tag, *, start_line=0, is_old_format=False) -> dict` | **NEW.** Total function. NEVER raises. | Parses `[Pre-Execution Loads]`, `[Decision Records …]` (optional), `[Post-Execution ROI]`, `[Authors]` (joint) into the `Receipt` dict (§3.1). On any parse miss, records a `parse_warnings[]` entry and continues. Free-text ROI handled per R2. |
| `validate_block(...)` | **Stays in validator** (imports `extract_blocks` from here). | Not moved. `audit_parse.py` is the parse/extract core; schema *validation* stays in the validator to keep concerns separate. |

**Lift mechanics (load-bearing per I1 + Phase-1 grep gate):** `extract_blocks`, `NEW_HEADER_RE`, `OLD_HEADER_RE`, `SECTION_RE` move to `audit_parse.py`. `audit-block-validator.py` deletes its local copies and does `from audit_parse import extract_blocks, NEW_HEADER_RE, OLD_HEADER_RE, SECTION_RE`. After the lift, `grep -c "def extract_blocks" hooks/*.py` MUST equal 1. The validator's count-line regexes (`COUNT_LINE_RES`), placeholder/mode/lightweight checks stay in the validator — those are validation, not extraction. `parse_block` re-implements the count-line *reads* (it extracts values; the validator checks schema legality) using the same regex shapes so the two never drift on what a "count line" looks like; the shared regexes live in `audit_parse.py` and both import them.

`parse_block` MUST NOT import `baselines.json`, `os`, harness shapes, or any writer. It is pure text→dict. This is what makes I2 + portability hold.

### 1.2 `telemetry-extract.py` — portable reader (T1) — NEW

Owns everything harness-specific and all NEW richer writers + CLI.

| Symbol | Contract |
|--------|----------|
| `iter_receipts_from_jsonl(path) -> Iterator[RawCandidate]` | **THE ONLY harness adapter (I1).** Reads a Claude-Code `.jsonl` line-by-line (R8: `encoding="utf-8", errors="replace"`; each `json.loads` in try/except; skip bad line, never abort). Runs the **two-pass join** (§2). Yields `RawCandidate(text, source_tag, tool_use_id, agent_slug_hint, usage)` — plain values, no envelope leakage past this boundary. |
| `iter_receipts_from_text(text, source_tag) -> Iterator[RawCandidate]` | For `--from text|stdin`. Calls `extract_blocks` directly (no join — text mode has no tool_use structure); `tool_use_id=None`, `agent_slug_hint=None`, `usage=None`. |
| `iter_receipts_from_dir(path) -> Iterator[RawCandidate]` | Globs `*.jsonl` (non-recursive) / `**/*.jsonl` (`--recursive`); fans into `iter_receipts_from_jsonl`. |
| `build_receipt(candidate) -> Receipt` | Calls `audit_parse.parse_block(candidate.text, candidate.source_tag, ...)`; overlays join-derived `tool_use_id` + `agent_slug` (join slug wins over in-block slug when both present, since the join is structurally trustworthy); attaches token reconciliation (R7) from `candidate.usage`. |
| `write_receipts(receipts, ctx_dir)` | NEW richer writers (§3.3) + canonical `audit-receipts.jsonl`. Dedup-gated (R4). Temp-file + `os.replace` (R8). Does NOT call os-tracker writers. |
| `summary(receipts) -> dict` | `--summary` JSON object (§3.4) — printed, no writes. The object Phase-3 data-analyst asserts against. |
| `main()` | CLI: `--from jsonl|text|stdin|dir`, `--path`, `--context-dir`, `--summary`, `--include-assistant-text`, `--include-no-block-fallback`, `--recursive`. |

### 1.3 `audit-block-validator.py` — `--role-aware` (T3) — REFACTOR (Phase 2)

- Imports `extract_blocks` (+ header regexes) from `audit_parse.py` (the lift).
- Adds `--role-aware` (**default ON**). When on, `scan_jsonl` delegates candidate selection to `telemetry-extract.iter_receipts_from_jsonl` (the join) instead of its current blind "any line containing 'Audit Block'" scan, then runs `validate_block` on the joined candidates only.
- `--no-role-aware` preserves the *current* blind `scan_jsonl` verbatim → reproduces the legacy ~22% raw pass-rate (the Phase-2 anti-regression anchor).
- **Import direction note:** to avoid a cycle, the join helper used by `--role-aware` lives in `telemetry-extract.py` and the validator imports it. `audit_parse.py` imports nothing from either consumer (it is the leaf). Dependency DAG: `audit_parse ← telemetry-extract ← validator` (validator also imports `audit_parse` directly for `validate_block`'s extract needs). No cycles.

### 1.4 `os-tracker.py` — DEPRECATE `--hook` (T4) — MINIMAL (Phase 2)

- `--hook`: warn-and-no-op shim (prints a one-line deprecation note to stderr, exits 0). Per D1 there is no PostToolUse; the hook path is dead.
- `--pre-inject`, `--diagnose`, `--diagnose --repair`, `--rollup`: **UNTOUCHED** (R3). `--diagnose --repair` remains the DR-index rebuild used in Phase 3.
- `append_roi_log` and all os-tracker writers: **UNTOUCHED** (R3). The extractor does NOT call them; it has its own richer writer. This is deliberate — rippling os-tracker's writers to add ROI columns would force re-testing `--diagnose`/`--rollup`, which we are not changing.

---

## 2. Two-Pass Structural Join (the load-bearing algorithm)

Lives entirely inside `iter_receipts_from_jsonl()` (I1). Role is NOT the discriminator (I4).

```
def iter_receipts_from_jsonl(path):
    # ---------- PASS 1: build the spawn map ----------
    # tool_use_id -> {slug, prompt}  for genuine Agent/Task spawns carrying the identity sentinel
    spawn_map = {}
    for obj in _iter_jsonl_objects(path):           # line-by-line, try/except per line (R8)
        for part in _content_parts(obj):            # normalizes message.content (list|str) -> parts
            if part.get("type") == "tool_use" and part.get("name") in ("Agent", "Task"):
                prompt = (part.get("input") or {}).get("prompt", "") or ""
                if IDENTITY_SENTINEL_RE.search(prompt):     # r"You are \*\*.+?\*\* (?:in|on)\b"
                    tid = part.get("id")                    # tool_use id
                    if tid:
                        spawn_map[tid] = {
                            "slug": _slug_from_prompt(prompt),   # [agent-key] in desc, else display-name->slug
                            "prompt": prompt,
                        }

    # ---------- PASS 2: accept blocks from exactly two sources ----------
    seen = set()
    for obj in _iter_jsonl_objects(path):
        # SOURCE (a) — tool_result whose tool_use_id is a genuine spawn  [PRIMARY, default ON]
        for part in _content_parts(obj):
            if part.get("type") == "tool_result":
                tid = part.get("tool_use_id")
                if tid in spawn_map:
                    text = _tool_result_text(part)          # flatten content -> str
                    for (ln, block, is_old) in extract_blocks(text):   # from audit_parse
                        yield RawCandidate(
                            text=block, source_tag=path.name,
                            tool_use_id=tid, agent_slug_hint=spawn_map[tid]["slug"],
                            usage=_usage_of(obj),           # R7 token reconciliation (optional)
                            start_line=ln, is_old=is_old,
                        )

        # SOURCE (b) — assistant-role text that LEADS with the block  [GATED, default OFF]
        if INCLUDE_ASSISTANT_TEXT and _role(obj) == "assistant":
            for part in _content_parts(obj):
                if part.get("type") == "text":
                    t = part.get("text", "")
                    head = t[:200]
                    if NEW_HEADER_RE.search(head) and "[Pre-Execution Loads]" in t:
                        for (ln, block, is_old) in extract_blocks(t):
                            h = sha256(_normalize(block))
                            if h in seen:          # dedup assistant-text by block hash
                                continue
                            seen.add(h)
                            yield RawCandidate(
                                text=block, source_tag=path.name,
                                tool_use_id=None, agent_slug_hint=None,
                                usage=None, start_line=ln, is_old=is_old,
                            )

        # EXCLUDE BY CONSTRUCTION: every other tool_result (Read/Bash/Grep/context-recall echoes),
        # all plain user/assistant text not matching (b). These are the decoy class that produced
        # the misleading 22% raw pass-rate. They are never yielded.
```

**Why two passes (not one):** the `tool_result` carrying a subagent's receipt and the `tool_use` that spawned it are different lines; the result may even precede full knowledge of the spawn in a streamed log. Pass 1 fully materializes `spawn_map` before Pass 2 filters, so acceptance is order-independent.

**Sentinel:** `IDENTITY_SENTINEL_RE = re.compile(r"You are \*\*.+?\*\* (?:in|on)\b")` — matches both "in a simulated Product Organization" (OS) and "on the {Team} Team" (ET). This is the same shape os-tracker's `AGENT_IDENTITY_PATTERN` uses, kept consistent.

**Decoy rejection (fixtures 4 + 10):** an Audit Block sitting inside a `Read`/`Bash` tool_result is rejected because its `tool_use_id` is NOT in `spawn_map` (that id named `Read`, not `Agent`/`Task`). Only the tool-name-gated join rejects it — a text scan cannot.

---

## 3. Data Contracts

### 3.1 `Receipt` object (in-memory dict; one per accepted block)

```python
Receipt = {
    "ts": str,                    # ISO-8601 UTC; from message.timestamp if present, else run-time
    "source_file": str,          # transcript basename (source_tag)
    "tool_use_id": str | None,   # join key (None for assistant-text / text-mode)
    "block_hash": str,           # sha256(normalized block) — always present; dedup fallback + provenance
    "agent_slug": str,           # join slug wins; else in-block slug; else "unknown-agent"
    "format": str,               # "v2" | "v1-legacy" | "joint"
    "authors": list[str],        # joint only: [slug, ...]; else [agent_slug]
    "loads": {
        "skill_md": {"ok": bool, "path": str},
        "preload_packs": {"count": int | None, "items": list[str]},
        "task_skills":   {"count": int | None, "items": list[str]},
        "conditional":   {"count": int | None, "items": list[str]},
        "mandatory":     {"count": int | None, "items": list[str]},
        "fallbacks": str,            # "none" or description
    },
    "decision_records": {            # OS deliverable blocks only; {} when section absent/ET/skipped
        "present": bool,
        "skipped_reason": str | None,    # e.g. "non-deliverable task"
        "read_pre_analysis": list[str],  # DR-YYYY-NNN honored
        "drafted":  list[str],           # DR-YYYY-NNN newly written
        "updated":  list[str],           # DR-YYYY-NNN status-changed
        "conflicts": list[str],
        "assumptions": list[str],        # A-NNN
    },
    "roi": {
        "reported_raw": str,         # the verbatim [Post-Execution ROI] block text (R2 — ALWAYS stored)
        "minutes": int | None,       # parsed Time-saved -> minutes; None if unparseable ("—")
        "tokens": int | None,        # parsed Tokens (e.g. "58k" -> 58000)
        "value_usd": int | None,     # parsed Value (e.g. "~$300" -> 300)
        "measured_tokens": int | None,   # from message.usage if present (R7); else None
        "drift": float | None,       # measured/reported ratio when both present; else None
    },
    "parse_warnings": list[str],     # human-readable, e.g. "roi.minutes: 'Time saved' line not parseable"
    "source": str,                   # "tool_result" | "assistant-text" | "text-mode" | "no-block-fallback"
}
```

**Free-text ROI parse contract (R2):** blessed regexes only; anything else → `None` + a `parse_warnings[]` entry. NEVER re-derive from baselines when a block exists (I2).

| Field | Regex (case-insensitive, anchored on the ROI line) | Normalization |
|-------|-----------------------------------------------------|---------------|
| `minutes` | `Time saved:\s*~?\s*([\d.]+)\s*(hr|hrs|hour|hours|min|mins|minutes)` | hrs×60 → int minutes; else raw minutes |
| `tokens`  | `Tokens?:\s*~?\s*([\d.]+)\s*([km]?)` | `k`→×1e3, `m`→×1e6 → int |
| `value_usd` | `Value:\s*~?\s*\$\s*([\d,]+)` | strip commas → int |

When `Time saved` is unparseable, write `minutes=None` and surface in `--summary` (R7: "Value with no Time-saved" is an implausibility flag). Never substitute a baseline number.

### 3.2 `audit-receipts.jsonl` line schema (CANONICAL source; R3)

One JSON object per receipt, `json.dumps(..., ensure_ascii=True)` (R8, surrogate-safe). This is the system of record; the `.md` writers are a **projection** of it.

```json
{
  "ts": "2026-05-30T09:15:00Z",
  "source_file": "ee5bb914-....jsonl",
  "tool_use_id": "toolu_01ABC...",
  "block_hash": "9f2c...",
  "agent_slug": "chief-architect",
  "format": "v2",
  "authors": ["chief-architect"],
  "loads": { "skill_md": {"ok": true, "path": ".claude/skills/chief-architect/SKILL.md"},
             "preload_packs": {"count": 4, "items": ["...","..."]},
             "task_skills": {"count": 0, "items": []},
             "conditional": {"count": 0, "items": []},
             "mandatory": {"count": 0, "items": []},
             "fallbacks": "none" },
  "decision_records": { "present": false, "skipped_reason": "ET agent — no DR registry",
                        "read_pre_analysis": [], "drafted": [], "updated": [],
                        "conflicts": [], "assumptions": [] },
  "roi": { "reported_raw": "- Time saved: ~3 hrs ...\n- Tokens: 58k ...\n- Value: ~$300 ...",
           "minutes": 180, "tokens": 58000, "value_usd": 300,
           "measured_tokens": 61240, "drift": 1.06 },
  "parse_warnings": [],
  "source": "tool_result"
}
```

**`tool_use_id | block_hash`:** `tool_use_id` is the primary dedup/provenance key when present; `block_hash` is always present and is the fallback key for assistant-text / text-mode receipts (R4).

### 3.3 Richer ROI `.md` row (projection of the jsonl)

`telemetry-extract.py` writes its OWN ROI log (NOT os-tracker's 7-column `append_roi_log`). Full protocol columns:

```
| Time | Source File | Agent | Format | Min Saved | Tokens | Value $ | Packs | DR Drafted | DR Updated | Drift | tool_use_id/hash |
```

Plus the existing interaction day-log + `current-session.md` (extractor writes its own copies into `context/interactions/` using the same on-disk shape os-tracker emits, so `/interaction-recall` and `--diagnose --repair`'s index rebuild keep working). DR events (drafted/updated, from `decision_records`) are appended to `context/decisions/index.md` as event lines.

### 3.4 `--summary` JSON (no writes; Phase-3 assertion target)

```json
{ "spawns": 213, "receipts": 207, "v1_legacy_count": 42, "v2_pass_rate": 0.94,
  "value_usd": 4200, "implausible": [{"source_file":"...","reason":"value-no-minutes"}],
  "by_source": {"tool_result": 201, "assistant-text": 0, "text-mode": 0, "no-block-fallback": 0} }
```

`spawns` = size of `spawn_map` across the run; `receipts` = accepted blocks. `v2_pass_rate` = blocks passing validator schema / total non-legacy. `implausible` carries R7 flags (drift > 3×, or value with no minutes).

---

## 4. Build Order (for backend-dev)

Build strictly Phase 1 → Phase 2. Each phase is gated by the named fixtures from plan §6 (qa-engineer authors all 11 with committed `expected-output.json`, asserted by diff).

### Phase 1 — Core portable reader (T1 + T2)

1. Create `audit_parse.py`. **Lift** `extract_blocks` + header/section regexes verbatim from the validator. Add `parse_block` (total, never-raises) + the shared count-line + ROI regexes. No envelope field-names, no baselines import (grep-verified by chief-architect).
2. Create `telemetry-extract.py`: `iter_receipts_from_jsonl` (two-pass join §2), `iter_receipts_from_text`, `iter_receipts_from_dir`, `build_receipt`, `write_receipts` (+ jsonl), `summary`, `main`.
3. Wire `audit_parse` import into the validator now ONLY as the lift target (no `--role-aware` yet — that is Phase 2) so the validator's existing behavior is unchanged but `extract_blocks` is defined once.

**Phase 1 gating fixtures (all 11; the load-bearing ones called out):**

| # | Fixture | MUST yield |
|---|---------|-----------|
| 1 | subagent-receipt-in-`tool_result` — **P0 happy path** | 1 receipt, `source:"tool_result"`, correct slug |
| 2 | clean v2 assistant emission | 1 (only with `--include-assistant-text`) |
| 3 | v1-legacy `Pre-Execution Self-Check` | 1, `format:"v1-legacy"` |
| 4 | real-transcript decoy `c0e15e9f` | **0 captures** |
| 5 | real-transcript mixed `e1dd6b95` | **exactly the genuine count** |
| 6 | joint-authoring block | 1, `format:"joint"`, `authors[]` populated |
| 7 | cross-file duplicate `tool_use_id` | 1 (idempotency) |
| 8 | truncated block (no `[Post-Execution ROI]`) | 1, `roi.minutes=None`, fail-open |
| 9 | malformed-JSON line mid-transcript | skip line + continue, exit 0 |
| 10 | audit block inside `Read`/`Bash` tool_result — **hard decoy** | **0** (only the tool-name join rejects) |
| 11 | OS block WITH `[Decision Records]` | 1, `decision_records.present=true`, DRs parsed |

**Phase 1 acceptance:** all 11 pass by diff; anchors `c0e15e9f`→0 and `e1dd6b95`→exact pass; fail-open verified (exit 0 + partial output on malformed JSON / truncated block / missing path / zero-byte file); `grep -c "def extract_blocks" hooks/*.py == 1`; `audit_parse.py` has zero envelope field-names.

### Phase 2 — Validator role-awareness + os-tracker deprecation (T3 + T4 + T5)

1. `audit-block-validator.py`: add `--role-aware` (default ON) routing candidate selection through the join; `--no-role-aware` preserves the verbatim blind `scan_jsonl`.
2. `os-tracker.py`: `--hook` → warn+no-op shim; everything else untouched (R3).
3. Commit `hooks/tests/` (the 11 fixtures + expected outputs + a small runner).

**Phase 2 gating:** anti-regression — `--no-role-aware` reproduces the legacy ~22% raw count on a known transcript; `--role-aware` excludes decoys (fixtures 4 + 10 = 0); `os-tracker --diagnose` still reports healthy; full suite green.

(Phases 3–5 — deploy/backfill/release — are devops/data-analyst/qa scope per the plan, not part of this build note.)

---

## 5. Portability Assertion

**The boundary rule (restated, I1):** all Claude-Code-jsonl-shape knowledge — `type`, `message.content`, `tool_use`/`tool_result`, `tool_use_id`, `message.usage` — lives in exactly one place: `iter_receipts_from_jsonl()` inside `telemetry-extract.py`. `audit_parse.py` receives only `(text, source_tag)` and MUST never *read* envelope structure.

**Gate (redefined per architecture sign-off 2026-05-30 — tests the real invariant, not string-absence):** the original `grep` for envelope field-name *strings* was gameable (a literal could be split to dodge it) and tested the wrong thing — the output field name `JOIN_KEY = "tool_use_id"` is a legitimate provenance field, not an envelope read. The gate is now two mechanical checks in `hooks/tests/run_tests.py` (`run_portability_gate`): **(a) import-isolation** — `audit_parse.py` imports nothing from `telemetry-extract`/the validator; **(b) no envelope-reads** — no `.get("tool_use"...)`, `["tool_result"]`, `message.content/usage`, etc. accesses in `audit_parse.py`. This catches the actual violation (reading harness structure) while allowing the honest output literal. `JOIN_KEY` is therefore spelled plainly.

**How the three input modes reuse the same core:**

| Mode | Adapter | Feeds the core via |
|------|---------|--------------------|
| `--from jsonl` | `iter_receipts_from_jsonl` (the one harness knower; runs the join) | `extract_blocks` + `parse_block` on joined `tool_result`/assistant-text |
| `--from dir` | `iter_receipts_from_dir` → fans into `iter_receipts_from_jsonl` | same |
| `--from text` / `--from stdin` | `iter_receipts_from_text` (no envelope, no join) | `extract_blocks` + `parse_block` on raw text |

Because `extract_blocks` and `parse_block` never see harness shapes, a future Cursor/Copilot/Gemini-CLI adapter is a single new `iter_receipts_from_<harness>()` function that produces `RawCandidate`s — zero changes to `audit_parse.py` or the writers. That is the portability the redesign exists to deliver, and it is structurally guaranteed, not merely intended.

---

## 6. Open Items / Non-Blockers

- **None architecture-blocking.** D1/D2/D3 + R1–R9 are settled; this note operationalizes them.
- Token reconciliation (R7) is best-effort: if a harness omits `message.usage`, `measured_tokens`/`drift` are `None` and `reported` stands (I2). Not a blocker.
- `--include-no-block-fallback` (R6) and `--include-assistant-text` (R1) ship OFF; both reintroduce lossy/decoy-prone behavior and exist only as documented escape hatches.
- The extractor writing its OWN interaction/session copies (rather than calling os-tracker writers) is the deliberate R3 trade: a small amount of writer duplication buys zero-risk to the untouched `--diagnose`/`--rollup`/`--pre-inject` paths. Acceptable; revisit only if the two writers drift.

### 6.1 Phase-1 audit backlog (P2 — known, deliberately deferred, 2026-05-30)

The 2026-05-30 adversarial audit (qa-engineer + chief-architect) surfaced eight findings. A1 (dedup data loss), A2 (sensitive-skill ROI parse), A3 (pass-rate inflation), A4 (header-prose junk receipt), and A5 (BOM-drop) were FIXED in the finalize pass (see FX-5/FX-1 + the A3/A4/A5 bundle, with RED→GREEN fixtures in `tests/`). The remaining three are documented here as accepted backlog — real but low-severity, not fixed in this pass:

- **A6 — portability AST gate misses dynamic envelope reads.** `run_portability_gate` in `tests/run_tests.py` detects envelope access via literal `.get("tool_use"...)` / `["tool_result"]` / `message.content|usage|role` AST shapes. It does NOT catch indirection: `getattr(obj, "content")`, `obj.__getitem__("tool_result")`, or a variable-keyed `obj.get(k)` where `k` holds an envelope name at runtime. `audit_parse.py` is currently clean (no dynamic reads), so the gate is sound today; the gap is that a *future* edit introducing a dynamic envelope read into the leaf would pass the gate falsely. Mitigation if it ever matters: extend the AST walker to flag `getattr`/`__getitem__`/`__getattribute__` calls whose first/second arg is an envelope-name constant, and flag `.get(<Name>)` where the name is locally bound to an envelope constant. Deferred because it guards against a hypothetical future regression, not a present defect.

- **A7 — spawn_map reused-`tool_use_id` collision (last-writer-wins).** PASS 1 of `iter_receipts_from_jsonl` builds `spawn_map[tid] = {slug, prompt}`. If a single transcript reuses the SAME `tool_use_id` for two DISTINCT genuine Agent/Task spawns (should not happen in a well-formed Claude-Code log — ids are unique — but is not asserted), the second write clobbers the first, so a receipt joined on that id may be mis-attributed to the wrong agent slug. Impact is attribution-only (the receipt is still captured; only its `agent_slug` can be wrong) and requires a malformed/adversarial transcript to trigger. Mitigation if needed: detect a pre-existing key in PASS 1 and emit a collision warning (and/or keep a list per id, attributing by proximity). Deferred — depends on a transcript pathology we have not observed.

- **A8 — validator blind `scan_jsonl` anti-regression framing.** The `--no-role-aware` blind scan (and the anti-regression count it anchors) reproduces the legacy "any line containing the header" behavior. That blind count is a meaningful anti-regression anchor ONLY for assistant-text-style emissions, where a line-scan and the role-aware join genuinely diverge. For `tool_result`-carried receipts the blind scan's over-count is an artifact of prose decoys, not a stable property, so the blind-vs-role-aware delta should be read as "assistant-text decoy rejection demonstrated," not as a universal pass-rate. This is a framing/interpretation note, not a code defect — the `AR_anti_regression.jsonl` fixture is built specifically with assistant-text decoys, which is the case where the framing holds. Deferred as documentation only.
