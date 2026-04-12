---
name: pestle-analysis
description: 'Conduct a PESTLE macro-environment analysis across Political, Economic, Social, Technological, Legal, and Environmental dimensions. Activate when: "PESTLE", "PEST", "macro environment", "political
  economic social", "external factors", "environment scan", "macro analysis" Do NOT activate for: market analysis (/market-analysis), competitive landscape (/competitive-landscape)'
argument-hint: '[market, industry, or geography] or [update path/to/pestle-analysis.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: strategy
  skill_type: task-capability
  owner: chief-architect
  primary_consumers:
  - general-counsel
  - chief-architect
  - head-corpdev
  - risk-manager
  secondary_consumers:
  - cpo
  - pm-dir
  - bizops
  - ci
  - contracts-counsel
  - privacy-counsel
  - ip-counsel
  - compliance-officer
  - employment-counsel
  - cloud-architect
  - security-architect
  - ma-analyst
  - corporate-venture
  - ceo
  - cmo
  - cfo
  - chro
  - cio
  - fpa-analyst
  - tax-planning
  - hr-dir
  - compensation-analyst
  - it-dir
  - market-researcher
  - analyst
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "refresh", "revise" in input | UPDATE | 100% |
| File path provided (`@path/to/pestle-analysis.md`) | UPDATE | 100% |
| "create", "new", "analyze environment" in input | CREATE | 100% |
| "find", "search", "list PESTLE" | FIND | 100% |
| "the PESTLE", "our macro analysis" | UPDATE | 85% |
| Just a market/industry name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Analyze all six PESTLE dimensions for the specified market or industry. Assess impact and trend direction for each factor.

**UPDATE**:
1. Read existing PESTLE analysis (search if path not provided)
2. Preserve structure and dimension organization
3. Update factors, impact ratings, or trend directions based on new developments
4. Show diff summary: "Updated: [dimensions changed]. New factors added: [count]."

**FIND**:
1. Search paths below for PESTLE analysis documents
2. Present results: market/industry, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `strategy/`
- `research/`
- `analysis/`
- `market/`

---
## Gotchas

- Each factor must be specific to the industry/region — generic macro trends add no value
- Political and Legal are different categories — don't conflate government policy with regulation
- Time horizon matters — state whether each factor is immediate, medium-term, or long-term



## Vision to Value Phase

**Phase 1: Strategic Foundation** - PESTLE analysis maps the macro-environment context that shapes strategic decisions, market entry, and risk assessment.

**Prerequisites**: Target market, industry, or geography identified
**Outputs used by**: `/strategic-intent` (environmental context), `/market-analysis` (market dynamics), `/strategic-bet` (risk factors), `/decision-record` (external constraints)

## Methodology

<!-- Source: PESTLE Analysis — Originally conceived as ETPS by Francis Aguilar in "Scanning the Business Environment" (1967), Harvard University Press. Aguilar proposed that businesses must systematically scan their external environment across Economic, Technical, Political, and Social dimensions to identify opportunities and threats. -->

<!-- Source: PEST Extension — The ETPS framework was reordered to PEST (Political, Economic, Social, Technological) and later extended to PESTLE by adding Legal and Environmental dimensions. The Legal dimension was separated from Political to reflect the growing importance of regulatory compliance distinct from government policy. The Environmental dimension was added in the 1990s-2000s as sustainability, climate change, and environmental regulation became strategic business factors. -->

<!-- Source: STEEPLE Variant — Some practitioners use STEEPLE (adding Ethics as a seventh dimension) or DESTEP (Demographics separated from Social). The PESTLE form has become the most widely adopted in strategic management education and practice. -->

<!-- Source: Inspiration — phuryn/pm-skills pestle-analysis skill contributed to the skill structure and activation pattern design. -->

### The Six Dimensions

| Dimension | Focus Areas | Key Questions |
|-----------|------------|---------------|
| **Political** | Government policy, political stability, trade policy, tax policy, government spending, regulation trends | How stable is the political environment? What regulations are changing? How does government policy affect our market? |
| **Economic** | GDP growth, interest rates, inflation, exchange rates, unemployment, consumer spending, business cycles | What is the economic trajectory? How do economic factors affect purchasing power? What are the cost pressures? |
| **Social** | Demographics, cultural trends, lifestyle changes, education, health consciousness, population growth, age distribution | How are customer preferences shifting? What demographic changes affect demand? What social movements matter? |
| **Technological** | R&D activity, automation, technology incentives, rate of tech change, innovation, digital transformation, AI adoption | What technologies are disrupting the market? How fast is adoption? What tech investments are competitors making? |
| **Legal** | Employment law, consumer protection, health & safety, data privacy, IP regulations, antitrust, international trade law | What laws constrain or enable us? What regulations are pending? What compliance requirements apply? |
| **Environmental** | Climate change, sustainability mandates, carbon regulations, waste management, ESG reporting, resource scarcity | What environmental regulations affect operations? How do sustainability expectations shape customer choices? What are the environmental risks? |

### Impact Assessment

For each factor identified, assess:

| Attribute | Scale | Description |
|-----------|-------|-------------|
| **Impact** | High / Medium / Low | How significantly does this factor affect the business or market? |
| **Probability** | High / Medium / Low | How likely is this factor to materialize or intensify? |
| **Trend** | Increasing / Stable / Decreasing | Is this factor becoming more or less significant over time? |
| **Timeframe** | Immediate / 1-2 years / 3-5 years | When will this factor have its greatest impact? |
| **Implication** | Opportunity / Threat / Both | Does this factor represent opportunity, threat, or both? |

