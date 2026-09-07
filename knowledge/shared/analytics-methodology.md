# Analytics Methodology Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: `data-lead`, `data-analyst`, `bi-engineer`
**Secondary Users**: `bizops`, `vp-product`, `product-manager`

**Sources consulted**:
- Anthropic Data plugin patterns — metric-tree design and analytics workflows
- dbt Labs, `dbt-core` (Apache-2.0) — data-modelling and semantic-layer concepts
- Metabase, `metabase/metabase` (AGPL-3.0) — publicly observable self-service analytics patterns
- Reforge Growth Series — AARRR, North Star, and growth-modelling frameworks
- Amplitude Analytics playbook — cohort-analysis and event-taxonomy practices

**Source licence**: the licence named beside each software source applies to that source; other entries are credited public resources.
**Our determination**: `describes-public-method` — this knowledge pack is original V2V prose describing public analytics methods and product patterns. No Metabase code or text is reproduced or redistributed.
**V2V refinements**: integrates metric trees, governance, experimentation, and agent-facing analytics into a Product Org OS operating reference.

---

## Metric Trees

### What Is a Metric Tree?

A metric tree is a hierarchical decomposition of a high-level business metric into its component drivers. It shows how input metrics compound to produce output metrics, enabling teams to understand which levers drive outcomes.

### Metric Tree Structure

```
North Star Metric
├── Driver A (e.g., Acquisition)
│   ├── Input A.1 (e.g., Website visitors)
│   ├── Input A.2 (e.g., Signup conversion rate)
│   └── Input A.3 (e.g., Channel mix)
├── Driver B (e.g., Activation)
│   ├── Input B.1 (e.g., Onboarding completion rate)
│   ├── Input B.2 (e.g., Time-to-first-value)
│   └── Input B.3 (e.g., Feature discovery rate)
├── Driver C (e.g., Retention)
│   ├── Input C.1 (e.g., D7 retention)
│   ├── Input C.2 (e.g., Feature stickiness)
│   └── Input C.3 (e.g., Support satisfaction)
└── Driver D (e.g., Monetization)
    ├── Input D.1 (e.g., Conversion to paid)
    ├── Input D.2 (e.g., ARPU)
    └── Input D.3 (e.g., Expansion rate)
```

### Metric Tree Design Principles

| Principle | Description |
|-----------|-------------|
| **MECE** | Drivers should be mutually exclusive, collectively exhaustive |
| **Actionable Leaves** | Leaf metrics should be ones a team can influence directly |
| **Measurable** | Every node must have a clear data source and calculation |
| **Directional** | Increasing a leaf metric should directionally increase the parent |
| **Owned** | Every metric has an owner who is accountable for movement |

> **2026-06 note**: Agentic / conversational analytics (e.g., natural-language queries over a metric tree) needs a *governed semantic substrate* — Snowflake Cortex Sense, the Open Semantic Interchange (OSI) spec, or the dbt Semantic Layer — so that agents resolve metric definitions consistently rather than re-deriving SQL. See `data-modeling.md` (2026-06 Delta Update) for the semantic-layer / OSI detail.

### Building a Metric Tree

1. **Start with the North Star** — What is the single metric that best captures value delivery?
2. **Decompose mathematically** — NSM = f(Driver A, Driver B, ...). Use multiplication, addition, or weighted combinations.
3. **Drill into drivers** — Each driver = f(Input 1, Input 2, ...). Continue until you reach metrics a team can directly act on.
4. **Validate direction** — Confirm that increasing an input increases the parent. Flag non-monotonic relationships.
5. **Assign owners** — Every leaf and driver has a team or individual accountable for it.

---

## AARRR (Pirate Metrics) Framework

### The Five Stages

| Stage | Question | Example Metrics |
|-------|----------|-----------------|
| **Acquisition** | How do users find us? | Channel traffic, CAC, signup volume, source attribution |
| **Activation** | Do users have a great first experience? | Onboarding completion, time-to-first-value, setup rate |
| **Retention** | Do users come back? | D1/D7/D30 retention, weekly active rate, churn rate |
| **Revenue** | How do we make money? | Conversion to paid, ARPU, LTV, MRR growth |
| **Referral** | Do users tell others? | NPS, referral rate, viral coefficient, organic share |

### AARRR Application Guidelines

- **Stage priority**: Fix leaks from left to right. No point acquiring users who don't activate.
- **One focus at a time**: Identify the stage with the biggest drop-off and concentrate there.
- **Cohorted**: Always measure by cohort (signup date), not aggregate. Aggregate metrics hide trends.
- **Segmented**: Different user segments may have different bottlenecks. Check by plan, channel, geography.

### AARRR to Metric Tree Mapping

The AARRR stages map to the top-level drivers of your metric tree. Each stage becomes a branch, and the specific metrics within that stage become leaves.

---

## North Star Framework

### Defining a North Star Metric

A North Star Metric (NSM) is the single metric that best captures the core value your product delivers to customers. It is the focal point for the entire organization.

### NSM Criteria

| Criterion | Test |
|-----------|------|
| **Value Expression** | Does it measure value delivered to customers, not just business output? |
| **Leading Indicator** | Does it predict future business success (revenue, retention)? |
| **Actionable** | Can teams influence it through product changes? |
| **Understandable** | Can everyone in the company explain it? |
| **Measurable** | Can you calculate it reliably with current instrumentation? |

### NSM Examples by Business Type

| Business Type | NSM Example | Why |
|---------------|-------------|-----|
| **B2B SaaS** | Weekly active teams completing core workflows | Measures ongoing value realization, not just login |
| **Marketplace** | Weekly transactions | Captures both supply and demand engagement |
| **Media/Content** | Daily active consumers spending 10+ min | Measures meaningful engagement, not drive-by visits |
| **E-commerce** | Weekly repeat purchase rate | Measures loyalty, not just acquisition |
| **Developer Tool** | Weekly API calls from production apps | Measures integration depth and production reliance |

