# Compliance Frameworks — Knowledge Pack

**Version**: 1.1.0 (update from v1.0 — added Singapore Agentic AI Governance, EU AI Act pointer references, current-status sidecar pattern, control-to-obligation mapping table)
**Owner**: compliance-officer
**Last updated**: 2026-04-11
**Consumers**: `/compliance-audit` (A4, Phase 3), `/ai-regulatory-audit` (C1.2b), `/ai-control-audit` (C1.2a)
**Sidecar**: `compliance-frameworks/current-status.md` (date-sensitive content)
**Sources**: `compliance-frameworks/sources.md` (canonical URLs)
**Sensitive**: true
**Re-verification cadence**: quarterly (next: 2026-07-11)

---

## 1. Purpose and Framing

### What this pack covers

Horizontal compliance and governance frameworks published by recognizable regulators, standards bodies, and public-interest institutions, used to structure compliance programs and AI governance posture. The pack catalogues the **structural elements** of each framework — risk tiers, obligation buckets, control categories, article groupings — that can be referenced without reproducing framework text.

The pack exists to feed three downstream skills with a shared reference vocabulary:
- `/compliance-audit` (A4, Phase 3) — horizontal control-level readiness gap against a named framework
- `/ai-regulatory-audit` (C1.2b) — AI system governance posture across applicable frameworks
- `/ai-control-audit` (C1.2a) — technical AI control taxonomy audit against an AI system

### What this pack does NOT cover

- Vendor certification content (certification-body playbooks, auditor workpapers, ISMS tooling vendor guidance)
- Consultancy playbooks and interpretive guidance from compliance tooling vendors
- Law firm publications, alerts, or interpretations (see Section 2.3)
- Non-public framework drafts, think-tank unpublished material, or material behind opaque paywalls
- Specific regulator enforcement decisions (these are case-specific and belong in case records, not a horizontal pack)
- Industry-specific certification content deep enough to substitute for specialist review (PCI DSS deep dive, FedRAMP control-by-control interpretation, etc.)

### Authoring discipline

1. **Pointer references only.** Every conceptual claim is accompanied by a pointer to the regulator source in `sources.md`. No content is lifted from source documents.
2. **Structural elements are the owned artifact.** Article numbers, control categories, risk tiers, and obligation bucket names are the stable references the pack asserts. These do not change version-to-version and are citable without reproducing text.
3. **Date-sensitive content lives in the sidecar.** Effective dates, transition deadlines, version numbers, and "status as of" claims go to `current-status.md`, never the main pack.
4. **No law firm citations.** The pack sources from regulators, standards bodies (ISO, AICPA, NIST), and academic governance programs. Not from law firms, consultancies, or vendor publications. Jurisdictional interpretation is explicitly deferred to licensed counsel per `sensitive-skill-guardrails.md`.
5. **First-principles authoring.** Every section is drafted from public regulator sources, not from forked compliance pack content or template libraries.

### Jurisdictional posture

This pack assumes a default multi-jurisdictional posture (US federal + EU + UK + Singapore + Israel for banking use cases). When a downstream skill uses this pack, the skill MUST declare the jurisdiction assumed in its output disclaimer per `sensitive-skill-guardrails.md` Section 3.1. Framework applicability is jurisdictional; the pack gives the structural reference, the skill applies it.

---

## 2. Framework Inventory

Each framework below is cited by its stable structural elements (article numbers, control categories, risk tiers, obligation buckets). For effective dates, version numbers, and status updates, see `current-status.md`. For canonical URLs, see `sources.md`.

### 2.1 SOC 2 (AICPA Trust Services Criteria)

**Published by**: American Institute of Certified Public Accountants (AICPA). Attestation framework for service organizations.

**Stable structural elements**:
- **Five Trust Services Criteria (TSCs)**: Security, Availability, Processing Integrity, Confidentiality, Privacy. Security is always included; the other four are included at the service organization's discretion based on service commitments.
- **Control categories** (Security TSC): CC1 (Control Environment), CC2 (Communication and Information), CC3 (Risk Assessment), CC4 (Monitoring Activities), CC5 (Control Activities), CC6 (Logical and Physical Access), CC7 (System Operations), CC8 (Change Management), CC9 (Risk Mitigation).
- **Report types**: Type I (design of controls at a point in time) vs Type II (design plus operating effectiveness over a period, typically 6-12 months).
- **Auditor**: Licensed CPA firm, not an accreditation body.

**Why it appears in the mapping**: SOC 2 CC categories provide partial coverage of several AI control obligations, particularly in model access (CC6), operational monitoring (CC7), and change management (CC8). SOC 2 is NOT an AI-specific framework; it is referenced for horizontal control coverage only.

**Non-overlap with AI frameworks**: SOC 2 does not address model provenance, bias assessment, or AI-specific transparency obligations. A SOC 2 Type II report does not satisfy EU AI Act Article 9 risk management requirements.

### 2.2 GDPR (Regulation (EU) 2016/679)

**Published by**: European Parliament and Council. Effective 2018-05-25. The foundational EU data protection framework.

