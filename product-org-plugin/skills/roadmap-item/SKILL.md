---
name: roadmap-item
description: Define a specific roadmap item
argument-hint: [item name]
---

Define a **Roadmap Item** (initiative, epic, or feature).

## V2V Phase

**Phase 3: Strategic Commitments** - Roadmap items are the specific commitments within themes.

**Prerequisites**: Roadmap theme defined, capacity understood
**Outputs used by**: PRDs, feature specs, sprint planning

## Output Structure

```markdown
# Roadmap Item: [Item Name]

**Item ID**: RI-[YYYY]-[NNN]
**Type**: Epic / Feature / Initiative
**Theme**: [Parent theme]
**Owner**: [Name]
**Status**: Proposed / Planned / In Progress / Completed

## Overview

**Description**: [What this item delivers]

**Customer Problem**: [What customer problem it solves]

**Value Proposition**: [Why customers care]

## Priority

**Priority**: P0 (Must have) / P1 (Should have) / P2 (Nice to have)

**Prioritization Rationale**:
- Strategic alignment: [High/Med/Low]
- Customer demand: [High/Med/Low]
- Revenue impact: [High/Med/Low]
- Effort: [S/M/L/XL]

## Target Timeline

**Target Quarter**: [Quarter]
**Target Release**: [Release/Version]
**Confidence**: High / Medium / Low

## Success Criteria

| Metric | Target | Timeframe |
|--------|--------|-----------|
| [Metric 1] | [Target] | [When] |
| [Metric 2] | [Target] | [When] |

## Scope

**In Scope**:
- [Item 1]
- [Item 2]
- [Item 3]

**Out of Scope**:
- [Item 1]
- [Item 2]

**Future Considerations**:
- [Item 1]

## Dependencies

| Dependency | Type | Owner | Status | Blocking? |
|------------|------|-------|--------|-----------|
| [Dependency] | Technical/Resource/External | [Owner] | [Status] | Yes/No |

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | High/Med/Low | High/Med/Low | [Plan] |

## Effort Estimate

**T-Shirt Size**: S / M / L / XL
**Engineering**: [Estimate]
**Design**: [Estimate]
**Other**: [Estimate]

## Related Items

- [Link to related roadmap items]
- [Link to PRD if exists]
```

## Instructions

1. Ask about the parent theme if not clear
2. Reference any related documents via @file syntax
3. Include clear success criteria
4. Be explicit about scope boundaries
5. Save in roadmap/ folder
