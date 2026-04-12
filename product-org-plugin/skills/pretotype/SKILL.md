---
name: pretotype
description: 'Design a pretotype to validate whether you''re building the right product before investing in building it right. Cheaper and faster than an MVP. Activate when: "pretotype", "pretotyping",
  "validate before building", "fake door test", "test demand", "the right it", "mechanical turk test", "validate idea cheaply" Do NOT activate for: experiment design (/experiment-design), MVP definition'
argument-hint: '[idea, hypothesis, or product concept to pretotype] or [update path/to/pretotype.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: product-management
  skill_type: task-capability
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "add results", "refine" in input | UPDATE | 100% |
| File path provided | UPDATE | 100% |
| "create", "new", "pretotype", "validate" in input | CREATE | 100% |
| "find", "search", "list pretotypes" | FIND | 100% |
| "the pretotype", "our test" | UPDATE | 85% |
| Just an idea or hypothesis | CREATE | 80% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Design a complete pretotype plan using the methodology below.

**UPDATE**:
1. Check document registry first, then search user's structure
2. Preserve original hypothesis and design
3. Add results data, update status, record learnings
4. Show whether hypothesis was validated, invalidated, or inconclusive

**FIND**: Check registry, then search user's folders for pretotype documents.

### Search Locations

- `{Product}/Product/pretotypes/`
- `{Product}/Product/experiments/`
- `context/documents/index.md`

---
## Gotchas

- Pretotypes test demand, not usability — the question is 'would anyone want this?' not 'can they use it?'
- Results must be quantified (conversion rate, signup count) — qualitative pretotype results are anecdotes



## Vision to Value Phase

**Phase 1: Strategic Foundation** -- Validate before building even an MVP. Pretotyping sits BEFORE prototyping in the validation sequence.

## Methodology

### Pretotyping Philosophy

<!-- Source: Alberto Savoia, "The Right It: Why So Many Ideas Fail and How to Make Sure Yours Succeed" (2019). Savoia, former Google Engineering Director, coined "pretotyping" after observing that most product failures fail not because they were built wrong, but because they were the wrong thing to build. The Law of Market Failure: most new products will fail in the market, even if competently executed. -->

**Core principle**: "Make sure you are building The Right It before you build It right."

The validation sequence:
1. **Pretotype** -- Is this the right thing to build? (demand validation)
2. **Prototype** -- Can we build it well? (feasibility validation)
3. **MVP** -- Will the market adopt it? (market validation)

Most teams skip straight to MVP, wasting months building something nobody wants. Pretotyping answers the demand question in days, not months.

### The XYZ Hypothesis

<!-- Source: Alberto Savoia, "The Right It" (2019). The XYZ Hypothesis replaces vague "we believe" statements with concrete, falsifiable predictions. The format forces specificity that makes validation possible. -->

Every pretotype starts with an XYZ Hypothesis:

**Format**: "At least **X%** of **Y** will **Z**."

| Component | What It Means | Example |
|-----------|--------------|---------|
| **X%** | Minimum success threshold | "At least 5%" |
| **Y** | Target audience, specifically defined | "of enterprise IT managers who visit our landing page" |
| **Z** | The specific action that proves demand | "will request a demo" |

**Good XYZ examples**:
- "At least 10% of visitors to the pricing page will click 'Start Free Trial'"
- "At least 3 out of 10 sales reps will use the new dashboard daily for 2 weeks"
- "At least 20% of beta users will invite a colleague within 7 days"

**Bad (not XYZ)**:
- "Users will love this feature" (not measurable)
- "The market is big enough" (not actionable)
- "People want AI in their workflow" (too vague)

### Pretotype Types

<!-- Source: Alberto Savoia, "The Right It" (2019), Chapters 7-10. Eight pretotype types, each designed for different validation needs. The taxonomy enables teams to choose the fastest, cheapest validation method for their specific hypothesis. -->

<!-- Source: Additional pretotype patterns from phuryn/pm-skills pretotyping skills (GitHub). -->

| Type | Description | Speed | Cost | Best For |
|------|-------------|-------|------|----------|
| **Mechanical Turk** | Human simulates the product behind the scenes | Days | Low | "Would they use this if it existed?" |
| **Pinocchio** | Non-functional physical/visual representation | Hours | Minimal | "Is this form factor right?" |
| **Fake Door** | Feature/product announcement that measures interest before building | Days | Low | "Is there demand for this?" |
| **Minimum Viable Pretotype** | Smallest possible version testing the core value prop | Days-Weeks | Low-Med | "Does the core mechanic work?" |
| **Provincial** | Test in a limited geography or segment before expanding | Weeks | Medium | "Does this work for a subset?" |
| **One Night Stand** | Offer the experience once (pop-up, one-time event) | Days | Low-Med | "Would they pay/show up?" |
| **Infiltrator** | Place your product inside existing channels/stores | Days | Low | "Does it get chosen when available?" |
| **Re-label** | Existing product, new label/positioning to test a different market | Days | Minimal | "Would a different audience want this?" |

### Pretotype Selection Guide

<!-- Source: Selection criteria synthesized from Savoia's pretotype type descriptions and Lean Startup experimentation principles (Eric Ries, "The Lean Startup", 2011). The matrix maps hypothesis type to optimal pretotype. -->

| What You're Testing | Recommended Pretotype | Why |
|--------------------|-----------------------|-----|
| Demand / willingness to act | Fake Door | Measures real intent with minimal build |
| Willingness to pay | One Night Stand, Fake Door (with pricing) | Tests economic behavior |
| Product-market fit for a concept | Mechanical Turk | Simulates full experience |
| New market for existing product | Re-label, Provincial | Tests positioning without rebuilding |
| Physical/visual form factor | Pinocchio | Tests reaction to tangible representation |
| Channel viability | Infiltrator | Tests distribution without product changes |
| Core value proposition | Minimum Viable Pretotype | Tests the essential mechanic only |

