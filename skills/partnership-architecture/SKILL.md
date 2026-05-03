---
name: partnership-architecture
description: 'Create a Partnership Architecture — the operating artifact for partnership strategy formulation. Defines strategic intent, partnership type, the make/buy/partner decision, partner-fit criteria, co-investment shape, and re-decision trigger. Sits at the same altitude as PRD (product strategy formulation) and /positioning-statement (GTM strategy formulation). Activate when: "partnership architecture", "partnership strategy", "make or buy or partner", "should we partner", "partner-fit", "ecosystem strategy", "co-investment", strategic-relationship formulation, deciding which partnerships to build at all. Do NOT activate for: closing deals with end customers (Sales — /sales-enablement, /account-exec), GTM strategy execution (/gtm-strategy), competitive analysis (/competitive-analysis), individual partnership contract review (/contract-review), inbound NDA triage (/nda-triage), individual deal records (/decision-record).'
argument-hint: '[partnership name or strategic question] or [update path/to/partnership-architecture.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: business-development
  skill_type: task-capability
  owner: bizdev
  primary_consumers:
  - bizdev
  - vp-product
  - cpo
  secondary_consumers:
  - head-corpdev
  - strategic-partnerships
  - bizops
  - pmm-dir
  - chief-architect
  - ma-analyst
  - ceo
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "modify" in input | UPDATE | 100% |
| File path provided (`@path/to/partnership-architecture.md`) | UPDATE | 100% |
| Architecture ID mentioned (`PA-2026-001`) | UPDATE | 100% |
| "create", "new", "formulate" in input | CREATE | 100% |
| "find", "search", "list partnership architectures" | FIND | 100% |
| "the partnership", "our partnership with X" | UPDATE | 85% |
| Just a partner name or strategic question | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate a complete new Partnership Architecture using the template below.

**UPDATE**:
1. Read the existing architecture (search if path not provided)
2. Preserve unchanged sections exactly
3. Update strategic intent, partnership type, make/buy/partner decision, partner-fit, co-investment, or re-decision trigger
4. Mark whether the re-decision trigger fired (and if so, which signal)
5. Increment version
6. Show diff summary: "Updated: [sections]. Version: X → Y."

**FIND**:
1. Search the locations below
2. Present results: partner / strategic question, version, status, owner
3. Ask: "Update one of these, or create new?"

### Search Locations

- `partnerships/`
- `bizdev/`
- `strategy/partnerships/`
- `context/decisions/` (filter by `partnership-architecture` tag)

---

## Vision to Value Phase

**Phase 2: Strategic Decisions** — Partnership Architecture is one of the three strategic formulation surfaces. It sits at the same altitude as the Product Requirements Document (product strategy formulation) and `/positioning-statement` (GTM strategy formulation).

**Prerequisites**: Strategic intent exists (Phase 1), and the capability or distribution gap the partnership would close is named.

**Outputs used by**: `/business-case` (financial framing of the partnership), `/decision-record` (commit the architecture as a reviewable decision), `/strategic-bet` (when the partnership is itself the bet), `/contract-review` (downstream — clause-level work happens after the architecture is set).

---

## Why This Artifact Exists

A partnership without an architecture is just a conversation. The artifact forces six commitments before deal terms are negotiated:

1. **Strategic intent** — what does this partnership unlock that we cannot unlock alone?
2. **Partnership type** — chosen from a defined taxonomy, not invented per deal
3. **Make/buy/partner decision** — explicit reasoning that this is the right shape vs. building or buying
4. **Partner-fit criteria** — the few attributes a partner must have for the strategy to work
5. **Co-investment shape** — what each side commits in plain language
6. **Re-decision trigger** — when this architecture gets reopened, and what signal would invalidate it

If any of the six is missing, the architecture is not yet ready to drive deal-making.

### BizDev is Not Sales (Reminder)

This skill is BizDev-owned. It produces a strategic-formulation artifact, not a deal close. Sales executes commercial relationships with end customers; BizDev formulates which strategic relationships should exist at all. If the input is "we have an inbound RFP from a customer," the right skill is `/sales-enablement` or `/proposal-writer`, not `/partnership-architecture`.

---

## Partnership Type Taxonomy

