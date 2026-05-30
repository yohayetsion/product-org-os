# Product Org OS — Agent Integration Guide

## Version

v2.0 — portable, manual-run telemetry (compatible with `telemetry-extract.py` and `os-tracker.py` v1.2.x utilities).

---

## What This Is

Product Org OS agents emit a structured **Spawn Audit Block** ("the receipt") at the top of every spawn response. The receipt reports, in-band, what the agent loaded, any decision records it touched, and its ROI. This guide tells you how to turn those in-band receipts into persistent telemetry (ROI logs, interaction logs, decision-record events).

**Capture is portable and manual by design.** You run a one-line command against your transcripts whenever you want telemetry refreshed. There is no background hook, no daemon, and no harness lock-in.

> **The PostToolUse hook is NOT required and NOT used.** Earlier versions wired capture to Claude Code's `PostToolUse` event. That approach was Claude-Code-only and re-derived numbers the agent already reported. The current design reads the agent's in-band receipt directly, so it works on a transcript from any tool that produces one.

---

## The Telemetry Extractor (primary tool)

**Location**: `hooks/telemetry-extract.py` (relative to the repo root)

**Requirements**: Python 3.8+ (stdlib only — no pip dependencies)

**Convenience runners** (zero hardcoded paths; resolve relative to themselves):

```bash
# macOS / Linux
hooks/run-telemetry.sh   --from dir --path <path-to-your-transcripts> --context-dir <path-to-context>

# Windows
hooks\run-telemetry.cmd  --from dir --path <path-to-your-transcripts> --context-dir <path-to-context>
```

Both runners simply forward all arguments to `python hooks/telemetry-extract.py`.

### How It Works

The extractor reads transcripts, finds genuine agent-spawn receipts via a structural `tool_use → tool_result` join (not a text scan, so decoy "Audit Block" mentions inside `Read`/`Bash` output are excluded), parses each receipt's self-reported numbers verbatim, and writes telemetry. The agent's reported ROI/loads/decision-records are the source of truth — the extractor does not re-derive them.

### Input Modes (`--from`)

Telemetry is **harness-agnostic**: all Claude-Code-specific transcript-shape knowledge is isolated in one adapter, so the same core parses any of these inputs.

| Mode | Use it for | Example |
|------|-----------|---------|
| `jsonl` (default) | A single Claude Code `.jsonl` transcript | `--from jsonl --path <one-transcript.jsonl>` |
| `dir` | A directory of transcripts (add `--recursive` to descend) | `--from dir --path <path-to-your-transcripts>` |
| `text` | A plain-text transcript from any other tool | `--from text --path <transcript.txt>` |
| `stdin` | Pipe a transcript in | `cat transcript.txt \| python hooks/telemetry-extract.py --from stdin` |

A future Cursor / Copilot / Gemini-CLI adapter is a single new input function; the parsing core does not change.

### Common Invocations

```bash
# Refresh telemetry from all transcripts (most common)
python hooks/telemetry-extract.py --from dir --recursive \
  --path <path-to-your-transcripts> --context-dir <path-to-context>

# Dry run — print a JSON summary, write nothing (always safe to run first)
python hooks/telemetry-extract.py --from dir --recursive \
  --path <path-to-your-transcripts> --summary

# Single transcript into a local context dir
python hooks/telemetry-extract.py --from jsonl \
  --path <one-transcript.jsonl> --context-dir ./context
```

On Claude Code, transcripts live under `~/.claude/projects/<project>/`. On other tools, point `--path` at wherever that tool writes its session logs.

### `--summary` (recommended first run)

`--summary` prints a machine-readable JSON report and writes nothing:

```json
{ "spawns": 213, "receipts": 207, "v1_legacy_count": 0, "v2_pass_rate": 0.94,
  "value_usd": 4200, "implausible": [], "by_source": {"tool_result": 207} }
```

- `spawns` — genuine `Agent`/`Task` spawns found
- `receipts` — audit blocks captured
- `v1_legacy_count` — receipts in the deprecated `Pre-Execution Self-Check` format (surfaces stale injection templates)
- `v2_pass_rate` — fraction of current-format receipts passing schema validation
- `implausible` — receipts flagged by sanity checks (e.g. a Value with no Time-saved)

Run `--summary` before any write to see the counts first.

### Flags

| Flag | Default | Effect |
|------|---------|--------|
| `--from {jsonl,text,stdin,dir}` | `jsonl` | Input mode |
| `--path PATH` | — | File or directory to read |
| `--context-dir DIR` | — | Where telemetry is written (omit with `--summary`) |
| `--summary` | off | Print JSON report, write nothing |
| `--recursive` | off | `dir` mode: descend into subdirectories |
| `--include-assistant-text` | off | Also accept assistant-text receipts (gated; inline personas emit no block, so yield ≈ 0) |
| `--include-no-block-fallback` | off | Reserved escape hatch (no-op) |

