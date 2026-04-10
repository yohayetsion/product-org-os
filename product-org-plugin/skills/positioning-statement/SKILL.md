---
name: positioning-statement
description: "Create a positioning statement defining market category, differentiation, and target audience framing. Activate when: \"define our positioning\", \"how should we position\", \"positioning statement\", differentiation, category creation, messaging framework Do NOT activate for: GTM execution strategy (/gtm-strategy), campaign briefs (/campaign-brief), competitive analysis (/competitive-analysis)"
argument-hint: "[product name] or [update path/to/positioning.md]"
user-invocable: true
metadata:
  author: Product Org OS
  version: 3.0.0
  category: market-analysis
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "modify" in input | UPDATE | 100% |
| File path provided (`@path/to/positioning.md`) | UPDATE | 100% |
| "create", "new", "draft" in input | CREATE | 100% |
| "find", "search", "list positioning" | FIND | 100% |
| "the positioning", "our positioning" | UPDATE | 85% |
| Just product name | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new positioning statement using template below.

**UPDATE**:
1. Read existing positioning doc (search if path not provided)
2. Preserve unchanged sections exactly
3. Update messaging, differentiation, or competitor sections
4. Increment version number
5. Show diff summary: "Updated: [sections]. Version: X → Y."

**FIND**:
1. Search paths below for positioning documents
2. Present results: product, version, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations for Positioning

- `positioning/`
- `marketing/`
- `gtm/`
- `messaging/`

---
## Gotchas

- Positioning must be based on real differentiation, not aspirational claims
- Target audience must be specific enough to exclude some customers — 'everyone' is not a segment
- Competitive frame of reference must name real alternatives the customer considers



Create a **Positioning Statement** for the specified product.

## Vision to Value Phase

**Phase 2: Strategic Decisions** - Positioning defines how we compete and is foundational to GTM.

**Prerequisites**: Phase 1 complete (competitive analysis, market segment, vision)
**Outputs used by**: Phase 3 (GTM strategy, messaging), Phase 4 (campaigns, sales enablement)

## Methodology

<!-- Source: April Dunford, "Obviously Awesome" (2019)
     Dunford's 5-step positioning process: Competitive Alternatives → Unique Attributes →
     Value → Target Customer Characteristics → Market Category.
     Key insight: positioning is NOT messaging — it's the strategic context that makes
     messaging obvious. Start from what customers would use if you didn't exist. -->

This skill follows **April Dunford's positioning methodology** from *Obviously Awesome*. The process works **inside-out**: start with competitive alternatives (what customers would do without you), derive unique attributes, map to customer value, identify who cares most, then choose the market category that makes your value obvious.

### Dunford's 5-Step Process

| Step | Question | Output |
|------|----------|--------|
| 1. Competitive Alternatives | What would customers use if we didn't exist? | List of real alternatives (including "do nothing") |
| 2. Unique Attributes | What do we have that alternatives lack? | Defensible capabilities, features, or properties |
| 3. Value | What value do those attributes enable? | Customer outcomes tied to unique attributes |
| 4. Target Customer Characteristics | Who cares most about that value? | Characteristics of best-fit customers |
| 5. Market Category | What context makes our value obvious? | Category name + positioning strategy |

### Category Strategy Decision

<!-- Source: April Dunford, "Obviously Awesome" ch. 10-12
     Three positioning strategies: Head-to-Head (win in existing category),
     Big Fish Small Pond (dominate a subsegment), Create New Category (reframe the market). -->

| Strategy | When to Use | Risk |
|----------|-------------|------|
| **Head-to-Head** | Strong in existing category, clear differentiator | Must beat incumbents on their turf |
| **Big Fish, Small Pond** | Can dominate a subsegment before expanding | Market may be too small |
| **Create New Category** | Truly novel, no existing category fits | Must educate market (expensive, slow) |

## Output Structure

