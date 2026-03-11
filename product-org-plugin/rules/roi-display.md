# ROI Display (SELECTIVE)

Show ROI when you produce a tangible deliverable. Skip for everything else.

---

## Quick Test

**"Did I create or deliver something the user would save as a file?"** YES → Show ROI. NO → Skip.

## Format

```
⏱️ ~[X] hrs/min saved in [Y]s (vs. [brief manual equivalent])
```

Always reference product work, never coding/development.

## Trigger Checklist

| Show ROI | Skip |
|----------|------|
| Created PRD, spec, analysis doc | Answered a question |
| Agent produced recommendations | Looked up context/feedback |
| PLT/gateway with synthesis | Explained something |
| | Failed/system operations |

## Calculation

1. Look up base time in `reference/roi-baselines.md`
2. Apply complexity: Simple 0.5× | Standard 1.0× | Complex 1.5× | Enterprise 2.0×
3. Calculate: Base Time × Factor = Savings

## Session Tracking

ROI logging is handled automatically by `hooks/os-tracker.py`. When hooks are configured (Claude Code PostToolUse), tracking happens without manual action. For manual setups, see `AGENT-INTEGRATION.md`.

For multi-agent ROI aggregation, see `agent-spawn-protocol.md` Section 3.

---

## Operating Principle

> "ROI tracking demonstrates value for meaningful work. Don't clutter simple interactions with metrics."
