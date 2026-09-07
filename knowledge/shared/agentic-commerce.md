---
name: agentic-commerce
owner: bizdev
consumers: [bizdev, director-product-marketing]
sensitive: false
---

# Agentic Commerce

**V2V OS pack on the 2026 agentic-commerce landscape — agent-led purchasing, the payment/checkout protocol stack, machine customers, and the BD / GTM / partnership implications of selling into (and through) AI agents.**

---

## Attribution

**Adapted from** (all dated; verify before citing as fact — this is a fast-moving surface):
- Google Cloud, "Announcing Agent Payments Protocol (AP2)" — cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol (published 2025-09-16; 60+ launch partners). Mandate-chain / verifiable-credential model.
- Stripe Newsroom, "Stripe powers Instant Checkout in ChatGPT and releases Agentic Commerce Protocol codeveloped with OpenAI" — stripe.com/newsroom/news/stripe-openai-instant-checkout. ACP open standard + Shared Payment Token (SPT) primitive. Spec site: agenticcommerce.dev.
- OpenAI, "Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol" — openai.com/index/buy-it-in-chatgpt/.
- Visa, "Intelligent Commerce" — visa.com/en-us/solutions/intelligent-commerce; Visa "Trusted Agent Protocol."
- Mastercard, "Agent Pay" / "Agent Pay for Machines" + Agentic Tokens — mastercard.com press 2026-06.
- Gartner, "Machine Customers" research line + "60% of brands will use agentic AI… by 2028" (newsroom 2026-01-15) and "Optimize Product Data for Agentic Commerce" (Jan 2026). Gartner numbers are predictions — attribute, do not present as realized fact.
- Forter "Trusted Agentic Commerce Protocol (TACP)"; Coinbase/Ethereum x402 (A2A x402 extension) for stablecoin agent payments.

**Source licence**: Public vendor announcements + analyst predictions; per-source terms. No formal OSS license on the announcements; AP2/ACP/x402 specs are open and published on GitHub (goo.gle/ap2, agenticcommerce.dev, google-a2a/a2a-x402).

**V2V refinements**:
- BD/partnership lens — frames protocol adoption as a Phase-2 strategic-bet / Phase-3 channel-commitment decision, not an engineering detail.
- Cross-references `gtm-playbooks.md` (§2 channel-led motion → "agent channel"), `pricing-frameworks.md` (§9 pricing-for-agents), `partnership-models.md`, and ET `a2a-architecture.md` / `mcp-architecture.md` / `agent-identity.md` (the technical substrate the BD lens sits on top of).
- Marketing-selection complement (§5.6): reframes Gartner's "Optimize Product Data for Agentic Commerce" (Jan 2026) recommendation as an operational feed/offer/merchant-trust optimization job distinct from GEO citation, paired with the `competitive-frameworks.md` §12.5 positioning consequence.
- Date-stamp-and-verify discipline applied to every vendor/protocol fact (this surface moves monthly).

> ⚠️ **Verify-before-citing.** Every protocol name, partner list, fee figure, and date below is dated to a 2025-09 → 2026-06 source. The agentic-commerce stack is consolidating in real time (protocols merging, fee structures changing, partners shifting). Treat every specific as "reported as of [date]" and re-validate at each refresh cycle before presenting to a customer or in a deliverable.

---

## 1. Purpose & When to Use

This pack equips `bizdev` (and `director-product-marketing`, consulted) to reason about a structural shift: **AI agents are becoming a buying surface and a buyer.** When a customer's purchase is initiated, negotiated, and settled by an AI agent rather than a human clicking "buy," the BD questions change — which agent platforms become channels, which payment/checkout protocols to adopt, how partnerships and marketplace economics shift, and how products must expose themselves to be "agent-legible."

Use this pack when the task touches: AI shopping agents as a distribution channel; agent-to-agent or agent-initiated purchasing; agentic checkout / payment protocols (AP2, ACP, Visa/Mastercard agent rails, x402); machine customers as a buyer segment; or the partnership/channel/marketplace implications of any of the above. It is a BD/GTM bench reference, **not** a payments-engineering spec (that's `a2a-architecture.md` + `mcp-architecture.md`) and **not** a security/identity control set (that's `agentic-security.md` + `agent-identity.md`).

## 2. What "Agentic Commerce" Means (the shift)

Traditional e-commerce was built for humans: the business controls the interface and the payment surface; the human browses, compares, and clicks. **In agentic commerce the agent sits between the business and the consumer** — it carries the buyer's identity, payment method, and purchase context into the transaction, and may discover, compare, negotiate, and settle on the buyer's behalf (Stripe/OpenAI framing, 2026).

