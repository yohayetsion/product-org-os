---
name: pirate-metrics
description: "Map your product's AARRR funnel (Acquisition, Activation, Retention, Revenue, Referral) and identify the One Metric That Matters. Activate when: \"pirate metrics\", \"AARRR\", \"acquisition activation retention\", \"funnel metrics\", \"growth funnel\", \"McClure\", \"startup metrics\", \"RARRA\" Do NOT activate for: north star metric (/north-star-metric), growth model (/growth-model), SaaS health check (/saas-health-check)"
argument-hint: "[product name] or [update path/to/pirate-metrics.md]"
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: metrics
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided (`@path/to/pirate-metrics.md`) | UPDATE | 100% |
| "create", "new", "map funnel" in input | CREATE | 100% |
| "find", "search", "list AARRR" | FIND | 100% |
| "the funnel", "our AARRR", "our pirate metrics" | UPDATE | 85% |
| Just product name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete AARRR funnel map with stage definitions, metrics, benchmarks, funnel analysis, and OMTM recommendation using template below.

**UPDATE**:
1. Read existing pirate metrics document (search if path not provided)
2. Preserve unchanged stages exactly
3. Update metrics, benchmarks, or OMTM recommendation
4. Show diff summary: "Updated: [sections]. Unchanged: [sections]."
5. Note: Changing the OMTM is a strategic pivot; document rationale for the shift

**FIND**:
1. Search paths below for pirate metrics documents
2. Present results: title, product, current OMTM, path
3. Ask: "Update one of these, or create new?"

### Search Locations for Pirate Metrics

- `product/`
- `metrics/`
- `growth/`
- `strategy/`

---
## Gotchas

- Never fabricate conversion rates, funnel numbers, or benchmark data -- use frameworks with [TBD] placeholders
- Activation is NOT signup -- it is the moment the user experiences core value (the "aha moment")
- RARRA is not a replacement for AARRR; it is a prioritization reordering for products past product-market fit
- The OMTM changes as the product matures -- an early-stage product focuses on Activation; a scaling product may focus on Retention or Revenue



Map the **AARRR Pirate Metrics** funnel for a product: define each stage, identify the key metrics and events, analyze stage-to-stage conversion, and recommend the One Metric That Matters.

## Vision to Value Phase

**Phase 5: Business & Customer Outcomes** - Pirate Metrics provide the measurement framework for understanding where customers succeed and where they fall off across the entire lifecycle.

**Prerequisites**: Phase 1-2 complete (target market defined, value proposition clear, product launched or in beta)
**Outputs used by**: Phase 5 (value realization, customer health), Phase 6 (outcome reviews, retrospectives), Phase 3 (roadmap prioritization informed by funnel bottlenecks)

## Methodology

<!-- Source: AARRR / Pirate Metrics -- Dave McClure, "Startup Metrics for Pirates" (2007 presentation, 500 Startups). McClure proposed the five-stage funnel as a simple framework for startup growth metrics. The name "Pirate Metrics" comes from the AARRR acronym sounding like a pirate. -->

<!-- Source: RARRA reordering -- Brian Balfour (Reforge, former VP Growth at HubSpot) and others have advocated reordering as Retention -> Activation -> Referral -> Revenue -> Acquisition, arguing that retention is the foundation all other metrics depend on. -->

