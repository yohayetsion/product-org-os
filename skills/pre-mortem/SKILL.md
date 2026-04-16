---
name: pre-mortem
description: 'Facilitate a Pre-Mortem analysis using Gary Klein''s prospective hindsight technique. Imagine the project has FAILED, then work backwards to identify failure modes and create mitigation plans.
  Activate when: "pre-mortem", "premortem", "pre mortem", "imagine failure", "prospective hindsight", "what could go wrong", "risk anticipation", "failure mode", "failure analysis", "project risks" Do NOT
  activate for: four risks check (/four-risks-check), retrospective (/retrospective), risk management (general), assumption mapping (/assumption-map)'
argument-hint: '[project, plan, or initiative to pre-mortem] or [update path/to/pre-mortem.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: risk-management
  skill_type: task-capability
  owner: ai-architect
  primary_consumers:
  - pm
  - ai-architect
  - cloud-architect
  - security-architect
  - ma-analyst
  - ml-engineer
  - tech-lead
  - devops
  - qa-engineer
  - it-security-policy
  - risk-manager
  secondary_consumers:
  - cpo
  - vp-product
  - pm-dir
  - bizdev
  - prodops
  - general-counsel
  - legal-dir
  - contracts-counsel
  - privacy-counsel
  - ip-counsel
  - compliance-officer
  - employment-counsel
  - chief-architect
  - api-architect
  - data-architect
  - head-corpdev
  - corporate-venture
  - cs-dir
  - csm
  - onboarding-csm
  - support-lead
  - data-lead
  - experimentation-analyst
  - design-dir
  - user-researcher
  - frontend-dev
  - backend-dev
  - ceo
  - cfo
  - chro
  - coo
  - cio
  - finance-dir
  - fpa-analyst
  - financial-controller
  - treasury-analyst
  - tax-planning
  - hr-dir
  - recruiter
  - compensation-analyst
  - performance-specialist
  - it-dir
  - enterprise-systems
  - data-governance
  - pr-comms-specialist
  - operations-dir
  - program-manager
  - project-manager
  - process-engineer
  - procurement-specialist
  - sales-engineer
  - account-exec
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "re-run pre-mortem" in input | UPDATE | 100% |
| File path provided (`@path/to/pre-mortem.md`) | UPDATE | 100% |
| "create", "new", "run pre-mortem", "imagine failure" in input | CREATE | 100% |
| "find", "search", "list pre-mortems" | FIND | 100% |
| "the pre-mortem", "our pre-mortem" | UPDATE | 85% |
| Just a project or plan name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Brief the plan, facilitate failure imagination, categorize failure modes, assess severity/likelihood, and create mitigation plans.

**UPDATE**:
1. Read existing pre-mortem (search if path not provided)
2. Preserve existing failure modes and mitigations
3. Add new failure modes from changed context, reassess severity/likelihood
4. Show diff summary: "New failure modes: [N]. Reassessed: [N]. Mitigations added: [N]."

**FIND**:
1. Search paths below for pre-mortem documents
2. Present results: project, date, failure mode count, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `product/`
- `planning/`
- `risk/`
- `decisions/`

---
## Gotchas

- The power of pre-mortem comes from the framing "it HAS failed" (past tense), not "it MIGHT fail" (conditional) -- the past-tense framing activates different cognitive processes and increases identification of failure modes by ~30%
- Pre-mortem is not a risk register exercise -- it is a creative, psychological technique that gives team members permission to voice concerns they might otherwise suppress due to groupthink or optimism pressure
- Run the pre-mortem BEFORE commitment, not after -- once resources are committed, cognitive dissonance makes it harder to imagine failure honestly
- Mitigations must be concrete and assignable -- "be careful" is not a mitigation plan

## Vision to Value Phase

**Phase 4: Coordinated Execution** - Pre-mortem is ideally run at the Phase 3 to Phase 4 transition, after commitments are planned but before the point of no return. It can also be applied at any major milestone before significant resource expenditure.

**Prerequisites**: A defined plan, project, or initiative with enough detail to imagine failure concretely (not just an idea or concept)
**Outputs used by**: `/launch-readiness` (failure modes inform readiness checklist), `/commitment-check` (mitigations become conditions for commitment), `/product-roadmap` (risk-adjusted sequencing)

## Methodology

