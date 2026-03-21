---
name: prioritize-features
description: |
  Prioritize a list of features or initiatives using proven frameworks (RICE, Kano, MoSCoW, WSJF). Produces scored, ranked output with rationale.
  Activate when: "prioritize", "rank features", "RICE score", "Kano", "MoSCoW", "feature scoring", "what to build first", "priority matrix", "WSJF", "which features first", "stack rank"
  Do NOT activate for: roadmap planning (/product-roadmap), commitment checks (/commitment-check), strategic bet formulation (/strategic-bet)
argument-hint: [list of features/initiatives] or [update path/to/prioritization.md]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: product-management
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "re-score" in input | UPDATE | 100% |
| File path provided (`@path/to/prioritization.md`) | UPDATE | 100% |
| "create", "new", "prioritize these" in input | CREATE | 100% |
| "find", "search", "list prioritizations" | FIND | 100% |
| "the prioritization", "our ranking" | UPDATE | 85% |
| Just a list of features | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Gather feature list, select framework(s), score, produce ranked output.

**UPDATE**:
1. Read existing prioritization (search if path not provided)
2. Preserve scores for unchanged items
3. Re-score modified or added items
4. Show diff summary: "Added: [items]. Re-scored: [items]. Unchanged: [items]."

**FIND**:
1. Search paths below for prioritization documents
2. Present results: title, framework used, item count, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `product/`
- `roadmap/`
- `planning/`
- `prioritization/`

---
## Gotchas

- Prioritization criteria must be stated explicitly — different frameworks (RICE, Kano, MoSCoW) give different results
- Never fabricate reach, impact, or confidence scores — use data or explicitly label as team estimates
- Prioritization without strategic alignment is just sorting — connect to strategic bets



## Vision to Value Phase

**Phase 3: Strategic Commitments** - Prioritization converts decisions into executable commitments by ranking what to build and in what order.

**Prerequisites**: Phase 2 complete (strategic decisions made, business viability confirmed)
**Outputs used by**: `/product-roadmap`, `/prd`, `/commitment-check`

## Methodology

<!-- Source: RICE Scoring — Intercom (Sean McBride, ~2014). Formula: (Reach x Impact x Confidence) / Effort. Originally developed at Intercom to prioritize product ideas objectively. Reach = people or events per time period. Impact = estimated effect per person. Confidence = percentage certainty in estimates. Effort = person-months of work. -->

<!-- Source: Kano Model — Noriaki Kano, "Attractive Quality and Must-Be Quality" (1984), Tokyo University of Science. Categories: Must-Be (Basic), Performance (One-Dimensional), Attractive (Delighters), Indifferent, Reverse. Uses paired functional/dysfunctional questions to classify features. Key insight: satisfaction is not linear — some features only cause dissatisfaction when absent, others delight only when present. -->

<!-- Source: MoSCoW Prioritization — Dai Clegg, Oracle UK (1994). Adopted by DSDM Consortium for Agile projects. Must Have, Should Have, Could Have, Won't Have (this time). Budget allocation rule: Must ~60%, Should ~20%, Could ~20%. Key principle: Must Haves are non-negotiable for the minimum usable subset. -->

<!-- Source: WSJF (Weighted Shortest Job First) — Don Reinertsen, "The Principles of Product Development Flow" (2009). Adopted by SAFe (Scaled Agile Framework). Formula: (Business Value + Time Criticality + Risk Reduction/Opportunity Enablement) / Job Size. Based on Cost of Delay economics. Key insight: prioritize by economic value delivered per unit of time, not just by value alone. -->

### Framework Selection Guide

| Framework | Best For | Strengths | Limitations |
|-----------|----------|-----------|-------------|
| **RICE** | Feature backlogs, product teams | Quantitative, accounts for reach | Effort estimation can be unreliable |
| **Kano** | Customer-facing features | Reveals non-obvious priorities | Requires customer survey data |
| **MoSCoW** | Release planning, MVP scoping | Simple, stakeholder-friendly | Subjective without scoring |
| **WSJF** | Agile/SAFe teams, flow-based | Accounts for time value | Requires relative sizing discipline |

When unsure, ask the user which framework to apply. If they say "just prioritize", default to RICE.

### RICE Scoring

| Component | Scale | Guidance |
|-----------|-------|---------|
| **Reach** | People or events per quarter | How many users/customers will this affect in a quarter? |
| **Impact** | 3 = Massive, 2 = High, 1 = Medium, 0.5 = Low, 0.25 = Minimal | How much will this move the needle per person reached? |
| **Confidence** | 100% = High, 80% = Medium, 50% = Low | How confident are you in these estimates? |
| **Effort** | Person-months | How many person-months will this take? |

