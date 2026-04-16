# AI-Agent Readiness Rubric — Design Systems & Component Libraries

## Overview

This knowledge pack defines a reusable 1-5 rubric for scoring a design system, component library, or token catalog against a single question: **can an AI agent consume this system and produce correct-by-construction output, or does it have to guess?**

The rubric has four dimensions. Each dimension is scored independently on a 1-5 scale with explicit anchors. Scores are aggregated to produce an overall readiness number, but the per-dimension scores matter more than the aggregate — a strong aggregate that hides a structurally weak dimension (especially machine-readable docs) is a false positive.

This rubric is the shared source of truth for:
- `/figma-agent-brief` — uses it for library-readiness gate before producing an agent-ready Figma brief
- `/generative-ui-spec` — uses it for runtime-consumption feasibility before producing a CopilotKit spec
- (Future) `/design-system-audit` — will consume this rubric as its core scoring mechanism
- Any future Extension Team skill that needs to know whether a target system is agent-consumable

The rubric is reusable across teams. The Design Team authored it, the Design Team owns it, but any team working against a design system (Frontend Dev, UI Designer, Visual Designer, Interaction Designer, AI Architect for runtime questions) can run it and cite its score.

**Owner**: 🎨 Visual Designer (Design Team, Extension)
**Consumers**: `/figma-agent-brief`, `/generative-ui-spec`, future `/design-system-audit`, Frontend Dev team, UI Designer skills
**Source of record**: This file.
**Evergreen vs dated**: The rubric itself is evergreen. Tool-specific references (CopilotKit, Figma Make, W3C DTCG, Zod) are dated and live in a separate appendix with a forced 6-month re-review calendar note.

---

## The Rubric

Score each of the four dimensions independently, then compute an aggregate.

| Score | Typed props | Variant coverage | Machine-readable docs | Token exposure |
|---|---|---|---|---|
| **1** | Absent — no prop types documented; components are "drop in and hope" | Absent — no variants listed, or only "primary" mentioned implicitly | Absent — no schemas, no structured prop tables, narrative only | Absent — no named tokens, colors and spacing are hardcoded |
| **2** | Narrative only — prose describes props but no structured table | Narrative only — variants mentioned in prose, not enumerated | Narrative with examples — markdown tables but no schema contract | Tokens named in prose but not cataloged |
| **3** | Partial structured — prop tables exist for some components, manual annotation, no enforcement | Common variants listed in tables; edge cases (loading, empty, error) missing or inconsistent | Human-readable tables with columns for prop/type/default/description, but no JSON Schema, OpenAPI, or equivalent | Tokens named and cataloged in tables, naming conventions documented, but not programmatically consumable |
| **4** | Most components have complete typed prop schemas, a few gaps | Exhaustive for primary components (states + sizes + contexts), mostly covered for secondary | Tables are parseable but not formally schematized; easy to convert | Tokens exposed via one channel (CSS vars OR JSON OR TS types), not all three |
| **5** | Complete typed prop schemas per component, enforced via TypeScript / Zod / JSON Schema | Exhaustive — every state, size, theme, and context combination enumerated, including empty/loading/error/disabled/focus | Machine-consumable schema (JSON Schema, OpenAPI, or equivalent) co-located with narrative docs; an LLM can parse the spec directly | Tokens exposed via ALL of: CSS custom properties, JSON output, TypeScript types, and design-tool integration (Figma variables or equivalent) |

---

## The Four Dimensions Explained

### Dimension 1 — Typed Props

**What it measures**: whether component props have explicit, narrow, machine-readable types. Can an AI agent pick a valid value for any prop without guessing?

**What "typed" means in this rubric**:
- TypeScript interfaces with literal unions (not `string`, not `any`)
- Zod schemas with runtime validators
- JSON Schema with enumerated values
- Any equivalent that produces a machine-readable contract an AI agent or build tool can consume

**What does not count**:
- Prose descriptions of props ("variant: enum of primary, secondary")
- Markdown tables with a "Type" column containing narrative values ("enum")
- PropTypes / runtime type checks without a schema export
- Comments in code

**Score anchors**:
- **1**: No prop types documented anywhere. Consumers infer from source.
- **2**: Prose descriptions of props exist, no structured table or schema.
- **3**: Structured prop tables exist in markdown with prop/type/default/description columns. Human-readable, not machine-consumable.
- **4**: Most components have TypeScript interfaces or equivalent machine contracts; a few gaps (legacy components, new additions not yet typed).
- **5**: Every component has a complete typed contract enforced by TypeScript / Zod / JSON Schema. Build fails on untyped additions.

