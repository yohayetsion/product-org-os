# Privacy & Data Governance Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: @privacy-counsel, @compliance-officer, @general-counsel

---
<!-- Attribution:
  CCPA/LGPD and privacy policy generation sections informed by:
  - Tempest privacy-policy-generator — CCPA/CPRA, LGPD Brazil compliance patterns, privacy policy generation framework
  Adapted and expanded for Product Org OS agents.
-->

## GDPR Framework (EU General Data Protection Regulation)

### Key Principles (Article 5)

| Principle | Requirement | Practical Implication |
|-----------|------------|----------------------|
| **Lawfulness, fairness, transparency** | Process data lawfully with clear notice | Privacy policy, cookie consent, processing agreements |
| **Purpose limitation** | Collect for specified, explicit purposes | Define purposes before collection, don't repurpose |
| **Data minimization** | Adequate, relevant, limited to necessity | Only collect what you need for stated purpose |
| **Accuracy** | Keep data accurate and up to date | Data correction processes, user profile editing |
| **Storage limitation** | Keep no longer than necessary | Retention policies, automated deletion |
| **Integrity & confidentiality** | Appropriate security measures | Encryption, access controls, incident response |
| **Accountability** | Demonstrate compliance | Documentation, DPIAs, records of processing |

### Lawful Bases for Processing (Article 6)

| Basis | When to Use | Key Requirements |
|-------|------------|------------------|
| **Consent** | Marketing emails, cookies, tracking | Freely given, specific, informed, unambiguous; easy withdrawal |
| **Contract** | Providing the service user signed up for | Processing necessary for contract performance |
| **Legal obligation** | Tax records, employment law compliance | Specific legal requirement mandates processing |
| **Vital interests** | Emergency medical situations | Life-threatening situations only |
| **Public interest** | Government/public authority functions | Rarely applicable to private companies |
| **Legitimate interest** | Analytics, security, B2B marketing | Requires balancing test (LIA); document reasoning |

### Data Subject Rights (Articles 15-22)

| Right | Response Deadline | Key Considerations |
|-------|-------------------|-------------------|
| **Access** (Art. 15) | 30 days | Provide copy of all personal data + processing details |
| **Rectification** (Art. 16) | 30 days | Correct inaccurate data without undue delay |
| **Erasure** ("Right to be forgotten") (Art. 17) | 30 days | Delete when no longer necessary; exceptions exist |
| **Restriction** (Art. 18) | 30 days | Stop processing but don't delete (e.g., during dispute) |
| **Portability** (Art. 20) | 30 days | Provide data in machine-readable format |
| **Object** (Art. 21) | 30 days | Stop processing based on legitimate interest/direct marketing |
| **Automated decisions** (Art. 22) | 30 days | Right not to be subject to solely automated decisions with legal effects |

### Cross-Border Data Transfers (Chapter V)

| Mechanism | Use Case | Complexity |
|-----------|----------|-----------|
| **Adequacy decision** | Transfers to countries deemed adequate (UK, Japan, etc.) | Low |
| **Standard Contractual Clauses (SCCs)** | Most common mechanism for US/other transfers | Medium |
| **Binding Corporate Rules (BCRs)** | Intra-group transfers in multinationals | High |
| **Consent** | One-off transfers with explicit consent | Low (limited use) |
| **EU-US Data Privacy Framework** | US companies self-certified under DPF | Medium |

**SCC Requirements (Post-Schrems II)**:
1. Transfer Impact Assessment (TIA) required
2. Evaluate destination country laws
3. Implement supplementary measures if needed (encryption, pseudonymization)
4. Document and regularly review

---

## CCPA/CPRA Framework (California)

### Key Definitions

| GDPR Term | CCPA/CPRA Term | Difference |
|-----------|---------------|------------|
| Data subject | Consumer | CCPA: California residents |
| Data controller | Business | Revenue >$25M, 100K+ consumers, or 50%+ revenue from selling PI |
| Data processor | Service provider | Must have contractual restrictions |
| Personal data | Personal information (PI) | CCPA is broader — includes household data |
| Special categories | Sensitive personal information (SPI) | CPRA added SPI category |

### Consumer Rights (CCPA/CPRA)

