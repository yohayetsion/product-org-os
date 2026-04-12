# Design Systems — Frameworks & Methods

## Overview

Design systems are the single source of truth for how a product looks, feels, and behaves. They bridge design and engineering by codifying decisions into reusable components, tokens, and patterns. A well-maintained design system accelerates delivery, enforces consistency, and reduces cognitive load for both builders and users.

This knowledge pack covers the foundational frameworks for building, maintaining, and evolving design systems. These are not theoretical — they are practical approaches that scale from startup to enterprise.

---

## Frameworks

### Atomic Design

**When to use**: Building a new design system from scratch, or restructuring an existing one that has grown organically without clear hierarchy.

**How it works**: Atomic Design, introduced by Brad Frost, organizes UI into five hierarchical levels:

1. **Atoms** — The smallest indivisible elements: buttons, labels, input fields, icons, color swatches. They do one thing and have no dependencies on other components.

2. **Molecules** — Simple combinations of atoms that function as a unit: a search bar (input + button), a form field (label + input + error message), a menu item (icon + text).

3. **Organisms** — Complex components made of molecules and atoms: a navigation header, a product card grid, a form section, a dashboard widget.

4. **Templates** — Page-level layouts that define where organisms go. They are content-agnostic wireframes — the structural skeleton without real data.

5. **Pages** — Templates populated with real content. Pages are where you test whether the system works with actual data, edge cases, and real-world constraints.

**Template**: When adding a new component to the system, ask:
- Is this an atom (indivisible)? → Add to atoms library
- Does it combine existing atoms? → It's a molecule
- Does it combine molecules? → It's an organism
- Does it define page structure? → It's a template

**Limitations**: Atomic Design can become over-rigid. Not every component fits neatly into one level. Use it as a mental model, not a strict taxonomy. Some teams find three levels (primitives, components, patterns) more practical.

---

### Design Tokens

**When to use**: Any project with more than one developer or platform. Tokens are the first thing to establish in a new design system.

**How it works**: Design tokens are named values that store visual design decisions. They create a shared language between design and engineering, enabling theming, consistency, and systematic updates.

**Token categories:**

| Category | Examples | Naming Pattern |
|----------|----------|----------------|
| Color | `color-primary-500`, `color-text-default` | `color-{role}-{variant}` |
| Typography | `font-size-lg`, `font-weight-bold` | `font-{property}-{scale}` |
| Spacing | `spacing-4`, `spacing-8` | `spacing-{value}` |
| Border | `border-radius-md`, `border-width-thin` | `border-{property}-{scale}` |
| Shadow | `shadow-sm`, `shadow-lg` | `shadow-{scale}` |
| Motion | `duration-fast`, `easing-default` | `{category}-{scale}` |
| Breakpoint | `breakpoint-sm`, `breakpoint-lg` | `breakpoint-{name}` |

**Token architecture (three tiers):**

1. **Global tokens** — Raw values: `blue-500: #3B82F6`. Platform-agnostic.
2. **Alias tokens** — Semantic mapping: `color-primary: {blue-500}`. Brand-specific.
3. **Component tokens** — Scoped to component: `button-bg: {color-primary}`. Component-specific.

**Theming**: Swap alias token values to create themes (light/dark, brand A/brand B) without touching component code. Global tokens stay the same; alias mappings change.

**Template for adding a new token:**
```
Name: [category]-[role]-[variant]
Value: [raw value]
Alias: [references which global token]
Used by: [list of components]
Rationale: [why this value]
```

**Limitations**: Token proliferation is real. Every token is maintenance. Start with fewer tokens and add only when reuse justifies the overhead. Avoid creating tokens for one-off values.

---

### Multi-Channel Token Exposure

**When to use**: Any design system that is consumed by more than one runtime (web + native + design-tool) OR that needs to be consumed by machine readers (build tools, codegen, AI agents).

**The principle**: A token that exists only in one channel (e.g., only as a CSS custom property) is a token only one class of consumer can use. A token exposed across all channels is a token any consumer can use — human designer in Figma, frontend engineer in TypeScript, build-time tool pulling JSON, AI agent reading a structured schema.

**The four channels**:

| Channel | Format | Consumed by | Example |
|---------|--------|-------------|---------|
| **Runtime CSS** | CSS custom properties (`--color-bg`) | Browsers, runtime theming, end users | `:root { --color-bg: #FFF; }` |
| **Tooling JSON** | W3C DTCG JSON format | Build tools, codegen, doc generators, AI agents | `{ "color": { "bg": { "$value": "#FFF", "$type": "color" } } }` |
| **Strongly-typed** | TypeScript types / enums | TS/JS consumers with IDE autocomplete + compile-time checks | `type ColorBg = "#FFF" \| "#000";` |
| **Design tool** | Figma Variables, Sketch Libraries, native design primitives | Designers producing specs | Figma Variables mapped 1:1 to DTCG JSON |

**The target**: a design system at Score 5 on the token exposure dimension (see the AI-Agent Readiness section below) publishes ALL four channels from a single source of truth. Tools like Style Dictionary, Theo, or the W3C DTCG reference transformers exist exactly to solve this problem.

**Minimal viable exposure**: If you only have engineering capacity for one channel, pick DTCG JSON. It is the only channel that other channels can be auto-generated FROM. CSS vars, TypeScript types, and Figma Variables can all be produced from DTCG JSON via existing tooling. The reverse is not true.

**Template for a multi-channel token declaration**:

```json
// tokens/color.json (W3C DTCG format — source of truth)
{
  "color": {
    "primary": {
      "500": { "$value": "#3B82F6", "$type": "color" }
    },
    "bg": {
      "default": { "$value": "{color.white}", "$type": "color" }
    }
  }
}
```

Generated from the JSON above:

```css
/* tokens.css — generated */
:root {
  --color-primary-500: #3B82F6;
  --color-bg-default: #FFFFFF;
}
```

```typescript
// tokens.ts — generated
export const tokens = {
  color: {
    primary: { 500: "#3B82F6" },
    bg: { default: "#FFFFFF" },
  },
} as const;
export type ColorToken = typeof tokens.color;
```

Figma Variables are imported from the same JSON via a Figma plugin or manual sync. When the JSON source updates, all four channels update together.

**Round-tripping**: Mature design systems close the loop — designers edit Figma Variables, a sync process writes back to DTCG JSON, and the new JSON propagates to CSS and TypeScript on the next build. This is the frontier; most systems do not yet round-trip cleanly.

**Limitations**: Multi-channel token exposure is the single most effort-saving investment a design system can make for AI-agent consumption, but it requires build tooling discipline. If the team cannot commit to a source-of-truth file that generates the other channels, DO NOT manually maintain multiple channels — drift will destroy them within a quarter. Pick one channel, do it well, plan the migration to multi-channel when you have tooling budget.

---

### Variant Taxonomy & Exhaustive Coverage

**When to use**: Any component that will be used in more than one context. Applies to every interactive component in the library (button, input, select, card, table, modal, tooltip, popover, tab, menu).

**The principle**: A component with implicit or partial variant coverage is a component where every consumer has to improvise the missing variants. A component with exhaustive variant coverage can be dropped into any context without improvisation. For AI-agent consumers, exhaustive variant coverage is the difference between "the agent can pick a variant from a list" and "the agent has to invent one and probably gets it wrong."

**The taxonomy**: Variants come in several orthogonal axes. Every interactive component should explicitly declare which axes it supports and which values exist on each axis.

| Axis | Typical values | Rule |
|------|----------------|------|
| **State** (required) | default, hover, focus, pressed, disabled, loading, error, empty, skeleton | REQUIRED for every interactive component — see State Coverage Checklist below |
| **Size** | sm, md, lg (or xs, sm, md, lg, xl) | REQUIRED when the component renders at more than one scale |
| **Density** | compact, regular, comfortable | OPTIONAL — include only when density is a product surface (data tables yes, hero buttons no) |
| **Theme** | light, dark, high-contrast | REQUIRED if the product supports theming |
| **Tone/Intent** | neutral, primary, success, warning, danger, info | REQUIRED for components that carry semantic weight (buttons, alerts, badges) |
| **Context** | on-surface, on-brand, on-image, on-dark, on-light | OPTIONAL — include when the component ships to contexts that change its contrast requirements |
| **Orientation** | horizontal, vertical | REQUIRED for components with a layout axis (tabs, menus, dividers) |

**State Coverage Checklist (REQUIRED vs OPTIONAL)**:

| State | Required? | Criterion |
|-------|-----------|-----------|
| default | REQUIRED | Every component has a resting state |
| hover | REQUIRED | Any component with pointer interaction |
| focus | REQUIRED | Any interactive component — accessibility mandate |
| pressed (active) | REQUIRED | Any component that accepts click/tap |
| disabled | REQUIRED | Any component that can be programmatically blocked |
| loading | REQUIRED | Any component that can trigger an async action OR whose data is async |
| error | REQUIRED | Any component with validation or failure modes |
| empty | REQUIRED | Any component that renders a collection (list, table, grid) |
| skeleton | OPTIONAL | Strongly recommended when the component's data is async and above-the-fold |
| read-only | OPTIONAL | Form controls that can be rendered in non-editable context |

**The rule**: mark a component "exhaustively covered" only when every REQUIRED state on every REQUIRED axis has an explicit variant with design, code, and documentation. If any required state is missing, the component is "partially covered" and should be flagged in the library inventory.

**Variant combinatorics**: Axes multiply. A button with 3 sizes × 5 tones × 8 states = 120 variant cells. You do not need 120 hand-designed comps — you need a declared system that produces any cell on demand, plus hand-designed proof for the canonical combinations (tone × state at md size is usually sufficient). The AI-agent readiness requirement is that the system can *name* every cell, not that every cell is hand-crafted.

**Template — variant declaration block**:

```yaml
# button.variants.yaml
component: Button
axes:
  state: [default, hover, focus, pressed, disabled, loading]
  size: [sm, md, lg]
  tone: [neutral, primary, success, warning, danger]
  theme: [light, dark]
required_combinations:
  - [default, md, primary, light]  # canonical
  - [disabled, md, primary, light]
  - [loading, md, primary, light]
  - [hover, md, primary, light]
  - [focus, md, primary, light]
total_cells: 180  # 6 × 3 × 5 × 2
hand_designed_cells: 10
generated_cells: 170
```

**Limitations**: Taxonomy is a discipline, not a deliverable. The cost of writing the taxonomy is small; the cost of enforcing it across a growing team is real. Tie taxonomy to PR review — a new component without a variant declaration block is a PR that does not merge.

---

### Typed Prop Schemas

**When to use**: Every component in the library, without exception. Typed props are the contract between the component author and every consumer — human or machine.

**The principle**: A component with narrative prop descriptions ("variant: enum of primary, secondary") is a component a human can infer and a machine cannot. A component with a typed schema (TypeScript interface, Zod schema, or JSON Schema) is a component both can consume. Typed props are the dimension 1 foundation for every agent-consumable design system.

**Pattern catalog — common component contracts**:

**Button**
```typescript
interface ButtonProps {
  variant: "primary" | "secondary" | "tertiary" | "danger" | "ghost";
  size: "sm" | "md" | "lg";
  tone?: "neutral" | "primary" | "success" | "warning" | "danger";
  state?: "default" | "loading" | "disabled";
  iconStart?: IconName;
  iconEnd?: IconName;
  onClick: (event: MouseEvent) => void;
  children: React.ReactNode;
  "aria-label"?: string;
}
```

**Input (text)**
```typescript
interface InputProps {
  type: "text" | "email" | "password" | "number" | "tel" | "url";
  size: "sm" | "md" | "lg";
  state: "default" | "hover" | "focus" | "disabled" | "error" | "read-only";
  value: string;
  onChange: (next: string) => void;
  placeholder?: string;
  error?: string;
  label: string;
  hint?: string;
  required?: boolean;
  autoComplete?: AutoCompleteToken;
}
```

**Select**
```typescript
interface SelectOption<T> {
  value: T;
  label: string;
  disabled?: boolean;
  group?: string;
}
interface SelectProps<T> {
  options: SelectOption<T>[];
  value: T | null;
  onChange: (next: T | null) => void;
  size: "sm" | "md" | "lg";
  state: "default" | "disabled" | "error" | "loading";
  placeholder?: string;
  searchable?: boolean;
  clearable?: boolean;
  label: string;
  error?: string;
}
```

**Card**
```typescript
interface CardProps {
  variant: "flat" | "elevated" | "outlined";
  padding: "none" | "sm" | "md" | "lg";
  interactive?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
}
// Card uses compound-component composition
Card.Header = (props: { children: React.ReactNode }) => ...;
Card.Body = (props: { children: React.ReactNode }) => ...;
Card.Footer = (props: { children: React.ReactNode }) => ...;
```

