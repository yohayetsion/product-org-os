---
name: continuation-threshold
description: 'Evaluate a strategic bet against its Continuation Threshold — the affirmative, signal-driven gate that a bet must clear before committing more capital at the next major checkpoint. Produces a structured pass / fail / reopen verdict with reasoning. Activate when: "continuation threshold", "should we keep funding this bet", "does this bet still hold", "evaluate the bet at the gate", "next-stage commitment check", "is the threshold met". Do NOT activate for: T+6 / T+12 invalidation review (/bet-invalidation-checkpoint), commitment readiness before initial commit (/commitment-check), portfolio-level tradeoffs (/portfolio-tradeoff), formulating a new bet (/strategic-bet), the upstream business case that DEFINES the threshold (/business-case).'
argument-hint: '[SB-YYYY-NNN bet ID] or [update path/to/threshold-evaluation.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: strategy
  skill_type: task-capability
  owner: bizops
  sensitive: false
  primary_consumers:
  - bizops
  - vp-product
  - cpo
  secondary_consumers:
  - pm-dir
  - director-product-management
  - value-realization
  - prodops
  - product-operations
  - cfo
  - finance-dir
---
## Purpose

The Continuation Threshold is the affirmative gate a strategic bet must clear before the organization commits more capital at the next major checkpoint. It is the inverse of an invalidation criterion: invalidation says "stop if this fires"; the Continuation Threshold says "continue only if this holds." If the threshold is not met, the default action is to reopen the decision and route the bet back to portfolio review — not to silently continue under the original commitment.

This skill walks the user through evaluating a specific strategic bet against its Continuation Threshold at a specific point in time, and produces a structured pass / fail / reopen verdict. The threshold itself is DEFINED upstream in the bet's business case (`/business-case`); this skill EVALUATES whether the threshold is met when the gate fires.

## Vision to Value Phase

**Phase 2 → Phase 3 gate** — the Continuation Threshold is the canonical evaluation that determines whether a strategic bet is permitted to advance from Strategic Decisions into Commitment. The downstream `/phase-check` skill consumes this skill's output to hard-gate the Phase 2 → Phase 3 transition: a Phase 3 advance is not authorized unless a current Continuation Threshold evaluation returns `pass`.

**Prerequisites**: A formulated strategic bet (`/strategic-bet`) with named re-decision triggers; a business case (`/business-case`) that defines the bet's continuation_threshold field with specific, signal-driven criteria; the bet has reached a major checkpoint where additional capital commitment is being considered.

**Consumed by**: `/phase-check` (uses the verdict to hard-gate Phase 2 → Phase 3); `/portfolio-status` (rolls up threshold-evaluation outcomes across the portfolio); `/bet-invalidation-checkpoint` (is informed by, but distinct from, threshold evaluation — invalidation tests "should this bet die?"; threshold tests "should this bet advance?").

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh the threshold check" + path | UPDATE | 100% |
| File path provided (`@path/to/threshold-evaluation.md`) | UPDATE | 100% |
| "create", "new", "evaluate the threshold" | CREATE | 100% |
| "find", "list threshold evaluations" | FIND | 100% |
| Bet ID + gate-firing context ("the bet is up for renewal", "Q4 review window") | CREATE | 90% |
| Just a bet ID with no gate-firing context | ASK | — |

**Threshold**: greater-or-equal 85% auto-proceed | 70-84% state assumption | <70% ask user.

### Mode Behaviors

**CREATE**:
1. Resolve the strategic bet (`SB-YYYY-NNN`) from `context/bets/index.md` and `context/bets/[YYYY]/`
2. Read the business case bound to the bet and extract its `continuation_threshold` field
3. Pull the bet's named re-decision triggers from the strategic-bet record and from `context/assumptions/registry.md`
4. Read the most recent prior threshold evaluation (if any) so the trajectory is visible
5. Walk the user through each criterion in the threshold and the firing state of each named re-decision trigger
6. Produce the verdict — pass / fail / reopen — with explicit reasoning per criterion
7. The verdict is the artifact; an evaluation without a verdict is incomplete and must not be filed

