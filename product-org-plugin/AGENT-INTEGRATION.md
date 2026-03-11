# Product Org OS — Agent Integration Guide

## Version

v1.2 — compatible with os-tracker.py v1.2.x

---

## What This Is

The Product Org OS tracks context (ROI, interactions, documents, cross-references) after agent work. This file tells any coding agent how to make tracking automatic.

**Problem**: ~7 "MANDATORY" post-agent operations exist in the OS rules (ROI logging, interaction logging, document registration, cross-references, session summary, feedback detection). All are prompt-dependent and almost none actually happen in practice.

**Solution**: `hooks/os-tracker.py` — a standalone CLI tool that handles all post-agent processing in one call.

---

## The Tracker CLI

**Location**: `hooks/os-tracker.py` (relative to this file)

**Requirements**: Python 3.8+ (stdlib only — no pip dependencies)

### Modes

```bash
# Hook mode — reads stdin JSON (Claude Code PostToolUse)
python hooks/os-tracker.py --hook

# Manual mode — explicit agent/skill invocation
python hooks/os-tracker.py --agent product-manager --skill prd --context-dir ./context

# Pre-inject mode — get related context before spawning an agent
python hooks/os-tracker.py --pre-inject "pricing strategy" --context-dir ./context

# Rollup mode — session-end summary
python hooks/os-tracker.py --rollup --context-dir ./context

# Diagnose mode — health check
python hooks/os-tracker.py --diagnose --context-dir ./context

# Diagnose + repair — rebuild indexes from markdown source
python hooks/os-tracker.py --diagnose --repair --context-dir ./context
```

### What It Tracks

| What | Where | Method |
|------|-------|--------|
| ROI (time saved) | `context/roi/session-log.md` | Append-only |
| Interactions | `context/interactions/YYYY/YYYY-MM-DD.md` | Append-only |
| Documents | `context/documents/registry.md` | Append-only |
| Session summary | `context/interactions/current-session.md` | Overwrite |
| Cross-references | Detected at query time | Not written on every call |
| JSON indexes | Rebuilt from markdown source | Via `--diagnose --repair` |

### When to Call (Post-Agent)

**Call after**: Agent spawns that produce deliverables, gateway sessions with synthesis, skills that create/update documents.

**Skip for**: Simple Q&A, context/feedback recalls, system ops (`/setup`), quick lookups, explanations.

**Rule of thumb**: "Did an agent do meaningful work that should be remembered?" YES = call tracker. NO = skip.

### When to Call (Pre-Agent)

**Call before**: Spawning any agent that will produce a deliverable. This gives the agent awareness of related decisions, feedback, and active bets.

**Skip for**: Simple Q&A, context recalls, system ops.

**Rule of thumb**: "Will this agent produce a deliverable that should account for past decisions?" YES = pre-inject. NO = skip.

### Design Principles

- **Local-first writes**: Append-only markdown files (fast, safe). JSON indexes rebuilt on demand.
- **Fail-open**: On ANY error, exits 0 silently. Never blocks the coding agent.
- **Idempotent**: Uses `tool_use_id` for dedup. Safe to call twice.
- **Standalone**: Python 3.8+ stdlib only. No pip install needed.

---

## Platform Integration

### Claude Code (Recommended)

PostToolUse hook — configured automatically by `/setup`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Agent",
        "hooks": [
          {
            "type": "command",
            "command": "python hooks/os-tracker.py --hook",
            "timeout": 10000
          }
        ]
      }
    ]
  }
}
```

The hook receives `tool_input` and `tool_response` on stdin as JSON. It extracts agent identity, determines if meaningful work was done, and logs accordingly.

**Agent identity convention**: When spawning agents, include the agent ID in the description field: `[product-manager] Review the PRD for authentication`. This gives the hook a structured way to identify the agent. Falls back to parsing the prompt body for the `You are **{emoji} {Display Name}**` pattern.

### Cursor

Add to `.cursorrules`:

```
Before delegating complex work or starting a new product deliverable, run:
python hooks/os-tracker.py --pre-inject "[topic keywords]" --context-dir ./context
Include the output (if any) as context for the task.

After completing agent work that produces a deliverable, run:
python hooks/os-tracker.py --agent [agent-id] --context-dir ./context
```

### Windsurf / Copilot / Other Agents

Add to your agent's system prompt or rules file:

```
Before producing product deliverables, query organizational context:
python [path-to-plugin]/hooks/os-tracker.py --pre-inject "[topic]" --context-dir ./context
If results are returned, honor existing decisions and incorporate feedback.

