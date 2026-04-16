---
name: figma-agent-brief
description: Generate structured Figma AI briefs with library-readiness preconditions and explicit out-of-scope boundaries
argument-hint: --surface NAME --library NAME [--readiness-score FILE] [--intent FILE]
metadata:
  skill_type: task-capability
  owner: ui-designer
  primary_consumers:
  - ext-design
  - generative-ui-spec
  sensitive: false
co_owner: interaction-designer
experimental: true
experimental_last_validated: 2026-04-11
---
# /figma-agent-brief

## Experimental Banner (ALWAYS display at top of every output)

> **EXPERIMENTAL SKILL.** This skill is a brief-structuring tool for Figma AI (Figma Make, Figma MCP, and sidebar AI actions). Figma AI agent surface area was last validated on **2026-04-11**. Figma is shipping changes quarterly. **Verify current Figma AI behavior before relying on any output from this skill.** If more than 90 days have passed since `experimental_last_validated`, treat the output as stale and re-run the Week-1 probe before use.

## Purpose

This skill structures a brief that **increases the probability** Figma AI (primarily Figma Make, secondarily sidebar AI actions) produces something useful on the first attempt. It does not generate design. It does not replace a designer. It does not invoke Figma AI programmatically. It produces a human-readable brief that a PM hands to a designer (or pastes into a Figma Make session) to get a higher-quality first scaffold.

The honest framing: Figma AI in Q1 2026 is a **library-awareness-dependent, card-granularity-reliable, brand-voice-unaware** tool. This skill makes the brief match what Figma AI can consume and explicitly fences off what it cannot.

## When to use

- Briefing Figma Make or Figma's sidebar AI for a **card-, section-, or single-screen-sized** surface
- The consuming team has a **mature, linked design system library** (see precondition below)
- You want the first Figma AI scaffold to use the right library components, the right variants, and the right states without hand-correction
- You need to hand the brief to a human designer (the normal case) and want the scope boundaries explicit

## When NOT to use

- Full product redesigns or multi-screen flows (scope too large; Figma AI scaffolds one surface at a time)
- Brand refreshes (brand voice is out of scope for Figma AI)
- Interaction flows, state machines, or prototypes (Figma Make emits static frames only)
- Design systems with AI-readiness score <3/5 on typed props or variant coverage (the brief has nothing to anchor against)
- Content-driven surfaces where editorial voice is load-bearing (e.g. story blocks, long-form editorial, brand manifesto pages)
- Edge-state work (Figma AI generates happy-path only; a skilled designer is required for the rest)
- Accessibility audits (sidebar AI can rename layers but cannot reason about ARIA, focus order, or screen-reader semantics)

## Required inputs

| Input | What |
|---|---|
| Target surface | Exactly one: single component, section, or screen. Reject multi-screen requests. |
| Library reference | Name of the linked Figma library the surface will be built against. Must be a real library the consuming team uses. |
| Content structure | Hierarchical information map (headings, sub-items, data fields) — NOT narrative copy |
| Variant requirements | Explicit list of variants to generate: default + any of hover, focus, error, loading, empty, skeleton, disabled, expanded |

## Optional inputs

| Input | Purpose |
|---|---|
| `--readiness-score FILE` | Path to the design-system AI-readiness audit (output of `design-system-ai-readiness-audit.md`). Enables the precondition check. |
| `--intent FILE` | Path to a PM intent doc or product brief. Used to derive surface and content structure automatically. |
| Prior Figma drafts | Existing Figma frames or screenshots. Figma AI cannot read them through this skill, but the human designer can. |
| Brand voice notes | Documented for the human designer. **Figma AI will ignore these** — they exist only as hand-off context. |

## Library-readiness precondition check (BLOCKING)

Before producing a brief, the skill checks the consuming team's design system AI-readiness.

**Required minimum**: ≥3/5 on **typed props** AND ≥3/5 on **variant coverage** (from `design-system-ai-readiness-audit.md`).

**If `--readiness-score` is provided**:
- Read the audit file. Extract typed-props score and variant-coverage score.
- If either <3/5: output a blocking warning, refuse to produce the brief, and point the user to `design-system-ai-readiness-audit.md` to improve the library first.
- If both ≥3/5: proceed.

**If `--readiness-score` is NOT provided**:
- Prompt the PM: "This skill requires a design system AI-readiness score of ≥3/5 on typed props and variant coverage. Have you run `/design-system-ai-readiness-audit`? [yes / no / don't know]"
- If "no" or "don't know": display the blocking warning anyway, produce the brief with a header caveat ("⚠️ Library readiness unverified — output may be unusable against an immature library"), and log the unverified state.
- If "yes": proceed.

The blocking warning is non-negotiable because without library readiness, the brief points to components that don't exist, and Figma Make silently substitutes primitives. The PM gets a scaffold that looks plausible and is wrong — the exact false-confidence failure mode this skill is meant to prevent.

## Method

### Step 1 — Read the intent and classify the surface

Read `--intent` (if provided) or prompt the PM for the surface. Classify it as one of:

- **Component** (single atomic element: button, card, badge)
- **Section** (a grouped region within a screen: hero, data table, comparison block)
- **Screen** (a full viewport surface: product page, dashboard, settings)
- **Flow** (multiple screens) → **REJECT**. Flows are out of scope. Redirect to a human designer.

Write the surface classification at the top of the brief.

### Step 2 — Run the library-readiness precondition

Per the precondition check above. If blocked, stop here and produce only the warning output. If unverified, proceed with the caveat header.

### Step 3 — Identify library components available for the surface

Name each library component the brief will reference **by its exact library name**, not by description.

- ✅ `ScoreCard/variant=trend-up`
- ❌ "a card showing the score with an upward trend"

If you (as the skill) don't know the library's component names: prompt the PM to supply them OR delegate to a human designer who has library access. Do not guess — guessed names will silently miss in Figma Make and fall through to primitives.

### Step 4 — Structure the content hierarchy (info, not copy)

Produce a hierarchical outline of the information the surface must display. This is structural, not narrative.

- ✅ `Title > Score (number) > Trend indicator (up/down/flat) > Timestamp > CTA to details`
- ❌ `"A prominent header saying 'Your Risk Score' with a big number showing..."`

Narrative copy is brand voice work. Figma AI cannot reason about it. Defer to the "Out of scope" section.

### Step 5 — Enumerate required variants

Enumerate every variant the surface must support. Include default plus all applicable states:

- `default`
- `hover` (if interactive)
- `focus` (if keyboard-navigable)
- `error` (if can fail)
- `loading` (if async)
- `empty` (if can have no data)
- `skeleton` (if has loading shimmer pattern)
- `disabled` (if can be disabled)
- `expanded` (if collapsible)

Figma Make generates happy-path only unless each variant is named. **Listing variants is the single highest-leverage thing this brief does.**

### Step 6 — Write the explicit out-of-scope section and hand-off to human designer

Every brief ends with an **Out of scope for Figma AI — human designer required** section. Never omit. Never implicit. Always explicit. See the template below.

## Output structure (the brief itself)

The skill produces a brief as a markdown document with this exact structure:

```markdown
# Figma AI Brief — {Surface Name}

{experimental banner}

## 1. Surface Definition
- **Classification**: {component | section | screen}
- **Target viewport**: {desktop | tablet | mobile | multi} + {breakpoints}
- **One-line description**: {what this surface is, in 15 words or fewer}

## 2. Library Reference
- **Linked library**: {library name}
- **AI-readiness status**: {verified ≥3/5 | unverified | blocked}

## 3. Library Component Inventory
Components the brief expects Figma AI to pull from the linked library.

| Component | Exact library name | Why it's needed |
|---|---|---|
| {role} | {LibraryNamespace/ComponentName/variant=X} | {purpose} |

## 4. Content Structure
Hierarchical information outline. Structural, not narrative.

- {top-level info block}
  - {sub-item}
    - {data field: type}
  - {sub-item}
    - {data field: type}

## 5. Variant List
Every variant the surface must support. Named and defined.

- **default** — {when shown}
- **hover** — {when shown}
- **focus** — {when shown}
- **error** — {when shown + what the error communicates}
- **loading** — {when shown}
- **empty** — {when shown + what empty communicates}
- **skeleton** — {when shown}
- **disabled** — {when shown}
- ... (only the applicable ones)

## 6. Responsive Considerations
- **Primary breakpoint**: {px range + rationale}
- **Secondary breakpoint** (if applicable): {px range + what changes}
- **Mobile collapse pattern** (if applicable): {e.g. "stacked with tabs below 600px"}

## 7. Out of Scope for Figma AI — Human Designer Required
The following are NOT covered by this brief and must be handled by the human designer (NOT by Figma Make, NOT by sidebar AI, NOT by Figma MCP):

- [ ] **Brand voice / editorial copy** — Figma AI defaults to neutral-corporate. All real copy must be written by a human with brand-voice context.
- [ ] **Motion and animation** — Figma Make produces static frames only. Transitions, streaming, hover animations, micro-interactions → motion spec, not this brief.
- [ ] **Edge states beyond the listed variants** — If the product has exotic states (e.g. "rate-limited," "mid-migration," "feature-flagged off"), human designer.
- [ ] **Accessibility semantics** — ARIA roles, focus order, screen-reader labels, reduced-motion behavior, color-contrast validation. Not generated by Figma AI.
- [ ] **Data-visualization semantics** — Sparklines, charts, graphs are decorative placeholders in Figma AI output. Real viz requires a designer who understands the data shape.
- [ ] **Product photography and illustration** — Figma AI emits placeholder images. Photo direction, illustration style, and asset sourcing are out of scope.
- [ ] **Interaction logic** — Click flows, state machines, multi-step forms. Prototype layer, not Figma Make.
- [ ] **Multi-surface consistency** — Ensuring this surface aligns with sibling surfaces across the product. Requires a design-system skill, not a single-surface brief.

## 8. Hand-off Instructions for the Human Designer
1. Review this brief end-to-end before opening Figma.
2. Open a Figma Make session with the linked library active.
3. Paste the "Surface Definition + Library Component Inventory + Content Structure + Variant List" sections into Figma Make's prompt field.
4. Generate the first scaffold.
5. Validate against the Quality Gates below (Section 9 of this SKILL.md).
6. Hand-edit everything in Section 7 "Out of Scope." This is the real design work.
7. Route to `/generative-ui-spec` if this surface also needs runtime rendering specification.
```

