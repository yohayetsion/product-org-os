---
name: nda-triage
description: Produces a decision-tree triage of an NDA leading to a verdict (sign-as-is / minor redlines / substantial negotiation / refuse), as a drafting and triage aid for human review, not a legal opinion.
argument-hint: '[NDA path or counterparty name] or [update path/to/nda-triage.md]'
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
  - sales
  sensitive: true
---
# /nda-triage

## Purpose

`/nda-triage` walks an NDA through a short **decision tree** of 5-7 high-leverage questions and lands on a **triage verdict**: Sign As-Is / Minor Redlines / Substantial Negotiation / Refuse or Walk Away. It is tightly scoped: it does NOT produce a full clause-by-clause contract review, and it does NOT author novel negotiating positions. It is a **drafting and triage aid** built for inbound-speed review of a high-volume, comparatively standard contract type.

What it IS: a structured triage that names the 3-5 findings that drove the verdict, tied to specific clauses in the specific NDA, so a reviewer can act in minutes rather than hours.

What it is NOT: legal advice, a substitute for licensed counsel, a full clause-by-clause review across all contract categories, a redline authoring tool, or a go/no-sign decision. Every finding is a hypothesis grounded in a specific clause of a specific NDA, for a human to verify.

The decision tree is the load-bearing idea. NDAs have a narrow surface area and a small number of clauses that almost always determine whether the document is safe to sign, worth negotiating, or structurally broken. The skill asks those questions in order, scores the answers, tallies them into verdict buckets, and emits the verdict plus the findings that drove it.

---

## When to Use

Invoke `/nda-triage` when you need to:

- Triage an inbound NDA at the speed of a sales or BD workflow (counterparty sent us their paper; we need a call in hours, not days)
- Triage our own outbound NDA before sending it to a counterparty, to catch anything unusual before it leaves
- Re-triage an NDA after the counterparty has proposed redlines (Update mode)
- Stress-test a high-value or structurally unusual NDA with an adversarial pass (`--mode adversarial`)
- Produce a one-page triage artifact that a non-lawyer stakeholder (PM, sales, BD, CorpDev) can act on

## When NOT to Use

Do NOT use `/nda-triage` when:

- You need a clause-by-clause review of an enterprise contract with multiple schedules → use `/contract-review` (Phase 3 A1). A1 is the full clause-library pass; A2 is the narrow decision-tree pass on an NDA.
- You need an initiative-level or deal-level risk landscape across six domains → use `/risk-analysis` (Phase 3 A5). `/risk-analysis` is upstream of this skill — it asks "what could hurt us across all functions?" `/nda-triage` asks "does this specific NDA land safely on the triage decision tree?"
- You need a privacy-program audit across an organization → use `/privacy-policy-audit` (Phase 3 A3)
- You need a compliance-readiness gap assessment for a regulated entity → use `/compliance-audit` (Phase 3 A4)
- You need a near-final contract stress-tested with fresh-context adversarial pressure → use `/contract-stress-test` (Phase 3 A7)
- The document is labeled "NDA" but is actually a full commercial agreement with confidentiality as one section → use `/contract-review`
- You need a licensed legal opinion — engage outside counsel; the skill does not substitute
- You need to author novel negotiation language for a non-standard position

The skill deliberately sits DOWNSTREAM of `/risk-analysis` and UPSTREAM of specialist legal review. It is the first-pass filter that decides whether an NDA is even worth spending more time on, and if so, where.

---

## Modes

### Create (default)

Run a decision-tree triage on a specific NDA. Produces a new nda-triage output file.

```
/nda-triage "SKYMOD vendor NDA from Acme Corp"
/nda-triage AXIA/Marketing/nda-draft-mutual-2026.pdf
/nda-triage "Legionis inbound NDA from enterprise prospect"
```

### Update

Re-triage after counterparty (or our) redlines. Pass the path to the prior triage output.

