---
name: generative-ui-spec
description: Generative UI spec for card-sized non-streaming components (implementation via CopilotKit) or streaming/flow patterns (principles-only).
argument-hint: --intent FILE [--runtime copilotkit|a2ui|auto] [--scope card|section|screen]
metadata:
  skill_type: task-capability
  owner: ui-designer
  primary_consumers:
  - ext-design
  - figma-agent-brief
  sensitive: false
co_owner: interaction-designer
experimental: true
experimental_last_validated: 2026-04-11
---
# /generative-ui-spec

> ⚠️ **EXPERIMENTAL.** This skill is experimental. Generative UI runtime last validated **2026-04-11** on CopilotKit Presentational (`useCopilotAction` with typed `render` and Zod parameter schemas). Verify current runtime behavior before relying on any output produced here. A2UI JSONL streaming is treated as **principles-only** — mid-stream failure semantics, out-of-order delta handling, and event return channels are not converged across implementations as of the validation date.

---

## Purpose and Scope

Generative UI in Q1 2026 splits cleanly into two worlds and this skill treats them differently. That is the whole point.

1. **CopilotKit Presentational** — stable enough for implementation today, scoped to card-sized, non-streaming components. The LLM emits a tool call, the SDK deserializes the arguments, Zod validates them against the schema, and a typed React component renders via a `render` function. This skill produces a full implementation-mode spec: component vocabulary, Zod schema draft, render contract (default / loading / error / empty / variants), event return spec, type-safety acknowledgment, test plan. A Frontend Developer can build from it without asking the PM follow-up questions.

2. **A2UI JSONL streaming (and streaming generative UI more broadly)** — pattern works for long-form text but is not stable at card granularity as of Q1 2026. Mid-stream failure handling, out-of-order delta semantics, event return channels, and rollback on failed-close are per-implementation. A PM spec produced for A2UI today would encode expectations the runtime cannot reliably meet, which is the worst failure mode: a spec that reads confident but produces unpredictable behavior. This skill therefore produces **principles-only** output for A2UI: component vocabulary, prop schema conventions, event contracts, migration path — NO runtime code, NO pretend-it's-implementation framing, NO claims of predictable behavior.

The skill picks mode from the `--runtime` flag or auto-detects from the intent input. If intent contains streaming, multi-step flow, or full-screen requirements, implementation mode is auto-rejected and the skill falls back to principles mode with a warning that names the specific triggering criterion.

**This is load-bearing honesty, not hedging.** The spike at `Product Org OS/reference/genui-spike-2026-W1.md` established that writing an implementation spec for an unstable runtime is worse than writing a principles spec for a mature one. An implementation spec carries an implicit promise: "build this and it will work predictably." A principles spec carries a different promise: "here is the vocabulary and the event model; when a runtime supports it reliably, here is the migration path." Principles mode is not a consolation prize. It is what the current state of the ecosystem supports for anything beyond a narrow CopilotKit slice, and it is the honest thing to hand to the Frontend Developer when the runtime is not ready.

---

## When to Use

- Card-sized AI-generated surfaces where the agent needs to render a typed component inline (task card, stat tile, notification, quick-action panel) → **implementation mode**
- Any streaming or flow-based generative UI requirement → **principles mode**
- New component vocabulary design for an agent product where the runtime is undecided → **either mode**, typically starting with principles
- When the Frontend Developer needs a spec that enumerates Zod schema, render states, and event contracts without ambiguity → **implementation mode**

## When NOT to Use

- **Full product redesigns or multi-screen user flows** — use traditional UX flow design. Generative UI is a surface inside an app, not a way to build an app.
- **Interaction flow design beyond event contracts** — use `@interaction-designer` directly. This skill defines event contracts for a single rendered component; it does not design flows that span multiple components, screens, or agent turns.
- **Brand voice, tone, or content strategy** — out of scope. The LLM emits content at runtime; this skill defines the shape the content fits into, not what the content says. Voice and tone belong to `@copywriter` or `@content-strategist`.
- **Accessibility audit** — out of scope. The spec MUST include ARIA, focus order, and screen-reader semantics fields in the render contract, but this skill does not audit an existing surface for compliance. For an audit, use a dedicated accessibility review.
- **Motion design or transitions** — use `@motion-designer`. The render contract may note "transitions out when dismissed," but motion timing and easing are a different craft.
- **Content strategy or copy direction** — use `@copywriter` or `@content-strategist`. The skill bounds the content shape (max lengths, enums) but does not write the content.
- **Runtime selection** — if the team is debating CopilotKit vs A2UI vs something else, that's an `@ai-architect` decision, not a spec decision. This skill assumes the runtime is chosen (or auto-falls-back to principles mode if it's not).

