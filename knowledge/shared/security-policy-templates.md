# Security Policy Templates Knowledge Pack

**Version**: 1.0
**Primary Users**: `it-security-policy`, `cio`, `compliance-officer`, `security-architect`
**Domain**: Enterprise Security Policy Design & Governance

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - JupiterOne/security-policy-templates (github.com/JupiterOne/security-policy-templates) — security policy structures
  - securitytemplates/sectemplates (github.com/securitytemplates/sectemplates) — security document templates
  Adapted and expanded for Product Org OS agents.
-->

## Information Security Policy (ISP)

The ISP is the master policy that establishes the organization's security posture and governs all subordinate policies.

### Structure

| Section | Purpose |
|---------|---------|
| **Purpose & Scope** | Why the policy exists, who/what it covers (employees, contractors, systems, data) |
| **Policy Statement** | Executive-level declaration of commitment to information security |
| **Roles & Responsibilities** | CISO, IT Security, Data Owners, Custodians, All Users |
| **Risk Management Approach** | Risk appetite statement, risk assessment methodology reference |
| **Compliance Requirements** | Applicable laws, regulations, contractual obligations |
| **Policy Framework** | Hierarchy of policies, standards, procedures, guidelines |
| **Enforcement & Sanctions** | Consequences of non-compliance, disciplinary process |
| **Review & Maintenance** | Annual review cycle, change triggers, approval authority |

### Key Elements

- Signed by CEO or board-level executive (not just CISO)
- References all subordinate policies by name
- Includes scope exceptions process
- States the organization's risk tolerance in qualitative terms
- Defines "information asset" broadly (data, systems, people, processes)

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.5.1 Information Security Policies |
| SOC 2 | CC1.1 COSO Principle 1 (Control Environment) |
| NIST CSF | GV.PO Policy |
| HIPAA | 164.316(a) Policies and Procedures |
| PCI DSS | Requirement 12 (Information Security Policy) |

---

## Acceptable Use Policy (AUP)

Defines permitted and prohibited use of organizational IT resources by employees, contractors, and third parties.

### Structure

| Section | Purpose |
|---------|---------|
| **Scope** | All users of organizational IT resources, including remote and BYOD |
| **Ownership of Resources** | Organization owns all systems, data, and communications on its network |
| **Permitted Use** | Business use, limited personal use boundaries |
| **Prohibited Activities** | Illegal activity, unauthorized software, circumventing controls, harassment |
| **Email & Communications** | Business communication standards, no expectation of privacy |
| **Internet Use** | Allowed categories, blocked categories, streaming/bandwidth limits |
| **Social Media** | Personal vs. corporate accounts, disclosure requirements |
| **Monitoring Statement** | Organization's right to monitor, log, and audit all activity |
| **Personal Devices** | BYOD boundaries, separation of personal/corporate data |
| **Acknowledgment** | Signature requirement, annual re-acknowledgment |

### Key Elements

- Written in plain language (not legalese) so all employees understand
- Explicit monitoring disclosure (legal requirement in many jurisdictions)
- Clear distinction between "must not" (prohibited) and "should not" (discouraged)
- Covers both on-premises and remote/cloud usage
- Annual acknowledgment requirement tied to HR onboarding

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.5.10 Acceptable Use of Information |
| SOC 2 | CC1.4 COSO Principle 4 (Competence Commitment) |
| NIST CSF | PR.AT Awareness and Training |
| HIPAA | 164.310(b) Workstation Use |
| PCI DSS | Requirement 12.3 (Usage Policies) |

---

## Access Control Policy

Governs how access to information systems and data is granted, reviewed, and revoked.

### Structure

| Section | Purpose |
|---------|---------|
| **Access Control Model** | RBAC, ABAC, or hybrid approach |
| **Principle of Least Privilege** | Users receive minimum access required for their role |
| **Account Lifecycle** | Provisioning, modification, suspension, termination |
| **Privileged Access Management** | Admin accounts, break-glass procedures, session recording |
| **Access Reviews** | Quarterly review cadence, attestation process, recertification |
| **Segregation of Duties** | Conflicting roles that cannot be combined (approve + execute) |
| **Remote Access** | VPN, zero-trust access, conditional access policies |
| **Service Accounts** | Non-human account management, credential rotation, ownership |
| **Third-Party Access** | Vendor access provisioning, time-bound access, monitoring |
| **Emergency Access** | Break-glass procedures, post-incident review requirements |

### Key Elements

- Access request workflow with approval chain (manager + data owner)
- Automated deprovisioning within 24 hours of termination
- Privileged accounts separate from daily-use accounts
- Service account inventory with assigned human owners
- Quarterly access reviews with evidence retention

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.5.15-5.18 Access Control, A.8.2-8.5 Authentication |
| SOC 2 | CC6.1-6.3 Logical and Physical Access |
| NIST CSF | PR.AA Identity Management, Authentication, Access Control |
| HIPAA | 164.312(a) Access Control |
| PCI DSS | Requirement 7 (Restrict Access), Requirement 8 (Identify Users) |

