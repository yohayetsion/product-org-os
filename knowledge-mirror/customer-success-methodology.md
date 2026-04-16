# Customer Success Methodology Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: @cs-dir, @csm, @cs-ops
**Secondary Users**: @value-realization, @bizops

<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - Gainsight Pulse library (public resources) — customer health scoring, QBR templates, success plan frameworks
  - Lincoln Murphy / Sixteen Ventures — customer success methodology and churn analysis
  - chatwoot/chatwoot (github.com/chatwoot/chatwoot) — conversation routing and automation patterns
  Adapted and expanded for Product Org OS agents.
-->

---

## Customer Health Scoring Framework

### Multi-Dimensional Health Model

A single metric cannot capture customer health. Use a composite score across these dimensions:

| Dimension | Weight (Typical) | Signals | Measurement |
|-----------|-----------------|---------|-------------|
| **Product Usage** | 25-30% | DAU/WAU/MAU, feature adoption, usage depth | Platform analytics |
| **Engagement** | 20-25% | Meeting attendance, response times, champion access | CRM/CS platform |
| **Support Sentiment** | 15-20% | Ticket volume trend, CSAT, escalation frequency | Help desk data |
| **Business Outcomes** | 20-25% | KPI achievement, ROI realization, goal progress | Success plan tracking |
| **Relationship Breadth** | 10-15% | Stakeholder count, executive sponsor access, multi-department usage | Relationship mapping |

### Health Score Calculation

```
Health Score = Σ (Dimension Score × Weight)

Each dimension: 0-100 scale
  0-30:   Red (At Risk)
  31-60:  Yellow (Needs Attention)
  61-80:  Green (Healthy)
  81-100: Champion (Advocate-ready)
```

### Health Score Validation

Health scores must be validated against actual outcomes:

| Validation Method | Frequency | Action |
|-------------------|-----------|--------|
| **Score vs. Renewal Outcome** | Quarterly | Correlate scores at T-90 days with renewal result |
| **Churn Autopsy** | Per event | Was health score accurate? If not, adjust weights |
| **False Green Audit** | Quarterly | Review churned accounts that were scored green |
| **False Red Audit** | Quarterly | Review renewed accounts that were scored red |

### Usage Scoring Rubric

| Level | Description | Score | Signals |
|-------|-------------|-------|---------|
| **Deep** | Power users across features | 90-100 | Multiple features daily, integrations active, workflows built |
| **Healthy** | Regular use of core features | 70-89 | Core features weekly, some advanced usage |
| **Light** | Inconsistent or shallow usage | 40-69 | Sporadic logins, only basic features |
| **At Risk** | Declining or minimal usage | 10-39 | Usage trending down, few active users |
| **Dormant** | No meaningful usage | 0-9 | No logins in 30+ days |

---

## Customer Segmentation Models

### Value-Complexity Matrix

| | Low Complexity | High Complexity |
|---|---|---|
| **High Value** | **Tech-Touch Premium**: Self-service with CSM oversight, automated health monitoring, quarterly business reviews | **High-Touch Strategic**: Named CSM, monthly check-ins, executive sponsor, custom success plans |
| **Low Value** | **Digital-Led**: Fully automated onboarding, community support, annual check-in | **Managed-Touch**: Pooled CSM model, playbook-driven engagement, as-needed support |

### Engagement Model by Segment

| Segment | CSM Ratio | Touchpoint Cadence | QBR Frequency | Escalation Path |
|---------|-----------|-------------------|---------------|-----------------|
| **Strategic** | 1:5-15 | Weekly/Bi-weekly | Quarterly | CSM → CS Dir → VP |
| **Enterprise** | 1:15-30 | Bi-weekly/Monthly | Quarterly | CSM → CS Dir |
| **Mid-Market** | 1:30-50 | Monthly | Semi-annual | Pooled CSM → CS Dir |
| **SMB** | 1:100+ | Quarterly/Digital | Annual | Digital + escalation queue |

### Segmentation Criteria

| Factor | How to Measure | Segmentation Impact |
|--------|---------------|---------------------|
| **ARR** | Contract value | Primary tier driver |
| **Strategic Value** | Logo value, reference potential, market influence | May upgrade tier |
| **Expansion Potential** | Whitespace analysis, usage vs. entitlement | Justifies higher touch |
| **Product Complexity** | Features used, integrations, customization | Drives implementation needs |
| **Risk Profile** | Industry, company size, competitive exposure | Adjusts engagement intensity |

