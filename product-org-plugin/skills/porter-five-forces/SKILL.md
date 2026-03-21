---
name: porter-five-forces
description: |
  Analyze industry structure and competitive dynamics using Porter's Five Forces framework.
  Activate when: "Porter", "five forces", "industry analysis", "competitive forces", "industry attractiveness", "barriers to entry", "supplier power", "buyer power"
  Do NOT activate for: competitive landscape (/competitive-landscape), competitive analysis (/competitive-analysis)
argument-hint: [industry or market] or [update path/to/porter-five-forces.md]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: strategy
compatibility: Requires Product Org OS v3+ context layer and rules
context: fork
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided (`@path/to/porter-five-forces.md`) | UPDATE | 100% |
| "create", "new", "analyze industry" in input | CREATE | 100% |
| "find", "search", "list five forces" | FIND | 100% |
| "the five forces", "our industry analysis" | UPDATE | 85% |
| Just an industry/market name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Analyze all five forces for the specified industry. Rate each force, assess overall industry attractiveness, and provide strategic implications.

**UPDATE**:
1. Read existing Five Forces analysis (search if path not provided)
2. Preserve force structure and rating methodology
3. Update individual force assessments based on new competitive data
4. Show diff summary: "Updated: [forces changed]. Overall attractiveness: [changed/unchanged]."

**FIND**:
1. Search paths below for Five Forces analysis documents
2. Present results: industry, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `strategy/`
- `research/`
- `competitive/`
- `analysis/`

---
## Gotchas

- Each force must be rated with evidence, not gut feeling — cite market data or examples
- Don't ignore substitute threats — the biggest competitive threat often comes from outside the industry
- Buyer power and supplier power depend on concentration — analyze the actual numbers, not assumptions



## Vision to Value Phase

**Phase 1: Strategic Foundation** - Five Forces analysis reveals industry structure and profitability dynamics, informing where-to-play decisions and competitive strategy.

**Prerequisites**: Industry or market identified for analysis
**Outputs used by**: `/strategic-intent` (industry context), `/competitive-landscape` (competitive dynamics), `/strategic-bet` (industry attractiveness inputs), `/positioning-statement` (differentiation strategy)

## Methodology

<!-- Source: Porter's Five Forces — Michael E. Porter, "How Competitive Forces Shape Strategy", Harvard Business Review (1979). Porter, a professor at Harvard Business School, introduced the framework to analyze industry profitability as determined by five competitive forces rather than just direct rivalry. The framework challenged the prevailing view that competition was only about existing competitors. -->

<!-- Source: Expanded framework — Porter elaborated the Five Forces in "Competitive Strategy: Techniques for Analyzing Industries and Competitors" (1980), Free Press. This book established the framework as a cornerstone of strategic management education and practice. It introduced the concepts of generic strategies (cost leadership, differentiation, focus) as responses to industry forces. -->

<!-- Source: 2008 Update — Porter revisited the framework in "The Five Competitive Forces That Shape Strategy", Harvard Business Review (2008). Key updates: emphasized that industry structure (not just competitive behavior) determines profitability, clarified common misapplications, and addressed how the framework applies to internet-era industries. Key insight: the internet has not made Five Forces obsolete but has shifted which forces dominate in different industries. -->

<!-- Source: Key insight on profitability — Porter's central argument is that industry profitability is determined by the STRUCTURE of the industry (the configuration of the five forces), not by whether the product is high-tech or low-tech, regulated or unregulated, manufacturing or service. The weakest competitive force determines the ceiling on profitability. -->

<!-- Source: Inspiration — phuryn/pm-skills and deanpeters/Product-Manager-Skills Porter implementations contributed to skill structure and activation pattern design. -->

### The Five Forces

#### 1. Threat of New Entrants
New entrants bring new capacity and desire to gain market share, putting pressure on prices, costs, and investment rates. The threat depends on barriers to entry:

| Barrier | Description |
|---------|-------------|
| **Economies of scale** | Established players have cost advantages at volume |
| **Capital requirements** | Large upfront investment deters entry |
| **Switching costs** | Customer cost of changing suppliers |
| **Access to distribution** | Existing channels are locked up |
| **Government policy** | Licenses, regulations, patents |
| **Brand identity** | Strong brands create loyalty barriers |
| **Expected retaliation** | Incumbents' reputation for aggressive response |

#### 2. Bargaining Power of Suppliers
Powerful suppliers capture more value by charging higher prices, limiting quality, or shifting costs.

