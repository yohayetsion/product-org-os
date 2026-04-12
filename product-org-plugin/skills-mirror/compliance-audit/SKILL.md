---
name: compliance-audit
description: Produces a control-level compliance-readiness gap assessment of an organization or initiative against a named regulatory framework, as a drafting and triage aid for human review, not a certification
  opinion.
argument-hint: '[organization or initiative name] --framework [soc2|gdpr|iso27001|hipaa|israeli-ppl|nist-csf|pci-dss|custom-{name}]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: legal-compliance
  skill_type: task-capability
  owner: compliance-officer
  primary_consumers:
  - ext-legal
  - product
  - ext-corpdev
  - ext-it
  sensitive: true
---
# /compliance-audit

## Purpose

`/compliance-audit` produces a control-level compliance-readiness gap assessment of an organization, business unit, product, or specific initiative against a named regulatory framework. For each control in the framework's catalog, it maps the control to the org's processes and systems, assesses what is in place versus what the control requires, identifies evidence available versus missing, and produces a prioritized remediation roadmap plus an evidence inventory. It is a **drafting and triage aid**, not a certification opinion, not an attestation, not a formal audit report, and not legal advice.

What it IS: an analytical ground-truth pass that names which controls a framework requires, maps them to the org's actual processes, and surfaces the gaps between "what the framework expects" and "what the org has in place today" — framed as gaps to verify and remediate, never as conclusions about compliance status.

What it is NOT: a certification audit, an attestation report, a replacement for a licensed auditor (CPA firm for SOC 2, accredited registrar for ISO 27001, QSA for PCI DSS), a legal opinion on regulatory exposure, or a pass/fail grade. Every finding is a hypothesis grounded in specific source documents and a specific control requirement, for a human (Compliance Officer + domain counsel + external auditor when relevant) to verify.

The skill is **parameterized by `--framework`**. The core method — scope → control mapping → gap analysis → remediation roadmap → evidence inventory — is identical across frameworks. Only the control catalog changes. This is a design choice, not a limitation: adding a framework should be a data update (a new adapter in the `compliance-frameworks` knowledge pack), not a skill rewrite.

---

## When to Use

Invoke `/compliance-audit` when you need to:

- Assess an organization's readiness for an upcoming certification audit (SOC 2 Type I/II, ISO 27001, HIPAA, PCI DSS) before engaging the external auditor
- Produce a gap analysis for an initiative that deploys into a new regulated environment (e.g., a SaaS product deploying at a regulated bank, a health app entering HIPAA territory, a consumer product entering the EEA)
- Prepare a compliance-readiness exhibit for M&A diligence (target-side or acquirer-side)
- Re-audit after a material change (new jurisdiction, new data flow, new sub-processor, new AI use case, new customer segment) in Update mode
- Triage a breach-response posture against the framework that governs the breach notification
- Prepare a control-level checklist for Compliance Officer before a substantive review by external auditor or counsel
- Stress-test a pre-certification compliance posture with an adversarial pass (`--mode adversarial`)

## When NOT to Use

Do NOT use `/compliance-audit` when:

- You need a **contract clause-by-clause review** → use `/contract-review` (Phase 3 A1). `/contract-review` audits a CONTRACT; `/compliance-audit` audits an ORG or INITIATIVE against a framework. Different unit of analysis.
- You need a **public-facing privacy policy disclosure audit** → use `/privacy-policy-audit` (Phase 3 A3). A3 audits a POLICY DOCUMENT for disclosure sufficiency; A4 audits the ORG's CONTROLS against the underlying regulatory framework. A3 is a subset of A4 when `--framework gdpr` is selected, but A3 is faster, narrower, and more focused for the disclosure-document case.
- You need an **NDA-specific triage** → use `/nda-triage` (Phase 3 A2)
- You need an **initiative-level risk landscape across six domains** → use `/risk-analysis` (Phase 3 A5). A5 is upstream — it asks "what could hurt us across legal, commercial, operational, regulatory, financial, reputational?" A4 is downstream of A5 for the regulatory domain — it takes the regulatory exposure A5 surfaced and maps it to a specific framework's control catalog.
- You need a **contract negotiation stress test** → use `/contract-stress-test` (Phase 3 A7)
- You need an **AI system governance posture assessment** across applicable frameworks → use `/ai-regulatory-audit` (Phase 5A C1.2b, future). A4 audits the org against a HORIZONTAL framework (SOC 2, GDPR, HIPAA). C1.2b audits an AI SYSTEM's governance posture across whichever frameworks apply to it. A company with no AI still needs A4. A company with AI but no horizontal regulatory exposure still needs C1.2b. They are **complements, not competitors**. When an AI system falls inside a regulated org, both skills run — A4 at the org level, C1.2b at the system level.
- You need a **licensed legal opinion** on regulator exposure or enforceability → engage outside counsel; the skill does not substitute.
- You need a **formal attestation report** for a customer, regulator, or investor → the skill produces gap analysis input to an auditor; the auditor produces the attestation.

