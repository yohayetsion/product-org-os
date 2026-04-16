---
name: cs-segmentation-model
description: Builds a two-axis (ARR band × strategic value) customer segmentation model with primary tier + override flags, calibrated to CSM capacity, for CS routing, health scoring, and tooling decisions.
argument-hint: '[--company-name NAME] [--input FILE]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: customer-success-operations
  skill_type: task-capability
  owner: cs-ops
  primary_consumers:
  - ext-cs
  - cs-tool-selection
  - health-score-design
  - ai-assisted-resolution-strategy
  sensitive: false
---
# /cs-segmentation-model

## Purpose

`/cs-segmentation-model` produces a customer segmentation model that tells a CS organization which customers belong to which service tier, how CSM capacity should be routed, and where automation versus human motion applies. The model uses a two-axis grid (ARR band × strategic value) collapsed to four tiers — **High-Touch Enterprise**, **Mid-Touch**, **Tech-Touch Pooled**, **PLG Self-Serve** — and layers override flags on top for hybrid customers who need treatment beyond their primary tier.

It is the foundation input for `/health-score-design` (which needs segment-specific signal weights) and `/cs-tool-selection` (which needs tier-specific tool stacks), and it feeds `/ai-assisted-resolution-strategy` with segment-specific CSAT floors. Ship this skill first in any CS build-out.

---

## When to Use

Invoke `/cs-segmentation-model` when you need to:

- Stand up a CS function from scratch and decide where each customer sits in the service model
- Re-segment an existing CS book when CSM capacity, ARR mix, or strategic priorities have shifted
- Prepare an input for `/health-score-design` so health weights reflect segment-specific signal importance
- Scope `/cs-tool-selection` so tool tier (Gainsight-heavy vs. spreadsheet + automation) matches segment shape
- Justify a CSM headcount ask to Finance with a tier-by-tier capacity roll-up

## When NOT to Use

Do NOT use `/cs-segmentation-model` when:

- You need a **pay equity audit** or compensation banding → that is an HR/comp skill, not CS segmentation
- You need a **strategic account plan** for a single high-value customer → that is `@csm` territory, specific to one account
- You need a **pricing strategy** or packaging decision → segmentation is downstream of pricing, not the same skill
- You need **sales territory design** or account assignment rules → that is sales ops territory, not CS ops
- You need a **vertical GTM plan** that happens to also segment customers → use a GTM segmentation skill, not this one

This skill is specifically about how CS routes service to existing (or committed) customers, not about how sales acquires them or how finance bands them.

---

## Inputs

### Required

1. **Customer list** — one row per customer, with at minimum:
   - Customer ID / name
   - ARR (or committed ARR for newly-signed accounts not yet live)
   - At least one strategic-value signal (see Step 1 for the rubric)

2. **CSM capacity** — total CSM headcount available OR a target book size per CSM per tier (used in Step 4 to calibrate)

### Optional (improves fidelity)

- **Override flag definitions** — if the company already runs specific programs (advocacy, expansion reviews, compliance artifact access) the skill maps them to override flags
- **Product usage signals** — feature adoption, DAU/MAU, seat utilization (strengthens the strategic_value score)
- **Product-line mix** — if the customer holds multiple SKUs, the mix influences strategic value
- **Regulatory context** — whether the customer operates in a regulated industry (drives `regulated_industry` override)
- **Logo tier / reference value** — whether the customer is a recognizable brand that serves as a sales reference (drives `strategic_logo` override)

If inputs are thin, the skill produces a lower-confidence model and flags the gaps in the output's "calibration confidence" section.

---

## Method

### Step 1 — Axis Definition

Define the two axes explicitly before any customer is placed on the grid. A segmentation model that starts with pre-baked bands always inherits someone else's assumptions; a model that defines axes from the customer portfolio inherits the real shape of the business.

**Axis A — ARR Band**

Choose one of two approaches:

- **Log scale bands** — appropriate when ARR distribution is long-tailed (a few very large customers, many very small ones). Example bands: <$1K, $1K–$10K, $10K–$100K, $100K–$500K, $500K+. Use this when the top 10% of customers hold >50% of ARR.
- **Quartile bands** — appropriate when ARR distribution is closer to uniform. Split the customer list into four equal-count buckets by ARR. Use this when no single customer holds >5% of ARR.

