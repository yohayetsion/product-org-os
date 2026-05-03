---
name: maturity-check
description: 'Diagnose organizational maturity using the Vision to Value Three Tiers framing or the sub-Series-C lane. Activate when: "maturity assessment", "how mature are we", "tier diagnosis", "tier-mismatch", "decision improvability", "where does this decision belong". Do NOT activate for: PM individual competency check (/pm-level-check), scalability assessment (/scale-check), Vision to Value phase check (/phase-check).'
argument-hint: '[capability area or decision class]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 4.0.0
  category: assessment
  skill_type: task-capability
  owner: chro
  primary_consumers:
  - pm-dir
  - product-mentor
  - chro
  secondary_consumers:
  - cpo
  - coo
  - hr-dir
  - performance-specialist
  - it-dir
  - operations-dir
  - process-engineer
  - coach
---

Diagnose **Organizational Maturity** for a specific capability area or decision class, using the Vision to Value Three Tiers framing — or the sub-Series-C lane when the organization does not yet have the seats to populate the three-tier altitude structure.

## Vision to Value Phase

**Cross-phase.** A maturity diagnosis informs the appropriate altitude, cadence, and decision-system shape at any phase.

**Prerequisites**: A specific capability area, decision class, or organizational dimension to diagnose.
**Outputs used by**: Decision-system design, Charter installation, role-and-cadence design, scaling decisions, and improvement planning.

## What changed from the prior four-level model

Earlier versions of `/maturity-check` used a four-level rubric (Enabling → Established → Company Leading → Market Leading). The Vision to Value book v5.2 reframed organizational maturity around **altitude**, not stage. The four-level model conflated three different things — capability strength, decision discipline, and organizational scale — and produced scores that did not tell a leader where to act.

The current rubric replaces that frame with two diagnostic shapes that operate side by side:

1. **The Three Tiers** for organizations with the seats to populate three altitudes of decision-making.
2. **The sub-Series-C lane** for organizations operating below the threshold where the Three Tiers can be populated cleanly. The sub-Series-C lane is not a lower maturity level. It is a different altitude, with a different correct decision-system shape.

### Reading this if you scored Company Leading under the prior four-level model

A Company Leading score under the four-level model meant "best practices, strategic alignment." That score is not invalidated by the new framing. It maps to a decision system in which Tier 2 (the product altitude) is running cleanly and Tier 1 (the vision altitude) is being run by people, not yet by a charter. The new diagnostic surfaces what the old score could not: whether the organization can repeat the Tier 2 work without the same individuals in the room, and whether the Tier 1 work has the structure to survive a leadership change. If your prior score was Company Leading, treat the new diagnostic as a refinement of where you are, not a re-evaluation. The work that earned Company Leading earned it; the new framing tells you what to install next.

## The diagnostic, in two shapes

### Shape A — The Three Tiers

For organizations with the seats to populate three altitudes of decision-making (typically late Series B and beyond, with Director-tier and VP-tier roles seated and a PLT installed or installable).

| Tier | Altitude and time-horizon | Who sits here | What gets decided here |
|------|---------------------------|---------------|------------------------|
| **Tier 1 — Vision** | Multi-year strategic direction, portfolio shape, category bets, commitments to outcomes measured in two-to-five years. | CPO, VP Product, board, Chief-tier peers. | Portfolio shape, category commitments, capital envelopes, board-level bet reviews. |
| **Tier 2 — Product** | One-to-two-year product-line direction, feature-level roadmap commitments, customer-evidence-driven scope decisions, interfaces with Chief-tier peer functions. | Director of Product Management, PM-Directors, Director of Product Marketing, peer-function Directors. | Roadmap commitments, scope tradeoffs, the Decision Interface Charter, peer-function interfaces. |
| **Tier 3 — Execution** | Quarterly delivery, sprint-level scope, customer-feedback loops tight to the release cadence, daily cross-functional coordination. | PMs, engineers, designers, PMMs. | Sprint scope, launch-readiness calls, release-level scope tradeoffs, daily coordination. |

The three tiers are not a hierarchy of importance but of **altitude and time-horizon**. A decision made at the wrong tier is a decision in the wrong room. The recurring failure modes are tier-mismatch failures: Tier 3 execution compensating for Tier 2 drift; Tier 2 absorbing Tier 1 elaboration; Tier 1 reaching down into Tier 3 and starving Tier 2 of air.

The diagnostic asks, for each capability area or decision class:

1. **At which tier is this decision being made?**
2. **At which tier should it be made?** (route by altitude and time-horizon, not by who is loudest in the room)
3. **If there is a mismatch, in which direction is it drifting?** (Tier 3 reach-up, Tier 2 absorption, Tier 1 reach-down)
4. **What is the smallest design move that returns the decision to the correct tier?**

### Shape B — The sub-Series-C lane

For organizations operating below the threshold where the Three Tiers can be cleanly populated. Typically: roughly thirty people or fewer, founder still standing in a product-leader seat, no Director of PM yet, no PLT, two-to-three product specialists total. Appendix F of the book ("Sub-Series-C, Reading the Book Before You Have the Seats") is the canonical reference.

The sub-Series-C diagnostic does not score the organization against the Three Tiers and find it lacking. It scores the organization against a **different correct shape**:

| Dimension | What "right for the stage" looks like |
|-----------|---------------------------------------|
| Decision forum | One standing forum: founder + head of product + one or two adjacent leaders. The PLT is deferred. |
| Inputs list per decision | A single list of three to five names, not three tiers of seats. |
| Charter | A compressed Charter (Appendix F) running one or two decision classes — typically pricing exceptions and platform intake — not the full Appendix A Charter network. |
| Sensor discipline | Informal: "write down what the customer told you and what the funnel did, before the decision gets made." Formal sensor-to-decision-compulsion protocol is deferred until two empowerment-tier directors are seated. |
| AI-augmentation overlay | Not yet. Write decision records that an agent could later parse; resist installing AI augmentation as a substitute for the decision system itself. |

The sub-Series-C diagnostic asks:

1. **Is the organization actually sub-Series-C, or is it past the threshold and running an under-installed decision system?** (If past the threshold, route to Shape A.)
2. **Are the standing forum, the compressed Charter, and the single-inputs list installed?** (If yes, the diagnostic is "right shape for the stage" — not low maturity.)
3. **Are practices being installed early as decoration?** (Formal sensor discipline, full PLT seating, AI-augmentation overlays installed before they can carry weight.)
4. **What is the next pivot, and what triggers it?** (Second product director joins → second Charter; third peer-function director joins and founder steps back → expand inputs list to three tiers and graduate to the full Charter.)

A sub-Series-C organization running the right shape for its stage is **not** a Tier 3 organization. It is a different organism. Scoring it against the Three Tiers and finding it "low maturity" is a category error.

## The Three capabilities — the evaluation lens

Vision to Value names three organizational capabilities that every chapter of the book returns to as the evaluation lens. The diagnostic surfaces all three for the area being assessed:

- **Decision quality** — making the right calls given available information and constraints. Were the right alternatives considered? Were the criteria explicit at decision time, not reconstructed afterward? Did the decision frame the actual problem, or only the surface symptom?
- **Decision repeatability** — enabling those decisions to be made consistently beyond individual leaders. If the senior person in the room is replaced, does the same class of decision still come out at the same quality? Are the inputs, the forum, and the criteria written down at all?
- **Decision durability** — ensuring decisions survive time, scale, and organizational pressure. Does the decision hold across the next planning cycle, the next leadership change, the next pricing pressure? Or does it quietly erode and get re-litigated under the next stress?

Vision turns into value only when **all three** are present. Quality without repeatability is fragile (it leaves with the founder). Repeatability without durability collapses under scale (the process holds until the org doubles, then breaks). Durability without quality preserves mistakes (the wrong decision gets enshrined).

The diagnostic produces a capability score for each of the three, on the area being assessed:

| Capability | Strong | Adequate | Weak |
|------------|--------|----------|------|
| Decision quality | Right alternatives considered, criteria explicit at decision time, actual problem framed. | Decisions are mostly right but reasoning is partly reconstructed afterward. | Decisions arrive without explicit alternatives; problem framing skips to solution. |
| Decision repeatability | Same class of decision comes out at same quality without the senior person in the room. | The forum exists but the senior person's judgment is still the binding input. | Each decision is bespoke; replacement of the senior person collapses the class. |
| Decision durability | Decisions hold across leadership changes, pricing pressure, the next planning cycle. | Decisions hold for one or two cycles, then erode quietly. | Decisions are re-litigated under the next stress; no durable record exists. |

## The Decision Improvability scoreboard

Decision Improvability is the scoreboard of a working product operating system: the organization's ability to make the same class of decision better this quarter than last, because quality, repeatability, and durability reinforce one another. It is measured not by a single decision but by the **trajectory of a class of decisions over a meaningful window**.

The diagnostic surfaces Decision Improvability for the area being assessed across three signals. The data source for this scoreboard is `/decision-quality-audit` — the trajectory-aware extension of that skill (the v5.1-37 sidecar) supplies the audit data this scoreboard reads.