The skill deliberately sits DOWNSTREAM of `/risk-analysis` (which surfaces the regulatory domain as one of six) and UPSTREAM of external auditor engagement (which issues the formal opinion). It is where the framework's control language meets the org's actual processes.

---

## Boundary Statement (Critical)

The compliance-audit skill sits at a specific intersection and MUST not drift into adjacent skills' territory. The boundary is load-bearing because drift creates duplicate findings, inconsistent severity, and confused ownership.

| Skill | Unit of Analysis | Primary Question |
|---|---|---|
| `/risk-analysis` (A5) | Initiative or deal | "What could hurt us across six domains?" |
| `/contract-review` (A1) | A specific contract | "What does this contract say, clause by clause?" |
| `/privacy-policy-audit` (A3) | A public-facing policy document | "Does the policy disclose what the regs require?" |
| **`/compliance-audit` (A4)** | **An org or initiative vs a framework** | **"What controls does the framework require, and what does the org have in place?"** |
| `/ai-regulatory-audit` (C1.2b, future) | An AI system | "What is the AI system's governance posture across applicable frameworks?" |

A4 is the **horizontal-framework, control-level** audit. It is bounded on four sides:

1. **Up** against A5: A4 does not re-do A5's six-domain risk landscape. If A5 surfaced a regulatory concern, A4 takes that concern as input and maps it to a specific framework's controls. Where A4 findings overlap with A5 findings, A4 explicitly notes the overlap and frames the A4 finding at the control level, not the deal level.
2. **Down** against contract and policy: A4 does not audit a specific contract's clauses (that's A1) or a specific policy document's disclosures (that's A3). If an A4 finding requires a contract clause change, A4 points at A1; if it requires a policy disclosure change, A4 points at A3.
3. **Sideways** against C1.2b: A4 audits horizontal frameworks applied to whatever the org does. C1.2b audits AI systems specifically. When an org has AI in scope for a horizontal framework (e.g., GDPR Art. 22 applied to an AI scoring product), A4 covers the GDPR control and C1.2b covers the AI system's specific governance posture. They do not overlap — A4 asks "is there a DPIA on record?" and C1.2b asks "is the AI system's DPIA methodology defensible?"
4. **Outward** against external auditors: A4 is a pre-audit gap assessment. It does not issue attestation language, does not opine on certification readiness as a legal conclusion, and does not replace a CPA/QSA/registrar engagement. Its output feeds the auditor's work, not the other way around.

When a user asks A4 to do something in the adjacent territory, the skill refuses and points at the correct sibling skill. This conversion of scope drift from invisible to blocking is the same pattern A3 uses against `/data-mapping`, `/dpia`, `/cookie-tracker-audit`, and `/dpa-review`.

---

## Modes

### Create (default)

Run a full framework-scoped audit on an organization, initiative, or product. Produces a new compliance-audit output file following the structure in the Output section.

```
/compliance-audit Legionis --framework soc2
/compliance-audit "AXIA Bank Discount deployment" --framework israeli-ppl-bank-discount
/compliance-audit SKYMOD --framework gdpr
/compliance-audit "acquisition target X" --framework custom-diligence-pack
```

### Update

Re-audit after a material change — new control evidence documented, a control remediated, a new jurisdiction or sub-processor added, or a framework revision. Pass the path to the existing audit output.

```
/compliance-audit update AXIA/Product/compliance-audit-israeli-ppl-bank-discount-2026-04-11.md
```

Update mode preserves the finding numbering (adds 7a, 7b rather than renumbering), marks resolved findings with `~~strikethrough~~` plus a one-line reason, and keeps a `## Changelog` at the bottom of the file noting what the org moved on.

### `--mode adversarial`

Invokes Pattern 5 Adversarial Review from `delegation-protocol.md`. A fresh-context adversarial agent (typically `@general-counsel` or a peer `@compliance-officer` instance) stress-tests the current audit findings without seeing the drafter's rationale. The pattern caps at two iterations. A named human tiebreaker must be specified BEFORE the review starts.

Use adversarial sub-mode ONLY when:

- The audit is pre-certification and the cost of a missed control gap is material (audit findings, certification delay, customer escalation)
- The audit is for an M&A diligence exhibit and the cost of a missed finding is material (deal risk, post-close indemnity)
- The audit is for a regulated deployment (bank, health system, critical infrastructure) and a missed control could delay go-live
- A named human tiebreaker is available
- The audit is near-final, not still evolving in scope

```
/compliance-audit "AXIA Bank Discount deployment" --framework israeli-ppl-bank-discount --mode adversarial --tiebreaker "Yohay Etsion"
```

