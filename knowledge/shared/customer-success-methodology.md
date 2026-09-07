---
pack: customer-success-methodology
consumers:
- cs-dir
- csm
- cs-ops
- support-lead
- onboarding-csm
- account-exec
- value-realization
---
# Customer Success Methodology Knowledge Pack

**Version**: 1.1 (refreshed 2026-05-18)
**Type**: knowledge-pack
**Primary Users**: `cs-dir`, `csm`, `cs-ops`
**Secondary Users**: `value-realization`, `bizops`

**Sources consulted**:
  - TSIA Value Score framework (publicly documented 2026) — value-realization quantification, customer-stated outcome verbatim, value-retention vs. seat-retention
  - Gainsight Pulse library (public resources) — health scoring, QBR templates, success plan frameworks
  - Lincoln Murphy / Sixteen Ventures — customer success methodology and churn analysis
  - Customer Success Association + Pulse 2026 content — NPS retirement industry consensus, CSAT-by-job-to-be-done framing
  - 2026 H1 landscape signals — NPS retirement (TSIA + Gainsight 2026 industry shift), per-seat pricing structural failure (cross-ref `pricing-frameworks.md`), Resolution Durability replacing ticket deflection (cross-ref `ai-agent-supervisor.md`)
  - chatwoot/chatwoot (github.com/chatwoot/chatwoot) — conversation routing and automation patterns

**Source licence**: TSIA and industry sources are per-source-terms; Chatwoot: MIT.

**V2V refinements**:
- Surgical 2026 H1 update preserving Health Score scaffolding as transitional context while pointing forward to `value-score-design.md` as the operational target
- Added "2026 Landscape Notes" appendix integrating four parallel structural shifts (Health → Value, NPS retirement, per-seat collapse, Resolution Durability) into a single CS methodology view rather than four disconnected pivots
- Cross-references made explicit to sibling packs (`value-score-design.md`, `ai-agent-supervisor.md`, `pricing-frameworks.md`, `metrics-frameworks.md`) so the CS methodology stays internally consistent with the wider Q2-2026 H1 refresh
- Inline framing notes flag the affected sections (Health Score Calculation, CS Metrics benchmarks, Support Ticket Deflection, NRR section) so a reader spotting an outdated convention is immediately steered to the 2026 view

---

## Refreshed 2026-05-18

This pack was authored before 2026 H1. Q2 2026 H1 developments integrated:

- **Health Score → Value Score transition** — sibling pack Q2-4.1 `value-score-design.md` is the operational target; this pack retains Health Score as transitional/historical context with explicit "moving to Value Score" guidance
- **NPS retirement** — added 2026 framing on NPS limits; CSAT-by-job-to-be-done + explicit value verbatim as replacement signal
- **Per-seat pricing structural failure** — cross-ref `pricing-frameworks.md` §[2026 per-seat structural failure] + `metrics-frameworks.md` §9; CS methodology adapts to value-not-seat-retention metric framing
- **Resolution Durability** — cross-ref Q2-4.2 `ai-agent-supervisor.md` as the AI-support KPI replacing ticket deflection

**Sections updated** (surgical): Customer Health Scoring Framework (added transition note), CS Metrics — Definitions and Benchmarks (NPS, Support Ticket Deflection, NRR), Net Revenue Retention (added value-retention reframing), bottom appendix "2026 Landscape Notes" (new).

**Sections preserved**: Multi-Dimensional Health Model dimensions and weights, Health Score Validation discipline, Customer Segmentation Models (Value-Complexity Matrix), Success Plan Framework, QBR Framework, Churn Analysis Framework, Expansion Revenue Framework, Customer Lifecycle Stages, Playbook Library. The methodology backbone holds; the metric layer is what needed refreshing.

---

## Customer Health Scoring Framework

