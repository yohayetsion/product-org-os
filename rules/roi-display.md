# ROI Display (SELECTIVE)

Show ROI when you produce a tangible deliverable. Skip for everything else.

---

## Quick Test

**"Did I create or deliver something the user would save as a file?"** YES → Show ROI. NO → Skip.

## Format

### Single Agent
```
⏱️ ~[X]hrs saved in [Y]s, [Z]k tkns ~$[C] cost, Value ~$[V]
```

### Multi-Agent (Gateway/PLT)
```
⏱️ Total: ~[X]hrs saved in [Y]min, [Z]k tkns ~$[C] cost, Value ~$[V]

└─ {emoji} {Display Name}: ~[X]hrs saved, [Z]k tkns ~$[C] cost, Value ~$[V]
└─ {emoji} {Display Name}: ~[X]hrs saved, [Z]k tkns ~$[C] cost, Value ~$[V]
```

### Field Definitions

| Field | How to Calculate |
|-------|-----------------|
| **Time saved** | Base time from `reference/roi-baselines.md` × complexity multiplier |
| **Elapsed** | Wall-clock time the agent(s) took. Parallel = max; sequential = sum |
| **Tokens** | Sum of input + output tokens used. Round to nearest 1k. Use `k` suffix |
| **Cost** | Tokens × model rate. Opus: ~$0.015/1k input + $0.075/1k output. Round to $0.1 |
| **Value** | Time saved in hours × $100/hr (senior product professional rate) |

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
3. Calculate: Base Time × Factor = Time Savings
4. Value = Time Savings (hrs) × $100/hr

## Session Tracking

ROI logging is handled automatically by `hooks/os-tracker.py`. When hooks are configured (Claude Code PostToolUse), tracking happens without manual action. For manual setups, see `AGENT-INTEGRATION.md`.

For multi-agent ROI aggregation, see `agent-spawn-protocol.md` Section 3.

---

## Operating Principle

> "ROI tracking demonstrates value for meaningful work. Don't clutter simple interactions with metrics."
