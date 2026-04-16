# SaaS Metrics Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: @revenue-analyst, @fpa-analyst, @bizops, @investor-relations

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - alirezarezvani/claude-skills (github.com/alirezarezvani/claude-skills) — finance reference materials
  - T2D3 framework (Neeraj Agrawal, Battery Ventures) — SaaS growth benchmarking
  Adapted and expanded for Product Org OS agents.
-->

## Revenue Metrics

### ARR / MRR (Annual & Monthly Recurring Revenue)

**What**: The normalized recurring revenue run rate. MRR is the monthly figure; ARR = MRR x 12.

**MRR Components**:
```
MRR = New MRR + Expansion MRR + Reactivation MRR - Contraction MRR - Churned MRR
```

| Component | Definition |
|-----------|-----------|
| **New MRR** | Revenue from brand-new customers acquired in the period |
| **Expansion MRR** | Revenue increase from existing customers (upsells, cross-sells, seat additions) |
| **Reactivation MRR** | Revenue from previously churned customers who return |
| **Contraction MRR** | Revenue decrease from existing customers (downgrades, seat removals) |
| **Churned MRR** | Revenue lost from customers who cancelled entirely |

**MRR Waterfall**: Present all five components each period. The waterfall is the single most important SaaS revenue report.

**ARR Calculation**:
```
ARR = Current MRR x 12
```

**Common Pitfalls**:
- Do NOT annualize one-time fees, professional services, or usage overages into ARR
- Do NOT count multi-year deals at full contract value — use the annualized portion only
- Signed contracts with future start dates are "Committed ARR," not live ARR
- Be explicit about whether ARR is "ending ARR" (snapshot) or "average ARR" (period average)

---

### Net Revenue Retention (NRR)

**What**: Measures how much revenue from an existing customer cohort grows or shrinks over time, excluding new customers.

**Formula**:
```
NRR = (Beginning MRR + Expansion - Contraction - Churn) / Beginning MRR x 100%
```

**Benchmarks by Company Stage**:

| Stage | Median NRR | Top Quartile | Context |
|-------|-----------|-------------|---------|
| Seed / Pre-Product-Market Fit | 80-90% | >95% | Still finding fit; high churn expected |
| Series A | 95-105% | >110% | PMF found; expansion starting |
| Series B | 100-110% | >120% | Expansion engine running |
| Series C+ / Scale | 110-120% | >130% | Land-and-expand mature |
| Public SaaS (median) | 110-115% | >130% | Best-in-class: Snowflake, Datadog, Twilio historically >130% |

**Why It Matters**: NRR > 100% means the business grows even with zero new customer acquisition. This is the single metric most correlated with SaaS valuation multiples.

**Common Pitfalls**:
- Calculate on a cohort basis (same set of customers), not by comparing two period-end snapshots
- Exclude reactivations — NRR measures existing customer behavior, not win-backs
- Segment NRR by customer size; enterprise NRR often masks SMB churn problems

---

### Gross Revenue Retention (GRR)

**What**: Measures revenue retained from existing customers, ignoring expansion. GRR can never exceed 100%.

**Formula**:
```
GRR = (Beginning MRR - Contraction - Churn) / Beginning MRR x 100%
```

**Benchmarks**:

| Segment | Good | Great | Concerning |
|---------|------|-------|------------|
| Enterprise | >90% | >95% | <85% |
| Mid-Market | >85% | >90% | <80% |
| SMB | >75% | >85% | <70% |

**Why It Matters**: GRR isolates your product's ability to retain value independent of sales-driven expansion. A company with 80% GRR and 120% NRR is masking a retention problem with aggressive upselling.

---

### ARPU / ARPA Trends

**What**: Average Revenue Per User (ARPU) or Per Account (ARPA). Use ARPA when one account has multiple users.

**Formulas**:
```
ARPU = MRR / Total Active Users
ARPA = MRR / Total Active Accounts
```

**Trend Analysis**:
- **Rising ARPA**: Healthy expansion, successful upselling, or moving upmarket
- **Flat ARPA**: Growth is purely volume-driven; pricing power may be weak
- **Declining ARPA**: Downmarket shift, discounting pressure, or product commoditization