**Table**
```typescript
interface TableColumn<T> {
  key: keyof T;
  header: string;
  width?: number | "auto";
  align?: "left" | "center" | "right";
  sortable?: boolean;
  render?: (value: T[keyof T], row: T) => React.ReactNode;
}
interface TableProps<T> {
  columns: TableColumn<T>[];
  rows: T[];
  state: "default" | "loading" | "empty" | "error";
  emptyState?: React.ReactNode;
  errorState?: React.ReactNode;
  sortBy?: keyof T;
  sortDir?: "asc" | "desc";
  onSort?: (key: keyof T, dir: "asc" | "desc") => void;
  density: "compact" | "regular" | "comfortable";
}
```

**Modal**
```typescript
interface ModalProps {
  open: boolean;
  onClose: () => void;
  size: "sm" | "md" | "lg" | "full";
  dismissible?: boolean;  // can close via escape/backdrop
  title: string;
  description?: string;
  children: React.ReactNode;
  footer?: React.ReactNode;
  initialFocus?: React.RefObject<HTMLElement>;
}
```

**Type discipline rules**:

1. **No `any`. No open `string` where an enum fits.** Prop types must be as narrow as the component's behavior. If a prop accepts one of five values, type it as a literal union, not `string`.
2. **Enumerations are explicit.** `variant: "primary" | "secondary"` is correct. `variant: string // one of primary, secondary` is not.
3. **Callbacks have explicit parameter types.** `onChange: (next: string) => void`, not `onChange: Function`.
4. **Optional props are marked with `?`.** The contract should be readable at a glance: what must I pass, what may I pass.
5. **Children types are explicit when constrained.** A component that only accepts specific child types should type them — e.g., `Tabs` should accept `children: TabElement[]`, not `React.ReactNode`.
6. **Accessibility props are first-class.** `aria-label`, `role`, `id` when needed — treat them as part of the contract, not implementation detail.
7. **Generic parameters for data components.** `Select<T>`, `Table<T>`, `Combobox<T>` — never force consumers to coerce `unknown`.

**Variant enumeration approach**: Do NOT use booleans for mutually exclusive variants. `<Button primary danger large>` creates 2³ = 8 combinatorial states, most of them invalid. Use a single `variant` or `tone` prop with an enumerated union. Reserve booleans for genuinely binary toggles that are independent of other props (`disabled`, `required`, `readonly`).

**Dual documentation**: For every component, the library should publish BOTH the TypeScript interface (or equivalent) AND a narrative prop table. The TypeScript interface is the source of truth; the narrative table is auto-generated from it for human readers. Never maintain both by hand — drift is guaranteed.

**Limitations**: Type discipline requires buy-in from component authors. The first few components will be under-typed and will need to be migrated. The migration is straightforward but takes time. Tie it to PR review — narrowly-typed new components, progressively-typed legacy components.

---

### Machine-Readable Documentation

**When to use**: Any design system that expects to be consumed by build tools, codegen, documentation generators, or AI agents. This is the dimension that most design systems score lowest on and that unlocks the most value when addressed.

**The principle**: Human-readable prose is the primary interface for designers and engineers. Machine-readable contracts are the primary interface for everything else — build tools, doc generators, codegen, AI agents, accessibility auditors. A mature design system publishes BOTH, co-located, with the machine contract as the source of truth and the narrative auto-generated or hand-written on top.

**Target formats**:

| Content | Machine format | Human format |
|---------|---------------|--------------|
| Tokens | [W3C DTCG JSON](https://www.w3.org/community/design-tokens/) | Token reference page |
| Component props | TypeScript interface OR JSON Schema | Props table (auto-generated) |
| Component variants | YAML or JSON variant declaration | Variant table (auto-generated) |
| Component states | Enumerated in props + YAML/JSON | State table (auto-generated) |
| Accessibility contract | ARIA role + keyboard map in JSON | Accessibility section |
| Examples | JSX/TSX source files | Rendered examples (auto-generated) |

**W3C Design Tokens Community Group (DTCG) format**:

The W3C Design Tokens Community Group publishes a JSON format for design tokens. It is the closest thing to an industry standard and is the format this knowledge pack recommends. The spec URL is `https://www.w3.org/community/design-tokens/` and the format spec lives in the community group's GitHub. Adoption is growing through Style Dictionary, Figma's Variables export, Amazon Style Dictionary, and Supernova.

Key properties:
- `$value` — the token value
- `$type` — one of `color`, `dimension`, `fontFamily`, `fontWeight`, `duration`, `cubicBezier`, `number`, `shadow`, `typography`, etc.
- `$description` — optional narrative
- `$extensions` — tool-specific metadata (respected but not required by the spec)

```json
{
  "color": {
    "primary": {
      "$type": "color",
      "500": {
        "$value": "#3B82F6",
        "$description": "Primary brand color, 500 step"
      }
    }
  },
  "spacing": {
    "$type": "dimension",
    "4": { "$value": "16px" },
    "8": { "$value": "32px" }
  }
}
```

**JSON Schema for component contracts**:

For component props, JSON Schema is the language-agnostic option; TypeScript interfaces are the TS-native option; Zod is the runtime-validation option. Pick one per project and commit. Mixing creates drift.

Example JSON Schema for a Button:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ds.example.com/schemas/button.json",
  "title": "Button",
  "type": "object",
  "required": ["variant", "size", "children"],
  "properties": {
    "variant": {
      "enum": ["primary", "secondary", "tertiary", "danger", "ghost"]
    },
    "size": { "enum": ["sm", "md", "lg"] },
    "state": { "enum": ["default", "loading", "disabled"] },
    "children": { "type": "string" }
  }
}
```

An AI agent handed this schema can generate valid props without guessing. A build tool can validate every Button usage in the codebase against it. A documentation generator can produce the props table from it. One source, many consumers.

**Co-location pattern**: place the machine contract next to the narrative docs.

```
components/
  Button/
    Button.tsx               # implementation
    Button.schema.json       # JSON Schema (machine contract)
    Button.variants.yaml     # variant declaration block
    Button.md                # narrative docs (references schema + variants)
    Button.stories.tsx       # live examples
```

**Auto-generation discipline**: Narrative docs are auto-generated from the machine contract wherever possible. Hand-written narrative covers only the "why" — decisions, rationale, trade-offs, anti-patterns. This guarantees that the props table in the docs always matches the actual component contract. Drift is the enemy of documentation trust.

**Limitations**: Machine contracts are an upstream investment. The first component to adopt them is expensive; every subsequent component is cheap. The return on the upstream investment is that the design system becomes consumable by AI agents, codegen, and tooling without per-consumer bespoke work.

---

### Component Library Patterns

**When to use**: When building reusable components that will be consumed by other designers and engineers.

**How it works**: Well-designed component libraries follow patterns that enable composition, extension, and predictable behavior.

**Composition pattern**: Components should compose rather than configure. Instead of a single `Card` component with 15 props, provide `Card`, `Card.Header`, `Card.Body`, `Card.Footer` that compose freely.

**Variant pattern**: Use explicit variants rather than boolean props. Instead of `<Button primary small>`, use `<Button variant="primary" size="sm">`. Variants are extensible; booleans create combinatorial explosion.

**State pattern**: Every interactive component defines these states:
- Default (resting state)
- Hover (pointer over element)
- Active/Pressed (during interaction)
- Focus (keyboard focus)
- Disabled (interaction blocked)
- Loading (async operation)
- Error (validation failure)
- Empty (no content)

**Props pattern**: Component props should be:
- **Typed** — Clear types, not `any` or `string` for everything
- **Defaulted** — Sensible defaults that work without configuration
- **Documented** — Every prop has a description and example
- **Constrained** — Enum values where possible, not open strings

**Template for documenting a component:**
```
## Component: [Name]

**Purpose**: [What problem it solves]
**Atomic level**: [Atom/Molecule/Organism]

### Variants
| Variant | Use Case | Visual |
|---------|----------|--------|
| primary | Main actions | [description] |
| secondary | Supporting actions | [description] |

### States
| State | Behavior | Visual Change |
|-------|----------|---------------|
| default | Resting | [description] |
| hover | Pointer over | [description] |

### Props
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| variant | enum | "primary" | Visual variant |

