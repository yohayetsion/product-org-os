---
name: heart-metrics
description: 'Apply Google''s HEART framework (Happiness, Engagement, Adoption, Retention, Task Success) with the Goals-Signals-Metrics process to measure UX quality at scale. Activate when: "HEART metrics",
  "HEART framework", "UX metrics", "happiness engagement adoption retention task success", "Google UX", "GSM", "goals signals metrics" Do NOT activate for: pirate metrics (/pirate-metrics), north star metric
  (/north-star-metric), customer health scorecard (/customer-health-scorecard)'
argument-hint: '[product or feature name] or [update path/to/heart-metrics.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: metrics
  skill_type: task-capability
  owner: bi-engineer
  primary_consumers:
  - data-analyst
  - bi-engineer
  - experimentation-analyst
  - design-dir
  - user-researcher
  - people-analyst
  - cro-specialist
  secondary_consumers:
  - pm
  - value-realization
  - onboarding-csm
  - kb-specialist
  - data-lead
  - ui-designer
  - interaction-designer
  - motion-designer
  - email-marketer
  - growth-marketer
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided (`@path/to/heart-metrics.md`) | UPDATE | 100% |
| "create", "new", "apply HEART" in input | CREATE | 100% |
| "find", "search", "list HEART" | FIND | 100% |
| "the HEART metrics", "our UX metrics" | UPDATE | 85% |
| Just product or feature name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete HEART x GSM matrix with dimension selection, goals, signals, metrics, and measurement plan using template below.

**UPDATE**:
1. Read existing HEART metrics document (search if path not provided)
2. Preserve unchanged dimensions exactly
3. Update goals, signals, or metrics for specific dimensions
4. Show diff summary: "Updated: [dimensions]. Unchanged: [dimensions]."
5. Note: Adding or removing a HEART dimension changes the measurement scope; document why

**FIND**:
1. Search paths below for HEART metrics documents
2. Present results: title, product/feature, dimensions used, path
3. Ask: "Update one of these, or create new?"

### Search Locations for HEART Metrics

- `product/`
- `metrics/`
- `ux/`
- `design/`

---
## Gotchas

- Not every product needs all five HEART dimensions -- pick 2-4 that matter most for your context
- Happiness metrics require surveys or feedback mechanisms; they cannot be derived from behavioral data alone
- Task Success requires defining specific tasks first -- it does not apply to open-ended exploration products
- HEART measures UX quality, not business outcomes -- pair with AARRR or NSM for the full picture



Apply Google's **HEART Framework** to measure UX quality at scale, using the **Goals-Signals-Metrics (GSM)** process to turn abstract UX goals into concrete, measurable metrics.

## Vision to Value Phase

**Phase 5: Business & Customer Outcomes** - HEART provides the UX measurement layer that complements business metrics, ensuring the product delivers quality experiences alongside business results.

**Prerequisites**: Phase 1-2 complete (product vision defined, user research done), product or feature launched or in beta
**Outputs used by**: Phase 5 (value realization, customer health), Phase 6 (outcome reviews, UX retrospectives), Phase 3 (roadmap prioritization based on UX gaps)

## Methodology

<!-- Source: HEART Framework -- Kerry Rodden, Hilary Hutchinson, and Xin Fu, "Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications" (CHI 2010, Google). Developed at Google to provide a comprehensive set of user-centered metrics that work at scale. -->

<!-- Source: Goals-Signals-Metrics (GSM) -- Developed alongside HEART at Google as the process for translating abstract UX goals into concrete, measurable metrics. The GSM process ensures metrics are goal-driven rather than data-driven. -->

<!-- Source: HEART at scale -- Google applied HEART across products including Search, Gmail, Maps, and YouTube. The framework was designed specifically for large-scale web applications where traditional lab-based UX methods are insufficient, but the principles apply to any digital product. -->

<!-- Source: Dimension selection -- Rodden et al. (2010) explicitly noted that not all five dimensions are relevant to every product. The recommendation is to choose the dimensions most aligned with your product goals rather than forcing all five. -->

### The Five HEART Dimensions

