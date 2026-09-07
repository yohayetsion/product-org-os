# Prioritization Frameworks — V2V OS pack on RICE / ICE / Weighted Scoring / MoSCoW / Kano / Opportunity Solution Trees

**Adapted from**:
- Industry-standard prioritization frameworks: Intercom "RICE" (Sean McBride), "ICE" (Sean Ellis), MoSCoW (DSDM), Kano model (Noriaki Kano 1984), Opportunity Solution Tree (Teresa Torres)
- 2026 Q2 PM landscape per V2V refresh survey §4 — deanpeters/Product-Manager-Skills (47 skills, 4.3k stars), Anthropic PM Plugin patterns

**Source licence**: Public methodology references
**V2V refinements**: Prioritization framed as Phase-3 Commitments activity (the conversion from Phase-2 Decisions into ordered execution); cross-references to roadmap-item + roadmap-theme skills + business-case methodology

---

## 1. Purpose

This pack equips `product-manager` and `director-product-management` with the working set of prioritization frameworks used in product organizations. It is reference knowledge, not a workflow skill: it explains what each framework is for, when to use it, when not to use it, and how each one breaks down in practice. The honest weakness assessments matter more than the formulas — every framework here is regularly misapplied, and the failure modes are well-documented.

The V2V refinement is the framing: prioritization is the **conversion of decisions into ordered execution**. It is a Phase-3 (Commitments) activity, not a Phase-2 (Decisions) activity. You do not run a RICE score to decide whether to do something; you decide first, then prioritize against agreed criteria. Mixing the two is the most common abuse of these frameworks — using RICE to launder a decision that should have been debated explicitly, or using MoSCoW to relitigate strategic intent under the cover of "scope."

---

## 2. When to Prioritize vs. When Not To

**Prioritize when**:
- You have a backlog of comparable items (features, fixes, opportunities) that compete for the same scarce capacity
- The items have been decided in principle (someone owns them, they fit the strategy) but ordering is open
- Stakeholders disagree on order and need a defensible basis for the call
- A release scope needs to be drawn through items already approved in principle

**Do NOT use a formal prioritization framework when**:
- **You have 1-3 items.** Just decide. The framework overhead exceeds its yield. Pick, document the reasoning, move.
- **The item is a strategic bet.** Strategic bets are irreversible commitments with multi-year payoff horizons. They do not belong in a RICE score next to a UI tweak. Use the `/strategic-bet` skill; the comparison set is the portfolio, not the backlog.
- **The item is regulatory or safety must-do.** There is no scoring needed. It is required. Score the implementation approach if you must, but not the doing-or-not-doing.
- **The item is a founder/exec mandate.** Either debate the mandate openly or accept it. Do not score around it — that is consensus-theatre and corrodes trust.
- **Tech debt that compounds.** Generic prioritization underprices it. Use a technical-debt-economics lens (carrying cost, optionality cost, rate of compounding) rather than RICE.

The biggest single failure mode in PM prioritization is reaching for a framework when the actual problem is undecided intent. If the team cannot articulate the outcome the item is serving, no scoring framework will help — you need a Decision Record, not a score.

---

## 3. RICE (Reach × Impact × Confidence ÷ Effort)

**Formula**: `RICE Score = (Reach × Impact × Confidence) ÷ Effort`

**Dimensions**:
- **Reach** — how many users/customers the item affects per time period (e.g., users per quarter). Concrete number.
- **Impact** — quasi-quantitative scale per person reached: 0.25 (minimal) / 0.5 (low) / 1 (medium) / 2 (high) / 3 (massive). The discrete buckets are intentional — they suppress fake precision.
- **Confidence** — confidence in your Reach and Impact estimates: 100% / 80% / 50% / 20%. Below 20% the item probably belongs in discovery, not prioritization.
- **Effort** — person-months (or person-weeks for tighter scope). Must include engineering input; PM-only effort estimates are unreliable.

**Example**:

| Item | Reach (users/qtr) | Impact | Confidence | Effort (person-months) | RICE |
|---|---|---|---|---|---|
| Onboarding redesign | 5,000 | 2 | 80% | 3 | 2,667 |
| Bulk-export | 10,000 | 1 | 50% | 2 | 2,500 |
| AI-summary feature | 2,000 | 3 | 100% | 1 | 6,000 |

