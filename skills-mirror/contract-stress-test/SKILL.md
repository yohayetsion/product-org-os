---
name: contract-stress-test
description: Applies Pattern 5 Adversarial Review to a near-final contract draft with fresh-context role separation, a two-iteration cap, and a named human tiebreaker, as a drafting and triage aid for human
  review, not a legal opinion.
argument-hint: '[contract path or counterparty name] --tiebreaker [name]'
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
# /contract-stress-test

## Purpose

`/contract-stress-test` is the canonical application of Pattern 5 Adversarial Review from `delegation-protocol.md` to a near-final contract draft. It takes a contract that has already been triaged clause-by-clause (typically by `/contract-review`) and stress-tests it with a fresh-context adversarial pass designed to surface risks the prior review missed or under-scored.

The skill's core mechanic is role separation. A fresh-context adversarial agent reads the current draft without access to the drafter's prior-turn rationale and without access to earlier iterations of the review. This prevents the adversarial agent from converging on the drafter's framing and is what makes the pattern "adversarial" rather than "collaborative review."

What it IS: a structured adversarial stress-test with explicit scope boundaries, a two-iteration cap, and a named human tiebreaker who resolves contested findings. Every finding is tagged for severity (P0/P1/P2), verdict (address/accept-with-risk/reject-as-hypothetical), and relationship to prior review (NEW/OVERLAP/CONTRADICT).

What it is NOT: legal advice, a substitute for licensed counsel, a redline authoring tool, a negotiation strategy, or a replacement for `/contract-review`. A7 does not re-do A1's clause-by-clause pass. It sits on top of A1 and deliberately targets what A1 missed.

---

## When to Use

Invoke `/contract-stress-test` ONLY when ALL of the following are true:

- The contract is **near-final**, not still evolving in structural shape
- The cost of a missed clause issue is **material** (enterprise deal with uncapped exposure, M&A doc with asymmetric information, IP licensing where ownership/grant scope is load-bearing, regulatory filing where a missed position creates real exposure, multi-year pricing commitment)
- A **named human tiebreaker** is available BEFORE the review starts (the pattern deadlocks without one)
- The contract has **already been through** `/contract-review` (or equivalent clause-by-clause triage by a human drafter), so the adversarial pass has a draft to stress-test, not an evolving document to shape

Typical triggers:

- AXIA EULA v2 before first enterprise signature
- M&A term sheet before the LOI lock date
- IP licensing agreement where AXIA is licensing a Frontier Model from a third party
- Multi-year SLA with uptime-credit structure facing a Fortune-500 buyer
- Regulatory filing where the legal position is argued in the submission itself
- Any contract where the drafter believes they have converged and wants a structured "break it" pass before handing to General Counsel

## When NOT to Use

Do NOT use `/contract-stress-test` when:

- **Routine contracts with templated risk profile** → use `/contract-review` (A1) in default Create mode with Pattern 1 Consultation to pull in specialists. Adversarial review overhead is not justified for low-stakes triage.
- **Early-stage drafts still evolving in shape** → use `/contract-review` or `/risk-analysis`. Pattern 5 presupposes a near-final draft. Stress-testing an evolving document generates noise because the shape will change.
- **Low-stakes contracts** (standard vendor SOW, routine NDA, simple SaaS subscription in the normal course of business) → use `/contract-review` or `/nda-triage` (A2). The two-iteration adversarial pass is expensive relative to the stakes.
- **No available tiebreaker** → the pattern deadlocks. Pattern 5 requires a named human who can resolve contested findings BEFORE the review starts. Without one, use `/contract-review --mode adversarial` which is lighter weight, or wait until a tiebreaker is available.
- **Time pressure makes two iterations infeasible** → accept single-pass Pattern 3 Review via `/contract-review --mode adversarial`.
- **The drafter wants a redline authored for them** → the adversarial agent produces findings, not draft text. Point at the clause library; engage a specialist for novel language.
- **One "correct" answer exists** → stress-testing is just delay. Pattern 5 is for genuine risk surface work, not for litigating a decided position.

