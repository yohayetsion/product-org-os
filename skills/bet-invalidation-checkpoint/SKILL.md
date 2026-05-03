---
name: bet-invalidation-checkpoint-t6-t12
description: 'Run the structured T+6 / T+12 month bet-invalidation checkpoint for a strategic bet, producing a continue / pivot / kill verdict. This is Value Realization''s signature decision authority — VR owns the call, not just the metrics. Activate when: "T+6 review", "T+12 review", "is this bet still working", "bet checkpoint", "invalidate the bet", "should we kill this bet", "bet review at six months", "bet status review". Do NOT activate for: outcome review of a shipped initiative (/outcome-review), portfolio-level tradeoffs (/portfolio-tradeoff), formulating a new bet (/strategic-bet), the upstream commitment check (/commitment-check).'
argument-hint: '[SB-YYYY-NNN bet ID] [--checkpoint t6 | t12] or [update path/to/checkpoint.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: learning
  skill_type: task-capability
  owner: value-realization
  primary_consumers:
  - value-realization
  - vp-product
  - cpo
  secondary_consumers:
  - pm-dir
  - bizops
  - competitive-intelligence
  - product-operations
  - cs-dir
  - data-lead
  - bi-engineer
  - experimentation-analyst
  sensitive: false
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "finalize", "add T+12 data" in input | UPDATE | 100% |
| File path provided (`@path/to/checkpoint.md`) | UPDATE | 100% |
| Existing checkpoint ID referenced | UPDATE | 100% |
| "create", "new", "run the T+6 checkpoint" | CREATE | 100% |
| "find", "search", "list checkpoints" | FIND | 100% |
| Bet ID + checkpoint timing word ("T+6", "T+12", "six months") | CREATE | 90% |
| Just a bet ID with no checkpoint word | ASK | — |

**Threshold**: greater-or-equal 85% auto-proceed | 70-84% state assumption | <70% ask user.

### Mode Behaviors

**CREATE**:
1. Resolve the strategic bet (`SB-YYYY-NNN`) from `context/bets/index.md` and `context/bets/[YYYY]/`
2. Pull all assumptions tied to the bet from `context/assumptions/registry.md`
3. Read the bet's success criteria and re-decision points
4. Read prior checkpoint if it exists (T+6 must be read before T+12)
5. Generate the checkpoint artifact below for the named checkpoint (T+6 or T+12)
6. The Verdict section is mandatory — no checkpoint ships without a continue / pivot / kill call