**Strengths**:
- Forces explicit effort estimation, which exposes hand-waving
- Comparable across teams when calibrated
- Confidence dimension surfaces what we don't know

**Weaknesses**:
- **False precision.** A score of 2,667 vs. 2,500 reads as "Onboarding wins" but the input uncertainty is wider than the score gap.
- **Gameable.** Reach is often estimated; Impact buckets are subjective; Confidence is wishful; Effort is optimistic. Any one of these can be tilted to favor a preferred item.
- **Strategic alignment invisible.** A high-RICE item that drifts from strategy still wins. Pair RICE with explicit theme/bet alignment, not as a substitute for it.
- **One-time work penalized vs. broad-reach work.** RICE structurally favors mass-market features over high-value-narrow features (e.g., enterprise unblockers).

---

## 4. ICE (Impact × Confidence × Ease)

**Formula**: `ICE Score = Impact × Confidence × Ease`, each scored 1-10.

**When to use**: Early-stage triage where Reach is unknown or irrelevant (e.g., experiments, growth-loop bets, internal tools).

**When NOT to use**: Scaled products where Reach is the differentiating variable. ICE collapses to "things that feel good and easy," which is the opposite of strategic prioritization.

**Strengths**: Faster than RICE. Lower-overhead. Good for batches of 20-50 candidate experiments.

**Weaknesses**: Heavily subjective. Without scoring calibration (e.g., "what does Impact=8 mean concretely?") two PMs will score the same item three points apart. The discussion is the value; the number is the byproduct.

---

## 5. Weighted Scoring (custom criteria)

**When to use**: You have multiple incomparable axes (strategic fit, customer pain, revenue, technical debt, competitive necessity) and need a single ordering. Common in roadmap reviews where leadership wants to see how priorities were derived.

**How to build**:
1. Select 4-7 criteria. Fewer than 4 collapses to RICE-with-extra-steps; more than 7 dilutes weight.
2. Assign weights summing to 100%. **The weight conversation is the strategic conversation.** If you cannot get the leadership team to agree on the weights, you don't have a prioritization problem, you have an alignment problem.
3. Score each item 1-5 per criterion.
4. Sum (score × weight) per item.

**Example**:

| Criterion | Weight | Item A score | Item A weighted | Item B score | Item B weighted |
|---|---|---|---|---|---|
| Strategic fit | 30% | 4 | 1.20 | 3 | 0.90 |
| Revenue impact | 25% | 3 | 0.75 | 5 | 1.25 |
| Customer demand | 20% | 5 | 1.00 | 2 | 0.40 |
| Tech feasibility | 15% | 2 | 0.30 | 4 | 0.60 |
| Competitive table-stakes | 10% | 3 | 0.30 | 4 | 0.40 |
| **Total** | **100%** | | **3.55** | | **3.55** |

(The tie above is realistic; weighted scoring produces ties more often than people expect, which is itself useful information.)

**Strengths**: Customizable. Team-owned. The criteria choices are documented, so future audits can ask "did our weights match what we said we cared about?"

**Weaknesses**:
- **Weight assignment is political.** Whoever controls the weights controls the outcome. This is not a bug; it's the feature — but pretend otherwise at your peril.
- **Recency bias.** PMs score the item they just saw demoed higher than the one from last quarter, regardless of true merit.
- **Pseudo-objectivity.** A weighted score reads more rigorous than it is. State explicitly: "this score is a decision-support tool, not a decision."

---

## 6. MoSCoW (Must / Should / Could / Won't)

**When to use**: Scope-bounded delivery — release planning, sprint commitment, fixed-deadline launches.

**Categories**:
- **Must** — release fails if missing. Hard constraint.
- **Should** — important but not blocking; include if capacity allows
- **Could** — nice to have; trade-out candidates
- **Won't** — explicitly out of scope (the most underused category)

**Strengths**: Surfaces what's actually in scope. The "Won't" column is the underrated one — explicit out-of-scope statements prevent the slow scope creep that kills releases.