---

## Governing AI Agents as a Policy Principal Class

**Adapted from**:
  - Security Boulevard — "The Rule of 17: AI Agent Growth and Security Risk in 2026" (securityboulevard.com, 2026-06-24)
  - Help Net Security / Delinea — "The rise of machine identities and agentic AI: Securing trust in the next era of digital autonomy" (helpnetsecurity.com, 2026-06-16)
**Source licence**: press materials, no OSS license; referenced by concept, no proprietary content reproduced.
**V2V refinements**:
- Scoped strictly to the *written-policy* layer: how an enterprise's AUP and Access Control Policy must name AI agents as a distinct principal class. Identity/auth *mechanics* are deliberately out of scope and pointer-hopped.
- Mapped agent-principal obligations onto the existing AUP / Access Control Policy / Account Lifecycle templates above rather than inventing a parallel policy.

*Added 2026-06-25. **POLICY-LAYER ONLY.***

### Why This Section Exists

Through mid-2026 the identity-security market moved decisively to treat AI agents as a governed principal distinct from both humans and traditional service accounts (vendor consolidation around non-human and agent identity was the visible signal). The *policy* implication for an IT organization is narrow but real: most AUP and Access Control Policy templates name only "users" (human) and "service accounts." An autonomous AI agent is neither — it acts with intent like a user but has no human at the wheel for the in-flight action. Policy must name it explicitly, or agent access falls into an ungoverned gap.

> **Hard anti-duplication pointer.** This section governs *policy wording*, not *mechanism*. The identity, authentication, capability-scoping, and federation **mechanics** for AI agents live in `agent-identity.md` (workload-vs-user-vs-agent identity, capability tokens, IdP integration) and the agent **threat model / defensive controls** live in `agentic-security.md`. Do **not** re-author identity mechanisms here. This pack only extends the policy templates to name the principal and assign its obligations.

### Extending the AUP

Add an "Autonomous Agents" clause to the Acceptable Use Policy that states: AI agents acting on organizational systems are subject to the AUP as principals; each agent has a named accountable human owner; an agent's permitted-use scope is explicitly enumerated (no implicit inheritance of its operator's full access).

### Extending the Access Control Policy (Agent Principal Obligations)

| Obligation | Policy Statement |
|------------|------------------|
| **Named human owner** | Every AI agent principal has a single accountable human owner of record, recorded in the access register alongside service-account owners. |
| **Least-privilege scope** | An agent is granted the minimum capability required for its defined task, scoped narrower than (never equal to) its operator's full access by default. |
| **Lifecycle (joiner/mover/leaver for agents)** | Agents are provisioned, modified, and **deprovisioned** under the same Account Lifecycle procedure as humans — including prompt revocation when the agent is retired or its owner leaves. Orphaned agents are a deprovisioning failure, not a tolerated state. |
| **Audit logging** | Every agent action is logged as an attributable event distinct from the underlying service account, sufficient to answer "which agent did this, on whose authority." |
| **Access review inclusion** | Agent principals are included in the quarterly privileged-access review, with the same evidence-retention bar as privileged human accounts. |

### Key Elements

- Policy names AI agents as a distinct principal class — not folded silently into "service accounts."
- Each agent maps to one accountable human owner; no ownerless agents in production.
- Agent scope is least-privilege and enumerated; deprovisioning is in-scope and time-bound.
- Agent actions are individually attributable in logs and included in access reviews.

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.5.15-5.18 Access Control (extended to non-human/agent principals), A.8.2 Privileged Access |
| SOC 2 | CC6.1-6.3 Logical Access (agent principals in scope) |
| NIST CSF | PR.AA Identity Management & Access Control (non-human identities) |

---

## Data Classification Policy

Establishes a taxonomy for categorizing information assets by sensitivity and defines handling requirements for each level.

### Classification Levels

| Level | Definition | Examples | Handling Requirements |
|-------|-----------|----------|---------------------|
| **Public** | Information approved for external release | Marketing materials, press releases, public filings | No restrictions on sharing; review before publication |
| **Internal** | General business information not for external parties | Org charts, internal memos, meeting notes, non-sensitive reports | Share within organization; no external distribution without approval |
| **Confidential** | Sensitive business information requiring protection | Financial data, customer lists, contracts, strategic plans, source code | Encrypt in transit and at rest; need-to-know access; NDA for external sharing |
| **Restricted** | Highest sensitivity; regulatory or critical business impact if disclosed | PII/PHI, payment card data, trade secrets, credentials, encryption keys | Strict access controls; full encryption; DLP monitoring; no removable media; audit logging |

### Structure

| Section | Purpose |
|---------|---------|
| **Classification Scheme** | The four levels with definitions and examples |
| **Data Owner Responsibilities** | Assign classification, review periodically, approve access |
| **Labeling Requirements** | How documents, files, emails are marked by classification |
| **Handling Procedures** | Storage, transmission, printing, discussion rules per level |
| **Declassification** | When and how data moves to a lower classification |
| **Breach Implications** | Incident severity mapping by classification level |

