# Product Org OS

**Add a complete product organization to your coding agent.**

Product Org OS is a free, MIT-licensed set of product roles, repeatable workflows, and professional knowledge for people who use coding agents to run product work. It helps the agent move from a vague request to a reviewed deliverable while keeping important decisions with a named human owner.

Version 6.2.0 is measured in `COMPONENT-MANIFEST.md`, which is generated from the runtime manifest. The package includes the product roles, their methods and controls, the knowledge packs they load, four operating workflows, the governing rules and companions, the installer and its engine, the official Product Org OS logo, and the installation and release documents at the repository root.

## What it gives you

| You need | Product Org OS provides |
|---|---|
| Product judgment | Eleven product roles covering leadership, management, marketing, operations, competitive intelligence, business operations, business development, and value realization |
| Repeatable work | Skills for product requirements, roadmaps, discovery, pricing, launches, positioning, decision records, portfolio reviews, and more |
| Grounded answers | Knowledge packs that roles load when the work calls for them |
| A reliable way to operate | Four workflows for planning, assigning specialist work, checking the result, and preserving useful context |
| Human control | A spawn protocol that records what the agent loaded, what it produced, and which decisions still belong to you |

Product Org OS is the open-source edition of the licensed ProductBeacon AI Agentic Workforce. It includes the PBAW harness and product team. In this public repository, PBAW means the governed method used to select a Product Org OS role, load the right instructions and knowledge, run the task, and report the evidence. You do not need to know the name before installing the system.

## Quick start

Requirements: Python 3.10 or newer, a local copy of this repository, and a project folder you open in Claude Code or Codex. The installer writes into the project you name; the repository copy stays the source for upgrades.

```powershell
git clone https://github.com/yohayetsion/product-org-os.git
cd product-org-os
python install.py --project-root <your-project> --preview
python install.py --project-root <your-project>
```

Then open the project in your coding agent and give it this instruction:

> Read `CLAUDE.md` and `agent-guide.md`. Explain Product Org OS in plain language, verify the installation, show me the available product roles, and help me choose a small first task. Do not change files until I approve the task.

See [INSTALL-AND-ONBOARD.md](./INSTALL-AND-ONBOARD.md) for a complete coding-agent installation, verification, upgrade, and troubleshooting guide.

## Repository map

```text
product-org-os/
├── README.md                         # This first-time-user overview
├── INSTALL-AND-ONBOARD.md           # Safe install, verification, and handoff
├── agent-guide.md                   # Complete coding-agent operating guide
├── CLAUDE.md                        # Repository front door for a coding agent
├── install.py                       # Installs into a project you name (wrapper over tools/build/setup-skills.py)
├── COMPONENT-MANIFEST.md            # Measured public release contents (generated)
├── runtime-manifest.json            # Every shipped file, its hash, and what it requires
├── index.html                       # Product overview
├── whats-new-v6.html                # Version 6 release story
├── agents/                          # The eleven product roles
├── skills/                          # Product methods and controls
├── harness/                         # The four operating workflows: plan, pbaw, audit, context-harvest
├── knowledge/                       # Knowledge packs the roles load
├── rules/                           # Governing rules, with their companions in rules/reference/
└── tools/                           # The installer engine, hooks, and the context-id allocator
```

The repository copy stays the installer's source: re-run `install.py` from it to upgrade. During product work, roles, knowledge packs, and governing instructions are resolved from the project's `.pbaw/` tree, never from the repository.

## How it works

```text
Your outcome in plain language
            ↓
Plan when the work is non-trivial
            ↓
Choose the right Product Org OS role
            ↓
Load its instructions, knowledge, and relevant local context
            ↓
Create or review the product work
            ↓
Audit before sign-off
            ↓
Preserve accepted decisions and learning locally
```

The coding agent handles the routing. The user can ask for a result such as “review this roadmap,” “turn these interviews into a decision,” or “audit this launch plan.” The agent identifies the role and method, shows what it loaded, and keeps unresolved material decisions with the human owner.

Small tasks do not require a large process. Planning and audit depth scale with consequence, uncertainty, and reversibility.

## The four operating workflows

| Workflow | What it does |
|---|---|
| `/plan` | Turns non-trivial work into an explicit plan and surfaces decisions for the owner |
| `/pbaw` | Selects and runs the right Product Org OS specialist under the governed spawn protocol |
| `/audit` | Checks a plan before execution or checks a completed result before sign-off |
| `/context-harvest` | Saves durable decisions, assumptions, learnings, feedback, and document references after the work is complete |

Start with the outcome you need. You do not need to know which role or workflow should handle it; the coding agent should route the request for you.

## What's included

### Eleven product roles

| Discipline | Roles |
|---|---|
| Product leadership | Chief Product Officer, VP Product, Director of Product Management |
| Product management | Product Manager |
| Product marketing | Director of Product Marketing, Product Marketing Manager |
| Operations and commercial | Product Operations, Business Operations, Business Development |
| Evidence and outcomes | Competitive Intelligence, Value Realization |

Specialist selection happens inside `/pbaw`. It routes an outcome to the relevant product role, or brings independent leadership perspectives together for a consequential cross-functional decision.

### Skills

The verified public inventory of product methods and supporting controls is listed in `COMPONENT-MANIFEST.md`. Examples include:

- strategy: strategic intent, market analysis, competitive landscape, Seven Powers, Wardley mapping, business model, and portfolio trade-offs;
- discovery: interview synthesis, assumption mapping, opportunity trees, design sprints, pretotyping, and experiment design;
- planning: product requirements, feature specifications, roadmaps, prioritization, decision records, ownership, and stakeholder alignment;
- go-to-market: positioning, messaging, pricing, launch planning, sales enablement, and campaign briefs;
- operations and outcomes: operating calendars, QBRs, product health, outcome reviews, customer value traces, and value realization reports;
- control and learning: planning, specialist assignment, audit, verification, feedback capture, context recall, and context harvest.

The complete measured list is in [COMPONENT-MANIFEST.md](https://github.com/yohayetsion/product-org-os/blob/v6.2.0/COMPONENT-MANIFEST.md). Direct command availability varies by coding-agent host; the files remain available as operating instructions.

### Knowledge packs

The release ships every knowledge file declared by its public product roles; the list is in `COMPONENT-MANIFEST.md`. Subjects include discovery, market research, prioritization, metrics, pricing, software-as-a-service economics, product marketing, growth, partnerships, public relations, operations, change management, design systems, agent supervision, agent security, compliance, and value measurement.

A role declares always-read and conditional packs. The coding agent reports what it loaded. If a required pack is missing, the run must say so instead of silently substituting generic model knowledge.

### Local context and decision records

Installation creates an empty, user-owned `context/` structure. It can hold:

- document references;
- accepted decisions and their owners;
- strategic bets and invalidation conditions;
- assumptions that need evidence;
- learnings supported by observed results;
- attributed feedback and interaction records.

No customer memory ships in the repository. Recommendations are not stored as accepted decisions unless a named human owner explicitly accepts them.

## Vision to Value

Product Org OS organizes product work around six connected phases:

1. **Vision and strategy:** define ambition, market position, strategic choices, and intended outcomes.
2. **Discover and validate:** investigate customer needs, evidence, risks, and assumptions.
3. **Plan and commit:** translate learning into accountable decisions, priorities, requirements, and roadmaps.
4. **Build and release:** maintain product intent through specifications, collaboration, readiness, and launch.
5. **Operate and grow:** improve adoption, coordinate the portfolio, and respond to evidence.
6. **Realize value:** measure outcomes and feed the learning into the next strategic choice.

The lifecycle is a map, not a required waterfall. A task may begin in any phase. The coding agent uses the map to identify missing upstream evidence and downstream consequences, then selects only the methods needed for the requested outcome.

## Use cases

### Review an existing artifact

```text
Review this product requirements document as a Product Manager. Do not edit it.
Identify missing user evidence, unresolved decisions, scope ambiguity, and weak
acceptance criteria. Show what instructions and knowledge you loaded.
```

### Prepare a material decision

```text
Help me decide whether to change our packaging. Use only the attached evidence.
Compare alternatives, identify assumptions, make a recommendation, and leave the
decision in draft for the named human owner.
```

### Audit before approval

```text
Audit this launch plan before I approve it. Separate blockers, important gaps,
and optional improvements. Cite the sections that support each finding.
```

### Coordinate product leadership

```text
Use the Product Leadership Team only if independent product-management,
product-marketing, operations, and value perspectives are necessary. Preserve
disagreements and give me one synthesis organized around the decision I need to make.
```

## What's new in version 6

- Four governed workflows provide one control loop for planning, specialist work, audit, and local memory.
- Planning ceremony is proportional to task risk and complexity.
- Material decisions are explicitly human-held, with recommendation and acceptance separated.
- Claude Code and Codex receive documented, environment-specific installation and onboarding paths.
- The public package ships every knowledge pack declared by its product roles.
- The public landing page and release page build on the proven version 5 visual and information architecture while using current, verified content.
- Private specialist teams, customer material, and private memory remain outside the public package.

See [What's new in Product Org OS 6](./whats-new-v6.html) for the full release story and [CHANGELOG.md](https://github.com/yohayetsion/product-org-os/blob/v6.2.0/CHANGELOG.md) for patch-level details.

## Supported use

| Environment | Support in this package |
|---|---|
| Claude Code | The four operating workflows on `.claude/skills/`, the rules on `.claude/rules/`, and every role, skill, and knowledge pack in the project's `.pbaw/` tree |
| Codex | The four operating workflows on `.agents/skills/`; product roles are invoked through `/pbaw` from the project's `.pbaw/` tree |
| Other tools that read `SKILL.md` | The files are portable, but you must connect the tool to the repository and follow `agent-guide.md` manually |

## What is not included

This repository contains the public product organization. It does not include ProductBeacon's private specialist teams or customer material. The installer creates an empty local `context/` structure for your own decisions and history; no user memory ships in the repository and no telemetry destination is configured.

## Documentation

- [Install and onboard](./INSTALL-AND-ONBOARD.md): the complete setup path for a coding agent
- [Agent guide](./agent-guide.md): how the system fits together and how to operate it
- [Component manifest](https://github.com/yohayetsion/product-org-os/blob/v6.2.0/COMPONENT-MANIFEST.md): measured package contents
- [What's new in version 6](./whats-new-v6.html): the release story
- [Changelog](https://github.com/yohayetsion/product-org-os/blob/v6.2.0/CHANGELOG.md): release history

## License

MIT. See [LICENSE](./LICENSE) and [NOTICE](./NOTICE).
