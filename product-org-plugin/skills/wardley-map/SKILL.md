---
name: wardley-map
description: 'Create a Wardley Map to visualize value chains and component evolution for strategic decision-making. Activate when: "wardley map", "value chain map", "component evolution", "strategic landscape",
  "wardley", "evolution stages", "map the landscape" Do NOT activate for: competitive landscape (/competitive-landscape), market analysis (/market-analysis), business model (/business-model-canvas)'
argument-hint: '[user need or business domain] or [update path/to/wardley-map.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: strategy
  skill_type: task-capability
  owner: chief-architect
  primary_consumers:
  - chief-architect
  secondary_consumers:
  - cpo
  - vp-product
  - ci
  - head-corpdev
  - corporate-venture
  - ceo
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided (`@path/to/wardley-map.md`) | UPDATE | 100% |
| "create", "new", "map" in input | CREATE | 100% |
| "find", "search", "list maps" | FIND | 100% |
| "the wardley map for [domain]" | UPDATE | 85% |
| Just a business domain or user need | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Identify anchor user need, map value chain, position components by evolution, identify strategic gameplay opportunities.

**UPDATE**:
1. Read existing Wardley Map (search if path not provided)
2. Preserve anchor user need and value chain structure
3. Update component positions based on market evolution or new intelligence
4. Show diff summary: "Updated: [components moved]. New gameplay: [opportunities]."

**FIND**:
1. Search paths below for Wardley Map documents
2. Present results: domain, anchor need, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `strategy/`
- `product/`
- `planning/`
- `analysis/`
- `competitive/`

---

## Gotchas

- The anchor MUST be a real user need, not an internal capability. "The user needs to [verb]" — not "we need a platform"
- Evolution positions are based on market maturity, NOT your company's maturity. A component you custom-built may already be a commodity in the market
- Maps are situational — they represent ONE user need and its value chain. Do not try to map everything in one map
- Movement arrows show where components ARE EVOLVING, not where you want them to be. Evolution is driven by competition and supply/demand, not by your strategy

## Vision to Value Phase

**Phase 1: Strategic Foundation** - Wardley Maps reveal strategic landscape before committing to product bets, showing where to invest, what to build vs. buy, and where competitors are vulnerable.

**Prerequisites**: Understanding of target user and their needs
**Outputs used by**: `/strategic-intent` (where to play decisions), `/strategic-bet` (informed by landscape), `/competitive-landscape` (evolution-aware competitive view), `/business-case` (build vs. buy decisions)

## Methodology

<!-- Source: Wardley Mapping — Simon Wardley, "Wardley Maps: Topographical Intelligence in Business" (CC BY-SA 4.0, 2017+). Available free at learnwardleymapping.com and medium.com/wardleymaps. Wardley developed this mapping technique while serving as CEO of Fotango in the mid-2000s, applying Sun Tzu's principles of landscape and movement to business strategy. The technique has since been adopted by organizations including the UK Government Digital Service. -->

<!-- Source: wardley-maps-community (GitHub) — open-source tools and resources for Wardley Mapping. -->

<!-- Source: Evolution characteristics — Ben Mosior (Hiredthought), "Map Camp" workshops and resources. Mosior's work on evolution characteristics and practical mapping workshops has significantly advanced the accessibility of Wardley Mapping. -->

<!-- Source: Climatic patterns and doctrine — Simon Wardley, "Wardley Maps" Chapter 8-10. Climatic patterns are the rules of the game (components evolve, there is no choice in evolution, past success breeds inertia). Doctrine is the set of universally useful principles (use appropriate methods, focus on user needs, think small). -->

### The Map Structure

A Wardley Map positions components along two axes:

| Axis | Represents | Direction |
|------|-----------|-----------|
| **Y-axis (Visibility)** | Value chain — from user need (top) to infrastructure (bottom) | Top = visible to user, Bottom = invisible |
| **X-axis (Evolution)** | Component maturity — from novel to commodity | Left = Genesis, Right = Commodity |

### Evolution Stages

| Stage | Characteristics | Market | Examples |
|-------|----------------|--------|---------|
| **I. Genesis** | Novel, uncertain, poorly understood, changing rapidly, high failure rate | Undefined, no market yet | New AI capabilities, experimental tech |
| **II. Custom Built** | Emerging understanding, bespoke solutions, increasing learning, divergent approaches | Early adopters, growing | Custom ML pipelines, in-house platforms |
| **III. Product (+Rental)** | Well-understood, increasingly standardized, feature differentiation declining | Mainstream, competitive | SaaS products, cloud services, commercial APIs |
| **IV. Commodity (+Utility)** | Standardized, essential, volume operations, well-defined, low margin | Mature, utility | Electricity, compute, storage, email |