| Right | CCPA | CPRA Addition |
|-------|------|---------------|
| Know | Yes | Extended to include SPI |
| Delete | Yes | Enhanced with exceptions |
| Opt-out of sale | Yes | Extended to "sharing" for cross-context behavioral advertising |
| Non-discrimination | Yes | Expanded |
| Correct | — | New right |
| Limit use of SPI | — | New right |
| Opt-out of automated decision-making | — | New right (regulations pending) |

### "Do Not Sell or Share" Requirements

1. "Do Not Sell or Share My Personal Information" link on homepage
2. Honor Global Privacy Control (GPC) signals
3. Respect opt-out for at least 12 months
4. No financial incentives that are unjust or coercive

---

## Other Global Privacy Laws

### Quick Reference Comparison

| Requirement | GDPR | CCPA/CPRA | LGPD (Brazil) | PIPL (China) | POPIA (S. Africa) |
|-------------|------|-----------|---------------|-------------|-------------------|
| Lawful basis required | Yes | No (opt-out model) | Yes | Yes | Yes |
| DPO required | Sometimes | No | Yes (for certain) | Yes (for certain) | Yes |
| Cross-border restrictions | Yes (SCCs/adequacy) | No (but contractual) | Yes (adequacy/consent) | Yes (security assessment) | Yes (adequacy/consent) |
| Breach notification | 72 hours | "Without unreasonable delay" | "Reasonable time" | Immediately | ASAP |
| Data subject rights | Comprehensive | Comprehensive | Comprehensive | Comprehensive | Comprehensive |
| Fines | Up to 4% global turnover | $2,500-$7,500 per violation | Up to 2% revenue | Up to 5% prior year revenue | Up to R10M |

### US State Privacy Laws (Active/Enacted)

| State | Law | Effective | Key Difference from CCPA |
|-------|-----|-----------|-------------------------|
| Virginia | VCDPA | Jan 2023 | Consent model (not opt-out) for sensitive data |
| Colorado | CPA | Jul 2023 | Universal opt-out mechanism required |
| Connecticut | CTDPA | Jul 2023 | Similar to Virginia |
| Utah | UCPA | Dec 2023 | Higher thresholds, narrower scope |
| Texas | TDPSA | Jul 2024 | No revenue threshold |
| Oregon | OCPA | Jul 2024 | Includes non-profits |
| Montana | MCDPA | Oct 2024 | Smallest state by population |
| 10+ additional states | Various | 2025-2026 | Ongoing wave of state laws |

---

## Data Protection Impact Assessment (DPIA)

### When Required (GDPR Article 35)

A DPIA is **mandatory** when processing is likely to result in **high risk** to individuals:

| Trigger | Example |
|---------|---------|
| Systematic evaluation of personal aspects (profiling) | Credit scoring, automated hiring decisions |
| Large-scale processing of special categories | Health data platform, biometric systems |
| Systematic monitoring of publicly accessible areas | CCTV, location tracking |
| New technologies | AI/ML models processing personal data |
| Cross-referencing datasets | Combining datasets from different sources |

### DPIA Template Structure

```
1. Description of Processing
   - What data, from whom, for what purpose
   - Data flows and systems involved
   - Retention periods

2. Necessity and Proportionality
   - Lawful basis
   - Why this processing is necessary
   - Could the same goal be achieved with less data?

3. Risk Assessment
   - Risks to data subjects (identity, reputation, economic)
   - Likelihood × Severity matrix
   - Consider: unauthorized access, data loss, excessive processing

4. Mitigation Measures
   - Technical measures (encryption, pseudonymization, access controls)
   - Organizational measures (policies, training, DPO oversight)
   - Residual risk assessment after mitigation

5. Consultation
   - DPO review and sign-off
   - Supervisory authority consultation if high residual risk remains
```

---

## Consent Management

### Valid Consent Checklist (GDPR Standard)

| Requirement | Implementation |
|-------------|---------------|
| **Freely given** | No bundling with service; granular choices; no detriment for refusing |
| **Specific** | Separate consent per purpose; no blanket consent |
| **Informed** | Clear language; identify controller; state purposes; mention rights |
| **Unambiguous** | Affirmative action (no pre-ticked boxes); clear opt-in |
| **Withdrawable** | Easy to withdraw as to give; mechanism provided |
| **Documented** | Record when, how, what was consented to |