**Weaknesses**:
- **Must-inflation.** Everyone calls everything Must. Without a forced ratio (rule of thumb: Must ≤ 60% of available capacity, ideally 50%), MoSCoW degenerates to a one-column list.
- **Does not order within category.** Says nothing about which Must to build first.
- **Stakeholder gaming.** Sales says feature X is a Must to close a deal; the deal closes without X. Document the "Must" assertion's basis in writing.

**Facilitation rule**: For every "Must" claim, ask "If we ship without this, what specifically fails?" If the answer is hedged ("customers might be unhappy"), it's a Should.

---

## 7. Kano Model (Noriaki Kano)

**Five categories**:
- **Must-Have (Basic)** — expected. Presence creates no satisfaction; absence creates strong dissatisfaction. Example: a shopping cart on an e-commerce site.
- **Performance (One-Dimensional)** — satisfaction scales linearly with implementation. Example: page-load speed, storage quota.
- **Delighter (Attractive)** — unexpected. Absence creates no dissatisfaction; presence creates disproportionate delight. Example: a clever onboarding moment that saves the user time on day 1.
- **Indifferent** — users don't care. Investment is wasted.
- **Reverse** — some users actively dislike the feature. Removing it improves satisfaction.

**Survey methodology**: Paired question per feature. (a) Functional: "How would you feel if this feature were present?" (b) Dysfunctional: "How would you feel if this feature were absent?" Five-point scale on each: "I like it / I expect it / I am neutral / I can tolerate it / I dislike it." Cross-reference using Kano's evaluation table to classify.

**When to use**: Feature-set design for v1 launches; competitive table-stakes assessment; portfolio decisions about where to invest delight-level effort vs. baseline coverage.

**Strengths**: Catches "delighter" investments that disproportionately move NPS and word-of-mouth. Surfaces the hygiene-vs-delight tradeoff explicitly. Forces the team to admit that some "performance" features are actually just hygiene with no upside.

**Weaknesses**:
- **Requires survey infrastructure.** Without real customer data, Kano is just guesswork in formal clothing.
- **Longitudinal drift.** Yesterday's Delighter becomes today's Performance feature becomes tomorrow's Must-Have. The Kano classification is a snapshot. Re-run periodically.
- **Sample-size sensitivity.** Small samples give noisy classifications. Need 30+ responses per feature for stable classification.

---

## 8. Opportunity Solution Tree (Teresa Torres)

**Structure**:
```
Desired Outcome
   └── Opportunity 1
   │      ├── Solution A
   │      │     └── Experiment / Test
   │      └── Solution B
   └── Opportunity 2
          └── ...
```

**When to use**: Continuous discovery; problem-space exploration; multi-team alignment on the opportunity space behind an outcome.

**The core discipline**: Every solution traces back to a problem; every problem traces back to the outcome. PMs own the problem-space (which opportunities matter); the team co-owns the solution-space (which solutions to try).

**Strengths**:
- Forces traceability. No more "we built X because someone asked for X" — every shipped solution must point back to an opportunity, and every opportunity must point back to an outcome.
- Surfaces opportunity gaps. If the same opportunity has only one candidate solution, you have a discovery gap, not a prioritization problem.
- Aligns multiple teams against the same outcome with visibility into who's exploring what.

**Weaknesses**:
- **Requires discovery discipline.** OST works when there is real ongoing customer research. Without it, the tree degenerates into solutions-with-pseudo-problems retro-fitted to look like an OST.
- **Outcome quality determines tree quality.** A vague outcome ("improve user satisfaction") yields a useless tree. Outcomes need to be specific and measurable.
- **Not an ordering mechanism per se.** OST helps you see the space; it does not by itself tell you which experiment to run first. Pair with ICE or RICE for ordering within branches.

---

## 9. Cost of Delay / WSJF (Weighted Shortest Job First)

**Formula**: `WSJF = Cost of Delay ÷ Job Duration`

Cost of Delay typically decomposed as: `User-business value + Time-criticality + Risk-reduction & opportunity-enablement`.

**When to use**: Agile portfolios with shared backlog under capacity constraint. Used in SAFe (Scaled Agile Framework) and Lean Agile programs.

**Strengths**:
- Captures the "what happens if we wait" dimension that RICE flattens
- Supports continuous-flow scheduling rather than batch quarterly planning
- Time-criticality term forces explicit reasoning about deadline-sensitive items (regulatory windows, competitive moves, market events)

