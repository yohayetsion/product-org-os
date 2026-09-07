# Support Operations Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: `support-lead`, `cs-ops`
**Secondary Users**: `cs-dir`, `kb-specialist`

<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - Support Driven community (supportdriven.com) — tiered support models, SLA design, support metrics
  - chatwoot/chatwoot (github.com/chatwoot/chatwoot) — ticket management and canned response patterns
  - ITIL v4 service management practices — incident and service request management adapted for CS
  Adapted and expanded for Product Org OS agents.
-->

---

## Tiered Support Model

### Tier Definitions

| Tier | Scope | Skills Required | Escalation Trigger |
|------|-------|----------------|-------------------|
| **Tier 0 (Self-Service)** | Knowledge base, FAQs, community forums, in-app help | None (automated) | Customer can't find answer |
| **Tier 1 (Frontline)** | Known issues, how-to, account/billing, basic troubleshooting | Product knowledge, communication | Issue requires investigation or code-level access |
| **Tier 2 (Technical)** | Complex troubleshooting, bug reproduction, configuration issues | Deep product + technical knowledge | Root cause unclear, product bug confirmed |
| **Tier 3 (Engineering)** | Bug fixes, infrastructure issues, data recovery | Engineering skills | Code change or infrastructure intervention needed |
| **Tier 4 (Vendor/External)** | Third-party integration issues, vendor escalations | Vendor relationship management | Issue traced to external dependency |

### Tier Routing Decision Tree

```
New ticket arrives →
  1. Is there a KB article that answers this? → Link to T0, close
  2. Is this a known issue with a workaround? → T1 applies workaround
  3. Does it require investigation? → T1 investigates, escalates to T2 if needed
  4. Is it a confirmed bug or infra issue? → T2 documents, escalates to T3
  5. Is it a third-party issue? → T2 manages vendor escalation (T4)
```

---

## SLA Framework

### SLA Definitions by Priority

| Priority | Definition | First Response | Resolution Target | Examples |
|----------|-----------|---------------|-------------------|---------|
| **P0 - Critical** | Service down, all users affected, no workaround | 15 min | 4 hours | Complete outage, data loss, security breach |
| **P1 - High** | Major feature broken, significant user impact, no workaround | 1 hour | 8 hours | Core workflow broken, performance severely degraded |
| **P2 - Medium** | Feature impaired, workaround exists | 4 hours | 2 business days | Non-critical feature bug, intermittent issue |
| **P3 - Low** | Minor issue, cosmetic, feature request | 1 business day | 5 business days | UI glitch, documentation error, enhancement request |

### SLA Measurement Rules

| Rule | Description |
|------|-------------|
| **Clock starts** | When ticket is created (not when agent views it) |
| **Clock pauses** | When waiting for customer response (status: "Awaiting Customer") |
| **Clock resumes** | When customer responds |
| **Business hours** | Define per contract (e.g., 9-5 local time vs. 24/7) |
| **Breach notification** | Auto-alert at 75% of SLA elapsed |
| **Resolution** | Issue confirmed fixed by customer, not just "response sent" |

### SLA Compliance Calculation

```
SLA Compliance Rate = (Tickets Resolved Within SLA / Total Tickets) × 100

Target by Priority:
  P0: 95%+ compliance
  P1: 90%+ compliance
  P2: 85%+ compliance
  P3: 80%+ compliance

Overall: Weighted average across priorities
```

---

## Ticket Triage Framework

### Triage Checklist (Every Ticket)

1. **Identify**: What is the customer trying to do?
2. **Classify**: Bug, how-to, feature request, account/billing, or incident?
3. **Prioritize**: What is the business impact? (P0-P3)
4. **Route**: Which tier/specialist should handle this?
5. **Context**: What account context matters? (segment, health, open issues)
6. **Acknowledge**: Send first response within SLA

### Ticket Classification Categories

| Category | Description | Typical Priority | Routing |
|----------|-----------|-----------------|---------|
| **Bug Report** | Product not working as expected | P1-P2 | T1 → T2 if confirmed |
| **How-To** | Customer needs guidance on using a feature | P3 | T1 (or T0 if KB exists) |
| **Feature Request** | Customer wants new functionality | P3 | T1 → log to product backlog |
| **Account/Billing** | Access, permissions, invoicing | P2-P3 | T1 (account team) |
| **Incident** | Service degradation or outage | P0-P1 | Incident response process |
| **Data Request** | Export, migration, deletion | P2-P3 | T1 → T2 if technical |
| **Integration** | Third-party integration issues | P2 | T2 (technical) |
| **Security** | Vulnerability report, compliance query | P0-P1 | Security team |

