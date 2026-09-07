# Companion — agent-metadata-schema (relocated reference)

> Relocated rationale/reference — the binding rule is `.claude/rules/agent-metadata-schema.md`;
> this file imposes nothing and relaxes nothing. Moved VERBATIM 2026-08-15
> (DR-2026-262). Do not edit here
> without the same review the rule itself requires.

---

<!-- from agent-metadata-schema · REFERENCE-MOVE · D14 measured Tier-1 distribution table (2026-05-18) -->

| Statistic | Value |
|---|---:|
| Median (p50) | 14,930 tokens |
| p75 | 19,895 tokens |
| p90 | 27,312 tokens |
| p95 | 34,608 tokens |
| p99 | 42,470 tokens |
| Max (`cs-ops`) | 44,222 tokens |

---

<!-- from agent-metadata-schema · REFERENCE-MOVE · measure-before-author precedent (Capability Embed 2026-07-13) -->

Precedent (Capability Embed, 2026-07-13): `ai-architect` measured 27k (over nominal), so new agent-memory + framework-selection content went into a new conditional pack `agent-runtime-patterns.md` rather than bloating the Tier-1 `ai-ml-patterns.md` — Tier-1 stayed flat. The counter-example on the same run: a ~1.3k append into a Tier-1 dev pack pushed `tech-lead` to 34.3k (689 tok from the hard cap), forcing a later M50 retier. Measure first; author to Tier-2 when headroom is thin.

---

<!-- from agent-metadata-schema · REFERENCE-MOVE · over-nominal-cap agent list (2026-05-18 baseline) -->

### Agents currently over the nominal cap (2026-05-18 baseline)

27 of 109 agents exceed 20k Tier-1 baseline. Of those, 6 exceed the 35k hard cap and need either case (b)-(d) declaration or pack diet:

| Agent | Tier-1 | Hard-cap status | Suggested variance case |
|---|---:|---|---|
| `cs-ops` | 44,222 | OVER | (d) operational-knowledge density |
| `head-corpdev` | 42,515 | OVER | (b) multi-specialist hub |
| `coo` | 41,958 | OVER | (c) cross-domain executive |
| `ma-analyst` | 41,039 | OVER | (b) multi-specialist hub |
| `operations-dir` | 36,487 | OVER | (b) multi-specialist hub |
| `compliance-officer` | 36,076 | OVER | (a) regulatory-density |

The remaining 21 agents (20k-35k) need either variance rationale added or M50 retiering.
