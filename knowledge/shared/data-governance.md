# Data Governance Methods Knowledge Pack

**Version**: 1.0
**Primary Users**: `data-governance`, `cio`, `data-architect`
**Domain**: Enterprise Data Governance & Management

---
<!-- Attribution:
  Data maturity model section informed by:
  - SuperNerb/Data-Maturity-Models (github.com/SuperNerb/Data-Maturity-Models) — data maturity assessment framework
  Adapted and expanded for Product Org OS agents.
-->

## DAMA-DMBOK2 Framework

### 11 Knowledge Areas

| # | Knowledge Area | Description | Key Activities |
|---|---------------|-------------|----------------|
| 1 | **Data Governance** | Planning, oversight, control | Policies, standards, stewardship, councils |
| 2 | **Data Architecture** | Blueprint for managing data assets | Conceptual/logical/physical models, data flows |
| 3 | **Data Modeling & Design** | Discovering, analyzing, representing data | Entity-relationship, dimensional modeling |
| 4 | **Data Storage & Operations** | Database management, operations | DBMS management, backup, recovery |
| 5 | **Data Security** | Privacy, confidentiality, access | Classification, encryption, masking, RBAC |
| 6 | **Data Integration & Interoperability** | Movement, consolidation, sharing | ETL/ELT, APIs, messaging, data virtualization |
| 7 | **Document & Content Management** | Unstructured data management | ECM, records management, digital assets |
| 8 | **Reference & Master Data** | Shared data management | MDM, reference data, golden records |
| 9 | **Data Warehousing & BI** | Analytical data management | DW design, ETL, BI platforms, OLAP |
| 10 | **Metadata** | Data about data | Business glossary, technical metadata, lineage |
| 11 | **Data Quality** | Data fitness for use | Profiling, cleansing, monitoring, scorecards |

### Data Governance Operating Model

```
Data Governance Council (Strategic)
├── Data Governance Office (Operational)
│   ├── Chief Data Officer / Data Governance Lead
│   ├── Data Governance Analysts
│   └── Data Quality Team
├── Data Stewards (Domain-level)
│   ├── Business Data Stewards (define rules)
│   └── Technical Data Stewards (implement rules)
└── Data Owners (Accountable)
    └── Business leaders who own data domains
```

### Roles & Responsibilities

| Role | Accountability | Example Activities |
|------|---------------|-------------------|
| **Data Owner** | Accountable for data quality in their domain | Approve access, define quality rules |
| **Business Data Steward** | Define business meaning and rules | Maintain business glossary, validate quality |
| **Technical Data Steward** | Implement data policies | Profile data, fix quality issues, manage metadata |
| **Data Custodian** | Manage physical data stores | Database admin, backup, security implementation |
| **Data Consumer** | Use data responsibly | Report issues, follow policies |

---

## Data Quality Management

### Data Quality Dimensions

| Dimension | Definition | Measurement Example |
|-----------|-----------|---------------------|
| **Accuracy** | Data correctly represents real-world entity | % records matching source of truth |
| **Completeness** | Required data elements are present | % non-null values for required fields |
| **Consistency** | Same data across systems agrees | % matching records across systems |
| **Timeliness** | Data is current for its intended use | Latency from event to data availability |
| **Validity** | Data conforms to defined format/range | % records passing validation rules |
| **Uniqueness** | No unintended duplicate records | Duplicate rate per entity type |

### Data Quality Improvement Process

```
1. Profile → Understand current data quality state
2. Define → Set quality rules and thresholds
3. Monitor → Implement automated quality checks
4. Alert → Notify stewards of quality issues
5. Remediate → Fix root causes (not just symptoms)
6. Report → Track quality trends over time
```

### Data Quality Scorecard Template

| Domain | Dimension | Rule | Threshold | Current | Status |
|--------|-----------|------|-----------|---------|--------|
| Customer | Completeness | Email not null | > 95% | | |
| Customer | Uniqueness | No duplicate IDs | > 99.9% | | |
| Product | Accuracy | Price > 0 | 100% | | |
| Financial | Timeliness | < 1 hour latency | > 99% | | |

---

## Master Data Management (MDM)

### MDM Styles