### Component Characteristics by Stage

| Characteristic | Genesis | Custom Built | Product | Commodity |
|---------------|---------|-------------|---------|-----------|
| **Ubiquity** | Rare | Emerging | Common | Widespread |
| **Certainty** | Poorly understood | Increasing clarity | Well understood | Fully defined |
| **Market** | Undefined | Niche | Competitive | Utility/volume |
| **Knowledge** | Exploration | Learning | Refinement | Operation |
| **User perception** | Exciting novelty | Enabling capability | Expected feature | Invisible utility |
| **Appropriate method** | Agile, experimentation | Lean, iteration | Six Sigma, best practice | Outsource, standardize |

### How to Create a Map

**Step 1: Anchor on User Need**
Start with a specific user need at the top of the map. "The user needs to..." — this anchors the entire value chain.

**Step 2: Map the Value Chain**
Work downward: what capabilities does the user need require? What does each capability depend on? Continue until you reach infrastructure components.

**Step 3: Position by Evolution**
For each component, assess where it sits on the evolution axis based on MARKET maturity (not your implementation maturity).

**Step 4: Identify Movement**
Add arrows showing which direction components are evolving. All components move left-to-right over time (toward commodity).

**Step 5: Apply Gameplay**
Identify strategic opportunities based on component positions and movements.

### Climatic Patterns (Rules of the Game)

| Pattern | Implication |
|---------|------------|
| **Everything evolves** | No component stays in Genesis forever; plan for evolution |
| **Components evolve through supply/demand competition** | You cannot stop evolution; you can only exploit it |
| **Past success breeds inertia** | Incumbents resist evolution of components they profit from |
| **Efficiency enables innovation** | Commoditized components become platforms for new Genesis work |
| **Higher-order systems create new sources of worth** | As components commoditize, value shifts up the stack |

### Doctrine (Universal Principles)

| Principle | Application |
|-----------|------------|
| **Focus on user needs** | Anchor every map on a real user need |
| **Use appropriate methods** | Agile for Genesis, Lean for Custom, Six Sigma for Product, outsource Commodity |
| **Think small** | Small autonomous teams, not large coordinated programs |
| **Be transparent** | Share maps widely; strategy improves with more eyes |
| **Challenge assumptions** | Maps expose assumptions; use them to have better debates |

### Gameplay (Strategic Moves)

| Move | Description | When to Use |
|------|-------------|-------------|
| **Open source** | Commoditize a component to undermine a competitor's profit center | When a competitor profits from a component that is ready to evolve |
| **Ecosystem play** | Build a platform on commoditized components, attract developers | When lower components are mature enough to standardize |
| **ILC (Innovate-Leverage-Commoditize)** | Innovate in Genesis, leverage in Custom/Product, commoditize to create platform | When you can drive the full evolution cycle |
| **Tower and moat** | Invest heavily in a component at the Product stage to own the market | When a component is crystallizing into product form |
| **Exploit inertia** | Move fast where incumbents resist change | When competitors have organizational inertia around evolving components |
| **Signal distortion** | Publish misleading intent to misdirect competitors | Competitive contexts with high-stakes positioning |

## Output Structure

