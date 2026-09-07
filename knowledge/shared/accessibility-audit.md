# Accessibility Audit — Frameworks & Methods

## Overview

Accessibility is not a feature — it is a quality attribute. Products that exclude users with disabilities fail a basic test of professional design. Accessibility compliance (WCAG 2.2 AA) is also a legal requirement in most markets, and accessibility improvements consistently benefit all users, not just those with permanent disabilities.

This knowledge pack covers the complete methodology for conducting accessibility audits: from automated scanning through manual keyboard and screen reader testing, to a structured output format that engineering teams can act on. These frameworks apply to web products, mobile applications, and internal tools alike.

**Primary Users**: `ui-designer`, `design-dir`, `user-researcher`, `interaction-designer`

---

## WCAG 2.2 AA Quick Reference

WCAG (Web Content Accessibility Guidelines) 2.2 is organized around four principles: Perceivable, Operable, Understandable, and Robust. Level AA is the legally recognized and industry-standard compliance target.

### Principle 1: Perceivable

Information and UI components must be presentable to users in ways they can perceive.

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| 1.1.1 Non-text Content | A | All images, icons, and non-text elements have text alternatives |
| 1.2.1 Audio-only / Video-only | A | Pre-recorded audio/video has transcript or audio description |
| 1.2.2 Captions (Pre-recorded) | A | All pre-recorded video has captions |
| 1.2.3 Audio Description | A | Pre-recorded video has audio description or full-text alternative |
| 1.2.4 Captions (Live) | AA | Live video has captions |
| 1.2.5 Audio Description (Pre-recorded) | AA | Pre-recorded video has audio description |
| 1.3.1 Info and Relationships | A | Structure, relationships conveyed through markup, not just visual presentation |
| 1.3.2 Meaningful Sequence | A | Reading/navigation order is logical and intentional |
| 1.3.3 Sensory Characteristics | A | Instructions don't rely solely on shape, size, location, or color |
| 1.3.4 Orientation | AA | Content is not restricted to a single display orientation |
| 1.3.5 Identify Input Purpose | AA | Form inputs have programmatic purpose (autocomplete attributes) |
| 1.4.1 Use of Color | A | Color is not the only means of conveying information |
| 1.4.2 Audio Control | A | Auto-playing audio can be paused/stopped |
| 1.4.3 Contrast (Minimum) | AA | Normal text: 4.5:1; Large text: 3:1 contrast ratio |
| 1.4.4 Resize Text | AA | Text can be resized to 200% without loss of content/functionality |
| 1.4.5 Images of Text | AA | Live text used instead of images of text (except logos) |
| 1.4.10 Reflow | AA | Content reflows at 320px width without horizontal scrolling |
| 1.4.11 Non-text Contrast | AA | UI components and graphics: 3:1 contrast ratio against adjacent colors |
| 1.4.12 Text Spacing | AA | No content loss when line-height, letter-spacing, word-spacing overridden |
| 1.4.13 Content on Hover or Focus | AA | Hover/focus tooltips are persistent, dismissable, and hoverable |

### Principle 2: Operable

UI components and navigation must be operable by all users.

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| 2.1.1 Keyboard | A | All functionality available via keyboard |
| 2.1.2 No Keyboard Trap | A | Focus can always be moved away from any component |
| 2.1.4 Character Key Shortcuts | A | Single-character keyboard shortcuts can be disabled or remapped |
| 2.2.1 Timing Adjustable | A | Time limits can be turned off, adjusted, or extended |
| 2.2.2 Pause, Stop, Hide | A | Moving/blinking/scrolling content can be paused |
| 2.3.1 Three Flashes or Below | A | No content flashes more than 3 times per second |
| 2.4.1 Bypass Blocks | A | Skip navigation link provided to bypass repeated content |
| 2.4.2 Page Titled | A | Pages have descriptive titles |
| 2.4.3 Focus Order | A | Focus order preserves meaning and operability |
| 2.4.4 Link Purpose (In Context) | A | Link text is meaningful in context |
| 2.4.5 Multiple Ways | AA | Multiple ways to locate a page within a site |
| 2.4.6 Headings and Labels | AA | Headings and labels are descriptive |
| 2.4.7 Focus Visible | AA | Keyboard focus indicator is visible |
| 2.4.11 Focus Not Obscured (Minimum) | AA | Focused component is not entirely hidden by sticky elements |
| 2.5.1 Pointer Gestures | A | Multi-point gestures have single-pointer alternatives |
| 2.5.2 Pointer Cancellation | A | Click/down events can be cancelled before activation |
| 2.5.3 Label in Name | A | Accessible name contains visible label text |
| 2.5.4 Motion Actuation | A | Functionality from motion has an alternative UI control |
| 2.5.7 Dragging Movements | AA | Dragging has a single-pointer alternative |
| 2.5.8 Target Size (Minimum) | AA | Touch targets are at least 24x24 CSS pixels |

