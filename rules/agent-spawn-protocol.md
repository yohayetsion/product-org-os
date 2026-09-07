# Agent Spawn Protocol (v2 — 2026-05-27; ROI section retired 2026-08-01)

Canonical rule for spawning, identifying, and presenting Product Org agents. Ensures sub-agents (which lack `.claude/rules/`) follow the Product Org response protocol.

> *Relocated 2026-08-15 (DR-2026-262): v1→v2 + 2026-08-01 changelog (history; the operative schema lives in §2/§3 and the spawn template) — full text in the companion agent-spawn-protocol.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

---

## 1. Agent Identity Registry

| Agent Key | Emoji | Display Name | Short |
|-----------|-------|--------------|-------|
| product-manager | 📝 | Product Manager | PM |
| cpo | 👑 | Chief Product Officer | CPO |
| vp-product | 📈 | VP Product | VP |
| director-product-management | 📋 | Director of Product Management | Dir PM |
| director-product-marketing | 📣 | Director of Product Marketing | Dir PMM |
| product-marketing-manager | 🎯 | Product Marketing Manager | PMM |
| bizops | 🧮 | BizOps | BizOps |
| bizdev | 🤝 | Business Development | BizDev |
| competitive-intelligence | 🔭 | Competitive Intelligence | CI |
| product-operations | ⚙️ | Product Operations | ProdOps |
| value-realization | 💰 | Value Realization | VR |

### Team routes (internal)

The fifteen Extension-Team routes (`ext-<team>`) are private components (`user-invocable: false`): the harness selects them, a human never types them. Three carry a presentation identity for Meeting Mode:

| Route Key | Emoji | Display Name | Short |
|-----------|-------|--------------|-------|
| ext-design | 🎨 | Design Team | Design |
| ext-architecture | 🏗️ | Architecture Team | Arch |
| ext-marketing | 📢 | Marketing Team | Mktg |

---

## 2. Mandatory Prompt Injection Template

Every Task tool call spawning a Product Org agent **MUST** prepend the **Agent Identity & Operating Protocol** block. Placeholders to substitute: `{emoji}`, `{Display Name}`, `{agent-slug}` — replace them with values from the Identity Registry (Section 1) when constructing the spawn prompt. The `{agent-slug}` substitutes the **canonical slug** from `metadata.name` in the agent's canonical SKILL.md (for example, `product-manager`, `vp-product`, `chief-architect`).