```markdown
# Wardley Map: [Domain/Context]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this strategic analysis]
**Anchor User Need**: [The user needs to...]

---

## User Need

**User**: [Who is the user]
**Need**: [What they need to accomplish]
**Context**: [Business context, market situation]

---

## Value Chain

### Components (Top to Bottom)

| # | Component | Evolution Stage | Visibility | Dependencies |
|---|-----------|----------------|------------|-------------|
| 1 | [User-facing capability] | [Genesis/Custom/Product/Commodity] | High (visible to user) | — |
| 2 | [Supporting capability] | [Stage] | Medium | Depends on #1 |
| 3 | [Enabling service] | [Stage] | Medium | Depends on #2 |
| 4 | [Platform/infrastructure] | [Stage] | Low | Depends on #3 |
| 5 | [Foundational component] | [Stage] | Low (invisible) | Depends on #4 |

---

## Map (Text Representation)

```
Visibility (Value Chain)
^
|  [User Need]
|     |
|  [Component A] ---------> (evolving)
|     |
|  [Component B]
|     |    \
|  [Component C]  [Component D] --> (evolving)
|     |
|  [Component E]
|
+--Genesis----Custom----Product----Commodity--> Evolution
```

---

## Evolution Analysis

| Component | Current Stage | Movement | Speed | Confidence |
|-----------|--------------|----------|-------|------------|
| [Component 1] | [Stage] | [Evolving toward X] | Fast/Medium/Slow | High/Med/Low |
| [Component 2] | [Stage] | [Stable / Evolving] | [Speed] | [Confidence] |
| [Component 3] | [Stage] | [Evolving toward X] | [Speed] | [Confidence] |

---

## Inertia Points

| Component | Who Has Inertia | Why | Strategic Implication |
|-----------|----------------|-----|---------------------|
| [Component] | [Company/Industry] | [Reason for resistance] | [How to exploit] |

---

## Strategic Gameplay Opportunities

### Opportunity 1: [Name]
**Type**: [Open source / Ecosystem / ILC / Tower and moat / Exploit inertia]
**Target component**: [Which component]
**Move**: [What to do]
**Expected outcome**: [What this achieves strategically]
**Risk**: [What could go wrong]

### Opportunity 2: [Name]
[Same structure]

---

## Build vs. Buy vs. Partner Analysis

| Component | Current Approach | Recommended | Rationale |
|-----------|-----------------|-------------|-----------|
| [Component 1] | [Build/Buy/Partner] | [Recommendation] | [Based on evolution stage] |
| [Component 2] | [Build/Buy/Partner] | [Recommendation] | [Based on evolution stage] |

**Principle**: Build in Genesis/Custom (competitive advantage). Buy/rent in Product/Commodity (table stakes).

---

## Method Mapping

| Component | Evolution Stage | Appropriate Method |
|-----------|----------------|-------------------|
| [Genesis component] | Genesis | Agile, experimentation, prototyping |
| [Custom component] | Custom Built | Lean, iteration, learning loops |
| [Product component] | Product | Best practice, feature comparison |
| [Commodity component] | Commodity | Outsource, standardize, SLA-driven |

---

## Key Assumptions

| # | Assumption | Component | Impact if Wrong | Validation |
|---|-----------|-----------|-----------------|-----------|
| 1 | [Assumption about evolution position] | [Component] | High/Med/Low | [How to validate] |
| 2 | [Assumption about user need] | [Component] | High/Med/Low | [How to validate] |

---

## Recommendations

### Strategic Priorities
1. **[Priority 1]**: [Action and rationale based on map]
2. **[Priority 2]**: [Action and rationale]
3. **[Priority 3]**: [Action and rationale]

### What to Stop Doing
- [Activity that the map reveals as misallocated effort]

### What to Start Doing
- [Activity the map reveals as strategic opportunity]

## Next Steps

- [ ] Validate evolution positions with market research via `/market-analysis`
- [ ] Frame strategic bets based on gameplay via `/strategic-bet`
- [ ] Feed build/buy decisions into business case via `/business-case`
- [ ] Map competitive positions via `/competitive-landscape`
- [ ] Save map to context registry via `/context-save`
```

## Instructions

1. Start by identifying the anchor user need — "The user needs to..." Must be a real external user need
2. Map the value chain top-down: what capabilities serve the need? What do those depend on?
3. Position each component on the evolution axis based on MARKET maturity (not your own implementation)
4. Identify which components are actively evolving and in which direction
5. Look for inertia points — where are incumbents resisting evolution?
6. Identify gameplay opportunities based on component positions and movements
7. Derive build vs. buy recommendations from evolution positions
8. Map appropriate methods (agile/lean/six sigma/outsource) to each component's stage
9. Save output as markdown file
10. Offer `/strategic-bet` to frame gameplay as a formal strategic bet

## Integration

- Links to `/strategic-intent` (map informs where to play)
- Links to `/strategic-bet` (gameplay becomes bets)
- Links to `/competitive-landscape` (evolution-aware competitive view)
- Links to `/market-analysis` (validate evolution positions)
- Links to `/business-case` (build vs. buy decisions)
- Links to `/business-model-canvas` (value chain informs business model)
- Links to `/context-save` (save strategic landscape analysis)
