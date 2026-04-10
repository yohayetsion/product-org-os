---
name: saas-health-check
description: "Diagnostic framework for assessing the health of a SaaS business across key metric categories. Activate when: \"SaaS health\", \"SaaS metrics\", \"SaaS diagnostic\", \"health check\", \"MRR analysis\", \"churn analysis\", \"unit economics\", \"SaaS scorecard\", \"business health\" Do NOT activate for: pirate metrics (/pirate-metrics), north star metric (/north-star-metric), growth model (/growth-model), customer health scorecard (/customer-health-scorecard — that's per-customer, this is business-level)"
argument-hint: "[product name or stage] or [update path/to/saas-health-check.md]"
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
| File path provided (`@path/to/saas-health-check.md`) | UPDATE | 100% |
| "create", "new", "run" in input | CREATE | 100% |
| "find", "search", "list health checks" | FIND | 100% |
| "the health check", "our SaaS metrics" | UPDATE | 85% |
| Just product name or stage | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new SaaS health scorecard using template below.

**UPDATE**:
1. Read existing health check (search if path not provided)
2. Preserve unchanged sections exactly
3. Update metrics with new data, recalculate traffic light ratings
4. Add new period to Historical Trend
5. Show diff summary: "Updated: [sections]. Previous overall: X → Current: Y."

**FIND**:
1. Search paths below for health check documents
2. Present results: product, overall rating, last updated, path
3. Ask: "Update one of these, or create new?"

### Search Locations for SaaS Health Checks

- `metrics/`
- `product/`
- `strategy/`
- `analytics/`

---
## Gotchas

- This is a **business-level** diagnostic — for per-customer health, use `/customer-health-scorecard`
- Benchmarks are stage-dependent — a 3% monthly churn rate is acceptable at pre-$1M ARR but alarming at $10M+
- Never fabricate metric values — use frameworks with [TBD] placeholders; only populate with user-provided data
- Quick Ratio and Rule of 40 require multiple inputs — flag which components are missing rather than skipping the calculation



Assess the **health of a SaaS business** across six metric dimensions, producing a traffic-light scorecard with stage-appropriate benchmarks and actionable recommendations.

## Vision to Value Phase

**Phase 5: Business & Customer Outcomes** - The SaaS health check evaluates whether the business model is working and where to focus improvement efforts.

**Prerequisites**: Phase 1-2 complete (product in market, revenue model defined, metrics instrumented)
**Outputs used by**: Phase 5 (value realization, north star metric tuning), Phase 6 (outcome reviews, retrospectives), Phase 2 (pricing strategy revisions, growth model updates)

## Methodology

<!-- Source: SaaS Metrics — David Skok, "SaaS Metrics 2.0" (forEntrepreneurs.com, 2013+). Skok is a serial entrepreneur and General Partner at Matrix Partners. His SaaS metrics framework is the industry standard reference. -->

<!-- Source: Rule of 40 — Brad Feld, Techstars / Foundry Group (popularized ~2015). The rule states that a healthy SaaS company's revenue growth rate + profit margin should exceed 40%. -->

<!-- Source: Digidai/product-manager-skills — SaaS metrics diagnostic patterns. Adapted with stage-appropriate benchmarks and traffic-light scoring. -->

<!-- Source: T2D3 framework — Neeraj Agrawal, Battery Ventures (2015). Triple-triple-double-double-double growth trajectory for enterprise SaaS: $2M→$6M→$18M→$36M→$72M→$144M ARR. -->

### Six Health Dimensions

| # | Dimension | What It Measures | Key Metrics |
|---|-----------|-----------------|-------------|
| 1 | **Growth** | Revenue momentum | MRR/ARR growth rate, net new MRR, expansion MRR |
| 2 | **Retention** | Customer and revenue stickiness | Logo churn, revenue churn, NRR |
| 3 | **Unit Economics** | Customer profitability | CAC, LTV, LTV:CAC ratio, CAC payback |
| 4 | **Engagement** | Product usage health | DAU/MAU, feature adoption, time-in-app |
| 5 | **Efficiency** | Capital and operational efficiency | Burn multiple, Rule of 40, magic number |
| 6 | **Revenue Quality** | Revenue durability and risk | Concentration, payment terms, annual vs monthly mix |

### Traffic Light Benchmarks by Stage

**Early Stage (Pre-$1M ARR)**:

| Dimension | Green | Yellow | Red |
|-----------|-------|--------|-----|
| Growth (m/m) | >15% | 5-15% | <5% |
| NRR | >110% | 100-110% | <100% |
| LTV:CAC | >5:1 | 3:1-5:1 | <3:1 |
| DAU/MAU | >25% | 15-25% | <15% |
| Rule of 40 | >40 | 20-40 | <20 |
| Top 10 customer concentration | <30% | 30-50% | >50% |

**Growth Stage ($1M-$10M ARR)**:

| Dimension | Green | Yellow | Red |
|-----------|-------|--------|-----|
| Growth (m/m) | >10% | 3-10% | <3% |
| NRR | >120% | 100-120% | <100% |
| LTV:CAC | >5:1 | 3:1-5:1 | <3:1 |
| DAU/MAU | >30% | 20-30% | <20% |
| Rule of 40 | >40 | 20-40 | <20 |
| Top 10 customer concentration | <20% | 20-40% | >40% |

**Scale Stage ($10M+ ARR)**:

| Dimension | Green | Yellow | Red |
|-----------|-------|--------|-----|
| Growth (y/y) | >50% | 20-50% | <20% |
| NRR | >130% | 110-130% | <110% |
| LTV:CAC | >5:1 | 3:1-5:1 | <3:1 |
| DAU/MAU | >30% | 20-30% | <20% |
| Rule of 40 | >40 | 25-40 | <25 |
| Top 10 customer concentration | <15% | 15-30% | >30% |

### Quick Ratio

**Quick Ratio** = (New MRR + Expansion MRR) / (Contraction MRR + Churned MRR)

| Rating | Quick Ratio | Interpretation |
|--------|------------|----------------|
| Green | >4.0 | Healthy — growth significantly outpaces losses |
| Yellow | 2.0-4.0 | Acceptable — monitor churn trends |
| Red | <2.0 | Leaky bucket — losing revenue almost as fast as gaining it |

## Output Structure

