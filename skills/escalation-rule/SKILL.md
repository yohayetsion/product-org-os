---
name: escalation-rule
description: 'Define escalation rules and triggers for a specific decision area. Activate when: "when to escalate", "escalation path", "create escalation rule", escalation triggers, escalation criteria,
  when to involve leadership Do NOT activate for: documenting individual decisions (/decision-record), decision ownership charters (/decision-charter), decision audits (/decision-quality-audit)'
argument-hint: '[decision area] or [update path/to/rule.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 3.0.0
  category: decisions
  skill_type: task-capability
  owner: compliance-officer
  primary_consumers:
  - pm-dir
  - prodops
  - legal-dir
  - compliance-officer
  - support-lead
  - coo
  - finance-dir
  - financial-controller
  - hr-dir
  - it-dir
  - it-security-policy
  - operations-dir
  - program-manager
  - risk-manager
  - sales-dir
  secondary_consumers:
  - cs-dir
  - cs-ops
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "modify" in input | UPDATE | 100% |
| File path provided | UPDATE | 100% |
| Rule ID mentioned (e.g., ESC-2026-001) | UPDATE | 100% |
| "create", "new", "define" in input | CREATE | 100% |
| "find", "search", "list" | FIND | 100% |
| "the escalation rule", "our rules" | UPDATE | 85% |
| Just decision area | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new escalation rule using template below.

**UPDATE**:
1. Check document registry first, then search user's structure
2. Preserve rule ID and version
3. Update triggers, matrix, or resolution expectations
4. Show diff summary

**FIND**: Check registry, then search user's folders for escalation rules.

---

Define **Escalation Rules** for a specific decision area.

## Vision to Value Phase

**Phase 2: Strategic Decisions** - Escalation rules ensure decision quality when standard authority is insufficient.

**Prerequisites**: Decision charters or patterns established
**Outputs used by**: All phases (provides escalation governance)

## Purpose
Escalation rules ensure decisions move up appropriately when they exceed normal authority or encounter blockers.

## Output Structure

```markdown
# Escalation Rule: [Decision Area]

**Rule ID**: ESC-[YYYY]-[NNN]
**Version**: 1.0
**Effective Date**: [Date]
**Owner**: [Role]

## Scope

**Decision Area**: [What types of decisions this covers]
**Default Owner**: [Role who normally decides]
**Normal Authority**: [What they can decide without escalation]

## Escalation Triggers

### Trigger 1: [Name]
**Condition**: [When this trigger activates]
**Examples**:
- [Example situation]
- [Example situation]

**Escalate To**: [Role]
**Timeline**: [How quickly]

### Trigger 2: [Name]
**Condition**: [When this trigger activates]
**Examples**:
- [Example situation]
- [Example situation]

**Escalate To**: [Role]
**Timeline**: [How quickly]

### Trigger 3: [Name]
**Condition**: [When this trigger activates]
**Examples**:
- [Example situation]
- [Example situation]

**Escalate To**: [Role]
**Timeline**: [How quickly]

## Escalation Matrix

| Trigger Type | Level 1 | Level 2 | Level 3 |
|--------------|---------|---------|---------|
| Budget exceeded | [Role] | [Role] | [Role] |
| Timeline risk | [Role] | [Role] | [Role] |
| Stakeholder conflict | [Role] | [Role] | [Role] |
| Technical blocker | [Role] | [Role] | [Role] |
| Resource constraint | [Role] | [Role] | [Role] |

## Escalation Process

### Step 1: Recognize the Trigger
- Identify which trigger condition applies
- Document the situation clearly

### Step 2: Prepare the Escalation
Before escalating, prepare:
- [ ] Summary of the situation (1 paragraph)
- [ ] What has been tried
- [ ] Options with pros/cons
- [ ] Recommended action
- [ ] Timeline for decision needed

### Step 3: Escalate
- Contact the appropriate escalation owner
- Provide prepared information
- Agree on decision timeline

### Step 4: Follow Up
- Document the escalated decision
- Communicate to affected parties
- Update relevant plans

## Information Required for Escalation

**Always include:**
1. What triggered the escalation
2. Impact if not resolved
3. Options considered
4. Recommended path forward
5. Decision needed by when

**Format**: [Template or document to use]

## Decision Frame Requirement (Mandatory)

An escalation that arrives as a problem statement turns the senior reviewer into an analyst. An escalation that arrives as a decision frame turns the senior reviewer into a decider. The escalation rule enforces the second shape.

Every escalation routed through this rule MUST present a **Decision Frame** with three named elements before the escalation is accepted by the receiver. The receiver should refuse to engage substantively with an escalation that is missing any of the three.

### The three required elements

| Element | What it answers | Failure mode if missing |
|---|---|---|
| **The Decision** | What specific decision is being asked of the escalation owner. Stated as a single sentence with a verb and an object. | The receiver cannot tell what they are deciding. The conversation defaults to "let me understand the situation" — i.e. analysis, not decision-making. |
| **The Alternatives** | At least two named, mutually exclusive options the receiver is choosing between. Each named option carries its own pros, cons, and rough cost. A "do nothing" or "defer" option is allowed and often correct. | The receiver is presented with one path and asked to bless it, which is rubber-stamping, not deciding. Alternatives force the tradeoff into the open. |
| **The Criteria** | The named criteria the receiver should use to choose between the alternatives, ordered by weight. Examples: "minimize regulatory exposure first, then cost," or "preserve customer trust first, then speed." | The receiver and the escalator may agree on the chosen alternative for different reasons, and the next similar escalation will not benefit from the precedent. |

### Decision Frame template

The escalating party fills out this block and includes it at the top of the escalation:

```markdown
## Decision Frame

