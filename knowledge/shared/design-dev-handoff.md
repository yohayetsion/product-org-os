# Design-to-Development Handoff — Frameworks & Methods

## Overview

Design handoff is where design intent either survives or dies. A complete handoff eliminates ambiguity for engineers, reduces back-and-forth, and prevents the "implementation drift" where the built product diverges from the design without anyone explicitly deciding to change it.

Good handoff documentation is not about volume — it is about precision. Engineers need to know what something looks like in every state, how it behaves at every breakpoint, what happens with edge-case content, and how tokens map to their codebase. This pack provides the templates, formats, and checklists to make that happen consistently.

**Primary Users**: `ui-designer`, `interaction-designer`, `design-dir`, `visual-designer`

---

## Handoff Spec Template

Use this template as the canonical format for any component or feature handoff. Adapt the sections to the scope — a single button needs a single-page spec; a full feature flow needs all sections.

```markdown
# Handoff Spec: [Component or Feature Name]

**Spec Version**: 1.0
**Date**: YYYY-MM-DD
**Designer**: [Name]
**Engineer(s)**: [Name(s)]
**Design File**: [Figma link, page, frame]
**Status**: Draft / Review / Final

---

## 1. Overview

[2-3 sentences: what this is, what problem it solves, where it lives in the product]

**Component type**: Atom / Molecule / Organism / Page
**Replaces**: [previous version or component, if applicable]

---

## 2. Anatomy

[Annotated screenshot or Figma embed link]

| Element | Description | Required? |
|---------|-------------|-----------|
| [Element name] | [What it is and does] | Yes / No / Conditional |

---

## 3. Design Tokens

| Property | Token | Resolved Value |
|----------|-------|----------------|
| Background | `color-surface-default` | `#FFFFFF` |
| Text | `color-text-primary` | `#111827` |
| Border | `border-radius-md` | `8px` |
| Padding | `spacing-4` | `16px` |
| [etc.] | | |

---

## 4. Component Variants

| Variant | Description | When to Use |
|---------|-------------|-------------|
| [variant-name] | [Visual/behavioral difference] | [Context] |

---

## 5. States

| State | Trigger | Visual Change | Notes |
|-------|---------|--------------|-------|
| Default | On load | — | Base state |
| Hover | Pointer over | [describe] | Desktop only |
| Active/Pressed | During click/tap | [describe] | |
| Focus | Keyboard focus | [describe] | See Accessibility section |
| Disabled | `disabled` prop | [describe] | |
| Loading | Async operation | [describe] | |
| Error | Validation failure | [describe] | |
| Empty | No content | [describe] | |
| Skeleton | Initial load | [describe] | |

---

## 6. Responsive Behavior

| Breakpoint | Token | Viewport | Changes |
|------------|-------|----------|---------|
| Mobile | `breakpoint-sm` | < 640px | [describe layout changes] |
| Tablet | `breakpoint-md` | 640-1024px | [describe layout changes] |
| Desktop | `breakpoint-lg` | > 1024px | Base layout |
| Wide | `breakpoint-xl` | > 1280px | [describe if relevant] |

---

## 7. Spacing & Layout

[Reference Figma frame for exact values, but include key measurements here]

- Padding (internal): [top] [right] [bottom] [left]
- Margin (external): [context-dependent or specify]
- Gap between elements: [value]
- Max width: [value or "full-width"]
- Min width: [value or "none"]

---

## 8. Typography

| Element | Token | Font | Size | Weight | Line Height |
|---------|-------|------|------|--------|-------------|
| Label | `font-label-md` | [family] | [size] | [weight] | [value] |
| Body | `font-body-md` | [family] | [size] | [weight] | [value] |

---

## 9. Animation & Motion

| Interaction | Trigger | Property | Duration | Easing | Delay |
|-------------|---------|----------|----------|--------|-------|
| [name] | [event] | [CSS property] | [ms] | [curve] | [ms or 0] |

