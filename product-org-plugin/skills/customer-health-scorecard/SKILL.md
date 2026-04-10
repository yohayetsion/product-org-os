---
name: customer-health-scorecard
description: "Create customer health scorecard assessing account status across engagement, adoption, and satisfaction. Activate when: \"customer health\", \"health score\", \"account health\", customer status assessment, churn risk, renewal readiness Do NOT activate for: value realization reports (/value-realization-report), customer value trace validation (/customer-value-trace), onboarding playbooks (/onboarding-playbook)"
argument-hint: "[customer name or segment] or [update path/to/scorecard.md]"
user-invocable: true
metadata:
  author: Product Org OS
  version: 3.0.0
  category: customer-success
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided (`@path/to/scorecard.md`) | UPDATE | 100% |
| "create", "new", "draft" in input | CREATE | 100% |
| "find", "search", "list scorecards" | FIND | 100% |
| "the scorecard", "[Customer] health" | UPDATE | 85% |
| Just customer name/segment | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new health scorecard using template below.

**UPDATE**:
1. Read existing scorecard (search if path not provided)
2. Preserve structure, update metrics with new data
3. Add new month to Historical Trend
4. Recalculate health scores
5. Show diff summary: "Updated scores. Previous: X/100 → Current: Y/100."

**FIND**:
1. Search paths below for health scorecards
2. Present results: customer, current score, last updated
3. Ask: "Update one of these, or create new?"

### Search Locations for Health Scorecards

- `customers/`
- `health/`
- `customer-success/`
- `accounts/`

---

Create a **Customer Health Scorecard** for the specified customer or segment.

## Vision to Value Phase
**Phase 5: Business & Customer Outcomes** - This skill tracks customer health indicators.

## Methodology

<!-- Source: Google HEART Framework — Kerry Rodden, Hilary Hutchinson, Xin Fu (2010)
     "Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications"
     Published at CHI 2010. Developed at Google to provide user-centered metrics at scale.
     Framework: 5 dimensions (Happiness, Engagement, Adoption, Retention, Task Success),
     each decomposed via Goals → Signals → Metrics (GSM process). -->

This skill uses **Google's HEART framework** as the primary measurement structure, extended with B2B account health indicators. HEART provides five user-centered dimensions, each defined through the **Goals → Signals → Metrics (GSM)** process.

### HEART Dimensions

<!-- Source: Google HEART — the 5 dimensions with GSM decomposition -->

| Dimension | What It Measures | Example Signals |
|-----------|-----------------|-----------------|
| **H**appiness | Subjective satisfaction, perceived ease of use | NPS, CSAT, SUS scores, sentiment |
| **E**ngagement | Depth and frequency of interaction | Session frequency, actions per session, DAU/MAU |
| **A**doption | New users/features gaining traction | New signups, feature adoption rate, use case expansion |
| **R**etention | Users/accounts returning over time | Churn rate, renewal rate, logo retention |
| **T**ask Success | Efficiency and effectiveness of core tasks | Task completion rate, time-on-task, error rate |

### Goals → Signals → Metrics (GSM) Process

<!-- Source: Google HEART — GSM is the process for turning dimensions into measurable metrics.
     Goals = what you want to achieve; Signals = user behaviors indicating progress;
     Metrics = quantifiable measures of those signals. -->

Before scoring, define GSM for each dimension relevant to this customer/product:

| Dimension | Goal | Signal | Metric |
|-----------|------|--------|--------|
| Happiness | [What satisfaction looks like] | [Observable user behavior] | [Quantified measure] |
| Engagement | [What good engagement looks like] | [Observable user behavior] | [Quantified measure] |
| Adoption | [What adoption success looks like] | [Observable user behavior] | [Quantified measure] |
| Retention | [What retention success looks like] | [Observable user behavior] | [Quantified measure] |
| Task Success | [What effective usage looks like] | [Observable user behavior] | [Quantified measure] |

## Output Structure

### 1. Overall Health Score
**Score: X/100** [🟢 Healthy / 🟡 At Risk / 🔴 Critical]

<!-- Source: Composite scoring structure extends Google HEART with B2B relationship layer.
     HEART covers user-level health; Relationship covers account-level health. -->

| Component | Weight | Score | Weighted Score |
|-----------|--------|-------|----------------|
| Happiness (HEART-H) | X% | X/100 | X |
| Engagement (HEART-E) | X% | X/100 | X |
| Adoption (HEART-A) | X% | X/100 | X |
| Retention (HEART-R) | X% | X/100 | X |
| Task Success (HEART-T) | X% | X/100 | X |
| Relationship (B2B) | X% | X/100 | X |
| **Total** | 100% | | X/100 |

### 2. Happiness Metrics (HEART-H)
<!-- Source: Google HEART "Happiness" dimension — subjective attitudes, satisfaction, perceived usability -->

| Metric | Current | Target | Trend | Score |
|--------|---------|--------|-------|-------|
| NPS score | X | X | ↑/↓/→ | X/100 |
| CSAT | X% | X% | ↑/↓/→ | X/100 |
| Perceived ease of use | X/10 | X/10 | ↑/↓/→ | X/100 |
| Sentiment (support/feedback) | Pos/Neu/Neg | Positive | ↑/↓/→ | X/100 |

### 3. Engagement Metrics (HEART-E)
<!-- Source: Google HEART "Engagement" dimension — depth and frequency of user interaction -->