For early-stage readiness assessments, routine annual maintenance, and low-stakes triage, use default Create mode with Pattern 1 Consultation for specialist input instead.

---

## Inputs Required

The skill MUST collect the following before producing output. If any are missing, it asks the user rather than guessing.

| Input | Required | Example |
|---|---|---|
| **`--framework`** | Yes | `soc2` / `gdpr` / `iso27001` / `hipaa` / `israeli-ppl` / `nist-csf` / `pci-dss` / `custom-{name}` |
| Organization or initiative name | Yes | "AXIA Bank Discount deployment" |
| Scope statement | Yes | "Employee-monitoring SaaS deployed at a Bank of Israel-regulated bank for an 8,600-employee workforce; cloud LLM inference; Israeli data residency" |
| Source documents | At least one | Plans, policies, prior audits, control matrices, contracts, architecture diagrams, prior risk analyses |
| Jurisdictions of operation | Yes (may be multi) | "Israel primary; cross-border considerations with EU residue and U.S. Delaware parent" |
| Stage | Yes | "preparing for first audit" / "pre-certification" / "annual maintenance" / "breach response" / "acquisition diligence" / "pre-deployment readiness" |
| Stakeholder list | If known | "Asaf Massuri (AXIA CTO), Yohay Etsion (Fractional CPO), Dan (Bank Discount sponsor)" |
| Known gaps the user wants examined | If any | "We know SOC 2 is not started; we want to know what can ship before a bridge letter is in place" |
| Tiebreaker (adversarial mode only) | Yes if adversarial | "Yohay Etsion" |

If jurisdiction is unknown, the skill makes a defensible assumption based on the documents and flags it explicitly in the output — it does NOT silently pick.

If the framework is unknown to the skill at v1.0.0 (the `compliance-frameworks` knowledge pack has not yet been authored — Phase 5A C1.5), the skill supports **inline framework definition**: the user provides a framework name plus a brief control list, OR the user uses a canonical name (soc2, gdpr, iso27001, hipaa, israeli-ppl, nist-csf, pci-dss) and the skill relies on Compliance Officer's domain knowledge of that framework as of the skill's authoring date. For custom frameworks, the user MUST provide the control catalog in the input.

---

## Framework Adapter Pattern

The skill is parameterized by `--framework`. The core method is identical across frameworks; only the control catalog changes.

### How it works

1. The skill loads a **framework adapter** for the named framework. An adapter is a structured control catalog: a list of control families, each with a list of controls, each with a control reference (e.g., "CC6.1"), a control statement (what the control requires), control objectives, and evidence expectations.
2. The skill maps each control to the org's processes and systems using the source documents and input context.
3. For each control, the skill produces one finding (or a small cluster of related findings) at the control level: control reference → what the control requires → what the org has in place vs what is missing → evidence available vs missing → severity → suggested remediation.

### Framework adapter source (v1.0.0 and beyond)

At v1.0.0, the skill ships BEFORE the `compliance-frameworks` knowledge pack exists. The pack is scheduled for Phase 5A C1.5. Until the pack is authored, the skill uses the following fallback mechanism:

- **Canonical named frameworks** (soc2, gdpr, iso27001, hipaa, israeli-ppl, nist-csf, pci-dss): the skill relies on Compliance Officer's domain knowledge of the framework as of the skill's authoring date. This is adequate for gap-assessment work but is NOT a substitute for an up-to-date adapter in the knowledge pack.
- **Custom frameworks** (`--framework custom-{name}`): the user provides the control catalog inline as part of the input. The skill uses the user-provided catalog verbatim. The user is responsible for the catalog's accuracy.
- **Hybrid frameworks** (e.g., `israeli-ppl-bank-discount` bundling PPL + Directive 361 + labor law): the user defines the bundle in the input, listing which underlying frameworks are in scope. The skill treats the bundle as a custom framework and runs the audit against the bundled scope.

### Adding a framework is a data update, not a skill rewrite

When the `compliance-frameworks` knowledge pack is authored in Phase 5A C1.5, adding a new framework becomes:

1. Author an adapter file (`compliance-frameworks/{framework-name}.md`) with the structured control catalog
2. No changes to this skill's code
3. The skill picks up the new adapter automatically

This design choice is why the skill ships at v1.0.0 even though the knowledge pack does not exist yet. The v1.0.0 limitation is "no structured adapter library"; the v1.0.0 capability is "runs the audit method against any framework the user can describe or name." The capability is useful now; the limitation is remediated in Phase 5A.

### `current-status.md` sidecar pattern for date-sensitive regulatory content

Regulatory frameworks evolve. EU AI Act milestones, Israeli PPL amendments (Amendment 13 arrived in 2024, Amendment 14 pending), Bank of Israel directive revisions, EDPB opinions, CNIL guidance — all of these have dates that age fast. Inlining specific dates in an audit output creates stale artifacts.

