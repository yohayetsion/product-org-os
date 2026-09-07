# Sales Operations Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: `sales-ops`, `sales-dir`
**Secondary Users**: `account-exec`, `sdr`, `revenue-analyst`

<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - MEDDPICC framework (public methodology) — pipeline management and deal qualification
  - erxes/erxes (github.com/erxes/erxes, MIT License) — CRM automation and pipeline management patterns
  - GTM Engine (the GTM operating model) — pipeline tracking and outreach operations
  - Anthropic Sales plugin patterns — sales process automation
  Adapted and expanded for Product Org OS agents.
-->

---

## Pipeline Management Framework

### Pipeline Coverage Model

```
Required Pipeline = Quota × Coverage Ratio

Coverage Ratio by Segment:
  SMB:        3.0x - 3.5x (higher volume, lower conversion)
  Mid-Market: 3.5x - 4.0x (moderate volume, moderate conversion)
  Enterprise: 4.0x - 5.0x (low volume, high variance)

Example:
  Quarterly Quota: [TBD]
  Required Coverage: Quota × 4.0 = [TBD]
  Current Pipeline: [TBD]
  Gap: Required - Current = [TBD]
```

### Pipeline Velocity Formula

```
Pipeline Velocity = (# Qualified Opps × Win Rate × Average Deal Size) / Average Sales Cycle Length

Components:
  Qualified Opportunities: Deals past discovery stage
  Win Rate: Stage-adjusted or historical
  Average Deal Size: Segment-weighted
  Sales Cycle Length: In days, measured from creation to close

Improving any one component improves velocity.
```

### Pipeline Health Indicators

| Indicator | Healthy | Warning | Critical |
|-----------|---------|---------|----------|
| Coverage Ratio | 3.5x+ | 2.5-3.5x | Below 2.5x |
| Stage Distribution | Balanced pyramid | Top-heavy or bottom-heavy | Deals clustered in one stage |
| Average Age vs. Benchmark | Within 1.2x of segment average | 1.2-1.5x of average | Over 1.5x of average |
| Push Rate | Below 15% | 15-25% | Over 25% |
| New Pipeline Created | On pace for next quarter | Declining trend | Insufficient for coverage |
| Win Rate Trend | Stable or improving | Declining 5-10% | Declining 10%+ |

### Stage Hygiene Rules

| Rule | Action | Frequency |
|------|--------|-----------|
| **Stale Deal Audit** | Flag deals with no activity in 2x stage duration | Weekly |
| **Stage Verification** | Verify exit criteria for top 20 deals | Weekly (pipeline review) |
| **Close Date Audit** | Flag deals with close date in the past | Daily (automated) |
| **Amount Audit** | Flag deals with $0 or placeholder amounts | Weekly |
| **Dead Deal Removal** | Move to Closed-Lost if no engagement in 60 days | Monthly |

---

## Forecasting Models

### Forecast Categories

| Category | Definition | Confidence Level |
|----------|-----------|-----------------|
| **Closed** | Contract signed, revenue recognized | 100% |
| **Commit** | Will close this period, verbal agreement, paper in process | 90%+ |
| **Best Case** | Strong probability, some risk factors remain | 60-80% |
| **Upside** | Could close if things go well, not committed | 30-50% |
| **Pipeline** | Active but too early to forecast with confidence | 10-25% |

### Weighted Pipeline Forecast

```
Forecast = Σ (Deal Amount × Stage Probability)

Stage Probabilities (adjust to your data):
  Discovery:   10-15%
  Solution:    20-30%
  Evaluation:  40-50%
  Negotiation: 60-75%
  Closing:     80-90%
  Commit:      90-95%

Example:
  Deal A: $100K at Evaluation (45%) = $45K
  Deal B: $200K at Negotiation (70%) = $140K
  Deal C: $50K at Commit (92%) = $46K
  Weighted Forecast: $231K
```

### Forecast Accuracy Tracking

```
Forecast Accuracy = 1 - |Actual - Forecast| / Actual × 100

Track by:
  - Rep-level accuracy
  - Segment accuracy
  - Category accuracy (commit vs. best case vs. upside)
  - Rolling 4-quarter trend

Benchmarks:
  Elite: 90%+ accuracy
  Good: 80-90%
  Average: 70-80%
  Poor: Below 70%
```