Two distinct BD-relevant patterns:
- **Agent-as-buying-surface (human present)** — the agent is a new storefront/channel. Example: ChatGPT Instant Checkout (Etsy live, Shopify merchants rolling out — Stripe/OpenAI, 2026). The human is in the loop; the agent is the discovery+checkout UI.
- **Agent-as-buyer / machine customer (human delegated or absent)** — the agent transacts under pre-authorized rules ("buy concert tickets the moment they go on sale, under $X"). This is Gartner's "machine customer" line: a nonhuman economic actor that obtains goods/services in exchange for payment. Far larger structural implication, earlier-stage adoption.

The BD takeaway: these are **two different channel/segment bets** with different protocol, pricing, and partnership consequences. Don't collapse them.

## 3. The Protocol & Standards Landscape (dated — verify)

The stack is consolidating around a few open protocols plus the card-network rails. As of 2026-06, no single winner; expect convergence.

| Protocol / initiative | Owner(s) | What it does | Status (as of) |
|---|---|---|---|
| **AP2 (Agent Payments Protocol)** | Google + 60+ partners (Mastercard, Amex, PayPal, Adyen, Worldpay, Coinbase, Salesforce, ServiceNow, Etsy, Intuit…) | Payment-agnostic trust layer; extends A2A + MCP. **Mandate chain**: Intent Mandate → Cart Mandate → Payment, each a cryptographically-signed verifiable credential → non-repudiable audit trail (authorization / authenticity / accountability). Supports cards, bank transfer, stablecoins. | Announced 2025-09-16; open spec on GitHub (goo.gle/ap2) |
| **ACP (Agentic Commerce Protocol)** | Stripe + OpenAI (open standard) | Merchant↔agent integration standard. **Shared Payment Token (SPT)**: lets an agent (e.g. ChatGPT) initiate payment scoped to a specific merchant + cart total without exposing buyer credentials. One integration → sell through agents; merchant keeps control of catalog, brand, fulfillment. Works with non-Stripe processors. | Launched ~2026-02 (Instant Checkout); spec at agenticcommerce.dev |
| **Visa Intelligent Commerce** + **Trusted Agent Protocol** | Visa | Enables AI agents to transact on Visa rails; agent authentication for merchants. | Initiative 2025; Trusted Agent Protocol ~2025-10 |
| **Mastercard Agent Pay** / **Agent Pay for Machines** + **Agentic Tokens** | Mastercard | Agent-scoped credentials ("Agentic Tokens") with programmable spend controls; machine-to-machine continuous payments across cards/accounts. | Agent Pay 2025; "for Machines" 2026-06 |
| **A2A x402 extension** | Google + Coinbase, Ethereum Foundation, MetaMask | Production stablecoin/crypto rail for agent-to-agent payments; extends AP2 core constructs. | 2025-09 |
| **TACP (Trusted Agentic Commerce Protocol)** | Forter | Fraud/trust layer for agent transactions; complements AP2. | 2025 |

