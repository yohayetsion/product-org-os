---
name: geo-playbook
description: Generative Engine Optimization (GEO) frameworks for AI search visibility across ChatGPT, Claude, Gemini, and Google AI Overviews
version: 1.0.0
category: seo
teams:
  - marketing
agents:
  - seo-specialist
  - growth-marketer
  - content-strategist
  - copywriter
  - social-media-manager
  - competitive-intelligence
---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - "The FULL LLM SEO Playbook 2026" (Ordemio) — GEO methodology, 4-engine model, and optimization strategies
  - aaron-he-zhu/seo-geo-claude-skills (github.com/aaron-he-zhu/seo-geo-claude-skills) — SEO/GEO skill patterns
  Adapted and expanded for Product Org OS agents.
-->

# GEO Playbook: Generative Engine Optimization

Reference knowledge pack for optimizing brand visibility across AI-powered search engines. Source: "The FULL LLM SEO Playbook 2026" (Ordemio), adapted for Product Org OS agents.

---

## 1. The 4-Engine Model

### Engine Characteristics

| Engine | How It Selects Content | What Gets Cited | What Gets Ignored |
|--------|----------------------|-----------------|-------------------|
| **ChatGPT (GPT)** | Internal associations from training data + browsing plugin | Brands with strong category-task associations built across many contexts | Promotional claims, niche brands with thin web presence |
| **Claude** | Safety-first eligibility, endorsement risk assessment | Operationally framed content, narrow scoped claims, neutral language | Superlatives, "best" claims, content that creates endorsement risk |
| **Gemini** | Real-time retrieval, document parsing, passage extraction | Well-structured pages with schema, clear authorship, information-dense passages | Thin content, missing structured data, unclear entity relationships |
| **AI Overviews** | Citation-based passage selection from indexed web | Direct Answer Fragments (40-80 words), self-contained logic blocks | Multi-topic pages, promotional language, passages requiring context |

### Engine-Specific Optimization Priorities

**ChatGPT**: Build brand-task associations across the web. Appear in multiple authoritative contexts linking your brand to your category. Integration pages, partnership announcements, case studies on third-party sites all contribute.

**Claude**: Pass the 3-gate eligibility model (see below). Use operational framing ("How teams use X for Y") rather than evaluative framing ("Why X is the best Y"). Keep claims narrow and scoped.

**Gemini**: Structure content for extraction. Use schema markup (Organization, Article, FAQPage, HowTo). Ensure passages are information-dense and self-contained. Authorship and entity clarity matter.

**AI Overviews**: Optimize individual passages, not pages. Create Direct Answer Fragments. Ensure single-role positioning (one clear thing per passage). Remove promotional tension from informational content.

---

## 2. Claude's 3-Gate Eligibility Model

Content must pass all three gates to be cited by Claude:

### Gate 1: Safety
**Question**: Can this question be answered with named brands safely?

- Factual/operational questions: PASS (e.g., "How do teams manage roadmaps?")
- Medical, financial, legal advice: FAIL or highly cautious
- Personal recommendations: FAIL ("What should I buy?")

### Gate 2: Endorsement Risk
**Question**: Does naming this brand create liability for Claude?

- Narrow, scoped claims: PASS ("X is a project management tool used by product teams")
- Superlative claims: FAIL ("X is the best project management tool")
- Promotional language repeated from brand: FAIL (sounds like endorsement)

### Gate 3: Operational Framing
**Question**: Is this framed as how teams work, or as a purchase recommendation?

- "How teams implement insider risk management" → PASS
- "What's the best insider risk tool to buy" → FAIL
- "Tools used for DLP in production environments" → PASS

### Writing for Claude Eligibility

**DO**: Use operational language. Describe what the product does and how teams use it. Keep claims narrow and specific. Attribute capabilities to the product, not to quality judgments.

**DO NOT**: Use superlatives. Make comparative claims without evidence. Frame content as purchase advice. Use promotional brand language in explanatory content.

---

## 3. AI Overview's 3 Selection Gates

### Gate 1: Retrieval
**Question**: Is this content eligible to be pulled at all?

- Indexed by Google: required
- Crawlable and accessible: required
- Schema markup present: strongly preferred
- Recent and maintained: preferred

### Gate 2: Extraction
**Question**: Can a clean answer be isolated from this content?

- Self-contained passages (no "as mentioned above"): required
- Clear topic sentences: strongly preferred
- 40-80 word answer blocks: optimal
- No blended evaluation + definition: required

### Gate 3: Trust
**Question**: Is this content safe to cite relative to competitors?

- Authoritative source: preferred
- No promotional tension: required
- Single-role positioning: preferred
- Consistent with other indexed sources: preferred

---

## 4. Citation Hierarchy (5 States)

