---
name: ai-control-audit
description: Per-release technical control audit of an AI system across 6 categories with named enforcement points and gap findings, as a drafting and triage aid.
argument-hint: --system NAME --release VERSION [--framework-alignment eu-ai-act,nist-ai-rmf,iso-42001,singapore-agentic]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: architecture-ai-governance
  phase: 5A
  sub_phase: C1.2a
  skill_type: task-capability
  owner: ai-architect
  primary_consumers:
  - ext-architecture
  - ext-legal
  - compliance-audit
  - ai-regulatory-audit
  - risk-analysis
  sensitive: true
inherits_pack: compliance-frameworks
---
# /ai-control-audit

> ⚠️ **Not legal advice. Not a certification opinion.** This output is a technical control audit produced by a product-organization skill as a drafting and triage aid for architecture, AI governance, and compliance review. It is NOT legal advice, NOT a certification attestation, and NOT a substitute for licensed counsel, external auditor engagement, or regulator dialogue. No attorney-client relationship is created by its production or use. Jurisdiction-specific questions, contested matters, and any decision with material legal, regulatory, safety, or commercial consequences require review by a licensed attorney in the relevant jurisdiction AND by qualified AI governance leadership. Do not rely on this output as the sole basis for any deployment, release, legal, or compliance decision.
>
> **Jurisdiction Assumed:** `{jurisdiction — e.g., "U.S. federal + EU (AI Act + GDPR) + UK"}`. If the system targets other jurisdictions, treat every finding as a hypothesis to verify with local counsel and in-jurisdiction AI governance reviewers.

---

## Purpose

`/ai-control-audit` produces a per-release technical control audit of a specific AI system across six categories: **model provenance, pre-deployment evaluation, runtime guardrails, observability, incident response, and change management**. For each category the skill names the controls expected, checks whether those controls are present, and — critically — names the **enforcement point** for each control (CI check, deploy gate, runtime assertion, runbook, or evidence artifact). Controls without named enforcement points are explicitly flagged as gap. The skill produces a release-gate recommendation (SHIP / SHIP WITH REMEDIATION / DO NOT SHIP) with remediation priority ordered by risk.

The technical-vs-regulatory distinction is load-bearing. Technical controls are about whether the AI system is **built and operated according to stated design** — does it have version pinning, eval harnesses, runtime guardrails, logging pipelines, rollback triggers, change approval? Regulatory obligations are about whether the system **satisfies the law in its jurisdiction** — does it meet EU AI Act Article 15, GDPR Article 22, NIST AI RMF MEASURE? The two overlap through the control-to-obligation mapping maintained in the `compliance-frameworks` knowledge pack, but they audit different things. An AI system can implement every technical control perfectly and still have regulatory gaps (because the jurisdiction's framework imposes obligations the technical controls don't cover). Conversely, a system can be regulatorily "aligned" on paper and still fail technically (because the stated controls have no enforcement point and drift unchecked). This skill audits the technical side. Its sibling `/ai-regulatory-audit` (C1.2b) audits the regulatory side. The control-to-obligation mapping is the bridge.

`/ai-control-audit` is a **drafting and triage aid**, not a certification opinion. Every finding is a hypothesis grounded in specific architecture documents, deployment artifacts, and observability telemetry, for a human (AI Architect + Security Architect + Compliance Officer + General Counsel where obligations are in scope) to verify.

---

## Boundary Statement (4-Sided, Critical)

The ai-control-audit skill sits at a specific intersection and MUST NOT drift into adjacent skills' territory. The boundary is load-bearing because drift creates duplicate findings, inconsistent severity framing, and confused ownership across architecture, legal, and product teams.

| Skill | Unit of Analysis | Primary Question | Owner |
|---|---|---|---|
| `/compliance-audit` (A4) | An organization or initiative vs a named framework | "Are we compliant with THIS regulation across our org/initiative?" | Compliance Officer |
| `/ai-regulatory-audit` (C1.2b) | An AI system vs all applicable frameworks | "Is this AI system responsibly governed, and which obligations does that governance satisfy?" | Compliance Officer |
| `/privacy-policy-audit` (A3) | A public-facing privacy policy document | "Does the policy disclose what the regs require?" | Privacy Counsel |
| `/risk-analysis` (A5) | An initiative, deal, or decision | "What could hurt us across six domains?" | General Counsel / VP Product |
| **`/ai-control-audit` (C1.2a)** | **A specific AI system release, technically** | **"Does this AI system implement the 6 categories of technical controls, with named enforcement points, for this release?"** | **AI Architect** |

C1.2a is bounded on four sides:

1. **Not `/compliance-audit` (A4).** A4 is horizontal and organization-level — it asks whether the org is ready for a SOC 2 / ISO 27001 / GDPR audit. C1.2a is system-level and technical — it asks whether a specific AI system release has its controls in place. A4 covers the whole organization; C1.2a covers one system's one release. If A4 surfaces a control gap that is specifically AI-technical (e.g., "no eval harness for the scoring model"), A4 points at C1.2a. If C1.2a surfaces a gap that is organization-wide (e.g., "no change management policy exists at all"), C1.2a points at A4.

