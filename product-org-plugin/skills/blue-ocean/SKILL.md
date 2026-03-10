---
name: blue-ocean
description: |
  Apply Blue Ocean Strategy to identify uncontested market space using the Strategy Canvas, ERRC Grid, and Six Paths Framework.
  Activate when: "blue ocean", "strategy canvas", "ERRC", "eliminate reduce raise create", "uncontested market", "value innovation", "red ocean blue ocean"
  Do NOT activate for: competitive landscape (/competitive-landscape), market segment (/market-segment), positioning statement (/positioning-statement)
argument-hint: [product or market] or [update path/to/blue-ocean.md]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: strategy
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "iterate" in input | UPDATE | 100% |
| File path provided (`@path/to/blue-ocean.md`) | UPDATE | 100% |
| "create", "new", "find blue ocean" in input | CREATE | 100% |
| "find", "search", "list blue ocean" | FIND | 100% |
| "the strategy canvas", "our blue ocean" | UPDATE | 85% |
| Just a product/market name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Build strategy canvas comparing current offering vs. competitors, generate ERRC grid, apply Six Paths Framework, identify noncustomers, and recommend blue ocean moves.

**UPDATE**:
1. Read existing Blue Ocean analysis (search if path not provided)
2. Preserve strategy canvas factors, update competitive positions or value curves
3. Refine ERRC actions based on new insights
4. Show diff summary: "Updated: [sections]. New factors: [count]. ERRC changes: [summary]."

**FIND**:
1. Search paths below for Blue Ocean strategy documents
2. Present results: product/market, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `strategy/`
- `product/`
- `competitive/`
- `analysis/`

---

## Vision to Value Phase

**Phase 1: Strategic Foundation** - Blue Ocean Strategy helps identify uncontested market space before committing to competitive positioning, creating the foundation for differentiated strategic intent.

**Prerequisites**: Understanding of current market, competitors, and industry factors
**Outputs used by**: `/strategic-intent` (differentiated direction), `/positioning-statement` (unique positioning), `/strategic-bet` (blue ocean move as a bet), `/market-segment` (noncustomer segments)

## Methodology

<!-- Source: Blue Ocean Strategy — W. Chan Kim & Renée Mauborgne, "Blue Ocean Strategy: How to Create Uncontested Market Space and Make the Competition Irrelevant" (2005, expanded edition 2015), Harvard Business Review Press. Kim and Mauborgne are professors at INSEAD. The book is based on a study of 150 strategic moves spanning more than 100 years and 30 industries. Key insight: the most successful companies create new market spaces ("blue oceans") rather than competing in existing markets ("red oceans"). -->

<!-- Source: Value Innovation — Kim & Mauborgne, "Value Innovation: The Strategic Logic of High Growth", Harvard Business Review (1997). The foundational concept: value innovation occurs when companies align innovation with utility, price, and cost positions. Unlike conventional strategy (which sees value-cost as a tradeoff), value innovation pursues BOTH differentiation AND low cost simultaneously by eliminating and reducing factors the industry competes on while raising and creating factors the industry has never offered. -->

<!-- Source: Strategy Canvas — Kim & Mauborgne. A diagnostic and action framework. The horizontal axis captures the range of factors the industry competes on and invests in. The vertical axis captures the offering level that buyers receive across these factors. The "value curve" is a graphic depiction of a company's relative performance across its industry's factors of competition. A blue ocean move requires a fundamentally different value curve, not incremental improvements. -->

<!-- Source: ERRC Grid (Four Actions Framework) — Kim & Mauborgne. Four questions that challenge industry logic: (1) Eliminate: Which factors that the industry takes for granted should be eliminated? (2) Reduce: Which factors should be reduced well below the industry standard? (3) Raise: Which factors should be raised well above the industry standard? (4) Create: Which factors should be created that the industry has never offered? The grid forces simultaneous pursuit of differentiation and low cost. -->