| Signal | What it measures | Read from |
|--------|------------------|-----------|
| **Decision frame quality** | Were decisions in this class framed as decisions (with named alternatives and explicit criteria) or as problem statements waiting for a recommendation? Trajectory: is frame quality improving, flat, or eroding across the window? | `/decision-quality-audit` frame-quality field, trajectory across the audit window. |
| **Alternative shortlist quality** | Did decisions consider the right alternatives, or did the shortlist arrive pre-narrowed? Trajectory: is the org getting better at surfacing alternatives the previous quarter would have missed? | `/decision-quality-audit` alternative-shortlist field, trajectory across the audit window. |
| **Criteria specification quality** | Were criteria specified at decision time, or only reconstructed post-hoc to justify the chosen path? Trajectory: is criteria-at-decision-time discipline strengthening or weakening? | `/decision-quality-audit` criteria-at-decision-time field, trajectory across the audit window. |

A class of decisions with strengthening trajectory across all three signals is **improving**. A class flat across all three is **stable but not learning**. A class with eroding trajectory on any signal is **losing the discipline that produced the prior quality** — the diagnostic flags this as a higher-priority gap than a class that has never had the discipline, because erosion compounds.

When this skill produces output, it does not invent the underlying audit numbers. It reads them from `/decision-quality-audit` if the audit data exists, or it flags that the audit has not been run for the class being assessed and recommends running it before the Decision Improvability scoreboard can be populated.

## Output Structure

```markdown
# Maturity Diagnosis: [Capability area or decision class]

**Diagnosis Date**: [Date]
**Assessor**: [Name]
**Scope**: [Team / org / decision class assessed]
**Diagnostic shape**: Three Tiers | sub-Series-C lane

## Why this shape

[One paragraph: why the Three Tiers shape applies, or why the sub-Series-C lane applies. If sub-Series-C: name the threshold conditions that locate the org below the Three-Tier altitude. If Three Tiers: name the seats that allow the three altitudes to be populated.]

---

## Shape A: Three Tiers diagnosis (use if applicable)

### Where is this decision being made today?

**Tier**: [1 / 2 / 3]
**Evidence**:
- [Who is in the room when this decision is made]
- [What forum or cadence the decision lives in]
- [What time-horizon the decision is committing to]

### Where should this decision be made?

**Tier**: [1 / 2 / 3]
**Reasoning**:
- [Altitude argument: time-horizon, reversibility, who carries the consequences]
- [Counterparty argument: which Charter and which peer roster apply]

### Tier-mismatch verdict

**Mismatch direction** (if any):
- [ ] Tier 3 reaching up (execution absorbing Tier 2)
- [ ] Tier 2 absorbing Tier 1 (product layer carrying portfolio decisions)
- [ ] Tier 1 reaching down (vision layer pulling Tier 3 detail into the boardroom)
- [ ] No mismatch — decision is at the right altitude

### Smallest design move to correct the tier

[One specific Charter, cadence, or decision-record move. Not a full reorg.]

---

## Shape B: Sub-Series-C diagnosis (use if applicable)

### Right-shape-for-stage check

| Dimension | Installed correctly | Missing | Installed as decoration |
|-----------|---------------------|---------|-------------------------|
| Standing forum (founder + head of product + 1-2 adjacent) | [ ] | [ ] | [ ] |
| Compressed Charter (one or two decision classes) | [ ] | [ ] | [ ] |
| Single inputs list (3-5 names per decision) | [ ] | [ ] | [ ] |
| Informal sensor discipline (writing down customer + funnel before deciding) | [ ] | [ ] | [ ] |
| Decision records written so an agent could later parse them | [ ] | [ ] | [ ] |

### Pivot triggers — what graduates this org out of the sub-Series-C lane

| Pivot | Trigger |
|-------|---------|
| Second Charter | Second product director joins. |
| Standing forum → PLT | Third peer-function director joins and founder steps back from the standing seat. |
| AI-augmentation overlay available | Underlying decision system is running (Charter network installed, telemetry layer exists). |

### Verdict

[ ] Right shape for the stage — not low maturity, just sub-Series-C.
[ ] Under-installed for the stage — install the missing dimension(s) above before scaling.
[ ] Past the threshold — graduate to the Three Tiers diagnosis.

---

## Three capabilities scorecard (applies to both shapes)

| Capability | Strong | Adequate | Weak | Evidence |
|------------|--------|----------|------|----------|
| Decision quality | [ ] | [ ] | [ ] | [Specific evidence] |
| Decision repeatability | [ ] | [ ] | [ ] | [Specific evidence] |
| Decision durability | [ ] | [ ] | [ ] | [Specific evidence] |

**The combination matters.** Quality without repeatability is fragile. Repeatability without durability collapses under scale. Durability without quality preserves mistakes. Name the weakest of the three, because that is the one that will break first under stress.

## Decision Improvability scoreboard (applies to both shapes)

**Audit data source**: `/decision-quality-audit` for [decision class], audit window: [window].

| Signal | Trajectory across window | Verdict |
|--------|--------------------------|---------|
| Decision frame quality | Improving / flat / eroding | [ ] |
| Alternative shortlist quality | Improving / flat / eroding | [ ] |
| Criteria specification quality | Improving / flat / eroding | [ ] |

**Improvability verdict**:
- [ ] Improving (strengthening trajectory across all three signals)
- [ ] Stable but not learning (flat across all three)
- [ ] Eroding (any signal worsening — higher-priority gap than never-had-the-discipline)
- [ ] No audit data — recommend running `/decision-quality-audit` for [decision class] before populating this scoreboard.

## Strengths to leverage

| Strength | Evidence | How to leverage |
|----------|----------|-----------------|
| [Strength 1] | [Evidence] | [Specific design move] |

## Gaps to close

| Gap | Impact | Priority | Smallest design move |
|-----|--------|----------|----------------------|
| [Gap 1] | High/Med/Low | P1/P2/P3 | [One specific move — Charter, cadence, decision record, or routing change] |

## Recommendations

**Immediate (this month)**:
1. [Specific Charter, cadence, or decision-record move]

**This quarter**:
1. [Capability investment, sequenced]

**Reading-this-if-you-scored-Company-Leading note** (only include if applicable):
[Map prior four-level Company Leading score to current Three-Tier diagnostic. Do not invalidate the prior judgement; clarify what the new framing surfaces that the old one did not.]
```

