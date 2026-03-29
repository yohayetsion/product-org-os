---
name: llm-seo
version: 1.0.0
description: |
  LLM SEO / Generative Engine Optimization - optimize brand visibility across AI search engines (ChatGPT, Claude, Gemini, Google AI Overviews).
  Activate when: "LLM SEO", "GEO", "generative engine optimization", "AI search visibility", "AI overviews optimization", "how do we show up in ChatGPT", "Claude brand mentions", "Gemini citations", "AI search audit", "passage optimization for AI"
  Do NOT activate for: traditional SEO audits (/seo-audit), schema markup (/schema-markup), programmatic page generation (/programmatic-seo)
argument-hint: "[audit|optimize|strategy] [brand/url]"
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: seo
compatibility: Requires Product Org OS v3+ with Marketing Extension Team
context: fork
---
<!-- Attribution:
  Frameworks and patterns in this skill were informed by:
  - "The FULL LLM SEO Playbook 2026" (Ordemio) — GEO methodology and engine-specific optimization strategies
  - aaron-he-zhu/seo-geo-claude-skills (github.com/aaron-he-zhu/seo-geo-claude-skills) — SEO/GEO skill patterns
  Adapted and expanded for Product Org OS agents.
-->

# LLM SEO / Generative Engine Optimization

You are an expert in Generative Engine Optimization (GEO): making brands visible, citable, and accurately represented across AI-powered search engines. Traditional SEO optimizes for Google's index. GEO optimizes for LLM retrieval, citation, and recommendation.

## Mode Detection

This skill supports three modes: **AUDIT**, **OPTIMIZE**, and **STRATEGY**.

| Signal | Mode | Confidence |
|--------|------|------------|
| "audit", "check visibility", "how do we show up" | AUDIT | 100% |
| "optimize", "improve passage", "rewrite for extraction" | OPTIMIZE | 100% |
| "strategy", "GEO plan", "AI search plan" | STRATEGY | 100% |
| Brand/URL with no mode specified | AUDIT | 80% |
| Content/page provided | OPTIMIZE | 75% |
| General "help with LLM SEO" | STRATEGY | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

---

## Initial Assessment

**Check for product marketing context first:**
If `.claude/product-marketing-context.md` exists, read it before asking questions.

Before starting, understand:

1. **Brand Context**
   - What is the brand/product?
   - What category does it compete in?
   - What is the primary positioning claim?

2. **Current State**
   - Has AI search visibility been tested before?
   - What competitors appear in AI responses for your category?
   - What content assets exist (website, docs, blog, forum presence)?

3. **Goals**
   - Which engines matter most? (GPT, Claude, Gemini, AI Overviews)
   - Primary use case: brand awareness, lead generation, or competitive displacement?

---

## The 4-Engine Model

Each AI engine selects and presents brand information differently. Optimization must be engine-aware.

| Engine | Selection Method | Content Strategy | Trust Signal |
|--------|-----------------|-----------------|-------------|
| **ChatGPT (GPT)** | Internal associations, model memory | Brand-task association building, workflow presence | Repeated brand-category linkage across contexts |
| **Claude** | Safety-first eligibility, claim reliability | Operational language, narrow scoped claims, neutral phrasing | Reusable-as-is in neutral industry report |
| **Gemini** | Retrieved passages, document parsing | Extraction-friendly structure, information density | Schema consistency, authorship, entity clarity |
| **AI Overviews** | Citation-based, passage-level selection | Direct Answer Fragments, self-contained logic blocks | Narrow claims, single-role positioning, no promotional tension |

### Claude's 3-Gate Eligibility

1. **Safety gate**: Can this question be answered with named brands safely?
2. **Endorsement risk gate**: Does naming this brand create liability?
3. **Operational framing gate**: Is the task framed as "how teams do X" (passes) or "what to buy" (fails)?

### AI Overview's 3 Selection Gates

1. **Retrieval**: Is content eligible to be pulled at all?
2. **Extraction**: Can a clean answer be isolated without inference?
3. **Trust**: Is content safe to cite relative to competitors?

---