| Factor | High Power When |
|--------|----------------|
| **Concentration** | Few suppliers dominate |
| **Switching costs** | Expensive to change suppliers |
| **Differentiation** | Supplier products are unique |
| **Forward integration** | Supplier can enter your market |
| **Importance** | Their input is critical to your product |
| **Substitute inputs** | No viable alternatives exist |

#### 3. Bargaining Power of Buyers
Powerful buyers can force prices down, demand higher quality, and play competitors against each other.

| Factor | High Power When |
|--------|----------------|
| **Concentration** | Few buyers purchase most volume |
| **Volume** | Individual buyers purchase in large quantities |
| **Switching costs** | Low cost to switch to competitors |
| **Information** | Buyers are well-informed about alternatives |
| **Price sensitivity** | Product is a significant cost for buyer |
| **Backward integration** | Buyer can produce the product themselves |
| **Undifferentiated product** | Buyer views products as commodities |

#### 4. Threat of Substitutes
Substitutes perform the same or similar function via a different means.

| Factor | High Threat When |
|--------|-----------------|
| **Performance** | Substitute offers comparable or better value |
| **Switching costs** | Low cost to switch to substitute |
| **Price-performance** | Substitute offers better price-performance ratio |
| **Buyer propensity** | Buyers are willing to try alternatives |
| **Industry convergence** | Technology is blurring industry boundaries |

#### 5. Competitive Rivalry
The intensity of competition among existing players.

| Factor | High Rivalry When |
|--------|-------------------|
| **Number of competitors** | Many competitors of similar size |
| **Industry growth** | Slow growth forces market share battles |
| **Fixed costs** | High fixed costs pressure utilization |
| **Differentiation** | Low differentiation leads to price competition |
| **Exit barriers** | High barriers keep struggling players in |
| **Strategic stakes** | Competitors have high strategic commitment |
| **Capacity increments** | Capacity must be added in large chunks |

### Force Rating Scale

| Rating | Meaning | Industry Impact |
|--------|---------|-----------------|
| **1 - Very Weak** | Force barely affects industry | Highly favorable for incumbents |
| **2 - Weak** | Force has limited impact | Favorable for incumbents |
| **3 - Moderate** | Force is present but manageable | Neutral |
| **4 - Strong** | Force significantly affects profitability | Unfavorable for incumbents |
| **5 - Very Strong** | Force dominates industry dynamics | Highly unfavorable for incumbents |

## Output Structure

