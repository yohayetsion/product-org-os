# Changelog

## [6.2.0] - 2026-09-06

- Removed per-file metadata versions. The package VERSION identifies the release.

## [6.1.0] - 2026-08-29

- The harness ships four human-facing skills: `/pbaw`, `/plan`, `/audit`, and `/context-harvest`. `/pbaw <task>` selects the specialist or specialists inside the run; there is nothing else to learn.
- Retired the `product` and `product-leadership-team` gateway skills and the alias registry. Retired with them, and intentionally not re-created: the depth modifiers, the voting, the roster, and the portfolio frameworks the leadership gateway carried.
- Retired the Product Mentor role. The public organization has eleven product roles.
- New installer. `python install.py --project-root <project>` installs into a project you name: every role, skill, knowledge pack, rule, and tool lands in the project's `.pbaw/` tree with an opaque-id runtime manifest, an install ledger, and a sync receipt; the four workflows are projected onto `.claude/skills/` and `.agents/skills/` with ownership markers; the rules land in `.claude/rules/` and their companions in `.claude/rules-reference/`. `--preview` writes nothing, `--backup-to` copies the host folders first, and an upgrade from 6.0.x removes only the previous release's managed directories. An older installation under the home directory is outside the installer's authority and is removed by hand.
- Counts moved out of the prose. `COMPONENT-MANIFEST.md` is generated from the runtime manifest and is the one place a figure is stated.

## [6.0.4] - 2026-08-25

- Reframed the landing page around the four harness commands: `/pbaw`, `/plan`, `/audit`, and `/context-harvest`.
- Removed manual role-spawn instructions from the landing-page use cases, operating guide, runtime example, and role inventory labels.
- Explained that the harness automatically selects the relevant product roles, skills, and knowledge packs at runtime.
- Shortened the opening Product Org OS and ProductBeacon AI Agentic Workforce positioning.
- Removed the "A Clean Package. A Hard Boundary." and "Verified. Complete." sections from What's New while retaining the established version 5 release-story system.
- Replaced private-repository-dependent raw and blob guide links with packaged relative links and a repository-local onboarding prompt.
- Added regression checks for the harness-first operating model, self-contained content links, intentional author attribution, and the two owner-approved release-section removals.

## [6.0.3] - 2026-08-24

- Restored the literal version 5 `index.html` as the landing-page baseline and evolved it with minimum copy, inventory, link, example, and unsupported-claim corrections.
- Built `whats-new-v6.html` from the literal version 5 release-story page, preserving its CSS and DOM composition while updating the narrative for the verified version 6 package.
- Defined ProductBeacon AI Agentic Workforce (PBAW) for first-time readers before using the acronym.
- Reconciled the outbound inventory to 12 product roles, 140 skill directories, 36 knowledge packs, and four governed workflows.
- Replaced obsolete private or unshipped skill examples and the unsupported remote-memory claim with shipped product methods and a local-context boundary.
- Added a regression gate that compares both outbound pages with the frozen version 5 CSS and DOM baselines.
- Synchronized the installer's command-line help with the 6.0.3 release identity.
- Replaced the unbreakable raw guide URL in the release-story feature card with repository-local guide names so the inherited v5 mobile layout does not overflow.

## [6.0.2] - 2026-08-24

- Rebuilt `index.html` on the established version 5 Product Org OS layout and visual system: dark branded palette, fixed navigation, terminal demonstration, lifecycle sections, role and skill cards, knowledge inventory, context model, principles, and installation close.
- Rebuilt `whats-new-v6.html` on the version 5 release-page composition with a release hero, verified-statistics band, five alternating feature stories, and a copy-ready onboarding prompt.
- Expanded `agent-guide.md` from the previous guide rather than replacing it: compatibility, lifecycle skill routing, strategy frameworks, document intelligence, operating principles, context structure, multi-product use, collaboration patterns, user onboarding, and the complete 140-directory inventory.
- Expanded `INSTALL-AND-ONBOARD.md`, `README.md`, and `CLAUDE.md` with an observed inventory tour, Claude Code and Codex project front doors, and a bounded first-request path.
- Added regression checks that preserve outbound layout continuity and coding-agent guide inheritance.
- Retained the 6.0.1 knowledge-pack correction: all 36 public knowledge packs declared by shipped roles remain present and automatically checked.
- The four core workflows are unchanged in this patch.

## [6.0.1] - 2026-08-24

- Added the owner-affirmed proportional-planning policy from DR-2026-364 to `plan`, `audit`, and `pbaw`: one controlling plan, evidence-based blockers, a loop escape, and risk-routed guidance.
- Rewrote the README, coding-agent install guide, agent guide, and website for a first-time external reader.
- Defined ProductBeacon AI Agentic Workforce (PBAW) before using the acronym.
- Restored 24 role-dependency knowledge files omitted by the lean v6.0.0 allowlist; the release now carries 36 Product Org OS knowledge packs plus the knowledge README.
- Removed the retired plugin-packaging reference from Product Operations.
- Added regression checks for outbound terminology, coding-agent onboarding completeness, and declared knowledge-pack conveyance.
- `context-harvest` is unchanged in this patch.

## [6.0.0] - 2026-08-24

- Rebuilt Product Org OS as a standalone public package with fresh repository history.
- Added the complete ProductBeacon AI Agentic Workforce (PBAW) operating layer: `pbaw`, `plan`, `audit`, and `context-harvest`.
- Added deterministic Claude Code installation and a Codex projection of exactly those four operator skills.
- Added the canonical seven-alias registry, current spawn protocol, rule companions, runtime hooks and context-ID allocator.
- Removed private ProductBeacon specialist teams, private development specialists, retired methodology references, and plugin-era manifests from the public package.
- Updated licensing, onboarding, component inventory, release site and upgrade guidance for the v6 package boundary.