### Priority Determination Matrix

| | High Business Impact | Low Business Impact |
|---|---|---|
| **Many Users Affected** | P0-P1 | P2 |
| **Few Users Affected** | P1-P2 | P3 |

Factor in: workaround availability, customer segment, renewal proximity.

---

## Response Templates — Best Practices

### Template Structure

```
[Greeting — personalized]

[Acknowledgment — show you understand the issue]

[Action taken or next step — be specific]

[Expected timeline — when will they hear back]

[Closing — human, not robotic]
```

### Template Categories

| Category | Purpose | Personalization Required |
|----------|---------|------------------------|
| **Acknowledgment** | Confirm receipt, set expectations | Customer name, issue summary |
| **Investigation** | Update while researching | Specific findings so far, next steps |
| **Workaround** | Provide temporary solution | Exact steps for their setup |
| **Resolution** | Confirm fix, close loop | What was fixed, why it happened, prevention |
| **Escalation** | Inform of routing change | Who is taking over, why, what's next |
| **Follow-Up** | Check post-resolution | Reference original issue, ask specifically |

### Response Quality Standards

| Standard | Requirement | Anti-Pattern |
|----------|------------|-------------|
| **Personalization** | Customer name, specific issue reference | "Dear Customer" or ticket number only |
| **Specificity** | Exact steps, specific answers | "Please try again" or "It should work now" |
| **Empathy** | Acknowledge impact and frustration | "As per our policy..." |
| **Completeness** | Answer all questions in the ticket | Addressing only the first question |
| **Actionability** | Clear next step for customer or agent | "We're looking into it" with no timeline |
| **Proactive info** | Include related tips or known issues | Only answering the literal question |

---

## Escalation Framework

### Escalation Types

| Type | Trigger | Owner | SLA |
|------|---------|-------|-----|
| **Technical** | Issue beyond current tier's capability | Next tier | Per priority SLA |
| **Management** | SLA breach, customer dissatisfaction, repeated issue | Team lead/manager | 1 hour acknowledgment |
| **Executive** | Strategic account at risk, legal threat, data breach | VP/C-level | Immediate notification |
| **Cross-functional** | Issue requires product, engineering, or legal input | Support Lead coordinates | 4 hours for plan |

### Escalation Handoff Template

```
## Escalation Handoff

**Ticket**: [ID]
**Customer**: [Name] | Segment: [Tier] | Health: [Score]
**Priority**: [P0-P3]
**Escalation Type**: [Technical/Management/Executive/Cross-functional]

### Issue Summary
[2-3 sentences — what the customer is experiencing]

### What's Been Tried
1. [Action 1] — Result: [outcome]
2. [Action 2] — Result: [outcome]

### Root Cause Hypothesis
[Best current understanding]

### Customer Impact
[Business impact, number of affected users, workaround status]

### What the Customer Expects
[Timeline, resolution type, communication preference]

### Recommended Next Steps
1. [Step]
2. [Step]
```

---

## Support Metrics Dashboard

### Operational Metrics

| Metric | Definition | Target | Frequency |
|--------|-----------|--------|-----------|
| **First Response Time** | Time from ticket creation to first human response | Per SLA by priority | Real-time |
| **Resolution Time** | Time from creation to confirmed resolution | Per SLA by priority | Real-time |
| **SLA Compliance** | % of tickets resolved within SLA | 90%+ overall | Weekly |
| **First Contact Resolution** | % resolved without escalation or follow-up | 60-70% | Weekly |
| **Reopen Rate** | % of resolved tickets reopened | <10% | Weekly |
| **Backlog Age** | Average age of open tickets | <2 business days | Daily |

### Quality Metrics

| Metric | Definition | Target | Frequency |
|--------|-----------|--------|-----------|
| **CSAT** | Post-interaction satisfaction | 90%+ | Per interaction |
| **Quality Score** | Internal review of response quality | 85%+ | Monthly (sample) |
| **Escalation Rate** | % of tickets escalated beyond T1 | 20-30% | Weekly |
| **Deflection Rate** | % of issues resolved by self-service | 30-50% | Monthly |

