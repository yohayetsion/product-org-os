---
name: roadmap-theme
description: Define a roadmap theme with initiatives
argument-hint: [theme name]
---

Define a **Roadmap Theme** with initiatives and success criteria.

## V2V Phase

**Phase 3: Strategic Commitments** - Themes organize roadmap commitments around strategic priorities.

**Prerequisites**: Strategic bets defined, roadmap structure established
**Outputs used by**: Roadmap items, resource allocation, quarterly planning

## Output Structure

```markdown
# Roadmap Theme: [Theme Name]

**Theme ID**: RT-[YYYY]-[NNN]
**Owner**: [Role/Name]
**Timeframe**: [Quarters covered]
**Investment**: [% of capacity]

## Theme Overview

**Description**: [What this theme is about - 1-2 sentences]

**Strategic Rationale**: [Why this theme matters to the business]

**Customer Value**: [What value customers get from this theme]

## Strategic Alignment

**Supports Strategic Bet**: [Link to strategic bet]
**Company Goal**: [Which company goal this serves]

## Success Metrics

| Metric | Baseline | Target | Timeframe |
|--------|----------|--------|-----------|
| [Metric 1] | [Current] | [Target] | [When] |
| [Metric 2] | [Current] | [Target] | [When] |
| [Metric 3] | [Current] | [Target] | [When] |

## Initiatives

### Initiative 1: [Name]
**Description**: [Brief description]
**Priority**: P0 / P1 / P2
**Effort**: S / M / L / XL
**Owner**: [Name]
**Target Quarter**: [Quarter]
**Dependencies**: [Dependencies]
**Success Criteria**: [How we know it's done well]

### Initiative 2: [Name]
[Same structure]

### Initiative 3: [Name]
[Same structure]

## Quarterly Breakdown

| Quarter | Initiatives | Capacity | Key Deliverables |
|---------|-------------|----------|------------------|
| [Q1] | [Initiatives] | X% | [Deliverables] |
| [Q2] | [Initiatives] | X% | [Deliverables] |

## Dependencies

| Dependency | Type | Owner | Status | Risk |
|------------|------|-------|--------|------|
| [Dependency] | Internal/External | [Owner] | [Status] | High/Med/Low |

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | High/Med/Low | High/Med/Low | [Plan] |

## Resource Requirements

- **Team**: [Who's needed]
- **Skills**: [What skills required]
- **External**: [External resources needed]
```

## Instructions

1. Ask about strategic alignment if not clear
2. Reference any roadmap or strategy documents via @file syntax
3. Include clear success metrics per theme
4. Break down into concrete initiatives
5. Save in roadmap/ folder
