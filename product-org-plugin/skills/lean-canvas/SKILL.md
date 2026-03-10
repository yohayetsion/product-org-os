---
name: lean-canvas
description: |
  Create a one-page Lean Canvas to capture and validate a business model for a new product, feature, or venture.
  Activate when: "lean canvas", "one-page business model", "startup canvas", "validate idea", "9-box model", "business model canvas for startups"
  Do NOT activate for: full business cases with ROI (/business-case), full business plans with operations (/business-plan), pricing decisions (/pricing-strategy)
argument-hint: [product or venture name] or [update path/to/lean-canvas.md]
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
| File path provided (`@path/to/lean-canvas.md`) | UPDATE | 100% |
| "create", "new", "draft canvas" in input | CREATE | 100% |
| "find", "search", "list canvases" | FIND | 100% |
| "the canvas", "our canvas" | UPDATE | 85% |
| Just a product/idea name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Facilitate filling all 9 boxes. Start with Problem and Customer Segments (the two most critical). Generate complete canvas.

**UPDATE**:
1. Read existing canvas (search if path not provided)
2. Preserve unchanged boxes exactly
3. Update specific boxes based on new learnings
4. Show diff summary: "Updated: [boxes]. Unchanged: [boxes]."
5. Re-evaluate riskiest assumption if boxes changed

**FIND**:
1. Search paths below for lean canvas documents
2. Present results: title, product, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `product/`
- `strategy/`
- `canvas/`
- `planning/`

---

## Vision to Value Phase

**Phase 1: Strategic Foundation** - The Lean Canvas is a lightweight tool for early-stage business model validation, before investing in full business cases.

**Prerequisites**: A product idea or venture concept
**Outputs used by**: `/business-case` (Phase 2), `/strategic-bet`, `/assumption-map`

## Methodology

<!-- Source: Lean Canvas — Ash Maurya, "Running Lean: Iterate from Plan A to a Plan That Works" (2012), O'Reilly Media. Adaptation of Alexander Osterwalder's Business Model Canvas (2010) specifically for startups and early-stage ventures. Key innovation: replaced Key Partners, Key Activities, Key Resources, and Customer Relationships with Problem, Solution, Key Metrics, and Unfair Advantage — focusing on risk and uncertainty rather than established operations. The canvas is designed to be completed in under 20 minutes and iterated frequently. -->

<!-- Source: Business Model Canvas (original) — Alexander Osterwalder & Yves Pigneur, "Business Model Generation" (2010). 9 building blocks: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure. The Lean Canvas deliberately diverges from BMC for startup contexts. -->

<!-- Source: Lean Startup principles — Eric Ries, "The Lean Startup" (2011). Build-Measure-Learn loop. The Lean Canvas embodies the principle of making assumptions explicit and testing the riskiest ones first. -->

### The 9 Boxes

Fill the canvas in this recommended order (risk-first):

| Order | Box | Key Question | Guidance |
|-------|-----|-------------|----------|
| 1 | **Problem** | What are the top 1-3 problems? | List existing alternatives customers use today |
| 2 | **Customer Segments** | Who has this problem? | Identify early adopters specifically, not just the broad market |
| 3 | **Unique Value Proposition** | What is the single clear message? | One sentence that explains why you are different AND worth attention |
| 4 | **Solution** | What are the top 3 features? | Keep it minimal — only what addresses the top problems |
| 5 | **Channels** | How will you reach customers? | Free vs paid, inbound vs outbound, direct vs indirect |
| 6 | **Revenue Streams** | How will you make money? | Pricing model, revenue model, lifetime value concept |
| 7 | **Cost Structure** | What are the major costs? | Customer acquisition costs, hosting, team, fixed vs variable |
| 8 | **Key Metrics** | What numbers matter? | The 1-3 metrics that indicate product-market fit progress |
| 9 | **Unfair Advantage** | What can't be easily copied? | Network effects, community, expertise, data, brand — NOT features |

### Riskiest Assumption Identification

After completing the canvas, identify the single riskiest assumption:

1. Review each box for implicit assumptions
2. Score each assumption: **Impact if wrong** (High/Med/Low) x **Confidence** (High/Med/Low)
3. The assumption with highest impact and lowest confidence is the riskiest
4. This assumption should be tested FIRST before investing further

## Output Structure

```markdown
# Lean Canvas: [Product/Venture Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this canvas]
**Iteration**: [1, 2, 3...]
**Status**: [Draft / Validated / Pivoted]

## The Canvas

### Problem
Top 1-3 problems:
1. [Problem 1]
2. [Problem 2]
3. [Problem 3]

**Existing Alternatives**: [How customers solve this today]

### Customer Segments
**Target customers**: [Who has this problem]

**Early adopters**: [Specific subset who will adopt first and why]

### Unique Value Proposition
**Single clear message**: [One sentence — why different AND worth attention]

**High-level concept**: [X for Y analogy, e.g., "Uber for laundry"]

### Solution
Top features for each problem:
1. [Solution for Problem 1]
2. [Solution for Problem 2]
3. [Solution for Problem 3]

### Channels
- [Channel 1]: [Free/Paid] — [How it works]
- [Channel 2]: [Free/Paid] — [How it works]

### Revenue Streams
- **Model**: [Subscription / Transaction / Freemium / etc.]
- **Price point**: [TBD — or user-provided]
- **Revenue drivers**: [What drives revenue growth]

### Cost Structure
- **Fixed costs**: [Team, infrastructure, etc.]
- **Variable costs**: [Per-customer costs, CAC, etc.]
- **Break-even indicator**: [What needs to be true to break even]

### Key Metrics
1. [Metric 1] — [Why it matters]
2. [Metric 2] — [Why it matters]
3. [Metric 3] — [Why it matters]

### Unfair Advantage
[What cannot be easily copied or bought — be honest, "none yet" is acceptable]

---

## Riskiest Assumption

**Assumption**: [Statement]
**Box**: [Which canvas box it comes from]
**Impact if wrong**: [High/Med/Low]
**Confidence**: [High/Med/Low]
**Proposed test**: [How to validate quickly]
**Timeline**: [When you'll know]

## Canvas Summary (Visual)

| Problem | Solution | UVP | Unfair Advantage | Customer Segments |
|---------|----------|-----|------------------|-------------------|
| [P1] | [S1] | [Single message] | [Advantage] | [Target] |
| [P2] | [S2] | | | [Early adopters] |
| [P3] | [S3] | | | |
| **Existing Alternatives** | | | | |
| [How solved today] | | | | |

| Key Metrics | Channels | Cost Structure | Revenue Streams |
|-------------|----------|---------------|-----------------|
| [M1] | [C1] | [Fixed] | [Model] |
| [M2] | [C2] | [Variable] | [Price] |
| [M3] | | [Break-even] | [Drivers] |

## Next Steps

- [ ] Test riskiest assumption via `/experiment-design`
- [ ] If validated, develop full `/business-case`
- [ ] Map all assumptions via `/assumption-map`
- [ ] Revisit canvas after each learning cycle (target: weekly iterations)
```

## Instructions

1. Start by asking for the product/venture concept if not provided
2. Fill Problem and Customer Segments FIRST — these are the foundation
3. Be honest about Unfair Advantage — "none yet" is better than a fabricated moat
4. Challenge vague UVPs — push for a single, specific, compelling sentence
5. For Key Metrics, focus on leading indicators of product-market fit, not vanity metrics
6. Always identify the riskiest assumption and propose a test
7. Encourage iteration — the canvas is designed to change frequently
8. Save output as markdown file
9. Offer `/assumption-map` for deeper assumption analysis or `/business-case` when ready to invest

## Integration

- Links to `/assumption-map` (deeper analysis of canvas assumptions)
- Links to `/experiment-design` (test the riskiest assumption)
- Links to `/business-case` (graduate from canvas to full business case when validated)
- Links to `/strategic-bet` (frame the venture as a strategic bet)
- Links to `/market-segment` (refine Customer Segments box)
- Links to `/context-save` (save canvas iterations for learning tracking)
