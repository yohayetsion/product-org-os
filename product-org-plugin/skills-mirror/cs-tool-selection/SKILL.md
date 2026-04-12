---
name: cs-tool-selection
description: Vendor-neutral CS tool selection framework with segmentation-tiered criteria, RFP templates, and weighted shortlist logic.
argument-hint: --segmentation FILE --health-score FILE [--budget USD] [--team-size COUNT]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: customer-success-operations
  skill_type: task-capability
  owner: cs-dir
  primary_consumers:
  - ext-cs
  sensitive: false
---
# /cs-tool-selection

## Purpose

`/cs-tool-selection` produces a **selection framework** — not a recommendation. It generates the evaluation criteria, the RFP question template, and the weighted shortlist rubric that a CS organization uses to run its own tool selection. The skill is **pure framework, vendor-neutral by construction**: no vendor names appear in the output. The buyer supplies the vendor list, runs the RFP, fills the rubric, and owns the choice.

This skill is deliberately downstream of `/cs-segmentation-model` and `/health-score-design`. The segmentation output determines which tool archetype is appropriate (enterprise CSP vs. product-analytics-led pooled tooling vs. hybrid); the health-score model determines where scores must originate and where they must be consumed. Skipping either input produces generic selection criteria that map to no real operating model — the common failure mode this skill is designed to avoid.

---

## When to Use

Invoke `/cs-tool-selection` when you need to:

- Run a **greenfield tool selection** for a CS function being stood up for the first time
- Execute a **tool consolidation** when the current stack has drifted into overlapping capabilities
- Structure a **contract renewal negotiation** where the incumbent is the default but should be challenged
- Rationalize the stack after an **M&A event** that combined two CS organizations with different tooling
- Respond to a **segmentation shift** that invalidates the previous tool selection (e.g., enterprise book pivots to PLG)

## When NOT to Use

Do NOT use `/cs-tool-selection` when:

- You need a **vendor performance review** of an existing tool → that is a vendor-management skill, not selection
- You need an **implementation plan** for a tool already selected → that is a separate `/cs-tool-implementation-plan` (not yet scoped)
- You need an **ROI model for a specific vendor's pricing quote** → that is a BizOps / vendor-specific analysis, not a selection framework
- You need a **single-feature evaluation** (e.g., "does this tool support NPS?") → that is a point question, not a selection
- You need a **build vs. buy decision** for CS infrastructure → that is a broader strategic question that precedes this skill

This skill is specifically about producing the apparatus a buyer uses to choose among candidate vendors. It does not choose.

---

## Required Inputs

### Required

1. **Segmentation model output** — from `/cs-segmentation-model`. The skill reads the tier distribution (High-Touch Enterprise / Mid-Touch / Tech-Touch Pooled / PLG Self-Serve) and the override flags. The tier shape is what drives the archetype mapping in Step 2. Without segmentation, the skill cannot differentiate between "you need a full CSP" and "you need product analytics plus lifecycle automation" — which are radically different procurement paths. If segmentation has not been run, route to `/cs-segmentation-model` first.

2. **Health-score model output** — from `/health-score-design`. The skill reads where signals originate (product telemetry, CRM, support platform, manual CSM flags) and where they must be consumed (CSM surfaces, executive dashboards, customer-facing indicators, automated playbooks). Tool evaluation criteria depend on whether the tool must natively compute health or simply ingest a score computed elsewhere. Without the health-score model, the data-integration and health-scoring dimensions of the RFP collapse to generic "supports health scoring" checkboxes, which no RFP response will usefully discriminate.

### Optional (strongly recommended)

- **Budget range** — annual license budget ceiling. Feeds pricing-model evaluation and eliminates archetypes that are structurally out of reach. A $50k/yr ceiling and a $500k/yr ceiling point to different tool classes. Without a budget, the framework still works but cannot eliminate archetypes on affordability grounds.
- **Team size** — number of CSMs, CS Ops headcount, and whether there is a CS Lead as the internal buyer. Team size feeds the complexity-of-adoption dimension; a 1-person CS function cannot absorb a 90-day implementation regardless of the tool's merits.
- **Deployment geography** — jurisdictions where customer data sits. Drives security/compliance/data-residency evaluation.
- **Existing stack** — CRM, product analytics, support platform, billing system currently in place. Drives integration-depth evaluation.

