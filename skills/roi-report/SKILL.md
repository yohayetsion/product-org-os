---
name: roi-report
description: 'View the computed workforce-hours report (hours only, never self-reported). Activate when: "show ROI", "hours delivered", "workforce hours", "productivity report", telemetry report, savings dashboard Do NOT activate
  for: portfolio status overview (/portfolio-status), business case ROI analysis (/business-case), value realization for customers (/value-realization-report)'
model: haiku
allowed-tools:
- Read
- Glob
user-invocable: true
metadata:
  author: Product Org OS
  category: context-layer
  skill_type: task-capability
---
# ROI Report

Report the **computed** hours the workforce delivered. Hours are produced by the telemetry
pipeline from the owner-affirmed activity table — never from anything an agent said about
its own work.

**SCOPE**: hours represent PRODUCT / KNOWLEDGE WORK (strategy, decisions, requirements, GTM,
analysis, documentation), NOT software development effort.

## The model (read this before reporting anything)

Per `rules/roi-display.md` and `rules/agent-spawn-protocol.md` §3 (hours-only switch,
2026-08-01):

- **Computed, not self-reported.** Agents emit no `[Post-Execution ROI]` section. Hours come
  from `tools/hooks/baselines.json` → `agents` rows (one owner-affirmed `baseMinutes` time basis per
  agent seat), resolved per canonical agent slug against the receipts store.
- **No fallback.** The `_default` row is refused by the resolution chain. A spawn whose
  canonical slug has no affirmed row is **counted, not priced**: shown with its spawn count,
  contributing zero hours, labelled "no time basis yet" — never `0 hrs` styled as a
  measurement, never an estimate.
- **Hours only.** No dollar figure, no rate table, no $/hr anywhere. Do not compute one, do
  not infer one, do not accept one from a legacy record.
- **Coverage is mandatory.** State priced spawns / total receipts wherever hours appear.
- **Sensitive seats.** Where hours for legal / HR / compliance / privacy seats are displayed,
  the framing stays "drafting and triage" per `roi-display.md` — never "review."

## Trigger Patterns

- `/roi-report` — full computed report
- `/roi-report [period]` — specific window (30d, 90d, month, quarter)

## Behavior

### 1. Load data

```
Receipts store:  context/roi/audit-receipts.jsonl   (appended by hooks/telemetry-extract.py)
Activity table:  tools/hooks/baselines.json               (agents rows; owner-affirmed)
Dashboard data:  the operator dashboard output configured for this install
                 (local default: telemetry-private\)
```

If a dashboard build exists, report from it — it is the same computation, already run. Only
fall back to reading the receipts store directly when no dashboard output is available.

**Legacy**: `context/roi/session-log.md` and any archived block carrying `[Post-Execution ROI]`
are tolerated-but-ignored history. Do NOT read them into this report, and never mix a
self-reported minute or a legacy dollar value into a computed figure.

### 2. Compute

For each receipt: resolve the canonical agent slug (alias map merges; identity for unmapped
slugs) → look up the affirmed `baseMinutes` → sum. Spawns with no affirmed row are counted
and listed unpriced. No multipliers, no complexity factors — those retired with the switch.

### 3. Output Format

```markdown
# Product Org OS — Workforce Hours (computed)

**Report Generated**: [date]
**Period**: [session | 30 days | 90 days | all time]

| Metric | Value |
|--------|-------|
| Receipts in window | [N] |
| Priced spawns | [P] |
| Coverage | [P/N] ([pct]%) |
| Hours (computed) | ~[X] |

## By agent seat

| Agent | Spawns | Hours (computed) | Basis |
|-------|--------|------------------|-------|
| product-manager | 12 | ~[X] | affirmed |
| @some-agent | 4 | — | no time basis yet (counted, not priced) |

## Counted, not priced

[List every slug with no affirmed row + its spawn count. This list is the input to the
owner's affirmation queue — never hide it, never estimate it away.]
```

### 4. Empty state

```markdown
# Product Org OS — Workforce Hours (computed)

**No receipts recorded yet.**

Receipts are written per spawn by the telemetry pipeline. Once spawns exist, hours appear
here for every seat with an owner-affirmed row in the activity table.
```

## Notes

- Hours are a **display** concern. This skill reports; it never asks an agent what it was worth.
- If the activity table has no affirmed row for a seat, the fix is an owner affirmation — not
  a default, not an estimate.
- All figures are computed approximations of manual product/knowledge work, not development effort.
