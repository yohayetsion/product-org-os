# Product Org OS Agent Guide

This guide tells a coding agent how to operate Product Org OS on behalf of a human user. Read it completely during setup and before the first product-role task.

The person using the system is the **operator**. The operator owns the goals, accepts trade-offs, and makes material product decisions. The coding agent may investigate, draft, structure, challenge, and verify. It must not silently turn a recommendation into an approved decision.

## What Product Org OS is

Product Org OS is an AI-enabled product organization stored as files:

- **Product roles** define the judgment, responsibilities, and boundaries of a Chief Product Officer, Product Manager, Product Marketing Manager, Product Operations leader, and other specialists.
- **Skills** define repeatable ways to create or review product work such as a product requirements document, roadmap, pricing analysis, launch plan, or decision record.
- **Knowledge packs** give roles task-specific professional reference material.
- **Rules** govern delegation, evidence, sensitive work, context, and decision authority.
- **Local memory** preserves the user's own decisions, assumptions, feedback, learnings, and document references between sessions.

Product Org OS is the open-source edition of the licensed ProductBeacon AI Agentic Workforce. It includes the PBAW harness and product team. In this repository, PBAW is not a separate product the user must learn. It is the governed process that tells the coding agent how to choose a product role, load the right instructions and knowledge, perform the work, and report what happened.

## How the system fits together

```text
Human outcome
    |
    v
Plan the work when it is non-trivial
    |
    v
Select a Product Org OS role and load its instructions
    |
    v
Use the role's skills, knowledge, and relevant local context
    |
    v
Produce or review the deliverable
    |
    v
Audit the result before sign-off
    |
    v
Preserve durable context after the result is accepted
```

The human can start with ordinary language. Do not require the user to know agent names or slash commands. Translate the requested outcome into the right role and workflow, explain the route briefly, and proceed only within the user's authority.

## Detect the coding-agent environment

Before claiming the system is ready, identify the environment and verify the actual installation paths.

| Environment | How to operate |
|---|---|
| Claude Code | Use the four operating workflows under the project's `.claude/skills/`. Product roles are selected and loaded through `/pbaw` from the project's `.pbaw/` tree; `.claude/rules/` supplies the governing instructions. |
| Codex | Use the four operating workflows under the project's `.agents/skills/`. Product roles are selected and loaded through `/pbaw`; they are not separate direct Codex skills. |
| Another tool that reads `SKILL.md` | Read the relevant files directly, adopt the role instructions explicitly, and follow the spawn protocol manually. Do not pretend unsupported slash commands or automatic rules are active. |

Verify the installation against `INSTALL-AND-ONBOARD.md`. Do not infer success from a command's exit code alone.

## First-session checklist

1. Read `CLAUDE.md` for the repository-level contract.
2. Read this guide completely.
3. Confirm the environment and installed paths.
4. Locate `.claude/rules/agent-spawn-protocol.md`.
5. Locate the product roles under the project's `.pbaw/agents/`.
6. Confirm `.pbaw/knowledge/` exists and that `.pbaw/runtime-manifest.json` lists the shipped knowledge packs.
7. Inspect the local `context/` directory. An empty directory is normal on a new installation.
8. Explain the system in plain language before using internal names.
9. Recommend one small, reversible first task.

## The four operating workflows

The installer exposes four workflows. Describe the purpose first; mention the command second.

### 1. Plan non-trivial work with `/plan`

Use planning when the request has several dependent steps, changes important files, involves more than one role, or contains a material decision. A useful plan states:

- the outcome and boundaries;
- the source material to inspect;
- the roles or skills that own each part;
- the sequence of work;
- the verification required before completion;
- the decisions only the human can make.

Do not plan simple lookups or tiny edits. Do not use a plan to hide uncertainty; state the uncertainty and ask only if two plausible readings would produce materially different work.

### 2. Run a product specialist with `/pbaw`

Use the PBAW workflow when a named product role should own the analysis or deliverable. It applies the governed spawn protocol. The coding agent must:

1. Resolve the requested role or route the outcome to the right role.
2. Read the role's `SKILL.md` completely.
3. Load every declared always-read knowledge pack.
4. Load conditional knowledge and task skills that match the request.
5. Search the local context for relevant prior decisions and evidence.
6. Preserve the role's findings without inventing agreement.
7. Report what was loaded, what was produced, and what remains for the human.

Example user request:

```text
Use the Product Manager role to review this requirements document. Do not edit it. Separate missing evidence, unclear decisions, and acceptance-criteria gaps.
```

The coding agent runs that through `/pbaw`. Specialist selection happens inside `/pbaw`. The user does not need to supply any syntax.

### 3. Check a plan or result with `/audit`

Audit has two modes:

- **Plan audit** checks whether proposed work is complete, safe, sequenced correctly, and verifiable before execution.
- **Result audit** checks whether completed work ran correctly, produced the intended outcome, and has enough evidence for sign-off.

An audit is not an automatic approval. Report blockers, important gaps, and optional improvements separately. A green result requires observed evidence, not confidence in the author.

### 4. Preserve useful context with `/context-harvest`

Use context harvest after a completed result creates knowledge worth carrying forward. It records durable items such as:

- a decision and its named owner;
- an assumption and the event that should cause it to be revisited;
- a learning supported by an observed result;
- feedback and where it came from;
- a strategic bet;
- a document reference that later work should be able to find.

Do not harvest drafts as settled facts. Do not mark a decision accepted unless the named human explicitly accepted it.

## Product roles

The public product organization contains eleven primary roles. Route by outcome, not by title familiarity.

| Role | Use it for |
|---|---|
| Chief Product Officer | Product vision, portfolio choices, operating-model decisions, and executive trade-offs |
| Vice President of Product | Product strategy, outcome management, prioritization, and cross-product execution |
| Director of Product Management | Roadmap governance, product-management quality, team structure, and planning discipline |
| Director of Product Marketing | Positioning, market strategy, launches, pricing communication, and go-to-market alignment |
| Product Manager | Discovery, requirements, user stories, acceptance criteria, and delivery decisions |
| Product Marketing Manager | Messaging, campaigns, enablement, adoption, and competitive communication |
| Business Operations | Business cases, operating metrics, pricing economics, and organizational coordination |
| Business Development | Partnerships, commercial opportunities, and early deal structure |
| Competitive Intelligence | Competitor analysis, market evidence, and strategic implications |
| Product Operations | Product process, launch readiness, tooling, ceremonies, and cross-team coordination |
| Value Realization | Adoption, customer outcomes, value measurement, and outcome reporting |

When the right role is not obvious, `/pbaw` selects it: one owner for a product request, or several leadership perspectives for a consequential decision.

## Skills

A role is responsible for judgment. A skill is a reusable method for doing a particular job. A role may invoke several skills during one task.

Examples include:

| Outcome | Likely skill |
|---|---|
| Define a feature clearly | Product requirements document or user-story workflow |
| Compare priorities | Prioritization, outcome, or roadmap workflow |
| Record a consequential choice | Decision-record workflow |
| Prepare a market launch | Go-to-market or launch-plan workflow |
| Review pricing | Pricing-strategy workflow with financial and market knowledge |
| Assess a completed initiative | Outcome-review or value-realization workflow |

Read the selected skill's `SKILL.md` completely before following it. If the environment does not support direct skill invocation, use the file as the procedure and say that you are doing so.

## Knowledge packs

Version 6.2.0 ships the Product Org OS knowledge packs listed in `COMPONENT-MANIFEST.md`. They cover the core methodology and the specialist subjects named by public product roles, including:

- prioritization, discovery, metrics, pricing, and stakeholder management;
- user and market research;
- product marketing, growth, public relations, and partnerships;
- financial modeling, software-as-a-service metrics, and value-score design;
- product operations, change management, and incident response;
- design systems, generative interfaces, agent supervision, and agent security;
- compliance and human-resources governance where product decisions touch those subjects.