| Style | Description | When to Use |
|-------|-------------|-------------|
| **Registry** | Index pointing to source systems | Quick wins, minimal disruption |
| **Consolidation** | Read-only golden record hub | Analytics, reporting |
| **Coexistence** | Bidirectional sync with sources | Multiple systems of record |
| **Centralized** | Single system of record | New implementations, clean slate |

### Common Master Data Domains

| Domain | Key Entities | Business Impact |
|--------|-------------|-----------------|
| **Customer** | Person, Organization, Account | Sales, marketing, support |
| **Product** | Product, SKU, Catalog, Category | Revenue, supply chain |
| **Employee** | Person, Role, Department, Location | HR, payroll, access |
| **Supplier** | Vendor, Contract, Location | Procurement, AP |
| **Financial** | Chart of accounts, Cost center | Reporting, compliance |
| **Location** | Address, Facility, Region | Operations, logistics |

### Entity Resolution Pattern

```
Source Records → Standardize → Match → Merge → Golden Record

Standardize: Normalize formats (phone, address, name)
Match: Deterministic (exact key) + Probabilistic (fuzzy matching)
Merge: Survivorship rules (which source wins for each attribute)
Golden Record: Single best version of each entity
```

---

## Data Mesh Principles

### Four Principles

| Principle | Description | Implementation |
|-----------|-------------|---------------|
| **Domain Ownership** | Data is owned by the business domain that produces it | Each domain team owns their data products |
| **Data as a Product** | Treat data as a product with consumers | SLAs, documentation, discoverability |
| **Self-Serve Platform** | Infrastructure that enables domain teams | Data platform team provides tools |
| **Federated Governance** | Decentralized governance with global standards | Domain-level policies, enterprise-wide interoperability |

### Data Product Design

```
A Data Product Must Have:
├── Data: The actual data (tables, events, files)
├── Code: Transformation, quality checks, serving
├── Infrastructure: Storage, compute, pipeline
├── Metadata: Schema, lineage, quality metrics, SLA
├── Documentation: Business context, usage guide
├── Access Control: Who can access and how
└── Owner: Named person accountable for quality
```

### Data Mesh vs. Data Lake vs. Data Warehouse

| Aspect | Data Warehouse | Data Lake | Data Mesh |
|--------|---------------|-----------|-----------|
| **Architecture** | Centralized, structured | Centralized, any format | Decentralized, domain-oriented |
| **Ownership** | Central data team | Central data team | Domain teams |
| **Governance** | Centralized | Centralized (often weak) | Federated |
| **Data Quality** | High (curated) | Variable (often low) | High (domain-owned SLAs) |
| **Schema** | Schema-on-write | Schema-on-read | Schema-on-write (per domain) |
| **Best For** | Structured analytics | Raw data exploration | Large organizations, many domains |

---

## Data Catalog & Metadata Management

### Data Catalog Components

| Component | Purpose | Examples |
|-----------|---------|---------|
| **Business Glossary** | Standard business terminology | "Revenue" = net revenue after returns |
| **Technical Metadata** | Schema, types, statistics | Table definitions, column types, row counts |
| **Data Lineage** | How data flows and transforms | Source → transformations → destination |
| **Data Classification** | Sensitivity and handling | Public, Internal, Confidential, Restricted |
| **Usage Metadata** | How data is accessed and used | Query frequency, popular tables, user access |
| **Quality Metadata** | Data quality scores and rules | Quality dimensions, rule results, trends |

### Data Classification Framework

| Level | Description | Handling | Examples |
|-------|-------------|----------|---------|
| **Public** | No restriction on access | No special controls | Marketing materials, public APIs |
| **Internal** | Organization members only | Standard access controls | Internal docs, non-sensitive reports |
| **Confidential** | Limited to authorized roles | Encryption, access logging | Financial data, employee records |
| **Restricted** | Strictly controlled | Encryption, MFA, monitoring, DLP | PII, PHI, payment data, trade secrets |

---

## Data Lifecycle Management

### Data Lifecycle Phases

| Phase | Activities | Governance Focus |
|-------|-----------|-----------------|
| **Create** | Data entry, system generation, acquisition | Quality at source, classification |
| **Store** | Database, data lake, archive | Security, backup, retention |
| **Use** | Query, analyze, report, share | Access control, purpose limitation |
| **Share** | Internal distribution, external sharing | Consent, agreements, anonymization |
| **Archive** | Long-term storage, reduced access | Retention compliance, cost optimization |
| **Destroy** | Secure deletion, decommission | Right to deletion, audit trail |