2. **Not `/ai-regulatory-audit` (C1.2b).** C1.2b is the regulatory posture counterpart — it asks whether the AI system satisfies the obligations imposed by whichever frameworks apply to it, across all applicable frameworks simultaneously. C1.2a is the technical control counterpart — it asks whether the system's controls are technically in place regardless of whether any specific obligation applies. The control-to-obligation mapping table in `compliance-frameworks` v1.1.0 Section 3 is the authoritative bridge: C1.2a identifies the controls and their enforcement points; C1.2b identifies the obligations and whether those controls satisfy them. When an organization has a deployed AI system, both skills run — C1.2a at every release (technical), C1.2b quarterly or at regulatory trigger events (regulatory). Where C1.2a's findings say "Category 2 pre-deployment evaluation is a P0 gap," C1.2b translates that into "EU AI Act Article 15 accuracy/robustness obligation is at risk."

3. **Not `/privacy-policy-audit` (A3).** A3 audits whether a public-facing privacy policy discloses what the regulations require for disclosure — it is a document audit focused on sufficiency of disclosure. C1.2a audits whether the underlying system actually implements the controls the policy describes. A3 asks "does the policy say the right things?"; C1.2a asks "does the system do the right things?" When A3 surfaces a disclosure gap (e.g., "the policy doesn't describe the DPIA process"), A3 points at A4 or A3 remediation. When C1.2a surfaces a technical gap (e.g., "no logging pipeline captures user decisions"), C1.2a flags it as a Category 4 gap regardless of whether the policy mentions logging.

4. **Not `/risk-analysis` (A5).** A5 is domain-level risk across an initiative or deal — it asks what could hurt us across legal, commercial, operational, regulatory, financial, reputational dimensions. C1.2a is narrowly technical and system-scoped. If A5 surfaces a regulatory risk in the regulatory domain for an AI product, A5 points at C1.2b (for regulatory posture) and/or C1.2a (for technical controls). If C1.2a surfaces a control gap with material business exposure, C1.2a points at A5 for broader risk framing.

When a user asks C1.2a to do something in the adjacent territory, the skill refuses and points at the correct sibling skill. This conversion of scope drift from invisible to blocking is the same pattern `/compliance-audit` (A4) uses against A1/A3/A5.

---

## When to Use

Invoke `/ai-control-audit` when you need to:

- **Every major release** of an AI system — new model version, new agent deployment, new orchestration pattern, new tool/integration surface. This is the primary use case.
- **Model version change** — upgrading the underlying base model (e.g., Claude 3.5 → Claude 4, GPT-4 → GPT-5, Llama 3 → Llama 4). Model changes invalidate prior eval evidence and change the behavior surface.
- **Infrastructure migration** — switching cloud provider, changing inference provider, moving from a managed API to self-hosted, migrating observability stack.
- **Post-incident review** — after a P0 or P1 incident involving the AI system, audit all 6 categories to identify which controls failed and which enforcement points were missing.
- **Vendor SLA review** — when a model provider, inference vendor, or observability vendor changes their terms, pricing, or capabilities in a way that affects control operation.
- **Pre-deployment readiness check** — before a major new deployment (new market, new customer segment, new jurisdiction) to verify all technical controls are in place for the deployment context.
- **Annual architecture review** — as part of a yearly technical governance cycle alongside SOC 2 / ISO 27001 / ISO 42001 certification work.

## When NOT to Use

Do NOT use `/ai-control-audit` when:

- You need a **regulatory posture audit** across applicable frameworks → use `/ai-regulatory-audit` (C1.2b). C1.2a audits controls; C1.2b audits regulatory obligations. They complement each other via the shared mapping table.
- You need a **horizontal framework readiness assessment** (SOC 2, GDPR, ISO 27001) at the organization level → use `/compliance-audit` (A4).
- You need a **privacy policy disclosure audit** → use `/privacy-policy-audit` (A3). A3 audits the document; C1.2a audits the system.
- You need a **deal-level or initiative-level risk landscape** across six domains → use `/risk-analysis` (A5). A5 is upstream of C1.2a for the regulatory/technical risk domain.
- You need a **contract clause review** (model provider terms, vendor SLA) → use `/contract-review` (A1).
- You need a **licensed legal opinion** on AI regulatory exposure → engage outside counsel; the skill does not substitute.
- You need a **formal certification attestation** (ISO 42001, SOC 2 Type II) → the skill produces gap analysis input; the auditor produces the attestation.
- The AI system has **no deployed release** to audit — the skill requires a concrete release with evidence artifacts. For pre-release design review, use `/four-risks-check` or architecture team consultation.
- The system is **not actually AI-based** — if it's rule-based, deterministic, or doesn't involve a learned model, use `/compliance-audit` or architecture review directly.

---

## Required Inputs

- **System name** — canonical name of the AI system being audited (e.g., "Legionis", "AXIA Insider Risk Engine", "Spring AI ALGINT").
- **Release version** — specific release identifier (semver, date, or build tag).
- **Pointer to architecture docs** — current (not stale) architecture documentation, release notes, deployment topology diagram.
- **Runtime access OR observability telemetry** — at least one of: direct runtime access for inspection, observability dashboards/logs, or a written telemetry summary from the on-call team. Without this, Category 4 (Observability) and Category 5 (Incident response) cannot be audited meaningfully and must be marked "cannot assess."
- **Incident history** — log of incidents, near-misses, and rollbacks affecting the release in question or the preceding release. Required for Category 5 audit quality.
- **Eval harness code and results (optional but strongly recommended)** — for Category 2 audit depth.
- **Framework alignment list (optional)** — comma-separated list of frameworks the user wants cross-referenced against the control-to-obligation mapping: `eu-ai-act`, `nist-ai-rmf`, `iso-42001`, `singapore-agentic`, `gdpr`, `soc2`. If omitted, the skill produces technical findings only without obligation cross-referencing.