<!-- Source: Six Paths Framework — Kim & Mauborgne. Six approaches to reconstructing market boundaries: (1) Look across alternative industries, (2) Look across strategic groups within the industry, (3) Look across the chain of buyers, (4) Look across complementary product and service offerings, (5) Look across functional-emotional appeal to buyers, (6) Look across time (trends). Each path provides a systematic way to identify blue ocean opportunities that competitors miss. -->

<!-- Source: Three Tiers of Noncustomers — Kim & Mauborgne. First tier: "soon-to-be" noncustomers on the edge of the market, ready to leave. Second tier: "refusing" noncustomers who consciously chose against the market. Third tier: "unexplored" noncustomers in distant markets who have never considered the industry's offerings. The largest growth potential often lies in the second and third tiers. -->

<!-- Source: Buyer Utility Map — Kim & Mauborgne. A 6x6 matrix: Six stages of the buyer experience cycle (Purchase, Delivery, Use, Supplements, Maintenance, Disposal) crossed with six utility levers (Customer Productivity, Simplicity, Convenience, Risk, Fun/Image, Environmental Friendliness). Used to identify utility blocks and unlock new demand. -->

<!-- Source: Inspiration — deanpeters/Product-Manager-Skills blue-ocean implementation contributed to skill structure and activation pattern design. -->

### Core Concepts

#### Red Ocean vs. Blue Ocean

| Dimension | Red Ocean | Blue Ocean |
|-----------|----------|------------|
| **Market space** | Compete in existing | Create uncontested |
| **Competition** | Beat the competition | Make competition irrelevant |
| **Demand** | Exploit existing | Create and capture new |
| **Value-cost** | Tradeoff (choose one) | Break the tradeoff |
| **Strategy** | Differentiation OR low cost | Differentiation AND low cost |

#### The Strategy Canvas

The strategy canvas has two axes:
- **Horizontal**: Key factors the industry competes on (e.g., price, features, service, brand, etc.)
- **Vertical**: Offering level (high to low) for each factor

Plot value curves for:
1. Your current offering
2. Key competitors
3. Your proposed blue ocean move

A blue ocean value curve looks fundamentally different from competitors, not just higher.

#### The ERRC Grid

| Action | Question | Effect |
|--------|----------|--------|
| **Eliminate** | Which factors that the industry takes for granted should be eliminated? | Removes cost, reduces complexity |
| **Reduce** | Which factors should be reduced well below the industry standard? | Strips away over-design |
| **Raise** | Which factors should be raised well above the industry standard? | Breaks from industry norms |
| **Create** | Which factors should be created that the industry has never offered? | Creates new sources of value |

#### Six Paths Framework

| Path | Look Across | Question |
|------|------------|----------|
| **1. Alternative industries** | Industries that serve the same purpose differently | Why do customers choose alternatives over our industry? |
| **2. Strategic groups** | Groups within the industry (e.g., premium vs. budget) | Why do customers trade up or down between groups? |
| **3. Buyer groups** | The chain of buyers (purchasers, users, influencers) | Which buyer group does the industry focus on? What if we focused on a different one? |
| **4. Complementary offerings** | Products/services used before, during, or after yours | What happens before, during, and after using the product? What pain points exist? |
| **5. Functional-emotional appeal** | Whether the industry competes on function or emotion | Can we switch from functional to emotional appeal, or vice versa? |
| **6. Time/Trends** | Trends that are decisive to the industry | What trends have high probability and irreversible trajectory? |

#### Three Tiers of Noncustomers

| Tier | Description | Distance from Market |
|------|------------|---------------------|
| **First** | "Soon-to-be" noncustomers on the market edge | Closest; use offerings minimally, ready to leave |
| **Second** | "Refusing" noncustomers | Consciously rejected the market's offerings |
| **Third** | "Unexplored" noncustomers | In distant markets; never considered the industry |

## Output Structure

