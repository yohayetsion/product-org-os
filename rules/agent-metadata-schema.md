---
globs:
  - "**/*"
---

# Agent Metadata Schema (v4.0)

Authoritative specification for `metadata:` fields in SKILL.md files across Product Org OS and Extension Teams. This schema uses the `metadata:` extension slot defined by the Agent Skills Specification (agentskills.io).

---

## Standard Fields (Agent Skills Spec)

These fields are top-level in the YAML frontmatter, defined by the Agent Skills spec:

| Field | Required | Type | Purpose |
|-------|----------|------|---------|
| `name` | Yes | string | Skill identifier (kebab-case) |
| `description` | Yes | string | Activation patterns for the LLM |
| `model` | No | string | Model override (e.g., `opus`) |
| `allowed-tools` | No | list | Tools this skill can use |
| `user-invocable` | No | bool | Whether users can invoke directly |
| `argument-hint` | No | string | Hint shown in CLI autocomplete |
| `globs` | No | list | File patterns for activation |

---

## Extension Fields (under `metadata:`)

All organizational data goes under `metadata:`. No custom top-level fields.

### Universal Fields (all skill types)

| Field | Type | Purpose |
|-------|------|---------|
| `skill_type` | enum: `agent`, `task-capability`, `gateway`, `alias` | What kind of SKILL.md this is |
| `author` | string | Authoring system (e.g., "Product Org OS") |
| `version` | string | Semantic version |
| `category` | string | Grouping category |

### Task-Capability Skill Fields

| Field | Type | Purpose |
|-------|------|---------|
| `owner` | string | Single agent accountable for correctness |
| `primary_consumers` | list[string] | Agents for whom this is core workflow |
| `secondary_consumers` | list[string] | Agents who use this occasionally |
| `sensitive` | bool | Subject to sensitive-skill-guardrails |

### Agent Skill Fields

| Field | Type | Purpose |
|-------|------|---------|
| `team` | string | Team this agent belongs to (e.g., "legal-team") |
| `emoji` | string | Agent identity emoji |
| `display_name` | string | Agent display name |
| `inherits_principles` | list[string] | PRINCIPLES.md path(s) — Tier 1 preload |
| `preload_knowledge_packs` | list[{path, reason}] | Tier 1: always read at start |
| `conditional_knowledge_packs` | list[{pack, trigger_keywords, action}] | Tier 2: read when trigger fires |
| `core_skills` | list[string] | Daily-workflow skills (primary consumer) |
| `supporting_skills` | list[string] | Specific-scenario skills (secondary consumer) |
| `mandatory_skill_invocations` | list[{skill, triggers, escape}] | Task types requiring specific skill invocation |
| `recommended_skills` | list[string] | Soft guidance (non-blocking) |
| `spawns_subagents` | list[string] | Agents this agent can delegate to |
| `delegation_patterns` | list[string] | consultation, delegation, review, debate, adversarial_review |
| `parallel_patterns` | list[{name, agents}] | Named parallel execution scenarios |
| `raci` | {accountable, responsible, consulted, informed} | RACI matrix entries |
| `key_deliverables` | list[{name, purpose, quality_bar}] | What this agent produces |
| `v2v_phases` | {primary, supporting} | Vision to Value phase assignments |
| `anti_patterns` | list[{name, why_harmful, what_I_do_instead}] | Behavioral guardrails |
| `guarded_principle` | {name, enforcement_actions} | Principle this agent actively enforces |
| `collaboration_map` | list[{with_agent, interface, handoff_pattern}] | Cross-agent interfaces |
| `tier1_variance_rationale` | string | Required if Tier-1 baseline exceeds the nominal cap (see "Token Budget Rule" §D14). Free-text citing variance case letter (a/b/c/d) + 1-2-sentence rationale. |

### Gateway Skill Fields

| Field | Type | Purpose |
|-------|------|---------|
| `routes_to` | list[string] | Agents this gateway can route to |

### Alias Skill Fields

| Field | Type | Purpose |
|-------|------|---------|
| `aliases_to` | string | Canonical skill this alias forwards to |

---

## Deprecated Fields (v4 migration)

These top-level fields are **deleted** in v4. Their content migrates to `metadata:`:

| Deprecated Field | Migrated To |
|------------------|-------------|
| `primary-skills` | `metadata.core_skills` |
| `supporting-skills` | `metadata.supporting_skills` |
| `validator-skills` | Merged into `metadata.supporting_skills` |
| `knowledge-packs` | `metadata.preload_knowledge_packs` |
| `owner` (top-level) | `metadata.owner` |
| `consumers` (top-level) | `metadata.primary_consumers` |
| `sensitive` (top-level) | `metadata.sensitive` |
| `compatibility` | Deleted (non-standard decoration) |
| `context` | Deleted (non-standard decoration) |

---

## Token Budget Rule (D14 — measurement-based, re-anchored 2026-05-18)

The 2024-era "≤ 2000 tokens for Tier 1 preload" cap is stale. The 2026-05-18 measurement established the Tier-1 baseline for the then-current agent corpus:

> *Relocated 2026-08-15 (DR-2026-262): D14 measured Tier-1 distribution table, 2026-05-18 (the binding caps derived from it remain below) — full table in the companion agent-metadata-schema.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

The pack ecosystem itself is heavier than the original cap assumed (133 packs measured; median pack = 5,011 tokens; max pack `operations-playbooks.md` = 17,928 tokens). A multi-domain hub agent that preloads 4-6 packs + PRINCIPLES naturally lands in the 20-30k range. M50 tier-discipline ("only declare a pack as Tier 1 if it's needed on >50% of invocations") holds — the issue is that the absolute spec was written before the pack ecosystem grew.

### Revised caps

| Cap | Tokens | Rationale |
|---|---:|---|
| **Nominal cap** | **≤ 20,000 tokens** | ≈ p75 of measured distribution. ~75% of agents are at or under this without intervention. Going above requires either (a) sustained M50 tier-discipline review, or (b) a documented variance case below. |
| **Hard cap** | **≤ 35,000 tokens** | ≈ p95 of measured distribution. Above this, the agent's spawn cost meaningfully degrades parallel-pattern budgets and forces the caller to pay context tax even for trivial tasks. Hard cap can only be exceeded with explicit `chief-architect` approval recorded in a DR. |

### Measure-before-author (pre-authoring discipline)

**MEASURE the owning agent's Tier-1 headroom BEFORE authoring new capability into its packs.** If the agent is already at or over the 20k nominal cap (or the new content would push it there), route the content to a NEW conditional (Tier-2) pack instead of appending it to a Tier-1 preload — this keeps Tier-1 flat and preserves hard-cap headroom. Appending to an already-heavy Tier-1 preload is how agents silently creep toward the 35k hard cap. Measure with tiktoken (cl100k) against the agent's deduped `inherits_principles` + `preload_knowledge_packs` before writing. This is a general D14 authoring discipline (not enrichment-only): it applies to any run that adds capability content to an agent's packs.

> *Relocated 2026-08-15 (DR-2026-262): measure-before-author precedent (Capability Embed 2026-07-13, history; the discipline itself is stated above and stays) — full text in the companion agent-metadata-schema.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

### Variance cases (when nominal cap can be exceeded without rework)

The following variance cases preserve the original D14 spirit while reflecting reality:

- **(a) Regulatory-density domain** — the agent operates in a regulated domain (legal, compliance, HR-AI, privacy, IP) where the regulatory landscape itself is dense and unavoidable. Example: `compliance-officer` (36,076 tokens — FCRA + EU AI Act + NIST + state laws + frameworks).
- **(b) Multi-specialist hub** — the agent coordinates 3+ specialists across different sub-domains and needs preloaded context spanning each (M&A, operations, cloud, customer-success-ops, executive). Example: `head-corpdev` (42,515 — M&A patterns + due diligence + valuation + integration).
- **(c) Cross-domain executive role** — the agent's accountability surface spans multiple functional domains by design (COO, CHRO at exec level). Example: `coo` (41,958 — operations playbooks + process + program + supply chain).
- **(d) Operational-knowledge density** — the agent's daily workflow requires deep operational pattern libraries (incident response, playbooks, runbooks). Example: `cs-ops` (44,222 — incident response + customer success ops + automation + data-tooling).

Variance cases (a)-(d) MUST be declared in the agent's SKILL.md frontmatter under `metadata.tier1_variance_rationale` (free-text 1-2 sentences citing the case letter). Without an explicit declaration, an agent over the nominal cap is in violation and the next M50 review will retier the heaviest packs to Tier 2 (conditional).

> *Relocated 2026-08-15 (DR-2026-262): over-nominal-cap agent list, 2026-05-18 baseline (point-in-time measurement; the caps and variance-declaration requirement above are the binding text) — full list in the companion agent-metadata-schema.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

### Measurement methodology

Token counts measured via `tiktoken` library, `cl100k_base` encoding (Claude/GPT-4 family tokenizer; the closest publicly-available proxy for actual Anthropic API tokens). Actual Anthropic counts may differ ±5-10% from tiktoken estimates. Reproducible via:

```bash
run the metadata validation helper
```

The script enumerates all Product Org OS and Extension Team knowledge packs and all `skill_type: agent` SKILL.md files, parses `metadata.preload_knowledge_packs` and `metadata.inherits_principles`, resolves each entry to a file via the 3-shape resolution chain (defined in the spawn template at `../harness/pbaw/spawn-template.md` — the §2 payload, governed by `agent-spawn-protocol.md` §2), and sums Tier-1 tokens per agent. Output: `d14-measurement-YYYY-MM-DD.{md,json}`.

Re-run on every quarterly refresh to detect Tier-1 growth and trigger M50 retiering before agents creep over the hard cap.

---

## Enforcement

- the metadata update helper applies schema uniformly (dry-run mode available)
- the metadata validation helper validates metadata ↔ body prose consistency
- the body-section generation helper creates starter body sections from mapping data