**Common Pitfalls**:
- Always track ARPA by cohort — blended ARPA can be misleading if customer mix shifts
- Separate ARPA for new vs. existing customers to detect pricing erosion on new deals

---

## Growth Metrics

### Month-over-Month Growth Rate

**Formula**:
```
MoM Growth = (MRR this month - MRR last month) / MRR last month x 100%
```

**Benchmarks**:

| Stage | Target MoM Growth |
|-------|-------------------|
| Pre-seed / MVP | 15-20%+ (small base) |
| Seed | 10-15% |
| Series A | 8-12% |
| Series B+ | 5-8% |
| Scale ($50M+ ARR) | 2-4% |

**Annualized Equivalent**: (1 + MoM%)^12 - 1. Example: 10% MoM = 214% annualized growth.

---

### T2D3 Framework

**What**: The venture-backed SaaS growth playbook — Triple, Triple, Double, Double, Double annual revenue over five years.

**The Pattern** (starting from ~$2M ARR):

| Year | Multiplier | ARR Target |
|------|-----------|-----------|
| Year 1 | 3x | $2M -> $6M |
| Year 2 | 3x | $6M -> $18M |
| Year 3 | 2x | $18M -> $36M |
| Year 4 | 2x | $36M -> $72M |
| Year 5 | 2x | $72M -> $144M |

**When to Reference**: Useful as a benchmark for VC-backed companies targeting $100M+ ARR. Not applicable to bootstrapped, lifestyle, or capital-efficient businesses.

**Common Pitfalls**:
- T2D3 assumes strong product-market fit is already achieved before Year 1
- Applies to ARR growth, not bookings or GMV
- Very few companies actually achieve T2D3; it is an aspirational framework, not a norm

---

### Rule of 40

**What**: A balanced scorecard combining growth rate and profitability. The sum should be >= 40%.

**Formula**:
```
Rule of 40 Score = Revenue Growth Rate (%) + Profit Margin (%)
```

**Profit Margin**: Typically EBITDA margin or FCF margin. Be consistent.

**Examples**:
```
Company A: 60% growth + (-20%) margin = 40 ✓
Company B: 20% growth + 25% margin = 45 ✓
Company C: 30% growth + 5% margin  = 35 ✗
```

**Benchmarks**:

| Score | Interpretation |
|-------|---------------|
| >60 | Elite (top decile public SaaS) |
| 40-60 | Strong |
| 25-40 | Acceptable for early-stage |
| <25 | Needs attention — neither growing fast nor profitable |

**Common Pitfalls**:
- Growth rate should be year-over-year, not MoM annualized (which inflates the number)
- At scale (>$100M ARR), profitability matters more; at early stage, growth matters more
- Some investors use a "Rule of 40 weighted" that gives 2x credit to growth: (Growth x 2) + Margin

---

### Quick Ratio (SaaS)

**What**: Measures growth efficiency — how much new and expansion revenue is generated relative to revenue lost.

**Formula**:
```
SaaS Quick Ratio = (New MRR + Expansion MRR) / (Churned MRR + Contraction MRR)
```

**Benchmarks**:

| Ratio | Interpretation |
|-------|---------------|
| >4.0 | Excellent — growing efficiently with low leakage |
| 2.0-4.0 | Good — healthy growth |
| 1.0-2.0 | Concerning — significant revenue leakage |
| <1.0 | Shrinking — losing more than gaining |

**Why It Matters**: A company can have strong top-line growth but a poor Quick Ratio if it is churning heavily and replacing lost revenue with expensive new acquisition.

---

## Unit Economics

### CAC (Customer Acquisition Cost)

**What**: The fully-loaded cost of acquiring one new customer.

**Formulas**:
```
Blended CAC = Total Sales & Marketing Spend / New Customers Acquired

Channel CAC = Channel-Specific S&M Spend / New Customers from That Channel
```

