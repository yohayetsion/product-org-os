---
globs:
  - "**/*"
---

# Parallel Agent Execution

This rule enables and governs parallel execution of agents for efficient cross-functional work.

## Configuration

```yaml
parallel_agents_enabled: true
max_parallel_agents: 4
```

---

## When to Parallelize

Spawn agents in parallel when:

1. **Gathering inputs from multiple functions** - Portfolio reviews, strategic planning sessions
2. **Needs don't depend on each other's output** - Independent analyses that will be synthesized
3. **Time-sensitive decisions requiring fast input collection** - Urgent strategic choices

Do NOT parallelize when:

1. **Outputs are dependencies** - One agent needs another's output as input
2. **Coordination is required** - Agents need to negotiate or align
3. **Sequence matters** - Phase order must be respected

---

## Common Parallel Patterns

### Portfolio Review
Gather cross-functional perspectives on portfolio health:

```
Parallel: @bizops, @competitive-intelligence, @value-realization, @product-operations
```

**Use case**: QBR preparation, strategic planning session
**Synthesizer**: @cpo or @product-leadership-team

### Launch Decision
Gather readiness assessments from all functions:

```
Parallel: @product-manager, @product-marketing-manager, @product-operations
```

**Use case**: Launch readiness review
**Synthesizer**: @director-product-management

### Strategic Planning Input
Gather market and business intelligence:

```
Parallel: @competitive-intelligence, @bizops, @value-realization
```

**Use case**: Annual planning, strategic bet formulation
**Synthesizer**: @vp-product or @cpo

### Go-to-Market Preparation
Gather all GTM components:

```
Parallel: @product-marketing-manager, @bizdev, @sales-enablement
```

**Use case**: GTM strategy development
**Synthesizer**: @director-product-marketing

### Customer Success Review
Gather customer-facing perspectives:

```
Parallel: @value-realization, @ux-lead, @product-manager
```

**Use case**: Customer health assessment, NPS response planning
**Synthesizer**: @vp-product

---

## How to Invoke Parallel Agents

Use multiple Task tool calls in a single message:

```markdown
I need inputs from multiple functions. Spawning parallel agents:

[Task: @bizops - Provide financial analysis for Q2 portfolio review]
[Task: @competitive-intelligence - Provide competitive update for Q2]
[Task: @value-realization - Provide customer outcome summary for Q2]
```

Each agent receives the same context and works independently. Results are synthesized when all return.

---

## Meeting Mode Presentation (CRITICAL)

**Agent responses are presented as a MEETING, not a monolithic synthesis.**

### Core Requirement

When multiple agents are invoked (parallel or sequential), their responses MUST be:

1. **Individually attributed** - Each agent's contribution is clearly labeled
2. **Shown in their voice** - Reflect the agent's role perspective and concerns
3. **Visible to the user** - Don't hide agent responses behind synthesis

### Presentation Format

```markdown
## Gathering Perspectives

**Inviting**: @bizops, @competitive-intelligence, @value-realization

---

### @bizops
"From a financial analysis perspective, I see..."

### @competitive-intelligence
"Looking at the competitive landscape, the key issue is..."

### @value-realization
"Customer outcome data suggests..."

---

## Points of Agreement
- [What agents align on]

## Points of Tension
- @bizops flags cost concern; @value-realization emphasizes customer need

## Synthesis
[Only AFTER individual voices shown]
```

### Why This Matters

- **Transparency**: User sees how the org thinks, not just conclusions
- **Trust**: Attribution builds confidence in the analysis
- **Learning**: Seeing multiple perspectives teaches the user about their org
- **Debugging**: When something goes wrong, you can trace which lens missed it

---

## Synthesis Responsibility

When parallel agents complete, a synthesizing agent must:

1. **Present individual outputs first** - Show each agent's attributed response
2. **Collect all outputs** - Gather results from each parallel agent
3. **Identify conflicts** - Note where perspectives differ (and show them)
4. **Synthesize insights** - Create unified view AFTER showing individual perspectives
5. **Recommend actions** - Propose path forward
6. **Document in context** - Save synthesized output with `/context-save`

---

## Agent-Specific Parallel Patterns

### For @cpo

**When reviewing portfolio**:
```
Parallel: @director-product-management, @director-product-marketing, @bizops
```

**When preparing board materials**:
```
Parallel: @bizops (financials), @competitive-intelligence (market), @value-realization (customers)
```

### For @director-product-management

**When planning roadmap**:
```
Parallel: @product-manager (requirements), @product-operations (capacity), @ux-lead (design)
```

**When assessing delivery**:
```
Parallel: @product-manager (feature status), @product-operations (process health)
```

### For @director-product-marketing

**When developing GTM**:
```
Parallel: @product-marketing-manager (campaigns), @competitive-intelligence (positioning), @bizdev (partnerships)
```

**When planning launch**:
```
Parallel: @product-marketing-manager (comms), @product-operations (readiness)
```

### For @product-leadership-team

**When making portfolio tradeoffs**:
```
Parallel: ALL relevant agents for comprehensive input
```

**When conducting outcome reviews**:
```
Parallel: @value-realization, @bizops, @product-manager
```

---

## Parallel Execution Guardrails

### Context Sharing

All parallel agents receive:
- Current session context via `/handoff`
- Portfolio status via `/portfolio-status`
- Relevant prior context via `/context-recall`

### Conflict Resolution

When parallel agents produce conflicting recommendations:
1. **Document the conflict** - Don't hide disagreement
2. **Identify root cause** - Different data? Different priorities? Different assumptions?
3. **Escalate if needed** - Use RACI to determine decision owner
4. **Record resolution** - Document how conflict was resolved

### Resource Limits

- **Max parallel agents**: 4 (configurable)
- **Timeout**: Agents should complete within reasonable time
- **Fallback**: If agent doesn't respond, proceed without and note the gap

---

## V2V Operating Principle

> "Parallel execution isn't about going faster - it's about getting comprehensive input while respecting everyone's expertise. Speed is a side effect of good design."