---

## Required Inputs

| Input | Required | Notes |
|---|---|---|
| `--intent FILE` | Yes | Markdown file describing what the agent should render, why, and the user context |
| `--runtime` | Optional | `copilotkit` \| `a2ui` \| `none` \| `auto` (default `auto`) |
| `--scope` | Optional | `card` \| `section` \| `screen` (default `card`; `section` and `screen` auto-fall-back to principles mode) |

Implementation mode requires `--runtime copilotkit` (or auto-detection landing on copilotkit AND scope gate passing). Principles mode works with any runtime including `none`.

---

## Scope Gate (Implementation Mode)

Implementation mode REJECTS any intent that triggers ANY of the following criteria. Auto-fall-back to principles mode is default. Only a buyer-documented exception overrides.

| # | Reject criterion | Why |
|---|---|---|
| 1 | **More than 3 content blocks + nav** (full screen) | CopilotKit Presentational renders atomically after validation; full-screen layouts cause perceptible wait and lose the value of inline agent rendering |
| 2 | **Streaming requirements** (progressive render, partial render, incremental data) | CopilotKit `render` runs once with fully-deserialized params; streaming is a different runtime story |
| 3 | **Multi-step interactive flows** (forms with >1 step, wizards, multi-screen navigation) | Event return channels and state management across steps are not natively supported by the Presentational pattern |
| 4 | **Real-time external updates** (pub/sub, live data, push notifications driving re-render) | Agent is not in the render event loop; re-render requires a new tool call |

**Auto-fallback trigger**: If ANY criterion is TRUE, the skill:
1. Writes the rejection reason to stderr with the triggering criterion number
2. Switches mode to principles
3. Produces principles-mode output with a top-note: *"Auto-fell-back to principles mode because [criterion]. To force implementation mode, the PM must document an exception in the intent file under the `exception:` field with business rationale."*

The buyer override is explicit and documented because silent override of the scope gate is how this skill becomes useless.

---

## Method (Implementation Mode)

### Step 1 — Read intent, classify component

Classify into one of: **card**, **form**, **list**, **media**, **data-viz**. Write the classification to the output so downstream reviewers know what vocabulary they are reading.

### Step 2 — Run scope gate

Run the 4-criteria check. If ANY criterion fails, auto-fall-back to principles mode per the rules above.

### Step 3 — Design the component vocabulary

Name each prop. Declare its type. Declare its constraints (string length, enum values, array bounds). Declare required vs optional. This is the shape of what the LLM will emit. Keep it tight — the more props, the more boundary failure modes.

Principles to apply:
- **Bounded strings over free text wherever possible.** Free text strings are the primary vector for LLM hallucination leaking into the rendered component. If the field is "title," cap it at a realistic max (120 chars for a card title, 30 for an action label). The LLM will respect the cap reliably when the Zod `.describe()` names it.
- **Enums over free-form status values.** The Zod schema catches enum violations before render; it cannot catch semantic drift in free-form status strings like "blocked" vs "paused" vs "on hold." Pick three to five values and hold the line.
- **Array bounds** (`min(0).max(3)`) for collections. Uncapped arrays produce unpredictable layout — the LLM may emit 1 or 11 items, and the render contract has to handle both. Caps make the render contract tractable.
- **Avoid nested components in v1.** Flat vocabularies render predictably; nested vocabularies wait for the whole tree to validate and the failure modes compound (the child Zod schema rejects but the parent validates, or vice versa).
- **Required vs optional is load-bearing.** Optional fields give the LLM permission to skip, which means the render contract must define what shows when the field is absent. Mark fields optional only when the empty state is designed.

### Step 4 — Draft Zod schema (the boundary validator)

Every vocabulary item becomes a Zod field. The skill outputs a draft schema the Frontend Developer can implement directly. This is the boundary validator — everything inside the `render` function can assume validated types; everything outside must be treated as adversarial LLM output.