### Signal Metrics (Product Feedback)

| Metric | Definition | Action | Frequency |
|--------|-----------|--------|-----------|
| **Top Ticket Categories** | Most common issue types | Product feedback, KB gaps | Weekly |
| **Bug Report Volume** | New bugs reported per period | Engineering prioritization | Weekly |
| **Feature Request Themes** | Common feature requests | Product backlog input | Monthly |
| **Repeat Issues** | Issues that recur for same customer | Root cause investigation | Weekly |

---

## Incident Management (Adapted from ITIL v4)

### Incident Severity Levels

| Severity | Criteria | Communication | Cadence |
|----------|----------|---------------|---------|
| **SEV1** | Complete outage, all customers | Status page + direct email + Slack | Every 30 min until resolved |
| **SEV2** | Major degradation, many customers | Status page + affected customer email | Every 1 hour |
| **SEV3** | Minor degradation, some customers | Status page update | Every 2 hours |
| **SEV4** | Localized issue, few customers | Direct communication to affected | As needed |

### Incident Response Process

| Phase | Actions | Timing |
|-------|---------|--------|
| **Detection** | Monitor alerts, customer reports, status checks | Immediate |
| **Triage** | Classify severity, assemble response team | <15 min |
| **Communication** | Notify customers per severity table | Per cadence |
| **Investigation** | Root cause analysis, identify fix | Ongoing |
| **Resolution** | Apply fix, verify, confirm with customers | ASAP |
| **Post-Mortem** | Root cause report, prevention plan, customer follow-up | Within 48 hours |

### Post-Incident Customer Communication Template

```
Subject: [Resolved] Service Incident — [Brief Description]

Hi [Name],

We wanted to follow up on the service incident that occurred on [date] between [start time] and [end time].

**What happened**: [Plain language explanation — not technical jargon]

**Impact**: [What customers experienced]

**Root cause**: [Why it happened]

**What we've done**: [Immediate fix and long-term prevention]

We take service reliability seriously, and we apologize for the disruption to your work. If you have any questions or concerns, please don't hesitate to reach out.

[Name]
```

---

## Canned Response Patterns (Adapted from Chatwoot)

### Response Categories for Automation

