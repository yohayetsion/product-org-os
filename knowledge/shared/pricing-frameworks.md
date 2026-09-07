# Pricing Frameworks

**V2V OS knowledge pack on SaaS / B2B / consumer pricing strategy, monetization models, and value-based pricing methodology.**

---

## Attribution

**Adapted from**:
- Industry-standard SaaS pricing methodology — Patrick Campbell / ProfitWell research (2015-2023), Madhavan Ramanujam and Georg Tacke, *Monetizing Innovation* (2016), Thomas Nagle and Georg Muller, *The Strategy and Tactics of Pricing* (6th ed., 2017), Kyle Poyar / OpenView SaaS pricing benchmarks (2018-2024), Bessemer Venture Partners *State of the Cloud* reports. Public methodology, no formal license.
- Hamilton Helmer, *7 Powers: The Foundations of Business Strategy* (2016) — competitive moat applied to pricing power.
- Peter van Westendorp, "NSS-Price Sensitivity Meter" (1976); Paul E. Green and V. Srinivasan, "Conjoint Analysis in Marketing" (1978) — survey-based WTP methodology.
- Stripe + Tomasz Tunguz (Redpoint) public pricing analyses (2020-2024) — usage-based pricing data.
- 2026-06 delta: Futurum Group 1H-2026 AI-pricing buyer survey; PYMNTS reporting on Adobe outcome-based pricing; HubSpot / Intercom / Zendesk public agent-pricing points (per-resolved-conversation). See the 2026-06 Delta Update section.

**Source licence**: Public methodology references; no license restriction on summary + framework attribution.

**V2V refinements**:
- Pricing framed as a Phase-2 (Decisions) strategic bet, not a Phase-4 execution detail.
- Joint authoring lens: `bizops` (financial-modeling perspective) + `director-product-marketing` (pricing-as-messaging perspective). Pricing decisions are co-owned across these seats — neither owns alone.
- Cross-reference to `business-case` skill: pricing assumptions feed business-case ROI.
- Cross-reference to `strategic-bet` skill: pricing is a strategic commitment with explicit assumptions, success criteria, and review triggers — not a tactical adjustment.

---

## Joint-Authoring Lens

Pricing sits at the intersection of **financial modeling** (margin, unit economics, sensitivity, capture rate) and **messaging architecture** (positioning relative to alternatives, willingness-to-pay framing, perceived value, pricing-page narrative). Neither seat owns pricing alone:

- **`bizops`** brings: cost-to-serve modeling, contribution margin per tier, LTV/CAC sensitivity to price changes, pricing-decision business case, scenario modeling for price increases / discount strategy.
- **`director-product-marketing`** brings: positioning relative to alternatives, value-metric naming and framing, pricing-page conversion, packaging narrative, competitive pricing response, segment-level price discrimination via tiers.

The V2V principle: **pricing is a strategic commitment, not a tactical execution**. A pricing decision sets ceilings on margin, signals positioning to the market, and constrains GTM motion. It belongs in Phase 2 (Decisions), reviewed at outcomes (Phase 5), with explicit assumptions tracked in the assumptions registry.

When you read this pack, you should be carrying both lenses simultaneously. A pricing recommendation that only models margin is incomplete. A pricing recommendation that only positions against competitors is incomplete. The deliverable carries both, or it goes back.

---

## 1. Pricing Model Taxonomy

The eight models below are the dominant patterns. Most real pricing structures are **hybrids** of two or three.

### Per-seat / Per-user

**Fits when**: Value scales with the number of people using the product (collaboration tools, CRM, productivity software). Buyer can easily count seats. Procurement-friendly for enterprise.

**Doesn't fit when**: Value is workflow-driven, not person-driven (e.g., a billing automation tool — value depends on transactions processed, not seats). At scale, per-seat creates discount pressure (large customers demand volume discounts that erode ARPU per seat).

**Data needed to validate**: Active seats per account over time, expansion patterns (does seat count grow with account tenure?), and seat-utilization (paid-but-unused seats are a churn risk).