### Data Retention Framework

| Data Category | Retention Period | Legal Basis | Destruction Method |
|--------------|-----------------|-------------|-------------------|
| Financial records | 7 years | Tax/regulatory | Secure deletion + audit |
| Employee records | Employment + 7 years | Employment law | Secure deletion |
| Customer PII | As long as needed + 3 years | GDPR/CCPA | Anonymization or deletion |
| System logs | 90 days - 1 year | Security/compliance | Automated rotation |
| Backups | 30-90 days | Business continuity | Automated expiry |

---

## Data Governance Maturity Model

| Level | Name | Characteristics |
|-------|------|-----------------|
| 1 | **Initial** | No formal governance, ad-hoc, data silos |
| 2 | **Reactive** | Basic policies, some stewardship, issues drive action |
| 3 | **Proactive** | Governance program, data quality monitoring, cataloging started |
| 4 | **Managed** | Measured and managed, enterprise-wide, automation |
| 5 | **Optimized** | Continuous improvement, data-driven culture, AI-enabled governance |

### Maturity Assessment Dimensions

| Dimension | L1 | L3 | L5 |
|-----------|-----|-----|-----|
| **Organization** | No roles defined | Stewards assigned | Federated governance model |
| **Policies** | None documented | Core policies exist | Automated enforcement |
| **Data Quality** | Unknown | Monitored for key datasets | Proactive, AI-assisted |
| **Metadata** | None | Business glossary exists | Full catalog with lineage |
| **Architecture** | Siloed | Enterprise data model | Data mesh/fabric |

---

*Last Updated: 2026-02-14*


## Common Pitfalls

- Data quality metrics must be measured, not assumed — establish baselines before improvement programs
- Master data management scope must be bounded — trying to govern all data at once fails
- Data lineage documentation is a prerequisite for data quality — you can't fix what you can't trace

---

## Data Maturity Model

<!-- Sources: SuperNerb/Data-Maturity-Models, CMMI Data Management Maturity Model (DMMM). Added 2026-03-29. -->

A structured 5-level framework for assessing and improving an organization's data management capabilities across all dimensions. Use for baseline assessments, roadmap prioritization, and board-level reporting on data program progress.

---

### 5-Level Data Maturity Scale

| Level | Name | Characteristics | Business Symptoms |
|-------|------|-----------------|-------------------|
| **1** | **Initial / Ad Hoc** | No formal governance; data practices depend on individuals; spreadsheet-driven; no shared definitions | "Every team has their own version of the numbers"; constant data disputes in meetings |
| **2** | **Managed** | Basic policies documented; some stewardship roles exist; reactive quality management; per-project governance | Data quality issues are fixed after they cause problems; governance exists on paper but not in practice |
| **3** | **Defined** | Enterprise-wide standards; formal data stewards in each domain; metadata management program; business glossary active | Consistent definitions across business units; data issues escalated through known channels |
| **4** | **Quantitatively Managed** | Metrics-driven governance; automated data quality monitoring; full lineage tracking; data quality SLAs | Data quality is measured and reported; issues detected before they impact decisions |
| **5** | **Optimizing** | AI-augmented governance; continuous improvement culture; self-healing data pipelines; data literacy embedded in all roles | Data governance is invisible — quality and trust are defaults, not achievements |

**How to use the scale**: Assess each of the seven dimensions below independently (an organization can be Level 3 in data quality but Level 1 in data literacy). Use the dimension scores to create a heatmap and identify the highest-priority improvement areas.

---

### Assessment Framework: 7 Dimensions (Score 1-5 Each)

#### Dimension 1: Data Quality Management

| Score | Description |
|-------|-------------|
| 1 | No quality metrics; issues discovered by end users or in production |
| 2 | Some manual quality checks; basic validation rules in key systems |
| 3 | Documented quality rules; stewards responsible for quality in their domains; quarterly reporting |
| 4 | Automated quality monitoring; dashboards; SLAs with defined thresholds; issues auto-escalated |
| 5 | Predictive quality management; AI flags anomalies before they propagate; self-healing transformations |