### Key Elements

- Default classification is "Internal" if not explicitly classified
- Data owners (business function heads) assign classification, not IT
- Classification applies to data in all forms: digital, physical, verbal
- Labeling is mandatory for Confidential and Restricted
- Classification review triggered by business changes, not just calendar

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.5.12-5.14 Information Classification, Labeling, Transfer |
| SOC 2 | CC6.7 Restriction of Data in Transmission/Storage |
| NIST CSF | ID.AM Asset Management, PR.DS Data Security |
| HIPAA | 164.312(e) Transmission Security, 164.312(a) Access Control |
| PCI DSS | Requirement 3 (Protect Stored Account Data), Requirement 4 (Encrypt Transmission) |

---

## Password and Authentication Policy

Defines requirements for credentials, multi-factor authentication, and identity verification.

### Structure

| Section | Purpose |
|---------|---------|
| **Password Requirements** | Minimum length (14+ characters), complexity or passphrase guidance |
| **Multi-Factor Authentication** | Where MFA is required (all external, privileged, sensitive systems) |
| **Passwordless Authentication** | FIDO2/WebAuthn, biometrics, certificate-based auth strategy |
| **Password Storage** | Hashing algorithms (bcrypt, Argon2), salting, no plaintext storage |
| **Credential Rotation** | Rotation cadence for service accounts, no forced rotation for user passwords with MFA |
| **Account Lockout** | Lockout threshold (5-10 attempts), lockout duration, progressive delay |
| **Single Sign-On** | SSO integration requirements, IdP standards (SAML, OIDC) |
| **Shared Accounts** | Prohibition of shared credentials, exceptions process |
| **Password Managers** | Approved tools, enterprise deployment requirements |

### Key Elements

- NIST 800-63B aligned: favor length over complexity, eliminate periodic rotation for users
- MFA required for all external-facing applications and privileged access
- Hardware security keys (FIDO2) for highest-risk accounts
- Password manager required; browser-saved passwords prohibited for corporate accounts
- Service account credentials rotated every 90 days minimum

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.8.2-8.5 Authentication Information |
| SOC 2 | CC6.1 Logical Access Security |
| NIST CSF | PR.AA-3 Authentication |
| HIPAA | 164.312(d) Person or Entity Authentication |
| PCI DSS | Requirement 8 (Identify and Authenticate Access) |

---

## Incident Response Policy

Establishes the framework for detecting, responding to, containing, and recovering from security incidents.

### Structure

| Section | Purpose |
|---------|---------|
| **Incident Definition & Classification** | What constitutes an incident; severity levels (P1-P4) |
| **Incident Response Team** | CSIRT composition, roles, contact information, on-call rotation |
| **Detection & Reporting** | How incidents are identified, reporting channels, mandatory reporting |
| **Triage & Classification** | Initial assessment, severity assignment, escalation criteria |
| **Containment** | Short-term containment (isolate), long-term containment (patch/rebuild) |
| **Eradication** | Root cause removal, malware cleanup, vulnerability remediation |
| **Recovery** | System restoration, monitoring for recurrence, return to operations |
| **Post-Incident Review** | Lessons learned, timeline reconstruction, improvement actions |
| **Communication Plan** | Internal notifications, external notifications, regulatory reporting |
| **Evidence Preservation** | Chain of custody, forensic imaging, log retention |

### Severity Matrix

| Severity | Definition | Response Time | Escalation |
|----------|-----------|---------------|------------|
| **P1 - Critical** | Active data breach, ransomware, system-wide compromise | 15 minutes | CISO, CEO, Legal, Board |
| **P2 - High** | Confirmed intrusion, significant data exposure risk | 1 hour | CISO, IT Director |
| **P3 - Medium** | Suspicious activity, policy violation with limited impact | 4 hours | Security team lead |
| **P4 - Low** | Minor policy violation, failed attack attempt | Next business day | Security analyst |

### Key Elements

- 24/7 incident reporting mechanism (hotline, email, chat)
- Mandatory reporting for all suspected incidents (no self-triage by end users)
- Regulatory notification timelines documented (GDPR 72 hours, state breach laws, PCI)
- Tabletop exercises conducted quarterly with executive participation
- Post-incident review within 5 business days of incident closure
- Retainer agreement with external forensics firm for P1/P2 incidents

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.5.24-5.28 Incident Management |
| SOC 2 | CC7.3-7.5 Monitoring, Response, Recovery |
| NIST CSF | RS.MA Incident Management, RS.AN Analysis, RS.MI Mitigation |
| HIPAA | 164.308(a)(6) Security Incident Procedures |
| PCI DSS | Requirement 12.10 (Incident Response Plan) |

---

## Business Continuity and Disaster Recovery Policy

Ensures the organization can maintain critical operations during disruptions and recover from disasters.

### Structure

