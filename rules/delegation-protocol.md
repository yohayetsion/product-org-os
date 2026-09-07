---
globs:
  - "**/*"
---

# Agent Delegation Protocol

Structured patterns for agent-to-agent collaboration. Each pattern has triggers, ownership rules, and attribution.

---

## Pattern 1: CONSULTATION (Default)

**Trigger**: Need a domain perspective you don't own
**Ownership**: Stays with requesting agent
**Attribution**: "I consulted {emoji} {Name} who noted..."

Spawn sub-agent with specific questions → integrate response into your deliverable → attribute contribution.

**When to use**: Data point or perspective needed, not a full deliverable. Quick turnaround.

---

## Pattern 2: DELEGATION

**Trigger**: Task requires specialist to own a complete deliverable
**Ownership**: Transfers to specialist for sub-task
**Attribution**: Specialist output presented directly, credited to them

**Prompt format**:
```
[DELEGATION] to @{agent} for {deliverable}
Scope: {what to cover}
Deliverable: {what to produce}
Constraints: {boundaries, focus areas}
Context: {relevant background}
```

**When to use**: Deep specialist expertise needed, deliverable stands alone, want to parallelize work.

---

## Pattern 3: REVIEW

**Trigger**: Deliverable needs quality validation before publishing
**Ownership**: Original agent owns final output; reviewer provides feedback
**Attribution**: "Reviewed by {emoji} {Name}. Key feedback: [summary]"

**Prompt format**:
```
[REVIEW] by @{agent}
Deliverable: {path or content}
Review criteria: {criterion 1}, {criterion 2}, {criterion 3}
```

**Response format**: Prioritized findings (P0 Blocker / P1 Important / P2 Nice-to-have) + GO / GO WITH CHANGES / NEEDS REWORK.

| Deliverable | Reviewer |
|------------|----------|
| PRD, feature spec | `director-product-management`, `design-dir` |
| Strategic bet | `vp-product`, `bizops` |
| GTM plan | `director-product-marketing`, `product-operations` |
| Roadmap | `vp-product`, `director-product-management` |
| Pricing | `bizops`, `vp-product` |

---

## Pattern 4: STRUCTURED DEBATE

**Trigger**: Genuine tradeoff where both sides have merit
**Ownership**: Senior agent/gateway owns synthesis
**Attribution**: Each agent speaks directly; synthesis by most senior

**Prompt format**:
```
[DEBATE] @{agent1} argues FOR {position A}
[DEBATE] @{agent2} argues FOR {position B}
Context: {the tradeoff}
Decision owner: @{senior agent}
```

Each agent presents: The Case, Evidence, Risks, Success Criteria, Conditions. Senior synthesizes.

**When NOT to use**: One option is clearly better, outcome predetermined, time pressure, information asymmetry.

---

---

## Pattern 5: ADVERSARIAL REVIEW

**Trigger**: A deliverable needs structured stress-testing before publication because the cost of a missed risk is high and the deliverable is inherently adversarial in context. Typical triggers: enterprise contracts, M&A documents, pricing commitments, IP licensing agreements, regulatory filings, security-critical architecture decisions.

**Ownership**: The drafter retains authorship of the underlying deliverable. The adversarial agent does NOT co-author — it produces structured findings against the draft. A named human tiebreaker resolves contested findings where drafter and adversarial agent disagree on severity or acceptance.

**Attribution**: "Adversarially reviewed by {emoji} {Name}. {N} findings surfaced: {P0 count} blockers, {P1 count} important, {P2 count} nice-to-have. Tiebreaker: {human name/role}."

### Role Separation (CRITICAL)

The drafter and the adversarial agent operate with strict role separation:

- The adversarial agent is spawned in a fresh context, does NOT see the drafter's prior-turn rationale, and does NOT see earlier iterations of the adversarial review.
- Each iteration of adversarial review is a fresh look at the current draft. This prevents the adversarial agent from converging on the drafter's framing.
- The drafter sees adversarial findings AFTER they are produced, not during generation.

This separation is what makes the pattern "adversarial" rather than "collaborative review."

### Stop Criteria

Adversarial review stops when EITHER of the following is true:

1. **No new material risks** — the current iteration surfaces no P0 or P1 findings that were not already surfaced in the previous iteration. Repeat-only findings do not extend the loop.
2. **Two iterations hit** — even if new findings keep surfacing, the pattern caps at two iterations. Diminishing returns + the adversarial agent's incentive to find SOMETHING new eventually generates noise. Two iterations is the ceiling.

If criterion 1 is met on iteration 1, the pattern stops at one pass. If criterion 2 hits, the pattern stops with whatever findings are on the table and hands off to the human tiebreaker.

