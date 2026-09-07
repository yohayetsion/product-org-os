# Compliance Program Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: `compliance-officer`, `general-counsel`, `privacy-counsel`, `legal-dir`

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - Anthropic knowledge-work-plugins (github.com/anthropics/knowledge-work-plugins) — legal/compliance-check
  - US DOJ FCPA Resource Guide (2020) — 7 elements of effective compliance programs
  - EU GDPR (Regulation 2016/679) and CCPA/CPRA (California Civil Code 1798.100+) — data privacy obligations
  - HHS Office of Inspector General Compliance Program Guidance — healthcare compliance reference
  Adapted and expanded for Product Org OS agents.
-->

---

## Strategic Posture — Why an Operational Program Still Matters

Compliance is the consequence of well-run decisioning, not its purpose. See `product-org-plugin/PRINCIPLES.md` Move C ("Compliance-as-Secondary"): a product organization that runs decisions through Charters, records assumptions, and attests at the Reviewer Checklist gate naturally produces the artifacts compliance regimes require.

The operational pack below exists because the regulator-recognized vocabulary (the DOJ 7 elements, GDPR Articles, FCPA controls, HIPAA safeguards) is what auditors, supervisors, and counterparties read. The 7 elements operationalize compliance once the decisioning system has produced it; they do not substitute for it. Use this pack to translate upstream decisioning outputs into the program-management shape regulators and certifiers expect — not as a blueprint for organizing the product org around compliance.

---

## Compliance Program Framework

### The 7 Elements of an Effective Compliance Program

Based on DOJ / USSC guidance. A program with all 7 elements in place signals good faith and is the international benchmark for corporate compliance.

| Element | Description | Minimum Standard |
|---------|-------------|-----------------|
| **1. Written Policies and Procedures** | Documented standards of conduct, code of ethics, and compliance policies | Code of Conduct + policies for each material risk area; reviewed annually |
| **2. Compliance Leadership and Oversight** | Designated Chief Compliance Officer or equivalent; board/audit committee oversight | CCO reports directly to board or C-suite; regular board reporting (at least annually) |
| **3. Training and Education** | Regular compliance training for all personnel; role-specific training for high-risk functions | Annual all-hands training; role-specific training for legal, finance, sales, HR |
| **4. Reporting and Investigation** | Confidential reporting mechanism (hotline); investigation procedures; non-retaliation policy | Anonymous hotline; written investigation procedure; documented outcomes |
| **5. Monitoring and Auditing** | Ongoing monitoring of compliance controls; periodic audits | Annual risk-based audit plan; real-time monitoring for high-risk areas (payments, data) |
| **6. Discipline and Enforcement** | Consistent enforcement; discipline for violations regardless of seniority | Published discipline matrix; no exceptions for executives |
| **7. Response and Prevention** | Respond to violations; remediate; improve controls | Root cause analysis for all material violations; track remediation to closure |

---

## Regulatory Compliance Checklist by Domain

### Data Privacy — GDPR (EU/EEA)

**Scope**: Applies to any organization processing personal data of EU/EEA residents, regardless of where the organization is located.

**Key Obligations Checklist:**

| Obligation | Requirement | Status |
|------------|-------------|--------|
| **Lawful Basis** | Every processing activity must have a documented lawful basis (consent, contract, legal obligation, vital interests, public task, legitimate interests) | |
| **Privacy Notice** | Transparent, accessible notice at time of data collection; covers purposes, retention, rights, transfers | |
| **Records of Processing (ROPA)** | Maintain Article 30 record of all processing activities; update when processing changes | |
| **Data Minimization** | Collect only what is necessary for the stated purpose; no "collect it all" approach | |
| **Storage Limitation** | Define and enforce retention periods; delete or anonymize when no longer needed | |
| **Security Measures** | Technical and organizational measures appropriate to risk; documented in security policy | |
| **DPA with Processors** | Data Processing Agreement required with every vendor who processes personal data on your behalf | |
| **Breach Notification** | 72-hour notification to supervisory authority; notification to affected individuals if high risk | |
| **DPO Appointment** | Required if: public authority, large-scale systematic monitoring, or large-scale processing of special categories | |
| **Cross-Border Transfers** | Adequate safeguards required for transfers outside EU/EEA (see transfer mechanisms below) | |

