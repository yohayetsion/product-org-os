#!/usr/bin/env python3
"""install.py - Product Org OS installer (client-run).

A thin wrapper over the shipped engine `tools/build/setup-skills.py`. One journalled
transaction projects this release tree onto YOUR project root: `.pbaw/` (agents,
capabilities, knowledge, rules, tools and the installed runtime manifest), the four harness
skills for Claude Code (`.claude/skills`) and Codex (`.agents/skills`), and the product rules
(`.claude/rules`). Skills and rules of your own in those folders are never touched. It then
scaffolds `context/` (your organizational memory, never shipped) and places
`context/allocate-id.py`.

Usage:
    python install.py --project-root PATH               # install into that project
    python install.py --project-root PATH --preview     # print the operation list, write nothing
    python install.py --project-root PATH --backup-to DIR   # durable copy of the host folders first
    python install.py --project-root PATH --no-context
"""
from __future__ import annotations
import argparse, importlib.util, shutil, sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
ENGINE = REPO_ROOT / "tools" / "build" / "setup-skills.py"
CONTEXT_SUBDIRS = (
    "decisions", "bets", "feedback", "learnings", "documents", "assumptions",
    "portfolio", "principles", "roi", "roi/history", "interactions", "handoffs", "preferences",
)

# The layout the PREVIOUS release's installer wrote into a project - declared here, never
# inferred from the tree under test. The engine may shrink or adopt exactly these once
# (an upgrade), and nothing else in those folders.
LEGACY_LAYOUT = {
    ".claude/skills": (
        "analytics-tracking", "ansoff-matrix", "assumption-map", "audit", "bcg-matrix",
        "bet-invalidation-checkpoint", "bias-check", "bizdev", "bizops", "blue-ocean",
        "brainstorming", "business-case", "business-model-canvas", "business-plan",
        "campaign-brief", "collaboration-check", "commitment-check", "competitive-analysis",
        "competitive-battlecard", "competitive-intelligence", "competitive-landscape",
        "competitor-alternatives", "compound", "context-harvest", "context-recall", "context-save",
        "continuation-threshold", "cpo", "customer-health-scorecard", "customer-journey-map",
        "customer-value-trace", "daci", "decision-charter", "decision-quality-audit",
        "decision-record", "design-sprint", "dhm-analysis", "director-product-management",
        "director-product-marketing", "dispatching-parallel-agents", "escalation-rule",
        "experiment-design", "feature-spec", "feedback-capture", "feedback-recall",
        "four-risks-check", "growth-model", "gtm-brief", "gtm-strategy", "handoff", "heart-metrics",
        "index-folder", "interaction-recall", "interview-synthesis", "kano-analysis",
        "launch-narrative-brief", "launch-plan", "launch-readiness", "launch-strategy",
        "lean-canvas", "llm-seo", "market-analysis", "market-segment", "marketing-psychology",
        "maturity-check", "mentor", "messaging-architecture", "north-star-metric", "okr-writer",
        "onboarding-playbook", "ooda-loop", "operating-calendar", "opportunity-tree",
        "outcome-review", "ownership-map", "partnership-architecture", "pbaw", "pestle-analysis",
        "phase-check", "pirate-metrics", "plan", "plt", "pm", "pm-dir", "pm-level-check", "pmm",
        "pmm-dir", "porter-five-forces", "portfolio-status", "portfolio-tradeoff",
        "positioning-statement", "prd", "prd-outline", "pre-mortem", "present", "press-release-faq",
        "pretotype", "pricing-model", "pricing-strategy", "prioritize-features", "prodops",
        "product", "product-leadership-team", "product-manager", "product-marketing-manager",
        "product-mentor", "product-operations", "product-roadmap", "product-teardown", "qbr-deck",
        "relevant-learnings", "retrospective", "roadmap-item", "roadmap-theme", "roi-report",
        "saas-health-check", "sales-enablement", "scale-check", "seven-powers", "shape-up",
        "stakeholder-brief", "stakeholder-map", "strategic-bet", "strategic-intent",
        "strategy-communication", "subject-line", "swot-analysis", "theory-of-constraints",
        "user-story", "v2v-install-90-day", "value-realization", "value-realization-report",
        "verification-before-completion", "vision-statement", "vision-to-value-document-map",
        "vp-product", "vpp", "wardley-map", "win-loss-decision-signal", "writing-plans",
    ),
    ".agents/skills": (
        "audit", "context-harvest", "pbaw", "plan",
    ),
    ".claude/rules": (
        "agent-metadata-schema.md", "agent-output-automation.md", "agent-spawn-protocol.md",
        "auto-context.md", "context-graph.md", "context-management.md", "delegate-first.md",
        "delegation-protocol.md", "dr-affirmation-presentation.md", "no-estimates.md",
        "parallel-execution.md", "presentation-format.md", "roi-display.md",
        "sensitive-skill-guardrails.md", "skill-awareness.md", "source-attribution.md",
    ),
    ".claude/rules-reference": (
    ),
}


