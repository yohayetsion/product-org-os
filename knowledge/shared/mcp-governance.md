---
pack: mcp-governance
consumers:
- it-security-policy
- chief-architect
- ai-architect
- cio
- general-counsel
---
# MCP Governance Pack — V2V scaffolding for Model Context Protocol governance, controls, and assurance

**Version**: 1.0.0
**Type**: knowledge-pack (operationally sensitive, not legally sensitive)
**Owner**: chief-architect (primary) + it-security-policy (substantive co-owner)
**Last updated**: 2026-05-18 (Q2-3.2, Wave 1)
**Consumers**: `chief-architect`, `security-architect`, `cio`, `it-security-policy`, `compliance-officer`, `ai-architect`, `data-architect`, `tech-lead`, `enterprise-systems`, downstream skills `/ai-control-audit`, `/risk-analysis`, `/compliance-audit` (when `--framework=mcp` or `--framework=iso42001` or `--framework=csa-aicm`)
**Sibling pack (HOW counterpart)**: `mcp-architecture.md` (Q2-5.1, Wave 2 — covers transport, schema, auth mechanics, capability negotiation)
**Sensitive**: false (operationally sensitive — security exposure — but NOT legally sensitive per `sensitive-skill-guardrails.md` §2; downstream skills that produce legal/regulatory output derived from this pack ARE sensitive and inherit the sensitive-skill scaffolding from their own consuming pack such as `eu-ai-act-annex-iv.md` or `ai-bom.md`)
**Re-verification cadence**: quarterly (next: 2026-08-18; mandatory re-read on any new MCP risk class publication or material Anthropic MCP spec revision)
**token_budget_variance_rationale**: D14 case (a) + (b) — this pack is joint-authored by two seats (Chief Architect + IT Security Policy) AND consumed across four functions (Architecture, IT, Compliance, CIO). Multi-author + multi-consumer scope requires more breadth than the 2000-token nominal budget allows without losing the boundary contract clarity (M38) that is the central authoring constraint.

---

**Adapted from**:
- Anthropic Model Context Protocol specification (modelcontextprotocol.io) — the protocol specification. Initial public spec November 2024; substantial revisions through 2025-2026; >200 MCP servers in production by mid-2026.
- The **7 MCP risk classes** — a publicly documented governance framework (2026) covering: (1) data exfiltration, (2) unauthorized actions, (3) overprivileged access, (4) supply-chain risk, (5) missing audit trails, (6) privilege escalation, (7) shadow AI sprawl. Surfaced in security research and CISO advisory channels through Q1-Q2 2026 as MCP-server adoption outpaced governance maturity.
- Cloud Security Alliance **AI Controls Matrix (AICM)** — 18 control domains × 243 controls covering AI system governance, lifecycle, supply chain, data, identity, and operational controls. Published under CC-BY 4.0 by Cloud Security Alliance (cloudsecurityalliance.org).
- ISO/IEC **42001:2023** — AI Management Systems Standard, Annex A controls. Cited by clause and Annex A control reference only (commercial standard; full text requires ISO subscription).
- **NSA** "Model Context Protocol (MCP): Security Design Considerations for AI-Driven Automation" — Cybersecurity Information Sheet (CSI), doc U/OO/6030316-26 / PP-26-1834, "May 2026 Ver. 1.0," posted to defense.gov dated 2026-06-02 (media.defense.gov/2026/Jun/02/2003943289/-1/-1/0/CSI_MCP_SECURITY.PDF). NSA-led guidance.

**Source licence**:
- Anthropic MCP specification: per Anthropic publication terms (publicly documented; no formal OSS license restriction on reference and summary).
- 7 MCP risk classes: publicly documented framework pattern (no proprietary owner); cited by class name.
- CSA AICM: CC-BY 4.0 — attribution required on every derived control reference.
- ISO/IEC 42001:2023: commercial standard; cited by clause and Annex A control ID only.
- NSA CSI on MCP Security: U.S. Government work, public-domain (primary PDF gated/403 in research; existence + date corroborated by secondary sources — executivegov.com, aicerts.ai).

**V2V refinements**:
- Authored the **explicit boundary contract** with `mcp-architecture.md` (M38): this pack covers WHAT-CONTROLS; the sibling pack covers HOW-IT-WORKS. The boundary is enforced visibly via `Out of scope (see mcp-architecture.md)` notes at the end of every risk-class section, not just by authoring discipline.
- Cross-mapped the 7 MCP risk classes to **product-organization governance touchpoints**: `it-security-policy` owns operational policy; `cio` owns IT-portfolio approval; `compliance-officer` owns audit-trail-and-evidence; `chief-architect` + `security-architect` own design-level controls.
- Added **MCP-server approval workflow** guidance for product orgs adopting MCP at scale (registry + intake + review gates + lifecycle), not present in either source framework.
- Added **incident-response scaffolding** (NOT full procedure — scaffolding only): the playbook elements a product org must populate, with named owners per element.
- Cross-mapped 7 risk classes to specific CSA AICM control domains and ISO 42001 Annex A controls so that an AICM-aligned or 42001-aligned org can adopt MCP governance without re-authoring its control library.
- Added (2026-06 delta) an **NSA Cybersecurity Information Sheet** anchor — the first authoritative government MCP-security guidance — and mapped its three prescribed control families (schema-based input validation, full observability/logging, data-classification-zone alignment) onto this pack's existing 7-risk-class control set, with the data-classification-zone pattern surfaced as a new cross-cutting control.

---

