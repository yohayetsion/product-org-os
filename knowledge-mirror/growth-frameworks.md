# Growth Frameworks — Methods & Playbooks

## Overview

Growth is the discipline of systematically increasing the rate at which a product acquires, activates, retains, and expands its user base. It differs from marketing in that it operates at the intersection of product, data, and distribution — changing the product itself to drive compounding growth, not just advertising spend.

This reference covers the foundational frameworks, measurement systems, and experimentation methods that growth practitioners use. The content is ordered from strategic framing to operational execution — start with growth loops and AARRR to establish your model, then move to experimentation and channel analysis to improve it.

**Version**: 1.0.0
**Type**: Knowledge Pack
**Primary Users**: 📈 Growth Marketer, 🎙️ CMO, 📢 Marketing Director

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - alirezarezvani/claude-skills (growth marketing reference)
  - Andrew Chen's growth loop frameworks and viral coefficient work
  - Brian Balfour's cohort analysis and retention curve methodology
  - Reforge growth systems curriculum
  - Sean Ellis's AARRR/Pirate Metrics framework
  Adapted and expanded for Product Org OS agents.
-->

---

## Growth Loop Framework

### What Is a Growth Loop

A growth loop is a closed system where the output of one cycle becomes the input of the next. Unlike funnels (which are linear and leak), loops compound — each iteration produces more than the last.

```
                  ┌─────────────────────────────────────────────┐
                  │                                             │
                  ▼                                             │
            New Users Enter                             Existing users take
            the product                                 actions that create
                  │                                     new inputs
                  ▼                                             │
            Core product                                        │
            experience                                          │
                  │                                             │
                  ▼                                             │
            Output (content / invites /                         │
            data network / SEO / referrals) ───────────────────┘
```

**Key insight**: Sustainable growth comes from building loops, not buying traffic. Ad spend is a one-time push; a loop compounds.

---

### The Four Growth Loop Archetypes

#### 1. Acquisition Loop (Viral / Sharing)
```
User creates value → shares with network → new users join → they create value → repeat

Examples:
- Dropbox: Refer a friend → both get storage → referee joins → refers more friends
- Canva: User shares design → viewer sees "Made with Canva" → clicks → signs up
- Notion: User publishes template → template gets discovered → reader signs up

Inputs to track:  invite rate, share rate, K-factor (see Viral Coefficient section)
Output metric:    Organic sign-ups from existing users
```

#### 2. Engagement Loop (Habit / Retention)
```
User takes core action → receives value / reward → prompted to return → takes action again

Examples:
- LinkedIn: Post → get likes/comments → notification draws user back → post again
- Duolingo: Complete lesson → streak maintained → loss aversion brings user back → complete lesson
- Slack: Message sent → colleague replies → notification → return to Slack

Inputs to track:  DAU/MAU ratio, notification CTR, streak rates
Output metric:    Retention rate, session frequency
```

#### 3. Content / SEO Loop (Distribution)
```
User generates content → content indexed by search engines → organic traffic arrives → some convert → create more content

Examples:
- Quora: User answers question → answer ranks on Google → searcher arrives → reads + maybe answers
- Yelp: Business owner claims listing → adds content → review indexed → searcher finds restaurant → leaves review
- GitHub: Developer pushes code → repo indexed → developer searches → finds GitHub result → signs up

Inputs to track:  content creation rate, indexed pages, organic search traffic
Output metric:    Organic sessions from search, SEO-attributed sign-ups
```

#### 4. Paid Loop (Performance Marketing)
```
Revenue generated → reinvested in paid acquisition → new users join → generate revenue → reinvest

Condition for a loop (not just a funnel):
  LTV:CAC > 3:1  AND  Payback period ≤ 12 months (ideally ≤ 6 months)

Inputs to track:  LTV, CAC, payback period, ROAS by channel
Output metric:    Marginal CAC as spend scales (watch for diminishing returns)
```

### Loop Identification Exercise