<!-- Source: One Metric That Matters (OMTM) -- Alistair Croll and Benjamin Yoskovitz, "Lean Analytics" (2013, O'Reilly). The idea that at any given stage of a startup, there is one metric that deserves more attention than all others because it captures the critical constraint. -->

<!-- Source: Activation and "Aha Moment" -- Chamath Palihapitiya (Facebook VP Growth) popularized the concept that activation to the core value moment is the most critical early metric. Facebook's "7 friends in 10 days" is the canonical example of identifying the aha moment. -->

### The AARRR Stages

| Stage | Key Question | Description | Example Metrics |
|-------|-------------|-------------|-----------------|
| **Acquisition** | How do users find you? | Channels and campaigns that drive users to your product | Traffic by channel, signups, CAC by channel, click-through rates |
| **Activation** | Do they have a great first experience? | The moment users experience core value for the first time | Onboarding completion, aha moment reached, time-to-value, setup completion |
| **Retention** | Do they come back? | Continued engagement over time | D1/D7/D30 retention, churn rate, DAU/MAU ratio, session frequency |
| **Revenue** | Do they pay? | Conversion from free to paid, expansion, monetization | Trial-to-paid conversion, ARPU, MRR, LTV, expansion revenue |
| **Referral** | Do they tell others? | Users bringing in new users organically | K-factor, NPS, referral rate, viral coefficient, invites sent |

### Funnel Mapping Process

1. **Define the specific events** that mark each stage transition for YOUR product (not generic)
2. **Identify the conversion rate** between each adjacent stage
3. **Find the biggest drop-off** -- this is your constraint
4. **Pick the OMTM** -- the metric at the stage with the biggest drop-off or highest leverage

### RARRA Variant (Retention-First)

For products past product-market fit, RARRA reorders the priority:

| Priority | Stage | Rationale |
|----------|-------|-----------|
| 1 | **Retention** | If users don't stay, nothing else matters |
| 2 | **Activation** | Improve the first experience to drive retention |
| 3 | **Referral** | Happy retained users are the best acquisition channel |
| 4 | **Revenue** | Monetize engaged users |
| 5 | **Acquisition** | Scale what already works |

### OMTM Selection Criteria

| Criterion | Description |
|-----------|-------------|
| **Biggest bottleneck** | The stage with the largest drop-off in your funnel |
| **Highest leverage** | The stage where improvement has the largest downstream impact |
| **Actionable** | Your team can directly influence this metric |
| **Stage-appropriate** | Matches your product's current maturity |

### Benchmark Ranges (Industry Averages)

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| Signup-to-Activation | <15% | 15-30% | 30-50% | >50% |
| D1 Retention | <10% | 10-25% | 25-40% | >40% |
| D30 Retention | <5% | 5-15% | 15-25% | >25% |
| Free-to-Paid | <1% | 1-3% | 3-7% | >7% |
| DAU/MAU | <10% | 10-20% | 20-40% | >40% |
| NPS | <0 | 0-30 | 30-50 | >50 |

*Note: Benchmarks vary significantly by industry, product type, and business model. Use as directional guidance only.*

## Output Structure

```markdown
# Pirate Metrics (AARRR): [Product Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Single accountable person -- typically Growth Lead or VP Product]
**Product**: [Product name]
**Product Stage**: Pre-PMF / Early Growth / Scaling / Mature
**Framework Variant**: AARRR / RARRA

## Funnel Overview

| Stage | Defining Event | Current Metric | Benchmark | Status |
|-------|---------------|---------------|-----------|--------|
| **Acquisition** | [Event] | [TBD] | [Range] | [Above/At/Below] |
| **Activation** | [Event] | [TBD] | [Range] | [Above/At/Below] |
| **Retention** | [Event] | [TBD] | [Range] | [Above/At/Below] |
| **Revenue** | [Event] | [TBD] | [Range] | [Above/At/Below] |
| **Referral** | [Event] | [TBD] | [Range] | [Above/At/Below] |

## Stage Detail

### Acquisition

**Key Question**: How do users find [Product Name]?

**Defining Event**: [The specific event that marks a user as "acquired" -- e.g., visits landing page, creates account]

**Metrics**:
| Metric | Current | Target | Source |
|--------|---------|--------|--------|
| [Traffic by channel] | [TBD] | [TBD] | [Analytics tool] |
| [Signup rate] | [TBD] | [TBD] | [Source] |
| [CAC by channel] | [TBD] | [TBD] | [Source] |

**Top Channels**:
| Channel | Volume | Conversion | CAC | Trend |
|---------|--------|-----------|-----|-------|
| [Channel 1] | [TBD] | [TBD] | [TBD] | [Up/Flat/Down] |
| [Channel 2] | [TBD] | [TBD] | [TBD] | [Up/Flat/Down] |

### Activation

**Key Question**: Do users experience the core value of [Product Name]?

**Aha Moment**: [Describe the specific moment when users first experience the product's core value]

**Defining Event**: [The specific measurable event -- e.g., completes first project, sends first message, invites teammate]

**Metrics**:
| Metric | Current | Target | Source |
|--------|---------|--------|--------|
| [Onboarding completion] | [TBD] | [TBD] | [Source] |
| [Time to aha moment] | [TBD] | [TBD] | [Source] |
| [Setup completion rate] | [TBD] | [TBD] | [Source] |

### Retention

**Key Question**: Do users keep coming back to [Product Name]?

**Defining Event**: [The specific event that marks "retained" -- e.g., returns within 7 days, active in trailing 30 days]

**Metrics**:
| Metric | Current | Target | Source |
|--------|---------|--------|--------|
| [D1 retention] | [TBD] | [TBD] | [Source] |
| [D7 retention] | [TBD] | [TBD] | [Source] |
| [D30 retention] | [TBD] | [TBD] | [Source] |
| [DAU/MAU ratio] | [TBD] | [TBD] | [Source] |

**Retention Curve Shape**: [Flattening (healthy) / Declining to zero (problem) / Unknown]

### Revenue

**Key Question**: Do users pay for [Product Name]?

**Defining Event**: [The specific monetization event -- e.g., upgrades to paid, first purchase, subscription renewal]

**Metrics**:
| Metric | Current | Target | Source |
|--------|---------|--------|--------|
| [Free-to-paid conversion] | [TBD] | [TBD] | [Source] |
| [ARPU] | [TBD] | [TBD] | [Source] |
| [LTV] | [TBD] | [TBD] | [Source] |
| [MRR / ARR] | [TBD] | [TBD] | [Source] |

### Referral

**Key Question**: Do users tell others about [Product Name]?

**Defining Event**: [The specific referral event -- e.g., sends invite, shares referral link, writes review]

**Metrics**:
| Metric | Current | Target | Source |
|--------|---------|--------|--------|
| [K-factor] | [TBD] | [TBD] | [Source] |
| [NPS] | [TBD] | [TBD] | [Source] |
| [Referral rate] | [TBD] | [TBD] | [Source] |
| [Viral coefficient] | [TBD] | [TBD] | [Source] |

## Funnel Analysis

### Stage-to-Stage Conversion

```
Acquisition --> Activation:  [TBD]% conversion
Activation  --> Retention:   [TBD]% conversion
Retention   --> Revenue:     [TBD]% conversion
Revenue     --> Referral:    [TBD]% conversion
```

### Biggest Drop-Off

**Stage**: [Where the largest conversion drop occurs]
**Current Conversion**: [TBD]%
**Impact**: [Why this matters -- downstream effects of this drop-off]

## One Metric That Matters (OMTM)

**OMTM**: [The single metric to focus on right now]
**Stage**: [Which AARRR stage it belongs to]
**Current Value**: [TBD]
**Target Value**: [TBD]
**Timeframe**: [By when]

**Why This Metric**:
[2-3 sentences explaining why this is the right metric to focus on given the product's current stage and funnel analysis]

**OMTM Validation**:
| Criterion | Pass? | Evidence |
|-----------|-------|----------|
| Biggest bottleneck or highest leverage | [Yes/No] | [Why] |
| Actionable by the team | [Yes/No] | [Who can influence it] |
| Stage-appropriate for product maturity | [Yes/No] | [Why] |
| Moving it will improve downstream stages | [Yes/No] | [How] |

## OMTM Evolution Plan

| Product Stage | Expected OMTM | Rationale |
|---------------|---------------|-----------|
| Pre-PMF | [Activation metric] | Validate core value delivery |
| Early Growth | [Retention metric] | Confirm users stay |
| Scaling | [Acquisition or Revenue] | Grow efficiently |
| Mature | [Revenue or Referral] | Optimize unit economics |

## Improvement Hypotheses

| # | Hypothesis | Stage | Expected Impact | Validation Method |
|---|-----------|-------|-----------------|-------------------|
| 1 | [If we do X, then Y will improve by Z] | [Stage] | [Impact on OMTM] | [How to test] |
| 2 | [Hypothesis] | [Stage] | [Impact] | [Test] |
| 3 | [Hypothesis] | [Stage] | [Impact] | [Test] |
```

## Instructions

1. Ask clarifying questions about the product's current funnel, available data, and product stage
2. **Check prior context**: Run `/context-recall [product]` to find related growth models, strategic bets, and positioning
3. **Check feedback**: Run `/feedback-recall [growth/retention/activation/churn]` for customer signals
4. Reference any analytics dashboards, usage data, or strategy documents provided via @file syntax
5. Define the specific events that mark each stage transition -- reject generic definitions
6. Use [TBD] for any metric values not provided by the user; never fabricate funnel numbers
7. Identify the biggest drop-off and recommend the OMTM with clear rationale
8. Include the RARRA variant discussion if the product is past product-market fit
9. Save in metrics/ or product/ folder
10. Offer to create presentation version using /present

## Context Integration

After generating the pirate metrics analysis:

1. **Offer to save**: Ask "Should I save this to the context registry? (`/context-save`)"
2. If yes, extract and save:
   - AARRR funnel map and OMTM to context
   - Link to related growth model, NSM, and strategic bets
   - Improvement hypotheses to `context/assumptions/registry.md`
3. Suggest using OMTM as input to `/north-star-metric` and `/experiment-design`
