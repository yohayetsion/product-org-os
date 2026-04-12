---
name: business-model-canvas
description: 'Map a complete business model using the 9-block Business Model Canvas framework. Visualizes how a business creates, delivers, and captures value. Activate when: "business model canvas", "BMC",
  "Osterwalder", "business model", "nine blocks", "canvas", "value proposition canvas" Do NOT activate for: lean canvas (/lean-canvas), business cases (/business-case), business plans (/business-plan)'
argument-hint: '[product or business name] or [update path/to/bmc.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: strategy
  skill_type: task-capability
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "add to canvas" in input | UPDATE | 100% |
| File path provided | UPDATE | 100% |
| "create", "new", "map", "canvas" in input | CREATE | 100% |
| "find", "search", "list canvases" | FIND | 100% |
| "the canvas", "our BMC" | UPDATE | 85% |
| Just a product/business name | CREATE | 80% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate a complete 9-block Business Model Canvas using the methodology below.

**UPDATE**:
1. Check document registry first, then search user's structure
2. Preserve existing blocks and assumptions
3. Update specific blocks with new information
4. Show what changed and how it affects connected blocks
5. Re-validate cross-block consistency

**FIND**: Check registry, then search user's folders for BMC documents.

### Search Locations

- `{Product}/Product/`
- `{Product}/Product/strategy/`
- `context/documents/index.md`

---
## Gotchas

- Revenue streams must be specific — 'subscriptions' is a model, not a stream. What subscriptions, at what price?
- Key partnerships must include what each party contributes and receives — one-sided partnerships fail
- Cost structure should distinguish fixed vs. variable costs — this affects scaling strategy



## Vision to Value Phase

**Phase 1: Strategic Foundation** -- Mapping the full business model to understand how value is created, delivered, and captured. Provides the strategic context for all subsequent phases.

## Methodology

### The Business Model Canvas

<!-- Source: Alexander Osterwalder & Yves Pigneur, "Business Model Generation" (2010). The Business Model Canvas is a strategic management template for developing new or documenting existing business models. Co-created with 470 practitioners from 45 countries. The canvas reduces a complex business model to 9 interconnected building blocks on a single page. -->

<!-- Source: Additional canvas thinking from Alexander Osterwalder, Yves Pigneur, Gregory Bernarda & Alan Smith, "Value Proposition Design" (2014). The Value Proposition Canvas zooms into the connection between Customer Segments and Value Propositions. -->

<!-- Source: Inspired by phuryn/pm-skills business-model skill structure. -->

The canvas has two sides:

| Side | Blocks | Focus |
|------|--------|-------|
| **Right side** (Value) | Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams | How value is CREATED and CAPTURED |
| **Left side** (Efficiency) | Key Resources, Key Activities, Key Partnerships, Cost Structure | How value is DELIVERED |

**The bridge**: Value Propositions connect the two sides. Everything on the left exists to deliver the promise made on the right.

### The 9 Building Blocks

#### Block 1: Customer Segments

<!-- Source: Osterwalder & Pigneur, "Business Model Generation" (2010), pp. 20-21. Customer segments define the different groups of people or organizations an enterprise aims to reach and serve. Segmentation types: mass market, niche, segmented, diversified, multi-sided platform. -->

Who are you creating value for? Who are your most important customers?

| Segmentation Type | Description | Example |
|-------------------|-------------|---------|
| **Mass market** | No distinction between segments | Consumer electronics |
| **Niche market** | Specialized, tailored segments | Luxury watchmaking |
| **Segmented** | Slightly different needs/problems | Banking (retail vs private) |
| **Diversified** | Unrelated segments with different needs | Amazon (retail + AWS) |
| **Multi-sided** | Two+ interdependent segments | Platform businesses |

For each segment, identify:
- Demographics / firmographics
- Jobs to be done
- Pains (frustrations, obstacles, risks)
- Gains (desired outcomes, benefits, aspirations)

#### Block 2: Value Propositions

<!-- Source: Osterwalder & Pigneur (2010), pp. 22-25. The Value Proposition describes the bundle of products and services that create value for a specific Customer Segment. Extended in "Value Proposition Design" (2014) with the Value Proposition Canvas: Pain Relievers, Gain Creators, and Products/Services mapped to customer Jobs, Pains, and Gains. -->

What value do you deliver? Which customer problems are you solving? What bundles of products and services do you offer?

Value creation mechanisms:

| Mechanism | How It Creates Value |
|-----------|---------------------|
| **Newness** | Satisfying an entirely new set of needs |
| **Performance** | Improving product/service performance |
| **Customization** | Tailoring to specific needs |
| **Getting the job done** | Helping customers get a job done |
| **Design** | Superior design/experience |
| **Brand/Status** | Value from brand association |
| **Price** | Similar value at lower price |
| **Cost reduction** | Helping reduce customer costs |
| **Risk reduction** | Reducing risks customers face |
| **Accessibility** | Making things available to new segments |
| **Convenience** | Making things easier/more convenient |