**What to Include in S&M Spend**:
- Sales team compensation (base + variable + benefits)
- Marketing team compensation
- Paid advertising and media
- Marketing tools and platforms
- Sales tools (CRM, outreach, etc.)
- Events and sponsorships
- Content production costs

**What to Exclude**: Customer success costs (post-sale), product costs, G&A overhead.

**Common Pitfalls**:
- Always use a lagged model — customers acquired this quarter were influenced by spend from prior quarters
- Segment CAC by channel (organic, paid, outbound, partner) — blended CAC hides channel economics
- Include sales ramp time — new AEs cost money before they produce

---

### LTV (Lifetime Value)

**What**: The total revenue (or gross profit) expected from a customer over the entire relationship.

**Calculation Methods**:

**Method 1 — Simple (for early-stage)**:
```
LTV = ARPA / Monthly Churn Rate
```

**Method 2 — Gross Margin Adjusted**:
```
LTV = (ARPA x Gross Margin %) / Monthly Churn Rate
```

**Method 3 — With Expansion (most accurate)**:
```
LTV = ARPA x Gross Margin % / (Monthly Churn Rate - Monthly Expansion Rate)
```
Only valid when churn rate > expansion rate. If expansion > churn (NRR > 100%), LTV is theoretically infinite — cap it at a reasonable time horizon (e.g., 5-7 years).

**Method 4 — Cohort-Based (gold standard)**:
Track actual cumulative revenue per cohort over time, fit a curve, and extrapolate.

**Common Pitfalls**:
- Use gross-margin-adjusted LTV for investment decisions — revenue LTV overstates value
- Do not use company-wide averages when segments have vastly different retention profiles
- Cap LTV projections at a reasonable horizon; "infinite LTV" is a modeling artifact, not reality

---

### LTV:CAC Ratio

**What**: The return on customer acquisition investment.

**Formula**:
```
LTV:CAC = Customer Lifetime Value / Customer Acquisition Cost
```

**Benchmarks**:

| Ratio | Interpretation |
|-------|---------------|
| >5:1 | Under-investing in growth — could spend more to acquire |
| 3:1-5:1 | Healthy — sustainable economics |
| 1:1-3:1 | Concerning — tight margins or long payback |
| <1:1 | Unsustainable — losing money on every customer |

**Common Pitfalls**:
- Compare like-for-like: if LTV is gross-margin-adjusted, CAC should be fully loaded
- Segment by customer type — enterprise LTV:CAC is usually very different from SMB
- A high ratio is not always good; >5:1 often signals under-investment in acquisition

---

### CAC Payback Period

**What**: The number of months to recover the cost of acquiring a customer.

**Formula**:
```
CAC Payback = CAC / (ARPA x Gross Margin %)
```

**Benchmarks**:

| Segment | Good | Great | Concerning |
|---------|------|-------|------------|
| SMB | <12 months | <6 months | >18 months |
| Mid-Market | <18 months | <12 months | >24 months |
| Enterprise | <24 months | <18 months | >30 months |

**Why It Matters**: Payback period determines how much working capital the business needs to fund growth. Shorter payback = less cash required = faster path to profitability.

---

### Magic Number

**What**: Measures sales efficiency — how much net new ARR is generated per dollar of sales and marketing spend.

**Formula**:
```
Magic Number = Net New ARR (this quarter) / Sales & Marketing Spend (prior quarter)
```

**Benchmarks**:

| Score | Interpretation | Action |
|-------|---------------|--------|
| >1.0 | Highly efficient — invest more aggressively in S&M |
| 0.75-1.0 | Efficient — continue investing |
| 0.5-0.75 | Moderate — optimize before scaling |
| <0.5 | Inefficient — fix unit economics before spending more |

**Common Pitfalls**:
- Use prior quarter S&M spend (lagged) because this quarter's revenue was driven by last quarter's investment
- Net new ARR = New ARR + Expansion ARR - Churned ARR - Contraction ARR
- One-time spikes (large enterprise deals) can distort a single quarter; track trailing averages

---

## Engagement Metrics

### DAU/MAU Ratio