| Section | Purpose |
|---------|---------|
| **Business Impact Analysis (BIA)** | Identify critical processes, RPO/RTO per system tier |
| **Recovery Tiers** | System classification by criticality (Tier 1-4) |
| **Backup Requirements** | Backup frequency, retention, encryption, offsite storage |
| **Recovery Procedures** | Runbooks per system tier, failover processes |
| **Testing Requirements** | Annual DR test, quarterly backup restoration test |
| **Crisis Communication** | Communication tree, stakeholder notification, media handling |
| **Alternate Processing** | Hot/warm/cold site requirements, cloud failover |
| **Plan Maintenance** | Annual review, update triggers, distribution list |

### Recovery Tier Matrix

| Tier | Criticality | RTO | RPO | Example Systems |
|------|-------------|-----|-----|-----------------|
| **Tier 1** | Mission-critical | < 1 hour | < 15 minutes | Payment processing, auth systems, primary database |
| **Tier 2** | Business-critical | < 4 hours | < 1 hour | ERP, CRM, email, collaboration tools |
| **Tier 3** | Important | < 24 hours | < 4 hours | Reporting, analytics, development environments |
| **Tier 4** | Non-critical | < 72 hours | < 24 hours | Archive systems, training platforms |

### Key Elements

- BIA reviewed annually or when significant business changes occur
- Backups tested for restorability (not just completion)
- Geographic diversity for backup storage (different region/zone)
- Documented succession plan for key personnel
- Third-party dependencies mapped with their DR capabilities

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.5.29-5.30 Business Continuity, A.8.13-8.14 Backup, Redundancy |
| SOC 2 | A1.1-A1.3 Availability |
| NIST CSF | RC.RP Incident Recovery Plan |
| HIPAA | 164.308(a)(7) Contingency Plan |
| PCI DSS | Requirement 12.10.1 (Incident Response Plan) |

---

## Remote Work / BYOD Security Policy

Governs security requirements for remote work arrangements and personal device use.

### Structure

| Section | Purpose |
|---------|---------|
| **Eligible Devices** | Corporate-issued vs. personal devices, minimum hardware requirements |
| **Device Enrollment** | MDM/UEM enrollment requirements, compliance checks |
| **Network Security** | VPN requirements, prohibited networks (public Wi-Fi without VPN) |
| **Data Handling** | No local storage of Restricted data on BYOD, containerization |
| **Physical Security** | Screen lock, clean desk, secure storage at home office |
| **Application Controls** | Approved app list, no sideloading, automatic updates |
| **Monitoring & Privacy** | What the organization monitors on BYOD vs. corporate devices |
| **Lost/Stolen Device** | Reporting timeline (immediate), remote wipe capability, personal data impact |
| **Offboarding** | Corporate data removal, MDM unenrollment, personal data preservation |

### Key Elements

- Clear distinction between corporate and BYOD security requirements
- Containerization (work profile) mandatory on personal devices
- Organization retains right to remote wipe corporate container on BYOD
- Employee privacy protections documented (what is and is not monitored on personal devices)
- Home network security recommendations (router firmware, WPA3, guest network)

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.6.7 Remote Working, A.8.1 User Endpoint Devices |
| SOC 2 | CC6.1, CC6.6 Endpoint Security |
| NIST CSF | PR.AC Access Control, PR.DS Data Security |
| HIPAA | 164.310(b)-(c) Workstation Use and Security |
| PCI DSS | Requirement 12.3.5 (Usage Policies for Remote Access) |

---

## Encryption Policy

Defines requirements for cryptographic protection of data at rest, in transit, and in use.

### Structure

| Section | Purpose |
|---------|---------|
| **Encryption Standards** | Approved algorithms and minimum key lengths |
| **Data at Rest** | Full-disk encryption, database encryption, file-level encryption |
| **Data in Transit** | TLS 1.2+ minimum, certificate management, VPN tunnels |
| **Key Management** | Key generation, storage (HSM/KMS), rotation, destruction |
| **Certificate Management** | CA hierarchy, certificate lifecycle, automated renewal |
| **Cryptographic Inventory** | Tracking all encryption implementations and dependencies |

### Approved Algorithms

| Use Case | Algorithm | Minimum Key Length |
|----------|-----------|--------------------|
| Symmetric encryption | AES | 256-bit |
| Asymmetric encryption | RSA | 2048-bit (3072+ preferred) |
| Asymmetric encryption | ECC | P-256 (P-384 preferred) |
| Hashing | SHA-2 or SHA-3 | SHA-256 minimum |
| Password hashing | bcrypt, Argon2id, scrypt | Per algorithm defaults |
| TLS | TLS 1.2 or 1.3 | N/A (protocol version) |

### Key Elements