**Lawful Bases — Decision Tree:**
```
Is processing necessary to perform a contract with the individual?
  → YES: Use CONTRACT basis. No need for consent.

Is processing required by law?
  → YES: Use LEGAL OBLIGATION basis.

Is processing for vital interests (life or death)?
  → YES: Use VITAL INTERESTS basis (narrow; emergency use only).

Is processing for legitimate interests of your organization or third parties?
  → YES: Conduct LIA (Legitimate Interests Assessment). Document.
  → Interests must not be overridden by individual's interests or rights.

Does none of the above apply?
  → Use CONSENT basis.
  → Consent must be freely given, specific, informed, unambiguous, withdrawable.
  → Not acceptable as lawful basis where power imbalance exists (employer/employee).
```

**DPIA (Data Protection Impact Assessment) Triggers:**
A DPIA is MANDATORY before commencing any processing that is "likely to result in a high risk":

- [ ] Systematic and extensive profiling with significant effects
- [ ] Large-scale processing of special categories (health, biometric, genetic, political, religious, ethnic)
- [ ] Systematic monitoring of publicly accessible area (CCTV at scale)
- [ ] New technologies (AI/ML, biometrics, IoT at scale)
- [ ] Processing that prevents individuals from exercising their rights
- [ ] Matching or combining datasets in a way individuals would not expect
- [ ] Processing of vulnerable individuals (children, employees, patients)

---

### Data Privacy — CCPA / CPRA (California)

**Scope**: Applies to for-profit businesses that: (1) gross revenues > $25M/year; OR (2) buy/sell/receive/share personal information of 100,000+ consumers or households; OR (3) derive 50%+ of revenues from selling/sharing personal information.

**Key Consumer Rights:**

| Right | What It Means | Response Time |
|-------|--------------|---------------|
| **Right to Know** | What categories of PI are collected, purposes, third parties shared with | 45 days (+ 45 day extension) |
| **Right to Access** | Specific pieces of PI collected about the consumer | 45 days (+ 45 day extension) |
| **Right to Delete** | Delete PI (with exceptions: legal obligation, security, repair, internal use) | 45 days (+ 45 day extension) |
| **Right to Correct** | Correct inaccurate PI (CPRA addition) | 45 days (+ 45 day extension) |
| **Right to Opt-Out** | Opt out of sale or sharing of PI for cross-context behavioral advertising | Immediate; no waiting period |
| **Right to Limit Use** | Limit use of sensitive PI to purposes disclosed at collection (CPRA) | Immediate |
| **Right to Non-Discrimination** | Cannot deny service or charge more for exercising rights | N/A — ongoing obligation |
| **Right to Data Portability** | Receive PI in portable format | 45 days (+ 45 day extension) |

**CCPA Compliance Checklist:**
- [ ] Privacy policy updated to include all required CCPA disclosures
- [ ] "Do Not Sell or Share My Personal Information" link on homepage
- [ ] Verified consumer request intake process (email, web form, toll-free number)
- [ ] Identity verification procedure for requests (prevents unauthorized access)
- [ ] Employee training on request intake and response
- [ ] Data inventory completed (what PI, sources, purposes, sharing)
- [ ] Service provider agreements updated with CCPA-compliant terms
- [ ] Opt-out signal honored (Global Privacy Control if applicable)
- [ ] Sensitive PI use limited or opt-out offered

---

### Data Processing Agreements (DPA) — Requirements and Checklist

A DPA is required under GDPR Article 28 whenever a data controller engages a processor.

**Required DPA Terms (Article 28):**

