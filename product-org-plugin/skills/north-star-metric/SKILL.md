---
name: north-star-metric
description: |
  Define the North Star Metric and its input metrics tree for a product.
  Activate when: "north star metric", "NSM", "key metric", "core metric", "what to measure", "product metric", "success metric"
  Do NOT activate for: customer health scorecards (/customer-health-scorecard), OKR definition, analytics tracking implementation
argument-hint: [product name] or [update path/to/north-star-metric.md]
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
| "update", "revise", "change" in input | UPDATE | 100% |
| File path provided (`@path/to/north-star-metric.md`) | UPDATE | 100% |
| "create", "new", "define" in input | CREATE | 100% |
| "find", "search", "list NSMs" | FIND | 100% |
| "the north star", "our NSM" | UPDATE | 85% |
| Just product name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new North Star Metric definition using template below.

**UPDATE**:
1. Read existing NSM document (search if path not provided)
2. Preserve unchanged sections exactly
3. Update metric definition, input metrics, or measurement plan
4. Show diff summary: "Updated: [sections]. Unchanged: [sections]."
5. Note: Changing the NSM is a significant strategic shift; document rationale

**FIND**:
1. Search paths below for NSM definitions
2. Present results: title, product, current NSM, path
3. Ask: "Update one of these, or create new?"

### Search Locations for North Star Metrics

- `product/`
- `strategy/`
- `metrics/`
- `analytics/`

---
## Gotchas

- North Star must be a customer-value metric, not a revenue metric — revenue is a lagging indicator
- Input metrics must be actionable by teams — metrics nobody can influence are useless



Define the **North Star Metric** for a product: the single metric that best captures the core value delivered to customers, along with the input metrics tree that drives it.

## Vision to Value Phase

**Phase 5: Business & Customer Outcomes** - The NSM defines how we measure value delivery and track whether the product is succeeding at its core mission.

**Prerequisites**: Phase 1-2 complete (clear vision, customer segments, value proposition defined)
**Outputs used by**: Phase 5 (value realization, customer health), Phase 6 (outcome reviews, retrospectives), Phase 3 (roadmap prioritization)

## Methodology

<!-- Source: North Star Metric - Concept popularized by Sean Ellis (GrowthHackers, author of "Hacking Growth" with Morgan Brown, 2017) and Amplitude (analytics platform). The NSM is the single metric that best captures the core value your product delivers to customers. It serves as both a compass for product decisions and an alignment mechanism across teams. -->

<!-- Source: Properties of a Good NSM - Sean Ellis and Amplitude's "North Star Playbook" (2020). A good NSM: (1) Measures value delivered to customers, not vanity (not page views, not signups alone). (2) Is a leading indicator of revenue (predicts future business success). (3) Is actionable by the product team (teams can influence it through their work). (4) Is simple enough to rally the entire organization around. -->

<!-- Source: NSM Equation - Amplitude's North Star framework. NSM = f(Breadth, Depth, Frequency, Efficiency). Breadth = how many customers experience value. Depth = how much value per interaction. Frequency = how often they experience value. Efficiency = how quickly they reach value. Not all four dimensions apply to every product; typically 2-3 dominate. -->

<!-- Source: Input Metrics - Amplitude and Reforge. The 3-5 metrics that directly drive the NSM. These are what teams actually optimize day-to-day. The NSM itself is often a lagging indicator; input metrics are leading indicators that teams can act on. Input metrics should be: orthogonal (non-overlapping), actionable (a team can own it), predictive (correlates with NSM movement). -->

<!-- Source: NSM Examples - Industry knowledge, widely cited. Spotify = "Time Spent Listening" (value = music enjoyment). Airbnb = "Nights Booked" (value = travel experiences). Slack = "Messages Sent in Channels" (value = team communication). Facebook = "Daily Active Users" (value = social connection). HubSpot = "Weekly Active Teams" (value = team productivity). Amplitude = "Weekly Learning Users" (value = product insights). -->

<!-- Source: Inspired by phuryn/pm-skills north-star-metric skill. Adapted and expanded with NSM equation, validation checklist, and input metrics tree structure. -->

### NSM Selection Criteria

| Criterion | Test Question | Red Flag |
|-----------|--------------|----------|
| **Value-based** | Does it measure value customers receive? | Measures internal efficiency, not customer value |
| **Leading indicator** | Does it predict future revenue? | Lags revenue by too long to be actionable |
| **Actionable** | Can the product team influence it? | Driven by external factors (market, economy) |
| **Simple** | Can you explain it in one sentence? | Requires complex calculation to understand |
| **Non-gameable** | Is it hard to inflate artificially? | Easy to boost without real value creation |

### NSM Categories by Business Type

| Business Type | Typical NSM Pattern | Example |
|--------------|-------------------|---------|
| **Marketplace** | Transactions completed | Nights Booked (Airbnb) |
| **SaaS / Productivity** | Active usage of core feature | Messages Sent (Slack) |
| **Media / Content** | Time or content consumed | Time Spent Listening (Spotify) |
| **E-commerce** | Purchase frequency or volume | Weekly Purchases per Customer |
| **Platform** | Active integrations or connections | Weekly Active Integrations |
| **Social** | Active social interactions | Daily Active Users (Facebook) |

## Output Structure