- Deprecated algorithms documented with migration timelines (DES, 3DES, MD5, SHA-1, TLS 1.0/1.1)
- Key rotation schedule: symmetric keys annually, asymmetric keys every 2 years
- Key escrow and recovery procedures for business continuity
- HSM or cloud KMS required for Restricted data encryption keys
- Crypto-agility planning for post-quantum readiness

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.8.24 Use of Cryptography |
| SOC 2 | CC6.1, CC6.7 Encryption |
| NIST CSF | PR.DS Data Security |
| HIPAA | 164.312(a)(2)(iv), 164.312(e)(2)(ii) Encryption |
| PCI DSS | Requirement 3 (Protect Stored Data), Requirement 4 (Encrypt Transmission) |

---

## Network Security Policy

Defines requirements for securing the organization's network infrastructure and communications.

### Structure

| Section | Purpose |
|---------|---------|
| **Network Architecture** | Segmentation strategy, DMZ, internal zones, zero-trust microsegmentation |
| **Firewall Rules** | Default deny, rule review cadence, change management |
| **Intrusion Detection/Prevention** | IDS/IPS deployment, signature updates, alert handling |
| **Wireless Security** | WPA3 Enterprise, SSID management, rogue AP detection |
| **DNS Security** | DNSSEC, DNS filtering, sinkholing |
| **Network Monitoring** | NetFlow/SFLOW, SIEM integration, anomaly detection |
| **Network Access Control** | 802.1X, device posture assessment, guest network isolation |
| **Cloud Network Security** | VPC design, security groups, network ACLs, transit gateways |

### Key Elements

- Network segmentation by data classification level
- Default deny on all firewalls; explicit allow rules documented with business justification
- Firewall rule review quarterly; unused rules removed
- Wireless networks separated: corporate (802.1X), guest (isolated, internet-only)
- Network diagrams maintained and updated with every infrastructure change
- DDoS protection for internet-facing services

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.8.20-8.23 Network Security, Web Filtering, Segregation |
| SOC 2 | CC6.6 System Boundaries, CC6.1 Logical Access |
| NIST CSF | PR.IR Technology Infrastructure Resilience |
| HIPAA | 164.312(e) Transmission Security |
| PCI DSS | Requirement 1 (Network Security Controls), Requirement 11 (Test Security) |

---

## Change Management Policy

Governs how changes to IT systems, infrastructure, and applications are requested, reviewed, approved, and implemented.

### Structure

| Section | Purpose |
|---------|---------|
| **Change Classification** | Standard, normal, emergency change types |
| **Change Request Process** | Submission, documentation requirements, impact assessment |
| **Change Advisory Board (CAB)** | Composition, meeting cadence, approval authority |
| **Risk Assessment** | Impact analysis, rollback plan requirement, testing evidence |
| **Implementation Windows** | Approved maintenance windows, blackout periods |
| **Emergency Changes** | Expedited approval, post-implementation review requirement |
| **Post-Implementation Review** | Success criteria, monitoring period, closure |

### Change Classification Matrix

| Type | Approval | Lead Time | Examples |
|------|----------|-----------|---------|
| **Standard** | Pre-approved (catalog) | None | Password resets, user provisioning, patching |
| **Normal** | CAB approval | 5+ business days | Infrastructure changes, application deployments, config changes |
| **Emergency** | Emergency CAB (2 approvers) | Immediate | Critical security patches, production outage fixes |

### Key Elements

- All changes logged in change management system with audit trail
- Rollback plan mandatory for all Normal and Emergency changes
- Separation of duties: requester cannot approve their own change
- Post-implementation monitoring period defined per change risk level
- Emergency changes undergo full CAB review within 5 business days after implementation

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.8.32 Change Management |
| SOC 2 | CC8.1 Change Management |
| NIST CSF | PR.IP Information Protection Processes |
| HIPAA | 164.312(e) Integrity Controls |
| PCI DSS | Requirement 6.5 (Change Management Procedures) |

---

## Third-Party / Vendor Security Policy

Governs security requirements for external vendors, suppliers, and service providers with access to organizational data or systems.

### Structure

| Section | Purpose |
|---------|---------|
| **Vendor Risk Assessment** | Pre-engagement security evaluation, tiering by data access |
| **Security Requirements** | Minimum security controls required of vendors |
| **Contractual Requirements** | Security clauses, SLAs, right to audit, breach notification |
| **Ongoing Monitoring** | Periodic reassessment cadence, continuous monitoring triggers |
| **Data Processing Agreements** | GDPR/privacy requirements for data processors |
| **Subcontractor Controls** | Flow-down requirements, subprocessor notification |
| **Vendor Offboarding** | Access revocation, data return/destruction, certificate of destruction |

### Vendor Risk Tiers

| Tier | Data Access | Assessment | Review Cadence |
|------|------------|------------|----------------|
| **Critical** | Restricted/Confidential data, system access | Full security assessment + SOC 2/ISO 27001 review | Annual reassessment |
| **High** | Internal data, limited system access | Security questionnaire + evidence review | Every 18 months |
| **Medium** | No data access, but network-connected services | Abbreviated questionnaire | Every 2 years |
| **Low** | No data or system access | Self-attestation | At contract renewal |

### Key Elements

