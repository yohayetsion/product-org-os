#!/usr/bin/env python3
"""
Product Org OS — Installer

Copies Product Org OS skills (and optionally rules + a context/ scaffold)
into the caller's Claude Code environment. Stdlib-only, cross-platform,
Python 3.8+.

Usage examples:

    # Default: install skills to ~/.claude/skills/, prompt for rules + context
    python install.py

    # Install skills elsewhere, skip both prompts
    python install.py --target /opt/claude/skills --no-rules --no-context

    # See what would happen without touching the filesystem
    python install.py --dry-run

    # Install skills + rules into a custom rules directory, skip context
    python install.py --rules-target ./project/.claude/rules --no-context

    # Windows
    python install.py --target C:/Users/me/.claude/skills

Flags:
    --target PATH         Where skills install (default: ~/.claude/skills/)
    --rules-target PATH   Where rules install (default: ./.claude/rules/)
    --no-rules            Skip the rules-install prompt entirely
    --no-context          Skip the context-layer bootstrap prompt entirely
    --dry-run             Print what would happen, don't touch the filesystem
    --help                Show this help

The installer NEVER overwrites an existing `index.md` in the context
scaffold. Skills and rules DO get overwritten on re-install.

Update flow: `cd <this repo> && git pull && python install.py`
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).resolve().parent
SKILLS_SRC = REPO_ROOT / "skills"
RULES_SRC = REPO_ROOT / "rules"

CONTEXT_SUBDIRS = [
    "decisions",
    "bets",
    "feedback",
    "learnings",
    "documents",
    "assumptions",
    "portfolio",
    "roi",
]


# ---------------------------------------------------------------------------
# Logging helpers
# ---------------------------------------------------------------------------

def log(msg: str, dry_run: bool = False) -> None:
    prefix = "[DRY RUN] " if dry_run else ""
    print(f"{prefix}{msg}")


def err(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Skills install
# ---------------------------------------------------------------------------

def install_skills(target: Path, dry_run: bool) -> int:
    """Copy every subdirectory under ./skills/ into the target directory.

    Returns the number of skill subdirs installed. Raises on filesystem errors.
    """
    if not SKILLS_SRC.is_dir():
        raise FileNotFoundError(
            f"Skills source directory not found: {SKILLS_SRC}. "
            "Are you running install.py from the Product Org OS repo root?"
        )

    if dry_run:
        log(f"Would create target directory if missing: {target}", dry_run=True)
    else:
        target.mkdir(parents=True, exist_ok=True)

    subdirs = sorted([p for p in SKILLS_SRC.iterdir() if p.is_dir()])
    count = 0
    for src_subdir in subdirs:
        dest_subdir = target / src_subdir.name
        action = "overwrite" if dest_subdir.exists() else "install"
        log(f"[{action}] {src_subdir.name}", dry_run=dry_run)
        if not dry_run:
            shutil.copytree(src_subdir, dest_subdir, dirs_exist_ok=True)
        count += 1

    log(f"Installed {count} skills to {target}", dry_run=dry_run)
    return count


# ---------------------------------------------------------------------------
# Rules install (prompted, overwrite-all)
# ---------------------------------------------------------------------------

def prompt_yes_no(question: str) -> bool:
    """Return True if the user types y / yes (case-insensitive)."""
    try:
        answer = input(f"{question} [y/N]: ").strip().lower()
    except EOFError:
        return False
    return answer in ("y", "yes")


def install_rules(rules_target: Path, dry_run: bool) -> int:
    """Copy every .md from ./rules/ into rules_target. Always overwrite."""
    if not RULES_SRC.is_dir():
        raise FileNotFoundError(
            f"Rules source directory not found: {RULES_SRC}. "
            "Are you running install.py from the Product Org OS repo root?"
        )

    if dry_run:
        log(f"Would create rules target if missing: {rules_target}", dry_run=True)
    else:
        rules_target.mkdir(parents=True, exist_ok=True)

    md_files = sorted(RULES_SRC.glob("*.md"))
    count = 0
    for src in md_files:
        dest = rules_target / src.name
        action = "overwrite" if dest.exists() else "install"
        log(f"[{action}] rules/{src.name}", dry_run=dry_run)
        if not dry_run:
            shutil.copy2(src, dest)
        count += 1

    log(f"Installed {count} rules to {rules_target}", dry_run=dry_run)
    return count


# ---------------------------------------------------------------------------
# Context-layer bootstrap (prompted, never overwrites index.md)
# ---------------------------------------------------------------------------

def bootstrap_context(base: Path, dry_run: bool) -> int:
    """Create ./context/<subdir>/index.md for each subdir, only if missing."""
    created = 0
    for sub in CONTEXT_SUBDIRS:
        dir_path = base / "context" / sub
        index_path = dir_path / "index.md"

        if dry_run:
            log(f"Would ensure directory: {dir_path}", dry_run=True)
            if not index_path.exists():
                log(f"Would create empty index: {index_path}", dry_run=True)
                created += 1
            else:
                log(f"Would skip existing index: {index_path}", dry_run=True)
            continue

        dir_path.mkdir(parents=True, exist_ok=True)
        if not index_path.exists():
            index_path.write_text("", encoding="utf-8")
            log(f"[create] context/{sub}/index.md")
            created += 1
        else:
            log(f"[skip — exists] context/{sub}/index.md")

    log(f"Context bootstrap: {created} new index.md file(s) created.", dry_run=dry_run)
    return created


# ---------------------------------------------------------------------------
# Next-steps block (printed only on success)
# ---------------------------------------------------------------------------

def print_next_steps(skills_target: Path) -> None:
    print()
    print("Next steps:")
    print(f"  - Skills installed to {skills_target}. Start a Claude Code session and")
    print("    invoke an agent: @pm, @vp-product, @cpo, @pmm-dir, or a gateway (/product, /plt).")
    print("  - Methodology: read PRINCIPLES.md in this repo for the Vision to Value")
    print("    6-phase model.")
    print("  - Invocation patterns: see agent-guide.md in this repo (@agent vs /skill,")
    print("    gateways, multi-agent meetings).")
    print("  - Update later: `cd <this repo> && git pull && python install.py`")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="install.py",
        description="Install Product Org OS skills (and optionally rules + context scaffold).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--target",
        type=str,
        default=str(Path.home() / ".claude" / "skills"),
        help="Where skills install (default: ~/.claude/skills/)",
    )
    parser.add_argument(
        "--rules-target",
        type=str,
        default=str(Path.cwd() / ".claude" / "rules"),
        help="Where rules install (default: ./.claude/rules/)",
    )
    parser.add_argument(
        "--no-rules",
        action="store_true",
        help="Skip the rules-install prompt entirely",
    )
    parser.add_argument(
        "--no-context",
        action="store_true",
        help="Skip the context-layer bootstrap prompt entirely",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would happen without touching the filesystem",
    )
    return parser.parse_args(argv)


def resolve_target(raw: str) -> Path:
    # pathlib does not expand `~` automatically.
    return Path(raw).expanduser().resolve()


def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    dry_run = args.dry_run

    skills_target = resolve_target(args.target)
    rules_target = resolve_target(args.rules_target)

    if dry_run:
        log("Dry-run mode: no filesystem changes will be made.", dry_run=True)
        log("Dry-run assumes 'yes' to all prompts (unless --no-rules / --no-context).", dry_run=True)

    # --- Skills (always) ---
    try:
        install_skills(skills_target, dry_run=dry_run)
    except (OSError, PermissionError, FileNotFoundError) as exc:
        err(f"Failed to install skills: {exc}")
        return 1

    # --- Rules (prompted unless --no-rules) ---
    if args.no_rules:
        log("Skipping rules install (--no-rules).", dry_run=dry_run)
    else:
        do_rules = True if dry_run else prompt_yes_no(
            "Copy behavioral rules into ./.claude/rules/ in the current directory?"
        )
        if do_rules:
            try:
                install_rules(rules_target, dry_run=dry_run)
            except (OSError, PermissionError, FileNotFoundError) as exc:
                err(f"Failed to install rules: {exc}")
                return 1
        else:
            print("Skipping rules install.")

    # --- Context-layer bootstrap (prompted unless --no-context) ---
    if args.no_context:
        log("Skipping context-layer bootstrap (--no-context).", dry_run=dry_run)
    else:
        do_context = True if dry_run else prompt_yes_no(
            "Initialize context layer in current directory? Creates context/ folder structure."
        )
        if do_context:
            try:
                bootstrap_context(Path.cwd(), dry_run=dry_run)
            except (OSError, PermissionError) as exc:
                err(f"Failed to bootstrap context layer: {exc}")
                return 1
        else:
            print("Skipping context-layer bootstrap.")

    # --- Success ---
    if not dry_run:
        print_next_steps(skills_target)
    else:
        log("Dry run complete. Re-run without --dry-run to apply.", dry_run=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