```markdown
# Blue Ocean Strategy: [Product / Market]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this analysis]
**Industry**: [Industry being analyzed]
**Current strategic posture**: [Red ocean / Partial blue / Blue ocean]

## Executive Summary

[2-3 paragraph overview: current competitive landscape, the blue ocean opportunity identified, and the proposed strategic move]

## Current Strategy Canvas

### Industry Competing Factors

| Factor | Industry Importance | Your Offering | Competitor A | Competitor B | Industry Average |
|--------|-------------------|---------------|-------------|-------------|-----------------|
| [Factor 1] | High/Med/Low | [1-10] | [1-10] | [1-10] | [1-10] |
| [Factor 2] | High/Med/Low | [1-10] | [1-10] | [1-10] | [1-10] |
| [Factor 3] | High/Med/Low | [1-10] | [1-10] | [1-10] | [1-10] |
| [Factor 4] | High/Med/Low | [1-10] | [1-10] | [1-10] | [1-10] |
| [Factor 5] | High/Med/Low | [1-10] | [1-10] | [1-10] | [1-10] |
| [Factor 6] | High/Med/Low | [1-10] | [1-10] | [1-10] | [1-10] |

### Value Curve Visualization

```
HIGH  |
      |     *---*           C = Competitor A
      | *--/     \    *     Y = Your offering
      |/          \--/ \    B = Competitor B
      |                 *
LOW   |________________________
       F1  F2  F3  F4  F5  F6
```

### Current Canvas Analysis
[What does the canvas reveal? Are all curves similar (red ocean)? Where are there convergence patterns?]

## ERRC Grid

### Eliminate

| Factor | Why Eliminate | Cost Saved | Customer Impact |
|--------|-------------|------------|-----------------|
| [Factor] | [Industry takes this for granted but customers don't value it] | [Impact] | [Minimal/None] |

### Reduce

| Factor | Reduce To | Why | Cost Saved | Customer Impact |
|--------|----------|-----|------------|-----------------|
| [Factor] | [New level] | [Over-designed relative to actual need] | [Impact] | [Acceptable] |

### Raise

| Factor | Raise To | Why | Investment | Customer Impact |
|--------|---------|-----|------------|-----------------|
| [Factor] | [New level] | [Industry standard is too low for buyer utility] | [Impact] | [Significant] |

### Create

| New Factor | Description | Why Unprecedented | Investment | Customer Impact |
|-----------|------------|-------------------|------------|-----------------|
| [Factor] | [What it is] | [Industry has never offered this] | [Impact] | [Transformative] |

### ERRC Validation
- Does eliminating/reducing offset the cost of raising/creating? [Yes/No/Partially]
- Does the new value curve diverge from industry standard? [Yes/No]
- Is the new curve focused, divergent, and compelling? [Assessment]

## Proposed Blue Ocean Strategy Canvas

| Factor | Industry Average | Your Blue Ocean Move |
|--------|-----------------|---------------------|
| [Eliminated factor] | [X] | 0 |
| [Reduced factor] | [X] | [Lower] |
| [Existing factor] | [X] | [Same] |
| [Raised factor] | [X] | [Higher] |
| [Created factor] | 0 | [New level] |

### New Value Curve
[Description of how the new curve is fundamentally different from the industry]

## Six Paths Analysis

### Path 1: Alternative Industries
- **Alternatives examined**: [What alternatives serve the same purpose?]
- **Key insight**: [Why customers choose alternatives]
- **Blue ocean opportunity**: [How to incorporate alternative industry strengths]

### Path 2: Strategic Groups
- **Groups identified**: [Premium, mid-market, budget, etc.]
- **Key insight**: [Why customers move between groups]
- **Blue ocean opportunity**: [How to bridge group boundaries]

### Path 3: Buyer Groups
- **Current industry focus**: [Purchaser / User / Influencer]
- **Overlooked buyer**: [Which group is being ignored?]
- **Blue ocean opportunity**: [What changes if we focus on the overlooked buyer?]

### Path 4: Complementary Offerings
- **Before/during/after usage**: [What pain points exist in the broader experience?]
- **Key insight**: [Untapped complementary needs]
- **Blue ocean opportunity**: [How to solve the complementary pain]

### Path 5: Functional-Emotional Appeal
- **Current industry appeal**: [Functional / Emotional]
- **Key insight**: [What happens if we switch?]
- **Blue ocean opportunity**: [How to redefine the appeal]

### Path 6: Time/Trends
- **Decisive trends**: [Trends with high probability and irreversible trajectory]
- **Key insight**: [How these trends reshape buyer value]
- **Blue ocean opportunity**: [How to ride the trend ahead of competitors]

### Most Promising Path(s)
[Which 1-2 paths offer the strongest blue ocean opportunity and why]

## Noncustomer Analysis

### First Tier: Soon-to-Be Noncustomers
- **Who**: [Description]
- **Why leaving**: [What pushes them to the edge]
- **How to pull them in**: [What would change their mind]

### Second Tier: Refusing Noncustomers
- **Who**: [Description]
- **Why refusing**: [What made them consciously reject]
- **How to convert**: [What would make them reconsider]

### Third Tier: Unexplored Noncustomers
- **Who**: [Description]
- **Why unexplored**: [Why the industry never targeted them]
- **How to reach**: [What new value proposition would attract them]

### Noncustomer Demand Potential
[Which tier represents the largest untapped demand? What would it take to unlock it?]

## Blue Ocean Move Recommendation

### The Proposed Move
[Clear statement of the blue ocean strategy: what to eliminate, reduce, raise, and create to unlock new demand]

### Value Innovation Test
- Does this break the value-cost tradeoff? [Yes/No]
- Does it create new demand (not just steal share)? [Yes/No]
- Does it make competition irrelevant? [Yes/No]
- Is the value curve divergent, focused, and compelling? [Yes/No]

### Key Risks
| Risk | Mitigation | Impact if Unmitigated |
|------|------------|----------------------|
| [Risk 1] | [Mitigation] | High/Med/Low |
| [Risk 2] | [Mitigation] | High/Med/Low |

### Assumptions to Validate
| # | Assumption | Validation Method | Timeline |
|---|-----------|------------------|----------|
| 1 | [Assumption] | [Method] | [When] |
| 2 | [Assumption] | [Method] | [When] |

## Next Steps

- [ ] Validate ERRC assumptions via `/assumption-map`
- [ ] Define strategic intent around the blue ocean move via `/strategic-intent`
- [ ] Frame as a strategic bet via `/strategic-bet`
- [ ] Test noncustomer hypotheses via `/experiment-design`
- [ ] Develop positioning for the new market space via `/positioning-statement`
- [ ] Identify target noncustomer segments via `/market-segment`
```

