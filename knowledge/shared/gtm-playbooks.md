# GTM Playbooks

**V2V OS pack on go-to-market motions, launch tiers, channel selection, and 2026 GTM landscape.**

---

**Adapted from**:
- Industry-standard GTM methodology (April Dunford "Obviously Awesome" + "Sales Pitch", Bob Moesta JTBD-applied-to-marketing, Reforge GTM curricula) — public methodology
- 2026 Q2 landscape research per V2V refresh survey §5 (Marketing Team) — GEO/LLM-SEO divergence, AI-SDR market dynamics
- V2V Vision-to-Value GTM-as-Phase-3-Commitment framing

**Source licence**: Public methodology references
**V2V refinements**: GTM motions framed as Phase-3 Commitments downstream of Phase-2 strategic-bet decisions; cross-references to launch-narrative-brief skill + messaging-architecture artifact

---

## 1. Purpose

This pack equips PMM agents (`director-product-marketing`, `product-marketing-manager`) with the working vocabulary, decision frames, and 2026-current landscape they need to make GTM choices that hold up against market reality. GTM is a *strategic choice*, not a downstream handoff — the motion you pick determines pricing-model viability, sales-team shape, content investment, and channel-mix economics. This pack is the bench reference for that choice.

Use this pack when authoring GTM strategy, launch briefs, positioning statements, channel plans, sales-marketing alignment proposals, or any commitment that frames *how* a product reaches its market. It pairs with `pricing-frameworks.md` (pricing constrains motion), `competitive-frameworks.md` (positioning informs motion), and the `launch-narrative-brief` / `messaging-architecture` skills (the deliverables this pack feeds).

## 2. GTM Motion Taxonomy

Five canonical motions plus the two hybrid combinations that dominate at scale. The motion question is not "which is best?" — it is "which fits the buyer's purchase behavior, the product's time-to-value, and the unit economics of acquisition?"

### Product-Led Growth (PLG)
- **Fits when**: low-friction signup; users can experience value before talking to anyone; individual-user value precedes team/org value; viral loops embedded in product (sharing, collaboration, output artifacts); freemium or free-trial economics work.
- **Doesn't fit when**: enterprise sales cycle is mandatory (security review, procurement, multi-stakeholder approval); product requires configuration or training to reach first value; ACV demands a sales conversation to justify.
- **Exemplars**: Figma (design collaboration → team upgrade), Notion (individual workspace → team plan), Linear (developer adoption → org rollout), Loom (single-user creator → workspace).
- **Core metrics**: activation rate, time-to-first-value (TTFV), free-to-paid conversion, viral coefficient (k-factor), product-qualified leads (PQLs).

### Sales-Led Growth (SLG)
- **Fits when**: enterprise ACV (>$50K typical floor); multi-stakeholder buying committee; mandatory security/procurement review; product requires implementation; champions need air cover to win internal budget battles.
- **Qualification**: MEDDPICC (Metrics, Economic buyer, Decision criteria, Decision process, Paper process, Implicate pain, Champion, Competition) is the dominant 2026 enterprise framework; BANT is residual for SMB velocity sales.
- **Sales motion shapes**: AE-led (account executive owns deal), SE-supported (solutions engineer for technical validation), BDR-fed (development reps fill top of funnel).
- **Core metrics**: pipeline-to-revenue ratio (3x healthy, 5x conservative), win rate, sales-cycle length, ACV trend.

### Marketing-Led Growth (MLG)
- **Fits when**: educated buyer market; long consideration cycle; content can compound (SEO, thought-leadership, gated assets); demand-gen funnel converts at predictable rates.
- **Engine components**: top-of-funnel content (blog, podcast, video), mid-funnel nurture (email sequences, gated assets), bottom-funnel conversion (demos, free trials, sales handoff).
- **Core metrics**: MQL→SQL conversion rate, content attribution to pipeline, CPL by source, cost-per-pipeline-dollar.

### Community-Led Growth (CLG)
- **Fits when**: developer/practitioner tools; open-source distribution; advocacy economics (champions become evangelists); community-as-moat dynamics.
- **Exemplars**: HashiCorp (Terraform community → enterprise), Hugging Face (ML practitioner community → enterprise inference), Vercel (Next.js community → platform).
- **Core metrics**: community-active-users, contribution velocity (PRs, posts, talks), community-to-customer conversion, advocate NPS.