**Stable structural elements**:
- **Key articles referenced in compliance work**:
  - Article 5 (principles of processing)
  - Article 6 (lawful basis for processing)
  - Article 9 (special category data)
  - Article 12-22 (data subject rights)
  - Article 22 (automated individual decision-making, including profiling — directly relevant to AI systems)
  - Article 25 (data protection by design and by default)
  - Article 30 (records of processing activities)
  - Article 32 (security of processing)
  - Article 33-34 (breach notification)
  - Article 35 (data protection impact assessment — DPIA)
  - Article 44-49 (international transfers)
- **Supervisory authority structure**: Member State Data Protection Authorities (DPAs) + European Data Protection Board (EDPB) for consistency mechanism.
- **EDPB guidance**: The EDPB issues guidelines on recurring interpretive questions (automated decision-making, AI, legitimate interests, international transfers). These are the closest thing to a regulator position the pack cites. See `sources.md` for the EDPB guidance index.

**Why it appears in the mapping**: Article 22 (automated decision-making) and Article 35 (DPIA for high-risk processing) overlap materially with EU AI Act and NIST AI RMF obligations for AI systems that process personal data.

**Non-overlap with AI frameworks**: GDPR is a data protection regime; it addresses personal data processing, not AI system safety or reliability. An AI system that processes no personal data is outside GDPR scope but may be squarely inside EU AI Act or NIST AI RMF scope.

### 2.3 ISO/IEC 27001 (ISMS)

**Published by**: International Organization for Standardization (ISO) / International Electrotechnical Commission (IEC). Current edition: ISO/IEC 27001:2022.

**Stable structural elements**:
- **Management system clauses**: Clause 4 (Context), Clause 5 (Leadership), Clause 6 (Planning), Clause 7 (Support), Clause 8 (Operation), Clause 9 (Performance Evaluation), Clause 10 (Improvement).
- **Annex A control themes** (2022 revision): Organizational (A.5, 37 controls), People (A.6, 8 controls), Physical (A.7, 14 controls), Technological (A.8, 34 controls). Total 93 controls in 4 themes (down from 114 in 14 domains in the 2013 revision).
- **Certification**: Three-year certificate with annual surveillance audits, conducted by accredited certification bodies.
- **Statement of Applicability (SoA)**: The mandatory document listing which Annex A controls are in scope, which are excluded, and why.

**Why it appears in the mapping**: ISO 27001 Annex A.8 (Technological) and A.5 (Organizational) provide horizontal coverage for several AI governance obligations, particularly around access control, cryptography, and supplier security.

**Non-overlap with AI frameworks**: ISO 27001 is an information security management system standard; it is not AI-specific. ISO 42001 (Section 2.4) is the AI-specific management system standard.

### 2.4 ISO/IEC 42001 (AI Management Systems)

**Published by**: ISO/IEC. First edition published December 2023. The AI-specific management system standard, structurally parallel to ISO 27001.

**Stable structural elements**:
- **Management system clauses**: Same 4-10 structure as ISO 27001 (Context, Leadership, Planning, Support, Operation, Performance Evaluation, Improvement), reframed for AI.
- **Annex A (AI-specific control objectives)**: Control objectives covering policies for AI, internal organization for AI, AI resources, AI system impact assessment, AI system lifecycle, data for AI systems, information for interested parties, use of AI systems, third-party relationships.
- **Scope**: Applicable to any organization providing or using AI systems, regardless of sector.
- **Relationship to ISO 27001**: Designed to integrate with an existing ISO 27001 ISMS. Organizations often pursue both certifications together.

**Why it appears in the mapping**: ISO 42001 is the only AI-specific management system standard currently published and is structurally the best match for AI control taxonomy integration. It provides management-system scaffolding that ad hoc AI governance programs lack.

**Non-overlap with AI frameworks**: ISO 42001 is a management system standard, not a regulatory framework. Certification demonstrates process maturity, not regulatory compliance. An organization certified to ISO 42001 still needs to satisfy EU AI Act, GDPR, etc., independently.

### 2.5 HIPAA (US Health Insurance Portability and Accountability Act)

**Published by**: US Department of Health and Human Services (HHS), Office for Civil Rights (OCR). Federal US health data regulation.

**Stable structural elements**:
- **Privacy Rule**: Covers use and disclosure of Protected Health Information (PHI).
- **Security Rule**: Administrative, physical, and technical safeguards for electronic PHI (ePHI). Three categories of required and addressable implementation specifications.
- **Breach Notification Rule**: Notification obligations to affected individuals, HHS, and (for large breaches) media.
- **Covered entities** (healthcare providers, health plans, healthcare clearinghouses) and **business associates** (vendors handling PHI under a Business Associate Agreement).

**Why it appears in the mapping**: HIPAA's Security Rule technical safeguards provide structural reference for access control and audit logging obligations on AI systems processing PHI in US healthcare contexts.

**Non-overlap with AI frameworks**: HIPAA is US-specific and health-data-specific. It does not address AI system safety, bias, or general-purpose governance. An AI system outside the healthcare sector is outside HIPAA scope.

### 2.6 CCPA / CPRA (California Consumer Privacy Act / California Privacy Rights Act)

**Published by**: California State Legislature; enforcement by California Privacy Protection Agency (CPPA) and California Attorney General. CCPA effective 2020; CPRA amendments effective 2023.