### Forecast Review Cadence

| Review | Frequency | Participants | Focus |
|--------|-----------|-------------|-------|
| **Pipeline Review** | Weekly | Sales Dir + Reps | Deal progression, stage validation, blockers |
| **Forecast Call** | Weekly | Sales Dir + Sales Ops | Category review, risk assessment, gap analysis |
| **Commit Review** | Bi-weekly | Sales Dir + AEs with commits | Verify commit deals, paper process status |
| **QBR** | Quarterly | Sales + Exec | Performance review, next quarter plan |

---

## Territory Design Framework

### Territory Design Principles

| Principle | Description |
|-----------|-------------|
| **Market Potential Balance** | Territories should have roughly equal revenue potential, not equal current revenue |
| **Workload Balance** | Account count and complexity should be manageable for one rep |
| **Geographic Efficiency** | Minimize travel time and maximize face-to-face opportunity (if field sales) |
| **Strategic Alignment** | Align with company growth priorities (new markets, expansion, etc.) |
| **Stability** | Minimize disruptions — territory changes reset relationships |

### Territory Modeling Inputs

| Data Point | Source | Weight |
|-----------|--------|--------|
| **Total Addressable Market** | Industry data, firmographics | High |
| **Current Revenue** | CRM | Medium |
| **Pipeline in Territory** | CRM | Medium |
| **Account Count** | CRM + market data | Medium |
| **Historical Win Rate** | CRM | Low-Medium |
| **Strategic Accounts** | Sales leadership | High |
| **Competitive Density** | CI, win/loss data | Low |

### Territory Assignment Template

```markdown
## Territory Plan

**Territory**: [Name/ID]
**Owner**: [Rep Name]
**Segment**: [Enterprise / Mid-Market / SMB]

**Market Profile**:
| Metric | Value |
|--------|-------|
| Total Addressable Accounts | [TBD] |
| Current Customers | [TBD] |
| Current ARR | [TBD] |
| Expansion Potential | [TBD] |
| Net New Target | [TBD] |

**Strategic Accounts** (Top 10):
| Account | ARR/Potential | Stage | Priority |
|---------|--------------|-------|----------|

**Quota**:
| Period | New Business | Expansion | Total |
|--------|-------------|-----------|-------|
```

---

## Quota Setting Framework

### Quota Methodology

| Approach | Description | When to Use |
|----------|-----------|-------------|
| **Top-Down** | Company target divided by rep capacity | Early stage, limited historical data |
| **Bottom-Up** | Territory potential × win rate × average deal | Mature org with good data |
| **Blended** | Top-down target validated by bottom-up analysis | Recommended for most orgs |

### Quota Setting Checklist

- [ ] Company revenue target defined
- [ ] Segment allocation determined (new vs. expansion vs. renewal)
- [ ] Territory potential modeled for each rep
- [ ] Pipeline coverage ratio confirmed (3.5-5.0x)
- [ ] Ramp schedule defined for new hires
- [ ] Historical attainment data reviewed (aim for 60-70% of team at quota)
- [ ] Compensation plan aligned with quota levels
- [ ] Quota presented with supporting data, not as a mandate

### Quota Health Metrics

| Metric | Healthy | Warning |
|--------|---------|---------|
| % of team at quota | 55-70% | Below 40% or above 90% |
| Average attainment | 90-110% | Below 80% or above 130% |
| Quota-to-OTE ratio | 4-6x | Below 3x or above 8x |
| Ramp to full quota | 1-2 quarters | Over 3 quarters |

---

## Sales Analytics Framework

### Funnel Metrics

| Metric | Formula | Benchmark |
|--------|---------|-----------|
| **Lead-to-Meeting** | Meetings / Leads | 10-25% (inbound), 2-5% (outbound) |
| **Meeting-to-Opportunity** | Opps / Meetings | 30-50% |
| **Opportunity-to-Close** | Wins / Opps | 15-30% |
| **Lead-to-Close** | Wins / Leads | 1-5% |
| **Average Deal Size** | Total Revenue / Deals | Segment-dependent |
| **Sales Cycle Length** | Avg days from Opp creation to Close | Segment-dependent |
| **Push Rate** | Deals that pushed close date / Total | Below 15% |