### Principle 3: Understandable

Information and the operation of UI must be understandable.

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| 3.1.1 Language of Page | A | Language of page is programmatically determinable |
| 3.1.2 Language of Parts | AA | Language of page sections is programmatically determinable |
| 3.2.1 On Focus | A | No context changes when component receives focus |
| 3.2.2 On Input | A | No context changes when user changes input settings (unless warned) |
| 3.2.3 Consistent Navigation | AA | Navigation that repeats across pages appears in same location |
| 3.2.4 Consistent Identification | AA | Components with same function are identified consistently |
| 3.3.1 Error Identification | A | Input errors identified and described to the user in text |
| 3.3.2 Labels or Instructions | A | Labels or instructions provided for user input |
| 3.3.3 Error Suggestion | AA | Error suggestions provided when known |
| 3.3.4 Error Prevention (Legal, Financial) | AA | Legal/financial submissions can be checked, confirmed, or reversed |

### Principle 4: Robust

Content must be robust enough to be interpreted by assistive technologies.

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| 4.1.2 Name, Role, Value | A | UI components have name, role, and value programmatically determinable |
| 4.1.3 Status Messages | AA | Status messages can be determined programmatically without focus |

---

## Color Contrast Requirements

| Text Type | Minimum Ratio (AA) | Enhanced Ratio (AAA) |
|-----------|-------------------|---------------------|
| Normal body text (< 18pt / < 14pt bold) | 4.5:1 | 7:1 |
| Large text (>= 18pt or >= 14pt bold) | 3:1 | 4.5:1 |
| UI component boundaries | 3:1 | 3:1 |
| Graphical objects (charts, icons) | 3:1 | 3:1 |
| Disabled/inactive elements | Exempt | Exempt |
| Logo/decorative text | Exempt | Exempt |
| Placeholder text in inputs | 4.5:1 | 7:1 |
| Text in focus indicators | 3:1 | 4.5:1 |

**Measurement rule**: Measure contrast between foreground text and the immediate background it sits on — not the page background. Account for opacity and overlays.

---

## Touch Target Size Requirements

| Standard | Minimum Size | Recommended | Applies To |
|----------|-------------|-------------|------------|
| WCAG 2.5.8 (AA) | 24 x 24 CSS px | 44 x 44 CSS px | All interactive targets |
| WCAG 2.5.5 (AAA) | 44 x 44 CSS px | 44 x 44 CSS px | All interactive targets |
| Apple HIG | 44 x 44 pt | 44 x 44 pt | iOS UI |
| Material Design | 48 x 48 dp | 48 x 48 dp | Android UI |

**Spacing rule**: When targets do not meet the minimum size, they must have at least 24px of clear space around them (no other targets in the zone). The target itself OR its clear space must together cover the 24x24 minimum.

**Exception**: Inline text links are exempt from size requirements when they are part of a sentence or paragraph.

---

## Common Accessibility Issues — Severity Ratings

### Critical (P0) — Blocks access entirely

| Issue | WCAG Criterion | Common Cause |
|-------|----------------|--------------|
| Images with no alt text | 1.1.1 | `<img>` without `alt` attribute |
| Interactive elements with no accessible name | 4.1.2 | Icon-only buttons with no `aria-label` |
| Keyboard focus trap | 2.1.2 | Modal or overlay that doesn't release focus |
| All functionality keyboard-inaccessible | 2.1.1 | Custom JS interactions without keyboard event handlers |
| Form inputs with no associated label | 1.3.1 / 4.1.2 | Placeholder-only labels, or `for`/`id` mismatch |
| Error messages not associated with inputs | 3.3.1 | Error text not linked via `aria-describedby` |
| Content only distinguishable by color | 1.4.1 | Required field asterisks, error states with no text |