The skill uses a **sidecar pattern** for date-sensitive content: when an audit output references a regulatory status that may change (e.g., "EU AI Act Article 10 applies from Q3 2026 per the staged commencement schedule"), the reference points at a sidecar file stored next to the audit output:

```
AXIA/Product/
  compliance-audit-israeli-ppl-bank-discount-2026-04-11.md          ← audit output
  compliance-audit-israeli-ppl-bank-discount-2026-04-11-status.md   ← sidecar
```

The sidecar holds: (1) current status of each referenced regulatory instrument with date and source, (2) known upcoming changes with effective dates, (3) citations that must be refreshed at next audit. When the audit is re-run in Update mode, the skill updates the sidecar first, then updates the audit findings against the refreshed status. This keeps the audit findings from drifting when the underlying regs move.

Sidecar pattern is inherited from the Phase 5A C1.5 proposal (originally for `/ai-regulatory-audit`), applied here because the same date-sensitivity problem applies.

---

## Output Structure

Every `/compliance-audit` output conforms to `sensitive-skill-guardrails.md` Section 3. Structure is non-negotiable; substantive findings vary per audit.

### 1. Disclaimer + UPL Guardrail Block (top)

Verbatim block from `sensitive-skill-guardrails.md` Section 3.1, with `{jurisdiction}` filled in. For compliance-specific framing, the block is adapted as follows (same structure, compliance-appropriate language):

> ⚠️ **Not legal or audit advice.** This output is a drafting and triage aid generated by a product-organization skill, not counsel, not an external auditor, and not a licensed compliance attestor. No attorney-client or auditor-client relationship is created by its production or use. Compliance questions are jurisdiction-specific and fact-specific; findings below are control-level gap hypotheses against published framework requirements, not legal conclusions about compliance status. Do not rely on this output as the sole basis for any certification, regulatory, or material compliance decision. Any contested matter, any regulator-facing submission, any certification audit, and any material decision with regulatory consequences require review by a licensed attorney qualified in the relevant jurisdiction AND engagement with an accredited external auditor (CPA firm for SOC 2, accredited registrar for ISO 27001, QSA for PCI DSS, or equivalent).
>
> **Jurisdictions in Scope:** {e.g., "Israel + U.S. Delaware residue"}. Findings are framed against the named framework's control requirements. If your operations extend to additional jurisdictions or additional regulated activities, treat every finding below as a hypothesis to re-verify per regime.

### 2. Audit Metadata Block

A small labeled block under the disclaimer with:

- **Framework**: the `--framework` value (e.g., `israeli-ppl-bank-discount`)
- **Framework Adapter Version**: date or version of the adapter used. At v1.0.0 with no knowledge pack, this is "inline definition, 2026-04-11" or "canonical name, Compliance Officer domain knowledge 2026-04-11"
- **Organization / Initiative**: what is being audited
- **Scope Statement**: the user-supplied scope
- **Jurisdictions in Scope**: named, explicit, including any cross-border considerations
- **Stage**: preparing-for-audit / pre-certification / annual-maintenance / breach-response / acquisition-diligence / pre-deployment-readiness
- **Source Documents**: enumerated with paths
- **Audit Date**: today
- **Audit Version**: 1.0.0 initial; 1.1, 1.2 etc. for updates
- **Sidecar Status File**: path to the `-status.md` sidecar, if one exists

### 3. `## Control Mapping` (short summary)

A short summary (half a page, not a multi-page table) of how the framework's control areas map to the org's processes and systems. The purpose is to make the frame explicit before the findings start. Format: a bullet list grouped by control family, with a one-line summary per family stating what is in scope and who owns it internally.

The Control Mapping is NOT the findings — it is the setup for the findings. If the mapping reveals that an entire control family is out of scope (e.g., "payment card processing controls are N/A because the org does not touch PAN"), the mapping says so, and no findings are produced for that family.

### 4. `## Findings`

Numbered list. Each finding is at the **control level** (not the deal level like A5, not the clause level like A1). Each finding has:

- **Control reference**: the specific framework citation (e.g., "SOC 2 CC6.1", "GDPR Art. 32", "ISO 27001 A.5.15", "HIPAA 164.308(a)(1)(i)", "Bank of Israel Directive 361 §4.2", "PPL Section 17B", "Data Security Reg 5777-2017 §5(b)(3)"). For bundled frameworks, the citation names the underlying regime and its specific clause.
- **Control family**: one of the framework's control families (e.g., "Access Control", "Audit Logging", "Outsourcing Management", "Employee Monitoring Notice")
- **What the control requires**: a grounded paraphrase of the control statement, not a fabrication. If the skill cannot state the control requirement precisely, it says so and flags the control for human verification.
- **What the org has in place**: grounded in the source documents with specific citation (e.g., "bank-discount-israeli-regulatory-compliance-plan.md Section 2.3"). If nothing is in place, say `[ABSENT]` and name where it would normally live.
- **Evidence available vs missing**: what artifacts exist (documents, logs, config snapshots, attestations) vs what is missing. Evidence gaps are often as important as control gaps.
- **Severity**: `P0` (material gap — must be addressed before the audit, certification, or deployment proceeds), `P1` (important — should be addressed or explicitly accepted with written rationale), `P2` (nice-to-have — track but does not block)
- **Suggested remediation**: specific next step. Acceptable forms: `Verify {X} against {Y}`, `Document {process}`, `Engage {specialist counsel} on {control}`, `Produce evidence artifact: {name}`, `Escalate to {role} for accept-with-risk decision`.

