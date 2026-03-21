---
name: dhm-analysis
description: |
  Assess product strategy through the Delight, Hard-to-Copy, Margin-Enhancing framework.
  Activate when: "DHM", "delight hard-to-copy margin", "Netflix strategy", "Gibson Biddle", "product strategy assessment", "competitive moat"
  Do NOT activate for: strategic bet formulation (/strategic-bet), competitive landscape mapping (/competitive-landscape)
argument-hint: [product, feature, or initiative name] or [update path/to/dhm-analysis.md]
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
| "update", "revise", "reassess" in input | UPDATE | 100% |
| File path provided (`@path/to/dhm-analysis.md`) | UPDATE | 100% |
| "create", "new", "assess", "evaluate" in input | CREATE | 100% |
| "find", "search", "list DHM analyses" | FIND | 100% |
| "the DHM", "our moat assessment" | UPDATE | 85% |
| Just product or feature name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new DHM analysis using template below.

**UPDATE**:
1. Read existing DHM analysis (search if path not provided)
2. Preserve unchanged sections exactly
3. Update specific pillars, scores, or initiative recommendations
4. Show diff summary: "Updated: [sections]. Unchanged: [sections]."
5. Note: Hard-to-copy advantages evolve over time; reassess periodically

**FIND**:
1. Search paths below for DHM analyses
2. Present results: title, product, overall DHM score, path
3. Ask: "Update one of these, or create new?"

### Search Locations for DHM Analyses

- `strategy/`
- `product/`
- `analysis/`
- `assessments/`

---
## Gotchas

- Delight, Hard-to-Copy, and Margin-Enhancing must each have specific evidence — not just checkboxes
- Hard-to-copy must be genuinely defensible — 'first mover advantage' is rarely defensible long-term



Assess a product or initiative through the **DHM (Delight, Hard-to-Copy, Margin-Enhancing)** framework to evaluate strategic strength and identify the most powerful product strategies.

## Vision to Value Phase

**Phase 2: Strategic Decisions** - DHM analysis informs which product strategies to pursue and which strategic bets to place.

**Prerequisites**: Phase 1 complete (market understanding, customer insight)
**Outputs used by**: Phase 2 (strategic bets, business cases), Phase 3 (roadmap prioritization)

## Methodology

<!-- Source: DHM Model - Gibson Biddle (former VP Product at Netflix 2005-2010, CPO at Chegg 2010-2012, currently product strategy advisor and educator). Published through his "Ask Gib" newsletter, Medium articles, and product strategy workshops (~2019-present). Core question: "How will your product delight customers in hard-to-copy, margin-enhancing ways?" The power is in strategies that achieve 2-3 pillars simultaneously with a single initiative. -->

<!-- Source: Three Pillars - Gibson Biddle. Delight: Creates emotional connection, solves pain points in ways customers love, generates NPS/word-of-mouth. Hard-to-Copy: Advantages that take years to replicate or cannot be copied at all. Margin-Enhancing: Increases revenue per user, reduces cost to serve, or improves unit economics over time. -->

<!-- Source: Hard-to-Copy Advantage Types - Combines Gibson Biddle's categories (Brand, Network Effects, Economies of Scale, Unique Technology, Counter-Positioning, Switching Costs) with Hamilton Helmer's "7 Powers" (2016, "7 Powers: The Foundations of Business Strategy"). Helmer's 7 Powers: Scale Economies, Network Economies, Counter-Positioning, Switching Costs, Branding, Cornered Resource, Process Power. Biddle's framework overlaps significantly but is more product-centric. -->

<!-- Source: GEM Extension - Gibson Biddle. Growth, Engagement, Monetization evaluation framework used alongside DHM to assess how initiatives drive business metrics. Growth = user acquisition and expansion. Engagement = depth and frequency of usage. Monetization = revenue generation and unit economics improvement. -->

### The Three Pillars

| Pillar | Core Question | What to Look For |
|--------|--------------|-----------------|
| **Delight** | Does this make customers measurably happier? | NPS improvement, retention lift, word-of-mouth, reduced support tickets, emotional response |
| **Hard-to-Copy** | Would a well-funded competitor struggle to replicate this? | Time to copy >2 years, requires unique assets, benefits from scale/network effects |
| **Margin-Enhancing** | Does this improve unit economics over time? | Higher ARPU, lower CAC, reduced cost-to-serve, pricing power, operating leverage |

### Hard-to-Copy Advantage Types

<!-- Source: Hamilton Helmer, "7 Powers: The Foundations of Business Strategy", 2016. Combined with Gibson Biddle's product-centric categorization. -->

| Advantage Type | Description | Strength | Time to Build |
|---------------|------------|----------|---------------|
| **Brand** | Emotional association, trust, identity | Strong | Years |
| **Network Effects** | Product improves as more people use it | Very Strong | Years |
| **Economies of Scale** | Cost advantages from volume | Strong | Years |
| **Counter-Positioning** | Incumbent can't copy without cannibalizing | Very Strong | Structural |
| **Switching Costs** | Pain of leaving exceeds pain of staying | Strong | Months-Years |
| **Cornered Resource** | Exclusive access to valuable asset (data, talent, IP) | Very Strong | Varies |
| **Process Power** | Organizational capabilities that can't be bought | Strong | Years |

### Pillar Scoring

| Score | Meaning | Evidence Required |
|-------|---------|------------------|
| **Strong** | Clear, demonstrable advantage | Multiple data points, customer evidence |
| **Moderate** | Emerging advantage, needs investment | Some signals, hypothesis supported |
| **Weak** | Minimal or no advantage today | Little evidence, aspiration only |