**How an agent uses this dimension**: At Score 4+ the agent reads the typed contract, picks a value from the enumerated set, and produces output that is valid against the contract. At Score 3 the agent parses the markdown table and guesses whether "enum" means a literal union or free-form string — error rate ~20%. At Score 2 or below the agent has no reliable contract and generates plausible-looking but frequently-wrong output — error rate ~50%.

### Dimension 2 — Variant Coverage

**What it measures**: whether components explicitly declare every state, size, theme, and context variant they support. Can an AI agent enumerate the valid combinations without inventing ones that don't exist?

**What "exhaustive variant coverage" means**:
- Every interactive component has the required states documented: default, hover, focus, pressed, disabled, loading, error, empty
- Every component that renders at multiple sizes documents its size enum
- Every component that supports theming documents its theme variants (light, dark, high-contrast)
- Every component that carries semantic weight documents its tone/intent variants
- The variant axes are named and orthogonal, not implicit

**What does not count**:
- "We have primary and secondary buttons" in prose
- A Storybook with rendered variants but no schema declaring them
- A Figma page with variant names but no machine-readable export

**Score anchors**:
- **1**: No variants listed. Components are single-state.
- **2**: Variants mentioned in prose (e.g., "supports primary, secondary, tertiary"). Not enumerated formally.
- **3**: Common variants listed in tables. Edge cases (loading, empty, error) missing or inconsistent across components.
- **4**: Exhaustive coverage for primary components (buttons, inputs, cards). Secondary components (tooltips, popovers, toasts) mostly covered.
- **5**: Every component declares every axis × value combination. State taxonomy is enforced by tooling — a component without a variant declaration block does not merge.

**State coverage sub-checklist** (used to score at Score 4+):

| State | Required for | Must be in declaration |
|-------|-------------|------------------------|
| default | Every component | Yes |
| hover | Any pointer-interactive component | Yes |
| focus | Any interactive component (a11y mandate) | Yes |
| pressed | Any click/tap component | Yes |
| disabled | Any blockable component | Yes |
| loading | Any async-triggering or async-data component | Yes |
| error | Any component with validation or failure modes | Yes |
| empty | Any collection-rendering component | Yes |
| skeleton | Above-the-fold async-data components | Recommended |
| read-only | Form controls in non-editable contexts | Optional |

**How an agent uses this dimension**: At Score 4+ the agent knows every state it must emit output for and never misses the loading/empty/error cases that are the usual failure modes of generated UI. At Score 3 the agent handles the happy path and misses edge cases ~40% of the time. At Score 2 or below the agent produces single-state output and humans discover the missing states in QA.

### Dimension 3 — Machine-Readable Docs

**What it measures**: whether the documentation itself is consumable by machines, not just humans. Is there a JSON Schema for components, a DTCG JSON for tokens, a structured declaration block for variants — or is everything in prose and markdown tables?

**This is the structurally load-bearing dimension.** The other three dimensions become agent-consumable *only when machine-readable docs are present to carry them*. A library that scores 5 on typed props but 2 on machine-readable docs has the information the agent needs but not in a form the agent can read. The agent has to parse TypeScript source files directly, which is fragile. The correct pattern is: typed contracts *published as* machine-readable artifacts.

**What "machine-readable" means**:
- W3C Design Tokens Community Group (DTCG) JSON for tokens
- JSON Schema for component props
- YAML or JSON variant declaration blocks
- ARIA contracts and keyboard maps in JSON
- Auto-generated narrative docs co-located with the machine contract

**What does not count**:
- Markdown tables, no matter how well-structured
- Prose descriptions of token architecture
- A Storybook docs page (good for humans, not a machine contract)
- A README with examples

**Score anchors**:
- **1**: No schemas of any kind. Narrative only. Read the source.
- **2**: Narrative with examples. Markdown tables exist but no schema contract.
- **3**: Human-readable tables with columns for prop/type/default/description. No formal schema.
- **4**: Tables are parseable (consistent column structure, no prose in type cells) and easy to convert to a formal schema.
- **5**: Machine-consumable schema (JSON Schema / OpenAPI / DTCG JSON) co-located with narrative docs. An LLM can parse the spec directly without touching prose.