```markdown
# Positioning Statement: [Product Name]

**Version**: [Version]
**Owner**: [Name]
**Date**: [Date]

## Positioning Canvas
<!-- Source: Derived from April Dunford's "Obviously Awesome" 5-step process -->

### Step 1: Competitive Alternatives
What would our best customers use if we didn't exist?
| Alternative | Type | Why customers use it |
|-------------|------|---------------------|
| [Alt 1] | Direct / Indirect / Status quo | [Reason] |
| [Alt 2] | Direct / Indirect / Status quo | [Reason] |

### Step 2: Unique Attributes
What do we have that none of the alternatives have?
| Attribute | Which alternatives lack it | Defensible? |
|-----------|---------------------------|-------------|
| [Attr 1] | [Which] | Yes/No + why |
| [Attr 2] | [Which] | Yes/No + why |

### Step 3: Value
What value do those attributes enable for customers?
| Attribute | Enabled Value | Evidence |
|-----------|--------------|----------|
| [Attr 1] | [Customer outcome] | [Proof] |
| [Attr 2] | [Customer outcome] | [Proof] |

### Step 4: Target Customer Characteristics
Who cares most about the value we deliver?
| Characteristic | Why it matters |
|---------------|----------------|
| [Char 1] | [They care because...] |
| [Char 2] | [They care because...] |

### Step 5: Market Category
What category context makes our value obvious?
**Category**: [Category name]
**Strategy**: Head-to-Head / Big Fish Small Pond / Create New Category
**Rationale**: [Why this category and strategy]

## Positioning Statement

**For** [target customer segment — from Step 4]
**Who** [statement of need or opportunity]
**The** [product name]
**Is a** [product category — from Step 5]
**That** [key benefit / reason to buy — from Step 3]
**Unlike** [primary competitive alternative — from Step 1]
**Our product** [primary point of differentiation — from Step 2]

## Expanded Positioning

### Target Customer
**Who they are**: [Description]
**What they do**: [Role/function]
**What they care about**: [Priorities]
**Best-fit characteristics**: [From Step 4 — what makes someone an ideal customer]

### Need / Opportunity
**The problem**: [What problem they face]
**Current solutions**: [How they solve it today — from Step 1]
**Gap**: [What's missing — links to Step 2]

### Category
**Category we play in**: [Category name — from Step 5]
**Category strategy**: [Head-to-Head / Big Fish Small Pond / Create New Category]
**Why this category**: [Rationale — why this context makes value obvious]
**Category alternatives considered**: [Other categories and why rejected]

### Key Benefit
**Primary benefit**: [Main benefit — from Step 3]
**Benefit proof**: [Evidence]
**Benefit to whom**: [Which persona cares most — from Step 4]

### Differentiation
**Primary differentiator**: [From Step 2]
**Defensibility**: [Why hard to copy]
**Evidence**: [Proof of differentiation]

## Positioning vs. Competitors

| Competitor | Their Position | Our Unique Attributes vs. Them | Our Value vs. Them |
|------------|----------------|-------------------------------|-------------------|
| [Competitor 1] | [Their positioning] | [What we have they don't] | [Value we enable they can't] |
| [Competitor 2] | [Their positioning] | [What we have they don't] | [Value we enable they can't] |

## Positioning Perceptual Map

**Axes**:
- X-axis: [Dimension 1, e.g., Simple ← → Complex]
- Y-axis: [Dimension 2, e.g., Cheap ← → Premium]

**Our Position**: [Where we sit and why]

## Message Hierarchy

**Tagline**: [Short memorable phrase]
**Elevator Pitch** (30 seconds): [Brief pitch]
**Key Messages** (each tied to a unique attribute → value pair):
1. [Message 1] ← [Attribute → Value link]
2. [Message 2] ← [Attribute → Value link]
3. [Message 3] ← [Attribute → Value link]

## Proof Points

| Claim | Proof | Source |
|-------|-------|--------|
| [Claim 1] | [Evidence] | [Customer quote / data / case study] |
| [Claim 2] | [Evidence] | [Customer quote / data / case study] |
| [Claim 3] | [Evidence] | [Customer quote / data / case study] |

## Positioning by Audience

| Audience | Emphasis | Key Message | Unique Attributes to Lead With |
|----------|----------|-------------|-------------------------------|
| [Buyer] | [What to emphasize] | [Message] | [Which attributes] |
| [User] | [What to emphasize] | [Message] | [Which attributes] |
| [Influencer] | [What to emphasize] | [Message] | [Which attributes] |
```

## Instructions

1. **Start with Competitive Alternatives** (Step 1) — ask "What would your customers do if you didn't exist?" if not clear
<!-- Source: Dunford principle — positioning starts from the customer's real alternatives, not your features -->
2. Work through Steps 2-5 in order — each step feeds the next
3. Reference any competitive or market documents via @file syntax
4. Ensure unique attributes (Step 2) are genuinely defensible
5. Verify value claims (Step 3) have evidence, not assumptions
6. Choose category strategy (Step 5) deliberately — don't default to "create new category"
<!-- Source: Dunford warns most startups default to category creation when they shouldn't —
     it's the hardest and most expensive strategy -->
7. Save in positioning/ or gtm/ folder