**Boundary contract** (M38): This pack covers **WHAT-CONTROLS** — governance, controls, audit, approval, supply-chain, incident response, sensitive-skill applicability. For **HOW MCP works** — transport mechanics, JSON-RPC framing, message schema, capability negotiation, auth handshake mechanics, tool-call invocation flow, resource-read semantics — see the sibling pack `mcp-architecture.md` (Q2-5.1). Each risk-class section below ends with an explicit `Out of scope (see mcp-architecture.md)` note naming the mechanics deliberately deferred. The boundary should be visible to the reader, not just enforced by the authors.

---

## 1. Why MCP Governance Matters in 2026

The Model Context Protocol (MCP) reached production maturity through 2025 and accelerated through Q1-Q2 2026. By mid-2026, **>200 MCP servers** are in active production deployment across SaaS vendors, internal enterprise integrations, and developer tooling. The protocol's core design value — a standardized way for AI assistants to invoke external tools, read external resources, and operate on external systems with capability negotiation — is also the source of its governance challenge. Every MCP server is a privileged integration surface. A single misconfigured MCP server exposes more than a single misconfigured API integration would, because the AI assistant on the other end has latitude to combine tools in ways the server author did not anticipate.

Governance has lagged adoption. Through 2025, MCP-server deployment in enterprise environments was largely developer-driven and architecturally invisible to IT, security, and compliance functions. Through Q1-Q2 2026, security research and CISO advisory channels surfaced what is now called the **7 MCP risk classes** — a governance framework that names the recurring failure modes observed in production MCP deployments. The 7 classes are not novel attack vectors invented by MCP; they are familiar enterprise-security risks (data exfiltration, overprivileged access, supply-chain compromise) elevated by the protocol's standardization and latitude. The novelty is that one protocol concentrates these risks at one integration layer that IT, security, and compliance often do not yet see.

This pack assumes a product organization is adopting MCP at scale — running an MCP-server registry, integrating internal services via MCP, or consuming third-party MCP servers from vendors — and needs governance scaffolding before sprawl becomes architecturally invisible. The pack does NOT teach the protocol. The pack DOES name the controls a product org must operate to adopt MCP safely.

## 2. Sensitive-Skill Applicability

This pack is **operationally sensitive** (security exposure if controls fail) but **NOT legally sensitive** per `sensitive-skill-guardrails.md` §2. The pack itself is reference material; it does not require the legal-sensitive scaffolding (disclaimer block, Cannot Assess Without licensed counsel) that consuming legal/regulatory packs apply.

**However**: downstream V2V skills that combine this pack with a legal or regulatory pack — for example, a `/compliance-audit --framework=eu-ai-act` run that touches MCP-server integrations under Article 12 logging and traceability — DO inherit sensitive-skill scaffolding from the consuming pack (in that example, `ai-act-readiness.md` (Q2-1.A) or the planned `eu-ai-act-annex-iv.md` (Q2-3.4)). Cross-references to legally sensitive packs in §10 below are **mechanical**: this pack contributes the technical risk-class mapping; the legally sensitive pack contributes the disclaimer + jurisdiction + reviewer-checklist scaffolding.

ROI framing for **downstream sensitive skills** consuming this pack: **"drafting and triage"** of MCP-governance posture, NEVER "review acceleration" or "MCP control assessment in place of security review" per the Prohibited Phrasings enumeration in `roi-display.md`.

## 3. The 7 MCP Risk Classes — Governance Lens

The 7 risk classes are presented here through a governance lens (controls, ownership, evidence) rather than a mechanics lens (how the attack works at the protocol layer). Each section identifies: the risk in plain terms; the governance controls that mitigate it; the named V2V owner role accountable for the control; the CSA AICM domain(s) and ISO 42001 Annex A control(s) that map to the control set. Each section closes with an explicit `Out of scope (see mcp-architecture.md)` note.

### 3.1 Data Exfiltration

**Risk in plain terms**: An MCP server exposes resources (files, database rows, document content) that the AI assistant on the other end can read. If the server's resource-scoping is too broad, or if the AI assistant on the other end is induced (prompt injection, malicious user instruction) to read resources it should not, sensitive data leaves the integration boundary in ways the server author did not authorize.

**Governance controls**:
- **Resource scoping policy** — every MCP server in the registry declares the maximum resource scope it will expose; the registry rejects servers that declare unbounded scope without an explicit, owner-signed exception.
- **Data-classification gate** — MCP servers that expose resources containing Tier-1 / regulated data (PII, PHI, financial transaction data, source code with IP) require a separate review path with named approval from the data owner.
- **Egress logging** — every resource read invocation is logged with caller identity, server identity, resource identifier, and timestamp; logs retained per the org's audit-trail retention standard (see §3.5).
- **DLP integration** — for high-sensitivity data classes, the MCP server pipeline integrates with the org's data-loss-prevention controls before resource content reaches the AI assistant.

**Owners**: `security-architect` (control design) + `it-security-policy` (operational policy) + `compliance-officer` (audit evidence) + the data-owning function for Tier-1 / regulated data.

**CSA AICM mapping**: Data Security and Privacy (DSP) domain controls; Identity and Access Management (IAM) domain controls (specifically scope-of-access controls); Logging and Monitoring (LM) domain.

**ISO 42001 mapping**: Annex A.8 (Impact Assessment of AI systems on individuals and groups), A.10 (Third-party AI relationships — applicable when the MCP server is operated by a third party).

**Out of scope (see mcp-architecture.md)**: How the MCP transport's `resources/read` operation actually carries data, the JSON-RPC framing of resource responses, content-type negotiation, and the streaming semantics for large resources.

### 3.2 Unauthorized Actions