- Security assessment completed before contract execution
- SOC 2 Type II or ISO 27001 certification required for Critical-tier vendors
- Breach notification clause: vendor must notify within 24-48 hours
- Right to audit clause for Critical and High tiers
- Vendor inventory maintained with risk tier, data flows, and contract renewal dates
- Annual review of vendor population for tier reclassification

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.5.19-5.23 Supplier Relationships |
| SOC 2 | CC9.2 Vendor and Business Partner Risk |
| NIST CSF | GV.SC Supply Chain Risk Management |
| HIPAA | 164.308(b) Business Associate Contracts |
| PCI DSS | Requirement 12.8 (Service Provider Management) |

---

## Physical Security Policy

Governs physical protection of facilities, equipment, and information assets.

### Structure

| Section | Purpose |
|---------|---------|
| **Facility Classification** | Security zones (public, general, restricted, high-security) |
| **Access Controls** | Badge systems, biometrics, visitor management |
| **Surveillance** | CCTV coverage, recording retention, monitoring |
| **Environmental Controls** | Fire suppression, HVAC, water detection, power redundancy |
| **Data Center Security** | Cabinet locks, hot/cold aisle, access logging |
| **Equipment Security** | Asset tagging, secure disposal, removal authorization |
| **Visitor Management** | Registration, escort requirements, badge return |
| **Clean Desk / Clean Screen** | End-of-day requirements, unattended workstation policy |

### Key Elements

- Layered physical security zones with increasing controls
- Visitor logs retained for minimum 90 days
- CCTV recording retention minimum 30 days (90 for high-security areas)
- Server room / data center: two-factor physical access (badge + biometric)
- Media destruction: NIST 800-88 compliant sanitization or physical destruction
- Environmental monitoring with automated alerts (temperature, humidity, water)

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.7.1-7.14 Physical Controls |
| SOC 2 | CC6.4-6.5 Physical Access |
| NIST CSF | PR.AC Physical Access |
| HIPAA | 164.310 Physical Safeguards |
| PCI DSS | Requirement 9 (Restrict Physical Access) |

---

## Security Awareness Training Policy

Defines requirements for building security culture through education, training, and simulation exercises.

### Structure

| Section | Purpose |
|---------|---------|
| **Training Requirements** | Mandatory for all employees, contractors; role-based additions |
| **Training Content** | Core curriculum by topic area |
| **Delivery Methods** | CBT, live sessions, microlearning, lunch-and-learns |
| **Frequency** | Annual comprehensive + monthly reinforcement |
| **Phishing Simulation** | Monthly simulations, reporting metrics, remediation for failures |
| **Metrics & Reporting** | Completion rates, phishing click rates, reporting rates |
| **Role-Based Training** | Additional modules for IT staff, developers, executives, finance |
| **New Hire Training** | Completion within first 5 business days |

### Core Curriculum

| Module | Audience | Frequency |
|--------|----------|-----------|
| Security Fundamentals | All | Annual |
| Phishing & Social Engineering | All | Quarterly + monthly simulation |
| Data Handling & Classification | All | Annual |
| Password & Authentication Hygiene | All | Annual |
| Physical Security & Clean Desk | All | Annual |
| Incident Reporting | All | Annual |
| Secure Development (OWASP) | Developers | Annual |
| Privileged Access Responsibilities | IT/Admin | Annual |
| Executive Threat Briefing | C-suite | Quarterly |
| Financial Fraud (BEC) | Finance, Procurement | Quarterly |

### Key Elements

- Completion tracking with escalation for non-compliance (manager notification at 7 days, HR at 14)
- Phishing simulation click rate target: below 5% organization-wide
- Repeat phishing failures trigger mandatory one-on-one remediation
- Training content updated at least annually and after significant incidents
- Gamification elements to drive engagement (leaderboards, recognition)

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.6.3 Information Security Awareness, Education, and Training |
| SOC 2 | CC1.4 COSO Principle 4 (Competence) |
| NIST CSF | PR.AT Awareness and Training |
| HIPAA | 164.308(a)(5) Security Awareness and Training |
| PCI DSS | Requirement 12.6 (Security Awareness Program) |

---

## Data Retention and Disposal Policy

Governs how long data is retained and how it is securely disposed of when no longer needed.

### Structure

| Section | Purpose |
|---------|---------|
| **Retention Schedule** | Data categories with minimum and maximum retention periods |
| **Legal Hold** | Process for suspending disposal during litigation or investigation |
| **Storage Requirements** | Where retained data is stored, encryption, access controls |
| **Disposal Methods** | Approved methods by media type (digital, physical, cloud) |
| **Disposal Verification** | Certificates of destruction, audit trail |
| **Cloud Data** | Provider deletion verification, data remanence considerations |

### Disposal Methods by Media Type

