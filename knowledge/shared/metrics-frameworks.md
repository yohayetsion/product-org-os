# Metrics Frameworks

**V2V OS pack on North Star Metric, HEART, AARRR / Pirate Metrics, KORE Score, metric trees, and Value Score (Health Score → Value Score evolution).**

---

## Attribution

**Adapted from**:
- North Star Metric (Sean Ellis / GrowthHackers, "The One Metric That Matters," 2010) — public methodology
- HEART (Google — Happiness / Engagement / Adoption / Retention / Task Success — Kerry Rodden, Hilary Hutchinson, Xin Fu, "Measuring the User Experience on a Large Scale," CHI 2010)
- AARRR / Pirate Metrics (Dave McClure, "Startup Metrics for Pirates," 2007 — Acquisition / Activation / Retention / Referral / Revenue)
- RARRA reordering (Andrew Chen, "New Mobile App Metrics," 2017 — retention-first reframe of AARRR)
- OKRs (Andy Grove, *High Output Management*, 1983; John Doerr, *Measure What Matters*, 2018; Christina Wodtke, *Radical Focus*, 2016)
- Metric trees (Aakash Gupta / Reforge popularization, 2024-2026; root pattern traces to system-dynamics influence diagrams)
- TSIA *State of Customer Success 2026* — Value Score framework (Health Score → Value Score evolution; the operational design lives in the planned `value-score-design` pack — this pack frames the strategic shift only)
- 2026 Q2 PM landscape per V2V refresh survey §4 — KORE Score, Resolution Durability; survey §16 — Customer Success metric retirement

**Source licence**: Public methodology references; no license restriction on summary + framework attribution.

**V2V refinements**:
- Joint authoring (`vp-product` strategic-bet lens + `value-realization` customer-outcome lens). Metrics-as-decisions belong to neither seat alone.
- Metrics framed as Phase-2 Decisions artifact. The NSM is the strategic-bet's success metric, not a dashboard line item.
- Cross-references to `value-score-design` (planned Q2-4 pack), `customer-value-trace`, `outcome-review`, `strategic-bet`, `north-star-metric`, `pirate-metrics`, `heart-metrics`, `value-realization-report` skills.
- 2026 landscape additions: KORE Score, Value Score (replacing Health Score), Resolution Durability, AI-citation rate, per-spawn cost, per-seat-pricing structural failure.

---

## Joint-Authoring Lens

Metrics sit at the intersection of **strategic intent** (which metric does this bet move? what does success look like before we ship?) and **customer outcome** (did the customer actually realize value? is adoption a leading indicator that the bet is paying off?). Neither seat owns metrics alone:

- **`vp-product`** brings: NSM-as-strategic-bet output, metric tree structure that translates strategy into team-level objectives, counter-metrics that prevent Goodhart's Law, re-decision thresholds tied to specific metric movements, OKR architecture across the portfolio.
- **`value-realization`** brings: outcome-vs-output distinction, adoption curve analysis, success-metrics-defined-before-launch discipline, Value Score design, customer-value-trace from NSM down to individual account outcomes, HEART and AARRR operational application.

The V2V principle: **a metric without a decision attached is a dashboard line item, not a metric**. Every metric in this pack should answer "what would we do differently if it moves?". A movement without a pre-committed action is a vanity signal. When you read this pack, carry both lenses: the strategic question (which bet does this measure?) and the outcome question (did customers actually realize value?). A metrics recommendation that only frames strategy is incomplete. A metrics recommendation that only tracks adoption without strategic context is incomplete. The deliverable carries both, or it goes back.

---

## 1. North Star Metric (NSM)

**Definition**: The single metric that best captures the value your product delivers to customers, frequently enough to serve as the team's primary compass.

**Three properties** (per Sean Ellis):
1. **Captures value delivered** — measures the customer outcome, not the company's internal activity
2. **Leading indicator** — correlates with long-term retention and revenue, but moves faster than either
3. **Behavior-anchored and ownable** — the product team can directly influence it through the work they ship

**Examples by product type**:

| Product | North Star Metric | Why it works |
|---------|-------------------|--------------|
| Spotify | Time spent listening | Engagement → retention → subscription continuation |
| Airbnb | Nights booked | Captures both supply (listings) and demand (bookers) |
| Slack | Daily active users sending ≥X messages in a workspace | Single-user accounts don't reflect collaboration value |
| Notion | Active workspaces with ≥5 collaborators | Distinguishes team value from solo notebook use |
| Zoom (peak 2020) | Annualized meeting minutes | Captures both new-user adoption and existing-user depth |
| Figma | Multiplayer files edited per week | Differentiates Figma from single-user design tools |

**When to use**: Always, for any product team. The NSM is the strategic frame; downstream metrics ladder up to it. A team without an NSM is a team optimizing in different directions.

**When NOT to use as the only metric**: NSM doesn't replace operational health metrics (uptime, P99 latency, login success rate). It complements them. A product can have a healthy NSM trajectory while operationally breaking; both views are needed.

**V2V framing**: The NSM is the Phase-2 Decisions output of a strategic bet. The bet says "we believe X will produce Y for customers." The NSM is how we measure Y. If you can't name the NSM, the bet isn't a bet — it's a wish.

**Common pitfalls**:
- Picking an internal metric (revenue, signups) as NSM — these are lagging, not leading
- Picking a metric the team can't influence (e.g., "market share" — depends on competitor moves)
- Letting NSM drift into vanity (e.g., "page views" instead of "engaged sessions")
- Failing to define a counter-metric (see §10)

---

## 2. Metric Trees

**Definition**: A causal hierarchy translating the NSM into input metrics, then into team-owned driver metrics. Each leaf is a metric a specific team owns and can move with the work they ship.

**Why it matters**: An NSM without a tree is a wall-poster. The tree is what makes the NSM actionable across an organization. Aakash Gupta and Reforge popularized the pattern in 2024-2026 product circles; the underlying structure traces to system-dynamics influence diagrams.

**Tree structure**:

```
                                NSM
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
          Input 1            Input 2            Input 3
              │                  │                  │
         ┌────┴────┐         ┌───┴───┐          ┌───┴───┐
         │         │         │       │          │       │
       Driver  Driver     Driver  Driver     Driver  Driver
       (Team A) (Team B) (Team A) (Team C)  (Team B) (Team C)
```

**Example tree for a B2B SaaS (NSM = Weekly Active Teams with ≥5 members sending ≥10 messages):**

| Level | Metric | Owner |
|-------|--------|-------|
| NSM | Weekly Active Teams (5+ members, 10+ messages) | Whole product org |
| Input | New teams reaching activation threshold per week | Onboarding squad |
| Input | Existing teams sustaining activation week-over-week | Retention squad |
| Driver | % of new signups completing guided setup in week 1 | Onboarding squad |
| Driver | Average messages-per-member in week 2 | Engagement squad |
| Driver | Integrations connected per team | Platform squad |
| Driver | Weekly invite-rate per existing team | Growth squad |

**When to use**: Any time you need to translate strategy into team-level metrics, especially in orgs with ≥3 product teams. The tree resolves "what does my team's work have to do with the company NSM?".