If inputs are thin, the skill produces a lower-confidence framework and flags the gaps in the output's "framework confidence" section.

---

## Method

### Step 1 — Classify the Tool Need

Before any criteria are generated, decide what **class** of tool is actually needed. The classes are not interchangeable and the selection framework differs materially across them:

| Class | What it is | Typical buyer trigger |
|---|---|---|
| **Full CSP** (Customer Success Platform) | Integrated platform covering health scoring, playbook automation, QBR tooling, renewal forecasting, usage analytics, and customer-facing surfaces | Enterprise-heavy book, named CSMs per account, multi-year contracts |
| **CRM extension** | Health scoring and CS workflow built on top of an existing CRM platform | CRM already entrenched, CS function growing out of sales, lower license budget |
| **Product-analytics-led** | Product analytics platform as the spine; CS workflows are lightweight automation on top | PLG-heavy book, product telemetry is the dominant signal, CSMs are few or pooled |
| **Digital-touch automation** | Lifecycle email, in-app messaging, triggered sequences keyed to behavioral events | Tech-Touch Pooled book, low CSM-to-account ratio, scale through automation |
| **Pooled support + KB** | Ticketing, SLA management, self-service knowledge base as the primary CS surface | Support-led CS, high-volume low-value accounts, customer self-serve expected |
| **Hybrid** | Two or more of the above running side-by-side with an integration spine | Mixed-segment book, tier-specific tooling within one organization |

Classification is not vanity. A full CSP bought for a PLG book is the canonical procurement failure. A product-analytics-led stack bought for an enterprise book fails to give CSMs the playbook surface they need to do the job.

### Step 2 — Map Segmentation Tier to Tool Archetype

Read the segmentation output. For each primary tier that has non-trivial customer count, apply the tier-to-archetype mapping:

| Primary segment | Primary archetype | Secondary archetypes (if hybrid) |
|---|---|---|
| **High-Touch Enterprise** | Full CSP with playbook automation, QBR tooling, exec-sponsor dashboards, multi-threaded account mapping | — |
| **Mid-Touch** | Lighter CSP OR CRM extension + health-score module + digital-touch automation | Full CSP if budget permits and account count justifies |
| **Tech-Touch Pooled** | Product analytics + in-app messaging + trigger-based playbooks (no dedicated CSM tooling per account) | Pooled support + KB for ticket handling |
| **PLG Self-Serve** | Product analytics + community + help center + usage-based outreach automation | Digital-touch automation for conversion events |

If the segmentation shows a **mixed book** (meaningful population in 2+ tiers), the output is a **hybrid** recommendation: a primary archetype for the dominant tier plus a secondary archetype for the non-dominant tier. The RFP question template and rubric then evaluate vendors against the hybrid's integration spine — can the tools exchange data, and who owns the system of record for health scores?

**Anti-pattern (flagged in Step 7)**: letting a single tier force the whole book into its archetype when the other tiers would be poorly served. A 60% Mid-Touch book with a 15% High-Touch Enterprise tier should NOT buy a full CSP just to satisfy the enterprise tier if the CSP cost makes Mid-Touch operations untenable — the hybrid path is the right answer.

### Step 3 — Derive Health-Score Consumption Requirements

Read the health-score model. Answer four questions that become load-bearing RFP requirements:

1. **Where are health scores computed?** CSP-native (the tool computes from signals it ingests), BI-layer-computed (the tool imports a pre-computed score from a data warehouse), or product-analytics-derived (the tool reads behavioral signals and a rule layer generates the score).
2. **Where are health scores consumed?** CSM workbench (every CSM sees a live score per account), executive dashboard (leadership rollup), customer-facing indicator (the customer sees their own health), automated playbook trigger (score crosses threshold → playbook fires).
3. **Which signal families must the tool support natively?** Behavioral telemetry, Relational (QBR / exec sponsor / multi-threading), Sentiment (NPS / ticket sentiment). The segment weight matrix from the health-score model lists them explicitly.
4. **Where does the cold-start variant live?** If the cold-start variant is distinct from the full model (it almost always is), the tool must support either two parallel scoring models or an automatic day-90 transition rule. This is a real discriminator in RFP responses — most vendors handle it poorly.

These four answers seed four specific evaluation dimensions in Step 4 and four RFP question categories in Step 5.

### Step 4 — Generate Evaluation Criteria (8-12 Dimensions, Weighted)