#### Block 3: Channels

<!-- Source: Osterwalder & Pigneur (2010), pp. 26-27. Channels describe how a company communicates with and reaches its Customer Segments to deliver a Value Proposition. Channel phases: awareness, evaluation, purchase, delivery, after-sales. -->

How do you reach your customer segments? Through which channels do they want to be reached?

| Phase | Question | Examples |
|-------|----------|---------|
| **Awareness** | How do customers learn about you? | Content, ads, PR, word of mouth |
| **Evaluation** | How do they evaluate your proposition? | Free trial, demos, reviews |
| **Purchase** | How do they buy? | Website, sales team, app store |
| **Delivery** | How do you deliver value? | Cloud, shipping, on-site |
| **After-sales** | How do you provide support? | Help desk, community, CSM |

**Own vs Partner channels**: Direct (sales force, website) vs Indirect (partner stores, wholesalers, affiliate).

#### Block 4: Customer Relationships

<!-- Source: Osterwalder & Pigneur (2010), pp. 28-29. Customer Relationships describe the types of relationships a company establishes with specific Customer Segments. Motivated by customer acquisition, retention, and upselling. -->

What type of relationship does each segment expect? How costly are they?

| Type | Description | When to Use |
|------|-------------|-------------|
| **Personal assistance** | Human interaction during/after sales | High-value, complex products |
| **Dedicated personal** | Dedicated representative per customer | Enterprise, key accounts |
| **Self-service** | No direct relationship, tools provided | Mass market, low-touch |
| **Automated services** | Automated + personalized self-service | SaaS, scaled personalization |
| **Communities** | User communities for knowledge sharing | Platform, developer tools |
| **Co-creation** | Customers participate in value creation | Open source, user-generated content |

#### Block 5: Revenue Streams

<!-- Source: Osterwalder & Pigneur (2010), pp. 30-33. Revenue Streams represent the cash a company generates from each Customer Segment. Two types: transaction (one-time) and recurring. Pricing mechanisms: fixed (list, feature-dependent, volume) and dynamic (negotiation, yield, auction, market). -->

For what value are customers willing to pay? How do they prefer to pay? How much does each stream contribute?

| Revenue Type | Mechanism | Examples |
|-------------|-----------|---------|
| **Asset sale** | Selling ownership | Physical products, perpetual licenses |
| **Usage fee** | Pay per use | Cloud compute, API calls |
| **Subscription** | Recurring access | SaaS, memberships |
| **Lending/Leasing** | Temporary access | Equipment, rental |
| **Licensing** | Permission to use IP | Patents, brand licensing |
| **Brokerage** | Intermediation fee | Marketplace take rate |
| **Advertising** | Attention monetization | Media, free-tier products |

#### Block 6: Key Resources

<!-- Source: Osterwalder & Pigneur (2010), pp. 34-35. Key Resources describe the most important assets required to make a business model work. Categories: physical, intellectual, human, financial. -->

What key resources does your value proposition require?

| Category | Examples |
|----------|---------|
| **Physical** | Manufacturing, buildings, vehicles, systems |
| **Intellectual** | Brands, patents, data, proprietary knowledge |
| **Human** | Domain experts, engineers, sales team |
| **Financial** | Cash, credit lines, stock option pools |

#### Block 7: Key Activities

<!-- Source: Osterwalder & Pigneur (2010), pp. 36-37. Key Activities describe the most important things a company must do to make its business model work. Categories: production, problem solving, platform/network. -->

What key activities does your value proposition require?

| Category | Focus | Examples |
|----------|-------|---------|
| **Production** | Designing, making, delivering | Manufacturing, software development |
| **Problem solving** | Finding solutions for individuals | Consulting, healthcare |
| **Platform/Network** | Managing and promoting platform | Platform development, community management |

#### Block 8: Key Partnerships

<!-- Source: Osterwalder & Pigneur (2010), pp. 38-39. Key Partnerships describe the network of suppliers and partners that make the business model work. Four types: strategic alliances, coopetition, joint ventures, buyer-supplier. Three motivations: optimization/economy of scale, reduction of risk/uncertainty, acquisition of resources/activities. -->

Who are your key partners? Which key resources come from partners? Which key activities do partners perform?

| Partnership Type | Description |
|-----------------|-------------|
| **Strategic alliances** | Non-competitors working together |
| **Coopetition** | Strategic partnerships between competitors |
| **Joint ventures** | New business developed jointly |
| **Buyer-supplier** | Reliable supply chain relationships |