Document which approach was chosen and why. Do not mix approaches.

**Axis B — Strategic Value**

Strategic value is NOT revenue. It is the non-revenue reason a customer matters beyond their ARR. Score each customer against 3–5 weighted factors. Recommended starter rubric (weights sum to 1.0):

| Factor | Weight | What it measures |
|---|---|---|
| Strategic logo | 0.25 | Is this a recognizable brand that serves as sales proof? |
| Expansion potential | 0.25 | Does the account have clear, near-term upsell/cross-sell runway (seats, modules, volume)? |
| Product influence | 0.20 | Does the customer meaningfully shape the roadmap or run design partnerships? |
| Reference value | 0.15 | Will the customer do public case studies, QBR testimonials, analyst reference calls? |
| Regulatory exposure | 0.15 | Does the customer operate in a regulated space (healthcare, finance, gov) where losing them creates sector-level risk? |

Score each factor 0–1 for each customer, multiply by weight, sum to a composite 0–1 strategic_value score. Bin the composite into Low (<0.3), Medium (0.3–0.6), High (>0.6).

Weights are configurable — a company with no public-reference program should zero out `reference_value` and redistribute to the remaining four. Document the weight choices in the output.

### Step 2 — Tier Assignment

Apply the 4-tier collapse to the 2D grid:

```
                       Strategic Value
                    Low       Medium      High
                  ─────────────────────────────
ARR   High-ARR  │  Mid-Touch  Mid-Touch   HIGH-TOUCH ENTERPRISE
                │
      Mid-ARR   │  Tech-Touch Mid-Touch   HIGH-TOUCH ENTERPRISE
                │
      Low-ARR   │  PLG SELF-   Tech-Touch  Mid-Touch
                │  SERVE
```

Tier definitions:

- **High-Touch Enterprise**: Named CSM, quarterly business reviews, executive sponsor, custom success plans, priority support. Applies when (High-ARR AND High strategic value) OR (Mid-ARR AND High strategic value). The "mid-ARR high-strategic-value" cell is the one most organizations get wrong — they force it into Mid-Touch because ARR is lower, but strategic value earns the enterprise treatment.
- **Mid-Touch**: Shared CSM pool, scheduled check-ins, templated success plans, standard support. Covers the diagonal and the Low-ARR/High-value cell.
- **Tech-Touch Pooled**: No named CSM; pooled team triggered by health signals; automated lifecycle emails; self-service + scheduled webinars. Covers Mid-ARR/Low-value and Low-ARR/Medium-value cells.
- **PLG Self-Serve**: Fully self-serve; product is the onboarding; CS triggered only on ARR threshold crossings or explicit escalation. Covers Low-ARR/Low-value cell.

### Step 3 — Override Flag Definition (Optional)

A customer has exactly one primary segment (which drives CSM routing, health score weights, and tool tier). Override flags don't reclassify the primary — they modulate it by unlocking specific treatments the primary tier wouldn't normally provide.

Canonical override flags:

| Flag | Trigger Condition | Unlocks |
|---|---|---|
| `strategic_champion` | Customer has publicly advocated (case study, conference talk, analyst call) in last 12 months | Advocacy program, early feature access, speaker bureau invites |
| `expansion_ready` | Product usage or stated intent indicates near-term upsell runway | Quarterly expansion review, dedicated AE-CSM pairing |
| `regulated_industry` | Customer operates under HIPAA/PCI/SOC2/gov framework | Compliance artifact access, audit support SLA, security review on request |
| `design_partner` | Active design-partner agreement exists | Product roadmap input, monthly PM touchpoint, beta access |
| `at_risk_retention` | Health score below threshold OR explicit churn signal | Retention playbook activation, exec sponsor engagement, discount desk access |
| `reference_account` | Agreed to serve as customer reference for sales | Sales enablement routing, quarterly reference hygiene check |
| `m_and_a_transition` | Customer going through M&A that affects contract | Transition-specific CSM playbook, legal routing for contract novation |
| `multi_product` | Customer holds >1 SKU | Cross-sell hygiene check, unified QBR across product lines |