| Category | Automation Level | Human Review Required |
|----------|-----------------|---------------------|
| **Acknowledgment** | Fully automated | No (but personalize greeting) |
| **Known Issue** | Semi-automated (template + context) | Yes (verify customer's case matches) |
| **How-To** | Semi-automated (link to KB article) | Yes (confirm article answers their question) |
| **Bug Confirmation** | Manual with template | Yes (specific reproduction and timeline) |
| **Escalation Notification** | Automated trigger, manual message | Yes (context-aware handoff) |
| **Resolution** | Manual with template | Yes (verify fix, personalize closing) |

### Conversation Routing Rules

| Rule | Condition | Action |
|------|-----------|--------|
| **VIP Routing** | Customer segment = Strategic/Enterprise | Route to senior agent + notify CSM |
| **Language Routing** | Detected language != English | Route to language-appropriate agent |
| **Topic Routing** | Keyword match (billing, API, etc.) | Route to specialist queue |
| **Round Robin** | Default | Distribute evenly across available agents |
| **Skill-Based** | Issue type matches agent expertise | Route to best-matched agent |

---

## Support Team Capacity Planning

### Capacity Formula

```
Required Agents = (Monthly Ticket Volume × Avg Handle Time) / (Work Hours per Agent × Utilization Rate)

Typical values:
  Avg Handle Time: 15-30 min (T1), 45-90 min (T2)
  Work Hours per Agent: 160 hours/month
  Utilization Rate: 70-80% (accounts for breaks, meetings, training)
```

### Coverage Model

| Model | Best For | Tradeoff |
|-------|----------|---------|
| **Follow-the-Sun** | Global customer base, 24/7 SLA | Higher headcount, coordination overhead |
| **On-Call** | After-hours P0/P1 coverage | Burnout risk, response time variance |
| **Shift-Based** | Extended hours without 24/7 | Handoff complexity, scheduling overhead |
| **Business Hours Only** | Regional, non-critical product | Limited coverage, SLA must reflect this |

---

## Agentic Support Operations (2026)

*Added 2026-06-24. Operations-metrics only — for AI-resolution **strategy** (CSAT-floor design, escape-hatch design, never-deflect-list authoring) invoke `/ai-assisted-resolution-strategy` and load the `ai-agent-supervisor` pack. This section does not duplicate that strategy; it covers how support **operations metrics and economics** change once an AI agent owns tier-1 resolution.*

**Adapted from**:
- Intercom Fin, Lorikeet, Zendesk AI — vendor-published per-resolution pricing (2026): Fin by Intercom $0.99/automated resolution; Lorikeet chat ~$0.80/resolution; Zendesk AI ~$1.50–$2.00/resolution (fin.ai, lorikeetcx.ai, myaskai.com, helply.com, accessed 2026-06-24)
- CNBC, "'I hate customer-service chatbots': The consumer-AI refund relationship is off to a rocky start" (cnbc.com, 2026-04-01)
- getperspective.ai ("From Deflection to Understanding"), swept.ai ("The Deflection Rate Dilemma: verify AI help-agent metrics"), bluetweak.com ("AI-to-Human Handoff: Best Practices") — accessed 2026-06-24

**Source licence**: publicly-cited vendor and press sources; no formal OSS license.

**V2V refinements**: CSAT-floor + escape-hatch + never-deflect discipline; deflection-must-be-verified-not-counted; handoff-continuity treated as the operational seam; cross-ref to `/ai-assisted-resolution-strategy` + `ai-agent-supervisor` for strategy (no strategy duplication here).

### The metric shift

When an AI agent (Fin / Sierra / Decagon-class) owns tier-1 resolution, three operational metrics change. These extend — they do not replace — the Support Metrics Dashboard above.

| Metric | What changes | How to measure |
|--------|-------------|----------------|
| **Verified Deflection Rate** | Deflection is now a **paid outcome** under per-resolution pricing, so an inflated number costs real money. Vendors and customers both miscount abandoned conversations as "resolutions." | Count **only confirmed resolutions** (issue closed, customer did not re-open or re-route within the follow-up window). Never count an abandoned or escalated conversation as deflected. Reconcile vendor-reported resolutions against your own re-open / re-contact data before paying. |
| **Handoff Continuity** | The AI→human escalation is the new make-or-break seam. A broken handoff forces the customer to re-explain — the cardinal anti-pattern. | % of AI→human escalations where full context (history, intent, attempted steps) transfers so the customer never re-explains. This is the agentic-era equivalent of First Contact Resolution quality. |
| **Resolution-cost-per-ticket** | Pricing moved from per-seat to **per-resolution** ($0.80–$2.00/resolution, vendor-published 2026). Deflection volume is now a direct cost line, not a free efficiency. | (AI resolutions × per-resolution rate) + human-handled cost. Track cost-per-resolved-ticket across the AI/human split, not just headcount capacity (see Capacity Formula above for the human side). |

### V2V caveat (NON-NEGOTIABLE)

AI agents resolve tier-1 volume; **humans own escalation.** Optimizing for raw deflection without these guardrails breaches the customer-experience floor (the 2026 consumer backlash is the evidence):

- **Hard CSAT floor** — set a CSAT threshold below which deflection is throttled and more volume routes to humans. Deflection is never optimized past the floor.
- **Mandatory escape hatch** — a one-click, always-available "reach a human" path in every AI conversation. No dead-ends, no loops back to the bot.
- **Never-deflect list** — categories the AI agent must hand to a human immediately, not attempt to resolve: billing disputes, security / data-loss / breach, churn / cancellation signals, legally-sensitive matters, and any VIP / strategic-account routing (per the Conversation Routing Rules above).
- **Optimize for understanding, not deflection** — a deflected ticket with a frustrated customer is a *deferred escalation*, not a resolution. The goal is resolved-and-satisfied, measured by Verified Deflection Rate × CSAT, never deflection volume alone.

---

*Last Updated: 2026-06-24*
*References: Support Driven community, chatwoot/chatwoot, ITIL v4 service management; agentic-support section adds Intercom Fin / Lorikeet / Zendesk AI pricing 2026, CNBC 2026-04-01, getperspective.ai, swept.ai, bluetweak.com (accessed 2026-06-24)*