**UPDATE**:
1. Read existing checkpoint (search `reviews/checkpoints/` and the bet's folder)
2. Preserve verdict, signals, and rationale already recorded
3. Update late-arriving data (e.g., a metric that finalized after the checkpoint date)
4. If the verdict itself is changing, that is a NEW checkpoint, not an update — create a follow-on record and link it

**FIND**:
1. Search `reviews/checkpoints/`, `context/bets/`, and the bet's folder
2. Present results: checkpoint ID, bet ID, T+6 vs T+12, verdict, owner, date
3. Ask: "Open one of these, or create a new checkpoint?"

### Search Locations

- `reviews/checkpoints/`
- `context/bets/[YYYY]/`
- `strategy/bets/[bet-id]/checkpoints/`
- `learnings/` (for follow-on context)

---

## Gotchas

- The verdict (continue / pivot / kill) is the artifact. A checkpoint without a verdict is incomplete and must not be filed.
- T+6 and T+12 are not the same artifact. Different signals, different verdicts, different decision shapes — see "T+6 versus T+12 — what changes" below.
- Never invent metric values. If the data is not in `context/`, in a referenced source, or supplied by the user, mark it `[TBD]` and flag the missing-data risk in the verdict.
- VR owns this decision. The checkpoint is authored by VR with input from the bet owner; the verdict is signed by VR. VP Product and CPO are informed and can challenge, but VR makes the call. If VR is overruled, that overrule is recorded in the checkpoint — silent overrules are a process failure.
- The pivoted intent must be written down explicitly. A "pivot" verdict that names a new direction without recording the abandoned one loses the learning.
- Invalidated assumptions are the leading signal. If three or more numbered assumptions on the bet are invalidated by T+6, the verdict bias is toward pivot or kill regardless of metrics — assumptions are why the bet exists.
- Don't conflate this with `/outcome-review`. Outcome review is post-initiative ("did this thing work"). Bet invalidation is mid-bet ("is the thesis still alive"). The bet may continue past T+12 with a "continue" verdict — outcome review fires when the bet's named outcome window closes.

---

## Purpose

The bet-invalidation checkpoint is the structured moment at T+6 months and T+12 months after a strategic bet was committed when Value Realization determines whether the bet is still on track or whether it needs to be invalidated and reopened. It exists because strategic bets that are not actively challenged by their owners drift — assumptions that were tagged as "we need to validate this" stop being checked, leading indicators get watched until they go yellow and then quietly stop being reported, and re-decision triggers are observed and ignored. The checkpoint forces the call.

This is Value Realization's **signature decision authority**. VR is not just reading metrics here — VR owns the verdict. The bet owner (often VP Product or PM-Dir) holds the bet; VR holds the invalidation question. The two sit on opposite sides of the table by design. VR's accountability is to the customer-outcome reality the bet promised, not to the bet's continued life.

## T+6 versus T+12 — what changes

The two checkpoints are deliberately different artifacts. Treat them that way.

**T+6 — leading-signal checkpoint**. Six months after commitment, lagging outcome metrics are usually too early to read. The signal at T+6 is leading-indicator metrics, assumption validation status, and whether the first re-decision triggers have been hit. T+6's job is to catch the bets that are clearly off the rails before another six months of investment compounds — bets where leading indicators are flat or moving the wrong direction, where multiple assumptions have been invalidated, or where a re-decision trigger has been hit and is being silently ignored. The verdict at T+6 leans toward continue-with-watch unless something specific is firing; pivot or kill at T+6 requires a named, evidence-backed reason.

**T+12 — outcome-signal checkpoint**. Twelve months in, lagging outcome metrics should be reading and the bet thesis is testable against actual customer behavior, business results, and market response. The signal at T+12 is outcome-indicator metrics against the bet's success criteria, full-scale invalidation triggers, and whether the bet thesis as written has been validated. T+12 is where most invalidation calls happen — because by twelve months you can see whether the bet worked. The verdict at T+12 is more decisive: continue (the thesis is validated, scale up), pivot (the thesis is partially right and the new intent is named), or kill (the thesis is wrong and the capital allocated to this bet is reopened for redeployment).

A bet that hits T+12 with a "continue" verdict generally moves out of active checkpoint cadence and into normal portfolio cadence with `/outcome-review` firing on the bet's outcome window.

## Output Structure

```markdown
# Bet-Invalidation Checkpoint: [Bet Name]

**Checkpoint ID**: BIC-[YYYY]-[NNN]
**Bet ID**: SB-[YYYY]-[NNN] (linked)
**Checkpoint Type**: T+6 / T+12
**Checkpoint Date**: [Date]
**Bet Commitment Date**: [Date]
**Months Elapsed**: [N]
**Owner (Bet)**: [Bet owner name / agent — typically VP Product or PM-Dir]
**Owner (Verdict)**: Value Realization (signature decision authority)
**Status**: Draft / Reviewed / Filed / Superseded

## Bet Recap (read-only — do not amend the original SB record)

**Original Bet Statement**: [Pull verbatim from SB record]
**Original Riskiest Assumption**: [Pull from SB record]
**Original Re-decision Triggers**: [Pull from SB record]
**Capital Envelope Committed**: [From SB or commitment-check]

## Signal Read at [T+6 / T+12]

### Leading-Indicator Metrics (primary at T+6, supporting at T+12)

| Metric | Baseline | Target [T+6 / T+12] | Actual | Variance | Direction | Quality |
|--------|----------|---------------------|--------|----------|-----------|---------|
| [Metric 1] | [Baseline] | [Target] | [Actual or TBD] | +/-X% | Up/Flat/Down | Strong/Weak/Suspect |
| [Metric 2] | [Baseline] | [Target] | [Actual or TBD] | +/-X% | Up/Flat/Down | Strong/Weak/Suspect |

**Quality note**: Mark "Suspect" if metric integrity is in question (definition drift, instrumentation gap, sample bias). Suspect signals do not support a positive verdict.

### Outcome-Indicator Metrics (T+12 primary; usually [TBD] at T+6)

| Metric | Baseline | Target T+12 | Actual | Variance | Verdict Bearing |
|--------|----------|-------------|--------|----------|-----------------|
| [Outcome metric 1] | [Baseline] | [Target] | [Actual or TBD] | +/-X% | Strong / Weak / Mixed |
| [Outcome metric 2] | [Baseline] | [Target] | [Actual or TBD] | +/-X% | Strong / Weak / Mixed |

### Assumption Validation Status

| # | Assumption (from SB record) | Original Confidence | Validation Method Used | Current Status | Source |
|---|------------------------------|---------------------|------------------------|----------------|--------|
| 1 | [Assumption] | Low/Med/High | [Method] | Validated / Invalidated / Untested / Partial | [Evidence] |
| 2 | [Assumption] | Low/Med/High | [Method] | Validated / Invalidated / Untested / Partial | [Evidence] |
| 3 | [Assumption] | Low/Med/High | [Method] | Validated / Invalidated / Untested / Partial | [Evidence] |

**Riskiest assumption status**: [Validated / Invalidated / Still untested]
**Count of assumptions invalidated**: [N of M]
**Count of assumptions still untested at this checkpoint**: [N of M]

> Decision rule: If three or more numbered assumptions are invalidated, OR if the riskiest assumption is invalidated, the verdict bias is toward pivot or kill. Assumption invalidation is a stronger signal than metric variance because assumptions are why the bet exists.

### Re-decision Triggers Status

| Trigger (from SB record) | Hit? | Date | Acknowledged in real time? |
|---------------------------|------|------|----------------------------|
| [Trigger 1] | Yes/No | [Date or N/A] | Yes / No / Late |
| [Trigger 2] | Yes/No | [Date or N/A] | Yes / No / Late |

> Triggers hit but not acknowledged in real time are themselves a verdict signal — they indicate the bet is being run on momentum rather than on evidence.

## Verdict (mandatory — no checkpoint ships without this section)

**Verdict**: Continue / Pivot / Kill
**Verdict Confidence**: High / Medium / Low
**Decided By**: Value Realization (signature)
**Acknowledged By**: [Bet owner] / [VP Product] / [CPO if escalated]

### Rationale

[2-4 paragraph narrative reading the signals together. Do not just restate the table data. The rationale answers: which signals carried weight, which were noise, what the assumption picture says about the thesis, and why the verdict follows.]

### If Verdict = Continue

**What "continue" means here**: Continue with current intent unchanged. The thesis is holding. Capital envelope unchanged. Next checkpoint at [T+12 if this was T+6, or normal portfolio cadence if T+12].

**Watch items between now and the next checkpoint**:
- [Item 1 — what to monitor]
- [Item 2 — what to monitor]

### If Verdict = Pivot

**Original intent (now abandoned)**: [Restate the original bet thesis verbatim]
**Revised intent (new bet thesis)**: [Write the new thesis explicitly. This becomes the basis for either an updated SB record or a new SB record — see Cross-references below for which.]

**What changed in the underlying picture**: [What did we learn that makes the new intent the right thesis]
**What is being preserved**: [Customer segment? Capital envelope? Team? Be specific.]
**What is being reset**: [Assumptions, success criteria, success window, re-decision triggers]
**Pivot capital envelope decision**: Continue under existing envelope / Resize / Reopen for portfolio reallocation

### If Verdict = Kill

**Reason for kill**: [Specific. Not "it didn't work." E.g., "Riskiest assumption invalidated; customer segment did not exhibit the buying behavior the thesis required."]
**Capital recovered for reallocation**: [Amount and which capital lines are released]
**What stays vs what unwinds**: [Team, IP, customer relationships, infrastructure]
**Learning captured to**: [Pointer to `/outcome-review` invocation that closes the bet, or to `context/learnings/`]

## Cannot Assess Without

[Items the checkpoint deliberately did not opine on. Examples: regulatory changes that may invalidate the thesis but have not yet ruled, data sources that are still instrumenting, customer cohorts whose behavior is not yet measurable. Make scope explicit so the verdict is not over-claimed.]

## Reviewer Checklist

- [ ] All numbered assumptions reviewed against current evidence
- [ ] All re-decision triggers checked against actual bet activity since commitment
- [ ] Suspect-quality metrics flagged and not used to support a positive verdict
- [ ] If pivot: original intent explicitly recorded; revised intent written down
- [ ] If kill: reason cited specifically; capital reallocation note present
- [ ] Bet owner has acknowledged the verdict (verdict can stand without acknowledgment, but the disagreement is recorded)
- [ ] If VR was overruled: the overruling agent and rationale are recorded — silent overrules are a process failure
- [ ] Cross-references back to SB record updated (status field, etc.)
- [ ] Checkpoint filed to `reviews/checkpoints/` and registered in context

## Cross-references

- **Upstream**: `/strategic-bet` SB-[YYYY]-[NNN] — the bet record that this checkpoint is reading against
- **Decision**: `/decision-record` — file the verdict (continue / pivot / kill) as a decision record. Pivot and kill verdicts always require a DR. Continue verdicts require a DR only if the verdict overrides any prior signal.
- **Portfolio**: `/portfolio-status` — surface the verdict to the active-bets register. Pivot or kill changes the active-bets state.
- **Audit**: `/decision-quality-audit` (V5.1-37 trajectory-aware extension) — the audit reads bet-invalidation outcomes for Decision Improvability assessment. Treat each checkpoint verdict as a data point about decision quality on the original commitment.
- **Assumption registry**: `context/assumptions/registry.md` — propagate validated / invalidated status from this checkpoint to the registry.
- **If kill at T+12**: `/outcome-review` — file the post-kill outcome review to close the learning loop.
- **If pivot**: either update the existing SB record (preserve history; add pivot section) or create a new SB record linked to the original. Decision rule: if the customer segment changed, new SB; if only the approach changed, update the existing SB.
```

## Instructions

1. **Resolve the bet first**. Read the SB record from `context/bets/`. If the bet ID does not resolve, stop and ask the user. Do not run a checkpoint against an inferred bet.
2. **Confirm checkpoint type**. T+6 versus T+12 changes the artifact shape. If the months-elapsed math does not match the user's stated checkpoint type, surface the mismatch before proceeding.
3. **Check prior context**. Run `/context-recall [bet name or ID]`. Read any prior checkpoint on this bet — T+12 must read T+6 first.
4. **Read assumptions explicitly**. Pull every numbered assumption from the bet's record and from `context/assumptions/registry.md`. The assumption picture is the verdict's spine.
5. **Read the re-decision triggers**. Triggers hit and not acknowledged are themselves a signal.
6. **Pull metrics from the source of record**. If the metric is not in `context/`, in a referenced data source, or provided by the user, mark `[TBD]` and flag the missing-data risk in the verdict.
7. **Generate the verdict last**. The signal read sets up the call; do not write the rationale before reading the signals.
8. **Save the checkpoint**. File to `reviews/checkpoints/BIC-[YYYY]-[NNN].md`, register in `context/decisions/index.md` if the verdict is pivot or kill (or a notable continue), update the bet's status in `context/portfolio/active-bets.md`, and propagate assumption status to `context/assumptions/registry.md`.
9. **Link to upstream and downstream artifacts** per the Cross-references list above.
10. **Offer to create a presentation**. Pivot and kill verdicts often need to be communicated to a wider audience — offer `/present` for the checkpoint document.

## Context Integration

After completing the checkpoint:

1. **Save the verdict as a decision record** — Pivot and kill verdicts are mandatory `/decision-record` invocations. A continue verdict requires a DR if it overrides a prior signal or trigger.
2. **Update the assumption registry** — for each assumption whose status changed, update `context/assumptions/registry.md` with the new status, evidence pointer, and date.
3. **Update the portfolio register** — `context/portfolio/active-bets.md` reflects the verdict. Kill verdicts move the bet out of active. Pivot verdicts update the bet's intent and may move capital.
4. **Trigger downstream skills** —
   - Pivot verdict: invoke `/strategic-bet` in update mode (existing bet pivots) or create mode (new SB linked to old) per the decision rule above
   - Kill verdict: invoke `/outcome-review` to close the learning loop
   - Either pivot or kill: notify portfolio-tradeoff cadence that capital may need redeployment
5. **Feed the audit signal** — `/decision-quality-audit` reads checkpoint outcomes for trajectory-aware Decision Improvability assessment. The checkpoint is the audit's source of truth for whether a strategic bet was honestly evaluated against its original thesis.