A customer can carry multiple override flags; they are additive, not exclusive. Flags must be mutually compatible — a `PLG Self-Serve` primary with `design_partner` flag is valid (unlocks monthly PM touchpoint without reclassifying the account), but a `Tech-Touch` primary with `strategic_champion` flag should probably be re-examined for promotion to Mid-Touch.

### Step 4 — Capacity Calibration

Count customers in each tier. Multiply by the CSM book-size norm for that tier:

| Tier | Typical book size per CSM |
|---|---|
| High-Touch Enterprise | 8–15 accounts |
| Mid-Touch | 40–80 accounts |
| Tech-Touch Pooled | 200–500 accounts (pooled) |
| PLG Self-Serve | 1,000+ accounts (pooled) |

Divide by current CSM headcount. If the tier breakdown doesn't match capacity:

- **Capacity shortage in enterprise tier** → tighten the strategic_value threshold (e.g., raise High bucket from >0.6 to >0.7) or raise the ARR band boundary. Fewer customers get High-Touch; more drop to Mid-Touch.
- **Capacity slack in enterprise tier** → loosen the thresholds, pulling more customers up.
- **Mid-touch absorbing everyone** → this is the failure mode. If >60% of customers land in Mid-Touch, the axes are not discriminating. Re-examine Step 1 weights.

Document the calibration decisions. A segmentation model that doesn't match capacity is a fantasy; the re-calibration is how reality re-enters.

### Step 5 — Validation

Run 5 sanity checks before shipping the model:

1. **No empty tiers** — every tier must have at least one customer. An empty Tech-Touch tier means the axes collapsed the grid.
2. **ARR coverage** — total ARR across tiers must equal total book ARR. A missing customer is a process failure.
3. **Strategic-value rubric used consistently** — every customer has a composite score, every score uses the same weights.
4. **Override flags mutually compatible** — no customer carries contradictory flags (e.g., `at_risk_retention` + `expansion_ready` is a genuine contradiction that should surface as a comment, not silently coexist).
5. **Stability test** — perturb ARR on 3 randomly-chosen customers by ±10%. If any customer changes tier under a 10% perturbation, the band boundaries are too tight and need softening.

Any failure aborts shipping the model and routes back to Step 1 or Step 4.

---

## Output Structure

The skill produces one markdown file at a company-appropriate location (e.g., `{Company}/Product/cs-segmentation-model-{date}.md`) with these sections:

1. **Model Summary** — one paragraph, plus the headline numbers: customer count, tier breakdown, CSM capacity fit
2. **Axis Definitions** — ARR band approach (log vs quartile) + boundaries; strategic_value weights and rubric
3. **Tier Definitions** — the 4 tiers with entry criteria, treatment description, and book-size target
4. **Override Flag Library** — the flags used for this company (may be a subset of the canonical 8) with trigger conditions
5. **Customer Segmentation Table** — one row per customer with: name, ARR, strategic_value score, primary_segment, override_flags[]
6. **Capacity Roll-Up** — tier × CSM headcount math, with gap/slack called out explicitly
7. **Re-Calibration Triggers** — the specific conditions that should trigger a re-run of this skill (see next section)
8. **Calibration Confidence** — any input gaps that limited the model (e.g., "no product usage data; strategic_value score is recognizer-driven only")

---

## Quality Gates

The skill applies these checks before emitting the final output. A check failure aborts the skill and routes back to the relevant step.

1. **No empty tiers** — every tier has at least one customer, OR the output explicitly documents why a tier is legitimately empty (e.g., "PLG Self-Serve empty: this company sells only enterprise deals")
2. **ARR sum matches input** — total ARR across all segmented customers equals the input book ARR within rounding
3. **Strategic-value rubric defined** — weights sum to 1.0, every factor scored 0–1, composite bucketed consistently
4. **Override flags mutually compatible** — no silent contradictions; explicit contradictions surfaced as comments
5. **Capacity fit explicit** — the output says "CSMs needed = X, CSMs available = Y, gap = Z" even if the gap is zero
6. **Mid-Touch under 60% of customers** — if Mid-Touch holds more than 60% of the book, the axes failed to discriminate; skill flags and routes back to Step 1
7. **Stability check passed** — ±10% ARR perturbation on 3 sample customers doesn't reclassify them
8. **Re-calibration triggers documented** — all four triggers (see next section) are explicitly stated in the output
9. **Input gaps flagged** — if required inputs were missing, the calibration confidence section names them

