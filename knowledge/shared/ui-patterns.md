# Interaction Design Patterns — Frameworks & Methods

## Overview

Interaction design patterns are proven solutions to recurring interface problems. They work because they match established user mental models — users already know how to use them. The best interaction design is invisible: users achieve their goals without thinking about the interface.

This knowledge pack covers the foundational laws, heuristics, and patterns that interaction designers apply daily. These are not trends — they are principles grounded in cognitive science and decades of interface research.

---

## Frameworks

### Gestalt Principles Applied to UI

**When to use**: Whenever arranging elements on a screen. Gestalt principles explain how users perceive visual grouping, which directly determines how they understand interface structure.

**How it works**: The human visual system automatically groups and organizes visual information. These grouping rules are predictable and can be exploited in design.

**Key principles for UI:**

| Principle | Rule | UI Application |
|-----------|------|----------------|
| **Proximity** | Elements near each other are perceived as a group | Group related form fields. Separate sections with whitespace. |
| **Similarity** | Elements that look alike are perceived as related | Style related actions consistently. Use same treatment for same function. |
| **Continuity** | Eyes follow smooth paths | Align elements in rows/columns. Use visual lines to connect related items. |
| **Closure** | Mind completes incomplete shapes | Card components work because users "close" the boundary mentally. |
| **Common Region** | Elements in the same bounded area are grouped | Use cards, borders, and background colors to group related content. |
| **Figure/Ground** | Users separate foreground from background | Use modals, overlays, and depth (shadow) to create clear layers. |

**Template for applying Gestalt:**
- Before finalizing any layout, ask: "If I squint at this screen, do the right things group together?"
- Use proximity BEFORE using borders. Whitespace is more effective than boxes.
- Test grouping by asking someone unfamiliar: "What goes with what on this screen?"

**Limitations**: Gestalt principles are perceptual, not behavioral. They tell you how users will see the layout, not how they will interact with it. Combine with task analysis for complete interaction design.

---

### Fitts's Law and Target Sizing

**When to use**: Whenever placing interactive elements — buttons, links, menu items, form controls. Fitts's Law governs how easily users can click or tap targets.

**How it works**: The time to reach a target is a function of the distance to the target and the size of the target. Closer and larger = faster and easier.

**Formula** (simplified): `Time = a + b * log2(Distance/Size + 1)`

**Practical UI implications:**

| Guideline | Minimum Size | Reasoning |
|-----------|-------------|-----------|
| Touch target (mobile) | 44x44 px (Apple), 48x48 dp (Material) | Finger pad is approximately 10mm |
| Click target (desktop) | 24x24 px minimum | Mouse cursor precision is higher |
| Primary action buttons | Largest interactive element on screen | Reduce time to most common action |
| Destructive actions | Smaller, away from primary | Increase time to accidental execution |

**Key patterns:**
- **Put primary actions in easy-to-reach zones**: Bottom of mobile screens (thumb zone), corners of desktop screens (infinite edge targets)
- **Group related actions together**: Reduce movement between sequential steps
- **Never put destructive and constructive actions next to each other**: "Save" and "Delete" side by side is a design failure
- **Use the full screen edges**: Targets at screen edges have infinite height/width in one direction (scrollbar, menu bar)

**Limitations**: Fitts's Law assumes the user knows where the target is. If they can't find the button, target size doesn't matter. Combine with visual hierarchy (make important things visible) and Gestalt (make things findable through grouping).

---

### Hick's Law and Choice Architecture

**When to use**: When designing menus, navigation, settings, or any interface where users must choose from options. Hick's Law governs how decision time scales with the number of choices.

**How it works**: Decision time increases logarithmically with the number of choices. More options = slower decisions = more cognitive load.

**Formula** (simplified): `Time = a + b * log2(n + 1)` where n = number of choices

**Practical UI implications:**
- **Reduce visible options**: Show 5-7 items maximum in a menu or group. Use progressive disclosure for more.
- **Categorize**: Group 30 items into 5 categories of 6 items each. Two simple decisions beat one complex decision.
- **Highlight recommended**: When there's a clear best choice, visually emphasize it. Reduces decision to "accept recommendation" vs. "explore alternatives."
- **Progressive disclosure**: Show basic options first. Reveal advanced options behind an "Advanced" toggle.
- **Smart defaults**: Pre-select the most common choice. Users who agree with the default don't need to decide at all.

**Template for choice architecture:**
```
Decision: [What the user is choosing]
Options: [Full list]
Recommended: [Which option and why]
Categories: [How options are grouped]
Default: [Pre-selected option]
Progressive disclosure: [What's hidden initially]
```

**Limitations**: Hick's Law applies to choices where all options are equally familiar. Expert users scanning a known menu are fast regardless of length. Context matters: a phone contact list with 500 entries works because users search/scroll, not scan.