**BD reading of the landscape**: the card networks (Visa, Mastercard) and the AI platforms (OpenAI, Google) are racing to **set the standard** — and the AI platforms are recruiting payment incumbents as partners rather than disintermediating them (Mastercard, Amex, PayPal, Adyen all appear across both AP2 and the network initiatives). The likely 2026-2027 shape: a small number of interoperable open protocols (AP2/ACP converging on the trust+token primitives) running on top of the existing card rails, with stablecoin rails (x402) as a parallel track. **Pick protocols for interoperability, not for a single platform bet** — "one integration, many agents" (ACP's pitch) is the durable posture.

## 4. The Machine Customer (segment lens)

Gartner's "machine customer" framing is the larger structural bet: by their projection, machine customers become a material buyer segment this decade (Gartner predictions — attribute as prediction, not fact). For BD this reframes ICP:
- **The buyer may not be human.** Product data, pricing, and APIs must be **agent-legible** — structured, queryable, comparable by a machine. A catalog optimized for human persuasion (lifestyle imagery, emotional copy) is invisible to an agent that filters on structured attributes + price + availability (cf. Gartner "Optimize Product Data for Agentic Commerce," Jan 2026).
- **Loyalty and brand work differently.** An agent optimizing on the buyer's stated constraints ("white running shoes, under $X, in stock") is a far more rational, lower-switching-cost buyer than a human. Brand premium and emotional positioning erode at the agent layer; structured value (price, spec-fit, availability, return terms) wins. This is a `pricing-frameworks.md` §9 problem too: per-seat/brand-premium logic weakens when a machine is the buyer.
- **B2B procurement is an early adopter.** AP2's own examples cite autonomous procurement (Google Cloud Marketplace, auto-scaling software licenses). Agent-led B2B procurement is a plausible early machine-customer beachhead — relevant to any OS product sold through a marketplace.

## 5. BD / GTM / Partnership Implications (the core of this pack)

### 5.1 New channel: the agent platform
AI assistants (ChatGPT, Gemini, and others) are becoming storefronts. Treat "agent platforms" as a **channel-led motion** (`gtm-playbooks.md` §2): the BD job is to evaluate which agent platforms concentrate your buyers' demand, what the integration cost is (one ACP/AP2 integration vs. per-platform), and what the channel economics are (see 5.3). The channel-selection discipline in `gtm-playbooks.md` §4 applies — agent channels saturate, have their own CAC, and shouldn't be chased monolithically.

### 5.2 Product must become agent-legible
A pre-BD readiness gate: can an agent discover, compare, and transact your product? This requires exposing catalog/pricing/checkout via the agent-facing protocols (ACP integration, structured product data, MCP/API surface). BD should flag this as a **partnership prerequisite**, not an afterthought — "we can't be in the agent channel until the product is agent-legible" is a roadmap dependency to coordinate with `vp-product` / `product-manager` (the same way a channel partnership has integration prerequisites).

### 5.3 Channel economics & the disintermediation risk
- **Take rates exist.** Agent-checkout channels carry fees (e.g., reported ~4% on ChatGPT Instant Checkout per third-party retailer guides — *verify against the platform's own terms before citing*). Model the agent channel's CAC + take-rate against direct, exactly as `gtm-playbooks.md` §4 does for any channel.
- **Disintermediation / loss of customer relationship is the strategic risk.** When the agent owns discovery and checkout, the merchant risks losing the direct customer relationship, the data, and the brand surface. ACP's explicit counter-pitch is "merchant retains the customer relationship + brand control + fulfillment." **BD must read the fine print on customer-data ownership and re-marketing rights in any agent-channel partnership** — this is the agentic-commerce analog of the classic marketplace-vs-direct tension. (Cross-ref `partnership-models.md` on dependency-creating terms; this is exactly the `bizdev` anti-pattern "dependency-creating terms → risk at scale.")

### 5.4 Partnership & ecosystem mapping
The agentic-commerce ecosystem is a multi-sided BD map: AI platforms (demand aggregators), payment networks (rails), PSPs/processors (Stripe, Adyen, Worldpay, Checkout.com), trust/fraud layers (Forter), and identity providers (Okta/Auth0, 1Password). For an OS product, the BD questions are: which layer are we, who do we need to partner with to be transactable, and which standards bodies/consortia (FIDO Alliance for verifiable credentials; the AP2/ACP open-spec communities) should we track or join. The 60+-partner AP2 roster is itself a partnership-target map.

### 5.5 Pricing-for-agents (cross-ref, do not duplicate)
Pricing belongs to `pricing-frameworks.md` §9 (per-agent/per-spawn, outcome-based, margin compression). The agentic-commerce-specific addition: **when a machine is the buyer**, value-metric and brand-premium pricing logic weakens, and structured/outcome pricing strengthens. Author pricing in `pricing-frameworks.md`; reference it here.

### 5.6 Feed & offer optimization — getting an agent to *select and transact* you (not just cite you)

§4 and §5.2 establish that a product must be **agent-legible** to be discoverable. This subsection is the operational marketing complement: once you are legible, the next lever is being **selected and transacted**. Being *cited* by an AI engine in the research phase (a GEO/LLM-SEO problem — see `competitive-frameworks.md` §12.1 and the `llm-seo` skill) is a different job from being the offer an agent actually *picks and buys* at the transaction moment. This is the marketing-owned half of agent-channel readiness, distinct from BD channel structuring (§5.3) and pricing (§5.5).

**The shift in what "conversion optimization" means.** When a human shops, merchandising optimizes for persuasion — imagery, copy, urgency, social proof. When an agent shops, it filters and ranks on **structured attributes**. The agent's "add to cart" decision is a function of machine-readable inputs, so the marketing work moves from persuasion to **data quality and completeness** (cf. Gartner "Optimize Product Data for Agentic Commerce," Jan 2026 — a prediction/recommendation, attribute as such).

**What an agent weighs at selection (the feed-optimization surface):**
- **Structured product data as ranking inputs** — title, category, unambiguous attributes (size, color, material, spec), GTIN/identifiers, and rich structured descriptions. Gaps or ambiguity here make you unrankable, not just less persuasive. An attribute a human infers from a photo must be an explicit field for an agent.
- **Availability & fulfillment signals** — real-time in-stock status, ship-time/delivery window, and fulfillment reliability. An agent optimizing on a buyer's constraint ("in stock, delivered by Friday") filters out anything that can't assert it in structured form.
- **Price and total-cost clarity** — the machine-comparable price including shipping/fees where the protocol exposes them; hidden or late-surfaced costs read as missing data.
- **Return terms & policy as structured fields** — return window, restocking, warranty. A more rational (lower-switching-cost) agent buyer weighs these explicitly where a human often ignores them.
- **Merchant-trust signals** — verified-merchant status, the trust/fraud attestations the rails expose (e.g. Visa Trusted Agent Protocol, Forter TACP — §3), review/rating aggregates in machine-readable form. Trust becomes a ranking input, not a brand halo.

**Feed freshness/accuracy is a conversion lever, not a hygiene task.** In human commerce a slightly stale feed costs a bounce; in agentic commerce it costs the transaction outright — an agent that finds a price or stock mismatch at checkout will drop the offer and pick the next-best structured match, with no human to forgive the discrepancy. Feed accuracy and update cadence therefore move from back-office hygiene to a front-line conversion metric the marketing/PMM owner should track (feed-error rate, attribute-completeness %, stock-accuracy at transaction).

**Where this sits.** This is a `director-product-marketing` / marketing operational responsibility that pairs with the BD channel decision (§5.3) and the agent-legibility readiness gate (§5.2). The positioning consequence — how competitive *positioning* changes when a machine compares offers on structured attributes and brand premium erodes — lives in `competitive-frameworks.md` §12.5 ("Positioning When the Buyer Is an Agent"); reference it, don't duplicate it here.

> `[pending next-harvest]` — a transaction-primary deep-dive (the exact per-protocol feed/catalog spec each rail requires: ACP product-feed schema, AP2 cart-mandate line-item fields, the specific merchant-trust attestation each network validates) is **not yet supported by in-pack sources**. When a future harvest adds the primary spec docs, expand this subsection with the protocol-specific feed field maps. Do not add a live forward cross-reference to that content until it exists.

## 6. Decision Frame: should we play in agentic commerce? (BD checklist)

A Phase-2 strategic-bet frame (use `/strategic-bet`):
1. **Is our buyer becoming an agent, or buying through one?** (segment bet — §2/§4). If neither is plausible in our category in 18-24 months, log "monitor, don't build."
2. **Is our product agent-legible, or could it be?** (§5.2 readiness gate). If not, the bet is a roadmap dependency first.
3. **Which protocols give us interoperability?** (§3). Prefer "one integration, many agents" (ACP/AP2) over a single-platform bet.
4. **What are the channel economics vs. direct?** (§5.3 — take rate, CAC, customer-data ownership).
5. **What's the disintermediation risk and how do we structure against it?** (§5.3 — data/relationship/brand retention terms). 
6. **Who do we need to partner with to be transactable?** (§5.4 ecosystem map).
7. **Success criteria + review trigger** — agent-sourced revenue %, agent-channel CAC vs direct, customer-data-retention terms held. Review when a protocol consolidates or a major platform shifts (this surface moves monthly — set a short review cadence).

## 7. V2V Cross-References

- `gtm-playbooks.md` — §2 channel-led motion (the "agent channel"), §4 channel selection/economics. Agentic commerce is a new channel in that taxonomy.
- `pricing-frameworks.md` — §9 AI-era pricing, per-agent/outcome pricing, machine-buyer pricing logic. Pricing lives there, not here.
- `partnership-models.md` / `/strategic-partnerships` — partnership structuring + dependency-risk framing for agent-channel deals.
- `competitive-frameworks.md` — §12.5 "Positioning When the Buyer Is an Agent / Structured-Attribute Competition": how positioning changes when a machine (not a human) compares you, brand-premium erosion at the agent layer, and the battlecard/counter-positioning implication. Resolves the §5.2/§5.6 forward reference.
- ET `a2a-architecture.md`, `mcp-architecture.md`, `agent-identity.md`, `agentic-security.md` — the technical/security substrate beneath the BD lens (payment rails, agent identity, mandate/credential security). Route body edits there to `chief-architect` / `security-architect`.
- `/strategic-bet` — the Phase-2 artifact where an agentic-commerce channel/segment bet is committed.

---

**🤝 BizDev's note**: I treat this as a live-fire surface, not a settled playbook. The protocols (AP2, ACP, Visa/Mastercard rails, x402) are consolidating monthly and the partner rosters shift — re-validate every specific before it goes in front of a customer. What's durable here is the *frame*: agent-as-channel vs. agent-as-buyer are two different bets; agent-legibility is a readiness gate; and the real BD risk is disintermediation — losing the customer relationship, the data, and the brand surface to the agent layer. Structure agent-channel partnerships the way I structure any partnership that could create dependency at scale: own the customer relationship, or don't sign.