**Weaknesses**:
- **Cost of Delay is itself estimated.** Each of the three CoD components is a subjective integer (usually Fibonacci-scaled: 1, 2, 3, 5, 8, 13, 20). The framework gives an air of rigor but rests on the same kinds of educated guesses as RICE.
- **Heavy SAFe context.** WSJF is most useful in organizations that have adopted the broader Lean-Agile portfolio model. Bolting it onto an otherwise traditional org creates ceremony without yield.
- **Duration estimation collapses to story points.** Which means CoD/Duration is "value-feel divided by effort-feel" — i.e., a more expensive ICE.

---

## 10. Anti-Frameworks: When NOT to Use ANY Formal Prioritization

The most-overlooked category. Formal frameworks are tools, and tools have non-applicable domains.

- **Strategic bets** — irreversible, portfolio-changing commitments need a different process. Use `/strategic-bet`. Scoring a strategic bet against a feature in the same backlog is a category error.
- **Regulatory and safety must-dos** — no scoring. They are required. Move directly to implementation prioritization.
- **Compounding tech debt** — generic frameworks underprice it. The cost grows over time, and the discount rate is wrong. Use a technical-debt-economics lens (carrying cost over horizon × probability of forced refactor).
- **Founder / exec mandates** — debate the mandate openly or accept it. Pretending to "score" it is consensus-theatre.
- **Sequence-locked items** — when item B cannot begin until item A ships, ordering them is meaningless. Treat as a single bundle and prioritize the bundle.
- **Items still in discovery** — if Confidence would be below 20% in RICE, the item belongs in discovery, not prioritization. Move it.

When a PM reaches for a framework reflexively, ask: "Is the question really 'in what order?' or is the question 'whether?'" Those are different questions and frameworks confuse them.

---

## 11. Common Prioritization Failures

Per-framework Weaknesses sub-bullets above call out failure modes specific to each technique. The failures below are cross-framework — they recur regardless of which scoring system the team has nominally adopted. They are the real reason prioritization rituals go sideways.

- **Scoring to launder undecided intent.** The team has not actually decided whether to do the item; the framework gets reached for as a way to avoid the harder conversation. The score becomes the "answer," which is consensus-theatre dressed up as rigor. Treatment: if the team cannot articulate the outcome the item serves, the deliverable is a Decision Record, not a score. Send it back to Phase 2.

- **Recency bias in scoring.** The item most recently demoed, raised in a customer call, or escalated by sales scores higher than items from earlier in the quarter, independent of merit. PMs are not immune to this; calibration sessions are. Treatment: re-score the top 10 from last quarter alongside this quarter's candidates before publishing the order.

- **Framework-as-political-cover.** Whoever controls the weights (in Weighted Scoring) or the bucket definitions (in Kano, MoSCoW) controls the outcome. This is not a bug to be eliminated — weight assignment IS the strategic conversation. But it gets pretended away. Treatment: state explicitly in the ranked output: "These weights were set by [decision-maker / forum] on [date]. Re-deciding weights re-opens the order."

- **Score-bloat (all items 4-5).** When everything scores 4 or 5 on every criterion, the framework has lost discriminating power and is producing noise. Either the criteria are too generic to differentiate the items, or PMs are inflating scores to protect their own items. Treatment: enforce forced distribution per cohort (e.g., no more than 30% of items can score top-bucket on any one criterion) OR re-cut the criteria until real differentiation surfaces.

- **One-time prioritization.** The team scores the backlog once at quarter-start, then treats the output as locked. Reality shifts — items deprioritized in week 1 may matter more by week 6, and items at the top may lose Confidence as discovery progresses. Treatment: re-running the framework on a regular cadence (every 4-6 weeks for a quarterly cycle) is part of the discipline, not a sign that the original prioritization "failed."

These five recur across every framework in this pack. They are the reason the per-framework weaknesses bite — the framework's specific failure mode (e.g., RICE's false precision, MoSCoW's Must-inflation) compounds with the cross-cutting failure (e.g., recency bias) and yields an output that looks rigorous and is wrong. Treat the framework's algebra as decision-support; treat these five as the watch-list.

---

## 12. 2026 Landscape

