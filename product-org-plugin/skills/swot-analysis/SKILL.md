---
name: swot-analysis
description: |
  Conduct a SWOT analysis with TOWS strategy matrix to assess internal strengths/weaknesses and external opportunities/threats.
  Activate when: "SWOT", "strengths weaknesses", "opportunities threats", "TOWS", "internal external analysis", "strategic assessment"
  Do NOT activate for: competitive landscape (/competitive-landscape), market analysis (/market-analysis)
argument-hint: [product, business, or initiative] or [update path/to/swot-analysis.md]
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
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided (`@path/to/swot-analysis.md`) | UPDATE | 100% |
| "create", "new", "run SWOT" in input | CREATE | 100% |
| "find", "search", "list SWOT" | FIND | 100% |
| "the SWOT", "our SWOT analysis" | UPDATE | 85% |
| Just a product/business name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Populate all four SWOT quadrants, generate TOWS strategy matrix, and produce prioritized strategic actions.

**UPDATE**:
1. Read existing SWOT analysis (search if path not provided)
2. Preserve quadrant items that remain valid
3. Add new items, remove outdated ones, recalculate TOWS strategies
4. Show diff summary: "Added: [items]. Removed: [items]. TOWS strategies recalculated."

**FIND**:
1. Search paths below for SWOT analysis documents
2. Present results: subject, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `strategy/`
- `product/`
- `analysis/`
- `planning/`

---

## Vision to Value Phase

**Phase 1: Strategic Foundation** - SWOT provides a holistic internal/external assessment that informs strategic direction, positioning, and risk management.

**Prerequisites**: Basic understanding of the product/business, market context (ideally from `/pestle-analysis` or `/market-analysis`)
**Outputs used by**: `/strategic-intent` (strategic direction), `/strategic-bet` (strength-opportunity alignment), `/positioning-statement` (differentiation from strengths), `/assumption-map` (assumptions behind each quadrant)

## Methodology

<!-- Source: SWOT Analysis — Widely attributed to Albert Humphrey, who led a research project at Stanford Research Institute (SRI) in the 1960s-1970s funded by Fortune 500 companies. Humphrey's team developed the framework (originally called SOFT: Satisfactory, Opportunity, Fault, Threat) as a systematic way to analyze why corporate planning failed. The framework was later refined to SWOT. Note: The exact origin is debated, with some attributing it to Harvard Business School professors Kenneth Andrews and C. Roland Christensen in their work on business policy in the 1960s, published in "Business Policy: Text and Cases" (1965). -->

<!-- Source: TOWS Matrix — Heinz Weihrich, "The TOWS Matrix: A Tool for Situational Analysis", Long Range Planning, Volume 15, Issue 2 (1982). Weihrich proposed systematically cross-referencing SWOT quadrants to generate four categories of strategies: SO (Maxi-Maxi), WO (Mini-Maxi), ST (Maxi-Mini), WT (Mini-Mini). This transformed SWOT from a descriptive exercise into a strategy generation tool. The key innovation was making the analysis actionable by forcing explicit strategy derivation from the intersection of internal and external factors. -->

<!-- Source: SWOT Best Practices — Common criticisms of SWOT include subjectivity, lack of prioritization, and tendency to produce long undifferentiated lists. Best practices to address these: (1) prioritize items within each quadrant, (2) use evidence rather than opinion, (3) be specific rather than vague, (4) limit each quadrant to 5-7 items, (5) always complete the TOWS matrix to make it actionable. See Helms & Nixon, "Exploring SWOT Analysis", Journal of Strategy and Management (2010). -->

<!-- Source: Inspiration — phuryn/pm-skills and deanpeters/Product-Manager-Skills SWOT implementations contributed to skill structure and activation pattern design. -->

### The SWOT Framework

|  | **Helpful** (to achieving objectives) | **Harmful** (to achieving objectives) |
|---|---|---|
| **Internal** (within organization) | **Strengths** | **Weaknesses** |
| **External** (in the environment) | **Opportunities** | **Threats** |

#### Strengths (Internal, Helpful)
What the organization does well or has as an advantage:
- Core competencies, unique capabilities
- Strong brand, reputation, market position
- Proprietary technology, IP, patents
- Financial resources, funding position
- Team expertise, culture, talent

