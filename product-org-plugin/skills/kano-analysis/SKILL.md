---
name: kano-analysis
description: 'Conduct a full Kano analysis to classify customer preferences into Must-Be, Performance, Attractive, Indifferent, and Reverse categories. Includes survey design, classification methodology,
  satisfaction coefficients, and strategic implications. Activate when: "Kano analysis", "Kano model", "customer satisfaction model", "delighters", "must-be features", "attractive quality", "feature classification",
  "Kano survey", "Kano questionnaire", "satisfaction coefficients" Do NOT activate for: feature prioritization (/prioritize-features), user research (/ux-lead agent), customer journey (/customer-journey-map)'
argument-hint: '[list of features to classify] or [update path/to/kano-analysis.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: product-management
  skill_type: task-capability
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "reclassify" in input | UPDATE | 100% |
| File path provided (`@path/to/kano-analysis.md`) | UPDATE | 100% |
| "create", "new", "run Kano", "classify" in input | CREATE | 100% |
| "find", "search", "list Kano" | FIND | 100% |
| "the Kano analysis", "our Kano" | UPDATE | 85% |
| Just a list of features | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Design Kano questionnaire pairs, classify features using the 5x5 evaluation table, compute satisfaction/dissatisfaction coefficients, and produce strategic recommendations.

**UPDATE**:
1. Read existing Kano analysis (search if path not provided)
2. Preserve classifications for unchanged features
3. Reclassify modified or added features, recompute coefficients
4. Show diff summary: "Added: [features]. Reclassified: [features]. Unchanged: [features]."

**FIND**:
1. Search paths below for Kano analysis documents
2. Present results: title, feature count, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `product/`
- `research/`
- `planning/`
- `prioritization/`

---
## Gotchas

- Ideal Kano analysis requires real customer survey data (20-30 responses minimum per feature for statistical validity) -- proxy classification based on product knowledge is acceptable but must be labeled as such
- Kano categories are not static -- Attractive features decay to Performance over time, and Performance decays to Must-Be (Kano Decay). Always note the temporal context.
- The 5x5 evaluation table produces Questionable (Q) results when respondents give contradictory answers -- high Q rates signal poorly worded questions, not feature problems
- Satisfaction/Dissatisfaction coefficients are ratios, not absolute scores -- they are meaningful for comparing features against each other, not in isolation

## Vision to Value Phase

**Phase 1: Strategic Foundation** - Kano analysis reveals the non-linear relationship between feature investment and customer satisfaction, informing which features to pursue and which to deprioritize during strategic discovery.

**Prerequisites**: A list of candidate features or capabilities to classify, ideally with access to customer survey data or deep product knowledge
**Outputs used by**: `/prioritize-features` (Kano categories as prioritization input), `/prd` (feature categorization informs requirement urgency), `/product-roadmap` (Must-Be before Attractive sequencing)

## Methodology

<!-- Source: Kano Model -- Noriaki Kano et al., "Attractive Quality and Must-Be Quality" (1984), Journal of the Japanese Society for Quality Control. Kano was a professor at Tokyo University of Science. -->

<!-- Source: uyanik/ShapKa -- Python implementation of SHAP + Kano integration. Referenced for survey design patterns. -->

<!-- Source: Satisfaction/Dissatisfaction coefficients -- Berger et al. (1993), extended Kano classification with quantitative coefficients for prioritization. -->

### The Kano Model

The Kano Model classifies customer preferences into five categories based on the non-linear relationship between feature implementation and customer satisfaction:

| Category | Japanese Term | When Present | When Absent | Example |
|----------|--------------|-------------|-------------|---------|
| **Must-Be (M)** | Atarimae | No increase in satisfaction (expected) | Strong dissatisfaction | Security in a banking app |
| **Performance (O)** | Ichi-gen-teki | Satisfaction increases proportionally | Dissatisfaction increases proportionally | Battery life in a phone |
| **Attractive (A)** | Miryoku-teki | Delights (unexpected satisfaction) | No dissatisfaction (not expected) | Free gift with purchase |
| **Indifferent (I)** | Mu-kanshin | No effect | No effect | Internal code refactoring |
| **Reverse (R)** | Gyaku | Dissatisfaction (actively unwanted) | Satisfaction | Forced social features for privacy users |

An additional category, **Questionable (Q)**, indicates contradictory responses that signal survey design issues.

