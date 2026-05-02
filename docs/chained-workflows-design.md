# Chained Workflows Design

**Status**: Design Only — Not Yet Implemented
**Date**: 2026-03-29
**Author**: Product Org OS
**Reference**: phuryn/pm-skills (chaining patterns)

## Concept

Chained Workflows link multiple skills into end-to-end sequences that execute as a single command. Instead of manually running `/assumption-map` → `/experiment-design` → `/context-save` in sequence, a chained workflow like `/discover` would orchestrate all three with automatic data handoff between steps.

## Problem Statement

Today, users must manually chain skills:
1. Run `/assumption-map` → save output
2. Read output, pick critical assumptions
3. Run `/experiment-design` for each assumption → save output
4. Run `/context-save` to record the experiments

This requires the user to be the orchestrator. Chained workflows automate the orchestration while keeping the user in control of decisions at key gates.

## Proposed Workflow Examples

### `/discover` — Full Discovery Workflow

```
Step 1: /assumption-map [product/feature]
   ↓ (auto-extract Critical Risk + Validate First assumptions)
Step 2: /experiment-design [for each critical assumption]
   ↓ (batch experiment designs)
Step 3: /prioritize-features [experiment backlog by ICE score]
   ↓ (ranked experiment plan)
Step 4: /context-save [save discovery plan]
   → Output: Discovery plan with prioritized experiments
```

**Gates**: After Step 1, user confirms which assumptions to test. After Step 3, user approves experiment priority order.

### `/validate-bet` — Strategic Bet Validation

```
Step 1: /strategic-bet [the bet]
   ↓ (extract key assumptions + success criteria)
Step 2: /four-risks-check [the bet]
   ↓ (identify highest-risk dimension)
Step 3: /pre-mortem [the bet]
   ↓ (failure modes → mitigation plans)
Step 4: /experiment-design [for riskiest assumption]
   → Output: Validated bet with risk mitigation + first experiment
```

### `/launch` — Launch Orchestration

```
Step 1: /launch-readiness [product]
   ↓ (readiness checklist with gaps)
Step 2: /launch-plan [addressing gaps]
   ↓ (execution plan)
Step 3: /campaign-brief [GTM campaign]
   ↓ (marketing plan)
Step 4: /stakeholder-brief [for leadership]
   → Output: Complete launch package
```

### `/compete` — Competitive Response

```
Step 1: /competitive-analysis [competitor + event]
   ↓ (competitive assessment)
Step 2: /competitive-battlecard [competitor]
   ↓ (sales tool)
Step 3: /positioning-statement [update if needed]
   → Output: Updated competitive toolkit
```

## Architecture

### Chain Definition Format

```yaml
name: discover
display: "Discovery Workflow"
description: "Full discovery cycle: assumptions → experiments → prioritization"
steps:
  - skill: assumption-map
    input: "{user_input}"
    output_key: assumptions
    gate: true  # pause for user confirmation
    gate_prompt: "Which assumptions should we test?"

  - skill: experiment-design
    input: "{assumptions.critical}"
    output_key: experiments
    loop: true  # run once per critical assumption

  - skill: prioritize-features
    input: "{experiments}"
    framework: ICE
    output_key: ranked_experiments
    gate: true
    gate_prompt: "Approve this experiment priority?"

  - skill: context-save
    input: "{ranked_experiments}"
    auto: true  # no gate, runs automatically
```

### Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Gate model** | Explicit gates at key decision points | Users must stay in control of strategic decisions; full automation would undermine V2V's decision quality focus |
| **Data passing** | Output keys referenced by subsequent steps | Simple, debuggable; avoids complex state management |
| **Looping** | Per-item loop support for batch operations | Many workflows need to process multiple items (e.g., multiple assumptions → multiple experiments) |
| **Error handling** | Fail at step, show context, let user decide | Chains involve judgment; auto-retry makes less sense than for code |
| **Partial execution** | Resume from any step | Long chains shouldn't restart from scratch on interruption |

### Storage

Chain definitions would live in `product-org-plugin/chains/` as YAML files. The chain runner would be a skill itself (`/chain` or invoked by workflow name).

## Implementation Considerations

1. **Context window**: Multi-step chains with large outputs could exceed context. Each step should produce a summary + full file, with only summaries passed forward.
2. **Agent spawning**: Steps that involve agent personas (e.g., `/competitive-analysis` by `@ci`) should spawn the agent as normal.
3. **Parallel steps**: Some chains could parallelize independent steps (e.g., `/four-risks-check` and `/pre-mortem` in `/validate-bet`).
4. **Skill compatibility**: All existing skills work standalone. Chains are additive, not required.

## What This Does NOT Cover

- Implementation timeline
- Specific code or tooling changes
- Changes to existing skills (chains wrap them, don't modify them)

## Next Steps (When Implementing)

1. Build the chain runner (reads YAML, orchestrates skill execution)
2. Create 4-6 chain definitions for common workflows
3. Test with real product work
4. Add `/chain list` and `/chain run [name]` commands