**Stable structural elements**:
- **Consumer rights**: Right to know, right to delete, right to correct, right to opt-out of sale/sharing, right to limit use of sensitive personal information, right to non-discrimination.
- **Business obligations**: Privacy notice at or before collection, response procedures for consumer requests, data minimization, purpose limitation.
- **Automated Decision-Making Technology (ADMT) rules**: CPRA authorizes rules on automated decision-making and profiling. Draft rules have been proposed by the CPPA; final rules are not yet in effect as of the pack's last update (see `current-status.md` for current status).
- **Sensitive personal information**: A defined category with additional use restrictions and opt-out rights.

**Why it appears in the mapping**: The ADMT rules, once finalized, will create US-state-level obligations on AI systems making automated decisions about California consumers, structurally parallel to GDPR Article 22.

**Non-overlap with AI frameworks**: CCPA/CPRA is a state consumer privacy regime. It does not address general-purpose AI governance, only AI systems insofar as they process California consumer personal information or make automated decisions.

### 2.7 NIST AI Risk Management Framework (AI RMF)

**Published by**: US National Institute of Standards and Technology (NIST). First version published January 2023. Voluntary framework for managing AI risks. The Generative AI Profile was published July 2024.

**Stable structural elements**:
- **Four core functions**:
  - **GOVERN** — cultivate a risk management culture across the organization; policies, roles, accountability
  - **MAP** — establish context and characterize AI risks in that context
  - **MEASURE** — analyze, assess, and track identified AI risks
  - **MANAGE** — prioritize and act on risks based on impact
- **Trustworthy AI characteristics**: Valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, fair with harmful bias managed.
- **Voluntary nature**: NIST AI RMF is not a regulation. US federal agencies are directed to reference it, and it is commonly referenced in vendor risk assessments and procurement.
- **Generative AI Profile**: Extends the base framework with generative-AI-specific risks (hallucination, prompt injection, content provenance, training data governance).

**Why it appears in the mapping**: NIST AI RMF is the most widely referenced voluntary AI risk framework in US-centric governance programs. Its GOVERN/MAP/MEASURE/MANAGE structure maps cleanly to the 6 control categories in the C1.2a technical taxonomy.

**Non-overlap with AI frameworks**: NIST AI RMF is voluntary and structural; it does not impose specific obligations or create enforcement exposure. It is a scaffold for organizations to build their own AI governance program.

### 2.8 EU AI Act (Regulation (EU) 2024/1689) — POINTER REFERENCE

**Published by**: European Parliament and Council. Adopted 2024. Phased entry into application across 2024-2027 (see `current-status.md` for the schedule).

**Stable structural elements**:
- **Four risk tiers**:
  - **Unacceptable risk** (Article 5) — prohibited AI practices (social scoring, manipulative techniques exploiting vulnerabilities, untargeted scraping for facial recognition databases, real-time remote biometric identification in public spaces by law enforcement with narrow exceptions, emotion recognition in workplace/education, categorization of natural persons based on biometric data to infer sensitive attributes, predictive policing based on profiling alone).
  - **High risk** (Article 6 + Annex I + Annex III) — AI systems used as safety components of regulated products (Annex I) or in listed sensitive domains (Annex III: biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, administration of justice, democratic processes).
  - **Limited risk** (Article 52) — transparency obligations for specific AI systems interacting with humans (chatbots, emotion recognition, deepfakes, synthetic content).
  - **Minimal risk** — most AI applications; no specific obligations beyond voluntary codes of conduct.
- **High-risk system obligations** (Articles 8-15):
  - Risk management system
  - Data and data governance
  - Technical documentation
  - Record-keeping (automatic logging)
  - Transparency and provision of information to deployers
  - Human oversight
  - Accuracy, robustness, and cybersecurity
- **General-Purpose AI (GPAI)** (Chapter V): Distinct obligations for GPAI model providers, including documentation, copyright policy, training data summary, and additional obligations for GPAI models with systemic risk.
- **AI Office**: Established at the Commission level to oversee enforcement for GPAI; Member State authorities for other provisions.
- **Conformity assessment**: High-risk systems undergo conformity assessment before placing on market. For most Annex III systems this is internal control-based; for certain uses (Annex I products, some biometrics) it requires notified body involvement.
- **CE marking**: Required for high-risk AI systems placed on the EU market.
- **Fines**: Up to EUR 35M or 7% of worldwide annual turnover for prohibited practices violations; lower tiers for other infringements.

**Pointer discipline**: The EU AI Act text is available at EUR-Lex (see `sources.md`). This pack does NOT reproduce article text; it cites article numbers and obligation bucket names. For current application dates see `current-status.md`. For interpretive questions, defer to licensed EU counsel — the pack explicitly does NOT take interpretive positions on AI Act application.

**Why it appears in the mapping**: EU AI Act high-risk system obligations (Articles 8-15) are the most concrete AI governance obligations currently in any regulatory framework. They provide structural reference for the control-to-obligation mapping in Section 3.

**Non-overlap with other AI frameworks**: EU AI Act is legally binding for EU-market AI systems; other frameworks (NIST AI RMF, ISO 42001, Singapore Agentic AI Governance) are voluntary or advisory. EU AI Act creates enforcement exposure; the others do not.

### 2.9 Singapore Agentic AI Governance Framework (IMDA) — POINTER REFERENCE