#### Weaknesses (Internal, Harmful)
Where the organization is disadvantaged or lacking:
- Capability gaps, skill shortages
- Resource constraints, limited funding
- Poor brand awareness, weak positioning
- Technical debt, legacy systems
- Organizational challenges, cultural issues

#### Opportunities (External, Helpful)
External conditions that could be exploited:
- Market trends, growing demand
- Competitor weaknesses or exits
- Technology changes enabling new approaches
- Regulatory changes creating openings
- Partnership or acquisition possibilities

#### Threats (External, Harmful)
External conditions that could cause trouble:
- Competitive pressure, new entrants
- Market decline, changing preferences
- Regulatory tightening, compliance costs
- Economic downturn, funding environment
- Technology disruption, substitutes

### TOWS Strategy Matrix

Cross-reference SWOT quadrants to generate actionable strategies:

| | **Opportunities** | **Threats** |
|---|---|---|
| **Strengths** | **SO Strategies (Maxi-Maxi)**: Use strengths to capture opportunities | **ST Strategies (Maxi-Mini)**: Use strengths to mitigate threats |
| **Weaknesses** | **WO Strategies (Mini-Maxi)**: Overcome weaknesses to capture opportunities | **WT Strategies (Mini-Mini)**: Minimize weaknesses to avoid threats |

## Output Structure