<!-- Source: Pre-Mortem -- Gary Klein, "Performing a Project Premortem" (Harvard Business Review, September 2007). Klein is a cognitive psychologist known for research on naturalistic decision making. -->

<!-- Source: Prospective hindsight research -- Deborah J. Mitchell, J. Edward Russo, and Nancy Pennington, "Back to the Future: Temporal Perspective in the Explanation of Events" (Journal of Behavioral Decision Making, 1989). Found that imagining an event has already occurred increases the ability to generate explanations by 30%. -->

<!-- Source: Inspired by phuryn/pm-skills pre-mortem skill. Adapted with full facilitation protocol, severity/likelihood matrix, and V2V phase integration. -->

### Why Pre-Mortem Works

Traditional risk assessment asks: "What might go wrong?" This engages cautious, hedging thinking.

Pre-mortem asks: "It's 6 months from now and this project has **failed spectacularly**. Why did it fail?" This engages explanatory thinking -- a fundamentally different cognitive mode.

**The science**: Mitchell, Russo, and Pennington (1989) demonstrated that imagining an event **has already occurred** increases the ability to generate explanations by approximately 30% compared to imagining it **might occur**. This is called **prospective hindsight**.

**The psychology**: Pre-mortem also overcomes two powerful group dynamics:
1. **Groupthink** -- team members suppress concerns to maintain harmony
2. **Optimism bias** -- teams systematically underestimate risks and overestimate positive outcomes

By making failure the starting assumption, the pre-mortem gives explicit permission to voice concerns. It reframes "negativity" as "contribution."

### The Pre-Mortem Protocol

#### Step 1: Brief the Plan (10 minutes)

Present the project plan, initiative, or strategy to the team. Everyone should understand:
- What we are building/doing
- Who the target customer/user is
- What success looks like
- The timeline and key milestones
- The resources committed

#### Step 2: Set the Scene (2 minutes)

The facilitator reads the following (adapt the timeframe to the project):

> "Imagine it is [6 months / 1 year] from now. This project has **failed**. Not a minor setback -- a **spectacular failure**. The kind that gets discussed in post-mortems and cautionary tales. It did not deliver what was promised. Stakeholders are disappointed. The team is demoralized. Resources were wasted."

> "Your job now is to explain **why it failed**. What went wrong? What did we miss? What assumptions turned out to be wrong? Write as many reasons as you can think of."

**Critical framing**: Use past tense. "It failed" not "it might fail." This is not a conditional -- it is a certainty in this scenario.

#### Step 3: Silent Writing (10 minutes)

Each participant writes failure reasons **individually and silently**. No discussion.

Rules:
- Write complete sentences: "It failed because..."
- Be specific: not "bad execution" but "the API integration with [vendor] took 3x longer than estimated because their documentation was wrong"
- No filtering: write everything, even if it feels unlikely or uncomfortable
- Aim for at least 5-7 failure reasons per person

#### Step 4: Round-Robin Sharing (15-20 minutes)

Go around the room. Each person shares **one** failure reason per round. Continue until all unique reasons are captured.

Rules:
- No debating or dismissing during sharing
- Duplicates are noted but every voice is heard
- Facilitator captures each reason on a visible board
- Continue until all unique reasons are exhausted

#### Step 5: Categorize Failure Modes (10 minutes)

Group the failure reasons into categories:

| Category | Examples |
|----------|---------|
| **Technical** | Architecture flaws, integration failures, scalability limits, security breaches |
| **Market** | Wrong customer segment, market timing off, price sensitivity misjudged |
| **Execution** | Scope creep, resource constraints, team turnover, dependency delays |
| **People** | Key person risk, skill gaps, misaligned incentives, communication breakdown |
| **External** | Regulatory changes, competitor moves, economic shifts, vendor failures |
| **Customer** | Adoption resistance, usability failures, value proposition misread, churn |

#### Step 6: Assess Severity and Likelihood (10 minutes)

For each failure mode, score:

| Dimension | Scale | Description |
|-----------|-------|-------------|
| **Severity** | Critical / High / Medium / Low | How bad is it if this happens? |
| **Likelihood** | Very Likely / Likely / Possible / Unlikely | How probable is this failure mode? |

**Priority matrix**:

```
              SEVERITY -->
              Low      Medium     High      Critical
         +----------+----------+----------+----------+
Very     |  Monitor | Mitigate | Prevent  | Prevent  |
Likely   |          |          |          |          |
         +----------+----------+----------+----------+
Likely   |  Accept  | Mitigate | Mitigate | Prevent  |
         |          |          |          |          |
         +----------+----------+----------+----------+
Possible |  Accept  | Monitor  | Mitigate | Mitigate |
         |          |          |          |          |
         +----------+----------+----------+----------+
Unlikely |  Accept  | Accept   | Monitor  | Mitigate |
         |          |          |          |          |
         +----------+----------+----------+----------+
LIKELIHOOD
```

#### Step 7: Create Mitigation Plans (15-20 minutes)

For each failure mode in the Prevent or Mitigate zones, define a concrete mitigation:

| Mitigation Type | Description | Example |
|-----------------|-------------|---------|
| **Prevent** | Eliminate the cause entirely | "Run a technical spike before committing to the vendor API" |
| **Detect** | Create early warning signals | "Set up weekly usage metrics dashboard; alert if adoption < threshold by week 4" |
| **Mitigate** | Reduce the impact if it occurs | "Build abstraction layer so we can swap vendors without full rewrite" |
| **Accept** | Acknowledge and monitor | "Economic downturn risk -- accepted; revisit if funding round delayed" |

Each mitigation must have:
- **Owner**: A specific person responsible
- **Trigger**: When to act (date, metric threshold, or event)
- **Action**: What specifically to do

### When to Run a Pre-Mortem

| Timing | Context |
|--------|---------|
| **Phase 3 to 4 transition** | After commitments are planned, before resources are locked in |
| **Before major launch** | Before go-to-market execution begins |
| **Before funding/investment decisions** | Before committing significant capital |
| **Quarterly roadmap planning** | Before locking the quarterly plan |
| **After major pivot** | When direction changes and new risks emerge |

### Pre-Mortem vs Other Risk Tools

| Tool | Focus | Timing | Style |
|------|-------|--------|-------|
| **Pre-Mortem** | Creative failure imagination | Before commitment | Divergent, psychological |
| **Risk Register** | Systematic risk cataloging | Ongoing | Convergent, operational |
| `/four-risks-check` | Marty Cagan's 4 risk categories | During discovery | Framework-driven |
| `/assumption-map` | Surfacing hidden assumptions | Phase 1-2 | Analytical |
| `FMEA` | Engineering failure modes | Design phase | Quantitative, technical |

## Output Structure