### Major (P1) — Significantly degrades experience

| Issue | WCAG Criterion | Common Cause |
|-------|----------------|--------------|
| Insufficient color contrast | 1.4.3 / 1.4.11 | Light grey text on white, low-contrast placeholder text |
| Focus indicator not visible | 2.4.7 | `outline: none` in CSS without replacement |
| Focus order illogical | 2.4.3 | DOM order differs from visual order; positive `tabindex` values |
| Heading hierarchy skipped | 1.3.1 | `<h1>` followed by `<h3>` |
| Link text non-descriptive | 2.4.4 | "Click here", "Read more", "Learn more" |
| Language not declared | 3.1.1 | Missing `lang` attribute on `<html>` |
| Zoom/text resize breaks layout | 1.4.4 / 1.4.10 | Fixed pixel layouts, `overflow: hidden` |
| Touch targets too small | 2.5.8 | Buttons under 24px, tight icon grids |
| Status messages not announced | 4.1.3 | Success/error toasts without `role="status"` or `aria-live` |
| Missing skip navigation | 2.4.1 | No skip link before repeated navigation blocks |

### Minor (P2) — Partial degradation, workaround exists

| Issue | WCAG Criterion | Common Cause |
|-------|----------------|--------------|
| Redundant alt text | 1.1.1 | Alt text repeats adjacent caption text |
| Title attribute misuse | 4.1.2 | `title` used as sole label (not consistently exposed) |
| Inconsistent navigation placement | 3.2.3 | Navigation moves between pages |
| Decorative images not hidden | 1.1.1 | `alt=""` missing on purely decorative images |
| Autocomplete not implemented | 1.3.5 | Standard form fields missing `autocomplete` attributes |
| Motion not respectable | 2.3.3 | Animations that don't respect `prefers-reduced-motion` |

---

## Testing Methodology — Five Layers

### Layer 1: Automated Scan

Automated tools catch approximately 30-40% of WCAG issues. They are fast and repeatable — run them first to clear low-hanging fruit before manual testing.

**Process**:
1. Install axe DevTools browser extension (Chrome or Firefox)
2. Navigate to each key page/flow
3. Run automated scan — review every violation
4. Export results as baseline
5. Verify no false positives before reporting

**What automated tools catch well**: Missing alt text, color contrast failures, missing form labels, invalid ARIA, missing page title, duplicate IDs, empty links and buttons.

**What automated tools miss**: Logical heading order, focus order, keyboard trap (without interaction), content meaning, label accuracy, cognitive load, context-dependent issues.

### Layer 2: Keyboard-Only Navigation

Navigate the entire product using only Tab, Shift+Tab, Enter, Space, and arrow keys. No mouse.

**Standard keyboard navigation checklist**:

- [ ] Tab moves focus forward through all interactive elements
- [ ] Shift+Tab moves focus backward
- [ ] Enter activates links and buttons
- [ ] Space activates buttons and checkboxes
- [ ] Arrow keys navigate within components (menus, sliders, tab panels, radio groups)
- [ ] Escape closes dialogs, dropdowns, and modals
- [ ] Focus indicator is clearly visible at all times
- [ ] Focus never gets trapped in a component (unless in a modal — that is intentional)
- [ ] Focus order follows logical reading order
- [ ] Skip links appear and function at page top
- [ ] Modals: focus moves to modal on open; focus returns to trigger on close
- [ ] Dropdowns/menus: arrow keys navigate options; Escape closes
- [ ] Carousels: arrow keys advance slides; auto-play pauses on focus
- [ ] Date pickers: keyboard navigation within the calendar grid works
- [ ] Forms: Tab navigates between fields; Enter submits on button focus

### Layer 3: Screen Reader Testing

Test with actual screen readers. Automated tools do not replicate screen reader behavior accurately.

**Recommended coverage**:
| Screen Reader | Browser | Platform | User Base |
|--------------|---------|----------|-----------|
| NVDA (free) | Chrome or Firefox | Windows | ~41% |
| JAWS | Chrome or Edge | Windows | ~53% |
| VoiceOver | Safari | macOS / iOS | ~9% |
| TalkBack | Chrome | Android | ~6% |

