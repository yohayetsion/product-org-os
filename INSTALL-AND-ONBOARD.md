# Install and Onboard Product Org OS 6.2.0

## Who this guide is for

This guide is written for the **coding agent helping a person install Product Org OS**. The human remains the owner of the machine, the repository, and every material product decision. Explain each action in plain language, show the destination paths before writing, and stop if the requested location is ambiguous.

Product Org OS is the open-source edition of the licensed ProductBeacon AI Agentic Workforce. It includes the PBAW harness and product team. Product Org OS gives a coding agent product roles, repeatable workflows, and knowledge packs; PBAW is the method that selects a role, loads its instructions and knowledge, runs the task, and reports what happened. The user should not need to know this name in advance.

## What will be installed

The installer works on one **project**: the folder the user opens in Claude Code or Codex. It reads this repository copy as its source and writes into the project.

| Destination in the project | Contents |
|---|---|
| `.pbaw/` | Every shipped role, skill, knowledge pack, rule, and tool at the same relative paths as this repository (`agents/`, `skills/`, `knowledge/`, `rules/`, `tools/`, `harness/`), plus `runtime-manifest.json` (the graph the roles load through), `install-manifest.json` (the install ledger), and `sync-receipt.json` (the before-and-after receipt) |
| `.claude/skills/` | Exactly four operating workflows: `plan`, `pbaw`, `audit`, and `context-harvest`, each marked as managed by the installer |
| `.agents/skills/` | The same four workflows for Codex, marked the same way |
| `.claude/rules/` | The governing rules, marked as managed; `.claude/rules-reference/` receives their companion documents |
| `context/` | Empty folders for decisions, assumptions, feedback, learnings, documents, portfolio records, interactions, handoffs, and preferences, plus the context-id allocator. Created locally, never shipped, preserved byte for byte on every re-run |

Product roles, methods, and knowledge are loaded from `.pbaw/` during a governed run. They are deliberately not projected onto the host skill directories. Anything else in `.claude/skills/`, `.agents/skills/`, `.claude/rules/`, or `.claude/rules-reference/` is left untouched: the installer only ever replaces what it marked as its own.

The measured contents of the release are listed in `COMPONENT-MANIFEST.md`, which is generated from the runtime manifest.

## Before you begin

Confirm all of the following:

- Python 3.10 or newer is available as `python`.
- This repository copy is in a normal local folder where the user expects it to remain. It stays the source for upgrades.
- The user has named the project folder to install into.
- The user has chosen a coding-agent environment:
  - **Claude Code** discovers the four workflows under the project's `.claude/skills/` and the rules under `.claude/rules/`.
  - **Codex** discovers the four workflows under the project's `.agents/skills/`.
- Existing `.claude/`, `.agents/`, or `context/` folders in the project have been identified. Do not delete or replace those folders wholesale; the installer does not either.

If the repository is not on the machine yet:

```powershell
git clone https://github.com/yohayetsion/product-org-os.git
cd product-org-os
```

Run all remaining commands from the repository root, the directory containing `install.py`.

## What the installer changes

`install.py` is a thin wrapper over the shipped engine `tools/build/setup-skills.py`. One journalled transaction:

- verifies every shipped file against `runtime-manifest.json` before writing anything;
- copies the shipped files into the project's `.pbaw/` tree and writes the installed manifest, the ledger, and the receipt;
- projects the four workflows onto `.claude/skills/` and `.agents/skills/` with an ownership marker in each directory;
- projects the rules onto `.claude/rules/` and their companions onto `.claude/rules-reference/` with a marker file;
- creates the missing `context/` folders and places `context/allocate-id.py`;
- on an upgrade from Product Org OS 6.0.x, removes the previous release's managed skill directories from the hosts and nothing else.

If any step fails, the transaction rolls back and the project is left exactly as it was.

The installer does **not**:

- send files, telemetry, or memory to a remote service;
- change repository visibility or publish a website;
- install private ProductBeacon specialist teams;
- delete unrelated skills, rules, or context files;
- touch anything outside the project root. An older installation under the home directory (`~/.claude/skills`, `~/.claude/rules`) is outside its authority: move those Product Org OS directories and rule files to a dated backup folder yourself;
- affirm decisions on the user's behalf.

## Preview

Always inspect the plan before writing:

```powershell
python install.py --project-root "C:\path\to\project" --preview
```

Read the reported operations back to the user. The preview stages the whole transaction and rolls it back; it makes no change to the project. If the project is wrong, choose it explicitly before continuing.

The available switches are:

| Switch | Meaning |
|---|---|
| `--project-root PATH` | The project to install into (required) |
| `--preview` | Stage, print the operation list, write nothing |
| `--backup-to DIR` | Copy the host folders into an absent directory before the first live write; the copy is hash-verified |
| `--context-dir PATH` | Choose the local memory directory (default: `<project>/context`) |
| `--no-context` | Do not create the local memory scaffold |

Use `python install.py --help` to inspect the current command-line contract; the help names this release's version.