### Per-usage / Metered

**Fits when**: Value scales with consumption (API calls, compute hours, transactions, messages, GB processed). Customer can predict their usage. The vendor has reliable, real-time metering infrastructure.

**Doesn't fit when**: Usage is unpredictable and customer fears bill shock. Buyer is procurement-led and needs fixed-budget commitments. Low-volume customers feel the model is "punishing" them.

**Data needed to validate**: Usage distribution across customers (median vs. P95), correlation between usage and customer-reported value, churn rate of low-usage cohorts (often a leading indicator of poor activation).

### Tiered (Good / Better / Best)

**Fits when**: You serve multiple distinct segments with one product. Most B2B SaaS. The middle tier ("Better") is designed as the anchor — most customers choose it by design.

**Doesn't fit when**: The product is so feature-uniform that tier boundaries feel arbitrary. Or when segments have radically different value metrics (then tiering masks bad pricing).

**Data needed to validate**: Tier mix (% in each), feature usage by tier (are "Best" features used? if not, the package is wrong), upgrade rate from middle to top tier, and downgrade signals.

### Flat-rate / Value-based fixed

**Fits when**: A single price point captures value for a well-defined segment. Simple, easy to communicate. Common in early-stage SaaS and consumer subscriptions.

**Doesn't fit when**: Customer value varies widely (small customers feel over-priced, large customers feel under-priced). Creates revenue plateau.

**Data needed to validate**: Customer value-delivered variance (if std dev is large, flat-rate is leaving money on the table).

### Hybrid (Base fee + usage, or seat + feature tier)

**Fits when**: You need revenue predictability (base fee) AND value-aligned pricing (usage component). Most modern SaaS uses some hybrid.

**Doesn't fit when**: Adds explanation overhead at the pricing page. Hybrid pricing requires clearer messaging than single-axis pricing.

**Data needed to validate**: Customer comprehension test — can a prospect predict their bill from the pricing page in under 60 seconds?

### Freemium / Free-trial / Reverse-trial

**Fits when**: Marginal cost of free user is low. Free tier has natural usage limits that drive upgrade. Network or content effects benefit from large free base.

**Doesn't fit when**: Free users are expensive to serve (heavy infra, support). Conversion rate is structurally low (<1-2%). Product has weak upgrade triggers.

- **Freemium**: Permanently free tier. Conversion benchmarks: 2-5% self-serve SaaS (ProfitWell); 4-6% best-in-class.
- **Free trial**: Time-limited (typically 14-30 days). Higher friction (signup), higher intent (conversion 15-25%).
- **Reverse trial**: Start with full features (auto-trial), downgrade to free or paid at end of period. Higher activation, ambiguous to design.

**Data needed to validate**: Free-to-paid conversion rate by cohort, time-to-conversion distribution, free-user cost-to-serve, activation rate within free tier.

### Enterprise / Custom

**Fits when**: Deal size justifies sales motion (>$25K ACV as a rough floor). Customers expect negotiation. Procurement demands custom contracts.

**Doesn't fit when**: Volume is high enough that custom pricing creates ops overhead per deal. Or when self-serve customers see "Contact Sales" and bounce.

**Data needed to validate**: Sales-cycle length, discount distribution (median + P90), ratio of list price to realized price.

### Outcome-based / Performance-based

**Fits when**: You can measure customer outcomes attributable to the product (e.g., revenue lifted, cost saved, fraud detected). Both sides agree on the measurement. Increasingly common in AI/agent products where outcome is measurable (resolved tickets, completed workflows).

**Doesn't fit when**: Outcome attribution is contested. Vendor bears outcome risk it can't control. Sales cycle slows down on measurement negotiation.

**Data needed to validate**: Outcome measurement reliability, customer-side accounting acceptance, vendor margin sensitivity to outcome variance.

---

## 2. Value-Based Pricing Methodology

Value-based pricing sets price as a function of the economic value the product delivers to the customer, **not** cost-plus and **not** competitor-anchored. The methodology has three steps + supporting research methods.