Findings are tagged by control family. Missing-control findings (controls the framework requires that are not in place at all) are tagged `[ABSENT]` and are often more important than present-but-incomplete controls. Cross-control findings (e.g., a data-residency commitment in one control area conflicts with a sub-processor disclosure in another) are tagged `[CROSS-CONTROL]`.

**Framing rule (non-negotiable)**: Findings are framed as **"control gap vs {framework} {control reference} requirements"** — never as **"the org is non-compliant with {framework}."** The former is a drafting-and-triage observation; the latter is a legal/auditor conclusion the skill is not authorized to make. Example:

- CORRECT: "Control gap vs Bank of Israel Directive 361 §4.2 (Outsourcing Material Classification): the source documents do not indicate whether Bank Discount's compliance team has classified AXIA as a material outsourcing arrangement. Suggest confirming the classification with the Bank Discount compliance contact before the technical deep-dive. If material, heightened requirements apply (pre-notification to regulator, enhanced oversight, exit plan). Engage @compliance-officer for the classification process and @general-counsel if the classification is contested."
- INCORRECT: "The org is non-compliant with Bank of Israel Directive 361 because the material outsourcing classification has not been completed."

**Cross-reference rule**: If an A5 or A1 finding already surfaced the same underlying issue, the A4 finding MUST name the prior finding explicitly (e.g., "A5 Finding 8 surfaced this at the deal level; the A4 control-level remediation builds on that prior work"). A4 does not duplicate — it reframes at the control level and extends with control-specific remediation and evidence requirements.

### 5. `## Remediation Roadmap`

A prioritized action list, grouped by P0 → P1 → P2. Each action names:

- The finding(s) it addresses (by finding number)
- The owner (role or specific named individual from the stakeholder list)
- An effort bucket — **S / M / L** only, never specific hours or days (per `no-estimates.md`). S ≈ one person-week or less, M ≈ multiple person-weeks, L ≈ person-months or more. If the effort is impossible to bucket without implementation estimates the skill is not authorized to produce, the action uses `[TBD]` and notes what input would unlock the estimate.
- Dependencies on other actions or on external parties

The roadmap is NOT a project plan. It is a prioritized list of actions that feeds the org's real project planning. Specific dates, FTE assignments, and implementation sequencing are out of scope for this skill and belong to `@program-manager` or the internal compliance PMO.

### 6. `## Evidence Inventory`

A two-column list: "existing evidence that supports compliance" and "missing evidence that must be created or obtained." Each evidence item names:

- The control it supports (by reference)
- The evidence type (document / log / config / attestation / third-party report / training record)
- The owner
- For missing items: the gap and the action needed to close it

The Evidence Inventory is the feeder list for an external auditor's evidence request. It makes the "what do we actually have" question visible before the auditor asks it.

### 7. `## Reviewer Checklist`

Explicit sign-off items. Minimum checklist:

- [ ] Framework scope confirmed against the actual regulatory environment the org operates in
- [ ] Jurisdictions in scope confirmed against the actual operations footprint
- [ ] Source documents enumerated and verified (no fabricated sources)
- [ ] Every P0 finding addressed or explicitly accepted-with-risk by named approver
- [ ] Every P1 finding triaged (addressed, accepted, or escalated)
- [ ] Every `[ABSENT]` finding either remediated with a control design or explicitly waived with documented reason
- [ ] Every `[CROSS-CONTROL]` finding verified — the interaction works in both directions
- [ ] Overlapping findings with A5 (risk analysis), A1 (contract review), or A3 (privacy policy audit) reconciled — no inconsistent severity
- [ ] Cross-references to sibling skills (A1, A3, C1.2b) followed up where a finding points at them
- [ ] Sidecar status file reviewed for date-sensitive items, updated if stale
- [ ] Counsel engaged for items in "Cannot Assess Without"
- [ ] External auditor engagement status confirmed (SOC 2 CPA firm, ISO 27001 registrar, etc.) if a certification path is in play
- [ ] Stakeholder list confirmed — each control family has a named internal owner

### 8. `## Cannot Assess Without Licensed Counsel or External Auditor`

Explicit list of what the skill deliberately did NOT opine on. Two categories:

- **Cannot Assess Without Licensed Counsel** — jurisdiction-specific enforceability questions, novel regulatory interpretation, labor-law and works-council-specific consultation requirements, cross-border transfer enforceability, securities-law implications, tax treatment of compliance-driven restructurings
- **Cannot Assess Without External Auditor** — formal attestation of control effectiveness, certification readiness as a binding opinion, control design adequacy for the specific framework's auditor expectations, evidence sufficiency as judged by an accredited auditor

Minimum 5 items total per output; more for multi-jurisdiction or regulated-industry deployments.

Format each as a single line: "Enforceability of {clause} in {jurisdiction}" / "Formal control-effectiveness opinion under {framework}" / "Evidence adequacy for {auditor type} audit" / etc.

### 9. (Optional) Changelog (update mode only)

If update mode, a `## Changelog` section at the bottom listing what the org moved on since the prior audit, which findings were resolved, which became moot, and which new findings appeared (e.g., from a new sub-processor, new jurisdiction, framework revision).

---

## Method

The skill's audit pass follows this sequence. Order matters because later steps depend on the output of earlier ones.

### Step 1 — Scope

Confirm what is in scope, what is out, what jurisdictions apply, and what framework the audit is run against. Read the scope statement and the source documents. Build an internal map of:

- The organizational boundary (which entity, which business unit, which product)
- The systems and processes in scope (which data flows, which third parties, which facilities, which personnel categories)
- The jurisdictions in scope (including secondary jurisdictions with residue exposure — e.g., a Delaware parent of an Israeli operating sub has residue Delaware exposure even if the operating activity is in Israel)
- The framework scope (which control families apply, which are out of scope and why)
- The stage (readiness, pre-cert, annual maintenance, breach, diligence, pre-deployment)

If the scope is unclear, the skill asks for clarification. It does NOT guess.

### Step 2 — Control Mapping

Load the framework adapter (from the knowledge pack, from canonical domain knowledge, or from the user-supplied inline definition). For each control family in the framework, map the framework's controls to the org's processes and systems using the source documents and input context.

Produce a short summary (the `## Control Mapping` section of the output) that names, for each control family in scope:

- Which org processes / systems the family maps to
- Who owns the family internally
- Whether the family is in scope or N/A for this audit (with a one-line reason for N/A)

Control Mapping is the setup for the findings, not the findings themselves.

### Step 3 — Gap Analysis

For each in-scope control, assess what the org has in place. Three states per control:

- **In place** — the source documents show a control that meets the framework requirement. Produce a finding ONLY if there is a verification concern or an evidence gap.
- **Partial** — the source documents show a control that partially meets the requirement (e.g., the control exists but evidence is thin, or the control covers some systems but not others). Produce a finding at P1 or P0 depending on materiality.
- **Absent** — no control is evident in the source documents. Produce a finding tagged `[ABSENT]` at P0 or P1 depending on materiality. Absence is often more important than weakness.

Findings MUST be grounded in something actually present in the source documents. Fabricated findings are not permitted. If the skill cannot find ground for a concern, it either asks the user for clarification or moves the item to "Cannot Assess Without."

Cross-reference findings with A5 (risk analysis) and A1 (contract review) if those outputs exist for the same initiative. Where overlap exists, the A4 finding reframes at the control level and names the prior finding explicitly.

### Step 4 — Remediation Roadmap

Sequence the findings by P0 → P1 → P2 and by dependency. For each action, name the owner, the effort bucket (S/M/L), and the dependencies. The roadmap is a prioritized action list, not a project plan.

Actions must be specific and actionable. "Improve access control" is not a roadmap action. "Document the quarterly access review process for the M365 AXIA connector (Directive 361 §5.3 evidence requirement); owner Asaf Massuri; effort S; depends on the architecture diagram (pending)" is a roadmap action.

### Step 5 — Evidence Inventory

For each control family in scope, enumerate what evidence exists (grounded in the source documents) and what is missing. This feeds the external auditor's evidence request when the audit graduates from readiness assessment to formal audit.

The Evidence Inventory is often the first thing an external auditor asks for. Producing it upfront accelerates the eventual certification cycle by weeks.

### Step 6 — Write "Cannot Assess Without"

Written BEFORE finalizing findings. If an item goes here, it cannot also appear as a confident finding. The section is how the skill makes its scope explicit.

Two sub-categories: Licensed Counsel (legal questions) and External Auditor (formal opinion questions). Both are mandatory for a complete output.

---

## Delegation Patterns Available

### Default: Pattern 1 Consultation

When a specific control family needs specialist input, `/compliance-audit` spawns a consultation per `delegation-protocol.md` Pattern 1:

| Trigger | Spawn |
|---|---|
| Data flow touches employee or customer PII, cross-border transfer, Art. 9 sensitive data | 🔒 Privacy Counsel |
| IP licensing, trademark, copyright controls | 📜 IP Counsel |
| AI system governance overlaps with a framework control (GDPR Art. 22, EU AI Act, Colorado AI Act) | 🤖 AI Architect (cross-system boundary with C1.2b territory) |
| Novel jurisdictional question or regulator posture uncertainty | ⚖️ General Counsel |
| Labor law, works council consultation, employee monitoring notice | 👔 Employment Counsel |
| Control implementation details (IT governance, ITIL, system-level controls) | 💻 IT Governance (CIO) or 🖥️ IT Security Policy Specialist |
| SOC 2 readiness, ISO 27001 scope, HIPAA-specific controls | ⚖️ Compliance Officer (self-consultation for a peer instance, or an external CPA firm liaison when the gap approaches certification audit territory) |
| Enterprise risk register, insurance alignment | 🛡️ Risk Manager |
| Contract-level remediation where a control gap requires a clause change | 📄 Contracts Counsel (and the user is directed to run `/contract-review` for the specific contract) |

Consultations are attributed in the Findings section: "I consulted 🔒 Privacy Counsel on the cross-border transfer finding, who noted that the adequacy assessment for Israel→EU flows must account for Amendment 13 PPL alignment." Ownership of the compliance audit stays with Compliance Officer.

### On Request: Pattern 5 Adversarial Review (`--mode adversarial`)

Use for pre-certification audits, M&A diligence exhibits, and regulated-deployment readiness assessments where the cost of a missed gap is material. Requires all four Pattern 5 guardrails: named human tiebreaker before the review starts, fresh-context spawn of the adversarial agent, maximum two iterations, and role separation (drafter does not see adversarial findings until after they are produced).

Do NOT use Pattern 5 for routine annual maintenance audits, early-stage readiness assessments, or when the goal is collaborative improvement (that is Pattern 3 Review).

---

## Quality Gates

`/compliance-audit` is a sensitive skill. It ships only after passing the two-pass publication gate defined in `sensitive-skill-guardrails.md` Section 4:

- **Pass 1 — Scaffolding Check** — 📋 Director of Legal Affairs verifies the structure (disclaimer, framework and jurisdictions fields, Control Mapping, Findings, Remediation Roadmap, Evidence Inventory, Reviewer Checklist, Cannot Assess Without, frontmatter, ROI framing, delegation citation, first-principles authoring, boundary statement, framework adapter pattern). 15 minutes, binary GO / REWORK.
- **Pass 2 — Substantive Check** — ⚖️ General Counsel verifies the legal reasoning, severity thresholds, control-family coverage, cross-skill boundary correctness (vs A1, A3, A5, C1.2b), jurisdiction handling, framework adapter integrity, and edge cases. **72-hour SLA** for subsequent-similar Phase 3 legal skills; the template pattern was validated by A5 `/risk-analysis`, A1 `/contract-review`, and A3 `/privacy-policy-audit`, so A4 inherits the subsequent-similar timeline.

On every invocation, the skill self-checks against Section 7 of `sensitive-skill-guardrails.md` BEFORE producing output. If the self-check fails on any item, the output does not publish.

---

## ROI Framing

ROI for `/compliance-audit` is reported as **"time saved on drafting and triage of a control-level compliance gap analysis"** — NEVER "time saved on compliance audit" or "time saved on legal review."

Legal/compliance rate: $300-400/hr blended per `feedback_roi_rates.md`. Default $350/hr for a Phase 3 compliance-readiness gap assessment across a multi-family framework.

Time-saved baseline: authoring a structured control-level gap assessment against a framework with 20-50 controls in scope, mapped to a real org's processes, producing 10-20 findings with remediation roadmap and evidence inventory = **~8-12 hours** of manual drafting and triage time for a senior compliance practitioner. Control mapping is laborious — that is where the time goes. Simpler audits (single-family scope, small org, routine framework) are ~4-6 hours baseline. Complex audits (bundled frameworks, regulated-industry deployment, multi-jurisdictional scope) are 15+ hours baseline.

The ROI tracks ONLY the time the skill saves on drafting the structured artifact, not the substantive compliance review time. The substantive review by Compliance Officer, General Counsel, and external auditor still happens in full.

Example ROI line for a standard compliance audit:

```
⏱️ ~10 hrs saved in 120s, 42k tkns ~$2.5 cost, Value ~$3,500
```

---

## Attribution and Maintenance

**Owner**: ✅ Compliance Officer. The skill's control-level reasoning is Compliance Officer's accountability. Framework-specific substantive reasoning is co-owned with ⚖️ General Counsel for legal interpretation and (future) external auditor contacts for certification-specific guidance.