### Kano Questionnaire Design

For each feature, ask a paired functional/dysfunctional question:

**Functional question**: "If [feature] were present, how would you feel?"
**Dysfunctional question**: "If [feature] were absent, how would you feel?"

Response options for both questions:

| Response | Code | Meaning |
|----------|------|---------|
| I like it that way | L | Positive reaction |
| I expect it that way | E | Taken for granted |
| I am neutral | N | No strong feeling |
| I can tolerate it | T | Mild negative |
| I dislike it that way | D | Strong negative |

### 5x5 Evaluation Table

Cross-reference functional (rows) and dysfunctional (columns) responses to classify:

| Functional \ Dysfunctional | Like | Expect | Neutral | Tolerate | Dislike |
|----|------|--------|---------|----------|---------|
| **Like** | Q | A | A | A | O |
| **Expect** | R | I | I | I | M |
| **Neutral** | R | I | I | I | M |
| **Tolerate** | R | I | I | I | M |
| **Dislike** | R | R | R | R | Q |

**Reading the table**: Find the row matching the functional response and the column matching the dysfunctional response. The cell gives the Kano category.

### Aggregation (Multiple Respondents)

When survey data covers multiple respondents, classify each feature by the category that receives the most responses. Report the distribution:

| Feature | M | O | A | I | R | Q | **Classification** |
|---------|---|---|---|---|---|---|-------------------|
| Feature X | 2 | 15 | 8 | 3 | 0 | 1 | **O (Performance)** |

**Minimum sample size**: 20-30 respondents per feature for statistical validity. Below 20, label results as directional only.

### Satisfaction and Dissatisfaction Coefficients

<!-- Source: Berger et al. (1993) extended the Kano model with quantitative coefficients that enable direct comparison between features. -->

Calculate coefficients using response counts:

**Satisfaction Index (SI)**: How much satisfaction increases if the feature is present.
```
SI = (A + O) / (A + O + M + I)
```
Range: 0 to 1. Closer to 1 = higher satisfaction potential.

**Dissatisfaction Index (DI)**: How much dissatisfaction increases if the feature is absent.
```
DI = (O + M) / (A + O + M + I) x (-1)
```
Range: -1 to 0. Closer to -1 = higher dissatisfaction if missing.

### SI vs DI Scatter Plot Interpretation

Plot features on a scatter chart with SI (x-axis) and DI (y-axis):

```
        SI (Satisfaction potential) -->
   0.0         0.5          1.0
   +------------+------------+
   |            |            |  0.0
   |  Indiff.   | Attractive |
   |            |            |
   +------------+------------+  -0.5
   |            |            |
   |  Must-Be   | Performance|
   |            |            |
   +------------+------------+  -1.0
                                DI (Dissatisfaction potential)
```

### Kano Decay (Temporal Dynamics)

Feature categories shift over time following a predictable pattern:

```
Attractive --> Performance --> Must-Be
(Delighter)   (Expected)    (Table stakes)
```

**Examples of Kano Decay**:
- Camera on phones: Attractive (2002) --> Performance (2008) --> Must-Be (2015)
- Free shipping: Attractive (2005) --> Performance (2012) --> Must-Be (2020)
- GPS navigation: Attractive (2000) --> Must-Be (2015)

**Implication**: Must-Be features accumulate over time. Products need a continuous pipeline of Attractive features to maintain competitive differentiation.

### Strategic Implications by Category

| Category | Investment Strategy | Risk of Skipping |
|----------|-------------------|------------------|
| **Must-Be** | Invest to threshold quality; over-investing yields diminishing returns | Critical -- customers will leave |
| **Performance** | Invest proportionally; direct correlation with competitive position | High -- competitors with better performance win |
| **Attractive** | Invest selectively for differentiation; highest ROI on satisfaction | Low short-term -- but no differentiation |
| **Indifferent** | Minimize investment; redirect resources elsewhere | None -- customers don't care |
| **Reverse** | Do NOT build; segment carefully if some users want it and others don't | Negative -- building this actively harms satisfaction |

## Output Structure