> **2026 transition note** [Owner: 💎]: Health Score remains widely used and is preserved here as an intermediate, operationally familiar metric. The forward direction across the industry (TSIA, Gainsight, Customer Success Association, 2026) is **Value Score** — anchored on customer-stated outcomes and the quantified value the customer attributes to the product, not on internal-signal composites. CS orgs running a Health Score today should treat it as a transitional artifact on the path to Value Score. See sibling pack `value-score-design.md` for the operational pattern, scoring model, and rollout playbook. The dimensions below remain useful as **inputs** to a Value Score (especially Product Usage and Business Outcomes), but Health Score as a standalone primary KPI is becoming legacy.

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

> **2026 reframing — value-retention, not seat-retention** [Owner: 🌟]: NRR as defined above mixes a structurally compromised input (seat-addition expansion under per-seat pricing) with a structurally honest one (value-tier upgrade, usage-tier expansion). With AI agents collapsing per-seat economics — fewer human seats producing the same or higher work output — seat-add expansion is increasingly an artifact of how the contract is priced, not a signal of value realized. The 2026 CS adaptation: track **NRR-value** (expansion driven by value-tier moves, usage-tier moves, outcome-attached pricing components) separately from **NRR-seat** (expansion driven purely by seat count). When NRR-seat is the dominant driver and NRR-value is flat, the customer is fragile even if headline NRR looks healthy. Cross-ref `pricing-frameworks.md` §[2026 per-seat structural failure] and `metrics-frameworks.md` §9 (Value-Retention vs. Seat-Retention).

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

## Agentic-CS Operating Layer (2026)

**Added 2026-06-24.**

**Sources consulted**:
  - Gainsight "Agentic AI and Customer Success" + Atlas AI / Renewal AI Agent + Staircase AI (gainsight.com/blog/agentic-ai-and-customer-success-redefining-the-journey, Pulse 2025→2026 content) — autonomous renewal + proactive-risk agents for long-tail segments
  - Lincoln Murphy / Sixteen Ventures, "Talking About Agentic AI Is the Most Customer Success Thing I've Done" (sixteenventures.com/agentic-cs-is-customer-success, 2026) — agentic CS framed as CS itself, not a new function
  - EverAfter, "The Ultimate Guide to Digital Customer Success in 2026" (everafter.ai) — shift from relationship management to outcome architecture; agents acting on customer signals in real time

**Source licence**: per-source-terms (public industry documentation)

**V2V refinements**: the human-ownership guardrail below + the routing-back-to-human trigger tied to this pack's existing Resolution Durability / value-attribution signals.

The 2024-2025 "Digital CSM" (automated cadences + dashboards) is evolving in 2026 into an **agentic operating layer**: autonomous agents that *act* on customer signals, not just surface them. The dominant 2026 pattern is to deploy agents where named-human coverage was never economically feasible — the long-tail / low-touch segments from the Value-Complexity Matrix above (Digital-Led, Managed-Touch).

| Agent type | What it does | Where it fits | Existing playbook it scales |
|---|---|---|---|
| **Renewal agent** | Hyper-personalized renewal outreach + renewal-motion orchestration in long-tail segments | SMB / Digital-Led, Managed-Touch | Renewal Preparation, Re-engagement |
| **Proactive-health / risk agent** | Scans emails, meetings, tickets, Slack for risk + opportunity signals; surfaces (and can act on) them before escalation | All segments as a signal layer; autonomous action gated to low-touch | At-Risk Intervention, Re-engagement |
| **In-app / adoption agent** | In-product guidance, adoption nudges, community moderation, self-service learning | Digital-Led at scale | New Customer Welcome, Advocacy Activation |