```markdown
# Porter's Five Forces Analysis: [Industry/Market]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this analysis]
**Industry scope**: [Specific industry definition and boundaries]

## Executive Summary

[Overview of industry attractiveness based on the five forces. Which forces dominate? What is the overall structural profitability outlook?]

**Overall Industry Attractiveness**: [Score] / 5.0 (1 = highly attractive, 5 = unattractive)

## Force 1: Threat of New Entrants — Rating: [1-5]

### Key Factors

| Factor | Assessment | Impact |
|--------|-----------|--------|
| Economies of scale | [Assessment] | High/Med/Low |
| Capital requirements | [Assessment] | High/Med/Low |
| Switching costs | [Assessment] | High/Med/Low |
| Access to distribution | [Assessment] | High/Med/Low |
| Government policy / regulation | [Assessment] | High/Med/Low |
| Brand identity | [Assessment] | High/Med/Low |
| Expected retaliation | [Assessment] | High/Med/Low |

### Analysis
[What makes entry easy or difficult? How is this changing?]

### Trend
[Is this force strengthening or weakening? Why?]

## Force 2: Bargaining Power of Suppliers — Rating: [1-5]

### Key Factors

| Factor | Assessment | Impact |
|--------|-----------|--------|
| Supplier concentration | [Assessment] | High/Med/Low |
| Switching costs | [Assessment] | High/Med/Low |
| Supplier differentiation | [Assessment] | High/Med/Low |
| Forward integration threat | [Assessment] | High/Med/Low |
| Importance of input | [Assessment] | High/Med/Low |
| Substitute inputs | [Assessment] | High/Med/Low |

### Analysis
[Who are the key suppliers? How much power do they have? What are the dynamics?]

### Trend
[Is supplier power increasing or decreasing? Why?]

## Force 3: Bargaining Power of Buyers — Rating: [1-5]

### Key Factors

| Factor | Assessment | Impact |
|--------|-----------|--------|
| Buyer concentration | [Assessment] | High/Med/Low |
| Purchase volume | [Assessment] | High/Med/Low |
| Switching costs | [Assessment] | High/Med/Low |
| Buyer information | [Assessment] | High/Med/Low |
| Price sensitivity | [Assessment] | High/Med/Low |
| Backward integration threat | [Assessment] | High/Med/Low |
| Product differentiation | [Assessment] | High/Med/Low |

### Analysis
[Who are the key buyers? How do they exert power? What are the dynamics?]

### Trend
[Is buyer power increasing or decreasing? Why?]

## Force 4: Threat of Substitutes — Rating: [1-5]

### Key Factors

| Factor | Assessment | Impact |
|--------|-----------|--------|
| Substitute performance | [Assessment] | High/Med/Low |
| Switching costs | [Assessment] | High/Med/Low |
| Price-performance ratio | [Assessment] | High/Med/Low |
| Buyer propensity to substitute | [Assessment] | High/Med/Low |
| Industry convergence | [Assessment] | High/Med/Low |

### Key Substitutes Identified
| Substitute | How It Competes | Threat Level |
|-----------|----------------|--------------|
| [Substitute 1] | [Mechanism] | High/Med/Low |
| [Substitute 2] | [Mechanism] | High/Med/Low |

### Analysis
[What alternatives exist? How are substitutes evolving?]

### Trend
[Is substitute threat increasing or decreasing? Why?]

## Force 5: Competitive Rivalry — Rating: [1-5]

### Key Factors

| Factor | Assessment | Impact |
|--------|-----------|--------|
| Number of competitors | [Assessment] | High/Med/Low |
| Industry growth rate | [Assessment] | High/Med/Low |
| Fixed costs / value added | [Assessment] | High/Med/Low |
| Product differentiation | [Assessment] | High/Med/Low |
| Exit barriers | [Assessment] | High/Med/Low |
| Strategic stakes | [Assessment] | High/Med/Low |

### Competitive Intensity Map
| Competitor | Market Position | Strategy | Aggressiveness |
|-----------|----------------|----------|----------------|
| [Competitor 1] | [Position] | [Strategy] | High/Med/Low |
| [Competitor 2] | [Position] | [Strategy] | High/Med/Low |

### Analysis
[How intense is competition? What drives rivalry? What are the competitive dynamics?]

### Trend
[Is rivalry intensifying or moderating? Why?]

## Five Forces Summary

| Force | Rating (1-5) | Trend | Key Driver |
|-------|-------------|-------|------------|
| Threat of New Entrants | [Rating] | Increasing/Stable/Decreasing | [Key driver] |
| Supplier Power | [Rating] | Increasing/Stable/Decreasing | [Key driver] |
| Buyer Power | [Rating] | Increasing/Stable/Decreasing | [Key driver] |
| Threat of Substitutes | [Rating] | Increasing/Stable/Decreasing | [Key driver] |
| Competitive Rivalry | [Rating] | Increasing/Stable/Decreasing | [Key driver] |
| **Overall Attractiveness** | **[Avg]** | **[Direction]** | |

## Strategic Implications

### Industry Structure Opportunities
- [Opportunity 1]: [Which forces create this]
- [Opportunity 2]: [Which forces create this]

### Industry Structure Threats
- [Threat 1]: [Which forces drive this]
- [Threat 2]: [Which forces drive this]

### Recommended Strategic Responses
1. [Response to force]: [Specific action]
2. [Response to force]: [Specific action]
3. [Response to force]: [Specific action]

### Positioning Recommendations
[Based on forces analysis: cost leadership, differentiation, or focus? Where can you build defensible positions?]

## Next Steps

- [ ] Deep-dive into competitive landscape via `/competitive-landscape`
- [ ] Develop positioning based on force gaps via `/positioning-statement`
- [ ] Frame strategic choices via `/strategic-intent`
- [ ] Monitor force changes: schedule review in [timeframe]
```

## Instructions

1. Define industry boundaries clearly before analyzing forces
2. Rate each force with evidence, not intuition
3. Identify the dominant force (the force that most limits industry profitability)
4. Look for force interactions (e.g., low entry barriers + high buyer power compound the effect)
5. Consider how forces are changing, not just current state
6. Use WebSearch for current industry data when available
7. Save output as markdown file
8. Offer `/competitive-landscape` for deeper competitor analysis or `/positioning-statement` for differentiation strategy

## Integration

- Links to `/competitive-landscape` (detailed competitor mapping)
- Links to `/competitive-analysis` (head-to-head competitor comparison)
- Links to `/positioning-statement` (differentiation based on force gaps)
- Links to `/strategic-intent` (industry context for strategy)
- Links to `/strategic-bet` (industry attractiveness as bet input)
- Links to `/context-save` (save for periodic industry structure review)
