# Competitive Frameworks — V2V OS Pack

**Sources consulted**:
- Porter's Five Forces (Michael Porter, "Competitive Strategy" 1980) — public methodology
- Jobs-to-be-Done competitive framing (Clayton Christensen, Bob Moesta) — public methodology
- Wardley Mapping (Simon Wardley) — public strategic-mapping method
- ArcKit v4.21 (`tractorjuice/arc-kit`) — tooling reference for Wardley application (per V2V refresh survey §2)
- April Dunford "Obviously Awesome" — alternative-positioning framing
- Win/Loss Analysis methodology — Klue / Crayon / PROS market practice
- "7 Powers" (Hamilton Helmer 2016) — competitive moats
- Counter-positioning (Helmer + Clay Christensen) — challenger strategy
- 2026 Q2 competitive landscape per V2V refresh survey
- Gartner "Machine Customers" research line + "Optimize Product Data for Agentic Commerce" (Jan 2026) — for §12.5 structured-attribute / agent-buyer positioning shift (Gartner figures are predictions; attribute as such)

**Source licence**: Simon Wardley's published Wardley Mapping work is CC BY-SA 4.0. The ArcKit repository is MIT-licensed except for its separately licensed `plugins/arckit-uk-gcloud/` directory. Other named methodologies are credited public references; Helmer's full text remains a book purchase, and the Gartner research line is cited as an analyst prediction.
**Our determination**: `describes-public-method` — this pack is original V2V prose describing and applying public methods. The Wardley and ArcKit lines are source credit, not a legal determination about this file; no Wardley or ArcKit code, text, diagrams, or other licensed work is reproduced or redistributed.
**V2V refinements**: Competitive analysis framed as Phase-1 Intent + Phase-2 Decisions input (competitive choice IS a strategic-bet input); cross-references to competitive-landscape + competitive-analysis + win-loss-decision-signal + wardley-map skills; §12.5 adds agent-buyer/structured-attribute positioning (brand-premium erosion at the agent layer, battlecard + counter-positioning implications) as the CI complement to `agentic-commerce.md`'s BD/marketing lens

---

## 1. Purpose

V2V OS pack on Porter Five Forces, JTBD-competitive, Wardley Mapping, win/loss analysis, 7 Powers, counter-positioning, and competitive intelligence cadence. Preloaded by `competitive-intelligence`; cross-referenced by the family of competitive skills.

Use this pack when producing competitive landscapes, battlecards, positioning strategies, strategic bets that hinge on competitive position, or any deliverable where competitive truth is load-bearing.

---

## 2. Framing — Competitive Analysis as Decision Input, Not Threat Tracking

The trap with competitive intelligence is treating it as surveillance — "what are competitors doing this week" — without ever translating signal into decision. Battlecards get authored and never used. Quarterly competitor reports get filed and never referenced. Win/loss interviews get conducted and never coded. Activity without consequence.

**V2V framing**: competitive analysis is an input to two specific phases:

- **Phase 1 — Intent**: market segmentation and positioning. Who do we compete against? What competitive set does the customer actually consider? Where do we *choose* to play?
- **Phase 2 — Decisions**: strategic bets. Counter-position vs incumbent or attack head-on? Defensive vs offensive posture on this category? Build, buy, or partner given the competitive trajectory?

Every competitive deliverable I author ends with a **decision recommendation**, not a competitor watch report. If a competitive analysis cannot answer "so what should we do differently?", it isn't competitive intelligence — it's market trivia.

Cross-references: `strategic-intent` (Phase 1), `strategic-bet` (Phase 2), `decision-record` (Phase 2 logging).

---

## 3. Porter Five Forces (1980)

Industry-level structural analysis. Five forces shape industry profitability and competitive intensity.