#### Dimension 2: Metadata Management

| Score | Description |
|-------|-------------|
| 1 | No catalog; data definitions exist only in individual knowledge |
| 2 | Informal documentation; some data dictionaries in spreadsheets |
| 3 | Business glossary active; technical metadata captured for key datasets; data lineage partially documented |
| 4 | Enterprise data catalog deployed; lineage tracked end-to-end; catalog actively maintained |
| 5 | Automated metadata harvesting; AI-assisted classification; catalog is the single source of truth for all data consumers |

#### Dimension 3: Data Architecture

| Score | Description |
|-------|-------------|
| 1 | No enterprise data model; siloed systems; no integration layer |
| 2 | Point-to-point integrations; informal data flow documentation |
| 3 | Conceptual and logical data models exist; enterprise data architecture documented; standards defined |
| 4 | Physical models aligned with logical; reference architecture enforced; architecture review board active |
| 5 | Adaptive architecture (data mesh or data fabric); domain-driven design; architecture automatically validates conformance |

#### Dimension 4: Data Security and Privacy

| Score | Description |
|-------|-------------|
| 1 | No data classification; access managed informally; no privacy program |
| 2 | Basic access controls; some classification for regulated data |
| 3 | Enterprise classification framework; RBAC implemented; privacy impact assessments conducted |
| 4 | Automated classification and tagging; DLP active; privacy-by-design enforced in development |
| 5 | Zero-trust data access; continuous compliance monitoring; automated consent management |

#### Dimension 5: Master Data Management

| Score | Description |
|-------|-------------|
| 1 | No MDM; same entity has different IDs in different systems |
| 2 | Manual golden record reconciliation for key entities (ad hoc) |
| 3 | MDM program for 1-2 critical domains (customer, product); stewardship process defined |
| 4 | MDM covers all critical domains; automated entity resolution; golden records consumed by all systems |
| 5 | Real-time MDM; probabilistic matching with AI; golden records trusted across all business processes |

#### Dimension 6: Data Literacy and Culture

| Score | Description |
|-------|-------------|
| 1 | Data used only by analysts; business users distrust data; no training |
| 2 | Data champions in some teams; informal data education; executives request data but don't self-serve |
| 3 | Data literacy program exists; self-service analytics available; governance awareness training |
| 4 | Measurable data literacy improvement; business users self-serve; data-driven decision culture visible in leadership |
| 5 | Data literacy is a hiring criterion; governance participation is incentivized; continuous learning embedded |

#### Dimension 7: Data Operations

| Score | Description |
|-------|-------------|
| 1 | Manual data pipelines; no monitoring; outages discovered by users |
| 2 | Basic pipeline monitoring; manual incident response; ad hoc SLAs |
| 3 | Operational SLAs defined; incident response process documented; change management for data systems |
| 4 | DataOps practices: CI/CD for data pipelines; automated testing; SLA compliance reported |
| 5 | Fully automated DataOps; self-healing pipelines; predictive capacity management |

---

### Maturity Assessment Questionnaire

Use these 3-5 questions per dimension to score current state. Conduct interviews with data owners, stewards, and consumers.

**Data Quality Management**
1. How do you currently know when a data quality issue exists?
2. Do you have documented data quality rules and who owns them?
3. How long does it typically take to detect and resolve a data quality incident?
4. Are there published data quality SLAs for any datasets?
5. Who is accountable for data quality in each business domain?

**Metadata Management**
1. Where would a new employee go to find the definition of "revenue" or "customer"?
2. Do you have a business glossary and is it actively maintained?
3. Can you trace where a specific report metric comes from, end-to-end?
4. Is there a data catalog, and is it the system of record for data definitions?

**Data Architecture**
1. Do you have an enterprise data model? When was it last updated?
2. How are new data systems integrated? Is there an architecture review process?
3. What is the current integration topology (point-to-point, hub-and-spoke, event-driven)?
4. Are data flow diagrams maintained?

**Data Security and Privacy**
1. How is sensitive data identified and classified?
2. Who controls access to PII and how is that access reviewed?
3. Have you completed privacy impact assessments for all key data processes?
4. How do you ensure data minimization and purpose limitation?