**Minimum viable SR test**: NVDA + Chrome (most common combination in enterprise; free).

**VoiceOver quick commands (macOS)**:
- Enable: Cmd+F5
- Next element: VO+Right (VO = Ctrl+Option)
- Read from top: VO+A
- Rotor (navigation menu): VO+U
- Navigate by heading: VO+Cmd+H
- Navigate by landmark: VO+Cmd+L

**NVDA quick commands (Windows)**:
- Enable/disable: Ctrl+Alt+N
- Browse mode / forms mode: NVDA+Space
- Next heading: H
- Navigate by landmark: D
- List all headings: NVDA+F7
- Read from top: NVDA+Down

**Screen reader testing checklist**:

- [ ] Page title is announced on load
- [ ] Heading structure is logical and navigable by heading key
- [ ] Landmark regions are present: header, nav, main, footer
- [ ] All images have meaningful alt text (or empty alt for decorative)
- [ ] Form labels are announced when input receives focus
- [ ] Error messages are announced when triggered
- [ ] Button purposes are clear (not just "button" or icon name)
- [ ] Link text is descriptive out of context
- [ ] Modal: focus announced as modal dialog; close button accessible
- [ ] Status messages announced without focus movement (live regions)
- [ ] Tables: headers announced with cell data
- [ ] Dynamic content updates announced via aria-live regions

### Layer 4: Color Contrast Check

**Manual contrast verification process**:
1. Export all text/background color combinations from design files
2. Test each pair with a contrast analyzer
3. Flag combinations below AA thresholds
4. Check UI component borders (buttons, inputs, focus indicators) at 3:1

**Edge cases to test**:
- Text on photographic/gradient backgrounds (test darkest and lightest areas)
- Placeholder text in form inputs
- Disabled element text (exempt from WCAG, but note if very low)
- Text rendered on top of semi-transparent overlays
- Focus ring color against all backgrounds it appears on

### Layer 5: Zoom and Reflow Testing

- [ ] Set browser zoom to 200% — verify no content is lost or overlapping
- [ ] Set browser zoom to 400% — verify content reflows to single column (1.4.10)
- [ ] Increase OS text size to maximum — verify layout does not break
- [ ] Test at 320px viewport width — verify no horizontal scrolling required
- [ ] Verify `prefers-reduced-motion: reduce` disables decorative animations

---

## ARIA Patterns Quick Reference

### Landmark Roles

| Role | HTML Equivalent | Usage |
|------|----------------|-------|
| `banner` | `<header>` | Main site header (once per page) |
| `navigation` | `<nav>` | Navigation sections (label each: `aria-label="Main"`) |
| `main` | `<main>` | Primary content area |
| `complementary` | `<aside>` | Supporting content |
| `contentinfo` | `<footer>` | Site footer |
| `search` | `<search>` / `role="search"` | Search widget or form |
| `form` | `<form>` | Form with accessible name |
| `region` | Sectioned content | Any section with `aria-labelledby` |

### Common Widget Roles

| Pattern | Role | Key Attributes |
|---------|------|----------------|
| Accordion | `button` on header, `region` on panel | `aria-expanded`, `aria-controls` |
| Alert dialog | `alertdialog` | `aria-modal="true"`, `aria-labelledby`, `aria-describedby` |
| Breadcrumb | `nav` with `aria-label="Breadcrumb"` | `aria-current="page"` on last item |
| Combobox / Autocomplete | `combobox` on input | `aria-expanded`, `aria-autocomplete`, `aria-controls` |
| Dialog / Modal | `dialog` | `aria-modal="true"`, `aria-labelledby` |
| Menu | `menu`, `menuitem` | `aria-haspopup`, `aria-expanded` on trigger |
| Progress indicator | `progressbar` | `aria-valuenow`, `aria-valuemin`, `aria-valuemax` |
| Slider | `slider` | `aria-valuenow`, `aria-valuemin`, `aria-valuemax`, `aria-label` |
| Tab panel | `tablist`, `tab`, `tabpanel` | `aria-selected`, `aria-controls`, `aria-labelledby` |
| Toggle button | `button` | `aria-pressed="true/false"` |
| Tooltip | `tooltip` | `aria-describedby` on trigger pointing to tooltip |