Respect `prefers-reduced-motion: reduce` — disable or reduce all non-essential animations.

---

## 10. Interactions & Behavior

[Describe user interactions that aren't obvious from static screens]

- On click/tap: [what happens]
- On keyboard: [key mappings]
- On swipe (mobile): [if applicable]
- On scroll: [if behavior changes]

---

## 11. Accessibility

- **Accessible name**: [how it's labeled — visible label / aria-label / aria-labelledby]
- **Role**: [native element or ARIA role]
- **Keyboard**: [tab stops, key actions]
- **Focus indicator**: [visual description]
- **Screen reader announcement**: "[exact announcement on focus]"
- **Live region**: [if applicable — what triggers announcement]
- **Color contrast**: [foreground/background pair and ratio]
- **Touch target size**: [px dimensions]

---

## 12. Edge Cases

| Scenario | Expected Behavior |
|----------|------------------|
| Text overflow (very long string) | [truncate / wrap / scroll] |
| Minimum content (empty/single word) | [behavior] |
| Maximum content (character limit) | [behavior] |
| Missing optional data | [fallback UI] |
| RTL languages | [mirroring behavior] |
| Slow network / loading state | [skeleton or spinner] |
| Offline / error state | [fallback] |

---

## 13. Asset Exports

| Asset | Format | Resolution | Filename |
|-------|--------|-----------|---------|
| [Icon name] | SVG | N/A | `icon-[name].svg` |
| [Image] | WebP / PNG | 1x, 2x | `[name]@1x.webp`, `[name]@2x.webp` |

---

## 14. Implementation Notes

[Any notes specific to this component that don't fit above — gotchas, dependencies, browser quirks, tech debt to acknowledge]

---

## 15. Open Questions

| Question | Owner | Due |
|----------|-------|-----|
| [question] | [name] | [date] |

```

---

## Design Token Documentation Format

Design tokens are the contract between design and engineering. Document them in a format that maps directly to the codebase.

### Color Tokens

```markdown
## Color Tokens

### Primitive Tokens (Global)
These are raw values. Never use directly in components.

| Token | Value | Usage |
|-------|-------|-------|
| `blue-50` | `#EFF6FF` | — |
| `blue-500` | `#3B82F6` | — |
| `blue-900` | `#1E3A8A` | — |
| `gray-100` | `#F3F4F6` | — |
| `gray-900` | `#111827` | — |

### Semantic Tokens (Alias)
These map intent to primitives. Use these in components.

| Token | Light Mode | Dark Mode | Usage |
|-------|------------|-----------|-------|
| `color-bg-default` | `gray-50` | `gray-950` | Page background |
| `color-surface-default` | `white` | `gray-900` | Card, panel backgrounds |
| `color-text-primary` | `gray-900` | `gray-50` | Body text |
| `color-text-secondary` | `gray-600` | `gray-400` | Supporting text |
| `color-text-disabled` | `gray-400` | `gray-600` | Disabled text |
| `color-primary-default` | `blue-500` | `blue-400` | Primary actions |
| `color-primary-hover` | `blue-600` | `blue-300` | Primary action hover |
| `color-primary-active` | `blue-700` | `blue-200` | Primary action press |
| `color-border-default` | `gray-200` | `gray-700` | Default borders |
| `color-border-focus` | `blue-500` | `blue-400` | Focus indicators |
| `color-status-error` | `red-600` | `red-400` | Error states |
| `color-status-success` | `green-600` | `green-400` | Success states |
| `color-status-warning` | `amber-600` | `amber-400` | Warning states |
```

### Typography Tokens

```markdown
## Typography Tokens

### Font Family
| Token | Value | Usage |
|-------|-------|-------|
| `font-family-base` | `'Inter', system-ui, sans-serif` | Body, UI text |
| `font-family-mono` | `'JetBrains Mono', monospace` | Code, data |
| `font-family-display` | `'[Brand font]', serif` | Marketing headings |

### Font Scale
| Token | rem | px | Usage |
|-------|-----|-------|-------|
| `font-size-xs` | 0.75rem | 12px | Labels, captions |
| `font-size-sm` | 0.875rem | 14px | Secondary text |
| `font-size-md` | 1rem | 16px | Body text (base) |
| `font-size-lg` | 1.125rem | 18px | Large body |
| `font-size-xl` | 1.25rem | 20px | H4 / sub-heading |
| `font-size-2xl` | 1.5rem | 24px | H3 |
| `font-size-3xl` | 1.875rem | 30px | H2 |
| `font-size-4xl` | 2.25rem | 36px | H1 |
| `font-size-5xl` | 3rem | 48px | Display |

### Font Weight
| Token | Value | Usage |
|-------|-------|-------|
| `font-weight-regular` | 400 | Body text |
| `font-weight-medium` | 500 | UI labels, subheadings |
| `font-weight-semibold` | 600 | Headings, strong labels |
| `font-weight-bold` | 700 | Display, emphasis |

### Line Height
| Token | Value | Usage |
|-------|-------|-------|
| `line-height-tight` | 1.25 | Headings |
| `line-height-snug` | 1.375 | UI labels |
| `line-height-normal` | 1.5 | Body text |
| `line-height-relaxed` | 1.625 | Long-form reading |
```

### Spacing Tokens

```markdown
## Spacing Tokens

Using a 4px base grid. All spacing values are multiples of 4px.

| Token | px | rem | Common Usage |
|-------|----|-----|--------------|
| `spacing-0.5` | 2px | 0.125rem | Micro gaps |
| `spacing-1` | 4px | 0.25rem | Icon padding, tight gaps |
| `spacing-2` | 8px | 0.5rem | Inline padding, compact items |
| `spacing-3` | 12px | 0.75rem | Form field internal padding |
| `spacing-4` | 16px | 1rem | Standard component padding |
| `spacing-5` | 20px | 1.25rem | Card padding (mobile) |
| `spacing-6` | 24px | 1.5rem | Section padding |
| `spacing-8` | 32px | 2rem | Card padding (desktop) |
| `spacing-10` | 40px | 2.5rem | Section gap |
| `spacing-12` | 48px | 3rem | Section heading gap |
| `spacing-16` | 64px | 4rem | Page section margin |
| `spacing-20` | 80px | 5rem | Hero section padding |
| `spacing-24` | 96px | 6rem | Large section separation |
```

### Elevation / Shadow Tokens

```markdown
## Elevation Tokens

| Token | CSS Value | Usage |
|-------|-----------|-------|
| `shadow-none` | `none` | Flat surfaces |
| `shadow-xs` | `0 1px 2px rgba(0,0,0,0.05)` | Subtle card lift |
| `shadow-sm` | `0 2px 4px rgba(0,0,0,0.1)` | Cards, inputs |
| `shadow-md` | `0 4px 12px rgba(0,0,0,0.1)` | Dropdowns, popovers |
| `shadow-lg` | `0 8px 24px rgba(0,0,0,0.12)` | Modals, drawers |
| `shadow-xl` | `0 16px 40px rgba(0,0,0,0.15)` | Command palettes, full-screen overlays |
```

### Motion Tokens

```markdown
## Motion Tokens

### Duration
| Token | Value | Usage |
|-------|-------|-------|
| `duration-instant` | 0ms | No animation (reduced motion) |
| `duration-fast` | 100ms | Micro-interactions (button press, toggle) |
| `duration-normal` | 200ms | State changes (hover, focus) |
| `duration-moderate` | 300ms | Component transitions (dropdown, tooltip) |
| `duration-slow` | 500ms | Page transitions, significant layout changes |
| `duration-slower` | 700ms | Onboarding, first-run animations |

### Easing Curves
| Token | Cubic Bezier | Usage |
|-------|-------------|-------|
| `easing-default` | `cubic-bezier(0.4, 0, 0.2, 1)` | General transitions |
| `easing-in` | `cubic-bezier(0.4, 0, 1, 1)` | Elements leaving the screen |
| `easing-out` | `cubic-bezier(0, 0, 0.2, 1)` | Elements entering the screen |
| `easing-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Playful, bouncy interactions |
| `easing-linear` | `linear` | Progress bars, spinners |
```

---

## Component Spec Format

Every component in the design system should have a spec that covers these sections completely.

```markdown
## Component: [ComponentName]

**Category**: Atom / Molecule / Organism
**Status**: Draft / Stable / Deprecated
**Version**: 1.x
**Design File**: [Figma link]
**Storybook**: [link if available]

### Purpose

[One sentence: what this component does and the problem it solves]

### Variants

| Variant | Description | Visual |
|---------|-------------|--------|
| `primary` | Main action, highest visual weight | [screenshot / Figma link] |
| `secondary` | Supporting action | |
| `ghost` | Low-emphasis, inline use | |
| `destructive` | Dangerous or irreversible actions | |

### Sizes

| Size | Height | Font Size | Padding | When to Use |
|------|--------|-----------|---------|-------------|
| `sm` | 32px | 14px | 8px 12px | Dense UIs, table actions |
| `md` | 40px | 16px | 10px 16px | Default |
| `lg` | 48px | 18px | 12px 24px | Prominent CTAs |

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `'primary' \| 'secondary' \| 'ghost' \| 'destructive'` | `'primary'` | Visual style |
| `size` | `'sm' \| 'md' \| 'lg'` | `'md'` | Component size |
| `disabled` | `boolean` | `false` | Disables interaction |
| `loading` | `boolean` | `false` | Shows loading state |
| `icon` | `ReactNode` | `undefined` | Leading icon |
| `iconPosition` | `'left' \| 'right'` | `'left'` | Icon placement |
| `fullWidth` | `boolean` | `false` | Expands to container width |
| `onClick` | `() => void` | `undefined` | Click handler |

### States

| State | Trigger | Visual Change | Token(s) |
|-------|---------|--------------|----------|
| Default | — | Base styling | `color-primary-default` |
| Hover | `:hover` | Background darkens | `color-primary-hover` |
| Active | `:active` | Background darkens further | `color-primary-active` |
| Focus | `:focus-visible` | Focus ring appears | `color-border-focus` |
| Disabled | `disabled` prop | Reduced opacity, no pointer | `color-text-disabled` |
| Loading | `loading` prop | Spinner replaces or overlays text | — |

### Behavior

- Click activates the `onClick` handler
- When `loading`, the button is non-interactive and shows a spinner
- When `disabled`, the button is non-interactive and has `aria-disabled="true"`
- Focus ring appears on keyboard focus only (`:focus-visible`, not `:focus`)
- `fullWidth` makes the button `width: 100%`

### Accessibility

- **Role**: `button` (native `<button>` element)
- **Keyboard**: Space and Enter both activate
- **Loading state**: `aria-busy="true"`, `aria-label` includes "[Action] in progress"
- **Disabled state**: `aria-disabled="true"` (not `disabled` attr, to keep focusable)
- **Icon-only**: Requires `aria-label` describing the action

### Edge Cases

| Scenario | Behavior |
|----------|----------|
| Very long label text | Truncate with ellipsis, tooltip with full text |
| Icon with no text | `aria-label` required on button element |
| Multiple loading buttons | Each has independent loading state |
| Used inside a form | Default `type="button"` to prevent accidental submit |

### Do / Don't

| Do | Don't |
|----|-------|
| Use primary for the single most important action per screen | Use multiple primary buttons side by side |
| Use destructive variant for delete/remove actions | Use red text to imply danger without `destructive` variant |
| Include icon to reinforce meaning | Use icons that contradict or are unrelated to the label |
```

---

## State Documentation — All Interactive States

Every interactive component must be designed and documented in all applicable states. Missing states are the most common source of implementation drift.

| State | Trigger | What Changes | Notes |
|-------|---------|-------------|-------|
| **Default** | Initial render | — | Resting state; baseline for all other states |
| **Hover** | Pointer over element | Background, border, cursor | Desktop/pointer devices only |
| **Active / Pressed** | During click/tap | Visual depression, color | Should feel immediate (< 100ms) |
| **Focus** | Keyboard navigation | Focus ring appears | `:focus-visible` only (not mouse click) |
| **Disabled** | `disabled` prop or state | Opacity reduction, no-cursor | Keep focusable with `aria-disabled` for AT |
| **Loading** | Async operation in progress | Spinner, prevent interaction | Communicate what is loading |
| **Error** | Validation failure | Red border, error message | Error text linked via `aria-describedby` |
| **Success** | Positive outcome | Checkmark, green, confirmation | Auto-dismiss or user-dismissable |
| **Warning** | Potential issue, non-blocking | Amber indicator | Don't block action |
| **Empty** | No data / no results | Empty state illustration + text | Include a CTA if appropriate |
| **Skeleton** | First load before data | Animated placeholder shapes | Match layout of loaded state |
| **Selected** | Item chosen | Highlight, check | Persists until deselected |
| **Expanded** | Disclosed content | «Energy Major» rotation, content visible | Managed with `aria-expanded` |
| **Dragging** | During drag-and-drop | Ghost element, drop zones activate | Needs single-pointer alternative |
| **Read-only** | Non-editable mode | Input styling, no pointer | Different from disabled — still readable |

---

## Responsive Behavior Matrix

Document how each component adapts across breakpoints. Focus on what changes, not just what it looks like.

| Breakpoint | Token | Range | Typical Changes |
|------------|-------|-------|----------------|
| `xs` | `breakpoint-xs` | < 480px | Stack all columns; hide non-essential elements; increase tap targets |
| `sm` | `breakpoint-sm` | 480-640px | 1-2 column layouts; compact navigation |
| `md` | `breakpoint-md` | 640-768px | Tablet portrait; side panels collapse to drawers |
| `lg` | `breakpoint-lg` | 768-1024px | Tablet landscape; 2-3 column layouts appear |
| `xl` | `breakpoint-xl` | 1024-1280px | Desktop baseline; full sidebar navigation |
| `2xl` | `breakpoint-2xl` | > 1280px | Wide desktop; max-width containers kick in |

**Component-level responsive spec format**:

```markdown
### Responsive: [Component Name]

| Breakpoint | Layout | Typography | Spacing | Visibility |
|------------|--------|------------|---------|------------|
| Mobile (< 640px) | Stacked, full-width | [size] | [values] | [hidden/shown elements] |
| Tablet (640-1024px) | [layout] | [size] | [values] | [hidden/shown elements] |
| Desktop (> 1024px) | [layout] | [size] | [values] | All visible |

**Breakpoint-specific behaviors**:
- At mobile: [specific behavior]
- At tablet: [specific behavior]
- At desktop: Base design
```

---

## Animation and Motion Specs

Document every animation that requires engineering effort. Static designs with transitions cost sprint time if underdocumented.

### Animation Spec Format

```markdown
### Animation: [Interaction Name]

| Property | Value |
|----------|-------|
| **Trigger** | [User event or state change] |
| **Element** | [What is animated] |
| **CSS Property** | [transform, opacity, height, etc.] |
| **Start value** | [value] |
| **End value** | [value] |
| **Duration** | [ms] → Token: `duration-[scale]` |
| **Easing** | [curve name] → Token: `easing-[type]` |
| **Delay** | [ms or 0] |
| **Iteration** | Once / Repeat / Infinite |
| **Direction** | Normal / Reverse / Alternate |
| **Reduced motion** | [what to do when `prefers-reduced-motion: reduce`] |
```

### Common Animation Patterns

| Pattern | Property | Duration | Easing | Reduced Motion |
|---------|----------|----------|--------|----------------|
| Button press feedback | `transform: scale(0.97)` | 100ms | `easing-default` | No animation |
| Dropdown open | `opacity: 0→1`, `transform: translateY(-8px→0)` | 200ms | `easing-out` | No animation |
| Modal enter | `opacity: 0→1`, `transform: scale(0.95→1)` | 300ms | `easing-out` | No animation |
| Modal exit | `opacity: 1→0`, `transform: scale(1→0.95)` | 200ms | `easing-in` | No animation |
| Toast slide-in | `transform: translateX(100%→0)` | 300ms | `easing-out` | Instant appear |
| Skeleton shimmer | Background gradient sweep | 1500ms | `linear` | Static color |
| Progress bar fill | `width: 0→n%` | Proportional | `linear` | Instant |
| Hover color transition | `background-color` | 150ms | `easing-default` | Instant |
| Accordion open | `height: 0→auto` | 300ms | `easing-out` | Instant |
| Page transition | `opacity: 0→1` | 200ms | `easing-out` | Instant |

---

## Edge Case Checklist

Before marking a spec complete, verify every edge case has a designed state.

### Content Length

- [ ] Minimum content: single character, single word, empty string
- [ ] Maximum content: does text truncate, wrap, or overflow? Specify which
- [ ] Long single word without spaces (URL, hash): specify word-break behavior
- [ ] Number of items: what happens at 0 items (empty state), 1 item, 100+ items

### Internationalization

- [ ] RTL languages: does the component mirror correctly?
- [ ] Long languages: German, Finnish can be 30-50% longer than English — does layout hold?
- [ ] Short languages: Chinese, Japanese can be significantly shorter — does layout still look right?
- [ ] Date/time formats: local format support, not just ISO
- [ ] Number formatting: commas vs periods, currency symbols, thousands separators

### Data and Loading States

- [ ] Slow network: skeleton state designed and specified
- [ ] Missing optional data: fallback for images, names, metadata
- [ ] Partial data: some fields present, some missing
- [ ] Stale data: loading refresh state

### User Scenarios

- [ ] First-time user with no data (onboarding empty state)
- [ ] Power user with maximum data (density, performance)
- [ ] Error state: what message, what action, can the user recover?
- [ ] Permission denied: what is shown to unauthorized users?

### Technical Edge Cases

- [ ] Very small viewport (320px): horizontal scroll prevention
- [ ] Very large viewport (2560px+): max-width container behavior
- [ ] Print stylesheet: should this component print? How?
- [ ] High contrast mode: does it work with Windows/browser forced colors?
- [ ] Dark mode: all tokens have dark mode values

---

## Asset Export Guidelines

Consistent asset naming and format selection prevents engineering confusion and asset management chaos.

### Format Selection

| Asset Type | Format | Why |
|-----------|--------|-----|
| Icons | SVG | Scalable, styleable with CSS, small file size |
| UI illustrations | SVG (simple) / WebP (complex) | SVG preferred; WebP for photorealistic |
| Product screenshots / photos | WebP with PNG fallback | WebP 30% smaller than PNG |
| Backgrounds / textures | WebP | Best compression for photographic |
| Logos | SVG | Scalable, no quality loss |
| Favicons | ICO + PNG (16, 32, 180, 192, 512px) | Multi-platform compatibility |
| Open Graph images | PNG or JPG (1200x630px) | Platform-specific requirements |
| Lottie / animation | JSON (Lottie format) | For complex micro-animations |

### Resolution Requirements

| Context | Density | Required Exports |
|---------|---------|-----------------|
| Web (standard screens) | 1x | `@1x` |
| Web (retina/HiDPI) | 2x | `@1x`, `@2x` |
| Mobile (iOS) | 1x, 2x, 3x | `@1x`, `@2x`, `@3x` |
| Android | mdpi to xxxhdpi | Multiple densities or vector |
| Email | 1x and 2x | Both always required |

### Naming Convention

```
[component]-[variant]-[state]-[size]@[density].[format]

Examples:
button-primary-default-lg@1x.webp
button-primary-hover-lg@2x.webp
icon-search.svg
illustration-empty-state-tasks.svg
logo-brand-horizontal.svg
logo-brand-mark.svg
og-image-homepage.png
```

**Rules**:
- All lowercase, no spaces, hyphen-separated
- No version numbers in filenames (use git or Figma versioning)
- No descriptive adjectives ("new", "final", "v2") — use component + variant + state only
- SVGs should be optimized (run through SVGO before handoff)

---

## Handoff Completeness Checklist

Use this before marking any spec as ready for engineering.

### Design File

- [ ] All states designed (default, hover, active, focus, disabled, loading, error, empty)
- [ ] All variants present in Figma
- [ ] Responsive layouts at all required breakpoints
- [ ] Component uses tokens (not hardcoded values)
- [ ] Auto-layout applied (not absolute positioning for responsive components)
- [ ] All layers are named logically (not "Rectangle 47" or "Group 12")
- [ ] Design file link included in spec

### Spec Document

- [ ] Anatomy annotated with element names
- [ ] Token table complete — every visual property mapped to a token
- [ ] States table complete — all 9+ states documented
- [ ] Responsive behavior specified for each breakpoint
- [ ] Animations documented with trigger, property, duration, easing
- [ ] Edge cases reviewed and designed
- [ ] Accessibility section complete
- [ ] Asset exports list included with format, resolution, naming

### Accessibility

- [ ] Color contrast verified (foreground/background pairs at all states)
- [ ] Touch target size confirmed (minimum 24x24px, recommended 44x44px)
- [ ] Keyboard behavior specified
- [ ] Screen reader announcement specified
- [ ] ARIA roles, properties, and states documented
- [ ] Focus indicator designed and specified

### Assets

- [ ] Icons exported as optimized SVG
- [ ] Images exported at required resolutions
- [ ] All assets follow naming convention
- [ ] Assets delivered in shared location (Figma, S3, Zeplin, Storybook)

### Handoff Sync

- [ ] Sync meeting scheduled with engineering lead
- [ ] Open questions listed and assigned
- [ ] Review cycle defined (how/when engineers can ask questions)
- [ ] Acceptance criteria agreed before development starts

---

## Design-to-Code Token Mapping

Tokens only work if design and engineering use the same names. This section shows how Figma token names map to CSS custom properties and common frameworks.

### Figma to CSS Custom Properties

| Figma Token | CSS Custom Property | Usage in CSS |
|------------|--------------------|----|
| `color/primary/500` | `--color-primary-500` | `background-color: var(--color-primary-500)` |
| `spacing/4` | `--spacing-4` | `padding: var(--spacing-4)` |
| `font/size/md` | `--font-size-md` | `font-size: var(--font-size-md)` |
| `shadow/md` | `--shadow-md` | `box-shadow: var(--shadow-md)` |
| `border/radius/md` | `--border-radius-md` | `border-radius: var(--border-radius-md)` |

### Figma to Tailwind CSS

| Figma Token | Tailwind Class | Notes |
|------------|---------------|-------|
| `color/primary/500` | `bg-primary-500` | Requires Tailwind config extension |
| `spacing/4` | `p-4` (16px) | Tailwind base unit = 4px; `p-4` = 16px |
| `spacing/8` | `p-8` (32px) | |
| `font/size/md` | `text-base` | |
| `font/size/lg` | `text-lg` | |
| `shadow/sm` | `shadow-sm` | |
| `shadow/md` | `shadow-md` | |

### Figma to CSS-in-JS (Styled Components / Emotion)

```javascript
// Token usage in styled-components
const Button = styled.button`
  background-color: ${({ theme }) => theme.colors.primary[500]};
  padding: ${({ theme }) => theme.spacing[4]};
  font-size: ${({ theme }) => theme.fontSize.md};
  border-radius: ${({ theme }) => theme.borderRadius.md};
  box-shadow: ${({ theme }) => theme.shadows.sm};
`;
```

---

## Figma-to-Code Workflows

### Recommended Handoff Stack

| Tool | Role | Best For |
|------|------|---------|
| **Figma** | Source of truth | All design work, component library |
| **Figma Dev Mode** | Inspection layer | Property values, asset export, CSS output |
| **Tokens Studio** (Figma plugin) | Token sync | Syncing design tokens to code via JSON |
| **Storybook** | Component documentation | Interactive component library for engineers |
| **Zeroheight / zeroheight** | Design system docs | Public-facing design system documentation |
| **Supernova** | Token pipeline | Design token management across platforms |

### Token Sync Workflow (Tokens Studio + Style Dictionary)

```
1. Designer defines tokens in Figma (Tokens Studio plugin)
2. Plugin exports tokens to JSON (committed to repo)
3. Style Dictionary transforms JSON → CSS variables, SCSS, JS, Android, iOS
4. Engineers import platform-native tokens
5. Design and code stay in sync via automated pipeline
```

**Token JSON format (W3C Design Tokens Community Group standard)**:
```json
{
  "color": {
    "primary": {
      "500": {
        "$value": "#3B82F6",
        "$type": "color",
        "$description": "Primary brand color, used for interactive elements"
      }
    }
  },
  "spacing": {
    "4": {
      "$value": "16px",
      "$type": "dimension"
    }
  }
}
```

### Figma Inspect → Code Checklist

When engineers use Figma Dev Mode inspect, they should receive:

- [ ] Auto-generated CSS properties (Figma generates these, but verify token names match codebase)
- [ ] Component variants visible in Figma (not just the base state)
- [ ] Asset exports accessible in Dev Mode
- [ ] Prototype links for interaction flows
- [ ] Design tokens panel showing token names (requires Tokens Studio or Variables setup)

---

## 2026-06 Delta Update (as of 2026-06-06)

**The design→code handoff is collapsing into a single agentic loop.** The discrete "handoff" — designer produces a spec, engineer reads it, engineer implements, drift is policed — is being compressed by design tools that commit code directly against the real codebase. Two May 2026 product moves point the same direction:

- **Figma Make (closed beta, 2026-05-28)** connects to your local codebase, lets you prompt contextually on individual design elements, and has an AI coding agent commit changes / open a PR (via Figma MCP) against your real design system. The "handoff document" becomes a PR against the codebase, not a spec a human re-implements.
- **Vercel v0 (~2026-05-13)** was repositioned in Vercel's own docs from "shadcn/ui component generator" to "an AI agent for creating real code, full-stack apps, and agents" (AI Elements added Voice & Code components, 2026-05-11) — the same collapse from design-artifact-generation to code-agent.

**Implication for this pack's practice.** The handoff spec template, token-sync workflow, and Dev Mode inspect checklist above are NOT obsolete — they become the design-system contract the agent commits *against* rather than the document a human implements *from*. The leverage shifts: a precise, token-mapped, accessible design system is now what makes the agentic PR correct on the first pass. Where handoff was once about eliminating ambiguity for a human engineer, in the agentic loop it is about giving the design-tool agent a vocabulary tight enough to emit a mergeable PR. The Dev Mode inspect checklist becomes a PR-review checklist. (Sibling pack `generative-ui.md` covers the runtime-generation side of the same shift.)

**Sources (2026-06 delta)**:
- https://www.figma.com/release-notes/
- https://vercel.com/blog/working-with-figma-and-custom-design-systems-in-v0

---

*Knowledge Pack: Design-to-Development Handoff | Team: Design | Attribution: Anthropic knowledge-work-plugins (design/design-handoff); 2026-06 delta adds Figma Make (figma.com/release-notes) + Vercel v0 repositioning (vercel.com/blog) | Last Updated: 2026-06-06*
