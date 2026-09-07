# Data Visualization & BI Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: `bi-engineer`, `data-analyst`
**Secondary Users**: `data-lead`, `bizops`, `value-realization`

**Sources consulted**:
- Edward Tufte, *The Visual Display of Quantitative Information* — data-visualisation principles
- dbt Labs, `dbt-core` (Apache-2.0) — semantic-layer and data-modelling concepts
- Metabase, `metabase/metabase` (AGPL-3.0) — publicly observable self-service BI patterns
- Evidence, `evidence-dev/evidence` (MIT) — code-driven BI and Markdown analytics patterns
- Apache Superset, `apache/superset` (Apache-2.0) — dashboard-design patterns

**Source licence**: the licence named beside each software source applies to that source; Tufte is credited as a published source.
**Our determination**: `describes-public-method` — this knowledge pack is original V2V prose describing public visualisation and BI methods. No Metabase code or text is reproduced or redistributed.
**V2V refinements**: combines visual design, dashboard operation, accessibility, governance, and agent-facing BI guidance in a Product Org OS operating reference.

---

## Tufte Principles of Data Visualization

### Core Principles

| Principle | Description | Application |
|-----------|-------------|-------------|
| **Data-Ink Ratio** | Maximize the share of ink devoted to data, minimize non-data ink | Remove gridlines, borders, backgrounds, decorations that don't carry information |
| **Chartjunk** | Avoid decorative elements that don't convey data | No 3D effects, gradients, or clip art. Every pixel should inform |
| **Lie Factor** | Visual representation should be proportional to the data | Lie Factor = Size of effect in graphic / Size of effect in data. Should be ~1.0 |
| **Small Multiples** | Repeat a chart for different slices of data | Same scale, same format, side by side — enables comparison |
| **Sparklines** | Intense, word-sized graphics embedded in context | Inline trends next to numbers in tables and text |
| **Micro/Macro** | Detail and overview should coexist | Allow users to see the big picture and drill into specifics |

### Chart Selection Guide

| Data Relationship | Best Chart Type | When NOT to Use |
|-------------------|----------------|-----------------|
| **Trend over time** | Line chart | Fewer than 5 data points (use bar) |
| **Comparison** | Bar chart (horizontal for >5 categories) | Too many categories (>15: use table or small multiples) |
| **Proportion** | Stacked bar, waffle chart | Pie charts (hard to compare angles). Only use pie for 2-3 slices |
| **Distribution** | Histogram, box plot, violin | Bar chart for continuous data (loses distribution shape) |
| **Correlation** | Scatter plot | Line chart (implies temporal ordering) |
| **Composition** | Stacked area, treemap | 3D stacked charts (impossible to read middle layers) |
| **Geospatial** | Choropleth, bubble map | When geography isn't relevant to the insight |
| **Ranking** | Horizontal bar chart | Vertical bar (harder to read labels) |
| **Part-to-whole** | Waterfall chart | When the parts don't meaningfully sum to the whole |
| **Flow** | Sankey diagram | When there are too many nodes (>10) |

### Color Usage Guidelines

| Use | Recommendation |
|-----|---------------|
| **Sequential** (low-to-high) | Single hue, varying lightness (e.g., light blue to dark blue) |
| **Diverging** (low-mid-high) | Two hues diverging from neutral midpoint (e.g., red-white-blue) |
| **Categorical** | Distinct hues, max 7-8 categories before color becomes useless |
| **Highlighting** | One accent color against gray/muted palette |
| **Accessibility** | Avoid red/green only. Use colorblind-safe palettes (e.g., Viridis, Cividis) |
| **Consistency** | Same metric = same color across all dashboards |

---

## Dashboard Design

### Dashboard Types