```
/nda-triage update ProductBeacon/Sales/nda-triage-acme-2026-04-11.md
```

Update mode preserves finding numbering (adds 3a, 3b rather than renumbering), marks resolved findings with `~~strikethrough~~` plus a one-line reason, re-runs the decision tree, and records the verdict change (if any) in a `## Changelog` at the bottom.

### `--mode adversarial`

Invokes Pattern 5 Adversarial Review from `delegation-protocol.md`. A fresh-context adversarial agent stress-tests the current triage without seeing the drafter's rationale. Caps at two iterations. A named human tiebreaker must be specified BEFORE the review starts.

Use adversarial sub-mode ONLY when:

- The NDA protects unusually high-value information (M&A target, unreleased IP, regulated data)
- The counterparty is a direct competitor, a regulated entity, or a sovereign actor
- The NDA has unusual structural features (perpetual term, global assignment, indemnity inside an NDA, etc.)
- A named human tiebreaker is available

```
/nda-triage nda-mna-target --mode adversarial --tiebreaker "Yohay Etsion"
```

For routine vendor and sales NDAs, use default Create mode with Pattern 1 Consultation for specialist questions (IP Counsel, Privacy Counsel, Employment Counsel).

---

## Inputs Required

The skill MUST collect the following before producing output. If any are missing, it asks the user rather than guessing.

| Input | Required | Example |
|---|---|---|
| NDA document (path or content) | Yes | `inbound/acme-nda-v1.pdf` |
| Counterparty | Yes | "Acme Corp, US SaaS vendor" |
| Direction | Yes | `one-way (we disclose)` / `one-way (we receive)` / `mutual` |
| Our role | Yes | `discloser` / `receiver` / `both` |
| Purpose of disclosure | Yes | "Evaluating Acme as a SOC 2 audit vendor" |
| Deal context | Yes | "Initial vendor qualification, no commitment" |
| Jurisdiction (or authorization to read off document) | Yes | "Reads governing-law clause and reports what IT says" |
| Known red lines | If known | "No non-solicit in any form", "Term capped at 3 years", "No assignment without consent" |
| Tiebreaker (adversarial mode only) | Yes if adversarial | "Yohay Etsion" |

If jurisdiction is unknown, the skill reads the governing-law clause of the NDA itself and reports what IT says, rather than silently picking a default. If the NDA is silent on governing law, that is itself a P0 finding.

---

## Output Structure

Every `/nda-triage` output conforms to `sensitive-skill-guardrails.md` Section 3. Structure is non-negotiable; substantive findings vary per NDA.

### 1. Disclaimer + UPL Guardrail Block (top)

Verbatim block from `sensitive-skill-guardrails.md` Section 3.1, with `{jurisdiction}` filled in from the NDA's governing-law clause (or marked `[NDA is silent — see Finding N]` if absent).

### 2. NDA Metadata Block

A small labeled block under the disclaimer with:

- **NDA**: title as written
- **Parties**: named entities
- **Effective Date**: as written, or `[blank]` if template
- **Direction**: one-way (we disclose) / one-way (we receive) / mutual
- **Our Role**: discloser / receiver / both
- **Purpose**: the stated business purpose of the disclosure
- **Jurisdiction Assumed**: read off the governing-law clause
- **Clause library version used**: date of `clause-patterns.md` at review time

### 3. `## Triage Verdict`

**This section is unique to A2 and appears BEFORE Findings.** Exactly one of:

- **Sign As-Is** — No findings above P2. No structural issues. No deviation from market norms in ways that matter.
- **Minor Redlines** — 1-3 findings at P1, zero at P0. Standard redlines available from library; counterparty is likely to accept.
- **Substantial Negotiation** — Multiple P1 findings OR one or more findings where market convergence is weak and negotiation is required. Engage Contracts Counsel for a full pass.
- **Refuse / Walk Away** — Any P0 finding that cannot be cured (e.g., hidden non-solicit in a vendor NDA, perpetual term on inbound commercial disclosure, assignment-of-inventions masquerading as confidentiality, counterparty is a sanctioned entity, NDA attempts to bind unrelated affiliates without consent).