| Dimension | What It Measures | Data Type | Example Metrics |
|-----------|-----------------|-----------|-----------------|
| **Happiness** | Subjective user attitudes | Attitudinal (surveys) | Satisfaction (CSAT), NPS, perceived ease-of-use, visual appeal rating |
| **Engagement** | Level of user involvement | Behavioral (analytics) | Session frequency, session duration, pages/features per session, depth of interaction |
| **Adoption** | New users or new feature uptake | Behavioral (analytics) | New signups, feature adoption rate, upgrades, new use case discovery |
| **Retention** | Existing users returning | Behavioral (analytics) | Returning user rate, churn rate, repeat usage, DAU/MAU |
| **Task Success** | Efficiency and effectiveness | Behavioral + logs | Task completion rate, time-on-task, error rate, search success rate |

### The GSM Process

The GSM process is the engine that makes HEART actionable:

| Step | Definition | Question | Output |
|------|-----------|----------|--------|
| **Goal** | What you want to achieve (qualitative) | What UX outcome do we want? | A clear statement of desired user experience |
| **Signal** | User behavior that indicates progress (observable) | What would we observe if the goal is met? | Specific user actions or attitudes |
| **Metric** | Quantifiable measurement of the signal (measurable) | How do we count or measure the signal? | A number with a data source |

### HEART x GSM Matrix

The core artifact is a matrix with HEART dimensions as rows and GSM steps as columns:

| Dimension | Goal | Signal | Metric |
|-----------|------|--------|--------|
| Happiness | Users find product easy and pleasant | High satisfaction survey scores | Average CSAT score (quarterly survey) |
| Engagement | Users deeply interact with core features | Frequent and varied feature usage | Average features used per session |
| Adoption | New users discover and adopt the product | Growing new user signups | New users per week, feature adoption % |
| Retention | Users continue to return and use product | Users return within defined timeframes | 30-day retention rate, DAU/MAU |
| Task Success | Users complete core tasks efficiently | Tasks completed without errors or delays | Task completion rate, median time-on-task |

### Dimension Selection Guide

| If Your Product Is... | Prioritize | Deprioritize |
|----------------------|-----------|--------------|
| New / early-stage | Adoption, Task Success | Engagement (too early) |
| Productivity / SaaS tool | Task Success, Engagement, Retention | Happiness (efficiency > delight) |
| Consumer / social app | Engagement, Happiness, Retention | Task Success (open-ended usage) |
| E-commerce / marketplace | Task Success, Adoption, Happiness | Engagement (transactional) |
| Internal tool / enterprise | Task Success, Happiness | Referral not applicable |

### Combining HEART with Business Metrics

HEART measures UX quality. Pair it with business metric frameworks:

| UX Layer (HEART) | Business Layer | Connection |
|-----------------|---------------|------------|
| Happiness | NPS/CSAT | Happiness drives NPS which predicts growth |
| Engagement | DAU/MAU (NSM) | Engagement depth feeds retention and revenue |
| Adoption | Acquisition (AARRR) | Adoption complements acquisition with feature-level detail |
| Retention | Retention (AARRR) | Same concept, HEART adds UX-quality lens |
| Task Success | Activation (AARRR) | Successful tasks drive activation |

## Output Structure

