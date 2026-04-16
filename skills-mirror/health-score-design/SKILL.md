---
name: health-score-design
description: Designs a calibrated customer health score model with segment-aware signal weights, a cold-start variant, and explicit recalibration triggers, taking /cs-segmentation-model as required input.
argument-hint: '[--segmentation FILE] [--churn-history FILE] [--new-product]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: customer-success-operations
  skill_type: task-capability
  owner: csm
  primary_consumers:
  - ext-cs
  - ai-assisted-resolution-strategy
  - value-realization
  sensitive: false
---
# /health-score-design

## Purpose

`/health-score-design` produces a **customer health score model** — the scoring system, not the scores themselves. It defines signal families, per-segment weights, a cold-start variant for <90-day customers, and the recalibration cadence that keeps the model honest over time. The output is a model document that a CS team can implement in Gainsight, a spreadsheet, or a custom pipeline.

This skill intentionally does NOT interpret scores against a real customer base. Interpretation (reading a live score, deciding whether to open a retention playbook, triaging at-risk accounts) is handled by the separate `/health-score-interpret` skill that consumes the model this skill produces. Keeping design and interpretation in different skills prevents the common failure mode where a health score model gets "tuned" every time a surprising customer outcome shows up — which is calibration thrash, not learning.

---

## When to Use

Invoke `/health-score-design` when you need to:

- Stand up a health scoring model for a **new product** that has no historical churn data
- Redesign health scores after a **segmentation refresh** (new segments need new weights)
- Run a **quarterly calibration cycle** against accumulated churn and retention data
- Perform a **health-score audit** after an unexpected churn where the score failed to flag the risk
- Introduce **segment-specific health models** where a single one-size-fits-all model has broken down

## When NOT to Use

Do NOT use `/health-score-design` when:

- You need to **interpret an existing score** for a specific customer → that is `/health-score-interpret` (deferred, consumes this skill's output)
- You need to design a **CSM playbook** that fires based on score → that is a CS playbook skill, not model design
- You need a **churn post-mortem** for a specific account → that is `@csm` territory with an incident review format
- You need an **individual customer risk assessment** → that is a single-account health call, not a model
- You need a **pricing or packaging** change to retain customers → that is `/pricing-strategy`, downstream of health scoring
- You need a **win/loss analysis** for newly-churned accounts → that is a sales or revenue skill, not a health model

This skill is specifically about the scoring apparatus: which signals count, how much each weighs, which segment gets which treatment, and when the whole thing gets recalibrated.

---

## Required Inputs

### Required

1. **Segmentation model output** — from `/cs-segmentation-model`. The skill reads the primary-segment assignments and the override flags. Without segmentation, the health score collapses to one-size-fits-all, which is exactly the failure mode this skill is designed to avoid. If the segmentation model has not been run, route to `/cs-segmentation-model` first.

2. **Churn data context** — one of three acceptable forms:
   - **Churn history** (Tier 1 input): at least 20 historical churns with dates, cited reasons, and per-customer signal values at the time of churn. This enables regression-tuned weights and a real confusion matrix.
   - **Partial churn history** (Tier 2 input): fewer than 20 churns, or churns without cited reasons. This forces an expert-weighted workshop instead of regression.
   - **No churn history** (Tier 3 input): new product, new segment, no historical data. This triggers benchmark-weight defaults and a mandatory two-quarter recalibration gate.

### Optional (improves fidelity)

- **Product usage telemetry** — DAU/WAU, feature breadth, time-to-first-value, seat velocity. Without this, Behavioral signals collapse to coarse proxies.
- **Support ticket history** — ticket volume trend, sentiment scoring, escalation rate.
- **Sales/CSM notes** — multi-threading depth, exec sponsor presence, QBR attendance.
- **Cold-start cohort** — count of customers under 90 days and their onboarding milestones.

If inputs are thin, the skill produces a lower-confidence model and flags the gaps in the output's "calibration confidence" section.

---

## Method

### Step 1 — Segment the Customer Base

Read the segmentation output. Establish which primary segments exist and which override flags are in use for this company. The skill does NOT re-segment customers — it inherits the segmentation. If the segmentation model is stale or missing, abort and route to `/cs-segmentation-model`.

Document which segments will receive differentiated health score treatment. In almost all cases, **High-Touch Enterprise**, **Mid-Touch**, and **Tech-Touch Pooled / PLG Self-Serve** get different weights. Combining Tech-Touch Pooled and PLG Self-Serve into a single "pooled" weight set is allowed if the signals available for both are the same (pure behavioral telemetry).

### Step 2 — Pick the Calibration Tier

Use a deterministic rule to choose calibration tier, not a judgment call:

| Tier | Entry rule | Method | Recalibration gate |
|---|---|---|---|
| **Tier 1** | ≥20 historical churns with dates + cited reasons | Logistic regression tuned weights, held-out validation, confusion matrix reporting (precision, recall, AUC) | Annual + on any significant drift |
| **Tier 2** | <20 historical churns OR churns without cited reasons | Expert-weighted workshop with CSM leads + sales + support; structured weight-assignment protocol | 90 days post-ship, then quarterly |
| **Tier 3** | No churn history (new product, new segment, pre-PMF) | Benchmark defaults — **Behavioral 60% / Relational 25% / Sentiment 15%** | Mandatory recalibration after **2 full quarters** |

A Tier 3 model with no recalibration plan is not a model; it is a guess dressed in math. The recalibration gate is non-optional.

### Step 3 — Define Signal Families + Specific Signals

Health signals come from three families, with hard bounds on the weights:

**Behavioral (≥50% weight, hard floor)** — leading indicators of retention. Product-side signals that move before the customer announces intent.

Canonical signals:
- **logins** — unique user logins per week (use with caution; binary-ish once users land)
- **DAU/WAU ratio** — daily-over-weekly active, measures stickiness
- **feature breadth** — number of distinct features used per week (leading indicator of depth)
- **time-to-first-value (TTFV)** — days from kickoff to first value event (cohort-specific)
- **admin activity** — admin logins, settings changes, user invites (leading indicator of investment)
- **seat velocity** — rate of seat activation against contracted seats

**Do not double-count.** Pick logins OR DAU/WAU, not both — they capture the same underlying phenomenon and double-counting silently bumps Behavioral weight beyond the intended share.

**Relational (mid-weight, typically 20–40%)** — harder to game, slower to move. The signals that show an account is embedded in the customer's operation.

Canonical signals:
- **QBR attendance** — last QBR held + attendance rate (missing QBRs are a real signal)
- **exec sponsor present** — binary; is there a named executive sponsor reachable?
- **support volume trend** — absolute volume is meaningless; **trend** (up or down by >25% MoM) is the signal
- **multi-threading depth** — number of distinct users at the customer who log in per month; an account with 1 champion is fragile, an account with 8 threads is sticky
- **CSM risk flags** — CSM-raised qualitative concerns (last 30 days)

**Sentiment (≤20% weight, hard ceiling)** — trailing indicators. Sentiment shifts AFTER the underlying reality has already changed.

Canonical signals:
- **last NPS/CSAT** — score and recency (stale scores decay)
- **ticket sentiment** — aggregated sentiment of recent tickets
- **escalation rate** — tickets escalated to L2+ (leading sub-signal of churn, but limited; lives in Sentiment because it's trailing by the time escalation happens)

**Weight ceiling rationale**: A health score that lets Sentiment dominate will always fire late. NPS goes bad after the customer has already decided. The ceiling forces the model to lead with behavior.

### Step 4 — Assign Weights Per Segment

Differentiate weights by primary segment from the segmentation input. The general pattern:

| Segment | Behavioral | Relational | Sentiment | Rationale |
|---|---|---|---|---|
| **High-Touch Enterprise** | 50% | 35% | 15% | Relational signals are available and matter; exec sponsor + QBR + multi-threading are load-bearing |
| **Mid-Touch** | 55% | 30% | 15% | Balanced; some relational signals exist, behavioral still dominant |
| **Tech-Touch Pooled** | 70% | 15% | 15% | Relational signals are thin (no named CSM); behavioral telemetry is the real signal |
| **PLG Self-Serve** | 80% | 5% | 15% | Relational signals don't exist; behavioral is the whole story |

These are **starting points**, not gospel. Tier 1 calibration will tune them against real churns. Tier 2 will adjust them in workshop. Tier 3 starts with these and recalibrates after two quarters.

**Override flag modulation** — override flags from segmentation bump specific signals within the segment's weight budget:

| Override flag | Effect on signal weights |
|---|---|
| `strategic_champion` | Bump Relational multi-threading weight (multi-threading matters more when the champion is load-bearing; losing them is a bigger risk) |
| `regulated_industry` | Add a **compliance-artifact-access** signal in Behavioral (has the customer pulled SOC2/GDPR/HIPAA artifacts in the last quarter?) |
| `expansion_ready` | Bump Behavioral **feature breadth** + **seat velocity** (expansion signals are the forward indicator) |
| `at_risk_retention` | Force the score into a monitoring mode; the health score is now confirming a known risk, not discovering one |
| `cold_start` | Skip the full health score entirely; apply the cold-start variant (Step 5) |
| `design_partner` | Bump Relational QBR attendance + product influence signals |

Overrides modulate weights; they never reclassify the primary segment. A PLG Self-Serve customer with `design_partner` still uses the PLG weight profile, but with a Relational signal bump within that profile.

### Step 5 — Cold-Start Variant (<90 days)

A full health score is not defensible for a customer in the first 90 days of the relationship. There is not enough signal density. Forcing the full model to fire early generates false negatives that erode CSM trust in the score.

The cold-start variant is a **3-signal onboarding score**:

1. **TTFV hit** — did the customer reach their first value event within the TTFV target (product-specific; commonly 14 or 30 days)?
2. **Admin + end-user activation** — is at least one admin AND at least one end-user active in the product?
3. **Kickoff call attended** — was the kickoff call (High-Touch / Mid-Touch) or onboarding checklist (Tech-Touch / PLG) completed?

Output is **green / yellow / red**, binary-ish:

- **Green** — all three hit. Customer is on the normal trajectory.
- **Yellow** — one miss. Onboarding CSM (or automated nudge for Tech-Touch / PLG) follows up.
- **Red** — two or more misses. Retention playbook activates; this is the earliest signal the product will give.

**Migration rule**: at day 90, the customer automatically moves from the cold-start variant to the full segment-specific health score. No manual step. The model documents this transition explicitly so it cannot be quietly forgotten.

If a segment has no customers under 90 days (a mature book with no new sales), the cold-start variant is documented but dormant. It is not optional to skip the variant — a mature book becomes an immature book the moment a new sale lands.

### Step 6 — Design the Recalibration Trigger

Recalibration is a structural commitment, not a nice-to-have. The skill declares an **annual minimum** plus **four trigger-based conditions**:

1. **Unexpected-churn rate exceeds 5%** — more than 5% of churns in a quarter were "green" or "yellow" at the time of churn. The model is missing signal.
2. **Segmentation refresh of 20%+** — if `/cs-segmentation-model` is re-run and more than 20% of customers change primary segment, the health score must be re-calibrated against the new segmentation.
3. **Signal source deprecation** — a telemetry source (product analytics platform, support platform) is replaced or goes offline. The model's signals have to be re-sourced.
4. **Product-line shift** — a new product launches or an existing product is materially repositioned. The meaning of "feature breadth" changes, and the weights must be re-examined.

For Tier 2 and Tier 3 models, add one more trigger:

5. **90 days post-ship** — Tier 2 and Tier 3 models carry more assumption risk. A 90-day check-in is mandatory to catch early-stage misweighting before it compounds.

Document the recalibration cadence **explicitly** in the output. A recalibration cadence that lives only in someone's head is not a cadence.

---

## Output Structure

The skill produces one markdown file at a company-appropriate location (e.g., `{Company}/Product/health-score-design-{date}.md`) with these sections:

1. **Model Summary** — one paragraph, plus headline fields: calibration tier (1/2/3), segments covered, cold-start variant present, recalibration cadence
2. **Segmentation Input Reference** — pointer to the `/cs-segmentation-model` output consumed, with segment counts and override flag library
3. **Signal Catalog** — every signal used, with:
   - Definition (what it measures)
   - Source (where it comes from — product analytics, CRM, support platform, manual CSM flag)
   - Update frequency (real-time, daily, weekly, monthly)
   - Clamp bounds (min/max values; how out-of-range values are handled)
   - Normalization rule (how the signal maps to a 0–1 contribution)
4. **Segment Weight Matrix** — one row per segment, one column per signal, with weights summing to 1.0 per segment. Explicit Behavioral family total (≥50%) and Sentiment family total (≤20%) displayed per row.
5. **Cold-Start Variant** — the 3-signal onboarding score, green/yellow/red thresholds, and the day-90 migration rule
6. **Override Flag Modulation Rules** — for each override flag in use, the specific signal-weight bumps it triggers
7. **Calibration Evidence**:
   - Tier 1 → confusion matrix, precision/recall/AUC, held-out validation details
   - Tier 2 → workshop participant list, weight-assignment protocol, unresolved disagreements
   - Tier 3 → benchmark source declaration, assumptions documented, 2-quarter recalibration commitment
8. **Recalibration Triggers** — the annual minimum + 4 (or 5 for Tier 2/3) trigger conditions
9. **Calibration Confidence** — any input gaps that limited the model (e.g., "no TTFV telemetry yet; cold-start variant uses manual CSM flag as proxy")

---

## Quality Gates

The skill applies these checks before emitting the final output. A check failure aborts the skill and routes back to the relevant step.

1. **Behavioral weight ≥50%** — every segment row in the weight matrix has Behavioral family ≥50%. Fails → re-route to Step 4 weight assignment.
2. **Sentiment weight ≤20%** — every segment row has Sentiment family ≤20%. Fails → re-route to Step 4 weight assignment.
3. **Every signal has source + update frequency** — no "TBD" sources, no "unknown" update frequency. If telemetry is not yet available, the signal is either dropped or documented as a manual proxy.
4. **No signal double-counts** — logins + DAU/WAU together is a double-count. feature breadth + admin activity may be OK (they capture different phenomena) but requires an explicit comment in the catalog.
5. **Cold-start variant exists for segments with <90-day customers** — if any segment in the segmentation has a cold-start cohort, the cold-start variant is defined. Fails → re-route to Step 5.
6. **Recalibration cadence ≤2 quarters** — no model ships with a recalibration gap longer than 6 months. Annual is a minimum, not a maximum.
7. **At least one leading indicator per segment** — every segment row has at least one Behavioral signal that moves BEFORE the customer decides to churn. A segment model that leans on trailing signals (Sentiment-heavy) fails this gate.

---

## Recalibration Cadence

Annual minimum. Trigger-based earlier recalibration fires when any of the following conditions are met:

- **Unexpected-churn rate >5%** in a single quarter (green/yellow customers churning)
- **Segmentation reshuffle ≥20%** of customers changing primary segment in a `/cs-segmentation-model` re-run
- **Signal source deprecation** (telemetry platform replaced, support platform replaced)
- **Product-line shift** (new SKU, material repositioning)
- **Tier 2 / Tier 3 models**: mandatory 90-day post-ship check regardless of other triggers

Do NOT recalibrate more often than quarterly in steady state. Health-score thrash is its own failure mode — CSMs stop trusting scores that change every few weeks, and the score loses operational utility.

---

## Related Skills + Hand-Off

This skill sits downstream of segmentation and upstream of the operational CS stack:

**Input**:
- **`/cs-segmentation-model`** (required) — provides the primary-segment and override-flag assignments that drive per-segment weighting.

**Output feeds**:
- **`/ai-assisted-resolution-strategy`** — consumes segment-specific health thresholds. Different segments have different CSAT floors before AI escalation; the health score model informs where those floors land.
- **`/value-realization`** — this skill provides activity-level signals (behavioral, relational, sentiment); `/value-realization` provides outcome-level signals (did the customer achieve their stated business outcome?). A mature CS stack runs both side-by-side, with the outcome signal as the ground truth the health score is eventually calibrated against.
- **Future `/health-score-interpret`** — consumes the model this skill produces and applies it to a real customer base. Split deliberately from this skill to prevent calibration thrash.

Default delegation pattern is **Pattern 1 Consultation** (see `rules/delegation-protocol.md`). Common consultations:
- `@cs-ops` for segmentation nuance ("does this segment really warrant its own weight profile, or can it share with Mid-Touch?")
- `@support-lead` for ticket-sentiment signal quality ("is our sentiment scoring reliable enough to carry 10% weight, or is it noise?")
- `@bizops` for churn-definition rigor ("what counts as a churn vs. a downgrade vs. a pause? the score is only as good as the churn label.")

Pattern 5 Adversarial Review is NOT required for this skill. Health scoring is a craft with established conventions; the cost of a missed edge case is a recalibration, not a liability event.

---

## Birth Test

Every new skill must be birth-tested against a real or synthetic portfolio before v1.0.0. For `/health-score-design`, the birth test runs against the **Legionis** context — consistent with the `/cs-segmentation-model` birth test that preceded it, so the two skills chain cleanly.

Legionis is a Tier 3 case by construction: a pre-PMF product with no churn history and a mandatory 2-quarter recalibration gate. It exercises:

- Tier 3 benchmark defaults (60 / 25 / 15)
- Per-segment differentiation across 4 segments (High-Touch Enterprise, Mid-Touch, Tech-Touch Pooled, PLG Self-Serve — the same 4 that emerged from the segmentation birth test)
- Cold-start variant (Legionis will have many <90-day customers in year 1)
- Recalibration plan scheduled for Q3 2026

The birth test output lives at: `Legionis/Product/health-score-design-birth-test-2026-04-11.md`

See the birth test file for the full segment weight matrix, the cold-start variant instantiation, the calibration confidence gaps, and the specific Q3 2026 recalibration triggers.

---

## ROI

Time saved on drafting and triage: the skill produces in ~25 minutes what a CS Ops lead + CSM working session would typically draft in 8–14 hours — signal catalog, per-segment weight matrices, cold-start variant design, calibration tier decision, recalibration trigger specification. Blended CS Ops rate: $175/hr.

Standard output after skill invocation:

> ⏱️ ~[X] hrs saved on drafting and triage in [Y] min, [Z]k tkns ~$[C] cost, Value ~$[V]
