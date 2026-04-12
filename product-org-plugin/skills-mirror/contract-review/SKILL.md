---
name: contract-review
description: Produces a clause-by-clause triage of a specific contract against a structured clause library and sensitive-skill-guardrails, as a drafting and triage aid for human review, not a legal opinion.
argument-hint: '[contract path or counterparty name] or [update path/to/contract-review.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: legal-contracts
  skill_type: task-capability
  owner: contracts-counsel
  primary_consumers:
  - ext-legal
  - product
  - ext-corpdev
  sensitive: true
---
# /contract-review

## Purpose

`/contract-review` produces a clause-by-clause triage of a specific contract. For each clause category in the library, it asks the reviewer questions, flags red flags, surfaces missing clauses that should be present, and points at cross-clause interactions that only become visible when the whole contract is read at once. It is a **drafting and triage aid**, not a legal opinion, not a redlined markup, and not a negotiation strategy.

What it IS: an analytical ground-truth pass that names what each clause actually says (versus what a summary or master plan claims it says), flags deviations from market norms and from the clause library, and hands the reviewer a checklist of sign-offs.

What it is NOT: legal advice, a substitute for licensed counsel, a redline authoring tool, or a go/no-sign recommendation. Every finding is a hypothesis grounded in a specific clause of a specific contract, for a human to verify.

---

## When to Use

Invoke `/contract-review` when you need to:

- Triage a draft contract (one we authored, or one received from a counterparty) before the first round of negotiation
- Ground-truth what a specific contract actually says when upstream summaries, master plans, or risk analyses may be relying on paraphrase rather than the actual text
- Re-review a contract after the counterparty has proposed redlines (Update mode)
- Populate or extend the clause library with patterns observed in a real document
- Prepare a clause-level checklist for General Counsel before a substantive review
- Stress-test an enterprise contract before signature with an adversarial pass (`--mode adversarial`)

## When NOT to Use

Do NOT use `/contract-review` when:

- You need an initiative-level or deal-level risk landscape across six domains → use `/risk-analysis` (Phase 3 A5). `/risk-analysis` is upstream — it asks "what could hurt us across all functions?" `/contract-review` is downstream — it asks "what does this specific contract actually say, clause by clause?"
- You need an NDA-specific triage with confidentiality, term, and residuals as the focus → use `/nda-triage` (Phase 3 A2)
- You need a privacy-program audit across an organization → use `/privacy-policy-audit` (Phase 3 A3)
- You need a compliance-readiness gap assessment for a regulated entity → use `/compliance-audit` (Phase 3 A4)
- You need a near-final contract stress-tested with fresh-context adversarial pressure → use `/contract-stress-test` (Phase 3 A7). Contract-review can run adversarial sub-mode, but A7 is the canonical pattern for near-final documents.
- You need a licensed legal opinion — engage outside counsel; the skill does not substitute
- You need a negotiation strategy or redline language for a non-standard position — the skill may flag deviation and suggest boilerplate redlines ONLY where market convergence is clear; it will not author novel negotiating positions

The skill deliberately sits DOWNSTREAM of `/risk-analysis` and UPSTREAM of specialist legal review. It is where the abstract risk landscape meets the concrete contract text.

---

## Modes

### Create (default)

Run a full clause-by-clause pass on a specific contract. Produces a new contract-review output file following the structure in the Output section.

```
/contract-review AXIA-Enterprise-License-Agreement-v2.pdf
/contract-review "SKYMOD watch vendor SOW"
/contract-review "Legionis reseller agreement - draft from Acme"
```

### Update

Re-review an existing contract after counterparty redlines or an internal revision. Pass the path to the existing contract-review output.

```
/contract-review update AXIA/Product/contract-review-eula-v2-2026-04-11.md
```

Update mode preserves the finding numbering (adds 7a, 7b rather than renumbering), marks resolved findings with `~~strikethrough~~` plus a one-line reason, and keeps a `## Changelog` at the bottom of the file noting what clauses the counterparty moved on.

### `--mode adversarial`

Invokes Pattern 5 Adversarial Review from `delegation-protocol.md`. A fresh-context adversarial agent (typically `@general-counsel` or a peer `@contracts-counsel` instance) stress-tests the current contract-review findings without seeing the drafter's rationale. The pattern caps at two iterations. A named human tiebreaker must be specified BEFORE the review starts.

Use adversarial sub-mode ONLY when:

- The contract is enterprise-scale (uncapped or large aggregate exposure, multi-year term, novel structure)
- The cost of a missed clause issue is material (enterprise deals, M&A, IP licensing, regulatory filings)
- A named human tiebreaker is available
- The contract draft is near-final, not still evolving in shape

```
/contract-review AXIA-EULA-v2 --mode adversarial --tiebreaker "Yohay Etsion"
```

For early-stage drafts, routine contracts, and low-stakes triage, use default Create mode with Pattern 1 Consultation to pull in specialists (Privacy Counsel, IP Counsel, Tax Planning) for the clauses that need their view.

---

## Inputs Required

The skill MUST collect the following before producing output. If any are missing, it asks the user rather than guessing.

| Input | Required | Example |
|---|---|---|
| Contract document (path or content) | Yes | `AXIA/Marketing/Collaterals/AXIA-EULA-v2.pdf` |
| Deal type | Yes | Vendor / Customer / Partnership / IP licensing / SaaS / NDA / Employment |
| Our stance | Yes | "Paper on paper" (we authored), "Theirs with redlines" (counterparty authored), "Joint draft" |
| Counterparty context | Yes | "Top-5 Israeli bank, regulated by Bank of Israel" / "US SaaS vendor, mid-market" |
| Jurisdiction (or authorization to assume + flag) | Yes | "Israel + U.S. Delaware" |
| Known red lines | If known | "No uncapped indemnity", "No assignment without consent", "Data residency must be Israel" |
| Specific clauses of concern | If any | "Section 8.2 LoL cap" / "Schedule D Order Form" |
| Tiebreaker (adversarial mode only) | Yes if adversarial | "Yohay Etsion" |

If jurisdiction is unknown, the skill reads the governing-law clause of the contract itself and reports what IT says, rather than silently picking a default. If the contract is multi-jurisdictional (as AXIA EULA v2 is — Israel for Israeli customers, Delaware for Americas customers), the skill names both and flags which one applies to the deal under review.

---

## Output Structure

Every `/contract-review` output conforms to `sensitive-skill-guardrails.md` Section 3. Structure is non-negotiable; substantive findings vary per contract.

### 1. Disclaimer + UPL Guardrail Block (top)

Verbatim block from `sensitive-skill-guardrails.md` Section 3.1, with `{jurisdiction}` filled in from the contract's governing-law clause (not assumed — read off the document).

### 2. Contract Metadata block

A small labeled block under the disclaimer with:

- **Contract**: title and version as written on the cover
- **Parties**: the named entities
- **Effective Date**: as written, or `[blank]` if the contract is a template
- **Our Stance**: `paper on paper` / `theirs with redlines` / `joint draft`
- **Deal Type**: vendor / customer / partnership / IP licensing / SaaS / NDA / employment
- **Jurisdiction Assumed**: from the governing-law clause; if multi-jurisdictional, named explicitly
- **Clause library version used**: the date of `clause-patterns.md` at the time of review

This block makes the inputs explicit and versionable.

### 3. `## Findings`

Numbered list. Each finding has:

- **Clause reference**: the specific section, sub-section, or schedule number as written in the contract (e.g., "Section 11.1", "DPA Section 9.4.1", "Schedule D §2.1"). If the clause is ABSENT (a missing-clause finding), the finding says "`[ABSENT]`" and names where it would normally appear.
- **Clause category**: one of the 10 library categories, or contract-type-specific (e.g., SLA, Royalty)
- **Severity**: `P0` (blocker — must be addressed before signature), `P1` (important — should be addressed or explicitly accepted), `P2` (nice-to-have — track but does not block)
- **What the clause says** (or doesn't): grounded quote or precise paraphrase
- **Why it matters**: the downstream risk or implication
- **Suggested next step**: verify, redline, engage specialist, escalate to GC, etc.

Findings are grouped or tagged by clause category. Missing-clause findings (things that SHOULD be in the contract and are not) are tagged `[MISSING]` and are often more important than present-but-bad clauses. Cross-clause interaction findings (e.g., the LoL cap in Section 11.1 conflicts with the carve-out scope in Section 11.3) are tagged `[CROSS-CLAUSE]`.

### 4. `## Reviewer Checklist`

Explicit sign-off items, clause by clause. Minimum checklist:

- [ ] Governing law and venue confirmed against counterparty domicile (if multi-jurisdictional contract, the applicable clause is unambiguous)
- [ ] All named parties have full legal names and entity types matching corporate registrations
- [ ] Every P0 finding addressed in redline or explicitly accepted-with-risk by named approver
- [ ] Every P1 finding triaged (addressed, accepted, or escalated)
- [ ] Every `[MISSING]` finding either added as a clause or explicitly waived with documented reason
- [ ] Every `[CROSS-CLAUSE]` finding verified — the interaction works in both directions
- [ ] All Schedules and Exhibits referenced from the core agreement are actually attached (no orphan references)
- [ ] Survival clause covers all obligations that must survive termination (confidentiality, indemnity, accrued fees, IP)
- [ ] Counsel engaged for items in "Cannot Assess Without"
- [ ] Insurance (E&O, D&O, cyber) verified against liability cap and indemnity scope
- [ ] Clause-by-clause sign-off recorded; any deviation from clause library noted with rationale

### 5. `## Cannot Assess Without Licensed Counsel`

Explicit list of what the skill deliberately did NOT opine on. Minimum 5 items; more for multi-jurisdiction contracts or regulated-industry counterparties.

Format each as a single line: "Enforceability of {clause} in {jurisdiction}" / "Regulatory exposure under {statute}" / "Tax treatment of {structure}" / etc.

### 6. (Optional) Changelog (update mode only)

If update mode, a `## Changelog` section at the bottom listing what the counterparty (or our drafter) moved on since the prior review, which findings were resolved, which became moot, and which new findings appeared.

---

## Method

The skill's clause-by-clause pass follows this sequence. Order matters because later steps depend on the output of earlier ones.

### Step 1 — Parse the Contract into its Clause Categories

Read the contract end-to-end. Do NOT skim. Build an internal map of:

- The clause categories that ARE present (using `clause-patterns.md` as the checklist)
- The clause categories that are NOT present (missing-clause candidates)
- The Schedules, Exhibits, Annexes, and DPAs that are attached vs. referenced but missing
- The cross-references inside the document (Section X references Section Y — verify Y exists and says what X claims)

If the contract is long (> 50 pages), the skill may chunk the reading, but it never produces findings on a clause it has not actually read.

### Step 2 — Apply the Clause Library, Category by Category

For each clause category present, the skill pulls the reviewer questions and red flags from `clause-patterns.md` and runs them against the actual clause text. For each:

- Does the clause match a known pattern in the library?
- Which of the library's red flags are present?
- Which of the library's reviewer questions can the clause answer, and which require specialist input?
- Does the clause deviate from market norms? If so, in whose favor?

Findings are ONLY produced when grounded in specific clause text. The skill does not say "this is probably bad" — it says "Section 8.2 disclaims implied warranties to the maximum extent permitted by applicable law, and does not name a fallback where the disclaimer is unenforceable."

### Step 3 — Surface Missing Clauses (`[MISSING]`)

For each clause category in the library that is NOT present in the contract, ask:

- Should this clause be here, given the deal type?
- What is the downstream risk of its absence?
- Is the absence deliberate (e.g., NDA contracts don't need IP Assignment) or an omission?

Missing-clause findings are often the most important. Reviewers pattern-match on what they SEE and miss what is absent.

### Step 4 — Surface Cross-Clause Interactions (`[CROSS-CLAUSE]`)

Once all clauses have been read individually, look at them together:

- Does the LoL cap (Section 11) align with the indemnity scope (Section 11 or elsewhere) and the insurance coverage commitment?
- Does the survival clause (usually in Termination) actually cover every obligation that should survive (confidentiality, fees, indemnity, IP)?
- Does the governing-law clause (one jurisdiction) conflict with the DPA (which may default to a different one)?
- Does the order-of-precedence clause put the DPA above the core EULA, or does a conflict become unresolvable?
- Does the IP clause transfer ownership in a way that conflicts with the licensing grant?

Cross-clause findings are the ones a clause-by-clause checklist misses. They only become visible when the whole document is in the reviewer's head at once.

### Step 5 — Assign Severity

Severity thresholds are defensible, not decorative:

- **P0 (blocker)** — if unaddressed, the contract should not be signed. Examples: uncapped liability on a startup's enterprise deal; missing data-processing addendum on EU/UK data; counterparty can terminate at will and we cannot; IP assignment sweeps in unrelated background IP; signing counterparty is a sanctioned entity.
- **P1 (important)** — should be addressed in redline or explicitly accepted with written rationale and named approver. Examples: liability cap is defensible but deviates from counterparty's usual; survival clause misses one obligation; sub-processor consent is vague; renewal auto-extends without a usable opt-out window.
- **P2 (nice-to-have)** — track but does not block. Examples: clause is imperfect but aligned with market norm; definition is slightly loose; cross-reference formatting is inconsistent.

When in doubt, escalate one level (P2 → P1, P1 → P0). The cost of being overly cautious is a longer reviewer conversation; the cost of under-severity is a missed issue at the counterparty's negotiation table.

### Step 6 — Suggest Next Steps

Each finding MUST include a specific next step. Acceptable forms:

- `Verify {X} against {Y}`
- `Redline to {specific change}` — only where market convergence is clear and the change is standard; not a novel negotiating position
- `Engage {specialist counsel} on {clause}`
- `Escalate to {GC/VP/CFO} for accept-with-risk decision`
- `Add missing {clause name} clause; sample language from library`

The skill does NOT author novel contract language. It points at the clause library and at specialists.

### Step 7 — Write "Cannot Assess Without"

Written BEFORE finalizing findings. If an item goes here, it cannot also appear as a confident finding. The section is how the skill makes its scope explicit.

---

## Delegation Patterns Available

### Default: Pattern 1 Consultation

When a specific clause category needs specialist input, `/contract-review` spawns a consultation per `delegation-protocol.md` Pattern 1:

| Trigger | Spawn |
|---|---|
| DPA, data residency, sub-processors, cross-border transfer | 🔒 Privacy Counsel |
| IP assignment, licensing grant, background IP, derivatives | 📜 IP Counsel |
| Payment structure, revenue share, equity, warrants, withholding | 💰 Tax Planning Specialist |
| Counterparty is a regulated entity (bank, healthcare, insurance) | ⚖️ Compliance Officer |
| Employment implications (monitoring, termination, PIP-adjacent) | 👔 Employment Counsel |
| Insurance coverage alignment against LoL cap + indemnity scope | 🛡️ Risk Manager |
| Multi-jurisdictional enforcement (forum, venue, enforceability) | ⚖️ General Counsel |
| Deal structure touches M&A, earn-out, asset vs. stock | 🏛️ M&A Analyst |

Consultations are attributed in the Findings section: "I consulted 🔒 Privacy Counsel, who noted that the DPA's 2-hour breach notification window is tighter than GDPR's 72-hour baseline but matches Bank of Israel Directive 361 expectations." Ownership of the contract review stays with Contracts Counsel.

### On Request: Pattern 5 Adversarial Review (`--mode adversarial`)

Use for enterprise contracts where the cost of a missed clause issue is material. Requires all four Pattern 5 guardrails: named human tiebreaker before the review starts, fresh-context spawn of the adversarial agent, maximum two iterations, and role separation (drafter does not see adversarial findings until after they are produced).

Do NOT use Pattern 5 for routine contracts, early-stage drafts, or deliverables where one "correct" answer exists. Use `/contract-stress-test` (A7) for the canonical near-final stress-test pattern; `/contract-review --mode adversarial` is a lighter-weight version for mid-review adversarial pressure without a full A7 engagement.

---

## Quality Gates

`/contract-review` is a sensitive skill. It ships only after passing the two-pass publication gate defined in `sensitive-skill-guardrails.md` Section 4:

- **Pass 1 — Scaffolding Check** — 📋 Director of Legal Affairs verifies the structure (disclaimer, contract metadata, Findings, Reviewer Checklist, Cannot Assess Without, frontmatter, ROI framing, delegation citation, first-principles authoring, clause library attribution). 15 minutes, binary GO / REWORK.
- **Pass 2 — Substantive Check** — ⚖️ General Counsel verifies the legal reasoning, severity thresholds, missing-clause coverage, cross-clause interaction logic, delegation-pattern appropriateness, scope boundary correctness, jurisdiction handling, and edge cases. **72-hour SLA** for subsequent-similar Phase 3 legal skills; the template pattern was validated by A5 `/risk-analysis` publication earlier today, so A1 inherits the subsequent-similar timeline rather than the 5-business-day first-of-type SLA.

On every invocation, the skill self-checks against Section 7 of `sensitive-skill-guardrails.md` BEFORE producing output. If the self-check fails on any item, the output does not publish.

---

## ROI Framing

ROI for `/contract-review` is reported as **"time saved on drafting and triage of a clause-by-clause contract review"** — NEVER "time saved on legal review."

Legal rate: $300-400/hr blended per `feedback_roi_rates.md`. Default $350/hr for a Phase 3 contract triage across 10-15 clause categories on a multi-schedule enterprise contract.

Time-saved baseline: a structured clause-by-clause triage of a 20-30 page enterprise contract with 2-4 schedules, producing 12-20 findings tied to specific clauses, is ~4-6 hours of manual drafting and triage time for a senior practitioner. Simpler contracts (NDAs, standard vendor SOWs) are 1-2 hours baseline. Mega-contracts with 5+ schedules, novel structure, or multi-jurisdictional complexity are 8+ hours baseline.

The ROI tracks ONLY the time the skill saves on drafting the structured artifact, not the substantive legal review time. The substantive review by Contracts Counsel and General Counsel still happens in full.

Example ROI line for a standard enterprise contract review:

```
⏱️ ~5 hrs saved in 90s, 30k tkns ~$1.9 cost, Value ~$1,750
```

---

## Attribution and Maintenance

**Owner**: 📄 Contracts Counsel. The skill's clause-by-clause reasoning is Contracts Counsel's accountability. The severity thresholds and the clause library are jointly owned with ⚖️ General Counsel.

**Consumers** (gateways that invoke this skill):
- `ext-legal` — legal team gateway, primary user
- `product` — product gateway when PM/VP Product receives a vendor SOW or customer redline and needs a clause-level triage before engaging counsel
- `ext-corpdev` — corp dev gateway for partnership agreements, IP licensing deals, and M&A ancillary documents

New consumers require a frontmatter update and a one-line note in the consuming gateway's skill list.

**Authoring**: First-principles. This skill was authored from scratch during Phase 3 Sub-phase 3.0, inheriting the structural pattern from A5 `/risk-analysis` (also first-principles) but with entirely original content. A1 is the first contract-specific skill; subsequent contract skills (A2 `/nda-triage`, A7 `/contract-stress-test`) inherit the clause-library pattern from here.

**Clause library dependency**: `/contract-review` reads from `reference/clause-patterns.md`. When the library is updated, `/contract-review` picks up the new patterns automatically. The library's version (date) is recorded in the Contract Metadata block of every output for traceability.

**Updates**: Via the two-pass publication gate. Minor edits (typos, formatting) can bypass Pass 2. Any edit touching severity thresholds, clause-category list, delegation patterns, or the output structure requires a full Pass 2 substantive review by General Counsel.

**Changelog**: Maintained at the bottom of this file. Version 1.0.0 — initial authoring 2026-04-11.

---

## Example Invocation

```
User: /contract-review AXIA-Enterprise-License-Agreement-v2.pdf

/contract-review v1.0.0 — reading:
  - AXIA/Marketing/Collaterals/AXIA-Enterprise-License-Agreement-v2.pdf
    (core EULA + Schedules A-D inline, approx 30 pages)

Collecting inputs:
  - Contract: AXIA Enterprise License Agreement v2.0
  - Parties: Axia Security Ltd. (Israel) + [Customer]
  - Deal Type: SaaS / enterprise license
  - Our Stance: Paper on paper (we authored)
  - Counterparty Context: First use against Bank Discount (regulated Israeli bank)
  - Jurisdiction: Section 14.1 — Israel for Israeli customers, Delaware for Americas.
    Bank Discount is Israeli → Section 14.1(a) applies.
  - Clause library version: 2026-04-11 (seed corpus; this review is part of the bootstrap)

Producing output at:
  AXIA/Product/contract-review-eula-v2-2026-04-11.md

[output follows standard structure: disclaimer → contract metadata → findings →
 reviewer checklist → cannot assess without]

⏱️ ~5 hrs saved in 90s, 30k tkns ~$1.9 cost, Value ~$1,750
```

---

## Changelog

- **1.0.0 (2026-04-11)** — Initial authoring. First-principles during Phase 3 Sub-phase 3.0. First contract-specific skill. Birth-tested against AXIA Enterprise License Agreement v2.0 with 14 clause-level findings; bootstrapped the initial `clause-patterns.md` library from the review. Substantive review passed by ⚖️ General Counsel on the 72-hour subsequent-similar SLA (A5 `/risk-analysis` validated the template pattern earlier today); scaffolding review passed by 📋 Director of Legal Affairs.