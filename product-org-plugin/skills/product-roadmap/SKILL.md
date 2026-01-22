---
name: product-roadmap
description: Create a complete product roadmap document
argument-hint: [timeframe or product area]
---

Create a **complete Product Roadmap** for the specified timeframe or product area.

## V2V Phase

**Phase 3: Strategic Commitments** - The roadmap is a key commitment artifact that follows strategic decisions.

**Prerequisites**: Phase 2 complete (business case approved, strategic bets defined)
**Outputs used by**: Phase 3 (PRDs, GTM), Phase 4 (execution tracking)

## Output Structure

Generate a comprehensive roadmap document with the following sections:

### 1. Executive Summary
- Roadmap timeframe
- Key themes and priorities
- Major milestones
- Resource summary

### 2. Product Vision Alignment
- Company vision reference
- Product vision statement
- How this roadmap advances the vision
- Strategic bets being addressed

### 3. Strategic Themes
For each theme:
- **Theme name**
- Strategic rationale
- Customer value
- Business value
- Success metrics
- Investment level (% of capacity)

### 4. Roadmap View

#### Now (Current Quarter)
| Initiative | Theme | Priority | Owner | Status |
|------------|-------|----------|-------|--------|
| [Name] | [Theme] | P0/P1/P2 | [Owner] | [Status] |

#### Next (Next Quarter)
| Initiative | Theme | Priority | Owner | Confidence |
|------------|-------|----------|-------|------------|
| [Name] | [Theme] | P0/P1/P2 | [Owner] | High/Med/Low |

#### Later (Future Quarters)
| Initiative | Theme | Priority | Dependencies |
|------------|-------|----------|--------------|
| [Name] | [Theme] | P0/P1/P2 | [Dependencies] |

### 5. Initiative Details
For each initiative in "Now":
- Description
- Target users
- Success criteria
- Key milestones
- Dependencies
- Risks

### 6. Dependencies Map
```
[Visual representation of dependencies between initiatives]
```

### 7. Success Metrics by Theme
| Theme | Metric | Current | Target | Timeline |
|-------|--------|---------|--------|----------|
| [Theme] | [Metric] | [Current] | [Target] | [When] |

### 8. Resource Requirements
- Engineering capacity needed
- Design capacity needed
- Other resources
- Capacity vs demand analysis

### 9. Risk Assessment
| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| [Risk] | High/Med/Low | High/Med/Low | [Plan] |

### 10. Stakeholder Communication Plan
| Audience | Cadence | Format | Owner |
|----------|---------|--------|-------|
| [Audience] | [Frequency] | [Format] | [Owner] |

### 11. Change Log
| Date | Change | Rationale |
|------|--------|-----------|
| [Date] | [What changed] | [Why] |

## Instructions

1. Ask about timeframe if not specified (quarterly, annual, etc.)
2. Reference any strategy documents provided via @file syntax
3. Ensure themes connect to strategic goals
4. Include explicit prioritization rationale
5. Save as markdown file
6. Offer to create presentation version using /present