1. **Threat of new entrants** — barriers to entry (capital, regulation, network effects, switching costs, scale economies). High barriers protect incumbents; low barriers invite disruption.
2. **Bargaining power of suppliers** — leverage held by upstream inputs (rare skills, monopolist APIs, sole-source components).
3. **Bargaining power of buyers** — leverage held by downstream customers (consolidated buyer base, low switching costs, commodity offerings).
4. **Threat of substitutes** — alternatives outside your direct category. **The most-missed force**, because by definition you don't see substitutes if you only watch direct competitors. Spreadsheets substitute for half of SaaS. "Do nothing" substitutes for everything.
5. **Industry rivalry** — intensity among existing players (number of competitors, growth rate, fixed-cost structure, exit barriers, differentiation).

**Template**:

| Force | Intensity (L/M/H) | Key Factors | Strategic Implication |
|---|---|---|---|
| New Entrants | | | |
| Supplier Power | | | |
| Buyer Power | | | |
| Substitutes | | | |
| Rivalry | | | |
| **Overall Industry Attractiveness** | | | |

**When to use**: industry-level analysis, strategic positioning, entry-decision evaluation (should we enter this market at all?).

**When NOT**: granular competitor positioning, feature-level decisions, or product-level differentiation work — Five Forces is too coarse.

**Modern critique**: Porter assumes industry boundaries are stable. They're not. AI-era industry boundaries shift quarterly — vertical SaaS competing with horizontal foundation-model providers; agentic systems eating workflow categories whole. Combine Porter with JTBD (Section 4) and Wardley (Section 5) to recover the dynamics Porter strips out.

Cross-ref: `porter-five-forces` skill.

---

## 4. Jobs-to-be-Done Competitive Framing (Christensen + Moesta)

Define the competitive set by the **job** customers hire products to do, not by industry category.

Christensen's milkshake example: morning-commute milkshakes compete with bananas, breakfast bars, bagels, and 7am boredom — not with afternoon milkshakes. The competitive set is defined by *job context*, not *product category*.

**Modern SaaS application**: a project management tool competes with Excel, with email + a shared folder, with ChatGPT-Notion improvisations, with "do nothing and keep using Slack," and yes, with the obvious named competitor. "Do nothing" is usually the biggest single competitor, and is invisible to feature-by-feature competitive analysis.

**Implication for analysis**: a competitive landscape that only lists named SaaS competitors is missing 60% of the actual decision space. The job-defined competitive set always includes manual workarounds, adjacent-category products, and abandonment.

**When to use**:
- Defining the competitive set for a new product or category
- Diagnosing low win-rate against unnamed competitors ("we lost to status quo")
- Validating that a positioning claim addresses the real alternative

Cross-refs: `discovery-methods` pack (Q2-2.4) JTBD section, `customer-value-trace` skill, `market-segment` skill.

---

## 5. Wardley Mapping (Simon Wardley)

Maps components on **Value Chain** (Y-axis: visible-to-user → invisible infrastructure) × **Evolution** (X-axis: Genesis → Custom-Built → Product → Commodity).

What it surfaces:
- **What's commoditizing** — components moving rightward toward Commodity. You should buy or rent these, not build.
- **What's strategic** — components in Genesis or Custom-Built that differentiate you. Build and protect.
- **Where competitors are positioned** — visualizing competitor maps side-by-side reveals where they're investing build effort vs. where they're consuming commodities.

**2026 update**: ArcKit v4.21 (tractorjuice/arc-kit, ~1.8k stars) provides ~70 commands for Wardley analysis plus 46 community overlays. Per V2V refresh survey §2, ArcKit is the current canonical tooling for Wardley work in agentic contexts.

**When to use**: strategic-bet decisions on build/buy/partner; competitive-positioning shifts; identifying where a market is about to commoditize (and you should exit) or evolve (and you should accelerate).

**When NOT**: tactical feature-level analysis, sales battlecard authoring, or any work where the unit of analysis is a deal not a market.

Cross-ref: `wardley-map` skill.

---

## 6. 7 Powers (Hamilton Helmer 2016)

Seven structural sources of durable competitive advantage. A "power" is a competitive advantage that survives — not a feature, not a price, not a campaign, but a structural reason customers continue to choose you that competitors cannot easily neutralize.

