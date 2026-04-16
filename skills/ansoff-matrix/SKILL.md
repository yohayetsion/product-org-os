---
name: ansoff-matrix
description: 'Analyze growth direction options using the Ansoff Product/Market Expansion Grid. Activate when: "Ansoff", "growth matrix", "market penetration", "diversification", "product market expansion",
  "growth direction", "where to grow" Do NOT activate for: market analysis (/market-analysis), strategic intent (/strategic-intent)'
argument-hint: '[product or business unit] or [update path/to/ansoff-matrix.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: strategy
  skill_type: task-capability
  owner: bizdev
  primary_consumers:
  - bizdev
  - head-corpdev
  secondary_consumers:
  - cpo
  - pm-dir
  - corporate-venture
  - strategic-partnerships
  - ceo
  - market-researcher
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided (`@path/to/ansoff-matrix.md`) | UPDATE | 100% |
| "create", "new", "analyze growth" in input | CREATE | 100% |
| "find", "search", "list matrices" | FIND | 100% |
| "the growth matrix", "our Ansoff" | UPDATE | 85% |
| Just a product/business name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Analyze current strategy placement, assess all four quadrants, produce risk-weighted growth recommendations.

**UPDATE**:
1. Read existing Ansoff analysis (search if path not provided)
2. Preserve core strategy placement assessment
3. Update quadrant options based on new market data or strategic shifts
4. Show diff summary: "Updated: [quadrants]. Risk assessment recalculated."

**FIND**:
1. Search paths below for Ansoff matrix documents
2. Present results: product, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `strategy/`
- `product/`
- `planning/`
- `analysis/`

---
## Gotchas

- Market penetration strategies must be distinct from new market development — same product, new segment is development
- Diversification is the highest-risk quadrant — flag it explicitly and require strong justification
- Each quadrant should have specific initiatives, not just strategic intent



## Vision to Value Phase

**Phase 1: Strategic Foundation** - The Ansoff Matrix helps determine growth direction before committing to specific strategies or bets.

**Prerequisites**: Understanding of current product portfolio and market position
**Outputs used by**: `/strategic-intent` (growth direction input), `/strategic-bet` (framing growth bets), `/market-analysis` (market development research)

## Methodology

<!-- Source: Ansoff Matrix — H. Igor Ansoff, "Strategies for Diversification", Harvard Business Review (1957). Also known as the Product/Market Expansion Grid. Ansoff is considered the father of strategic management. The matrix provides a systematic framework for identifying growth opportunities by examining the intersection of products (existing vs. new) and markets (existing vs. new). Originally published as a 2x2 matrix yielding four strategic options with increasing risk as you move away from the familiar (existing product, existing market). -->

<!-- Source: Risk escalation concept — Ansoff's key insight is that risk increases diagonally: Market Penetration (lowest risk) → Market Development or Product Development (medium risk) → Diversification (highest risk). This risk gradient helps organizations make conscious choices about growth risk appetite. Expanded in Ansoff's later work "Corporate Strategy" (1965, McGraw-Hill) and "Strategic Management" (1979). -->

<!-- Source: Related vs. Unrelated Diversification — Ansoff distinguished between related diversification (new product + new market but with synergies to existing business) and unrelated diversification (pure conglomerate strategy, highest risk). This distinction was further developed by Richard Rumelt in "Strategy, Structure, and Economic Performance" (1974). -->

<!-- Source: Inspiration — phuryn/pm-skills ansoff-matrix skill contributed to the skill structure and activation pattern design. -->

### The Four Growth Strategies

| | **Existing Products** | **New Products** |
|---|---|---|
| **Existing Markets** | **Market Penetration** | **Product Development** |
| **New Markets** | **Market Development** | **Diversification** |

#### Market Penetration (Lowest Risk)
Grow by increasing share in existing markets with existing products.
- Tactics: Increase usage frequency, win competitor customers, convert non-users
- Risk level: Low (familiar territory)
- Typical approaches: Pricing adjustments, marketing investment, loyalty programs, distribution expansion

#### Market Development (Medium Risk)
Grow by taking existing products to new markets.
- Tactics: New geographies, new customer segments, new use cases, new channels
- Risk level: Medium (known product, unknown market dynamics)
- Typical approaches: International expansion, new verticals, channel partnerships

#### Product Development (Medium Risk)
Grow by creating new products for existing markets.
- Tactics: New features, adjacent products, next-generation solutions
- Risk level: Medium (known market, unknown product-market fit)
- Typical approaches: R&D investment, acquisition of capabilities, platform extensions

#### Diversification (Highest Risk)
Grow by entering new markets with new products.
- **Related diversification**: Leverages existing capabilities, technology, or customer relationships
- **Unrelated diversification**: Pure conglomerate play, no synergies
- Risk level: High (unknown product AND unknown market)
- Typical approaches: Acquisitions, joint ventures, internal incubation

### Risk Assessment Framework

For each quadrant, assess:

| Dimension | Question |
|-----------|----------|
| **Feasibility** | Can we actually execute this? Do we have/can we get the capabilities? |
| **Attractiveness** | Is the opportunity large enough to justify the investment? |
| **Risk tolerance** | Does this fit our organization's risk appetite? |
| **Time to value** | How long before this generates meaningful returns? |
| **Resource requirements** | What investment (people, capital, time) is needed? |

## Output Structure

```markdown
# Ansoff Growth Matrix: [Product/Business Unit]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this analysis]
**Current primary strategy**: [Which quadrant dominates today]

## Current State Assessment

### Current Products
- [Product/capability 1]
- [Product/capability 2]

### Current Markets
- [Market/segment 1]
- [Market/segment 2]

### Current Strategy Placement
[Which quadrant(s) the organization currently operates in and why]

## Growth Matrix Analysis

### Market Penetration (Existing Products x Existing Markets)

**Current share**: [TBD — user to provide or estimate]
**Growth potential**: High / Medium / Low

| Opportunity | Approach | Estimated Impact | Effort |
|-------------|----------|-----------------|--------|
| [Opportunity 1] | [How] | [Impact] | [Effort] |
| [Opportunity 2] | [How] | [Impact] | [Effort] |

**Risk level**: Low
**Key assumption**: [What must be true for this to work]

### Market Development (Existing Products x New Markets)

**Target new markets**: [Geographies, segments, verticals]

| New Market | Entry Strategy | Market Size | Barriers |
|------------|---------------|-------------|----------|
| [Market 1] | [Strategy] | [Size] | [Barriers] |
| [Market 2] | [Strategy] | [Size] | [Barriers] |

**Risk level**: Medium
**Key assumption**: [What must be true for this to work]

### Product Development (New Products x Existing Markets)

**Product extension opportunities**: [Features, adjacent products, next-gen]

| New Product/Feature | Customer Need | Development Complexity | Differentiation |
|--------------------|---------------|----------------------|-----------------|
| [Product 1] | [Need] | [Complexity] | [Differentiation] |
| [Product 2] | [Need] | [Complexity] | [Differentiation] |

**Risk level**: Medium
**Key assumption**: [What must be true for this to work]

### Diversification (New Products x New Markets)

**Diversification type**: Related / Unrelated

| Opportunity | Synergies with Core | Market Attractiveness | Risk Level |
|-------------|--------------------|-----------------------|------------|
| [Opportunity 1] | [Synergies] | [Attractiveness] | [Risk] |
| [Opportunity 2] | [Synergies] | [Attractiveness] | [Risk] |

**Risk level**: High
**Key assumption**: [What must be true for this to work]

## Comparative Assessment

| Quadrant | Risk | Potential Return | Time to Value | Resource Need | Recommendation |
|----------|------|-----------------|---------------|---------------|----------------|
| Market Penetration | Low | [Assessment] | [Timeline] | [Resources] | [Priority] |
| Market Development | Medium | [Assessment] | [Timeline] | [Resources] | [Priority] |
| Product Development | Medium | [Assessment] | [Timeline] | [Resources] | [Priority] |
| Diversification | High | [Assessment] | [Timeline] | [Resources] | [Priority] |

## Recommended Growth Path

### Primary Growth Strategy
[Which quadrant to prioritize and why]

### Secondary Growth Strategy
[Which quadrant to explore as a secondary path]

### Sequencing
1. [Phase 1]: [Strategy] — [Rationale]
2. [Phase 2]: [Strategy] — [Rationale]
3. [Phase 3]: [Strategy] — [Rationale]

### What We Are NOT Doing (And Why)
- [Quadrant/opportunity deliberately excluded]: [Reason]

## Assumptions to Validate

| # | Assumption | Quadrant | Validation Method | Impact if Wrong |
|---|-----------|----------|------------------|-----------------|
| 1 | [Assumption] | [Quadrant] | [Method] | High/Med/Low |
| 2 | [Assumption] | [Quadrant] | [Method] | High/Med/Low |

## Next Steps

- [ ] Validate key assumptions via `/assumption-map`
- [ ] Develop strategic intent for chosen path via `/strategic-intent`
- [ ] Frame growth bet via `/strategic-bet`
- [ ] Conduct market analysis for new market quadrants via `/market-analysis`
```

## Instructions

1. Start by understanding the current product portfolio and market position
2. Assess all four quadrants even if some seem unlikely — the exercise reveals blind spots
3. Be explicit about risk tolerance and resource constraints
4. Challenge the default (most organizations default to Market Penetration without considering alternatives)
5. Sequence recommendations — rarely should an organization pursue all four simultaneously
6. Document what is deliberately NOT being pursued and why
7. Save output as markdown file
8. Offer `/strategic-bet` to frame the chosen growth direction as a formal bet

## Integration

- Links to `/strategic-intent` (growth direction feeds strategic intent)
- Links to `/strategic-bet` (frame growth choice as a bet)
- Links to `/market-analysis` (deep dive on new market quadrants)
- Links to `/assumption-map` (validate growth assumptions)
- Links to `/business-case` (build case for chosen growth path)
- Links to `/context-save` (save growth direction decisions)
