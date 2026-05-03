---
name: cadence-adherence-telemetry
description: 'Surface Principle 8 cadence-stack adherence: which decisions, bets, portfolio reviews, handoffs, and learning logs are overdue against the four-layer cadence stack. Activate when: "cadence check", "what is overdue", "cadence telemetry", "cadence adherence", "weekly cadence sweep", "what reviews am I behind on", "principle 8 sensing", "decision rot check", "are we on rhythm". Do NOT activate for: a single bet checkpoint (/bet-invalidation-checkpoint), a single decision review (/outcome-review), or the maturity diagnostic (/maturity-check) — this skill is the upstream sensor those consumers read.'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: cadence
  skill_type: task-capability
  owner: product-operations
  primary_consumers:
    - product-operations
    - vp-product
    - cpo
  secondary_consumers:
    - maturity-check
  sensitive: false
---

## Purpose

The cadence-adherence-telemetry skill is the user-facing sensor for Principle 8 ("Organizations Learn Through Outcomes"). It walks the `context/` tree, identifies cadence-stack records that have aged past their threshold or are missing entirely, and surfaces them as a ranked, actionable report. The point is not bookkeeping. It is the early warning system that keeps strategic bets, decisions, and portfolio reviews from rotting in place. Decisions that aged past 90 days with no outcome review compound silently into decision debt — this skill makes that visible while there is still time to act on it.

This skill is the user-facing wrapper around `cadence_check.scan()` (V5.1-30, internal module). The scan itself is read-only and never mutates `context/`; this skill renders the scan output as markdown, persists the report to `context/telemetry/` for audit trail, and surfaces it to the user.

## When to invoke

- **Weekly sensing cadence (default)** — invoke once per week as a Principle 8 health check. The report fits on one screen and reads in 30 seconds.
- **Before strategic decisions** — invoke before any portfolio tradeoff, new strategic bet, or major commitment, so prior-decision rot is on the table when the new commitment is being made.
- **Before /maturity-check** — `/maturity-check` (V5.1-26/27/28 rewrite) reads the cadence dimension from this scan as input to the Three Tiers diagnostic. Run cadence-adherence first so the maturity assessment has the freshest signal.
- **On suspicion** — invoke whenever you suspect a project has gone dormant, a bet thesis is being run on momentum rather than evidence, or you've been off the system for a stretch and need to see what aged while you were away.

## What it does (data flow)

1. Reads `context/preferences/conventions.md` for any threshold overrides under the `cadence_thresholds:` key. Assembles them as a parameter dict.
2. Calls `cadence_check.scan(context_root, today=None, threshold_overrides={...})` (the V5.1-30 module). The scan walks five subdirectories — `decisions/`, `bets/`, `portfolio/`, `handoffs/`, `learnings/` — plus cross-references against `context/index.json`. Returns a `CadenceFindings` object.
3. Sorts findings by severity (P0 → P1 → P2) then by signal-type display order (outcome_review_missing first, then decision_review_missing, then portfolio, bet, handoff, learning) then by `age_days` descending so the oldest at each tier surfaces first.
4. Renders the `CadenceFindings` object as a markdown report using the `render_cadence_report.py` helper module (alongside this SKILL.md). The helper attaches a `Suggested next step` per finding so the report is actionable, not just diagnostic.
5. Persists the report to `context/telemetry/cadence-adherence-{YYYY-MM-DD}.md`. One file per scan day. If a report for today already exists, overwrite (the scan is deterministic for a given context state).
6. Surfaces the report path to the user. Does NOT auto-open or auto-present — this is a sensing report, not a deliverable.

## Invocation pattern (for agents reading this skill)

The Python invocation runs the scanner and renderer end-to-end. The `cadence-check/` and `cadence-adherence-telemetry/` skill folders both live under `skills/` in the OS root, so adding both to `sys.path` exposes the modules as flat imports:

```bash
cd C:/dev/product-org-os
python - <<'PY'
import sys
from pathlib import Path
from datetime import date

sys.path.insert(0, "skills/cadence-check")
sys.path.insert(0, "skills/cadence-adherence-telemetry")

import cadence_check
import render_cadence_report

# Threshold overrides: read from context/preferences/conventions.md if present.
# Schema (YAML-ish):
#   cadence_thresholds:
#     bet_review_overdue: 60       # override default 30d
#     portfolio_review_overdue: 120 # override default 90d
overrides = None  # or a dict like {"bet_review_overdue": 60}

today = date.today()
findings = cadence_check.scan(Path("context"), today=today, threshold_overrides=overrides)
report_md = render_cadence_report.render(findings, today=today)

out_path = Path(f"context/telemetry/cadence-adherence-{today.isoformat()}.md")
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(report_md, encoding="utf-8")

print(f"Report persisted to: {out_path}")
print(f"Total findings: {findings.summary['total']}")
print(f"By severity: {findings.summary['by_severity']}")
PY
```

After persistence, surface the report path to the user with a brief one-paragraph summary (total findings, breakdown by severity, top P0 if any).

## Output shape

The persisted report follows this structure:

```markdown
# Cadence Adherence Telemetry — {YYYY-MM-DD}

Principle 8 cadence-stack adherence scan. Surfaces overdue items across the
four-layer cadence stack (portfolio review, bet review, decision T+30 /
outcome T+60, handoff freshness, learning log activity).

## Summary

**Scan date**: {today}
**Scan timestamp (UTC)**: {ISO timestamp}
**Scan duration**: {N}ms
**Total findings**: {N}

**By severity**:
- P0: {count}
- P1: {count}
- P2: {count}

**By signal type**:
- outcome_review_missing: {count}
- decision_review_missing: {count}
- ...

**Scan health**: clean | (degraded-signal flags listed if any)

## Findings

### P0 — Blocker (decision rotted in place)

#### [P0] outcome_review_missing

- **Target**: `DR-YYYY-NNN`
- **Age**: {N}d (threshold: {N}d)
- **Detail**: {human_readable from cadence_check}
- **Suggested next step**: {action — e.g. "Run /outcome-review against this decision..."}

### P1 — Important (over threshold)

#### [P1] bet_review_overdue
...

### P2 — Notice (within 20% of threshold)
...
```

Findings are grouped by severity tier, then by signal-type display order within each tier, then by age descending. If there are zero findings, the report says so explicitly — empty result is itself a positive signal.

## Threshold overrides

Yohay (or the OS owner in any installation) can override the default cadence thresholds per signal in `context/preferences/conventions.md`. The defaults from H.5 spec §4 are:

| Signal | Default threshold |
|---|---|
| `portfolio_review_overdue` | 90 days |
| `bet_review_overdue` | 30 days |
| `decision_review_missing` | 30 days |
| `outcome_review_missing` | 60 days |
| `handoff_stale` | 7 days |
| `learning_log_dormant` | 60 days |

To override, add a `cadence_thresholds:` block to `conventions.md`. Example:

```yaml
cadence_thresholds:
  bet_review_overdue: 60        # slow-moving research bets review monthly is too aggressive
  portfolio_review_overdue: 120 # quarterly is the right portfolio cadence here
```

Overrides are per-signal-type (not per-record). If a single bet needs a different cadence from the rest of the portfolio, document that on the bet record itself; do not encode it in conventions.

## Failure modes

`cadence_check.scan()` (V5.1-30) is engineered to degrade gracefully and never raise on partial data. This skill inherits that behavior:

- **`context/` missing**: surfaces as a single P1 finding ("context layer not initialized — run /setup"). Report still renders.
- **A subdirectory empty**: no findings for that slice; `scan_metadata.empty_directories` records it. Surfaced under "Scan health" if present.
- **`context/index.json` missing or malformed**: cross-reference check (T+30 / T+60 outcome links) falls back to body-text search across `context/learnings/`. The "Scan health" section flags `index_unavailable: true` so the reader knows the cross-ref signal is degraded.
- **A record can't be parsed** (no date, no Status): logged to `scan_metadata.parse_failures`, aggregated into a single P2 "parse_failures" finding pointing the reviewer at the metadata block.
- **Permission error on a subdirectory**: logged + skipped + surfaced as a P2 "permission_error" finding. Scan completes for what it could read.

The skill never throws. If something is wrong with the scan, the report says what's wrong — degraded data is itself actionable signal.

## R-018 attestation

V5.1-31 is a NEW skill cell. It introduces:
- One new skill folder: `skills/cadence-adherence-telemetry/`
- Two new files: `SKILL.md` (this file) + `render_cadence_report.py` (rendering helper)
- One new context subdirectory: `context/telemetry/`

It touches zero v5.0 surface. It only READS from `context/` (via `cadence_check.scan()`) and WRITES only to `context/telemetry/` (a new subdirectory not present in v5.0). No v5.0 skill is amended. No v5.0 schema is changed. v5.0.0 stays tag-ready.

R-018 holds.

## Invocation example

```
> /cadence-adherence-telemetry

⚙️ Product Operations: Scanned the cadence stack against
context/. 9 P1 findings surfaced — 3 decisions past T+30 with no
review link, 3 decisions past T+60 with no outcome review, 2 active
bets past 30d without a Status update, and a stale handoff at 11d.
No P0 (no decisions yet rotted past 90d). Persisted to
context/telemetry/cadence-adherence-2026-05-03.md. The two oldest
items: SB-2026-003 (45d) and DR-2026-014 (62d, T+60 missing) — want
to walk through them?
```

## Cross-references

- **Upstream**: `cadence_check` (V5.1-30, internal module) — the read-only scanner this skill consumes. Stable contract per H.5 spec §3.
- **Consumer**: `/maturity-check` (V5.1-26/27/28 rewrite) — reads P0/P1 counts from this telemetry as input to the Three Tiers cadence dimension.
- **Adjacent**: `/portfolio-status` (acts on portfolio_review_overdue findings), `/bet-invalidation-checkpoint` (acts on bet_review_overdue), `/outcome-review` (acts on outcome_review_missing), `/handoff` (acts on handoff_stale), `/context-save` (acts on learning_log_dormant).
- **Future**: `/observability-telemetry` (V5.2-S09) extends this skill into a richer 5-signal envelope. Wrapping is additive — V5.1-31's contract stays stable through the v5.2 transition.