def log(message: str) -> None:
    print(message)


def err(message: str) -> None:
    print("ERROR: " + message, file=sys.stderr)


def load_engine():
    if not ENGINE.is_file():
        raise FileNotFoundError("the shipped engine is absent: %s" % ENGINE)
    spec = importlib.util.spec_from_file_location("pbaw_setup_skills", ENGINE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def scaffold_context(ctx: Path) -> None:
    """Create the local context/ memory (folders only) and place the id allocator beside it."""
    for sub in CONTEXT_SUBDIRS:
        (ctx / sub).mkdir(parents=True, exist_ok=True)
    allocator = REPO_ROOT / "tools" / "allocate-id.py"
    if allocator.is_file():
        shutil.copy2(allocator, ctx / "allocate-id.py")
        log("  placed allocate-id.py at %s" % (ctx / "allocate-id.py"))
    else:
        err("tools/allocate-id.py not found - context ids will collide. "
            "The bundle is expected to carry it.")
    log("Scaffolded context/ memory at %s (%d subdirs; index files: the assistant writes them)"
        % (ctx, len(CONTEXT_SUBDIRS)))


def main() -> int:
    version_file = REPO_ROOT / "VERSION"
    version = version_file.read_text(encoding="utf-8").strip() if version_file.exists() else "unknown"
    ap = argparse.ArgumentParser(description="Install Product Org OS %s into a project." % version)
    ap.add_argument("--project-root", required=True, help="the project to install into (opened in Claude Code / Codex)")
    ap.add_argument("--context-dir", help="where to scaffold context/ (default: <project>/context)")
    ap.add_argument("--no-context", action="store_true")
    ap.add_argument("--preview", action="store_true", help="stage, print the operation list, write nothing")
    ap.add_argument("--backup-to", metavar="DIR",
                    help="durable copy of the host folders into an ABSENT directory before the sync")
    args = ap.parse_args()
    project = Path(args.project_root).resolve()
    if not project.is_dir():
        err("project root does not exist: %s" % project)
        return 2
    engine = load_engine()
    config = engine.WorkspaceConfig(project, engine.default_allowlist(REPO_ROOT), source=REPO_ROOT,
                                    legacy_managed={key: set(names) for key, names in LEGACY_LAYOUT.items()})
    if args.preview:
        result = engine.sync_workspace(config, preview=True)
        log("Preview (nothing written): %d operations for %s" % (len(result["operations"]), project))
        for op in result["operations"]:
            log("  %s %s%s" % (op["kind"], op["target"], " (existing)" if op["existed"] else ""))
        return 0
    try:
        report = engine.sync_workspace(config, backup_to=args.backup_to)
    except Exception as exc:  # the engine rolled back; nothing half-installed remains
        err("Installation refused or rolled back: %s" % exc)
        return 1
    if not args.no_context:
        scaffold_context(Path(args.context_dir).resolve() if args.context_dir else project / "context")
    log("\nProduct Org OS installed into %s" % project)
    log("  - copied %d, updated %d, deleted %d; receipt: %s"
        % (report["copied"], report["updated"], report["deleted"], config.receipt))
    log("  - Claude Code: .claude/skills/{audit, context-harvest, pbaw, plan}; Codex: .agents/skills/{...}")
    log("  - the workforce loads its agents, capabilities and knowledge from .pbaw/ (see agent-guide.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