### Cookie Consent Requirements

| Category | Consent Required? | Examples |
|----------|-------------------|---------|
| **Strictly necessary** | No | Session cookies, security, load balancing |
| **Functional** | Yes (GDPR) / Varies | Language preference, user settings |
| **Analytics** | Yes | Google Analytics, Mixpanel, PostHog |
| **Marketing** | Yes | Ad tracking, retargeting, social pixels |

### Consent Management Platform (CMP) Requirements

1. Banner must appear before non-essential cookies fire
2. "Reject All" must be as easy as "Accept All"
3. Granular category selection available
4. Consent stored and auditable
5. Re-consent on material changes
6. GPC/DNT signal handling

---

## Privacy by Design Principles

| Principle | In Practice |
|-----------|------------|
| **Proactive not reactive** | Build privacy into design specs, not as afterthought |
| **Privacy as default** | Default settings should be privacy-protective |
| **Privacy embedded in design** | Part of architecture, not bolt-on |
| **Full functionality** | Privacy AND functionality, not either/or |
| **End-to-end security** | Data protected throughout lifecycle |
| **Visibility & transparency** | Users can verify privacy claims |
| **Respect for user privacy** | User-centric design, strong defaults, granular controls |

---

## Data Breach Response

### Notification Timeline

| Jurisdiction | Authority Notification | Individual Notification |
|-------------|----------------------|------------------------|
| GDPR | 72 hours (Art. 33) | "Without undue delay" if high risk (Art. 34) |
| CCPA/CPRA | Varies by incident | "Most expedient time possible" |
| HIPAA | 60 days | 60 days |
| SEC (public companies) | 4 business days (Form 8-K) | As applicable |
| State laws (US) | Varies (30-60 days typical) | Varies |

### Breach Response Checklist

```
Immediate (0-24 hours):
- [ ] Contain the breach (stop data loss)
- [ ] Preserve evidence
- [ ] Activate incident response team
- [ ] Initial assessment: what data, how many affected, how it happened

Assessment (24-72 hours):
- [ ] Determine scope and severity
- [ ] Identify affected data subjects
- [ ] Assess risk to individuals
- [ ] Determine notification obligations by jurisdiction

Notification (per jurisdiction deadlines):
- [ ] Notify supervisory authorities
- [ ] Notify affected individuals (if high risk)
- [ ] Notify business partners/processors
- [ ] Consider law enforcement notification

Recovery (1-4 weeks):
- [ ] Root cause analysis
- [ ] Remediation measures
- [ ] Update security measures
- [ ] Document everything for accountability
```

---

## Records of Processing Activities (ROPA)

### Required Fields (GDPR Article 30)

| Field | Controller Record | Processor Record |
|-------|-------------------|------------------|
| Name/contact of controller/processor | Yes | Yes |
| Purposes of processing | Yes | N/A |
| Categories of data subjects | Yes | N/A |
| Categories of personal data | Yes | Yes |
| Recipients/categories of recipients | Yes | N/A |
| Transfers to third countries | Yes | Yes |
| Retention periods | Yes | N/A |
| Security measures (general description) | Yes | Yes |

---

*Last Updated: 2026-02-14*
*References: GDPR (Regulation 2016/679), CCPA (Cal. Civ. Code §1798.100-199.100), CPRA amendments, LGPD (Lei 13.709/2018), EDPB Guidelines*
*Disclaimer: This is informational guidance, not legal advice. Consult qualified legal counsel for binding decisions.*


## Common Pitfalls

- GDPR, CCPA, and other privacy frameworks have different requirements — don't conflate them
- Data processing agreements must specify data residency and cross-border transfer mechanisms
- Consent mechanisms must be active (not pre-checked boxes) under GDPR

---

## Additional Privacy Regulations

*Sources: Tempest privacy-policy-generator reference, IAPP Global Privacy Law Reference, ANPD guidance*

### CCPA/CPRA Deep Dive

#### Consumer Rights (Full Enumeration)