**How an agent uses this dimension**: At Score 5 the agent reads the JSON Schema and generates valid output directly. At Score 4 the agent parses the markdown tables and produces output with minor inaccuracies on types. At Score 3 the agent has enough information to try and enough ambiguity to fail. At Score 2 or below the agent treats the docs as natural language and produces pattern-matched output.

**Below Score 3 = NOT AI-ready, regardless of aggregate.** This dimension is structurally load-bearing for the others. A library that scores 5/5/2/5 is not AI-ready because nothing is actually machine-readable. Flag it explicitly.

### Dimension 4 — Token Exposure

**What it measures**: whether design tokens are published across multiple runtime channels (CSS vars + JSON + TypeScript types + design-tool integration) from a single source of truth, so that any consumer — human designer in Figma, engineer in TypeScript, build tool consuming JSON, AI agent reading a schema — can use them without hand-translation.

**The four channels**:

| Channel | Format | Primary consumer |
|---------|--------|------------------|
| Runtime CSS | CSS custom properties | Browsers, runtime theming |
| Tooling JSON | W3C DTCG JSON | Build tools, codegen, AI agents |
| Strongly-typed | TypeScript types / enums | TS consumers, compile-time checks |
| Design tool | Figma Variables, Sketch Libraries | Designers producing specs |

**Score anchors**:
- **1**: No named tokens. Colors and spacing are hardcoded in components.
- **2**: Tokens named in prose or in code comments. Not cataloged centrally.
- **3**: Tokens named, cataloged in tables, naming conventions documented. Not programmatically consumable — the catalog is a markdown file.
- **4**: Tokens exposed via ONE runtime channel (CSS vars OR JSON OR TS types). Other channels absent or manually maintained (drift guaranteed).
- **5**: Tokens exposed via ALL of: CSS custom properties, JSON output (DTCG format), TypeScript types, AND design-tool integration (Figma Variables or equivalent). Generated from a single source of truth; round-trip where possible.

**How an agent uses this dimension**: At Score 5 the agent emits output that uses the active theme's tokens correctly on any channel the consumer happens to use. At Score 4 the agent uses the one available channel and produces output that works for that channel but drifts from the others. At Score 3 the agent knows the token names but cannot reference them programmatically and produces output that uses the values literally (breaking theming). At Score 2 or below the agent hardcodes values.

**Token exposure is the cheapest dimension to fix.** Style Dictionary, Theo, and the W3C DTCG reference transformers exist exactly to solve the multi-channel problem. A team that commits DTCG JSON as source-of-truth and runs it through Style Dictionary gets Scores 4-5 on this dimension for minimal engineering cost.

---

## Running the Rubric

### Setup

Before running the rubric, identify:
- **The library under audit**: file path or URL to the design system's documentation home
- **The auditor**: a named agent (UI Designer, Visual Designer, or Interaction Designer are the typical ones)
- **The consumer context**: which agent skill will consume the library (the answer determines which dimensions matter most)
- **The baseline, if any**: previous audits of the same library, so scores can be compared over time

### Per-Dimension Scoring Procedure

For each of the four dimensions:

1. **Locate the evidence in the library**. Dimension 1 evidence is prop tables, TypeScript interfaces, Zod schemas. Dimension 2 evidence is variant declarations, state listings, Storybook variant pages. Dimension 3 evidence is the file format of the documentation itself. Dimension 4 evidence is the token publication pipeline.
2. **Match the evidence to the score anchor.** Be strict — a score of 3 means the score anchor is met in full, not partially. If evidence is partial, score down.
3. **Record the evidence with a direct quote or pointer.** The audit must be reproducible — a later reader should be able to verify the score by looking at the same evidence.
4. **Record the gap to the next score.** What would need to change to raise this dimension by one point?

### Aggregate Calculation

```
Aggregate = (Typed props + Variant coverage + Machine-readable docs + Token exposure) / 4
```

Round the aggregate to two decimal places for the record, to one decimal place for discussion, and to the nearest integer only when a single number is required. The spread of dimension scores is more informative than the aggregate.

### Interpretation

