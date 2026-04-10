---
name: stakeholder-map
description: "Map stakeholder power, interest, and influence for a product initiative or decision using the Mendelow Power/Interest Matrix and RACI framework. Use when user says 'stakeholder map', 'stakeholder analysis', 'power interest matrix', 'who to involve', 'stakeholder engagement', 'influence grid', or 'RACI'. Do NOT activate for ownership mapping for accountability (/ownership-map) or collaboration quality checks (/collaboration-check)."
argument-hint: "[initiative or decision name] or [update path/to/stakeholder-map.md]"
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: product-management
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided (`@path/to/stakeholder-map.md`) | UPDATE | 100% |
| "create", "new", "map" in input | CREATE | 100% |
| "find", "search", "list stakeholder maps" | FIND | 100% |
| "the stakeholder map for [initiative]" | UPDATE | 85% |
| Just initiative or decision name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new stakeholder map using template below.

**UPDATE**:
1. Read existing stakeholder map (search if path not provided)
2. Preserve unchanged sections exactly
3. Update stakeholder positions, influence levels, or engagement strategies
4. Show diff summary: "Updated: [sections]. Unchanged: [sections]."
5. Note: Stakeholder positions shift over time; reassess before major milestones

**FIND**:
1. Search paths below for stakeholder maps
2. Present results: title, initiative, stakeholder count, path
3. Ask: "Update one of these, or create new?"

### Search Locations for Stakeholder Maps

- `product/`
- `strategy/`
- `stakeholders/`
- `plans/`
- `launch/`

---
## Gotchas

- Power and influence assessments must be evidence-based, not assumptions about job titles
- Stakeholder positions can change — stakeholder maps need refresh dates



Map **Stakeholder Power, Interest, and Influence** for an initiative or decision, with engagement strategies per quadrant and RACI for key decisions.

## Vision to Value Phase

**Phase 3: Strategic Commitments** - Mapping stakeholder influence before committing resources ensures organizational alignment and reduces execution risk.

**Prerequisites**: Phase 2 complete (decision made on what to build/pursue)
**Outputs used by**: Phase 3 (commitment check, roadmap communication), Phase 4 (launch coordination, stakeholder briefs)

## Methodology

<!-- Source: Power/Interest Matrix - Aubrey Mendelow (1991), "Environmental Scanning: The Impact of the Stakeholder Concept". Published in proceedings of the International Conference on Information Systems (ICIS). 2x2 grid classifying stakeholders by Power (ability to influence outcomes) and Interest (degree of concern about the initiative). Four quadrants with distinct engagement strategies: Manage Closely (high power + high interest), Keep Satisfied (high power + low interest), Keep Informed (low power + high interest), Monitor (low power + low interest). -->

<!-- Source: RACI Matrix - Origin debated; widely attributed to project management practices from the 1950s-1960s. Formalized in PMI's PMBOK Guide. RACI = Responsible (does the work), Accountable (owns the decision, single person), Consulted (provides input before decision), Informed (notified after decision). Critical rule: exactly one "A" per decision. -->

<!-- Source: Stakeholder Influence/Support Assessment - Combines stakeholder analysis from PMI's PMBOK Guide (6th edition, 2017, Chapter 13: Project Stakeholder Management) with influence/support categorization. Categories: Champion (actively promotes), Supporter (generally positive), Neutral (no strong position), Critic (raises concerns), Blocker (actively resists). Movement strategies: convert Blockers to Critics, Critics to Neutral, Neutral to Supporters, Supporters to Champions. -->

<!-- Source: Inspired by phuryn/pm-skills stakeholder-map skill. Adapted and expanded with influence/support assessment, engagement strategy templates, and RACI integration. -->

### Power/Interest Matrix

```
                        HIGH INTEREST
                        |
    KEEP SATISFIED      |      MANAGE CLOSELY
    (High Power,        |      (High Power,
     Low Interest)      |       High Interest)
    Strategy: Keep      |      Strategy: Active
    happy, don't bore   |      engagement, close
    with detail         |      collaboration
                        |
   ---------------------+---------------------
                        |
    MONITOR             |      KEEP INFORMED
    (Low Power,         |      (Low Power,
     Low Interest)      |       High Interest)
    Strategy: Minimal   |      Strategy: Regular
    effort, watch for   |      updates, address
    changes             |      concerns
                        |
                        LOW INTEREST

    HIGH POWER -------------------- LOW POWER
```

### Influence/Support Spectrum

| Position | Description | Engagement Goal |
|----------|------------|----------------|
| **Champion** | Actively promotes and advocates | Leverage and empower |
| **Supporter** | Generally positive, willing to help | Maintain and activate when needed |
| **Neutral** | No strong position either way | Educate and demonstrate value |
| **Critic** | Raises concerns, questions approach | Address concerns, find common ground |
| **Blocker** | Actively resists or obstructs | Understand root cause, escalate if needed |

### Movement Strategy

| From | To | Tactics |
|------|-----|---------|
| Blocker | Critic | Private conversation, understand fears, address root concerns |
| Critic | Neutral | Provide evidence, show risk mitigation, offer involvement |
| Neutral | Supporter | Demonstrate value to their goals, make it easy to support |
| Supporter | Champion | Give them visibility, credit their contribution, co-create |

## Output Structure

