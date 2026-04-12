---
name: present
description: 'Convert an existing deliverable document to an HTML slide presentation. Activate when: "make a presentation", "create slides", "convert to slides", document as presentation, present this Do
  NOT activate for: creating new content or documents (use domain skills), QBR deck creation (/qbr-deck), strategy communication (/strategy-communication)'
argument-hint: '[document-path]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 5.0.0
  category: utility
  skill_type: task-capability
---
Convert a markdown deliverable into a **self-contained, brand-adaptive HTML presentation** with inline commenting.

## Vision to Value Phase

**Cross-phase** — presentations can be created from deliverables in any phase.

## Process

1. **Run `agent-output-handler.py`** — this is the canonical generator:
   ```bash
   python "G:\My Drive\Claude\agent-output-handler.py" "<path-to-md-file>" --no-telegram
   ```
2. The script handles everything: markdown parsing, slide splitting (by `## ` headers), brand detection, HTML generation, commenting engine, and browser auto-open.
3. Output saved to `C:\dev\presentations\` with a slugified filename.

That's it. Do NOT manually generate HTML presentations — always use the handler script.

## What the Handler Produces

- **Self-contained HTML** — no external JS/CSS (only Google Fonts link)
- **Brand-adaptive** — auto-detects brand from title (AXIA, Legionis, SKYMOD, Maad House) and applies correct colors, favicon, and logo
- **Scrollable slides** — `min-height: 100vh; overflow: auto` (NEVER clips content)
- **Nav bar** — CSS Grid bottom bar with section dots, slide counter, slide dots
- **Keyboard + touch** — arrow keys, swipe, Home/End, slide jump overlay
- **Inline commenting** — always-on, every content block commentable, review slide at end with export

## Technical Reference

For CSS variables, z-index layers, IIFE scope rules, brand color table, and commenting engine internals:

**`templates/presentations/TEMPLATE-REFERENCE.md`**

## Auto-Presentation (via `agent-output-automation.md` rule)

The output automation rule triggers this automatically after any agent produces a meaningful deliverable. Manual `/present` invocation is for converting existing documents that don't yet have a presentation.

## Deliverables That Get Presentations

| Auto-Present | On Request | Never |
|---|---|---|
| Strategic Bet, Decision Record, Decision Charter, Product Vision, Roadmap Theme, GTM Brief, Pricing Model, Competitive Analysis, Launch Readiness, Outcome Review, QBR | Feature Spec | User Story |