Schema discipline:
- Use `.strict()` or explicit unknown-key handling (default `.passthrough()` silently drops LLM intent, which is a semantic failure the user will not see)
- Use `.describe()` on every field — this is what the LLM sees when it tries to emit the tool call, and it's the primary way to prevent malformed output
- Use enum validation, not string pattern matching, for constrained choices

### Step 5 — Define render contract

For every prop combination that matters, define what the component renders. The render contract covers, at minimum:
- **Default state** (happy path, all props present and valid)
- **Loading state** (the tool call is in-flight; CopilotKit is atomic here so this window is short but it must exist — the LLM takes 500ms to 2s to emit a structured tool call, and a card-shaped hole during that window is a design failure)
- **Error state** (Zod rejected the LLM output; what shows instead of a card-shaped hole — typically an inline compact "I tried to show you a task card but couldn't, here's the text version" fallback that preserves the user's conversational flow)
- **Empty state** (valid props that happen to be empty — e.g., `actions: []` validates against Zod but needs its own render decision: does the card show without action buttons, or does it collapse actions to a placeholder?)
- **Applicable variants** — every enum value should have its own variant entry. For a task card with `status: "pending" | "in_progress" | "done"`, that's three variants. If any variant renders identically, say so explicitly so the Frontend Developer does not build duplicate code.

The spike at `genui-spike-2026-W1.md` is explicit that error-state design is where this pattern feels brittle. Invalid-input recovery is where users notice generative UI is not real UI. A card-shaped hole when Zod rejects is bad UX. The spec MUST name the error-state fallback in words a Frontend Developer can implement without follow-up questions.

### Step 6 — Define event return spec (co-owned with @interaction-designer)

This section is **load-bearing** and co-authored with 🕹️ Interaction Designer. Every interactive element in the rendered component needs an event contract:

- **Event type** (click, hover, focus, change, submit)
- **Return channel** — which of the three options applies:
  1. **Pure hyperlink** — click navigates via `<a href>`, agent never sees it. Simplest, works for deep links to app routes, loses the conversational feedback loop.
  2. **Client-side handler with no agent callback** — `onClick` fires local behavior (toggle, filter, copy-to-clipboard). Agent never sees it. Appropriate when the user action has no effect the agent needs to know about.
  3. **Client-side handler that calls a second CopilotKit action** — `onClick` fires a second tool call (e.g., `report_task_card_action_clicked`) that the agent sees and can react to. Full conversational loop. Most expensive in plumbing but the only option that closes the loop.
- **Acknowledgment** — does the click produce visible feedback before the agent responds? Option 3 has a latency window (second tool call + agent response) that must be designed for. Typically: button shows pressed state, then disabled-with-spinner, then resolves to success or error when the agent replies.
- **Out-of-scope events** — explicitly name which events this component does NOT support. Example: "v1 does not support status editing via click; the status chip is display-only. A future version may add click-to-cycle-status with a third CopilotKit action." This is how the spec draws a line that keeps v1 shippable.

**@interaction-designer note (load-bearing)**: Event return channels are the hidden complexity of generative UI. The PM spec makes the choice, the Frontend Developer cannot guess, and the user experience diverges across the three options in ways the user can feel — option 1 is silent, option 2 is local-only, option 3 has a visible latency window. Any spec missing the event return channel is not ready for implementation. A common failure mode: the spec says "the user can click the action button" and stops there. All three options satisfy that sentence and produce three different user experiences. The event return spec prevents that ambiguity.

---

## Method (Principles Mode)

Principles mode is shorter in process steps but equally rigorous in output quality. The rigor shifts from "will a Frontend Developer build this today" to "will a Frontend Developer in 12 months still find the vocabulary and event contracts useful when the runtime situation has changed."

### Step 1 — Read intent, acknowledge scope outside implementation mode

Write a one-paragraph framing of what the intent is asking for, and explicitly state why it is outside implementation mode. Name the specific triggering criterion (scope-gate #1-7, or `--runtime` choice, or buyer preference). This paragraph becomes the top-note of the output so readers know immediately what they are reading. Do NOT soften the framing. "This is principles mode because the intent describes a wizard with 4 steps and the current CopilotKit Presentational pattern does not reliably support multi-step state" is the correct level of specificity.

### Step 2 — Design component vocabulary as runtime-agnostic

Same shape as implementation mode Step 3 but runtime-neutral. No Zod, no React, no SDK-specific idioms. Just: what fields does the LLM need to emit, what are their types, what are their bounds, what are the required-vs-optional semantics. The vocabulary should be expressible in TypeScript, in a Zod schema, in a JSON Schema, or in a streaming delta format without any loss of meaning. If the vocabulary depends on runtime specifics to be understood, it is not runtime-agnostic and needs to be redesigned.

### Step 3 — Prop schema conventions (runtime-neutral)

Describe the type discipline in runtime-neutral terms — "bounded strings," "enums for status," "array bounds" — and explain WHY each convention matters regardless of which runtime eventually renders the component. The "why" is what makes principles-mode output still useful when the team picks a runtime 6 months later. A team reading a conventions section that says "use enums for status" but doesn't explain why has to re-derive the reasoning. A section that says "use enums for status because runtime schemas catch enum violations before render but cannot catch semantic drift in free-form strings" is self-contained.

### Step 4 — Event contracts (co-owned with @interaction-designer)

Runtime-agnostic event contracts. What events matter. What data they carry. Where they return. This section is still load-bearing — principles mode does not mean hand-waving event design. The runtime is hypothetical; the event model is not. The three return-channel options (hyperlink / local handler / second-action callback) still apply in runtime-neutral form: "events return as navigation, as local state changes, or as a back-channel to the agent." The spec picks one or enumerates when each applies.

@interaction-designer's contribution is load-bearing here. In implementation mode she specifies the exact CopilotKit plumbing; in principles mode she specifies the abstract event model that any runtime would need to support. Both are real work.

### Step 5 — Hand-off: migration path if a compatible runtime matures

Name the specific conditions under which this principles-mode spec could become an implementation-mode spec:
- Which runtime capabilities would have to stabilize (e.g., "A2UI mid-stream failure semantics converge on rollback-to-close," "CopilotKit adds streaming render," "MCP UI extensions reach a stable spec")
- Which scope-gate criteria would have to be addressed by the runtime (e.g., "if A2UI converges on ordered-delta guarantees, the out-of-order reject criterion can be relaxed")
- What re-review the spec would need before advancing (typically: re-run the spike, re-validate the vocabulary against the new runtime, re-run quality gates with implementation-mode checks)

This migration path is not a promise. It is a pointer for the team reading this spec in 2027 so they do not have to re-derive the reasoning from scratch.

---

## Output Structure (Implementation Mode)

```markdown
# [Component Name] — Generative UI Spec (Implementation Mode)

> ⚠️ EXPERIMENTAL. Runtime last validated 2026-04-11 on CopilotKit Presentational.

## Component Classification
[card | form | list | media | data-viz]

## Component Vocabulary
[Named fields with types, constraints, required/optional]

## Zod Schema (Draft)
```ts
[Draft Zod schema with .describe() on every field]
```

## Render Contract
### Default
### Loading
### Error
### Empty
### Variants
[One sub-section per applicable variant]

## Event Return Spec
[Co-owned with @interaction-designer]
[Each interactive element: event type, return channel (1/2/3), acknowledgment, out-of-scope events]

## Type-Safety Acknowledgment
Zod + CopilotKit gives validation **at the boundary**, not end-to-end.

**What the schema catches**: the LLM emitting the wrong TYPE for a prop. `status: 42` when the schema says `status: "pending" | "in_progress" | "done"` gets rejected before `render` is called. Inside `render`, the TypeScript types are real and can be trusted.

**What the schema does NOT catch**: the LLM calling `show_task_card` when the user asked a general question and a task card is the wrong surface entirely. The schema cannot catch semantic intent mismatch. It cannot catch the LLM emitting `status: "pending"` when the real task is done. It cannot catch hallucinated content that happens to validate (`title: "Fix the bug in the auth flow"` when no such bug exists). End-to-end correctness requires EVALUATION TESTING — scenario tests of agent behavior — in addition to schema validation.

This distinction is load-bearing. A spec that assumes "the schema protects me" encodes a false safety guarantee that will surface as user-reported confusion in production. The Frontend Developer needs to know the schema is a boundary check, not an intent check.

## Test Plan
- Boundary validation: unit tests of Zod schema against sample LLM outputs (happy + all known failure modes)
- Evaluation testing: scenario tests of agent behavior — does the agent pick this component for the right intents?

## Runtime Staleness Warning
This spec assumes CopilotKit Presentational as of 2026-04-11. Re-validate on every CopilotKit major release. See `Product Org OS/reference/genui-spike-2026-W1.md` for the baseline reality check.
```

## Output Structure (Principles Mode)

```markdown
# [Component Name] — Generative UI Spec (Principles Mode)

> ⚠️ EXPERIMENTAL + PRINCIPLES ONLY. No runtime code. No implementation guarantees.

## Scope Framing
[Why this is principles mode — which scope-gate criterion triggered or which runtime choice forced it]

## Component Vocabulary (Runtime-Agnostic)
[Fields, types, constraints, in runtime-neutral language]

## Prop Schema Conventions
[Type discipline, runtime-neutral, with rationale]

## Event Contracts (Runtime-Agnostic)
[Co-owned with @interaction-designer]
[What events matter, what data they carry, where they return]

## Migration Path
[What would have to happen in the runtime world for this to become implementation-mode]
[Specific conditions, not vague hopes]
```

---

## Quality Gates

The skill's output is not ready until ALL of these pass:

1. [ ] **Mode explicit** — output declares implementation or principles at the top
2. [ ] **Scope gate passed** (implementation only) — or scope-gate exception documented with rationale
3. [ ] **Zod schema draft present** (implementation only)
4. [ ] **Render contract covers default + loading + error + empty + applicable variants** (implementation only)
5. [ ] **Event return spec present** (both modes) — every interactive element has a return channel named
6. [ ] **Type-safety acknowledgment present** (implementation only) — validation-at-boundary vs end-to-end
7. [ ] **Interaction-designer contribution present in event-contract section** (both modes) — named and load-bearing, not decorative
8. [ ] **Out-of-scope section present** — interaction flow, brand voice, accessibility audit, motion, content strategy all named as NOT covered
9. [ ] **Experimental banner wired** — top of output with 2026-04-11 validation date

Any quality-gate failure blocks publication of the spec.

---

## Related Skills and Hand-off

### Input

- **`/figma-agent-brief`** — when visual design and runtime spec overlap. The Figma agent brief answers "what should this look like" with visual direction and design-system tokens. This skill answers "what is the runtime contract" with vocabulary, schema, and event semantics. Both are needed for a complete generative-UI component: without the Figma brief, the render contract has no visual language; without this spec, the visual language has no way to land predictably in the runtime. Typical flow: `/figma-agent-brief` produces the visual direction, then `/generative-ui-spec` locks the runtime contract, then the Frontend Developer implements from both.

### Reference

- **`Product Org OS/reference/genui-spike-2026-W1.md`** — baseline reality check on the state of CopilotKit vs A2UI runtime maturity. Read this first when modifying the skill. If the runtime landscape shifts (new CopilotKit release, A2UI convergence, new SDK entrant), the spike is re-run and the `experimental_last_validated` date on this skill resets.

### Cross-team consultability

- **`@frontend-dev`** — consumability gate. Can a frontend dev actually build the component from this spec without asking the PM for clarification? If no, the spec fails review. The birth test at `Legionis/Product/generative-ui-spec-birth-test-task-card-2026-04-11.md` is the reference point: a Frontend Developer should be able to implement that task card from the spec alone. If any spec this skill produces is less complete than the birth test, it is not ready.
- **`@interaction-designer`** — event-contract and interaction-state co-owner. Every spec routes event-contract sections through her. She is named as `co_owner` in the frontmatter; this is not a courtesy credit but a load-bearing collaboration. On borderline implementation-vs-principles cases, her event contracts become the deciding factor (see "Co-authoring model" below).
- **`@ai-architect`** — runtime evaluation framing. When the PM asks "which runtime should we pick," that's her question, not this skill's. This skill assumes the runtime is chosen or defaults to principles mode. If a team wants to debate CopilotKit vs A2UI vs OpenAI Apps SDK vs MCP UI extensions, @ai-architect runs that evaluation and this skill produces specs for the chosen runtime after.
- **`@visual-designer`** — when the component needs brand treatment beyond the Figma brief (icons, illustrations, specific brand applications). Not required for most card-sized components but load-bearing for brand-heavy surfaces.

---

## Co-authoring Model (UI Designer + Interaction Designer)

This skill is co-owned. The co-authorship is structural, not decorative. Here is how ownership splits in practice:

| Section | Owner | Co-owner role |
|---|---|---|
| Component classification | 🎨 UI Designer | Interaction Designer reviews |
| Component vocabulary | 🎨 UI Designer | Interaction Designer reviews for event-implication side effects |
| Zod schema draft | 🎨 UI Designer | Interaction Designer reviews for state-management implications |
| Render contract (default / loading / empty / variants) | 🎨 UI Designer | Interaction Designer reviews for interaction-state completeness |
| Render contract (error state) | 🎨 UI Designer + 🕹️ Interaction Designer (co-authored) | Shared authorship because error-state design is equal parts visual fallback and interaction recovery |
| **Event return spec** | 🕹️ Interaction Designer (primary) | UI Designer reviews for visual feedback specification |
| Test plan (boundary validation) | 🎨 UI Designer | Interaction Designer reviews |
| Test plan (evaluation testing scenarios) | 🕹️ Interaction Designer (primary) | UI Designer reviews |
| Type-safety acknowledgment | 🎨 UI Designer | — |
| Quality gates | Both | — |

### Co-owner Decision Rule on Borderline Cases

If an intent is 80% implementation-mode-eligible but has ONE streaming or flow sub-requirement, the skill defaults to **principles mode** and @interaction-designer's event contracts become load-bearing — they become the primary artifact the Frontend Developer can still use. The rationale: a 20% unstable spec produces 100% unpredictable behavior at runtime, but a principles-mode spec with a strong event model remains useful even when the runtime changes.

The co-owner has veto power on the implementation-vs-principles decision. If @interaction-designer says "the interaction state is too complex for the Presentational pattern," that's a principles-mode call even if the visual surface is card-sized.

---

## Runtime Staleness Maintenance

Quarterly re-review. When CopilotKit ships a major release that changes the `useCopilotAction` contract (Zod schema handling, render signature, tool-call transport), the `experimental_last_validated` date resets and the spike at `Product Org OS/reference/genui-spike-2026-W1.md` is re-run before any new spec ships. Any spec produced against the old validation date is flagged stale on next use.

The same applies if A2UI converges on a stable implementation that addresses the streaming reject criterion. That would be a version bump, not a silent update.

---

## Anti-patterns (DO NOT DO)

Observed failure modes from the spike thought-experiment and from Figma-agent-brief reviews. These are the specific ways a generative-UI spec goes wrong in production.

1. **"The schema will catch it."** No, the schema catches type errors at the boundary. It does not catch the LLM picking the wrong component, hallucinating content, or emitting valid-but-semantically-wrong props. Always include the type-safety acknowledgment.
2. **Card-shaped hole on validation failure.** The most common UX failure. When Zod rejects, the user sees a gap where the card should have been, the agent retries silently, and the conversation feels broken. Always design the error-state fallback.
3. **"The user can click the action."** Ambiguous sentence that satisfies all three event-return options. Always name the option (1/2/3) and the acknowledgment behavior.
4. **Free-form status strings.** `status: string` is an invitation to semantic drift. Always use enums.
5. **Uncapped arrays.** `actions: Array<Action>` without bounds forces the render contract to handle 0-to-infinity. Always use `min/max`.
6. **Nested generative components.** The whole tree waits for the whole JSON to validate, and the failure modes compound. v1 is flat. Nested is a v2+ conversation and probably a different pattern entirely.
7. **Assuming streaming works at card granularity.** It doesn't. Props-arriving-one-at-a-time looks like broken progressive loading, not intentional design. If the team wants streaming, either stream at item-level (not prop-level) or use a different pattern.
8. **Skipping the out-of-scope events section.** The spec looks complete without it, but the Frontend Developer builds click handlers for events the PM never authorized. The out-of-scope section is a contract.
9. **Silent override of the scope gate.** If an intent fails the scope gate and the PM wants to override, the override goes in the intent file with rationale. No quiet overrides. The gate exists because the runtime does not reliably support out-of-scope shapes.
10. **Accessibility as "we'll add it later."** ARIA, focus order, and screen-reader semantics must be in the render contract at v1, not deferred. Generative UI emits components at runtime; there is no Figma mockup a designer can annotate later.

---

## Auto-fallback Trigger Conditions (Exact)

The auto-fallback from implementation mode to principles mode triggers when ANY of these are true:

1. **Intent includes the word "streaming," "progressive," "incremental," "realtime," "live," or "pub/sub"** in the context of rendering (not in the context of data the agent fetches before rendering).
2. **Intent describes a flow with explicit sequential steps** — "first the user does X, then Y, then Z" — regardless of whether the steps are on the same screen.
3. **Intent describes a full screen or page** — 4+ content blocks OR explicit navigation structure OR a layout that spans the viewport.
4. **Intent specifies a wizard, multi-step form, or workflow** — any state-carrying interaction across more than one user action.
5. **`--scope section` or `--scope screen`** flag is present (these are principles-mode-only scopes by definition).
6. **`--runtime a2ui` or `--runtime none`** flag is present.
7. **Intent includes nested generative components** — "inside each card, the agent can render another card" — the pattern does not support this predictably.

If ALL of the above are false AND `--runtime` is `copilotkit` (or auto-detected as copilotkit), implementation mode runs. Otherwise, principles mode runs with the specific triggering criterion named in the output top-note.

A buyer override is possible but requires an `exception:` field in the intent file with a written rationale. The override does NOT disable the scope gate; it documents that the PM accepts the runtime risk of producing an implementation spec for something the runtime may not reliably support.

---

## Pattern

Pattern 1 Consultation default (per `rules/delegation-protocol.md`). Consult:
- `@interaction-designer` for event contracts and interaction-state sections (co-owned, named in output)
- `@frontend-dev` for consumability review (can the spec be built without follow-up questions?)
- `@ai-architect` when the runtime choice itself is under debate (evaluation framing, not spec production)

Not a sensitive skill. `sensitive: false`.

---

## Birth Test

One real spec produced under this skill: a **Legionis agent task card** in CopilotKit Presentational implementation mode. See `Legionis/Product/generative-ui-spec-birth-test-task-card-2026-04-11.md`. The birth test exercises every quality gate, including the Zod schema draft, the render-contract state matrix, the event return spec (with out-of-scope events named), the type-safety acknowledgment, and the test plan.

---

## Versioning

Every spec produced by this skill includes a version field (in the render contract or the header) and a dependency on the runtime validation date. When the runtime changes (CopilotKit major release, A2UI convergence, SDK swap), in-flight agent sessions do NOT automatically know. The PM has to:
1. Version the component explicitly (semver or date)
2. Gate the component by agent capability (the agent only emits v2 cards when it knows the client can render v2)
3. Leave the old version running until sessions roll over

The spec should include a "Schema evolution plan" paragraph in the render contract section that names how v1 → v2 would work if a new field is added, how deprecated enum values are handled, and what the deprecation window looks like. Without this plan, the LLM starts emitting v2 props against a v1 client and the rendered component silently drops the new field.

---

## ROI Framing

Time saved on drafting and triage: **~3.5 hours per spec** at the blended rate of ~$200/hr for a UI Designer + Interaction Designer co-authorship on a generative-UI spec, producing vocabulary + Zod draft + render contract + event spec + test plan + type-safety acknowledgment + versioning plan. This is drafting and triage, not final implementation.

Role split on what this skill does NOT replace:
- **Frontend Developer** — reviews the Zod schema, implements the component, wires the `useCopilotAction` hook, handles the edge cases the spec identified but the code has to actually catch
- **QA Engineer** — designs and runs the evaluation tests (the scenario tests of agent behavior, not just the boundary validation tests)
- **Product Manager** — validates intent coverage (does the LLM actually emit this component for the right user intents?)
- **Interaction Designer** — owns the event contract and interaction-state reviews on any update to the spec

This skill produces the structured first pass that those roles review and own. Framing it any other way — "time saved on frontend implementation," "time saved on QA" — would overstate what a design-level spec can accomplish and set up the Frontend Developer to inherit ambiguity.