| Media | Method | Standard |
|-------|--------|----------|
| HDDs | Degaussing + physical destruction | NIST 800-88 Purge/Destroy |
| SSDs | Cryptographic erase + physical destruction | NIST 800-88 Purge |
| Paper | Cross-cut shredding (DIN 66399 Level P-4+) | DIN 66399 |
| Optical media | Shredding | NIST 800-88 Destroy |
| Cloud storage | Provider-confirmed deletion + encryption key destruction | CSA guidance |
| Mobile devices | Factory reset + cryptographic erase via MDM | NIST 800-88 Clear/Purge |

### Key Elements

- Retention periods defined per data category with legal, regulatory, and business justifications
- "When in doubt, don't delete" during active legal holds
- Automated retention enforcement where possible (email archival, cloud lifecycle policies)
- Disposal logged with date, method, responsible party, and verification
- Third-party disposal vendors require certificates of destruction and auditable processes

### Compliance Mapping

| Framework | Relevant Controls |
|-----------|------------------|
| ISO 27001 | A.8.10 Information Deletion, A.8.14 Redundancy |
| SOC 2 | CC6.5 Disposal of Assets |
| NIST CSF | PR.DS Data Security |
| HIPAA | 164.310(d)(2)(i) Disposal |
| PCI DSS | Requirement 3.1 (Data Retention), Requirement 9.4 (Media Destruction) |

---

## Policy Governance Framework

Governs how policies themselves are managed, reviewed, and maintained.

### Review Cadence

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Full policy review | Annual (minimum) | Policy owner + CISO |
| Interim review | Triggered by incidents, regulatory changes, org changes | CISO |
| New policy creation | As needed | CISO with executive approval |
| Policy retirement | When superseded or no longer applicable | Policy owner |

### Ownership Model

| Role | Responsibility |
|------|---------------|
| **Policy Owner** | Business/functional leader accountable for the policy's content and relevance |
| **CISO** | Overall policy framework governance, consistency, and completeness |
| **Policy Author** | Drafts and updates policy content (often IT Security team) |
| **Approver** | Executive or committee that formally approves (CIO, executive committee, board) |
| **Legal/Compliance** | Reviews for regulatory alignment and enforceability |

### Exception Management

| Element | Requirement |
|---------|-------------|
| Exception request | Formal written request with business justification |
| Risk acceptance | Risk owner (not IT) must accept residual risk |
| Compensating controls | Document alternative controls that mitigate the risk |
| Expiration | All exceptions time-bound (max 12 months, renewable) |
| Tracking | Exception register maintained and reviewed quarterly |
| Escalation | Exceptions for Restricted data require CISO + executive approval |

### Versioning

- Major versions (1.0, 2.0): significant changes to scope, requirements, or controls
- Minor versions (1.1, 1.2): clarifications, formatting, non-material updates
- All versions retained in document management system with change history
- Effective date clearly stated; transition period defined for material changes

---

## Compliance Framework Mapping

### Master Policy-to-Framework Matrix

| Policy | SOC 2 | ISO 27001 | NIST CSF | HIPAA | PCI DSS |
|--------|-------|-----------|----------|-------|---------|
| Information Security Policy | CC1.1 | A.5.1 | GV.PO | 164.316(a) | Req 12 |
| Acceptable Use | CC1.4 | A.5.10 | PR.AT | 164.310(b) | Req 12.3 |
| Access Control | CC6.1-6.3 | A.5.15-5.18, A.8.2-8.5 | PR.AA | 164.312(a),(d) | Req 7, 8 |
| Data Classification | CC6.7 | A.5.12-5.14 | ID.AM, PR.DS | 164.312(a),(e) | Req 3, 4 |
| Password / Authentication | CC6.1 | A.8.2-8.5 | PR.AA | 164.312(d) | Req 8 |
| Incident Response | CC7.3-7.5 | A.5.24-5.28 | RS.MA, RS.AN | 164.308(a)(6) | Req 12.10 |
| BC/DR | A1.1-A1.3 | A.5.29-5.30, A.8.13-8.14 | RC.RP | 164.308(a)(7) | Req 12.10.1 |
| Remote Work / BYOD | CC6.1, CC6.6 | A.6.7, A.8.1 | PR.AC, PR.DS | 164.310(b)-(c) | Req 12.3.5 |
| Encryption | CC6.1, CC6.7 | A.8.24 | PR.DS | 164.312(a)(2)(iv) | Req 3, 4 |
| Network Security | CC6.6 | A.8.20-8.23 | PR.IR | 164.312(e) | Req 1, 11 |
| Change Management | CC8.1 | A.8.32 | PR.IP | 164.312(e) | Req 6.5 |
| Third-Party / Vendor | CC9.2 | A.5.19-5.23 | GV.SC | 164.308(b) | Req 12.8 |
| Physical Security | CC6.4-6.5 | A.7.1-7.14 | PR.AC | 164.310 | Req 9 |
| Security Awareness | CC1.4 | A.6.3 | PR.AT | 164.308(a)(5) | Req 12.6 |
| Data Retention / Disposal | CC6.5 | A.8.10, A.8.14 | PR.DS | 164.310(d)(2)(i) | Req 3.1, 9.4 |

---