#### Block 9: Cost Structure

<!-- Source: Osterwalder & Pigneur (2010), pp. 40-41. Cost Structure describes all costs incurred to operate a business model. Two broad classes: cost-driven (minimize costs) and value-driven (focus on value creation). Cost characteristics: fixed, variable, economies of scale, economies of scope. -->

What are the most important costs inherent in your business model? Which key resources and activities are most expensive?

| Characteristic | Description |
|---------------|-------------|
| **Fixed costs** | Stay the same regardless of volume |
| **Variable costs** | Scale with volume |
| **Economies of scale** | Cost advantages from growth |
| **Economies of scope** | Cost advantages from breadth |

**Cost-driven vs Value-driven**: Is the model optimized for lowest cost or premium value?

### Cross-Block Connections

<!-- Source: The interconnection analysis is what makes the BMC more than a checklist. Osterwalder emphasizes that business model innovation often comes from changing the connections between blocks, not just the content within them. This cross-block analysis approach is adapted from Strategyzer's facilitation methodology. -->

After filling all blocks, analyze connections:

| Connection | Question |
|-----------|----------|
| VP <-> CS | Does the value proposition address the segment's jobs/pains/gains? |
| VP <-> RS | Is the revenue model aligned with how customers perceive value? |
| CH <-> CS | Are channels matched to how segments want to be reached? |
| CR <-> CS | Is the relationship type appropriate for the segment? |
| KR <-> KA | Do we have the resources to perform the key activities? |
| KP <-> KR | Which resources come from partners vs internal? |
| CS <-> RS | Does the cost structure allow profitable revenue from each stream? |
| VP <-> KA | Are our activities focused on delivering the value proposition? |

### Assumption Extraction

For each block, identify the key assumption that must hold true:

| Block | Assumption Pattern |
|-------|-------------------|
| Customer Segments | "These customers exist in sufficient numbers and are reachable" |
| Value Propositions | "Customers value this enough to act (buy/switch/adopt)" |
| Channels | "We can reach customers through these channels cost-effectively" |
| Revenue Streams | "Customers will pay this amount in this way" |
| Key Resources | "We can acquire and maintain these resources" |
| Key Activities | "We can perform these activities at the required quality/speed" |
| Key Partnerships | "Partners will collaborate on these terms" |
| Cost Structure | "Our costs allow for viable unit economics" |

## Output Structure