**Risk in plain terms**: An MCP server exposes tools — functions the AI assistant can invoke. If a tool's authorization model is misconfigured, or if the assistant is induced to invoke a tool the user did not intend, actions are taken that were not authorized. Unlike data exfiltration (which leaks information), unauthorized actions cause state changes — records written, payments triggered, notifications sent, infrastructure modified.

**Governance controls**:
- **Tool authorization gate** — every tool declared by an MCP server in the registry is classified as **read-only**, **state-changing-reversible**, or **state-changing-irreversible**. State-changing-irreversible tools (delete, send-payment, trigger-deployment, send-external-email) require human-in-the-loop confirmation at invocation time, not just at server-approval time.
- **Tool-scope minimization principle** — registry rejects MCP servers that expose state-changing-irreversible tools when a read-only or reversible alternative would meet the use case.
- **Invocation logging and alerting** — every state-changing tool invocation is logged with caller, server, tool, parameters, timestamp; irreversible-tool invocations also trigger near-real-time alerts to the operational on-call.
- **Rate-limiting and circuit breakers** — MCP servers enforce per-caller rate limits on state-changing tools; anomalous invocation patterns (volume spikes, off-hours bursts) trigger automatic circuit-break to the on-call.

**Owners**: `security-architect` + `chief-architect` (control design) + `tech-lead` (implementation oversight) + `it-security-policy` (operational policy) + the action-owning function for irreversible operations.

**CSA AICM mapping**: Application and Interface Security (AIS) domain; Identity and Access Management (IAM); Security Incident Management, eDiscovery, and Cloud Forensics (SEF) domain (for the alerting and circuit-breaker pattern).

**ISO 42001 mapping**: Annex A.9 (AI system lifecycle — specifically operational controls during AI system operation).

**Out of scope (see mcp-architecture.md)**: How the MCP transport's `tools/call` operation is structured, parameter-schema negotiation, tool-result error semantics, and the framing of multi-step tool sequences.

### 3.3 Overprivileged Access

**Risk in plain terms**: An MCP server is granted credentials, OAuth scopes, or API tokens with more privilege than the server's declared tools and resources require. When the AI assistant on the other end is induced to misbehave, or when the server itself is compromised, the blast radius is the full credential scope, not the declared scope. This is the **principle of least privilege** problem applied to MCP servers, which are often deployed with developer-convenience credentials that exceed production need.

**Governance controls**:
- **Credential scoping audit at intake** — every MCP server admitted to the registry has its credentials reviewed against its declared tools and resources; broader-than-declared credentials require explicit scope reduction or a documented exception with named approver and re-review date.
- **Per-server credential isolation** — MCP servers do not share credentials. Each server has its own credential with its own scope; revocation of one server's credential does not affect others.
- **Just-in-time credential elevation** — for MCP servers that need higher-privilege credentials only for specific operations, credentials are elevated just-in-time with attribution to the elevation request, not granted permanently.
- **Periodic credential review** — every MCP server's credential scope is reviewed at the cadence of the highest data classification it touches (Tier-1 quarterly, Tier-2 semi-annually, Tier-3 annually).

**Owners**: `security-architect` + `cio` (IT-portfolio level credential governance) + `it-security-policy` (operational policy) + the credential-issuing platform owner.

**CSA AICM mapping**: Identity and Access Management (IAM) domain (the canonical mapping); Governance, Risk, and Compliance (GRC) domain for the periodic review cadence.

**ISO 42001 mapping**: Annex A.6 (Internal organization — roles and responsibilities), A.10 (Third-party AI relationships).

**Out of scope (see mcp-architecture.md)**: How the MCP auth handshake actually authenticates the AI client to the server, OAuth flow specifics, token-refresh mechanics, and the protocol-level credential transmission.

### 3.4 Supply-Chain Risk

**Risk in plain terms**: An MCP server is often a third-party artifact — published by a SaaS vendor, an open-source maintainer, or a community contributor. The product organization adopting the server inherits the security posture of the server's authoring organization, its build pipeline, its dependency tree, and its release process. A compromise upstream (typo-squatted package, compromised maintainer credential, malicious update) becomes a compromise downstream.

**Governance controls**:
- **MCP-server provenance verification** — every MCP server in the registry has documented provenance: who publishes it, what release channel it ships through, what signing or attestation the release carries, and what fallback exists if the upstream is compromised.
- **SBOM and dependency review** — third-party MCP servers admitted to the registry have an SBOM (Software Bill of Materials) reviewed at intake; significant version updates trigger SBOM re-review.
- **Pinned versions in production** — production environments do not auto-update MCP servers from upstream; version updates go through the change-management process.
- **Vendor risk assessment for SaaS MCP servers** — MCP servers operated by SaaS vendors are subject to the org's standard vendor risk assessment (SOC 2 / ISO 27001 evidence, BAA if PHI is involved, data-residency review, breach-notification SLA).

**Owners**: `security-architect` + `compliance-officer` (vendor assessment evidence) + `cio` (IT vendor relationships) + `enterprise-systems` (registry and version pinning).

**CSA AICM mapping**: Supply Chain Management, Transparency, and Accountability (STA) domain (the canonical mapping); Governance, Risk, and Compliance (GRC) for the vendor assessment cadence.

**ISO 42001 mapping**: Annex A.10 (Third-party AI relationships — explicit third-party provenance and accountability obligations).

**Out of scope (see mcp-architecture.md)**: How MCP server release packaging is structured, transport-level integrity verification of server responses, and the protocol-level handshake that establishes server identity.

### 3.5 Missing Audit Trails