**Published by**: Singapore Infocomm Media Development Authority (IMDA). Complements the existing Singapore Model AI Governance Framework. Focused specifically on agentic AI systems (systems that plan and execute multi-step actions with some degree of autonomy).

**Stable structural elements**:
- **Seven risk categories for agentic AI** (from the IMDA framework):
  1. **Intended purpose misalignment** — the agent acts outside its specified purpose or takes on tasks it was not designed for
  2. **Autonomy creep** — the agent progressively expands its action space beyond the originally authorized scope
  3. **Deception** — the agent deceives users, other agents, or oversight systems about its actions, capabilities, or intent
  4. **Privacy violation** — the agent improperly collects, uses, or discloses personal information during its autonomous operation
  5. **Security compromise** — the agent is exploited to breach security boundaries, including via prompt injection or tool-chain abuse
  6. **Discrimination** — the agent produces discriminatory outcomes in its autonomous decisions
  7. **Transparency failure** — the agent's reasoning, decisions, and actions cannot be explained or audited
- **Relationship to Model AI Governance Framework**: The Agentic AI Framework extends the Model AI Governance Framework (which addresses general AI systems) with agent-specific risks. Both are voluntary frameworks published by IMDA as guidance for Singapore-deployed AI systems.
- **Governance recommendations**: Risk assessment, human-in-the-loop for consequential actions, boundary controls on agent action spaces, observability and logging, incident response procedures.

**Pointer discipline**: The IMDA Agentic AI Governance Framework text is available at the IMDA website (see `sources.md`). This pack cites the 7 risk categories and the structural relationship to the Model AI Governance Framework without reproducing framework text. For current version and status see `current-status.md`.

**Why it appears in the mapping**: The Singapore 7-category risk taxonomy is the most structured public framework specifically addressing agentic AI risks. It provides risk categories that map directly to several C1.2a technical control categories (particularly runtime guardrails, observability, and incident response).

**Non-overlap with other AI frameworks**: Singapore frameworks are voluntary; they do not impose legal obligations. They provide risk framing structure that complements EU AI Act (which addresses AI systems broadly but does not have a dedicated agentic AI risk taxonomy) and NIST AI RMF (which addresses AI risks at a higher level of generality).

### 2.10 OECD AI Principles

**Published by**: Organisation for Economic Co-operation and Development (OECD). Adopted 2019; the first intergovernmental standard on AI.

**Stable structural elements**:
- **Five values-based principles**:
  1. Inclusive growth, sustainable development, and well-being
  2. Human rights and democratic values, including fairness and privacy
  3. Transparency and explainability
  4. Robustness, security, and safety
  5. Accountability
- **Five recommendations for policymakers**: Investing in AI R&D, fostering digital ecosystem, shaping enabling policy environment, building human capacity, international cooperation.
- **Soft-law status**: Non-binding recommendations endorsed by OECD member states and adhering countries.

**Why it appears in the mapping**: OECD AI Principles are the most widely adopted intergovernmental AI governance reference. They provide a values framework that organizations cite to demonstrate international alignment, though they create no direct obligations.

**Non-overlap with other AI frameworks**: OECD principles are values-level statements; they do not contain testable obligations or controls. They are referenced as a foundational layer under which NIST AI RMF, EU AI Act, and national frameworks sit.

### 2.11 Israeli Protection of Privacy Law 5741-1981 + Banking Directive 361

**Published by**: Israeli Knesset (PPL) and the Bank of Israel Supervisor of Banks (Directive 361). The PPL is Israel's foundational data protection law; Directive 361 is a banking-sector specific directive on information security and technology risk management.

**Stable structural elements**:
- **PPL core obligations**: Database registration, consent for processing, data subject access rights, breach notification (via the 2025 amendment, pending full effect).
- **PPL Privacy Protection Authority (PPA)**: The Israeli data protection supervisory authority.
- **Directive 361 scope**: Applies to Israeli banking institutions; covers information security, technology risk management, cloud adoption, third-party risk, and (per 2024 amendments) AI-related risk management.
- **Relationship to compliance-audit A4 birth test**: Directive 361 was used as a custom framework in the A4 `/compliance-audit` skill's birth test for Bank Discount. It is cited here because downstream skills may reference Israeli banking-sector obligations as a structural input.

**Pointer discipline**: PPL text is available via the PPA; Directive 361 is published by the Bank of Israel. Both are in Hebrew with unofficial English translations circulating; the pack does not cite unofficial translations as authoritative. See `sources.md` for URLs (canonical paths flagged for verification).

**Why it appears in the mapping**: The A4 `/compliance-audit` skill ships with Israeli banking framework support, and the pack maintains structural reference for downstream skills that consume it.

**Non-overlap with other frameworks**: Israeli banking directives are sector-specific and jurisdiction-specific. They do not substitute for GDPR analysis when EU data is involved, and they do not substitute for general-purpose AI governance frameworks.

---

## 3. Control-to-Obligation Mapping Table (Load-Bearing — Shared Between C1.2a and C1.2b)

This table is the authoritative mapping between the 6 AI control categories (from the `/ai-control-audit` C1.2a technical taxonomy) and the regulatory obligations they satisfy under each framework. It is consumed by both `/ai-control-audit` (to identify which controls are "load-bearing for compliance") and `/ai-regulatory-audit` (to identify which obligations are "satisfied by existing controls").