### States and Properties Reference

| Attribute | Values | Use When |
|-----------|--------|----------|
| `aria-expanded` | `true` / `false` | Collapsible elements (accordion, dropdown, menu) |
| `aria-pressed` | `true` / `false` / `mixed` | Toggle buttons |
| `aria-checked` | `true` / `false` / `mixed` | Checkboxes, radio buttons, switch |
| `aria-selected` | `true` / `false` | Tabs, list options, grid cells |
| `aria-disabled` | `true` / `false` | Unavailable but visible elements |
| `aria-hidden` | `true` / `false` | Decorative elements to hide from AT |
| `aria-live` | `polite` / `assertive` | Dynamic regions that update without focus |
| `aria-atomic` | `true` / `false` | Whether entire live region is re-read on update |
| `aria-busy` | `true` / `false` | Content loading / updating |
| `aria-required` | `true` / `false` | Required form fields |
| `aria-invalid` | `true` / `false` / `grammar` / `spelling` | Invalid form inputs |
| `aria-label` | string | Accessible name when no visible label |
| `aria-labelledby` | ID reference | Accessible name from another element |
| `aria-describedby` | ID reference | Additional description (error messages, hints) |

**Rule of thumb**: Use native HTML semantics first. Add ARIA only when native semantics are insufficient. Bad ARIA is worse than no ARIA.

---

## Mobile Accessibility Considerations

Mobile accessibility extends beyond touch target sizing. Key areas unique to mobile contexts:

**Gestures**:
- All multi-finger gestures must have a single-tap alternative (2.5.1)
- Swipe gestures must be operable with assistive technology (TalkBack/VoiceOver swipe navigation)
- Drag-and-drop operations must have a tap-to-select + tap-to-place alternative

**Screen reader mode**:
- VoiceOver (iOS) and TalkBack (Android) use touch-based exploration — swipe to next element, double-tap to activate
- Test that interactive elements are reachable by swipe navigation, not just visual tapping
- Avoid relying on long-press for primary actions — screen readers intercept long-press

**Orientation**:
- Content must work in both portrait and landscape (1.3.4)
- Exception: Video viewers and certain games have legitimate orientation locks

**System font scaling**:
- Test with iOS Dynamic Type set to Accessibility sizes (XXL and above)
- Test with Android font size set to largest
- Layouts must accommodate text at 200% without clipping or overlap

**Custom gestures in native apps**:
- Provide accessibility actions (`UIAccessibilityCustomAction` / `AccessibilityAction`) as alternatives to custom swipe patterns
- Avoid gesture conflicts with OS-level accessibility gestures

---

## Audit Output Template

Use this format for accessibility audit reports. One findings table per WCAG principle.

```markdown
# Accessibility Audit Report

**Product**: [Product Name]
**Version / Build**: [version]
**Audit Date**: [YYYY-MM-DD]
**Auditor**: [Name / Team]
**Scope**: [Pages/flows tested]
**Standard**: WCAG 2.2 Level AA
**Tools Used**: [axe DevTools, NVDA + Chrome, VoiceOver, Colour Contrast Analyser]

---

## Executive Summary

| Severity | Count | Blocking? |
|----------|-------|-----------|
| Critical (P0) | [n] | Yes |
| Major (P1) | [n] | Partial |
| Minor (P2) | [n] | No |
| **Total** | [n] | |

**Overall Status**: [Pass / Conditional Pass / Fail]

---

## Principle 1: Perceivable

| ID | Criterion | Page / Component | Issue | Severity | Recommendation |
|----|-----------|-----------------|-------|----------|----------------|
| A-001 | 1.1.1 | [location] | [description] | P0/P1/P2 | [fix] |

## Principle 2: Operable

| ID | Criterion | Page / Component | Issue | Severity | Recommendation |
|----|-----------|-----------------|-------|----------|----------------|
| B-001 | 2.1.1 | [location] | [description] | P0/P1/P2 | [fix] |

## Principle 3: Understandable

| ID | Criterion | Page / Component | Issue | Severity | Recommendation |
|----|-----------|-----------------|-------|----------|----------------|
| C-001 | 3.1.1 | [location] | [description] | P0/P1/P2 | [fix] |

## Principle 4: Robust

| ID | Criterion | Page / Component | Issue | Severity | Recommendation |
|----|-----------|-----------------|-------|----------|----------------|
| D-001 | 4.1.2 | [location] | [description] | P0/P1/P2 | [fix] |

---

## Remediation Priorities

### P0 — Resolve before launch
[List of critical issues with assigned owner and target date]

### P1 — Resolve within [sprint/timeframe]
[List of major issues]

### P2 — Resolve in backlog prioritization
[List of minor issues]

---

## Re-test Checklist
- [ ] P0 issues verified as resolved
- [ ] Regression test: previously passing criteria still pass
- [ ] Screen reader re-test for changed components
```