Understanding where a brand sits in the citation hierarchy for a given query:

| State | Description | Example | Optimization Goal |
|-------|-------------|---------|------------------|
| **1. Primary Citation** | Named as the go-to solution | "Teams typically use [Brand] for [task]" | Maintain through narrow claims and task alignment |
| **2. Secondary Citation** | Named alongside others | "[Brand], [Competitor], and [Other] are commonly used for [task]" | Differentiate through specificity to move to Primary |
| **3. Named Mention** | Used as an example | "Tools like [Brand] offer [capability]" | Strengthen category association to move to Secondary |
| **4. Paraphrased Abstraction** | Genericized | "Various tools exist for [task]" | Create distinctive, citable passages to break out |
| **5. Omitted** | Not mentioned | No reference to brand | Build web presence and category association from scratch |

### Moving Up the Hierarchy

**5 to 4**: Increase web presence. Get mentioned on third-party sites, forums, comparison pages. Build basic category association.

**4 to 3**: Create distinctive, specific content. Make the brand name unavoidable when discussing the category. Target comparison queries.

**3 to 2**: Strengthen positioning specificity. Own a specific niche within the category. Create content that positions the brand alongside leaders.

**2 to 1**: Narrow the claim. Own one specific task or use case completely. Build depth of association through case studies, documentation, community content.

---

## 5. Passage Optimization

The fundamental unit of GEO optimization is the **passage**, not the page.

### Strong Extractable Passages

Characteristics:
- **Open with a clear claim** (not a question, not a vague statement)
- **State context explicitly** (do not rely on surrounding content)
- **Complete logic loop** in one block (claim + evidence + conclusion)
- **Self-contained**: survives being extracted and placed in any context
- **40-80 words** for Direct Answer Fragments (DAFs)
- **No brand tone** embedded in the explanation
- **No pronouns without anchors** (every "it", "this", "they" has a clear referent)

### Weak Passages (Will Be Ignored)