**Control categories** (from C1.2a taxonomy):
1. Model provenance
2. Pre-deployment evaluation
3. Runtime guardrails
4. Observability
5. Incident response
6. Change management

**Mapping**:

| # | Control | Obligation | Framework | Evidence type |
|---|---|---|---|---|
| 1 | Model provenance (training data lineage) | Data governance obligation — training data quality, relevance, representativeness | EU AI Act Article 10 | Training data documentation, dataset datasheet, provenance log |
| 2 | Model provenance (model card + version history) | Technical documentation obligation | EU AI Act Article 11 + Annex IV | Model card, version history, documentation package |
| 3 | Model provenance (third-party model attribution) | GPAI model documentation obligation | EU AI Act Article 53 (GPAI) | Upstream model documentation, license records, training data summary |
| 4 | Model provenance (data minimization at training) | Data minimization principle | GDPR Article 5(1)(c) | DPIA, data flow diagram, training data retention policy |
| 5 | Pre-deployment evaluation (accuracy and robustness testing) | Accuracy, robustness, cybersecurity obligation | EU AI Act Article 15 | Test reports, benchmark results, adversarial test documentation |
| 6 | Pre-deployment evaluation (bias and fairness assessment) | Data governance obligation, protection against discriminatory outcomes | EU AI Act Article 10 + Recital 44 | Bias audit report, fairness metrics, subgroup performance evaluation |
| 7 | Pre-deployment evaluation (DPIA for automated decision-making) | Data protection impact assessment for high-risk processing | GDPR Article 35 | DPIA document, risk assessment, mitigation plan |
| 8 | Pre-deployment evaluation (NIST AI RMF MEASURE function) | Measure identified AI risks | NIST AI RMF MEASURE | Risk measurement documentation, measurement methodology |
| 9 | Runtime guardrails (input validation and prompt injection defense) | Cybersecurity obligation | EU AI Act Article 15 | Guardrail design documentation, penetration test results |
| 10 | Runtime guardrails (output filtering and content moderation) | Transparency obligation for AI-generated content | EU AI Act Article 52 | Content filter policy, moderation logs |
| 11 | Runtime guardrails (human-in-the-loop for consequential actions) | Human oversight obligation | EU AI Act Article 14 | HITL design documentation, escalation procedures |
| 12 | Runtime guardrails (autonomy boundary enforcement) | Autonomy creep risk category | Singapore Agentic AI Governance (Risk 2) | Boundary control design, tool access controls, scope logs |
| 13 | Runtime guardrails (access control to AI system) | Logical access control | SOC 2 CC6; ISO 27001 A.5.15, A.8.3; ISO 42001 Annex A | Access control policy, access review records, MFA evidence |
| 14 | Observability (decision logging) | Record-keeping obligation (automatic logging) | EU AI Act Article 12 | Decision logs, log retention policy, log access controls |
| 15 | Observability (input/output capture for audit) | Records of processing activities | GDPR Article 30 | RoPA, audit log specifications |
| 16 | Observability (model drift detection) | Post-market monitoring obligation | EU AI Act Article 72 | Drift detection dashboards, drift alert records |
| 17 | Observability (NIST AI RMF MEASURE — continuous) | Continuous measurement of AI risks | NIST AI RMF MEASURE | Continuous monitoring design, measurement frequency documentation |
| 18 | Observability (transparency to affected individuals) | Transparency obligation for AI interaction | EU AI Act Article 52; GDPR Article 22(3) | User-facing disclosures, decision explanation capability |
| 19 | Incident response (AI incident reporting) | Serious incident reporting obligation | EU AI Act Article 73 | Incident log, regulator notification procedure, 15-day reporting SLA |
| 20 | Incident response (breach notification when personal data involved) | Personal data breach notification | GDPR Articles 33-34 | Breach register, 72-hour notification procedure |
| 21 | Incident response (NIST AI RMF MANAGE function) | Manage identified AI risks via response | NIST AI RMF MANAGE | Incident response plan, response playbooks |
| 22 | Change management (model retraining governance) | Substantial modification triggers reassessment | EU AI Act Article 43(4) | Change log, substantial-modification assessment, re-conformity records |
| 23 | Change management (version control and rollback) | System operations control | SOC 2 CC8; ISO 27001 A.8.32 | Version control system, rollback procedures, change approval records |
| 24 | Change management (pre-deployment review for changes) | Quality management system obligation | EU AI Act Article 17; ISO 42001 Clause 8 | QMS documentation, change review records, approval workflows |
| 25 | Change management (supplier and third-party model changes) | Third-party risk management | ISO 27001 A.5.19-A.5.22; ISO 42001 Annex A third-party controls | Supplier contracts, change notification SLAs, supplier audit records |

