# Agent Context Tracking

Context tracking has two halves: **pre-inject** (before spawning) and **post-track** (after completion). Both are handled by `hooks/os-tracker.py`.

---

## Pre-Inject: Context Before Agents

Before spawning a deliverable-producing agent, inject related context:

```bash
python hooks/os-tracker.py --pre-inject "[topic keywords]" --context-dir ./context
```

If output is non-empty, prepend it to the agent's prompt. This gives the agent awareness of related decisions, feedback, active bets, and organizational conventions without relying on the agent to run `/context-recall` itself.

Pre-inject always includes `context/preferences/conventions.md` (if it exists) regardless of topic keywords.

See `agent-spawn-protocol.md` Section 7 for the full spawn flow.

## Post-Track: Logging After Agents

### If hooks are configured (Claude Code)

Post-agent tracking is automatic via PostToolUse hook. No manual action needed.

### If hooks are NOT configured

After agent tasks that produce deliverables, run:

```bash
python [plugin-path]/hooks/os-tracker.py --agent [agent-id] --context-dir ./context
```

## What counts as "meaningful"

**Pre-inject + post-track for**: Agent spawns with deliverables, gateway sessions, skills producing documents.

**Skip for**: Q&A, context recalls, system ops, lookups.

## Data Flow

- Markdown files are source of truth (append-only)
- JSON indexes are rebuilt from source on demand (`--diagnose --repair`)
- Cross-references detected at query time, not write time
- ROI calculated from `hooks/baselines.json`

## Self-Diagnosis

```bash
python hooks/os-tracker.py --diagnose --context-dir ./context          # check health
python hooks/os-tracker.py --diagnose --repair --context-dir ./context  # fix issues
```

## Full Integration Guide

See `AGENT-INTEGRATION.md` in the plugin root.

---

## Vision to Value Operating Principle

> "Reliable tracking requires automation, not discipline. The system should track context without depending on prompt compliance."