| Term | Requirement |
|------|-------------|
| **Subject matter and duration** | Clearly defined scope and term of processing |
| **Nature and purpose** | What processing is performed and why |
| **Type of personal data and data subjects** | Categories of data and individuals covered |
| **Controller's obligations and rights** | Processor acts only on documented instructions |
| **Sub-processing** | Processor must notify controller of sub-processors; controller approval required |
| **Security measures** | Processor implements appropriate technical and organizational measures |
| **Return/deletion** | Data returned or deleted at end of services at controller's choice |
| **Cooperation** | Processor assists controller with DSAR responses, DPIAs, breach notifications |
| **Audit rights** | Controller may audit processor's compliance |

**DPA Review Checklist:**
- [ ] All 8 Article 28 elements present
- [ ] Sub-processor list available and changes notified
- [ ] Processor's security standards align with controller's requirements
- [ ] Data retention and deletion timelines specified
- [ ] Breach notification timeline: processor notifies controller within 24–48 hours of discovery (not the 72-hour GDPR clock, which runs from controller's knowledge)
- [ ] Governing law and jurisdiction specified
- [ ] SCCs or other transfer mechanism incorporated if sub-processors outside EEA

---

### Data Subject Rights — Handling Procedures

```
STEP 1: INTAKE (Day 0)
  Receive request via designated channel (email, web form, phone)
  Log: Requester name, contact, request type, date received, deadline
  Deadline = 45 days from receipt (CCPA) / 1 calendar month (GDPR)

STEP 2: IDENTITY VERIFICATION (Day 0–3)
  Verify requester identity proportionate to sensitivity of data requested
  Use at least 2 data points matching your records (email + last 4 SSN, email + account details)
  Do NOT require government ID for low-sensitivity requests
  Log: Verification method, date verified

STEP 3: DATA SEARCH (Day 3–20)
  Search all systems: CRM, marketing tools, support system, databases, backups, email
  Engage system owners to confirm search completeness
  Document search scope and results

STEP 4: FULFILL OR DENY (Day 20–45)
  Fulfill: Provide response in required format (portable for access, deletion confirmation, etc.)
  Deny: Only if exception applies; provide denial reason and right to appeal/complaint
  Partial fulfill: Where exceptions apply to some data; explain which data is excluded and why

STEP 5: LOG AND CLOSE (Day 45)
  Update request log with outcome and date fulfilled
  Retain record for audit purposes (minimum 24 months)
```

---

### Cross-Border Data Transfer Mechanisms

For transfers of personal data from the EU/EEA to third countries without an adequacy decision:

| Mechanism | How It Works | When to Use |
|-----------|-------------|-------------|
| **Standard Contractual Clauses (SCCs)** | EC-approved contract terms incorporated into data transfer agreements | Most common; required for all transfers without adequacy; updated 2021 SCCs are current |
| **Adequacy Decision** | EC has declared the recipient country's laws provide adequate protection | Transfers to UK (post-Brexit adequacy), Switzerland, Japan, South Korea, others |
| **Binding Corporate Rules (BCRs)** | Intra-group transfer mechanism approved by lead DPA | Only for transfers within a corporate group; requires DPA approval (lengthy process) |
| **Derogations (Article 49)** | Specific limited exceptions (consent, contract performance, public interest) | Narrow; not for systematic transfers; last resort |
| **Adequacy for UK (IDTA)** | International Data Transfer Agreement for UK GDPR post-Brexit | UK → EU transfers or EU → UK on UK GDPR basis |

**SCC Selection Guide (2021 SCCs):**
```
Controller → Processor:    Module 2 (most common for SaaS vendors)
Controller → Controller:   Module 1 (data sharing between independent controllers)
Processor → Processor:     Module 3 (sub-processing)
Processor → Controller:    Module 4 (unusual; processor sends data back to non-EU controller)
```

---

## Industry-Specific Compliance

### Technology / SaaS Companies

| Area | Key Regulations | Core Obligations |
|------|----------------|-----------------|
| **Data Privacy** | GDPR, CCPA/CPRA, LGPD (Brazil), PIPL (China), PIPEDA (Canada) | Privacy program, DSARs, DPAs, breach notification |
| **Cybersecurity** | SOC 2, ISO 27001, NIST CSF | Annual audit, pen testing, incident response plan |
| **AI / Algorithmic** | EU AI Act (2026), NYC Local Law 144 (hiring algorithms) | Risk classification, transparency, human oversight for high-risk AI |
| **Payments** | PCI-DSS | Card data security; don't store CVV; tokenize where possible |
| **Accessibility** | ADA (US), WCAG 2.1 AA, EAA (EU) | Web accessibility compliance; audit annually |

### Financial Services

| Area | Key Regulations | Core Obligations |
|------|----------------|-----------------|
| **AML / KYC** | BSA (US), AMLD6 (EU), FATF standards | Customer due diligence, SAR filing, transaction monitoring |
| **Securities** | SEC, FINRA, MiFID II (EU) | Record-keeping, reporting, suitability, best execution |
| **Consumer Protection** | CFPB (US), Consumer Duty (UK FCA) | Fair dealing, transparent fees, complaints handling |
| **Data** | GLBA (US), DORA (EU) | Financial data privacy; cyber resilience for financial infrastructure |

### Healthcare

| Area | Key Regulations | Core Obligations |
|------|----------------|-----------------|
| **Privacy** | HIPAA Privacy Rule, HITECH | PHI protection, minimum necessary, notice of privacy practices |
| **Security** | HIPAA Security Rule | Administrative, physical, technical safeguards for ePHI |
| **Breach Notification** | HIPAA Breach Notification Rule | 60-day notification to HHS + affected individuals for breaches of unsecured PHI |
| **Vendor** | HIPAA BAA required | Business Associate Agreement with every vendor who handles PHI |

---

## Compliance Risk Assessment Methodology

Run annually (or when material regulatory or business changes occur).

### Step 1: Identify the Risk Universe

For each business unit and function, identify:
- Applicable regulations (by geography, industry, activity)
- Internal policies and standards
- Contractual compliance obligations

### Step 2: Score Each Risk

Rate each identified compliance risk on two dimensions:

| Dimension | 1 (Low) | 2 (Medium) | 3 (High) | 4 (Critical) |
|-----------|---------|------------|----------|--------------|
| **Likelihood** | Rare (< once in 5 years) | Possible (once in 2–5 years) | Likely (annually) | Almost certain (multiple times/year) |
| **Impact** | Minor fine / internal only | Regulatory sanction, manageable | Material fine, reputational damage | Existential (criminal, license revocation) |

**Risk Score = Likelihood × Impact**

| Score | Zone | Action |
|-------|------|--------|
| 1–2 | Green — Low | Monitor; standard controls |
| 3–4 | Yellow — Medium | Enhance controls; assign owner |
| 6–8 | Orange — High | Priority remediation; board visibility |
| 9–16 | Red — Critical | Immediate escalation; CCO + GC + CEO |

### Step 3: Evaluate Control Effectiveness

For each high/critical risk, assess existing controls:

| Control Maturity | Definition |
|-----------------|------------|
| **Absent** | No control in place |
| **Ad hoc** | Control exists informally; not documented or consistently applied |
| **Defined** | Control is documented and consistently applied |
| **Managed** | Control is monitored; metrics tracked; exceptions reported |
| **Optimized** | Control is automated or built into processes; continuously improved |

**Residual Risk = Inherent Risk adjusted for Control Maturity**

### Step 4: Prioritize and Plan

Rank residual risks by score. For top 10:
- Assign owner (named individual, not a team)
- Define remediation action
- Set deadline
- Define success metric
- Track monthly to CCO; quarterly to board/audit committee

---

## Compliance Monitoring and Testing Program

### Monitoring vs. Auditing

| | Monitoring | Auditing |
|--|------------|---------|
| **Frequency** | Continuous / real-time | Periodic (annual or ad hoc) |
| **Who** | Compliance team (first/second line) | Internal audit or external (third line) |
| **Focus** | Are controls working day-to-day? | Comprehensive evaluation of design AND effectiveness |
| **Output** | Alerts, dashboards, exception reports | Audit findings, management letter |

### Monitoring Program Design

For each high/critical compliance area, define:

```
MONITORING CONTROL CARD

Risk Area:       [e.g., GDPR Article 13 Privacy Notice Compliance]
Control:         [e.g., All web forms display current privacy notice at point of collection]
Monitoring Method: [e.g., Automated scan of web forms monthly; manual QA sample quarterly]
Frequency:       [Monthly automated + quarterly manual]
Owner:           [Name / role]
Threshold:       [What triggers an exception? e.g., any form missing notice link]
Escalation:      [What happens when exception is found? Who is notified?]
Evidence:        [What is retained as proof of monitoring? e.g., scan report + screenshot log]
```

### Testing Plan (Annual)

| Quarter | Focus Area | Method |
|---------|------------|--------|
| Q1 | Data privacy controls (DSAR response, consent records, DPAs) | File review + process walkthrough |
| Q2 | Information security (access controls, encryption, incident response) | Technical testing + tabletop exercise |
| Q3 | Third-party / vendor compliance (DPAs, contractual compliance clauses) | Contract review + vendor questionnaire sample |
| Q4 | Training compliance (completion rates, attestations) + policy currency | LMS report review + policy review |

---

## Incident Response for Compliance Violations

```
HOUR 0–4: CONTAIN AND ASSESS
  └── Identify and stop the violation or breach
  └── Preserve evidence (do not delete logs or communications)
  └── Notify CCO and GC immediately
  └── Assemble incident response team

DAY 1: INITIAL ASSESSMENT
  └── Scope: What happened? What data/systems/processes are affected?
  └── Severity: What is the potential regulatory exposure?
  └── Notification obligation: Is regulatory or individual notification required? By when?
  └── Legal privilege: Engage external counsel if criminal or material civil risk

DAY 1–3: NOTIFICATION DECISIONS
  └── GDPR breach: 72 hours to supervisory authority if likely risk to individuals
  └── CCPA breach: No fixed regulatory timeline; civil action risk
  └── HIPAA breach: HHS within 60 days; individuals within 60 days; annual report for small breaches
  └── Securities: Material events require prompt disclosure (SEC 8-K within 4 business days for material cybersecurity)

DAY 1–30: INVESTIGATION AND REMEDIATION
  └── Root cause analysis (5 Whys or equivalent)
  └── Control gap identified and remediated
  └── Process changes documented
  └── Training provided to affected personnel

DAY 30–90: CLOSURE
  └── Final incident report (timeline, impact, root cause, remediation)
  └── Board / audit committee briefing if material
  └── Lessons learned incorporated into compliance program
  └── Update risk assessment to reflect new control state
```

---

## Training Program Design

### Training Matrix

| Audience | Frequency | Topics | Format |
|----------|-----------|--------|--------|
| All employees | Annual | Code of Conduct, anti-bribery/corruption, data privacy basics, reporting obligations | Online module (30–45 min) |
| New hires | Within 30 days | All of above + role-specific | Online module + live onboarding |
| Sales, BD, partnerships | Annual + upon hire | Anti-corruption, gifts & entertainment, FCPA/UK Bribery Act | Online + scenario-based |
| Finance, accounting | Annual + upon hire | Anti-money laundering, expense policy, financial controls | Online + case study |
| Engineering, product | Annual + upon hire | Data privacy (technical), security policies, vulnerability disclosure | Online + technical workshop |
| Legal, HR, Compliance | Annual + as regulations change | Role-specific advanced training; regulatory updates | Live seminar + self-study |
| Board / Audit Committee | Annual | Program overview, high-risk areas, benchmark vs. peers | In-person briefing |
| Third parties (high-risk) | Upon engagement + upon material change | Anti-corruption, data privacy | Online certification |

### Training Effectiveness Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Completion rate | > 95% all employees | LMS report |
| Assessment pass rate (first attempt) | > 80% | LMS assessment data |
| Phishing simulation click rate | < 5% (mature program) | Phishing simulation platform |
| Time to complete annual training | < 60 days from assignment | LMS report |
| Training-related hotline reports | Track trend (not a specific target) | Hotline log cross-referenced to training |

---

## Third-Party Due Diligence Framework

### Risk-Tiered Approach

| Tier | Profile | Due Diligence Level |
|------|---------|---------------------|
| **Tier 1 — High Risk** | Agents, intermediaries, JV partners in high-risk jurisdictions; large payments; public procurement interface | Enhanced DD: ownership verification, sanctions screening, integrity check, senior management approval |
| **Tier 2 — Medium Risk** | Vendors with data access, financial intermediaries, strategic partners | Standard DD: ownership, sanctions screening, compliance questionnaire, contract compliance terms |
| **Tier 3 — Low Risk** | Commodity suppliers, standard SaaS tools without data access, routine services | Basic DD: sanctions screening, standard contract terms |

### Third-Party Due Diligence Checklist (Standard — Tier 2)

- [ ] Entity verification (registration, ownership, beneficial ownership for Tier 1)
- [ ] Sanctions screening: OFAC SDN list, EU Consolidated Sanctions, UN Sanctions, HM Treasury
- [ ] PEP (Politically Exposed Person) screening for Tier 1
- [ ] Adverse media search (last 3 years)
- [ ] Compliance questionnaire returned and reviewed
- [ ] Data processing agreement executed (if applicable)
- [ ] Anti-corruption / FCPA / UK Bribery Act representation in contract
- [ ] Right to audit clause in contract (Tier 1 and 2)
- [ ] Annual re-screening for ongoing relationships (Tier 1: quarterly)

---

## Compliance Reporting Structure

### Board / Audit Committee Reporting (Annual Minimum)

Required content for each annual compliance report to the board:

```
1. PROGRAM OVERVIEW
   - Structure and staffing of compliance function
   - Budget vs. prior year
   - Key regulatory changes since last report

2. RISK LANDSCAPE
   - Top 5 compliance risks (current risk assessment)
   - Changes from prior year (new risks, resolved risks)
   - Industry / sector regulatory developments

3. PROGRAM EFFECTIVENESS
   - Training completion rates
   - Monitoring and audit findings summary
   - Hotline activity (volume, categories, resolution rates)
   - Key performance metrics vs. benchmarks

4. INCIDENTS AND VIOLATIONS
   - Material incidents in the period (summary; details in executive session)
   - Regulatory actions, investigations, inquiries
   - Remediation status

5. LOOKING AHEAD
   - Regulatory changes requiring program updates
   - Areas for investment or improvement
   - Commitments and resource requests
```

### Management Reporting (Quarterly)

- Hotline call volume and trending categories
- Training completion by department
- Open audit findings by age and owner
- Third-party screening results
- Regulatory inquiry / examination updates
- Key risk indicators (KRIs) vs. thresholds

---

## Whistleblower / Hotline Program Design

### Program Requirements

| Element | Standard |
|---------|----------|
| **Channels** | Phone hotline (toll-free) + web form. Anonymous option mandatory. |
| **Availability** | 24/7/365. Multiple languages for international organizations. |
| **Third-party administrator** | Preferred for anonymity (Navex Global, NAVEX EthicsPoint, Lighthouse, etc.). In-house is acceptable for small organizations with strong controls. |
| **Non-retaliation policy** | Published, prominently communicated, includes retaliation as a compliance violation subject to discipline. |
| **Intake logging** | Every report logged with: date, channel, category, summary, anonymity flag. |
| **Acknowledgment** | Reporter acknowledged within 5 business days (if contact info provided). |
| **Investigation** | Written investigation procedure; outcome documented; reporter informed of outcome (if not anonymous). |
| **Records** | Retain all hotline reports and investigation records for minimum 7 years. |

### EU Whistleblower Directive Compliance (EU Directive 2019/1937)

Required for EU entities with 50+ employees (effective since December 2023 for entities with 50–249 employees):

- [ ] Internal reporting channel established
- [ ] Designated person for receiving reports
- [ ] Acknowledgment within 7 days
- [ ] Follow-up feedback within 3 months
- [ ] Anonymous reporting option
- [ ] Non-retaliation protections in place and communicated
- [ ] Records of reports maintained with appropriate confidentiality

---

## Compliance Metrics and KPIs

### Program Maturity Metrics

| KPI | Definition | Benchmark (Mature Program) |
|----|------------|---------------------------|
| Training completion rate | % employees completing annual training within 60 days | > 95% |
| Policy currency | % policies reviewed within last 12 months | 100% |
| Risk assessment currency | Months since last full risk assessment | < 12 months |
| Third-party screening coverage | % active Tier 1/2 vendors screened in last 12 months | 100% |
| Open audit findings (> 90 days) | # of findings open beyond agreed remediation date | 0 critical; < 5 high |
| Hotline reports per 1,000 employees | Industry benchmark indicator of program awareness | 1.5–3.5 (NAVEX benchmark) |
| Substantiation rate | % of hotline reports substantiated after investigation | Track trend; wide variance by org |
| Time to close investigations | Average days from report to final determination | < 45 days for standard; < 90 days for complex |

---

## Regulatory Change Management Process

Regulations change. A compliance program that doesn't adapt creates gaps.

```
STEP 1: MONITOR
  Sources: Regulatory agency websites, legal subscriptions (Lexology, Practical Law),
           industry associations, external counsel alerts, government registers.
  Owner: CCO with input from external counsel for each key jurisdiction.
  Frequency: Weekly scan; monthly summary to compliance team.

STEP 2: ASSESS IMPACT
  For each material regulatory change:
  - Which business units / processes / systems are affected?
  - What is the compliance deadline?
  - What is the gap between current practice and new requirement?
  - What is the implementation effort (low / medium / high)?

STEP 3: PRIORITIZE
  Triage by: (a) mandatory deadline, (b) enforcement risk, (c) business impact.
  Regulatory requirements with enforcement dates are non-negotiable.
  Build into compliance roadmap and resource plan.

STEP 4: IMPLEMENT
  Assign cross-functional team: Legal, IT, product, operations as needed.
  Update: Policies, procedures, training, systems, contracts, notices.
  Test controls before deadline.

STEP 5: COMMUNICATE AND TRAIN
  Communicate changes to affected staff before effective date.
  Update training content.
  Re-train if change is material.

STEP 6: VERIFY AND CLOSE
  Confirm implementation by deadline.
  Document in compliance program record.
  Update risk register to reflect new control state.
```

---

## Audit Preparation Checklist

Use before any regulatory examination, external audit, or internal audit of the compliance program.

### 30 Days Before

- [ ] Confirm audit scope and document requests received
- [ ] Assign internal coordinator (single point of contact for auditors)
- [ ] Brief relevant team members on scope and process
- [ ] Begin document collection and organization
- [ ] Conduct internal pre-audit walkthrough of key controls
- [ ] Identify any known gaps; prepare remediation plans

### 2 Weeks Before

- [ ] Document repository ready (organized by request category)
- [ ] Key personnel briefed on audit process and interview protocol
- [ ] Interview preparation for any personnel likely to be interviewed
- [ ] Legal counsel engaged for scope and privilege questions
- [ ] Logistical arrangements confirmed (secure data room, interview schedule)

### During Audit

- [ ] All document requests fulfilled within agreed timelines
- [ ] Track every document provided (description, date, who provided)
- [ ] Brief legal counsel on all material findings in real time
- [ ] Maintain daily log of auditor activity and requests
- [ ] Escalate material findings to CCO and GC immediately

### After Audit

- [ ] Receive preliminary findings; review carefully
- [ ] Respond to factual errors within stated response window
- [ ] Develop remediation plan for substantiated findings
- [ ] Incorporate findings into ongoing compliance program
- [ ] Update risk assessment and training as needed
- [ ] Retain all audit documentation for minimum 7 years