```markdown
# Business Model Canvas: [Product/Business Name]

**Date**: [YYYY-MM-DD]
**Author**: [Name/Role]
**Product**: [Product name]
**Version**: [1.0 / iteration number]
**Related**: [SB-YYYY-NNN, DR-YYYY-NNN]

## Canvas Overview

[2-3 sentences: What this business does, who it serves, and how it makes money. The "elevator pitch" version of the canvas.]

---

## RIGHT SIDE: Value Creation & Capture

### 1. Customer Segments

**Primary segment**: [Segment name]
- Profile: [Who they are]
- Jobs to be done: [What they need accomplished]
- Pains: [Frustrations, obstacles]
- Gains: [Desired outcomes]

**Secondary segment**: [Segment name]
- Profile: [Who they are]
- Jobs / Pains / Gains: [Brief]

**Segment type**: [Mass / Niche / Segmented / Diversified / Multi-sided]

> **Key assumption**: [What must be true about these segments]

### 2. Value Propositions

**For [Primary Segment]**:
| Product/Service | Pain Reliever | Gain Creator |
|----------------|---------------|--------------|
| [Offering 1] | [What pain it addresses] | [What gain it enables] |
| [Offering 2] | [Pain addressed] | [Gain enabled] |

**Value creation mechanism**: [Newness / Performance / Customization / Price / etc.]
**Differentiator**: [What makes this proposition unique]

> **Key assumption**: [What must be true about the value proposition]

### 3. Channels

| Phase | Channel | Own/Partner |
|-------|---------|-------------|
| Awareness | [Channel] | [Own / Partner] |
| Evaluation | [Channel] | [Own / Partner] |
| Purchase | [Channel] | [Own / Partner] |
| Delivery | [Channel] | [Own / Partner] |
| After-sales | [Channel] | [Own / Partner] |

> **Key assumption**: [What must be true about channel effectiveness]

### 4. Customer Relationships

| Segment | Relationship Type | Purpose |
|---------|------------------|---------|
| [Primary] | [Type] | [Acquisition / Retention / Upsell] |
| [Secondary] | [Type] | [Purpose] |

> **Key assumption**: [What must be true about customer relationships]

### 5. Revenue Streams

| Stream | Type | Pricing | Contribution |
|--------|------|---------|-------------|
| [Stream 1] | [Transaction / Recurring] | [Mechanism] | [Primary / Secondary] |
| [Stream 2] | [Transaction / Recurring] | [Mechanism] | [Primary / Secondary] |

**Pricing philosophy**: [Cost-based / Value-based / Competition-based]

> **Key assumption**: [What must be true about revenue]

---

## LEFT SIDE: Value Delivery (Infrastructure)

### 6. Key Resources

| Resource | Category | Source |
|----------|----------|--------|
| [Resource 1] | [Physical / Intellectual / Human / Financial] | [Internal / Partner] |
| [Resource 2] | [Category] | [Source] |

**Most critical resource**: [Which one, if lost, would break the model]

> **Key assumption**: [What must be true about resources]

### 7. Key Activities

| Activity | Category | Importance |
|----------|----------|------------|
| [Activity 1] | [Production / Problem Solving / Platform] | [Why critical] |
| [Activity 2] | [Category] | [Why critical] |

**Core competency**: [What must we be BEST at]

> **Key assumption**: [What must be true about our ability to execute]

### 8. Key Partnerships

| Partner | Type | What They Provide | What We Provide |
|---------|------|-------------------|-----------------|
| [Partner 1] | [Alliance / Coopetition / JV / Buyer-Supplier] | [Their contribution] | [Our contribution] |
| [Partner 2] | [Type] | [Contribution] | [Contribution] |

**Partnership motivation**: [Optimization / Risk reduction / Resource acquisition]

> **Key assumption**: [What must be true about partnerships]

### 9. Cost Structure

| Cost Item | Type | Relative Size |
|-----------|------|--------------|
| [Cost 1] | [Fixed / Variable] | [Largest / Medium / Small] |
| [Cost 2] | [Fixed / Variable] | [Size] |

**Model type**: [Cost-driven / Value-driven]
**Economies of scale?**: [Yes/No -- where]

> **Key assumption**: [What must be true about cost viability]

---

## Cross-Block Analysis

### Connections That Strengthen the Model
| Connection | Why It Works |
|-----------|-------------|
| [Block A <-> Block B] | [How they reinforce each other] |

### Connections That Need Attention
| Connection | Risk |
|-----------|------|
| [Block A <-> Block B] | [Tension or misalignment identified] |

## Assumptions Summary

| # | Block | Assumption | Confidence | Impact if Wrong |
|---|-------|-----------|------------|-----------------|
| 1 | [Block] | [Assumption] | High/Med/Low | High/Med/Low |
| 2 | [Block] | [Assumption] | High/Med/Low | High/Med/Low |

**Critical assumptions to validate first**: [Top 2-3 that need `/assumption-map` or `/pretotype`]

## Canvas Evolution Notes

[What would change this canvas? What triggers a revision? Market shifts, customer feedback, competitive moves, or internal capability changes that would require re-mapping.]
```

## Instructions

1. **The canvas is a discussion tool, not a document.** The best BMCs emerge from conversation, not solo analysis. Ask clarifying questions for blocks where information is thin.
2. Start with the right side (customer-facing). Value Propositions and Customer Segments are the foundation. Don't fill the left side until the right side is clear.
3. Be specific. "Everyone" is not a customer segment. "Great product" is not a value proposition.
4. Every block must have a key assumption stated explicitly. These feed directly into `/assumption-map`.
5. The Cross-Block Analysis is where real insight lives. Tensions between blocks often reveal business model risks.
6. For multi-sided platforms, create a separate Value Proposition and Customer Segment entry per side.
7. Save canvases to `{Product}/Product/` or `{Product}/Product/strategy/`.
8. When updating, highlight which blocks changed and trace the impact on connected blocks.
9. Do NOT fabricate financial figures (revenue estimates, cost numbers). Use "[TBD]" placeholders per the no-estimates rule. The canvas maps the MODEL, not the numbers.
10. Consider offering `/pretotype` for critical assumptions identified in the canvas.

## Integration

- Feeds into: `/assumption-map` (assumptions per block), `/strategic-bet` (the canvas supports the bet), `/business-case` (canvas informs financial modeling), `/pricing-strategy` (Revenue Streams block)
- Feeds from: `/market-analysis` (Customer Segments), `/competitive-landscape` (differentiation), `/context-recall` (existing strategic context)
- Related to but distinct from: `/business-case` (financial analysis of a specific decision), `/business-plan` (comprehensive operational plan)
- Connects to: `/positioning-statement` (Value Proposition informs positioning), `/gtm-strategy` (Channels and Customer Relationships inform GTM)

## Vision to Value Operating Principle

> "A business model is not a business plan. It's a hypothesis about how your organization creates, delivers, and captures value. The canvas makes that hypothesis visible, discussable, and testable."