```markdown
# SaaS Health Check: [Product Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Single accountable person]
**Product**: [Product name]
**Stage**: Early (<$1M ARR) / Growth ($1M-$10M) / Scale ($10M+)
**Overall Health**: [Green / Yellow / Red]

## Executive Summary

[2-3 sentences: overall health verdict, strongest dimension, most urgent concern]

## Scorecard Overview

| # | Dimension | Rating | Score | Key Metric | Benchmark |
|---|-----------|--------|-------|------------|-----------|
| 1 | Growth | [Green/Yellow/Red] | [Value] | [Primary metric] | [Stage benchmark] |
| 2 | Retention | [Green/Yellow/Red] | [Value] | [Primary metric] | [Stage benchmark] |
| 3 | Unit Economics | [Green/Yellow/Red] | [Value] | [Primary metric] | [Stage benchmark] |
| 4 | Engagement | [Green/Yellow/Red] | [Value] | [Primary metric] | [Stage benchmark] |
| 5 | Efficiency | [Green/Yellow/Red] | [Value] | [Primary metric] | [Stage benchmark] |
| 6 | Revenue Quality | [Green/Yellow/Red] | [Value] | [Primary metric] | [Stage benchmark] |

**Quick Ratio**: [Value] — [Green/Yellow/Red]

## 1. Growth

| Metric | Current | Benchmark | Rating | Trend |
|--------|---------|-----------|--------|-------|
| MRR/ARR growth rate | [TBD] | [Stage-appropriate] | [G/Y/R] | [Up/Down/Flat] |
| Net new MRR | [TBD] | — | [G/Y/R] | [Up/Down/Flat] |
| Expansion MRR (% of new) | [TBD] | >30% | [G/Y/R] | [Up/Down/Flat] |

**T2D3 Trajectory Check**: [On track / Behind / Ahead] — [context]

## 2. Retention

| Metric | Current | Benchmark | Rating | Trend |
|--------|---------|-----------|--------|-------|
| Logo churn (monthly) | [TBD] | <2-3% | [G/Y/R] | [Up/Down/Flat] |
| Revenue churn (monthly) | [TBD] | <1-2% | [G/Y/R] | [Up/Down/Flat] |
| Net revenue retention (NRR) | [TBD] | [Stage-appropriate] | [G/Y/R] | [Up/Down/Flat] |

**Cohort Analysis**: [Summary of retention by cohort if data available]

## 3. Unit Economics

| Metric | Current | Benchmark | Rating | Trend |
|--------|---------|-----------|--------|-------|
| CAC | [TBD] | — | — | [Up/Down/Flat] |
| LTV | [TBD] | — | — | [Up/Down/Flat] |
| LTV:CAC ratio | [TBD] | >3:1 | [G/Y/R] | [Up/Down/Flat] |
| CAC payback (months) | [TBD] | <18 | [G/Y/R] | [Up/Down/Flat] |

## 4. Engagement

| Metric | Current | Benchmark | Rating | Trend |
|--------|---------|-----------|--------|-------|
| DAU/MAU ratio | [TBD] | [Stage-appropriate] | [G/Y/R] | [Up/Down/Flat] |
| Feature adoption (core features) | [TBD] | >60% | [G/Y/R] | [Up/Down/Flat] |
| Average session duration | [TBD] | [Varies by type] | [G/Y/R] | [Up/Down/Flat] |

## 5. Efficiency

| Metric | Current | Benchmark | Rating | Trend |
|--------|---------|-----------|--------|-------|
| Burn multiple | [TBD] | <2x | [G/Y/R] | [Up/Down/Flat] |
| Rule of 40 | [TBD] | >40 | [G/Y/R] | [Up/Down/Flat] |
| Magic number | [TBD] | >0.75 | [G/Y/R] | [Up/Down/Flat] |

**Rule of 40 Breakdown**: Growth rate [TBD]% + Profit margin [TBD]% = [TBD]

## 6. Revenue Quality

| Metric | Current | Benchmark | Rating | Trend |
|--------|---------|-----------|--------|-------|
| Top 10 customer concentration | [TBD] | [Stage-appropriate] | [G/Y/R] | [Up/Down/Flat] |
| Annual vs monthly contract mix | [TBD] | >50% annual | [G/Y/R] | [Up/Down/Flat] |
| Average contract length | [TBD] | — | — | [Up/Down/Flat] |

## Recommendations

### Urgent (Red Dimensions)
| Dimension | Issue | Recommended Action | Expected Impact |
|-----------|-------|-------------------|-----------------|
| [Dimension] | [What's wrong] | [What to do] | [Expected outcome] |

### Improve (Yellow Dimensions)
| Dimension | Issue | Recommended Action | Expected Impact |
|-----------|-------|-------------------|-----------------|
| [Dimension] | [What to monitor] | [What to do] | [Expected outcome] |

### Maintain (Green Dimensions)
| Dimension | Strength | How to Sustain |
|-----------|----------|----------------|
| [Dimension] | [What's working] | [Keep doing this] |

## Historical Trend

| Period | Overall | Growth | Retention | Unit Econ | Engagement | Efficiency | Rev Quality |
|--------|---------|--------|-----------|-----------|------------|------------|-------------|
| [T-2] | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] |
| [T-1] | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] |
| Current | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] | [G/Y/R] |
```

## Instructions

1. Ask about the product's stage (Early/Growth/Scale) and which metrics are available — do not assume data exists
2. **Check prior context**: Run `/context-recall [product]` to find related growth models, pricing strategies, and business cases
3. **Check feedback**: Run `/feedback-recall [revenue/churn/growth]` for relevant business signals
4. Reference any dashboards, analytics exports, or financial docs provided via @file syntax
5. Apply stage-appropriate benchmarks — never use Scale benchmarks for an Early-stage company
6. Calculate Quick Ratio and Rule of 40 when sufficient inputs are provided; flag missing components
7. Provide specific, actionable recommendations tied to each dimension's rating
8. Save in metrics/ or product/ folder
9. Offer to create presentation version using /present

## Integration

- **Inputs from**: `/growth-model` (growth loops inform Growth dimension), `/pricing-strategy` (pricing impacts Unit Economics), `/north-star-metric` (NSM informs Engagement benchmarks)
- **Outputs to**: `/outcome-review` (health check feeds periodic reviews), `/strategic-bet` (red dimensions may trigger strategic pivots), `/business-case` (unit economics feed investment decisions)
- **Related**: `/customer-health-scorecard` (per-customer health, not business-level), `/value-realization-report` (outcome tracking)

## Context Integration

After generating the health check:

1. **Offer to save**: Ask "Should I save this to the context registry? (`/context-save`)"
2. If yes, extract and save:
   - Overall health rating and dimension scores to context
   - Link to related growth models, pricing strategies, and business cases
   - Red-dimension issues as assumptions to validate in `context/assumptions/registry.md`
3. Suggest scheduling periodic updates (monthly for Growth/Scale, quarterly for Early)