**UPDATE**:
1. Read existing evaluation
2. Preserve the verdict, criterion findings, and rationale already recorded
3. Update late-arriving data (e.g., a metric that finalized after the evaluation date)
4. If the verdict itself is changing, that is a NEW evaluation, not an update — create a follow-on record and link the predecessor

**FIND**:
1. Search `reviews/threshold-evaluations/`, `context/bets/`, and the bet's folder
2. Present results: evaluation ID, bet ID, evaluation date, verdict, owner
3. Ask: "Open one of these, or create a new evaluation?"

### Search Locations

- `reviews/threshold-evaluations/`
- `context/bets/[YYYY]/`
- `strategy/bets/[bet-id]/thresholds/`
- `business/` and `cases/` (for the source business case)

---

## Gotchas

- The verdict is the artifact. An evaluation without a pass / fail / reopen call is incomplete and must not be filed.
- The threshold is the AFFIRMATIVE gate, not the inverse of an invalidation criterion. "No kill-criteria fired" is not the same as "threshold met." Continuation requires positive signal that the bet's thesis still holds, not the absence of bad news.
- Never invent metric values. If the data is not in `context/`, in a referenced source, or supplied by the user, mark it `[TBD]` and flag the missing-data risk in the verdict.
- The default verdict when the threshold is not clearly met is **reopen**, not **continue**. Silent continuation under the original commitment is a process failure — the bet must be reopened and routed back to portfolio review.
- The re-decision triggers minimum is a hard floor. If too many of the bet's named re-decision triggers have fired, the threshold is NOT met regardless of how the headline criteria look — too many fired triggers mean the bet's underlying assumptions have shifted enough that the original commitment is no longer the same commitment.
- This skill does NOT replace the T+6 / T+12 invalidation checkpoint (`/bet-invalidation-checkpoint`). Invalidation tests "should this bet die?" — Continuation Threshold tests "should this bet advance to a larger capital commitment?" Both can fire on the same bet at different gates and produce different verdicts.

---

## Output Structure