1. **Scale Economies** — unit costs decline as you scale; large players permanently advantaged.
2. **Network Economies** — value to each user increases with total users (marketplaces, social networks, standards).
3. **Counter-Positioning** — see Section 7.
4. **Switching Costs** — customers face friction (financial, procedural, relational) when leaving.
5. **Branding** — durable affective trust premium (not just awareness).
6. **Cornered Resource** — preferential access to a scarce input (IP, talent, contract, location, data).
7. **Process Power** — embedded operational know-how that competitors cannot copy without restructuring.

**When to use**: assessing the durability of your or a competitor's position; M&A defensibility analysis; strategic-bet evaluation against the question "is this advantage durable or temporary?"

**V2V refinement**: 7 Powers, Wardley, and Porter complement rather than substitute. Porter tells you the industry shape. Wardley tells you which components are moving. 7 Powers tells you whether a position is defensible once you arrive. Use all three for high-stakes competitive bets.

Cross-ref: `seven-powers` skill.

---

## 7. Counter-Positioning (Helmer + Christensen)

A challenger strategy: take a position the **incumbent cannot copy because doing so would cannibalize their existing business**. The incumbent's strength becomes their constraint.

**Classic examples**:
- Vanguard low-cost index funds vs Fidelity's actively-managed business — Fidelity couldn't aggressively push index because their existing fee structure depended on active management
- Netflix streaming vs Blockbuster physical rental — Blockbuster couldn't aggressively launch streaming because they'd cannibalize per-store unit economics and franchise relationships
- AWS infrastructure-as-a-service vs IBM consulting — IBM couldn't push self-service cloud because it cannibalized the consulting hours that paid for everything
- Robinhood zero-commission trading vs full-service brokerages — they couldn't match without destroying their revenue model
- Open-source LLMs vs closed-source providers — closed-source providers can't open-weight their models without surrendering the moat

**Diagnostic question**: "If the incumbent matched our move, what would they have to destroy in their existing business?" If the answer is "nothing serious," it's not counter-positioning, it's just competition.

**When to use**: as a challenger, scanning for positions where incumbent revenue model creates structural inability to respond.

**When NOT**: when there's no structural reason the incumbent can't copy you — in that case you're just hoping they're slow, which is not a strategy.

Cross-ref: Helmer's *7 Powers* counter-positioning chapter; `strategic-bet` skill.

---

## 8. Win/Loss Analysis (Operational Competitive Intelligence)

Capture **why** deals are won and lost — from the customer's perspective, not from sales's internal-attribution. Sales reps blame pricing 80% of the time; customer interviews reveal the truth is usually feature gaps, relationship, or perceived risk.

**Interview cadence**: every won and lost deal above a defined ARR threshold (e.g., $X). Within 2-4 weeks of decision — memory fades fast.

