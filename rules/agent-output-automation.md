# Agent Output Automation (Personal - Outside OS)

This rule automates post-processing of meaningful agent deliverables. **Not part of the Product Org OS.**

---

## The Rule

After meaningful agent work completes, automatically create **one** HTML presentation and open it in the browser.

**Critical distinction — Single vs. Multi-Agent engagements:**

| Engagement Type | Presentation Behavior |
|-----------------|----------------------|
| **Single agent** (one `/pbaw` spawn) | Present that agent's deliverable directly |
| **Multi-agent** (harness-selected agent sets, parallel agents) | **ONE presentation only** — a storytelling synthesis of all agents' work |

### Multi-Agent Rule (NON-NEGOTIABLE)

When multiple agents are spawned in the same engagement:

1. **Do NOT** run the handler after each individual agent finishes
2. **Wait** until all agents have completed and synthesis is done
3. **Create one synthesis MD file** that tells the story:
   - Narrative arc, not a dump of individual outputs
   - Weave agent perspectives into a coherent storyline
   - Use agent attributions naturally within the narrative ("As the VP Product noted..." / "The competitive analysis revealed...")
   - End with aligned recommendations / decisions / next steps
4. **Run the handler once** on the synthesis file
5. Individual agent files are still saved to their proper locations for reference

### What Counts as "Meaningful Deliverable"

| Include | Exclude |
|---------|---------|
| PRDs, specs, analysis docs | Simple Q&A responses |
| Strategy documents | Status checks |
| Review findings (saved to file) | Context recalls |
| Presentations, reports | Error messages |
| Any document agent creates | Inline conversation |

**Rule of thumb:** If the agent created or significantly updated a file, run the handler.

---

## How to Trigger

After agent work completes (and synthesis is ready, if multi-agent), run:

```bash
python "agent-output-handler.py" "<path-to-md-file>" --no-telegram --brand <project-brand>
```

> **Referenced by the spawn protocol (§2.7 Output & Presentation Contract).** This rule is the *mechanics* layer behind the protocol's presentation contract. The **default** path (`md_to_mobile_html`) already produces a **branded + commentable** deck — inline commenting is always-on, no flag needed — so the orchestrator passes only `--brand <project-brand>` (brand auto-selected by the project; the handler also path/title-auto-detects). **Do NOT pass `--commentable`** — that flag selects a separate legacy prototype renderer (`md_to_commentable_html`) that is *unbranded*; it exists for the HTML-passthrough case, not for branded markdown decks. For **multi-agent** decks, the one storytelling synthesis MD may carry **one slide per agent** by separating agent-voice sections with a markdown `---` (a hard slide-break the handler honors). If this rule is absent on a fresh install, the protocol's graceful fallback applies (produce the MD + print the exact handler command).

### Options

| Flag | Effect |
|------|--------|
| `--no-telegram` | Skip Telegram notification (ALWAYS use this) |
| `--no-browser` | Don't auto-open in browser |
| `--json` | Output result as JSON |

Inline commenting is always enabled in all presentations (no flag needed).

---

## Automatic Invocation Pattern

### Single Agent

```
1. User: "ext-architecture review the PRD"
2. Agent creates: "examples/architecture-review.md"
3. Run handler on that file → browser opens
```

### Multi-Agent (Parallel)

```
1. User: "/pbaw evaluate the launch plan"
2. The harness spawns product-manager, director-product-marketing, product-operations (each saves their own file)
3. DO NOT run handler after each agent
4. Synthesize into one storytelling MD: "examples/launch-plan-evaluation.md"
   - Narrative structure, not agent-by-agent sections
   - Tells the story: context → key findings → tensions → recommendations
5. Run handler ONCE on the synthesis file → browser opens
```

---

## Self-Check (MANDATORY)

After completing ANY agent task that produced a file, ask:

- [ ] Did an agent create or update a document file?
- [ ] Is it a meaningful deliverable (not just a lookup)?
- [ ] **Is this a multi-agent engagement?**
  - YES → Have all agents finished and is synthesis complete? Only then run handler.
  - NO → Run handler now.

**If all checks pass:** Run the output handler **once**.

---

> *Relocated 2026-08-15 (DR-2026-262): handler behavior description (reference; the binding format spec is presentation-format.md and the trigger command above) — full text in the companion agent-output-automation.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

---

## File Locations

| Component | Path |
|-----------|------|
| Handler script | `agent-output-handler.py` |
| Presentations output | `presentations\` (GitHub: `your-org/presentations`) |
| This rule | `.claude\rules\agent-output-automation.md` |