Partnership type is not a free-text field. It is chosen from the taxonomy below, and the choice drives the rest of the architecture.

| Type | What It Is | Typical Co-Investment | Usual Owner |
|---|---|---|---|
| **Technology partnership** | We integrate with their product (or vice versa) to extend capability | Engineering on both sides; joint roadmap commitment; usually no revenue share | BizDev with @chief-architect |
| **Distribution partnership** | They take our product to their customers (resale, agency, embedded) | GTM enablement, margin share, exclusivity terms | BizDev with @pmm-dir |
| **Co-sell** | Joint sales motion with non-competing vendor; aligned account plans | Sales-team time, joint marketing, account mapping; no revenue share | BizDev with @sales-dir |
| **OEM** | They embed our product in theirs (white-label or branded) | Engineering for embedment; exclusivity and term length matter; revenue share or per-unit fee | BizDev with @ip-counsel |
| **Joint venture** | New legal entity, both sides contribute capital and operating commitments | Capital, governance seats, IP grants, multi-year operating commitment | BizDev with @head-corpdev and @general-counsel |
| **Channel partnership** | Recurring third-party seller, MSP, or systems integrator program | Partner program design, certification, margin tiers | BizDev with @sales-dir |
| **Platform / ecosystem partnership** | We become a complement on their platform (or they on ours) | Engineering investment; marketplace economics; revenue share to platform | BizDev with @chief-architect and @cmo |
| **Strategic supply / capacity** | We secure capability or supply we don't have internally | Capital, multi-year commitment, exclusivity, audit rights | BizDev with @procurement-specialist |

If the type doesn't fit one of these eight, force a decision: either pick the closest type and document the variance, or escalate to @vp-product to confirm whether the taxonomy needs extending. Don't invent a type per deal.

---

## Make / Buy / Partner Decision Framework

This is the heart of partnership strategy formulation. For any capability or distribution gap, three options exist — building it, acquiring it, or partnering for it. The framework below decides which.

### Step 1 — Name the Capability or Distribution Gap

State plainly what the company cannot do today that the strategy requires. Example shapes:

- "We need to operate in [region] but lack a sales team there."
- "We need [technical capability] but our team has no expertise in it."
- "We need our product embedded in [adjacent product category] for our customers to adopt us."
- "We need to certify against [compliance regime] and we have no internal program."

### Step 2 — Score Each Option Against Five Dimensions

| Dimension | Make (Build) | Buy (Acquire) | Partner |
|---|---|---|---|
| **Strategic control** | Highest (we own it) | High (we acquire it) | Lowest (counterparty has agency) |
| **Time to capability** | Slowest (build curve) | Fastest (immediate) | Fast (deal close + ramp) |
| **Capital required** | Medium (compounding payroll) | Highest (one-time + integration) | Lowest (operating commitment, not capital) |
| **Reversibility** | Highest (we can stop building) | Lowest (acquisition is hard to undo) | High (partnerships end) |
| **Strategic-fit risk** | Lowest (we shape it) | Medium (cultural/integration risk) | Medium (counterparty incentive drift) |

### Step 3 — Apply Decision Heuristics

The framework gives a clear answer when the capability sits cleanly in one bucket:

- **Build when** the capability is core to long-term differentiation, the time-to-capability curve fits the strategic window, and we have the talent to execute. Don't partner for what defines you.
- **Buy when** the capability is core but the build curve is too slow, a clean acquisition target exists, the price is defensible, and integration risk is manageable. Buying compresses time but consumes capital and bandwidth.
- **Partner when** the capability is enabling but not core differentiation, the partner has a structural advantage we can't replicate quickly, and the architecture has a credible re-decision trigger that lets us exit if the partner's incentives drift.

The framework returns "ambiguous" when the capability is core but the build curve is too long AND no acquisition target is clean AND the strategic window is short. In that case, name the ambiguity in the artifact and escalate the call — don't paper over with a partnership.

### Step 4 — Document the Counterfactual

The Partnership Architecture must answer: **"If we did not partner here, what would we do instead, and why is partnering better?"** A partnership architecture without a documented counterfactual is a deal log, not a strategic formulation.

---

## Partner-Fit Criteria

The few attributes a partner must have for the strategy to work. Three to seven items, no more — fewer attributes that are genuinely load-bearing beat a long checklist of nice-to-haves.