**Common pitfalls**:
- Trees that don't actually causally connect (NSM correlated with input, but no mechanism)
- Trees with leaf metrics no one owns (purely descriptive — produces blame, not action)
- Trees that are too deep (5+ levels) — teams lose the line of sight
- Treating the tree as a permanent artifact instead of a hypothesis (the tree's causal claims should be tested and revised)

**V2V cross-reference**: The metric tree is the bridge from strategic-bet (Phase 2) to team-level commitments (Phase 3). If a team's commitment doesn't ladder to a leaf in the tree, it's strategically disconnected.

---

## 3. HEART Framework

**Source**: Kerry Rodden, Hilary Hutchinson, Xin Fu — "Measuring the User Experience on a Large Scale" (Google, CHI 2010).

**Five dimensions**:

| Dimension | What it measures | Example metrics |
|-----------|------------------|-----------------|
| **Happiness** | Subjective user sentiment | NPS, CSAT, SUS, app store rating, survey responses |
| **Engagement** | Depth of interaction | Sessions per user per week, actions per session, time-in-product |
| **Adoption** | New users + new feature use | Weekly new signups, feature first-use rate, upgrade-tier rate |
| **Retention** | Returning users | DAU/MAU, 30-day cohort retention, monthly active user retention curve |
| **Task Success** | Did the user complete what they came to do? | Completion rate, time-on-task, error rate |

**Goals-Signals-Metrics structure**: For each dimension, define the Goal (what you want to achieve), Signals (user behaviors indicating progress), and Metrics (specific measurable quantities). Rodden's discipline is the structured G-S-M mapping, not just the five dimensions.

**When to use**:
- UX-heavy products where user experience IS the product (consumer apps, design tools, content platforms)
- Specific feature evaluation post-launch
- Products where adoption and retention are leading indicators of revenue

**When NOT to use** (or use partially):
- Enterprise B2B sales-led products where buyer ≠ user (HEART assumes self-serve usage; in many B2B products, an admin buys and end users are mandated to adopt — Happiness/Adoption don't map cleanly)
- Compliance or back-office products where users have no choice (Task Success matters; Happiness and Engagement are noise)
- Early-stage products without enough usage volume for stable metrics

**Common pitfalls**:
- Tracking all five dimensions equally — most products genuinely care about 2-3
- Metric overload (5+ metrics per dimension) — focus on 1-2 per dimension
- Confusing Happiness with NPS-only — Happiness is broader (surveys, ratings, qualitative)

**V2V cross-reference**: `/heart-metrics` skill is the operational authoring workflow.

---

## 4. AARRR / Pirate Metrics

**Source**: Dave McClure, "Startup Metrics for Pirates," 2007.

**Five funnel stages**:

| Stage | Question | Example metrics |
|-------|----------|-----------------|
| **Acquisition** | How do users find us? | Traffic by channel, signup rate, CAC by channel |
| **Activation** | Did the first experience deliver value? | Onboarding completion, time-to-first-value, "aha moment" rate |
| **Retention** | Do users come back? | DAU/WAU/MAU, retention curves, churn rate |
| **Revenue** | Do users pay? | Free-to-paid conversion, ARPU, MRR, expansion revenue |
| **Referral** | Do users tell others? | Viral coefficient, NPS, organic-share-of-signups |

**When to use**:
- PLG funnel design and diagnosis
- Growth-team operating cadence
- Identifying the leakiest stage to prioritize (rule: fix the biggest leak first, generally right-to-left — Retention before Acquisition)

**Modern complement — RARRA** (Andrew Chen, 2017): Retention / Activation / Referral / Revenue / Acquisition. The reordering reflects the post-2015 insight that retention is the most leveraged stage (a leaky bucket cannot be filled by faster pouring). Mobile/consumer products especially are RARRA-shaped.

**When NOT to use**:
- Enterprise B2B sales-led products — the funnel is more like Awareness → MQL → SQL → Opportunity → Closed-Won, not AARRR
- Products with non-linear journeys (e.g., marketplaces with bidirectional supply/demand)
- Internal tools (no Acquisition or Referral concepts)

**V2V cross-reference**: `/pirate-metrics` skill is the operational AARRR application workflow.

---

## 5. KORE Score

**Source**: Per V2V refresh survey §4 — emerging 2025-2026 customer-outcome metric in TSIA-influenced CS practice.

**Definition**: KORE Score is a composite customer-outcome metric integrating:
- **K** — known objective achievement (is the customer hitting the outcomes they bought the product to achieve?)
- **O** — operational engagement (are they actively using it in a way consistent with the value model?)
- **R** — renewal probability (model-driven prediction of renewal, not just historical health-score correlation)
- **E** — expansion potential (signals that the account is ready for upsell/cross-sell)

**Why it's emerging**: Traditional Health Scores correlate with renewal historically but not predictively — they tell you the patient was alive yesterday. KORE-style scores attempt to forecast outcome AND objective achievement, not just survival.

**When to use**: Mid-to-late-stage SaaS with enough customer history to model objective achievement and renewal patterns. Requires explicit "what objectives is this customer here to achieve?" data — usually from sales handoff + early CS conversations.

**When NOT to use**: Early-stage products without enough renewal history to model. Self-serve products where there's no formal "objective set" per account.

**V2V cross-reference**: The planned `value-score-design` pack (Q2-4) will author the operational design. This section frames KORE as the strategic shift away from Health Score.

---

## 6. Value Score — Health Score Retirement

**Source**: TSIA *State of Customer Success 2026* (per V2V refresh survey §16 + §3).

**The retirement**: Health Score has been the dominant CS leading indicator since ~2015. TSIA's 2026 consensus: Health Score is structurally insufficient for the AI era. The reasons:

1. **Health Score ≈ "they're still alive"** — usage telemetry tells you the account is logging in. It does not tell you whether the account is achieving the strategic outcome they bought for.
2. **Health Score is product-centric, not outcome-centric** — a customer can be heavy users of features that don't deliver the outcome they bought. Score green, churn imminent.
3. **Per-seat pricing degradation** — AI products are cutting headcount in customer organizations. Per-seat ARPU degrades even as outcome value grows. Health Score (often correlated with seat count and login frequency) becomes a misleading signal.
4. **Renewal probability ≠ login frequency** — modern AI-driven CS uses conversation data (CSM notes, support tickets, exec sponsor calls, deal-cycle signals) to forecast renewal. Health Score's usage-only signal is too narrow.

**Value Score definition**:

$$\text{Value Score} = \text{renewal probability} \times \text{objective achievement} \times \text{strategic value index}$$

- **Renewal probability**: model-driven (logistic / gradient-boosted), trained on historical renew/churn outcomes with usage + conversation + commercial features
- **Objective achievement**: explicit measurement against the objectives set at sales handoff and refreshed quarterly
- **Strategic value index**: account's strategic importance to the vendor (logo value, expansion potential, reference value, market signal value)

**Dynamic objective-mapping**: Objectives change over the customer lifecycle. A customer who bought to "consolidate three tools" in year 1 may, in year 2, be focused on "extend to two new business units." Value Score must reflect the current objectives, not the founding objectives. Refresh cadence: quarterly minimum, ideally per-QBR.

**AI-driven scoring**: 2026 Value Score implementations pull from unstructured data (CSM call transcripts, support tickets, exec sponsor emails, deal-cycle signals) — not just product usage telemetry. The shift is from telemetry-only health to multi-source value forecasting.

**V2V framing**: Value Score is the metric that the Customer-Outcome Decision Interface Charter (V5.2 Appendix C) decides against. The Charter says "when Value Score crosses threshold T, action A fires." Without Value Score (or KORE Score), the Charter has nothing to anchor on.

**V2V cross-reference**: `value-score-design` (planned Q2-4 pack) — operational scoring design. `customer-value-trace` skill — traces NSM to individual account Value Score. `outcome-review` skill — periodic assessment uses Value Score as a primary input.

---

## 7. OKRs vs. KPIs vs. NSMs — The Perennial Confusion

Three artifacts product orgs routinely conflate. They serve different purposes at different cadences.

| Artifact | What it is | Time horizon | Cadence | Example |
|----------|-----------|--------------|---------|---------|
| **OKR** | Aspirational outcome with measurable Key Results | Quarter / Year | Quarterly cycle | "Grow weekly active teams by 3x (KR1: WAT from 5K to 15K; KR2: team activation rate from 35% to 55%; KR3: NPS ≥ 40)" |
| **KPI** | Operational health indicator | Continuous | Real-time / weekly | "Login success rate ≥ 99%; P99 latency ≤ 250ms; ticket-deflection ≥ 60%" |
| **NSM** | Strategic value metric — the single compass | Continuous, multi-year | Continuous-as-strategic-anchor | "Weekly active teams with ≥5 members and ≥10 messages" |

**When teams conflate** (common failure modes):
- Using KPIs as OKRs ("KR1: uptime ≥ 99.95%") — operational floors are not aspirational outcomes
- Setting the NSM as an OKR target ("KR1: WAT to 15K") — fine as a milestone, but the NSM is permanent; OKRs are temporary
- Treating OKRs as KPIs (real-time tracking) — destroys the quarterly-stretch nature of OKRs
- Tracking 12 OKRs and calling them all priorities — by definition, that's not prioritization

**OKR-specific failures** (recurring patterns):
- Output-based KRs ("Launch feature X") instead of outcome-based ("Move activation from 30% to 45% via the new onboarding")
- Sandbagged OKRs that always hit 1.0 — kills the stretch function (target 0.7-0.8 should be normal for ambitious OKRs)
- Using OKRs as performance review inputs — kills ambition; teams will sandbag to protect compensation
- Too many OKRs per team (>3 Objectives or >5 KRs per Objective) — focus is the point

**V2V framing**: OKRs translate Phase-2 strategic bets into Phase-3 commitments. KPIs are Phase-4 execution guardrails. NSM is the Phase-2 / Phase-5 strategic anchor — the single thread from Decisions through Outcomes.

---

## 8. Counter-Metrics and Guardrails

**Goodhart's Law**: "When a measure becomes a target, it ceases to be a good measure." Any metric you optimize will be gamed, unless you pair it with a counter-metric that catches the gaming.

**Counter-metric examples**:

| Primary metric | What can be gamed | Counter-metric |
|----------------|-------------------|----------------|
| Engagement minutes | Auto-play, dark-pattern session extension | Session bounce-back rate (returns within 5 min of leaving — signals dissatisfaction) |
| MRR | Heavy discounting, short-term promos that don't renew | Net Revenue Retention (NRR); involuntary churn rate |
| Feature adoption rate | Forcing users into the feature with dark patterns | Feature uninstall / dismissal rate; NPS by feature-exposed cohort |
| Activation rate | Lowering the activation bar to look better | Day-30 retention of activated users; activated-vs-retained gap |
| Ticket deflection (AI support) | Closing tickets without resolving | Resolution Durability (see §9) |
| Sales-cycle close rate | Closing low-fit deals that churn | First-year customer retention by deal cohort |
| NPS | Survey timing manipulation | NPS by segment + qualitative theme analysis |

**Rule**: Every primary metric in a metric tree should have at least one counter-metric. If you can't name a way it could be gamed, you haven't thought hard enough.

**V2V framing**: Decision Interface Charters require explicit counter-metric thresholds. The Charter doesn't say "fire action A when metric M crosses T" — it says "fire action A when M crosses T AND counter-metric C is still in band." This is what prevents the Charter from being a Goodhart engine.

---

## 9. 2026 Metrics Landscape

Per V2V refresh survey §4 + §16, the dominant metric-landscape shifts in 2025-2026:

### Resolution Durability (CS / Support)

**Replaces**: Ticket deflection as the canonical AI-support KPI.

**Definition**: Did the resolution actually hold? Measured by 7-10 day reopen rate of "resolved" tickets. AI-resolved tickets that reopen within 7-10 days are not resolved — they're closed.

**Why now**: 2024-2025 AI-support deployments hit "97% deflection" headlines, then 2025-2026 churn data showed customers leaving because their issues weren't actually fixed. The industry moved from deflection-as-success to durability-as-success.

**Cross-reference**: `ai-assisted-resolution-strategy` skill — operational design for AI-assisted resolution that holds.

### Per-Seat-Pricing Structural Failure

**The shift**: TSIA 2026 — AI cuts headcount in customer organizations. Per-seat ARPU degrades even as outcome value grows. Vendor revenue per customer falls while customer ROI rises. The economic model breaks.

**Implication for metrics**: Per-seat ARPU is no longer a reliable revenue health metric for AI-leveraged products. Substitutes:
- Value-based pricing tied to outcomes (e.g., "per ticket resolved with durability ≥ 7 days")
- Consumption-based pricing tied to AI inference cost + value-capture margin
- Platform / outcome bundles (fixed price for committed outcome)

**Cross-reference**: `pricing-frameworks` pack — pricing-model taxonomy includes the per-seat structural-failure case.

### AI-Citation Rate (PMM-side metric)

**Definition**: Frequency with which your brand is cited in AI search results (ChatGPT, Claude, Gemini, Google AI Overviews) for category-defining queries.

**Why it matters**: As LLMs replace traditional search for high-intent buyer research, brand visibility in LLM responses becomes a top-of-funnel demand signal that traditional SEO doesn't capture.

**Cross-reference**: `/llm-seo` skill — operational measurement and optimization.

### Per-Spawn Cost / Per-Agent Cost (Engineering-side metric for AI products)

**Definition**: Inference and infrastructure cost per AI agent invocation, normalized to a unit of customer value (per ticket resolved, per email drafted, per analysis produced).

**Why it matters**: AI-product margin economics depend on the spread between per-spawn cost and per-spawn captured value. If per-spawn cost trends up (larger models, longer contexts) while pricing is fixed, gross margin compresses.

**Cross-reference**: `business-case` skill — AI-product business cases must include per-spawn cost sensitivity.

---

## 9.5 Agentic-Product Metrics

**Adapted from**:
- Agent-metrics practitioner writing on task-completion / containment / autonomy / cost-per-task (support-automation vendor metric definitions and agent-platform evaluation essays, 2024-2026) — practitioner-synthesis, no single proprietary framework.
- LLM-evaluation practice: eval-set + LLM-as-judge + regression-eval discipline (public LLM-eval practitioner writing and OSS eval frameworks such as DeepEval, Braintrust, Promptfoo patterns, 2024-2026).

**Source licence**: Public practitioner methodology; no license restriction on summary + attribution.

**V2V refinements**:
- Framed agent metrics as an outcome-NSM metric tree (§2) with mandatory counter-metrics (§8), not a raw dashboard.
- Positioned evals as the PM-owned *acceptance-criteria* artifact and ship-gate — distinct from the engineer's technical eval pack (`llm-evaluation.md`, planned/companion).
- Tied cost-per-successful-task to outcome-based pricing as the billing/value unit (`pricing-frameworks`).

---

The engagement funnels in §3–§4 (HEART, AARRR) measure a human *choosing to return*. An agentic product measures a machine *completing delegated work* — so DAU / retention / session-depth **mislead**: an agent that resolves a request in one shot and the user never "returns" is a success, not a churn signal. Fewer sessions can mean more value delivered. Non-determinism compounds the problem — the same input can produce different outputs — so you need a metric set built for delegated, variable work.

**Core agentic metrics:**

| Metric | Definition | What it tells you |
|---|---|---|
| Task-completion rate | % of attempted tasks finished to the defined success criterion | Primary quality metric — did it do the job? |
| Containment / autonomy rate | % of tasks completed with no human intervention or handoff | How much work the agent absorbs vs. deflects |
| Escalation rate | % of tasks handed off to a human (inverse of containment) | Where the agent hits its competence boundary |
| Human-intervention rate | % of tasks needing a human edit/correction mid-run | Trust + steerability signal (distinct from full escalation) |
| Steps-to-completion | Avg agent actions/turns per completed task | Efficiency + cost driver; rising = drift or looping |
| Cost-per-successful-task | Inference + infra cost ÷ successfully completed tasks | Unit economics — ties to §9 per-spawn cost and to pricing |

**Why these over engagement metrics:** engagement funnels reward time-in-product; agentic value rewards *outcomes delivered per unit cost with minimal human touch*. The right compass is an outcome NSM ("successful tasks completed") laddered via a metric tree (§2) to task-completion, containment, and cost-per-successful-task. Pair each with a counter-metric (§8): containment gamed by closing tasks the user reopens → pair with a reopen/durability counter (mirrors Resolution Durability, §9); autonomy gamed by acting without confirmation on risky tasks → pair with an intervention-correctness or error-rate counter.

**Value tie:** cost-per-successful-task and task-completion rate are the two numbers that make outcome-based pricing legible — they become the billing/value unit (see `pricing-frameworks` §10, Agentic Value-Capture).

### Agent evals as acceptance criteria (PM ownership)

For a non-deterministic agent, "acceptance criteria" cannot be a checklist that deterministically passes or fails. The PM's discipline is to convert acceptance criteria into an **eval set + judged rubric + ship-gate**:

1. **Eval set** — a curated, versioned collection of representative task inputs with defined success criteria (the "golden set"). This IS the acceptance-criteria artifact for an agent. Grow it with every production failure (regression eval-set discipline — each bug becomes a permanent test case).
2. **Judge / rubric** — because outputs vary, grade them with an LLM-judge against an explicit rubric (or human raters for high-stakes) rather than exact-match. The rubric IS the acceptance criterion, expressed as gradeable dimensions.
3. **Ship-gate as a threshold, not pass/fail** — gate on an aggregate score over the eval set (e.g., "task-completion ≥ [your threshold] on the golden set, no regression vs. last release"), not on every case passing. Non-determinism means you accept a distribution, not a single result: set the threshold, block the ship if the eval score regresses.

This is the PM's ownership discipline — defining *what good looks like* and *where the ship-gate sits*. It is distinct from the engineer's technical evaluation tooling (harness design, judge calibration, statistical rigor), which lives in the companion `llm-evaluation.md` pack (planned) — cross-reference it, do not reproduce it here.

---

## 10. V2V Cross-References

| Skill / Pack | Relationship to this pack |
|--------------|---------------------------|
| `/strategic-bet` | NSM is the strategic-bet's success metric (Phase 2 Decisions) |
| `/north-star-metric` | NSM authoring workflow (this pack frames; the skill operationalizes) |
| `/customer-value-trace` | Traces NSM to individual customer outcomes |
| `/outcome-review` | Periodic outcome assessment uses these metrics as input (Phase 5 Outcomes) |
| `/pirate-metrics` | Operational AARRR application workflow |
| `/heart-metrics` | Operational HEART application workflow |
| `/value-realization-report` | Phase-5 Outcomes deliverable using Value Score + NSM data |
| `/customer-health-scorecard` | Account-level health (transitioning to Value Score) |
| `/health-score-design` | Operational design; being superseded by `value-score-design` |
| `value-score-design` pack | Planned Q2-4 — operational Value Score design (KORE / TSIA-aligned) |
| `pricing-frameworks` pack | Per-seat structural failure (§9) ties to pricing-model taxonomy; §9.5 agentic metrics become the billing unit in `pricing-frameworks` §10 |
| `llm-evaluation.md` pack (planned) | Engineer's technical eval tooling; §9.5 "Agent evals as acceptance criteria" is the PM-owned complement — cross-reference, don't duplicate |
| `/feature-spec`, `/prd` skills | Should cross-reference §9.5 Agentic-Product Metrics when speccing a non-deterministic agent (wiring pending) |
| `customer-success-methodology` pack | Conditional preload for `value-realization` — pairs with this pack on CS outcome practice |
| `saas-metrics` pack | Conditional preload for `value-realization` — operational SaaS retention/adoption analysis |
| `/decision-record` | Re-decision triggers reference metric thresholds defined here |
| `/four-risks-check` | "Viability" risk (Marty Cagan) maps to metric-based outcome validation |

---

## Selection Guide

| Situation | Recommended frame | Why |
|-----------|-------------------|-----|
| Defining strategic compass for a product line | NSM + metric tree | Single strategic anchor; tree translates to teams |
| Quarterly team goal-setting | OKRs ladder to metric tree leaves | Quarterly ambition; permanent strategic anchor |
| Comprehensive product UX health | HEART | UX + engagement + retention coverage |
| Funnel diagnosis (PLG / consumer) | AARRR or RARRA | Leakiest-stage prioritization |
| Customer outcome forecasting | Value Score / KORE Score | Replaces structurally-insufficient Health Score |
| AI-support program health | Resolution Durability + counter-metrics | Deflection is gamed; durability is real |
| Re-decision trigger design | Primary metric + counter-metric + threshold | Goodhart-resistant; tied to Decision Charters |
| Feature launch success | Metric tree leaf + HEART task-success | Outcome-based, not output-based |

---

## Sources

- Sean Ellis, "The One Metric That Matters" (2010)
- Kerry Rodden, Hilary Hutchinson, Xin Fu, "Measuring the User Experience on a Large Scale" (CHI 2010)
- Dave McClure, "Startup Metrics for Pirates" (2007)
- Andrew Chen, "New Mobile App Metrics" (2017) — RARRA reordering
- Andy Grove, *High Output Management* (1983)
- John Doerr, *Measure What Matters* (2018)
- Christina Wodtke, *Radical Focus* (2016)
- Dan Olsen, *The Lean Product Playbook* (2015) — metrics hierarchy
- Aakash Gupta / Reforge — metric tree pattern (2024-2026)
- TSIA, *State of Customer Success 2026* — Health Score retirement, Value Score, KORE Score
- V2V refresh survey §4 (PM landscape), §5 (PMM landscape), §16 (CS landscape) — 2026 Q2

---

**Pack version**: v4.1.0 (2026-05-18) — joint `vp-product` + `value-realization` authoring, KORE / Value Score / metric tree / 2026 landscape additions.
