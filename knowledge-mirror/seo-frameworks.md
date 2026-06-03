# SEO Playbook

<!-- Attribution:
  GEO (Generative Engine Optimization) section informed by:
  - aaron-he-zhu/seo-geo-claude-skills (github.com/aaron-he-zhu/seo-geo-claude-skills) — GEO methodology and AI search optimization
  Adapted and expanded for Product Org OS agents.
-->

Knowledge pack for SEO-related agents. Contains real frameworks, processes, and templates for organic search optimization.

---

## Technical SEO Fundamentals

### Crawlability and Indexation

**When to use**: Before any content strategy work. Technical foundation must be solid first.

**How it works**: Search engines discover and understand your site through crawling. If they cannot crawl or index your pages, no amount of content optimization matters.

**Checklist:**
- [ ] XML sitemap submitted and updated (include lastmod dates)
- [ ] robots.txt allows crawling of important pages
- [ ] No accidental noindex tags on important pages
- [ ] Canonical tags resolve duplicate content
- [ ] Internal linking connects all important pages (max 3 clicks from homepage)
- [ ] 301 redirects handle URL changes (no redirect chains)
- [ ] HTTPS across entire site
- [ ] Hreflang tags for multi-language/region sites

**Limitations**: Technical SEO is necessary but not sufficient. A perfectly crawlable site with thin content will not rank.

### Core Web Vitals

**When to use**: When site performance affects rankings or user experience metrics are poor.

**How it works**: Google uses three metrics as ranking signals:

| Metric | What It Measures | Target | Common Fix |
|--------|-----------------|--------|------------|
| **LCP** (Largest Contentful Paint) | Loading speed | < 2.5s | Optimize images, server response, render-blocking resources |
| **INP** (Interaction to Next Paint) | Interactivity | < 200ms | Reduce JavaScript execution, break long tasks |
| **CLS** (Cumulative Layout Shift) | Visual stability | < 0.1 | Set explicit dimensions for images/ads, avoid dynamic content injection |

**Measurement tools**: PageSpeed Insights, Chrome UX Report, Search Console Core Web Vitals report.

**Limitations**: Core Web Vitals are one of many ranking factors. Improving speed will not overcome poor content or weak authority.

---

## On-Page SEO

### Title Tag and Meta Description Optimization

**When to use**: For every indexable page. These are the first elements users see in search results.

**Title tag formula:**
```
[Primary Keyword] — [Benefit or Modifier] | [Brand]
```

**Constraints:**
- Title: 50-60 characters (Google truncates at ~600px)
- Meta description: 150-160 characters (Google may rewrite)

**Template:**
```
Title: [Primary Keyword]: [Compelling Benefit] | [Brand Name]
Meta: [Action verb] [what the page offers]. [Specific benefit]. [CTA or unique value].
```

**Example:**
```
Title: Insider Risk Management: AI-Powered Threat Detection | AXIA
Meta: Detect insider threats before they become breaches. AXIA's AI understands intent, not just actions. See how it works.
```

**Limitations**: Google increasingly rewrites meta descriptions. Focus on accuracy over persuasion — Google prefers descriptions that match page content.

### Header Hierarchy (H1-H6)

**When to use**: Structuring any content page for both users and search engines.

**How it works:**
- **H1**: One per page. Contains primary keyword. Matches search intent.
- **H2**: Major sections. Contains secondary keywords or topic facets.
- **H3-H4**: Subsections. Long-tail variations, specific questions.

**Template:**
```markdown
# [Primary Keyword/Topic] — H1
## [Subtopic 1 / Secondary Keyword] — H2
### [Specific question or detail] — H3
## [Subtopic 2 / Secondary Keyword] — H2
### [Specific question or detail] — H3
```

**Limitations**: Header optimization alone has minimal impact. Content quality within each section matters far more than the header text.

---

## Content Cluster Strategy

### Topic Cluster Architecture

**When to use**: Planning content strategy for an entire topic area. Essential for building topical authority.

**How it works**: A pillar page covers a broad topic comprehensively. Cluster pages cover specific subtopics in depth. Internal links connect cluster pages to the pillar and to each other.