## Quality gates (8 checks applied to every brief before publication)

1. **Library readiness ≥3/5** on typed props AND variant coverage (or unverified-warning header present)
2. **Target surface is component, section, or screen** — not a flow, not a multi-screen redesign
3. **Content structure is hierarchical, not narrative** — no paragraphs of prose in the content structure section
4. **All applicable variants enumerated** — default + every state the surface can enter
5. **Out-of-scope section present and non-empty** — at least 5 items from the default list or their justified absence
6. **No brand voice or copy in the brief body** — brand voice belongs ONLY in the hand-off context for the designer, never in the Figma AI-facing fields
7. **No edge states in the main brief body** — edge states are explicitly deferred to the human designer
8. **Experimental banner present at the top of the output** — non-negotiable

If any gate fails, the skill blocks output and returns a numbered failure list.

## Out-of-scope defaults (NEVER in scope for this skill)

These are ALWAYS out of scope. Do not attempt to handle them with this skill even if the PM asks:

- Full product redesigns
- Brand voice and copywriting
- Edge-state design (beyond the enumerated variant list)
- Accessibility audits
- Interaction design (click flows, state machines)
- Content strategy
- Motion and animation
- Multi-surface consistency (use a design-system skill)
- Data-visualization semantics
- Product photography direction

If the PM's request crosses into any of these, redirect: "This is out of scope for `/figma-agent-brief`. Route to {appropriate specialist / skill}."

## Related skills and hand-off

| Direction | Skill / agent | Relationship |
|---|---|---|
| Input | `design-system-ai-readiness-audit.md` | Provides the readiness score this skill requires |
| Input | PM intent doc | Source of the surface description and content structure |
| Output feeds | `/generative-ui-spec` | When the briefed surface is a component family that also needs runtime rendering spec |
| Output feeds | `@interaction-designer` (consultation) | For variant enumeration discipline — "did I miss a state?" |
| Output feeds | `@visual-designer` (consultation) | For library-readiness assessment when the PM doesn't have a score |
| Hand-off | Human UI designer | Everything in the "Out of scope" section — brand voice, motion, edge states, accessibility, photography, interaction logic, multi-surface consistency |

## Delegation pattern

Default: **Pattern 1 Consultation** (from `delegation-protocol.md`).

Typical consultations:
- `@interaction-designer` for variant enumeration discipline on surfaces with complex state machines
- `@visual-designer` for library-readiness sanity-check when the audit doesn't exist

This skill does NOT use Pattern 4 Debate or Pattern 5 Adversarial Review. There is no genuine tradeoff to debate, and the output is not adversarial-review-worthy (low liability, experimental status, reversible).

## Maintenance cadence

**Quarterly re-review.** Figma AI is shipping changes every ~quarter. `experimental_last_validated` must be updated at each re-review.

**90-day staleness flag.** If more than 90 days have passed since `experimental_last_validated`, the experimental banner escalates to a stale warning and the skill prompts the user to re-run the Week-1 Figma agent probe before producing output. The stale warning is non-blocking but visible.

**Sunset on any Figma AI major release.** If Figma ships a major Figma Make / MCP reverse-direction / sidebar AI overhaul, this skill must be rewritten, not patched. The probe notes should be re-run from scratch.

## Birth test

This skill's first real output is a brief for the **AXIA risk-dashboard alert detail card**, saved at `AXIA/Product/figma-agent-brief-birth-test-alert-detail-card-2026-04-11.md`. The birth test exercises:

- Surface classification (component, not screen)
- Library component inventory (with exact names where known)
- Content structure (risk score + evidence chain, hierarchical)
- Variant list (default, hover, expanded, loading, error, empty)
- Out-of-scope section (brand voice, motion on evidence-chain expansion, accessibility audit of color-coded severity, responsive collapse behavior)

If the birth test produces a brief a frontend dev could **independently** open and understand (without asking the PM for clarification), the consumability gate passes for Sub-phase 4C.3.

## ROI framing

Time saved on **drafting and triage** of a Figma AI brief (not on design work itself). Design blended rate: **$200/hr**. A thoughtful Figma AI brief takes a PM ~45-90 minutes to draft well from a blank page; this skill compresses that to ~15 minutes of structured fill-in, for ~30-60 minutes saved per brief.

Display format:
⏱️ ~[X] hrs saved on drafting and triage in [Y] min, [Z]k tkns ~$[C] cost, Value ~$[V]

Where Value = hours saved × $200/hr.