---

## Re-Calibration Cadence

Re-run the skill annually as a baseline. In addition, re-run when any of these fire:

1. **ARR distribution shifts by 20% in any tier** — if the High-Touch Enterprise tier's total ARR moves by 20% up or down, the band boundaries no longer reflect the book
2. **CSM capacity changes by 15%** — a hire wave, a reduction in force, or a reorg that changes CSM headcount by 15% requires re-calibration; tier boundaries were tuned to the old capacity
3. **Segment-level churn exceeds 1.5x target** — if churn in a single tier runs 1.5x the target rate for two consecutive quarters, the tier treatment is misaligned with the actual customer needs; the segmentation itself may be wrong
4. **Major product-line launch changes strategic_value definition** — a new SKU that creates a new form of strategic value (e.g., launching an AI product that makes product_influence matter more) requires re-weighting the strategic_value rubric

Do NOT re-run more often than quarterly in steady state. Segmentation thrash is its own failure mode — CSMs can't build account relationships if the account keeps moving between tiers.

---

## Related Skills + Hand-Off

This skill is the upstream foundation for the rest of the CS operations stack:

- **Feeds `/health-score-design`**: the segmentation model is a required input. Health score signal weights differ by segment — an enterprise account's health is driven by exec-sponsor engagement and expansion signals; a PLG account's health is driven by feature adoption and seat velocity. The segmentation output's `primary_segment` field is what `/health-score-design` keys on.
- **Feeds `/cs-tool-selection`**: the tier distribution determines the tool stack. A book that is 80% PLG Self-Serve does not need a Gainsight license; a book that is 40% High-Touch Enterprise probably does. The tier roll-up is the sizing input.
- **Feeds `/ai-assisted-resolution-strategy`**: segment-specific CSAT floors apply. High-Touch Enterprise customers carry a higher CSAT floor before AI escalation; PLG Self-Serve customers carry a lower floor and more permissive AI resolution.

Default delegation pattern is **Pattern 1 Consultation** (see `rules/delegation-protocol.md`). Common consultations:
- `@cs-dir` for tier boundary calibration ("does High-Touch Enterprise at 12 accounts match your CSM plans for the year?")
- `@csm` for signal weight ("which of these five strategic-value factors actually shows up in your QBRs?")
- `@bizops` for ARR band shape ("log vs quartile — what does the ARR distribution actually look like?")

Pattern 5 Adversarial Review is NOT required for this skill. Segmentation is a craft skill with established conventions; the cost of a missed edge case is a re-calibration, not a liability event.

---

## Birth Test

Every new skill must be birth-tested against a real or synthetic customer portfolio before it is declared v1.0.0 ready. For `/cs-segmentation-model`, the birth test was run against the **Legionis target customer profile** (builder-consumer split, $10/mo individual workspace + $25/mo all-teams bundle) as it exercises all four tiers cleanly — the AXIA portfolio is enterprise-only and does not test the PLG or Tech-Touch tiers.

The birth test output lives at: `Legionis/Product/cs-segmentation-birth-test-2026-04-11.md`

The birth test validates:
- Axis definition (log-scale ARR bands work for Legionis's long-tail distribution)
- Tier collapse produces a non-degenerate 4-tier breakdown
- Override flags catch the "design partner" and "strategic champion" cases the primary tier alone would miss
- Capacity calibration surfaces the CSM headcount gap
- Re-calibration triggers are actionable, not decorative

See the birth test file for the synthetic customer list, step-by-step walkthrough, and a short list of edge cases the skill handled (and one it punted on).

---

## ROI

Time saved on drafting and triage: the skill produces in ~20 minutes what a CS Ops lead would typically draft in 6–10 hours across a working session — axis definition, rubric weights, customer placement, capacity math, and quality gates. Blended CS Ops rate: $175/hr.

Standard output after skill invocation:

> ⏱️ ~[X] hrs saved on drafting and triage in [Y] min, [Z]k tkns ~$[C] cost, Value ~$[V]
