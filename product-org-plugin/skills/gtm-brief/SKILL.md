---
name: gtm-brief
description: Create a go-to-market brief
argument-hint: [product/feature name]
---

Create a **Go-to-Market Brief** for a product or feature launch.

## V2V Phase

**Phase 3: Strategic Commitments** - GTM briefs summarize the go-to-market commitment for execution.

**Prerequisites**: GTM strategy approved, positioning finalized
**Outputs used by**: Phase 4 (campaigns, sales enablement, launch activities)

## Output Structure

```markdown
# GTM Brief: [Product/Feature Name]

**Brief ID**: GTM-[YYYY]-[NNN]
**Owner**: [Name]
**Launch Date**: [Date]
**Status**: Draft / In Review / Approved

## Launch Overview

**What**: [What's being launched - 1 sentence]
**Why**: [Why it matters - 1 sentence]
**When**: [Launch date and any phases]

## Target Market

**Primary Segment**: [Description]
**Secondary Segment**: [Description]
**Market Size**: [TAM/SAM/SOM if known]

## Target Buyer

**Title/Role**: [Who buys]
**Pain Points**:
- [Pain 1]
- [Pain 2]
- [Pain 3]

**Buying Triggers**:
- [Trigger 1]
- [Trigger 2]

## Positioning

**Category**: [What category we compete in]

**Positioning Statement**:
For [target customer] who [need], [product] is a [category] that [benefit]. Unlike [competitor], we [differentiator].

## Key Messages

**Primary Message**: [Main message - one sentence]

**Supporting Messages**:
1. [Message 1]
2. [Message 2]
3. [Message 3]

**Proof Points**:
- [Proof point 1]
- [Proof point 2]

## Competitive Positioning

| Competitor | Their Strength | Our Response |
|------------|----------------|--------------|
| [Competitor 1] | [Strength] | [Response] |
| [Competitor 2] | [Strength] | [Response] |

## Pricing

**Model**: [Pricing model]
**Price Points**: [Prices]
**Packaging**: [Tiers/options]

## Launch Activities

| Activity | Owner | Date | Status |
|----------|-------|------|--------|
| [Activity 1] | [Owner] | [Date] | [Status] |
| [Activity 2] | [Owner] | [Date] | [Status] |

## Success Metrics

| Metric | Target | Timeframe |
|--------|--------|-----------|
| [Metric 1] | [Target] | [When] |
| [Metric 2] | [Target] | [When] |

## Sales Enablement Needs

- [ ] Sales deck
- [ ] Demo script
- [ ] Battle cards
- [ ] FAQ
- [ ] Pricing guide
```

## Instructions

1. Ask about launch date if not specified
2. Reference any positioning or competitive documents via @file syntax
3. Keep brief focused and actionable
4. Include clear success metrics
5. Save in gtm/ folder
6. Offer to create presentation version using /present
