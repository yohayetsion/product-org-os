# Companion — delegate-first (relocated reference)

> Relocated rationale/reference — the binding rule is `.claude/rules/delegate-first.md`;
> this file imposes nothing and relaxes nothing. Moved VERBATIM 2026-08-15
> (DR-2026-262). Do not edit here
> without the same review the rule itself requires.

---

<!-- from delegate-first · REFERENCE-MOVE · shared-skill orchestrator problem statement -->

### Problem Statement

When a specialist skill (e.g., `/risk-analysis`, `/contract-stress-test`, `/ai-control-audit`) is consumed by multiple gateways, ownership fragments. Two teams quietly co-edit the skill, assumptions drift apart, and a change made for one gateway breaks the other. Silent dependencies + unversioned changes = production incidents that are hard to root-cause.

---

<!-- from delegate-first · REFERENCE-MOVE · shared-skill orchestrator worked example (hypothetical) -->

### Example (Hypothetical)

`/risk-analysis` is authored by `general-counsel` (owner) but consumed by:
- `ext-legal` gateway (primary consumer — legal risk framing)
- `product` gateway (secondary consumer — strategic bet risk analysis)
- `ext-corpdev` gateway (secondary consumer — M&A deal risk)

Frontmatter:
```yaml
name: risk-analysis
owner: general-counsel
consumers: [ext-legal, product, ext-corpdev]
sensitive: true
deprecation: { status: active }
```

When `head-corpdev` wants to change the output schema to add a "deal-specific risk" section, the change flows through `general-counsel` for approval. If approved, all three consumer gateways get the change at once with a note in the release log. No silent drift.