**Consumers** (gateways that invoke this skill):
- `ext-legal` — legal team gateway, primary user
- `product` — product gateway when PM/VP Product needs a compliance-readiness gap assessment before a Phase 2 or Phase 3 decision
- `ext-corpdev` — corp dev gateway for M&A diligence exhibits and partnership due diligence
- `ext-it` — IT governance gateway, because compliance often touches IT controls (access, logging, change management, vendor management). Added to reflect the real invocation path in enterprise orgs where the CIO's team owns a significant fraction of the control inventory.

New consumers require a frontmatter update and a one-line note in the consuming gateway's skill list.

**Authoring**: First-principles. This skill was authored from scratch during Phase 3 Sub-phase 3.0, inheriting the structural pattern from A5 `/risk-analysis`, A1 `/contract-review`, and A3 `/privacy-policy-audit` but with entirely original content. A4 is the first compliance-framework audit skill; the framework adapter pattern is introduced here and will be reused by future compliance skills as they ship.

**Framework adapter dependency**: `/compliance-audit` will read from `compliance-frameworks/` knowledge pack when Phase 5A C1.5 ships the pack. At v1.0.0, the skill ships BEFORE the pack exists and uses the fallback mechanism documented in the Framework Adapter Pattern section. The v1.0.0 adapter version is recorded in the Audit Metadata block of every output for traceability.

**Sidecar pattern dependency**: the `current-status.md` sidecar file is authored alongside each audit output when date-sensitive regulatory content is referenced. The sidecar has no separate knowledge pack — it is a per-audit artifact stored next to the audit output file.

**Updates**: Via the two-pass publication gate. Minor edits (typos, formatting) can bypass Pass 2. Any edit touching severity thresholds, framework adapter pattern, boundary statement, delegation patterns, or the output structure requires a full Pass 2 substantive review by General Counsel.

**Changelog**: Maintained at the bottom of this file. Version 1.0.0 — initial authoring 2026-04-11.

---

## Example Invocation

```
User: /compliance-audit "AXIA Bank Discount deployment" --framework israeli-ppl-bank-discount

/compliance-audit v1.0.0 — reading:
  - AXIA/Product/bank-discount-israeli-regulatory-compliance-plan.md (329 lines)
  - AXIA/Product/bank-discount-master-plan.md
  - AXIA/Product/risk-analysis-bank-discount-deal-2026-04-11.md (prior A5)
  - AXIA/Product/contract-review-eula-v2-2026-04-11.md (prior A1)
  - AXIA/Marketing/Collaterals/AXIA-Enterprise-License-Agreement-v2.pdf (Schedules A-D)

Framework adapter: inline bundle definition
  Bundled regimes:
    - Israeli Privacy Protection Law 5741-1981 (PPL), including Amendment 13 (2024)
    - Protection of Privacy Regulations (Data Security) 5777-2017
    - Bank of Israel Directive 361 (Cyber Defense Management)
    - Israeli Collective Agreements Law 5717-1957 (works council consultation)
    - Cross-border data transfer restrictions (PPL + banking secrecy)
    - Israeli labor court precedent on workplace monitoring (proportionality test)

Collecting inputs:
  - Organization: AXIA (Axia Security Ltd., Israel) deploying at Bank Discount
  - Scope: Employee-monitoring SaaS at 8,600-employee regulated bank; cloud/on-prem
    TBD; Israeli data residency required
  - Jurisdictions in scope: Israel primary; Delaware residue (AXIA parent)
  - Stage: Pre-deployment readiness, pre-signature
  - Source documents: 5 files enumerated above
  - Stakeholders: Asaf Massuri (AXIA CTO), Yohay Etsion (Fractional CPO), Dan (Bank
    Discount sponsor), TBD Bank Discount compliance contact

Producing output at:
  AXIA/Product/compliance-audit-israeli-ppl-bank-discount-2026-04-11.md
  AXIA/Product/compliance-audit-israeli-ppl-bank-discount-2026-04-11-status.md (sidecar)

[output follows standard structure: disclaimer → audit metadata → control mapping →
 findings → remediation roadmap → evidence inventory → reviewer checklist →
 cannot assess without]

⏱️ ~10 hrs saved in 120s, 42k tkns ~$2.5 cost, Value ~$3,500
```

---

## Changelog

- **1.0.0 (2026-04-11)** — Initial authoring. First-principles during Phase 3 Sub-phase 3.0. Inherits structural pattern from A5 `/risk-analysis`, A1 `/contract-review`, and A3 `/privacy-policy-audit`. Introduces the framework adapter pattern (parameterized by `--framework`) and the `current-status.md` sidecar pattern for date-sensitive regulatory content. Boundary statement vs A1, A3, A5, and C1.2b made explicit. Birth-tested against AXIA Bank Discount Israeli regulatory readiness with 14 control-level findings across 6 control families. Substantive review passed by ⚖️ General Counsel on the 72-hour subsequent-similar SLA; scaffolding review passed by 📋 Director of Legal Affairs.