```markdown
# HEART Metrics: [Product or Feature Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Single accountable person -- typically UX Lead or Product Manager]
**Product**: [Product name]
**Scope**: Product-Level / Feature-Level / Flow-Level
**Dimensions Selected**: [List the 2-5 HEART dimensions in scope]

## Dimension Selection Rationale

| Dimension | Included? | Rationale |
|-----------|-----------|-----------|
| Happiness | [Yes/No] | [Why included or excluded for this product] |
| Engagement | [Yes/No] | [Rationale] |
| Adoption | [Yes/No] | [Rationale] |
| Retention | [Yes/No] | [Rationale] |
| Task Success | [Yes/No] | [Rationale] |

## HEART x GSM Matrix

### [Dimension 1: e.g., Happiness]

| Component | Definition |
|-----------|-----------|
| **Goal** | [Qualitative statement of the desired UX outcome] |
| **Signal** | [Observable user behavior or attitude that indicates progress] |
| **Metric** | [Quantifiable measurement with data source] |

**Current Value**: [TBD]
**Target Value**: [TBD]
**Data Source**: [Survey tool, analytics platform, log system]
**Collection Method**: [How and how often this data is gathered]

### [Dimension 2: e.g., Engagement]

| Component | Definition |
|-----------|-----------|
| **Goal** | [Goal statement] |
| **Signal** | [Signal description] |
| **Metric** | [Metric definition] |

**Current Value**: [TBD]
**Target Value**: [TBD]
**Data Source**: [Source]
**Collection Method**: [Method]

### [Dimension 3: e.g., Task Success]

| Component | Definition |
|-----------|-----------|
| **Goal** | [Goal statement] |
| **Signal** | [Signal description] |
| **Metric** | [Metric definition] |

**Current Value**: [TBD]
**Target Value**: [TBD]
**Data Source**: [Source]
**Collection Method**: [Method]

### [Dimension 4] (if applicable)

[Same structure]

### [Dimension 5] (if applicable)

[Same structure]

## Consolidated HEART Dashboard

| Dimension | Goal (Summary) | Metric | Current | Target | Status |
|-----------|---------------|--------|---------|--------|--------|
| [Dim 1] | [1-line goal] | [Metric name] | [TBD] | [TBD] | [On Track / At Risk / Below] |
| [Dim 2] | [1-line goal] | [Metric name] | [TBD] | [TBD] | [Status] |
| [Dim 3] | [1-line goal] | [Metric name] | [TBD] | [TBD] | [Status] |

## Key Tasks Defined (for Task Success dimension)

| Task | Description | Success Criteria | Expected Time | Error Threshold |
|------|------------|-----------------|---------------|-----------------|
| [Core task 1] | [What the user is trying to do] | [Completion definition] | [Target time] | [Acceptable error %] |
| [Core task 2] | [Description] | [Criteria] | [Time] | [Error %] |

*Only include this section if Task Success is a selected dimension.*

## Measurement Plan

### Data Sources

| Metric | Source | Collection Method | Refresh Rate |
|--------|--------|------------------|-------------|
| [Happiness metric] | [Survey tool] | [Quarterly survey / in-app prompt] | [Quarterly] |
| [Engagement metric] | [Analytics] | [Event tracking] | [Daily] |
| [Task Success metric] | [Logs / analytics] | [Task logging] | [Weekly] |

### Survey Design (for Happiness dimension)

| Question | Scale | Frequency | Target Audience |
|----------|-------|-----------|-----------------|
| [Satisfaction question] | [1-5 / 1-7 / NPS] | [Quarterly] | [All users / segment] |
| [Ease-of-use question] | [Scale] | [Frequency] | [Audience] |

### Reporting Cadence

| Audience | Metrics | Frequency | Format |
|----------|---------|-----------|--------|
| UX Team | All HEART dimensions | Weekly | Dashboard |
| Product Team | Selected dimensions + trends | Bi-weekly | Report |
| Leadership | Summary dashboard | Monthly | Slide |

## UX Improvement Hypotheses

| # | Dimension | Hypothesis | Expected Impact | Validation Method |
|---|-----------|-----------|-----------------|-------------------|
| 1 | [Dimension] | [If we do X, then Y will improve] | [Impact on metric] | [How to test] |
| 2 | [Dimension] | [Hypothesis] | [Impact] | [Test method] |
| 3 | [Dimension] | [Hypothesis] | [Impact] | [Test method] |

## Integration with Business Metrics

| HEART Dimension | Business Metric Link | Relationship |
|----------------|---------------------|--------------|
| [Dimension] | [AARRR stage or NSM] | [How they connect] |
| [Dimension] | [Business metric] | [Connection] |
```

## Instructions

1. Ask clarifying questions about the product type, scope (whole product vs feature), and available data sources
2. **Check prior context**: Run `/context-recall [product]` to find related UX research, strategic bets, and NSM definitions
3. **Check feedback**: Run `/feedback-recall [UX/usability/satisfaction/experience]` for customer signals about experience quality
4. Reference any analytics dashboards, survey results, or UX research provided via @file syntax
5. Help the user select the right HEART dimensions -- push back on "all five" unless justified
6. Write GSM entries that are specific to the product, not generic definitions
7. Use [TBD] for any metric values not provided by the user; never fabricate UX metrics
8. For Task Success, insist on defining specific tasks before writing metrics
9. Save in metrics/, ux/, or product/ folder
10. Offer to create presentation version using /present

## Context Integration

After generating the HEART metrics:

1. **Offer to save**: Ask "Should I save this to the context registry? (`/context-save`)"
2. If yes, extract and save:
   - HEART dimensions and key metrics to context
   - Link to related NSM, pirate metrics, and UX research
   - UX improvement hypotheses to `context/assumptions/registry.md`
3. Suggest pairing HEART with `/pirate-metrics` or `/north-star-metric` for full measurement coverage