### The three-step process

1. **Identify the customer's next best alternative.** What would they do, buy, or build if your product didn't exist? Calculate the cost and outcome of that alternative.
2. **Quantify the differentiation value above the alternative.** What incremental value (revenue gained, cost avoided, risk reduced, time saved) does your product deliver vs. the alternative?
3. **Set price as a fraction of differentiation value.** Capture 20-40% of differentiation value as a rough heuristic (Nagle). The remainder is the customer's "consumer surplus" — their reason to buy.

### Willingness-to-Pay (WTP) research methods

#### Van Westendorp Price Sensitivity Meter (PSM)

Survey customers/prospects with four questions about a described product:

1. At what price would the product be **so expensive you would not consider buying it**? (Too Expensive)
2. At what price would the product be **so low that you would question its quality**? (Too Cheap)
3. At what price would the product be **getting expensive, but you might still consider buying it**? (Expensive/High)
4. At what price would the product be **a bargain — a great buy for the money**? (Cheap/Good Value)

Plot cumulative frequency distributions for all four. Intersections reveal:
- **Point of Marginal Cheapness (PMC)**: Too Cheap ∩ Expensive — price floor.
- **Point of Marginal Expensiveness (PME)**: Too Expensive ∩ Cheap — price ceiling.
- **Indifference Price Point (IPP)**: Expensive ∩ Cheap — median acceptable.
- **Optimal Price Point (OPP)**: Too Cheap ∩ Too Expensive — minimizes extreme reactions.

Acceptable range: PMC to PME. Requires 100+ respondents for reliability. Hypothetical — stated WTP overstates actual.

#### Gabor-Granger

Direct WTP question at a series of price points. "Would you buy at $X? At $Y? At $Z?" Builds a demand curve. Simpler than Van Westendorp, gives a revenue-maximizing point but less context.

#### Conjoint Analysis (Choice-based)

Respondents choose among product profiles that vary on attributes (price + features + tier). Statistical analysis extracts implicit utility of each attribute level — including price sensitivity AND feature-level WTP. The most quantitatively defensible method.