**Master Data Management**
1. If the same customer appears in CRM, billing, and support — how do you know it's the same customer?
2. Are golden records maintained for any entities? Which ones?
3. How are duplicate records detected and resolved today?

**Data Literacy and Culture**
1. Can business users answer their own data questions without asking an analyst?
2. Is there a data literacy training program? Who participates?
3. How often do business leaders cite data in decision-making meetings?
4. Do people trust the data, or do they challenge it frequently?

**Data Operations**
1. How do you monitor data pipelines for failures or delays?
2. What is your process for releasing changes to data transformations?
3. Do you have SLAs for data freshness and availability?

---

### Maturity Heatmap Visualization Guide

After scoring each dimension, plot on a heatmap to communicate current state and target state to stakeholders.

```
Dimension                    | L1 | L2 | L3 | L4 | L5 |
-----------------------------|----|----|----|----|-----|
Data Quality Management      | ██ |    |    |    |    |  Score: 1.5
Metadata Management          |    | ██ |    |    |    |  Score: 2.0
Data Architecture            |    | ██ |    |    |    |  Score: 2.5
Data Security & Privacy      |    |    | ██ |    |    |  Score: 3.0
Master Data Management       | ██ |    |    |    |    |  Score: 1.0
Data Literacy & Culture      | ██ |    |    |    |    |  Score: 1.5
Data Operations              |    | ██ |    |    |    |  Score: 2.0

████ = Current state    ░░░░ = Target state (12-month horizon)
```

**Color coding (for slide presentations):**
- Level 1-2: Red — Significant risk to business operations
- Level 3: Amber — Managed, improvement in progress
- Level 4-5: Green — Competitive capability

**Usage in board reporting**: Present overall average score with trend (quarterly), highlight dimensions that improved and dimensions at risk, tie scores to business outcomes (e.g., "Level 1 in MDM is driving 12% data reconciliation overhead in financial reporting").

---

### Improvement Roadmap Template

Use to translate assessment findings into an actionable multi-quarter program.

| Dimension | Current Score | Target Score (12M) | Gap | Priority Initiatives | Estimated Timeline | Owner |
|-----------|--------------|-------------------|-----|---------------------|-------------------|-------|
| Data Quality Management | 1.5 | 3.0 | 1.5 | Implement quality rules for top 5 datasets; assign domain stewards | Q2-Q3 | CDO |
| Metadata Management | 2.0 | 3.5 | 1.5 | Deploy enterprise data catalog; migrate glossary | Q1-Q2 | Data Governance Lead |
| Data Architecture | 2.5 | 3.0 | 0.5 | Document current-state data flows; establish architecture review | Q2 | Data Architect |
| Data Security & Privacy | 3.0 | 4.0 | 1.0 | Automate classification for PII; implement DLP policies | Q3-Q4 | CISO / Data Governance |
| Master Data Management | 1.0 | 2.5 | 1.5 | Implement registry-style MDM for customer domain | Q3-Q4 | MDM Lead |
| Data Literacy & Culture | 1.5 | 3.0 | 1.5 | Launch data literacy training; enable self-service BI | Q2-Q3 | CDO / HR |
| Data Operations | 2.0 | 3.5 | 1.5 | Implement pipeline monitoring; define data SLAs | Q1-Q2 | Data Engineering |

**Roadmap phases:**

| Phase | Timeline | Focus | Milestone |
|-------|----------|-------|-----------|
| **Foundation** | Q1 (3 months) | Quick wins: catalog deployment, steward appointments, pipeline monitoring | First governance council meeting; baseline metrics published |
| **Consolidation** | Q2-Q3 (6 months) | Core programs: quality rules, MDM for top domains, literacy training | Quality dashboards live; golden records for Customer domain |
| **Optimization** | Q4+ (ongoing) | Automation, AI augmentation, culture embedding | Level 4 achieved in top 3 priority dimensions |

---

### Common Maturity Anti-Patterns

Patterns that consistently prevent organizations from advancing beyond Level 2.

**1. Governance Theater**
- **Symptom**: Data governance council meets, policies are written, nothing changes in practice
- **Root cause**: Governance has no authority — it is advisory, not accountable. Data owners ignore policies without consequence.
- **Fix**: Assign explicit accountability (data owners with performance objectives linked to data quality). Governance council needs teeth: budget authority, blocking capability on new initiatives.