```markdown
# Kano Analysis: [Product/Feature Set]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this analysis]
**Data Source**: [Customer survey (N=X) / Product team proxy / Mixed]
**Confidence**: [High (N>30 survey) / Medium (N=20-30) / Low (proxy classification)]

## Executive Summary

[2-3 paragraph synthesis: key findings, distribution of categories, strategic recommendations]

## Features Analyzed

| # | Feature | Description |
|---|---------|-------------|
| 1 | [Feature name] | [Brief description] |
| 2 | [Feature name] | [Brief description] |

## Kano Classification Results

| # | Feature | M | O | A | I | R | Q | Classification | SI | DI |
|---|---------|---|---|---|---|---|---|---------------|----|----|
| 1 | [Feature] | [n] | [n] | [n] | [n] | [n] | [n] | [Category] | [0.XX] | [-0.XX] |
| 2 | [Feature] | [n] | [n] | [n] | [n] | [n] | [n] | [Category] | [0.XX] | [-0.XX] |

## Category Distribution

| Category | Count | Features |
|----------|-------|----------|
| Must-Be (M) | [n] | [Feature names] |
| Performance (O) | [n] | [Feature names] |
| Attractive (A) | [n] | [Feature names] |
| Indifferent (I) | [n] | [Feature names] |
| Reverse (R) | [n] | [Feature names] |

## Satisfaction Coefficient Analysis

### Highest Satisfaction Potential (SI)
1. [Feature] -- SI: [value] -- [Implication]
2. [Feature] -- SI: [value] -- [Implication]

### Highest Dissatisfaction Risk (DI)
1. [Feature] -- DI: [value] -- [Implication]
2. [Feature] -- DI: [value] -- [Implication]

## Strategic Recommendations

### Immediate Priorities (Must-Be gaps)
- [Features that are Must-Be but currently missing or below threshold]

### Competitive Differentiators (Performance investment)
- [Features where Performance investment will improve competitive position]

### Innovation Pipeline (Attractive opportunities)
- [Features that can delight customers and create differentiation]

### Deprioritize (Indifferent features)
- [Features where investment can be redirected]

### Kano Decay Watch
- [Features at risk of category shift based on market maturity]

## Questionnaire Design

### Functional/Dysfunctional Pairs Used

| # | Feature | Functional Question | Dysfunctional Question |
|---|---------|-------------------|----------------------|
| 1 | [Feature] | "If [feature description], how would you feel?" | "If [feature description] were absent, how would you feel?" |

## Assumptions & Limitations

- [Survey methodology limitations]
- [Sample size constraints]
- [Temporal context -- when was data collected]
- [Segment specificity -- results may vary by customer segment]

## Next Steps

- [ ] Validate Must-Be features are at threshold quality
- [ ] Feed results into `/prioritize-features` for integrated prioritization
- [ ] Design experiments for high-SI Attractive features via `/experiment-design`
- [ ] Map assumptions behind classifications via `/assumption-map`
- [ ] Schedule re-analysis in [6/12] months to track Kano Decay
```

## Instructions

1. Ask the user for: (a) the list of features/capabilities to classify, (b) whether they have customer survey data or want proxy classification based on product knowledge
2. If survey data is available, process the functional/dysfunctional response pairs through the 5x5 evaluation table
3. If proxy classification, work with the user to classify each feature by discussing expected customer reactions -- clearly label output as "proxy classification"
4. Always compute SI and DI coefficients, even for proxy classifications
5. Challenge "Must-Be" inflation -- not everything is a must-have. Ask: "Would customers actually leave if this were missing?"
6. Flag features with high Questionable (Q) counts as potential survey design issues
7. Note Kano Decay risks for any Attractive features in mature markets
8. Save output as markdown file
9. Offer `/prioritize-features` to integrate Kano results with other frameworks (RICE, WSJF) or `/experiment-design` to validate surprising classifications

## Integration

- Links to `/prioritize-features` (Kano categories as one input to multi-framework prioritization)
- Links to `/prd` (Must-Be features become non-negotiable requirements)
- Links to `/product-roadmap` (category-informed sequencing: Must-Be first, then Performance, then Attractive)
- Links to `/experiment-design` (validate surprising or contested classifications)
- Links to `/assumption-map` (surface assumptions behind proxy classifications)
- Links to `/customer-journey-map` (map satisfaction drivers to journey stages)
- Links to `/context-save` (save for periodic re-analysis to track Kano Decay)

## Vision to Value Operating Principle

> "Customer satisfaction is not linear. The Kano Model reveals that some features only matter when absent, while others only matter when present. Understanding this asymmetry is the foundation of smart product investment."