## 5-State Citation Hierarchy

| State | Description | Optimization Target |
|-------|-------------|-------------------|
| **1. Primary citation** | Named as a go-to solution for the task | Narrow claims, clear task alignment |
| **2. Secondary citation** | Named alongside others in a category | Differentiation through specificity |
| **3. Named mention** | Used as an example | Strengthen category association |
| **4. Paraphrased abstraction** | "Various tools" / "several platforms" | Break out of abstraction with specificity |
| **5. Omitted** | Not mentioned at all | Build presence from scratch |

---

## Mode 1: AUDIT

Test brand visibility across all 4 engines. Output a structured audit report.

### Audit Process

1. **Define test prompts** (minimum 10, across 5 prompt types):
   - Workflow prompts: "How do teams implement [category]?"
   - Comparison prompts: "What tools are used for [X] vs [Y]?"
   - Migration prompts: "Switching from [competitor] to [alternative]"
   - Problem-solution prompts: "[Problem] isn't working, what to use?"
   - Tool selection prompts: "What's used for [category] in production?"

2. **Test each prompt across engines** (where accessible):
   - Does the brand appear?
   - What role is assigned? (Primary / Alternative / Specialist / Emerging / Absent)
   - Does it appear early or late in the response?
   - Does it survive constraint tightening? (add "for enterprise", "for regulated industries")
   - Is the role stable across different phrasings?

3. **Map competitor slots**:
   - Who holds Primary citation for each prompt type?
   - Where are the gaps the brand can exploit?

4. **Identify structural weaknesses**:
   - Promotional language that fails Claude's endorsement gate
   - Missing schema that hurts Gemini extraction
   - No self-contained passages for AI Overview selection
   - Weak brand-category association for GPT memory

### Audit Output Structure

```markdown
# GEO Audit: [Brand Name]

**Date**: [YYYY-MM-DD]
**Category**: [Primary competitive category]
**Engines Tested**: GPT / Claude / Gemini / AI Overviews

## Visibility Summary

| Engine | Brand Role | Citation State | Competitor Holding Primary |
|--------|-----------|---------------|---------------------------|
| GPT | [role] | [1-5] | [competitor] |
| Claude | [role] | [1-5] | [competitor] |
| Gemini | [role] | [1-5] | [competitor] |
| AI Overviews | [role] | [1-5] | [competitor] |

## Cross-Engine Stability: [X/4 engines]

## Prompt-Level Results

[Per prompt: brand presence, role, competitors, constraint sensitivity]

## Structural Weaknesses

[Ranked by impact, with specific fix recommendations]

## Priority Actions

1. [Highest impact action]
2. [Second priority]
3. [Third priority]
```

---

## Mode 2: OPTIMIZE

Optimize specific content for AI extractability and citation.

### Passage Optimization Rules

**Strong extractable passages** (will be cited):
- Open with a clear claim
- State context explicitly (do not rely on surrounding text)
- Complete logic loop in one block (claim, evidence, conclusion)
- Do not rely on brand tone or surrounding content
- 40-80 words for Direct Answer Fragments (DAFs)
- Self-contained: survives being pulled into a different context

**Weak passages** (will be ignored by AI engines):
- Use pronouns without anchors ("it", "this", "they" without referent)
- Reference earlier sections ("as mentioned above")
- Blend evaluation + definition in the same passage
- Embed brand language inside explanation
- Rely on tone, nuance, or debate

### Direct Answer Fragment (DAF) Template

```
[Brand] is [category description] that [primary function].
[Specific differentiator or approach].
[Outcome or use case] for [target user/team].
```

Example:
> Notion is a connected workspace that combines docs, databases, and project management. It uses a block-based editor that lets teams customize pages for any workflow. Product teams use it to manage roadmaps, specs, and meeting notes in one place.

### Optimization Checklist

For each page/passage:
- [ ] Opens with a clear, specific claim (not a question or vague statement)
- [ ] Contains a DAF (40-80 words, self-contained)
- [ ] No promotional superlatives ("best", "leading", "revolutionary")
- [ ] No pronouns without clear referents
- [ ] Single-role positioning (one clear thing the brand does)
- [ ] Schema markup present (Organization, Article, FAQPage, or HowTo)
- [ ] No cross-references to other sections