**Structure:**
```
Pillar Page: "Insider Risk Management" (2,000-4,000 words)
├── Cluster: "Types of Insider Threats" (1,500+ words)
├── Cluster: "Insider Threat Indicators" (1,500+ words)
├── Cluster: "Insider Risk vs. DLP" (1,500+ words)
├── Cluster: "Building an Insider Risk Program" (1,500+ words)
├── Cluster: "Insider Threat Case Studies" (1,500+ words)
└── Cluster: "Insider Risk Tools Comparison" (1,500+ words)
```

**Internal linking rules:**
1. Every cluster page links to the pillar (in the first 200 words)
2. The pillar links to every cluster page
3. Related cluster pages link to each other
4. Anchor text uses natural keyword variations (not exact match every time)

**Template for cluster planning:**

| Cluster Page | Primary Keyword | Search Intent | Funnel Stage | Target Word Count |
|-------------|----------------|---------------|--------------|-------------------|
| [Title] | [keyword] | Informational / Commercial / Transactional | TOFU / MOFU / BOFU | [count] |

**Limitations**: Clusters require consistent publication and maintenance. A half-built cluster performs worse than individual optimized pages because it signals incomplete topical coverage.

---

## E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

### Demonstrating E-E-A-T

**When to use**: For all content, but especially critical for YMYL (Your Money or Your Life) topics including security, finance, and health.

**How it works**: Google's quality raters assess E-E-A-T signals. While not a direct algorithm factor, content demonstrating these signals tends to rank better.

| Signal | How to Demonstrate |
|--------|--------------------|
| **Experience** | First-hand accounts, screenshots, case studies, "we did X and learned Y" |
| **Expertise** | Author credentials, technical depth, accurate terminology, cited sources |
| **Authoritativeness** | Industry recognition, backlinks from authoritative sites, brand mentions |
| **Trustworthiness** | Accurate information, transparent sourcing, clear authorship, secure site |

**Implementation checklist:**
- [ ] Author bios with credentials on all content
- [ ] Author pages with linked published content
- [ ] About page with company background
- [ ] Sources cited for claims and statistics
- [ ] Content reviewed by subject matter experts
- [ ] Regular content updates (especially for time-sensitive topics)

**Limitations**: E-E-A-T cannot be faked with cosmetic changes. It requires genuine expertise and a track record of quality content over time.

---

## Keyword Research Process

### Keyword Selection Framework

**When to use**: Before creating any content. Determines whether the effort is worth the investment.

**Step 1: Seed keyword expansion**
- Start with 5-10 seed keywords from your positioning
- Expand using: Ahrefs/Semrush keyword explorer, "People Also Ask", Google Suggest, competitor page analysis

**Step 2: Evaluate each keyword on four dimensions**

| Dimension | Question | How to Assess |
|-----------|----------|---------------|
| **Volume** | How many people search this monthly? | Keyword tools (note: tools often underestimate) |
| **Difficulty** | How hard is it to rank? | KD score + manual SERP analysis |
| **Intent match** | Does this align with what we offer? | Review top 10 results — does our content type fit? |
| **Business value** | Will ranking here drive meaningful outcomes? | Map to funnel stage and conversion likelihood |

**Step 3: Prioritize using a scoring matrix**

```
Priority Score = (Business Value × 3) + (Intent Match × 2) + Volume - Difficulty
```

Weight business value highest because ranking for high-volume low-relevance keywords wastes resources.

**Template:**

| Keyword | Volume | KD | Intent | Business Value | Priority Score | Status |
|---------|--------|-----|--------|---------------|----------------|--------|
| [keyword] | [vol] | [kd] | Info/Comm/Trans | High/Med/Low | [score] | New/Active/Ranking |

**Limitations**: Keyword volume data is estimated, not exact. Search volume alone does not predict traffic — click-through rates vary dramatically by SERP features (featured snippets, ads, knowledge panels).

---

## Schema Markup

### Structured Data Implementation

**When to use**: For all pages where schema can enhance SERP appearance (rich snippets, knowledge panels, FAQ sections).

**Priority schema types for SaaS/B2B:**

| Schema Type | Best For | SERP Enhancement |
|-------------|----------|------------------|
| `Organization` | Homepage, About page | Knowledge panel |
| `FAQPage` | FAQ sections, informational content | FAQ rich results |
| `HowTo` | Tutorials, guides | Step-by-step rich results |
| `Article` | Blog posts, thought leadership | Article rich results |
| `Product` | Product pages, pricing | Product rich results |
| `Review` | Testimonial pages | Star ratings |
| `BreadcrumbList` | All pages | Breadcrumb navigation in SERP |