### Accessibility
- Role: [ARIA role]
- Keyboard: [interaction]
- Screen reader: [announcement]
```

**Limitations**: Over-abstraction kills usability. Not every UI element needs to be a library component. Components should be created when they are used in 3+ places. Premature abstraction creates components nobody uses.

---

### Theme Architecture

**When to use**: Products that support light/dark mode, white-labeling, brand customization, or multi-tenant theming.

**How it works**: Theme architecture separates visual decisions from component structure using a layered token system.

**Theme layers:**

1. **Foundation** — Global tokens (colors, sizes, fonts). Shared across all themes.
2. **Theme** — Alias tokens that map foundation values to semantic roles. Swapped per theme.
3. **Component** — Component-specific tokens that reference alias tokens. Rarely change.

**Implementation pattern:**
```css
/* Foundation (never changes) */
:root {
  --blue-500: #3B82F6;
  --gray-900: #111827;
  --white: #FFFFFF;
}

/* Light theme */
[data-theme="light"] {
  --color-bg: var(--white);
  --color-text: var(--gray-900);
  --color-primary: var(--blue-500);
}

/* Dark theme */
[data-theme="dark"] {
  --color-bg: var(--gray-900);
  --color-text: var(--white);
  --color-primary: var(--blue-400);
}
```

**Theme switching considerations:**
- Store preference in `localStorage` or user settings
- Respect `prefers-color-scheme` as default
- Transition between themes smoothly (avoid flash)
- Test all components in every theme combination
- Ensure contrast ratios meet WCAG AA in every theme

**Template for theme definition:**
```
Theme: [Name]
Base: [Which foundation palette]
Mapping:
  Background: [token → value]
  Surface: [token → value]
  Text: [token → value]
  Primary: [token → value]
  Contrast ratios: [verified AA/AAA]