- Use pronouns without anchors
- Reference earlier sections ("as mentioned above", "building on this")
- Blend evaluation + definition (conflates what something IS with whether it's GOOD)
- Embed brand marketing language inside explanatory content
- Rely on tone, nuance, or rhetorical devices
- Require the reader to have read previous content

### Direct Answer Fragment (DAF) Template

```
[Brand/Product] is [category descriptor] that [primary function].
[Specific approach, method, or differentiator].
[Outcome or use case] for [target user segment].
```

**Good DAF**:
> Datadog is a cloud monitoring platform that aggregates metrics, traces, and logs across infrastructure. It uses an agent-based architecture to collect telemetry from containers, serverless functions, and traditional hosts. DevOps teams use it to detect and resolve production incidents through correlated observability data.

**Bad passage** (will be ignored):
> We're the leading monitoring solution that helps your team work better. Our powerful platform integrates everything you need. See why thousands of companies trust us for their monitoring needs.

### Passage Audit Checklist

For each key passage on a page:
- [ ] Contains a clear claim in the first sentence
- [ ] Is 40-80 words (DAF) or has a 40-80 word extractable block within it
- [ ] No promotional superlatives ("best", "leading", "revolutionary", "powerful")
- [ ] No pronouns without clear referents within the same passage
- [ ] No cross-references to other content ("as discussed", "see above")
- [ ] Single topic per passage (not blending multiple concepts)
- [ ] Would make sense if extracted and placed in a completely different article

---

## 6. Schema Markup for GEO

Only 4 schema types materially impact AI extraction:

| Schema Type | GEO Impact | When to Use |
|-------------|-----------|-------------|
| **Organization** | Entity clarity for all engines | Homepage, about page |
| **Article** | Authorship and publication signals | Blog posts, guides, thought leadership |
| **FAQPage** | Direct extraction of Q&A pairs | FAQ sections, knowledge bases |
| **HowTo** | Step-by-step extraction | Tutorials, implementation guides |

Additional schema types (Product, Review, Event) help traditional SEO but have minimal incremental GEO impact. Prioritize the four above.

---

## 7. Forum Seeding Strategy

Forum content is a significant input to LLM training and retrieval. Strategic presence in Reddit and Quora influences AI responses.

### Reddit Strategy: Distributed Reinforcement

**Target threads**:
- Tool comparisons ("What do you use for [task]?")
- Stack decisions ("Building a [type] stack, what should I include?")
- Migration discussions ("Moving from [X] to [Y]")
- Problem diagnosis ("[Problem] keeps happening, any solutions?")

**Writing rules**:
- Blend naturally into the discussion (not promotional posts)
- One idea per comment section
- Avoid opinion-heavy language ("I love X" is less useful than "X handles [task] by [method]")
- Self-contained explanations that survive being copied into different contexts
- Include specific details (not just brand name drops)

### Quora Strategy: Structured Retrieval Surfaces

**Target questions**:
- "What is [category]?" definitional queries
- "How do companies handle [task]?" operational queries
- "What are alternatives to [competitor]?" comparison queries

**Writing rules**:
- Comprehensive, structured answers (not one-liners)
- Include the brand naturally within a broader category explanation
- Write as a knowledgeable practitioner, not a marketer
- Self-contained: the answer should be useful even without clicking any links

---

## 8. Testing Methodology

### Prompt Types to Test (Minimum 10 prompts, 2+ per type)

| Type | Template | What It Tests |
|------|----------|--------------|
| **Workflow** | "How do teams implement [category]?" | Operational framing, brand-task association |
| **Comparison** | "What tools are used for [X] vs [Y]?" | Competitive positioning, citation state |
| **Migration** | "Switching from [competitor] to [alternative]" | Brand as alternative, migration pathways |
| **Problem-solution** | "[Problem] isn't working, what to use?" | Problem association, solution positioning |
| **Tool selection** | "What's used for [category] in production?" | Production credibility, enterprise positioning |

### What to Track Per Prompt

- Does brand appear consistently across multiple runs?
- Does it appear early or late in the response?
- Does it appear without external citations? (stronger in GPT, indicates trained-in association)
- Is the assigned role stable across different phrasings?
- Does brand survive constraint tightening? ("for enterprise", "for regulated industries", "at scale")

### Constraint Pressure Tests

After baseline testing, add constraints to see if the brand holds:
- Industry: "for healthcare", "for financial services", "for government"
- Scale: "for enterprise", "for startups", "for 1000+ users"
- Compliance: "HIPAA compliant", "SOC 2 certified", "GDPR ready"
- Migration: "switching from [specific competitor]"

If the brand disappears under constraints, the positioning is shallow.

---

## 9. Monitoring KPIs

| KPI | Definition | Measurement Method | Target |
|-----|-----------|-------------------|--------|
| **Citation elevation** | Movement from lower to higher citation state | Monthly re-audit | Upward trend |
| **Citation decay** | Movement from higher to lower citation state | Monthly re-audit | Zero or near-zero |
| **Abstraction rate** | % of responses that abstract brand to "various tools" | Test prompt battery | Decreasing |
| **Constraint sensitivity** | Does brand survive when constraints are added | Pressure test battery | Brand persists under 2+ constraints |
| **Role consistency** | Same role assigned across different prompt phrasings | Cross-prompt comparison | Consistent across 80%+ of prompts |
| **Cross-engine stability** | Brand present across how many engines | Multi-engine audit | 3/4 or 4/4 engines |

### Monitoring Cadence

- **Monthly**: Full audit with prompt battery (all 4 engines)
- **After content changes**: Re-test affected passages
- **After competitor moves**: Test competitor-specific prompts
- **Quarterly**: Full strategy review with trend analysis

---

## 10. Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| **Promotional website copy** | Fails Claude's endorsement gate, AI Overviews trust gate | Rewrite in operational framing |
| **"Best in class" claims** | Gets abstracted or omitted by all engines | Replace with specific, narrow claims |
| **No self-contained passages** | Nothing extractable for AI Overviews or Gemini | Create DAFs for each key capability |
| **Thin forum presence** | No training data for GPT, no retrieval for Gemini | Build authentic Reddit/Quora presence |
| **Broad positioning** | "We do everything" gets abstracted to "various tools" | Own one specific category-task combination |
| **Missing schema** | Gemini cannot parse entity relationships | Add Organization + Article schema minimum |
| **Ignoring Claude's gates** | Content fails safety or endorsement checks | Audit content against the 3-gate model |
| **Page-level thinking** | Optimizing pages instead of passages | Shift to passage-level optimization |

---

## 11. GEO vs Traditional SEO

| Dimension | Traditional SEO | GEO | Overlap |
|-----------|----------------|-----|---------|
| **Unit of optimization** | Page | Passage | Both need quality content |
| **Ranking signal** | Backlinks, authority, relevance | Training data, retrieval, citation eligibility | Both value authoritative sources |
| **Content format** | Keyword-optimized, long-form | Self-contained, extractable blocks | Both reward structured content |
| **Schema** | All types for rich results | Organization, Article, FAQPage, HowTo | Both benefit from structured data |
| **Competition** | SERP positions | Citation slots | Both require competitive monitoring |
| **Measurement** | Rankings, traffic, CTR | Citation state, role consistency, engine coverage | Both need regular auditing |

**Key insight**: GEO does not replace SEO. Strong traditional SEO provides the retrieval foundation that Gemini and AI Overviews depend on. GEO adds a layer of passage-level optimization and engine-specific strategy on top.