| Aggregate | Per-dimension minimum | Interpretation |
|-----------|----------------------|----------------|
| ≥ 4.0 | ≥ 3 on every dimension | AI-ready. Downstream skills can consume directly. |
| 3.0 - 3.9 | ≥ 3 on every dimension | Human-useful, agent-marginal. Downstream skills can consume with adapter work. |
| 3.0 - 3.9 | < 3 on any dimension | NOT AI-ready. The weak dimension gates the others. Fix before agent consumption. |
| 2.5 - 2.9 | — | Human-useful at best. Downstream agent consumption blocked. |
| < 2.5 | — | Not AI-ready. Needs foundation work before any agent skill should touch it. |

### The 3/5 Threshold Rationale

**Why score 3 is the threshold for "an AI agent can do something useful"**:

- Below 3, the documentation is narrative-only. An agent consuming it is pattern-matching over prose, not reading a contract. Output quality is "plausible-looking JSX" not "valid-against-contract JSX." Error rates are high and failures are silent.
- At 3, the documentation has enough structure that the agent can extract information with effort. An agent consuming a Score-3 library produces output that is mostly right with known edge cases (loading, empty, error states missed frequently; prop type ambiguity handled case-by-case).
- At 4, the structure is machine-friendly even if not formally schematized. An agent produces output that is correct-by-construction on the happy path with minor inaccuracies on edge cases.
- At 5, the structure is formal. Output is correct-by-construction, period. Errors happen at the taste/judgment layer, not the contract layer.

**The load-bearing rule**: *Below 3 on the machine-readable-docs dimension, a library is NOT AI-ready regardless of aggregate.* This dimension structurally gates the others. A library with typed props, variant coverage, and tokens at Score 5 but machine-readable docs at Score 2 has all the right information in a form the agent cannot read. The agent has to parse TypeScript source directly, which is fragile and breaks on refactors.

Flag this case explicitly in every audit: "Aggregate is X, but machine-readable-docs is Y which is below the threshold. Library is NOT AI-ready until docs are upgraded."

### Re-Audit Cadence

- **Minor version bump** (new components added, no contract changes): no re-audit required.
- **Major refactor** (new variant taxonomy, new token architecture, new schema format): re-audit required.
- **Quarterly review** (no trigger): optional, useful for trend tracking.
- **Before any new agent skill consumes the library**: required. The library might have drifted since the last audit.

---

## Library-Readiness Precondition Pattern

This pattern is the reason the rubric exists. Agent skills that consume a design system should publish an explicit precondition: *before I do this work, I require the library to meet these criteria*. If the library does not meet the criteria, the skill stops and reports rather than silently producing lower-quality output.

### How a Skill Declares Its Precondition

In the skill's SKILL.md frontmatter or documentation, include a block like:

```yaml
library_readiness_precondition:
  min_aggregate: 4.0
  min_per_dimension:
    typed_props: 4
    variant_coverage: 4
    machine_readable_docs: 4
    token_exposure: 3  # optional — skill does not need design-tool integration
  on_fail: stop_and_report  # or "degrade_to_fallback" with explicit fallback pattern
```

The skill's entry-point code reads the library's self-score from `ai-agent-readiness-rubric.md` in the target project OR runs the rubric against the library if no self-score exists. If any dimension is below the minimum, the skill stops and emits a structured error naming the failing dimension and the gap.

### Why `stop_and_report` Is The Default

The alternative is `degrade_to_fallback` — the skill produces a lower-fidelity output when the library is not agent-ready. This is sometimes the right choice (the user might not care about contract correctness for a throwaway prototype), but it should be an explicit opt-in, not a silent default.

The failure mode of silent degradation is worse than the failure mode of stop-and-report: silent degradation produces output that looks correct, gets shipped, and causes bugs downstream. Stop-and-report produces no output and a clear explanation, which the user acts on immediately.

### Example: `/figma-agent-brief`

The `/figma-agent-brief` skill produces an agent-ready Figma brief that downstream Figma Make pipelines consume. Its precondition:

```yaml
library_readiness_precondition:
  min_aggregate: 4.0
  min_per_dimension:
    typed_props: 4
    variant_coverage: 4
    machine_readable_docs: 4
    token_exposure: 4
  on_fail: stop_and_report
```

When invoked against a library at Score 2.75, the skill stops and emits:

> "Cannot produce agent-ready brief. Target library scores 2.75 aggregate (3/3/2/3 per dimension). Machine-readable-docs dimension is below the 4 threshold. Upgrade the library to formal schema (JSON Schema for props, DTCG JSON for tokens) before running this skill."

