---
name: daci
description: |
  Create a DACI decision-making framework to clarify decision roles: Driver, Approver, Contributors, and Informed. Prevents decision paralysis by explicitly assigning accountability.
  Activate when: "DACI", "decision framework", "who decides", "decision roles", "driver approver", "RACI", "decision accountability", "decision rights", "decision ownership", "who has the call"
  Do NOT activate for: decision records (/decision-record), decision quality audits (/decision-quality-audit), escalation rules (/escalation-rule)
argument-hint: [decision or set of decisions to assign roles for] or [update path/to/daci.md]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: decision-making
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "change roles" in input | UPDATE | 100% |
| File path provided (`@path/to/daci.md`) | UPDATE | 100% |
| "create", "new", "set up DACI", "assign roles" in input | CREATE | 100% |
| "find", "search", "list DACI" | FIND | 100% |
| "the DACI", "our decision roles" | UPDATE | 85% |
| Just a decision or topic | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Define the decision(s), assign D/A/C/I roles, document rationale, and establish escalation path.

**UPDATE**:
1. Read existing DACI document (search if path not provided)
2. Preserve role assignments that remain valid
3. Update changed roles, add new decisions
4. Show diff summary: "Changed: [role changes]. Added: [new decisions]. Unchanged: [decisions]."

**FIND**:
1. Search paths below for DACI documents
2. Present results: decision area, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `product/`
- `decisions/`
- `governance/`
- `planning/`

---
## Gotchas

- There must be exactly ONE Approver per decision -- committees do not approve; individuals do. If you cannot name one person, that is the problem DACI is solving.
- Driver is NOT the Approver -- the Driver owns the process (gathering input, scheduling, synthesizing), while the Approver owns the final call. Conflating these roles defeats the purpose.
- Contributors who believe they are Approvers will derail decisions -- make the DACI visible and explicit at the start, not after conflict arises
- DACI applies to the decision, not the implementation -- after the Approver decides, implementation ownership may transfer to someone else entirely

## Vision to Value Phase

**Cross-phase** - DACI is used throughout the Vision to Value methodology. Every phase involves decisions that need clear ownership: strategic direction (Phase 1), pricing and positioning (Phase 2), roadmap commitments (Phase 3), launch decisions (Phase 4), outcome interpretation (Phase 5), learning actions (Phase 6).

**Prerequisites**: An identified decision or set of decisions that lack clear ownership or are stalling due to ambiguous authority
**Outputs used by**: `/decision-record` (DACI roles feed into decision documentation), `/commitment-check` (clear decision authority enables commitment), `/stakeholder-brief` (Informed parties need appropriate communication)

## Methodology

<!-- Source: DACI Framework -- Intuit internal practice, later popularized by Atlassian's Team Playbook (atlassian.com/team-playbook/plays/daci). DACI is a variant of the RACI matrix specifically optimized for decision-making rather than task assignment. -->

<!-- Source: Atlassian Team Playbook -- open resource providing collaborative plays for team effectiveness. DACI is one of their most popular plays. -->

### The DACI Roles

| Role | Symbol | Count | Definition | Key Question |
|------|--------|-------|------------|--------------|
| **Driver** | D | Exactly 1 | The person who drives the decision to completion. Gathers input, schedules discussions, synthesizes options, and ensures the decision gets made on time. | "Who is responsible for making this decision happen?" |
| **Approver** | A | Exactly 1 | The person who makes the final call. Has veto power. Must be a single individual, never a committee. | "Who has the authority to say yes or no?" |
| **Contributors** | C | 1 or more | Subject matter experts and stakeholders whose input is actively sought before the decision. They influence but do not decide. | "Whose expertise or perspective is needed?" |
| **Informed** | I | 0 or more | People who are told about the decision after it is made. They do not provide input during the decision process. | "Who needs to know the outcome?" |

### DACI vs RACI