**The Decision**: [One sentence. Verb + object. e.g., "Whether to grant Vendor X a six-month extension on the data-processing addendum."]

**The Alternatives**:
1. **[Option A name]** — [1-2 sentence description]
   - Pros: [list]
   - Cons: [list]
   - Rough cost: [time, money, or risk]
2. **[Option B name]** — [1-2 sentence description]
   - Pros: [list]
   - Cons: [list]
   - Rough cost: [time, money, or risk]
3. **[Option C name, e.g., "Defer / Do Nothing"]** — [1-2 sentence description]
   - Pros: [list]
   - Cons: [list]
   - Rough cost: [time, money, or risk]

**The Criteria** (ordered by weight):
1. [Criterion 1 — e.g., "Minimize regulatory exposure"]
2. [Criterion 2 — e.g., "Preserve the customer relationship"]
3. [Criterion 3 — e.g., "Limit cost to under $50k"]

**Recommended Alternative**: [Option name] — [one sentence rationale tying recommendation to the named criteria]
```

### Skill behavior — validation step

When this skill runs an escalation flow (creating a rule, validating an incoming escalation, or coaching a team through an escalation), the skill performs a **Decision Frame validation step** before allowing the escalation to proceed:

1. Inspect the escalation input. Does it include all three elements (The Decision, The Alternatives, The Criteria)?
2. If YES → proceed with the rule's normal escalation flow (matrix, resolution expectations, follow-up).
3. If NO → the skill DOES NOT escalate. Instead, the skill walks the user back through framing:
   - "I can see the problem you're describing. Before this can be escalated, we need to convert it into a decision frame. Let's work through three questions."
   - Ask: "What specific decision are you asking [escalation owner] to make? State it as one sentence with a verb and an object."
   - Ask: "What are the alternatives [escalation owner] is choosing between? At least two, ideally three. Each with rough pros, cons, and cost."
   - Ask: "What criteria should [escalation owner] use to choose? Ordered by weight."
   - Once all three are answered, populate the Decision Frame template, then proceed with the escalation.

### Why this is mandatory, not optional

A problem statement that lands on a senior reviewer's desk consumes the reviewer's time twice: once to understand the situation, once to formulate the decision. A decision frame consumes it once. Across an organization with hundreds of escalations per quarter, the second pattern is structurally cheaper and produces better decisions because the alternatives are surfaced before the reviewer's anchor bias kicks in.

The rule is also a coaching mechanism. Teams that escalate decision frames, not problem statements, learn the discipline of framing — which is the same discipline that produces good `/decision-record` entries, good `/business-case` documents, and good `/strategic-bet` formulations. Enforcing the frame at escalation time pays compound returns.

## Resolution Expectations

| Priority | Response Time | Resolution Time |
|----------|---------------|-----------------|
| Critical | < 4 hours | < 24 hours |
| High | < 24 hours | < 72 hours |
| Medium | < 48 hours | < 1 week |
| Low | < 1 week | < 2 weeks |

## Anti-Patterns (Don't Do This)

- **Escalating a problem statement, not a decision frame**: The problem-statement shape ("X is broken, please advise") forces the reviewer to do the analyst's job. The decision-frame shape ("Choose between A, B, C using criteria 1, 2, 3 — I recommend B") forces the reviewer to do the decider's job. The skill rejects problem-statement escalations and walks the user back through framing.
- **Escalating without preparation**: Always come with options
- **Skipping levels**: Follow the escalation path
- **Waiting too long**: Escalate early when triggers hit
- **Escalating everything**: Use judgment; not everything needs escalation

## Related Rules

- [Link to related escalation rules]
- [Link to related decision charters]
```

## Instructions

1. Ask about the decision area if not specified
2. Reference any governance documents provided via @file syntax
3. Be specific about trigger conditions
4. Include clear escalation paths
5. Define expected resolution times
6. Validate every escalation against the Decision Frame Requirement before allowing the escalation to proceed. If The Decision, The Alternatives, or The Criteria are missing, walk the user back through framing instead of escalating.
7. Save in rules/ or governance/ folder