## Install

After the human confirms the preview:

```powershell
python install.py --project-root "C:\path\to\project" --backup-to "C:\path\to\backup-before-install"
```

Repeat the exact project path that passed the preview. Do not silently switch to another folder.

The command must exit successfully and print the copied, updated, and deleted counts with the receipt path. Treat the printed summary as evidence, then verify the resulting files directly.

## Verify the installation

### Verify the receipt

Read `.pbaw/sync-receipt.json` in the project. It records the before-and-after hash of every host folder, the installed `.pbaw/` map, and the `context/` hash. `unmanaged_and_context_preserved` must be `true`.

### Verify Claude Code

Confirm these directories exist under the project's `.claude/skills/`, each with a `SKILL.md` and a `.pbaw-managed.json` marker:

```text
plan/
pbaw/
audit/
context-harvest/
```

Confirm `.claude/rules/` contains `agent-spawn-protocol.md` and a `.pbaw-managed.json` marker, and that `.claude/rules-reference/` contains the companion documents.

### Verify Codex

Confirm the project's `.agents/skills/` contains exactly these four Product Org OS directories:

```text
.agents/skills/plan/
.agents/skills/pbaw/
.agents/skills/audit/
.agents/skills/context-harvest/
```

The product roles are deliberately not projected as direct skills on either host. A governed run reaches them through `/pbaw`, which reads the role from `.pbaw/agents/` and resolves its knowledge through `.pbaw/runtime-manifest.json`.

### Verify the runtime tree

Confirm `.pbaw/runtime-manifest.json` exists and that `.pbaw/agents/`, `.pbaw/skills/`, `.pbaw/knowledge/`, `.pbaw/rules/`, `.pbaw/tools/`, and `.pbaw/harness/` are present. Do not edit anything under `.pbaw/`; the next install replaces it from the manifest.

### Verify local memory

Confirm the context directory exists and contains folders for decisions, assumptions, feedback, learnings, documents, portfolio records, interactions, handoffs, and preferences, plus `allocate-id.py`. Existing user files must remain unchanged; the receipt's `context/` hash is the same before and after.

Finally run the preview again. It should report no remaining operations:

```powershell
python install.py --project-root "C:\path\to\project" --preview
```

## Onboard the coding agent

Open the clone as the working folder. Give the coding agent this copy-ready prompt:

> Read `CLAUDE.md` and `agent-guide.md` completely. Verify which Product Org OS files and workflows are available in this environment. Explain the system to me without assuming I know its internal names. Show the product roles in a short table, explain the four operating workflows, and recommend one small first task. Do not edit files or make a product decision until I approve the task.

The agent should then:

1. Identify whether it is running in Claude Code, Codex, or another compatible tool.
2. Confirm the installed paths instead of assuming the defaults were used.
3. Explain that the human owns decisions and the agent may only draft decision records.
4. Show the roles most relevant to the user's immediate work.
5. Recommend a first task using ordinary language before naming a workflow.
6. Read `.claude/rules/agent-spawn-protocol.md` before the first specialist run.

### Show the inventory

The first coding-agent response after installation should be an observed inventory tour, not a generic welcome message. Ask the agent to read the repository and report:

| Inventory | What the agent should verify | What it means to the user |
|---|---|---|
| 11 product roles | Role directories and their canonical definitions | Specialist product judgment across strategy, management, marketing, operations, intelligence, partnerships, and value; specialist selection happens inside `/pbaw` |
| Four governed workflows | `plan`, `pbaw`, `audit`, and `context-harvest` | Plan substantial work, assign a specialist, check the result, and preserve accepted learning |
| Skills and knowledge | `.pbaw/skills/` and `.pbaw/knowledge/`, listed in `COMPONENT-MANIFEST.md` | Product methods, supporting controls, and the professional knowledge roles load when the task requires it |
| Local context | The configured `context/` tree | User-owned memory for decisions, assumptions, bets, learnings, feedback, and document references |

Require the agent to distinguish the manifest's contents from direct command availability. Both hosts receive exactly four direct workflows; every product role is loaded through the governed specialist workflow from the project's `.pbaw/` tree.

### Establish the project front door

The install destination and the project where the user does product work may be different. Add a short pointer to the project's existing instruction file so a fresh coding-agent session knows where Product Org OS lives.

For Claude Code, offer to append this block to the project's `CLAUDE.md`:

```markdown
## Product Org OS

For product work, read `<absolute-repository-path>/agent-guide.md` and operate from the
installed Product Org OS inventory. Begin with the user's desired outcome in plain language.
Use planning, specialist assignment, audit, and context harvest proportionally. Keep material
decisions with a named human owner and verify results before claiming completion.
```

For Codex, offer to append the same operating contract to the project's `AGENTS.md`, adjusted only to say that product roles are loaded through `/pbaw` rather than projected as direct Codex skills.

Rules for the coding agent making this change:

1. Inspect the existing front-door file first.
2. Preserve all existing instructions.
3. Replace `<absolute-repository-path>` with the path actually verified during installation.
4. Do not create both `CLAUDE.md` and `AGENTS.md` unless the user uses both environments.
5. Show the proposed block before writing when the project has sensitive or highly customized instructions.
6. Verify that a fresh session can follow the pointer.

If the user does not want a project-level pointer, keep the clone open as the working directory for product tasks.

### First request

Use this prompt after the inventory and project front door are verified:

> Inspect the source material I give you and help me choose one small, reversible product outcome. Explain which Product Org OS role and methods fit, what evidence you need, and what decisions remain mine. Do not edit files until I approve the task.

A suitable first request has known source material, one recognizable result, low irreversible risk, and a clear review point. Strong examples are a read-only product requirements review, interview synthesis, roadmap evidence check, or launch-plan audit.

A poor first request is “run the whole product organization.” It has no bounded outcome, no acceptance standard, and no useful way to verify whether the installation improves the work.

## Run the first task

Use a real but bounded outcome. Examples:

```text
Help me turn these interview notes into a clear problem statement. Plan the work first and show me any decisions I need to make.
```

```text
Use the Product Manager role to review this product requirements document. Tell me what context and knowledge you loaded, then list gaps without editing the document.
```

```text
Audit this launch plan before I approve it. Separate factual gaps, unresolved decisions, and optional improvements.
```

The coding agent should translate these into the appropriate workflow. The user does not need to memorize slash commands.

## Upgrade from an earlier version

Do not start an upgrade until the current local memory location is known.

1. Record the project path and the existing `context/` path. If an earlier installation kept `context/` inside the repository copy rather than in the project, copy it into the project first; the installer preserves an existing `context/` byte for byte.
2. Make a recoverable copy of the user's `context/` directory if it contains data.
3. Replace this repository copy with the new release (pull the tag or unpack it).
4. Run the preview and read the operation list: an upgrade from 6.0.x shows the previous release's managed skill directories being removed from `.claude/skills/` and nothing else being deleted.
5. Run `python install.py --project-root <project> --backup-to <absent folder>`.
6. Verify the receipt, the four workflow directories on each host, and `.pbaw/runtime-manifest.json`.
7. Confirm existing context files are byte-for-byte unchanged (the receipt's `context/` hash).
8. An installation from version 5 or 6.0.x that lives under the home directory (`~/.claude/skills`, `~/.claude/rules`) is not touched: move its Product Org OS directories and rule files to a dated backup folder by hand.
9. Read the newest section of `CHANGELOG.md`, then run one bounded audit task before normal use.

## Reinstall, move, or uninstall

Re-running the installer is the supported update path. It replaces what it marked as its own and never removes unrelated directories or files.

To move to a different project: preview and install into the new project, verify it, then uninstall from the old one.

To uninstall, run the engine directly. It removes exactly the marked workflow directories, the managed rule files and their markers, and `.pbaw/`; it leaves `context/` and everything unmanaged in place:

```powershell
python tools\build\setup-skills.py --project-root "C:\path\to\project" --source . uninstall
```

The uninstall writes `.pbaw-uninstall-receipt.json` in the project root.

## Troubleshooting

| Symptom | What the coding agent should check |
|---|---|
| `python` is not found | Confirm Python 3.10+ is installed and use the platform's correct command, such as `py -3` on Windows if configured |
| `project root does not exist` | Pass the project folder that is actually open in the coding agent; the installer never creates it |
| `source digest mismatch` or a runtime-manifest error | The repository copy is incomplete or edited. Restore it from the release; the installer refuses a source whose files disagree with its manifest |
| `Installation refused or rolled back` | Read the printed reason. A workflow-named directory without a marker, a tampered marker, or an existing `--backup-to` folder each stop the transaction before any live write; resolve it and re-run |
| A slash workflow is not visible | Restart the coding-agent session after installation and verify the four directories on the host the session uses |
| A product role cannot load knowledge | Verify `.pbaw/runtime-manifest.json` lists the file and that it exists under `.pbaw/knowledge/`; re-run the installer from the repository copy if `.pbaw/` is incomplete |
| Rules are not active | Verify `.claude/rules/` in the project and confirm the tool supports that rules mechanism |
| Codex shows more or fewer than four Product Org OS workflows | Inspect `.agents/skills/` for unrelated pre-existing directories before changing anything; the installer only manages the four it marked |
| Existing context appears missing | Stop. Confirm the original context path and restore from the recoverable copy; do not create replacement records from memory |
| A task asks the agent to approve a decision | Refuse the approval step. Draft the decision for a named human owner instead |

## Handoff checklist

Before telling the user setup is complete, report:

- the repository path and the project path;
- the four workflow directories on each host;
- the `.pbaw/` tree and the receipt path;
- the local memory destination;
- the copied, updated, and deleted counts from the installer and the receipt's `unmanaged_and_context_preserved` value;
- the first recommended task;
- any limitation specific to the user's coding-agent environment.

Then direct the user to `agent-guide.md` for the operating model and worked examples.