> **V2V caveat — human owns the relationship and every renewal commitment** [Owner: 🌟]: an autonomous renewal/health agent is a **force multiplier on a CSM's playbook, not a substitute for the CSM's accountability**. CS is a trust domain. The agent may draft outreach, orchestrate a low-touch renewal flow, and surface risk in real time — but a **named human owns the customer relationship and signs off on every renewal *commitment*** (price, term, concession, save offer). Autonomous *action* (as opposed to drafting) is acceptable only in low-touch segments and only while the quality signals hold. **Routing-back-to-human trigger**: if **Resolution Durability** (see CS Metrics + `ai-agent-supervisor.md`) or **value-attribution** drops below threshold for a customer or segment, route that segment's agent traffic to human-supervised mode until the underlying cause is identified. A confident-wrong agent in a renewal conversation costs a logo, not a re-opened ticket — the durability discipline that governs AI support applies with *more* force to AI renewal/relationship work. Cross-ref `ai-agent-supervisor.md` (Q2-4.2) for the supervision framework and `value-score-design.md` (Q2-4.1) for the value signal the agent must not degrade.

---

## CS Metrics — Definitions and Benchmarks

| Metric | Definition | SaaS Benchmark | Measurement | 2026 Status |
|--------|-----------|----------------|-------------|-------------|
| **Gross Revenue Retention** | Revenue retained excluding expansion | 85-95% | Monthly/Quarterly | Active |
| **Net Revenue Retention** | Revenue retained including expansion | 100-130% | Monthly/Quarterly | Active — split into NRR-value vs. NRR-seat (see NRR section above) |
| **Logo Retention** | Customer count retained | 85-95% | Monthly/Quarterly | Active |
| **Time-to-First-Value** | Days from contract to first meaningful outcome | [Varies by product] | Per customer | Active — aligns with Value Score |
| **Value Score** | Composite of customer-stated outcome attainment + quantified value | [TBD by org] | Quarterly | **Primary 2026 forward metric** — see `value-score-design.md` |
| **NPS** | Net Promoter Score | 30-50 (B2B SaaS) | Quarterly/Semi-annual | **Demoted 2026** — see CSAT-by-JTBD note below |
| **CSAT by Job-To-Be-Done** | Per-JTBD satisfaction + verbatim "what value did you get" | [TBD per JTBD] | Per JTBD touchpoint | **New 2026 primary** signal replacing NPS |
| **CSAT** | Customer Satisfaction (per interaction) | 85-95% | Per interaction | Active — interaction-level only |
| **Health Score Distribution** | % of customers in each health tier | 60%+ green | Monthly | **Transitional** — moving to Value Score (see Health Score section) |
| **CSM Capacity** | Accounts per CSM by segment | See segmentation table | Monthly | Active |
| **Expansion Rate** | % of customers that expand annually | 20-40% | Annually | Active — but classify expansion by value vs. seat (see NRR section) |
| **Resolution Durability** | % of AI-agent resolutions that stay resolved (no re-open within N days) | [Varies; 70-85% emerging benchmark] | Monthly | **Primary 2026 AI-support KPI** — see `ai-agent-supervisor.md` |
| **Support Ticket Deflection** | % of issues resolved by self-service | 30-50% | Monthly | **Demoted 2026** — Resolution Durability replaces it as the headline AI-era KPI; deflection rate without durability hides re-opens |

### 2026 framing notes on the demoted metrics

**NPS — why demoted, not retired** [Owner: 💎]: The industry consensus through 2026 H1 (TSIA, Gainsight Pulse content, Customer Success Association) is that NPS as the *primary* CS measurement signal has structural problems: a single-question stand-in for value masks **which job** the customer is satisfied with, NPS scores plateau before churn signals appear, and "would you recommend" no longer correlates strongly with renewal decisions in AI-era B2B SaaS. The replacement pattern: **CSAT by job-to-be-done** (ask the satisfaction question per critical workflow) + **explicit value verbatim** (ask the customer to state, in their own words, what value they got — captured as structured data feeding Value Score). NPS retains two legitimate residual uses: (1) longitudinal benchmarking against the years of NPS data the org already has, and (2) reference-readiness signal (a 9-10 NPS customer is still a useful advocacy candidate). Stop treating NPS as a headline KPI; keep it as a historical trendline and a screening signal for the advocacy playbook.