Each criterion is stated as: **attribute → why it matters → how we'd verify it.**

Example shape (technology partnership):

| Attribute | Why It Matters | How Verified |
|---|---|---|
| Integration depth (open API, not just webhooks) | Architecture relies on bi-directional state sync | Engineering review of partner API |
| Roadmap alignment for the next 18 months | Joint capability requires their roadmap to land first | Their roadmap doc + signed alignment letter |
| Customer overlap below 30% | Avoids cannibalization | CRM cross-reference |
| Exclusivity in adjacent capability for 24 months | Prevents partner from arming our competitor | Term in deal |

If a candidate partner fails on a load-bearing criterion, the partnership doesn't proceed regardless of deal economics. Partner-fit is the gate; deal terms are downstream.

---

## Co-Investment Shape

What each side commits, in plain language. Five categories — name what's committed, by whom, on what timeline.

| Category | Our Side Commits | Their Side Commits |
|---|---|---|
| **Engineering / capability** | [hours, FTEs, capability area] | [hours, FTEs, capability area] |
| **GTM motion** | [campaigns, sales-team time, joint marketing] | [their channel access, their sales-team time, their marketing] |
| **Capital** | [revenue share %, fees, equity if applicable] | [revenue share %, fees, equity if applicable] |
| **Exclusivity / restrictions** | [what we can't do during the term] | [what they can't do during the term] |
| **Time / term** | [duration, ramp milestones] | [duration, ramp milestones] |

The shape must be balanced. If our side commits engineering, GTM, capital, AND exclusivity while their side commits only logo placement, the architecture is not a partnership — it is us subsidizing their distribution. Surface the asymmetry in the artifact and decide whether that's still acceptable.

---

## Re-Decision Trigger (NON-NEGOTIABLE)

Every Partnership Architecture states **when the architecture gets reopened and what signal would invalidate it**. Without a re-decision trigger, the architecture becomes immortal and partnerships outlive their strategic rationale by years.

Format the trigger as a sentence with a named signal and a named threshold:

> "We reopen this architecture when [observable signal] crosses [threshold]. Examples include: partner roadmap divergence beyond [X], counterparty incentive drift such as the partner acquiring a competitor or pivoting to a competing product, our internal build cost dropping below [Y] making partner unnecessary, or partner failure to hit ramp milestone [Z] by [date]."

The trigger must be **observable** (someone could check it without subjective judgment) and **time-bounded** (an explicit review date if no signal fires earlier).

Re-decision is not termination — it's a forced reopening of the make/buy/partner call with current information. The partnership may continue, may renegotiate, or may end.

---

## Output Structure