### Channel / Partner-Led
- **Fits when**: indirect distribution outperforms direct (integrators, resellers, OEM); category requires channel trust (regulated industries, geographic localization); platform marketplaces concentrate buyer demand (AWS Marketplace, Azure Marketplace, Salesforce AppExchange).
- **Channel economics**: typical reseller margin 20-40%, integrator margin 30-50%, OEM royalty 10-25%. Marketplace fee tiers vary by provider (3-15% typical, with private-offer reductions).
- **Core metrics**: partner-sourced pipeline %, partner-influenced pipeline %, partner activation rate, channel CAC vs direct CAC.

### Hybrid: PLG-to-SLG (most common at $1M+ ARR)
The dominant scaling pattern. PLG lands individual or team users; once an account crosses a usage or ACV threshold, sales activates expansion (upgrade tier, multi-team rollout, enterprise contract). Transition mechanics: PQL → AE-assigned account → expansion play. Failure modes: sales handoff feels predatory to PLG users (kills self-serve trust); PLG-funded sales team doesn't have full enterprise muscle (loses to pure SLG competitor in $500K+ deals).

### Hybrid: MLG-to-PLG expansion
Marketing builds the brand and educates the category; product captures the conversion. Common in developer tools (content → docs → signup) and SaaS categories with established budget categories. The risk: marketing-attributed pipeline never matches direct-acquisition pipeline cleanly; attribution gets political.

## 3. Launch Tier Framework

Adapted from Reforge launch curricula. Calibrates investment to launch significance — under-tiering wastes a strategic moment; over-tiering causes campaign fatigue and budget burn.

### Tier 1 — Major product launch
- **Trigger**: new product, new category entry, major repositioning, major pricing-model change.
- **Investment**: full marketing campaign (paid, organic, PR, analyst briefings), launch event (physical or virtual), executive air cover, dedicated sales enablement, customer migration plan if applicable.
- **Budget envelope**: typically 15-30% of annual marketing budget for the campaign.
- **Lead time**: 12-16 weeks for cross-functional coordination (Product, PMM, Marketing, Sales, CS, Support, Legal).

### Tier 2 — Significant feature launch
- **Trigger**: substantial new capability that changes product positioning or unlocks new use cases; pricing-tier addition; new persona target.
- **Investment**: focused campaign (3-5 channels), customer comms (in-app, email, webinar), sales briefing, updated collateral.
- **Budget envelope**: 5-10% of annual marketing budget.
- **Lead time**: 6-8 weeks.

### Tier 3 — Incremental feature launch
- **Trigger**: meaningful enhancement to existing capability; quality-of-life improvement; integration addition.
- **Investment**: release notes, changelog post, in-app messaging, support enablement, optional blog post.
- **Budget envelope**: minimal — internal-resource cost only.
- **Lead time**: 2 weeks.

### Tier 0 — Silent launch / beta (V2V refinement)
- **Trigger**: capability that needs production validation before being a public commitment; controlled rollout to limited cohort; capability whose marketing claim isn't yet supportable.
- **Investment**: zero external marketing; internal-only enablement to selected sales/CS reps; analytics instrumentation for validation.
- **Why it exists**: V2V's commitment-discipline view holds that *announcing a thing is a commitment*. Tier 0 lets the org ship the artifact without committing the narrative. Promotion to Tier 1/2/3 happens after validation, not before.

**Cross-functional coordination requirements** scale with tier. Tier 1 requires named owners in Product, PMM, Marketing, Sales Enablement, CS, Support, Legal, and Comms. Tier 3 needs Product + PMM only.

## 4. Channel Selection Framework

Channel choice is a portfolio decision — no single channel scales monolithically without saturating or diminishing-returns. The decision frame has four axes:

### CAC by channel (2026 benchmarks, public sources)
- **Paid search (Google, Bing)**: predictable, ranges $50-$500 CPL for B2B SaaS depending on category competitiveness; CAC payback 9-18 months typical.
- **Paid social (LinkedIn, Meta)**: LinkedIn higher CPL ($150-$800) but stronger B2B intent; Meta cheaper ($30-$200) but lower B2B fit.
- **Content / SEO / organic**: high CAC upfront (content investment 6-18 months to payback), low CAC at scale; defensible.
- **Outbound sales (SDR/BDR-driven)**: high CAC ($300-$2000 per qualified meeting), justifiable only at $20K+ ACV.
- **Partnerships / channel**: variable CAC depending on partner economics; often most efficient for international expansion.
- **Events / field**: high cost-per-attendee ($500-$5000) but quality conversion at enterprise level.