**Support Ticket Deflection — why demoted** [Owner: 🌟]: Deflection counts an AI agent (or KB article) "resolving" a ticket as a win without checking whether the customer comes back for the same issue. In an AI-support era where re-open rates inflate easily — confident-sounding wrong answers, edge-case failures the model masks behind fluency — deflection-only measurement creates the illusion of efficiency while customer experience degrades. **Resolution Durability** (per `ai-agent-supervisor.md`) measures whether the resolution actually held: did the customer re-open within N days, did the same root cause re-emerge in a related ticket, did a human have to clean up? Track both — deflection as the rate metric, durability as the quality metric — and prioritize durability when they diverge.

---

## 2026 Landscape Notes (Appendix)

Four parallel structural shifts hit CS methodology in 2026 H1. Each is covered above in-line; this appendix is the consolidated view for quickly orienting a CS leader to the changed terrain.

### 1. Health Score → Value Score

**The shift**: From internal-signal composite (usage + engagement + support + sentiment + relationship) to customer-stated outcome attainment + quantified value. Health Score asks "how is this account?"; Value Score asks "is this customer getting the value they paid for, as they define it?"

**Why now**: AI-era buyer scrutiny — CFOs and procurement teams want value claims they can audit, not vendor-asserted health badges. TSIA's Value Score framework gave the industry a shared vocabulary; Gainsight and Pulse content followed.

**Operational pattern**: See `value-score-design.md` for the scoring model, customer-stated outcome capture, and the rollout playbook (Health Score → Hybrid → Value Score over ~2-3 quarters).

**Don't delete Health Score yet**: many CS orgs still operate on it, many CS platforms are instrumented for it, and Health Score signals remain valid **inputs** to Value Score (Product Usage dimension feeds Value Score's outcome-attainment input; Business Outcomes dimension feeds the value-quantification input).

### 2. NPS Retirement (Partial)

**The shift**: NPS demoted from primary CS measurement to historical benchmark + advocacy screen. Replacement primary signals: **CSAT by job-to-be-done** + **explicit value verbatim**.

**Why now**: NPS plateaus before churn signals appear; AI-era B2B buyers don't make recommendation decisions on a 0-10 scale; "would you recommend" doesn't disaggregate which workflow worked vs. which didn't.

**Operational pattern**: Replace the quarterly NPS survey with per-JTBD CSAT pulses tied to actual customer workflows. At QBR, capture explicit value verbatim ("In your words, what value did our product deliver this quarter?") and feed it into Value Score.

**Honest caveat**: NPS isn't truly dead — it's a long-running longitudinal series many orgs can't and shouldn't abandon, and a 9-10 NPS score is still a defensible advocacy signal. The retirement is from "primary KPI" status, not from existence.

### 3. Per-Seat Pricing Structural Failure

**The shift**: Per-seat pricing is breaking down structurally in 2026 as AI agents enable fewer human seats to produce the same or greater work output. The CS implication: **expansion-by-seat-count is no longer a reliable value signal**. A customer renewing flat or downsizing on seats may be getting *more* value than last year if they've replaced seats with AI-driven workflows.

**Why now**: Cross-ref `pricing-frameworks.md` §[2026 per-seat structural failure] for the pricing analysis; `metrics-frameworks.md` §9 for the metric-layer adaptation.

**CS methodology adaptation**:
- Split NRR into **NRR-value** (value-tier moves, usage-tier moves, outcome-attached pricing) and **NRR-seat** (seat count changes). See NRR section above.
- Replace "seat retention" anywhere it appears in CS dashboards with "value retention" + a seat-count companion metric.
- Re-segment risk: a customer downsizing seats while *increasing* usage-tier or value-tier consumption is **not** an at-risk account; the old playbook would have flagged them red.
- Renewal forecasting: stop using seat-count trajectory as a leading indicator; use Value Score + value-tier trajectory.

### 4. Resolution Durability Replaces Ticket Deflection

