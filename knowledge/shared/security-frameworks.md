# Cybersecurity Frameworks Knowledge Pack

**Version**: 1.0
**Primary Users**: `it-security-policy`, `cio`, `security-architect`
**Domain**: Enterprise Cybersecurity Governance

---

## NIST Cybersecurity Framework 2.0

### Core Functions

| Function | Purpose | Categories |
|----------|---------|------------|
| **GOVERN (GV)** | Establish cybersecurity risk management strategy | Context, Strategy, Roles/Responsibilities, Policy, Oversight, Supply Chain |
| **IDENTIFY (ID)** | Understand assets and risks | Asset Management, Risk Assessment, Improvement |
| **PROTECT (PR)** | Implement safeguards | Identity Management, Awareness/Training, Data Security, Platform Security, Technology Infrastructure |
| **DETECT (DE)** | Discover cybersecurity events | Continuous Monitoring, Adverse Event Analysis |
| **RESPOND (RS)** | Act on detected events | Incident Management, Analysis, Reporting/Communication, Mitigation |
| **RECOVER (RC)** | Restore operations | Incident Recovery Plan, Recovery Communication |

### Implementation Tiers

| Tier | Name | Risk Management | External Participation |
|------|------|-----------------|----------------------|
| 1 | Partial | Ad hoc, reactive | Limited awareness |
| 2 | Risk Informed | Approved but not org-wide | Understands ecosystem role |
| 3 | Repeatable | Org-wide, regularly updated | Actively participates |
| 4 | Adaptive | Continuous, uses lessons learned | Leads ecosystem |

### Security-control capability maturity pointer (supplementary)