A7 deliberately sits DOWNSTREAM of A1 `/contract-review`. A1 is the clause-by-clause triage; A7 is the adversarial overlay that runs on top. A7 ALWAYS assumes A1 has already run (or implicitly run by the same drafter) and targets what A1 missed or under-scored.

---

## Modes

### Create (default)

Run a Pattern 5 Adversarial Review iteration 1 against a near-final contract. The skill spawns a fresh-context adversarial agent and produces a findings list with the Pattern 5 output format.

```
/contract-stress-test AXIA-Enterprise-License-Agreement-v2.pdf --tiebreaker "Yohay Etsion"
/contract-stress-test "Acme Reseller Agreement" --tiebreaker "@general-counsel"
```

There is NO `--mode adversarial` flag — the whole skill IS adversarial mode by definition. A non-adversarial contract review is just `/contract-review` (A1), which is a different skill with a different structure.

### Update

Re-stress-test after a counterparty round or after the drafter has resolved iteration 1's findings and wants iteration 2. Pass the path to the existing stress-test output. The adversarial agent for iteration 2 MUST be a fresh-context spawn (distinct agent identity if possible), not the same agent that produced iteration 1.

```
/contract-stress-test update AXIA/Product/contract-stress-test-eula-v2-2026-04-11.md
```

Update mode enforces the two-iteration cap. If the existing output is already iteration 2, the skill refuses to produce iteration 3 and directs the user to the named human tiebreaker for final resolution.

---

## Inputs Required

The skill MUST collect the following before producing output. If any are missing, it refuses to run rather than defaulting.

| Input | Required | Example |
|---|---|---|
| Contract document (path or content) | Yes | `AXIA/Marketing/Collaterals/AXIA-EULA-v2.pdf` |
| **Named human tiebreaker** | **Yes — skill refuses output without it** | "Yohay Etsion" / "@general-counsel" / "Asaf Massuri" |
| Counterparty context | Yes | "Top-5 Israeli bank, regulated by Bank of Israel" |
| Iteration number | Yes (defaults to 1) | 1 or 2 — **cap at 2** |
| Stake assessment | Yes | "First enterprise deal with regulated bank counterparty; cost of missed clause is multi-year reputational and contractual exposure" |
| Prior review output | Optional but recommended | `AXIA/Product/contract-review-eula-v2-2026-04-11.md` |
| Jurisdiction | Yes | "Israel + U.S. Delaware (multi-jurisdictional EULA)" |

**Named tiebreaker is NON-NEGOTIABLE.** If no tiebreaker is named, the skill asks the user rather than producing output. This is enforced because Pattern 5's stop criteria include "hand off contested findings to named human" — without a named human, contested findings have nowhere to go and the pattern deadlocks. Default tiebreaker for legal deliverables in this workspace: **Yohay Etsion**.

**Prior review awareness.** If the user provides a prior `/contract-review` output, the skill's adversarial pass MUST NOT re-litigate findings already surfaced in the prior review. Findings that overlap with the prior review are tagged `OVERLAP` and noted briefly; the substantive work targets NEW findings the prior review missed, and CONTRADICT findings where the adversarial agent scores a prior finding differently. If no prior review is provided, the skill still runs, but notes in its metadata that it is running as both A1 and A7 collapsed (which is a weaker application of Pattern 5 and is flagged in the output).

---

## Output Structure

Every `/contract-stress-test` output conforms to `sensitive-skill-guardrails.md` Section 3 AND to Pattern 5's output format from `delegation-protocol.md`. Structure is non-negotiable.

### 1. Disclaimer + UPL Guardrail Block (top)

Verbatim block from `sensitive-skill-guardrails.md` Section 3.1, with `{jurisdiction}` filled in from the contract's governing-law clause.

### 2. Adversarial Review Metadata block

A labeled block under the disclaimer with:

- **Contract**: title and version of the document being stress-tested
- **Counterparty**: the counterparty context
- **Drafter**: whose work is being stress-tested (the human or agent who authored the current draft)
- **Adversarial Agent**: the fresh-context spawn identity producing this iteration's findings (MUST be distinct from the drafter; on birth tests or small-team deployments, the same agent may produce both but MUST explicitly note the fresh-context simulation and note that a stronger Pattern 5 invocation would use distinct agents)
- **Iteration**: N of 2 (cap enforced)
- **Named Human Tiebreaker**: the human who resolves contested findings; set BEFORE the review starts
- **Stake Assessment**: what is the cost of a missed risk? One or two sentences naming the commercial / regulatory / reputational exposure
- **Prior Review**: path to the `/contract-review` output (or any prior clause-level review) the stress test is built on top of, or "none" if the stress test is running without prior review (flagged as weaker Pattern 5)
- **Fresh-context confirmation**: explicit statement that the adversarial agent did not see the drafter's prior-turn rationale or earlier iterations

This metadata block is the Pattern 5 scaffold. It is how the reader knows the review is operating under the guardrails.

### 3. Jurisdiction Assumed (field)

As written in the contract's governing-law clause. If multi-jurisdictional, named explicitly.

### 4. `## Findings`

Numbered list. Each finding follows the Pattern 5 output format (from `delegation-protocol.md`):