**2. Tool-First Thinking**
- **Symptom**: Organization purchases a data catalog / MDM / quality platform, then expects the maturity level to rise automatically
- **Root cause**: Tools solve the last 20% of the problem. The first 80% is organizational (roles, processes, standards, culture). Tools amplify whatever behavior already exists.
- **Fix**: Define roles, processes, and standards before selecting tools. Use tools to enforce and scale what humans have already agreed on.

**3. Boil-the-Ocean Scope**
- **Symptom**: Program attempts to govern all data domains simultaneously; 18 months in, nothing is measurably better
- **Root cause**: Data governance scope set to "all data" without prioritization. No quick wins to build momentum.
- **Fix**: Start with 2-3 highest-value data domains (usually Customer, Revenue, and one operational domain). Demonstrate measurable improvement, then expand.

**4. Stewardship Without Empowerment**
- **Symptom**: Data stewards are appointed but have no time, authority, or tools to do their jobs
- **Root cause**: Stewardship is treated as an add-on role with no dedicated capacity. Stewards are accountable but not empowered.
- **Fix**: Define stewardship as a formal role with 10-20% dedicated time, clear authority to enforce quality rules, and tooling access.

**5. Measuring Activity, Not Outcomes**
- **Symptom**: Governance program reports on "number of policies written" and "catalog records created" rather than data quality scores and business outcomes
- **Root cause**: Output metrics are easier to produce than outcome metrics. Organizations report what they can measure, not what matters.
- **Fix**: Define outcome KPIs from day one: data quality scores per domain, time-to-resolve data incidents, percentage of decisions made with trusted data, reduction in data reconciliation effort.

**6. Ignoring Data Consumers**
- **Symptom**: Governance program focuses entirely on producers (engineering, IT) and ignores the business users who consume data
- **Root cause**: Governance programs are often IT-led and focus on technical compliance rather than business usability.
- **Fix**: Include data consumers in governance design. The business glossary, data catalog, and quality rules must be built for consumer needs, not just producer compliance.

---

## AI-Era Data Governance — Governing Data FOR Agents and Agents' Data Access

<!--
**Adapted from**:
  - C2PA Specification v2.3, Dec 2025 (open standard, c2pa.org) — content provenance assertions
  - EU AI Act, Regulation (EU) 2024/1689 Art. 10 (training-data provenance/scope) + Art. 50 synthetic-content disclosure, applicable 2026-08-02 (public/EU)
  - CSA Non-Human Identity & Agentic-AI Governance research, 2026 (CC-BY 4.0, cloudsecurityalliance.org)
**Source licence**: C2PA (open spec), EU AI Act (public EU law), CSA (CC-BY 4.0). Vendor capabilities (Databricks, Microsoft) cited as dated market evidence, NOT as framework.
**V2V refinements**:
- Recast the whole pack's human-consumer assumption explicitly as the gap this section closes (agents are now first-class data consumers).
- Authored as governance-POLICY (what the program must REQUIRE), with pointer-hops — not restatements — to the threat, design, identity, and copyright layers owned by other packs.
Added 2026-06-25.
-->