Knowledge is loaded in tiers:

- **Always-read packs** are declared by the role and loaded for every invocation.
- **Conditional packs** are loaded only when task keywords or subject matter match.
- **On-demand references** are used when a skill or investigation needs them.

If a role names a knowledge pack, resolve the declared component through the installed runtime manifest and read its canonical `knowledge/shared/` file. No authoring-workspace fallback or broad file search is permitted.

Report a missing required pack. Do not substitute general model knowledge and claim that the declared pack was loaded.

## Context and memory

The local `context/` directory belongs to the user. It is created empty and is never populated from the release package.

Before product work, search for relevant:

- decisions;
- assumptions;
- strategic bets;
- feedback;
- learnings;
- documents;
- portfolio records;
- prior handoffs.

Use context to avoid reopening settled questions or contradicting known constraints. Treat context as evidence with provenance, not as an unquestionable truth. If an old record conflicts with newer source material, surface the conflict.

## Decision authority

Product Org OS is designed around a simple boundary:

- The coding agent may draft, analyze, compare, recommend, and record.
- A named human owns and accepts material decisions.

When the work creates a decision:

1. State the decision in plain language.
2. Show the evidence and alternatives considered.
3. State the recommendation and why.
4. Name the human owner.
5. Leave the record in draft until the owner explicitly accepts it.

Never fabricate approval, a signature, a seal, or an acceptance timestamp.

## The spawn report

A governed specialist run should open with a short audit block or equivalent report that states:

- the canonical role used;
- the role instructions read;
- the knowledge packs loaded;
- the context injected;
- the task-specific skills used;
- any fallback or missing file;
- the output files produced.

This is evidence that the specialist was actually grounded. It is not a place for the agent to praise its own value.

## Run the first task

Choose a bounded task with source material the user can recognize. A read-only review is ideal.

### Example: review a product requirements document

User prompt:

```text
Review this product requirements document as a Product Manager. Do not edit it. Identify missing user evidence, unresolved decisions, unclear scope, and weak acceptance criteria. Explain what you loaded before the findings.
```

Expected route:

1. Plan only if the document or review scope is substantial.
2. Use `/pbaw` with the Product Manager role.
3. Load the role's always-read packs and relevant conditional packs.
4. Search context for related decisions and feedback.
5. Produce a review with evidence tied to document sections.
6. Audit the result if it will be used for approval.
7. Harvest only accepted decisions or durable learnings.

### Example: prepare a pricing decision

User prompt:

```text
Help me decide whether to change our packaging. Use the relevant product leadership and business-operations roles. Use only the data in the attached files. Show unresolved inputs as TBD and recommend the next decision.
```

Do not invent willingness-to-pay data, conversion rates, revenue, effort, or timing. If critical evidence is absent, say what is missing and structure the decision around verified facts.

### Example: audit a launch plan

User prompt:

```text
Audit this launch plan before I approve it. Separate blockers, important gaps, and optional improvements. Do not rewrite the plan.
```

Use result-audit mode if the launch work has already been completed; use plan-audit mode if this is still a proposal.

## Multi-role work

Use more than one role only when their perspectives are independently necessary. Keep one named owner for the final synthesis.

For a multi-role engagement:

1. State why each role is needed.
2. Give every role the same relevant source context.
3. Preserve disagreements instead of averaging them away.
4. Synthesize the result around the user's decision or outcome.
5. Produce one coherent handoff, not a pile of disconnected role outputs.

Do not invoke several roles to make routine work look more rigorous.

## Boundaries and sensitive work

The public package contains product roles, not private specialist teams. A product role may identify when qualified legal, security, privacy, finance, employment, or clinical review is needed. It must not pretend that product guidance is professional approval in those domains.

For sensitive work:

- describe the output as drafting or triage;
- identify the qualified reviewer required;
- avoid irreversible actions;
- protect secrets and personal data;
- cite sources for material claims;
- keep customer material in the user's local environment.

## Compatibility and post-install operating contract