```markdown
# Partnership Architecture: [Partner Name or Strategic Question]

**Architecture ID**: PA-[YYYY]-[NNN]
**Version**: [Version]
**Owner**: [BizDev lead]
**Status**: Draft / In Negotiation / Active / Under Re-decision / Closed
**Date**: [Date]

---

## 1. Strategic Intent

**What does this partnership unlock that we cannot unlock alone?**

[Plain-language statement, 2-4 sentences. Name the capability, distribution channel, ecosystem position, or strategic option this partnership creates. Tie back to a named strategic bet (`SB-YYYY-NNN`) or strategic intent if one exists.]

**Strategic bet this serves**: [SB-ID or "none — standalone partnership architecture"]

---

## 2. Capability or Distribution Gap

**What can we not do today that the strategy requires?**

[1-2 sentences naming the gap explicitly.]

---

## 3. Make / Buy / Partner Decision

### 3.1 Option Comparison

| Option | Strategic Control | Time to Capability | Capital Required | Reversibility | Strategic-Fit Risk | Verdict |
|---|---|---|---|---|---|---|
| Build | [score] | [time estimate] | [$ or "[TBD]"] | High | Low | [Selected / Rejected — reason] |
| Buy | [score] | [time estimate] | [$ or "[TBD]"] | Low | Medium | [Selected / Rejected — reason] |
| Partner | [score] | [time estimate] | [$ or "[TBD]"] | High | Medium | [Selected / Rejected — reason] |

### 3.2 Decision

**Selected option**: Partner

**Rationale**: [3-5 sentences. Why partnering beats building and beats buying for this specific gap.]

### 3.3 Counterfactual

**If we did NOT partner here, what would we do instead?**

[Plain answer. Either: "We would build it on the following timeline..." OR "We would acquire [target]..." OR "We would not address the gap and accept the strategic cost of [X]." This section is what makes the partnership a deliberate choice rather than an opportunistic deal.]

---

## 4. Partnership Type

**Type chosen from taxonomy**: [Technology / Distribution / Co-sell / OEM / Joint venture / Channel / Platform / Strategic supply]

**Why this type**: [2-3 sentences. The type determines the co-investment shape and the legal structure — name why this type is the right shape for the strategic intent above.]

---

## 5. Partner-Fit Criteria

| # | Attribute | Why It Matters | How Verified | Met by Candidate? |
|---|---|---|---|---|
| 1 | [Attribute] | [Why load-bearing] | [Verification method] | Yes / No / Pending |
| 2 | [Attribute] | [Why load-bearing] | [Verification method] | Yes / No / Pending |
| 3 | [Attribute] | [Why load-bearing] | [Verification method] | Yes / No / Pending |

**Gate**: A candidate failing a load-bearing criterion does NOT proceed regardless of deal economics.

---

## 6. Co-Investment Shape

| Category | Our Side Commits | Their Side Commits |
|---|---|---|
| Engineering / capability | [Specifics] | [Specifics] |
| GTM motion | [Specifics] | [Specifics] |
| Capital | [Specifics] | [Specifics] |
| Exclusivity / restrictions | [Specifics] | [Specifics] |
| Time / term | [Specifics] | [Specifics] |

**Asymmetry check**: [Is the shape balanced? If asymmetric, name the asymmetry and whether it is still acceptable given the strategic intent.]

---

## 7. Success Metrics

What we measure to know the partnership is working. Distinct from deal terms.

| # | Metric | How Measured | Target by [Date] |
|---|---|---|---|
| 1 | [Metric] | [Source] | [Target — use [TBD] if unknown] |
| 2 | [Metric] | [Source] | [Target — use [TBD] if unknown] |
| 3 | [Metric] | [Source] | [Target — use [TBD] if unknown] |

---

## 8. Re-Decision Trigger

**When this architecture gets reopened**:

[Sentence stating the observable signal and threshold. Example: "We reopen this architecture if partner roadmap diverges from joint commitments for two consecutive quarterly reviews, OR if our internal build cost drops below $X per [unit], OR if partner is acquired by or pivots toward a direct competitor, OR by [explicit review date] regardless of signals."]

**Explicit review date** (independent of signals): [Date — typically 12 or 18 months]

---

## 9. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Partner incentive drift | [H/M/L] | [H/M/L] | [Mitigation] |
| Roadmap dependency lock-in | [H/M/L] | [H/M/L] | [Mitigation] |
| Customer / channel cannibalization | [H/M/L] | [H/M/L] | [Mitigation] |
| Exit cost if architecture is reopened | [H/M/L] | [H/M/L] | [Mitigation] |

---

## 10. Cross-References

- **Positioning context**: [Link to `/positioning-statement` if relevant — does the partnership change positioning?]
- **GTM context**: [Link to `/gtm-strategy` if the partnership reshapes the GTM motion]
- **Release narrative context**: [Link to `/launch-narrative-brief` if the partnership is part of a release narrative]
- **Business case**: [Link to `/business-case` for financial framing]
- **Strategic bet**: [Link to `/strategic-bet` if the partnership is itself a bet]
- **Decision record**: [Link to `/decision-record` capturing the commit decision]
- **Contract**: [Link to `/contract-review` artifact once deal-stage]

---

## 11. Stakeholders

| Role | Stakeholder | Type |
|---|---|---|
| Architecture Owner | [BizDev lead] | Accountable |
| Strategic Sponsor | [VP Product / CPO] | Accountable |
| Partner counterpart | [Their lead] | External |
| Engineering review | [Chief Architect or Tech Lead] | Consulted |
| Legal review | [Contracts Counsel / IP Counsel] | Consulted |
| GTM review | [PMM-Dir] | Consulted |
| Finance review | [BizOps / FP&A] | Consulted |
| M&A consult (if buy was a real option) | [Head Corp Dev / M&A Analyst] | Consulted |
```