```markdown
# SWOT Analysis: [Product / Business / Initiative]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this analysis]
**Scope**: [What is being assessed]
**Context**: [Market/competitive situation]

## Executive Summary

[2-3 paragraph synthesis of the most critical findings and strategic direction they suggest]

## SWOT Grid

### Strengths (Internal)

| # | Strength | Evidence | Significance |
|---|----------|----------|--------------|
| S1 | [Strength] | [Evidence/data] | High/Med/Low |
| S2 | [Strength] | [Evidence/data] | High/Med/Low |
| S3 | [Strength] | [Evidence/data] | High/Med/Low |
| S4 | [Strength] | [Evidence/data] | High/Med/Low |
| S5 | [Strength] | [Evidence/data] | High/Med/Low |

### Weaknesses (Internal)

| # | Weakness | Evidence | Significance |
|---|----------|----------|--------------|
| W1 | [Weakness] | [Evidence/data] | High/Med/Low |
| W2 | [Weakness] | [Evidence/data] | High/Med/Low |
| W3 | [Weakness] | [Evidence/data] | High/Med/Low |
| W4 | [Weakness] | [Evidence/data] | High/Med/Low |
| W5 | [Weakness] | [Evidence/data] | High/Med/Low |

### Opportunities (External)

| # | Opportunity | Source/Evidence | Timeframe | Significance |
|---|------------|----------------|-----------|--------------|
| O1 | [Opportunity] | [Source] | [When] | High/Med/Low |
| O2 | [Opportunity] | [Source] | [When] | High/Med/Low |
| O3 | [Opportunity] | [Source] | [When] | High/Med/Low |
| O4 | [Opportunity] | [Source] | [When] | High/Med/Low |
| O5 | [Opportunity] | [Source] | [When] | High/Med/Low |

### Threats (External)

| # | Threat | Source/Evidence | Timeframe | Significance |
|---|--------|----------------|-----------|--------------|
| T1 | [Threat] | [Source] | [When] | High/Med/Low |
| T2 | [Threat] | [Source] | [When] | High/Med/Low |
| T3 | [Threat] | [Source] | [When] | High/Med/Low |
| T4 | [Threat] | [Source] | [When] | High/Med/Low |
| T5 | [Threat] | [Source] | [When] | High/Med/Low |

## TOWS Strategy Matrix

### SO Strategies (Strengths x Opportunities) — Offensive

*Use strengths to capture opportunities:*

| Strategy | Strengths Used | Opportunities Captured | Priority |
|----------|---------------|----------------------|----------|
| [SO-1: Strategy] | S1, S3 | O1, O2 | High/Med/Low |
| [SO-2: Strategy] | S2, S4 | O3 | High/Med/Low |

### WO Strategies (Weaknesses x Opportunities) — Developmental

*Overcome weaknesses to capture opportunities:*

| Strategy | Weaknesses Addressed | Opportunities Enabled | Priority |
|----------|---------------------|----------------------|----------|
| [WO-1: Strategy] | W1, W2 | O1 | High/Med/Low |
| [WO-2: Strategy] | W3 | O4, O5 | High/Med/Low |

### ST Strategies (Strengths x Threats) — Defensive

*Use strengths to mitigate threats:*

| Strategy | Strengths Used | Threats Mitigated | Priority |
|----------|---------------|-------------------|----------|
| [ST-1: Strategy] | S1, S5 | T1, T2 | High/Med/Low |
| [ST-2: Strategy] | S3 | T3 | High/Med/Low |

### WT Strategies (Weaknesses x Threats) — Survival

*Minimize weaknesses to avoid threats:*

| Strategy | Weaknesses Addressed | Threats Avoided | Priority |
|----------|---------------------|-----------------|----------|
| [WT-1: Strategy] | W1, W4 | T1 | High/Med/Low |
| [WT-2: Strategy] | W2, W5 | T4 | High/Med/Low |

## Strategic Priority Matrix

| Rank | Strategy | Type | Impact | Feasibility | Urgency | Recommendation |
|------|----------|------|--------|-------------|---------|----------------|
| 1 | [Strategy] | SO/WO/ST/WT | High/Med/Low | High/Med/Low | High/Med/Low | [Action] |
| 2 | [Strategy] | SO/WO/ST/WT | High/Med/Low | High/Med/Low | High/Med/Low | [Action] |
| 3 | [Strategy] | SO/WO/ST/WT | High/Med/Low | High/Med/Low | High/Med/Low | [Action] |
| 4 | [Strategy] | SO/WO/ST/WT | High/Med/Low | High/Med/Low | High/Med/Low | [Action] |
| 5 | [Strategy] | SO/WO/ST/WT | High/Med/Low | High/Med/Low | High/Med/Low | [Action] |

## Key Insights

### Dominant Theme
[What is the overall strategic posture the SWOT suggests? Offensive, defensive, developmental, or survival?]

### Critical Gaps
[Which weaknesses are most dangerous given the threat landscape?]

### Biggest Leverage Points
[Which strength-opportunity combinations offer the highest strategic value?]

## Assumptions

| # | Assumption | Quadrant | Confidence | Validation Method |
|---|-----------|----------|------------|------------------|
| 1 | [Assumption] | [S/W/O/T] | High/Med/Low | [Method] |
| 2 | [Assumption] | [S/W/O/T] | High/Med/Low | [Method] |

## Next Steps

- [ ] Validate assumptions via `/assumption-map`
- [ ] Develop strategic intent from TOWS priorities via `/strategic-intent`
- [ ] Frame key SO strategies as strategic bets via `/strategic-bet`
- [ ] Feed external factors into `/pestle-analysis` for deeper macro analysis
- [ ] Review and update quarterly
```

## Instructions

1. Gather input from the user on the product/business/initiative being assessed
2. Be specific and evidence-based in each quadrant; avoid vague generalizations
3. Limit each quadrant to 5-7 items maximum (prioritized by significance)
4. Always complete the TOWS matrix; SWOT without TOWS is a descriptive exercise, not a strategic one
5. Rank TOWS strategies by impact, feasibility, and urgency
6. Challenge items that lack evidence: "Is this really a strength, or a hope?"
7. Use WebSearch for current market data to populate external quadrants when available
8. Save output as markdown file
9. Offer `/strategic-intent` to translate TOWS strategies into strategic direction or `/assumption-map` to validate key assumptions

## Integration

- Links to `/pestle-analysis` (external factors feed O and T quadrants)
- Links to `/porter-five-forces` (industry forces inform T quadrant)
- Links to `/strategic-intent` (TOWS strategies inform direction)
- Links to `/strategic-bet` (SO strategies become strategic bets)
- Links to `/assumption-map` (validate assumptions behind each quadrant)
- Links to `/positioning-statement` (strengths inform differentiation)
- Links to `/context-save` (save for periodic reassessment)
