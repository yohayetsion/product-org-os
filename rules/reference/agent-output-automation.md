# Companion — agent-output-automation (relocated reference)

> Relocated rationale/reference — the binding rule is `.claude/rules/agent-output-automation.md`;
> this file imposes nothing and relaxes nothing. Moved VERBATIM 2026-08-15
> (DR-2026-262). Do not edit here
> without the same review the rule itself requires.

---

<!-- from agent-output-automation · REFERENCE-MOVE · handler behavior description -->

## What the Handler Does

1. **Reads the MD file** and splits by `## ` headers into slides
2. **Converts to brand-adaptive slide-based HTML** with nav bar, keyboard/touch navigation
3. **Auto-detects brand** («Security Vendor»/«AI Platform»/«DTC Brand»/«Design Agency») and sets colors + favicon accordingly
4. **Wraps all content blocks** in `.commentable` divs (inline commenting is always-on)
5. **Adds Review slide** (last slide) with comment export (Markdown/JSON)
6. **Saves to** `presentations\`
7. **Opens in browser**

Full template specification: `knowledge/os-support/templates/presentations/TEMPLATE-REFERENCE.md`
