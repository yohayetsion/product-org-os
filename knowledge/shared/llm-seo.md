---
pack: llm-seo
consumers:
- seo-specialist
---
# LLM SEO / Generative Engine Optimization (GEO)

**Adapted from**:
- aaron-he-zhu/seo-geo-claude-skills (github.com/aaron-he-zhu/seo-geo-claude-skills) — original GEO skill scaffolding and engine-specific patterns
- "The FULL LLM SEO Playbook 2026" (Ordemio) — engine-specific optimization strategies
- amplifying-ai/awesome-generative-engine-optimization (github.com/amplifying-ai/awesome-generative-engine-optimization, Jan 2026) — de facto GEO/LLM-SEO community reference, tracker tools, agentic-commerce protocols, AI crawler UA lists
- AutoGEO (ICLR 2026, CMU) — automated content-rewrite framework that learns generative-engine preferences
- Brandlight 2026 report — empirical schema-citation correlation finding
- Google AI Overviews / AI Mode May 2026 update (Search Engine Land 2026-05-06; 9to5Google 2026-05-06; Google Search I/O 2026 blog post 2026-05-19) — inline-citation + community-perspective + Gemini 3.5 Flash default changes

**Source licence**: aaron-he-zhu/seo-geo-claude-skills (MIT), amplifying-ai (CC0), AutoGEO (research code under associated paper license), Brandlight (publicly cited report), Ordemio (publicly published playbook), Google/Search Engine Land/9to5Google (publicly published articles + vendor blog)

**V2V refinements**:
- 2026 H1 landscape integration (amplifying-ai, AutoGEO, llms.txt, Brandlight schema-citation finding)
- 2026-06 delta: Google AI Overviews / AI Mode May 2026 structural overhaul integrated as datable GEO-tactic shifts (inline-citation passage optimization, community-perspective seeding reinforcement, Gemini 3.5 Flash default as new algorithm-layer change)
- Cross-reference to V2V Phase 5 (Outcomes) decision interface — AI-citation rate as a new Outcomes metric peer to organic traffic
- Updated GEO-vs-traditional-SEO investment decision criteria reflecting the Google-top-link / AI-citation overlap collapse
- Sensitive-skill framing absent (this is a marketing pack, not legal/HR); standard ROI framing applies

---

## Refreshed 2026-05-18

This pack was originally authored Q1 2026 (content lived in `seo-frameworks.md` § Generative Engine Optimization + the `/llm-seo` capability). Q2 2026 H1 landscape developments integrated in this refresh, consolidated into a dedicated pack so `seo-specialist` and `content-strategist` can preload it:

- **amplifying-ai/awesome-generative-engine-optimization** (Jan 2026, CC0, 358 stars) — added as the de facto GEO/LLM-SEO aggregator. Tracker-tool taxonomy (Profound, Goodie, Otterly, AthenaHQ, Scrunch, Rankscale, ZipTie), enterprise platforms (Ahrefs Brand Radar, SEMrush AI Visibility, HubSpot AI Search Grader), agentic-commerce protocols (Google UCP, OpenAI Agentic Commerce Protocol), AI crawler UA lists — all flow from this aggregator.
- **llms.txt protocol** — coverage added. Status as of 2026-05: emergent, NOT standardized. Pre-RFC. Adopted by Anthropic docs, some Vercel/Cloudflare doc properties; not honored by OpenAI/Google crawlers as a binding directive. Treat as "publish but don't depend on it."
- **AutoGEO** (ICLR 2026 paper, CMU) — first academic open-source content-rewrite framework for AI citation. Closes the loop between trackers (telling you IF you're cited) and rewrite (changing whether you are). Research code, not production-polished.
- **Brandlight 82.5% schema-citation finding** — Brandlight 2026 report claims pages with structured data (Organization/Article/FAQPage schema) appear in AI Overviews and ChatGPT citations at 82.5% rate vs. ~37% for pages without schema. Single-vendor finding, directionally consistent with Google's own AI Overviews documentation; cite as Brandlight's claim, not as independently replicated.
- **Google top-link / AI-citation overlap collapse** — per V2V refresh survey §5, the overlap between Google's top-10 organic results and the sources cited in AI Overviews + ChatGPT Browse responses dropped from ~70% (2024 baseline) to <20% (2026). Frames the strategic decision: AI-citation rate is its own metric, not a downstream of traditional rank.

**Sections updated**: Attribution block (new), Refreshed-2026-05-18 (new), Schema Markup for GEO (Brandlight finding integrated), llms.txt Protocol (new section), Automated Rewrite Engines (new section), GEO vs. Traditional SEO (overlap-collapse data added), Tracker Tools (new section), Investment Decision Criteria (new section).

**Sections preserved unchanged**: 4-Engine Model, Claude's 3-Gate Eligibility, Google AI Overviews 3 Selection Gates, Citation Hierarchy (5 States), Direct Answer Fragment (DAF) Rules, Passage-Level Optimization Rules, Forum Seeding Strategy, GEO Testing Methodology, GEO Monitoring KPIs. These Q1 frameworks hold up — the H1 landscape adds tools and empirical findings, doesn't invalidate the underlying model.

---

## 2026-06 Delta Update (as of 2026-06-06)

Google shipped the biggest AI Overviews / AI Mode change since launch in May 2026, across two dated waves. These are additive to the existing 4-Engine Model and Google AI Overviews sections — the underlying selection gates are unchanged; what shifted is the surface UX and the default model, both of which create new datable GEO levers.

### Wave 1 — AI Overviews / AI Mode structural overhaul (2026-05-06)

Five structural changes shipped together (Search Engine Land 2026-05-06; 9to5Google 2026-05-06):

| # | Change | What shipped | GEO tactical implication |
|---|---|---|---|
| 1 | **Inline source links** | Source links now placed directly next to the generated text they support, not collected in a side panel | Optimize to be the **inline-cited passage**, not merely "a source in the list." The DAF that maps cleanly to a single generated sentence is now the unit that earns the inline link. Tighten DAFs to one-claim-per-passage (already a rule) — the payoff is now visible inline placement. |
| 2 | **Desktop hover-previews** | Hovering a citation on desktop shows site name + page title | Page title and site-name clarity become a citation-CTR lever. Titles must be self-describing at a glance; brand/site name must be unambiguous (entity-registration discipline pays off here). |
| 3 | **Subscription-link highlighting** | Links the user already subscribes to are highlighted; early tests showed higher CTR on subscription-labeled links | For publishers/brands with subscriber relationships, being a known/subscribed entity now compounds citation CTR. Reinforces entity-registration + brand-authority investment. |
| 4 | **Expert advice / community perspectives** | AI responses now pull Reddit / forum / social quotes into "expert advice" and "community perspectives" blocks | **Strengthens the case for the Forum Seeding Strategy section below.** Community content is now surfaced as a labeled block inside the response, not just an implicit training signal. Genuine Reddit/Quora presence on category topics now has a direct, visible surface. |
| 5 | **"Explore new angles"** | Follow-up suggestion chips proposing adjacent questions | Topic-cluster breadth (see `seo-frameworks.md` Content Cluster Strategy) maps to the adjacent-question space these chips open. Coverage of the cluster's long-tail facets increases the chance of being the cited source on a follow-up. |

### Wave 2 — Google I/O 2026 (2026-05-19)

Announced at Google I/O 2026 (blog.google Search I/O 2026 post, 2026-05-19):

- **Gemini 3.5 Flash is now the default model in AI Mode globally.** This is a **new datable algorithm-layer change** — re-baseline any AI Mode citation tracking from 2026-05-19 forward; pre- and post-change citation states are not directly comparable. Treat 2026-05-19 as a tracking discontinuity in the GEO Monitoring KPIs.
- **AI Mode passed 1B monthly users** — the AI-citation surface is now at consumer scale; the overlap-collapse strategic argument (AI-citation rate as a co-equal metric to organic traffic) is strengthened, not weakened.
- **Follow-up questions can be asked directly from AI Overviews** — reinforces the "Explore new angles" cluster-coverage implication above.
- **Redesigned multimodal Search box** — multimodal query entry (image + text) is now first-class; image/alt-text and visual-content discipline gain GEO relevance for queries entered multimodally.

### Net GEO posture shift (2026-06)

The May 2026 changes do not invalidate the 4-Engine Model or the DAF discipline — they sharpen two existing levers and add one re-baseline event:

1. **Inline-cited-passage optimization** supersedes generic "be a source" framing for Google AI Overviews. Tighten DAFs so each maps to a single generated sentence.
2. **Community-content seeding** is reinforced — the Forum Seeding Strategy section is now backed by a visible "community perspectives" surface, not just a training-data argument.
3. **Gemini 3.5 Flash default (2026-05-19)** is a tracking discontinuity — re-baseline AI Mode citation tracking from that date.

**Sources**: https://searchengineland.com/google-updates-links-within-ai-overviews-ai-mode-476571 ; https://9to5google.com/2026/05/06/google-ai-mode-overviews-direct-links/ ; https://blog.google/products-and-platforms/products/search/search-io-2026/

---

## What is GEO

Generative Engine Optimization (GEO) is the practice of optimizing content to be discovered, cited, and surfaced by AI-powered search engines — ChatGPT (with browsing), Claude, Gemini, Google AI Overviews, Perplexity — rather than exclusively targeting traditional SERP rankings.

**Why it matters now (H1 2026)**: The overlap between Google top-10 organic and AI-cited sources has collapsed from ~70% (2024) to <20% (per V2V refresh survey 2026-05). Ranking #1 on Google no longer implies being cited by ChatGPT or Gemini. AI-citation rate is now its own metric, peer to organic traffic, not downstream of it. Product orgs must instrument it explicitly.

**The core shift**: Traditional SEO optimizes for algorithmic ranking signals (PageRank, on-page, UX). GEO optimizes for LLM comprehension, trust, and citation eligibility. The content unit shifts from page to passage. The success metric shifts from rank position to citation state.

---

## 4-Engine Model

Each major AI search engine has a distinct retrieval and citation model. Optimize separately for each.

| Engine | Retrieval Mechanism | Citation Bias | Key Optimization Lever |
|---|---|---|---|
| **ChatGPT** (GPT-4o + Browse) | Live web browsing + memory layer | Authoritative, structured, frequently linked | Schema markup, structured answers, brand-task association |
| **Claude** | Safety-first 3-gate eligibility | Conservative, neutral framing, avoids promotional tone | Safety-gate compliance, operational framing, third-party endorsement signals |
| **Gemini** | Deep Google web index + Knowledge Graph | Favors Google-endorsed entities, Wikipedia presence | Knowledge Graph registration, FAQPage schema, entity association |
| **Google AI Overviews** | 3-gate selection from web index | Highly-trusted sources for contested; diverse for informational | Trust signals (DR, brand authority), exact-match passage extraction |
| **Perplexity** | Live web + curated source set | Citations-mandatory model; prefers sources with clear publication date + author | Date-stamping, named-author content, schema |

**Implication**: A single piece of content should pass all engines' filters simultaneously. The common denominator: accurate, authoritative, structured, extractable, non-promotional, recently dated.

---

## Claude's 3-Gate Eligibility Model

| Gate | Question | Failure Condition | Fix |
|---|---|---|---|
| **1. Safety** | Violates Anthropic safety guidelines? | Controversial claims, dangerous instructions | Remove |
| **2. Endorsement Risk** | Would citing imply Claude endorses? | Promotional language, sales-first framing | Reframe as educational, third-party validated |
| **3. Operational Framing** | Operationally useful to user? | Vague thought leadership, no actionable substance | Add how-to, structured frameworks |

**Practical rule**: Write for Claude by removing promotional language, framing claims as industry fact (not brand claim), and ensuring every section provides operational value.

---

## Google AI Overviews: 3 Selection Gates

| Gate | Mechanism | How to Pass |
|---|---|---|
| **Retrieval** | Indexed and accessible? | Clean crawlability, fast load, sitemap inclusion |
| **Extraction** | Content extractable as clean passage? | DAFs, concise paragraph answers |
| **Trust** | Source trusted for this topic? | Domain authority, author credentials, E-E-A-T, site age |

---

## Citation Hierarchy (5 States)

| State | Description | Indicator | Path to Next Level |
|---|---|---|---|
| **1. Primary Source** | LLM directly cites as authoritative | URL appears in AI citations | Maintain freshness, schema, DAF optimization |
| **2. Supporting Citation** | Cited among several sources | URL alongside others | Increase topical authority, peer-cited backlinks |
| **3. Mentioned** | Brand referenced without direct cite | Brand name in AI responses | Build DAFs, increase entity registrations |
| **4. Known but Not Cited** | Processed but not surfaced | Verifiable via direct prompting | Improve trust, reduce promotional framing |
| **5. Unknown** | No knowledge of content | Not surfaced on direct brand queries | Foundational SEO, forum seeding, entity registration |

**Testing your state**: Query the AI engine directly: "What do you know about [Brand/Topic]?" and "What are the best resources for [your target topic]?"

---

## Direct Answer Fragment (DAF) Optimization

The DAF is the fundamental unit of GEO. A self-contained paragraph (40-120 words) that answers a specific question completely, without surrounding context.

**DAF Rules:**
- Starts with the answer, not context-building
- Contains the question keyword in the first sentence
- Grammatically and semantically complete as standalone extract
- No internal references ("as mentioned above", "see section 3")
- No superlatives or promotional language ("the best", "industry-leading")
- Ends with a concrete fact, number, or actionable step

**DAF Template:**
```
[Topic/Question keyword] is/refers to/works by [direct definition or answer].
[Supporting fact or mechanism — 1-2 sentences].
[Practical implication or how-to — 1 sentence].
[Specific number, source, or concrete detail — 1 sentence].
```

**Example (bad — not extractable):**
> "In today's complex cybersecurity landscape, organizations face increasingly sophisticated insider threats. Our platform helps security teams..."

**Example (good — DAF):**
> "Insider risk management (IRM) is a security discipline focused on detecting and mitigating threats from employees, contractors, and partners with legitimate system access. Unlike perimeter security, IRM monitors behavioral signals — unusual data access, policy violations, communication patterns — to identify risk before damage occurs. Effective IRM programs reduce breach dwell time by an average of 40% compared to reactive detection (Ponemon Institute, 2024)."

---

## Passage-Level Optimization Rules

1. **One claim per paragraph** — LLMs extract at paragraph level. Mixed claims reduce extraction accuracy.
2. **Lead with the conclusion** — State the main point in sentence one.
3. **Cite sources inline** — "(Source, Year)" signals factual grounding.
4. **Use numeric specificity** — "73% of breaches involve..." beats "most breaches involve..."
5. **Avoid hedge stacking** — One hedge maximum per claim.
6. **Terminate with a data point** — Paragraphs ending with a specific fact are cited at higher rates.

---

## Schema Markup for GEO

Schema helps AI engines understand entity relationships and extract structured answers. **Brandlight 2026 report finds pages with Organization/Article/FAQPage schema appear in AI Overviews and ChatGPT citations at 82.5% rate vs. ~37% for pages without schema** — single-vendor finding (Brandlight), directionally consistent with Google's AI Overviews documentation, treat as Brandlight's claim pending independent replication. The effect is real enough that schema is now table-stakes, not optional.

| Schema Type | GEO Benefit | Priority |
|---|---|---|
| `Organization` | Registers entity in Knowledge Graphs; improves brand citation accuracy | High (homepage) |
| `Article` | Signals authoritative authorship, publication date, topic domain | High (all content pages) |
| `FAQPage` | Maps to LLM FAQ extraction patterns; highest citation conversion | High (product/info pages) |
| `HowTo` | Maps to instructional extraction; Claude + ChatGPT cite preferentially | Medium (guides, tutorials) |
| `Person` | Associates author expertise; supports E-E-A-T | Medium (author pages) |
| `SpeakableSpecification` | Marks content as suitable for voice/AI extraction | Low (emerging) |

**GEO-critical FAQPage rule**: Questions must mirror actual user query phrasing. Query "People Also Ask" and Google Suggest for exact user language. Do not write FAQ questions in marketing tone.

---

## llms.txt Protocol (status: emergent, not standardized)

**llms.txt** is a proposed robots.txt-equivalent for LLM crawlers — a markdown file at the site root that tells AI crawlers which pages to prefer for citation and how to interpret content boundaries.

**Status as of 2026-05**:
- Proposed by Jeremy Howard (Answer.AI) Sept 2024; gained traction H1 2025
- Adopted by: Anthropic docs, some Vercel/Cloudflare doc properties, growing developer-tool documentation
- NOT honored by OpenAI, Google, or Perplexity as a binding directive
- Pre-RFC, no W3C or IETF standardization track

**Recommendation**: Publish `/llms.txt` because the cost is near-zero and early adopters of standards benefit if standardization happens, but do NOT architect your GEO strategy around it. Treat as a hint, not a contract. Re-evaluate quarterly.

**Minimal llms.txt template**:
```
# [Brand Name]

> [One-sentence brand summary — this is the entity description LLMs may use]

## Core Pages
- [Homepage URL]: [purpose]
- [Product page URL]: [purpose]
- [Pricing URL]: [purpose]

## Documentation
- [Docs URL]: [purpose]

## Optional
- [About URL]: [purpose]
```

---

## Automated Rewrite Engines — AutoGEO (ICLR 2026)

**AutoGEO** (CMU, ICLR 2026) is the first academic open-source framework that learns generative-engine citation preferences and automatically rewrites web content to increase LLM traction. Where tracker tools (Profound, Otterly) tell you IF you're cited, AutoGEO is the rewrite layer that changes whether you are.

**How it works (per the paper)**: Trains a rewrite model on (content → citation outcome) pairs across target engines. Output is a rewritten passage that preserves factual claims but reorders, restructures, and re-phrases for higher extraction probability.

**Practical state H1 2026**: Research code, not production-polished. Expect rough edges, manual fix-up, and engine-specific tuning. Useful as a thought partner for the DAF rewrite process; not yet a press-the-button-and-ship tool.

**When to use**: After a GEO audit identifies State-3-or-worse (mentioned but not cited; known but not cited; unknown) on important pages, AutoGEO-style rewriting is the implementation backbone. Pair with the `copywriter` and `seo-specialist` for QA — automated rewrites can drift from brand voice if not gated.

---

## Tracker Tools (status: paid, fragmented)

The 2026 tracker-tool landscape per amplifying-ai aggregator:

| Tool | Tier | Focus | Notes |
|---|---|---|---|
| **Profound** | Enterprise ($499+/mo) | Multi-engine citation tracking | Most comprehensive coverage |
| **Goodie** | Mid-market | ChatGPT-first | Tighter ChatGPT instrumentation |
| **Otterly** | Mid-market | Multi-engine | Mid-price, broad coverage |
| **AthenaHQ** | Enterprise | Multi-engine + competitive | Stronger competitor benchmarking |
| **Scrunch** | Mid-market | Multi-engine | Newer entrant |
| **Rankscale** | SMB | Limited engines | Lower price, narrower coverage |
| **ZipTie** | SMB | ChatGPT + Perplexity | Niche focus |
| **Ahrefs Brand Radar** | Enterprise (part of Ahrefs subscription) | AI mention tracking | Bundled with existing Ahrefs |
| **SEMrush AI Visibility Toolkit** | Enterprise (part of SEMrush) | AI mention tracking | Bundled with existing SEMrush |
| **HubSpot AI Search Grader** | Free | Basic visibility check | Adequate for awareness, not for instrumentation |

**Recommendation**: For most product orgs, manual monthly prompt audits (per the GEO Testing Methodology section below) are sufficient through Q4 2026. Tracker tools become defensible past ~25 target keywords or when AI-citation rate is a quarterly OKR. Otherwise the tool cost outweighs the marginal-precision gain over manual audits.

---

## Forum Seeding Strategy

LLMs are trained heavily on forum content (Reddit, Quora, Stack Exchange, Hacker News). Forum consensus disproportionately influences LLM responses on contested topics.

**Why forums matter**: When a user asks an LLM "What's the best tool for X?", the response is heavily influenced by aggregated forum sentiment, not brand content.

| Platform | Best For | Content Type | Cadence |
|---|---|---|---|
| Reddit | Consumer software, security, dev tools | Genuine problem-solving + brand mention in comments | 2-4x/month per relevant subreddit |
| Quora | B2B, professional services, SaaS | Authoritative answer posts with cited examples | 2x/month per topic |
| Stack Exchange | Technical products, dev tools | Technical answers with brand in context | As relevant questions arise |
| Hacker News | Developer/startup products | Show HN posts, genuine discussion | Quarterly product launches |

**Rules:**
- Never astroturf or create fake accounts. Genuine participation only.
- Mention brand in context of solving a problem, never as promotional recommendation.
- Answers must provide standalone value — brand mention is secondary.
- Disclose affiliation when directly recommending your own product.

---

## GEO Testing Methodology

GEO requires a different testing paradigm than traditional SEO.

**Prompt Type Framework:**

| Prompt Type | Example | What It Tests |
|---|---|---|
| Definition query | "What is insider risk management?" | Topical association |
| Comparison query | "What are the best IRM platforms?" | Brand citation eligibility |
| Brand knowledge query | "Tell me about [Brand]" | Entity knowledge state |
| Problem-first query | "How do I detect insider threats before a breach?" | DAF extraction quality |
| Opinion/recommendation | "Which IRM vendor should I consider?" | Trust + endorsement signals |

**Test protocol:**
1. Run each prompt type across all engines (ChatGPT, Claude, Gemini, AI Overviews, Perplexity)
2. Record: cited / mentioned / not cited per brand + competitor
3. Run monthly — track citation state movement
4. When new content publishes, re-test relevant prompt types within 2-4 weeks

---

## GEO vs. Traditional SEO — Investment Decision Criteria

**The 2026 overlap collapse changes the decision math.** When Google top-10 and AI citations overlapped 70% (2024), strong traditional SEO got most of GEO "for free." At <20% overlap (2026 per V2V refresh survey §5), traditional SEO and GEO are now genuinely distinct disciplines requiring distinct investment.

| Dimension | Traditional SEO | GEO |
|---|---|---|
| Target | Search engine algorithm | LLM retrieval + citation model |
| Primary signal | Backlinks + on-page relevance | Trust, extractability, entity registration |
| Measurement | Rank position, organic traffic | Citation frequency, mention state, AI referral |
| Content unit | Page | Passage / paragraph (DAF) |
| Time to result | 3-6 months | 2-8 weeks (LLMs re-crawl frequently) |
| Competitive moat | Domain authority (slow to build) | Content depth + entity trust (faster) |
| Schema importance | Moderate (rich snippets) | High (entity registration, FAQPage extraction) — see Brandlight 82.5% finding |
| Forum signals | Indirect (links) | Direct (training data, forum consensus) |
| Brand prominence | Diluted across result set | High (LLM may cite only 1-3 sources) |

**When to weight investment toward GEO over traditional SEO:**
- Audience uses AI assistants for category research (B2B SaaS, dev tools, security, finance)
- Target buyer is "doing research" not "ready to buy" (top-of-funnel)
- Brand is newer / lower DA — GEO compounds faster than traditional SEO
- Category has <10 named competitors (LLMs cite few; concentration favors GEO)

**When to weight toward traditional SEO:**
- E-commerce, transactional intent (AI assistants rarely close transactions yet)
- Category has 50+ named competitors (LLM citation slots are crowded; rank position scales linearly)
- Local/geographic intent
- Existing strong DA — traditional SEO compounding is sunk-cost-positive

**The product-org strategic decision** (V2V Phase 5 Outcomes integration): AI-citation rate becomes a co-equal outcome metric to organic traffic. Instrumenting it requires the GEO Testing Methodology above. The investment-allocation question is no longer "SEO or not" but "what split of SEO / GEO / paid given audience and funnel stage."

---

## GEO Monitoring KPIs

| KPI | Tracking Method | Frequency | Owner |
|---|---|---|---|
| Citation rate by engine | Manual AI prompts OR tracker tool | Monthly | SEO specialist |
| Citation state score (1-5 avg) | Prompt audit scoring | Monthly | SEO specialist |
| AI referral sessions | GA4 (look for chatgpt.com, claude.ai, perplexity.ai, gemini.google.com) | Weekly | Analytics |
| Competitor citation share | Prompt audit + comparison | Monthly | CI / SEO |
| DAF coverage (% pages with DAF) | Content audit | Quarterly | Content team |
| Schema validation pass rate | Google Rich Results Test | Post-publish | Dev / SEO |
| Forum mention volume | Brand monitoring tools | Weekly | Marketing |
| llms.txt published | Manual check | Quarterly | SEO specialist |

---

## V2V Phase 5 (Outcomes) Integration

AI-citation rate is a new Outcomes metric peer to organic traffic. Surface it in the Outcomes review packet:

- **Citation rate by engine** (this month vs. last month, by target query category)
- **Citation state movement** (how many target queries moved up or down the 5-state hierarchy)
- **AI referral traffic** (GA4) vs. organic traffic (GA4) trend
- **Competitor citation share** (are we gaining or losing share-of-AI-voice)

Tie movement to specific content investments (DAF rewrites, schema additions, forum seeding). The V2V decision question at Phase 5: "Should next quarter's content investment weight more toward GEO or traditional SEO?" — answer with the overlap-collapse data, audience, and funnel stage from the decision criteria above.

---

## V2V Cross-References

**Sibling Q2-6 packs**:
- **`mmm-modeling.md` (Q2-6.1)** — channel-mix overlap. AI-citation rate joins paid-channel mix as a measurable surface; the 2026 GEO vs traditional SEO investment decision consumes MMM-style channel ROI curves alongside organic-traffic measurement. The investment-allocation question in §"GEO vs. Traditional SEO" is informed by MMM channel coefficients.
- **`retention-marketing.md` (Q2-6.2)** — organic re-engagement overlap. Branded-search demand from former / disengaged customers indicates win-back readiness; AI-citation rate movement on brand queries is a re-engagement readiness signal. Schema markup (FAQPage) and DAF discipline support the customer-research journey that re-engagement campaigns surface.

**Sibling Q2-7 packs (sales-funnel adjacency)**:
- **`ai-native-rfp.md` (Q2-7.2)** — content library overlap. RFP-response content (when externalized, e.g., security questionnaire answers published as KB articles) feeds the LLM-citation pipeline; FAQPage schema on those externalized answers improves both RFP-response reuse and AI-citation visibility.

**Sibling Q2-8 packs**:
- **`generative-ui.md` (Q2-8.1)** — when product surfaces are runtime-generated, the AI-citation discipline applies inside the product surface (LLMs that render content within Pattern 2 / Pattern 3 surfaces consume the same citation hierarchy as external AI search engines).

**Existing packs**:
- `seo-frameworks.md` — traditional SEO discipline; this pack extends rather than replaces (the Q1 frameworks preserved per "Refreshed 2026-05-18" header).
- `/schema-markup` — structured-data implementation discipline; the Brandlight 82.5% finding makes schema table-stakes for GEO, not optional.
- `content-marketing.md` + `/content-strategy` — broader content discipline that DAF authoring and passage-level optimization sit within.
- `/social-content` — forum-seeding strategy intersects with broader social-content discipline.
- `analytics-methodology.md` + `experimentation-ml.md` — AI-citation rate testing methodology and measurement infrastructure.
- `/brand-strategy` — brand authority and entity-registration framing that GEO trust signals depend on.

**Sensitive-skill applicability**: Not sensitive per `sensitive-skill-guardrails.md` §2 (marketing reference pack; no legal/HR/compliance output). Standard ROI framing applies.

---

## Common Pitfalls

- Single-vendor empirical claims (Brandlight 82.5%) are directional, not gospel — replicate before betting strategy on them
- llms.txt is emergent, not standardized — publish but don't depend on it
- Tracker tools are paid + fragmented — manual audits work fine for <25 target keywords
- AutoGEO is research code — automate the rewrite step at your own QA cost
- AI-citation rate movement is noisier than rank tracking — use 3-month moving averages, not month-over-month
- Promotional language fails Claude's gate 2 even when factually accurate — operational framing is the cost of entry