```markdown
# Continuation Threshold Evaluation: [Bet Name]

**Evaluation ID**: CT-[YYYY]-[NNN]
**Bet**: SB-[YYYY]-[NNN] — [Bet title]
**Evaluation Date**: [Date]
**Gate Firing**: [What major checkpoint triggered this evaluation — e.g., "Q4 portfolio review", "Series-stage funding decision", "Phase 2 to Phase 3 commit"]
**Owner**: [Single accountable person — typically the bet owner or the BizOps gating sensor]
**Verdict**: Pass / Fail / Reopen
**Capital Decision Pending**: [Specific commitment under consideration — e.g., "double headcount", "extend runway 6 months", "advance to Phase 3"]

## The Threshold (from /business-case)

[Verbatim restatement of the continuation_threshold field from the bet's business case. This is the standard the bet was committed to clear at this gate — restated here so the evaluation cannot quietly redefine the test.]

## Re-Decision Triggers Minimum

**Named Re-Decision Triggers (from /strategic-bet)**:

| # | Trigger | Type (outcome / market) | Status |
|---|---------|-------------------------|--------|
| 1 | [Trigger description] | [outcome / market] | not yet fired / fired-on-[date] |
| 2 | [Trigger description] | [outcome / market] | not yet fired / fired-on-[date] |
| 3 | [Trigger description] | [outcome / market] | not yet fired / fired-on-[date] |

**Minimum required in "not yet fired" state**: [N from business case]
**Currently in "not yet fired" state**: [count]
**re_decision_triggers_minimum_met**: TRUE / FALSE

If FALSE, the threshold is NOT met regardless of headline criteria — too many triggers have fired and the bet's underlying assumptions have moved.

## Criterion-by-Criterion Evaluation

For each criterion named in the Continuation Threshold, evaluate:

### Criterion 1: [Name]

**Threshold definition**: [What the business case said this criterion required]
**Observed signal**: [What the data shows now — with source]
**Evidence source**: [Where the signal came from — context registry / dashboard / CS report / customer evidence]
**Verdict on this criterion**: Met / Not met / Indeterminate (data missing)
**Reasoning**: [1-2 sentences on why]

### Criterion 2: [Name]

[Repeat structure]

### Criterion N: [Name]

[Repeat structure]

## Overall Verdict

**Verdict**: Pass / Fail / Reopen

**Decision rule**:
- **Pass** = ALL criteria met AND `re_decision_triggers_minimum_met` is TRUE
- **Fail** = One or more criteria explicitly not met (the bet's thesis has been disproven at this gate; route to invalidation checkpoint, not reopen)
- **Reopen** = Threshold ambiguous OR `re_decision_triggers_minimum_met` is FALSE OR data missing on a load-bearing criterion (the original commitment is no longer the same commitment; route back to portfolio review)

**Reasoning**: [3-5 sentences explaining the verdict, citing specific criteria and trigger states. The reasoning is the audit trail — a future reviewer must be able to reconstruct why this verdict was reached from this section alone.]

## Capital Decision

If verdict is **Pass**: The pending capital commitment is authorized to proceed. Document the new commitment level, the next gate firing date, and the threshold criteria for the next evaluation.

If verdict is **Fail**: The pending capital commitment is NOT authorized. Route the bet to `/bet-invalidation-checkpoint` for a continue / pivot / kill verdict. Do not proceed with the capital commitment under the current bet structure.

If verdict is **Reopen**: The pending capital commitment is paused. Route the bet back to portfolio review (`/portfolio-tradeoff` or `/strategic-bet` update). The original commitment is not the same commitment — the bet must be re-formulated against the new evidence base before any capital decision proceeds.

## Cross-References

- Source business case: [Path to the /business-case record that defined this threshold]
- Source strategic bet: [Path to the /strategic-bet record with named re-decision triggers]
- Most recent invalidation checkpoint (if any): [Path to /bet-invalidation-checkpoint record]
- Phase check consuming this verdict (if any): [Path to /phase-check record]
- Prior threshold evaluation (if any): [Path to predecessor]

## Reviewer Sign-off

- [ ] Owner has reviewed and signed off on the verdict
- [ ] Verdict has been logged in `context/bets/[YYYY]/[SB-ID].md` as a Continuation Threshold event
- [ ] If verdict is Reopen or Fail: routing record created (portfolio review or invalidation checkpoint)
- [ ] If verdict is Pass: next gate firing date and updated threshold criteria recorded for the next evaluation
```

---

## Instructions

1. Resolve the bet ID and read the bound business case before producing the evaluation. The threshold definition lives in the business case, not in this skill.
2. Read the strategic bet's named re-decision triggers and check each one's firing status against `context/assumptions/registry.md` and recent decision records.
3. Produce one verdict only. The decision rule above is the rule — pass requires ALL criteria met AND re_decision_triggers_minimum_met TRUE; anything else is fail or reopen.
4. The default when the threshold is ambiguous or data is missing on a load-bearing criterion is **Reopen**, not Pass. Silent continuation is a process failure.
5. Save the evaluation in `reviews/threshold-evaluations/` and link it from the bet record in `context/bets/[YYYY]/`.
6. If a `/phase-check` is downstream-consuming this evaluation to gate a Phase 2 → Phase 3 transition, surface the verdict in the phase-check input clearly.

## Context Integration

After generating the threshold evaluation:

1. **Save to context registry**: Log the verdict as a Continuation Threshold event on the bet's record in `context/bets/[YYYY]/[SB-ID].md`. The verdict is part of the bet's audit trail.
2. **Update assumption status**: If criterion findings invalidate or strengthen an assumption, update its status in `context/assumptions/registry.md`.
3. **Route on Reopen / Fail**: If the verdict is Reopen, create a portfolio-review queue entry. If Fail, create a `/bet-invalidation-checkpoint` invocation.
4. **Cross-reference for /phase-check**: If a Phase 2 → Phase 3 advance is pending, the consuming `/phase-check` record references this evaluation by ID; a Pass verdict from this skill is the structural prerequisite for that phase advance to be authorized.