### Activity Metrics

| Metric | Purpose | Caution |
|--------|---------|---------|
| Calls per day | Outbound effort | Do not optimize for volume over quality |
| Emails sent | Outreach volume | Track replies and meetings, not just sends |
| Meetings held | Engagement level | Qualify meeting quality, not just count |
| Proposals sent | Deal progression | Track proposal-to-close rate |
| Pipeline created | Leading indicator | Weight by quality (stage advancement rate) |

### Efficiency Metrics

| Metric | Formula | What It Tells You |
|--------|---------|-------------------|
| **CAC** | Total Sales + Marketing Cost / New Customers | Cost to acquire a customer |
| **CAC Payback** | CAC / (ARR × Gross Margin) × 12 | Months to recover acquisition cost |
| **Magic Number** | Net New ARR / Prior Quarter S&M Spend | Sales efficiency (target: 0.7-1.0+) |
| **Revenue per Rep** | Total Revenue / Quota-Carrying Reps | Rep productivity |
| **Win Rate by Source** | Wins / Opps, grouped by source | Which channels produce closeable pipeline |

---

## CRM Hygiene Standards

### Required Fields by Stage

| Stage | Required Fields |
|-------|----------------|
| **Discovery** | Company, contact, source, estimated value, close date, next step |
| **Solution** | Pain identified, decision criteria, champion identified |
| **Evaluation** | MEDDPICC score (3+ fields at 2+), technical contact, POC status |
| **Negotiation** | Proposal sent, pricing approved, legal contact, procurement timeline |
| **Closing** | Contract sent, expected signature date, paper process status |

### Data Quality Rules

| Rule | Check | Frequency |
|------|-------|-----------|
| No close date in the past | Automated flag | Daily |
| No $0 deal amounts | Automated flag | Daily |
| Next step populated | Pipeline review | Weekly |
| Contact role mapped | Stage gate | At stage transition |
| Activity in last 14 days | Stale deal flag | Weekly |
| MEDDPICC score updated | Pipeline review | Weekly |

---

## Sales Compensation Patterns

### Common Comp Structures

| Structure | Base/Variable Split | When to Use |
|-----------|-------------------|-------------|
| **50/50** | Equal base and variable | Standard AE, balanced incentive |
| **60/40** | Higher base | Complex/enterprise sales, longer cycles |
| **40/60** | Higher variable | Transactional sales, proven territory |
| **70/30** | High base, low variable | SDR, customer success, new market |

### Accelerator Models

| Model | Description | Incentive |
|-------|-----------|-----------|
| **Linear** | 1:1 pay for every dollar over quota | Steady, predictable |
| **Tiered** | Higher rate above threshold (e.g., 2x above 100%) | Rewards over-performance |
| **Uncapped** | No ceiling on variable comp | Maximum motivation for top performers |
| **SPIFs** | One-time bonuses for specific behaviors | Short-term behavior change |

---

## Sales Tech Stack Categories

| Category | Purpose | Common Tools |
|----------|---------|-------------|
| **CRM** | Deal and relationship management | Salesforce, HubSpot, Pipedrive, Close |
| **Sales Engagement** | Outbound sequences and cadences | Outreach, SalesLoft, Apollo, Lemlist |
| **Revenue Intelligence** | Call recording and coaching | Gong, Chorus, Clari |
| **Prospecting** | Lead data and enrichment | ZoomInfo, Apollo, LinkedIn Sales Nav |
| **CPQ** | Configure-price-quote | Salesforce CPQ, DealHub, PandaDoc |
| **Analytics** | Pipeline and performance dashboards | Clari, InsightSquared, native CRM |
| **Sales Enablement** | Content and training | Highspot, Seismic, Showpad |

---

## AI-Era Pipeline Ops & the Machine Buyer (2026)