### Time-to-conversion by channel
Paid search and intent-based channels convert fastest (days to weeks). Content and SEO convert slowest but compound. Outbound sales sits in middle. Events have long tails (deals close 3-12 months post-event).

### Scalability vs. saturation
- **Scalable to high spend without diminishing returns**: paid search at the margin (until competitor bidding saturates), content (compounds), partnerships (until partner bandwidth caps).
- **Saturate quickly**: niche paid social audiences, narrow keyword sets, single-event reliance.

### Multi-touch attribution implications
First-touch attribution under-credits content and SEO; last-touch under-credits brand and demand-gen; multi-touch models (linear, time-decay, U-shape, W-shape) each carry political weight. The 2026 reality: most orgs run *blended attribution* — accept that no single model is correct, triangulate with marketing-mix modeling (§7) for strategic decisions, use multi-touch for tactical optimization.

## 5. Sales-Marketing Alignment

The perennial GTM org dysfunction. When sales and marketing disagree on lead quality, attribution, or handoff timing, deals stall in the funnel and both functions blame each other. Mechanisms that work in 2026:

### SLA-based handoffs
Document the MQL → SQL → Opp transition with explicit definitions:
- **MQL**: marketing-qualified lead — meets demographic + behavioral criteria (e.g., target persona, engaged with 2+ assets in 30 days).
- **SQL**: sales-qualified lead — accepted by sales after BDR or AE qualification; has confirmed pain, budget signal, timeline signal.
- **Opp**: opportunity — sales-stage entry; sales owns from here.

SLAs typically specify response time (e.g., MQL contacted within 24h), rejection-with-reason if sales declines an MQL, and feedback-loop cadence to refine MQL criteria.

### Account-based marketing (ABM) coordination
For enterprise GTM, marketing and sales co-target named accounts. Marketing runs air cover (ads, content syndication, events) tuned to the named account list; sales runs ground game (outbound, champion-building). Tier accounts into 1:1 (top 20, custom programs), 1:few (mid-50, segment programs), 1:many (long tail, broad campaigns).

### Pipeline review cadence
Weekly pipeline review with marketing-sourced vs marketing-influenced vs sales-sourced pipeline broken out. Monthly closed-loop: which lead sources converted at what rate, what's the win-rate trend by segment.

### Closed-loop feedback
Sales-back-to-marketing on lead quality, common objections, competitive losses. Marketing-back-to-sales on content engagement (which assets champions read before deals close). The loop is operationalized in CRM + marketing automation; the cultural part is the harder part.

## 6. Positioning + Messaging

Cross-reference to the `messaging-architecture` skill for the artifact deliverable. This section captures the methodology that informs the artifact.

### April Dunford 10-step positioning process
From *Obviously Awesome* (2019) and reinforced in *Sales Pitch* (2023):
1. Understand customers who love your product.
2. Form a positioning team (cross-functional, not just marketing).
3. Align your understanding of true competitive alternatives (what customers would do if you didn't exist).
4. Isolate your unique attributes.
5. Map attributes to value themes.
6. Determine who cares a lot about that value.
7. Find a market frame of reference (the category context).
8. Layer on trends (relevant macro-context that lifts your position).
9. Capture your positioning in a documented positioning statement.
10. Share the positioning across the company.

### "Sales Pitch" five-act narrative structure
From Dunford 2023 — what works in deal-closing conversations:
1. **Insight** — the surprising market truth that reframes how the buyer should think.
2. **Alternative approaches and their flaws** — competitive alternatives the buyer is considering, and where each falls short.
3. **Perfect-world solution** — the criteria for what an ideal solution would do.
4. **Introduce your product** — mapped against the perfect-world criteria.
5. **Proof** — customer evidence, demos, ROI data.

### Category-creation vs. category-leadership vs. niche positioning
- **Category creation**: "We're a new category" — high risk, high reward; requires education investment and analyst validation. Examples: Drift (conversational marketing), Snowflake (cloud data warehouse).
- **Category leadership**: "We're the best at the established category" — works when category is large and you have a real claim to leadership.
- **Niche positioning**: "We're the best for [specific segment]" — works when broader competition dominates the general category but ignores a defensible niche.

### Counter-positioning and market re-segmentation
Counter-positioning (per Hamilton Helmer, *7 Powers*) is when an incumbent can't follow you without damaging its existing business. Examples: Netflix DVD-by-mail (Blockbuster couldn't follow without cannibalizing retail), Tesla direct-sales (dealers were sacred to incumbents). When you find a counter-position, the moat is the incumbent's own constraints.