---

### Nielsen's 10 Usability Heuristics

**When to use**: As a evaluation framework for any interface. These heuristics are the most widely-used checklist for identifying usability problems. Use them in heuristic evaluations, design reviews, and self-assessment.

**How it works**: Evaluate the interface against each heuristic. Rate severity of violations (0=not a problem, 4=catastrophe). Prioritize fixes by severity.

| # | Heuristic | What It Means | Common Violation |
|---|-----------|---------------|------------------|
| 1 | **Visibility of system status** | Users know what's happening | No loading indicator, no success confirmation |
| 2 | **Match between system and real world** | Uses familiar language and concepts | Technical jargon, unfamiliar icons |
| 3 | **User control and freedom** | Easy undo, clear exits | No back button, no cancel option, no undo |
| 4 | **Consistency and standards** | Same action = same result everywhere | Different patterns for similar functions |
| 5 | **Error prevention** | Prevent errors before they happen | No confirmation for destructive actions |
| 6 | **Recognition over recall** | Show options rather than require memory | Hidden commands, empty states with no guidance |
| 7 | **Flexibility and efficiency** | Shortcuts for experts, simplicity for novices | No keyboard shortcuts, no bulk actions |
| 8 | **Aesthetic and minimalist design** | Show only what's relevant | Cluttered screens, irrelevant information |
| 9 | **Help users recognize and recover from errors** | Clear error messages with solutions | "Error 500", vague "Something went wrong" |
| 10 | **Help and documentation** | Searchable, task-focused help | No help, or help that only describes features (not tasks) |

**Severity rating scale:**
- **0**: Not a usability problem
- **1**: Cosmetic — fix if time allows
- **2**: Minor — low priority fix
- **3**: Major — important to fix, high priority
- **4**: Catastrophe — must fix before release

**Limitations**: Heuristic evaluation is expert-based, not user-based. Evaluators may miss problems that real users encounter, and flag problems that don't actually affect users. Always complement heuristic evaluation with usability testing.

---

### Navigation Patterns

**When to use**: When structuring how users move through the product. Navigation is the skeleton of the user experience.

**How it works**: Different navigation patterns suit different content structures and user tasks.

**Pattern comparison:**

| Pattern | Best For | Limitations |
|---------|----------|-------------|
| **Tab bar** (mobile) | 3-5 primary destinations | Doesn't scale beyond 5 |
| **Sidebar** (desktop) | Deep hierarchies, 10+ sections | Steals horizontal space |
| **Breadcrumbs** | Deep hierarchies, need for orientation | Requires clear parent-child structure |
| **Mega menu** | Large sites with many categories | Complex, can overwhelm |
| **Hub and spoke** | Task-focused apps (settings, search) | Returns to hub between tasks |
| **Hamburger menu** | Secondary navigation, limited space | Hides content, reduces discoverability |
| **Bottom sheet** (mobile) | Contextual actions, filters | Can obscure content |

**Navigation design principles:**
- **Persistent navigation** for primary destinations (always visible)
- **Contextual navigation** for secondary (appears in context)
- **Progressive navigation** for deep hierarchies (breadcrumbs + local nav)
- **Maximum 3 levels deep** before users lose orientation
- **Current location** must always be clear (active state, breadcrumbs)

**Limitations**: No single navigation pattern works for all products. Match the pattern to content structure and user tasks. Test with tree testing (text-only navigation) before committing to visual design.

---

### Form Design Patterns

**When to use**: Any interface where users input data — registration, settings, search, checkout, data entry.

**How it works**: Form design patterns reduce error rates, increase completion rates, and minimize frustration.

**Key patterns:**

| Pattern | What It Does | When to Use |
|---------|-------------|-------------|
| **Single-column layout** | One field per row, top-aligned labels | Default for all forms — highest completion rate |
| **Inline validation** | Validate as user moves to next field | Email format, password strength, required fields |
| **Progressive disclosure** | Show fields as they become relevant | Complex forms with conditional logic |
| **Smart defaults** | Pre-fill with most common value | Country, date format, currency |
| **Field masking** | Format as user types (phone, credit card) | Structured data entry |
| **Floating labels** | Label moves above field when focused | Space-constrained forms |
| **Error messaging** | Show error next to the field, not in a banner | All validation errors |

**Form design principles:**
- **Ask only what you need** — Every field reduces completion rate
- **Mark optional, not required** — If most fields are required, mark the exceptions
- **Group related fields** — Use fieldsets and visual grouping (Gestalt proximity)
- **Disable submit until valid** only if you also show what's wrong — otherwise users can't tell why the button is disabled
- **Preserve input on error** — Never clear the form when validation fails

**Limitations**: Form best practices are well-established but context-dependent. A checkout form and a complex data entry form have different optimal patterns. Always test forms with real users and real data.

---

### Error Handling Patterns