**What**: Measures product stickiness — what fraction of monthly users engage daily.

**Formula**:
```
DAU/MAU = Daily Active Users / Monthly Active Users
```

**Benchmarks**:

| Ratio | Interpretation | Examples |
|-------|---------------|----------|
| >50% | Exceptional — daily habit | Slack, messaging apps |
| 25-50% | Strong — regular usage | Productivity tools, project management |
| 10-25% | Moderate — periodic usage | Analytics, reporting tools |
| <10% | Low — infrequent usage | Quarterly planning tools, tax software |

**Context**: The "right" ratio depends on the product's natural usage frequency. A payroll tool used biweekly is not worse than a chat app used daily.

---

### Feature Adoption Rate

**What**: The percentage of users or accounts using a specific feature.

**Formula**:
```
Feature Adoption Rate = Users Who Used Feature / Total Active Users x 100%
```

**Tracking Layers**:
- **Breadth**: What % of users have tried the feature at least once
- **Depth**: How frequently do adopters use it
- **Time to Adopt**: How long after signup until first use

**Why It Matters**: Features with high adoption and high depth drive retention. Features with low adoption may indicate discoverability problems or poor product-market fit for that capability.

---

### Time to Value (TTV)

**What**: The elapsed time from signup/purchase to the moment the customer first realizes meaningful value.

**Measurement Approaches**:
- **Technical TTV**: Time to complete setup and configuration
- **Functional TTV**: Time to first meaningful action (e.g., first report generated, first workflow automated)
- **Outcome TTV**: Time to first measurable business result

**Why It Matters**: Shorter TTV correlates strongly with higher activation rates and lower early churn. Every day between signup and value realization is a day the customer might leave.

---

### Product-Qualified Leads (PQLs)

**What**: Users or accounts that have demonstrated buying intent through product usage behavior, not just marketing engagement.

**Typical PQL Signals**:
- Exceeding free tier limits
- Using premium-only features in trial
- Inviting team members
- High engagement velocity (many actions in short time)
- Connecting integrations or importing data
- Returning multiple days in a row

**PQL vs. MQL**:

| Dimension | MQL | PQL |
|-----------|-----|-----|
| Signal source | Marketing engagement | Product usage |
| Intent quality | Inferred | Demonstrated |
| Typical conversion rate | 1-5% | 15-30% |
| Best for | Top-of-funnel, outbound | Product-led growth |

---

## Churn Analysis

### Logo Churn vs. Revenue Churn

**Formulas**:
```
Logo Churn Rate = Customers Lost / Beginning Customers x 100%
Revenue Churn Rate = MRR Lost / Beginning MRR x 100%
```

**Key Distinction**: A company can have high logo churn (many small customers leaving) but low revenue churn (large customers staying and expanding). Both must be tracked.

| Scenario | Logo Churn | Revenue Churn | Implication |
|----------|-----------|--------------|-------------|
| SMB leaking, enterprise strong | High | Low | Acceptable if moving upmarket intentionally |
| Large customer lost | Low | High | Concentration risk; investigate immediately |
| Both high | High | High | Product-market fit or retention crisis |

---

### Cohort Analysis Methodology

**What**: Grouping customers by their start date (or other attribute) and tracking behavior over time.

**Steps**:
1. **Define cohorts**: Usually by signup month/quarter. Can also segment by acquisition channel, plan, or company size.
2. **Choose the metric**: Revenue retention, logo retention, engagement, or feature adoption.
3. **Build the matrix**: Rows = cohorts, Columns = months since signup, Cells = metric value.
4. **Read the curves**: Are newer cohorts retaining better or worse than older ones? Is there a "shelf" where retention flattens?

**What to Look For**:
- **Improving cohorts over time**: Product and onboarding are getting better
- **Consistent drop at Month 3**: Onboarding or value realization problem
- **No flattening**: Product has not found a retention floor; churn is linear
- **Segment differences**: Enterprise cohorts retain differently than SMB

---

### Churn Prediction Signals

**Leading indicators that a customer is at risk**:

| Signal | Timeframe | Weight |
|--------|-----------|--------|
| Login frequency declining | 2-4 weeks before churn | High |
| Support tickets increasing | 4-6 weeks before churn | Medium |
| Key feature usage dropping | 2-4 weeks before churn | High |
| Champion left the company | Variable | Very High |
| Contract renewal approaching with no expansion discussion | 60-90 days before renewal | High |
| NPS/CSAT score dropped | 1-3 months before churn | Medium |
| Billing failures (involuntary) | Immediate | High |
| Competitor evaluation signals | Variable | High |

---

### Voluntary vs. Involuntary Churn

| Type | Cause | Fix |
|------|-------|-----|
| **Voluntary** | Customer actively cancels — dissatisfaction, budget cuts, competitor switch, no longer needs the product | Improve product, onboarding, customer success, competitive positioning |
| **Involuntary** | Payment failure — expired card, insufficient funds, billing errors | Dunning sequences, card updater services, pre-expiry reminders, payment retry logic |

**Involuntary churn typically accounts for 20-40% of total churn in SMB SaaS.** Fixing dunning alone can recover 30-50% of involuntary churn.

---

## Efficiency Metrics

### Burn Multiple

**What**: Measures how efficiently a company converts cash burn into revenue growth. Lower is better.

**Formula**:
```
Burn Multiple = Net Burn / Net New ARR
```

**Benchmarks**:

| Burn Multiple | Interpretation |
|---------------|---------------|
| <1.0x | Amazing — generating more ARR than burning |
| 1.0-1.5x | Great — efficient growth |
| 1.5-2.0x | Good — acceptable for early-stage |
| 2.0-3.0x | Mediocre — needs improvement |
| >3.0x | Concerning — burning cash faster than creating value |

**Why It Matters**: The Burn Multiple (coined by David Sacks) has become a key investor metric in capital-constrained environments. It captures what Rule of 40 misses: the cash cost of growth.

**Common Pitfalls**:
- Net Burn = Total cash out - Total cash in (operating, not fundraising)
- A company with negative burn (cash-flow positive) has a burn multiple of 0 or negative — which is ideal
- Burn multiple is most useful at scale; very early-stage companies will naturally have high burn multiples

---

### Hype Ratio

**What**: Compares implied ARR from valuation to actual ARR. Measures how much of a company's valuation is "hype" vs. revenue-backed.

**Formula**:
```
Hype Ratio = Enterprise Value / ARR
```

This is effectively the ARR multiple. In public SaaS, this is the EV/Revenue multiple.

**Benchmarks** (private SaaS, 2024-2026 environment):

| Hype Ratio | Interpretation |
|-----------|---------------|
| <5x | Value territory — mature or slower growth |
| 5-15x | Fair — typical for growth-stage SaaS |
| 15-30x | Premium — high growth + strong retention required to justify |
| >30x | Hype-heavy — needs exceptional metrics or market timing |

**Note**: Benchmarks shift dramatically with market conditions. In 2021, 30-50x was common for high-growth SaaS; by 2023-2025, 10-20x became the norm.

---

### SaaS Operating Benchmarks by Stage

| Metric | Seed | Series A | Series B | Series C+ / Scale |
|--------|------|----------|----------|--------------------|
| ARR | $0-1M | $1-5M | $5-20M | $20M+ |
| YoY Growth | >200% | 100-200% | 70-100% | 40-70% |
| NRR | >80% | >100% | >110% | >115% |
| GRR | >70% | >80% | >85% | >90% |
| Gross Margin | >60% | >65% | >70% | >75% |
| LTV:CAC | >2:1 | >3:1 | >3:1 | >3.5:1 |
| CAC Payback | <24 mo | <18 mo | <15 mo | <12 mo |
| Burn Multiple | <3.0x | <2.0x | <1.5x | <1.5x |
| Rule of 40 | N/A (growth focused) | >30 | >35 | >40 |
| Magic Number | >0.5 | >0.75 | >0.75 | >0.8 |
| Headcount | 5-15 | 15-50 | 50-150 | 150+ |