**Rationale**: 1-2 sentences naming the findings that drove the verdict. E.g., "Minor Redlines — Finding 2 (definition of Confidential Information is over-broad) and Finding 4 (term is 5 years; our red line is 3) are both P1 but both match library boilerplate for a counterparty reply."

### 4. `## Findings`

Numbered list of 3-5 findings — the ones that drove the verdict. `/nda-triage` is deliberately tighter than `/contract-review`: we do not try to surface every imperfection, only the ones that moved the verdict needle.

Each finding has:

- **Clause reference**: specific section or subsection as written in the NDA (e.g., "Section 3", "§2.1(b)"). If ABSENT, the finding says `[ABSENT]` and names where it would normally appear.
- **Decision-tree question**: which of the 7 tree questions this finding came from (Q1 through Q7)
- **Severity**: P0 (blocker — feeds Refuse or Substantial Negotiation) / P1 (important — feeds Substantial or Minor Redlines) / P2 (nice-to-have — does not move the verdict)
- **What the clause says** (or doesn't): grounded quote or precise paraphrase
- **Why it matters**: downstream risk or implication, tied to our role (discloser vs receiver) and the business purpose
- **Suggested next step**: verify, redline to library boilerplate, engage specialist, escalate to GC, or refuse

Findings omitted from the main list (P2 items that did not move the verdict) can be captured in a short `### Also Noted` subsection after the main findings — they exist for traceability but are explicitly not part of the verdict rationale.

### 5. `## Reviewer Checklist`

Explicit sign-off items:

- [ ] Direction and reciprocity match the deal intent (mutual where mutual is expected; one-way where one-way is expected)
- [ ] Definition of Confidential Information scoped to the purpose and the disclosure type
- [ ] Permitted uses explicitly limited to the stated purpose
- [ ] Term is reasonable for the type of information (trade secrets may require indefinite survival; routine business info typically 2-3 years)
- [ ] Return/destruction obligations are mandatory, verifiable, and have a deadline
- [ ] Exclusions/carve-outs cover the standard four (rightfully received, independently developed, publicly available, required by law)
- [ ] No hidden non-solicit, non-compete, or assignment-of-inventions clauses
- [ ] Governing law and venue are unambiguous and enforceable against this counterparty
- [ ] Every P0 finding addressed in redline or the NDA refused
- [ ] Every P1 finding triaged (addressed, accepted, or escalated)
- [ ] Specialist consultations attached (IP Counsel / Privacy Counsel / Employment Counsel) where findings triggered them

### 6. `## Cannot Assess Without Licensed Counsel`

Explicit list of what the skill deliberately did NOT opine on. Minimum 5 items for an NDA triage.

Format each as a single line: "Enforceability of {clause} in {jurisdiction}" / "Interaction with {statute}" / "Treatment of {structure} under local employment law" / etc.

### 7. (Optional) Changelog (update mode only)

A `## Changelog` at the bottom listing what moved, which findings resolved, which became moot, and whether the verdict changed.

---

## The Decision Tree

This is the load-bearing section of A2. The skill runs through 7 questions in order, scoring each branch into one of four buckets. At the end, the bucket with the highest score sets the verdict, with an explicit tie-break rule.

### Q1 — Direction and Reciprocity

**Question**: Is this a mutual NDA, a one-way NDA (we disclose), or a one-way NDA (we receive)? Does the direction match the deal intent?

**Branches**:
- **Match** (mutual deal → mutual NDA, one-way deal → one-way NDA) → +1 Sign As-Is
- **Mismatch, favorable to us** (we only receive, counterparty's NDA only protects us) → +1 Sign As-Is, note for discloser's own record
- **Mismatch, unfavorable to us** (we disclose too but NDA only protects counterparty) → +1 Minor Redlines (ask to make mutual), or +1 Substantial Negotiation if counterparty refuses
- **Structurally broken** (e.g., mutual NDA but definitions only cover counterparty's info) → +1 Refuse until fixed

### Q2 — Definition of Confidential Information

**Question**: Is "Confidential Information" defined narrowly (tied to the purpose, marked or identifiable, excluded for the standard four categories) or as a broad sweep (everything the discloser ever says or does)?

**Branches**:
- **Narrow, purpose-scoped, with all four exclusions** → +1 Sign As-Is
- **Broad but with all four exclusions and a reasonable marking/identification requirement** → +1 Minor Redlines
- **Broad, missing one or more of the four exclusions** → +1 Substantial Negotiation (library boilerplate for exclusions is standard; getting it back is usually easy but requires a round-trip)
- **Broad, no exclusions, and includes things like "any information disclosed, observed, or derived"** → +1 Refuse (this sweeps in residuals and independent development and is usually unenforceable anyway, but we do not sign unenforceable paper)

### Q3 — Permitted Uses

**Question**: Are permitted uses explicitly limited to the stated business purpose, or is the counterparty free to use the information for "evaluation, internal business purposes, or as otherwise agreed"?

**Branches**:
- **Limited to the stated purpose, with explicit prohibition on any other use** → +1 Sign As-Is
- **Limited to the stated purpose with a short list of reasonable ancillary uses (e.g., audit, regulatory reporting)** → +1 Minor Redlines or Sign As-Is depending on the list
- **Vague ("evaluation and related business purposes") with no specific purpose named** → +1 Substantial Negotiation
- **Unlimited or gives the counterparty broad latitude to use information beyond the purpose** → +1 Refuse

### Q4 — Term and Survival

**Question**: How long does confidentiality last? Is there a distinction between the term of the NDA and the survival of confidentiality obligations on information disclosed during the term?

**Branches**:
- **Reasonable term (2-3 years for routine business info; longer or indefinite for identified trade secrets) with clear survival** → +1 Sign As-Is
- **Longer term (5 years) but market-standard for the counterparty type, with clear survival** → +1 Minor Redlines (standard redline to 3 years)
- **Perpetual or indefinite confidentiality on non-trade-secret information** → +1 Substantial Negotiation
- **Perpetual, no carve-out for trade secrets vs non-trade-secret info, AND we are the discloser** → +1 Refuse (perpetual obligations on vague scope is a drafting red flag; do not sign)

**Discloser vs receiver asymmetry**: If we are the receiver, a shorter term benefits us. If we are the discloser, a longer term on genuine trade secrets may benefit us. The scoring bucket should reflect our role, not a neutral reading.

### Q5 — Return and Destruction

**Question**: Upon termination or request, must the receiving party return or destroy Confidential Information? Is destruction verifiable (certification, deadline, named officer)? Are there carve-outs for backup tapes, legal holds, board materials?

**Branches**:
- **Mandatory return or destruction, with certification, deadline, and reasonable carve-out for backup/legal hold** → +1 Sign As-Is
- **Mandatory but no certification or deadline** → +1 Minor Redlines
- **Discretionary ("may return or destroy at receiving party's option")** → +1 Substantial Negotiation
- **Silent, or explicitly allows retention indefinitely** → +1 Substantial Negotiation (or Refuse if we are the discloser of high-value info)

### Q6 — Exclusions and Carve-Outs

**Question**: Does the NDA exclude from Confidential Information: (a) information already known to the receiving party; (b) information independently developed without use of the disclosure; (c) information that becomes publicly known through no fault of the receiving party; (d) information required to be disclosed by law or regulatory order?

**Branches**:
- **All four exclusions present, with reasonable notice provisions for (d)** → +1 Sign As-Is
- **Three of four present** → +1 Minor Redlines (missing exclusion is a standard redline)
- **Two or fewer present** → +1 Substantial Negotiation
- **Zero exclusions, or exclusions written in a way that makes them unusable (e.g., "unless the receiving party can prove by clear and convincing evidence under sealed affidavit")** → +1 Refuse

### Q7 — Hidden Clauses Masquerading as NDA Terms

**Question**: Does the NDA contain clauses that go beyond confidentiality — specifically: non-solicit of employees, non-solicit of customers, non-compete, assignment of inventions, license grants, indemnity, or binding arbitration with unusual terms? These are a common red flag: counterparties attach substantive business terms to an NDA because NDAs get less scrutiny than commercial agreements.

**Branches**:
- **None of the above** → +1 Sign As-Is
- **Reasonable non-solicit of the specific individuals who received the disclosure, time-limited, narrowly scoped** → +1 Minor Redlines or Substantial Negotiation depending on scope
- **Broad non-solicit (all employees, all customers), assignment of inventions in a vendor NDA, license grant going beyond permitted uses, indemnity inside an NDA** → +1 Substantial Negotiation or Refuse depending on severity
- **Hidden non-compete of any scope, assignment-of-inventions that sweeps background IP, license grant that survives term, or indemnity exceeding actual damages from breach of confidentiality** → +1 Refuse

**Why this question matters most**: Q7 is the highest-signal question in the tree. Counterparties rarely hide things in Q1-Q6, which are expected; they do hide things in Q7, which reviewers often skip because the document is labeled "NDA." A senior practitioner scanning an NDA for the first time should ask Q7 first in practice; the skill asks it last so that the scoring of Q1-Q6 is not biased by discovering a hidden non-compete early.

### Scoring and Verdict

After all 7 questions, the skill tallies the four buckets:

- **Refuse** — If any Q scored +1 Refuse, the default verdict is **Refuse / Walk Away**, UNLESS the Refuse-triggering finding can be cured by a standard library redline (in which case the verdict becomes **Substantial Negotiation** with the curing redline as the required action).
- **Substantial Negotiation** — If Refuse bucket is zero and Substantial Negotiation bucket is 2 or more, verdict is **Substantial Negotiation**.
- **Minor Redlines** — If Refuse and Substantial Negotiation buckets are zero or one, and Minor Redlines bucket is 1-3, verdict is **Minor Redlines**.
- **Sign As-Is** — If all 7 questions scored Sign As-Is, OR if Sign As-Is scored 5+ and no other bucket exceeds 1, verdict is **Sign As-Is**.

**Tie-break rule**: When two buckets tie, escalate to the more cautious bucket (Minor Redlines ties Substantial → Substantial; Substantial ties Refuse → Refuse). The cost of being overly cautious is a longer reviewer conversation; the cost of under-scoring is a missed clause issue at signing.

The verdict is reported in the `## Triage Verdict` section with a 1-2 sentence rationale naming the 2-3 Qs that drove it.

---

## Method

The skill's decision-tree pass follows this sequence. Order matters.

### Step 1 — Read the NDA end-to-end

Do NOT skim. Build an internal map of:

- The sections present (title, recitals, definitions, obligations, term, exclusions, remedies, misc)
- The sections ABSENT (e.g., no exclusions section at all)
- Any Schedules, Exhibits, or cross-referenced documents that are attached vs referenced but missing
- Cross-references inside the document (Section X references Section Y — verify Y exists and says what X claims)

An NDA should fit in a single read pass; if it is more than 10 pages, ask the user whether this is actually an NDA or a full commercial agreement (in which case route to `/contract-review`).

### Step 2 — Walk the Decision Tree

Run Q1 through Q7 in order. For each question, cite the specific clause in the NDA that drove the answer. If the answer requires reading multiple clauses together, say so and cite both.

The skill does NOT skip questions. Even if Q2 is clearly a Sign-As-Is, Q2 still gets scored and cited. The decision tree is the audit trail for the verdict; every question must have a visible answer.

### Step 3 — Score the Branches

For each Q, the chosen branch adds +1 to exactly one of the four buckets (Sign As-Is / Minor Redlines / Substantial Negotiation / Refuse). No branch adds to multiple buckets. No Q is worth more than +1.

### Step 4 — Tally Buckets and Apply Verdict Rules

Apply the verdict rules and tie-break rule from the Decision Tree section above. Land on exactly one verdict.

### Step 5 — Emit Verdict and Drive-Findings

The `## Triage Verdict` section states the verdict and its rationale. The `## Findings` section lists the 3-5 findings that drove the verdict — these are the Qs that scored non-Sign-As-Is, re-framed as clause-level findings with severity, clause reference, and suggested next step.

P2 items that did not move the verdict but were observed during the pass go in `### Also Noted` for traceability.

### Step 6 — Write "Cannot Assess Without"

Written BEFORE finalizing findings. If an item goes here, it cannot also appear as a confident finding in the main list. The section is how the skill makes its scope explicit.

### Step 7 — Reviewer Checklist

Copy the standard checklist and add any NDA-specific sign-off items surfaced by the tree walk (e.g., "IP Counsel consulted on assignment-of-inventions clause in Section 6").

---

## Delegation Patterns Available

### Default: Pattern 1 Consultation

When the decision tree surfaces a question the skill cannot answer alone, `/nda-triage` spawns a consultation per `delegation-protocol.md` Pattern 1:

| Trigger | Spawn |
|---|---|
| Assignment of inventions, background IP, license grant inside an NDA | 📜 IP Counsel |
| PII, employee data, cross-border transfer, data processing | 🔒 Privacy Counsel |
| Non-solicit of employees, non-compete, employment-adjacent terms | 👔 Employment Counsel |
| Counterparty is a regulated entity (bank, healthcare, insurance) | ⚖️ Compliance Officer |
| Multi-jurisdictional enforcement (forum, venue, enforceability) | ⚖️ General Counsel |
| Counterparty is an M&A target or the NDA protects an M&A process | 🏛️ M&A Analyst (secondary: General Counsel) |

Consultations are attributed in the Findings section. Ownership of the triage stays with Contracts Counsel.

### On Request: Pattern 5 Adversarial Review (`--mode adversarial`)

Use for high-value or structurally unusual NDAs. Requires all four Pattern 5 guardrails: named human tiebreaker before the review starts, fresh-context spawn of the adversarial agent, maximum two iterations, and role separation.

Do NOT use Pattern 5 for routine vendor or sales NDAs. The default Create mode with Pattern 1 Consultation is sufficient for the vast majority of NDAs.

---

## Quality Gates

`/nda-triage` is a sensitive skill. It ships only after passing the two-pass publication gate defined in `sensitive-skill-guardrails.md` Section 4:

- **Pass 1 — Scaffolding Check** — 📋 Director of Legal Affairs verifies the structure (disclaimer, NDA metadata, Triage Verdict, Decision Tree, Findings, Reviewer Checklist, Cannot Assess Without, frontmatter, ROI framing, delegation citation, first-principles authoring, clause library attribution). 15 minutes, binary GO / REWORK.

- **Pass 2 — Substantive Check** — ⚖️ General Counsel verifies the decision-tree logic, branch scoring, verdict rules, severity thresholds, delegation-pattern appropriateness, scope boundary correctness, jurisdiction handling, and edge cases. **72-hour SLA** for subsequent-similar Phase 3 legal skills; the template pattern was validated by A5 `/risk-analysis` and A1 `/contract-review` publication earlier in Phase 3.

- **Birth Test — DEFERRED** — Per Yohay's Option E decision on 2026-04-11, A2 ships as v1.0.0 **without a birth test**. See the Attribution and Maintenance section for the full rationale.

On every invocation, the skill self-checks against Section 7 of `sensitive-skill-guardrails.md` BEFORE producing output. If the self-check fails on any non-deferred item, the output does not publish.

---

## ROI Framing

ROI for `/nda-triage` is reported as **"time saved on drafting and triage of an NDA"** — NEVER "time saved on legal review."

Legal rate: $300-400/hr blended per `feedback_roi_rates.md`. Default $350/hr for an NDA triage.

Time-saved baseline: a structured decision-tree triage of a 3-10 page NDA, producing a verdict and 3-5 clause-level findings tied to specific sections, is ~1 hour of manual drafting and triage time for a senior practitioner. Unusual or long-form NDAs (10+ pages, novel structure, multi-jurisdictional) may baseline at 1.5-2 hours.

`/nda-triage` is a high-frequency skill. It is designed to be invoked weekly or more (every inbound NDA from sales, BD, CorpDev, or vendor qualification). The per-invocation ROI is modest; the cumulative ROI across a weekly cadence over a year is material.

Example ROI line for a standard NDA triage:

```
⏱️ ~1 hr saved in 60s, 12k tkns ~$0.7 cost, Value ~$350
```

---

## Attribution and Maintenance

**Owner**: 📄 Contracts Counsel. The skill's decision-tree reasoning, branch scoring, and severity thresholds are Contracts Counsel's accountability. The verdict rules are jointly owned with ⚖️ General Counsel.

**Consumers** (gateways that invoke this skill):
- `ext-legal` — legal team gateway, primary user
- `product` — product gateway when PM, VP Product, or BD receives an inbound NDA and needs a fast triage before engaging counsel
- `ext-corpdev` — corp dev gateway for M&A NDAs, partnership NDAs, and evaluation NDAs
- `sales` — sales gateway for customer-inbound NDAs that land in the sales workflow and need a triage before the deal can progress (unique to A2; A1 does not list sales as a consumer because clause-by-clause enterprise contract review is not a sales-workflow fit)

New consumers require a frontmatter update and a one-line note in the consuming gateway's skill list.

**Authoring**: First-principles. This skill was authored from scratch during Phase 3 Sub-phase 3.1 on 2026-04-11, inheriting the structural pattern from A1 `/contract-review` (the first contract-specific Phase 3 skill) but with entirely original content. The decision tree is the novel contribution unique to A2.

**Clause library dependency**: `/nda-triage` reads primarily from the Confidentiality category of `reference/clause-patterns.md` (bootstrapped by A1's birth test against the AXIA EULA v2). Secondary references: Jurisdiction & Governing Law, Term/Termination, IP, and Data Protection categories. When the library is updated, `/nda-triage` picks up new patterns automatically. The library's version (date) is recorded in the NDA Metadata block of every output for traceability.

### Birth Test — DEFERRED per Option E

**Status at v1.0.0**: No birth test. Shipping anyway.

**Rationale**: The Phase 3 Sub-phase 3.1 plan named a completed SKYMOD vendor NDA as the birth-test target for A2. Yohay searched the workspace for a completed SKYMOD vendor NDA on 2026-04-11 and none exists as a file. Rather than fabricate a synthetic NDA or a fake birth-test output (which would violate first-principles authoring — no fabricated test fixtures), Yohay chose **Option E**: ship A2 without a birth test, explicitly flagged as "awaiting first real triage," and let the first real NDA that arrives through the Etsion Brands pipeline (SKYMOD corporate gifting, Maad House vendor work, ProductBeacon practice engagements, AXIA enterprise sales, or any other channel) become the natural v1.0.0 birth test.

**When the first real NDA arrives**: Run `/nda-triage` on it, capture the verdict and the 3-5 driving findings, validate the decision-tree branches against the actual text, and feed the observed clause patterns back into the Confidentiality category of `clause-patterns.md`. The resulting triage output becomes the v1.0.0 birth test and gets noted in the Changelog as validating (or requiring correction to) the decision tree.

**First real NDA triage will serve as v1.0.0 validation.** Until then, the skill is authored and reviewed but not yet exercised against real paper. Reviewers using A2 in this interim period should be aware of the deferral and weight the verdict accordingly.

**Quality gate deferral is explicit**: `sensitive-skill-guardrails.md` Section 7 item "birth test" is marked DEFERRED at v1.0.0. All other Section 7 items — disclaimer, UPL block, jurisdiction handling, output structure, delegation citation, ROI framing, first-principles authoring, scaffolding review — pass at v1.0.0.

**Updates**: Via the two-pass publication gate. Minor edits (typos, formatting) can bypass Pass 2. Any edit touching the decision tree, verdict rules, severity thresholds, scoring logic, or the output structure requires a full Pass 2 substantive review by General Counsel. When the first real birth test lands, any resulting corrections to the tree are a material edit requiring Pass 2.

**Changelog**: Maintained at the bottom of this file.

---

## Example Invocation

```
User: /nda-triage "inbound NDA from Acme Corp for vendor evaluation"

/nda-triage v1.0.0 — reading:
  - inbox/acme-nda-2026-04-11.pdf (5 pages, one-way, we are the receiver)

Collecting inputs:
  - NDA: Acme Corp Mutual Non-Disclosure Agreement (marked "Mutual" on cover)
  - Parties: Acme Corp + [Our Entity]
  - Direction: Marked "Mutual" on cover; Section 2 definitions only protect Acme's info → STRUCTURAL MISMATCH
  - Our Role: Receiver (vendor evaluation; no disclosure from us planned)
  - Purpose: SOC 2 audit vendor evaluation, no commitment
  - Jurisdiction: Section 9.1 — Delaware; counterparty Delaware-incorporated. Clean.
  - Clause library version: 2026-04-11

Walking decision tree:
  Q1 Direction/Reciprocity: Marked mutual but definitions one-way → Structurally broken → +1 Refuse (curable via redline)
  Q2 Definition of CI: Broad but has all four exclusions → +1 Minor Redlines
  Q3 Permitted Uses: Limited to "evaluation purposes" with no ancillary list → +1 Sign As-Is
  Q4 Term: 3 years; survival clear → +1 Sign As-Is
  Q5 Return/Destruction: Mandatory with 30-day deadline and certification; backup carve-out → +1 Sign As-Is
  Q6 Exclusions: All four present with reasonable notice provision for (d) → +1 Sign As-Is
  Q7 Hidden Clauses: Section 7 contains 18-month non-solicit of "any employee of the disclosing party" → +1 Substantial Negotiation (not Refuse because scope is narrow; would be Refuse if all employees)

Bucket tally: Refuse 1 (curable), Substantial Negotiation 1, Minor Redlines 1, Sign As-Is 4
Curable Refuse → Substantial Negotiation per rules
Verdict: Substantial Negotiation

Producing output at:
  ProductBeacon/Sales/nda-triage-acme-2026-04-11.md

[output follows standard structure: disclaimer → NDA metadata → triage verdict →
 findings → reviewer checklist → cannot assess without]

⏱️ ~1 hr saved in 60s, 12k tkns ~$0.7 cost, Value ~$350
```

---

## Changelog

- **1.0.0 (2026-04-11)** — Initial authoring. First-principles during Phase 3 Sub-phase 3.1. Second contract-specific Phase 3 skill; inherits structural pattern from A1 `/contract-review`. Decision tree is the novel contribution unique to A2. **Birth test DEFERRED per Yohay's Option E decision**: the Phase 3 plan's named SKYMOD vendor NDA target does not exist as a file in the workspace; the skill ships awaiting first real NDA triage through the Etsion Brands pipeline as v1.0.0 validation. Substantive review passed by ⚖️ General Counsel on the 72-hour subsequent-similar SLA (A5 and A1 validated the template pattern earlier in Phase 3); scaffolding review passed by 📋 Director of Legal Affairs. All other `sensitive-skill-guardrails.md` Section 7 items pass at v1.0.0.