**When to use**: Every interactive system. Errors are inevitable — the design question is how to handle them gracefully.

**How it works**: Error handling design has three layers: prevention, detection, and recovery.

**Layer 1 — Prevention:**
- Constrain inputs (dropdowns instead of free text)
- Disable invalid actions (gray out unavailable options)
- Confirm destructive actions (modal before delete)
- Auto-save to prevent data loss

**Layer 2 — Detection:**
- Inline validation (validate on blur, not on every keystroke)
- Form-level validation (check relationships between fields)
- Server-side validation (always — client-side is convenience, not security)

**Layer 3 — Recovery:**
- **Clear error message**: What went wrong, in plain language
- **Specific guidance**: How to fix it, step by step
- **Preserve context**: Don't lose the user's work
- **Easy retry**: One-click retry for transient errors
- **Undo**: Reverse the action that caused the error

**Error message format:**
```
[What happened] + [Why it happened] + [How to fix it]

"Your password must be at least 8 characters. Add 3 more characters to continue."

NOT: "Error: Invalid input"
NOT: "Something went wrong. Please try again."
```

**Limitations**: Error handling adds complexity. Over-validation (validating every keystroke) is as bad as no validation (users get frustrated by premature errors). Validate at the right moment: on blur for individual fields, on submit for form-level rules.

---

### Responsive Breakpoint Strategies

**When to use**: Any product that must work across screen sizes — which is effectively every product.

**How it works**: Responsive design adapts layout, navigation, and content presentation based on viewport size.

**Common breakpoint system:**

| Breakpoint | Width | Typical Devices |
|------------|-------|-----------------|
| xs | < 576px | Small phones |
| sm | 576-767px | Large phones, small tablets |
| md | 768-991px | Tablets |
| lg | 992-1199px | Small laptops |
| xl | 1200-1399px | Desktops |
| xxl | 1400px+ | Large desktops |

**Responsive design strategies:**

| Strategy | How It Works | When to Use |
|----------|-------------|-------------|
| **Reflow** | Content stacks vertically at small sizes | Multi-column layouts |
| **Reveal/hide** | Show/hide elements by viewport | Supplementary content |
| **Transform** | Component changes form (tabs to accordion) | Navigation, complex components |
| **Scale** | Element sizes adjust proportionally | Typography, spacing, images |
| **Prioritize** | Reorder content by importance at small sizes | Feature-rich pages |

**Mobile-first approach:**
1. Design for the smallest viewport first
2. Add complexity as viewport grows
3. This forces content prioritization
4. CSS: start with mobile styles, add `min-width` media queries

**Limitations**: Breakpoints are a simplification. Real devices have thousands of viewport sizes. Design with fluid values (%, rem, vw) between breakpoints, not just at breakpoints. Test on real devices, not just browser resizing.

---

## Decision Framework

When selecting interaction patterns, ask:

1. **Is there an established convention?** → Use it (users already know it)
2. **Does it match the user's mental model?** → Test to confirm
3. **Is it the simplest solution?** → Simpler almost always wins
4. **Does it work with keyboard/screen reader?** → If not, find another pattern
5. **Does it work on all target devices?** → If not, adapt per breakpoint

---

## React Compiler & shadcn Registry (as of 2026-06-24)

*Added 2026-06-24 (DD-14).* **Adapted from**: React Compiler 1.0 (facebook/react#31924); shadcn registry (ui.shadcn.com/docs/changelog "June 2026 — GitHub Registries"). **Source licence**: publicly documented.

- **Drop manual memoization in new component code.** React Compiler 1.0 (stable) auto-memoizes at build time — manual `useMemo`/`useCallback`/`React.memo` is the **escape hatch** (`"use no memo"` to opt a component out), not the default. Keep manual memoization only for effect-dependency control or where the compiler is explicitly disabled. (Full nuance in framework-specific performance guidance.)
- **shadcn registry is now a distribution platform, not just components.** A a registry manifest / GitHub registry distributes components, hooks, utilities, design tokens, pages, config, docs, **agent rules/instructions, CI workflows, templates, and MCP files** — the registry is a code-and-config distribution mechanism, not only a UI source. Relevant when standardizing component + agent-rule distribution across projects.

---

## References

- Jakob Nielsen, *10 Usability Heuristics for User Interface Design* (1994)
- Paul Fitts, *The Information Capacity of the Human Motor System* (1954)
- William Edmund Hick, *On the Rate of Gain of Information* (1952)
- Luke Wroblewski, *Web Form Design* (2008)
- Material Design Guidelines, Apple Human Interface Guidelines


## Common Pitfalls

- Mobile interaction patterns differ from desktop — don't assume patterns transfer
- Loading states and error states are part of the design — don't treat them as afterthoughts
- Animation should serve function (feedback, orientation) — decorative animation can harm usability