```

**Limitations**: Theme systems add complexity. If you only need light mode, don't build a theme system. Add theming when the business need is clear (dark mode, white-labeling). Premature theming is engineering overhead without user value.

---

### Documentation Standards

**When to use**: Any design system with more than one consumer (designer or engineer).

**How it works**: Design system documentation is the primary interface for adoption. Poor documentation means poor adoption, regardless of component quality.

**Documentation categories:**

1. **Getting Started** — Installation, setup, first component. Under 5 minutes to first render.
2. **Principles** — Why decisions were made. Not rules, but reasoning.
3. **Component Docs** — Per-component: purpose, variants, states, props, examples, accessibility.
4. **Pattern Docs** — Common combinations: forms, navigation, data display, empty states.
5. **Token Reference** — Complete token list with values, usage, and visual examples.
6. **Migration Guides** — How to upgrade between versions. Breaking changes highlighted.
7. **Contribution Guide** — How to propose new components or changes.

**Documentation quality checklist:**
- [ ] Every component has a live example
- [ ] All variants are shown side-by-side
- [ ] States are demonstrated (not just listed)
- [ ] Accessibility requirements are explicit
- [ ] Do/don't examples prevent misuse
- [ ] Props table is complete and typed
- [ ] Related components are cross-referenced

**Limitations**: Documentation rots fast. The best documentation is auto-generated from the source code where possible (props from TypeScript, examples from Storybook). Manual documentation should cover the "why" that code cannot express.

---

## Decision Framework

When making design system decisions, use this priority order:

1. **Does it already exist in the system?** → Use it
2. **Can an existing component be extended?** → Extend it
3. **Is it needed in 3+ places?** → Create a new component
4. **Is it a one-off?** → Build it locally, consider promotion later

---

## AI-Agent Readiness

This section is new to the pack as of April 2026 and addresses a question the original pack did not: **can a design system be consumed directly by an AI agent?** The short answer is yes, but only when the system meets a small number of preconditions that are orthogonal to the question of whether the system is good for humans. A design system can be excellent for humans and invisible to agents simultaneously.

This section has two sub-sections: an **Evergreen** block of principles that survive tool churn, and a **Current tool state as of April 2026** appendix that references specific vendors and frameworks that were stable or maturing at the time of writing. The evergreen block is authoritative. The dated appendix is advisory and should be re-reviewed every six months — see the re-review calendar note at the end.

### Evergreen Principles

**What "AI-agent readiness" means**:

A design system is "AI-agent ready" when an AI agent — a large language model, an autonomous codegen tool, a generative-UI runtime, a Figma-to-code pipeline — can consume the design system's contracts and produce output that is *correct by construction* rather than *plausible by pattern matching*. The difference matters.

An agent consuming a prose-only design system is pattern matching. It sees "primary button" in a paragraph and produces JSX that "looks like" a primary button. It does not know whether `danger` is a valid `variant` value for this specific library, whether `size="large"` or `size="lg"` is the convention, or whether the library has a loading state at all. It guesses. Guesses drift from the actual library over time. The output has to be inspected and corrected by a human.

An agent consuming a machine-contract-ready design system is doing something fundamentally different. It reads the schema, picks a variant from the enumerated set, and produces JSX that is *valid against the schema* before it ever renders. If the schema says `variant: "primary" | "secondary" | "danger"`, the agent cannot emit `variant: "tertiary"`. The output is correct-by-construction against the contract. Humans still review for taste and appropriateness, but correctness on the contract dimension is free.

**The four preconditions**:

| Precondition | What it unlocks | Minimum score on the rubric |
|---|---|---|
| Typed props (TypeScript / Zod / JSON Schema) | The agent can pick valid prop values without guessing | 4 / 5 |
| Variant coverage (exhaustive + taxonomized) | The agent knows every state that must be handled | 4 / 5 |
| Machine-readable docs (DTCG + JSON Schema) | The agent can consume the spec directly without parsing prose | 4 / 5 |
| Token exposure (multi-channel) | The agent can emit values that match the active theme | 4 / 5 |

A design system that scores **3 or lower on any foundation dimension** is not AI-agent ready. The library-readiness precondition used by downstream agent skills (see the next sub-section) will fail, and the agent will refuse to proceed or will degrade to a lower-fidelity fallback.

**The library-readiness precondition pattern**:

Agent skills that consume a design system should publish an explicit precondition: *before I do this work, I require the library to meet these criteria*. If the library does not meet the criteria, the agent should not silently proceed — it should stop and report. This pattern is used by:

- `/figma-agent-brief` — refuses to generate agent-ready briefs against a library below Score 4 on typed props and variant coverage
- `/generative-ui-spec` — refuses to generate a CopilotKit runtime binding against a library below Score 4 on machine-readable docs and token exposure
- (Future) `/design-system-audit` — will consume this rubric as its core scoring mechanism

The precondition pattern is what makes the AI-readiness rubric *load-bearing* rather than decorative. It is the gate that protects downstream agent workflows from garbage-in.

**How generative UI runtimes consume a design system**:

A generative UI runtime (CopilotKit Presentational, A2UI, or equivalent) renders components at runtime based on agent-produced structured output. The runtime needs two things from the design system:

1. **A render contract** — a mapping from a component name to an actual React (or native) component. The runtime looks up `"Button"` and finds the library's `Button` component, not a hand-rolled approximation.
2. **A prop validator** — a schema that the runtime uses to reject invalid props before rendering. Zod schemas are the common choice because they double as TypeScript types and runtime validators.

A library that publishes both gets generative UI for free. A library that publishes neither requires a per-project adapter layer that is brittle, expensive, and drifts. The difference in implementation cost is roughly 10×.

**Evergreen checklist — the design system is AI-agent ready when**:

- [ ] Every component in the library has a typed prop interface (TS / Zod / JSON Schema). No `any`. No open `string` where an enum fits.
- [ ] Every component declares an exhaustive variant block naming every required state × size × tone × theme combination.
- [ ] Tokens are published as DTCG JSON as the source of truth.
- [ ] Tokens are exposed in at least three runtime channels (CSS vars + JSON + TS types minimum; Figma Variables preferred).
- [ ] Narrative docs are co-located with machine contracts and auto-generated wherever possible.
- [ ] The library publishes an AI-agent-readiness self-score against the rubric in `ai-agent-readiness-rubric.md`.
- [ ] Agent skills that consume the library declare their library-readiness preconditions explicitly.

**Versioning rule**: An AI-agent-ready design system MUST use semantic versioning with breaking-change discipline. An agent session started against v2.3 that encounters a v3.0 breaking change mid-session is a session-kill, not a graceful degradation. Major-version changes should be announced to consumer skills with a sunset window, not pushed silently.

### Current Tool State as of April 2026

> **Re-review calendar**: This sub-section references specific vendors and frameworks that were stable or maturing at April 2026. **Re-review every six months** — next forced re-review **October 2026**. Pin this date to the quarterly skill-health script. When re-reviewing, remove items that have been discontinued or superseded, add items that have stabilized, and update the staleness date.

The evergreen principles above are authoritative and should not change with tool churn. This appendix names the specific tools that, at the time of writing, implement those principles with varying degrees of maturity. The appendix is advisory.

**Generative UI runtimes**:

- **CopilotKit Presentational** — stable as of April 2026 for React-based stacks. Renders library components at runtime from structured agent output. Requires a render contract + prop validator. Production-ready for internal and early external use.
- **A2UI (Agent-to-UI) runtime** — not yet stable as of April 2026. Promising direction but spec and implementations are still moving. Do not build production flows against it yet; monitor.
- **Vercel AI SDK UI / RSC** — stable for server-rendered React flows, narrower scope than CopilotKit. Good for specific agent-driven pages; less suited for generalized library consumption.

**Design-to-code pipelines**:

- **Figma Make** — library-awareness maturing as of April 2026. The pipeline can consume Figma Variables and component variants, but generated code quality depends heavily on how well the library was structured in Figma. Requires a Score 4+ library to produce usable output.
- **Anima / Locofy / Builder.io** — mature general-purpose Figma-to-code, weaker on design-system awareness. Use when the design system is simple; revisit when agent-native pipelines mature.

**Token standards**:

- **W3C Design Tokens Community Group (DTCG) format** — adoption growing, spec nearing 1.0 as of April 2026. Style Dictionary 4.x supports it natively. Figma Variables export to DTCG is available. This is the format to commit to.
- **Style Dictionary (Amazon)** — mature, 8+ years of production use, now supports DTCG natively. The de-facto transformer for multi-channel token exposure.
- **Supernova / Specify** — commercial token management platforms; good UX, variable vendor lock-in, some DTCG support. Evaluate based on team size and willingness to adopt a SaaS layer.

**Schema and validation**:

- **TypeScript interfaces** — universal in JS/TS monorepos; zero runtime cost but no runtime validation.
- **Zod** — mature as of April 2026; provides TypeScript types + runtime validators from one definition. Near-universal in CopilotKit and similar runtimes.
- **JSON Schema** — language-agnostic; use when consumers include non-TS tooling (Python agents, Go services, design-tool plugins). More verbose than Zod but more portable.

**Reference libraries (existence proofs only)**:

- Material Design 3 — large, well-structured, strong token system, variable machine-readability
- IBM Carbon Design System — strong token architecture, published DTCG output, agent-consumable
- Salesforce Lightning Design System — mature, huge surface area, variable depth of machine contracts
- Ant Design — popular, well-typed, weak token exposure for agent consumption
- Radix UI — headless primitives, excellent type discipline, minimal token opinions by design
- Shadcn/ui — distribution model fits agent consumption patterns well (copy-into-repo, own the source)

**Do not lift content from any of these systems.** They are cited as existence proofs that the patterns in this pack are achievable at scale. The pack is first-principles work.

**Known-unstable areas (caveat emptor)**:

- A2UI runtime spec — in flux
- Figma Variables round-trip sync — one-way in most toolchains
- JSON Schema adoption for React component props — narrower than TypeScript adoption
- Auto-generation of narrative docs from Zod schemas — tooling exists but is fragmented

### Sources

- `Extension Teams/design-team/design-system-ai-readiness-audit.md` — the Week-1 audit that scored the prior version of this pack against the four dimensions and motivated this expansion. Aggregate baseline 2.75 / 5; per-dimension 3/3/2/3.
- `Extension Teams/design-team/figma-agent-probe-notes.md` — the Week-1 probe of Figma Make's library-awareness behavior, which informed the "library-readiness precondition" pattern used by `/figma-agent-brief`.
- `Extension Teams/reference/knowledge/ai-agent-readiness-rubric.md` — the standalone reusable rubric pack extracted from the audit.

---

## References

- Brad Frost, *Atomic Design* (2016)
- Nathan Curtis, *Modular Web Design* (2009)
- W3C Design Tokens Community Group specification — `https://www.w3.org/community/design-tokens/` (authoritative machine-readable token format)
- JSON Schema — `https://json-schema.org/` (language-agnostic component contract format)
- Material Design, IBM Carbon Design System, Salesforce Lightning, Ant Design, Radix UI — cited as existence proofs only; no content lifted


## Common Pitfalls

- Design tokens must be defined before component implementation — retrofitting is expensive
- Accessibility (WCAG 2.1 AA minimum) is a requirement, not a nice-to-have
- Design system adoption fails without developer buy-in — include engineers in design system decisions