> **V2V caveat — policy layer only.** This section defines what the enterprise data-governance *program must require* in the agentic era. It does NOT implement enforcement (that's the data platform / security stack), threat-model it, or opine on legal exposure. Each of those is pointer-hopped below, not duplicated.

Every framework above this section assumes **humans are the primary data consumers** — access reviews, classification handling, and lineage were designed around human query patterns. As of 2026, autonomous AI agents query enterprise data at machine scale, acquire permissions dynamically at runtime, and spawn sub-agents — a consumption model the human-centric controls were not built for. Governance policy must extend to two new objects: **agents that consume governed data**, and **data that is consumed to build/run AI** (training, fine-tuning, RAG).

### 1. Agent Data-Access Governance (what the program must require)

Static, human-centric access models (periodic RBAC reviews, named-user grants) break when the consumer is an agent acting thousands of times per minute. The governance policy requirement is to shift from *"who can read this table"* to **runtime, contextual policy enforcement on what an agent may do with data in a given interaction**.

| Governance policy requirement | What it means at the program level |
|---|---|
| **Contextual / runtime authorization** | Access decisions evaluated per-action at runtime against current context (the invoking user's scope, the agent's registered data surface), not granted statically at provisioning |
| **Scope inheritance from the human principal** | An agent acting on a user's behalf must not exceed that user's data scope — row/column-level restrictions apply transparently so the agent sees only what the user could |
| **Action-level allow / deny / require-approval** | Governance covers not just read access but *what the agent does* — writing to sensitive domains or invoking high-impact actions can require human approval |
| **Per-action audit for non-human actors** | Every agent data access is attributable (agent identity → capability → query → result) and fed to the enterprise audit/compliance store |

**Dated market evidence (cited, not endorsed as a framework):** **Databricks Unity AI Gateway**, announced at Data + AI Summit on **2026-06-16**, extends Unity Catalog from governing data to governing what agents/models/MCP services do at runtime — including inspecting agent-generated queries against a registered data surface and rejecting unapproved tables/columns. **Microsoft Purview + Entra** route agent-action audit logs into the existing compliance store and extend conditional-access to agents. These illustrate that the *capability* exists in 2026; the governance program's job is to set the **policy** these tools enforce.

- **Pointer-hop → `agentic-security.md`** for the *threat model* (prompt injection, indirect data exfiltration, blast-radius of a compromised agent credential, MITRE ATLAS mapping). This section sets the access *policy*; that pack handles the *attack* surface. Do not duplicate.
- **Pointer-hop → `agent-identity.md`** for the *identity substrate* this depends on — agent as a fourth identity class, scoped time-bounded capability tokens, delegation with capability-narrowing, revocation lifecycle (Entra Agent ID / Cisco Agentic ZT / Google Agent Identity / CSA Agentic Trust Framework). An access policy is only as good as the identity it binds to.

### 2. Data-for-AI Provenance & Lineage (governing the data that builds AI)

When data is consumed to train, fine-tune, or ground (RAG) an AI system, governance must record **provenance** *and* **lineage** — they are distinct and both are now required:

- **Provenance** = proof of origin: where data came from, who collected it, consent/licensing basis, whether it is authentic. Answers *"is this data trustworthy and permitted for this use?"*
- **Lineage** = flow: how data moved and transformed across systems into the model. Answers *"how did this data get into the model?"* (the pack's existing lineage treatment, extended to the model boundary).

| Governance policy requirement | Anchor |
|---|---|
| **Documented training-data provenance, scope & characteristics** for high-risk AI | EU AI Act **Art. 10** — datasets must carry documented provenance, scope, and main characteristics |
| **Machine-readable synthetic-content / AI-generation disclosure** | EU AI Act **Art. 50**, applicable **2026-08-02** — deployers disclose AI-generated/manipulated content via visible marking + machine-readable metadata |
| **Provenance assertions on content assets** | **C2PA v2.3 (Dec 2025)** — extends content-provenance assertions beyond media to unstructured text / LLM outputs, including AI-training-data-use assertions; usable as the technical metadata standard the governance catalog records |
| **Lineage to the model boundary** | Extend existing data-lineage catalog entries so training/RAG datasets trace source → consent basis → transformations → which model consumed them |

- **Pointer-hop → `ip-law.md`** for the *copyright / legal exposure* of training data (Bartz transformative-but-piracy + the **$1.5B** preliminary settlement; Kadrey; Thomson Reuters v. Ross; USPTO guidance). This section governs the provenance *control*; that pack owns the *liability* analysis. A provenance record is the governance artifact; whether a given use is lawful is a counsel question — do not opine here.
- **Pointer-hop → `data-modeling.md`** (Architecture team) for the *schema/pipeline design* that physically captures lineage. Governance defines what must be recorded; that pack designs how the data is structured to record it.

### 3. Non-Human Identity (NHI) Governance — pointer

Agent data-access governance presupposes that agents have governed identities. The **CSA Non-Human Identity & Agentic-AI Governance** body of work (2026) frames NHI lifecycle (creation, scoping, rotation, revocation) as "the defining security gap of the agentic era." **Pointer-hop → `agent-identity.md`** (which already absorbs the CSA Agentic Trust Framework and the Entra/Cisco/Google identity patterns) — this pack does not re-author identity; it consumes it as the trust anchor for the access policies in Part 1.

---

*AI-era section added: 2026-06-25*