---

## Method

### Step 1 — Load system architecture and release context

Pull architecture documentation, release notes, deployment topology, and current production state. Identify: which model(s) are in use, which providers, which orchestration frameworks, which runtime guardrails are claimed in the docs, which observability stack is in place, and the release diff from the prior release (what changed). Capture the deployment boundary — what is in scope for "this AI system at this release" vs what is adjacent infrastructure.

### Step 2 — Audit Category 1: Model Provenance

Apply the per-category audit protocol (see Section "Per-Category Audit Protocol" below) to model provenance. Inspect model cards, dataset lineage documentation, base-model version pinning mechanisms, fine-tune lineage records, and training data attribution. For each expected control, verify presence and name its enforcement point. Controls without enforcement points are marked gap.

### Step 3 — Audit Category 2: Pre-deployment Evaluation

Inspect eval harness code, eval runs, acceptance thresholds, red-team protocols, bias/fairness evaluations, capability benchmarks, and safety benchmarks. Verify: evaluations run automatically (CI check or deploy gate), results are recorded (evidence artifact), acceptance thresholds are named (not "the team reviews results"), and failures actually block release (enforcement point).

### Step 4 — Audit Category 3: Runtime Guardrails

Inspect input validation, output filtering, rate limits, tool-use permissions, content filters, and prompt injection defenses. For each claimed guardrail, verify: it is enforced at runtime (not as documentation-only), it rejects or logs violations (evidence artifact), and the enforcement happens at a named point in the request path.

### Step 5 — Audit Category 4: Observability

Inspect logging schemas, drift monitors, cost/latency dashboards, output quality tracking, and user feedback capture. Verify: logs are actually written to durable storage (not just `console.log`), the logging schema captures the fields needed to reconstruct a decision, drift monitors have alert thresholds and on-call routing, and user feedback flows back into the eval harness (Category 2 closed loop).

### Step 6 — Audit Category 5: Incident Response

Inspect rollback triggers, kill switches, audit trails, on-call rotation, incident playbooks, and post-mortem templates. Verify: rollback procedures are documented as runbooks (not tribal knowledge), kill switches are actually testable, the audit trail supports incident reconstruction, and the post-mortem template produces learnings that feed back to Category 6 change management.

### Step 7 — Audit Category 6: Change Management

Inspect version pinning, shadow deployment procedures, canary release gates, A/B gating, and the model-update approval workflow. Verify: version pinning is enforced at deploy gate (not at developer discretion), canary releases have automated promotion criteria or a named human approver, and model updates flow through a change review with recorded approval.

### Step 8 — Cross-reference control-to-obligation mapping (if `--framework-alignment` provided)

Load the 25-row mapping table from `compliance-frameworks` knowledge pack v1.1.0 Section 3. For each row whose framework appears in `--framework-alignment`, check whether the corresponding control (identified in Steps 2-7) is present AND has a named enforcement point. If the control is absent or has no enforcement point, flag a **control-to-obligation gap**: the obligation depends on a control that is not operating. Produce the control-to-obligation gap table as part of the output. Note that this cross-reference identifies technical control gaps that create regulatory exposure; the regulatory interpretation ("is this actually a violation?") is deferred to `/ai-regulatory-audit` (C1.2b) and licensed counsel.

---

## Per-Category Audit Protocol

Each of the 6 categories is audited with the same protocol: (a) what the category controls, (b) specific controls expected, (c) enforcement point map, (d) common gap patterns, (e) evidence types accepted.

### Category 1: Model Provenance

**What this category controls.** The identity, lineage, and documentation of the models used in the system. Model provenance answers: which model, at which version, trained on which data, fine-tuned with which process, attributed to which upstream sources. Without provenance, you cannot audit the other five categories — you don't know what system you're auditing.

**Specific controls expected (3-6):**
1. **Model card** — per model in use, documenting intended use, training data summary, known limitations, safety evaluations.
2. **Version pinning** — each deployed model has an explicit version identifier pinned in code or configuration, not "latest."
3. **Dataset lineage** — for self-trained or fine-tuned models, the training and fine-tune data sources are documented with provenance.
4. **Fine-tune lineage** — for fine-tuned models, the base model version, fine-tune data, fine-tune method, and fine-tune date are recorded.
5. **Third-party attribution** — for models from external providers (Anthropic, OpenAI, Google, Meta, etc.), the provider, model family, and version are recorded along with license terms.
6. **Provenance artifact** — a single queryable artifact (JSON file, database table, model registry entry) that ties the above together for each release.

**Enforcement points map.** Model provenance controls are typically enforced via **evidence artifacts** (model cards, registry entries) produced at CI time and validated at deploy gate. A CI check that a model card exists before build is the strongest enforcement; a runbook that says "update the model card before release" is the weakest. Runtime assertions are rare for provenance (the model is what it is at request time).