| Type | Purpose | Refresh | Audience | Interaction Level |
|------|---------|---------|----------|-------------------|
| **Strategic** | KPI monitoring, executive decision support | Daily/Weekly | Leadership | Low (view, filter by time) |
| **Operational** | Real-time monitoring, alert-driven | Real-time/Hourly | Operations | Medium (filter, drill-down) |
| **Analytical** | Deep exploration, hypothesis testing | On-demand | Analysts, PMs | High (filter, pivot, segment, export) |
| **Tactical** | Campaign/initiative-specific tracking | Daily | Execution teams | Medium (filter by segment/campaign) |

### Dashboard Design Principles

| Principle | Implementation |
|-----------|---------------|
| **Inverted pyramid** | Most important metrics at top, details below. If they only see the first row, they get the key story |
| **Progressive disclosure** | Summary → drill-down → raw data. Don't show everything at once |
| **Context everywhere** | Every number has comparison: prior period, target, benchmark. Standalone numbers are meaningless |
| **Consistent layout** | Metric cards at top, trends in middle, tables at bottom. Same layout across dashboards |
| **Annotations** | Key events (launches, incidents, holidays) marked on time series. "Why did this spike?" answered before asked |
| **Action-oriented** | Dashboard should make the next action obvious. If it doesn't suggest action, it's a report, not a dashboard |

### Dashboard Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| **Wall of numbers** | Information overload, no hierarchy | Use visual hierarchy: big KPIs, smaller supporting metrics |
| **Rainbow dashboards** | Too many colors, cognitive overload | Limit to 3-5 colors with clear meaning |
| **No time context** | Don't know if current values are good or bad | Add sparklines, period comparisons, targets |
| **Too many filters** | Analysis paralysis, performance issues | Default to most common view, allow drill-down |
| **Stale data badge** | Users don't know if data is current | Show last-updated timestamp prominently |

### Dashboard Lifecycle

| Phase | Activities | Exit Criteria |
|-------|-----------|---------------|
| **Design** | Stakeholder interviews, metric selection, wireframe | Audience, questions, and metrics agreed |
| **Build** | Implement queries, visualizations, filters | Dashboard functional and accurate |
| **Review** | User testing, accuracy validation, performance check | Stakeholders confirm it answers their questions |
| **Launch** | Documentation, training, access provisioning | Users actively using the dashboard |
| **Monitor** | Usage tracking, feedback collection, performance monitoring | Usage meets threshold, no accuracy issues |
| **Iterate/Sunset** | Update based on feedback, or sunset if unused | Decision to iterate or remove |

---

## Semantic Layer Patterns

### What Is a Semantic Layer?

A semantic layer is an abstraction between raw data and business users. It provides consistent metric definitions, standardized naming, and governed calculations — ensuring everyone sees the same numbers regardless of which tool they use.

### Semantic Layer Architecture

```
Raw Data (warehouse)
  ↓
Staging Models (clean, rename, type-cast)
  ↓
Intermediate Models (business logic, joins)
  ↓
Mart Models (one-table-per-entity or per-metric-domain)
  ↓
Semantic Layer (metric definitions, dimensions, filters)
  ↓
BI Tools (dashboards, ad-hoc queries, exports)
```

### Metric Definition Standard

```yaml
metric:
  name: monthly_active_users
  display_name: Monthly Active Users (MAU)
  description: Users who performed at least one core action in the last 30 days
  calculation: COUNT(DISTINCT user_id) WHERE last_core_action_date >= CURRENT_DATE - 30
  data_source: mart_users
  owner: data-lead
  dimensions:
    - plan_type
    - signup_source
    - geography
  filters:
    - exclude_internal: true
    - exclude_test_accounts: true
  grain: daily
  freshness: updated daily by 06:00 UTC
  caveats:
    - Does not include API-only users
    - "Core action" defined in event taxonomy
```

### Semantic Layer Best Practices

| Practice | Why |
|----------|-----|
| **One definition per metric** | Prevents conflicting numbers across dashboards |
| **Version controlled** | Changes to metric logic are tracked and reviewed |
| **Documented dimensions** | Users know what filters and breakdowns are available |
| **Tested** | Automated tests validate metric calculations daily |
| **Governed** | Changes require review by metric owner |

---

## dbt Modeling Patterns