### Data Collection

<!-- Source: Savoia's "Skin in the Game" principle: only count behaviors where people invest something (time, money, reputation). Stated preferences are unreliable. Revealed preferences (actual behavior) are what matter. Related to Kahneman's distinction between experienced utility and predicted utility. -->

**The Skin in the Game principle**: Only count behaviors where the participant invests something real.

| Investment Type | Reliability | Examples |
|-----------------|-------------|---------|
| **Money** | Highest | Pre-order, deposit, subscription signup with card |
| **Time** | High | Signed up AND completed an action, came to an event |
| **Reputation** | High | Shared publicly, referred a colleague, posted review |
| **Attention** | Medium | Clicked, watched, read (but didn't act further) |
| **Stated intent** | Low | "I would definitely use this" (discount heavily) |

## Output Structure

```markdown
# Pretotype Plan: [Concept Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Who runs this pretotype]
**Product**: [Product name]
**Related**: [A-NNN assumptions, SB-YYYY-NNN bets]

## The Idea

[2-3 sentences describing the product/feature concept being validated]

## XYZ Hypothesis

> At least **[X]%** of **[Y]** will **[Z]**.

**Justification for X%**: [Why this threshold? What's the minimum viable demand?]
**Definition of Y**: [Precisely who, how many, how reached]
**Definition of Z**: [Exactly what action, how measured]

## Pretotype Design

### Type Selected: [Pretotype Type]

**Why this type**: [Why it's the best fit for this hypothesis]
**What it looks like**: [Concrete description of the pretotype]

### Setup

| Element | Detail |
|---------|--------|
| **What to build/create** | [Minimal setup needed] |
| **Audience** | [Who will see it, how they'll be reached] |
| **Duration** | [How long the test runs] |
| **Sample size** | [Minimum N for meaningful results] |
| **Skin in the game** | [What participants must invest] |

### Success Criteria

| Metric | Pass (Validated) | Fail (Invalidated) | Inconclusive |
|--------|-----------------|-------------------|--------------|
| Primary: [metric] | >= [X]% | < [Y]% | [Y-X]% range |
| Secondary: [metric] | [criteria] | [criteria] | [range] |

### What We're NOT Testing

[Explicitly state what this pretotype does NOT validate. E.g., "This tests demand, not usability." This prevents over-interpreting results.]

## Data Collection Plan

| Data Point | How Collected | Skin in the Game? |
|------------|--------------|-------------------|
| [Metric 1] | [Method] | Yes: [what they invest] / No: stated only |
| [Metric 2] | [Method] | Yes / No |

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk 1] | [What goes wrong] | [How to prevent/handle] |
| [Risk 2] | [What goes wrong] | [How to prevent/handle] |

## Cost & Timeline

| Item | Estimate |
|------|----------|
| Setup effort | [Hours/days, not $] |
| Run duration | [Days/weeks] |
| Analysis time | [Hours/days] |
| Total elapsed | [End-to-end timeline] |

## Decision Tree

```
Results in:
├── Validated (>= X%) → [Next step: prototype, MVP, invest, etc.]
├── Invalidated (< Y%) → [Next step: pivot, abandon, retest, etc.]
└── Inconclusive (Y-X% range) → [Next step: adjust and rerun, gather more data, etc.]
```

## Results (Fill After Running)

**Status**: [Not started / Running / Complete]
**Run dates**: [Start] to [End]
**Sample size achieved**: [N] of [Target N]

### Raw Data

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Primary: [metric] | >= [X]% | [actual]% | Pass / Fail / Inconclusive |
| Secondary: [metric] | [target] | [actual] | Pass / Fail / Inconclusive |

### Outcome

**Verdict**: [Validated / Invalidated / Inconclusive]

### Key Observations
- [What surprised us]
- [What confirmed expectations]
- [What we'd do differently]

### Decision
[What we're doing based on these results]

### Assumptions Updated
- [A-NNN]: [Validated / Invalidated] based on [evidence]
```

## Instructions

1. **Start with the XYZ Hypothesis.** If the user can't articulate an XYZ hypothesis, help them form one before designing the pretotype. A pretotype without a clear hypothesis is just playing.
2. Always define what the pretotype is NOT testing. This prevents over-interpreting results.
3. Insist on "skin in the game" metrics. Stated intent ("I'd use that!") is not validation.
4. Keep setups minimal. If your pretotype takes more than a week to set up, it's too complex. Consider a simpler pretotype type.
5. The decision tree must be defined BEFORE running. Deciding success criteria after seeing results is confirmation bias.
6. Connect to existing assumptions from `/assumption-map`. A pretotype should validate a specific assumption.
7. Save pretotype plans to `{Product}/Product/pretotypes/` or `{Product}/Product/experiments/`.
8. After completion, run `/compound` to extract learnings and update assumption status via `/context-save`.
9. When updating with results, be honest about the verdict. Inconclusive is a valid outcome that requires action, not dismissal.

## Integration

- Feeds from: `/assumption-map` (which assumptions to test), `/strategic-bet` (which bets to de-risk)
- Feeds into: `/experiment-design` (more rigorous follow-up experiments), `/context-save` (learnings), `/compound` (learning extraction)
- Related to but distinct from: `/experiment-design` (pretotypes are pre-experiment; experiments are more rigorous and come later)
- Can trigger: Go/no-go decisions on prototyping or MVP investment

## Vision to Value Operating Principle

> "The graveyard of failed products is full of things that were built right but were the wrong thing to build. Pretotyping is the cheapest insurance against building something nobody wants."