---

## Success Plan Framework

### Success Plan Structure

```
## Customer Success Plan

**Customer**: [Name]
**CSM**: [Name]
**Start Date**: [Date]
**Review Cadence**: [Monthly/Quarterly]

### Customer Goals (Co-Created)
| # | Goal | Success Metric | Target | Timeline | Status |
|---|------|---------------|--------|----------|--------|
| 1 | [Goal] | [Metric] | [Target] | [Date] | [On track/At risk/Achieved] |

### Stakeholder Map
| Name | Title | Role | Engagement Level | Last Contact |
|------|-------|------|-----------------|-------------|

### Adoption Milestones
| Milestone | Target Date | Actual Date | Status |
|-----------|------------|-------------|--------|

### Risk Register
| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|-----------|-------|

### Expansion Opportunities
| Opportunity | Value | Timing | Readiness | Next Step |
|------------|-------|--------|-----------|-----------|

### Action Items
| Item | Owner | Due | Status |
|------|-------|-----|--------|
```

---

## QBR Framework

### QBR Structure (60 Minutes)

| Section | Duration | Content | Owner |
|---------|----------|---------|-------|
| **Business Review** | 15 min | Customer goals, progress, ROI metrics | CSM |
| **Product Adoption** | 10 min | Usage data, feature adoption, benchmarks | CSM |
| **Support Review** | 5 min | Ticket summary, resolution times, trends | CSM |
| **Roadmap Preview** | 10 min | Relevant upcoming features, beta opportunities | CSM + PM |
| **Strategic Discussion** | 15 min | Priorities, challenges, partnership growth | Customer + CSM |
| **Action Items** | 5 min | Next steps, owners, deadlines | CSM |

### QBR Preparation Checklist

- [ ] Pull usage analytics for the quarter
- [ ] Calculate ROI metrics tied to customer goals
- [ ] Review support ticket history and trends
- [ ] Check health score components and trends
- [ ] Identify expansion opportunities
- [ ] Draft 2-3 recommendations with supporting data
- [ ] Prepare relevant roadmap items
- [ ] Share pre-read with customer 3 days before

### QBR Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|--------------|-------------|-----------------|
| Product demo as QBR | Not strategic, wastes executive time | Focus on business outcomes, not features |
| CSM monologue | Customer disengages | 50/50 talk ratio, ask open-ended questions |
| No data | Vague claims, no credibility | Every assertion backed by a metric |
| No action items | Meeting without outcomes | Close with 3-5 specific, owned, dated actions |
| Skip when things are good | Misses expansion and relationship deepening | Good accounts deserve investment too |

---

## Churn Analysis Framework

### Churn Classification

| Type | Definition | Prevention Window |
|------|-----------|------------------|
| **Avoidable - Product** | Left due to missing features or bugs | 6+ months before renewal |
| **Avoidable - Service** | Left due to poor support or CS engagement | 3+ months before renewal |
| **Avoidable - Value** | Left because they couldn't prove ROI | Entire lifecycle |
| **Unavoidable - Business** | Company acquired, went bankrupt, changed strategy | Limited |
| **Unavoidable - Budget** | Genuine budget cut, not value-based | Limited (can offer downsell) |
| **Competitive** | Switched to competitor | 6+ months before renewal |

### Churn Autopsy Template

```
## Churn Autopsy

**Customer**: [Name]
**ARR Lost**: [Amount]
**Churn Date**: [Date]
**Classification**: [Type from above]
**CSM**: [Name]

### Timeline
- [Date]: First warning signal
- [Date]: Escalation point
- [Date]: Intervention attempted
- [Date]: Churn confirmed

### Root Cause
[Deep analysis — not "they didn't see value" but WHY they didn't see value]

### Warning Signals We Missed
- [Signal 1]
- [Signal 2]

### What We Could Have Done Differently
- [Action 1]
- [Action 2]

### Systemic Recommendations
- [Process change]
- [Tooling need]
- [Product feedback]
```

---

## Expansion Revenue Framework

### Expansion Motion Types

