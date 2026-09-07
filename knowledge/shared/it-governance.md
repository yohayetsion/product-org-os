# IT Governance Knowledge Pack

**Version**: 1.0
**Primary Users**: `cio`, `it-dir`, `enterprise-systems`
**Domain**: IT Governance Frameworks & Service Management

---

## COBIT 2019 Framework

### Governance System Principles

| Principle | Description |
|-----------|-------------|
| **1. Provide Stakeholder Value** | IT governance exists to meet stakeholder needs |
| **2. Holistic Approach** | Consider all components of the governance system |
| **3. Dynamic Governance System** | Adapt governance as the enterprise changes |
| **4. Governance Distinct from Management** | Governance evaluates, directs, monitors; Management plans, builds, runs |
| **5. Tailored to Enterprise Needs** | Customize using design factors |
| **6. End-to-End Governance System** | Cover full enterprise IT, not just IT department |

### COBIT Governance & Management Objectives

| Domain | Code | Objectives |
|--------|------|------------|
| **Evaluate, Direct, Monitor (EDM)** | EDM01-05 | Governance framework, benefits delivery, risk optimization, resource optimization, stakeholder transparency |
| **Align, Plan, Organize (APO)** | APO01-14 | IT management framework, strategy, architecture, innovation, portfolio, budget, HR, relationships, service agreements, vendors, quality, risk, security, data |
| **Build, Acquire, Implement (BAI)** | BAI01-11 | Programs/projects, requirements, solutions, availability, change enablement, IT changes, IT change acceptance, knowledge, assets, configuration, development |
| **Deliver, Service, Support (DSS)** | DSS01-06 | Operations, service requests/incidents, problems, continuity, security services, business process controls |
| **Monitor, Evaluate, Assess (MEA)** | MEA01-04 | Performance/conformance monitoring, internal controls, external compliance, assurance |

### COBIT Design Factors

| Factor | Options | Impact |
|--------|---------|--------|
| Enterprise Strategy | Growth, Innovation, Cost Leadership, Client Service | Shapes IT priorities |
| Enterprise Goals | Financial, Customer, Internal, Learning | Maps IT goals |
| Risk Profile | Low, Normal, High | Controls depth |
| IT-Related Issues | Current IT challenges | Focus areas |
| Threat Landscape | Normal, High | Security investment |
| Compliance Requirements | Low, Normal, High | Governance rigor |
| Role of IT | Support, Factory, Turnaround, Strategic | Investment level |
| Sourcing Model | Outsourced, Cloud, In-house, Hybrid | Governance scope |
| IT Implementation Methods | Agile, DevOps, Traditional | Process design |
| Technology Adoption | First Mover, Follower, Slow Adopter | Innovation investment |
| Enterprise Size | Large, SME | Governance complexity |

### Capability Maturity Model

| Level | Name | Description |
|-------|------|-------------|
| 0 | Incomplete | Process not implemented or fails to achieve purpose |
| 1 | Performed | Process achieves purpose but not managed |
| 2 | Managed | Process is planned, monitored, and adjusted |
| 3 | Established | Process follows a defined standard process |
| 4 | Predictable | Process operates within defined limits |
| 5 | Optimizing | Process is continuously improved |

---

## ITIL 4 Framework

### Service Value System

```
Guiding Principles
    ↓
Governance
    ↓
Service Value Chain (Plan → Improve → Engage → Design & Transition → Obtain/Build → Deliver & Support)
    ↓
Practices (34 total)
    ↓
Continual Improvement
```

### ITIL 4 Guiding Principles

| Principle | Application |
|-----------|-------------|
| **Focus on Value** | Everything the organization does should map back to value for stakeholders |
| **Start Where You Are** | Assess current state before creating something new |
| **Progress Iteratively** | Don't try to do everything at once |
| **Collaborate and Promote Visibility** | Working together produces better results |
| **Think and Work Holistically** | No service or element stands alone |
| **Keep It Simple and Practical** | Use the minimum number of steps to accomplish the objective |
| **Optimize and Automate** | Maximize value of human and technical resources |

### ITIL 4 Practices

**General Management Practices (14)**:
- Strategy management, Portfolio management, Architecture management
- Service financial management, Workforce and talent management
- Continual improvement, Measurement and reporting
- Risk management, Information security management
- Knowledge management, Organizational change management
- Project management, Relationship management, Supplier management

**Service Management Practices (17)**:
- Business analysis, Service catalog management, Service design
- Service level management, Availability management, Capacity management
- IT asset management, Monitoring and event management
- Release management, Service configuration management
- Deployment management, Change enablement
- Incident management, Problem management, Service request management
- Service desk, Service validation and testing

**Technical Management Practices (3)**:
- Infrastructure and platform management
- Software development and management
- Deployment management

### Incident vs Problem vs Change

| Process | Purpose | Trigger | Goal |
|---------|---------|---------|------|
| **Incident** | Restore service | Service disruption | Minimize impact, restore ASAP |
| **Problem** | Find root cause | Recurring incidents | Prevent future incidents |
| **Change** | Implement modifications | Business need, problem fix | Controlled modification |

### Change Types

| Type | Risk | Approval | Example |
|------|------|----------|---------|
| **Standard** | Low, pre-approved | No approval needed | Password reset, software update |
| **Normal** | Medium | Change Advisory Board | New server deployment |
| **Emergency** | High, urgent | Emergency CAB | Critical security patch |

---

## 2026-06 Delta Update (as of 2026-06-06)

### ITIL AI Governance (Version 5) module — planned Q2 2026