**Risk in plain terms**: MCP servers operating without consistent, retained, query-able logs produce no evidence of what happened when an incident occurs. Audit trail gaps are an evidence problem first (regulators and customers cannot answer the question "what did your AI assistant do with my data on date X") and a forensics problem second (the org's own incident response cannot reconstruct the sequence of events that led to a compromise).

**Governance controls**:
- **Logging completeness standard** — every MCP server in the registry meets a minimum logging standard: caller identity, server identity, operation type (resource read / tool call / prompt), operation identifier (resource URI / tool name / prompt name), parameters (with sensitive parameter redaction policy applied), timestamp (with timezone), result status (success / error / partial), and correlation identifier across multi-step operations.
- **Log retention** — logs retained per the org's audit-trail retention standard, with retention tied to the highest data classification the server touches (often 7 years for regulated data; jurisdiction-specific).
- **Log query-ability** — logs land in a query-able store (SIEM, security data lake, or equivalent) with index on caller, server, tool, timestamp; logs that are written but not query-able are evidence in name only.
- **Audit-trail integrity** — logs are tamper-evident (append-only or signed); a compromised MCP server cannot silently rewrite its own audit history.

**Owners**: `security-architect` + `it-security-policy` (logging standard) + `compliance-officer` (retention and evidence) + `enterprise-systems` (log infrastructure).

**CSA AICM mapping**: Logging and Monitoring (LM) domain (the canonical mapping); Security Incident Management, eDiscovery, and Cloud Forensics (SEF) for the incident-evidence path; Audit Assurance and Compliance (AAC) for retention.

**ISO 42001 mapping**: Annex A.9 (AI system lifecycle — logging during operation), Clause 9 (Performance evaluation — monitoring, measurement, analysis, and evaluation).

**Out of scope (see mcp-architecture.md)**: How the MCP transport layer carries operation identifiers, the format of MCP server response metadata, and the protocol-level correlation identifier semantics across multi-step operations.

### 3.6 Privilege Escalation

**Risk in plain terms**: An attacker (or a compromised MCP server) uses one privilege as a stepping stone to another. The escalation path on MCP often runs through tool composition (a tool that should be read-only is induced via crafted parameters to write), through credential mixing (one server's credentials are used to invoke another server's tools), or through chained sessions (the AI assistant's session context carries a state-changing intent from a compromised earlier call into a later trusted call).

**Governance controls**:
- **Inter-server isolation** — MCP servers cannot directly invoke other MCP servers under the same caller identity; cross-server flows go through the orchestrating AI assistant under that assistant's authorization context, with the cross-server intent explicit.
- **Session scope minimization** — AI assistant sessions are scoped to the minimum tool and resource set required for the user's declared task; broader sessions require explicit user opt-in or a new session.
- **State-change preconditions** — state-changing tools that depend on prior read operations declare their preconditions; the precondition state is verified at invocation time, not inherited from session context that may have been tainted by earlier compromised operations.
- **Anomaly detection on session graphs** — sessions that compose tools in patterns outside the declared use-case profile (e.g., read-then-write-then-external-send) trigger review.

**Owners**: `security-architect` (control design) + `chief-architect` (cross-server architecture) + `it-security-policy` (operational policy) + `compliance-officer` (anomaly evidence retention).

**CSA AICM mapping**: Identity and Access Management (IAM) domain; Threat and Vulnerability Management (TVM) domain (for the anomaly detection control); Application and Interface Security (AIS) for the precondition pattern.

**ISO 42001 mapping**: Annex A.9 (AI system lifecycle — operational controls), Clause 8 (Operation — operational planning and control).

**Out of scope (see mcp-architecture.md)**: How MCP session context is structured at the transport layer, the protocol-level semantics of multi-server orchestration, and the schema for cross-server capability negotiation.

### 3.7 Shadow AI Sprawl

**Risk in plain terms**: MCP servers are easy to spin up. A developer connects an AI assistant to a useful internal database in an afternoon. The integration works. It is never registered with IT, never reviewed by security, never assessed for compliance, never logged in any audit-able place. Over months, hundreds of these integrations accumulate. The product org has no inventory of which AI assistants can reach which internal systems, what data flows through, who authorized any of it, or what the blast radius would be if any one of them were compromised. **This is the governance failure that makes the other six risk classes invisible.**

**Governance controls**:
- **MCP-server registry as the system of record** — every MCP server operating in production has a registry entry; an MCP server without a registry entry is, by policy, not authorized to operate. The registry entry is the precondition for credential issuance, network access, and log-store onboarding.
- **Discovery sweep cadence** — the org runs periodic discovery sweeps (network telemetry, AI-assistant configuration telemetry, developer-tooling telemetry) to surface unregistered MCP servers and bring them into the registry or sunset them.
- **Approval workflow with friction calibrated to risk** — see §4 below. Low-risk servers go through a lightweight intake; high-risk servers go through full review. The point is not to slow developers down; the point is to make the path of least resistance flow through registration.
- **Sunset policy** — MCP servers that fall out of use are removed from the registry and have their credentials revoked; the registry is not a graveyard of historical entries.

**Owners**: `cio` (IT-portfolio accountability — this is the seat that owns "we know what's running") + `it-security-policy` (registry policy) + `chief-architect` (architectural integration of the registry into developer workflow) + `enterprise-systems` (registry tooling).

**CSA AICM mapping**: Governance, Risk, and Compliance (GRC) domain (the canonical mapping — shadow IT / shadow AI is fundamentally a governance gap); Supply Chain Management, Transparency, and Accountability (STA) for the unregistered-third-party-server case; Logging and Monitoring (LM) for the discovery telemetry.

**ISO 42001 mapping**: Clause 6 (Planning — addressing risks and opportunities, AI objectives), Annex A.6 (Internal organization — clear roles and responsibilities including for shadow-AI detection).

**Out of scope (see mcp-architecture.md)**: How MCP server discovery actually works at the transport layer, the protocol-level service-discovery semantics, and any auto-registration handshake mechanics.

---

## 4. MCP Server Approval Workflow

Product organizations adopting MCP at scale need a registered approval workflow before sprawl becomes architecturally invisible (§3.7 above). This section describes the scaffolding; the org's actual workflow tooling lives outside this pack.

### 4.1 Intake

Every MCP server proposed for production deployment files an intake record with: server name and purpose; publisher (internal team or third party); declared tools and their classifications (read-only / state-changing-reversible / state-changing-irreversible per §3.2); declared resources and their data classifications (per §3.1); credentials required and their scope (per §3.3); provenance and supply-chain attestation (per §3.4); logging endpoint and retention (per §3.5); inter-server interaction needs (per §3.6); proposed sunset date.

### 4.2 Risk tiering at intake

Intake records are tiered by the highest-risk attribute:
- **Tier 1 (highest)** — touches regulated data (PII, PHI, financial), exposes state-changing-irreversible tools, OR runs in production-customer-facing systems.
- **Tier 2 (medium)** — touches Tier-2 internal data, exposes state-changing-reversible tools, OR runs in internal production systems.
- **Tier 3 (lower)** — read-only on non-sensitive data, OR runs in developer/staging environments only.

### 4.3 Review path by tier

- **Tier 1** — full review: `security-architect` design review + `it-security-policy` operational review + `compliance-officer` evidence review + data-owner approval + named human approver from IT leadership (`cio` or delegate). Re-review at the cadence of the data classification (quarterly for Tier-1).
- **Tier 2** — partial review: `security-architect` or `it-security-policy` review (one or the other, not both) + automated control checks against the registry standard. Re-review semi-annually.
- **Tier 3** — lightweight intake: automated control checks against the registry standard + named developer-owner accountability. Re-review annually or on material change.

### 4.4 Lifecycle gates

Servers move through: **Proposed → Approved → Active → Under Review → Sunset / Retired**. Movement between states is logged. A server in **Under Review** state (e.g., during quarterly re-review or after an incident) may have its operational status held pending review outcome.

### 4.5 Anti-pattern — rubber-stamping

The single most common failure mode of an MCP-server approval workflow is rubber-stamping: every intake is approved within hours, no review evidence is recorded, the workflow exists in name only. The workflow is only valuable if Tier-1 reviews actually take days to weeks and reject some proposals. Approval velocity is a leading indicator that requires monitoring: if Tier-1 approval median time is <48 hours, the review is not happening.

---

## 5. ISO 42001 + CSA AICM Mapping

This section consolidates the per-risk-class mappings from §3 into a single matrix for governance leaders adopting the pack into an existing ISO 42001 AIMS or CSA AICM control library. The mapping is mechanical: each MCP risk class points to the canonical CSA AICM domain(s) and ISO 42001 Annex A / clause references. Existing control authoring under those domains is reused; the contribution of this pack is the **MCP-specific application** of the controls.

| MCP Risk Class | CSA AICM Domain(s) | ISO 42001 Anchor |
|---|---|---|
| 3.1 Data Exfiltration | DSP (Data Security and Privacy); IAM (scope-of-access); LM (Logging and Monitoring) | A.8 (Impact Assessment), A.10 (Third-party) |
| 3.2 Unauthorized Actions | AIS (Application and Interface Security); IAM; SEF (Incident Management and Forensics) | A.9 (AI system lifecycle — operational) |
| 3.3 Overprivileged Access | IAM (canonical); GRC (review cadence) | A.6 (Internal organization), A.10 (Third-party) |
| 3.4 Supply-Chain Risk | STA (Supply Chain, Transparency, and Accountability); GRC (vendor assessment) | A.10 (Third-party AI relationships) |
| 3.5 Missing Audit Trails | LM (canonical); SEF (incident evidence); AAC (Audit Assurance and Compliance) | A.9 (lifecycle — logging), Clause 9 (Performance evaluation) |
| 3.6 Privilege Escalation | IAM; TVM (Threat and Vulnerability Management); AIS (precondition pattern) | A.9 (lifecycle), Clause 8 (Operation) |
| 3.7 Shadow AI Sprawl | GRC (canonical); STA (unregistered third-party); LM (discovery telemetry) | Clause 6 (Planning), A.6 (Internal organization) |

**Mapping completeness note**: The 7 MCP risk classes cleanly cover the operational-security exposure of MCP adoption. They do NOT cover:
- The legal/regulatory exposure of AI systems built ON MCP-mediated integrations (that maps to `ai-act-readiness.md` (Q2-1.A), and the planned `eu-ai-act-annex-iv.md` (Q2-3.4) for the documentation evidence side, and `ai-bom.md` (Q2-3.5) for AI Bill of Materials).
- The model-risk side (training data, model evaluation, hallucination control); that maps to AI-architecture and ML-engineering packs separately.
- The identity / agent-identity layer (which agent is invoking which MCP server with which authority); that maps to `agent-identity.md` (Q2-3.1, Wave 1 sibling).

## 5.5 2026-06 Delta Update (as of 2026-06-06) — NSA MCP Security Guidance

In **May 2026 (Ver. 1.0)**, the **NSA** published a Cybersecurity Information Sheet (CSI), **"Model Context Protocol (MCP): Security Design Considerations for AI-Driven Automation"** (doc U/OO/6030316-26 / PP-26-1834), posted to defense.gov dated **2026-06-02**. This is the first authoritative government-issued MCP-security guidance and gives this pack an external, non-vendor anchor for its governance posture.

**The NSA's framing.** The CSI characterizes MCP as **"flexible and underspecified,"** drawing an explicit analogy to the early web — a powerful, rapidly-adopted protocol whose security model has not caught up to its deployment. This matches §1 of this pack (governance has lagged adoption) and §3.7 (shadow AI sprawl is the governance failure that makes the rest invisible).

**The three control families the NSA prescribes**, mapped onto this pack's existing controls:

| NSA Control Family | What It Requires | Maps to this pack |
|---|---|---|
| **(1) Schema-based input validation** | Validate inputs against a declared schema on every per-tool / per-model invocation. | Strengthens §3.2 (Unauthorized Actions) tool-authorization gate and §3.6 (Privilege Escalation) state-change-precondition control — validation happens at invocation time, per tool, not just at server-approval time. |
| **(2) Full observability / logging** | Log invocation parameters, caller/server identities, and **cryptographic hashes of outputs**. | Directly reinforces §3.5 (Missing Audit Trails). The output-hash requirement is a tighter bar than §3.5's current logging-completeness standard — adopt it: log a cryptographic hash of each tool/resource output so audit trails are tamper-evident on content, not just on invocation metadata. |
| **(3) Data-classification-zone alignment** | Segregate tools that touch sensitive / regulated data into distinct classification zones. | Extends §3.1 (Data Exfiltration) data-classification gate from a per-server review path into a **cross-cutting architectural control**: tools touching Tier-1 / regulated data run in segregated zones, not co-mingled with non-sensitive tools. Reviewer should treat zone segregation as a registry-standard attribute, not an ad-hoc design choice. |

**New cross-cutting control — data-classification zones.** Where this pack previously handled data classification as a §3.1 gate (review path for Tier-1 servers), the NSA guidance elevates it to an architectural segregation principle. Product orgs adopting MCP at scale SHOULD define data-classification zones and assign each registered MCP server (and its tools) to a zone at intake (§4.1), so blast radius is bounded by zone, not by the whole MCP surface. This is additive to §4.2 risk tiering: the tier determines review depth; the zone determines runtime segregation.

**Confidence caveat (preserved).** The primary defense.gov PDF returned **HTTP 403** during research. The CSI's **existence and date are High confidence** (corroborated by multiple secondary sources — executivegov.com, aicerts.ai). However, **co-authorship is UNVERIFIED** — whether the CSI is NSA-only or joint with CISA / Five Eyes partners could not be confirmed against the gated primary source. This pack therefore frames the guidance as **"NSA-led"** and does **not** assert joint authorship. A reviewer with access to the primary PDF should confirm the authoring agencies before any external citation that names co-authors.

**Cross-reference**: `mcp-architecture.md` (Q2-5.1) — the NSA's "schema-based input validation" control is a HOW-mechanics concern (per-invocation schema enforcement at the protocol layer) that the architecture sibling elaborates; this pack carries the WHAT-CONTROLS governance framing per the M38 boundary contract.

Sources: NSA CSI primary (media.defense.gov/2026/Jun/02/2003943289/-1/-1/0/CSI_MCP_SECURITY.PDF, gated/403); executivegov.com/articles/nsa-model-context-protocol-deployment; aicerts.ai/news/nsa-tightens-ai-context-protocols-security-with-new-guidance/.

## 5.6 2026-06-24 Delta Update (MCP 2026-07-28 RC — auth hardening + migration governance)

**Adapted from**: MCP 2026-07-28 Specification Release Candidate, blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ (authors David Soria Parra + Den Delimarsky, Lead Maintainers; published 2026-05-21, RC locked 2026-05-21, final dated 2026-07-28). SEP + RFC references per the same post.
**Source licence**: Apache-2.0 (open protocol) / publicly documented; RFC 9207 per IETF (public).
**V2V refinements**:
- Mapped the RC's six authorization-hardening SEPs onto this pack's §3.3 (Overprivileged Access) credential-governance controls.
- Added a **migration-governance** control: a protocol-version-bump is itself a registry event requiring re-review, extending §3.4 (Supply-Chain) version-pinning + §4.4 (lifecycle gates).
- Cross-referenced the HOW-mechanics to `mcp-architecture.md` 2026-06-24 delta per the M38 boundary contract (this pack = WHAT-CONTROLS; auth mechanics live in the architecture sibling).

This section is additive to §5.5 (NSA guidance), which remains correct. The RC's auth changes reinforce that delta's posture and add credential-handshake hardening.

### A. Authorization hardening (six SEPs) — governance read

- **`iss` validation per RFC 9207 (SEP-2468).** Clients MUST validate the `iss` parameter on authorization responses — mitigates an authorization-server mix-up attack class more prevalent in MCP's single-client/many-server pattern. **Governance action:** add "supplies `iss` on auth responses" to the §4.1 intake checklist for any remote-auth server.
- **OIDC Dynamic Client Registration `application_type` declared (SEP-837).** Clients declare desktop/CLI vs web at DCR time, reducing brittle-auth misconfiguration that pushed teams toward overbroad workaround credentials (a §3.3 driver).
- **Credential-to-issuer binding + re-registration on migration (SEP-2352).** Maps to §3.3 per-server credential isolation — a migrated resource cannot silently reuse a credential minted by a different authorization server.
- **Refresh-token flow (SEP-2207); scope accumulation on step-up clarified (SEP-2350); `.well-known` discovery suffix clarified (SEP-2351).** Tighten the just-in-time elevation + periodic-review controls in §3.3.

**Net for §3.3:** the RC moves MCP auth toward standards-aligned OAuth/OIDC, making the credential-scoping/isolation/review controls enforceable against well-understood primitives. The control set does not change; its enforceability improves.

**Out of scope (see mcp-architecture.md):** OAuth/OIDC flow mechanics, `_meta` credential transport, the `iss`/`issuer` handshake, DCR request/response shapes — architecture sibling §4 + 2026-06-24 delta.

### B. Migration governance — a protocol-version bump is a registry event

- **Registry attribute: protocol version per server.** Every registered server declares its MCP protocol version (`2025-11-25` vs `2026-07-28`). Extends §3.4 pinned-versions discipline to the protocol version.
- **Migration re-review (extends §4.4 lifecycle gates).** A server moving to the `2026-07-28` core transits Active → Under Review → Active, confirming: stateless-core conformance, routing-header emission, client-side `iss` validation, `-32602` error handling, Tasks-extension migration. At least the depth of the server's original intake tier (§4.3).
- **Deprecation-window tracking.** Roots/Sampling/Logging carry 12-month removal windows (SEP-2577). The registry tracks dependents and surfaces the window so migration is planned, not incident-driven.
- **Anomaly note (extends §7.4 credential drift):** the stateless core means "any request lands on any instance" — per-instance allowlisting / IP-pinning controls that assumed sticky sessions must be revisited; flag in the migration re-review.

**Out of scope (see mcp-architecture.md):** deployment-topology mechanics (stateless functions, serverless/edge fit, `ttlMs`/`cacheScope`, W3C Trace Context) — architecture sibling 2026-06-24 delta §A + §E.

## 6. Incident Response Scaffolding

This section is scaffolding, NOT a full incident-response procedure. The org's actual IR procedure lives in the security function's runbooks. The contribution here is the list of MCP-specific playbook elements the org must populate, with named owners per element.

### 6.1 Detection
- **Anomalous tool invocation patterns** — owner: `security-architect` + SOC if present. Trigger: rate-limit breach, off-hours irreversible-tool invocation, cross-server orchestration outside use-case profile.
- **Audit-trail gap detection** — owner: `compliance-officer` + `it-security-policy`. Trigger: missing logs for an MCP server that should be producing them, log-store integrity alarms.
- **Discovery-sweep findings** — owner: `cio` + `it-security-policy`. Trigger: unregistered MCP server detected in production telemetry.

### 6.2 Containment
- **Per-server credential revocation** — owner: credential-issuing platform owner. Action: revoke the server's credential; verify revocation propagates to running sessions.
- **Server quarantine** — owner: `enterprise-systems` + `security-architect`. Action: move the server's registry state to **Under Review**; block new invocations; preserve audit trail.
- **Session termination** — owner: AI-assistant-platform owner. Action: terminate active sessions that touched the compromised server; preserve session-context evidence.

### 6.3 Eradication
- **Root cause analysis on the server** — owner: server publisher (internal team or vendor escalation contact for third-party). Action: identify whether the compromise was at the server, in its credentials, in its supply chain, or in a downstream AI assistant inducing misuse.
- **Cross-server impact assessment** — owner: `security-architect`. Action: determine whether the compromise reached other registry entries via privilege escalation (§3.6) or credential sharing (which §3.3 forbids — but verify).

### 6.4 Recovery
- **Server re-onboarding** — owner: full review path per §4.3 Tier-1 (regardless of original tier, since the server has been compromised).
- **Affected-party notification** — owner: `compliance-officer` + `privacy-counsel` (if PII was exfiltrated) + `general-counsel`. The breach-notification obligation is jurisdiction-specific and lives in legal/regulatory packs, NOT here.

### 6.5 Lessons learned
- **Post-incident review** — owner: `chief-architect` + `it-security-policy`. Action: identify whether the incident exposes a gap in the registry standard, the approval workflow, or the discovery sweep; update §3, §4, or §6 accordingly. Update this pack's `Last updated` field and Re-verification cadence.

**Out of scope (see mcp-architecture.md)**: The transport-level forensic artifacts (JSON-RPC frame captures, MCP session state dumps) used by IR investigators; the protocol-level mechanics of session termination and credential revocation propagation.

---

## 7. Anti-Patterns / Common Failures

Authoring discipline names the failure modes V2V has seen in product orgs adopting MCP without governance scaffolding. The mitigation pattern is named in each entry.

### 7.1 Governance bolted on after sprawl
**Pattern**: The org adopts MCP for 12-18 months without a registry. Discovery sweeps then surface 80-200 servers nobody can attest to. Governance is attempted retroactively; most servers cannot pass intake (no provenance documentation, no SBOM, no documented credential scope). The org chooses between "shut them all down" (operationally painful) and "grandfather them" (governance abandoned at inception).
**Mitigation**: The registry is the precondition for operation from day one. New MCP integrations cannot get network access or credentials without a registry entry. Discovery sweeps run from week one, not month 18.

### 7.2 Audit-trail blind spots
**Pattern**: MCP servers log to console / stdout / a developer-local file that nobody can query. The logs technically exist. They contribute zero evidentiary value.
**Mitigation**: Logging-to-a-query-able-store is a registry standard (§3.5). A server that cannot meet it is not approved. The query-able store is named in the intake record; rejected if it is "developer laptop" or "service container ephemeral storage."

### 7.3 Approval-workflow rubber-stamping
**Pattern**: Tier-1 servers are approved within hours of intake. No review evidence is recorded. The workflow exists in name only. When an incident reveals a misconfigured server, the post-incident review surfaces that the server was approved without any meaningful examination.
**Mitigation**: Approval velocity is itself monitored. Tier-1 median approval time <48 hours is a leading indicator that review is not happening. Approval evidence (named reviewer, what was checked, what was found) is required to register a server as Active; absence blocks state transition.

### 7.4 Credential drift after approval
**Pattern**: A server is approved with a narrow credential scope. Months later, a developer needs the server to do one more thing. The credential is broadened to enable it. The intake record is never updated. The server's actual privilege now exceeds its declared privilege. When discovery sweeps surface this, the gap may be months old.
**Mitigation**: Credential changes trigger a re-review through the same path as the original approval. The registry tracks declared-vs-actual credential scope and alerts on drift. Quarterly re-review for Tier-1 catches drift that slipped through.

### 7.5 The "internal-only" loophole
**Pattern**: Third-party MCP servers go through vendor risk assessment. Internal MCP servers (built by the company's own developers) are presumed safe and skip review. The internal server's developer-convenience credentials are broader than its declared scope; nobody caught it because internal servers do not go through the same intake.
**Mitigation**: One intake workflow for all MCP servers. Internal-vs-third-party is a tier attribute, not a review-skip attribute. Internal Tier-1 servers go through the same review depth as third-party Tier-1.

### 7.6 The "governance is IT's problem" handoff
**Pattern**: Security designs the controls. IT operates the registry. Compliance retains the audit evidence. Architecture is not in the loop. The controls do not survive contact with the architectural realities of how developers actually use MCP (cross-server flows, session composition, capability negotiation), because Architecture was not consulted.
**Mitigation**: This pack is **joint-owned** by Chief Architect + IT Security Policy precisely to prevent this handoff. Pattern-1 consultation with `cio` (IT-portfolio level) on registry tooling and approval workflow. The MCP-server approval workflow lives at the intersection of Architecture (cross-server design), IT (registry and credentials), Security (controls), and Compliance (evidence); cutting any one out is the failure pattern.

---

## 8. V2V Cross-References

**Sibling Q2-3 packs**:
- **`agent-identity.md` (Q2-3.1)** — the identity layer (which agent invokes which MCP server with which authority) interlocks with §3.3 (Overprivileged Access) and §3.6 (Privilege Escalation). CSA risk classes 1-3 + 6 are mitigated at that pack's identity layer; this pack handles risk classes 4, 5, 7.
- **`csa-ai-controls-matrix.md` (Q2-3.3)** — the AICM control library §3 + §5 map to; AICM is the canonical source for control wording and evidence packaging.
- **`eu-ai-act-annex-iv.md` (Q2-3.4)** — Annex IV documentation evidence requirements that MCP-server audit trails (§3.5) and registry records (§3.7 + §4) contribute to for high-risk AI systems consuming MCP integrations.
- **`ai-bom.md` (Q2-3.5)** — AI BOM §2.6 (Third-Party Components) inherits this pack's MCP-server governance posture; AI BOM §3.1 cross-maps MCP-server SBOM (§3.4) into the broader AI Bill of Materials evidentiary substrate.

**Sibling Q2-5 packs (M38 boundary contract)**:
- **`mcp-architecture.md` (Q2-5.1)** — **explicit M38 boundary partner**. The HOW counterpart to this pack's WHAT-CONTROLS. Every `Out of scope (see mcp-architecture.md)` note in this pack is a forward reference; every `Out of scope (see mcp-governance.md)` note in that pack is the reciprocal reference. Boundary enforced visibly from both sides per M38.
- **`a2a-architecture.md` (Q2-5.2)** — A2A is the agent-to-agent collaboration protocol; the governance pattern in this pack applies to A2A peer-call boundaries as well as MCP integration boundaries, not just MCP. Registry, approval workflow, and audit-trail standards extend.
- **`agentic-security.md` (Q2-5.3)** — MITRE ATLAS v5.4 tactic and OWASP LLM Top 10 v2.0 risk mapping at the agentic-system level; MCP-server compromise (§3.1-§3.6 risk classes) maps to specific OWASP items (LLM03 Supply Chain, LLM06 Excessive Agency). That pack cites this pack for layered governance on CSA risk classes 4, 5, 7.
- **`subagent-driven-development.md` (Q2-5.4)** — sub-agent driven dev consumes MCP as its plumbing layer; this pack's governance scaffolding (registry, approval workflow, audit) applies equally to sub-agent tool use, not just MCP integrations generally.

**Upstream regulatory anchors (existing)**:
- **`ai-act-readiness.md` (Q2-1.A)** — Article 12 logging and traceability obligations for high-risk systems consuming MCP integrations.
- **`hr-ai-governance.md` (Q2-1.B)** — when an MCP server touches HR-AI workflows, FCRA + Title VII + AEDT + TRAIGA obligations layer on top of MCP governance.

**Existing packs**:
- `compliance-frameworks.md` — control-to-obligation cross-map; AICM domains identified in §5 trace through that pack to specific regulatory obligations.
- `security-frameworks.md` + `security-policy-templates.md` — broader enterprise-security policy context that MCP-specific policy slots into.
- `it-governance.md` — `cio`-owned IT-portfolio governance the MCP-server registry (§3.7, §4) plugs into.

**Anti-Patterns overlap with `mcp-architecture.md` §7**: this pack's Anti-Patterns §7.1-§7.6 cover governance-layer failures (registry sprawl, audit blind spots, rubber-stamping, credential drift, internal-only loophole, IT-handoff). The architecture sibling's §7.1-§7.7 cover architecture-layer failures (capability-negotiation bypass, timeout handling, session expiration, stdio-for-production, namespace collision, error-layer conflation, statefulness drift). M38 boundary is preserved — no governance failure pattern is duplicated in the architecture pack and vice versa.

## 9. Operating Principle

> *MCP governance is the difference between adopting an AI integration protocol and operating it safely at enterprise scale. The protocol does the integration; the governance does the trust.*