| Right | Description | CPRA Enhancement |
|-------|-------------|-----------------|
| **Know** | Request disclosure of PI collected, sources, purposes, third parties | Extended to sensitive PI; includes specific pieces collected |
| **Delete** | Request deletion of PI held by business and service providers | Enhanced — must flow deletion request to service providers and contractors |
| **Opt-Out of Sale/Sharing** | Stop sale of PI and sharing for cross-context behavioral advertising | CPRA added "sharing" to cover ad targeting without monetary exchange |
| **Non-Discrimination** | No penalty for exercising rights | Expanded; financial incentive programs must be reasonably related to PI value |
| **Correct** | Correct inaccurate PI (CPRA only) | New right — must correct and notify third parties |
| **Limit Use of Sensitive PI** | Restrict use of SPI to necessary purposes (CPRA only) | New right; requires "Limit the Use of My Sensitive Personal Information" link |
| **Opt-Out of Automated Decision-Making** | Pending CPPA rulemaking | Regulations in progress as of 2026 |

#### Business Obligations

| Obligation | Details |
|-----------|---------|
| **Notice at Collection** | Inform consumers at or before point of collection — categories of PI, purposes, whether PI is sold/shared |
| **Privacy Policy** | Comprehensive disclosure including all rights, categories collected/disclosed, retention periods, data sources |
| **Service Provider Contracts** | Written contract specifying prohibited uses; service providers cannot sell/share PI received |
| **Data Minimization (CPRA)** | PI collected must be reasonably necessary and proportionate to disclosed purpose |
| **Purpose Limitation (CPRA)** | PI cannot be used for purposes incompatible with disclosed context |
| **Retention Limits (CPRA)** | Retention period must be disclosed; cannot retain longer than reasonably necessary |
| **Global Privacy Control** | Must honor GPC opt-out signal as a valid opt-out of sale/sharing |
| **Response Timeline** | 45 days to respond to consumer requests (extendable 45 days with notice) |

#### Enforcement

| Mechanism | Details |
|-----------|---------|
| **AG Enforcement** | California Attorney General; civil penalties $2,500 per unintentional violation, $7,500 per intentional violation |
| **CPPA Enforcement (CPRA)** | California Privacy Protection Agency — dedicated enforcement authority; investigative and rulemaking powers |
| **Private Right of Action** | Limited to data breaches involving non-encrypted, non-redacted PI; $100–$750 per consumer per incident or actual damages |
| **Data Breach Liability** | Businesses that fail to implement reasonable security are exposed to class action without proving harm |

#### CPRA-Specific Additions

- **CA Privacy Protection Agency (CPPA)**: Independent enforcement body; rulemaking authority
- **Sensitive Personal Information (SPI)**: New category covering SSN, financial account credentials, precise geolocation, racial/ethnic origin, religious beliefs, union membership, mail/email/text content, genetic data, biometric data, health data, sex life/sexual orientation
- **Contractor category**: New to CPRA — distinct from service providers; covers those processing PI on behalf of business under written contract
- **Audit requirements (pending)**: CPPA may require cybersecurity audits and risk assessments for high-risk businesses

---

### LGPD (Lei Geral de Protecao de Dados — Brazil)

**Effective**: September 2020 | **Enforcement body**: ANPD (Autoridade Nacional de Protecao de Dados)

#### 10 Legal Bases for Processing (Article 7)

| Legal Basis | Description |
|-------------|------------|
| **Consent** | Free, informed, specific, unambiguous; withdrawal must be possible |
| **Legal obligation** | Compliance with a legal or regulatory obligation |
| **Public policy execution** | Data processing by public administration |
| **Research** | By research body; anonymization preferred |
| **Contract performance** | Necessary for executing a contract or pre-contractual steps |
| **Judicial/administrative exercise** | Exercising rights in judicial, administrative, or arbitration proceedings |
| **Vital interests** | Protection of life or physical safety |
| **Legitimate interests** | Balanced against data subject rights; must be documented |
| **Credit protection** | As established by specific legislation |
| **Health protection** | Healthcare services, epidemiological research (by health professionals) |

#### Data Subject Rights (Article 18)

