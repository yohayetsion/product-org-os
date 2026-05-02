# AutoResearch Eval Loops Design

**Status**: Design Only — Not Yet Implemented
**Date**: 2026-03-29
**Author**: Product Org OS
**Reference**: Maad House pitch deck pipeline (first real-world application)

## Concept

AutoResearch Eval Loops are a 3-file pattern for autonomous skill/prompt optimization. An agent generates output, an evaluator scores it against locked criteria, and a strategy file records what works. Over iterations, the agent's prompts improve without human intervention for each cycle.

The pattern is borrowed from ML training loops: generate → evaluate → update strategy → repeat.

## The 3-File Pattern

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  1. TRAINABLE    │────→│  2. LOCKED EVAL   │────→│  3. STRATEGY    │
│  (Agent Prompt)  │     │  (Scoring Rubric) │     │  (What Works)   │
│                  │←────│                   │     │                 │
│  Adapts based on │     │  Never changes    │     │  Accumulates    │
│  strategy file   │     │  during a cycle   │     │  learnings      │
└─────────────────┘     └──────────────────┘     └─────────────────┘
        ↑                                                │
        └────────────────────────────────────────────────┘
                        Feedback loop
```

### File 1: Trainable Agent Prompt

The prompt/skill that generates the output. This file CAN be modified between cycles based on learnings from the strategy file.

```markdown
# Generate Pitch Deck Config

## Instructions
{Current best-known approach}

## Strategy Learnings (auto-injected from File 3)
- Competitor sections must reference specific named competitors, not generic "industry players"
- Quick wins should be website-specific, not template content
- ...
```

### File 2: Locked Evaluation Rubric

The scoring criteria. This file is LOCKED during a cycle — it cannot be modified by the agent being evaluated. This prevents the agent from optimizing for easy scores rather than real quality.

```markdown
# Pitch Deck Config Evaluation

## Scoring Criteria (LOCKED)
- C1: Competitor specificity (named competitors, not generic) — 0-10
- C2: Quick win relevance (specific to THIS company) — 0-10
- C3: Brand voice match (uses company's language, not template) — 0-10
- ...

## Pass Threshold: Average >= 7.0, no individual score < 4
```

### File 3: Strategy File

Accumulates learnings across cycles. After each eval, the system records what scored well and what didn't, along with hypotheses for improvement.

```markdown
# Strategy Log

## Cycle 1 (2026-03-15)
- Average score: 5.2 (FAIL)
- Weak areas: C1 (3/10), C3 (4/10)
- Hypothesis: Agent needs explicit instruction to research competitors before generating config
- Action: Added "Step 0: Research competitors via website" to trainable prompt

## Cycle 2 (2026-03-16)
- Average score: 7.8 (PASS)
- Improved: C1 (8/10), C3 (7/10)
- Still weak: C5 (5/10) — CTA specificity
- Hypothesis: CTA template is too generic; needs industry-specific variants
- Action: Added CTA variant library to trainable prompt
```

## Real-World Application: Pitch Deck Pipeline

This pattern maps directly to the Maad House pitch deck pipeline:

| Component | Current Implementation | AutoResearch Pattern |
|-----------|----------------------|---------------------|
| **Trainable** | `/generate-deck-config` (Claude agent) | Agent prompt with strategy injection |
| **Locked Eval** | `gemini-qa-decks.py` (Gemini AI QA) | Scoring rubric (C1-C9, S1-S7) |
| **Strategy** | Manual fixes between batches | Auto-accumulated learnings |

**Current flow** (manual):
1. Claude generates config → 2. Gemini QA scores it → 3. Human reads QA, fixes config → 4. Regenerate → 5. Re-QA

**AutoResearch flow** (autonomous):
1. Claude generates config (reads strategy file) → 2. Gemini QA scores it → 3. If FAIL: Claude reads QA scores, updates strategy, regenerates (max 2 cycles) → 4. If PASS: done

## Architecture

### Loop Runner

```python
def autoresearch_loop(trainable_prompt, eval_rubric, strategy_file, max_cycles=3):
    for cycle in range(max_cycles):
        # Step 1: Generate (using trainable prompt + strategy)
        output = run_agent(trainable_prompt, inject=strategy_file)

        # Step 2: Evaluate (using locked rubric)
        scores = run_eval(eval_rubric, output)

        # Step 3: Check pass/fail
        if scores.passes_threshold():
            return output, scores

        # Step 4: Update strategy (agent analyzes its own failure)
        learnings = analyze_failure(scores, output)
        append_to_strategy(strategy_file, cycle, scores, learnings)

    # Max cycles reached — return best attempt + flag for human review
    return best_output, "MAX_CYCLES_REACHED"
```

### Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Eval must be locked** | Cannot be modified by the trainable agent | Prevents gaming — agent optimizes for quality, not easy scores |
| **Max 2-3 cycles** | Hard cap on retries | Prevents infinite loops; if 3 cycles can't fix it, human judgment needed |
| **Strategy is append-only** | New learnings added, old ones preserved | Builds institutional knowledge; avoids oscillation |
| **Different models for generate vs eval** | Recommended (e.g., Claude generates, Gemini evaluates) | Cross-model eval is more robust than self-eval |
| **Human review for MAX_CYCLES** | Required | Persistent failure likely indicates a rubric gap or edge case |

## Applicability Beyond Pitch Decks

| Application | Trainable | Eval | Strategy |
|-------------|-----------|------|----------|
| **PRD Generation** | `/prd` prompt | PRD quality rubric (completeness, clarity, testability) | What makes good PRDs for this org |
| **Email Copy** | `/subject-line` + `/copywriting` prompts | Open rate / response rate data | Subject line patterns that work |
| **Competitive Analysis** | `/competitive-analysis` prompt | Accuracy rubric (verifiable claims, source quality) | Research patterns that find real intel |
| **OKR Writing** | `/okr-writer` prompt | OKR quality rubric (measurability, ambition, alignment) | Common OKR mistakes in this org |

## What This Does NOT Cover

- Implementation code
- Specific eval rubrics for each application
- Changes to existing skills
- How strategy learnings persist across sessions (could use context layer)

## Next Steps (When Implementing)

1. Formalize the 3-file template structure
2. Build the loop runner (Python script or chain workflow)
3. Apply to pitch deck pipeline as first proof-of-concept
4. If successful, generalize to PRD and OKR generation
5. Consider integration with context layer for cross-session strategy persistence