| Aspect | DACI | RACI |
|--------|------|------|
| **Purpose** | Decision-making | Task/deliverable assignment |
| **D = Driver** | Drives the decision process | R = Responsible (does the work) |
| **A = Approver** | Makes the final call | A = Accountable (ultimate authority) |
| **C = Contributors** | Input before the decision | C = Consulted (two-way communication) |
| **I = Informed** | Told after the decision | I = Informed (one-way communication) |
| **Best for** | Strategic decisions, cross-functional calls | Project execution, work assignments |

**When to use DACI over RACI**: When the question is "who decides?" rather than "who does the work?" Use DACI for decisions; use RACI for tasks.

### Common Decision Types and Typical DACI

| Decision Type | Typical Driver | Typical Approver | Typical Contributors |
|--------------|---------------|-----------------|---------------------|
| Feature prioritization | PM | VP Product or PM-Dir | Engineering, Design, BizOps, Customer Success |
| Pricing changes | BizOps | VP Product or CPO | PM, PMM, Finance, Sales |
| Go-to-market strategy | PMM-Dir | VP Product | PM, BizDev, Sales, Marketing |
| Architecture decisions | Tech Lead | Chief Architect or VP Eng | PM, Security, DevOps |
| Hiring decisions | Hiring Manager | Skip-level manager | Interview panel, HR |
| Budget allocation | BizOps | CPO or VP Product | PM-Dir, PMM-Dir, Finance |
| Partnership deals | BizDev | VP Product or CEO | Legal, PM, Finance |
| Launch go/no-go | ProdOps | PM-Dir or VP Product | PM, QA, PMM, Support |

### Anti-Patterns (Must Avoid)

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| **Multiple Approvers** | No one has final authority; decisions stall in consensus-seeking | Pick ONE. If genuinely shared authority, escalate to their common manager as Approver. |
| **Driver = Approver** | Person driving the process also decides; no separation of investigation from judgment | Split the roles. Driver synthesizes options; Approver evaluates them. |
| **Contributor Creep** | Everyone is a Contributor; meeting bloat, decision paralysis | Limit Contributors to people with unique, material input. Everyone else is Informed. |
| **Shadow Approver** | The named Approver defers to someone else (their boss, a louder voice) | Make the real power structure explicit. DACI that does not reflect reality is decoration. |
| **No Approver** | Decision made "by committee" or "by consensus" | Someone always has authority. Find them. If no one does, escalate to create that authority. |
| **Informed Who Act Like Contributors** | People in the I role provide unsolicited input and reopen decisions | Reinforce DACI at kickoff. Informed means informed, not consulted. |

### The DACI Process

**Step 1: Define the Decision**
Write a clear, specific decision statement. Not "product strategy" but "Which market segment do we target for Q3 expansion?"

**Step 2: Assign Roles**
- Start with the Approver: who has the authority?
- Then the Driver: who will run the process?
- Then Contributors: whose input is essential (not nice-to-have)?
- Then Informed: who needs to know the outcome?

**Step 3: Communicate the DACI**
Share the DACI assignment with all parties BEFORE the decision process starts. This prevents role confusion mid-process.

**Step 4: Run the Decision Process**
- Driver gathers input from Contributors
- Driver synthesizes options with pros/cons
- Driver presents recommendation to Approver
- Approver makes the call (may ask for more input, but eventually decides)

**Step 5: Communicate the Decision**
- Driver notifies Informed parties of the outcome
- Decision is documented (via `/decision-record`)

### Escalation: When Driver and Approver Disagree

If the Driver's recommendation differs from the Approver's decision:
1. The **Approver's decision stands** -- that is the role
2. The Driver may **formally register disagreement** in the decision record
3. If the Driver believes the decision is harmful, escalate to the **Approver's manager** -- but this should be rare
4. After the decision, everyone commits (disagree and commit)

### When NOT to Use DACI

| Situation | Why Not | Alternative |
|-----------|---------|-------------|
| Routine operational decisions | Overhead of DACI exceeds value | Standing authority (e.g., "PM decides feature scope") |
| Emergency/crisis decisions | No time for process | Incident commander model |
| Individual contributor decisions | One person already owns it | Just decide |
| Brainstorming or exploration | No decision being made yet | `/brainstorming` |

## Output Structure

