---
name: pricing-model
description: Design a pricing model
argument-hint: [product name]
---

Design a **Pricing Model** for the specified product.

## V2V Phase

**Phase 2: Strategic Decisions** - Pricing model selection is a key commercial decision.

**Prerequisites**: Value proposition defined, competitive context understood
**Outputs used by**: Pricing strategy, GTM strategy, sales enablement

## Output Structure

```markdown
# Pricing Model: [Product Name]

**Version**: [Version number]
**Owner**: [Name]
**Effective Date**: [Date]
**Status**: Draft / Proposed / Approved / Active

## Pricing Philosophy

**Value Basis**: [What customers are paying for]
**Pricing Approach**: Value-based / Cost-plus / Competitive / Penetration

## Pricing Model Type

**Selected Model**: [Per user / Per usage / Flat rate / Tiered / Freemium / etc.]

**Rationale**: [Why this model fits]

**Alternatives Considered**:
| Model | Pros | Cons | Why Not |
|-------|------|------|---------|
| [Alt 1] | [Pros] | [Cons] | [Reason] |
| [Alt 2] | [Pros] | [Cons] | [Reason] |

## Pricing Tiers

| Tier | Price | Billing | Target Segment | Key Limits |
|------|-------|---------|----------------|------------|
| Free | $0 | - | [Segment] | [Limits] |
| Starter | $X/mo | Monthly/Annual | [Segment] | [Limits] |
| Professional | $X/mo | Monthly/Annual | [Segment] | [Limits] |
| Enterprise | Custom | Annual | [Segment] | Unlimited |

## Feature Matrix

| Feature | Free | Starter | Pro | Enterprise |
|---------|------|---------|-----|------------|
| [Feature 1] | ✓ | ✓ | ✓ | ✓ |
| [Feature 2] | ✗ | ✓ | ✓ | ✓ |
| [Feature 3] | ✗ | ✗ | ✓ | ✓ |
| [Feature 4] | ✗ | ✗ | ✗ | ✓ |

## Usage Limits

| Metric | Free | Starter | Pro | Enterprise |
|--------|------|---------|-----|------------|
| [Users] | X | X | X | Unlimited |
| [Storage] | X GB | X GB | X GB | Unlimited |
| [API calls] | X/mo | X/mo | X/mo | Unlimited |

## Add-Ons

| Add-On | Price | Available On |
|--------|-------|--------------|
| [Add-on 1] | $X/mo | Pro+ |
| [Add-on 2] | $X/mo | All paid |

## Discount Policy

| Discount Type | Amount | Approval | Criteria |
|---------------|--------|----------|----------|
| Annual prepay | X% | Auto | Commit to annual |
| Multi-year | X% | Manager | 2+ year commit |
| Volume | Up to X% | Director | X+ seats |
| Strategic | Up to X% | VP | Strategic account |

## Competitive Comparison

| Competitor | Their Price | Our Price | Position |
|------------|-------------|-----------|----------|
| [Comp 1] | $X | $X | Premium/Parity/Value |

## Financial Model

| Scenario | ARPU | Customers | MRR |
|----------|------|-----------|-----|
| Conservative | $X | X | $X |
| Base | $X | X | $X |
| Optimistic | $X | X | $X |
```

## Instructions

1. Ask about target segments and value metrics if not clear
2. Reference any competitive or financial documents via @file syntax
3. Ensure tiers have clear upgrade paths
4. Include competitive context
5. Save in pricing/ folder
6. Offer to create presentation version using /present