**Formula**: RICE Score = (Reach x Impact x Confidence) / Effort

### Kano Classification

For each feature, ask the functional/dysfunctional question pair:

- **Functional**: "How would you feel if this feature were present?"
- **Dysfunctional**: "How would you feel if this feature were absent?"

| Response Options | Code |
|-----------------|------|
| I like it | L |
| I expect it | E |
| I am neutral | N |
| I can tolerate it | T |
| I dislike it | D |

**Classification matrix** (Functional x Dysfunctional):

|  | Like | Expect | Neutral | Tolerate | Dislike |
|--|------|--------|---------|----------|---------|
| **Like** | Q | A | A | A | O |
| **Expect** | R | I | I | I | M |
| **Neutral** | R | I | I | I | M |
| **Tolerate** | R | I | I | I | M |
| **Dislike** | R | R | R | R | Q |

M = Must-Be, O = One-Dimensional, A = Attractive, I = Indifferent, R = Reverse, Q = Questionable

**Priority order**: Must-Be > One-Dimensional > Attractive > Indifferent

### MoSCoW Classification

| Category | Definition | Budget Target |
|----------|-----------|---------------|
| **Must Have** | Non-negotiable for this release. Without it, the release is a failure. | ~60% |
| **Should Have** | Important but not critical. Painful to leave out but workarounds exist. | ~20% |
| **Could Have** | Desirable. Included if time/budget allows. | ~20% |
| **Won't Have** | Agreed to be out of scope this time. May be reconsidered later. | 0% |

### WSJF Scoring

| Component | Scale (Fibonacci: 1, 2, 3, 5, 8, 13, 20) | Question |
|-----------|------|----------|
| **Business Value** | Relative | What is the relative business value? |
| **Time Criticality** | Relative | How much does delay cost us? |
| **Risk Reduction / Opportunity Enablement** | Relative | Does this reduce risk or enable new opportunities? |
| **Job Size** | Relative | How big is this work item? |

**Formula**: WSJF = (Business Value + Time Criticality + Risk Reduction) / Job Size

## Output Structure

```markdown
# Feature Prioritization: [Context/Product Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this prioritization]
**Framework(s)**: [RICE / Kano / MoSCoW / WSJF]
**Input source**: [Backlog, stakeholder request, etc.]

## Features Under Consideration

| # | Feature/Initiative | Description |
|---|-------------------|-------------|
| 1 | [Feature name] | [Brief description] |
| 2 | [Feature name] | [Brief description] |

## Scoring

### [Framework Name] Scores

[Framework-specific scoring table — see framework sections above]

## Ranked Results

| Rank | Feature | Score | Category/Tier | Rationale |
|------|---------|-------|---------------|-----------|
| 1 | [Feature] | [Score] | [Must/High/etc.] | [Why it ranked here] |
| 2 | [Feature] | [Score] | [Should/Med/etc.] | [Why it ranked here] |

## Key Insights

- **Top priority**: [Feature] because [reason]
- **Surprising result**: [Feature] ranked [higher/lower] than expected because [reason]
- **Tension**: [Feature A] vs [Feature B] — [tradeoff description]

## Assumptions & Caveats

- [Key assumptions that affect the scoring]
- [Data gaps that reduce confidence]
- [Recommendations for improving confidence]

## Next Steps

- [ ] Validate scores with [stakeholders]
- [ ] Feed top priorities into roadmap via `/product-roadmap`
- [ ] Design experiments for low-confidence items via `/experiment-design`
```

## Instructions

1. Ask the user for: (a) the list of features/initiatives, (b) which framework(s) to use (default: RICE)
2. If the user provides features without descriptions, ask for brief descriptions
3. For RICE: ask the user to estimate Reach and Effort; propose Impact and Confidence based on context
4. For Kano: note that ideal Kano requires customer survey data; offer to classify based on product knowledge as a proxy
5. For MoSCoW: facilitate classification discussion; challenge "Must Have" inflation
6. For WSJF: use relative sizing (Fibonacci); anchor with the smallest item as 1
7. Multiple frameworks can be applied to the same list for cross-validation
8. Save output as markdown file
9. Offer `/product-roadmap` to convert prioritized list into a roadmap

## Integration

- Links to `/product-roadmap` (prioritized features feed roadmap themes)
- Links to `/commitment-check` (validate that prioritized commitments are achievable)
- Links to `/assumption-map` (surface assumptions behind scoring)
- Links to `/experiment-design` (test assumptions for low-confidence scores)
- Links to `/context-recall` (check past prioritization decisions for consistency)
