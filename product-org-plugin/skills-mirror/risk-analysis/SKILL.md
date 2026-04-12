---
name: risk-analysis
description: Produces a structured, multi-domain risk landscape for an initiative, decision, or deal as a drafting and triage aid for human review, not a legal conclusion.
argument-hint: '[initiative or decision name] or [update path/to/risk-analysis.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: legal-risk
  skill_type: task-capability
  owner: general-counsel
  primary_consumers:
  - ext-legal
  - product
  - ext-corpdev
  sensitive: true
---
# /risk-analysis

## Purpose

`/risk-analysis` produces a structured, multi-domain risk landscape for an initiative, decision, or deal. It surfaces risks, assigns severity, and suggests next steps so a human reviewer can triage exposure quickly. It is a **drafting and triage aid**, not a legal conclusion, a business case, or a go/no-go recommendation.

What it IS: an analytical first pass that names the risks across six domains and makes the review gate visible.

What it is NOT: legal advice, a regulatory opinion, a substitute for licensed counsel, or a decision. Every finding is a hypothesis for a human to verify.

---

## When to Use

Invoke `/risk-analysis` when you need to:

- Triage exposure on a new commercial proposal, partnership, or deal structure before committing resources
- Produce a risk section for a Phase 2 Strategic Decision deliverable (business case, strategic bet, pricing commitment)
- Pre-brief a GC, CFO, or COO before they engage with a live negotiation
- Stress-test a late-stage draft of a high-stakes deliverable (with `--mode adversarial`)
- Compare the risk profile of two or more alternatives at a decision point
- Frame a risk register for an outcome review or retrospective

## When NOT to Use

Do NOT use `/risk-analysis` when:

- You need a contract clause-by-clause review → use `/contract-review` (Phase 3 A1)
- You need an NDA-specific triage → use `/nda-triage` (Phase 3 A2)
- You need a privacy program audit → use `/privacy-policy-audit` (Phase 3 A3)
- You need a compliance readiness gap assessment → use `/compliance-audit` (Phase 3 A4)
- You need a contract negotiation stress test → use `/contract-stress-test` (Phase 3 A7)
- You need a licensed legal opinion → engage outside counsel; the skill will not substitute
- You need an effort or timeline estimate → out of scope; `/risk-analysis` does not opine on implementation cost

The skill deliberately sits UPSTREAM of the more specialized legal skills. Use it first to map the landscape, then spin specialized skills for the domains that surfaced as P0/P1.

---

## Modes

### Create (default)

Run the full analytical pass on a named initiative, decision, or deal. Produces a new risk-analysis output file following the structure in the Output section.

```
/risk-analysis Bank Discount Deal
/risk-analysis Legionis GTM launch
/risk-analysis Acquire CompanyX
```

### Update

Revise an existing risk analysis against new information (new counterparty response, new document, changed deal structure). Pass the path to the existing file.

```
/risk-analysis update AXIA/Product/risk-analysis-bank-discount-deal-2026-04-11.md
```

Update mode preserves the finding numbering (adds 8a, 8b rather than renumbering), marks superseded findings with `~~strikethrough~~` + a one-line reason, and keeps a changelog at the bottom of the file.

### `--mode adversarial`

Invokes Pattern 5 Adversarial Review from `delegation-protocol.md`. A fresh-context adversarial agent stress-tests the current analysis without seeing the drafter's rationale. The pattern caps at two iterations. A named human tiebreaker must be specified BEFORE the review starts.

Use adversarial mode ONLY when:

- The underlying draft is near-final, not evolving in shape
- The cost of a missed risk is material (enterprise contracts, M&A, pricing commitments, regulatory filings)
- A named human tiebreaker is available
- Time allows for the two-iteration cycle

For early-stage drafts and lower-stakes triage, use default Create mode with Pattern 1 Consultation for specialist input instead.

```
/risk-analysis Bank Discount Deal --mode adversarial --tiebreaker "Yohay Etsion"
```

---

## Inputs Required

The skill MUST collect the following before producing output. If any are missing, it asks the user rather than guessing.

