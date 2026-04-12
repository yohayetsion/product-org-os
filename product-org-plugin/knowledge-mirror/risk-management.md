# Enterprise Risk Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: @risk-manager, @coo, @operations-dir

---

## COSO ERM Framework (2017)

### Five Components

| Component | Focus | Key Activities |
|-----------|-------|---------------|
| **Governance & Culture** | Board oversight, operating structure, values | Define risk appetite, establish culture, attract/develop talent |
| **Strategy & Objective-Setting** | Business context, risk appetite, strategy | Analyze business context, define risk appetite, evaluate strategy |
| **Performance** | Risk identification, assessment, prioritization, response | Identify risk, assess severity, prioritize risks, implement responses |
| **Review & Revision** | Monitoring substantial change, reviewing risk and performance | Assess change, review risk, pursue improvement |
| **Information, Communication & Reporting** | Leverage information systems, communicate risk | Use relevant information, communicate risk, report on risk/culture/performance |

### Risk Appetite Framework

| Level | Description | Example |
|-------|-------------|---------|
| **Risk Averse** | Avoid risk where possible | Regulated financial institution |
| **Risk Cautious** | Prefer safe options, minimal risk | Government agency |
| **Risk Aware** | Take calculated risks with mitigation | Most commercial organizations |
| **Risk Seeking** | Actively pursue risk for return | Venture capital, startups |

### Risk Appetite Statement Template

```
[Organization] seeks to [achieve strategic objective] while maintaining
risk exposure within the following boundaries:

Strategic Risk: [willing to pursue market expansion with up to X% failure rate]
Financial Risk: [will not exceed Y% of reserves in any single initiative]
Operational Risk: [will maintain [Z]% uptime for critical systems]
Compliance Risk: [zero tolerance for regulatory violations]
Reputation Risk: [will not pursue activities that risk brand integrity]

Risk appetite is reviewed [quarterly/annually] by the [Board/Risk Committee].
```

---

## ISO 31000 Risk Management

### Risk Management Process

```
1. Scope, Context, Criteria
   → Define scope of risk management
   → Understand internal/external context
   → Define risk criteria (likelihood, impact scales)

2. Risk Assessment
   a. Risk Identification
      → What can happen? How? Why?
      → Sources: PESTLE, SWOT, brainstorming, checklists, historical data

   b. Risk Analysis
      → Determine likelihood and consequences
      → Consider existing controls
      → Determine level of risk

   c. Risk Evaluation
      → Compare against criteria
      → Prioritize for treatment
      → Determine if risk is acceptable

3. Risk Treatment
   → Select treatment option(s)
   → Design treatment plan
   → Implement treatments
   → Assess residual risk

4. Monitoring & Review
   → Track risk changes
   → Evaluate treatment effectiveness
   → Update risk register

5. Communication & Consultation
   → Engage stakeholders throughout
   → Report risk status regularly
```

### Risk Treatment Options

| Option | Description | When to Use |
|--------|-------------|-------------|
| **Avoid** | Eliminate the risk by not doing the activity | Risk exceeds appetite, no mitigation possible |
| **Mitigate** | Reduce likelihood or impact | Most common approach for medium-high risks |
| **Transfer** | Share risk with third party | Insurance, outsourcing, contractual allocation |
| **Accept** | Acknowledge and monitor | Low risk within appetite, cost of treatment exceeds benefit |
| **Exploit** | Increase exposure to capture upside (for opportunities) | Positive risk/opportunity worth pursuing |

---

## Risk Register Management

### Risk Register Template

| Field | Description | Example |
|-------|-------------|---------|
| **Risk ID** | Unique identifier | R-2026-001 |
| **Category** | Risk domain | Strategic, Operational, Financial, Compliance |
| **Description** | What could happen | "Key vendor could discontinue product" |
| **Cause** | Why it might happen | "Vendor is startup with limited funding" |
| **Impact** | What happens if it occurs | "6-month delay while migrating to alternative" |
| **Likelihood** | Probability (1-5) | 3 (Possible) |
| **Impact Score** | Severity (1-5) | 4 (Major) |
| **Risk Score** | Likelihood x Impact | 12 (High) |
| **Current Controls** | Existing mitigations | "Monthly vendor health monitoring" |
| **Treatment Plan** | Additional actions | "Identify and evaluate alternative vendors" |
| **Owner** | Person accountable | VP Engineering |
| **Status** | Current state | Open, Mitigating, Accepted, Closed |
| **Review Date** | Next review | 2026-03-15 |

### Likelihood Scale

| Score | Label | Description | Frequency |
|-------|-------|-------------|-----------|
| 1 | Rare | Very unlikely | <5% chance in 12 months |
| 2 | Unlikely | Not expected | 5-20% chance |
| 3 | Possible | Might occur | 20-50% chance |
| 4 | Likely | Will probably occur | 50-80% chance |
| 5 | Almost Certain | Expected to occur | >80% chance |

### Impact Scale

| Score | Label | Financial | Operational | Reputational |
|-------|-------|-----------|-------------|-------------|
| 1 | Negligible | <$10K | Minor inconvenience | No external notice |
| 2 | Minor | $10K-$100K | Some disruption, workaround available | Limited stakeholder awareness |
| 3 | Moderate | $100K-$1M | Significant disruption, degraded service | Industry notice |
| 4 | Major | $1M-$10M | Extended outage, major service impact | Media attention |
| 5 | Catastrophic | >$10M | Complete service failure | Regulatory action, existential |