**Practical setup**:
- 4-6 attributes (one is price, others are features/levels you're considering)
- 3-4 levels per attribute
- 200-300+ respondents
- Choice-based conjoint software (Sawtooth, Qualtrics, etc.)

Use conjoint when you need to know: "What feature should be in the middle tier vs. the top tier?" and "How much can we raise price if we add feature X?"

### Value-metric identification

The **value metric** is the customer-facing variable your price scales with. A good value metric:

| Criterion | Why it matters |
|---|---|
| Scales with customer success | Aligns vendor incentive with customer outcome |
| Easy to understand | Customer can predict their bill |
| Easy to measure | Reduces billing disputes; supports accurate metering |
| Predictable for the buyer | Procurement accepts the model |

Examples by product type:
- Collaboration tool → seats
- API/infrastructure → requests, compute hours, GB
- Marketing automation → contacts, sends
- Payments → transaction volume, $$ processed
- AI agent → resolved tickets, completed workflows, per-spawn

A misaligned value metric is the single most common SaaS pricing mistake. A correct value metric does more work than any other pricing decision.

### Pricing power assessment

How much price can you capture before churn? Test with:
- Cohort retention by entry-price band (do higher-priced cohorts retain at the same rate?)
- NPS / health-score correlation with price tier
- Renewal-time price elasticity (do annual renewals churn more at higher prices?)
- Discount-request frequency in sales motion (rising = approaching price ceiling)

### Customer segmentation by WTP

Different segments have different WTP for the same product. Tiered pricing is the standard mechanism to capture segment WTP differences without explicit price discrimination. Conjoint analysis lets you cluster respondents by utility profile, which often corresponds to natural segments (SMB vs. mid-market vs. enterprise) and informs tier design.

---

## 3. Monetization Strategy Frameworks

### Ramanujam — Monetizing Innovation (2016)

Ramanujam's central claim: most products fail commercially because pricing is decided AFTER the product is built, not designed-in. He categorizes pre-launch pricing into four outcomes:

| Category | Pattern | Outcome |
|---|---|---|
| **Aspirational** | Priced for a small premium segment | Niche success, limited TAM penetration |
| **Boundary-Breaking** | Priced to create a new category | Category leadership, defensible moat |
| **Pricing-as-Marketing** | Priced to signal positioning (cheap = mass; premium = luxury) | Positioning win, margin tradeoff |
| **Unsuccessful** | Pricing not decided until post-launch | Generic failure mode |

**V2V translation**: Pricing belongs in Phase 1 (Intent) and Phase 2 (Decisions), not Phase 4 (Execution). Author the pricing strategy as a `/strategic-bet` with explicit category claim (Aspirational vs. Boundary-Breaking vs. Pricing-as-Marketing) before the product reaches commit.

### OpenView SaaS pricing benchmarks (Poyar)

Annual *SaaS Benchmarks* survey covers pricing models, GTM motion fit, expansion mechanics. Key public findings (2022-2024 reports):

- Usage-based pricing companies grew NRR 10-20 points faster than pure subscription peers in the 2020-2023 cohort.
- Hybrid (base + usage) is the dominant model among $50M+ ARR SaaS, not pure subscription.
- Self-serve + sales-assisted hybrid GTM correlates with the broadest price-band coverage.

### Bessemer State of the Cloud

Tracks public SaaS metrics including ARR multiples on price changes, gross margin by pricing model, NRR distribution. Useful for benchmarking but limited to public/late-stage companies — early-stage references should be Stripe Atlas or ProfitWell.

### 2026 trends (verified observations, not invented numbers)

- **AI-feature pricing experimentation**: Vendors are stratifying — usage-based for inference-heavy features, per-seat for collaborative-AI features, per-outcome for agent products. As of the 2026-06 delta below, the picture has hardened: hybrid (consumption + outcome) is now the standard at 41% adoption (Futurum 1H-2026), and outcome-based pricing for agent products has named live price points. See the 2026-06 Delta Update for the specifics.
- **Usage-based surge**: Stripe + Tunguz reports show usage-based or hybrid pricing growth in new SaaS launches.
- **Per-agent / per-spawn pricing**: Emerging post-Anthropic Skills + plugin marketplace. Replicate, Anthropic API, OpenAI Assistants are real-world references. Margin economics depend heavily on foundation-model pricing (which is itself falling rapidly).
- **Margin compression risk on AI features**: Foundation-model API costs have dropped meaningfully year-over-year. Vendors that priced AI features as a margin-rich add-on are facing customer pressure to repackage as included.
- **Workflow integration as durable differentiation**: When the underlying AI model commoditizes, the workflow integration (agents, automations, data plumbing) is what customers pay for.
- **Per-seat-pricing structural failure in AI-leveraged products**: When AI cuts customer headcount, per-seat ARPU degrades even as outcome value grows — vendor revenue per customer falls while customer ROI rises. The pricing-strategy implication: per-seat is no longer a safe default for AI-leveraged products; consider outcome-based, consumption-based, or platform-bundle alternatives. See `metrics-frameworks` §9 (Per-Seat-Pricing Structural Failure) for the metrics-side view of this shift.

---

## 4. Pricing Power + Pricing Leverage (Helmer's 7 Powers)

Hamilton Helmer's *7 Powers* (2016) catalogs the seven persistent sources of competitive advantage. Each translates directly to pricing power — the ability to charge above commodity price without losing share.

| Power | Pricing translation | Example |
|---|---|---|
| **Scale Economies** | Unit cost falls with volume; you can price below entrants and still earn margin | AWS, Amazon retail |
| **Network Economies** | Product value rises with user count; latecomers face WTP gap | Slack, LinkedIn, Visa |
| **Counter-Positioning** | Incumbents can't match your pricing without cannibalizing themselves | Vanguard vs. active funds; Netflix vs. cable |
| **Switching Costs** | Customers face data/process/relational cost to leave; supports premium renewal pricing | Salesforce, SAP, Snowflake |
| **Branding** | Identity-bound trust premium; lets you price above functional equivalents | Apple, Hermès, Stripe-vs-PayPal |
| **Cornered Resource** | Exclusive access to a critical input (talent, IP, supply); priced like a toll | Pixar (early), TSMC leading nodes |
| **Process Power** | Embedded operational know-how slow to copy; lets you maintain margin while scaling | Toyota Production System, Costco |

**Pricing power vs. market power vs. brand power**:
- Pricing power: can you raise price without losing volume? (this is what 7 Powers measures)
- Market power: do you set price for the category? (rare — usually antitrust-relevant)
- Brand power: one of the 7 powers (Branding), not all of pricing power

**Use this**: Before recommending a price increase, identify which Power supports the increase. If none → the price increase will erode share. If one or more → quantify the headroom.

---

## 5. Pricing Experiments

### A/B testing on price points

**When it works**: Low-stakes, high-volume products (consumer apps, self-serve SaaS at the entry tier). Different prospects can see different prices without sales team or media noise contaminating the test.

**When it breaks**: Low-volume (you need months for statistical significance). High-stakes deals (a single enterprise deal swamps the sample). Public-pricing products (customers will discover the experiment via screenshots, comparison threads, Reddit).

**Statistical-significance note**: For pricing tests, you need enough trials at each price to detect a meaningful conversion-rate delta. At a typical 5% baseline conversion and 20% lift detection, you need ~3,000+ trials per arm. Most SMB SaaS doesn't have that volume per quarter.

### Conjoint analysis for tier design

Conjoint analysis is the statistical method for designing tiers (what feature goes in which tier, what's the right price spread). When you have 200+ survey respondents, conjoint produces a defensible tier structure with WTP for each feature.

### Grandfathering strategy for price increases

When raising prices on existing customers, the standard pattern:
1. Announce the new pricing 30-90 days in advance.
2. Honor old pricing for existing customers for 6-12 months ("grandfathered").
3. New customers pay new price immediately.
4. Migrate grandfathered customers at renewal with a clear value-narrative (new features, expanded support, etc.).

Variants: percentage cap on per-customer increase, multi-year price-lock for high-tenure customers, opt-in early migration with bonus.

### When NOT to A/B test

- Low volume + high stakes (enterprise deals)
- Public pricing page where the test will be discovered
- When the messaging architecture is more important than the price point (the pricing-page narrative carries more conversion weight than the $X figure)
- When pricing is bundled with a launch announcement and you can't separate signals

---

## 6. Common Pricing Mistakes

| Mistake | Failure mode | Diagnostic |
|---|---|---|
| Underpricing relative to value delivered | Most common SMB SaaS mistake. Leaves 30-50% of WTP on the table. | If <10% of prospects push back on price, you're underpriced. |
| Overpricing relative to switching cost | Enterprise sales risk — long deals stall on procurement budget gates. | Median sales cycle is rising; discount requests are rising. |
| Per-seat at scale → discount degradation | Volume discounts erode ARPU/seat at largest accounts; pricing-page price is fiction. | List-to-realized price ratio < 0.6 at top decile. |
| Pricing transparency vs. opacity tradeoff | "Call for pricing" suppresses inbound conversion; published pricing surrenders negotiation room. | Test: hide pricing for a segment, measure inbound velocity. |
| Pricing-page complexity suppresses conversion | More than 3-4 tiers, or comparison tables with 20+ rows, drives bounce. | Pricing-page exit rate > category benchmark. |
| Pricing as a tactical decision | Pricing decided after launch by sales pressure. | No `/strategic-bet` or `/pricing-strategy` document exists at GA. |
| Misaligned value metric | Customer can't predict their bill. | Bill-shock complaints, NRR below cohort baseline. |
| Single-tier pricing in a multi-segment market | Either small accounts churn (too expensive) or large accounts dictate price (too cheap). | Customer-size standard deviation is wide; ARPU is flat. |

---

## 7. Selection Guide

| Situation | Recommended approach | Why |
|---|---|---|
| New product, unknown WTP | Van Westendorp + 5-10 customer interviews | Low cost, directional |
| Feature-price tradeoff decisions | Conjoint analysis | Quantifies feature-level WTP |
| Differentiated product, measurable value | Value-based pricing | Captures fair share of value |
| Established market, clear competitors | Competitive pricing informed by value | Market context matters but should not dominate |
| Large addressable market, low marginal cost | Freemium + paid tiers | Build base, convert power users |
| Variable consumption, clear usage metric | Usage-based with base fee | Aligns price with value, base fee for predictability |
| Multiple segments, single product | Tiered (Good / Better / Best) | Serves segments efficiently with one product |
| Enterprise + self-serve | Hybrid: self-serve tiers + Enterprise (Contact Sales) | Avoids the "Contact Sales" friction for SMB |
| Setting a price floor | Cost-plus (sanity check only) | Never knowingly price below cost |
| AI/agent product, measurable outcome | Outcome-based or per-spawn | Aligns price with model-cost AND customer outcome |

---

## 8. V2V Cross-References

This pack feeds into and depends on adjacent OS material:

- **`business-case` skill** — Pricing assumptions (ARPU, conversion rate, discount rate, expansion rate) are required inputs to a business case. A business case without an explicit pricing-assumption section is incomplete. Cross-reference: `business-case` MANDATORY-INVOCATION includes a pricing-assumptions section.
- **`strategic-bet` skill** — Pricing is a strategic commitment. The bet should declare: pricing model, value metric, price level, segment WTP assumption, success criteria (NRR target, ARPU target), review trigger (when do we revisit?).
- **`pricing-strategy` skill** — Authors the pricing-strategy decision deliverable. This pack is its primary preload reference.
- **`pricing-model` skill** — Authors the actual pricing model with tiers, packaging, features-per-tier. Use this pack's Section 1 Taxonomy and Section 7 Selection Guide as inputs.
- **`gtm-playbooks` knowledge pack** (sibling Q2-2.2) — Pricing structure constrains GTM motion fit. PLG requires published pricing and self-serve checkout; SLG accommodates Contact-Sales and custom pricing; channel motion adds margin allocation complexity.
- **`metrics-frameworks` knowledge pack** (sibling Q2-2.5) — ARPU, ACV, LTV, NRR, gross margin metrics tie directly to pricing decisions. Pricing changes show up in these metrics on a 1-2 quarter lag.
- **`competitive-frameworks` knowledge pack** — Competitive pricing requires competitive intelligence on positioning, tiers, value-metric choices, and discount patterns.

---

## 9. 2026 AI-Era Pricing Considerations

The AI-product wave has shifted pricing economics in five concrete ways. These are observations from public references (Anthropic, OpenAI, Replicate, Stripe, Bessemer 2024-2025 reports), not invented numbers.

### Per-agent / per-spawn pricing models

Post-Anthropic Skills + Claude Code plugin marketplace, per-spawn pricing is an emerging pattern. Examples in production: Anthropic API (per-token), OpenAI Assistants (per-thread + tool-use), Replicate (per-prediction), various agent platforms (per-agent-run, per-workflow-execution). No dominant pattern yet — the design space is open.

**Open question**: When the agent performs N actions per spawn, do you charge per-spawn (predictable) or per-action (aligned but unpredictable)? Hybrid (per-spawn fee + per-action overage) is increasingly common.

### Usage-based pricing for AI inference costs

When the underlying cost is a per-token foundation-model call, usage-based pricing aligns vendor margin with customer behavior. Subscription pricing for inference-heavy features creates margin volatility — heavy users erode margin, light users overpay. Stripe + Bessemer 2024 data show usage-based or hybrid pricing growing as the dominant AI-feature pricing pattern.

### Margin compression on AI features

Foundation-model API costs have dropped meaningfully year-over-year (publicly: OpenAI, Anthropic, Google have all cut API prices multiple times since 2023). Vendors who priced AI features as a high-margin add-on now face customer pressure to repackage as included (no premium) or to lower prices. Pricing-strategy implication: don't lock in an AI feature as a high-margin SKU — design for repricing as inputs commoditize.

### Differentiation through workflow integration

When the AI model commoditizes, the workflow integration (agents, automations, data plumbing, domain context) is what customers pay for. Pricing should reflect the integration value, not the inference cost. This pattern is the AI-era version of "software ate the world, then APIs ate software, then workflows ate APIs."

### Pricing for outcomes rather than tokens

Outcome-based pricing (Section 1) is increasingly viable for AI products because the agent's output is measurable (resolved tickets, completed workflows, generated assets accepted). When you can agree on the outcome metric with the customer, outcome-based pricing maximizes value-capture AND aligns vendor risk with customer success. The harder problem is attribution and measurement contract — get that right before the pricing model. As of the 2026-06 delta, this pattern now has named live price points and even a documented price cut — see the 2026-06 Delta Update below.

---

## 2026-06 Delta Update (as of 2026-06-06)

The May "per-seat fails / outcome-based emerging" thesis now has named live price points, a large-incumbent commitment, AND a documented price decrease signaling competitive compression:

- **HubSpot Customer Agent reportedly dropped to $0.50 per resolved conversation (April 2026, down from $1.00)** — a real price CUT signaling competitive compression in the agent-pricing market. (Caveat: this number should be double-checked against HubSpot's own pricing page before being presented as fact; treat as "reported" until verified.)
- **Intercom Fin: $0.99 per resolved conversation**; **Zendesk** charges per successful AI resolution. These are concrete outcome-metric price points for support-agent products.
- **Adobe** announced outcome-based pricing for its new "Adobe CX Enterprise" AI suite (priced partly on outcomes such as ad campaigns completed) — a large incumbent committing to the outcome model, not just startups.
- **Futurum 1H-2026 buyer survey**: 43% of buyers prefer consumption-based pricing, 27% prefer outcome-based, and **hybrid (consumption + outcome) is now the standard at 41% adoption.** This hardens the "hybrid is the dominant model" finding from the OpenView benchmarks (§3) into the AI-pricing era specifically.

**Strategy implication**: per-outcome pricing for agent products is no longer experimental — it has settled on a "$/resolved conversation" value metric with competitive price points in the sub-$1 range, and the floor is already being tested downward (the HubSpot cut). When designing outcome-based pricing for a support/agent product, benchmark against $0.50-$0.99 per resolved conversation and assume continued downward pressure. Hybrid (base + consumption + outcome) is the defensible default per the Futurum data.

**Sources (2026-06 delta)**:
- https://www.pymnts.com/artificial-intelligence-2/2026/adobe-plans-outcome-based-pricing-for-new-ai-product-suite/
- https://futurumgroup.com/press-release/are-outcome-based-and-hybrid-ai-pricing-models-rewriting-the-vendor-playbook/
- HubSpot / Intercom / Zendesk vendor pricing pages (verify the HubSpot $0.50 figure directly before citing as fact)

---

## 10. Agentic Value-Capture / Outcome-Based Pricing for Agents

**Adapted from**:
- Outcome-based / usage-based pricing literature already cited in this pack (Ramanujam, *Monetizing Innovation*; Nagle & Muller; OpenView / Poyar usage-based benchmarks) applied to the agent case.
- Named 2026 agent outcome-price points (Intercom Fin, Zendesk, HubSpot, Adobe; Futurum 1H-2026 survey) — see the 2026-06 Delta Update sources above.
- Agent unit-economics framing (cost-per-successful-task) — practitioner-synthesis, no single proprietary source.

**Source licence**: Public methodology references; no license restriction on summary + attribution.

**V2V refinements**:
- Bound the pricing value metric explicitly to the agentic metric set in `metrics-frameworks` §9.5 (billing unit = successful task, not a seat or token).
- Added the cost-per-successful-task COGS floor + distribution-not-mean margin discipline.
- Added agent-specific outcome-pricing risks (containment volatility, eval-rubric-as-success-definition against gaming, documented downward price pressure).

---

Per-seat pricing structurally fails for agentic products (§9, and `metrics-frameworks` §9): the agent replaces the seats you used to bill on, so the billing base shrinks as the value grows. The value-capture question for an agent is therefore *what unit of successful work do we charge for?* — and the answer comes straight from the agentic metric set in `metrics-frameworks` §9.5.

**The billing unit is a successful task, not a seat or a token.** Map the value metric to the agentic metrics:

| Value metric | Underlying agentic metric | When it fits |
|---|---|---|
| Per successful task / resolved outcome | task-completion rate | Outcome is discrete + measurable (resolved ticket, completed workflow); both sides agree on "success" |
| Per contained / autonomous task | containment rate | Buyer's value is labor deflected from a human queue |
| Per action + base fee (hybrid) | steps-to-completion | Work varies widely per task; base fee gives predictability |
| Consumption (per-spawn/token) + margin | cost-per-successful-task | Early / uncertain outcome definition; align vendor margin to inference cost |

**Cost-of-goods floor.** Outcome pricing only works if price-per-successful-task > cost-per-successful-task with margin. Because cost-per-successful-task is volatile (model choice, retries, steps-to-completion drift), model the margin on the *distribution*, not the mean — a task that loops 10× can invert the unit economics. Track cost-per-successful-task as the live COGS input (§9 per-agent cost).

**Risks specific to agent outcome-pricing:**
- **Containment volatility** — if you bill per contained task, a model regression that drops containment cuts revenue AND the customer sees more escalations: revenue and quality fall together. Watch the containment counter-metric (reopen / durability).
- **Gaming / attribution** — billing on "successful task" incentivizes loose success definitions. The success criterion must be the eval-set rubric (`metrics-frameworks` §9.5, "Agent evals as acceptance criteria"), auditable by the customer, or the model invites disputes.
- **Downward price pressure** — named live points sit in the sub-$1 "per resolved conversation" range and are already being cut (2026-06 Delta Update). Design for repricing; do not lock the outcome SKU at a high margin.

**Margin formula** (placeholders per `no-estimates.md`):

`gross margin per task = price-per-successful-task − (inference + infra + retry cost) ÷ task-completion rate`

Dividing cost by task-completion rate loads the cost of failed attempts onto the successful (billed) ones. Use `[your rate]` for each input.

**Cross-reference:** `metrics-frameworks` §9.5 (the agentic metric set that becomes the billing unit) and §9 (per-seat structural failure, per-spawn cost).

---

## Sources

- Madhavan Ramanujam and Georg Tacke, *Monetizing Innovation* (Wiley, 2016) — Pre-launch pricing strategy, value-metric design.
- Thomas Nagle and Georg Muller, *The Strategy and Tactics of Pricing* (6th ed., Routledge, 2017) — Comprehensive pricing theory, value-based pricing methodology.
- Hamilton Helmer, *7 Powers: The Foundations of Business Strategy* (Deep Strategy LLC, 2016) — Sources of pricing power.
- Patrick Campbell, ProfitWell / Paddle research (2015-2023) — SaaS pricing benchmarks, freemium conversion rates.
- Kyle Poyar, OpenView Partners *SaaS Benchmarks* and Growth Blog (2018-2024) — Usage-based pricing trends, GTM-pricing fit.
- Peter van Westendorp, "NSS-Price Sensitivity Meter" (ESOMAR Congress, 1976) — PSM methodology.
- Paul E. Green and V. Srinivasan, "Conjoint Analysis in Marketing: New Developments with Implications for Research and Practice" (*Journal of Marketing*, 1990) — Conjoint methodology foundations.
- Bessemer Venture Partners *State of the Cloud* reports (2020-2024) — Public SaaS pricing model distribution.
- Tomasz Tunguz, Redpoint Ventures blog (2018-2024) — Usage-based pricing data, hybrid model evolution.
- Stripe Atlas pricing guides (2020-2024) — Early-stage pricing benchmarks.