## Output Structure

```markdown
# DHM Analysis: [Product/Initiative Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Single accountable person]
**Product**: [Product name - optional, for multi-product organizations]
**Scope**: [Entire product / Specific feature / Initiative]

## Executive Summary

[One paragraph: Overall DHM assessment and the key strategic insight]

## Pillar 1: Delight

**Score**: Strong / Moderate / Weak

### Current Delight Sources
| Source | Customer Segment | Evidence | Strength |
|--------|-----------------|----------|----------|
| [What delights] | [Who] | [NPS, quotes, data] | [Strong/Moderate/Weak] |

### Delight Gaps
| Gap | Impact | Opportunity |
|-----|--------|------------|
| [What's missing] | [How it hurts] | [What to do] |

### Delight Trajectory
[Is delight growing, stable, or declining? Why?]

## Pillar 2: Hard-to-Copy

**Score**: Strong / Moderate / Weak

### Current Advantages
| Advantage Type | Description | Strength | Time for Competitor to Replicate |
|---------------|------------|----------|--------------------------------|
| [Type from table above] | [Specific advantage] | [Strong/Moderate/Weak] | [Months/Years/Cannot] |

### Advantage Durability Assessment
| Advantage | Current Moat | Threats to Moat | Investment to Maintain |
|-----------|-------------|----------------|----------------------|
| [Advantage] | [How deep] | [What could erode it] | [What's needed] |

### Missing Advantages
| Advantage Type | Feasibility | Investment Required | Timeline |
|---------------|------------|-------------------|----------|
| [Type not yet present] | [High/Medium/Low] | [What it takes] | [How long] |

## Pillar 3: Margin-Enhancing

**Score**: Strong / Moderate / Weak

### Unit Economics Impact
| Metric | Current | Trend | Impact of Strategy |
|--------|---------|-------|-------------------|
| ARPU | [Current or TBD] | [Up/Flat/Down] | [How strategy affects it] |
| CAC | [Current or TBD] | [Up/Flat/Down] | [How strategy affects it] |
| LTV:CAC | [Current or TBD] | [Up/Flat/Down] | [How strategy affects it] |
| Gross Margin | [Current or TBD] | [Up/Flat/Down] | [How strategy affects it] |

### Margin Trajectory
[Does this strategy improve margins over time, or is it margin-neutral/negative?]

### Pricing Power Assessment
[Does this strategy give us more pricing power? How?]

## DHM Scorecard

| Pillar | Score | Key Evidence | Trend |
|--------|-------|-------------|-------|
| **Delight** | [Strong/Moderate/Weak] | [Primary evidence] | [Improving/Stable/Declining] |
| **Hard-to-Copy** | [Strong/Moderate/Weak] | [Primary advantage] | [Strengthening/Stable/Eroding] |
| **Margin-Enhancing** | [Strong/Moderate/Weak] | [Primary metric] | [Improving/Stable/Declining] |

**Overall DHM Strength**: [Strong (3/3) / Good (2/3) / Needs Work (1/3) / Critical (0/3)]

## GEM Evaluation

| Dimension | Impact | How |
|-----------|--------|-----|
| **Growth** | [High/Medium/Low/None] | [How this drives user growth] |
| **Engagement** | [High/Medium/Low/None] | [How this deepens engagement] |
| **Monetization** | [High/Medium/Low/None] | [How this improves monetization] |

## Strategic Initiatives (Multi-Pillar Opportunities)

The most powerful strategies hit 2-3 DHM pillars simultaneously.

### Initiative 1: [Name]

**Pillars Hit**: [D + H / D + M / H + M / D + H + M]

| Pillar | How This Initiative Contributes |
|--------|-------------------------------|
| Delight | [Specific delight mechanism] |
| Hard-to-Copy | [Specific advantage created] |
| Margin-Enhancing | [Specific margin improvement] |

**Priority**: [P0 / P1 / P2]
**Rationale**: [Why this initiative is powerful]

### Initiative 2: [Name]

[Same structure]

## Recommendations

### Strengthen (Current Weakest Pillar)
[What to do about the weakest DHM pillar]

### Protect (Current Strongest Pillar)
[How to maintain the strongest advantage]

### Build (Highest-Impact Multi-Pillar Initiative)
[Which initiative to prioritize and why]

## Assumptions

| # | Assumption | Confidence | If Wrong |
|---|-----------|-----------|----------|
| 1 | [Assumption] | [Low/Med/High] | [Impact] |
| 2 | [Assumption] | [Low/Med/High] | [Impact] |
```

## Instructions

1. Ask clarifying questions about the product's current position and available data
2. **Check prior context**: Run `/context-recall [product]` to find related strategic bets, competitive analyses, and positioning decisions
3. **Check feedback**: Run `/feedback-recall [product/delight/satisfaction]` for customer signals
4. Reference any competitive analysis, market research, or strategy documents provided via @file syntax
5. Score each pillar honestly; Weak is a valid and useful assessment
6. Focus on multi-pillar initiatives as the key strategic output
7. Distinguish between current state and aspiration
8. Save in strategy/ or product/ folder
9. Offer to create presentation version using /present

## Context Integration

After generating the DHM analysis:

1. **Offer to save**: Ask "Should I save this to the context registry? (`/context-save`)"
2. If yes, extract and save:
   - DHM scores and key findings to context
   - Link to related strategic bets, competitive landscape, and positioning
   - Assumptions to `context/assumptions/registry.md`
3. Suggest `/strategic-bet` for high-priority multi-pillar initiatives