After agent tasks that produce documents, run:
python [path-to-plugin]/hooks/os-tracker.py --agent [agent-id] --context-dir ./context
```

Replace `[path-to-plugin]` with the actual path to the Product Org OS plugin directory.

---

## Self-Diagnosis

### On Session Start

```bash
python hooks/os-tracker.py --diagnose --context-dir ./context
```

Outputs one of:
- `healthy` — all context files exist, tracking is operational
- `broken: [reason] — fix: [action]` — specific issue with fix instructions

### During Operation

If a write fails, the tracker enters silent mode. It will never block your workflow. Check stderr for debug info (only visible with `--verbose`).

### If Tracking Isn't Working

1. Run `--diagnose` to identify the issue
2. Run `--diagnose --repair` to rebuild indexes from markdown source files
3. Common fixes:
   - Run `/setup` to create missing context directories
   - Ensure Python 3.8+ is available: `python --version`
   - Check file permissions on the context directory
   - For Claude Code: verify hooks in `.claude/settings.json`

### Circuit Breaker

If 3+ consecutive write failures occur in a session, the tracker disables itself for the remainder of the session. This prevents repeated slow failures from degrading performance. The next session starts fresh.

---

## Smoke Test

```bash
# Test pre-inject (should return context or empty if no data yet)
python hooks/os-tracker.py --pre-inject "pricing" --context-dir ./context

# Test manual post-agent tracking
python hooks/os-tracker.py --agent product-manager --context-dir ./context

# Verify it worked
tail -1 context/roi/session-log.md

# Test diagnose
python hooks/os-tracker.py --diagnose --context-dir ./context
```

---

## ROI Baselines

The tracker uses `hooks/baselines.json` for ROI calculations. This file is compiled from `reference/roi-baselines.md` and contains base times for all skills, agents, and gateways.

Complexity is auto-detected from response length:
- < 1000 chars: Simple (0.5x)
- 1000-3000 chars: Standard (1.0x)
- 3000-8000 chars: Complex (1.5x)
- > 8000 chars: Enterprise (2.0x)

---

## Context Layer Architecture

The OS has two context layers that work together:

### Automatic Layer (os-tracker.py)

Handles background tracking with zero user action when hooks are configured:

- **Pre-inject** (`--pre-inject`): Scans context/ before agent work, surfaces related decisions, bets, feedback, learnings, and conventions
- **Post-track** (`--hook` / `--agent`): Logs ROI, interactions, documents, session summary after agent work
- **Self-heal** (`--diagnose --repair`): Rebuilds stale indexes from markdown source files

### Explicit Layer (Skills / User Commands)

User-initiated knowledge management operations:

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| `/context-save` | Save decisions, bets, learnings, conventions | After creating strategic documents |
| `/context-recall` | Deep query with synthesis + recommendations | "What did we decide about pricing?" |
| `/feedback-capture` | Structured feedback with metadata + sentiment | When encountering customer feedback |
| `/feedback-recall` | Feedback query with theme analysis | Before decisions in an area |
| `/interaction-recall` | Past conversation search by agent/date/topic | "What did @pm say last week?" |
| `/relevant-learnings` | Surface applicable lessons from past work | Before starting work in a familiar area |
| `/handoff` | Session context transfer between agents | When delegating work |
| `/index-folder` | Bulk-index a folder for retrieval | Cataloging existing documents |

**The division**: Automatic handles what should always happen (tracking). Explicit handles what requires user intent (saving knowledge, querying deeply).

### Conventions / Preferences

Organizational norms stored in `context/preferences/conventions.md` are always included in pre-inject output — no keyword matching needed. Save conventions with `/context-save` using type "preference".

---

## For Plugin Developers

### Adding a new skill/agent to baselines

1. Add the entry to `reference/roi-baselines.md` (human-readable)
2. Add the corresponding entry to `hooks/baselines.json` (machine-readable)
3. Both files must stay in sync

### Extending the tracker

The tracker pipeline is: Parse Input > ROI Calculation > ROI Log > Interaction Log > Session Summary > Document Detection. Each step is independently try/except'd. Add new steps by adding a new function call in the pipeline — it will fail-open automatically.