## Output Structure

```markdown
# PESTLE Analysis: [Market / Industry / Geography]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this analysis]
**Scope**: [Market, industry, or geography being analyzed]
**Review cycle**: [Quarterly / Semi-annual / Annual]

## Executive Summary

[2-3 paragraph overview of the most critical macro-environment factors, their combined impact, and strategic implications]

## Political Factors

| Factor | Impact | Probability | Trend | Timeframe | Implication |
|--------|--------|-------------|-------|-----------|-------------|
| [Factor 1] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |
| [Factor 2] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |

**Analysis**: [What these political factors mean for strategy]
**Key risk**: [Most significant political risk]
**Key opportunity**: [Most significant political opportunity]

## Economic Factors

| Factor | Impact | Probability | Trend | Timeframe | Implication |
|--------|--------|-------------|-------|-----------|-------------|
| [Factor 1] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |
| [Factor 2] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |

**Analysis**: [What these economic factors mean for strategy]
**Key risk**: [Most significant economic risk]
**Key opportunity**: [Most significant economic opportunity]

## Social Factors

| Factor | Impact | Probability | Trend | Timeframe | Implication |
|--------|--------|-------------|-------|-----------|-------------|
| [Factor 1] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |
| [Factor 2] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |

**Analysis**: [What these social factors mean for strategy]
**Key risk**: [Most significant social risk]
**Key opportunity**: [Most significant social opportunity]

## Technological Factors

| Factor | Impact | Probability | Trend | Timeframe | Implication |
|--------|--------|-------------|-------|-----------|-------------|
| [Factor 1] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |
| [Factor 2] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |

**Analysis**: [What these technological factors mean for strategy]
**Key risk**: [Most significant technology risk]
**Key opportunity**: [Most significant technology opportunity]

## Legal Factors

| Factor | Impact | Probability | Trend | Timeframe | Implication |
|--------|--------|-------------|-------|-----------|-------------|
| [Factor 1] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |
| [Factor 2] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |

**Analysis**: [What these legal factors mean for strategy]
**Key risk**: [Most significant legal risk]
**Key opportunity**: [Most significant legal opportunity]

## Environmental Factors

| Factor | Impact | Probability | Trend | Timeframe | Implication |
|--------|--------|-------------|-------|-----------|-------------|
| [Factor 1] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |
| [Factor 2] | High/Med/Low | High/Med/Low | Increasing/Stable/Decreasing | [Timeframe] | Opportunity/Threat |

**Analysis**: [What these environmental factors mean for strategy]
**Key risk**: [Most significant environmental risk]
**Key opportunity**: [Most significant environmental opportunity]

## Cross-Dimension Analysis

### Heat Map Summary

| Dimension | Overall Impact | Trend Direction | Priority |
|-----------|---------------|-----------------|----------|
| Political | High/Med/Low | Increasing/Stable/Decreasing | [1-6] |
| Economic | High/Med/Low | Increasing/Stable/Decreasing | [1-6] |
| Social | High/Med/Low | Increasing/Stable/Decreasing | [1-6] |
| Technological | High/Med/Low | Increasing/Stable/Decreasing | [1-6] |
| Legal | High/Med/Low | Increasing/Stable/Decreasing | [1-6] |
| Environmental | High/Med/Low | Increasing/Stable/Decreasing | [1-6] |

### Key Interactions
[Where dimensions intersect, e.g., political regulation + technology adoption, social trends + economic pressures]

### Top 5 Factors to Monitor
1. [Factor] (Dimension) — [Why critical]
2. [Factor] (Dimension) — [Why critical]
3. [Factor] (Dimension) — [Why critical]
4. [Factor] (Dimension) — [Why critical]
5. [Factor] (Dimension) — [Why critical]

## Strategic Implications

### Opportunities
- [Opportunity 1]: [Which dimensions create this]
- [Opportunity 2]: [Which dimensions create this]

### Threats
- [Threat 1]: [Which dimensions drive this]
- [Threat 2]: [Which dimensions drive this]

### Recommended Actions
1. [Action] — Response to [factor/dimension]
2. [Action] — Response to [factor/dimension]
3. [Action] — Response to [factor/dimension]

## Next Steps

- [ ] Integrate findings into `/strategic-intent`
- [ ] Feed threats into `/assumption-map` for validation
- [ ] Update `/competitive-landscape` with regulatory/technology shifts
- [ ] Schedule review per cycle: [Quarterly / Semi-annual]
```

## Instructions

1. Ask about specific geography or market scope if not provided
2. Use WebSearch for current macro-environment data when available
3. Focus on factors that are actionable and relevant to the specific business context
4. Distinguish between factors that are certain vs. speculative
5. Identify cross-dimension interactions (e.g., regulation driving technology adoption)
6. Prioritize the top 5 factors that require active monitoring
7. Save output as markdown file
8. Offer `/strategic-intent` to incorporate findings into strategy or `/swot-analysis` for internal/external synthesis

## Integration

- Links to `/strategic-intent` (macro context shapes strategic direction)
- Links to `/market-analysis` (PESTLE feeds market understanding)
- Links to `/swot-analysis` (external factors feed Opportunities and Threats)
- Links to `/assumption-map` (validate assumptions about macro trends)
- Links to `/strategic-bet` (macro factors as risk inputs)
- Links to `/context-save` (save for periodic review and updating)