Installation makes files available. It does not prove that the active coding-agent session has discovered, read, or adopted them. Complete these checks after every installation, upgrade, or destination change.

| Check | Claude Code | Codex | File-driven agent |
|---|---|---|---|
| Repository front door | Read the project's `CLAUDE.md` | Read the project's `AGENTS.md` when present | Read the project instruction file supported by the host |
| Core workflows | Directly discoverable under the project's `.claude/skills/` | Directly discoverable under the project's `.agents/skills/` | Read the four workflow `SKILL.md` files directly |
| Product roles | Loaded through the governed `/pbaw` workflow from `.pbaw/agents/` | Loaded through the governed `/pbaw` workflow from `.pbaw/agents/` | Read the selected role and apply its instructions explicitly |
| Governing rules | Loaded from `.claude/rules/` when supported | Read by `/pbaw` from `.pbaw/rules/` | Read the relevant rule files manually |
| Knowledge packs | Resolved from `.pbaw/knowledge/` through the runtime manifest | Resolved from `.pbaw/knowledge/` through the runtime manifest | Resolve the path named by the role |
| Local memory | Use the configured `context/` destination | Use the configured `context/` destination | Use it only if the host can read the directory |

Post-install, do not say “Product Org OS is ready” until all of the following are observed:

1. The four operating workflow files exist at the chosen destination.
2. The project's `.pbaw/` tree matches `.pbaw/install-manifest.json`: all 11 role definitions and every declared knowledge pack are present.
3. The project front door points the agent to this guide and the local installation.
4. A fresh session can explain the system without assuming the user knows its internal names.
5. One read-only product-role task produces a grounded spawn report and a useful result.

If the host cannot expose a capability automatically, downgrade the claim. “I can follow this file manually” is accurate. “The integration is installed and active” is not.

## Skills by Vision to Value phase

The skill inventory is broader than the examples in the quick-start sections. Route skills through the six-phase Vision to Value lifecycle, while recognizing that some methods support more than one phase.

### Phase 1: Vision and strategy

Use these methods to frame the ambition, understand the market, compare strategic options, and define the intended value:

- `vision-statement`, `strategic-intent`, `market-analysis`, `market-segment`, `competitive-landscape`, `competitive-analysis`;
- `pestle-analysis`, `porter-five-forces`, `seven-powers`, `wardley-map`, `blue-ocean`;
- `ansoff-matrix`, `bcg-matrix`, `business-model-canvas`, `lean-canvas`, `business-plan`, `business-case`;
- `strategic-bet`, `portfolio-tradeoff`, `partnership-architecture`, `growth-model`, `north-star-metric`, `okr-writer`.

### Phase 2: Discover and validate

Use these methods to inspect customer problems, assumptions, desirability, viability, feasibility, and evidence quality:

- `brainstorming`, `assumption-map`, `bet-invalidation-checkpoint`, `pre-mortem`, `bias-check`;
- `interview-synthesis`, `customer-journey-map`, `opportunity-tree`, `design-sprint`, `pretotype`;
- `experiment-design`, `four-risks-check`, `kano-analysis`, `product-teardown`, `customer-health-scorecard`;
- `feedback-recall`, `feedback-capture`, `relevant-learnings`, `win-loss-decision-signal`.

### Phase 3: Plan and commit

Use these methods to convert evidence into accountable choices, specifications, priorities, and outcome plans:

- `prd`, `prd-outline`, `feature-spec`, `user-story`, `product-roadmap`, `roadmap-theme`, `roadmap-item`;
- `prioritize-features`, `shape-up`, `daci`, `decision-charter`, `decision-record`, `decision-quality-audit`;
- `ownership-map`, `stakeholder-map`, `stakeholder-brief`, `strategy-communication`, `commitment-check`;
- `plan`, `writing-plans`, `phase-check`, `maturity-check`, `scale-check`, `continuation-threshold`.

### Phase 4: Build and release

Use these methods to keep customer intent, release readiness, launch dependencies, and handoffs visible:

- `collaboration-check`, `handoff`, `launch-readiness`, `launch-plan`, `launch-narrative-brief`;
- `gtm-brief`, `campaign-brief`, `press-release-faq`, `sales-enablement`, `subject-line`;
- `verification-before-completion`, `audit`, `dispatching-parallel-agents` where the work is genuinely independent.

### Phase 5: Operate and grow

Use these methods to run the portfolio, improve adoption, coordinate the organization, and respond to changing evidence:

- `operating-calendar`, `portfolio-status`, `qbr-deck`, `retrospective`, `outcome-review`;
- `saas-health-check`, `pirate-metrics`, `heart-metrics`, `analytics-tracking`, `onboarding-playbook`;
- `gtm-strategy`, `launch-strategy`, `pricing-strategy`, `pricing-model`, `marketing-psychology`, `llm-seo`;
- `escalation-rule`, `ooda-loop`, `theory-of-constraints`, `collaboration-check`.

### Phase 6: Realize value

Use these methods to connect product work to observed customer and business outcomes:

- `customer-value-trace`, `value-realization-report`, `roi-report`, `outcome-review`;
- `value-realization`, `saas-health-check`, `customer-health-scorecard`, `win-loss-decision-signal`;
- `context-harvest`, `context-save`, `feedback-capture`, `relevant-learnings`, `retrospective`.

Do not force every task through all six phases. Use the lifecycle to identify upstream evidence and downstream consequences, then select only the methods the present outcome requires.

## Strategy frameworks

The public inventory retains the earlier guide's broad framework coverage. A framework is a lens, not an answer. Choose one because it changes the decision, not because its name is familiar.

| Decision need | Useful lenses | Required caution |
|---|---|---|
| External market pressure | PESTLE, Porter Five Forces, market analysis | Time-sensitive claims require current evidence |
| Durable advantage | Seven Powers, Wardley mapping, competitive landscape | Separate observed advantage from aspiration |
| Portfolio allocation | BCG matrix, Ansoff matrix, portfolio trade-off | Do not invent market share or growth figures |
| Category and value design | Blue Ocean, value-score design, positioning | Validate that customers recognize the proposed value |
| Business model | Business Model Canvas, Lean Canvas, pricing model | Label unverified economics and willingness to pay |
| Goals and measurement | North Star Metric, OKRs, HEART, pirate metrics | Choose measures tied to the intended outcome |
| Flow and constraints | Theory of Constraints, OODA loop, operating calendar | Use operational evidence, not generic process advice |

Framework outputs should state the source facts, analytical interpretation, assumption set, implication, and decision that the analysis informs. Do not present a filled canvas as proof that the underlying claim is true.

## Document intelligence

Many product assignments begin with an existing document. Treat the document as evidence and an artifact with a purpose, not as text to summarize mechanically.

When reviewing a product document:

1. Identify its stated audience, decision, and intended next action.
2. Map claims to evidence in the document or linked sources.
3. Separate missing information from genuine contradictions.
4. Locate open decisions, implied commitments, dates, owners, and dependencies.
5. Check whether the artifact fits its Vision to Value phase.
6. Recommend the smallest change that improves the intended outcome.
7. Preserve exact section references so the user can verify each finding.

Common artifact routes include:

| Artifact | Lead role | Useful checks |
|---|---|---|
| Strategy or vision | Chief Product Officer or VP Product | Strategic choices, evidence, coherence, outcome measures |
| Product requirements document | Product Manager | Problem evidence, scope, risks, decisions, acceptance criteria |
| Roadmap | Director of Product Management | Outcomes, evidence, sequencing, dependencies, trade-offs |
| Positioning or messaging | Product Marketing Manager | Audience, category, differentiation, proof, consistency |
| Pricing proposal | Business Operations plus product leadership | Value metric, evidence, economics, unresolved inputs |
| Launch plan | Product Marketing and Product Operations | Readiness, owners, dependencies, risk, feedback loop |
| QBR or outcome review | Value Realization or Product Operations | Baseline, observed outcome, attribution limits, next decision |