### Risk Heat Map

```
IMPACT
5 │  5  │ 10  │ 15  │ 20  │ 25  │
4 │  4  │  8  │ 12  │ 16  │ 20  │
3 │  3  │  6  │  9  │ 12  │ 15  │
2 │  2  │  4  │  6  │  8  │ 10  │
1 │  1  │  2  │  3  │  4  │  5  │
  └─────┴─────┴─────┴─────┴─────┘
    1     2     3     4     5
                LIKELIHOOD

Green (1-4): Accept and monitor
Yellow (5-9): Mitigate, regular review
Orange (10-15): Active mitigation required
Red (16-25): Immediate action required
```

---

## Business Continuity Planning (BCP)

### BCP Components

| Component | Purpose | Deliverable |
|-----------|---------|------------|
| **Business Impact Analysis (BIA)** | Identify critical functions and dependencies | BIA report with RTOs and RPOs |
| **Risk Assessment** | Evaluate threats to operations | Threat assessment matrix |
| **Recovery Strategy** | Define how to restore operations | Recovery strategy document |
| **Plan Development** | Document detailed procedures | BCP document |
| **Testing & Exercise** | Validate plan effectiveness | Test results and improvements |
| **Maintenance** | Keep plan current | Annual review and update |

### Business Impact Analysis (BIA)

| Function | RTO | RPO | Impact per Hour | Dependencies | Priority |
|----------|-----|-----|-----------------|-------------|----------|
| Customer-facing API | 1 hour | 0 (real-time) | High | Cloud infra, DB, CDN | P0 |
| Payment processing | 4 hours | 1 hour | High | Payment gateway, DB | P0 |
| Email service | 8 hours | 4 hours | Medium | Email provider, templates | P1 |
| Reporting | 24 hours | 8 hours | Low | Data warehouse, BI tool | P2 |
| Internal wiki | 48 hours | 24 hours | Low | Wiki platform | P3 |

**RTO** (Recovery Time Objective): Maximum acceptable downtime
**RPO** (Recovery Point Objective): Maximum acceptable data loss (in time)

### Disaster Recovery Strategies

| Strategy | RTO | Cost | Description |
|----------|-----|------|-------------|
| **Cold Site** | Days-Weeks | Low | Empty facility, must provision everything |
| **Warm Site** | Hours-Days | Medium | Pre-configured, needs data restore |
| **Hot Site** | Minutes-Hours | High | Fully operational replica, near-real-time sync |
| **Active-Active** | Seconds | Very High | Multiple live sites, automatic failover |
| **Cloud DR** | Minutes-Hours | Variable | Cloud-based recovery (AWS, Azure, GCP) |

---

## Risk Identification Methods

### PESTLE Analysis

| Factor | Description | Risk Examples |
|--------|-------------|---------------|
| **P**olitical | Government policy, regulation, trade | Regulatory changes, sanctions, political instability |
| **E**conomic | Economic conditions, markets | Recession, interest rates, currency fluctuation |
| **S**ocial | Demographics, culture, trends | Talent shortage, changing customer preferences |
| **T**echnological | Innovation, disruption, obsolescence | Tech obsolescence, cybersecurity threats, AI disruption |
| **L**egal | Legislation, litigation, compliance | New laws, lawsuits, IP disputes |
| **E**nvironmental | Climate, sustainability, resources | Climate events, sustainability regulations, resource scarcity |

### Scenario Analysis

| Scenario Type | Description | Method |
|---------------|-------------|--------|
| **Best Case** | Favorable assumptions hold | Identify upside opportunities |
| **Base Case** | Expected outcome | Current trajectory continuation |
| **Worst Case** | Unfavorable assumptions materialize | Stress test resilience |
| **Black Swan** | Extreme, unexpected event | Challenge assumptions fundamentally |

### Risk Reporting

| Audience | Frequency | Content | Format |
|----------|-----------|---------|--------|
| Board | Quarterly | Top 10 risks, trends, emerging risks | Risk dashboard + narrative |
| Executive team | Monthly | All high risks, treatment progress | Risk register summary |
| Risk owners | Weekly | Their risks, action item status | Risk detail + actions |
| All staff | Quarterly | Risk awareness, culture reminders | Town hall / newsletter |

---

## Emerging Risk Categories (2025-2026)

| Category | Key Risks | Monitoring Sources |
|----------|-----------|-------------------|
| **AI/ML Risks** | Model bias, hallucination, regulatory compliance, IP | EU AI Act, NIST AI RMF |
| **Supply Chain** | Vendor concentration, geopolitical disruption | Supplier monitoring, news feeds |
| **Cyber** | Ransomware, supply chain attacks, zero-day exploits | CISA alerts, threat intelligence |
| **Climate** | Physical climate events, transition risks, regulation | TCFD framework, climate models |
| **Talent** | Remote work challenges, skills gaps, retention | HR metrics, market surveys |
| **Regulatory** | Privacy laws proliferation, AI regulation, ESG requirements | Legal monitoring, trade associations |

---

*Last Updated: 2026-02-14*
*References: COSO ERM Framework (2017), ISO 31000:2018, BCI Good Practice Guidelines, NIST SP 800-34*


## Common Pitfalls

- Risk likelihood and impact must be assessed separately — don't conflate them
- Risk appetite should be defined by leadership, not assumed by the risk manager
- Business continuity plans must be tested — untested plans are assumptions