| Right | Description |
|-------|------------|
| **Confirmation** | Whether processing of their data occurs |
| **Access** | Access to their data |
| **Correction** | Correct incomplete, inaccurate, or outdated data |
| **Anonymization/blocking/deletion** | Of unnecessary, excessive, or non-compliant data |
| **Portability** | Data portability to another service provider (regulation pending) |
| **Deletion of consent-based data** | Request deletion of data processed on consent basis |
| **Consent information** | Information about entities with which data was shared |
| **Denial consequences** | Information about what happens if they deny consent |
| **Consent revocation** | Revoke consent at any time |

#### DPO (Encarregado) Requirements

| Requirement | Detail |
|-------------|--------|
| **Mandatory for** | All controllers (public and private) processing personal data — no size threshold |
| **Appointment** | Must be publicly disclosed (name and contact) |
| **Role** | Accepts complaints from data subjects, communicates with ANPD, provides guidance to employees |
| **Qualifications** | No formal certification required by law, but technical expertise expected |
| **Can be external** | Third-party DPO permissible |

#### ANPD Enforcement Powers

- Issue administrative sanctions (up to 2% of company's revenue in Brazil, capped at R$50 million per violation)
- Warning notices; publication of violation; temporary blocking or deletion of data
- Partial or total suspension of activities related to data processing
- No private right of action (unlike CCPA) — enforcement is administrative

---

### Privacy Policy Generation Framework

#### Required Sections Checklist

| Section | GDPR | CCPA/CPRA | LGPD | Notes |
|---------|------|-----------|------|-------|
| Identity and contact of data controller | Required | Required | Required | Include DPO contact if applicable |
| Categories of data collected | Required | Required | Required | |
| Purposes and legal basis for processing | Required | Required | Required | GDPR requires legal basis per purpose |
| Data sources | Not required | Required | Not required | CCPA must disclose third-party sources |
| Third parties data is shared with | Required | Required | Required | |
| International transfers | Required | Not required | Required | GDPR and LGPD require safeguard descriptions |
| Retention periods | Required | Required (CPRA) | Not required | Best practice universally |
| Data subject rights | Required | Required | Required | Jurisdiction-specific rights |
| Right to withdraw consent | Required | N/A | Required | |
| Complaint/enforcement body | Required | Required | Required | Supervisory authority contact |
| Last updated date | Best practice | Best practice | Best practice | Required for re-consent tracking |

#### Language Requirements by Jurisdiction

| Jurisdiction | Requirement |
|-------------|------------|
| **GDPR** | "Concise, transparent, intelligible, and easily accessible" — plain language, no legal jargon |
| **CCPA/CPRA** | Must be readable and understandable to an average consumer |
| **LGPD** | Clear, precise, and appropriate to consumer's understanding; prior and express consent |
| **Children's data** | Enhanced clarity required globally (COPPA, GDPR Art 8, UK AADC) |

#### Policy Update Notification Requirements

| Trigger | Action Required |
|---------|----------------|
| Material change to data practices | Re-notify users; re-obtain consent if consent-based processing affected |
| New processing purposes | Must have new lawful basis; inform users |
| New categories of data | Update policy; notify at collection |
| Change in legal basis | Notify if switching from consent to legitimate interest (or vice versa) |
| **GDPR**: "without undue delay" after material changes | Direct notification preferred (email) over policy page update alone |

#### Cookie Consent Requirements (Multi-Jurisdiction)

| Regulation | Requirement |
|-----------|------------|
| **ePrivacy Directive (EU)** | Prior consent required for non-essential cookies; informational notice minimum |
| **GDPR (overlapping)** | Consent must meet GDPR standard (specific, informed, unambiguous, withdrawable) |
| **CCPA/CPRA** | Opt-out model; honor GPC; "Do Not Sell or Share" covers behavioral ad cookies |
| **LGPD** | Consent required for non-essential cookies; must be withdrawable |
| **UK PECR** | Same as ePrivacy; ICO guidance requires granular consent |

---

### Privacy Impact Assessment (PIA) Template

```
PIA Template

1. Project Overview
   - Project name, owner, date
   - Description of new processing or system change
   - Data flows: what data, from whom, to whom, stored where

2. Necessity and Proportionality
   - What is the purpose of this processing?
   - Is processing necessary to achieve that purpose?
   - Could the same goal be achieved with less/no personal data?
   - Is the volume/scope proportionate?

3. Data Subject Impact
   - Who is affected? (employees, customers, children, vulnerable groups)
   - What are the potential harms? (financial, reputational, physical, psychological)
   - Likelihood and severity of each harm (Low/Medium/High)

4. Legal Basis and Compliance
   - Lawful basis for each processing activity
   - Special category data? If yes, additional justification
   - Cross-border transfers? If yes, mechanism used
   - Conflict with existing privacy notices?

5. Risk Assessment Matrix
   | Risk | Likelihood (1-5) | Severity (1-5) | Risk Score | Mitigation |
   |------|-----------------|----------------|------------|------------|
   | Unauthorized access | [X] | [X] | [X] | [Action] |
   | Data loss/destruction | [X] | [X] | [X] | [Action] |
   | Excessive collection | [X] | [X] | [X] | [Action] |
   | Scope creep | [X] | [X] | [X] | [Action] |

6. Mitigation Measures
   - Technical controls (encryption, access control, pseudonymization)
   - Organizational controls (training, policies, contractual)
   - Residual risk after mitigation

7. Sign-off
   - DPO review: [ ] Approved / [ ] Approved with conditions / [ ] Rejected
   - Legal review: [ ] Approved
   - Supervisory authority consultation required? [ ] Yes / [ ] No
```

---

### Privacy by Design — 7 Foundational Principles (Cavoukian)

| Principle | Core Requirement | Practical Application |
|-----------|-----------------|----------------------|
| **1. Proactive not reactive; preventive not remedial** | Anticipate and prevent privacy invasions before they occur | Privacy review in design phase, not after build |
| **2. Privacy as the default setting** | Maximum privacy without user action required | Default settings = no data sharing; user must opt in to share more |
| **3. Privacy embedded into design** | Part of the system architecture, not added on | Privacy requirements in technical specifications; reviewed at code review |
| **4. Full functionality — positive-sum, not zero-sum** | Privacy AND security AND functionality; not trade-offs | "Privacy OR usability" is a false choice; find solutions that achieve both |
| **5. End-to-end security — full lifecycle protection** | Data protected from collection to deletion | Encryption at rest and in transit; secure deletion procedures |
| **6. Visibility and transparency — keep it open** | Components and operations remain visible and verifiable | Published privacy policy; accessible DPO contact; audit trail available |
| **7. Respect for user privacy — keep it user-centric** | User interests are paramount; strong privacy defaults | Granular consent controls; easy rights exercise; clear notices |

---

### Cross-Jurisdiction Compliance Matrix

| Key Dimension | GDPR (EU) | CCPA/CPRA (California) | LGPD (Brazil) |
|---------------|-----------|------------------------|---------------|
| **Model** | Rights-based (opt-in for sensitive) | Opt-out (opt-in for SPI/minors) | Rights-based (opt-in for consent) |
| **Lawful basis required** | Yes — 6 bases (Article 6) | No — opt-out of sale/sharing only | Yes — 10 bases (Article 7) |
| **DPO required** | Conditional (systematic processing, special categories, public authority) | No | Yes — all controllers |
| **Breach notification** | 72 hours to authority; "without undue delay" to individuals | Expedient to individuals; no authority requirement | Reasonable timeframe to ANPD and affected subjects |
| **Children's age** | 16 (member state can lower to 13) | 13 (COPPA); 16 for SPI (CPRA) | 18 (or parents/guardians) |
| **Private right of action** | Member state dependent; data breach | Data breach only ($100-$750/incident) | None — administrative enforcement only |
| **Fines** | Up to €20M or 4% global turnover | $2,500-$7,500 per violation | Up to 2% Brazil revenue (R$50M cap) |
| **Cross-border transfer mechanism** | SCCs, BCRs, adequacy, DPF | Contractual only (no formal mechanism) | Adequacy decisions, standard clauses, global policies |
| **Sensitive data category** | Special categories (Article 9) | Sensitive Personal Information (CPRA) | Sensitive data (Article 5, XI) |
| **Right to correction** | Article 16 | CPRA only | Article 18(III) |
| **Data portability** | Article 20 (machine-readable) | Not currently required | Regulation pending |