```markdown
# Pre-Mortem: [Project/Initiative Name]

**Date**: [YYYY-MM-DD]
**Facilitator**: [Name]
**Participants**: [Names and roles]
**Project**: [Brief description of what was pre-mortemed]
**Timeframe**: [The imagined failure horizon -- e.g., "6 months from now"]

## The Failure Scenario

"It is [date]. [Project name] has failed. [1-2 sentence vivid description of the failure state]."

## Failure Modes Identified

### Category: Technical

| # | Failure Mode | Severity | Likelihood | Priority | Owner |
|---|-------------|----------|------------|----------|-------|
| FM-1 | [Specific failure description] | [Critical/High/Med/Low] | [VLikely/Likely/Possible/Unlikely] | [Prevent/Mitigate/Monitor/Accept] | [Name] |
| FM-2 | [Specific failure description] | [Severity] | [Likelihood] | [Priority] | [Name] |

### Category: Market

| # | Failure Mode | Severity | Likelihood | Priority | Owner |
|---|-------------|----------|------------|----------|-------|
| FM-3 | [Specific failure description] | [Severity] | [Likelihood] | [Priority] | [Name] |

### Category: Execution

| # | Failure Mode | Severity | Likelihood | Priority | Owner |
|---|-------------|----------|------------|----------|-------|
| FM-4 | [Specific failure description] | [Severity] | [Likelihood] | [Priority] | [Name] |

### Category: People

| # | Failure Mode | Severity | Likelihood | Priority | Owner |
|---|-------------|----------|------------|----------|-------|
| FM-5 | [Specific failure description] | [Severity] | [Likelihood] | [Priority] | [Name] |

### Category: External

| # | Failure Mode | Severity | Likelihood | Priority | Owner |
|---|-------------|----------|------------|----------|-------|
| FM-6 | [Specific failure description] | [Severity] | [Likelihood] | [Priority] | [Name] |

### Category: Customer

| # | Failure Mode | Severity | Likelihood | Priority | Owner |
|---|-------------|----------|------------|----------|-------|
| FM-7 | [Specific failure description] | [Severity] | [Likelihood] | [Priority] | [Name] |

## Priority Summary

| Priority | Count | Failure Modes |
|----------|-------|---------------|
| **Prevent** | [N] | FM-1, FM-3, ... |
| **Mitigate** | [N] | FM-2, FM-4, ... |
| **Monitor** | [N] | FM-5, ... |
| **Accept** | [N] | FM-6, ... |

## Mitigation Plans

### FM-1: [Failure Mode Title] -- PREVENT

**What failed**: [Description]
**Mitigation**: [Specific preventive action]
**Owner**: [Name]
**Trigger**: [When to execute -- date, event, or metric threshold]
**Success criteria**: [How we know the mitigation worked]
**Status**: [Not started / In progress / Complete]

### FM-2: [Failure Mode Title] -- MITIGATE

**What failed**: [Description]
**Detection mechanism**: [Early warning signal]
**Mitigation**: [Action to reduce impact]
**Owner**: [Name]
**Trigger**: [When to execute]
**Contingency**: [What if mitigation is insufficient]
**Status**: [Not started / In progress / Complete]

### FM-3: [Failure Mode Title] -- MONITOR

**What failed**: [Description]
**Monitoring mechanism**: [What to watch]
**Threshold**: [When it becomes a problem]
**Escalation**: [Who to alert and what action to take]

## Key Themes

### Most Dangerous Cluster
[Which category has the highest concentration of Prevent/Mitigate items? What does this tell us?]

### Blindspot Check
[Were any categories empty? Empty categories may indicate blind spots rather than absence of risk.]

### Confidence Assessment
[Overall confidence that identified failure modes are comprehensive. What might we still be missing?]

## Integration with Project Plan

- [ ] Mitigation owners confirmed and briefed
- [ ] Prevention actions added to project timeline
- [ ] Detection mechanisms set up (dashboards, alerts, check-ins)
- [ ] Re-run pre-mortem scheduled for [date] or [milestone]

## Assumptions Surfaced

| # | Assumption | Related Failure Mode | Confidence | Validation Plan |
|---|-----------|---------------------|------------|-----------------|
| 1 | [Assumption exposed by failure mode] | FM-X | [High/Med/Low] | [How to validate] |
```

## Instructions

1. **Require a plan or project to pre-mortem.** The pre-mortem needs enough concrete detail to imagine failure -- a vague idea is too early (use `/assumption-map` instead).
2. Brief the project clearly before the failure imagination step. Context enables specificity.
3. Use the exact framing: "It is [future date] and this project has **failed spectacularly**." Past tense is essential.
4. If facilitating with a real team, enforce silent writing before sharing -- this prevents anchoring on the first person's ideas.
5. Do not dismiss any failure mode during the generation phase. Assessment comes later.
6. Every Prevent and Mitigate item must have a named owner, a trigger, and a specific action. "We should be careful" is not a mitigation.
7. Flag empty categories -- they often indicate blind spots, not absence of risk.
8. Do not fabricate severity or likelihood scores without basis. Use the team's judgment or ask the user.
9. Save output as markdown file.
10. Offer `/commitment-check` to validate that mitigations are in place before committing, or `/assumption-map` to formally track assumptions surfaced by the pre-mortem.

## Integration

- Links to `/commitment-check` (pre-mortem mitigations become pre-conditions for commitment)
- Links to `/launch-readiness` (failure modes inform launch readiness checklist)
- Links to `/assumption-map` (assumptions surfaced during pre-mortem feed the assumption registry)
- Links to `/four-risks-check` (complementary risk assessment from a different angle)
- Links to `/experiment-design` (high-uncertainty failure modes may need experiments to validate)
- Links to `/retrospective` (compare pre-mortem predictions to actual outcomes for learning)
- Links to `/decision-record` (pre-mortem results may trigger changes to decisions)
- Links to `/context-save` (save pre-mortem results as organizational learning)

## Vision to Value Operating Principle

> "Optimism is not a strategy. The pre-mortem harnesses the power of prospective hindsight to surface risks that groupthink and optimism bias would otherwise hide. The best time to imagine failure is before you commit -- when you can still change course."