---

## Remediation Priority Framework

### P0 — Critical: Resolve Before Launch

**Definition**: Issues that completely block access for one or more disability groups. The product is unusable without resolving these.

**Examples**: Keyboard traps, missing form labels, content only accessible by color, all functionality requiring a mouse.

**Resolution SLA**: Must be resolved before any production release. These are launch blockers.

**Escalation**: If resolution is not feasible before launch, the feature must be gated or removed from scope.

### P1 — Major: Resolve Within Current Sprint or Next Sprint

**Definition**: Issues that significantly degrade the experience for users with disabilities. Workarounds may exist, but the experience is materially worse.

**Examples**: Insufficient color contrast, invisible focus indicators, non-descriptive link text, missing skip navigation, broken heading hierarchy.

**Resolution SLA**: Resolve within the current sprint for pre-launch products. For live products, resolve within 1-2 sprint cycles.

### P2 — Minor: Backlog Prioritization

**Definition**: Issues that cause partial degradation with functional workarounds available. Users can still complete their task, but with friction.

**Examples**: Redundant alt text, missing autocomplete attributes, inconsistent navigation placement, decorative images not hidden from AT.

**Resolution SLA**: Prioritize against other backlog items. Address in quarterly accessibility sprints.

---

## Tools Reference

### Automated Scanners

| Tool | Type | Best For | Free? |
|------|------|----------|-------|
| **axe DevTools** | Browser extension | Comprehensive automated scan, CI integration | Core free, Pro paid |
| **Lighthouse** | Browser built-in (Chrome) | Quick accessibility score, CI audits | Yes |
| **WAVE** | Browser extension | Visual overlay on page, educational | Yes |
| **IBM Equal Access Checker** | Browser extension | WCAG 2.1/2.2 + IBM rules | Yes |
| **Deque axe-core** | npm package | CI/CD pipeline integration | Yes |
| **Playwright/Cypress + axe** | Testing framework | Automated regression testing | Yes |

### Color Contrast Analyzers

| Tool | Platform | Features |
|------|----------|---------|
| **Colour Contrast Analyser** (TPGi) | Desktop (Win/Mac) | Pick colors from screen, APCA support |
| **WebAIM Contrast Checker** | Web | URL-based, AA/AAA thresholds |
| **Stark** | Figma / Sketch plugin | In-design contrast checking, simulation |
| **Leonardo** (Adobe) | Web | Contrast-compliant color palette generation |

### Screen Reader Testing

| Tool | Platform | Cost |
|------|----------|------|
| **NVDA** | Windows | Free |
| **JAWS** | Windows | Paid (annual license ~$90-1000) |
| **VoiceOver** | macOS, iOS | Built-in (free) |
| **TalkBack** | Android | Built-in (free) |
| **Narrator** | Windows | Built-in (free) |

### Simulation Tools

| Tool | Simulates |
|------|-----------|
| NoCoffee (Chrome extension) | Visual impairments (blur, scotoma, acuity loss) |
| Silktide (Chrome extension) | Dyslexia, visual impairments, motor |
| Chrome DevTools CSS emulation | `prefers-reduced-motion`, `prefers-color-scheme` |
| Accessibility Insights for Web | Guided manual testing, FastPass |

---

*Knowledge Pack: Accessibility Audit | Team: Design | Attribution: Anthropic knowledge-work-plugins (design/accessibility-review) | Last Updated: 2026-03-29*
