---
name: product-teardown
description: 'Reverse-engineer an existing product to understand its strategy, business model, UX decisions, and growth mechanics. A learning exercise that builds PM judgment. Activate when: "teardown",
  "product teardown", "reverse engineer", "analyze this product", "how does [product] work", "product deep dive" Do NOT activate for: competitive analysis (/competitive-analysis), competitive landscape
  (/competitive-landscape)'
argument-hint: '[product name or URL] — e.g., "Notion", "Linear", "https://cal.com"'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: learning
  skill_type: task-capability
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "add to", "refresh" in input | UPDATE | 100% |
| File path provided | UPDATE | 100% |
| "create", "new", "teardown" in input | CREATE | 100% |
| "find", "search", "list teardowns" | FIND | 100% |
| "the teardown", "last teardown" | UPDATE | 85% |
| Just a product name | CREATE | 80% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new teardown using template below.

**UPDATE**:
1. Check document registry first, then search user's structure
2. Preserve existing analysis sections
3. Add new observations, update competitive context
4. Show diff summary of what changed

**FIND**: Check registry, then search user's folders for teardown documents.

### Search Locations

- `{Product}/Product/teardowns/`
- `context/documents/index.md`
- `context/learnings/`

---

## Vision to Value Phase

**Phase 6: Learning & Adaptation** -- Judgment building through reverse engineering. Teardowns are a learning exercise, not a strategic deliverable.