For each of your current growth channels, ask:
1. What is the output of a user taking the core action?
2. Does that output create new users, or just retain existing ones?
3. If it creates new users, does the system automatically route that output back as input?
4. If yes → you have a loop. If no → you have a funnel (leaky, doesn't compound).

---

## AARRR Pirate Metrics

### Framework Overview

AARRR (coined by Dave McClure) is a funnel model for mapping the customer lifecycle to measurable stages. It is a diagnostic framework, not a growth strategy.

```
Acquisition  →  Activation  →  Retention  →  Revenue  →  Referral
   │                │               │             │           │
How do they     Do they have    Do they come    Do they     Do they
come to us?     a good first    back?           pay?        tell others?
                experience?
```

Note: Some practitioners reorder to AARRR-Referral last; others use RARRA (Retention first) to emphasize that retention is the foundation of all other growth.

---

### Acquisition

**Definition**: A potential user becomes aware of the product and takes the first step toward trying it (visits site, installs app, signs up).

**Key Metrics**:

| Metric | Formula | Typical Benchmark (SaaS) |
|--------|---------|--------------------------|
| Visitor-to-sign-up rate | Sign-ups / Unique visitors | 2–5% |
| CAC by channel | Spend / New users acquired | Varies; model vs LTV |
| Organic vs paid mix | Organic sign-ups / Total sign-ups | Target >50% organic at scale |
| Time-to-sign-up | Time from first visit to account creation | Median, not mean |

**Acquisition Channel Taxonomy**:
- **Paid**: Search ads, social ads, display, sponsorships
- **Organic Search**: SEO, content marketing
- **Viral / Word of Mouth**: Referrals, social sharing, product-led virality
- **Partnerships**: App stores, integrations, BD deals
- **Community**: Open source, forums, developer ecosystems
- **Direct / Brand**: Email, PR, offline events

---

### Activation

**Definition**: A new user reaches the "aha moment" — the first experience of the core value the product promises. Activation is the most high-leverage stage for most products.

**Key Metrics**:

| Metric | Formula |
|--------|---------|
| Activation rate | Users who reach activation milestone / Total sign-ups |
| Time-to-activate | Median time from sign-up to first value moment |
| Drop-off by step | Users completing step N / Users completing step N-1 |
| Setup completion | Users who complete onboarding checklist / Total sign-ups |

**Finding the Activation Milestone**:
```
Method: Cohort correlation analysis
1. Define candidate activation events (e.g., "created first project", "invited teammate", "ran first query")
2. For each cohort, compare D30 retention of users who hit event vs. those who did not
3. The event with the highest retention lift that occurs early (D1-D7) is your activation milestone
4. This becomes your North Star for activation optimization
```

**Note**: Activation is a lagging indicator. It measures whether you've successfully communicated and delivered the core value promise. If activation is low, the problem is either that users don't understand the value (onboarding/messaging problem) or don't reach it (UX/friction problem).

---

### Retention

**Definition**: An activated user returns to the product repeatedly. Retention is the foundation of all other growth metrics — without it, acquisition is pouring water into a leaky bucket.

**Key Metrics**:

| Metric | Definition | Calculation |
|--------|-----------|-------------|
| Day N Retention | % of users still active N days after sign-up | Users active on day N / Users who signed up |
| Weekly Retention | % of weekly cohort active the following week | Active users week W+1 / Active users week W |
| Monthly Retention | % of monthly cohort active the following month | MAU month M+1 / MAU month M |
| Retention by cohort | Retention for a specific sign-up cohort over time | Cohort analysis table |

**Retention Curve Shapes**:

```
Healthy retention — flattens at a non-zero plateau:
  100% ─┐
        │╲
        │  ╲___________   ← plateau (retained base uses product regularly)
   D0   D7  D30  D90  D180

Leaky (no retention) — approaches zero:
  100% ─┐
        │╲
        │  ╲
        │    ╲
        │      ╲__________  ← approaches 0% (product has no retained value)

Resurrection (smile curve):
  100% ─┐
        │╲          ╱
        │  ╲______╱   ← win-back / seasonal campaigns working
```

**Action**: If your retention curve approaches zero, fix retention before investing in acquisition. Adding more users to a product with zero retention only accelerates burn rate.

---

### Revenue

**Definition**: Users generate economic value for the business. This stage measures monetization efficiency.

**Key Metrics**:

| Metric | Formula |
|--------|---------|
| ARPU | Total Revenue / Total Active Users |
| ARPA | Total Revenue / Total Active Accounts |
| MRR | Sum of all active monthly recurring subscriptions |
| ARR | MRR × 12 |
| LTV | ARPU × Average Customer Lifetime (or ARPU / Churn Rate) |
| LTV:CAC ratio | LTV / CAC — target >3:1 for SaaS |
| Payback period | CAC / (ARPU × Gross Margin) — target <12 months |

**Revenue expansion metrics** (for SaaS):

| Metric | Definition |
|--------|-----------|
| Net Revenue Retention (NRR) | (Starting MRR + Expansion - Contraction - Churn) / Starting MRR |
| Expansion MRR | New MRR from upsells and cross-sells to existing accounts |
| Contraction MRR | Lost MRR from downgrades |
| Churn MRR | Lost MRR from cancellations |

NRR > 100% means existing customers are paying you more over time — the business grows even with zero new customers. Best-in-class SaaS achieves 120-130% NRR.

---

### Referral

**Definition**: Existing users bring in new users, creating organic acquisition. The referral stage closes the loop from retention back to acquisition.

**Key Metrics**:

| Metric | Formula |
|--------|---------|
| Referral rate | Users who made a referral / Total active users |
| Referral conversion rate | Referred sign-ups / Referral invites sent |
| K-factor | Invites per user × Referral conversion rate (see Viral Coefficient section) |
| Referred user LTV vs organic | Compare LTV of referred users vs other channels |

**Note**: Referred users typically have 16-25% higher LTV than non-referred users (they come with social proof and have a relationship with an existing user).

---

## North Star Metric Framework

### What Is a North Star Metric

A single metric that best captures the core value your product delivers to customers. It aligns the entire team around the same output and serves as the leading indicator of long-term revenue.

```
Properties of a good North Star Metric:
  ✓ Measures value delivered to customers (not vanity metrics like page views)
  ✓ Predictive of long-term revenue (leading, not lagging)
  ✓ Actionable — every team can influence it
  ✓ Understandable — can be explained to any team member in one sentence
  ✓ Not a ratio — an absolute count so that growth shows up clearly
```

### North Star Examples by Business Type

| Company Type | North Star Metric | Why |
|-------------|------------------|-----|
| B2B SaaS (seat-based) | Weekly active teams | Teams using product = value delivered |
| B2B SaaS (usage-based) | API calls per month | Usage = customer commitment |
| Consumer social | DAU / MAU ratio | Habit strength |
| Marketplace (supply) | Listings with ≥1 booking/month | Supply quality + demand match |
| E-commerce | Orders per month | Direct revenue proxy |
| Media / Content | Monthly reading minutes | Engagement depth |
| Gaming | Daily sessions per DAU | Addiction / engagement |

### North Star Identification Process

```
Step 1: List 5-10 candidate metrics
Step 2: Filter: Is it a measure of value to users? (eliminate pure revenue metrics)
Step 3: Filter: Is it predictive of revenue? (run correlation analysis if data exists)
Step 4: Filter: Can every team influence it? (eliminate metrics owned by one team)
Step 5: Test comprehension: ask 10 team members to explain it — if they can't, simplify
Step 6: Select one. Commit to it for at least 6 months.
```

### The NSM Tree

```
North Star Metric
├── Input Metric 1 (lever)
│   ├── Sub-driver 1a
│   └── Sub-driver 1b
├── Input Metric 2 (lever)
│   ├── Sub-driver 2a
│   └── Sub-driver 2b
└── Input Metric 3 (lever)
```

Decompose the NSM into the 3-5 input metrics (levers) that directly drive it. Teams own specific levers. This is how the NSM cascades into team-level OKRs.

---

## Product-Led Growth (PLG) Strategy

### PLG vs. Sales-Led Growth

| Dimension | Product-Led Growth | Sales-Led Growth |
|-----------|-------------------|-----------------|
| Primary acquisition | Free tier / trial / freemium | SDR/BDR outreach |
| Conversion driver | Product experience | Sales relationship |
| CAC | Low (product does the work) | High (human labor) |
| Best fit | Self-serve products, individual/team buyers | Complex enterprise, long sales cycles |
| Time to value | Immediate | Weeks to months |
| Scalability | Highly scalable | Linear with headcount |
| NRR driver | In-product expansion signals | Renewal + upsell by CSM |

### Free Tier Design Principles

**The goal**: The free tier must deliver enough value that users become habituated and want more — not so much value that they never upgrade.

```
Freemium Design Constraints — choose your limit type:

Feature limits:     Free = basic features; Paid = advanced features
Usage limits:       Free = up to X; Paid = unlimited or higher limits
Seat limits:        Free = 1-5 users; Paid = full team
Storage limits:     Free = 5GB; Paid = 100GB+
Branding limits:    Free = includes product branding; Paid = white-label

The limit must be:
  (a) hit by users who are getting genuine value (not too low)
  (b) felt as a real constraint, not a soft suggestion (not too high)
  (c) aligned with the expansion vector (usage limit → usage-based pricing)
```

### Activation Optimization for PLG

```
PLG Activation Checklist:
  □ Time-to-value < 5 minutes for the median new user
  □ Sign-up requires no credit card (removes commitment barrier)
  □ Onboarding is contextual, not a generic product tour
  □ First session delivers one concrete output the user keeps (a file, a report, a result)
  □ Empty states have content suggestions, templates, or sample data
  □ Activation milestone is tracked as a product event
  □ Users who don't activate within 48h receive a nudge (email or in-app)
```

### Expansion Revenue in PLG

```
Expansion triggers (monitor these in product):
  - User hitting a usage/seat/storage limit
  - User inviting teammates (viral + expansion signal)
  - User accessing a locked premium feature
  - Power user behavior (>N actions per week for >M weeks)

PQL (Product Qualified Lead): a user who has exhibited behavior predictive of
conversion. Define your PQL criteria based on activation and engagement signals.

PQL criteria example:
  - Created ≥3 projects AND
  - Invited ≥1 team member AND
  - Active for ≥2 of last 4 weeks
```

---

## Viral Coefficient

### Formula

```
K = i × r

Where:
  K = Viral Coefficient
  i = Average number of invitations sent per existing user
  r = Conversion rate of invitations (invited → signed up)

Examples:
  K = 2 invites × 25% conversion = 0.5   → sub-viral (growth depends on acquisition)
  K = 3 invites × 40% conversion = 1.2   → viral (each user generates more than one new user)
  K = 5 invites × 30% conversion = 1.5   → strongly viral
```

### K-Factor Interpretation

| K-Factor | Meaning | Strategy |
|----------|---------|----------|
| K < 1 | Each cohort produces fewer users than the prior | Growth requires sustained acquisition investment |
| K = 1 | Each cohort reproduces exactly (neutral) | Flat organic growth; acquisition sustains total user base |
| K > 1 | Each cohort produces more users than the prior | Exponential organic growth |

**Important**: Most companies operate with K < 1. That is not a failure — it means you need acquisition and retention to drive growth alongside the referral mechanism. Pure virality (K > 1) is rare and typically only in the early phase of a viral product.

### Viral Loop Cycle Time

```
Total Viral Growth = f(K, cycle time)

A K of 1.5 with a 30-day cycle is far slower than K of 1.5 with a 3-day cycle.

Cycle time = time between a user joining and their invites being sent + converted

Optimize both K and cycle time. Often easier to reduce cycle time (improve UX of
invite flow, trigger invites earlier in onboarding) than to increase K itself.
```

### Referral Program Design

**What makes referral programs work**:

| Principle | Guidance |
|-----------|---------|
| Incentive alignment | Both referrer AND referee must benefit (double-sided reward) |
| Incentive timing | Reward immediately on sign-up, not after a purchase |
| Incentive size | Large enough to motivate action; not so large it attracts fraud |
| Friction | One-click sharing; pre-written message; multiple share channels |
| Trigger timing | Ask for referral immediately after activation (peak satisfaction moment) |
| Social proof | Show how many friends are already on the platform |

**Referral program structures**:
```
Cash reward:         $X for each referral (Uber, Cash App)
Credit reward:       $X account credit (Airbnb, Dropbox storage)
Feature unlock:      Unlock premium feature for N referrals
Discount ladder:     Each referral = % off next purchase
Mutual benefit:      "Give $X, get $X" — double-sided
Gamified:            Leaderboard, badges, tiered rewards
```

---

## Retention Curve Analysis

### Cohort Analysis Structure

```
Cohort Table Format:
              Week 0   Week 1   Week 2   Week 3   Week 4  ...
Jan Cohort:   100%     45%      32%      28%      27%
Feb Cohort:   100%     48%      35%      30%      29%
Mar Cohort:   100%     52%      40%      36%      36%

Reading the table:
  - Each row is users who signed up in that month
  - Each column is % still active N weeks after sign-up
  - Flatten = plateau forming (healthy retained base)
  - Continuous decline = no retained value
  - Row comparison = is retention improving over cohorts? (product improvement signal)
```

### J-Curve Recognition

```
A J-curve appears when early retention is low but improves sharply with engagement.

  100%
    |╲
    |  ╲
    |    ╲___   ← early drop
    |        ╲___
    |            ╲   ← secondary decline
    |              ╲
   D0  D1  D3  D7  D14  D30

Versus healthy early retention:
  100%
    |╲
    |  ╲
    |    ╲____________________  ← plateau after D7
   D0  D1  D3  D7  D14  D30
```

### Retention Segmentation

Segment retention curves by:
- **Acquisition channel**: Do SEO users retain better than paid? (channel quality signal)
- **Activation milestone**: Do activated users retain at 3x the rate of non-activated? (activation impact)
- **Plan/tier**: Do paid users retain better than free? (monetization health)
- **Geography**: Any regional differences? (localization opportunity)
- **Use case**: Does a specific workflow segment retain much better? (ICP signal)

---

## Growth Experimentation Framework

### ICE Scoring

Prioritize experiments with ICE: Impact × Confidence × Ease (each 1-10 scale).

```
ICE Score = Impact × Confidence × Ease

Impact:     How much will this move the needle if it works? (10 = massive, 1 = trivial)
Confidence: How confident are we the hypothesis is correct? (10 = near certain, 1 = wild guess)
Ease:       How easy is it to implement and test? (10 = 1 day, 1 = 3 months of eng work)

Example:
  Hypothesis: Adding social proof counter to sign-up page increases activation
  Impact: 7 (could move activation 10-15%)
  Confidence: 8 (strong evidence from other products and heatmap data)
  Ease: 9 (one-day implementation)
  ICE Score: 7 × 8 × 9 = 504

  Hypothesis: Rebuilding onboarding flow with interactive product tour
  Impact: 9
  Confidence: 4 (no evidence yet)
  Ease: 2 (3-month engineering project)
  ICE Score: 9 × 4 × 2 = 72

→ Test social proof first. Gather data before committing to onboarding rebuild.
```

### Hypothesis Template

```
We observed: [data / user research finding that identifies the problem]

We believe that: [the specific change we are making]

Will cause: [the expected outcome / behavior change]

For: [the specific user segment this applies to]

We'll measure this by: [primary metric + secondary guardrail metric]

We consider it a success if: [quantitative threshold, e.g., +10% activation rate]

Our confidence level is: [high / medium / low] because [evidence or rationale]

Minimum sample size needed: [N per variant, based on power calculation]
```

### Minimum Sample Size Reference

| Baseline Conversion | Target Relative Lift | Required Sample (per variant, 80% power, α=0.05) |
|--------------------|---------------------|--------------------------------------------------|
| 1% | 30% (1.0% → 1.3%) | ~20,000 |
| 2% | 20% (2.0% → 2.4%) | ~16,000 |
| 5% | 10% (5.0% → 5.5%) | ~14,000 |
| 10% | 10% (10% → 11%) | ~7,000 |
| 20% | 5% (20% → 21%) | ~15,000 |
| 30% | 5% (30% → 31.5%) | ~10,000 |

**Rule of thumb**: The smaller the baseline conversion and the smaller the lift you want to detect, the more sample you need. Don't start a test you can't finish.

### Experiment Documentation Standard

```
Experiment ID: EXP-2026-042
Name: Sign-up page social proof counter
Hypothesis: [see template above]
Start date: 2026-03-15
End date: 2026-04-05 (or when N reached)
Owner: [growth marketer]
Engineer: [name]

Variant A (Control): Current sign-up page, no social proof
Variant B (Treatment): "Join 47,000 teams already using [Product]" above CTA

Primary metric: Activation rate (% who complete first project within 7 days)
Guardrail metrics: Sign-up rate (should not decrease), D30 retention (should not decrease)

Sample size target: 5,000 per variant
Traffic split: 50/50

Results: [fill in after experiment]
Decision: [Implement / Iterate / Discard]
Learning: [what we learned, regardless of outcome]
```

---

## User Activation Framework

### The Aha Moment

The "aha moment" is the specific product experience where a new user first understands and feels the product's core value. It is not an abstract concept — it is a concrete product event that can be instrumented and optimized.

```
Finding the Aha Moment (data-driven):

1. Instrument all meaningful first-session actions as events
   (e.g., created_project, invited_teammate, published_report, ran_query)

2. For each event, build a cohort:
   - Cohort A: Users who performed the event in their first week
   - Cohort B: Users who did not

3. Compare D30 / D60 retention for each event cohort

4. The event that produces the largest retention lift AND occurs early (D1-D3)
   is the aha moment candidate

5. Validate with user interviews: do users who hit the event describe an "aha"?

6. Instrument it as your activation milestone and optimize to get more users there faster
```

### Activation Milestone Ladder

```
New user enters → Onboarding begins
        │
        ▼
   Setup milestone:   User completes minimum viable setup
   (e.g., connected first data source, imported first file)
        │
        ▼
   Aha milestone:     User experiences core value for the first time
   (e.g., first insight generated, first design created, first message sent)
        │
        ▼
   Habit milestone:   User has returned 3+ times and used core feature repeatedly
   (e.g., used core feature in 3 of 4 consecutive weeks)
        │
        ▼
   Activation:        User is considered "activated" — retained base
```

### Common Activation Friction Points

| Friction Type | Symptom | Fix |
|--------------|---------|-----|
| Empty state | User sees blank screen, doesn't know what to do | Add templates, sample data, guided first action |
| Long setup | User must complete 10+ steps before seeing value | Defer non-essential setup; get to value first |
| Unclear value | User doesn't understand what the product does | Improve onboarding messaging; show outcome, not features |
| Technical barrier | Integration or import required before value visible | Offer sandbox / demo mode with pre-loaded data |
| Social requirement | Value only appears with teammates, but user is alone | Add solo value mode; delay "invite team" to post-activation |
| Permission/approval | User must get IT approval before full access | Build a path that works without approval |

---

## Growth Team Structure

### The Growth Team Model

```
Option A — Centralized Growth Team:
  Head of Growth
  ├── Growth PM (owns experimentation roadmap)
  ├── Growth Engineer (full-stack, owns test infra + experiments)
  ├── Growth Analyst (data, cohorts, experiment design)
  ├── Growth Designer (landing pages, onboarding flows)
  └── Growth Marketer (channel experiments, paid)

  Best for: Early-stage companies, small overall team

Option B — Embedded Growth Function:
  Core Product Teams (own their metrics)
  + Central Growth Platform Team (owns tools, data infra, experimentation platform)
  + Growth Marketing Team (owns acquisition channels)

  Best for: Mid-stage companies with multiple product areas

Option C — Full Growth Operating Model:
  Each product squad has growth accountability (OKRs tied to growth metrics)
  Centralized Growth Platform + Analytics (shared services)
  No separate "growth team" — growth is everyone's job

  Best for: Growth-mature companies (Spotify, Airbnb model)
```

### Growth Team Reporting

```
Who should Growth report to?

  Reports to CPO:     Maximizes product influence; experiments can change core product
  Reports to CMO:     Maximizes channel/acquisition influence; may limit product changes
  Reports to CEO:     Maximizes cross-functional authority; CEO bandwidth risk

  Recommendation: Report to CPO with strong dotted line to CMO.
  Growth sits at the intersection of product and marketing — needs authority in both.
```

### Growth Team Cadence

```
Weekly:  Growth standup (experiment status, blockers, new hypotheses queued)
Weekly:  Experiment review (results of completed experiments, learnings documented)
Monthly: Growth metrics review (NSM tree, cohort analysis, channel performance)
Monthly: Experimentation backlog grooming (re-score ICE, add new hypotheses)
Quarterly: Growth strategy review (are the loops working? channel portfolio health)
```

---

## Growth Accounting

### The Four User States

```
At the end of any period, every user is in exactly one state:

  New:          Used product for the first time this period
  Retained:     Used product this period AND last period
  Resurrected:  Used product this period, did NOT use last period, but used before
  Churned:      Did NOT use product this period, but used last period

Accounting identity:
  MAU(this month) = New + Retained + Resurrected
  Users who churned are subtracted from the "would have been retained" pool
```

### Growth Accounting Dashboard

```
Month:           Jan    Feb    Mar    Apr
New:             1,200  1,400  1,600  1,800
Retained:        3,400  3,600  3,800  4,100
Resurrected:       200    250    300    350
Churned:          (800)  (900)  (950)  (980)
─────────────────────────────────────────────
MAU:             4,000  4,350  4,750  5,270
MoM Growth:        —    +8.8%  +9.2%  +11.0%

Quick ratio:     (New + Resurrected) / Churned
                  =  1,400 / 900 = 1.56 (Feb)
```

**Quick Ratio Benchmarks**:

| Quick Ratio | Health Signal |
|------------|--------------|
| < 1.0 | Shrinking; churn exceeds new growth |
| 1.0–2.0 | Growing but fragile; small churn spike could hurt |
| 2.0–4.0 | Healthy growth with adequate buffer |
| > 4.0 | Exceptional; early-stage hypergrowth or exceptional retention |

### Retention vs. Acquisition Sensitivity

```
Simulate to understand which lever matters more:

Base case: 1,000 MAU, 10% monthly churn, 100 new users/month

Scenario A — Improve acquisition 50%:
  New users: 150/month (+50 additional)
  Retained after 12 months: ~1,268 MAU

Scenario B — Improve retention 25% (10% → 7.5% churn):
  New users: 100/month (unchanged)
  Retained after 12 months: ~1,367 MAU

→ Retention improvement generated more MAU growth than 50% more acquisition.
   This math holds for most products with established user bases.
   Fix retention before investing heavily in acquisition.
```

---

## Channel / Market Fit Analysis

### Channel Fit Assessment

Not every channel works for every product. Channel fit is the alignment between your product's user behavior, unit economics, and the characteristics of a given channel.

**Channel Fit Matrix**:

| Channel | CAC Profile | Best Fit | Poor Fit |
|---------|-----------|---------|---------|
| SEO / Content | Low CAC, slow ramp | Products with long buying journeys, B2B | Impulse purchases, time-sensitive |
| Paid Search (SEM) | Medium CAC, fast | High-intent buyers, clear search terms | Novel products with no search demand |
| Paid Social | High CAC, scalable | Consumer, visual products, B2C | Complex B2B, technical buyers |
| Viral / Referral | Very low CAC, network dependent | Communication tools, social products | Solo-use, no sharing occasion |
| Product-Led / Freemium | Low CAC, requires product fit | Self-serve SaaS, developer tools | High-complexity enterprise |
| Outbound Sales | High CAC, predictable | Enterprise, high ACV | Low ACV products |
| Partnerships / BD | Variable, channel-dependent | Marketplace, platform products | Point solutions |
| Community | Very low CAC, slow | Open source, developer, niche B2B | Broad consumer |

### The Channel Portfolio Principle

```
Don't rely on a single channel. Build a diversified portfolio.

Channel portfolio health check:
  □ At least one organic channel (SEO, viral, word-of-mouth)
  □ At least one paid channel (for controllable growth when needed)
  □ No single channel > 40% of acquisition (concentration risk)
  □ At least one channel with LTV:CAC > 5:1 (your profitable core)
  □ At least one experimental channel (testing next growth vector)
```

### Channel Saturation Signals

```
Signs a channel is saturating:
  - CAC increasing faster than inflation (competing for same audience)
  - CTR declining without creative changes
  - Diminishing ROAS on incremental spend (diminishing returns curve)
  - Similar-profile users converting at lower rates over time

Response:
  1. Creative refresh (short-term)
  2. Audience expansion (medium-term)
  3. New channel investment (long-term hedge)
```

---

## Growth Model Templates

### Bottom-Up Growth Forecast

```
Step 1 — Define the growth equation for your model:

  For a PLG product:
  MAU(t) = MAU(t-1) × (1 - monthly_churn) + new_signups(t) × activation_rate

  For an e-commerce product:
  Revenue(t) = active_customers(t) × avg_order_value × purchase_frequency

  For a marketplace:
  GMV(t) = active_supply(t) × average_listing_price × conversion_rate × visits(t)

Step 2 — Identify the 3-5 input variables that drive the equation

Step 3 — Research or estimate each input variable
  (use actuals where available, benchmarks where not)

Step 4 — Build the model month by month for 12-24 months

Step 5 — Run three scenarios: Base, Bull (+30% on each input), Bear (-30% on each input)

Step 6 — Identify which input variable has the most sensitivity on the outcome
  → that's where to focus growth investment
```

### SaaS Growth Model Template

```
Inputs (monthly):
  new_signups          = [acquisition channels × conversion rates]
  activation_rate      = activated / signed_up (target: 40-60%)
  monthly_churn_rate   = churned MAU / prior MAU (target: <2% for SMB, <1% for enterprise)
  expansion_rate       = expansion MRR / prior MRR
  ARPU                 = MRR / MAU

Derived monthly outputs:
  new_activated        = new_signups × activation_rate
  churned              = MAU(t-1) × monthly_churn_rate
  MAU(t)               = MAU(t-1) - churned + new_activated + resurrected
  MRR(t)               = MAU(t) × ARPU + expansion_MRR - churn_MRR
  ARR(t)               = MRR(t) × 12

Model health checks:
  LTV                  = ARPU / monthly_churn_rate (target: >3× CAC)
  Payback period       = CAC / (ARPU × gross_margin) (target: <12 months)
  Quick ratio          = (new + resurrected) / churned (target: >2.0)
  NRR                  = (MRR_start + expansion - contraction - churn) / MRR_start × 100%
                         (target: >100%, best-in-class: >120%)
```

### Viral Growth Model

```
K-factor model:

  Users(t) = Users(t-1) × (1 - churn) + acquired_external(t) + acquired_viral(t)

  acquired_viral(t) = Users(t-1) × invite_rate × conversion_rate
                    = Users(t-1) × K-factor

  If K = 0.4 and external acquisition = 200 users/month, churn = 5%:
  Month 1:   1,000 users  → viral: 400 + external: 200 - churn: 50  = 1,550
  Month 2:   1,550 users  → viral: 620 + external: 200 - churn: 78  = 2,292
  Month 3:   2,292 users  → viral: 917 + external: 200 - churn: 115 = 3,294

  Even with K < 1, the viral multiplier significantly amplifies external acquisition.
  The goal is not K > 1; it is increasing K from 0.1 → 0.4 → 0.6 at each stage.
```

---

## Growth Experimentation Anti-Patterns

| Anti-Pattern | Description | Correct Approach |
|-------------|------------|-----------------|
| Peeking | Stopping a test early when results look good | Pre-commit to sample size and run to completion |
| HARKing | Hypothesizing after results are known | Write hypothesis before experiment |
| Multiple metrics without correction | Declaring success on any one of 10 metrics | Pre-specify primary metric; others are exploratory |
| Ignoring guardrail metrics | Activation up but retention tanks | Always define guardrails; honor them |
| Testing trivial variants | Button color changes, font size adjustments | Test structural changes; save cosmetic tests for low-traffic sites |
| No documentation | Running tests without recording learnings | Every experiment gets a write-up, win or lose |
| Insufficient sample | Calling statistical significance at n=200 | Calculate minimum sample before starting |
| Not segmenting results | Aggregate results hide segment-level effects | Always cut results by key segments (new vs. existing, mobile vs. desktop) |
