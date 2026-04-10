---
name: growth-model
description: "Map growth loops, assess Racecar components, and identify the next growth lever for your product. Activate when: \"growth model\", \"growth loops\", \"growth strategy\", \"viral loop\", \"PLG\", \"product-led growth\", \"Racecar framework\", \"growth engine\" Do NOT activate for: go-to-market strategy (/gtm-strategy), market sizing or analysis (/market-analysis)"
argument-hint: "[product or initiative name] or [update path/to/growth-model.md]"
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
| "update", "revise", "modify" in input | UPDATE | 100% |
| File path provided (`@path/to/growth-model.md`) | UPDATE | 100% |
| "create", "new", "map" in input | CREATE | 100% |
| "find", "search", "list growth models" | FIND | 100% |
| "the growth model", "our growth loops" | UPDATE | 85% |
| Just product or initiative name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new growth model using template below.

**UPDATE**:
1. Read existing growth model (search if path not provided)
2. Preserve unchanged sections exactly
3. Update specific sections (loops, Racecar assessment, recommendations)
4. Show diff summary: "Updated: [sections]. Unchanged: [sections]."
5. Note: Loop maturity ratings may need recalibration

**FIND**:
1. Search paths below for growth models
2. Present results: title, product, loops identified, path
3. Ask: "Update one of these, or create new?"

### Search Locations for Growth Models

- `strategy/`
- `growth/`
- `product/`
- `plans/`

---
## Gotchas

- Never fabricate growth rates, conversion funnels, or viral coefficients — use frameworks with [TBD]
- Growth loops are theoretical until validated — don't present models as projections
- Acquisition channel costs must be current — CAC on any platform changes quarter to quarter



Map the **Growth Model** for a product, identifying active loops, Racecar components, and the next growth lever.

## Vision to Value Phase

**Phase 2: Strategic Decisions** - Growth strategy informs GTM approach, pricing model, and resource allocation decisions.

**Prerequisites**: Phase 1 complete (market analysis, customer segments understood)
**Outputs used by**: Phase 3 (GTM strategy, roadmap themes), Phase 2 (pricing strategy, business case)

## Methodology

<!-- Source: Growth Loops (vs Funnels) - Reforge (Brian Balfour, Casey Winters, Elena Verna, ~2018-present). Key insight: Loops are closed systems where output reinvests as input, creating compounding growth. Funnels leak; loops compound. Types: Viral Loop (user invites user), Content Loop (UGC/SEO drives traffic drives content), Paid Loop (revenue funds ads funds revenue), Sales Loop (pipeline closes expands pipeline), Product-Led Loop (usage creates value creates conversion). -->

<!-- Source: Racecar Growth Framework - Reforge (Brian Balfour, ~2019). Components: Engine (self-sustaining loops that compound over time), Turbo Boosts (one-off acceleration events like PR launches, conferences, viral moments - temporary), Lubricants (optimization efforts like conversion rate, retention improvements - efficiency multipliers), Fuel (consumed inputs - capital, content, users - must be replenished). Key insight: Most companies confuse Turbo Boosts for Engines. -->

<!-- Source: GEM Framework - Gibson Biddle (former VP Product Netflix, CPO Chegg, ~2019). Three strategy questions: How does this improve Growth? How does this improve Engagement? How does this improve Monetization? Used as a lens for evaluating product initiatives. -->

<!-- Source: Retention Formula - Industry standard formalized by Reforge and others. Retention = f(Activation quality, Engagement depth, Resurrection capability). Activation: getting users to the "aha moment". Engagement: building habits around core value. Resurrection: winning back churned users. -->

### Growth Loop Types

| Loop Type | Input | Process | Output | Compounds? |
|-----------|-------|---------|--------|------------|
| **Viral** | Existing user | Invites/shares | New user | Yes - each user brings more |
| **Content** | Content creation | SEO/distribution | Traffic + new content | Yes - content attracts creators |
| **Paid** | Ad spend | Acquisition + monetization | Revenue for more ads | Yes - if LTV > CAC |
| **Sales** | Leads | Close + expand | Revenue + referrals | Yes - if expansion revenue grows |
| **Product-Led** | Free user | Usage + value realization | Conversion + advocacy | Yes - usage drives conversion |

### Racecar Component Assessment

| Component | Definition | Duration | Compounds? |
|-----------|-----------|----------|------------|
| **Engine** | Self-sustaining growth loops | Permanent | Yes |
| **Turbo Boosts** | One-off acceleration (PR, events, launches) | Temporary | No |
| **Lubricants** | Optimization (conversion, retention, activation) | Ongoing | Multiplier |
| **Fuel** | Consumed inputs (capital, content, users) | Consumed | Must replenish |

### Loop Health Scoring

| Dimension | Strong | Moderate | Weak |
|-----------|--------|----------|------|
| **Cycle time** | Days | Weeks | Months |
| **Conversion rate** | >10% | 3-10% | <3% |
| **Compounding** | Accelerating | Linear | Decelerating |
| **Defensibility** | Hard to copy | Can be copied | Easy to copy |