| Metric | Current | Target | Trend | Score |
|--------|---------|--------|-------|-------|
| DAU/MAU | X% | X% | ↑/↓/→ | X/100 |
| Session frequency | X/week | X/week | ↑/↓/→ | X/100 |
| Session duration | X min | X min | ↑/↓/→ | X/100 |
| Actions per session | X | X | ↑/↓/→ | X/100 |
| Feature usage breadth | X% | X% | ↑/↓/→ | X/100 |

### 4. Adoption Metrics (HEART-A)
<!-- Source: Google HEART "Adoption" dimension — new users and new use cases gaining traction -->

| Metric | Current | Target | Trend | Score |
|--------|---------|--------|-------|-------|
| Activated users | X% | X% | ↑/↓/→ | X/100 |
| Use cases live | X/X | X/X | ↑/↓/→ | X/100 |
| Feature adoption rate | X% | X% | ↑/↓/→ | X/100 |
| Integration depth | X | X | ↑/↓/→ | X/100 |
| Admin engagement | X | X | ↑/↓/→ | X/100 |

### 5. Retention Metrics (HEART-R)
<!-- Source: Google HEART "Retention" dimension — rate at which users/accounts return over time -->

| Metric | Current | Target | Trend | Score |
|--------|---------|--------|-------|-------|
| Logo retention | X% | X% | ↑/↓/→ | X/100 |
| Net revenue retention | X% | X% | ↑/↓/→ | X/100 |
| User churn rate | X% | X% | ↑/↓/→ | X/100 |
| Renewal rate | X% | X% | ↑/↓/→ | X/100 |

### 6. Task Success Metrics (HEART-T)
<!-- Source: Google HEART "Task Success" dimension — efficiency and effectiveness of key user tasks.
     Measures whether users can accomplish what they came to do. -->

| Metric | Current | Target | Trend | Score |
|--------|---------|--------|-------|-------|
| Core task completion rate | X% | X% | ↑/↓/→ | X/100 |
| Time-on-task (key workflows) | X min | X min | ↑/↓/→ | X/100 |
| Error rate | X% | X% | ↑/↓/→ | X/100 |
| Support tickets per task | X | X | ↑/↓/→ | X/100 |

### 7. Relationship Metrics (B2B Extension)

| Metric | Current | Trend | Score |
|--------|---------|-------|-------|
| Executive sponsor engaged | Yes/No | - | X/100 |
| Champion identified | Yes/No | - | X/100 |
| QBR participation | X% | ↑/↓/→ | X/100 |
| Escalation frequency | X/quarter | ↑/↓/→ | X/100 |

### 8. Expansion Signals

| Signal | Status | Implication |
|--------|--------|-------------|
| Approaching usage limits | 🟢/🟡/🔴 | [Opportunity/Risk] |
| New use case interest | 🟢/🟡/🔴 | [Opportunity/Risk] |
| Team growth | 🟢/🟡/🔴 | [Opportunity/Risk] |
| Contract renewal approaching | 🟢/🟡/🔴 | [Opportunity/Risk] |

### 9. Churn Risk Indicators

| Indicator | Status | Impact | Action |
|-----------|--------|--------|--------|
| Usage decline (HEART-E drop) | 🟢/🟡/🔴 | High/Med/Low | [Action] |
| Champion departure | 🟢/🟡/🔴 | High/Med/Low | [Action] |
| Task success degradation (HEART-T drop) | 🟢/🟡/🔴 | High/Med/Low | [Action] |
| Happiness decline (HEART-H drop) | 🟢/🟡/🔴 | High/Med/Low | [Action] |
| Competitive evaluation | 🟢/🟡/🔴 | High/Med/Low | [Action] |

### 10. Action Recommendations

**Immediate (This Week):**
| Action | HEART Dimension | Owner | Due Date |
|--------|----------------|-------|----------|
| [Action] | [H/E/A/R/T] | [Owner] | [Date] |

**This Month:**
| Action | HEART Dimension | Owner | Due Date |
|--------|----------------|-------|----------|
| [Action] | [H/E/A/R/T] | [Owner] | [Date] |

### 11. Historical Trend

| Month | Health Score | HEART Breakdown (H/E/A/R/T) | Key Events |
|-------|-------------|------------------------------|------------|
| [Month -3] | X/100 | X/X/X/X/X | [Events] |
| [Month -2] | X/100 | X/X/X/X/X | [Events] |
| [Month -1] | X/100 | X/X/X/X/X | [Events] |
| Current | X/100 | X/X/X/X/X | [Events] |

## Instructions

1. **Start with GSM** — define Goals, Signals, Metrics for each HEART dimension before scoring
<!-- Source: Google HEART GSM process — don't jump to metrics without defining what success looks like -->
2. Ask about specific customer if not specified
3. Reference any customer data provided via @file syntax
4. Not all HEART dimensions apply equally — weight by product type:
<!-- Source: Google HEART guidance — "not every dimension is equally important for every product" -->
   - **B2C high-frequency**: Weight Engagement + Retention highest
   - **B2B enterprise**: Weight Task Success + Happiness + Relationship highest
   - **Growth-stage**: Weight Adoption + Engagement highest
5. Include both leading indicators (Engagement, Task Success) and lagging indicators (Retention, Happiness)
6. Provide specific, actionable recommendations tied to HEART dimensions
7. Save as markdown file
8. Offer to create presentation version using /present