**The shift**: Ticket deflection — % of tickets resolved without human touch — was the AI-support headline metric through 2024-2025. In 2026, **Resolution Durability** (% of resolutions that stay resolved, no re-open within N days, no root-cause re-emergence in related tickets) becomes the durable quality signal.

**Why now**: Cross-ref `ai-agent-supervisor.md` (Q2-4.2 sibling) for the AI-agent supervision framework. Confident-wrong AI resolutions inflate deflection while degrading actual customer experience; orgs measuring only deflection didn't see the underlying erosion until customer-effort scores and CSAT-by-JTBD started reflecting it.

**CS methodology adaptation**:
- Track both deflection (rate) and durability (quality). Prioritize durability when they diverge.
- AI-support escalation rules: if Resolution Durability drops below threshold for a customer or segment, route AI-agent traffic for that segment to human-supervised mode until the underlying issue is identified.
- Feed durability data into Health Score / Value Score: a customer with high deflection but low durability is at risk even if their dashboard looks green.
- QBR section "Support Review" should now include: ticket volume, durability, durability-trend, and any segments where AI-agent traffic is currently routed to human-supervised mode.

### Cross-Reference Map

**Q2-4 siblings (CS-specific methodology stack)**:
| When CS work involves... | Read also |
|---|---|
| Health scoring / scoring redesign / Value Score rollout | `value-score-design.md` (Q2-4.1) |
| AI-support quality, ticket flow, AI agent KPIs | `ai-agent-supervisor.md` (Q2-4.2) |
| Renewal forecasting, expansion classification, NRR breakdown | `pricing-frameworks.md` §[per-seat], `metrics-frameworks.md` §9 |
| Quarterly customer business review, value evidence | `value-score-design.md` + this pack (QBR Framework section) |
| Churn analysis with 2026 framing | This pack (Churn Analysis Framework) + `value-score-design.md` (value-attribution post-mortem) |

**Q2-6 siblings (marketing-CS adjacency)**:
| When CS work involves... | Read also |
|---|---|
| Renewal saves / win-back coordination / payment recovery | `retention-marketing.md` (Q2-6.2) — retention-marketing complements CS-retention; the value-vs-seat retention framing here mirrors that pack's §2026 Per-Seat Structural Failure |
| Customer-research signals from search demand | `llm-seo.md` (Q2-6.3) — branded-search demand from disengaged customers is a re-engagement readiness signal |
| Channel-mix tradeoffs between paid acquisition and retention | `mmm-modeling.md` (Q2-6.1) |

**Q2-7 siblings (sales-CS adjacency)**:
| When CS work involves... | Read also |
|---|---|
| Transactional customer-facing email reputation | `deliverability-engineering.md` (Q2-7.1) — main-domain isolation protects CS communication paths |
| Renewal RFP responses, customer-references in proposals | `ai-native-rfp.md` (Q2-7.2) |

**Q2-3 siblings (sensitive scaffolding when CS consumes AI scoring)**:
| When CS work involves... | Read also |
|---|---|
| Customer-AI-decision exposure (Value Score, AI-driven renewal) | `eu-ai-act-annex-iv.md` (Q2-3.4) + `csa-ai-controls-matrix.md` (Q2-3.3) |
| AI inventory for customer-facing AI systems | `ai-bom.md` (Q2-3.5) |

**Q2-5 siblings (technical-architecture for AI support deployments)**:
| When CS work involves... | Read also |
|---|---|
| AI support agent security / threat model | `agentic-security.md` (Q2-5.3) |
| MCP-mediated customer-context tooling | `mcp-architecture.md` (Q2-5.1) + `mcp-governance.md` (Q2-3.2) |

---

*Last Updated: 2026-05-18 (refresh) — original 2026-03-29*
*References: TSIA Value Score framework (2026), Gainsight Pulse library, Lincoln Murphy / Sixteen Ventures, Customer Success Association + Pulse 2026 content, chatwoot/chatwoot patterns*