**The template payload moved out of this file (2026-08-02, Phase 2 Shipment A).** The full block — Phase 0 injected-context handling, Phase 1 self-orientation (packs and rules resolve by the runtime manifest's `requires` edges), §2.4 verify-before-declaring-missing, Phase 1.5 DR context check, Phase 2 task-specific loading, the §2.5 Spawn Audit Block schemas + rules, §2.6 inline-persona exclusion, §2.7 output & presentation contract, §2.8 machine-checkable schema, and the response rules — now lives in ONE template file, prepended verbatim at spawn construction:

- **Canonical copy**: `.pbaw/harness/pbaw/spawn-template.md` — installed from the release's runtime manifest; never hand-edited (the next install replaces it).
- **Host projections (read at spawn-construction time)**: `.claude/skills/pbaw/spawn-template.md` and `.agents/skills/pbaw/spawn-template.md` — the same bytes, marked as managed by the installer. Read it by ABSOLUTE path (the Read tool requires absolute paths; a relative `.claude/...` path is not guaranteed to resolve in spawned-agent context).


The template file is PAYLOAD, not policy: it remains governed by this rule, and any change to it is a §2 change carrying this rule's review bar. References elsewhere to §2.4–§2.8 resolve inside the template file. (The two plugin copies of this rule under `Product Org OS/product-org-plugin*/rules/` intentionally keep the full inline template — they ship self-contained.)

### Agent Identity for Tracking

When spawning agents via the Agent/Task tool, include the agent key in the description field using the format: `[agent-key] descriptive text`. Example: `[product-manager] Review the PRD for authentication`. This gives the PostToolUse hook (`../tools/hooks/os-tracker.py`) a structured way to identify the agent for ROI and interaction logging. The prompt regex (`You are **{emoji} {Display Name}**`) is used as fallback.

---

## Multi-Agent DR Ownership Rule (NON-NEGOTIABLE)

In any multi-agent run (harness-selected agent sets; parallel patterns like Brand Launch or Portfolio Review; sequenced workflows), **only ONE participant carries DR responsibility**. Sub-agents do NOT each emit DR sections.

### Ownership hierarchy

| Run shape | DR owner |
|---|---|
| Single-agent OS spawn (deliverable task) | The spawned agent |
| Single-agent ET spawn | No DR phase fires |
| Multi-domain run selected by `/pbaw` | The named senior agent owning synthesis (typically OS) |
| Portfolio / strategic trade-off review | The senior agent producing the synthesis (`cpo` or `vp-product`) |
| Parallel pattern with named synthesizer | That synthesizer |
| Parallel pattern with no synthesizer (raw outputs handed back to Claude) | **Claude itself** (the orchestrator) — runs Phase 1.5 as part of synthesis |
| Joint-authoring spawn with at least one OS author | The senior OS author |
| All-ET multi-agent run | No DR section emitted by anyone |

### Why single-owner

- **Sub-agents MAY surface candidate DRs verbally** in their individual responses ("I notice this decision is novel — worth a DR"), but only the synthesis owner commits them.
- Prevents: duplicate DR creation across sub-agents; conflicting status updates from different sub-agents; performative DR sections rubber-stamped in every sub-agent's Audit Block.
- The synthesis owner sees all sub-agent outputs and is the only participant with the full picture needed to draft a coherent DR.

### What this means for Claude (the orchestrator)

When you (Claude) coordinate a multi-agent run with no named synthesizer — for example, you spawn `product-manager`, `bizops`, and `competitive-intelligence` in parallel and then synthesize their outputs into a response to the user — **you carry the DR responsibility**. Run `/context-recall` before synthesis. Sniff during synthesis. Draft / update DRs as part of your synthesis response. Surface a `[Decision Records]` summary in your final user-facing response (Claude itself does not emit an Audit Block — this is folded into the synthesis prose with explicit DR-NNN references).

---

## 3. ROI — the computed hours model (2026-08-01)

> *Relocated 2026-08-15 (DR-2026-262): computed-hours ROI model detail — CANONICAL rule: .claude/rules/roi-display.md ("The Computed Model" + "Display Surfaces"; agents emit no ROI, hours priced from the owner-affirmed table); verbatim text preserved in the companion agent-spawn-protocol.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

**Migration note (the one legacy rule):** Audit Blocks already emitted with a `[Post-Execution ROI]` section — the historical corpus and every conveyed archive — remain **valid history, tolerated-but-ignored**: the validator no longer requires the section (its `roi_present`-gated body check still validates legacy blocks), the parser keeps reading it for the historical record, and nothing on any published path reads it. Sunset of the tolerated legacy schema lands on the next conveyance cut, not on a date.

---

## 4. Spawning Decision Tree

```
User request (`/pbaw <task>`, or any task the harness recognises as agent work) →
  1. Names a capability (/skill-name)? → Invoke the skill inline (Skill tool)
  2. Clear single-domain? → The harness selects the primary agent from the routing table (Section 6) and spawns it (Task tool)
  3. Multi-domain / ambiguous? → The harness selects the relevant canonical product agents from the Domain Ownership Map (Section 6); one named senior agent owns synthesis
  4. Portfolio / strategic trade-off? → `cpo` or `vp-product` owns synthesis; the harness adds the relevant domain agents from the portfolio roster (Section 6)
```

**Don't spawn for**: Simple factual questions, system ops, context retrieval, or active inline persona conversations. These do not emit an Audit Block.

---

## 5. Sub-Agent Spawning & Delegation

Include in agent prompts when the agent may need cross-domain expertise:

```
### Sub-Agent Spawning & Delegation
You may spawn sub-agents for expertise outside your domain.

**Delegation patterns** (see `rules/delegation-protocol.md`):
- **Consultation** (default): Spawn, integrate, attribute: "I consulted {emoji} {Name} who noted..."
- **Delegation** [DELEGATION]: Specialist owns sub-deliverable. Include scope/deliverable/constraints.
- **Review** [REVIEW]: Quality validation. Include criteria/deliverable.
- **Debate** [DEBATE]: Structured advocacy for genuine tradeoffs.
- **Adversarial Review** [ADVERSARIAL]: Fresh-context stress-test of high-stakes deliverables.

Include identity protocol in sub-agent prompts. (Sub-agent spawns are priced by the telemetry pipeline like any other spawn — you emit no ROI for them or for yourself, per §3.) **You retain DR ownership** unless you explicitly delegate synthesis.
```

---

## 6. Domain Routing Table

The harness selects agents from these declarations; a human types `/pbaw <task>`, never an agent handle. Cells name canonical slugs.

| Domain | Primary Agent | Backup |
|--------|--------------|--------|
| Requirements, PRD, user stories, delivery | `product-manager` | `director-product-management` |
| Vision, portfolio, pricing strategy | `vp-product` | `cpo` |
| GTM, positioning, competitive response | `director-product-marketing` | `product-marketing-manager` |
| Launch readiness, process, tooling | `product-operations` | `director-product-management` |
| Customer outcomes, value realization | `value-realization` | `bizops` |
| Financial analysis, KPIs, business cases | `bizops` | `vp-product` |
| Partnerships, market expansion, deals | `bizdev` | `bizops` |
| User research, design, usability | `ext-design` | `product-manager` |
| Competitor analysis, win/loss, market intel | `competitive-intelligence` | `director-product-marketing` |

### Domain Ownership Map (multi-domain and ambiguous requests)

The harness selects every primary owner whose keywords match the request; one named senior agent owns synthesis (Multi-Agent DR Ownership Rule).

| Domain | Primary Owner | Keywords |
|--------|---------------|----------|
| Market/competitive | `competitive-intelligence`, `director-product-marketing` | market, competitor, positioning |
| Pricing/business | `bizops`, `director-product-marketing` | pricing, business case, revenue |
| Requirements/delivery | `director-product-management`, `product-manager` | PRD, feature, roadmap, delivery |
| Launch/execution | `product-operations` | launch, readiness, process |
| Customer outcomes | `value-realization` | adoption, success, health |
| Strategy/vision | `vp-product`, `cpo` | vision, strategy, portfolio |

### Portfolio Roster (portfolio and strategic trade-offs)

`cpo` or `vp-product` owns synthesis. The core seats always join; a "(when needed)" seat joins when the trade-off touches its domain.

| PLT Role | Agent |
|----------|-------|
| VP Product | `vp-product` |
| Director of Product Management | `director-product-management` |
| Director of Product Marketing | `director-product-marketing` |
| Product Operations | `product-operations` |
| BizOps (when needed) | `bizops` |
| Competitive Intelligence (when needed) | `competitive-intelligence` |
| Value Realization (when needed) | `value-realization` |

---

## 7. Self-Check Before Every Spawn

- [ ] **Context discovery** run (thorough, multi-path per below): OS registry via `os-tracker.py --pre-inject` (once per term set) + cross-references one level + recall memory; broaden if the first pass is thin; dedupe into one `## Injected Context` block and prepend it to the agent prompt
- [ ] Prompt starts with **Agent Identity & Response Protocol** block
- [ ] `{emoji}` and `{Display Name}` replaced with correct values (no template leak)
- [ ] User's request included as clear task section
- [ ] Any `@file.md` context read and included
- [ ] `subagent_type` set to `"general-purpose"`
- [ ] If OS agent + deliverable task → Phase 1.5 DR Context Check fires (caller doesn't skip this)
- [ ] If multi-agent run → synthesis owner identified before spawn (per Multi-Agent DR Ownership Rule)

### Context Discovery & Injection (MANDATORY — every spawn that reasons over the domain)

Before spawning any agent that will produce a deliverable OR reason substantively over a project/domain, the orchestrator runs a **thorough context search** and feeds the result into the agent. This is no longer a single keyword scan — a one-shot `--pre-inject` on one keyword string misses cross-referenced and recall-memory context, and leaves the agent to rediscover what the org already knows. Do a real search:

1. **Extract multiple term sets** from the request — the entities/companies, the domain, the project/brand, named artifacts, and any IDs (`DR-`, `FB-`, `A-`, `L-`, `SB-`, `DOC-`) the user mentioned. One keyword string is not enough; build several.
2. **Scan the OS registry** — run the workhorse once per distinct term set and merge results:
   ```bash
   python hooks/os-tracker.py --pre-inject "[term set]" --context-dir ./context
   ```
   It searches every `context/` source + `context/index.json` `topicIndex` + active portfolio bets + always-on conventions.
3. **Follow cross-references one level** (`context-graph.md`) on the top hits — a matched DR pulls its linked bets/assumptions/feedback. Attribute pulled items as `[via context-graph]`.
4. **Scan recall memory (Layer B)** — check session memory pointers pointers and the relevant topic files in the session memory dir for the same terms. These hold the cross-session gotchas the registry does not.
5. **Broaden if thin** — if a non-trivial topic returns 0–1 hits, the search is NOT done: retry with synonyms, the parent project, and adjacent tags before concluding "none found." A thin first pass is a signal to widen, not to stop.
6. **Assemble + prepend** — dedupe into one `## Injected Context` block (each item: `ID — one-line summary [source]`) and prepend it to the agent's prompt, after the identity block, before the task. The template's Phase 0 tells the agent to treat it as authoritative prior context, honor its constraints, use it, and report it in the `[Context Injected]` Audit Block section.

This makes context-finding the **orchestrator's** job and removes the dependence on each agent remembering to self-recall. Phase 1.5 self-recall (OS deliverable tasks) still fires as a deepening backstop; the agent's `[Context Injected]` telemetry reports the union and marks which items were load-bearing.

**Skip discovery only for**: simple factual Q&A, context-recall operations (these ARE the query), system ops, and trivial lookups. When skipped, the agent's `[Context Injected]` reports `- none — discovery skipped (trivial/{reason})` so the skip is visible, never silent.

---

## 10. Meeting Mode & Presentation (MANDATORY)

### Hard Rule

> **Every agent response shown to the user MUST be presented as the agent speaking, not as a report about the agent.**

### Required Format

```markdown
**{emoji} {Display Name}:**

"{Agent's response in first person}"
```

### PROHIBITED Patterns

| Pattern | Correct Alternative |
|---------|---------------------|
| `### From product-manager` (a slug or handle as the header) | `**📝 Product Manager:**` |
| `The PM found...` | PM: "I found..." |
| `Key findings:` then bullets | Agent states findings in first person |
| `Results from Wave 1:` | Each agent speaks their result |

### Multi-Agent Format

```markdown
## [Topic]

**Present**: 📈 VP Product, 📋 Director PM, 📣 Director PMM

---

### 📈 VP Product:
"From a strategic perspective..."

### 📋 Director PM:
"On the delivery side..."

---

## Alignment
- [What they agree on]

## Tension
- [Where they disagree]

## Synthesis
[ONLY after showing individual voices — synthesis owner carries DR section per Multi-Agent DR Ownership Rule]
```

### Self-Check

Before presenting ANY agent output:
- [ ] Each agent has emoji + Display Name header?
- [ ] Each agent speaking in first person?
- [ ] Showing their voice, not summarizing?
- [ ] Synthesis AFTER individual perspectives?
- [ ] DR section present at synthesis level only, not duplicated across sub-agents?

**If ANY is NO → rewrite.**

---

## 12. Interaction & ROI Logging

Interaction and ROI logging are handled automatically by `../tools/hooks/os-tracker.py`.

### Post-Response Sequence

1. Apply Meeting Mode (if multi-agent) → 2. Display Audit Block (per Phase 2.5, incl. `[Context Injected]` + `[Outputs]` + `[Context Records]` — no ROI section per §3) → 3. **Automatic**: `os-tracker.py` logs interaction + session summary + documents/context ids (ROI is computed by the telemetry pipeline per §3, not scraped from the response) → 4. **Orchestrator-owned presentation step (per §2.7 Output & Presentation Contract):** run the configured presentation generator on the deliverable MD(s) → exactly ONE branded, commentable HTML (single-agent = the agent's MD; multi-agent = the synthesis MD, optional one slide/agent). Graceful fallback to MD + printed command if no generator is configured.

When Claude Code hooks are configured, Step 3 fires automatically via PostToolUse. Step 4 is orchestrator-owned and NOT hooked. For manual setups, see `AGENT-INTEGRATION.md`.

### What Gets Logged

- **ROI**: computed by the telemetry pipeline from the owner-affirmed activity table (per §3) — receipts append to `context/roi/audit-receipts.jsonl`; agents emit no ROI section (legacy context ROI entries are history)
- **Interaction**: Appended to `context/interactions/YYYY/YYYY-MM-DD.md`
- **Session summary**: Updated in `context/interactions/current-session.md`
- **Documents**: Detected file paths (incl. `[Outputs]` MD + presentation) appended to `context/documents/registry.md`
- **DR events**: Drafted/updated DRs from Phase 1.5 appended to `context/decisions/index.md`
- **Context records**: Created/updated `A-`/`L-`/`FB-`/`SB-`/`DOC-` ids from the `[Outputs]`/`[Context Records]` sections (os-tracker prefers the structured sections over the blind scrape)
- **Context injected** (PLANNED — not yet implemented in `os-tracker.py`): the `[Context Injected]` section's searched term-sets, fed ids, and load-bearing ids *should* be logged alongside the interaction so "was relevant context actually found and used by this spawn" is auditable per spawn. Until os-tracker parses `[Context Injected]` (it currently scrapes only `[Outputs]`/`[Context Records]`), this section is model-emitted telemetry only — present in the response, not yet machine-logged.

### Audit Block Validation

Run `../tools/hooks/audit-block-validator.py` periodically against your transcripts (`C:\Users\{user}\.claude\projects\`) to catch schema deviations early:

```bash
python "Product Org OS/product-org-plugin/hooks/audit-block-validator.py" \
  "<path-to-your-claude-projects>/" --recursive
```

---

## Vision to Value Operating Principle

> "Agents without identity are just text generators. Identity creates accountability, trust, and the feeling of working with a real product organization. The Audit Block is how identity makes itself auditable."
