---
name: v2v-install-90-day
description: 'Produce a Vision to Value 90-day install plan for a newly-seated product leader (CPO, VP Product, or Director of Product Operations) inheriting a functioning-but-drifting product organization. Activate when: "install the operating system", "first 90 days", "I just took the seat", "what do I do in my first quarter", "Appendix B install", "ninety-day install", "90 day plan", "Vision to Value install" Do NOT activate for: an existing PLT looking to retune (use /scale-check or /maturity-check); a PMF-stage team without a PLT (use /maturity-check to confirm stage; the install plan does not yet apply); changing an org chart (use /scale-check Director-Span Constraint and /raci-builder).'
argument-hint: '[organization name + leader role + stage] or [update path/to/install-plan.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: operating-system-install
  skill_type: task-capability
  owner: cpo
  primary_consumers:
  - cpo
  - vp-product
  - prodops
  secondary_consumers:
  - pm-dir
  - bizops
  - value-realization
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided | UPDATE | 100% |
| "create", "new", "draft", "I just took the seat" | CREATE | 100% |
| "find", "search", "list" | FIND | 100% |
| "the install plan", "our 90-day plan" | UPDATE | 85% |
| Just leader role + stage | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate a complete new 90-day install plan using the structure below. Begin with the Where You Are Now entry checkpoint (the diagnostic Three Tiers); only then proceed to the six moves and the failure-mode register.

**UPDATE**:
1. Check document registry first, then search user's structure
2. Preserve the install-plan ID, version, and the Where You Are Now classification (re-classify only if the underlying organization moved tiers)
3. Update progress against the six moves and the failure-mode watch list
4. Show diff summary

**FIND**: Check registry, then search user's folders for install plans.

---

Produce a **Vision to Value 90-Day Install Plan** for a newly-seated product leader installing the Decision Interface Charter, the operating cadence, and the observability signals described in the Vision to Value book. The skill is the executable form of Appendix B of the Vision to Value book — the six moves at named windows, paired with the four named failure modes that catch new leaders in their first quarter.

## Vision to Value Phase

**Cross-phase, install-time** — This skill is the install plan a newly-seated leader produces in their first week before they have run a single Charter cycle. Every phase the Vision to Value book describes (Strategic Foundation, Strategic Decisions, Strategic Commitments, Coordinated Execution, Business Outcomes, Learning Loop) operates inside the install this plan produces.

**Prerequisites**: Reader is newly-seated as CPO, VP Product, or Director of Product Operations; reader has read Chapters 4 and 5 of the Vision to Value book; reader has the Decision Interface Charter template open (`/decision-charter`) and is about to make the most common first-90-days mistake — trying to install the whole operating system at once.