**Common gap patterns:**
- Model card exists but has not been updated for the current release (stale evidence).
- Version pinning is done in developer environments but production uses "latest" via a pointer that is not pinned.
- Fine-tune lineage is tribal knowledge ("Alex trained this last quarter") with no recorded artifact.
- Third-party model attribution is missing from the deployment — the provenance artifact doesn't capture which upstream model is in use.
- No single queryable provenance artifact exists; information is scattered across GitHub, Confluence, and Slack.

**Evidence types accepted.**
- Model card files (`MODEL_CARD.md`, `model-card.yaml`, or equivalent) in the repository.
- Model registry entries (e.g., MLflow, Weights & Biases, custom registry).
- `compiled-personas.json` or similar compiled artifacts that capture version and source.
- CI pipeline output that validates model card presence before build.
- License records (contracts, terms-of-service snapshots) for third-party models.

### Category 2: Pre-deployment Evaluation

**What this category controls.** The evaluation gate between "a model version exists" and "that model version is deployed to production." Pre-deployment evaluation answers: has this version been tested for accuracy, robustness, safety, bias, and fitness-for-purpose, and did the results meet the acceptance threshold?

**Specific controls expected (3-6):**
1. **Eval harness** — an automated, repeatable evaluation suite that runs against each model version before deployment.
2. **Acceptance thresholds** — named numerical or categorical thresholds (not "the team reviews results") that the eval must meet.
3. **Red-team protocol** — a documented procedure for adversarial testing, including prompt injection tests, jailbreak attempts, and misuse scenarios.
4. **Fairness/bias test** — a documented subgroup evaluation identifying disparate performance across relevant demographic or contextual dimensions.
5. **Capability evaluation** — task-level performance measurement relevant to the system's intended use (e.g., accuracy on domain benchmarks, tool-use success rate).
6. **Safety benchmark** — for systems that produce text output to users, a content safety evaluation (refusal on disallowed content, harmful output rates).

**Enforcement points map.** Pre-deployment evaluation controls are typically enforced as **deploy gates** — the eval runs, fails close the gate, passes open it. CI checks are common for eval-on-every-commit patterns; runbooks are the fallback when automated gating isn't feasible (e.g., human-in-the-loop eval review). Runtime assertions do not apply (eval is by definition pre-deployment).

**Common gap patterns:**
- Eval harness exists but is not run automatically; it's "the team runs this before a release" (no enforcement).
- Eval results are produced but no acceptance threshold is documented — the team reviews the numbers subjectively.
- Red-team protocol is documented for the first release but has not been re-run against subsequent releases.
- Fairness/bias testing is absent entirely or run only against one demographic dimension.
- Eval harness tests the model in isolation, not the full system (agent + tools + orchestration), missing system-level failure modes.
- Eval results are stored in an ephemeral CI run, not in a durable artifact for audit.

**Evidence types accepted.**
- Eval harness code in the repository (`evals/`, `tests/model/`, `tests/ai/`, etc.).
- Eval run output logs stored in durable storage (S3, GCS, database).
- CI pipeline configuration showing eval gate with fail-close behavior.
- Red-team report documents (internal or external).
- Fairness evaluation reports with subgroup performance breakdowns.
- Release gate records showing eval pass/fail per release.

### Category 3: Runtime Guardrails

**What this category controls.** The behaviors enforced on the AI system at request time — what inputs are accepted, what outputs are filtered, what rate limits apply, what tools the system can call, and what content filters run. Runtime guardrails answer: when the system is live, what actually happens when something goes wrong?

**Specific controls expected (3-6):**
1. **Input validation** — the system validates user input for shape, length, content policy, and obvious adversarial patterns before passing to the model.
2. **Output filtering** — the system filters model output for safety, PII leakage, and policy violations before returning to the user.
3. **Rate limits** — the system enforces per-user, per-API-key, or per-tenant rate limits to prevent abuse.
4. **Tool-use permissions** — for agentic systems, tools available to the model are gated by user role, context, and explicit permission grants.
5. **Content filters** — either provider-supplied content moderation (OpenAI moderation API, Anthropic built-in filters) or self-hosted classifier, actually wired into the request path.
6. **Prompt injection defenses** — explicit defenses against prompt injection: input sanitization, system prompt isolation, instruction hierarchy enforcement.

**Enforcement points map.** Runtime guardrails are, by definition, **runtime assertions** — they MUST be enforced at request time. A runtime guardrail documented in architecture but not present in the request path is not a control; it's aspiration. Deploy gates can verify the guardrail code exists; runtime assertions enforce it per-request. Evidence artifacts (filter hit logs) provide after-the-fact verification.

**Common gap patterns:**
- Guardrails are documented as requirements but not implemented in code (the architecture diagram shows a filter box but the code path skips it).
- Input validation is present on the HTTP layer but the model is called from a background job that bypasses validation.
- Output filtering is only run in synchronous paths; streaming responses bypass the filter.
- Rate limits exist at the API gateway but not at the LLM call level, so a single authenticated request can burn the budget.
- Tool-use permissions are documented but not enforced — the model has access to any tool regardless of user context.
- Prompt injection defenses are "the system prompt says don't follow instructions" — no structural defense.

**Evidence types accepted.**
- Source code showing the guardrail in the request path (specific file + line).
- Runtime logs showing filter hits with per-request records.
- Integration tests that exercise the guardrail with adversarial inputs.
- Penetration test results (internal or external) targeting the guardrails.
- Configuration files showing rate limit thresholds wired into the runtime.