---

## Instructions

1. **Confirm this is a partnership-strategy formulation, not a deal close**. If the input is an inbound customer RFP, route to `/sales-enablement` or `/proposal-writer`. If the input is a contract clause-level review, route to `/contract-review`. This skill is for formulating whether a strategic relationship should exist at all.

2. **Start with strategic intent (§1)**. If the user cannot state in 2-4 sentences what the partnership unlocks that they cannot unlock alone, the architecture is not yet ready — surface that and ask the question explicitly.

3. **Force the make/buy/partner comparison (§3)**. Do not skip the build and buy options even if the user has already decided to partner. The counterfactual is what makes the partnership a deliberate choice.

4. **Choose partnership type from the taxonomy (§4)**. Do not invent a type per deal. If no type fits, force the decision and note the variance.

5. **Limit partner-fit criteria to 3-7 load-bearing attributes (§5)**. A long checklist of nice-to-haves is the failure mode — fewer attributes that are genuinely gating beat exhaustive lists.

6. **Make the co-investment shape balanced (§6)**. If the asymmetry is severe (we commit heavily, they commit logo placement), surface the asymmetry as a finding and decide whether the strategic intent still justifies it.

7. **The re-decision trigger is non-negotiable (§8)**. The trigger must be observable and time-bounded. A partnership without a re-decision trigger becomes immortal — refuse to publish without one.

8. **Cross-reference adjacent artifacts (§10)**. Link to `/launch-narrative-brief`, `/positioning-statement`, `/gtm-strategy`, `/business-case`, `/strategic-bet`, and `/decision-record` as relevant. Partnership Architecture is a formulation surface; the downstream artifacts are where the architecture gets executed.

9. **Save to `partnerships/` or `strategy/partnerships/`**. Auto-register with the document index per `context-management.md`.

10. **Do not invent financials**. For capital, time-to-capability, and revenue projections, use `[TBD]` placeholders or cite user-provided sources. The framework value is in the structured decision; the numbers are owned downstream.

---

## Gotchas

- **Confusing partnership formulation with deal close**: If the artifact reads like a sales pitch to the partner, it's wrong altitude — it should read like a strategic decision document to ourselves.
- **Skipping the counterfactual**: A partnership architecture without "what we'd do if we didn't partner" is a deal log. Force the counterfactual.
- **Inventing a partnership type**: The taxonomy exists so the type carries structure. "Strategic alliance" is not a type — pick from the eight or escalate.
- **Long partner-fit checklists**: 12 nice-to-have attributes are worse than 4 load-bearing ones. Cut to what's gating.
- **Unbalanced co-investment hidden in narrative**: If our side commits engineering + GTM + capital + exclusivity and their side commits a logo, the architecture should surface that asymmetry, not bury it.
- **Missing re-decision trigger**: An architecture without a trigger outlives its strategic rationale. Refuse to ship without one.
- **Partnership architecture for what should be an acquisition**: If the partner provides core differentiation and we'd lose the strategy if they walked, it's a buy candidate, not a partner candidate. Surface the mismatch.

---

## Related Skills

| Skill | Relationship |
|---|---|
| `/positioning-statement` | Sibling — GTM strategy formulation surface (same altitude as Partnership Architecture) |
| `/launch-narrative-brief` | Downstream — uses partnership context when a release narrative includes the partner |
| `/gtm-strategy` | Downstream — incorporates partner channel decisions |
| `/business-case` | Adjacent — financial framing of the partnership economics |
| `/strategic-bet` | Adjacent — when the partnership is itself the strategic bet |
| `/decision-record` | Downstream — the commit-point record of the architecture decision |
| `/contract-review` | Downstream — clause-level work after the architecture is set |
| `/competitive-landscape` | Upstream input — ecosystem map informs partner-fit and counterfactual |
| `/seven-powers` | Upstream input — assesses whether the partnership creates durable strategic power |
| `/risk-analysis` | Adjacent — partnership-specific risk dimensions feed §9 |

---

## Operating Principle

> "Partnership architecture is a strategic choice, not a deal log. The architecture decides which strategic relationships should exist; the deal terms decide how to make a chosen one work."