**Caveat**: These are median benchmarks for VC-backed B2B SaaS. Bootstrapped, PLG, vertical SaaS, and usage-based models may have different healthy ranges.

---

## Reporting Frameworks

### Board Deck Metrics Template

**Frequency**: Quarterly (minimum). Monthly for early-stage.

**Recommended Layout**:

| Section | Metrics |
|---------|---------|
| **Revenue Health** | ARR (ending), MRR waterfall (new/expansion/contraction/churn), ARR growth YoY, NRR, GRR |
| **Growth Efficiency** | Net new ARR, Magic Number, Quick Ratio, Rule of 40 score |
| **Unit Economics** | Blended CAC, LTV:CAC, CAC Payback, Gross Margin |
| **Customer Health** | Total customers, logo churn rate, revenue churn rate, top 10 customer concentration |
| **Pipeline & Sales** | Pipeline coverage, win rate, average deal size, sales cycle length |
| **Cash & Runway** | Cash balance, monthly burn, runway (months), Burn Multiple |

**Presentation Tips**:
- Always show trend lines (3-6 months minimum), not just point-in-time snapshots
- Highlight cohort improvements or deteriorations
- Flag any metric that crossed a threshold (positive or negative)
- Include brief commentary on "why" behind significant changes

---

### Investor Metrics Package

**For fundraising or investor updates. More detail than board deck.**

| Category | Metrics |
|----------|---------|
| **Headline** | ARR, ARR growth, NRR, Gross Margin, Burn Multiple, Rule of 40 |
| **Revenue Detail** | MRR waterfall (12-month history), ARR by segment, ARPA trend, revenue concentration (top 10/20 customers as % of ARR) |
| **Retention Detail** | NRR and GRR by segment, cohort retention curves (revenue and logo), monthly churn rate trend |
| **Unit Economics** | CAC by channel, LTV:CAC by segment, CAC Payback by segment, Magic Number (trailing 4 quarters) |
| **Engagement** | DAU/MAU, feature adoption for core features, time to value, PQL conversion rate (if PLG) |
| **Efficiency** | Burn Multiple (trailing 4 quarters), gross margin trend, operating expense as % of revenue by category |
| **Forward Looking** | Pipeline, quota attainment, expansion pipeline, renewal forecast |

---

### Operating Review Metrics

**For internal leadership. Weekly or biweekly cadence.**

| Focus Area | Metrics | Cadence |
|-----------|---------|---------|
| **Weekly Pulse** | New MRR added, churned MRR, pipeline created, deals closed, active trials | Weekly |
| **Sales Efficiency** | Win rate, sales cycle, average deal size, quota attainment by rep | Biweekly |
| **Product Health** | DAU/MAU, feature adoption changes, NPS/CSAT, support ticket volume | Biweekly |
| **Customer Risk** | At-risk accounts (usage decline), upcoming renewals, expansion opportunities | Weekly |
| **Acquisition** | Lead volume by channel, MQL-to-PQL conversion, trial-to-paid conversion, CAC by channel | Biweekly |
| **Financial** | Cash burn, forecast vs. actual, expense variance | Monthly |

---

## Common Cross-Metric Pitfalls

| Pitfall | Why It Happens | How to Avoid |
|---------|---------------|--------------|
| Conflating bookings with revenue | Bookings = contract signed; revenue = recognized over time | Report both separately; never mix in the same chart |
| Using gross churn when net churn tells a different story | Gross churn ignores expansion | Always report both; net churn for health, gross churn for retention quality |
| Comparing metrics across different definitions | One team uses MRR, another uses ARR; one includes overages, another doesn't | Publish a metrics glossary with canonical definitions |
| Celebrating growth without efficiency context | 100% growth at 5x burn multiple is not healthy | Always pair growth metrics with efficiency metrics |
| Ignoring seasonality | Q4 enterprise deals inflate quarterly metrics | Use trailing 12-month or trailing 4-quarter averages for trend analysis |
| Revenue concentration blindness | 3 customers = 40% of ARR; lose one and growth story breaks | Track and report top-10 and top-20 customer concentration every period |