| Motion | Trigger | CSM Action | Timing |
|--------|---------|-----------|--------|
| **Upsell** | Current plan limits reached | Show usage vs. entitlement, ROI case | After value proven |
| **Cross-sell** | Adjacent use case identified | Connect to new stakeholders, run pilot | After primary use case succeeds |
| **User expansion** | New teams/departments interested | Facilitate internal advocacy, shared demo | When champion is strong |
| **Tier upgrade** | Feature needs exceed current tier | Map needs to premium features, business case | Aligned with renewal |

### Expansion Readiness Checklist

- [ ] Customer has realized measurable value from current product
- [ ] Health score is green (61+)
- [ ] Executive sponsor is engaged and accessible
- [ ] Internal champion is willing to advocate
- [ ] Business case for expansion is clear and data-backed
- [ ] Timing aligns with customer budget cycle
- [ ] No open critical support issues

---

## Net Revenue Retention (NRR) Calculation

```
NRR = (Starting MRR + Expansion - Contraction - Churn) / Starting MRR × 100

Components:
- Starting MRR: Revenue at period start
- Expansion: Upsells, cross-sells, seat additions
- Contraction: Downgrades, seat removals
- Churn: Full cancellations

Benchmarks:
- Below 100%: Losing ground — churn exceeds expansion
- 100-110%: Healthy — growth covers losses
- 110-130%: Strong — expansion-driven growth
- 130%+: Exceptional — significant expansion engine
```

---

## Customer Lifecycle Stages

| Stage | Duration | Key Activities | Exit Criteria |
|-------|----------|---------------|---------------|
| **Onboarding** | 0-90 days | Implementation, training, first value | User adoption targets met |
| **Adoption** | 90-180 days | Feature expansion, workflow integration | Core use case embedded |
| **Value Realization** | 180-365 days | ROI measurement, goal tracking | Measurable outcomes achieved |
| **Growth** | Ongoing | Expansion, advocacy, strategic partnership | Account expanding or at steady state |
| **Renewal** | T-90 to T-0 | Renewal preparation, negotiation, recommit | Contract renewed |

---

## Playbook Library — Standard CS Playbooks

| Playbook | Trigger | Key Steps | Owner |
|----------|---------|-----------|-------|
| **New Customer Welcome** | Contract signed | Welcome email → Kickoff scheduling → Stakeholder mapping | Onboarding CSM |
| **At-Risk Intervention** | Health score drops below 40 | Root cause analysis → Intervention plan → Executive escalation | CSM + CS Dir |
| **Renewal Preparation** | T-90 days to renewal | Usage review → ROI calculation → Stakeholder alignment | CSM |
| **Executive Sponsor Change** | Champion leaves or changes role | New sponsor identification → Relationship building → Re-anchor success plan | CSM |
| **Product Incident Response** | P1 incident affecting customer | Proactive notification → Status updates → Post-incident review | Support Lead + CSM |
| **Expansion Opportunity** | Expansion readiness criteria met | Business case creation → Stakeholder mapping → Proposal | CSM |
| **Re-engagement** | Customer goes silent (30+ days no contact) | Multi-channel outreach → Value reminder → Executive escalation | CSM |
| **Advocacy Activation** | Health 80+, NPS 9-10 | Reference request → Case study facilitation → Community invitation | CSM + PMM |

---

## CS Metrics — Definitions and Benchmarks

| Metric | Definition | SaaS Benchmark | Measurement |
|--------|-----------|----------------|-------------|
| **Gross Revenue Retention** | Revenue retained excluding expansion | 85-95% | Monthly/Quarterly |
| **Net Revenue Retention** | Revenue retained including expansion | 100-130% | Monthly/Quarterly |
| **Logo Retention** | Customer count retained | 85-95% | Monthly/Quarterly |
| **Time-to-First-Value** | Days from contract to first meaningful outcome | [Varies by product] | Per customer |
| **NPS** | Net Promoter Score | 30-50 (B2B SaaS) | Quarterly/Semi-annual |
| **CSAT** | Customer Satisfaction (per interaction) | 85-95% | Per interaction |
| **Health Score Distribution** | % of customers in each health tier | 60%+ green | Monthly |
| **CSM Capacity** | Accounts per CSM by segment | See segmentation table | Monthly |
| **Expansion Rate** | % of customers that expand annually | 20-40% | Annually |
| **Support Ticket Deflection** | % of issues resolved by self-service | 30-50% | Monthly |

---

*Last Updated: 2026-03-29*
*References: Gainsight Pulse library, Lincoln Murphy / Sixteen Ventures, chatwoot/chatwoot patterns*