**Outputs used by**: `/decision-charter` (the first install target — the Charter the plan installs in Days 1-30); `/maturity-check` (the diagnostic that scopes which moves apply at the reader's stage); `/strategic-intent` (the Move 5 commitment hardens against the strategic intent); `/scale-check` (the Director-Span Constraint applies to PLT seating in Move 3).

## Purpose

The Vision to Value 90-Day Install Plan is the executable form of Appendix B of the Vision to Value book. It walks a newly-seated leader through six named moves at named windows, classifies the organization into one of three diagnostic tiers (so the leader installs the right shape, not the canonical shape regardless of stage), and names the four most common failure modes that capture leaders in their first quarter. The plan is deliberately the move that buys the leader time to install correctly rather than the move that lets the leader feel decisive in Week One.

## The Six Moves at Named Windows

These six moves are the canonical Appendix B sequence. They are the map. The named windows below are the itinerary.

| Move | Name | Window | Output |
|---|---|---|---|
| Move 1 | Read the landscape before replacing it | Week One (Days 1-7) | One-page state-of-the-decision-system note |
| Move 2 | Install ONE Charter on one decision | Days 1-30 | A single Decision Interface Charter, run as a commit not a proposal |
| Move 3 | Name the PLT and its seats | Days 1-30 (parallel with Move 2) | Seven seats named at director altitude |
| Move 4 | Name the four CPO interfaces | Days 30-60 | CPO-CTO, CPO-CRO, CPO-CFO, CPO-CMO interfaces named at decision altitude |
| Move 5 | Convert one Decision to a Commitment | Days 60-90 | One Decision hardened by attaching a resource (hire, funding, sequencing, external promise) |
| Move 6 | Install the Portfolio and Product-line Reviews | Days 60-90 (concludes the quarter) | Portfolio Review (quarterly, 90 min) + Product-line Review (monthly, 60 min) + first re-decision trigger fires against documented threshold |

The pattern is sequencing, not standing. The right first move is to change nothing at all in Week One, install one Charter in the first 30 days, expand the operating layer in Days 30-60, and harden the first Decision into a Commitment with a clean re-decision in Days 60-90.

## Output Structure

```markdown
# Vision to Value 90-Day Install Plan: [Organization Name]

**Plan ID**: V2VI-[YYYY]-[NNN]
**Version**: 1.0
**Newly-Seated Leader**: [Name, Role — CPO / VP Product / Director of Product Operations]
**Reporting To**: [Role]
**Plan Author Date**: [Date]
**Plan Window**: Day 0 through Day 90 ([start date] to [end date])

## Where You Are Now (Entry Checkpoint)

Classify the organization into one of three diagnostic tiers before applying the six moves. The tier determines which moves apply now and which are deferred. A tier mismatch is the single largest cause of an install plan that produces decoration rather than architecture.

| Tier | Stage Signals | What This Plan Applies As |
|---|---|---|
| **Tier 1 — Pre-PLT (compressed)** | Team 10-30 (Series A through early Series B). Head of product, sometimes VP. No PLT as a forum. Some of the seven seats present in name; others carried by founders or adjacent functions. | Compressed install: Move 1 + Move 2 only. Run the compressed Charter (Appendix F.2 shape) on one decision. Do NOT seat the seven-seat PLT yet. Do NOT name the four CPO interfaces yet. Revisit Moves 3-6 when peers at director altitude are seated in at least four of the seven default seats. |
| **Tier 2 — PLT-emerging (transitional)** | Team 30-100 (late Series B going into Series C). PLT taking shape. Second product director hired. Product marketing seated. First cross-functional interface meeting on a cadence. | Bridge install: Move 1, Move 2, Move 3 inside the first 60 days. Begin Move 6 cadence install. Defer Move 4 (CPO interfaces) and Move 5 (Commitment hardening) until the second peer-function director is seated. The compressed Charter is graduating to the full Appendix A Charter, one decision at a time. |
| **Tier 3 — PLT-installed (full canonical)** | Team 100+ (Series C and beyond). CPO seated. Peer-VP interfaces named. PLT runs on a cadence. The question is no longer whether to install but whether the running install is the right shape. | Full canonical install: All six moves at the named windows. The plan operates exactly as Appendix B describes. |

**Diagnostic prompts the skill asks**:
1. How many people report into Product (PM, PMM, BizDev, CI, BizOps, ProdOps, CS-VR)?
2. Is there a standing PLT forum that meets on a cadence with director-altitude owners across the seven default seats? (Yes / Partial / No)
3. Are the four CPO-counterparty interfaces (CTO, CRO, CFO, CMO) named at decision altitude with at least one decision recorded against each? (Yes / Partial / No)
4. Has the organization run a clean re-decision (a bet stopped or restructured against a documented trigger) in the last six months? (Yes / No)
5. Is ProdOps held by a director or VP, or by a coordinator? (Director+ / Coordinator)

**Tier classification**: [Tier 1 / Tier 2 / Tier 3]
**Rationale**: [One paragraph naming the 3-5 signals that drove the classification]
**Plan shape applied**: [Compressed / Bridge / Full canonical]

## Move 1 — Read the Landscape Before You Replace It (Week One)

**Window**: Days 1-7
**Output**: One-page state-of-the-decision-system note
**Install Action**: None. The diagnostic is the move.

Do not change anything in Week One. The temptation will be large, especially if the dysfunction is visible enough that the CEO hired the new leader to fix it. Resist it. Map what is already installed, memorized as ritual, and missing — across existing cadences, decision records, the commitment register, and in-flight bets — before replacing anything.

**Four artifacts to inventory**:

1. **Existing cadences** — every recurring forum with a product dependency. For each: is this forum making decisions, or is it running status?
2. **Existing decision records** — search the last 12 months of PRDs, launch readiness memos, portfolio reviews, kill decisions. Findability test: can a decision made in Q2 of last year be found in under 30 seconds? If not, the archive is missing and ProdOps work is ahead.
3. **Commitment register** — what the organization currently believes it has committed to. Roadmap, board deck, top-of-funnel promises, contractual commitments to lighthouse customers. Surface mismatches between what three different leaders think is committed.
4. **In-flight bets** — which bets are live, who owns them, what T+2 / T+6 / T+12 indicators are instrumented. If instrumentation is absent, re-decision triggers cannot fire.

**Close Move 1 with**: A one-page state-of-the-decision-system note. What is installed. What is memorized. What is missing. What is drifting. Share with CEO/CPO and the standing leadership forum (or PLT, if one exists) as a read, not a plan.

## Move 2 — Install ONE Charter on One Decision (Days 1-30)

**Window**: Days 1-30 (lands in parallel with Move 3)
**Output**: A single Decision Interface Charter installed as a commit
**Install Action**: Pick the highest-leverage first-install candidate, fill out the Charter in full (`/decision-charter`), take it to the PLT (or compressed forum) as a commit, not a proposal.

**The first Charter has three properties**: visibly broken (someone will thank you for fixing it), high-stakes enough that the PLT will care about the outcome, bounded enough that it can be instrumented in 30 days.

**The book names three first-install candidates**:

| Candidate | Right For |
|---|---|
| **Launch Readiness** | A new VP Product inheriting a shipping-velocity problem. Almost always the right first install for this profile. |
| **Pricing Exceptions** | A CPO inheriting a commercial-integrity problem. Fastest path to visible commercial-outcome improvement. |
| **Platform Intake** | A ProdOps director installing the operating layer below an existing CPO. Cleanest first win because it has the most visible queue pathology. |

**Charter completion checklist** (every field filled, none skipped):
- [ ] Single accountable owner named
- [ ] Required-inputs grouped as core / empowerment / execution (not flat — the three-tier structure is what converts the Charter from process document to architecture)
- [ ] Explicit "say no" boundaries
- [ ] At least one outcome-evidence re-decision trigger (with named threshold)
- [ ] At least one market-evidence re-decision trigger (with named threshold)
- [ ] Forum on the calendar with pre-read deadline
- [ ] Decision artifact location exists
- [ ] Charter taken to the PLT/forum as a commit, asking for input on inputs and triggers, NOT asking whether to install

**The 30-day rule**: Do not install a Charter on any other decision in this window. Not platform intake, not pricing exceptions, not portfolio sequencing. A second install in Week Three competes for the same limited organizational attention the first install needs to actually land.

**First install candidate (selected)**: [Launch Readiness / Pricing Exceptions / Platform Intake / Other]
**Why this candidate**: [Rationale — visibility, stakes, instrumentability]
**Accountable owner**: [Role]
**Forum cadence**: [Cadence — e.g., Thursdays 14:00 with pre-read by EOD Tuesday]
**First Charter review date**: [Date]

## Move 3 — Name the PLT and Its Seats (Days 1-30, parallel with Move 2)

**Window**: Days 1-30 (parallel with Move 2)
**Output**: Seven director-altitude seats named on the PLT
**Install Action**: Name the seven default PLT seats and seat each one with a director-altitude owner. Apply the `/scale-check` Director-Span Constraint to the PLT structure before locking it.

**The seven default PLT seats**:

| Seat | Function | Default Title |
|---|---|---|
| 1 | Product Management | Director of Product Management |
| 2 | Product Marketing | Director of Product Marketing |
| 3 | Business Development | Business Development Leader |
| 4 | Competitive Intelligence | CI Lead (gating sensor identity) |
| 5 | Business Operations | Director of Business Operations |
| 6 | Product Operations | Director of Product Operations |
| 7 | Customer Success and Value Realization | Director of CS + VR Lead (co-seated) |

**Seating discipline**:
- Seat each seat with a director-altitude owner — not a coordinator, not a proxy, not "someone from that team will attend."
- The forum's composition is load-bearing. A PLT seated at coordinator altitude cannot hold a re-decision; a PLT with gaps cannot gate the sensor reads Principle 8 requires.
- If the Business Operations director is represented by a senior analyst at the first Charter review, the Charter is already losing.
- Run `/scale-check` Director-Span Constraint on every seated director's reporting line. A Director with fewer than 6 reports is overhead; a Director with more than 12 is calibration-only management. Outside the band, the seat is structurally compromised even when the individual is strong.

**PLT roster (current state)**:
| Seat | Owner | Director-altitude? | Direct Reports | Director-Span Verdict | Action |
|---|---|---|---|---|---|
| Product Management | [Name] | Yes/No | [N] | Pass / Concern / Fail | [Action] |
| Product Marketing | [Name] | Yes/No | [N] | Pass / Concern / Fail | [Action] |
| Business Development | [Name] | Yes/No | [N] | Pass / Concern / Fail | [Action] |
| Competitive Intelligence | [Name] | Yes/No | [N] | Pass / Concern / Fail | [Action] |
| Business Operations | [Name] | Yes/No | [N] | Pass / Concern / Fail | [Action] |
| Product Operations | [Name] | Yes/No | [N] | Pass / Concern / Fail | [Action] |
| Customer Success / VR | [Name] | Yes/No | [N] | Pass / Concern / Fail | [Action] |

## Move 4 — Name the Four CPO Interfaces (Days 30-60)

**Window**: Days 30-60 (in parallel with Move 6 cadence install)
**Output**: Four CPO-counterparty interfaces named at decision altitude with at least one decision recorded against each by Day 60
**Install Action**: Name each interface as the altitude at which it decides, not as a consultative pairing. Record the first decision per interface inside this window.

| Interface | What It Decides | First Decision to Record |
|---|---|---|
| **CPO ↔ CTO (Platform Envelope)** | Reliability posture, architectural-debt retirement sequencing, build-buy-OSS at the platform layer — as joint calls rather than escalation resolutions | [First decision e.g., "Reliability posture for Q2: SLO floor 99.9%, error budget allocation 70/20/10"] |
| **CPO ↔ CRO (Commercial Motion Mix)** | Pricing exception authority, enterprise deal concession structure, expansion-motion design — against the customer-promise register | [First decision e.g., "Pricing exception threshold: discount above 25% requires CPO + CRO joint sign-off"] |
| **CPO ↔ CFO (Capital Envelope)** | Portfolio sequencing against the bet ledger, mid-cycle re-allocation triggers — decided before the board deck is written | [First decision e.g., "Mid-cycle re-allocation trigger: Bet X T+6 outcome miss > 30%"] |
| **CPO ↔ CMO (Brand-Calendar Boundary)** | Launch-tier classification (T1 / T2 / T3), corporate-narrative synchronization | [First decision e.g., "Q3 launch-tier classification: Bet A = T1, Bet B = T2"] |

These are not consultative pairings. They are the altitudes at which executive trust compounds or does not. An unnamed interface is one the organization narrates around by ad-hoc escalation; a named interface is one that carries its own cadence and its own record.

**Tier 1 (Pre-PLT) note**: Defer Move 4 entirely until at least three of the four counterparts (CTO, CRO, CFO, CMO) are seated as peers and the standing leadership forum holds joint decisions across the four altitudes. Naming interfaces that the organization has no peer-altitude counterpart for produces a slide, not an interface.

## Move 5 — Convert One Decision to a Commitment (Days 60-90)

**Window**: Days 60-90
**Output**: One Decision from the first Charter's output hardened into a Commitment by attaching a resource
**Install Action**: Pick a single Decision and harden it. The hardening forms below are the named ways the conversion happens.

**Forms of hardening** (pick one — multiple are stronger):

| Form | What it looks like |
|---|---|
| **Hire released** | A hire requisition opened or a candidate slated against the Decision. The Decision now drives recruiting. |
| **Funding moved** | Capital moved into the sequencing the Charter named, against the Bet Ledger. The CFO sees the move at quarter close. |
| **Sequencing locked** | A roadmap item moved out of "exploration" and into "committed quarter," with the dependencies named. |
| **External promise made** | A customer commitment, a board milestone, or a public delivery date that makes reversal costly. |

A roadmap item that triggered hiring is a Commitment. A slide in a deck is not. This is the move that converts the Charter from analysis into architecture. Without it, the Charter reads as a well-structured opinion. With it, the organization has committed to a direction that now carries consequences.

**Decision selected for hardening**: [Decision ID + name]
**Hardening form(s)**: [Hire released / Funding moved / Sequencing locked / External promise made]
**Resource attached**: [Specific resource — e.g., "Senior PM hire requisition #PM-203 opened"]
**Reversal cost**: [What it would cost to reverse the Commitment now]

## Move 6 — Install the Portfolio and Product-line Reviews (Days 60-90)

**Window**: Days 60-90 (concludes the quarter)
**Output**: Portfolio Review on the calendar; Product-line Review on the calendar; first re-decision trigger fires
**Install Action**: Cadence installed in named order with named gating inputs.

**Three cadences, in this order**:

1. **Portfolio Review** — Quarterly, 90 minutes, VP Product or CPO as owner. **Gating inputs**: Business Operations pre-read AND CI market read. If either pre-read is absent or stale, the review cannot adjourn with a continue decision on the bets those sensors cover.
2. **Product-line Review** — Monthly, 60 minutes, Group PM or Director PM as owner. Bet-level re-decision is the output. This catches over- and under-performance before it becomes a portfolio-review problem.
3. **Launch Readiness Review** — The first Charter's instantiation, rolled out to every material release on a T-6 / T-14 rhythm.

**Wire the observability**: Principle 8 names five signals on the operating layer itself, separate from signals on the bets inside it.

| Signal | What It Measures | Owner |
|---|---|---|
| Decision latency | Time from forum-entry to decision-recorded | ProdOps |
| Commitment drift | Variance between committed scope/timeline and current state | ProdOps |
| Cadence adherence | % of scheduled rituals running on time with full pre-reads | ProdOps |
| Charter decay | Time since last Charter review against named decay floor | ProdOps |
| Re-decision integrity | % of re-decision triggers that fire run as named events vs. ad-hoc conversations | ProdOps |

ProdOps operates these. The CPO consumes them at Portfolio Review. Do not collapse the two tiers — cadence adherence and charter decay are telemetry on the machinery ProdOps runs; share-of-decisions-with-measured-outcomes is a sensor read Business Operations delivers.

**The first re-decision**: Somewhere in this window, the first re-decision trigger should fire on an existing bet. Run it as a named event against the documented trigger, in the named forum, with the required inputs. **The first clean re-decision is the moment the operating system earns its license.**

| Cadence | First Run Date | Owner | Pre-Read Owner(s) |
|---|---|---|---|
| Portfolio Review | [Date] | [Role] | BizOps + CI |
| Product-line Review | [Date] | [Role] | PM-Director |
| Launch Readiness Review | [Date] | [Role] | PMM + Eng + ProdOps |
| First re-decision trigger | [Trigger + bet] | [Role] | [Pre-read owners] |

## Common Failure Modes (the Four)

Four failure modes capture new leaders in their first 90 days. Name them in the plan before they happen. The watch list is a living section: each move advances and the leader checks it for early signs of failure.

### Failure Mode 1 — Install-Everywhere-At-Once

**Pattern**: The new leader installs Charters on launch readiness, platform intake, pricing exceptions, and portfolio sequencing simultaneously in the first 60 days, runs out of organizational attention by Day 45, and ends with four half-installed charters nobody runs.

**Detection signals**:
- More than one Charter in the install plan inside the first 30-day window.
- Calendar shows three or more new recurring forums introduced in the same week.
- Direct reports report fatigue or cite "yet another new process" by Day 30.

**Recovery path**: Stop the second-Charter install in flight. Return to the sequencing rule — one Charter in the first 30 days, three by Day 90, not seven. Document the half-installed Charters as deferred, not abandoned.

### Failure Mode 2 — The CEO Who Doesn't Want a Decision System

**Pattern**: The CEO hired the leader to ship faster and reads the Week One state-of-the-decision-system note as evidence the leader is about to slow things down by adding process. The leader installs the system despite the CEO and is reversed at the first friction point.

**Detection signals**:
- CEO uses the word "process" pejoratively in feedback on the Week One note.
- CEO asks "when will you start shipping?" inside the first 14 days.
- CEO requests scope-tradeoff conversations to happen outside the first Charter's forum.

**Recovery path**: Install the first Charter on a decision the CEO cares about the **outcome** of, not the **process** of. If the first Charter's first re-decision produces a visibly better commercial outcome (revenue, retention, time-to-market), the CEO learns the system ships value. If the Charter is installed on process hygiene instead, the CEO learns the system is overhead. Pick the visible-commercial-outcome path.

### Failure Mode 3 — ProdOps Installed As Admin, Not Infrastructure

**Pattern**: At coordinator-altitude installation, ProdOps is seated as a scheduler and note-taker rather than as the function that runs the operating calendar, the archive, and the machinery telemetry. The role-block at scale puts ProdOps at director or VP level, not coordinator.

**Detection signals**:
- ProdOps owner has the title "Coordinator" or "Specialist" rather than Director / Senior PM / VP.
- ProdOps does not own the decision-record archive or the operating calendar.
- ProdOps cannot produce the five-signal observability layer (Move 6) because the seat does not have the mandate.

**Recovery path**: If the ProdOps seat is coordinator-altitude, install the Charter from the leader's own seat for the first quarter, and escalate the ProdOps mandate as a Q2 decision. Do not try to install the operating system from a coordinator-altitude ProdOps seat — the seat does not have the authority to hold the cadence.

### Failure Mode 4 — PLT Composition Without Empowerment-Director Empowerment

**Pattern**: The PLT exists on paper but the Business Operations and CI directors do not deliver sensor reads as gating inputs — they deliver them as slides in a PMM-narrated deck. The sensor read enters the room already narrative-washed. The Portfolio Review reaches a continue decision on a bet whose sensor reads would have forced a stop if they had landed as evidence.

**Detection signals**:
- BizOps pre-read for the Portfolio Review is delivered by PMM or a coordinator, not by the BizOps director.
- CI market read is paraphrased in a launch deck rather than presented as a standalone gating input.
- Continue decisions on bets whose sensor reads, presented neutrally, would have triggered a stop or restructure.

**Recovery path**: Apply the structural fix from Appendix A — sensor reads are gating inputs, not consultative commentary. The empowerment-director (BizOps for economic signal, CI for market signal, VR for customer-outcome signal) must deliver the read directly to the decision. If the empowerment-director cannot, the Charter is not installed. Re-seat the role or escalate the mandate.

## Quarter 1 Close Checklist

By Day 90, the install plan succeeds when:

- [ ] One Decision Interface Charter installed and run cleanly twice (Move 2)
- [ ] PLT seated at director altitude across the seven default seats (Move 3) — Director-Span Constraint passed
- [ ] Four CPO-counterparty interfaces named, with at least one recorded decision per interface (Move 4) — Tier 3 only; Tier 2 may have 2-3; Tier 1 deferred
- [ ] One Decision hardened into a Commitment by attaching a resource (Move 5)
- [ ] Portfolio Review and Product-line Review on the calendar, with gating pre-reads from BizOps and CI (Move 6)
- [ ] First re-decision trigger fired and run as a named event against the documented threshold (Move 6) — this is the moment the operating system earns its license
- [ ] Four failure modes monitored on a watch list throughout the quarter, with detection signals named and recovery paths recorded if any pattern surfaced
- [ ] First Outcome Review run at Day 90 — T+6 / T+12 checkpoints fire on older bets; Value Realization's signature-decision authority operationalizes (bet-invalidation calls as named decisions, not research exercises)

## Related Skills

- `/decision-charter` — The Charter installed in Move 2 (and expanded in Move 5). The output of this skill names a Decision Interface Charter; the install plan is the sequencing rule for getting the first one in cleanly.
- `/maturity-check` — Diagnoses the organization's tier (Three Tiers) and confirms which moves apply at the reader's stage. Pair this skill with `/maturity-check` when classifying the entry checkpoint.
- `/strategic-intent` — Move 5's Commitment hardening is most durable when it ties to a documented strategic intent.
- `/scale-check` — The Director-Span Constraint applies to every seat seated in Move 3.
- `/decision-record` — Every decision the first Charter produces should be recorded as a `/decision-record` entry.
- `/decision-quality-audit` — At Q1 close, the first Outcome Review feeds `/decision-quality-audit` for the first quarterly read on Decision Improvability.
- `/escalation-rule` — The Decision Frame Requirement applies the moment the first Charter starts handling escalations.

## When to Use

- A newly-seated CPO, VP Product, or Director of Product Operations is about to begin their first quarter
- A leader who has been seated for 1-2 weeks is about to install Charters everywhere at once and needs the sequencing rule
- A Tier 2 (PLT-emerging) organization is graduating from the compressed Charter to the full Appendix A version

## When NOT to Use

- The organization is pre-PMF and the standing leadership forum has not yet stabilized — the principles still apply but the install plan does not yet
- The Tier 3 install is already complete and the question is retuning, not installing — use `/scale-check` or `/maturity-check` instead
- The leader has been seated for more than two quarters — the install window has closed; the right skill at that point is `/maturity-check` followed by a re-decision against the running install

## Operating Principle

> "Installation is core-tier work. A new leader's first quarter is about sequencing, not standing — and the right first move is to change nothing at all in Week One."