**Table notes**:
- **Row count**: 25 rows covering all 6 control categories and 6 frameworks (EU AI Act, GDPR, NIST AI RMF, SOC 2, ISO 27001, ISO 42001, Singapore Agentic AI Governance).
- **Coverage distribution**: Model provenance (4 rows), Pre-deployment evaluation (4 rows), Runtime guardrails (5 rows), Observability (5 rows), Incident response (3 rows), Change management (4 rows).
- **Framework distribution**: EU AI Act appears in 11 rows (most concrete obligations); GDPR in 4; NIST AI RMF in 3; SOC 2 in 2; ISO 27001 in 3; ISO 42001 in 3; Singapore Agentic AI Governance in 1.
- **Ownership**: This mapping is authored by the Compliance Officer and co-consumed by C1.2a (`/ai-control-audit`) and C1.2b (`/ai-regulatory-audit`). Changes flow through the Compliance Officer for approval per `delegate-first.md` shared skill orchestrator pattern. Consumers are listed in the pack frontmatter.
- **Scope limitation**: Every "obligation" cell cites the framework article or section; every "evidence type" cell describes what a reviewer would accept as evidence the control is operating. These are the pack's owned claims. **Jurisdictional interpretation of whether the control actually satisfies the obligation is deferred to licensed counsel.** The pack identifies the mapping; it does not assert compliance.
- **This table does NOT claim exhaustive coverage.** Additional obligations exist for sector-specific cases (healthcare, financial services, children's data, biometrics). Downstream skills must expand the mapping for specific domains and declare the expansion in their output.

---

## 4. Framework Selection Rubric

Given an AI system or organization seeking to build a compliance posture, which frameworks apply?

### 4.1 Jurisdictional triggers

| Signal | Framework applies |
|---|---|
| System deployed in EU or processes EU residents' data | GDPR, EU AI Act |
| System deployed in UK | UK GDPR, UK AI regulatory approach (outcomes-based, sector regulators) |
| System deployed in Singapore | IMDA Model AI Governance Framework, IMDA Agentic AI Framework (voluntary) |
| System processes California consumer data | CCPA/CPRA (including ADMT rules when in force) |
| System processes US health data | HIPAA |
| System deployed at US federal agency | NIST AI RMF (directed), sector-specific framework |
| Israeli banking institution | PPL + Directive 361 |
| Multi-jurisdictional enterprise deployment | GDPR + EU AI Act + NIST AI RMF + ISO 42001 as baseline |

### 4.2 System-characteristic triggers

| Signal | Framework applies |
|---|---|
| System makes automated decisions about individuals | GDPR Article 22, EU AI Act (check Annex III), CCPA ADMT (California) |
| System is a general-purpose AI / foundation model | EU AI Act GPAI provisions (Chapter V) |
| System is an agentic AI (multi-step autonomous action) | Singapore Agentic AI Governance (voluntary); EU AI Act if high-risk domain; NIST AI RMF Generative AI Profile |
| System processes biometric data | GDPR Article 9, EU AI Act (potentially Annex III high-risk) |
| System used in hiring / employment decisions | EU AI Act Annex III high-risk, GDPR Article 22, local employment law |
| System used in education assessment | EU AI Act Annex III high-risk |
| System used in critical infrastructure | EU AI Act Annex III high-risk, NIST CSF (security layer) |

### 4.3 Voluntary certification triggers

| Signal | Framework applies |
|---|---|
| Customer-facing trust signal for B2B SaaS (US market) | SOC 2 Type II |
| Customer-facing trust signal for B2B SaaS (EU/international) | ISO 27001 |
| AI management system certification | ISO/IEC 42001 |
| Intergovernmental alignment signal | OECD AI Principles |

### 4.4 Selection rule

For any AI system in production or near-production, the baseline selection is:
- **Mandatory layer**: Frameworks triggered by jurisdictional or system-characteristic rules above. No discretion.
- **Voluntary layer**: Frameworks selected for market signaling, customer requirements, or internal governance. Select based on business case.
- **Advisory layer**: NIST AI RMF as a voluntary scaffold when no other AI-specific framework applies. OECD AI Principles as values-level alignment.

The voluntary and advisory layers are cumulative with the mandatory layer, not substitutes for it.

---

## 5. Overlap and Boundary Matrix

When two or more frameworks apply simultaneously, how do they interact? Short rules for common overlaps:

### 5.1 EU AI Act + GDPR

**When it applies**: An AI system processes personal data of EU residents and falls within EU AI Act scope (particularly high-risk systems).

**Overlap**: Article 10 (data governance) in the AI Act and Articles 5, 9, 25, 35 in GDPR both address training data quality, bias, and impact assessment. A DPIA under GDPR Article 35 does not fully substitute for AI Act Article 9 risk management, but the two processes share evidence and should be coordinated.

**Rule of thumb**: Run DPIA and AI Act risk management in parallel with shared artifacts. DPIA covers personal data processing risks; AI Act risk management covers AI system risks more broadly. Neither substitutes for the other.

### 5.2 EU AI Act + ISO 42001

**When it applies**: Organization seeks ISO 42001 certification while also being subject to EU AI Act.

**Overlap**: ISO 42001 provides management system scaffolding that supports several EU AI Act obligations (quality management under Article 17, human oversight under Article 14, risk management under Article 9). ISO 42001 certification does NOT satisfy EU AI Act by itself — the Act requires specific conformity assessment procedures.

**Rule of thumb**: ISO 42001 is a strong enabler for EU AI Act compliance but is not a substitute. The two should be pursued together, with ISO 42001 as the management scaffold and AI Act obligations as the content.

### 5.3 Singapore Agentic AI Governance + ISO 42001

**When it applies**: Singapore-deployed agentic AI system where the organization also seeks ISO 42001 certification.

**Overlap**: Both frameworks address AI lifecycle management, risk assessment, and operational controls. Singapore's 7-category risk taxonomy provides agent-specific risk framing that ISO 42001's more general structure does not contain.

**Rule of thumb**: Use ISO 42001 as the management system; use the Singapore Agentic AI Governance 7 risk categories as the risk taxonomy within that management system's risk register.

### 5.4 NIST AI RMF + EU AI Act

**When it applies**: Organization deploys AI in both US and EU markets, or US-based organization seeking voluntary alignment that maps to EU AI Act structure.

**Overlap**: NIST AI RMF's MAP/MEASURE/MANAGE functions map to EU AI Act's risk management (Article 9), data governance (Article 10), and post-market monitoring (Article 72). The NIST framework is structurally compatible with AI Act obligations but does not create legal binding.

**Rule of thumb**: NIST AI RMF is an excellent scaffolding document for organizations building an AI governance program that will need to satisfy EU AI Act. Start with NIST, layer EU AI Act-specific documentation on top.

### 5.5 SOC 2 + ISO 27001 + ISO 42001

**When it applies**: B2B SaaS provider with AI features pursuing all three certifications.

**Overlap**: SOC 2 and ISO 27001 have ~70% control overlap (access control, change management, operational monitoring). ISO 42001 adds AI-specific controls not addressed by the other two.

**Rule of thumb**: "Certify once, comply twice" for SOC 2 + ISO 27001 — build a unified control framework. For ISO 42001, treat as an additive layer with AI-specific control objectives that do not substitute for the underlying information security controls.

### 5.6 HIPAA + AI frameworks

**When it applies**: AI system processing US healthcare data (PHI).

**Overlap**: HIPAA Security Rule technical safeguards (access control, audit controls, integrity, transmission security) are independent of AI-specific obligations under EU AI Act or NIST AI RMF. HIPAA does not address model bias, transparency, or data governance at the AI-system level.

**Rule of thumb**: HIPAA compliance is necessary but not sufficient for a US healthcare AI system. Pair HIPAA with NIST AI RMF or ISO 42001 for AI-specific governance.

---

## 6. Boundary With `/compliance-audit`, `/ai-regulatory-audit`, and `/ai-control-audit`

This pack feeds three downstream skills. Each has a distinct scope; the pack supports all three without any of them substituting for the others.

### 6.1 `/compliance-audit` (A4, Phase 3 — shipped)

**Skill scope**: Horizontal control-level readiness gap assessment of an organization or system against a named framework. The skill answers: **"Are we compliant with THIS regulation?"**

**What the pack provides**: Framework structural elements (control categories, article numbers) that the skill uses to structure its gap assessment. The pack is the vocabulary the skill uses to ask its questions.

**What the skill contributes back**: Real-world application evidence — when `/compliance-audit` is run, the skill's output identifies gaps against specific framework elements. These are skill-specific, not pack-owned.

**Boundary**: `/compliance-audit` is framework-specific. If the user specifies "GDPR audit," the skill assesses against GDPR only, using the pack's GDPR section for structural reference.

### 6.2 `/ai-regulatory-audit` (C1.2b)

**Skill scope**: AI system governance posture assessment across applicable regulatory frameworks simultaneously. The skill answers: **"Is THIS AI system responsibly built, documented, and monitored regardless of which specific regulation applies?"**

**What the pack provides**: Framework selection rubric (Section 4), overlap matrix (Section 5), and the control-to-obligation mapping table (Section 3). The skill uses the mapping table to translate AI-specific governance posture into regulatory obligation language.

**What the skill contributes back**: System-specific findings that identify which obligations are satisfied, which are partially satisfied, and which are open — across all applicable frameworks at once.

**Boundary**: `/ai-regulatory-audit` is system-specific and framework-agnostic. It produces a posture report, not a framework compliance report. Where `/compliance-audit` asks "are we compliant with GDPR?", `/ai-regulatory-audit` asks "is this AI system responsibly governed, and which frameworks does that governance satisfy?"

### 6.3 `/ai-control-audit` (C1.2a)

**Skill scope**: Technical AI control taxonomy audit against a specific AI system. The skill answers: **"Does this AI system implement the 6 categories of technical controls required for responsible deployment?"**

**What the pack provides**: The control-to-obligation mapping table (Section 3) is shared with `/ai-regulatory-audit` as the authoritative cross-reference between technical controls (C1.2a's domain) and regulatory obligations (C1.2b's domain).

**What the skill contributes back**: Technical control taxonomy — the 6-category breakdown (model provenance, pre-deployment evaluation, runtime guardrails, observability, incident response, change management) that the mapping table uses as its row structure.

**Boundary**: `/ai-control-audit` is technical; it assesses whether controls exist and operate. It does NOT assess whether those controls satisfy specific regulatory obligations — that is `/ai-regulatory-audit`'s job. The mapping table is the bridge.

### 6.4 Non-overlap summary

| Skill | Scope | Output |
|---|---|---|
| `/compliance-audit` (A4) | Organization vs a named framework | Framework-specific gap report |
| `/ai-regulatory-audit` (C1.2b) | AI system vs all applicable frameworks | Multi-framework posture report |
| `/ai-control-audit` (C1.2a) | AI system vs 6-category technical taxonomy | Technical control assessment |

All three skills reference this pack. None substitutes for the others. A comprehensive AI governance program uses all three at different times: `/ai-control-audit` during development, `/ai-regulatory-audit` before deployment, `/compliance-audit` for annual framework-specific review.

---

## 7. Re-Verification Cadence

### 7.1 Quarterly schedule

The pack and its sidecars are re-verified quarterly. Next verification due: **2026-07-11**. The `last_verified` header in `current-status.md` is updated at each verification cycle. The main pack file's `Last updated` field is updated only when structural content changes; date-sensitive content lives in the sidecar.

### 7.2 Re-verification triggers (outside quarterly schedule)

Re-verify immediately when ANY of the following occur:

- **Regulator announcement** — A covered regulator publishes a new guideline, enforcement priority statement, or interpretive note that materially affects a framework's structural elements or obligation buckets.
- **Case law** — A published decision by a court or supervisory authority reinterprets a framework obligation in a way that changes how it maps to controls.
- **Enforcement action** — A regulator takes enforcement action under a covered framework that reveals a previously-unflagged interpretation or scope question.
- **Framework revision** — A standards body publishes a revision to a covered framework (new ISO edition, NIST framework version update, AICPA TSC revision).
- **Effective date approaches** — An obligation becomes applicable (e.g., EU AI Act high-risk system obligations applying 2026-08-02). Verify that `current-status.md` reflects the status change.

### 7.3 Re-verification procedure

For each triggered re-verification:
1. Pull the canonical source URLs from `sources.md`
2. Compare against `current-status.md` entries for date-sensitive content
3. Compare against this pack's structural element claims
4. Update `current-status.md` with new timestamped entries (never delete old entries; append with dates)
5. If structural elements have changed, update the main pack and increment minor version
6. Log the verification in a dated entry at the bottom of `current-status.md`

### 7.4 What is explicitly NOT re-verified

The pack does NOT re-verify by pulling law firm alerts, vendor compliance tooling updates, consultancy blog posts, or trade association guidance. Only regulator primary sources and recognized standards bodies. This is a deliberate scope limitation — staying close to primary sources avoids interpretation drift.

---

## 8. References

Canonical URLs for all sources cited above are maintained in `sources.md`. The main pack intentionally does not list URLs inline; mechanical re-verification pulls from `sources.md`, which is the single source of truth for source URLs.

Frameworks referenced in this pack:
- SOC 2 (AICPA Trust Services Criteria)
- GDPR (Regulation (EU) 2016/679) and EDPB guidance
- ISO/IEC 27001:2022
- ISO/IEC 42001:2023
- HIPAA (US Privacy, Security, Breach Notification Rules)
- CCPA/CPRA (California)
- NIST AI RMF 1.0 + Generative AI Profile
- EU AI Act (Regulation (EU) 2024/1689)
- Singapore IMDA Model AI Governance Framework + Agentic AI Governance Framework
- OECD AI Principles
- Israeli PPL 5741-1981 + Bank of Israel Directive 361

---

## 9. Pack Metadata

**Authoring discipline**: First-principles authoring from public regulator and standards-body sources. No law firm citations. No vendor or consultancy content. Every conceptual claim is pointer-backed to `sources.md`.

**Consumers**:
- `/compliance-audit` (A4, Phase 3 — shipped)
- `/ai-regulatory-audit` (C1.2b — Phase 5A)
- `/ai-control-audit` (C1.2a — Phase 5A)

**Sidecar files**:
- `compliance-frameworks/current-status.md` — date-sensitive content (first instance of the sidecar pattern per `.claude/rules/delegate-first.md` shared skill orchestrator)
- `compliance-frameworks/sources.md` — canonical URL manifest for mechanical re-verification

**Sensitive pack**: This is a sensitive-adjacent knowledge pack. Downstream skills consuming it MUST follow `sensitive-skill-guardrails.md` for disclaimer structure, jurisdiction-assumed fields, findings/reviewer checklist/cannot-assess-without sections, and two-pass publication gates. The pack itself does not produce user-facing output; it is a reference consumed by skills.

**Owner**: Compliance Officer (Legal Team, Extension Teams). Changes to the pack or the control-to-obligation mapping table flow through the Compliance Officer. Consumer skills may propose changes but do not merge them independently.

**Not legal advice.** This pack is a drafting and triage aid. It does not constitute legal advice and does not create an attorney-client relationship. Jurisdiction-specific questions, contested matters, and any decision with material legal or regulatory consequences require review by a licensed attorney in the relevant jurisdiction.

---

*Version 1.1.0 — published 2026-04-11. Previous version: 1.0 (2026-02-14). Change summary: added Singapore Agentic AI Governance Framework (pointer reference), added EU AI Act as explicit pointer reference with article-level structural elements, added ISO/IEC 42001, added Israeli PPL + Directive 361, added control-to-obligation mapping table (Section 3), added framework selection rubric (Section 4), added overlap matrix (Section 5), added boundary statements with `/compliance-audit`, `/ai-regulatory-audit`, and `/ai-control-audit` (Section 6), added re-verification cadence (Section 7), introduced current-status.md and sources.md sidecars, removed vendor and consultancy references.*