### Category 4: Observability

**What this category controls.** The ability to see what the AI system is doing in production — what inputs it received, what outputs it produced, what tools it called, how it performed over time, and how users are reacting. Observability answers: after the fact, can we reconstruct what happened and why?

**Specific controls expected (3-6):**
1. **Logging schema** — structured logs capturing per-request inputs (or input hashes if PII is involved), outputs, tool calls, latency, cost, and model version used.
2. **Drift monitors** — automated monitoring for output distribution drift, latency drift, cost drift, and quality drift, with alert thresholds.
3. **Cost/latency dashboards** — real-time visibility into per-request and aggregate cost and latency, broken down by model, user, and feature.
4. **Output quality tracking** — sampled output quality review, either via human review, automated quality checks, or user feedback proxies.
5. **User feedback capture** — thumbs up/down, flagging, or equivalent mechanism routed into an analyzable data store, not just a support ticket.
6. **Log retention and access control** — logs are retained per policy and access is gated.

**Enforcement points map.** Observability controls are primarily **runtime assertions** (logs must be written per request) and **evidence artifacts** (dashboards must exist and be accessible). CI checks can validate logging instrumentation presence; deploy gates can verify log pipeline health. Runbooks cover on-call response to drift alerts.

**Common gap patterns:**
- Logging writes to `console.log` or ephemeral container logs, not to durable storage.
- Logging schema is unstructured ("we log everything to stdout") and not queryable.
- Drift monitors exist but have no alert thresholds — nobody is paged when drift occurs.
- Dashboards exist but are not reviewed; no on-call rotation monitors them.
- User feedback is captured but sits in a database table nobody queries.
- Log retention is not configured — logs are truncated after the container restarts.
- PII is logged without redaction, creating a secondary compliance issue.

**Evidence types accepted.**
- Log pipeline configuration (Datadog, Splunk, Loki, CloudWatch, etc.) showing durable storage.
- Log schema documentation with field definitions.
- Dashboard URLs (or screenshots at the audit date) for drift monitors, cost dashboards, quality tracking.
- Drift alert configuration (threshold, recipient, cadence).
- User feedback pipeline showing the path from UI event to analyzable data store.

### Category 5: Incident Response

**What this category controls.** The procedures for detecting, responding to, recovering from, and learning from AI system incidents. Incident response answers: when something goes wrong, can we stop the bleeding, reconstruct what happened, and prevent recurrence?

**Specific controls expected (3-6):**
1. **Rollback triggers** — documented, named conditions under which the system is rolled back (e.g., "output error rate > 5% for 10 minutes → automatic rollback"), and the mechanism to execute the rollback.
2. **Kill switches** — a mechanism to immediately disable the AI system (or specific model version) with a documented trigger path and testing cadence.
3. **Audit trails** — the observability logs + provenance artifacts combine to support full incident reconstruction, with retention sufficient for post-mortem.
4. **On-call rotation** — named humans are on-call for AI system incidents, with escalation paths and runbook access.
5. **Incident playbooks** — step-by-step runbooks for common incident classes (model degradation, provider outage, guardrail failure, PII leakage, harmful output).
6. **Post-mortem templates** — structured post-mortem format that captures root cause, contributing factors, remediation actions, and learnings fed back into Category 6 change management.

**Enforcement points map.** Incident response controls are primarily **runbooks** (human-followed procedures) combined with **runtime assertions** for automated rollback triggers. Evidence artifacts (incident logs, post-mortems) support after-the-fact verification. Deploy gates can enforce the presence of rollback procedures before release; CI checks rarely apply.

**Common gap patterns:**
- Rollback procedures exist in documentation but have never been tested — no "game day" exercise validates the runbook works.
- Kill switch exists in code but cannot be invoked without developer access — operations cannot actually use it.
- On-call rotation is "whoever built it is on-call" — no formal rotation, no escalation.
- Incident playbooks are absent; each incident is handled ad hoc, producing no learnings.
- Post-mortem template exists but post-mortems are not actually conducted after incidents.
- Audit trail coverage gaps — logs don't support incident reconstruction because Category 4 observability is incomplete.
- Rollback triggers are aspirational ("we would roll back if...") with no implementation.

**Evidence types accepted.**
- Runbook documents with step-by-step procedures.
- Rollback configuration (feature flags, canary pipeline config, deployment rollback scripts).
- Kill switch code path (specific file + line) and testing records.
- On-call schedule (PagerDuty, Opsgenie, or equivalent).
- Past post-mortem documents showing the template is actively used.
- Incident log showing response times, resolution, and follow-up actions.

### Category 6: Change Management

**What this category controls.** The governance of changes to the AI system — model updates, prompt changes, tool additions, infrastructure migrations. Change management answers: when something about the system changes, is there a defined process to review, test, approve, and roll out the change?

**Specific controls expected (3-6):**
1. **Version pinning in production** — the production deployment pins the model version, the orchestration version, and the tool inventory explicitly.
2. **Shadow deployment** — new model versions or major changes run in shadow mode (parallel to production, not user-facing) before promotion.
3. **Canary releases** — changes are deployed to a small percentage of traffic first, with automated promotion criteria or a named human approver.
4. **A/B gating** — for UX-affecting changes, A/B testing or gated rollout is used with named success metrics.
5. **Model-update approval workflow** — a documented workflow (with recorded approvals) for any change that updates the model, prompts, or tool inventory.
6. **Release documentation** — a release note or change log entry per release recording what changed, who approved, and eval results.