For PDFs, spreadsheets, or presentations, use the host's supported reader and visual checks. If only extracted text was inspected, say so. Do not imply that layout, formulas, charts, or speaker notes were reviewed when they were not.

## Vision to Value and operating principles

Vision to Value is the lifecycle that connects intent to realized evidence:

```text
Vision and strategy
        ↓
Discover and validate
        ↓
Plan and commit
        ↓
Build and release
        ↓
Operate and grow
        ↓
Realize value
        ↺ learning informs the next strategic choice
```

Apply these operating principles across every phase:

- **Outcomes over output.** Clarify the change the user wants before choosing the artifact.
- **Evidence over fluency.** A confident narrative does not convert an assumption into a fact.
- **Human-held decisions.** Agents can recommend, but a named human accepts material choices.
- **Proportional ceremony.** Match planning, delegation, and audit depth to risk and reversibility.
- **Selective context.** Load what the task needs and report it; do not flood the run with unrelated history.
- **Visible assumptions.** Record unknowns and the evidence or event that should revisit them.
- **Verification before completion.** Observe the result and report the evidence before claiming success.
- **Closed learning loop.** Preserve accepted outcomes so future work starts from what the organization learned.

## Context structure and multi-product use

The local context registry has six primary memory types. Keep their semantics distinct.

| Context type | What belongs there | What does not |
|---|---|---|
| Documents | A durable reference to an artifact and why it matters | A duplicate of every draft produced |
| Decisions | A choice accepted by a named human owner | An agent recommendation awaiting acceptance |
| Strategic bets | A material commitment with intended outcome and invalidation conditions | A generic aspiration |
| Assumptions | An unverified belief that affects action | A fact already supported by evidence |
| Learnings | A conclusion supported by an observed result | A prediction or preference |
| Feedback | Attributed input from a person or evidence source | An unattributed paraphrase presented as consensus |

A useful context record includes a stable identifier, date, status, source, owner where applicable, scope, cross-references, and the content itself. Follow the allocator and templates in the installed context system. Do not create competing identifier formats.

For multi-product work:

- keep product-specific records in their product scope;
- store portfolio decisions at the portfolio level and link to affected products;
- use cross-references instead of copying one decision into several folders;
- surface conflicts between product and portfolio context;
- never assume a decision for one product automatically applies to another.

Context recall is selective. Search identifiers, titles, product scope, and relevant terms before a task. Context harvest happens only after the user accepts the result or explicitly asks to preserve a still-open item as an assumption or draft.

## Collaboration patterns

Use the smallest collaboration pattern that preserves the required judgment.

### One role, one owner

Default to one role for a bounded product task. The role may use several skills, but it remains accountable for one coherent result.

### Selection inside `/pbaw`

When the user describes an outcome and the right product discipline is unclear, `/pbaw` selects the owner; it routes, it does not become a generic author that hides who did the work. When a consequential issue truly requires independent product-management, product-marketing, operations, or value perspectives, `/pbaw` brings them together: preserve disagreements and assign one synthesis owner.

### Parallel independent analysis

Parallel work is appropriate only when assignments do not mutate the same files or depend on each other's intermediate results. Give each role the same decision frame and source set. Reconcile findings before presenting them.

### Sequential handoff

Use a sequential pattern when downstream work depends on an accepted upstream result. For example: Product Manager evidence synthesis, human scope decision, Product Marketing positioning, Product Operations launch-readiness check.

Every handoff should state the outcome, source material, completed work, evidence, unresolved decisions, constraints, and next owner. Do not hand over a folder of files without a clear next action.

## Onboard the user

The coding agent owns the first explanation. The user should not need to know the acronym, directory structure, or command syntax before receiving value.

### Show the inventory

After installation, summarize in plain language:

- 11 product roles and the outcomes they own;
- four governed workflows for planning, specialist assignment, audit, and memory;
- the product methods, supporting controls, and professional knowledge packs listed in `COMPONENT-MANIFEST.md`;
- the empty local context structure that belongs to the user.

### Establish the project front door

