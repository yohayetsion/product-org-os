---
name: market-segment
description: Define a market segment
argument-hint: [segment name]
---

Define a **Market Segment** for targeting and GTM purposes.

## V2V Phase

**Phase 1: Strategic Foundation** - Segment definition determines who we serve and how we target them.

**Prerequisites**: Market analysis, initial opportunity hypothesis
**Outputs used by**: Phase 2 (business case), Phase 3 (GTM strategy), Phase 4 (campaigns)

## Output Structure

```markdown
# Market Segment: [Segment Name]

**Segment ID**: MS-[YYYY]-[NNN]
**Owner**: [Name]
**Date**: [Date]
**Status**: Proposed / Active / Deprioritized

## Segment Definition

**Name**: [Segment name]
**Description**: [Brief description]

## Firmographic Criteria

| Criterion | Specification |
|-----------|---------------|
| Industry | [Industries included] |
| Company Size | [Revenue range or employee count] |
| Geography | [Regions/countries] |
| Technology | [Tech stack requirements] |
| Growth Stage | [Startup/Growth/Mature] |

## Segment Size

| Metric | Value | Source |
|--------|-------|--------|
| TAM (Total companies) | X | [Source] |
| SAM (Reachable) | X | [Source] |
| SOM (Target) | X | [Source] |
| Revenue potential | $X | [Calculation] |

## Buyer Profile

**Primary Buyer**:
- Title: [Title]
- Reports to: [Role]
- Budget authority: [Yes/No, amount]
- Buying triggers: [What causes them to buy]

**Economic Buyer**:
- Title: [Title]
- What they care about: [Priorities]

**Technical Buyer**:
- Title: [Title]
- What they evaluate: [Criteria]

## Needs & Pain Points

| Need/Pain | Severity | Our Solution |
|-----------|----------|--------------|
| [Need 1] | Critical/High/Medium | [How we address] |
| [Need 2] | Critical/High/Medium | [How we address] |
| [Need 3] | Critical/High/Medium | [How we address] |

## Buying Behavior

**Typical Buying Process**:
1. [Stage 1]
2. [Stage 2]
3. [Stage 3]

**Sales Cycle**: [Typical length]
**Deal Size**: [Average/range]
**Decision Makers**: [How many involved]

## Competitive Landscape

| Competitor | Strength in Segment | Our Advantage |
|------------|---------------------|---------------|
| [Comp 1] | [Strength] | [Our advantage] |
| [Comp 2] | [Strength] | [Our advantage] |

## Segment Attractiveness

| Factor | Rating | Notes |
|--------|--------|-------|
| Size | High/Med/Low | [Notes] |
| Growth | High/Med/Low | [Notes] |
| Profitability | High/Med/Low | [Notes] |
| Accessibility | High/Med/Low | [Notes] |
| Competition | High/Med/Low | [Notes] |
| **Overall** | **High/Med/Low** | |

## Go-to-Market Approach

**Positioning for Segment**: [Tailored positioning]
**Key Messages**: [Segment-specific messages]
**Channels**: [How to reach them]
**Motion**: [Sales motion - self-serve, inside, field]

## Success Metrics

| Metric | Target | Timeframe |
|--------|--------|-----------|
| Segment penetration | X% | [When] |
| Win rate | X% | [When] |
| Average deal size | $X | [When] |
```

## Instructions

1. Ask about segment definition criteria if not clear
2. Use WebSearch for market sizing data
3. Reference any market research via @file syntax
4. Include specific targeting criteria
5. Save in segments/ or market/ folder