<!-- Source: Product teardowns as a PM learning tool. Inspired by compound-pm-marketplace `/pm:teardown` (Abhitsian). Also draws from First Round Review's "Product Teardown" series and Lenny Rachitsky's product deep-dives (Lenny's Newsletter). The core insight: reverse-engineering successful products builds product intuition faster than reading frameworks. -->

## Methodology

### The Teardown Framework

<!-- Source: Adapted from compound-pm-marketplace teardown structure (Abhitsian, 2024). The framework combines strategic analysis (business model, positioning) with product craft analysis (UX, growth loops). Key influence: Ben Thompson's Stratechery analysis style — understand the strategy through the product, not just the product through features. -->

Analyze the product through 8 lenses:

#### Lens 1: Target User
- Who is the primary user? Secondary?
- What job are they hiring this product to do?
- What was the user doing before this product existed?

<!-- Source: Jobs-to-be-Done framework, Clayton Christensen, "Competing Against Luck" (2016). The "hiring" metaphor for product adoption. -->

#### Lens 2: Problem Solved
- What pain point does this address?
- How acute is the pain? (Vitamin vs painkiller vs life-saving)
- How is the problem currently solved (alternatives)?

#### Lens 3: Business Model
- How does this product make money?
- What's the pricing structure? (Freemium, subscription, usage, marketplace take rate)
- Who is the economic buyer vs the user?
- What are the unit economics likely to look like?

<!-- Source: Business model analysis approach from Alex Osterwalder & Yves Pigneur, "Business Model Generation" (2010). Revenue model taxonomy from Ash Maurya, "Running Lean" (2012). -->

#### Lens 4: Key Features (Why They Exist)
- List 5-8 core features
- For each: WHY does this feature exist? What behavior does it drive?
- What's notably ABSENT? What did they choose NOT to build?
- What's the feature that makes you go "that's clever"?

#### Lens 5: Growth Mechanics
- What is the primary growth loop? (Viral, content, paid, sales-led)
- Is there a network effect? What kind? (Direct, cross-side, data)
- What's the activation moment? How quickly do new users reach it?
- What's the retention hook?

<!-- Source: Growth loop taxonomy from Reforge (Brian Balfour, Casey Winters). Network effects classification from NFX (James Currier). Activation concept from Chamath Palihapitiya's Facebook growth team. -->

#### Lens 6: Monetization Strategy
- When in the user journey does monetization kick in?
- What triggers the upgrade/purchase decision?
- Is pricing aligned with value delivered?
- What's the expansion revenue mechanism?

#### Lens 7: Competitive Positioning
- Where does this sit in the market?
- What's the core differentiator? (Cost, feature, experience, brand, network)
- Who are they NOT competing with (and why)?
- What would make a user switch away?

<!-- Source: Positioning analysis influenced by April Dunford, "Obviously Awesome" (2019). Competitive strategy categories from Michael Porter, "Competitive Strategy" (1980). -->

#### Lens 8: What to Steal / What to Avoid
- 2-3 things this product does brilliantly that you'd want to emulate
- 1-2 things that are weak or risky that you'd avoid
- 1 non-obvious insight from studying this product

### Quality Gate

A good teardown should make you say "I now understand WHY they built it this way" -- not just WHAT they built.

## Output Structure

```markdown
# Product Teardown: [Product Name]

**Date**: [YYYY-MM-DD]
**Analyst**: [Name/Role]
**Product URL**: [URL]
**Category**: [SaaS / Marketplace / Consumer / Developer Tool / etc.]

## Executive Summary

[2-3 sentences: What this product is, who it serves, and the one insight that stood out most from this teardown.]

## 1. Target User

**Primary user**: [Who]
**Job-to-be-done**: [What they hire this product to do]
**Previous solution**: [What they did before]
**User sophistication**: [Technical / Non-technical / Mixed]

## 2. Problem Solved

**Core pain**: [The problem in one sentence]
**Pain intensity**: [Vitamin / Painkiller / Life-saving]
**Current alternatives**: [How people solve this without the product]
**Why alternatives fail**: [Gap that this product fills]

## 3. Business Model

**Revenue model**: [How it makes money]
**Pricing structure**: [Tiers, pricing philosophy]
**Economic buyer vs user**: [Same / Different — who pays, who uses]
**Monetization timing**: [When in the journey does payment happen]

## 4. Key Features Analysis

| Feature | Why It Exists | Behavior It Drives | Clever Because |
|---------|--------------|-------------------|----------------|
| [Feature 1] | [Strategic reason] | [User behavior] | [Insight] |
| [Feature 2] | [Strategic reason] | [User behavior] | [Insight] |
| [Feature 3] | [Strategic reason] | [User behavior] | [Insight] |

**Notable absences**: [What they chose NOT to build and why]

## 5. Growth Mechanics

**Primary growth loop**: [Viral / Content / Paid / Sales-led / Product-led]
**Network effects**: [Type or None]
**Activation moment**: [What aha moment drives retention]
**Retention hook**: [What keeps users coming back]
**Expansion mechanism**: [How usage/revenue grows within accounts]

## 6. Monetization Strategy

**Free-to-paid trigger**: [What drives conversion]
**Value alignment**: [Is pricing tied to value delivered? How?]
**Expansion revenue**: [How do accounts grow in spend over time]
**Pricing psychology**: [Any clever pricing tactics observed]

## 7. Competitive Positioning

**Market position**: [Leader / Challenger / Niche / Disruptor]
**Core differentiator**: [What makes them defensible]
**NOT competing with**: [Adjacent products they deliberately avoid]
**Switch triggers**: [What would make users leave]

## 8. Steal / Avoid

### What to Steal
1. [Brilliant thing #1 — and why it works]
2. [Brilliant thing #2 — and why it works]
3. [Brilliant thing #3 — and why it works]

### What to Avoid
1. [Weakness #1 — and the risk it creates]
2. [Weakness #2 — and the risk it creates]

### Non-Obvious Insight
[The one thing you didn't expect to learn from this teardown]

## Judgment Notes

[What did this teardown teach you about product strategy? How does it change how you think about your own product decisions?]
```

## Instructions

1. **This is a learning skill, not a deliverable skill.** The output builds PM judgment through reverse engineering. It does not produce strategic documents for the organization.
2. Research the product thoroughly before writing. Use the product if possible. Read their pricing page, changelog, blog, and job postings for clues.
3. Focus on the WHY behind decisions, not just the WHAT.
4. Be opinionated in the "Steal / Avoid" section. Weak teardowns hedge everything.
5. The "Non-Obvious Insight" should genuinely surprise. If it doesn't, dig deeper.
6. Save teardowns to `{Product}/Product/teardowns/` or a personal learning folder.
7. After completing, offer to extract learnings via `/compound` for organizational memory.
8. Consider connecting insights to active products via `/context-save`.

## Integration

- Feeds into: `/compound` (learning extraction), `/context-save` (organizational memory)
- Related to but distinct from: `/competitive-analysis` (strategic), `/competitive-landscape` (market mapping)
- Can inform: `/strategic-bet` (insights from studying others), `/positioning-statement` (differentiation ideas)

## Vision to Value Operating Principle

> "The best product leaders are students of other products. Teardowns build the pattern recognition that separates good decisions from great ones."