### NSM Anti-Patterns

| Anti-Pattern | Problem | Better Alternative |
|--------------|---------|-------------------|
| Revenue as NSM | Lagging, not actionable, doesn't measure value | Value metric that predicts revenue |
| Signups as NSM | Vanity metric, doesn't measure value delivery | Activated users who complete core action |
| DAU/MAU ratio as NSM | Descriptive but not directly actionable | Specific engagement action tied to value |

---

## Cohort Analysis

### Types of Cohort Analysis

| Type | Cohort Definition | Use Case |
|------|-------------------|----------|
| **Acquisition Cohort** | Grouped by signup/first-use date | Retention curves, lifecycle tracking |
| **Behavioral Cohort** | Grouped by action taken (or not taken) | Feature adoption impact, activation analysis |
| **Attribute Cohort** | Grouped by characteristic (plan, channel, geo) | Segment comparison, targeting |

### Retention Cohort Table

```
         Week 0    Week 1    Week 2    Week 3    Week 4
Jan W1   100%      45%       32%       28%       26%
Jan W2   100%      48%       35%       30%       --
Jan W3   100%      42%       30%       --        --
Jan W4   100%      50%       --        --        --
Feb W1   100%      --        --        --        --
```

### Reading Retention Tables

- **Rows**: Compare across rows to see if newer cohorts retain better (product improving)
- **Columns**: Read down columns to see if retention at a given age is improving over time
- **Diagonals**: Calendar-time effects (seasonality, incidents)
- **Flattening**: Where the curve flattens indicates natural retention level

### Cohort Analysis Best Practices

| Practice | Why |
|----------|-----|
| **Always cohort by time** | Aggregate metrics hide improvement or degradation trends |
| **Use appropriate granularity** | Daily for early-stage, weekly for growth, monthly for enterprise |
| **Compare to benchmark** | Is 30% D7 retention good? Depends on category. Compare to peers |
| **Look for inflection points** | Where do users drop fastest? That's the activation problem |
| **Segment within cohorts** | The average masks important differences between segments |

---

## Funnel Analysis

### Funnel Design

```
Step 1: Landing Page Visit
  ↓ [X% conversion]
Step 2: Signup Initiated
  ↓ [X% conversion]
Step 3: Signup Completed
  ↓ [X% conversion]
Step 4: Onboarding Started
  ↓ [X% conversion]
Step 5: Core Action Completed (Activation)
  ↓ [X% conversion]
Step 6: Second Session
```

### Funnel Analysis Guidelines

| Guideline | Description |
|-----------|-------------|
| **Conversion AND drop-off** | Report both. "75% converted" and "25% dropped off at step 3" tell different stories |
| **Time between steps** | Not just whether users convert, but how long it takes. Slow funnels leak |
| **Segment the funnel** | Mobile vs desktop, organic vs paid, plan type — different segments have different bottlenecks |
| **Session vs. user funnels** | Single-session funnels vs. multi-session funnels measure different things |
| **Ordered vs. unordered** | Strict step order vs. any-order completion — choose based on the journey being measured |

### Common Funnel Pitfalls

| Pitfall | Impact | Mitigation |
|---------|--------|------------|
| **Wrong event definitions** | Steps don't match actual user behavior | Validate with engineering, check event firing |
| **Missing steps** | Gap in funnel hides the real bottleneck | Map the full journey before selecting funnel steps |
| **Too many steps** | Every step looks like a problem; no focus | Keep to 5-7 steps for actionable analysis |
| **Ignoring time** | Funnel completion over 30 days is not the same as 30 minutes | Set appropriate time windows |

---

## Event Taxonomy

### Event Naming Convention

```
[Object]_[Action]
```

Examples: `page_viewed`, `button_clicked`, `signup_completed`, `feature_used`, `plan_upgraded`

### Event Properties Standard

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `event_name` | string | Yes | Standardized event name |
| `timestamp` | datetime | Yes | ISO 8601 timestamp |
| `user_id` | string | Yes | Unique user identifier |
| `session_id` | string | Yes | Session identifier |
| `platform` | string | Yes | web, ios, android |
| `source` | string | No | Traffic source or referrer |
| `properties` | object | No | Event-specific key-value pairs |

### Event Taxonomy Governance

- **Central registry**: All events documented in a single source of truth
- **Naming convention enforced**: Code review or automated validation
- **Deprecation process**: Old events marked deprecated, migration documented
- **Property standards**: Required vs optional properties per event type
- **Versioning**: Schema changes tracked and communicated

---

## Data Quality Framework

### Data Quality Dimensions

| Dimension | Definition | How to Measure |
|-----------|-----------|----------------|
| **Completeness** | All expected data is present | % of null/missing values per field |
| **Accuracy** | Data correctly represents reality | Spot checks against ground truth |
| **Consistency** | Same data appears the same everywhere | Cross-source comparison |
| **Timeliness** | Data is available when needed | Latency from event to availability |
| **Uniqueness** | No unintended duplicates | Duplicate detection rate |

### Data Quality Checks

```
1. Freshness: Is the latest data within expected recency?
2. Volume: Is row count within expected range (±20%)?
3. Schema: Do all expected columns exist with correct types?
4. Distribution: Are value distributions within expected ranges?
5. Uniqueness: Are primary keys actually unique?
6. Referential: Do foreign keys reference valid records?
7. Business rules: Do calculated fields follow expected logic?
```

---

*Last Updated: 2026-03-29*
*References: dbt-labs/dbt-core patterns, metabase/metabase, Reforge Growth Series, Amplitude Analytics playbook*