Produce the weighted evaluation rubric. Every dimension has: a definition, a weight (integer, so buyer can adjust), a scoring specification (how to score 1-5), and a "why this matters" rationale tied back to the segmentation and health-score inputs.

**Required dimensions** (these ship with the framework; weights are calibrated to the buyer's context):

1. **Data integration depth** — how deeply the tool integrates with the buyer's CRM, product analytics, billing, and support platforms. Score: depth, documentation, maintenance burden.
2. **Health-score model support and flexibility** — can the tool represent the segment-specific weight matrix and the cold-start variant? Is the model editable by CS Ops without a vendor professional-services engagement?
3. **Playbook automation** — trigger types, branching, human-in-the-loop steps, SLA enforcement.
4. **Reporting and BI export** — native dashboards and ability to export raw data to a BI layer for custom reporting.
5. **Security, compliance, data residency** — per deployment geography. SOC 2, ISO 27001, data residency guarantees, sub-processor transparency.
6. **Pricing model fit** — per-seat, per-account, platform-flat, usage-based. The fit to the buyer's growth shape matters more than the headline price.
7. **Implementation timeline and complexity** — from kickoff to first usable dashboard. Realistic, not vendor-sales-claim.
8. **Professional services quality** — quality and scope of vendor PS engagement. For a 1-CSM buyer, PS is not optional.
9. **Vendor reference relevance** — references in the buyer's segment and ARR band. A reference in a different segment is decorative; a reference in the same segment is load-bearing.
10. **Roadmap velocity and direction** — release cadence, public roadmap or NDA roadmap access, direction alignment with the buyer's needs.
11. **Total cost of ownership (3-year)** — license + implementation + ongoing PS + internal Ops time. Sticker price is a fraction of TCO and the selection must reflect the full curve.
12. **Operator experience** — does the CSM who will use the tool daily actually find it usable? This is frequently missing from enterprise selections and is the single biggest source of post-purchase regret.

**Weights sum to 100**, integer weights. The framework ships with suggested default weights; the buyer tunes them before the shortlist is filled. Default suggested weights:

| Dimension | Default weight |
|---|---|
| Data integration depth | 12 |
| Health-score model support and flexibility | 12 |
| Playbook automation | 10 |
| Reporting and BI export | 8 |
| Security, compliance, data residency | 10 |
| Pricing model fit | 10 |
| Implementation timeline and complexity | 8 |
| Professional services quality | 6 |
| Vendor reference relevance | 8 |
| Roadmap velocity and direction | 5 |
| Total cost of ownership (3-year) | 6 |
| Operator experience | 5 |
| **Total** | **100** |

**Quality gate**: the weights must sum to exactly 100. If the buyer tunes them and they drift from 100, the skill re-normalizes or aborts depending on severity.

### Step 5 — Produce the RFP Question Template (~20 Questions, Categorized)

The RFP template is the most durable asset the skill produces. Questions are **vendor-neutral by construction**: any vendor in any of the Step 1 tool classes can answer them without being led. The framework ships 20 questions across 10 categories:

**Category A — Data Integration (2 questions)**
1. How does your platform ingest data from CRM, product analytics, billing, and support platforms? Describe native integrations vs. middleware-required integrations.
2. What is the maintenance burden on the buyer's team when an upstream system schema changes? Who owns the repair?

**Category B — Health Scoring (2 questions)**
3. How does your platform compute health score, and what signal families does it natively support (Behavioral, Relational, Sentiment)? Can the weight matrix vary by customer segment?
4. Does your platform support a distinct cold-start score for new customers, and how does the transition from cold-start to the full score happen?

**Category C — Playbook Automation (2 questions)**
5. What trigger types are supported for playbook activation (score threshold, event, time-based, manual, external webhook)? Can playbooks branch on conditions, and can they include human-in-the-loop approval steps?
6. How are playbook SLAs enforced and escalated? Where do overdue playbook steps surface?

**Category D — Reporting and BI (2 questions)**
7. What native dashboards ship with the platform, and which can be customized without professional services engagement?
8. How is raw data exported to an external BI layer? Describe the export cadence, completeness, and the data contract.

**Category E — Security and Compliance (2 questions)**
9. What security certifications does your platform hold (SOC 2, ISO 27001, others)? Provide the most recent SOC 2 report summary.
10. Where does customer data reside, and what data residency options do you support? Describe sub-processor transparency and the process for sub-processor changes.

**Category F — Pricing (2 questions)**
11. Describe your pricing model (per-seat, per-account, platform-flat, usage-based). What drives price as the buyer grows?
12. Provide a 3-year total-cost illustration at the buyer's stated starting scale and at 2x growth. Include license, implementation, and ongoing professional services.

**Category G — Implementation (2 questions)**
13. What is the realistic timeline from contract signature to a usable production instance? Describe the critical-path dependencies.
14. What does the buyer's team need to staff for the implementation, and what does the vendor team deliver?

**Category H — Professional Services (2 questions)**
15. Describe the professional services scope included at contract signature. What is billed separately?
16. How is ongoing PS structured after go-live — by hour, by retainer, by package?

**Category I — References (2 questions)**
17. Provide three customer references in the buyer's segment and ARR band, with permission to contact. At least one reference must be within the last 12 months.
18. Describe a customer that did not succeed on your platform and what happened. A vendor who cannot answer this question is flagging that they do not look.

**Category J — Roadmap (2 questions)**
19. Share your public or NDA roadmap for the next 12 months. Which items are committed vs. directional?
20. Describe one capability the platform does NOT currently support that customers frequently request.

**Construction test**: each question must be answerable by any vendor in the Step 1 tool-class universe without the question prejudicing the answer. No "does your platform do X better than Y?" No "how does your CSP compare to alternatives?" Questions are about the vendor's own platform, not comparisons.

### Step 6 — Produce the Shortlist Scoring Rubric (Blank)

The rubric is a blank template. The buyer supplies vendor columns and scores. The framework ships:

- **Row structure**: one row per evaluation dimension (12 rows), with weight in the second column
- **Column structure**: first column = dimension, second column = weight, columns 3-N = vendor A, vendor B, vendor C... (blank; buyer fills)
- **Per-cell scoring spec**: each cell holds a 1-5 integer score with a short evidence note (2-3 sentences citing the RFP response that justifies the score)
- **Row calculation**: dimension weight × vendor score = weighted contribution
- **Column total**: sum of weighted contributions = vendor's framework score
- **Tie-break**: if two vendors land within 5 points of each other, the Step 7 decision framework takes over

The rubric is **vendor-blank** when the skill emits it. If the skill output contains any vendor name in the rubric, the selection has been compromised and the output is rejected.

### Step 7 — Decision Framework (Combining Score + Non-Scoreable Factors)

The shortlist score is a necessary condition for a good decision; it is not a sufficient one. Four non-scoreable factors must be combined with the rubric result before the buyer commits:

1. **Vendor relationship reality** — does the buyer have a working relationship with the account team? A high rubric score with a hostile or absentee account team is a bad buy. Ask: "If I have a P1 issue at 4pm on a Friday, who picks up?"
2. **Reference depth** — beyond the three required references in Category I, did the buyer talk to any of those references in a 30-minute call? A one-line email reference is not a reference. This is a gate, not a tiebreaker.
3. **Operator fit** — did at least one CSM who will use the tool daily see a demo and give a verdict? An executive selection over operator objections is a procurement failure that will surface 6 months in.
4. **Walk-away alternative** — in a renewal negotiation, does the buyer have a credible walk-away option? No alternative = no leverage = no negotiation.

The decision framework is structural: the buyer records their position on each of the four non-scoreable factors alongside the rubric result. A vendor cannot be selected if ANY of the four is a hard negative.

---

## Output Structure

The skill produces one markdown file at a company-appropriate location (e.g., `{Company}/Product/cs-tool-selection-framework-{date}.md`) with these sections:

1. **Framework Summary** — one paragraph, plus headline fields: tool-class classification, primary archetype, hybrid flag, budget ceiling, team size
2. **Segmentation Input Reference** — pointer to the `/cs-segmentation-model` output consumed, with tier distribution
3. **Health-Score Input Reference** — pointer to the `/health-score-design` output consumed, with signal families and consumption requirements
4. **Tool-Need Classification** — Step 1 output: which class(es) of tool are in scope
5. **Segment-to-Archetype Mapping** — Step 2 output: the mapping table for this buyer's portfolio
6. **Health-Score Consumption Requirements** — Step 3 output: the four load-bearing answers
7. **Evaluation Criteria Table** — Step 4 output: 12 dimensions with weights, scoring spec, "why this matters"
8. **RFP Question Template** — Step 5 output: the 20 questions across 10 categories
9. **Shortlist Scoring Rubric** — Step 6 output: blank vendor-column template
10. **Decision Framework** — Step 7 output: the four non-scoreable factors and how to combine with rubric score
11. **Anti-Patterns** — the common selection failures (see below)
12. **Framework Confidence** — any input gaps that limited the framework (e.g., "no budget provided; pricing-model dimension cannot eliminate archetypes on affordability grounds")

---

## Quality Gates

The skill applies these checks before emitting the final output. A check failure aborts the skill and routes back to the relevant step.

1. **Zero vendor names in output** — grep the entire output for vendor names from a standard reference list (the skill's internal check). If any vendor name appears, the output is rejected and rewritten. This is the single most load-bearing gate in the skill.
2. **Segmentation input present and feeding archetype mapping** — the output section 5 cites specific tiers from the segmentation. "The segmentation shows 40% Mid-Touch, 20% High-Touch..." If the section is generic, segmentation was not actually consumed and the skill fails.
3. **Health-score input present and feeding consumption requirements** — section 6 cites specific signal families and consumption surfaces from the health-score model. Generic = fail.
4. **Evaluation criteria weights sum to exactly 100** — integer weights, exact sum. Off-by-one aborts.
5. **RFP questions leading-question-free** — test: can any vendor in any of the Step 1 tool classes answer the question without being prejudiced? If the answer is no, the question is rewritten.
6. **Shortlist rubric is vendor-blank** — columns 3-N have no vendor names; the template is a skeleton.
7. **Decision framework addresses non-scoreable factors explicitly** — all four (vendor relationship, reference depth, operator fit, walk-away alternative) appear in section 10.
8. **Anti-patterns section present** — section 11 is non-empty and contains the named failures from Step 7.
9. **Pricing-model comparison included** — the four models (per-seat, per-account, platform-flat, usage-based) are compared in section 7 (dimension 6) with fit-to-growth-shape guidance.

---

## Evaluation Dimensions — Extended Notes

The 12 dimensions above are the full set. Notes on the three most frequently under-weighted:

- **Operator experience** (dimension 12) — almost every enterprise selection under-weights this. The CSM using the tool daily has a higher impact on tool ROI than the CRO who signed the contract. Force at least one CSM into the demo cycle.
- **Total cost of ownership 3-year** (dimension 11) — sticker price is 30-60% of TCO in CS tooling. Implementation, ongoing PS, internal Ops time, and the cost of switching to a second tool if the first fails — all load-bearing. The 3-year horizon is mandatory because year-1 numbers always favor the vendor with the lowest sticker.
- **Vendor reference relevance** (dimension 9) — references in a different segment or ARR band are decorative. A $10M ARR SaaS asking for references at $100M ARR enterprises is buying a tool calibrated for a book it does not have. Force segment-matched references.

The skill's 12th dimension is **operator experience**, which was added beyond the suggested 8-12 baseline. Rationale: the baseline list focused on the procurement-team perspective (integration, security, pricing, implementation) and risked producing a selection that an executive would sign and a CSM would hate. Operator experience is the dimension that fails loudest 6 months after go-live — the CSM opens a spreadsheet instead of the tool because the tool is slower than the spreadsheet — and skipping it is the fastest way to waste a CS tooling budget.

---

## Anti-Patterns

The common failures this framework is designed to prevent:

1. **Vendor-led scoping** — letting a vendor define the evaluation criteria. Every vendor will optimize for their own strengths. The criteria must come from the buyer's segmentation + health-score model, not from a vendor's demo deck.
2. **Feature-checklist without weight** — buying the longest feature list rather than the highest-leverage features for the buyer's segmentation. A feature the buyer will never use because their book is PLG does not earn weight just because it exists.
3. **Enterprise tooling on PLG segmentation** — the canonical expensive mistake. Full CSP pricing, capability 80% unused, CSMs pile data into spreadsheets because the platform was built for a different operating model.
4. **Renewal negotiation without a walk-away alternative** — the buyer cannot negotiate without credible alternatives. A renewal cycle that skips the shortlist step is not a negotiation; it is a rubber stamp.
5. **Ignoring the operator experience** — tools chosen by executives, used by CSMs. The operator must be in the demo loop. The CSM veto is a feature.
6. **Choosing the vendor that presents best** — sales teams vary; platforms vary less. A vendor with a weak demo and strong references is often a better buy than a vendor with a strong demo and weak references.
7. **Scoring the shortlist before writing the weights** — the worst procurement failure. When the weights are tuned after the scores are known, they are calibrated to produce the pre-decided winner. Weights must be locked before any vendor is scored.
8. **Skipping the reference calls** — a one-line email testimonial is not a reference. A 30-minute call with a segment-matched customer where the reference says "we almost didn't buy because X" is a reference. Do the calls.
9. **Buying for the aspirational book, not the real one** — selection based on "where we want to be in 3 years" rather than "where we are and where we'll be in 12 months" leads to capability overkill and integration pain. Buy for the 12-month shape, re-evaluate when it changes.

---

## Related Skills + Hand-Off

This skill sits at the end of the CS foundational triad (segmentation → health score → tool selection) and feeds operational planning:

**Required inputs**:
- **`/cs-segmentation-model`** — tier shape determines archetype
- **`/health-score-design`** — signal origin and consumption determine health-scoring RFP requirements

**Output feeds**:
- **Future `/cs-tool-implementation-plan`** — not yet scoped; will consume the selected vendor and produce an implementation timeline, integration plan, and rollout sequence
- **Future `/vendor-negotiation-prep`** — not yet scoped; will consume the shortlist result and produce a negotiation brief (leverage points, walk-away thresholds, contract red lines)

**Cross-team consultation**:
- **`@proposal-writer`** (Sales Engineering Extension Team) — for RFP delivery formatting, response parsing, and scoring hygiene when the buyer is running a structured RFP process
- **`@contracts-counsel`** (Legal Extension Team) — for vendor contract review once a shortlist winner emerges; contract terms are not a dimension the framework scores but they can be a hard negative
- **`@bizops`** (Product Org) — for TCO modeling, especially the 3-year cost curves at different growth scenarios
- **`@cs-ops`** — for operator-experience grounding; the CS Ops specialist has the best line of sight on which current tools' quirks are load-bearing vs. fixable

Default delegation pattern is **Pattern 1 Consultation** (see `rules/delegation-protocol.md`). The skill consults `@cs-ops` for segmentation-tier realities, `@bizops` for TCO modeling, and `@cs-dir` (owner) for pricing-model tradeoffs.

Pattern 5 Adversarial Review is NOT required for this skill. Tool selection is a craft with established conventions; the cost of a missed edge case is a procurement do-over, not a liability event. The vendor-blank constraint + the Step 7 decision framework are themselves the structural adversarial check — they are designed to prevent the specific failures that adversarial review would otherwise catch.

---

## Birth Test

Every new skill must be birth-tested against a real or synthetic portfolio before v1.0.0. For `/cs-tool-selection`, the birth test runs against the **Legionis** context — consistent with the `/cs-segmentation-model` and `/health-score-design` birth tests that preceded it, so the full triad chains cleanly against one buyer.

Legionis is a first-CS-hire case: 1 CS Lead, $50k/year year-1 budget ceiling, a 4-tier segmentation (Low / Mid / High / Enterprise), and a Tier 3 cold-start health score model. It exercises:

- Tool-need classification (mixed-book → hybrid archetype)
- Segment-to-archetype mapping across 4 tiers
- Health-score consumption requirements (score originates in BI layer / product analytics given no CSP)
- Evaluation criteria with weights calibrated for a 1-person CS function
- RFP question template (vendor-neutral, 20 questions)
- Shortlist rubric (blank — Legionis will fill vendor columns during actual procurement)
- Decision framework with Legionis-specific non-scoreable factors

The birth test output lives at: `Legionis/Product/cs-tool-selection-birth-test-2026-04-11.md`

See the birth test file for the full tier-to-archetype mapping, the Legionis-tuned weight calibration, and the framework confidence gaps specific to a pre-PMF first-CS-hire buyer.

---

## ROI

Time saved on drafting and triage: the skill produces in ~25 minutes what a CS Ops lead + CS Director working session would typically draft in 10–16 hours — tool-class classification, archetype mapping, evaluation criteria with weights and scoring specs, RFP question template, shortlist rubric, decision framework, and anti-pattern documentation. Blended CS Ops rate: $175/hr.

Standard output after skill invocation:

> ⏱️ ~[X] hrs saved on drafting and triage in [Y] min, [Z]k tkns ~$[C] cost, Value ~$[V]