## AI-SDR Market Dynamics

**Adapted from**: Public 2025-2026 industry coverage of the AI-SDR pure-play category — the 11x reputational collapse (Q1 2025), the Artisan "Stop hiring humans" billboard backlash (Q2 2025), and the Salesloft-Clari consolidation (Q3 2025). Sources SRC-243, SRC-307, SRC-308, SRC-379, SRC-311.
**Source licence**: per-source terms (public coverage; no formal OSS license). Dated 2025-2026; verify each event against primary coverage before citing externally.
**V2V refinements**: reframed the collapse as a *channel-economics* lesson about the outbound/SLG motion (§2, §4), not a vendor-scandal narrative; separated the market-dynamics layer (this section) from the deliverability-engineering depth (`deliverability-engineering.md`) and the deal-execution / qualification-under-AI angle (`sales-methodology.md`); added the build-vs-buy AI-SDR decision frame and the reputation-vs-volume tradeoff for GTM-motion choice.

> This section is the **market-dynamics + channel-economics** layer that `sales-methodology.md` and `sales-operations.md` cross-reference for "the outbound / AI-SDR channel angle." It deliberately does **not** restate the sender-reputation engineering (owned by `deliverability-engineering.md`) or the deal-execution / qualification-under-AI angle (owned by `sales-methodology.md`).

### AI-SDR is a cost-structure lever on the outbound motion, not a motion of its own

The first framing error is treating "AI-SDR" as a new GTM motion. It is not. It sits *inside* the outbound/SLG motion (§2, "Sales-Led Growth" → BDR-fed shape) and shows up on exactly one line of the channel framework (§4, "Outbound sales (SDR/BDR-driven)" — the $300-$2000-per-qualified-meeting line). The pure-play category's promise was narrow and purely economic: collapse that outbound CAC by replacing SDR labor with autonomous agents. That means the motion-fit question comes *first* — if outbound doesn't fit your buyer (per the §2 SLG fit test), a cheaper outbound engine does not make it fit. It just makes a mis-fit motion cheaper to run into the ground.

### The pure-play rise-and-collapse (2024-2025)

The pure-play AI-SDR category — vendors selling fully-autonomous "AI digital worker" outbound as a standalone product — rose fast in 2024 and re-priced sharply through 2025:

- **11x (Q1 2025)** — the highest-profile pure-play hit a reputational crisis over public scrutiny of revenue and customer-quality claims. The operationally relevant failure was that autonomous-send volume outran sender reputation across the customer base (the mechanism lives in `deliverability-engineering.md`).
- **Artisan "Stop hiring humans" billboards (Q2 2025)** — a positioning controversy that converted into a buyer-side question about whether the underlying outbound was even landing in inboxes, accelerating the human-in-loop consensus.
- **Salesloft-Clari consolidation (Q3 2025)** — the signal that the **standalone-outbound-tool category was folding into the broader RevOps / sales-engagement stack**. AI-SDR capability moved from a category to a *feature* inside platforms that already own the workflow, the data, and the deliverability surface.

The through-line is a category re-classification: what was pitched as a durable standalone software category in 2024 was, by end-2025, absorbing into RevOps as an assistive feature. Reported logo churn for pure-play vendors ran high (the landscape survey put it in the ~50-70%/yr range; treat as directional and verify before external citation). For a GTM buyer, high logo churn in a vendor category is itself a signal — you are underwriting the vendor's survival, not just the tool's output.

### The durable posture: human-in-loop, reputation-bounded