```markdown
# Stakeholder Map: [Initiative/Decision Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Single accountable person for stakeholder management]
**Initiative**: [Brief description of what's being decided/built]
**Product**: [Product name - optional, for multi-product organizations]
**Phase**: [Current Vision to Value phase]

## Stakeholder Inventory

| # | Name/Role | Organization | Power | Interest | Quadrant | Current Position | Desired Position |
|---|-----------|-------------|-------|----------|----------|-----------------|-----------------|
| 1 | [Name, Title] | [Team/Dept] | High/Med/Low | High/Med/Low | [Quadrant] | [Champion/Supporter/Neutral/Critic/Blocker] | [Target position] |
| 2 | [Name, Title] | [Team/Dept] | High/Med/Low | High/Med/Low | [Quadrant] | [Position] | [Target] |
| 3 | [Name, Title] | [Team/Dept] | High/Med/Low | High/Med/Low | [Quadrant] | [Position] | [Target] |

## Power/Interest Matrix

### Manage Closely (High Power, High Interest)

| Stakeholder | Current Position | Key Concern | Engagement Strategy |
|-------------|-----------------|-------------|-------------------|
| [Name] | [Position] | [What they care about] | [Specific actions] |

**Engagement cadence**: [Weekly 1:1s, steering committee, etc.]

### Keep Satisfied (High Power, Low Interest)

| Stakeholder | Current Position | Key Concern | Engagement Strategy |
|-------------|-----------------|-------------|-------------------|
| [Name] | [Position] | [What would trigger their interest] | [Specific actions] |

**Engagement cadence**: [Monthly updates, escalation-only, etc.]

### Keep Informed (Low Power, High Interest)

| Stakeholder | Current Position | Key Concern | Engagement Strategy |
|-------------|-----------------|-------------|-------------------|
| [Name] | [Position] | [What they want to know] | [Specific actions] |

**Engagement cadence**: [Regular updates, town halls, etc.]

### Monitor (Low Power, Low Interest)

| Stakeholder | Current Position | Watch For |
|-------------|-----------------|-----------|
| [Name] | [Position] | [Conditions that would change their power or interest] |

**Engagement cadence**: [Quarterly check-in, passive monitoring]

## Influence Assessment

### Champions (Leverage These)
| Champion | Their Influence | How to Leverage |
|----------|----------------|----------------|
| [Name] | [Who they influence, what credibility they have] | [Ask them to present, co-author, sponsor] |

### Blockers (Address These)
| Blocker | Root Cause of Resistance | Mitigation Plan | Escalation Path |
|---------|------------------------|-----------------|-----------------|
| [Name] | [Why they resist] | [Specific actions to address] | [Who to escalate to if mitigation fails] |

## RACI Matrix

| Decision/Deliverable | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|---------------------|----------------|-----------------|---------------|--------------|
| [Key decision 1] | [Who does the work] | [Single owner] | [Who gives input] | [Who gets notified] |
| [Key decision 2] | [Who] | [Single owner] | [Who] | [Who] |
| [Key decision 3] | [Who] | [Single owner] | [Who] | [Who] |
| [Key deliverable 1] | [Who] | [Single owner] | [Who] | [Who] |
| [Key deliverable 2] | [Who] | [Single owner] | [Who] | [Who] |

**RACI Validation**:
- [ ] Every row has exactly one "A"
- [ ] No person is both R and A on the same row (unless team is very small)
- [ ] C and I are distinct (consulted before, informed after)
- [ ] No stakeholder is overloaded (too many Rs)

## Communication Plan

| Stakeholder Group | Channel | Frequency | Content | Owner |
|------------------|---------|-----------|---------|-------|
| Manage Closely | [1:1, steering] | [Weekly] | [Detailed progress, decisions needed] | [Who] |
| Keep Satisfied | [Email, brief] | [Monthly] | [Summary, risks, asks] | [Who] |
| Keep Informed | [Newsletter, town hall] | [Bi-weekly] | [Updates, milestones, impact] | [Who] |
| Monitor | [Shared doc] | [Quarterly] | [High-level status] | [Who] |

## Risks & Contingencies

| Risk | Trigger | Impact | Contingency |
|------|---------|--------|------------|
| [Key stakeholder leaves] | [Departure] | [Loss of sponsorship] | [Backup champion identified] |
| [Blocker escalates] | [Formal objection] | [Delay/derail] | [Escalation to exec sponsor] |
| [Interest shift] | [Org change, priority shift] | [Loss of support] | [Re-engagement plan] |

## Stakeholder Map Evolution

| Milestone | Reassessment Action | Date |
|-----------|---------------------|------|
| [Phase transition] | Full stakeholder reassessment | [Date] |
| [Major decision point] | Check blocker status | [Date] |
| [Launch] | Expand map to include customers/partners | [Date] |
```

## Instructions

1. Ask clarifying questions about the initiative and key stakeholders
2. **Check prior context**: Run `/context-recall [initiative]` to find related decisions, commitments, and organizational context
3. **Check feedback**: Run `/feedback-recall [initiative]` for stakeholder-related signals
4. Reference any org charts, project plans, or strategy documents provided via @file syntax
5. Be specific about engagement strategies; generic "keep informed" is not actionable enough
6. Ensure RACI has exactly one Accountable person per row
7. Identify blockers and create specific mitigation plans
8. Save in product/ or strategy/ folder
9. Offer to create presentation version using /present

## Context Integration

After generating the stakeholder map:

1. **Offer to save**: Ask "Should I save this to the context registry? (`/context-save`)"
2. If yes, extract and save:
   - Stakeholder map summary and key findings to context
   - Link to related decisions, commitments, and launch plans
3. Suggest running `/commitment-check` to verify stakeholder alignment before resource commitment