### What It Writes

| What | Where | Method |
|------|-------|--------|
| Canonical receipts | `context/roi/audit-receipts.jsonl` | Append-only (system of record) |
| ROI rows | `context/roi/session-log.md` | Append-only (projection of the jsonl) |
| Interactions | `context/interactions/YYYY/YYYY-MM-DD.md` + `current-session.md` | Append / overwrite |
| Decision-record events | `context/decisions/index.md` | Append-only |

### Design Principles

- **Portable**: harness-specific transcript knowledge is isolated in one adapter; the parser is plain text → data.
- **Parse, don't re-derive**: the agent's self-reported numbers are authoritative.
- **Fail-open**: bad JSON lines / truncated blocks are skipped; the run never aborts (exit 0).
- **Idempotent**: dedup by `tool_use_id` (block-hash fallback). Re-running is a no-op.
- **Stdlib only**: Python 3.8+, no pip install.

---

## Optional: Run It On A Schedule

Capture is manual by design, but if you want it to refresh automatically you can wrap the runner in your OS scheduler. This is entirely optional.

**cron (macOS / Linux)** — refresh hourly:

```cron
0 * * * * /path/to/product-org-os/hooks/run-telemetry.sh --from dir --recursive --path <path-to-your-transcripts> --context-dir <path-to-context>
```

**Task Scheduler (Windows)** — create a Basic Task that runs:

```
C:\path\to\product-org-os\hooks\run-telemetry.cmd --from dir --recursive --path <path-to-your-transcripts> --context-dir <path-to-context>
```

There is no PostToolUse hook to configure, and none is needed.

---

## Validating Receipts

`hooks/audit-block-validator.py` checks that emitted audit blocks conform to the schema. By default it is `--role-aware`: it scores only genuine spawn receipts (selected by the same structural join the extractor uses), not decoy "Audit Block" mentions in tool output.

```bash
# Validate genuine receipts in a transcript (default: role-aware)
python hooks/audit-block-validator.py <path-to-transcript-or-dir>

# Reproduce the legacy raw scan (counts every "Audit Block" string)
python hooks/audit-block-validator.py <path> --no-role-aware
```

---

## Decision-Record Index Maintenance (`os-tracker.py`)

`hooks/os-tracker.py` retains its context-maintenance utilities:

```bash
# Surface related context before spawning a deliverable-producing agent
python hooks/os-tracker.py --pre-inject "<topic>" --context-dir <path-to-context>

# Health check
python hooks/os-tracker.py --diagnose --context-dir <path-to-context>

# Rebuild decision-record / index files from markdown source
python hooks/os-tracker.py --diagnose --repair --context-dir <path-to-context>
```

> `os-tracker.py --hook` is **deprecated** (warn-and-no-op). Per the portable design there is no PostToolUse event to feed it. Use `telemetry-extract.py` for capture.

---

## Tests

A golden-fixture suite covers the extractor and the structural join (including the decoy-rejection and idempotency anchors):

```bash
python hooks/tests/run_tests.py
```

Fixtures under `hooks/tests/fixtures/` are synthetic, hand-built transcripts — they contain no real session data.

---

## ROI Baselines

The extractor reads the agent's self-reported ROI verbatim and does not re-derive it. `hooks/baselines.json` is retained for `os-tracker.py`'s utilities and for the opt-in no-block fallback only.

---

## Context Layer Architecture

The OS has two context layers:

### Telemetry Layer (`telemetry-extract.py`)

Captures in-band agent receipts into ROI / interaction / decision-record telemetry. Manual, portable, run on demand.

### Explicit Layer (Skills / User Commands)

User-initiated knowledge management:

| Skill | Purpose |
|-------|---------|
| `/context-save` | Save decisions, bets, learnings, conventions |
| `/context-recall` | Deep query with synthesis |
| `/feedback-capture` | Structured feedback with metadata |
| `/feedback-recall` | Feedback query with theme analysis |
| `/interaction-recall` | Past conversation search |
| `/relevant-learnings` | Surface applicable lessons |
| `/handoff` | Session context transfer |
| `/index-folder` | Bulk-index a folder for retrieval |

---

## For Framework Contributors

### Adding a new skill/agent to baselines

1. Add the entry to `reference/roi-baselines.md` (human-readable)
2. Add the corresponding entry to `hooks/baselines.json` (machine-readable)
3. Keep both in sync.

### Adding a new harness adapter

All transcript-shape knowledge lives in `telemetry-extract.py`'s input adapters; the parsing core (`audit_parse.py`) sees only plain text. To support a new tool, add one `iter_receipts_from_<harness>()` function that yields candidates — no changes to the parser or writers are needed.