## Output Structure

```markdown
# Growth Model: [Product Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Single accountable person]
**Product Stage**: Pre-PMF / Early Growth / Scaling / Mature
**Product**: [Product name - optional, for multi-product organizations]

## Current Growth Profile

**Primary Growth Motion**: [Viral / Content / Paid / Sales / Product-Led]
**Growth Stage**: Searching / Found / Scaling / Optimizing
**Key Constraint**: [What is currently limiting growth]

## Active Growth Loops

### Loop 1: [Loop Name]

**Type**: [Viral / Content / Paid / Sales / Product-Led]
**Status**: Active / Emerging / Stalled / Planned

**Loop Mechanics**:
```
[Input] --> [Step 1] --> [Step 2] --> [Output] --> feeds back to [Input]
```

**Loop Health**:
| Dimension | Rating | Evidence |
|-----------|--------|----------|
| Cycle time | [Days/Weeks/Months] | [Data point] |
| Conversion rate | [Strong/Moderate/Weak] | [Data point] |
| Compounding | [Accelerating/Linear/Decelerating] | [Data point] |
| Defensibility | [Hard/Can be/Easy to copy] | [Rationale] |

**Overall Loop Maturity**: Nascent / Growing / Mature / Declining

### Loop 2: [Loop Name]

[Same structure as Loop 1]

## Racecar Assessment

### Engine (Self-Sustaining Loops)
| Loop | Status | Contribution | Maturity |
|------|--------|-------------|----------|
| [Loop name] | [Active/Planned] | [Primary/Secondary] | [Nascent/Growing/Mature] |

### Turbo Boosts (One-Off Acceleration)
| Boost | Expected Impact | Duration | Planned Date |
|-------|----------------|----------|--------------|
| [Event/PR/Launch] | [Impact] | [Temporary] | [When] |

### Lubricants (Optimization)
| Area | Current | Target | Impact on Engine |
|------|---------|--------|-----------------|
| [Activation rate] | [Current %] | [Target %] | [How it helps loops] |
| [Retention rate] | [Current %] | [Target %] | [How it helps loops] |
| [Conversion rate] | [Current %] | [Target %] | [How it helps loops] |

### Fuel (Consumed Inputs)
| Fuel Type | Current Supply | Burn Rate | Sustainability |
|-----------|---------------|-----------|----------------|
| [Capital/Content/Users] | [Amount] | [Rate] | [Months runway] |

## GEM Evaluation

| Dimension | Current State | Growth Model Impact |
|-----------|--------------|-------------------|
| **Growth** | [Current growth rate/state] | [How this model drives growth] |
| **Engagement** | [Current engagement metrics] | [How loops deepen engagement] |
| **Monetization** | [Current revenue model] | [How loops support monetization] |

## Retention Foundation

| Component | Status | Key Metric | Gap |
|-----------|--------|-----------|-----|
| **Activation** | [Strong/Moderate/Weak] | [Metric] | [What's missing] |
| **Engagement** | [Strong/Moderate/Weak] | [Metric] | [What's missing] |
| **Resurrection** | [Strong/Moderate/Weak] | [Metric] | [What's missing] |

## Next Growth Lever

**Recommendation**: [What to focus on next and why]

**Rationale**:
- [Why this lever over alternatives]
- [Expected impact on primary loop]
- [How it strengthens the Engine vs being a Turbo Boost]

**Key Assumptions**:
| # | Assumption | Confidence | Validation Method |
|---|-----------|-----------|------------------|
| 1 | [Assumption] | [Low/Med/High] | [How to test] |
| 2 | [Assumption] | [Low/Med/High] | [How to test] |

## Growth Anti-Patterns to Avoid

- [ ] Confusing Turbo Boosts for Engines (one-off wins mistaken for sustainable growth)
- [ ] Optimizing Lubricants before the Engine works (polishing a broken loop)
- [ ] Running multiple unproven loops simultaneously (diluted focus)
- [ ] Ignoring retention while chasing acquisition (leaky bucket)
```

## Instructions

1. Ask clarifying questions about the product's current growth state and available data
2. **Check prior context**: Run `/context-recall [product]` to find related strategic bets, pricing decisions, and GTM strategies
3. **Check feedback**: Run `/feedback-recall [growth/retention/acquisition]` for customer signals
4. Reference any analytics, metrics, or strategy documents provided via @file syntax
5. Be explicit about which loops are proven vs hypothetical
6. Distinguish between Engines and Turbo Boosts clearly
7. Focus the "Next Growth Lever" on the highest-impact, most-validated opportunity
8. Save in strategy/ or growth/ folder
9. Offer to create presentation version using /present

## Context Integration

After generating the growth model:

1. **Offer to save**: Ask "Should I save this to the context registry? (`/context-save`)"
2. If yes, extract and save:
   - Growth model summary and key loops to context
   - Link to related strategic bets and GTM strategies
   - Assumptions to `context/assumptions/registry.md`
3. Link to dependent pricing, GTM, and roadmap decisions