ITIL Version 5 launched 2026-05-12 as the successor to ITIL 4. PeopleCert (the ITIL governing body / certification authority) lists a dedicated **ITIL AI Governance (Version 5)** module as **planned for Q2 2026**, positioned around "responsible, transparent, value-driven AI adoption." This is the ITSM standards body's formal entry into AI governance — the ITIL-native counterpart to the AI-governance scaffolding already covered under COBIT design factors and the broader risk frameworks.

**Status (important — no fabrication)**: as of 2026-06-06 **no firm release date is confirmed**. PeopleCert's public materials frame it as "planned Q2 2026"; treat the module as forthcoming, not shipped. The core ITIL Version 5 launch (2026-05-12) is confirmed; the AI Governance module is the planned add-on.

**What is publicly indicated** (subject to change until release):
- Scope framed as responsible, transparent, value-driven AI adoption within the ITIL Service Value System
- Positioned as a Version 5 module layered on the existing ITIL practices (Information security management, Risk management, Knowledge management, and the Governance component of the Service Value System are the natural integration points)
- A formal AI-governance certification track from the ITSM standards body, complementing — not replacing — COBIT 2019's governance objectives (EDM03 risk optimization, APO12 risk, APO13 security) and design factors

**Integration with existing IT governance**: when the module ships, map it against the COBIT governance/management objectives above (especially EDM and the APO risk/security/data objectives) and against the IT Governance Bodies table (a Security Governance Committee or a dedicated AI Governance Council is the natural home for the module's controls). Until release, use the COBIT design factors (Threat Landscape, Compliance Requirements, Role of IT, Technology Adoption) to frame AI-governance maturity.

**Cross-reference**: `risk-management.md` for the risk-framework layer that the ITIL AI Governance module operationalizes within the ITSM context.

**Sources** (added 2026-06-06):
- PeopleCert — "ITIL Version 5 Explained" (peoplecert.org/news-and-announcements/itil-version-5-explained)
- Advised Skills — "ITIL Version 5 in 2026: what is confirmed, what is available, and what comes next" (advisedskills.com/blog/it-service-management/itil-version-5-in-2026-what-is-confirmed-what-is-available-and-what-comes-next)
- ITIL® is a registered trademark of PeopleCert; frameworks referenced by name and concept only, no proprietary content reproduced.

---

## IT Service Management Metrics

### Service Level Metrics

| Metric | Description | Typical Target |
|--------|-------------|----------------|
| Availability | % time service is operational | 99.9% (8.76 hrs/yr downtime) |
| MTTR | Mean Time to Restore | < 1 hour (P1), < 4 hours (P2) |
| MTBF | Mean Time Between Failures | > 30 days |
| First Contact Resolution | % resolved on first contact | > 70% |
| Customer Satisfaction | CSAT/NPS for IT services | CSAT > 4.0/5.0 |

### Availability Tiers

| Tier | Availability | Annual Downtime | Use Case |
|------|-------------|-----------------|----------|
| 99% | Two 9s | 3.65 days | Internal tools |
| 99.9% | Three 9s | 8.76 hours | Standard business apps |
| 99.95% | Three and a half 9s | 4.38 hours | Important services |
| 99.99% | Four 9s | 52.6 minutes | Critical services |
| 99.999% | Five 9s | 5.26 minutes | Mission-critical |

### IT Financial Metrics

| Metric | Description | Benchmark |
|--------|-------------|-----------|
| IT spend as % of revenue | Total IT cost / total revenue | 3-8% (varies by industry) |
| IT spend per employee | Total IT cost / employee count | $5,000-$15,000 |
| Projects on time/budget | % projects delivered within plan | > 60% |
| Application TCO | Total cost of owning an application | License + implementation + 5yr ops |
| Shadow IT spend | Unmanaged technology spending | < 15% of total IT |

---

## IT Portfolio Management

### Application Portfolio Categories

| Category | Action | Criteria |
|----------|--------|----------|
| **Invest** | Increase capability | High business value, high technical quality |
| **Maintain** | Keep running | High business value, adequate technical quality |
| **Migrate** | Move to modern platform | High business value, poor technical quality |
| **Retire** | Decommission | Low business value, poor technical quality |
| **Tolerate** | Accept as-is | Low business value, adequate technical quality |

### Technology Radar

| Ring | Meaning | Action |
|------|---------|--------|
| **Adopt** | Proven, recommended | Use for new projects |
| **Trial** | Worth pursuing, low risk | Pilot in non-critical use |
| **Assess** | Worth exploring | Evaluate through research/POC |
| **Hold** | Proceed with caution | Don't use for new projects |

---

## IT Governance Bodies

### Recommended Governance Structure

| Body | Composition | Frequency | Scope |
|------|-------------|-----------|-------|
| **IT Steering Committee** | CEO, CIO, C-suite | Quarterly | IT strategy, major investments |
| **Architecture Review Board** | CIO, architects, senior devs | Monthly | Technology standards, architecture decisions |
| **Change Advisory Board** | IT Dir, service owners, security | Weekly | Change approvals, risk assessment |
| **Data Governance Council** | CIO, data stewards, legal | Monthly | Data policies, quality, privacy |
| **Security Governance Committee** | CIO, CISO, legal, compliance | Monthly | Security posture, incidents, policy |

---

*Last Updated: 2026-02-14 (2026-06 delta: ITIL AI Governance Version 5 module — see "2026-06 Delta Update" section above)*


## Common Pitfalls

- COBIT and ITIL frameworks should be adapted to organization size — full implementation is for enterprises
- IT governance maturity assessments are subjective — always state the assessment methodology
- Shadow IT exists in most organizations — address it, don't assume it away