### Scope Boundary (NON-NEGOTIABLE)

The adversarial agent MAY:
- Stress-test clauses, assumptions, structural choices, and risk framing in the draft
- Surface edge cases the drafter did not consider
- Question the severity of risks the drafter flagged as low
- Point to named public frameworks, regulations, or precedents that the draft does not address

The adversarial agent MAY NOT:
- Invent facts about the counterparty ("the buyer will probably argue X" without evidence)
- Hallucinate behavior ("this clause is typically interpreted as Y" without citation)
- Fabricate regulatory positions that cannot be cited to a real framework
- Generate new draft text for the drafter to adopt — its job is findings, not rewrites

Any finding that violates scope is marked "reject-as-hypothetical" and removed from the final output.

### Named Human Tiebreaker

Every adversarial review invocation must name a human tiebreaker BEFORE the review starts. The tiebreaker resolves contested findings — cases where the drafter and adversarial agent disagree on severity or the drafter wants to accept-with-risk a P0 finding.

Default tiebreakers by deliverable type:

| Deliverable | Tiebreaker |
|---|---|
| Legal deliverable (contract, filing, legal memo) | `general-counsel` |
| M&A deliverable (term sheet, LOI, due diligence memo) | `head-corpdev` + `general-counsel` |
| Pricing commitment / enterprise quote | `vp-product` + `cfo` |
| IP licensing | `ip-counsel` |
| Regulatory filing | `compliance-officer` + `general-counsel` |
| Security-critical architecture | `chief-architect` + `security-architect` |

### Prompt Format

```
[ADVERSARIAL REVIEW] @{adversarial-agent} stress-tests {deliverable}
Deliverable: {path or content}
Iteration: {1 or 2}
Fresh context: YES (no prior-turn rationale)
Scope: stress-test clauses, assumptions, structure
Scope boundary: MAY NOT invent counterparty facts or hallucinate behavior
Stop criteria: no new material risks OR 2 iterations
Tiebreaker: @{human-tiebreaker-role}
Expected output: numbered findings with severity (P0/P1/P2) and verdict
```

### Output Format

The adversarial agent produces a numbered findings list. Each finding:

```
### Finding {N}
**What**: {specific issue with the draft}
**Why it matters**: {the risk or implication}
**Severity**: P0 / P1 / P2
**Verdict**: address / accept-with-risk / reject-as-hypothetical
**Citation** (if verdict = address): {public framework, regulation, or precedent name + pointer URL}
```

- **P0 Blocker** — must be addressed or explicitly accepted-with-risk by the tiebreaker before publication
- **P1 Important** — should be addressed; drafter may accept-with-risk with documented reasoning
- **P2 Nice-to-have** — drafter's discretion

- **address** — drafter revises the draft to resolve the finding
- **accept-with-risk** — drafter leaves the draft as-is and documents the accepted risk in the deliverable itself
- **reject-as-hypothetical** — finding violates scope boundary (invented facts, hallucinated behavior, uncited position) and is removed

### When to Use

- Enterprise contracts with uncapped exposure or novel structure
- M&A documents with asymmetric information
- Pricing commitments that lock in for multi-year terms
- Regulatory filings where a missed position creates real exposure
- IP licensing where ownership/grant scope is load-bearing
- Architecture decisions that are hard to reverse

### When NOT to Use

- Routine contracts with templated risk profile (use Pattern 3 Review instead)
- Early-stage drafts still evolving in shape (use Pattern 1 Consultation — adversarial review presupposes a near-final draft)
- Deliverables where one "correct" answer exists and stress-testing is just delay
- When the drafter's time pressure makes two iterations infeasible (accept single-pass Pattern 3 Review)
- When you lack a named human tiebreaker — without a tiebreaker the pattern deadlocks

> *Relocated 2026-08-15 (DR-2026-262): Pattern 5 relationship to Patterns 3/4 (rationale; the Pattern Selection table below is the binding chooser) — full text in the companion delegation-protocol.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

---

## Pattern Selection

| Situation | Pattern |
|-----------|---------|
| Need a data point | **Consultation** |
| Specialist owns sub-deliverable | **Delegation** |
| Quality check before publishing | **Review** |
| Genuine tradeoff needs analysis | **Debate** |
| Genuine adversarial stress-test needed (high-stakes, near-final draft) | **Adversarial Review** |
| Not sure | **Consultation** (start simple) |

All patterns use standard Task tool spawning from `agent-spawn-protocol.md` Section 2.

---

## Vision to Value Operating Principle

> "Good delegation amplifies team intelligence. The right pattern at the right time turns individual expertise into collective wisdom."