The consensus 2026 model is **AI-assist inside existing sales-engagement workflows with a human send-approval gate**, not full automation. The market-dynamics reason (the engineering reason is in `deliverability-engineering.md`, don't restate here): the binding constraint on the outbound channel was never SDR *labor cost* — it was **sender reputation and reply-rate**, and volume automation degrades exactly those. So the economic thesis inverted. Automating the cheap input (labor) while blowing out the scarce input (reputation) is negative-sum. The reputation-vs-volume tradeoff is the durable lesson: on the outbound channel, reputation is the constraint and volume is the variable, not the reverse.

### Build-vs-buy AI-SDR for GTM motion design

| Option | When it fits | Channel-economics caveat |
|---|---|---|
| **Buy a pure-play AI-SDR** | Rarely first choice in 2026 — only if it demonstrably clears the reputation-vs-volume bar on your domains | High category logo churn; reputation risk accrues to *your* sending domains, not the vendor's; you inherit the switching cost when the vendor consolidates or fails |
| **Buy AI-assist inside your incumbent sales-engagement platform** | Default for most orgs post-Salesloft-Clari — the capability is folding into platforms you already run | Cost is a feature uplift, not a new CAC line; deliverability stays where the platform already manages it |
| **Build in-house AI-assist** | Only with real deliverability-ops muscle (see `deliverability-engineering.md` for what that requires) | You own reputation, warmup, and monitoring end-to-end; do not build without that discipline |

The GTM-motion takeaway: AI-SDR changes the *cost structure* of an outbound motion; it does not change the *motion-fit* decision. Run the §2 fit test and the §4 channel economics first. If outbound is the right motion, AI-assist inside your engagement stack is the 2026 default; a pure-play standalone is the exception that must clear the reputation bar. Cross-references: `deliverability-engineering.md` (the sender-reputation / 5pp-gap engineering), `sales-methodology.md` §"AI-Assisted Deal Execution" (qualification-under-AI), `sales-operations.md` (where the outbound channel rolls up in forecasting).

## 7. 2026 GTM Landscape

Material shifts in the last 12 months that change the GTM playbook. From V2V refresh survey §5 (Marketing Team, 2026 Q2).

### GEO / LLM-SEO divergence
The overlap between Google top-10 organic results and AI-engine citations (ChatGPT, Perplexity, Claude, Google AI Overviews) dropped from ~70% to **<20%** in the past 12 months. Implications:
- SEO and GEO (Generative Engine Optimization) are now distinct disciplines with distinct deliverables.
- **llms.txt deployment** — a new file at site root analogous to robots.txt, declaring content-licensing terms and AI-crawl preferences. Adoption climbing rapidly.
- **Schema markup** — structured data (JSON-LD) matters more than ever; AI engines lean heavily on schema for citation extraction.
- **AutoGEO rewriting** — emerging tooling category that rewrites existing content for AI-engine optimization (clearer claims, attribution, citation-friendly formatting).
- Cross-reference: `geo-playbook.md` pack (sibling) and `/llm-seo` skill.

### AI-SDR category (pointer)
The category that promised to replace BDRs/SDRs with AI agents had a messy 2024-2025 and re-priced into a RevOps feature. Full treatment — the pure-play rise-and-collapse (11x, Artisan, Salesloft-Clari), the human-in-loop durable posture, and the build-vs-buy / reputation-vs-volume channel economics — is in the dedicated **§ AI-SDR Market Dynamics** above. Deliverability engineering depth lives in `deliverability-engineering.md`; the qualification-under-AI angle lives in `sales-methodology.md`.

### AI-native RFP
Arphie and Tribble are decimating Loopio and Responsive in the RFP-response market. Reported cycle-time drops: 17.5 hours → 6 hours per RFP. For GTM teams selling enterprise, RFP turnaround is becoming a competitive vector — slow RFP response loses deals on velocity alone.

### Marketing Mix Modeling (MMM) re-emergence
**Google Meridian** (open-source, 2025) and **Meta Robyn** (open-source, 2022) have collapsed what used to be a six-figure consulting engagement into work a single ops engineer can run in-house. Drivers:
- Cookie deprecation made multi-touch attribution unreliable.
- Privacy regulations (GDPR, CCPA, state laws) constrained behavioral tracking.
- AI/ML accessibility made econometric modeling practical for non-PhD teams.

The 2026 GTM team that doesn't run MMM (or equivalent) is making blind portfolio decisions on channel spend.

## 8. GTM Sequencing per V2V Phase Model

GTM choices live across the six V2V phases. Mapping each:

| Phase | GTM Activity | Artifact / Skill |
|---|---|---|
| **1. Intent** | Market segmentation hypothesis, positioning hypothesis, target-persona definition | `/market-segment`, `/positioning-statement` (hypothesis form) |
| **2. Decisions** | Strategic bet on GTM motion (PLG vs SLG vs MLG vs hybrid); pricing-model decision (constrains motion); ICP lock-in | `/strategic-bet`, `pricing-frameworks.md` |
| **3. Commitments** | Launch-narrative-brief authoring; launch-tier classification; channel-mix commitment; messaging-architecture lock | `/launch-narrative-brief`, `/messaging-architecture`, `/launch-plan` |
| **4. Execution** | Campaign execution; sales enablement shipping; content shipping; channel activation | `/campaign-brief`, `/sales-enablement` |
| **5. Outcomes** | Measurement against North Star + GTM-specific metrics (pipeline, conversion, CAC, payback) | `/value-realization-report` |
| **6. Learning** | Win/loss analysis; GTM postmortem; positioning health check; channel-mix retrospective | `/outcome-review`, `/retrospective` |

The pattern that breaks orgs: doing Phase 4 (campaign execution) before Phase 2 (motion decision) is settled. Marketing ends up running a PLG-style content engine while sales runs an enterprise motion — the funnel doesn't connect.

## 9. Common GTM Failures

The failures I see most often, named so the org can recognize and resist them:

### PLG-when-you-need-SLG
Founder bias — "if I built it well, users will come." Works for products with clear individual-user value and viral mechanics; doesn't work when the buyer is a CISO/CFO/CIO making a six-figure procurement decision. Tell: signup volume looks healthy, ACV is anemic, deals stall at security review.

### SLG-when-you-need-PLG
Enterprise-sales motion against an individual-use-case product. Tell: AEs complaining that "leads don't have budget," CAC blowing past LTV, sales-cycle length growing instead of shrinking.

### Launch-tier inflation
Every launch treated as Tier 1. Campaign fatigue inside the org (no signal-to-noise for sellers and customers), budget burn, declining campaign performance as audience habituates. Tell: every quarter has a "major launch"; press / analysts stop responding.

### Positioning-by-feature-list
"Here's everything we do" — no clear *what we are NOT* boundary. The buyer can't slot the product into their mental category, can't compare it cleanly to alternatives, can't justify the decision internally. Tell: sales calls drift into feature-by-feature comparison instead of value-frame conversation.

### Channel-of-the-month chasing
Re-platforming GTM motion every 6 months. "We're a PLG company" → "actually we need enterprise sales" → "no, content is our channel" → "let's try ABM." Each pivot has a 6-12 month investment cost before it pays back; chronic re-platforming means none of them ever do. Tell: leadership-team channel-mix discussion looks completely different quarter-to-quarter.

### MQL-as-vanity-metric
Marketing reports thousands of MQLs; sales reports they're all unqualified. The MQL definition has drifted from what sales can convert. Tell: MQL→SQL conversion rate <20% and the marketing-sales SLA hasn't been refreshed in 6+ months.

## 10. V2V Cross-References

- **`launch-narrative-brief` skill** — the Phase-3 launch-strategy deliverable. Pulls heavily from §3 (launch tiers) and §6 (positioning).
- **`messaging-architecture` skill** — the durable messaging artifact. Operationalizes §6.
- **`partnership-architecture` skill** — when GTM motion includes a partner channel (§2 channel-led, §4 partnership-economics).
- **`pricing-frameworks.md` pack** (sibling Q2-2.1) — pricing structure determines viable GTM motions. Read together.
- **`competitive-frameworks.md` pack** (sibling Q2-2.7) — competitive positioning informs motion choice. Read together.
- **`geo-playbook.md` pack** — companion deep-dive on §7 GEO/LLM-SEO mechanics.
- **`/strategic-bet` skill** — Phase-2 decision artifact where GTM-motion choice is committed.
- **`/launch-readiness` skill** — Phase-3 gate that validates GTM commitments before Phase-4 execution.

---

**📣 Director of Product Marketing's note**: I treat this pack as a working bench reference, not a final word. The 2026 landscape section especially will date — re-validate the AI-SDR, GEO, and MMM claims each refresh cycle. The motion taxonomy and Dunford methodology are stable; the channel economics shift quarterly. When in doubt, escalate the GTM-motion call to a Phase-2 strategic bet rather than letting it drift in as a Phase-3 default.