**Enforcement points map.** Change management controls are typically a mix of **CI checks** (validate version pinning, check release note present), **deploy gates** (canary promotion criteria, shadow deployment requirement), **runbooks** (approval workflow), and **evidence artifacts** (release notes, approval records). Runtime assertions rarely apply to change management itself (they apply to what is deployed, not to the deployment process).

**Common gap patterns:**
- Version pinning is inconsistent — some components pinned, some tracking "latest" implicitly.
- Shadow deployment is documented but not practiced; new versions go directly to production.
- Canary releases exist at the infrastructure level but not at the AI system level — the whole AI system is swapped at once.
- Approval workflow is "the team discusses it in Slack" — no recorded approval.
- Release notes are absent or describe code changes but not model/prompt/tool changes.
- Model updates flow through a different process than code updates, bypassing the change review.
- No A/B gating infrastructure exists — UX changes are released to 100% of users without measurement.

**Evidence types accepted.**
- Version pinning evidence (configuration files, package-lock files, compiled artifacts).
- Shadow deployment infrastructure documentation and example runs.
- Canary pipeline configuration and promotion criteria.
- Approval workflow records (tickets, pull request approvals, change advisory board logs).
- Release notes in a findable location (GitHub releases, internal docs, changelog).
- A/B test infrastructure configuration and recent test records.

---

## Output Structure

The skill produces a single audit output document with the following structure (Markdown):

### 1. Header

- System name and release version audited
- Audit date
- Jurisdiction assumed (for disclaimer and control-to-obligation mapping)
- Framework alignment list (if provided)
- Auditor identity (🤖 AI Architect + consulted agents)

### 2. Disclaimer block (verbatim, see top of this SKILL)

### 3. Executive summary

- Release-gate recommendation: **SHIP** / **SHIP WITH REMEDIATION** / **DO NOT SHIP**
- One-paragraph rationale tied to P0 findings count and severity
- Top 3 P0 gaps that drive the recommendation

### 4. Per-category audit results

For each of the 6 categories:

- **Category name**
- **Summary verdict**: PRESENT / GAP / PARTIAL
- **Controls audited** (list of expected controls from the per-category protocol)
- **Per-control findings table**:
  | Control | Status | Enforcement Point | Evidence Pointer | Severity | Remediation Owner |
  |---|---|---|---|---|---|
  | (control name) | present / gap / partial | CI / Deploy / Runtime / Runbook / Evidence / **none (gap)** | (specific pointer or "none") | P0 / P1 / P2 / N/A | (named role) |

### 5. Control-to-obligation gap table (if `--framework-alignment` provided)

A table derived from the `compliance-frameworks` v1.1.0 Section 3 mapping, filtered to the frameworks in `--framework-alignment`, and annotated with the Step 2-7 findings.

| # | Control | Obligation | Framework | C1.2a Finding | Gap Severity |
|---|---|---|---|---|---|
| (from mapping) | (from mapping) | (from mapping) | (from mapping) | present / gap / partial | P0 / P1 / P2 / N/A |

Each row where the control is "gap" or "partial" indicates a **technical control gap that creates regulatory exposure**. The regulatory interpretation is deferred to `/ai-regulatory-audit` (C1.2b) and licensed counsel. This table is the bridge between the C1.2a technical audit and the C1.2b regulatory audit.

### 6. Remediation priority list

Ordered list of P0 / P1 / P2 remediations with:
- Finding reference (category + control)
- Remediation action
- Remediation owner (named role)
- Target release for remediation (this release, next release, backlog)

### 7. Findings (numbered)

Numbered list of findings across all categories, each with:
- **Finding N**
- **What** (specific control gap)
- **Why it matters** (risk or implication, linked to obligation if framework alignment provided)
- **Severity** (P0 / P1 / P2)
- **Enforcement point expected** (CI / Deploy / Runtime / Runbook / Evidence)
- **Current state** (present / gap / partial, with evidence pointer or "none")
- **Suggested next step** (what the reviewer should do)

### 8. Reviewer Checklist (see Quality Gates section)

### 9. Cannot Assess Without (see section below)

### 10. Related Skills and Hand-off (see Related Skills section)

---

## Quality Gates

Before the audit output is considered complete, all of the following must be true:

1. [ ] All 6 categories have been audited (no skipped categories).
2. [ ] Every claimed control has a named enforcement point OR is explicitly marked as gap with "none — no enforcement point" in the enforcement column.
3. [ ] Evidence pointers are specific (file path + line, log query, dashboard URL, document title + date) — never "see docs" or "team knows."
4. [ ] If `--framework-alignment` was provided, the control-to-obligation cross-reference table is populated from the `compliance-frameworks` v1.1.0 Section 3 mapping, filtered to the specified frameworks.
5. [ ] Remediation priority list is ordered by risk (P0 first, then P1, then P2), with every item having a named remediation owner.
6. [ ] Release-gate recommendation is explicit (SHIP / SHIP WITH REMEDIATION / DO NOT SHIP) with a one-paragraph rationale tied to P0 findings count.
7. [ ] No vendor content lifted — grep-check the output for phrases from Anthropic, OpenAI, Google, or AWS AI governance docs. Paraphrase any concept referenced; cite only by public-framework name.
8. [ ] No vague language — the output must not contain "comprehensive," "robust," "state-of-the-art," "industry-standard," "best practices," or "world-class." Every assertion is specific.
9. [ ] Every gap has a named remediation owner (role name, not "the team"). If the owner is unknown, flag it as a P0 finding in its own right.
10. [ ] "Cannot Assess Without" section is populated (not empty) — there is always something the audit could not assess without additional input.