- **Clause reference**: specific section, sub-section, or schedule number. If `[ABSENT]`, name where it would normally appear.
- **Severity**: `P0` (blocker), `P1` (important), `P2` (nice-to-have)
- **Verdict**: `address` / `accept-with-risk` / `reject-as-hypothetical`
- **Relationship to prior review**: `NEW` (drafter/prior review missed), `OVERLAP` (drafter/prior review caught — brief note only, do not re-litigate), or `CONTRADICT` (drafter/prior review scored differently; goes to tiebreaker)
- **What the clause says** (or doesn't): grounded quote or precise paraphrase
- **Why it matters**: the downstream risk or implication
- **Citation** (when verdict = `address`): the public framework, regulation, or precedent the finding relies on — named and pointer where possible. MANDATORY for `address` verdicts. If the finding has no public citation, it is `reject-as-hypothetical` per scope boundary.

Findings that violate scope boundary (invented counterparty facts, hallucinated behavior, uncited regulatory position) are marked `reject-as-hypothetical` and are STILL listed in the output, not silently removed. The listing is the scope boundary made visible — the reader sees that the adversarial agent considered and rejected the finding.

Tag distribution target: a well-functioning Pattern 5 iteration 1 surfaces AT LEAST 3 NEW findings relative to prior review. If iteration 1 produces zero NEW findings, Pattern 5 is decorative for this contract and the skill says so explicitly in the Stop Criteria Assessment section (see below).

### 5. `## Reviewer Checklist`

Explicit sign-off items, with the Pattern 5 guardrails made visible:

- [ ] Adversarial agent confirmed fresh-context (no drafter rationale exposure)
- [ ] Iteration count correct (1 or 2, not 3+)
- [ ] Named human tiebreaker confirmed before review started
- [ ] Stake assessment matches deal reality
- [ ] All P0 findings addressed, or `accept-with-risk` decision logged by tiebreaker
- [ ] All P1 findings triaged (address, accept-with-risk, or reject)
- [ ] All CONTRADICT findings resolved by tiebreaker
- [ ] Scope boundary respected (no invented facts; no hallucinated counterparty behavior)
- [ ] Counsel engaged for items in "Cannot Assess Without"

### 6. `## Cannot Assess Without Licensed Counsel`

Explicit list of what the adversarial pass deliberately did NOT opine on. Minimum 5 items for an enterprise contract. Format: "Enforceability of {clause} in {jurisdiction}" / "Regulatory exposure under {statute}" / etc.

### 7. `## Tiebreaker Required`

A dedicated section listing contested findings for the named human tiebreaker. Two categories:

- **CONTRADICT findings**: where the adversarial agent scores a prior-review finding differently (e.g., A1 scored a finding P1, A7 argues P0, or vice versa)
- **Drafter wants accept-with-risk on a P0**: any P0 finding the drafter wants to leave unresolved requires explicit tiebreaker sign-off under Pattern 5

If no contested findings, the section says verbatim: **"No contested findings — no tiebreaker action required."**

This section is how Pattern 5's named-tiebreaker requirement becomes operational rather than decorative.

### 8. `## Stop Criteria Assessment`

Short section at the bottom applying Pattern 5's stop criteria:

- Did this iteration surface NEW P0 or P1 findings relative to prior review / prior iteration? (Yes / No)
- Are we at iteration 2? (Yes / No)
- **Disposition**: `STOP — no new material risks` / `STOP — iteration 2 cap reached` / `QUEUE ITERATION 2 — new findings surfaced, tiebreaker not yet engaged`

If the disposition is QUEUE ITERATION 2, the skill names which agent should produce iteration 2 (MUST be a distinct fresh-context spawn, not the iteration-1 agent).

If the disposition is STOP because iteration 1 produced zero NEW findings, the skill says so explicitly and flags that Pattern 5 was decorative for this contract. This is the honesty mechanism. Without it, Pattern 5 becomes a ritual.

---

## Method

The skill's adversarial pass follows this seven-step sequence. Order matters — each step depends on the prior step.

### Step 1 — Iteration Check

Confirm this is iteration 1 or 2. If the user requests iteration 3, refuse and direct them to the tiebreaker. The two-iteration cap is a Pattern 5 non-negotiable.

If iteration 2, confirm the iteration-1 output is available for comparison AND confirm that a distinct fresh-context agent is producing iteration 2 (not the iteration-1 agent).

### Step 2 — Spawn Adversarial Agent in Fresh Context

The adversarial agent is spawned in a fresh context with:
- Access to: the contract document, the clause library (`reference/clause-patterns.md`), the prior review output if provided, and the stake assessment
- NO access to: the drafter's prior-turn rationale, earlier iterations of this adversarial review, other drafter-side commentary that would anchor the adversarial agent to the drafter's framing

On small-team deployments where a literal fresh-context spawn is not feasible (e.g., a single Contracts Counsel instance performing both drafting and stress-testing), the skill simulates fresh context by explicitly disclaiming prior knowledge and approaching the contract as if reading it for the first time. This is weaker than a true fresh-context spawn and is flagged in the metadata.

### Step 3 — Read the Contract End-to-End in Fresh Context

No skim. The adversarial agent reads the full document, including schedules, exhibits, and DPAs. Build a mental map of:
- What clauses are present and what their interaction is
- What clauses are absent (missing-clause candidates)
- What assumptions the draft makes about the counterparty (contract may assume the counterparty is in a specific regulatory posture, a specific jurisdiction, a specific commercial band)
- What structural choices the drafter made that could have been different (subscription vs. perpetual, uncapped vs. capped, mutual vs. one-way)

### Step 4 — Stress-Test Against Clause Library + Pattern 5 Scope Boundary

For each clause category, run the adversarial questions:
- Does this clause match a known market pattern? If it deviates, in whose favor and by how much?
- What does the market-normal counterparty redline of this clause look like? Did the drafter anticipate it?
- What edge cases does this clause fail on (breach scenarios, regulator intervention, dispute escalation, termination for cause)?
- What cross-clause interactions does this clause create with other parts of the draft?
- What is the draft NOT saying that a sophisticated counterparty would insist on?
- What clauses are the drafter's "accept-with-risk" assumptions baked into the structure?

For each candidate finding, apply the Pattern 5 scope boundary:
- **May**: stress-test clauses, assumptions, structural choices, risk framing; surface edge cases; question prior-review severity; point at public frameworks/regulations/precedents
- **May NOT**: invent counterparty facts, hallucinate counterparty behavior, fabricate regulatory positions, generate novel draft text

Any candidate finding that relies on invented facts or hallucinated behavior is marked `reject-as-hypothetical` and retained in the output (not silently dropped) so the scope boundary is visible.

### Step 5 — Score Severity + Verdict

- **P0** — blocker. Must be addressed or explicitly accept-with-risk by the tiebreaker before publication. Examples: missing IP indemnity the contract itself gestures at; uncapped regulatory-fine indemnity; disclaimer that is facially unenforceable in the governing jurisdiction.
- **P1** — important. Should be addressed; drafter may accept-with-risk with documented reasoning.
- **P2** — nice-to-have. Track but does not block.

- **address** — drafter revises the draft to resolve the finding
- **accept-with-risk** — drafter leaves the draft as-is and documents the accepted risk (for P0, requires tiebreaker sign-off)
- **reject-as-hypothetical** — finding violates scope boundary

When in doubt, escalate one level (P2 → P1, P1 → P0). The cost of over-severity is a longer tiebreaker conversation; the cost of under-severity is a missed issue at the counterparty's negotiation table.

### Step 6 — Compare Against Prior Review

For each finding, tag the relationship to prior review:

- **NEW**: the prior review did not surface this finding. The substantive value of A7 lives in NEW findings.
- **OVERLAP**: the prior review already surfaced this finding. A7 notes it briefly (one line) and does NOT re-litigate. The NEW findings are where the adversarial pattern earns its overhead.
- **CONTRADICT**: the prior review surfaced this finding but scored it differently, or the adversarial agent disagrees with the prior review's verdict. CONTRADICT findings go to the tiebreaker.

If prior review is "none," tag every finding as NEW and note in metadata that the skill is running as a collapsed A1+A7 pass (weaker Pattern 5).

### Step 7 — Apply Stop Criteria

Two stop criteria from `delegation-protocol.md`:

1. **No new material risks** — iteration surfaces no NEW P0 or P1 findings relative to prior iteration (or, for iteration 1, relative to prior review). Repeat-only OVERLAP findings do not extend the loop.
2. **Two iterations hit** — cap at 2 even if new findings keep surfacing. Diminishing returns plus adversarial-agent incentive to find SOMETHING new eventually generates noise.

If criterion 1 is met on iteration 1, stop. If criterion 2 is met, stop and hand off to tiebreaker.

**Honesty mechanism**: if iteration 1 produces ZERO NEW findings, the Stop Criteria Assessment section says so explicitly. Pattern 5 was decorative for this contract. This is important — without the honesty mechanism, Pattern 5 becomes a ritual that always surfaces at least one finding for performance reasons. The pattern must be willing to report "nothing NEW found" to be credible.

---

## Delegation Patterns Available

`/contract-stress-test` IS Pattern 5. It does not invoke other patterns as the primary motion.

However, WITHIN the adversarial pass, the adversarial agent may spawn Pattern 1 Consultations for specialist questions that require domain expertise outside contracts counsel. Examples:

- Adversarial agent spawns 🔒 Privacy Counsel consultation on a DPA cross-border transfer clause
- Adversarial agent spawns 📜 IP Counsel consultation on a licensing grant scope
- Adversarial agent spawns ⚖️ Compliance Officer consultation on a regulated-industry clause
- Adversarial agent spawns 💰 Tax Planning Specialist consultation on a payment-structure clause

Consultations are attributed in the finding: "I consulted 🔒 Privacy Counsel, who confirmed that the DPA's cross-border transfer carve-out is stronger than GDPR requires but weaker than Bank of Israel Directive 361 expects for outsourced data processors."

Pattern 1 Consultations inside an adversarial pass do NOT break the fresh-context rule because the consultation is scoped to a specific domain question, not a reading of the drafter's prior rationale.

`/contract-stress-test` does NOT invoke Pattern 2 Delegation (the stress-test is atomic — it cannot be handed off and still preserve fresh-context role separation), Pattern 3 Review (which is lighter weight than Pattern 5), or Pattern 4 Structured Debate (which is for genuine tradeoffs, not stress-testing).

---

## Relationship to `/contract-review` (A1)

A7 is NOT A1's replacement. The two skills have different jobs:

| Skill | Primary Motion | Typical Use |
|---|---|---|
| A1 `/contract-review` | Pattern 1 Consultation — clause-by-clause triage | Default for any contract (routine or high-stakes); bootstraps the clause library |
| A7 `/contract-stress-test` | Pattern 5 Adversarial Review — fresh-context stress-test | Near-final high-stakes contracts; runs on TOP of A1's output |

The typical flow for a high-stakes contract:

1. Drafter runs `/contract-review` to produce a clause-by-clause triage with 10-20 findings
2. Drafter resolves the findings through redline, specialist consultation, or accept-with-risk
3. Contract converges to a near-final draft
4. Drafter runs `/contract-stress-test` to stress-test the near-final draft with fresh-context adversarial pressure
5. A7 surfaces NEW findings A1 missed, or CONTRADICT findings where A1 under-scored
6. Named human tiebreaker resolves contested findings
7. Contract goes to General Counsel for final substantive review and signature

For routine contracts, step 4 is skipped entirely — the A1 output is sufficient.

A7's value is concentrated in the NEW findings. If A7 consistently produces zero NEW findings on a particular type of contract, the team should stop running A7 on that type — the overhead is not earning its keep. Conversely, if A7 consistently produces NEW P0 findings, the A1 clause library needs updating to catch those findings earlier.

---

## Quality Gates

`/contract-stress-test` is a sensitive skill. It ships only after passing the two-pass publication gate defined in `sensitive-skill-guardrails.md` Section 4:

- **Pass 1 — Scaffolding Check** — 📋 Director of Legal Affairs verifies the structure (disclaimer, adversarial review metadata block, Findings with Pattern 5 format, Reviewer Checklist with Pattern 5 guardrails, Cannot Assess Without, Tiebreaker Required section, Stop Criteria Assessment, frontmatter, ROI framing, delegation citation, first-principles authoring). 15 minutes, binary GO / REWORK.
- **Pass 2 — Substantive Check** — ⚖️ General Counsel verifies the Pattern 5 guardrails are correctly operationalized, severity thresholds are defensible, fresh-context simulation is credibly described, stop criteria are applied correctly, the birth test demonstrates the pattern working on a real contract, and the honesty mechanism is visibly applied. **72-hour subsequent-similar SLA** for Phase 3 legal skills; the template pattern was validated by A5 `/risk-analysis` → A1 `/contract-review` → A2 `/nda-triage` → A3 `/privacy-policy-audit` → A4 `/compliance-audit` earlier in Phase 3, so A7 inherits the subsequent-similar timeline.

On every invocation, the skill self-checks against Section 7 of `sensitive-skill-guardrails.md` BEFORE producing output. If the self-check fails on any item, the output does not publish.

---

## ROI Framing

ROI for `/contract-stress-test` is reported as **"time saved on adversarial stress-testing of a near-final contract"** — NEVER "time saved on legal review."

Legal rate: **$400/hr** blended per `feedback_roi_rates.md`, higher than A1's $350/hr because adversarial review is a more specialized motion requiring fresh-context discipline and a structured honesty mechanism. Senior practitioners who can maintain fresh-context role separation alone (without tooling) are rare.

Time-saved baseline: a structured fresh-context adversarial pass on a 20-30 page enterprise contract with 2-4 schedules, producing 6-10 findings tagged for NEW/OVERLAP/CONTRADICT with Pattern 5 output format, is **~6-8 hours** of manual drafting and adversarial reasoning time for a senior practitioner. The fresh-context discipline is hard to maintain alone — the practitioner naturally drifts back to the drafter's framing. Simpler contracts (NDAs, short vendor SOWs) do not warrant Pattern 5 at all. Multi-schedule enterprise contracts with novel structure may require 10+ hours baseline.

The ROI tracks ONLY the time the skill saves on the adversarial pass, not the substantive legal review time. The substantive review by General Counsel (tiebreaker sign-off on contested findings, final pre-signature review) still happens in full.

Example ROI line for a standard enterprise contract stress-test:

```
⏱️ ~7 hrs saved in 120s, 35k tkns ~$2.2 cost, Value ~$2,800
```

---

## Attribution and Maintenance

**Owner**: 📄 Contracts Counsel. The skill's adversarial reasoning and Pattern 5 operationalization are Contracts Counsel's accountability. The clause library dependency is jointly owned with ⚖️ General Counsel. The Pattern 5 guardrails themselves are owned by `delegation-protocol.md` and are reference-only here.

**Consumers** (gateways that invoke this skill):
- `ext-legal` — legal team gateway, primary user
- `product` — product gateway when a PM/VP Product needs near-final contract stress-tested before handing to counsel
- `ext-corpdev` — corp dev gateway for M&A term sheets, LOIs, and IP licensing agreements

**Authoring**: First-principles. A7 was authored during Phase 3 Sub-phase 3.0 as the last of seven Phase 3 legal skills. It inherits the structural pattern from A1 `/contract-review` (sibling skill, same owner) but the method section, metadata block, findings format, tiebreaker section, and stop criteria assessment are original to A7 and reflect the Pattern 5 guardrails from `delegation-protocol.md`.

**Relationship to Phase 3 A6**: A6 is the delegation-protocol.md Pattern 5 Adversarial Review definition itself. A7 is the first full skill that directly invokes Pattern 5 as its core method. The relationship is: A6 defines the pattern; A7 applies it to contracts. If Pattern 5 evolves (e.g., the two-iteration cap changes, the fresh-context requirement is relaxed, the scope boundary is tightened), A7 updates to match.

**Pattern 5 birth test**: A7 was birth-tested against the AXIA EULA v1→v2 diff document, with A1's prior review of the EULA v2 as the prior-review reference. Birth test output: `AXIA/Product/contract-stress-test-eula-v1-v2-diff-2026-04-11.md`. The birth test demonstrated that Pattern 5 can surface NEW findings A1 did not catch on the same contract. If the birth test had produced zero NEW findings, the honesty mechanism would have reported it and the team would have reconsidered whether Pattern 5 earns its overhead on this class of contract.

**Updates**: Via the two-pass publication gate. Minor edits (typos, formatting) can bypass Pass 2. Any edit touching Pattern 5 operationalization (fresh-context rules, iteration cap, stop criteria, tiebreaker section, scope boundary) requires a full Pass 2 substantive review by General Counsel AND a cross-check against `delegation-protocol.md` to ensure the skill and the pattern definition stay aligned.

**Changelog**: Maintained at the bottom of this file. Version 1.0.0 — initial authoring 2026-04-11, closes Phase 3.

---

## Example Invocation

```
User: /contract-stress-test AXIA-EULA-v1-vs-v2-Comparison.docx --tiebreaker "Yohay Etsion"

/contract-stress-test v1.0.0 — reading:
  - AXIA/Marketing/Collaterals/AXIA-EULA-v1-vs-v2-Comparison.docx (12-row comparison table)
  - AXIA/Marketing/Collaterals/AXIA-Enterprise-License-Agreement-v2.pdf (near-final draft)
  - AXIA/Product/contract-review-eula-v2-2026-04-11.md (prior review, 14 findings)

Collecting inputs:
  - Contract: AXIA EULA v1→v2 diff (stress-testing the v2 as near-final draft)
  - Counterparty: First enterprise deal — Bank Discount (regulated Israeli bank)
  - Drafter: Asaf Massuri / AXIA Legal
  - Adversarial agent: 📄 Contracts Counsel (fresh-context spawn, simulated)
  - Iteration: 1 of 2
  - Tiebreaker: Yohay Etsion (confirmed before review started)
  - Stake: First enterprise deal with regulated bank; cost of missed clause is
    multi-year reputational and contractual exposure
  - Prior review: AXIA/Product/contract-review-eula-v2-2026-04-11.md (14 findings)
  - Jurisdiction: Israel + U.S. Delaware

Iteration check: 1 of 2 ✓
Fresh-context spawn: confirmed (simulated — single-agent deployment)
Clause library loaded: reference/clause-patterns.md @ 2026-04-11

Producing output at:
  AXIA/Product/contract-stress-test-eula-v1-v2-diff-2026-04-11.md

[output follows standard structure: disclaimer → adversarial review metadata →
 findings with Pattern 5 format → reviewer checklist → cannot assess without →
 tiebreaker required → stop criteria assessment]

⏱️ ~7 hrs saved in 120s, 35k tkns ~$2.2 cost, Value ~$2,800
```

---

## Changelog

- **1.0.0 (2026-04-11)** — Initial authoring. First-principles during Phase 3 Sub-phase 3.0. First skill to directly invoke Pattern 5 Adversarial Review from `delegation-protocol.md` as its core method. Birth-tested against AXIA EULA v1→v2 diff with A1's prior review as the prior-review reference. Closes Phase 3. Substantive review on the 72-hour subsequent-similar SLA inherited from A5/A1/A2/A3/A4.