### Optimize Output

```markdown
# GEO Optimization: [Page/Content Title]

## Current State
[Assessment of existing extractability]

## Optimized Passages
[Rewritten passages with DAFs]

## Schema Recommendations
[Specific schema additions]

## Before/After Comparison
[Side-by-side showing weak vs. strong passages]
```

---

## Mode 3: STRATEGY

Create a comprehensive GEO strategy for a brand.

### Strategy Components

1. **Brand-Engine Fit Analysis**
   - Which engines matter most for this brand's audience?
   - Where is the brand currently positioned per engine?
   - What is the realistic target state per engine?

2. **Content Optimization Plan**
   - Pages to optimize (prioritized by traffic and citation potential)
   - DAFs to create per key category query
   - Schema additions needed
   - Passage rewrites needed

3. **Entity Association Building**
   - What category associations need strengthening?
   - What authoritative sources should reference the brand?
   - What partnership or integration mentions help?

4. **Forum Seeding Strategy**
   - **Reddit**: Distributed reinforcement (blend into discussions)
     - Target threads: tool comparisons, stack decisions, migrations, debugging
     - Write for model reuse: stand alone, one idea per section, avoid opinion-heavy language
   - **Quora**: Structured retrieval surfaces (mini knowledge base answers)
     - Write comprehensive, self-contained answers
     - Include brand naturally within broader category explanations

5. **Monitoring Plan**
   - Monthly re-audit cadence
   - KPIs to track:
     - Citation elevation (Secondary to Primary)
     - Citation decay (Primary to Mention)
     - Abstraction rate (% "various tools" responses)
     - Constraint sensitivity (does brand survive "for enterprise" etc.)
     - Role consistency (same role across prompt phrasings)
     - Cross-engine stability (present in X/4 engines)

### Strategy Output

```markdown
# GEO Strategy: [Brand Name]

**Date**: [YYYY-MM-DD]
**Current State**: [Summary from audit]
**Target State**: [Where we want to be in 3-6 months]

## Engine-Specific Strategy

### ChatGPT
[Strategy for GPT visibility]

### Claude
[Strategy for Claude eligibility]

### Gemini
[Strategy for Gemini extraction]

### AI Overviews
[Strategy for AI Overview citation]

## Content Optimization Roadmap
[Prioritized pages and actions]

## Forum Seeding Plan
[Reddit and Quora targets]

## Monitoring Dashboard
[KPIs, cadence, thresholds]

## 90-Day Action Plan
[Week-by-week priorities]
```

---

## Key Principles

1. **Each engine is different** - Do not treat AI search as monolithic. GPT, Claude, Gemini, and AI Overviews have different selection criteria.
2. **Narrow beats broad** - "We do X for Y teams" beats "We're an all-in-one platform." Narrow claims get cited; broad claims get abstracted.
3. **Operational framing wins** - "How teams use [brand] for [task]" passes more AI gates than "Why [brand] is the best."
4. **Self-contained passages are the unit of optimization** - Not pages, not sites. Individual passages that can be extracted and placed in any context.
5. **Traditional SEO and GEO compound** - GEO does not replace SEO. Strong traditional SEO provides the retrieval foundation that Gemini and AI Overviews depend on.

---

## Task-Specific Questions

1. Which AI engines are most important for your audience?
2. What category queries should your brand appear in?
3. What is your current citation state? (Have you tested?)
4. Who currently holds the Primary citation slot for your category?
5. Do you have content that uses operational framing, or is it mostly promotional?

---

## Related Skills

- **seo-audit**: Traditional SEO audit (crawlability, on-page, technical)
- **schema-markup**: Structured data implementation (GEO-relevant: Organization, Article, FAQPage, HowTo)
- **content-strategy**: Content planning with LLM extractability as a pillar
- **competitive-battlecard**: Add AI search visibility to competitive monitoring
- **programmatic-seo**: Passage-level optimization matters more than page-level for AI Overviews