## Policy Writing Best Practices

### Clarity

- Write for the reader, not the author; avoid jargon unless defined in a glossary
- Use "must" for mandatory requirements, "should" for recommendations, "may" for optional guidance
- One requirement per sentence; do not chain requirements with "and"
- Include a glossary section for technical terms
- Use active voice: "The data owner must classify all data" not "Data must be classified"

### Enforceability

- Every "must" statement needs a corresponding enforcement mechanism
- Define who monitors compliance and how violations are detected
- State consequences clearly: informal warning, formal warning, termination, legal action
- Avoid aspirational language ("strive to", "best effort") in mandatory requirements
- Include an exceptions process so the policy is not bypassed silently

### Measurability

- Define metrics for each policy: compliance rate, incident count, training completion
- Set targets: "95% of employees complete training within 30 days of hire"
- Report metrics to management quarterly
- Use metrics to drive policy improvement, not just compliance reporting
- Automate measurement where possible (SIEM, MDM, IdP reporting)

### Structure Consistency

All policies should follow a consistent structure:

1. Purpose
2. Scope
3. Definitions / Glossary
4. Policy Statements (the requirements)
5. Roles and Responsibilities
6. Compliance and Enforcement
7. Exceptions
8. Related Policies and Standards
9. Revision History

---

## Common Policy Anti-Patterns

| Anti-Pattern | Problem | Better Approach |
|--------------|---------|-----------------|
| **Copy-paste from templates** | Policies don't reflect actual environment, controls, or risks | Start from templates but customize to your organization's risk profile and capabilities |
| **Policy without enforcement** | Creates a false sense of security; fails audits when evidence is requested | Every policy requirement needs a monitoring mechanism and documented enforcement actions |
| **Aspirational policies** | Requirements exceed the organization's ability to comply, breeding habitual non-compliance | Write policies you can actually enforce today; use a roadmap for aspirational controls |
| **Monolithic mega-policy** | A single 100-page document that nobody reads or maintains | Modular policies linked by the ISP; each policy owned by a specific individual |
| **Technical implementation in policy** | Policies tied to specific products/versions become outdated quickly | Policy states the requirement; a separate standard/procedure specifies the implementation |
| **No version control** | Impossible to determine which version is current or what changed | Use a document management system with version tracking, change history, and effective dates |
| **Annual review only** | Policies drift from reality between review cycles | Annual full review plus triggered reviews (after incidents, regulatory changes, org changes) |
| **IT-only ownership** | Policies lack business context and buy-in; perceived as IT bureaucracy | Business function leaders own policies for their domain; IT provides technical guidance |
| **Missing exceptions process** | People bypass policies entirely because there is no legitimate path for exceptions | Formal exception process with risk acceptance, compensating controls, and time limits |
| **Compliance-driven, not risk-driven** | Policies optimize for passing audits rather than reducing actual risk | Use compliance frameworks as a floor; design controls based on your threat landscape |
| **No training on policies** | Employees cannot comply with policies they have never read or understood | Publish policies accessibly; train on key requirements; test comprehension |
| **Policy/standard/procedure confusion** | Mixing "what" (policy), "how much" (standard), and "how to" (procedure) in one document | Maintain a clear hierarchy: Policy (why/what) -> Standard (how much) -> Procedure (how to) |

---

## Quick Reference: Policy Document Hierarchy

```
Information Security Policy (ISP)
  |
  +-- Acceptable Use Policy
  +-- Access Control Policy
  |     +-- Privileged Access Standard
  |     +-- Account Lifecycle Procedure
  +-- Data Classification Policy
  |     +-- Data Handling Standard
  |     +-- Labeling Procedure
  +-- Password & Authentication Policy
  |     +-- MFA Standard
  +-- Incident Response Policy
  |     +-- IR Runbooks (per incident type)
  |     +-- Communication Procedure
  +-- BC/DR Policy
  |     +-- Backup Standard
  |     +-- DR Runbooks (per system tier)
  +-- Remote Work / BYOD Policy
  |     +-- BYOD Enrollment Procedure
  +-- Encryption Policy
  |     +-- Key Management Standard
  |     +-- Certificate Management Procedure
  +-- Network Security Policy
  |     +-- Firewall Rule Standard
  |     +-- Wireless Security Standard
  +-- Change Management Policy
  |     +-- Standard Change Catalog
  |     +-- Emergency Change Procedure
  +-- Third-Party / Vendor Security Policy
  |     +-- Vendor Assessment Questionnaire
  |     +-- Vendor Tiering Standard
  +-- Physical Security Policy
  |     +-- Visitor Management Procedure
  |     +-- Media Disposal Procedure
  +-- Security Awareness Training Policy
  |     +-- Phishing Simulation Procedure
  |     +-- Role-Based Training Matrix
  +-- Data Retention & Disposal Policy
        +-- Retention Schedule
        +-- Disposal Procedure
```

---

> "Good security policies are invisible when followed and invaluable when tested. Write for the incident you haven't had yet."