### Example: `/generative-ui-spec`

The `/generative-ui-spec` skill produces a CopilotKit Presentational runtime spec. Its precondition:

```yaml
library_readiness_precondition:
  min_aggregate: 4.0
  min_per_dimension:
    typed_props: 5   # CopilotKit needs Zod / strict TS types
    variant_coverage: 4
    machine_readable_docs: 4
    token_exposure: 3   # runtime CSS vars sufficient
  on_fail: stop_and_report
```

The typed-props requirement is stricter because CopilotKit's runtime validator needs actual Zod schemas or TypeScript types, not markdown tables.

---

## Integration Points

### Current consumers (as of April 2026)

| Skill | Dimension focus | Purpose |
|-------|-----------------|---------|
| `/figma-agent-brief` | All four, ≥4 | Agent-ready Figma brief for pipelines |
| `/generative-ui-spec` | Typed props ≥5, others ≥4 | CopilotKit runtime binding spec |
| `/design-system-audit` (future) | All four | Score any design system against this rubric, produce an audit report |

### Potential future consumers

- `/design-token-migration` — consumes Score 4+ libraries, produces migration plans from legacy CSS-only tokens to DTCG JSON
- `/component-contract-generator` — consumes typed props at Score 4+, produces Zod schemas from TypeScript types
- `/variant-completeness-check` — consumes variant coverage at Score 3+, produces a gap report
- `/design-system-ai-grade` — consumes all dimensions, produces a badge (similar to a test coverage badge) that lives in the library's README

### Teams that run this rubric

- **Design Team** — authors and owns the rubric; runs it against Design Team-managed libraries
- **Frontend Dev Team** — runs it against libraries the team consumes, to decide whether to adopt as-is or wrap in an adapter layer
- **Architecture Team** (AI Architect in particular) — runs it as part of AI-native stack feasibility assessments
- **UX Lead / Interaction Designer** — runs it when evaluating external design systems for potential adoption

Any future Extension Team that introduces AI-driven component consumption patterns should consult this rubric before declaring its library dependency.

---

## Limitations

- **The rubric measures contract readiness, not design quality.** A library can score 5/5/5/5 and still be ugly, inconsistent, or poorly thought-out. The rubric is necessary, not sufficient, for good design system outcomes.
- **The rubric assumes the library exists.** Running it against an early-stage system that is still converging is premature. Wait until the library has ≥10 components and a stable token architecture before scoring.
- **The rubric is pattern-specific.** It is optimized for component libraries consumed at runtime or build time. It does not score icon libraries, illustration systems, or motion libraries cleanly — those need their own rubrics (future work).
- **The 3/5 threshold is empirical, not theoretical.** It is based on observed failure rates of AI-agent consumption of libraries at each score level as of April 2026. If agent capabilities shift materially — better at parsing prose, better at handling ambiguity — the threshold may move. Re-evaluate annually.

---

## Sources

- `Extension Teams/design-team/design-system-ai-readiness-audit.md` — the Week-1 audit of the Design Systems knowledge pack that produced this rubric as an extractable artifact. The per-dimension and aggregate scores in that audit are the worked example for how the rubric is applied.
- `Extension Teams/design-team/figma-agent-probe-notes.md` — the Week-1 probe of Figma Make's library-awareness behavior, which motivated the `stop_and_report` precondition pattern.
- `Extension Teams/reference/knowledge/design-systems.md` — the foundation + AI-readiness layer pack that cites this rubric as its scoring framework.

---

## Re-Review Calendar Note

This rubric's evergreen principles (the 1-5 anchors, the four dimensions, the 3/5 threshold rationale, the library-readiness precondition pattern) are stable and should not change on short timescales. They survive tool churn.

The integration-points section (which specific skills consume the rubric) and any tool-specific references (CopilotKit, W3C DTCG, Style Dictionary, Figma Make) are dated and should be re-reviewed **every six months**.

**Next forced re-review: October 2026.**

When re-reviewing:
- Remove skills that have been deprecated or archived
- Add new skills that have adopted the precondition pattern
- Update any tool names that have been renamed, superseded, or discontinued
- Re-examine the 3/5 threshold against observed agent-capability shifts over the prior 6 months
- Update this date to the next 6-month window

Pin this re-review to the quarterly skill-health script so it cannot be silently skipped.