Three shifts in the 2026 PM tooling and methodology landscape are changing how prioritization works at the margins. None of them invalidate the frameworks above — but each one moves where the framework boundary should sit.

- **AI-tooling has cheapened experimentation.** A few years ago, running a small test cost more than scoring the item against RICE or ICE; the framework was the cheap path and the experiment was the expensive one. With AI-assisted prototyping, feature-flag platforms, and synthesis tools, the cost curve has flipped on a meaningful subset of items. When the experiment costs less than the scoring conversation, the right move is to skip the framework for high-uncertainty items and route them straight to a small experiment. Use ICE for the experiment-design triage (which 5 of 30 to actually run) rather than for the build-or-not call. Cross-reference: `discovery-methods` pack §11 covers the discovery-tooling side of this same shift.

- **AI-assisted research synthesis raises the bar on Confidence inputs.** Tools like Dovetail and Reduct now ship AI-features that synthesize interview transcripts, tag themes at scale, and surface cross-customer patterns in hours rather than weeks. When synthesis is cheap, the Confidence dimension in RICE (or its analog in ICE/Weighted Scoring) implicitly assumes you have actually done discovery. A Confidence-80% score should now be backed by real synthesis, not by vibe. PMs who continue to score Confidence high without the underlying synthesis are exposing themselves — the gap between "looks rigorous" and "is rigorous" widened in 2026.

- **Open-source PM skill libraries are direct peers, not adjacent tools.** Per V2V refresh survey §4: `deanpeters/Product-Manager-Skills` (47 skills, 4.3k stars, v0.79 May 2026) is the closest peer to V2V's `prioritization` pack — overlapping framework coverage (RICE, ICE, MoSCoW, Kano, OST, WSJF) and similar agent-augmentation framing. The Anthropic PM Plugin pattern (and similar vendor-PM templates) defaults to RICE for prioritization decisions. V2V's structural difference from both is two-pronged: (a) Phase-3 (Commitments) anchoring — prioritization is the conversion of decided items into ordered execution, NOT the place where decision-or-not happens (the deanpeters pack and the Anthropic default both treat scoring as a decision tool, which conflates the two activities); (b) mandating WHEN to NOT use any formal framework (§10 Anti-Frameworks above). The differentiation has held in real use, but it requires that the team actually internalize the Phase-3 framing — not just adopt the templates.

For high-stakes items where AI-cheapened experimentation is insufficient (irreversible commitments, multi-team dependencies, regulatory-adjacent scope), `business-case` remains the right next step — a one-page business case forces explicit reasoning about value, cost, and counterfactual that a RICE score elides. The 2026 shift makes experimentation cheaper for the bottom half of the backlog; it does not make business cases obsolete for the top.

---

## 13. V2V Cross-References

Prioritization is a Phase-3 (Commitments) activity in the Vision to Value model. The decision-already-made flows from Phase-2 (Decisions); the executable plan flows into Phase-4 (Execution). Use these adjacent V2V skills:

| Skill | Use |
|---|---|
| `roadmap-item` | Defining a single roadmap entry with scope, dependencies, and success criteria |
| `roadmap-theme` | Grouping prioritized items into a thematic roadmap section |
| `product-roadmap` | Publishing the full roadmap document — the prioritization output's home |
| `business-case` | High-stakes items earn a business case, not just a RICE score |
| `strategic-bet` | Portfolio-changing bets — out of scope for backlog prioritization |
| `decision-charter` | Recurring prioritization calls (e.g., quarterly roadmap review) need a Decision Interface Charter naming the decider, inputs, escalation path |
| `decision-record` | Every material prioritization call should leave a Decision Record so the rationale survives the people who made it |
| `prioritize-features` | The workflow skill that operationalizes RICE/ICE/MoSCoW for a specific backlog |
| `kano-analysis` | The standalone Kano workflow skill — survey design, evaluation table, classification |
| `commitment-check` | Pre-commitment gate before shipping the prioritized list as a plan |
| `phase-check` | Phase 2→3 transition verification |

The skill-vs-pack distinction: **this pack is reference**. The skills above are the active workflows that consume this reference. When `product-manager` or `director-product-management` runs `/prioritize-features`, the skill produces a deliverable; this pack supplies the conceptual scaffolding the skill assumes.