**Implementation template (JSON-LD):**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question text]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer text]"
      }
    }
  ]
}
```

**Validation**: Always test with Google Rich Results Test before deploying.

**Limitations**: Schema does not directly improve rankings. It improves SERP appearance, which can improve click-through rates. Google may choose not to display rich results even when schema is valid.

---

## Link Building Principles

### Earning Backlinks

**When to use**: After content foundation is solid. Link building without quality content is futile.

**Effective approaches (ranked by sustainability):**

1. **Original research and data** — Surveys, studies, unique datasets that others cite
2. **Comprehensive resources** — Definitive guides that become reference material
3. **Expert commentary** — Quoted in industry publications and news
4. **Tool/calculator creation** — Free tools that solve problems and attract links
5. **Digital PR** — Newsworthy content that earns media coverage

**Metrics that matter:**

| Metric | What It Tells You | Target |
|--------|-------------------|--------|
| Referring domains (unique) | Breadth of authority | Growing month over month |
| Domain Rating of linking sites | Quality of authority | Focus on DR 40+ sites |
| Relevance of linking sites | Topical authority | Same industry or adjacent |
| Anchor text distribution | Natural link profile | Mix of branded, topical, and generic |

**Limitations**: Link building is slow. It takes 3-6 months for new backlinks to meaningfully affect rankings. Purchased or manipulated links risk penalties that can take years to recover from.

---

## SEO Audit Process

### Quarterly SEO Health Check

**When to use**: Quarterly at minimum. After major site changes, migrations, or ranking drops.

**Audit structure:**

1. **Technical health** (30 min)
   - Crawl site with Screaming Frog or Sitebulb
   - Check Search Console for coverage errors
   - Review Core Web Vitals
   - Verify sitemap and robots.txt

2. **Content performance** (45 min)
   - Identify top 20 pages by organic traffic
   - Identify declining pages (month-over-month and year-over-year)
   - Find thin content (< 300 words, low engagement)
   - Check for content gaps vs. competitors

3. **Backlink profile** (30 min)
   - Review new and lost backlinks
   - Check for toxic/spammy links
   - Compare referring domain growth vs. competitors
   - Identify link building opportunities

4. **Competitive position** (30 min)
   - Compare keyword overlap with top 3 competitors
   - Identify keywords competitors rank for that you do not
   - Review competitor content strategy changes
   - Assess SERP feature ownership

**Output template:**

| Area | Status | Key Finding | Action | Priority |
|------|--------|-------------|--------|----------|
| Technical | Green/Yellow/Red | [finding] | [action] | P0/P1/P2 |
| Content | Green/Yellow/Red | [finding] | [action] | P0/P1/P2 |
| Links | Green/Yellow/Red | [finding] | [action] | P0/P1/P2 |
| Competitive | Green/Yellow/Red | [finding] | [action] | P0/P1/P2 |

**Limitations**: SEO audits are point-in-time snapshots. Search algorithms change continuously. An audit identifies current state, not future trajectory.

---

## Search Intent Classification

### Intent Types and Content Mapping

**When to use**: When deciding what content format to create for a keyword.

| Intent Type | User Goal | Content Format | Funnel Stage |
|-------------|-----------|----------------|--------------|
| **Informational** | Learn about a topic | Blog post, guide, explainer | Top of funnel |
| **Navigational** | Find a specific page/brand | Homepage, branded page | Mid funnel |
| **Commercial** | Compare options, evaluate | Comparison page, review, case study | Mid-bottom funnel |
| **Transactional** | Take action (buy, sign up) | Product page, pricing, signup | Bottom of funnel |

**How to determine intent**: Look at the top 10 search results for the keyword. If 8 of 10 are blog posts, the intent is informational. If 8 of 10 are product pages, the intent is transactional. Content that mismatches intent will not rank regardless of quality.

**Limitations**: Intent can be mixed or ambiguous for some queries. Google may show different result types over time as user behavior data evolves.


## Common Pitfalls

- Search algorithm changes can invalidate SEO strategies — date all recommendations
- Keyword difficulty scores are estimates, not guarantees — competition varies by domain
- Technical SEO issues (crawlability, indexation) must be verified with actual tools, not assumed

---

## Generative Engine Optimization (GEO)

<!-- Sources: aaron-he-zhu/seo-geo-claude-skills, Ordemio LLM SEO Playbook. Added 2026-03-29. -->

### What is GEO

Generative Engine Optimization (GEO) is the practice of optimizing content to be discovered, cited, and surfaced by AI-powered search engines — including ChatGPT (with browsing), Claude, Gemini, and Google AI Overviews — rather than exclusively targeting traditional SERP rankings.

**Why it matters now**: AI search handles a growing share of zero-click queries. Being cited in an AI response is increasingly more valuable than a traditional blue link, as AI responses command attention before organic results. GEO and traditional SEO are complementary, not competing disciplines.

**The core shift**: Traditional SEO optimizes for algorithmic ranking signals (PageRank, on-page signals, UX). GEO optimizes for LLM comprehension, trust, and citation eligibility. The content must be written so an AI can extract a clean, accurate, self-contained answer fragment.

---

### 4-Engine Model

Each major AI search engine has a distinct retrieval and citation model. Optimize separately for each.

| Engine | Retrieval Mechanism | Citation Bias | Key Optimization Lever |
|--------|--------------------|--------------------|------------------------|
| **ChatGPT** (GPT-4o + Browse) | Live web browsing + memory layer | Authoritative, structured, frequently linked content | Schema markup, clear headings, structured answers |
| **Claude** | Safety-first eligibility gates (3-gate model) | Conservative, prefers neutral framing, avoids promotional tone | Safety gate compliance, third-party endorsement signals, operational framing |
| **Gemini** | Deep Google web index + Knowledge Graph | Favors Google-endorsed entities, Wikipedia presence, structured data | Knowledge Graph entity registration, FAQPage schema, Google entity association |
| **Google AI Overviews** | 3-gate selection from web index | Prefers highly-trusted sources for contested topics; diverse sources for informational | Trust signals (DR, brand authority), exact-match passage extraction |

**Implication**: A single piece of content should be written to pass all four engines' filters simultaneously. Contradictions between engines are rare — the common denominator is: accurate, authoritative, structured, extractable, non-promotional.

---

### Claude's 3-Gate Eligibility Model

Claude applies three sequential filters before citing content in a response:

| Gate | Question | Failure Condition | Fix |
|------|----------|-------------------|-----|
| **Gate 1: Safety** | Does this content violate Anthropic safety guidelines? | Controversial claims, dangerous instructions, explicit content | Remove policy-violating content entirely |
| **Gate 2: Endorsement Risk** | Would citing this imply Claude endorses a product/brand? | Overtly promotional language, sales-first framing | Reframe as educational, factual, third-party validated |
| **Gate 3: Operational Framing** | Is this content operationally useful to the user? | Vague thought leadership, no actionable substance | Add specific how-to instructions, structured frameworks |

**Practical rule**: Write for Claude by removing all promotional language, framing claims as industry fact rather than brand claim, and ensuring every section provides operational value.

---

### Google AI Overviews: 3 Selection Gates

| Gate | Mechanism | How to Pass |
|------|-----------|-------------|
| **Retrieval** | Is the page indexed and accessible? | Clean crawlability, fast load, sitemap inclusion |
| **Extraction** | Can the content be extracted as a clean passage? | Direct Answer Fragments (see below), concise paragraph answers |
| **Trust** | Is the source trusted for this topic? | Domain authority, author credentials, E-E-A-T signals, site age |

---

### Citation Hierarchy (5 States)

Understanding where your content sits in an LLM's citation hierarchy allows you to set realistic goals and prioritize efforts.

| State | Description | Indicator | Path to Next Level |
|-------|-------------|-----------|-------------------|
| **1. Primary Source** | LLM directly cites your content as the authoritative answer | Your URL appears in AI citations | Maintain freshness, schema, DAF optimization |
| **2. Supporting Citation** | LLM cites you as one of several sources | URL present alongside others | Increase topical authority, earn more backlinks from cited peers |
| **3. Mentioned** | LLM references your brand/content without direct citation | Brand name appears in AI responses | Build direct answer fragments, increase entity registrations |
| **4. Known but Not Cited** | LLM has processed your content but does not surface it | Verifiable with direct AI prompting | Improve trust signals, reduce promotional framing |
| **5. Unknown** | LLM has no knowledge of your content | Not surfaced even on direct brand queries | Build foundational SEO, forum seeding, entity registration |

**Testing your state**: Query the AI engine directly: "What do you know about [Brand/Topic]?" and "What are the best resources for [your target topic]?"

---

### Direct Answer Fragment (DAF) Optimization

The DAF is the fundamental unit of GEO. It is a self-contained paragraph (60-120 words) that answers a specific question completely, without requiring surrounding context.

**DAF Rules:**
- Starts with the answer, not with context-building
- Contains the question keyword in the first sentence
- Is grammatically and semantically complete as a standalone extract
- Contains no internal references ("as mentioned above", "see section 3")
- Avoids superlatives and promotional language ("the best", "industry-leading")
- Ends with a concrete fact, number, or actionable step

**DAF Template:**
```
[Topic/Question keyword] is/refers to/works by [direct definition or answer].
[Supporting fact or mechanism — 1-2 sentences].
[Practical implication or how-to — 1 sentence].
[Specific number, source, or concrete detail — 1 sentence].
```

**Example (bad — not extractable):**
> "In today's complex cybersecurity landscape, organizations face increasingly sophisticated insider threats. Our platform helps security teams navigate these challenges..."

**Example (good — DAF):**
> "Insider risk management (IRM) is a security discipline focused on detecting and mitigating threats from employees, contractors, and partners with legitimate system access. Unlike perimeter security, IRM monitors behavioral signals — unusual data access, policy violations, and communication patterns — to identify risk before damage occurs. Effective IRM programs reduce breach dwell time by an average of 40% compared to reactive detection (Ponemon Institute, 2024)."

---

### Passage-Level Optimization Rules

Beyond DAFs, every content passage should follow these rules to maximize AI extractability:

1. **One claim per paragraph** — LLMs extract at the paragraph level. Mixed claims reduce extraction accuracy.
2. **Lead with the conclusion** — State the main point in the first sentence of every paragraph. AI engines use the opening sentence to assess relevance before reading further.
3. **Cite sources inline** — "(Source, Year)" format signals factual grounding to LLMs.
4. **Use numeric specificity** — "73% of breaches involve..." is more citable than "most breaches involve..."
5. **Avoid hedge stacking** — "It may potentially be somewhat helpful..." destroys extraction confidence. One hedge maximum per claim.
6. **Terminate with a data point** — Paragraphs ending with a specific fact, study, or number are cited at higher rates.

---

### Schema Markup for GEO

Schema helps AI engines understand entity relationships and extract structured answers. GEO-specific schema priorities:

| Schema Type | GEO Benefit | Implementation Priority |
|-------------|-------------|------------------------|
| `Organization` | Registers your entity in Knowledge Graphs; improves brand citation accuracy | High (homepage) |
| `Article` | Signals authoritative authorship, publication date, and topic domain | High (all blog/content pages) |
| `FAQPage` | Directly maps to LLM FAQ extraction patterns; highest citation conversion | High (product/informational pages) |
| `HowTo` | Maps to instructional extraction; Claude and ChatGPT cite HowTo-structured content preferentially | Medium (guides, tutorials) |
| `Person` | Associates author expertise with content; supports E-E-A-T signals for AI | Medium (author pages) |
| `SpeakableSpecification` | Explicitly marks content as suitable for voice/AI extraction | Low (emerging standard) |

**GEO-critical FAQPage implementation**: Questions must mirror actual user query phrasing. Do not write FAQ questions in marketing language. Query "People Also Ask" and Google Suggest for exact user language.

---

### Forum Seeding Strategy

LLMs are trained heavily on forum content (Reddit, Quora, Stack Exchange, Hacker News). Forum consensus disproportionately influences LLM responses on contested topics.

**Why forums matter**: When a user asks an LLM "What's the best tool for X?", the response is heavily influenced by aggregated forum sentiment, not brand content.

**Forum seeding approach:**

| Platform | Best For | Content Type | Cadence |
|----------|----------|-------------|---------|
| Reddit | Consumer software, security, developer tools | Genuine problem-solving posts + brand mention in comments | 2-4x/month per relevant subreddit |
| Quora | B2B, professional services, SaaS | Authoritative answer posts with cited examples | 2x/month per topic |
| Stack Exchange | Technical products, developer tools | Technical answers with brand in context | As relevant questions arise |
| Hacker News | Developer/startup products | Show HN posts, genuine discussion participation | Quarterly product launches |

**Rules for forum seeding:**
- Never astroturf or create fake accounts. Genuine participation only.
- Mention the brand in context of solving a problem, never as a promotional recommendation.
- Answers must provide standalone value — the brand mention is secondary.
- Disclose affiliation when directly recommending your own product.

**Outcome**: Consistent, genuine forum presence ensures LLMs associate your brand with the problem category at training and retrieval time.

---

### GEO Testing Methodology

GEO requires a different testing paradigm than traditional SEO (which relies on rank tracking tools).

**Prompt Type Framework:**

| Prompt Type | Example | What It Tests |
|-------------|---------|---------------|
| **Definition query** | "What is insider risk management?" | Topical association |
| **Comparison query** | "What are the best IRM platforms?" | Brand citation eligibility |
| **Brand knowledge query** | "Tell me about AXIA Security" | Entity knowledge state |
| **Problem-first query** | "How do I detect insider threats before a breach?" | DAF extraction quality |
| **Opinion/recommendation** | "Which IRM vendor should I consider?" | Trust and endorsement signals |

**Test protocol:**
1. Run each prompt type across all 4 engines (ChatGPT, Claude, Gemini, AI Overview)
2. Record: cited / mentioned / not cited for each brand and competitor
3. Run monthly — track citation state movement over time
4. When a new piece of content is published, re-test relevant prompt types within 2-4 weeks

**What to track (GEO Monitoring KPIs):**

| KPI | How to Measure | Target Direction |
|-----|---------------|-----------------|
| Citation frequency | Manual AI prompt audits (monthly) | Increasing |
| Citation state (1-5 scale above) | Prompt-based brand query | Moving toward Primary Source |
| AI referral traffic | GA4 source/medium (look for ChatGPT, Perplexity, claude.ai) | Growing |
| Brand mention share | Share of LLM responses mentioning brand vs. top 3 competitors | >= competitor parity |
| DAF extraction rate | % of content passages successfully extracted verbatim | > 30% of target passages |

---

### GEO vs. Traditional SEO Comparison

| Dimension | Traditional SEO | Generative Engine Optimization (GEO) |
|-----------|----------------|--------------------------------------|
| **Target** | Search engine algorithm | LLM retrieval and citation model |
| **Primary signal** | Backlinks + on-page relevance | Trust, extractability, entity registration |
| **Measurement** | Rank position, organic traffic | Citation frequency, mention state, AI referral |
| **Content unit** | Page | Passage / paragraph (DAF) |
| **Time to result** | 3-6 months | 2-8 weeks (LLMs re-crawl frequently) |
| **Competitive moat** | Domain authority (slow to build) | Content depth + entity trust (faster to establish) |
| **Schema importance** | Moderate (rich snippets) | High (entity registration, FAQPage extraction) |
| **Forum signals** | Indirect (links) | Direct (training data, forum consensus) |
| **Brand prominence** | Diluted across result set | High (LLM may cite only 1-3 sources) |

**Key insight**: GEO rewards being the clearest, most credible, most extractable answer. Traditional SEO rewards having the most authoritative domain. A newer site with excellent GEO can out-cite a high-DA site with poor extractability in AI results.

---

### GEO Monitoring KPIs (Summary Dashboard)

| Metric | Tracking Method | Frequency | Owner |
|--------|----------------|-----------|-------|
| Citation rate by engine | Manual AI prompts | Monthly | SEO specialist |
| Citation state score (avg) | Prompt audit scoring | Monthly | SEO specialist |
| AI referral sessions | GA4 (channel grouping) | Weekly | Analytics |
| Competitor citation share | Prompt audit + comparison | Monthly | CI / SEO |
| DAF coverage (% of pages with DAF) | Content audit | Quarterly | Content team |
| Schema validation pass rate | Google Rich Results Test | Post-publish | Dev / SEO |
| Forum mention volume | Brand monitoring tools | Weekly | Marketing |
