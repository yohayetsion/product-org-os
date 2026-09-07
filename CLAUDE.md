# Operating Product Org OS

This repository is Product Org OS 6.2.0: a public product organization for coding agents. It includes 11 product roles, their methods and controls, the knowledge packs they load, operating rules, and four governed workflows; the measured contents are in `COMPONENT-MANIFEST.md`.

Product Org OS is the open-source edition of the licensed ProductBeacon AI Agentic Workforce. It includes the PBAW harness and product team. Here, PBAW means the process for selecting a Product Org OS role, loading its instructions, knowledge, and relevant context, running the task, and reporting the evidence. Explain the method in ordinary language before using the acronym with a first-time user.

## First run

1. Follow `INSTALL-AND-ONBOARD.md`; preview before writing.
2. Read `agent-guide.md` completely.
3. Detect whether this session is running in Claude Code, Codex, or another compatible tool.
4. Verify the actual install paths and counts.
5. Read `.claude/rules/agent-spawn-protocol.md` before the first product-role run.
6. Keep decisions with the named human owner. Roles may draft decisions; they do not affirm them.
7. Do not invent numbers. Use sourced data or `[TBD]`.

The installer writes into the project you name: every role, skill, knowledge pack, rule, and tool into the project's `.pbaw/` tree with its runtime manifest; exactly `pbaw`, `plan`, `audit`, and `context-harvest` onto `.claude/skills/` and `.agents/skills/`; the rules onto `.claude/rules/`; and an empty local `context/` scaffold.

## Environment contract

Claude Code and Codex do not expose the inventory in the same way.

- **Claude Code:** use the four installed operating workflows and the rules directly. Load product roles, their methods, declared knowledge, and relevant context through `/pbaw` from the project's `.pbaw/` tree. Verify the actual directories before claiming they are active.
- **Codex:** use the four installed operating workflows directly. Load product roles, their methods, declared knowledge, and relevant context through `/pbaw` from the project's `.pbaw/` tree.
- **Another file-driven agent:** read the selected role and skill files directly, follow the spawn protocol manually, and disclose that the host does not provide the native command surface.

Keep the repository copy available for upgrades. During specialist work, roles, knowledge packs, and governing files are resolved from the project's `.pbaw/` tree through `.pbaw/runtime-manifest.json`.

## Show the inventory on onboarding

For a first-time user, verify and explain:

| Capability | Verified public release |
|---|---|
| Product judgment | 11 primary roles; specialist selection happens inside `/pbaw` |
| Repeatable methods | The skills under `.pbaw/skills/`, listed in `COMPONENT-MANIFEST.md` |
| Professional reference | The knowledge packs under `.pbaw/knowledge/`; every declared public-role dependency is included |
| Governed operation | `plan`, `pbaw`, `audit`, and `context-harvest` |
| Local memory | Empty user-owned context scaffold until the user creates or accepts records |

Describe capabilities before internal names. State that direct visibility varies by host. Do not present repository counts as a claim that every directory becomes a direct slash command.

## Operating workflows

- `/plan`: plan multi-step work and surface material decisions.
- `/pbaw`: select and run Product Org OS specialists under the governed protocol.
- `/audit`: verify a plan or completed result.
- `/context-harvest`: record durable decisions, assumptions, learnings and feedback after completed work.

Translate a user's outcome into these workflows; do not require them to memorize the names. Routing lives in `.claude/rules/delegate-first.md`. The binding spawn contract lives in `.claude/rules/agent-spawn-protocol.md`.

## Product-role operation

For every governed specialist run:

1. Resolve the canonical role from the requested outcome.
2. Read the role's `SKILL.md` completely.
3. Load every always-read knowledge pack declared by the role.
4. Load conditional knowledge and task skills only when relevant.
5. Recall related local decisions, assumptions, bets, feedback, and learnings.
6. State what was loaded before presenting the work.
7. Preserve disagreements and missing evidence.
8. Leave material decisions with a named human owner.
9. Verify the result before claiming completion.

Use multiple roles only when independent perspectives are necessary. Keep one owner for the synthesis. Do not create ceremonial multi-role work for a routine request.

## First task

Recommend one small, reversible task with source material the user can verify. A suitable prompt is:

```text
Review this product artifact without editing it. Choose the most relevant Product Org OS
role, show what instructions and knowledge you loaded, separate evidence from assumptions,
and identify the decisions that remain mine.
```

After the user accepts the task, follow the proportional workflow. Harvest context only when the finished result creates a durable record worth preserving.

## Required completion report

Before handing work back, include:

- the outcome achieved;
- the role, skills, knowledge, and context used;
- the files created or changed;
- the verification performed and observed result;
- unresolved assumptions, risks, or owner decisions;
- direct paths or links the user should review.

## Boundaries

- This public package contains Product Org OS. It does not contain ProductBeacon's private specialist teams or customer material.
- Treat legal, security, privacy, employment, finance, and other regulated subjects as drafting or triage when qualified review is required.
- Search local context before consequential work, but treat records as evidence that may need reconciliation with newer sources.
- Before completion, run the relevant verification and report observed evidence, changed files, and unresolved owner decisions.