Offer to add a short instruction block to the user's project-level `CLAUDE.md` or `AGENTS.md`. Do not overwrite existing instructions. A suitable block is:

```markdown
## Product Org OS

For product work, read `<repository-path>/agent-guide.md` and operate from the installed
Product Org OS inventory. Start with the user's outcome in plain language. Use the four
governed workflows proportionally, load product roles through the supported environment,
keep material decisions with a named human owner, and preserve durable context only after
acceptance. Verify results before claiming completion.
```

Replace `<repository-path>` with the actual path observed during installation. Keep the repository copy available for upgrades; knowledge packs and rules are resolved from the project's `.pbaw/` tree.

### First request

Invite the user to begin with an artifact or decision they already understand. A useful prompt is:

```text
Inspect the Product Org OS installation and explain the available product capabilities in
plain language. Then help me choose one small, reversible product outcome to complete first.
Use only the source material I give you and show what you load for the task.
```

The first result should make the system easier to trust: bounded scope, visible sources, a clear role, a useful artifact or review, explicit open questions, and no invented organizational knowledge.

## Complete skill inventory

The measured inventory of product roles, operating workflows, product methods, and supporting controls is `COMPONENT-MANIFEST.md`, generated from the runtime manifest at release time. Use it to verify the released file population; use the directory names under `.pbaw/agents/`, `.pbaw/harness/`, and `.pbaw/skills/` to find the canonical `SKILL.md`. Do not infer that every host exposes every directory as a direct command.

## File reference

| Path | Purpose |
|---|---|
| `README.md` | First-time-user overview and quick start |
| `INSTALL-AND-ONBOARD.md` | Installation, verification, upgrade, and coding-agent handoff |
| `CLAUDE.md` | Repository-level instructions for the operating assistant |
| `runtime-manifest.json` | Every shipped file, its hash, and what it requires; installed as `.pbaw/runtime-manifest.json` |
| `agents/`, `skills/` | Product roles and task skills; installed under `.pbaw/` |
| `knowledge/` | Core method knowledge; installed under `.pbaw/knowledge/` |
| `.claude/rules/agent-spawn-protocol.md` | Binding steps for a governed role invocation |
| `.claude/rules/delegate-first.md` | Current routing guidance |
| `harness/pbaw/spawn-template.md` | Prompt payload used for a governed specialist run |
| `context/` | User-owned local memory created at installation |
| `COMPONENT-MANIFEST.md` | Measured release contents |

## Troubleshooting

### A role is not visible

- Confirm the tool and installation mode.
- Verify the role directory exists under the project's `.pbaw/agents/`.
- On either host, use `/pbaw`; do not expect product roles to be projected as direct skills.

### A knowledge pack appears missing

- Read the role's exact declared filename.
- Check `.pbaw/knowledge/` in the project and the file's row in `.pbaw/runtime-manifest.json`.
- Re-run `install.py` from the repository copy if `.pbaw/` is incomplete.
- Report the missing file if neither path exists. Do not claim a fallback was loaded unless it was.

### Prior decisions are not being found

- Confirm the actual `context/` destination chosen during installation.
- Check that the working folder exposes that directory to the coding agent.
- Do not recreate lost context from memory. Restore a recoverable copy or ask the user.

### The workflow terminology confuses the user

Return to outcomes:

- plan the work;
- use the right product specialist;
- check the result;
- preserve what should be remembered.

The internal names are shortcuts, not prerequisites.

### The agent wants to mark a decision approved

Stop at a draft. Present the decision, recommendation, evidence, and named owner. Wait for explicit human acceptance.

## Completion standard

Before saying the work is complete:

- verify the requested outcome, not only the file edits;
- run the relevant checks and inspect their output;
- state which files changed;
- distinguish facts, inferences, recommendations, and unresolved decisions;
- give the user direct review links or paths;
- preserve durable context only after the result is accepted.

Product Org OS should make the coding agent easier to trust because its work is grounded, inspectable, and governed. The user should not have to learn the machinery before receiving that benefit.