## Instructions

1. Start by mapping the current industry's competing factors (the strategy canvas horizontal axis)
2. Plot your offering and 2-3 key competitors on the canvas
3. Look for convergence: if all value curves look similar, the industry is a red ocean
4. Work through the ERRC grid systematically: eliminations and reductions must offset raises and creations
5. Apply at least 3 of the 6 Paths to generate blue ocean ideas
6. Always analyze noncustomers: the biggest opportunities often lie outside current customers
7. Validate that the proposed move breaks the value-cost tradeoff (not just differentiation at higher cost)
8. Use WebSearch for competitive data and industry analysis when available
9. Save output as markdown file
10. Offer `/strategic-bet` to frame the blue ocean move as a formal strategic bet or `/assumption-map` for validation

## Integration

- Links to `/strategic-intent` (blue ocean move defines strategic direction)
- Links to `/strategic-bet` (frame the move as a bet with explicit assumptions)
- Links to `/positioning-statement` (positioning for the new market space)
- Links to `/market-segment` (noncustomer segments as new targets)
- Links to `/assumption-map` (validate ERRC and noncustomer assumptions)
- Links to `/experiment-design` (test noncustomer hypotheses)
- Links to `/competitive-landscape` (input for current strategy canvas)
- Links to `/context-save` (save for tracking execution of the blue ocean move)