### Model Layers

| Layer | Prefix | Purpose | Example |
|-------|--------|---------|---------|
| **Staging** | `stg_` | 1:1 with source, rename, type-cast, clean | `stg_stripe__charges` |
| **Intermediate** | `int_` | Business logic, joins, aggregations | `int_orders__pivoted_by_status` |
| **Mart** | `fct_` / `dim_` | Fact and dimension tables for consumption | `fct_orders`, `dim_customers` |
| **Metrics** | `mtr_` | Pre-aggregated metric tables | `mtr_daily_active_users` |

### Naming Conventions

| Convention | Rule | Example |
|------------|------|---------|
| **Source prefix** | `stg_{source}__{entity}` | `stg_stripe__subscriptions` |
| **Fact tables** | `fct_{verb_noun}` | `fct_order_items` |
| **Dimension tables** | `dim_{entity}` | `dim_customers` |
| **Boolean columns** | `is_` or `has_` prefix | `is_active`, `has_subscription` |
| **Date columns** | `_date` suffix | `signup_date`, `churned_date` |
| **Timestamp columns** | `_at` suffix | `created_at`, `updated_at` |
| **Count columns** | `_count` suffix | `order_count`, `session_count` |
| **ID columns** | `_id` suffix | `user_id`, `account_id` |

### dbt Testing Patterns

| Test Type | Purpose | Example |
|-----------|---------|---------|
| **not_null** | Critical columns are always populated | Primary keys, required fields |
| **unique** | No duplicates on primary keys | `user_id` in `dim_customers` |
| **accepted_values** | Values are in expected set | `status` in ('active', 'churned', 'trial') |
| **relationships** | Foreign keys are valid | `customer_id` references `dim_customers` |
| **custom** | Business logic validation | Revenue per order > 0, dates are reasonable |

---

## Self-Service Analytics

### Self-Service Maturity Model

| Level | Description | User Capability | Data Team Role |
|-------|-------------|-----------------|----------------|
| **1 - Request-Based** | All analysis goes through data team | Users submit tickets | Full-service analysis |
| **2 - Dashboard-Driven** | Key metrics available in dashboards | Users read dashboards | Build dashboards, answer ad-hoc |
| **3 - Guided Exploration** | Users can filter and drill-down | Users explore within guardrails | Design self-service tools, training |
| **4 - Self-Serve** | Users build their own analyses | Users write queries, build charts | Maintain platform, govern metrics, complex analysis |

### Enabling Self-Service

| Enabler | Implementation |
|---------|---------------|
| **Metric catalog** | Searchable directory of all governed metrics with definitions |
| **Curated datasets** | Clean, documented tables designed for exploration |
| **Templates** | Pre-built query templates for common analyses |
| **Training** | Regular data literacy sessions for non-technical users |
| **Guardrails** | Row-level security, query limits, governed dimensions |
| **Documentation** | FAQ, how-to guides, example analyses |

---

## Dashboard Performance Optimization

### Query Optimization Checklist

| Check | Action |
|-------|--------|
| **Pre-aggregate** | Materialize commonly used aggregations |
| **Limit date range** | Default to last 30/90 days, not all-time |
| **Reduce joins** | Denormalize for BI consumption |
| **Index properly** | Index columns used in filters and GROUP BY |
| **Cache results** | Cache slow queries with appropriate TTL |
| **Limit cardinality** | Reduce distinct values in dimension filters |

### Performance Benchmarks

| Metric | Target | Action if Exceeded |
|--------|--------|-------------------|
| **Dashboard load time** | < 5 seconds | Optimize queries, add caching |
| **Filter response time** | < 2 seconds | Pre-aggregate, reduce cardinality |
| **Export time** | < 10 seconds | Limit row count, optimize query |
| **Concurrent users** | Platform-dependent | Monitor, scale infrastructure |

---

*Last Updated: 2026-03-29*
*References: Edward Tufte visualization principles, dbt-labs/dbt-core, metabase/metabase, Evidence, Apache Superset*