```markdown
# DACI: [Decision Area / Context]

**Date**: [YYYY-MM-DD]
**Owner**: [Who created this DACI]
**Scope**: [What decisions does this DACI cover]
**Status**: [Active / Superseded / Archived]

## Decision Inventory

| # | Decision | Status | Target Date |
|---|----------|--------|-------------|
| 1 | [Specific decision statement] | [Open / Decided / Deferred] | [YYYY-MM-DD] |
| 2 | [Specific decision statement] | [Open / Decided / Deferred] | [YYYY-MM-DD] |

## DACI Assignments

### Decision 1: [Decision Statement]

| Role | Person | Rationale |
|------|--------|-----------|
| **Driver (D)** | [Name, Title] | [Why this person drives the process] |
| **Approver (A)** | [Name, Title] | [Why this person has final authority] |
| **Contributors (C)** | [Name, Title] | [What unique input they provide] |
|  | [Name, Title] | [What unique input they provide] |
|  | [Name, Title] | [What unique input they provide] |
| **Informed (I)** | [Name, Title] | [Why they need to know] |
|  | [Name, Title] | [Why they need to know] |

**Decision process**: [How will input be gathered? Meeting, async doc review, 1:1 interviews?]
**Timeline**: [Key dates -- input deadline, decision meeting, communication]

### Decision 2: [Decision Statement]

[Same structure as above]

## Escalation Path

| Scenario | Escalation |
|----------|-----------|
| Driver and Approver disagree | [Escalation process] |
| Contributor raises blocker | [How it's handled] |
| Decision deadline passes without resolution | [What happens] |

## Communication Plan

| Milestone | Audience | Channel | Owner |
|-----------|----------|---------|-------|
| DACI published | All roles | [Email/Slack/Doc] | Driver |
| Input gathered | Approver | [Meeting/Doc] | Driver |
| Decision made | Informed | [Email/Slack] | Driver |
| Decision documented | All stakeholders | [Decision record link] | Driver |

## Anti-Pattern Check

- [ ] Exactly one Approver per decision (no committees)
- [ ] Driver is NOT the same person as Approver
- [ ] Contributors limited to people with essential input
- [ ] Informed parties will NOT be asked for input
- [ ] All parties have been notified of their roles
- [ ] DACI reflects actual power structure (no shadow approvers)

## Decisions Log

### Decision 1: [Statement]
**Decided**: [YYYY-MM-DD]
**Outcome**: [What was decided]
**Rationale**: [Why this option was chosen]
**Dissent**: [Any formal disagreements registered]
**Decision Record**: [Link to /decision-record if created]
```

## Instructions

1. Start by understanding what decisions need DACI assignment -- a single decision or a set of related decisions
2. For each decision, write a specific, actionable decision statement (not a topic area)
3. Assign the Approver FIRST -- this is the hardest role to fill and the most important
4. Challenge "committee approval" -- push for a single Approver. If they insist on two, ask: "If these two people disagree, who wins?"
5. Limit Contributors to people with essential, unique input. Use the test: "Would the decision quality materially decrease without this person's input?"
6. Make the DACI visible -- hidden DACIs do not prevent conflict
7. For recurring decisions, create a standing DACI that does not need to be re-established each time
8. Save output as markdown file
9. Offer `/decision-record` to document the actual decision once made, or `/stakeholder-brief` to communicate outcomes to Informed parties

## Integration

- Links to `/decision-record` (DACI roles documented in the decision record)
- Links to `/stakeholder-map` (stakeholder analysis informs C and I assignments)
- Links to `/commitment-check` (clear decision authority enables commitment)
- Links to `/stakeholder-brief` (Informed parties receive structured communication)
- Links to `/collaboration-check` (verify cross-functional decision-making is effective)
- Links to `/escalation-rule` (escalation paths for decision deadlocks)
- Links to `/context-save` (save standing DACIs for organizational memory)

## Vision to Value Operating Principle

> "Decision paralysis is not caused by lack of information -- it is caused by lack of clarity about who decides. DACI makes the invisible power structure visible and the decision process navigable."