```markdown
# North Star Metric: [Product Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Single accountable person - typically VP Product or CPO]
**Product**: [Product name - optional, for multi-product organizations]
**Status**: Proposed / Active / Under Review

## The North Star Metric

**NSM**: [Metric name in plain language]

**Definition**: [Precise definition - what counts, what doesn't, measurement window]

**Why This Metric**:
[2-3 sentences explaining why this metric best captures the core value the product delivers to customers]

## NSM Validation Checklist

| Criterion | Pass? | Evidence |
|-----------|-------|----------|
| Measures customer value delivered | [Yes/No/Partial] | [Why] |
| Leading indicator of revenue | [Yes/No/Partial] | [Correlation data or rationale] |
| Actionable by the product team | [Yes/No/Partial] | [Which teams can influence it] |
| Simple enough to rally around | [Yes/No/Partial] | [One-sentence explanation test] |
| Hard to game without creating real value | [Yes/No/Partial] | [Gaming risk assessment] |

**Validation Result**: [Strong NSM / Acceptable / Needs Refinement]

## NSM Equation

**[NSM] = f([Dimension 1], [Dimension 2], [Dimension 3])**

| Dimension | Definition | Relative Importance |
|-----------|-----------|-------------------|
| **Breadth** | [How many customers experience value] | [High/Medium/Low] |
| **Depth** | [How much value per interaction] | [High/Medium/Low] |
| **Frequency** | [How often they experience value] | [High/Medium/Low] |
| **Efficiency** | [How quickly they reach value] | [High/Medium/Low] |

**Dominant dimensions for this product**: [Which 2-3 matter most and why]

## Input Metrics Tree

```
[North Star Metric]
|
+-- Input Metric 1: [Name]
|   Definition: [What it measures]
|   Owner: [Team/person]
|   Current: [Value or TBD]
|   Target: [Value or TBD]
|
+-- Input Metric 2: [Name]
|   Definition: [What it measures]
|   Owner: [Team/person]
|   Current: [Value or TBD]
|   Target: [Value or TBD]
|
+-- Input Metric 3: [Name]
|   Definition: [What it measures]
|   Owner: [Team/person]
|   Current: [Value or TBD]
|   Target: [Value or TBD]
|
+-- Input Metric 4: [Name] (optional)
|   Definition: [What it measures]
|   Owner: [Team/person]
|   Current: [Value or TBD]
|   Target: [Value or TBD]
```

### Input Metrics Detail

| Input Metric | NSM Dimension | Actionable By | Correlation to NSM | Priority |
|-------------|--------------|--------------|-------------------|----------|
| [Metric 1] | [Breadth/Depth/Frequency/Efficiency] | [Team] | [Strong/Moderate/Weak] | [P0/P1/P2] |
| [Metric 2] | [Dimension] | [Team] | [Strength] | [Priority] |
| [Metric 3] | [Dimension] | [Team] | [Strength] | [Priority] |

### Input Metric Quality Check

| Check | Metric 1 | Metric 2 | Metric 3 |
|-------|----------|----------|----------|
| Orthogonal (non-overlapping) | [Yes/No] | [Yes/No] | [Yes/No] |
| Actionable (team can own it) | [Yes/No] | [Yes/No] | [Yes/No] |
| Predictive (correlates with NSM) | [Yes/No] | [Yes/No] | [Yes/No] |

## Measurement Plan

### Data Sources
| Metric | Source | Collection Method | Refresh Rate |
|--------|--------|------------------|-------------|
| [NSM] | [System/tool] | [How collected] | [Daily/Weekly] |
| [Input 1] | [System/tool] | [How collected] | [Daily/Weekly] |
| [Input 2] | [System/tool] | [How collected] | [Daily/Weekly] |

### Reporting Cadence
| Audience | Metric Set | Frequency | Format |
|----------|-----------|-----------|--------|
| Product team | NSM + all inputs | Daily/Weekly | Dashboard |
| Leadership | NSM + key inputs | Weekly/Monthly | Report |
| Company | NSM only | Monthly/Quarterly | All-hands |

## Alternatives Considered

| Candidate NSM | Why Rejected | When to Reconsider |
|--------------|-------------|-------------------|
| [Alternative 1] | [Reason] | [Under what conditions] |
| [Alternative 2] | [Reason] | [Under what conditions] |

## NSM Evolution Triggers

The NSM should be reconsidered when:
- [ ] Product fundamentally changes its value proposition
- [ ] New customer segment becomes dominant
- [ ] NSM stops correlating with revenue
- [ ] Business model changes (e.g., subscription to usage-based)
- [ ] NSM is consistently gamed without value creation

## Team Alignment

| Team | Primary Input Metric | How They Contribute to NSM |
|------|---------------------|---------------------------|
| [Engineering] | [Metric] | [Contribution] |
| [Product] | [Metric] | [Contribution] |
| [Marketing] | [Metric] | [Contribution] |
| [Sales] | [Metric] | [Contribution] |
| [Customer Success] | [Metric] | [Contribution] |
```

## Instructions

1. Ask clarifying questions about the product's core value proposition and available data
2. **Check prior context**: Run `/context-recall [product]` to find related vision statements, strategic bets, and positioning
3. **Check feedback**: Run `/feedback-recall [value/satisfaction/usage]` for customer signals about what they value most
4. Reference any analytics, usage data, or strategy documents provided via @file syntax
5. Apply the validation checklist rigorously; reject NSM candidates that fail critical criteria
6. Ensure input metrics are orthogonal, actionable, and predictive
7. Provide concrete alternatives considered with rejection rationale
8. Save in product/ or strategy/ folder
9. Offer to create presentation version using /present

## Context Integration

After generating the NSM definition:

1. **Offer to save**: Ask "Should I save this to the context registry? (`/context-save`)"
2. If yes, extract and save:
   - NSM definition and input metrics to context
   - Link to related vision statement, strategic bets, and roadmap themes
3. Suggest using the NSM as success criteria in `/strategic-bet` and `/outcome-review`