---

## Reviewer Checklist

Before acting on this audit output, the human reviewer MUST sign off on:

- [ ] Jurisdiction assumption confirmed and correct for the target deployment.
- [ ] System identification correct — this audit is scoped to the specific release intended.
- [ ] Evidence pointers independently verified for at least the P0 findings (the auditor may have mis-cited or hallucinated a file path).
- [ ] Enforcement point claims verified — for each control marked "present with CI enforcement," the reviewer confirmed the CI check actually fails closed.
- [ ] Remediation owners engaged and acknowledgment obtained for P0 items.
- [ ] Release-gate recommendation reviewed by AI Architect + Security Architect + (if regulatory exposure) Compliance Officer + General Counsel.
- [ ] If `--framework-alignment` provided, the control-to-obligation gap table has been reviewed by Compliance Officer and any P0 obligation gaps have a licensed-counsel follow-up path.
- [ ] Post-audit action: this audit is stored as evidence for the release record per change management Category 6.

---

## Cannot Assess Without

The following are explicitly out of scope for this skill and REQUIRE additional input (from other agents, roles, or licensed experts) to assess properly:

- **Runtime access to the deployed system** — without direct runtime inspection or a recent observability snapshot, Category 3 (Runtime Guardrails) and Category 4 (Observability) cannot be audited with confidence. The audit can note expected controls from architecture docs but cannot verify they operate.
- **Architecture documentation that is current** — stale architecture docs produce stale findings. If the docs are known to be stale, the audit must note this and down-weight findings derived from them.
- **Release notes and deployment topology** — without a release diff, the audit cannot assess Category 6 (Change Management) for this specific release.
- **Incident history for the preceding release** — Category 5 (Incident Response) cannot be audited realistically without incident history to check against. An audit that says "Category 5 is fine" without incident history is an aspirational audit, not a technical one.
- **Eval harness code and results** — Category 2 (Pre-deployment Evaluation) cannot be audited at depth without access to the eval code and recent eval run output.
- **Legal and compliance sign-off on specific obligations** — this skill identifies technical control gaps and their potential link to regulatory obligations via the mapping table. The regulatory interpretation ("is this a violation under the specific facts?") is OUT OF SCOPE. Use `/ai-regulatory-audit` (C1.2b) for multi-framework regulatory posture and engage licensed counsel in the relevant jurisdictions for interpretation.
- **Product-level business risk framing** — this skill does not frame findings at the deal or initiative level. Use `/risk-analysis` (A5) for cross-domain business risk and `/compliance-audit` (A4) for organization-level framework readiness.
- **Sector-specific obligations** (healthcare PHI, biometrics, critical infrastructure, children's data, financial services) — the base mapping table does not cover sector-specific obligations. For systems in these sectors, C1.2a output must be reviewed against sector-specific frameworks by sector-specialized counsel.
- **Security architecture depth on runtime guardrails** — for adversarial robustness depth, consult `@security-architect` for threat modeling and penetration-test planning. C1.2a audits whether guardrails exist and have enforcement points; it does not audit whether the guardrails defeat a determined attacker.
- **Deploy-gate implementation depth** — for deploy gate configuration review (canary criteria, promotion logic), consult `@cloud-architect` for infrastructure-side enforcement review.

---

## Delegation Pattern

This skill uses **Pattern 1 Consultation** (default) from `.claude/rules/delegation-protocol.md`. The AI Architect owns the audit and may consult:

- **@security-architect** — for runtime guardrail depth (Category 3), particularly around prompt injection defenses, adversarial robustness, and security-critical guardrail paths. Consultation, not delegation — the AI Architect integrates the security perspective into the finding.
- **@cloud-architect** — for deploy-gate enforcement review (Category 6), particularly around canary pipeline configuration, shadow deployment infrastructure, and version pinning enforcement at the deployment boundary.
- **@compliance-officer** — for control-to-obligation mapping interpretation (Step 8), particularly where a control gap may create regulatory exposure. Consultation, not delegation — the Compliance Officer informs the severity framing; the actual regulatory posture audit is `/ai-regulatory-audit` (C1.2b).

**Pattern 5 Adversarial Review** is available **on request** for high-stakes release gates — releases where a missed control gap creates material business, safety, or regulatory exposure. In adversarial mode, a second AI Architect (or the Chief Architect) is spawned in fresh context to stress-test the draft audit findings. The adversarial review stops at the first iteration with no new P0/P1 findings or at two iterations maximum, per the pattern specification. Default is Consultation; Adversarial is opt-in.

---

## ROI Framing

ROI is reported as **time saved on drafting and triage** for the AI Architect and the release-gate review team, at $300/hr architecture blended rate. This framing is mandatory per `.claude/rules/roi-display.md` "Sensitive Skill ROI Framing" — the skill does NOT claim to save time on "AI governance review" or "compliance review," because those activities are the human reviewer's irreducible work. The skill produces a structured first-pass audit; the human reviewer then validates, corrects, and owns the final assessment.

Typical per-audit ROI:
- Drafting a structured per-release AI control audit from scratch: 6-10 hours for a mid-complexity AI system (the 6 categories, per-category finding tables, control-to-obligation cross-reference, remediation priority, release-gate recommendation).
- With this skill: 30-60 minutes of AI Architect review + sign-off on the drafted audit.
- Time saved: 5-9 hours per audit. At $300/hr: $1,500-$2,700 value per audit.

---

## Related Skills and Hand-off

### Input from

- **`compliance-frameworks` knowledge pack v1.1.0** (owned by Compliance Officer) — Section 3 control-to-obligation mapping table is the authoritative cross-reference between the 6 technical control categories and regulatory obligations across EU AI Act, GDPR, NIST AI RMF, SOC 2, ISO 27001, ISO 42001, and Singapore Agentic AI Governance. This pack is the C1.2a-C1.2b bridge.
- **`compliance-frameworks/current-status.md`** — date-sensitive content (effective dates, transition deadlines) that the audit references when interpreting framework alignment.

### Cross-references

- **`/ai-regulatory-audit`** (C1.2b, Phase 5A) — the regulatory posture counterpart. When C1.2a finds a gap that appears in the control-to-obligation table, C1.2b is the next step for the regulatory interpretation.
- **`/compliance-audit`** (A4, Phase 3) — the horizontal framework audit at the organization level. A4 covers the organization; C1.2a covers one system's one release.
- **`/risk-analysis`** (A5) — the deal-level or initiative-level risk landscape. A5 is upstream for AI systems where multiple risk domains interact.
- **`/privacy-policy-audit`** (A3) — for the privacy disclosure document counterpart.

### Hand-off

After a C1.2a audit is complete:

1. If `--framework-alignment` was provided and the control-to-obligation gap table has P0 rows, hand off to `/ai-regulatory-audit` (C1.2b) for the regulatory posture view.
2. If the audit surfaces a control gap that requires organization-wide change (e.g., "no change management policy exists"), hand off to `/compliance-audit` (A4) at the organization level.
3. If the audit surfaces a contract issue (e.g., vendor SLA inadequate for Category 5 incident response), hand off to `/contract-review` (A1).
4. If the audit surfaces a product-level risk, hand off to `/risk-analysis` (A5).

Store the audit output as a release-gate evidence artifact per Category 6 change management.

---

## Findings (skill-level note)

The skill's OUTPUT contains a Findings section (see "Output Structure" Section 7 above). The Findings below are skill-level — they describe known limitations of `/ai-control-audit` itself:

### Finding 1 — Category 4 Observability is only as good as the telemetry access
**What**: Without runtime observability access, Category 4 audit is aspirational, not factual.
**Why it matters**: An audit that says "logs are written to durable storage" based on code review alone may miss a production configuration override. The auditor saw the code path; they did not confirm the pipeline runs.
**Severity**: P1 (skill limitation, not a specific audit failure).
**Mitigation**: The Cannot Assess Without section names runtime access as a hard requirement. If absent, the auditor must mark Category 4 "cannot assess" rather than "present."

### Finding 2 — Control-to-obligation mapping is horizontal, not sector-specific
**What**: The 25-row mapping table in `compliance-frameworks` v1.1.0 covers horizontal frameworks. Sector-specific obligations (healthcare, biometrics, critical infrastructure, children's data, financial services) are not in the base table.
**Why it matters**: A C1.2a audit of an AI system in a regulated sector may miss obligations that are sector-specific. The auditor must flag sector-specific review as a Cannot Assess Without item.
**Severity**: P1 (skill limitation).
**Mitigation**: The Cannot Assess Without section names sector-specific obligations as out of scope. The audit output must explicitly declare this.

### Finding 3 — The audit assumes controls operate at claimed enforcement points
**What**: A control marked "present with CI enforcement" relies on the auditor having verified the CI check actually fails closed. Without a test run, the claim is aspirational.
**Why it matters**: Enforcement point tagging is the load-bearing innovation of this skill. If the tag is wrong, the audit is theater.
**Severity**: P0 (load-bearing risk).
**Mitigation**: The Reviewer Checklist requires the reviewer to independently verify enforcement point claims for P0 findings. The auditor should name the verification path ("I ran the CI job on this commit and confirmed fail-close") or flag that verification was not possible.

---

## Metadata

- **Phase**: 5A Sub-phase C1.2a
- **Version**: 1.0.0
- **Sensitive**: true (per `.claude/rules/sensitive-skill-guardrails.md`)
- **First-principles authoring**: Yes. NIST AI RMF, ISO/IEC 42001, and EU AI Act are referenced by stable structural elements (function names, clause numbers, article numbers) without lifting text. No vendor content from Anthropic, OpenAI, Google, or AWS AI governance documentation.
- **Knowledge pack inherited**: `compliance-frameworks` v1.1.0
- **Publication gate**: Two-pass per `sensitive-skill-guardrails.md` Section 4 — Pass 1 (scaffolding) by Director of Legal Affairs or Chief Architect, Pass 2 (substantive) by General Counsel + AI Architect.
- **Next review**: 2026-07-11 (quarterly, synchronized with `compliance-frameworks` pack re-verification cadence).