**Interview structure**:
- Interview the economic buyer or primary evaluator, not just your champion (champion has confirmation bias toward "we picked you for good reasons")
- Use a third party if possible (Klue, Crayon, an in-house team that doesn't carry quota) — prospects are more honest with neutral interviewers
- Both wins and losses (wins reveal what to protect; losses reveal what to fix)

**Standard interview guide**:
1. What triggered the evaluation? (Business need / event / mandate)
2. What criteria were most important in your decision?
3. Which solutions did you evaluate? (Real competitive set — usually wider than sales thinks)
4. What were the top 2-3 factors in your final decision?
5. Was there anything that almost changed the decision?
6. How did you perceive [our product] vs [competitor]?
7. What could we have done differently?

**Synthesis cadence**: themes per quarter, surfaced to PMM + Product + Sales Enablement. Individual interviews are stories; aggregated themes are intelligence.

**Anti-pattern: sales-team-internal-attribution-only**. If win/loss data comes only from CRM "lost reason" fields filled in by reps, the data will systematically blame pricing and timing — because reps are incentivized to externalize loss. External-interviewer win/loss is the only credible signal.

Cross-refs: `win-loss-decision-signal` skill and `competitive-battlecard` skill.

---

## 9. Competitive Intelligence Cadence

Continuous competitive monitoring requires a layered cadence — different work at different intervals. Without cadence, CI becomes either firehose (everything is urgent) or stale (nothing gets refreshed).

| Cadence | Activity | Owner | Output |
|---|---|---|---|
| **Daily** | Monitoring — RSS, Crunchbase alerts, news, AI search results, social signals, GitHub releases | CI / PMM | Slack channel, alert digest |
| **Weekly** | Synthesis — PMM + CI briefing; what matters this week | CI + PMM | Weekly digest, decision asks |
| **Monthly** | Deep-dive on one competitor or one market segment (rotating) | CI | Updated competitor profile, segment scan |
| **Quarterly** | Full competitive landscape refresh — positioning, market share, pricing, key moves | CI | Refreshed landscape doc |
| **Annually** | Strategic-bet validation against competitive position — are our bets still defensible? | CI + VP Product + CPO | Bet review, strategic refresh input |

Cross-refs: `competitive-landscape` skill (quarterly), `strategic-bet` skill (annual review).

---

## 10. Competitive Battlecards (Sales-Facing Artifact)

A battlecard is a concise (1-2 page) competitive reference designed for sales use during active deals. It must be current, practical, and focused on winning, not informing.

**Standard sections**:

1. **Quick overview** — competitor name, positioning statement, key metrics (size, funding, pricing), one-line "they position as X, we position as Y"
2. **How they win / how they lose** — top 3 strengths (honest — sales loses trust in dismissive battlecards), top 3 weaknesses (specific and verifiable), segments where they win, segments where they lose
3. **Objection handling** — `objection | response | proof point` table; every response something a salesperson can say confidently
4. **Win themes** — top 3 reasons customers choose us; discovery questions that favor our strengths without being negative; questions that expose competitor weakness without trash-talking
5. **Land mines** — topics to avoid (play to competitor strengths), pricing-comparison pitfalls, feature-comparison traps
6. **FUD handling** — what competitor reps say about us, and how to respond truthfully

**Anti-patterns**:
- Marketing-authored battlecards that sales never opens (the cure: sales-team co-authoring, real-deal validation, regular use audits)
- Overly negative cards that erode sales trust (the cure: acknowledge competitor strengths honestly)
- Stale cards quarterly out-of-date (the cure: ownership + cadence + version date prominently displayed)
- Feature-parity matrices that pretend product equivalence settles deals (the cure: focus on win themes and proof points, not feature ticks)

Cross-ref: `competitive-battlecard` skill.

---

## 11. Common Competitive Analysis Failures

Patterns I see repeatedly. If you're doing competitive work, audit your output against this list before shipping.

1. **Watching "obvious" competitors while missing substitution threats**. Category killers always come from outside the category — Excel-replacement SaaS missed by enterprise software incumbents; foundation models eating workflow tools incumbents never watched. Section 3's threat-of-substitutes force is the most-missed because by definition substitutes aren't where you're already looking.

2. **Confirmation-bias intelligence**. Only finding evidence the incumbent is weak, or that "our differentiation is holding." Genuine CI looks equally hard for evidence the bet isn't working.

3. **Stale battlecards**. Sales loses confidence in a battlecard that's 6 months out of date; stops using it; CI loses its sales-feedback loop. Quarterly refresh minimum, monthly for major competitors.

4. **"Feature parity" arms race**. Competing on features instead of differentiated positioning. The instinct is to add the competitor's feature so sales can tick the matrix; the result is a product that does nothing well and stands for nothing.

5. **Mistaking "competitor activity" for "competitor strategy"**. Most competitor moves are tactical — A/B-test launches, sales-led experiments, individual rep tactics. Treating every tactical move as strategic signal generates over-response and burns CI credibility. Genuine strategic signal: pattern across quarters, exec-articulated positioning shift, M&A, pricing-model change.

6. **Internal-attribution win/loss only** (see Section 8). If win/loss data lives in CRM "loss reason" fields, it's not data — it's sales rationalization.

7. **Competitive analysis that ends without a decision**. If the deliverable doesn't conclude "so we should do X," it isn't intelligence. See Section 2 framing.

---

## 12. 2026 Competitive Landscape Shifts

Per V2V refresh survey + current state of the market. Treat these as the most consequential shifts CI must track across every competitive scan in 2026.

**12.1 — GenAI search visibility (GEO)**. Competitive position now includes "do AI engines cite us when buyers ask category questions?" Survey §5 documents the citation-overlap collapse: roughly 70% historical overlap between Google top-10 and AI-engine citations has dropped to under 20%. Competitors with high GEO citation visibility are functionally outranking you in the buyer-research phase, even if traditional SEO favors you. Cross-ref: `seo-frameworks` pack, `llm-seo` skill, `geo-monitoring-setup` skill.

**12.2 — AI-feature commoditization**. Within ~12 months of a competitor adopting an AI feature, the rest of the category matches or differentiates elsewhere. AI-features as differentiation have a short half-life. Sustainable differentiation moves to **data quality, workflow integration, and trust** (regulatory posture, security, customer data sovereignty). Cross-ref: 7 Powers Section 6 — durable advantages survive feature copying.

**12.3 — Foundation-model dependency as commodity risk**. Competitive advantage built solely on foundation-model access is short-lived; every competitor will have GPT-class capabilities within months. Differentiation moves to proprietary data, workflow ownership, trust posture, and process power (Helmer #7). Wardley-map your foundation-model components honestly — they're moving rightward toward Commodity faster than vendor marketing admits.

**12.4 — Open-source convergence**. Competitive moats from closed-source software erode as OSS catches up, especially in dev tooling, infrastructure, and increasingly in vertical workflow categories. Closed-source incumbents face counter-positioning pressure (Section 7) from OSS competitors who can give core capability away and monetize adjacent layers.

**12.5 — Positioning when the buyer is an agent (structured-attribute competition)**. A distinct shift from 12.1: 12.1 (GEO) is about being *cited* when a human's AI assistant researches a category; 12.5 is about competing when the *buyer itself is a machine* that discovers, compares, and transacts on structured attributes — the "machine customer" (Gartner) and agent-as-buyer surface. When an agent, not a human, runs the comparison, the basis of competition changes and CI/PMM positioning must change with it.

- **Brand and emotional premium erode at the agent layer.** A human weighs affective trust, aesthetics, and story; an agent optimizing on the buyer's stated constraints ("in stock, under $X, returnable, ships by Friday") is a more rational, lower-switching-cost buyer. Helmer's Branding power (Section 6) weakens specifically at the agent-mediated transaction — it still works on the human who *configures* the agent, but not on the agent's per-transaction pick. This is a genuine power-erosion CI must flag, not a marketing nicety.
- **Competition collapses onto structured attributes.** Spec-fit, price, availability, fulfillment reliability, and return terms — expressed as machine-readable fields — become the rivalry surface (a Porter buyer-power intensifier, Section 3: agents lower buyer switching cost and raise price/attribute transparency). The differentiation that survives is the same trio as 12.2/12.3 — data quality, workflow integration, and structurally verifiable trust (verified-merchant / trust-protocol attestations) — because those are legible to a machine, whereas an emotional positioning claim is not.
- **Implication for battlecards (Section 10).** Agent-era battlecards need an "attribute-parity" view: where do we win/lose on the *structured* fields an agent actually filters on (price incl. fees, in-stock %, delivery window, return window, verified-trust status), not on the narrative win-themes that persuade a human. A feature-parity matrix — normally an anti-pattern (Section 11.4) — is closer to the real decision surface when the evaluator is a machine, but only on the attributes the agent can read.
- **Implication for counter-positioning (Section 7).** Incumbents whose model depends on brand premium or high-touch human sales face a structural bind: fully exposing themselves to agent comparison (structured feeds, transparent all-in pricing, verifiable trust) commoditizes the premium their revenue depends on — a counter-positioning opening for a challenger built agent-legible from the start. Conversely, a challenger's agent-legibility advantage is only durable if paired with a machine-legible power (process, cornered data, switching cost), since attribute-only leads are copyable within a feed cycle.

The *operational* marketing complement — how to optimize product feeds, offers, and merchant-trust signals so an agent selects and transacts you — lives in `agentic-commerce.md` §5.6; the segment/channel BD framing lives in `agentic-commerce.md` §4 (machine customer) and §5.2 (agent-legibility readiness gate). Cross-ref: `agentic-commerce.md` §4 / §5.2 / §5.6, `positioning-statement` skill, `competitive-battlecard` skill.

---

## 13. V2V Cross-References

Competitive frameworks pack relates to the rest of the V2V system through these skills:

- `competitive-landscape` skill — market-level scan, quarterly refresh artifact
- `competitive-analysis` skill — feature-level competitor comparison
- `competitive-battlecard` skill — sales-facing artifact (Section 10)
- `competitive-intelligence` skill — `competitive-intelligence` agent's primary domain skill
- `wardley-map` skill — Wardley application (Section 5)
- `seven-powers` skill — Helmer application (Section 6)
- `porter-five-forces` skill — Porter application (Section 3)
- `win-loss-decision-signal` skill — win/loss synthesis (Section 8)
- `strategic-bet` skill — competitive bet authoring (Section 2 framing)
- `strategic-intent` skill — Phase 1 competitive positioning input
- `positioning-statement` skill — competitive context for positioning
- `market-segment` skill — competitive set defined by segment (Section 4 JTBD)
- `decision-record` skill — logging competitive decisions
- `agentic-commerce` knowledge pack — §4 (machine customer segment), §5.2 (agent-legibility readiness gate), §5.6 (feed/offer/merchant-trust optimization). §12.5 of this pack is the CI/positioning complement to that pack's BD/marketing lens; the two are reciprocal.
- `gtm-playbooks` knowledge pack — §12 (2026 landscape) shifts in competitive positioning (GEO/LLM-SEO citation collapse, AI-feature commoditization, foundation-model commodity risk, OSS convergence) all have direct GTM-motion implications; see gtm-playbooks §7 (2026 GTM landscape) for the reciprocal view

---

## Selection Guide

| Situation | Recommended Framework | Why |
|---|---|---|
| Industry structure analysis | Porter's Five Forces (§3) | Maps forces shaping competition |
| Defining the real competitive set | JTBD competitive framing (§4) | Includes substitutes + "do nothing" |
| Build/buy/partner decisions | Wardley Mapping (§5) | Surfaces commoditization vs differentiation |
| Assessing position durability | 7 Powers (§6) | Structural moat analysis |
| Challenger strategy | Counter-positioning (§7) | Find position incumbent can't copy |
| Improving win rates | Win/Loss Analysis (§8) | Real decision factors, not internal attribution |
| Sales enablement | Battlecards (§10) | Practical, deal-focused |
| Responding to competitor moves | CI cadence + threat assessment (§9) | Distinguish tactical noise from strategic signal |
| Comprehensive bet evaluation | Porter + Wardley + 7 Powers | Industry shape × component movement × position durability |

---

## Sources

- Michael E. Porter, *Competitive Strategy* (1980) — Five Forces and competitive analysis
- Michael E. Porter, *Competitive Advantage* (1985) — Value chain and differentiation
- Clayton Christensen + Bob Moesta — Jobs-to-be-Done competitive framing
- Simon Wardley, *Wardley Maps* (CC-BY-SA 4.0); ArcKit v4.21 tooling (tractorjuice/arc-kit)
- Hamilton Helmer, *7 Powers* (2016) — durable competitive advantage
- April Dunford, *Obviously Awesome* (2019) — positioning with competitive context
- Al Ries + Jack Trout, *Positioning: The Battle for Your Mind* (1981) — competitive positioning origins
- Ellen Naylor, *Win/Loss Analysis* (2016) — systematic win/loss methodology
- Klue, Crayon, Kompyte — battlecard and CI platform best practices
- V2V refresh survey 2026 Q2 §2 (ArcKit) and §5 (GEO citation collapse)