## Instructions

1. **Identify the diagnostic shape first.** Ask whether the organization has the seats to populate the Three Tiers (Director-tier seated, PLT installed or installable, peer-function Directors present) or whether it is sub-Series-C (founder still in a product-leader seat, no PLT, three-to-five-name forum). If unclear, ask. Do not default to the Three Tiers and then "find the org wanting." A sub-Series-C organization running the right shape for its stage is not low maturity.
2. **Diagnose at the level of a capability area or a decision class**, not the whole organization at once. "Pricing exceptions" is a decision class. "Roadmap commitments" is a decision class. "Launch-readiness calls" is a decision class. "Product organization maturity" as a single number is not a useful target.
3. **Locate the decision at the correct altitude (Three Tiers shape) or check right-shape-for-stage (sub-Series-C shape)** before scoring capabilities. Tier-mismatch is the most common finding and the most actionable.
4. **Do not populate the Decision Improvability scoreboard from intuition.** Read it from `/decision-quality-audit` data for the decision class. If the audit has not been run, say so and recommend running it.
5. **Surface all three capabilities — quality, repeatability, durability — and name the weakest.** The weakest one is what will break first under stress. A strong-quality / weak-repeatability score is a different problem from a strong-quality / weak-durability score, and the corrective design moves are different.
6. **For users who previously scored Company Leading under the four-level model**, include the reader-continuity note in the output. The prior score is not invalidated; the new framing refines what was already there.
7. **Recommend the smallest design move that corrects the diagnosis.** A Charter installation, a cadence change, a decision-record-writing discipline, a single seat addition. Not a reorg. The book's design discipline is "smallest move that restores decision quality."
8. Save the output in the assessments/ folder.
9. Offer to create a presentation version using `/present` if the diagnosis is being briefed to a leadership forum.

## Cross-references

- `/decision-quality-audit` (V5.1-37 sidecar) — supplies the audit data the Decision Improvability scoreboard reads. Run it for the decision class before populating the scoreboard.
- `/decision-charter` — the Charter discipline that runs at every tier; the design move that corrects most tier-mismatch findings.
- `/scale-check` — orthogonal scalability check (process / system / initiative at 2x / 10x / 100x). Pair with `/maturity-check` when the diagnosis is "right altitude but the system will not survive the next scale step."
- `/phase-check` — Vision to Value phase position. Orthogonal to maturity altitude; a Phase 3 commitment can be made at Tier 1, Tier 2, or Tier 3 depending on the bet's altitude.
- Vision to Value Appendix F — canonical reference for the sub-Series-C lane.