| Input | Required | Example |
|---|---|---|
| Initiative or decision name | Yes | "AXIA Bank Discount Deal" |
| Jurisdiction (or authorization to assume + flag) | Yes | "Israel + U.S. Delaware" |
| Counterparty / stakeholders | Yes | "Bank Discount (Israel), AXIA (Delaware parent + Israeli sub)" |
| Relevant documents | At least one | Proposal, master plan, EULA, term sheet |
| Deal / initiative stage | Yes | "Pre-signature, proposal sent, awaiting technical deep-dive" |
| Known constraints or red lines | If known | "SOC 2 not yet certified; bridge letter required" |
| Tiebreaker (adversarial mode only) | Yes if adversarial | "Yohay Etsion" |

If jurisdiction is unknown, the skill makes a defensible assumption based on the documents and flags the assumption explicitly in the output — it does NOT silently pick.

---

## Output Structure

Every `/risk-analysis` output conforms to `sensitive-skill-guardrails.md` Section 3. Structure is non-negotiable; clarity of findings varies per analysis.

### 1. Disclaimer + UPL Guardrail Block (top)

Verbatim block from `sensitive-skill-guardrails.md` Section 3.1, with `{jurisdiction}` filled in:

```
> ⚠️ **Not legal advice.** This output is a drafting and triage aid generated
> by a product-organization skill, not counsel. No attorney-client relationship
> is created by its production or use. Jurisdiction-specific questions,
> contested matters, and any decision with material legal or regulatory
> consequences require review by a licensed attorney in the relevant
> jurisdiction. Do not rely on this output as the sole basis for any legal,
> compliance, or employment decision.
>
> **Jurisdiction Assumed:** {e.g., "Israel + U.S. Delaware"}. If your
> jurisdiction differs, treat every finding below as a hypothesis to verify
> with local counsel.
```

### 2. Jurisdiction Assumed (field)

Named, explicit, at the top of the output body. If the user specified it, quote their input. If the skill assumed it, say "Assumed by skill" and name the assumption.

### 3. `## Findings`

Numbered list. Each finding has:

- **Severity**: `P0` (blocker — must be addressed before proceeding), `P1` (important — should be addressed or explicitly accepted with written rationale), `P2` (nice-to-have — track but does not block)
- **What**: the observation or issue, grounded in a specific document or fact
- **Why it matters**: the downstream risk or implication
- **Suggested next step**: what the human reviewer should DO with this finding (verify, escalate, engage counsel, add clause, walk away)

Findings are grouped or tagged by domain (Legal / Commercial / Operational / Regulatory / Financial / Reputational) so the reviewer can triage by function. The skill does NOT hide small findings inside large ones — one atomic issue per numbered finding.

### 4. `## Reviewer Checklist`

Explicit sign-off items. This is the review gate made visible. Minimum checklist:

- [ ] Jurisdiction confirmed against actual counterparty + governing-law clause
- [ ] Material facts in each finding verified against source documents
- [ ] Counterparty context reviewed (regulated entity? works council? sovereign?)
- [ ] All P0 findings addressed or explicitly accepted as risk with named approver
- [ ] All P1 findings triaged (addressed, accepted, or escalated)
- [ ] Counsel engaged for items flagged in "Cannot Assess Without"
- [ ] Insurance coverage verified against findings with insurance implications
- [ ] Record kept of which findings were accepted-with-risk and by whom

### 5. `## Cannot Assess Without Licensed Counsel`

Explicit list of what the skill deliberately did NOT opine on. This converts scope drift from invisible to blocking. Minimum 4 items per output; more when the deal touches multiple regulated domains.

Format each as a single line: "Enforceability of {clause} in {jurisdiction}" / "Regulatory exposure under {statute}" / "Tax treatment of {structure}" / etc.

### 6. (Optional) Changelog (update mode only)

If update mode, a `## Changelog` section at the bottom listing what changed since the previous version and why.

---

## Method

The skill's analytical pass follows this sequence. The order matters — domains are not parallelized internally because downstream domains reference upstream findings.

### Step 1 — Identify Domains in Scope

The six canonical risk domains are the starting frame:

| Domain | Typical Risks |
|---|---|
| **Legal** | UPL exposure, enforceability of key clauses, governing law, IP ownership and licensing, liability caps, indemnification scope, termination conditions |
| **Commercial** | Revenue concentration, margin exposure, price protection, customer churn, renewal risk, discount stacking, precedent-setting for future deals |
| **Operational** | Delivery capacity, staffing, dependencies, integration risk, SLA exposure, incident response capability, support load |
| **Regulatory** | Industry compliance (Bank of Israel Directive 361, GDPR, HIPAA, SOX), privacy law, employment law, sector licensing, export controls, AI regulation |
| **Financial** | Cash flow impact, currency exposure, payment terms, tax treatment, transfer pricing, revenue recognition, insurance cost |
| **Reputational** | PR risk, customer trust, partner relationships, investor optics, social license, works council / labor relations |

The six domains are the starting frame, NOT a hard limit. If the deal touches ESG, cybersecurity insurance, sanctions, or antitrust, the skill adds domains as needed.

### Step 2 — Surface Risks per Domain

For each in-scope domain, the skill reads the source documents and asks:

- What obligations does this initiative create?
- What assumptions does it rest on?
- What does the counterparty expect that might not be deliverable?
- What clauses, if invoked, would hurt the most?
- What is the "bad day" scenario?

Findings MUST be grounded in something actually present in the documents. Fabricated findings are not permitted. If the skill cannot find ground for a concern, it either asks the user for clarification or moves it to "Cannot Assess Without."

### Step 3 — Assign Severity

Severity thresholds are defensible, not decorative:

- **P0 (blocker)** — if unaddressed, the deal cannot ethically or commercially proceed. Example: unbounded liability cap on a 4-person startup's first enterprise deal; uncapped indemnification for regulated data; signing counterparty is sanctioned.
- **P1 (important)** — should be addressed or explicitly accepted with a written rationale and named approver. Example: net-60 payment from a slow-paying counterparty when cash is tight; precedent clause that will be hard to walk back on the next deal.
- **P2 (nice-to-have)** — track but does not block. Example: a clause is imperfect but aligned to market norms; a risk exists but is insurable at reasonable cost.

When in doubt, escalate one level (P2 → P1, P1 → P0). The cost of being overly cautious is a longer reviewer conversation; the cost of under-severity is a missed risk.

### Step 4 — Suggest Next Steps

Each finding MUST include a specific, actionable next step. "Engage counsel" is acceptable only when paired with WHICH counsel (contracts / privacy / IP / tax / employment) and WHAT they are being asked. "Verify X against Y" is the preferred format.

The skill does NOT prescribe the decision. It prescribes the next action a human should take.

### Step 5 — Write "Cannot Assess Without"

This section is not optional and not a checkbox. It is the explicit scope boundary. The skill writes it BEFORE finalizing findings — if an item is named here, it cannot also appear as a confident finding.

---

## Delegation Patterns Available

### Default: Pattern 1 Consultation

When a specific domain needs deeper specialist input, `/risk-analysis` spawns a consultation per `delegation-protocol.md` Pattern 1:

| Trigger | Spawn |
|---|---|
| Data flow touches employee or customer PII | 🔒 Privacy Counsel |
| Deal includes equity, warrants, or revenue share | 💰 CFO or Tax Planning Specialist |
| Deal includes IP licensing or assignment | 📜 IP Counsel |
| Counterparty is in a regulated industry | ⚖️ Compliance Officer |
| M&A or corporate combination | 🏛️ M&A Analyst |
| Employment actions downstream (termination, monitoring) | 👔 Employment Counsel |

Consultations are attributed in the Findings section: "I consulted 🔒 Privacy Counsel, who noted that…". Ownership of the risk analysis stays with General Counsel.

### On Request: Pattern 5 Adversarial Review (`--mode adversarial`)

Use for near-final, high-stakes deliverables. Pattern 5 requires:

1. A **named human tiebreaker** specified BEFORE the review starts
2. **Fresh-context spawn** of the adversarial agent (no prior-turn rationale, no earlier iterations)
3. **Maximum two iterations** (diminishing returns cap)
4. **Role separation**: the drafter sees adversarial findings AFTER they are produced, not during generation

Contested findings (drafter and adversarial agent disagree on severity or the drafter wants accept-with-risk on a P0) go to the named tiebreaker for resolution. Unresolved contests block publication.

Do NOT use Pattern 5 for: early-stage drafts, low-stakes triage, or when the goal is collaborative improvement (that is Pattern 3 Review).

---

## Quality Gates

`/risk-analysis` is a sensitive skill. It ships only after passing the two-pass publication gate defined in `sensitive-skill-guardrails.md` Section 4:

- **Pass 1 — Scaffolding Check** — 📋 Director of Legal Affairs verifies the structure (disclaimer, jurisdiction field, Findings, Reviewer Checklist, Cannot Assess Without, frontmatter, ROI framing, delegation citation, first-principles authoring). 15 minutes, binary GO / REWORK.
- **Pass 2 — Substantive Check** — ⚖️ General Counsel verifies the legal reasoning, severity thresholds, delegation-pattern appropriateness, scope boundary correctness, jurisdiction defaults, and edge cases. 5 business days SLA for this first-of-type Phase 3 legal skill; 72 hours for subsequent similar skills.

On every invocation, the skill self-checks against Section 7 of `sensitive-skill-guardrails.md` BEFORE producing output. If the self-check fails on any item, the output does not publish.

---

## ROI Framing

ROI for `/risk-analysis` is reported as **"time saved on drafting and triage of a risk landscape"** — NEVER "time saved on legal review."

Legal rate: $300-400/hr blended per `feedback_roi_rates.md`. Default $350/hr for a Phase 2 risk landscape across six domains on a live deal.

Time-saved baseline: authoring a structured 8-15 finding risk landscape against a multi-document source set = ~3-5 hours manual drafting and triage time for a senior practitioner (not counting substantive review, which happens on top regardless of whether the skill is used).

Example ROI line for a standard run:

```
⏱️ ~4 hrs saved in 90s, 28k tkns ~$1.8 cost, Value ~$1,400
```

The ROI explicitly tracks time the skill saves on drafting a structured risk artifact, not time it saves on review. The substantive review by General Counsel still happens in full.

---

## Attribution and Maintenance

**Owner**: ⚖️ General Counsel. The skill's reasoning is General Counsel's accountability.

**Consumers** (gateways that invoke this skill):
- `ext-legal` — legal team gateway, primary user
- `product` — product gateway when PM/VP Product needs risk triage before a Phase 2 decision
- `ext-corpdev` — corp dev gateway for M&A and partnership deal triage

New consumers require a frontmatter update and a one-line note in the consuming gateway's skill list. Adding a consumer does not change the skill's reasoning — it changes who can invoke it.

**Authoring**: First-principles. This skill was authored from scratch during Phase 3 Sub-phase 3.0, not forked from an existing skill or lifted from a template. Subsequent Phase 3 legal skills (A1-A4, A7) inherit this structure but are authored independently — they do not copy content from this skill.

**Updates**: Via the two-pass publication gate. Minor edits (typos, formatting) can bypass Pass 2. Any edit touching severity thresholds, domain definitions, delegation patterns, or the output structure requires a full Pass 2 substantive review.

**Changelog**: Maintained at the bottom of this file. Version 1.0.0 — initial authoring 2026-04-11.

---

## Example Invocation

```
User: /risk-analysis Bank Discount Deal

/risk-analysis v1.0.0 — reading:
  - AXIA/Product/bank-discount-proposal-v3.md
  - AXIA/Product/bank-discount-master-plan.md

Collecting inputs:
  - Initiative: AXIA Bank Discount Deal
  - Jurisdiction: Assumed Israel (governing law) + Delaware (AXIA parent entity). Flagged as assumption — confirm in Order Form governing-law clause.
  - Counterparty: Bank Discount (Israel Discount Bank), Top-5 Israeli bank, regulated by Bank of Israel Directive 361
  - Stage: Pre-signature, proposal v3 drafted, awaiting technical deep-dive
  - Known constraints: SOC 2 not yet certified, bridge letter required; 4-person startup delivery capacity; AXIA Israeli entity not yet formed

Producing output at:
  AXIA/Product/risk-analysis-bank-discount-deal-2026-04-11.md

[output follows standard structure: disclaimer → jurisdiction → findings →
 reviewer checklist → cannot assess without]

⏱️ ~4 hrs saved in 90s, 28k tkns ~$1.8 cost, Value ~$1,400
```

---

## Changelog

- **1.0.0 (2026-04-11)** — Initial authoring. First-principles during Phase 3 Sub-phase 3.0 scaffolding. Template skill for A1-A4, A7 Phase 3 legal skills. Substantive review passed by ⚖️ General Counsel; scaffolding review passed by 📋 Director of Legal Affairs.