[Secure Controls Framework SCR-CMM](https://securecontrolsframework.com/free-content/capability-maturity-model-scr-cmm) is a separately published five-level security-control capability model that a reviewer may select when the work specifically calls for control-maturity criteria.

SCR-CMM levels are not interchangeable with NIST CSF implementation tiers or the CISA zero-trust maturity model. Do not translate, score, certify, infer compliance, or claim assurance from one model to another. Name the selected model and its criteria for the particular assessment.

### NIST CSF Profile Template

| Category | Current Tier | Target Tier | Gap | Priority | Timeline |
|----------|-------------|-------------|-----|----------|----------|
| GV.RM Risk Management Strategy | | | | | |
| ID.AM Asset Management | | | | | |
| PR.AC Access Control | | | | | |
| DE.CM Continuous Monitoring | | | | | |
| RS.RP Response Planning | | | | | |
| RC.RP Recovery Planning | | | | | |

---

## CIS Controls v8

### Implementation Groups

| Group | Target | Controls |
|-------|--------|----------|
| **IG1** | Essential cyber hygiene (all orgs) | 56 safeguards |
| **IG2** | Organizations with IT complexity | 74 additional safeguards |
| **IG3** | Sophisticated attackers expected | 23 additional safeguards |

### CIS Controls (18 Total)

| # | Control | IG1 | IG2 | IG3 |
|---|---------|-----|-----|-----|
| 1 | Inventory and Control of Enterprise Assets | Yes | Yes | Yes |
| 2 | Inventory and Control of Software Assets | Yes | Yes | Yes |
| 3 | Data Protection | Yes | Yes | Yes |
| 4 | Secure Configuration of Enterprise Assets | Yes | Yes | Yes |
| 5 | Account Management | Yes | Yes | Yes |
| 6 | Access Control Management | Yes | Yes | Yes |
| 7 | Continuous Vulnerability Management | - | Yes | Yes |
| 8 | Audit Log Management | - | Yes | Yes |
| 9 | Email and Web Browser Protections | - | Yes | Yes |
| 10 | Malware Defenses | Yes | Yes | Yes |
| 11 | Data Recovery | Yes | Yes | Yes |
| 12 | Network Infrastructure Management | - | Yes | Yes |
| 13 | Network Monitoring and Defense | - | - | Yes |
| 14 | Security Awareness and Skills Training | Yes | Yes | Yes |
| 15 | Service Provider Management | - | Yes | Yes |
| 16 | Application Software Security | - | Yes | Yes |
| 17 | Incident Response Management | Yes | Yes | Yes |
| 18 | Penetration Testing | - | - | Yes |

---

## ISO 27001:2022

### Information Security Management System (ISMS)

**Plan-Do-Check-Act Cycle**:

| Phase | Activities |
|-------|-----------|
| **Plan** | Define scope, policy, risk assessment methodology, Statement of Applicability |
| **Do** | Implement risk treatment plan, controls, awareness training |
| **Check** | Internal audits, management review, measurement |
| **Act** | Corrective actions, continual improvement |

### Annex A Control Categories

| Category | Controls | Examples |
|----------|----------|---------|
| **Organizational (37)** | Policies, roles, asset management | Information security policy, threat intelligence |
| **People (8)** | HR security, awareness | Screening, terms of employment, awareness |
| **Physical (14)** | Physical security | Security perimeters, entry controls, equipment |
| **Technological (34)** | Technical controls | Access control, cryptography, logging, malware |

### Certification Process

| Phase | Duration | Activity |
|-------|----------|----------|
| Gap analysis | 2-4 weeks | Assess current vs ISO 27001 requirements |
| Remediation | 3-12 months | Implement missing controls, documentation |
| Stage 1 audit | 1-2 days | Documentation review (readiness) |
| Stage 2 audit | 3-10 days | Control effectiveness testing |
| Certification | After Stage 2 | 3-year certificate, annual surveillance audits |

---

## Incident Response Framework

### NIST SP 800-61 Incident Response Lifecycle

```
Preparation → Detection & Analysis → Containment, Eradication, Recovery → Post-Incident Activity
     ↑                                                                            ↓
     └────────────────────── Lessons Learned ──────────────────────────────────────┘
```

### Incident Severity Levels

| Level | Description | Response Time | Escalation |
|-------|-------------|---------------|------------|
| **P1 Critical** | Service down, data breach, active attack | 15 minutes | CIO, Legal, CEO (if breach) |
| **P2 High** | Major degradation, potential data exposure | 1 hour | IT Dir, Security Lead |
| **P3 Medium** | Limited impact, contained | 4 hours | IT Team Lead |
| **P4 Low** | Minimal impact, informational | Next business day | IT Analyst |

### Incident Response Playbook Template

```markdown
## Playbook: [Incident Type]

### Identification
- Detection sources: [SIEM alerts, user reports, monitoring]
- Key indicators: [what to look for]
- Classification criteria: [how to determine severity]

### Containment
- Immediate: [isolate affected systems]
- Short-term: [temporary workarounds]
- Evidence preservation: [what to capture]

### Eradication
- Root cause analysis: [investigation steps]
- Remediation: [fix the vulnerability]
- Validation: [confirm eradication]

### Recovery
- Restoration: [bring systems back]
- Monitoring: [enhanced monitoring period]
- Verification: [confirm normal operation]

### Communication
- Internal: [who to notify, templates]
- External: [regulatory, customers, if applicable]
- Timeline: [notification deadlines]
```

### Common Incident Types and Response

| Incident Type | Containment | Key Action |
|--------------|-------------|------------|
| Ransomware | Isolate network segment | Do NOT pay; restore from backup |
| Phishing (credential theft) | Reset credentials, check access logs | Force MFA, scan for lateral movement |
| Data breach | Identify scope, isolate source | Legal notification, forensic preservation |
| DDoS | Activate mitigation service | Traffic filtering, CDN scaling |
| Insider threat | Restrict access, monitor | HR involvement, legal counsel |
| Supply chain compromise | Isolate affected vendor connections | Assess blast radius, vendor notification |

---

## Zero Trust Architecture

### Core Principles

| Principle | Implementation |
|-----------|---------------|
| **Never trust, always verify** | Authenticate and authorize every access request |
| **Least privilege access** | Grant minimum access needed for the task |
| **Assume breach** | Design as if the perimeter is already compromised |
| **Verify explicitly** | Use all available data points (identity, device, location, behavior) |
| **Micro-segmentation** | Create granular security zones |

### Zero Trust Maturity Model (CISA)

| Pillar | Traditional | Advanced | Optimal |
|--------|-------------|----------|---------|
| **Identity** | Passwords, some MFA | MFA everywhere, SSO | Continuous verification, risk-based |
| **Devices** | Managed devices only | EDR, device health | Real-time device assessment |
| **Networks** | Perimeter-based | Macro-segmentation | Micro-segmentation, encrypted |
| **Applications** | On-prem, VPN access | Cloud-aware, SSO | Per-app authorization |
| **Data** | Perimeter protection | Classification, DLP | Automated classification, rights mgmt |

---

## Security Policy Templates

### Essential Security Policies

| Policy | Scope | Review Frequency |
|--------|-------|-----------------|
| Information Security Policy | Enterprise-wide | Annual |
| Acceptable Use Policy | All employees | Annual |
| Access Control Policy | IT systems | Annual |
| Data Classification Policy | All data | Annual |
| Incident Response Policy | IT and security teams | Semi-annual |
| Business Continuity Policy | Enterprise-wide | Annual |
| Password/Authentication Policy | All users | Annual |
| Remote Work Security Policy | Remote employees | Annual |
| Third-Party Risk Policy | Vendor management | Annual |
| Change Management Policy | IT operations | Annual |

### Policy Document Structure

```markdown
1. Purpose
2. Scope
3. Policy Statements (numbered, specific, enforceable)
4. Roles and Responsibilities
5. Compliance and Enforcement
6. Exceptions Process
7. Related Policies
8. Definitions
9. Review and Update History
```

---

## Security Metrics Dashboard

| Category | Metric | Target |
|----------|--------|--------|
| **Vulnerability** | Mean time to patch (critical) | < 72 hours |
| **Vulnerability** | % systems scanned monthly | > 95% |
| **Identity** | MFA adoption rate | > 99% |
| **Identity** | Privileged access accounts | Minimize, review quarterly |
| **Incident** | Mean time to detect (MTTD) | < 24 hours |
| **Incident** | Mean time to respond (MTTR) | < 4 hours (P1) |
| **Awareness** | Phishing simulation click rate | < 5% |
| **Compliance** | Policy compliance rate | > 95% |
| **Third-party** | Vendor risk assessments current | > 90% |

---

*Last Updated: 2026-02-14*


## Common Pitfalls

- Security framework recommendations must match regulatory requirements for the industry
- Penetration test results have a shelf life — they're point-in-time assessments
- Zero trust is an architecture philosophy, not a product — vendor-specific recommendations need justification