<!-- Attribution:
  **Adapted from**:
    - Salesforce, State of Sales 2026 — selling-time + AI-adoption statistics (salesforce.com/sales/state-of-sales/sales-statistics/, Feb 2026)
    - autogpt.net, "Top AI Sales Tools of 2026" (autogpt.net/top-ai-sales-tools/)
    - Gartner top-2026 strategic prediction — 90% of B2B buying AI-agent-intermediated / ~$15T by 2028, as reported by GSPANN, Commercetools, Orbilon (Nov 2025-2026)
  **Source licence**: publicly-documented analyst/vendor patterns; no formal OSS license — cited, not claimed as proprietary.
  **V2V refinements**: framed AI hygiene as human-reviews-the-write; framed AI forecasting as a triangulation input over the existing weighted/category model (not a replacement); machine-buyer kept as a POINTER, not a commerce deep-dive, with cross-refs out.
-->

> Added 2026-06-24. The pipeline, forecasting, territory, quota, analytics, and CRM-hygiene frameworks above are **unchanged**. This section is additive: it covers the AI layer over operations and a forward pointer on the machine buyer.

### Agentic CRM Hygiene

The 2026 case for automation: Salesforce's State of Sales (Feb 2026) puts reps at ~28-30% selling time, with CRM updates a major drag. AI/agentic tooling now auto-fills fields, enriches contacts, detects stale deals, and flags data-quality violations against the rules already defined above (Stage Hygiene Rules, Data Quality Rules).

| Hygiene Task (from above) | 2026 AI-Assisted Mode | V2V Caveat |
|---------------------------|-----------------------|------------|
| Stale-deal audit | Agent flags + drafts a nudge | Manager still decides push vs. close-lost |
| Field completeness / next-step | Agent auto-fills from call/activity | **Human reviews the write** before it commits to CRM |
| Close-date / amount audit | Agent flags anomalies in real time | Correction is human-confirmed, not auto-applied |
| MEDDPICC score updates | Agent drafts from transcripts | Score is a draft — see `sales-methodology.md` §"AI-Assisted Deal Execution" |

**V2V caveat (NON-NEGOTIABLE): a human reviews the write.** Agentic hygiene that auto-commits to the CRM without review re-creates the garbage-in problem at machine speed. The agent drafts; the rep or ops owner confirms the write.

### AI-Augmented Forecasting

AI forecasting is a **triangulation input to** the weighted-pipeline and category models above — not a replacement. Run the AI forecast alongside the rep-committed and weighted-stage forecasts; where they diverge, that divergence is a *coaching and risk signal*, not an instruction to overwrite the human call. Forecast-accuracy benchmarks (Elite 90%+, etc.) are unchanged and still measured against actuals. Reward forecast accuracy over optimism — including over AI optimism.

### The Machine Buyer (Pointer)

A structural signal worth tracking, not yet a playbook: Gartner's top-2026 strategic prediction is that **90% of B2B buying will be AI-agent-intermediated, with over ~$15T of B2B spend flowing through AI-agent exchanges, by 2028** (reported across GSPANN, Commercetools, Orbilon, Nov 2025-2026). For sales operations this elevates two existing concerns: (1) **machine-readable, clean deal/product data becomes table stakes** — an AI buyer agent can only evaluate what it can parse, so CRM and catalog data quality (above) is now externally consequential; and (2) **stage definitions may need a "buyer-agent-mediated" variant** as agents do the research/compare/shortlist steps reps used to influence directly.

> **Cross-ref (anti-dup):** This is a *pointer only*. The full agentic-commerce / selling-to-a-machine treatment belongs in the companion `agentic-commerce.md` knowledge pack (the canonical home for buyer-agent mechanics, AP2/agent-payment rails, and catalog readiness) — see it for depth, not this section. The outbound/AI-SDR channel-economics angle is owned by `gtm-playbooks.md` §"AI-SDR market dynamics". Do not expand this section into a commerce deep-dive.

---

*Last Updated: 2026-06-24*
*References: MEDDPICC framework, erxes/erxes CRM patterns, GTM Engine, Anthropic Sales plugin patterns; AI-Era Pipeline Ops §: Salesforce State of Sales 2026, autogpt.net 2026, Gartner 2026 strategic prediction (via GSPANN/Commercetools/Orbilon)*
