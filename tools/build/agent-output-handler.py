#!/usr/bin/env python3
"""
================================================================================
AGENT OUTPUT HANDLER - Post-process agent deliverables
================================================================================

Handles the workflow:
1. Save content to MD file
2. Convert to MOBILE-FRIENDLY HTML presentation (scroll-based, responsive)
3. Get Google Drive shareable links
4. Open in browser
5. Send Telegram notification with Drive links

USAGE:
    python agent-output-handler.py <md_file_path>
    python agent-output-handler.py <md_file_path> --no-telegram
    python agent-output-handler.py <md_file_path> --no-browser
    python agent-output-handler.py <md_file_path> --no-drive

Called automatically by Claude Code via the post-agent-output rule.

================================================================================
"""

import sys
import os
import json
import argparse
import subprocess
import re
import sqlite3
import time
from pathlib import Path
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.parse import urlencode

# ── Configuration ─────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
CONFIG_FILE = SCRIPT_DIR / "telegram-bridge-config.json"
# Paths are configurable via environment (M12 — portability + first-run provisioning).
# Current values are the defaults, so existing behavior is unchanged when the env
# vars are unset; downstream installs override AOH_PRESENTATIONS_DIR / AOH_DRIVE_ROOT /
# AOH_DRIVEFS_DB to fit their environment.
PRESENTATIONS_DIR = Path(os.environ.get("AOH_PRESENTATIONS_DIR", "presentations"))
DRIVE_ROOT = Path(os.environ.get("AOH_DRIVE_ROOT", "«drive-root»"))
DRIVEFS_DB = Path(os.environ.get(
    "AOH_DRIVEFS_DB",
    r"AppData/Local/Google/DriveFS/«drivefs-account-id»/metadata_sqlite_db"))
# Commentable-engine asset files (referenced by md_to_commentable_html +
# inject_commentable_layer). They live alongside the generated decks in the
# presentations dir; both callers guard on .exists() so absence degrades gracefully.
COMMENTABLE_ENGINE_CSS = PRESENTATIONS_DIR / "commentable-engine.css"
COMMENTABLE_ENGINE_JS = PRESENTATIONS_DIR / "commentable-engine.js"

# ── Secret-detection guard (added 2026-05-18 after the May 6 PB Resend leak) ──
#
# Scans MD content for API keys / tokens / credentials BEFORE any HTML is
# generated or published. Halts the build with a clear error showing the
# match line. Override with --allow-secrets when documenting a secret pattern
# is legitimate (e.g. in a runbook explaining what to rotate).

SECRET_PATTERNS = {
    # Provider-prefixed keys (high precision, near-zero false positives)
    "resend_api_key":      r"\bre_[A-Za-z0-9_-]{20,}\b",
    "openai_key":          r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b",
    "anthropic_key":       r"\bsk-ant-[A-Za-z0-9_-]{32,}\b",
    "github_pat":          r"\bgh[pousr]_[A-Za-z0-9]{36,}\b",
    "github_fine_pat":     r"\bgithub_pat_[A-Za-z0-9_]{82,}\b",
    "google_api_key":      r"\bAIza[A-Za-z0-9_-]{35}\b",
    "aws_access_key":      r"\bAKIA[0-9A-Z]{16}\b",
    "stripe_live_secret":  r"\b(?:sk|rk)_live_[A-Za-z0-9]{24,}\b",
    "stripe_live_pub":     r"\bpk_live_[A-Za-z0-9]{24,}\b",
    "slack_token":         r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b",
    "jwt_token":           r"\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b",
    "pdl_api_key_env":     r"PDL_API_KEY\s*[:=]\s*['\"]?[a-f0-9]{40,}['\"]?",
}


def scan_content_for_secrets(content: str) -> list:
    """Scan MD content for known secret patterns. Returns list of dicts
    with keys: pattern_name, match, line_number, line_excerpt.
    """
    findings = []
    lines = content.split("\n")
    for name, pattern in SECRET_PATTERNS.items():
        for match in re.finditer(pattern, content):
            # Compute line number from offset
            offset = match.start()
            line_no = content[:offset].count("\n") + 1
            line_excerpt = lines[line_no - 1] if line_no - 1 < len(lines) else ""
            # Redact the actual secret in the excerpt for display
            redacted_excerpt = re.sub(pattern, lambda m: m.group(0)[:8] + "...[REDACTED]", line_excerpt)
            findings.append({
                "pattern_name": name,
                "match": match.group(0)[:8] + "...[REDACTED]",
                "line_number": line_no,
                "line_excerpt": redacted_excerpt.strip()[:200],
            })
    return findings


# ── Utilities ─────────────────────────────────────────────────────────────────

def load_config():
    """Load Telegram config."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}


def send_telegram(message: str, config: dict) -> bool:
    """Send Telegram notification."""
    bot_token = config.get("bot_token")
    chat_id = config.get("chat_id")

    if not bot_token or not chat_id:
        print("Telegram not configured, skipping notification")
        return False

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = urlencode({
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }).encode()

    try:
        req = Request(url, data=data)
        with urlopen(req, timeout=10) as response:
            return response.status == 200
    except Exception as e:
        print(f"Telegram error: {e}")
        return False


def open_in_browser(file_path: Path):
    """Open file in default browser."""
    if sys.platform == 'win32':
        os.startfile(str(file_path))
    elif sys.platform == 'darwin':
        subprocess.run(['open', str(file_path)])
    else:
        subprocess.run(['xdg-open', str(file_path)])


def get_drive_link(file_path: Path, max_retries: int = 3) -> str:
    """Get Google Drive shareable link for a file.

    Uses the DriveFS metadata database to find the file ID.
    Retries a few times since sync may not be instant.
    """
    # Check if file is in Google Drive folder
    try:
        relative_path = file_path.resolve().relative_to(DRIVE_ROOT)
    except ValueError:
        return None  # Not in Drive folder

    filename = file_path.name

    if not DRIVEFS_DB.exists():
        print(f"DriveFS database not found at {DRIVEFS_DB}")
        return f"[In Google Drive: {relative_path}]"

    for attempt in range(max_retries):
        try:
            conn = sqlite3.connect(str(DRIVEFS_DB))
            cursor = conn.cursor()

            # Query for the file ID (exclude local-only entries)
            cursor.execute(
                "SELECT id FROM items WHERE local_title = ? AND id NOT LIKE 'local-%'",
                (filename,)
            )
            result = cursor.fetchone()
            conn.close()

            if result:
                file_id = result[0]
                return f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"

            # File not synced yet, wait and retry
            if attempt < max_retries - 1:
                print(f"File not synced yet, waiting... (attempt {attempt + 1}/{max_retries})")
                time.sleep(2)

        except Exception as e:
            print(f"Drive link error: {e}")
            break

    # Fallback to path reference
    return f"[In Google Drive: {relative_path}]"


# ── Mobile-Friendly HTML Template ─────────────────────────────────────────────

MOBILE_HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="{html_lang}"{html_dir}{html_theme_class}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<title>{title}</title>
{favicon}
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&family=Roboto+Slab:wght@400;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
/* Hide scrollbar completely */
::-webkit-scrollbar {{ display: none; }}
html, body {{ scrollbar-width: none; -ms-overflow-style: none; }}

:root {{
  --primary: {primary_color};
  --accent: {accent_color};
  --bg-dark: #0D1117;
  --bg-card: #161B22;
  --bg-elevated: #1C2128;
  --text-primary: #E6EDF3;
  --text-secondary: #8B949E;
  --text-muted: #6B7280;
  --border: rgba(255,255,255,0.08);
  --gradient-brand: linear-gradient(135deg, {primary_color}, {accent_color});
}}

* {{ margin: 0; padding: 0; box-sizing: border-box; }}

html, body {{
  font-family: 'Manrope', system-ui, sans-serif;
  background: var(--bg-dark);
  color: var(--text-primary);
  height: 100%; width: 100%;
}}

/* ── RTL Support ── */
html[dir="rtl"] body,
html[dir="rtl"] .slide,
html[dir="rtl"] .slide * {{
  text-align: right;
}}
html[dir="rtl"] table {{ direction: rtl; }}
html[dir="rtl"] th, html[dir="rtl"] td {{ text-align: right; }}
html[dir="rtl"] ul, html[dir="rtl"] ol {{ padding-right: 1.5em; padding-left: 0; }}
html[dir="rtl"] .brand-bar {{ flex-direction: row-reverse; }}
html[dir="rtl"] .brand-logo {{ flex-direction: row-reverse; }}
html[dir="rtl"] .bottombar {{ direction: ltr; }}

/* ── Slide System ── */
.slide {{
  display: none;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px 80px;
  position: relative;
  overflow-y: auto;
  flex-direction: column;
}}
.slide.active {{ display: flex; }}

/* ── Mobile safety: never exceed the viewport width; scale media down ── */
html, body {{ overflow-x: hidden; max-width: 100%; }}
.slide {{ overflow-x: hidden; }}
.slide svg {{ max-width: 100% !important; height: auto !important; }}
.commentable {{ max-width: 100%; }}
.hero-title, h1, h2, h3, p, li, blockquote {{ overflow-wrap: break-word; word-wrap: break-word; }}

/* Print / Save as PDF — render as a FLOWING DOCUMENT, not slide screenshots */
@media print {{
  @page {{ margin: 18mm 16mm; }}
  /* Re-map theme variables so every var(--...) reference resolves to light-on-white */
  :root {{
    --bg-dark: #ffffff; --bg-card: #ffffff; --bg-elevated: #f4f4f4;
    --text-primary: #111111; --text-secondary: #2a2a2a; --text-muted: #555555;
    --border: #cccccc;
  }}
  html, body {{
    height: auto !important; overflow: visible !important;
    background: #ffffff !important; color: #111111 !important;
    -webkit-print-color-adjust: exact; print-color-adjust: exact;
    font-size: 11pt; line-height: 1.55;
  }}
  /* Continuous flow: slides become document sections, NOT one-per-page screenshots */
  .slide {{
    display: block !important; min-height: 0 !important; height: auto !important;
    padding: 0 !important; margin: 0 0 6pt !important; overflow: visible !important;
    page-break-after: auto !important; break-after: auto !important;
    page-break-before: auto !important; break-before: auto !important;
  }}
  .slide > div[style] {{ display: block !important; }}   /* flatten the centered hero wrapper */
  /* Brand logo ONCE at the top; drop the repeated logos + redundant per-slide labels */
  .slide:not([data-slide="1"]) .brand-bar {{ display: none !important; }}
  .slide[data-slide="1"] .brand-bar {{ border: none !important; margin-bottom: 10pt !important; }}
  .section-label {{ display: none !important; }}
  .slide[data-slide="review"] {{ display: none !important; }}   /* drop the interactive Review slide */
  /* Document title (hero) — solid ink, left-aligned, normal document size */
  .hero-title {{
    background: none !important; -webkit-text-fill-color: var(--primary) !important;
    color: var(--primary) !important; font-size: 22pt !important; line-height: 1.15 !important;
    text-align: left !important; margin: 0 0 6pt !important;
  }}
  .hero-subtitle {{ color: #1a1a1a !important; font-size: 12pt !important; max-width: none !important; }}
  /* Section headings — solid ink, kept with the text that follows */
  h1, h2 {{
    background: none !important; -webkit-background-clip: border-box !important;
    background-clip: border-box !important;
    -webkit-text-fill-color: var(--primary) !important; color: var(--primary) !important;
    font-size: 15pt !important; margin: 14pt 0 6pt !important;
    page-break-after: avoid !important; break-after: avoid !important;
  }}
  h3 {{ color: #222222 !important; font-size: 12.5pt !important; margin: 10pt 0 4pt !important;
       page-break-after: avoid !important; break-after: avoid !important; }}
  p, li, td, .hero-subtitle, .timeline-text {{ color: #1a1a1a !important; orphans: 3; widows: 3; }}
  p, li, blockquote, tr, .card, .kpi-card, .table-container {{ page-break-inside: avoid; break-inside: avoid; }}
  strong {{ color: #000000 !important; }}
  em {{ color: #0b6f66 !important; }}            /* darker teal — the cyan accent is too light on white */
  a {{ color: var(--primary) !important; }}
  blockquote {{ background: #f4f4f4 !important; border-left: 3px solid var(--primary) !important; }}
  blockquote p {{ color: #111111 !important; }}
  .card, .kpi-card, .table-container {{ background: #ffffff !important; border: 1px solid #cccccc !important; box-shadow: none !important; }}
  table, th, td {{ border-color: #bbbbbb !important; }}
  th {{ background: #eeeeee !important; color: #111111 !important; }}
  /* Hide all interactive chrome */
  .nav-bar, .nav-arrow, .comment-badge, #jumpOverlay, .comment-popover, #feedbackPanel,
  .scroll-nav-pill, .print-btn, .nav-dots, .mode-toggle {{ display: none !important; }}
  .commentable::after {{ display: none !important; content: none !important; }}
}}

/* Desktop padding */
@media (min-width: 768px) {{
  .slide {{ padding: 50px 60px 80px; }}
}}
@media (min-width: 1200px) {{
  .slide {{ padding: 60px 100px 80px; }}
}}

/* Subtle grid bg */
.slide::before {{
  content: '';
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px);
  background-size: 60px 60px;
  pointer-events: none;
}}

/* ── Brand Bar ── */
.brand-bar {{
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 24px; position: relative; z-index: 1;
}}
.brand-logo {{
  display: flex; align-items: center; gap: 10px;
}}
.logo-mark {{
  width: 32px; height: 32px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-weight: 800; font-size: 16px; color: #fff;
}}
.logo-mark.logo-letter {{
  background: var(--gradient-brand);
  border-radius: 8px;
}}
.logo-mark.logo-wide {{
  width: 200px !important; height: 117px !important;
}}
.logo-mark.logo-wide svg {{
  width: 200px; height: 117px;
}}
.logo-mark svg {{
  width: 32px; height: 32px;
}}
.logo-text {{
  font-size: 20px; font-weight: 800; letter-spacing: 0.06em;
  color: var(--text-primary);
}}
.section-label {{
  font-size: 11px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.1em; color: var(--primary);
  font-family: 'JetBrains Mono', monospace;
  display: none;
}}
@media (min-width: 768px) {{ .section-label {{ display: block; }} }}

/* ── Typography ── */
h1 {{
  font-size: 1.8rem; font-weight: 800; line-height: 1.15;
  letter-spacing: -0.02em; margin-bottom: 16px;
  position: relative; z-index: 1;
}}
@media (min-width: 768px) {{ h1 {{ font-size: 2.5rem; }} }}
@media (min-width: 1200px) {{ h1 {{ font-size: 52px; }} }}

h2 {{
  font-size: 1.4rem; font-weight: 700; line-height: 1.2;
  letter-spacing: -0.01em; margin-bottom: 12px;
  position: relative; z-index: 1;
  background: linear-gradient(135deg, var(--text-primary), var(--accent));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}}
@media (min-width: 768px) {{ h2 {{ font-size: 1.8rem; }} }}
@media (min-width: 1200px) {{ h2 {{ font-size: 36px; }} }}

h3 {{
  font-size: 1.1rem; font-weight: 600; color: var(--text-primary);
  margin: 1.5rem 0 0.75rem; position: relative; z-index: 1;
}}
@media (min-width: 768px) {{ h3 {{ font-size: 1.3rem; }} }}

h4 {{
  font-size: 1rem; font-weight: 600; color: var(--text-secondary);
  margin: 0.5rem 0 0.4rem; position: relative; z-index: 1;
}}

p {{
  font-size: 0.95rem; line-height: 1.7; color: var(--text-secondary);
  margin-bottom: 0.9rem; position: relative; z-index: 1;
}}
@media (min-width: 768px) {{ p {{ font-size: 1.05rem; }} }}

strong {{ color: var(--text-primary); font-weight: 600; }}
em {{ color: var(--accent); font-style: italic; }}
.deck-disclosure em {{ color: #e5e7eb; font-style: italic; }}
.deck-disclosure a, .deck-disclosure a.md-link {{ color: #e5e7eb; text-decoration: underline; text-underline-offset: 2px; }}

/* ── Cards ── */
.card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 16px;
  position: relative; z-index: 1;
}}
.bq-head {{ font-weight: 800; color: var(--accent); font-style: normal; font-size: 1.05em; margin-bottom: 8px; }}
.bq-gap {{ height: 12px; }}

/* ── Blockquotes (agent voices) ── */
blockquote {{
  background: var(--bg-card);
  border-left: 3px solid var(--primary);
  border-radius: 0 8px 8px 0;
  padding: 16px 18px;
  margin: 1rem 0;
  font-style: italic;
  position: relative; z-index: 1;
}}
blockquote p {{ color: var(--accent); margin-bottom: 0; }}

/* ── Tables ── */
.table-container {{
  overflow-x: auto;
  margin: 1rem 0;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
  position: relative; z-index: 1;
}}
.table-container::-webkit-scrollbar {{ display: none; }}

table {{
  border-collapse: collapse;
  width: 100%;
  min-width: 280px;
  font-size: 0.82rem;
}}
@media (min-width: 768px) {{ table {{ font-size: 0.88rem; }} }}

th, td {{
  border: 1px solid var(--border);
  padding: 8px 10px;
  text-align: left;
  vertical-align: top;
}}
@media (min-width: 768px) {{ th, td {{ padding: 10px 14px; }} }}

th {{
  background: var(--bg-elevated);
  color: var(--primary);
  font-weight: 600;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  font-family: 'JetBrains Mono', monospace;
}}
tr:nth-child(even) {{ background: rgba(255,255,255,0.02); }}

/* ── Code ── */
pre {{
  background: rgba(0,0,0,0.3);
  padding: 14px 16px;
  border-radius: 8px;
  overflow-x: auto;
  font-size: 0.82rem;
  margin: 1rem 0;
  -webkit-overflow-scrolling: touch;
  border: 1px solid var(--border);
  position: relative; z-index: 1;
}}
code {{
  background: rgba(255,255,255,0.06);
  padding: 0.15em 0.4em;
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.88em;
}}
pre code {{ padding: 0; background: none; }}

/* ── Lists ── */
ul, ol {{
  margin: 0.75rem 0 0.75rem 1.25rem;
  position: relative; z-index: 1;
}}
li {{ margin-bottom: 0.5rem; line-height: 1.6; color: var(--text-secondary); }}
li > ul, li > ol {{ margin-top: 0.3rem; }}

/* ── Links ── */
a {{ color: var(--primary); text-decoration: none; }}
a.md-link {{ color: var(--accent); text-decoration: underline; text-underline-offset: 2px; }}
a.md-link:hover {{ opacity: 0.85; }}

/* ── Horizontal rules ── */
hr {{ border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; position: relative; z-index: 1; }}

/* ── KPI Grid ── */
.kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 14px; margin: 20px 0; position: relative; z-index: 1; }}
.kpi-card {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px; padding: 18px; text-align: center; }}
.kpi-value {{ font-size: 2rem; font-weight: 800; background: var(--gradient-brand); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.kpi-label {{ font-size: 0.8rem; color: var(--text-muted); margin-top: 4px; }}

/* ── Chapter Number ── */
.chapter-num {{ font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: var(--primary); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 8px; position: relative; z-index: 1; }}

/* ── Hero Slide ── */
.hero-title {{ font-size: 2.2rem; font-weight: 800; line-height: 1.1; background: var(--gradient-brand); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 16px; position: relative; z-index: 1; }}
@media (min-width: 768px) {{ .hero-title {{ font-size: 3.2rem; }} }}
@media (min-width: 1200px) {{ .hero-title {{ font-size: 4rem; }} }}
.hero-subtitle {{ font-size: 1.1rem; color: var(--text-secondary); line-height: 1.6; max-width: 700px; position: relative; z-index: 1; }}
@media (min-width: 768px) {{ .hero-subtitle {{ font-size: 1.3rem; }} }}

/* ── Timeline ── */
.timeline {{ position: relative; z-index: 1; margin: 20px 0; padding-left: 24px; border-left: 2px solid var(--border); }}
.timeline-item {{ margin-bottom: 20px; position: relative; }}
.timeline-item::before {{ content: ''; position: absolute; left: -29px; top: 6px; width: 10px; height: 10px; border-radius: 50%; background: var(--primary); }}
.timeline-label {{ font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: var(--primary); letter-spacing: 0.05em; margin-bottom: 4px; }}
.timeline-text {{ font-size: 0.9rem; color: var(--text-secondary); }}
.timeline-text strong {{ color: var(--text-primary); }}

/* ── Stat Highlight ── */
.stat-highlight {{ font-size: 4rem; font-weight: 800; background: var(--gradient-brand); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1; margin: 16px 0; position: relative; z-index: 1; }}
@media (min-width: 768px) {{ .stat-highlight {{ font-size: 5rem; }} }}

/* ── SVG diagrams ── */
svg:not(.nav-bar svg) {{
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1.5rem auto;
  border-radius: 12px;
}}

/* ── Navigation ── */
.nav-bar {{
  position: fixed; bottom: 0; left: 0; right: 0;
  background: rgba(13,17,23,0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-top: 1px solid var(--border);
  padding: 10px 16px;
  display: grid; grid-template-columns: 1fr auto 1fr;
  align-items: center;
  z-index: 100;
}}
@media (min-width: 768px) {{ .nav-bar {{ padding: 10px 24px; }} }}

.nav-sections {{
  display: flex; gap: 4px; justify-self: start;
  flex-wrap: wrap;
}}
.nav-section-dot {{
  width: 8px; height: 8px;
  border-radius: 50%;
  background: var(--text-muted);
  opacity: 0.3;
  cursor: pointer;
  transition: all 0.2s;
  -webkit-tap-highlight-color: transparent;
}}
.nav-section-dot.active {{
  background: var(--primary);
  opacity: 1;
  width: 24px;
  border-radius: 4px;
}}

.nav-center {{
  display: flex; align-items: center; gap: 12px;
}}
@media (min-width: 768px) {{ .nav-center {{ gap: 16px; }} }}

.nav-btn {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  color: var(--text-primary);
  width: 36px; height: 36px;
  border-radius: 8px;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  font-size: 16px;
  transition: all 0.2s;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}}
.nav-btn:hover {{ border-color: var(--primary); background: var(--bg-elevated); }}
.nav-btn:disabled {{ opacity: 0.3; cursor: default; }}

.nav-counter {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px; color: var(--text-muted);
  min-width: 50px; text-align: center;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}}

.nav-slide-dots {{
  display: none; gap: 3px; justify-self: end;
  flex-wrap: wrap;
}}
@media (min-width: 768px) {{ .nav-slide-dots {{ display: flex; }} }}

.nav-slide-dot {{
  width: 6px; height: 6px;
  border-radius: 50%;
  background: var(--text-muted);
  opacity: 0.2;
  cursor: pointer;
  transition: all 0.2s;
}}
.nav-slide-dot.active {{
  background: var(--accent);
  opacity: 1;
}}
.nav-slide-dot.section-start {{
  opacity: 0.5;
}}

/* ── Slide Jump Overlay ── */
.slide-jump-overlay {{
  display: none; position: fixed; inset: 0;
  background: rgba(0,0,0,0.7);
  backdrop-filter: blur(4px);
  z-index: 200; align-items: center; justify-content: center;
}}
.slide-jump-box {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px 32px;
  text-align: center;
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}}
.slide-jump-box input {{
  width: 80px; padding: 8px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--bg-dark);
  color: var(--text-primary);
  font-size: 18px;
  text-align: center;
  font-family: 'JetBrains Mono', monospace;
}}

/* ── Commentable Engine ── */
.nav-slide-dot.has-comment {{ background: var(--primary); opacity: 0.8; }}
.commentable {{ position: relative; padding: 6px 40px 6px 12px; margin: 2px 0; border-radius: 8px; border: 1px solid transparent; transition: all 0.2s; cursor: pointer; }}
.commentable::after {{ content: '+'; position: absolute; right: 8px; top: 50%; transform: translateY(-50%); width: 24px; height: 24px; border-radius: 50%; background: var(--bg-elevated); border: 1px solid var(--border); color: var(--text-muted); font-size: 16px; font-weight: 300; display: flex; align-items: center; justify-content: center; opacity: 0; transition: all 0.2s; line-height: 1; z-index: 5; }}
.commentable:hover {{ background: color-mix(in srgb, var(--primary) 6%, transparent); border-color: color-mix(in srgb, var(--primary) 20%, transparent); }}
.commentable:hover::after {{ opacity: 1; color: var(--primary); border-color: color-mix(in srgb, var(--primary) 30%, transparent); }}
.commentable.has-comment {{ border-left: 2px solid var(--primary); background: color-mix(in srgb, var(--primary) 4%, transparent); }}
.commentable.has-comment::after {{ content: ''; background: var(--primary); border-color: var(--primary); width: 8px; height: 8px; opacity: 1; right: 12px; }}
.commentable.active-comment {{ background: color-mix(in srgb, var(--primary) 10%, transparent); border-color: var(--primary); }}

/* ── Comment Popover ── */
.comment-popover {{ position: fixed; right: 60px; top: 50%; transform: translateY(-50%); width: 360px; background: var(--bg-elevated); border: 1px solid var(--border); border-radius: 12px; padding: 16px; box-shadow: 0 16px 48px rgba(0,0,0,0.5); z-index: 150; display: none; animation: popoverIn 0.15s ease; }}
@keyframes popoverIn {{ from {{ opacity: 0; transform: translateY(-50%) translateX(8px); }} to {{ opacity: 1; transform: translateY(-50%) translateX(0); }} }}
.comment-popover.visible {{ display: block; }}
.popover-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }}
.popover-header .section-ref {{ font-size: 12px; color: var(--text-muted); font-weight: 500; }}
.popover-close {{ background: none; border: none; color: var(--text-muted); cursor: pointer; font-size: 18px; padding: 2px; line-height: 1; transition: all 0.2s; }}
.popover-close:hover {{ color: var(--text-primary); }}
.comment-textarea {{ width: 100%; min-height: 80px; background: var(--bg-dark); border: 1px solid var(--border); border-radius: 8px; color: var(--text-primary); font-size: 14px; font-family: inherit; padding: 10px 12px; resize: vertical; outline: none; transition: all 0.2s; line-height: 1.5; }}
.comment-textarea:focus {{ border-color: var(--primary); box-shadow: 0 0 0 3px color-mix(in srgb, var(--primary) 25%, transparent); }}
.comment-textarea::placeholder {{ color: var(--text-muted); }}
.popover-actions {{ display: flex; justify-content: space-between; align-items: center; margin-top: 10px; }}
.cbtn {{ padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 500; cursor: pointer; transition: all 0.2s; border: 1px solid transparent; font-family: inherit; }}
.cbtn-primary {{ background: var(--primary); color: #000; border-color: var(--primary); }}
.cbtn-primary:hover {{ filter: brightness(1.1); }}
.cbtn-ghost {{ background: transparent; color: var(--text-muted); border-color: var(--border); }}
.cbtn-ghost:hover {{ background: var(--bg-card); color: var(--text-primary); }}
.cbtn-danger {{ background: transparent; color: #EF4444; border: none; font-size: 12px; padding: 4px 8px; cursor: pointer; }}
.cbtn-danger:hover {{ background: rgba(239,68,68,0.1); }}
.comment-badge {{ font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--primary); background: color-mix(in srgb, var(--primary) 10%, transparent); border: 1px solid color-mix(in srgb, var(--primary) 30%, transparent); border-radius: 12px; padding: 2px 10px; cursor: pointer; transition: all 0.2s; }}
.comment-badge:empty {{ display: none; }}
.comment-badge:hover {{ background: color-mix(in srgb, var(--primary) 20%, transparent); }}

/* ── Toast ── */
.toast {{ position: fixed; bottom: 70px; left: 50%; transform: translateX(-50%) translateY(20px); background: var(--bg-elevated); border: 1px solid var(--border); color: var(--text-primary); padding: 8px 20px; border-radius: 8px; font-size: 13px; opacity: 0; transition: all 0.3s; z-index: 200; pointer-events: none; }}
.toast.visible {{ opacity: 1; transform: translateX(-50%) translateY(0); }}

/* ── Review Slide ── */
.review-slide-content {{ position: relative; z-index: 1; flex: 1; overflow-y: auto; }}
.feedback-list {{ display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px; }}
.feedback-item {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: 10px; padding: 14px 18px; }}
.feedback-item-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }}
.feedback-item-anchor {{ font-size: 13px; font-weight: 600; color: var(--primary); }}
.feedback-item-slide {{ font-size: 11px; color: var(--text-muted); font-family: 'JetBrains Mono', monospace; }}
.feedback-item-text {{ font-size: 14px; color: var(--text-secondary); line-height: 1.5; }}
.feedback-item-actions {{ display: flex; gap: 8px; margin-top: 8px; }}
.general-textarea {{ width: 100%; min-height: 60px; background: var(--bg-card); border: 1px solid var(--border); border-radius: 8px; color: var(--text-primary); font-size: 14px; font-family: inherit; padding: 10px 12px; resize: vertical; outline: none; }}
.general-textarea:focus {{ border-color: var(--primary); }}
.submit-area {{ display: flex; gap: 12px; align-items: center; margin-top: 16px; }}
.btn-submit {{ background: var(--primary); color: #000; border: none; padding: 10px 20px; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; font-family: inherit; }}
.btn-submit:hover {{ filter: brightness(1.1); }}
.btn-download {{ background: var(--bg-card); color: var(--text-primary); border: 1px solid var(--border); padding: 10px 20px; border-radius: 8px; font-size: 14px; cursor: pointer; font-family: inherit; }}
.btn-download:hover {{ border-color: var(--primary); }}
.format-selector {{ display: flex; gap: 4px; }}
.format-option {{ padding: 4px 12px; border-radius: 6px; font-size: 12px; font-weight: 500; background: var(--bg-card); border: 1px solid var(--border); color: var(--text-muted); cursor: pointer; font-family: inherit; }}
.format-option.active {{ background: color-mix(in srgb, var(--primary) 15%, transparent); color: var(--primary); border-color: color-mix(in srgb, var(--primary) 30%, transparent); }}
.empty-state {{ text-align: center; padding: 40px; color: var(--text-muted); font-size: 14px; }}
@media (max-width: 767px) {{
  .comment-popover {{ right: 16px !important; left: 16px !important; width: auto !important; top: auto !important; bottom: 60px !important; transform: none !important; }}
  .commentable::after {{ right: 6px; width: 20px; height: 20px; font-size: 12px; opacity: 0.35; }}
  .commentable.has-comment::after {{ right: 8px; }}
  .commentable {{ margin: 2px 0; padding: 6px 36px 6px 12px; }}
}}
@media (hover: none) {{
  .commentable::after {{ opacity: 0.3; }}
  .commentable:active::after {{ opacity: 1; color: var(--primary); border-color: color-mix(in srgb, var(--primary) 30%, transparent); }}
}}
</style>
</head>
<body>

{slides_html}

<!-- Review Slide -->
<div class="slide" data-slide="review">
<div class="brand-bar"><div class="brand-logo"><div class="{logo_class}">{logo_letter}</div><span class="logo-text">{logo_text}</span></div><span class="section-label">Review</span></div>
<div class="review-slide-content">
  <h2>Your Feedback</h2>
  <p style="color:var(--text-secondary);margin-bottom:20px;">All comments collected during your review. Edit, remove, or add general notes.</p>
  <div class="feedback-list" id="feedbackList"><div class="empty-state" id="emptyState"><div style="font-size:48px;margin-bottom:12px;">&#128172;</div><p>No comments yet. Navigate to any slide and click on highlighted sections to add feedback.</p></div></div>
  <div style="margin-bottom:16px;"><h3 style="margin-bottom:8px;">General Feedback</h3><textarea class="general-textarea" id="generalFeedback" placeholder="Overall thoughts, concerns, or direction..."></textarea></div>
  <div style="display:flex;align-items:center;gap:16px;margin-bottom:12px;">
    <span style="font-size:13px;color:var(--text-muted);">Export as:</span>
    <div class="format-selector"><button class="format-option active" data-format="markdown" onclick="window.setFormat('markdown')">Markdown</button><button class="format-option" data-format="json" onclick="window.setFormat('json')">JSON</button></div>
  </div>
  <div class="submit-area"><button class="btn-submit" onclick="window.copyFeedback()">&#128203; Copy to Clipboard</button><button class="btn-download" onclick="window.downloadFeedback()">&#128190; Download</button></div>
  <div style="margin-top:12px;"><button class="cbtn cbtn-ghost" onclick="window.togglePreview()" id="previewToggle">Show preview</button><pre id="outputPreview" style="display:none;margin-top:10px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:14px;font-size:12px;color:var(--text-muted);overflow-x:auto;white-space:pre-wrap;max-height:200px;overflow-y:auto;"></pre></div>
</div>
</div>

<div class="nav-bar">
<div></div>
<div class="nav-center">
<button class="nav-btn" id="prevBtn" aria-label="Previous">&larr;</button>
<span class="nav-counter" id="navCounter" onclick="window.promptSlide()">{num_slides_display}</span>
<span class="comment-badge" id="commentBadge" onclick="window.goToReview()"></span>
<button class="nav-btn" id="nextBtn" aria-label="Next">&rarr;</button>
</div>
<div style="justify-self:end;"><button class="nav-btn print-btn" onclick="window.print()" title="Print / Save as PDF" aria-label="Save as PDF" style="width:auto;padding:0 12px;font-size:13px;white-space:nowrap;">&#11015; PDF</button></div>
</div>

<div id="jumpOverlay" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,0.7);z-index:200;align-items:center;justify-content:center;">
<div class="slide-jump-box">
<p style="margin-bottom:12px;color:var(--text-secondary);">Jump to slide:</p>
<input id="jumpInput" type="number" min="1" max="{num_sections}" />
<p style="margin-top:8px;font-size:12px;color:var(--text-muted);">Enter &crarr; to go &bull; Esc to close</p>
</div>
</div>

<script>
(function() {{
  'use strict';

  var slides = document.querySelectorAll('.slide');
  var totalSlides = slides.length;
  var currentSlide = 0;

  var sections = {sections_json};

  var prevBtn = document.getElementById('prevBtn');
  var nextBtn = document.getElementById('nextBtn');
  var counter = document.getElementById('navCounter');
  var jumpOverlay = document.getElementById('jumpOverlay');
  var jumpInput = document.getElementById('jumpInput');

  function getCurrentSection(slideIndex) {{
    for (var i = 0; i < sections.length; i++) {{
      if (slideIndex >= sections[i].start && slideIndex <= sections[i].end) return i;
    }}
    return 0;
  }}

  window.showSlide = function(n) {{
    if (n < 0) n = 0;
    if (n >= totalSlides) n = totalSlides - 1;
    slides[currentSlide].classList.remove('active');
    slides[n].classList.add('active');
    currentSlide = n;
    counter.textContent = (n + 1) + ' / ' + totalSlides;
    prevBtn.disabled = n === 0;
    nextBtn.disabled = n === totalSlides - 1;
    // Scroll slide to top when navigating
    slides[n].scrollTop = 0;

  }};

  window.promptSlide = function() {{
    jumpOverlay.style.display = 'flex';
    jumpInput.value = '';
    jumpInput.focus();
  }};

  window.closeJump = function() {{
    jumpOverlay.style.display = 'none';
  }};

  jumpInput.addEventListener('keydown', function(e) {{
    if (e.key === 'Enter') {{
      var val = parseInt(jumpInput.value);
      if (val >= 1 && val <= totalSlides) window.showSlide(val - 1);
      window.closeJump();
    }} else if (e.key === 'Escape') {{
      window.closeJump();
    }}
  }});

  jumpOverlay.addEventListener('click', function(e) {{
    if (e.target === jumpOverlay) window.closeJump();
  }});

  prevBtn.addEventListener('click', function() {{ window.showSlide(currentSlide - 1); }});
  nextBtn.addEventListener('click', function() {{ window.showSlide(currentSlide + 1); }});

  // Footnote links: clicking a ¹ ref (or the ↩ back-link) navigates to the slide
  // holding the target (References slide for #fn-N) and scrolls it into view.
  document.addEventListener('click', function(e) {{
    var a = e.target.closest && e.target.closest('a[href^="#fn-"], a[href^="#fnref-"]');
    if (!a) return;
    e.preventDefault();
    var el = document.getElementById(a.getAttribute('href').slice(1));
    if (!el) return;
    var sl = el.closest ? el.closest('.slide') : null;
    if (sl) {{
      var idx = Array.prototype.indexOf.call(slides, sl);
      if (idx >= 0) window.showSlide(idx);
    }}
    setTimeout(function() {{ el.scrollIntoView({{behavior: 'smooth', block: 'center'}}); }}, 60);
  }});

  document.addEventListener('keydown', function(e) {{
    if (jumpOverlay.style.display === 'flex') return;
    if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {{
      e.preventDefault(); window.showSlide(currentSlide - 1);
    }} else if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {{
      e.preventDefault(); window.showSlide(currentSlide + 1);
    }} else if (e.key === 'Home') {{
      e.preventDefault(); window.showSlide(0);
    }} else if (e.key === 'End') {{
      e.preventDefault(); window.showSlide(totalSlides - 1);
    }} else if (e.key === 'Escape') {{
      window.closeJump();
    }}
  }});

  window.showSlide(0);
}})();
</script>

<!-- Comment Popover -->
<div class="comment-popover" id="commentPopover">
  <div class="popover-header"><span class="section-ref" id="popoverRef">Section</span><button class="popover-close" onclick="window.closePopover()">&times;</button></div>
  <textarea class="comment-textarea" id="commentInput" placeholder="What's your feedback on this section?"></textarea>
  <div class="popover-actions">
    <button class="cbtn-danger" id="deleteCommentBtn" onclick="window.deleteComment()" style="display:none;">Remove</button>
    <div style="display:flex;gap:8px;margin-left:auto;"><button class="cbtn cbtn-ghost" onclick="window.closePopover()">Cancel</button><button class="cbtn cbtn-primary" onclick="window.saveComment()">Save</button></div>
  </div>
</div>
<div class="toast" id="toast"></div>

<script>
(function(){{
  'use strict';
  var comments=new Map(),activeSection=null,exportFormat='markdown';
  var slides=document.querySelectorAll('.slide'),totalSlides=slides.length;
  var storageKey='feedback_'+document.title.toLowerCase().replace(/[^a-z0-9]+/g,'_');

  // Commentable Engine - bind click handlers
  document.querySelectorAll('.commentable').forEach(function(el){{el.addEventListener('click',function(e){{if(e.target.closest&&e.target.closest('a')){{return;}}e.stopPropagation();openPopover(el);}});}});

  function openPopover(el){{
    var section=el.dataset.section,label=el.dataset.label||section;
    var popover=document.getElementById('commentPopover'),input=document.getElementById('commentInput'),del=document.getElementById('deleteCommentBtn'),ref=document.getElementById('popoverRef');
    if(activeSection){{var p=document.querySelector('.commentable[data-section="'+activeSection+'"]');if(p)p.classList.remove('active-comment');}}
    activeSection=section;el.classList.add('active-comment');ref.textContent=label;
    var ex=comments.get(section);input.value=ex?ex.text:'';del.style.display=ex?'inline-block':'none';
    popover.classList.add('visible');setTimeout(function(){{input.focus();}},100);
    // Trap keyboard in popover
    input.onkeydown=function(e){{e.stopPropagation();if(e.key==='Escape')window.closePopover();}};
  }}

  window.closePopover=function(){{var p=document.getElementById('commentPopover');p.classList.remove('visible');if(activeSection){{var el=document.querySelector('.commentable[data-section="'+activeSection+'"]');if(el)el.classList.remove('active-comment');activeSection=null;}}}};

  window.saveComment=function(){{
    if(!activeSection)return;var text=document.getElementById('commentInput').value.trim();if(!text){{window.deleteComment();return;}}
    var el=document.querySelector('.commentable[data-section="'+activeSection+'"]'),sl=el.closest('.slide');
    comments.set(activeSection,{{text:text,label:el.dataset.label||activeSection,slideIndex:Array.from(slides).indexOf(sl),timestamp:new Date().toISOString()}});
    el.classList.add('has-comment');window.closePopover();updateBadge();persistState();updateNavDots();showToast('Comment saved');
  }};

  window.deleteComment=function(){{if(!activeSection)return;var key=activeSection;var el=document.querySelector('.commentable[data-section="'+key+'"]');comments.delete(key);if(el)el.classList.remove('has-comment');window.closePopover();updateBadge();persistState();updateNavDots();showToast('Comment removed');}};

  window.deleteCommentBySection=function(s){{var el=document.querySelector('.commentable[data-section="'+s+'"]');comments.delete(s);if(el)el.classList.remove('has-comment');updateBadge();updateReviewSlide();persistState();updateNavDots();showToast('Comment removed');}};

  window.editCommentFromReview=function(s){{var el=document.querySelector('.commentable[data-section="'+s+'"]');if(!el)return;var sl=el.closest('.slide'),idx=Array.from(slides).indexOf(sl);window.showSlide(idx);setTimeout(function(){{openPopover(el);}},300);}};

  window.goToReview=function(){{window.showSlide(totalSlides-1);}};

  function updateBadge(){{var b=document.getElementById('commentBadge');if(!b)return;var c=comments.size;b.textContent=c>0?c+' comment'+(c>1?'s':''):'';}};

  function updateNavDots(){{
    var dotsEl=document.getElementById('navDots');
    if(!dotsEl)return;
    dotsEl.querySelectorAll('.nav-slide-dot').forEach(function(d,i){{
      d.classList.remove('has-comment');
      var sl=slides[i],cs=sl.querySelectorAll('.commentable'),hc=false;
      cs.forEach(function(c){{if(comments.has(c.dataset.section))hc=true;}});
      if(hc)d.classList.add('has-comment');
    }});
  }}

  function updateReviewSlide(){{
    var list=document.getElementById('feedbackList'),empty=document.getElementById('emptyState');
    if(comments.size===0){{list.innerHTML='';list.appendChild(empty);empty.style.display='block';return;}}
    if(empty)empty.style.display='none';list.innerHTML='';
    var sorted=Array.from(comments.entries()).sort(function(a,b){{return(a[1].slideIndex||0)-(b[1].slideIndex||0);}});
    sorted.forEach(function(entry){{var s=entry[0],d=entry[1];var item=document.createElement('div');item.className='feedback-item';
      item.innerHTML='<div class="feedback-item-header"><span class="feedback-item-anchor">'+escapeHtml(d.label)+'</span><span class="feedback-item-slide">Slide '+((d.slideIndex||0)+1)+'</span></div><div class="feedback-item-text">'+escapeHtml(d.text)+'</div><div class="feedback-item-actions"><button class="cbtn cbtn-ghost" onclick="window.editCommentFromReview(\\\''+s+'\\\')" style="font-size:12px;padding:3px 10px;">Edit</button><button class="cbtn-danger" onclick="window.deleteCommentBySection(\\\''+s+'\\\')">Remove</button></div>';
      list.appendChild(item);}});
    if(document.getElementById('outputPreview').style.display!=='none')updatePreview();
  }}

  // Hook into showSlide to update review when navigating to it
  var origShowSlide=window.showSlide;
  window.showSlide=function(n){{
    origShowSlide(n);
    if(slides[n]&&slides[n].dataset.slide==='review')updateReviewSlide();
    updateNavDots();
  }};

  window.setFormat=function(f){{exportFormat=f;document.querySelectorAll('.format-option').forEach(function(el){{el.classList.toggle('active',el.dataset.format===f);}});if(document.getElementById('outputPreview').style.display!=='none')updatePreview();}};

  function generateMarkdown(){{
    var g=document.getElementById('generalFeedback').value.trim();
    var sorted=Array.from(comments.entries()).sort(function(a,b){{return(a[1].slideIndex||0)-(b[1].slideIndex||0);}});
    var md='## Feedback on: '+document.title+'\\nDate: '+new Date().toISOString().split('T')[0]+'\\n\\n';
    if(sorted.length>0){{md+='### Inline Comments\\n\\n';sorted.forEach(function(e,i){{md+=(i+1)+'. **Slide '+((e[1].slideIndex||0)+1)+' - "'+e[1].label+'"**: "'+e[1].text+'"\\n';}});md+='\\n';}}
    if(g)md+='### General Feedback\\n\\n"'+g+'"\\n';if(sorted.length===0&&!g)md+='_No feedback provided._\\n';return md;
  }}

  function generateJSON(){{
    var g=document.getElementById('generalFeedback').value.trim();
    var sorted=Array.from(comments.entries()).sort(function(a,b){{return(a[1].slideIndex||0)-(b[1].slideIndex||0);}});
    return JSON.stringify({{document:document.title,date:new Date().toISOString().split('T')[0],comments:sorted.map(function(e){{return{{slide:(e[1].slideIndex||0)+1,section:e[0],label:e[1].label,feedback:e[1].text,timestamp:e[1].timestamp}};}}),generalFeedback:g||null,totalComments:sorted.length}},null,2);
  }}

  function getOutput(){{return exportFormat==='json'?generateJSON():generateMarkdown();}}

  window.copyFeedback=function(){{navigator.clipboard.writeText(getOutput()).then(function(){{showToast('Copied to clipboard');}});}};
  window.downloadFeedback=function(){{var ext=exportFormat==='json'?'json':'md';var blob=new Blob([getOutput()],{{type:exportFormat==='json'?'application/json':'text/markdown'}});var url=URL.createObjectURL(blob);var a=document.createElement('a');a.href=url;a.download='feedback-'+document.title.toLowerCase().replace(/[^a-z0-9]+/g,'-')+'.'+ext;a.click();URL.revokeObjectURL(url);showToast('Downloaded');}};
  window.togglePreview=function(){{var p=document.getElementById('outputPreview'),b=document.getElementById('previewToggle');if(p.style.display==='none'){{p.style.display='block';b.textContent='Hide preview';updatePreview();}}else{{p.style.display='none';b.textContent='Show preview';}}}};
  function updatePreview(){{document.getElementById('outputPreview').textContent=getOutput();}}

  function persistState(){{try{{var gf=document.getElementById('generalFeedback').value;if(comments.size===0&&!gf){{localStorage.removeItem(storageKey);return;}}localStorage.setItem(storageKey,JSON.stringify({{comments:Object.fromEntries(comments),generalFeedback:gf}}));}}catch(e){{}}}}
  function loadState(){{try{{var saved=localStorage.getItem(storageKey);if(saved){{var data=JSON.parse(saved);if(data.comments){{var keys=Object.keys(data.comments);if(keys.length===0){{localStorage.removeItem(storageKey);return;}}keys.forEach(function(k){{comments.set(k,data.comments[k]);}});comments.forEach(function(v,s){{var el=document.querySelector('.commentable[data-section="'+s+'"]');if(el)el.classList.add('has-comment');}});updateBadge();}}if(data.generalFeedback)document.getElementById('generalFeedback').value=data.generalFeedback;}}}}catch(e){{}}}}

  document.getElementById('generalFeedback').addEventListener('input',persistState);
  function escapeHtml(t){{var d=document.createElement('div');d.textContent=t;return d.innerHTML;}}
  function showToast(m){{var t=document.getElementById('toast');t.textContent=m;t.classList.add('visible');setTimeout(function(){{t.classList.remove('visible');}},2000);}}
  document.addEventListener('click',function(e){{var p=document.getElementById('commentPopover');if(p.classList.contains('visible')&&!p.contains(e.target)&&!e.target.closest('.commentable'))window.closePopover();}});
  loadState();updateNavDots();
}})();
</script>

</body>
</html>'''


# ── Commentable Presentation Template (prototype-style) ──────────────────────

COMMENTABLE_HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  :root {{
    --bg: #0a0a0a;
    --surface: #141414;
    --surface-2: #1c1c1c;
    --border: #2a2a2a;
    --border-hover: #3a3a3a;
    --text: #e8e8e8;
    --text-muted: #888;
    --text-dim: #555;
    --accent: #14b8a6;
    --accent-dim: rgba(20, 184, 166, 0.08);
    --accent-border: rgba(20, 184, 166, 0.25);
    --accent-glow: rgba(20, 184, 166, 0.15);
    --warning: #f59e0b;
    --danger: #ef4444;
    --radius: 10px;
    --radius-sm: 6px;
    --transition: 0.2s ease;
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    overflow: hidden;
    height: 100vh;
    width: 100vw;
  }}

  /* ── Scroll mode overrides ── */
  body.scroll-mode {{
    overflow: auto;
    height: auto;
  }}

  body.scroll-mode .slide-viewport {{ display: none; }}
  body.scroll-mode .bottombar {{ display: none; }}
  body.scroll-mode .nav-arrow {{ display: none; }}
  body.scroll-mode .keyboard-hint {{ display: none; }}
  body.scroll-mode .topbar-nav {{ display: none; }}
  body.scroll-mode .scroll-content {{ display: block; }}

  /* ── Top bar ── */
  .topbar {{
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 48px;
    background: rgba(10, 10, 10, 0.92);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px;
    z-index: 100;
    font-family: inherit;
  }}

  .topbar-left {{
    display: flex;
    align-items: center;
    gap: 16px;
  }}

  .topbar-title {{
    font-size: 13px;
    font-weight: 600;
    color: var(--text);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 300px;
  }}

  .topbar-right {{
    display: flex;
    align-items: center;
    gap: 16px;
  }}

  /* ── Mode picker ── */
  .mode-picker {{
    display: flex;
    align-items: center;
    gap: 2px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    padding: 2px;
  }}

  .mode-picker button {{
    padding: 4px 12px;
    font-size: 12px;
    font-weight: 500;
    color: var(--text-dim);
    background: none;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-family: inherit;
    transition: var(--transition);
    display: flex;
    align-items: center;
    gap: 5px;
  }}

  .mode-picker button:hover {{
    color: var(--text-muted);
  }}

  .mode-picker button.active {{
    background: var(--surface-2);
    color: var(--text);
  }}

  /* ── Slide nav in topbar ── */
  .topbar-nav {{
    display: flex;
    align-items: center;
    gap: 4px;
  }}

  .topbar-nav button {{
    background: none;
    border: 1px solid transparent;
    color: var(--text-muted);
    width: 32px; height: 32px;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: var(--transition);
    font-size: 16px;
  }}

  .topbar-nav button:hover {{
    background: var(--surface);
    border-color: var(--border);
    color: var(--text);
  }}

  .topbar-nav button:disabled {{
    opacity: 0.3;
    cursor: default;
  }}

  .topbar-nav button:disabled:hover {{
    background: none;
    border-color: transparent;
    color: var(--text-muted);
  }}

  .slide-indicator {{
    font-size: 12px;
    color: var(--text-dim);
    font-variant-numeric: tabular-nums;
    min-width: 48px;
    text-align: center;
  }}

  /* ── Slide viewport ── */
  .slide-viewport {{
    position: fixed;
    top: 48px;
    left: 0; right: 0;
    bottom: 48px;
    overflow: hidden;
  }}

  .slide-track {{
    display: flex;
    height: 100%;
    transition: transform 0.4s cubic-bezier(0.25, 0.1, 0.25, 1);
    will-change: transform;
  }}

  .slide {{
    flex: 0 0 100%;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding: 48px 80px;
    overflow-y: auto;
  }}

  .slide-inner {{
    max-width: 800px;
    width: 100%;
    margin-top: auto;
    margin-bottom: auto;
  }}

  .slide h1 {{
    font-size: 40px;
    font-weight: 700;
    letter-spacing: -0.5px;
    margin-bottom: 16px;
    line-height: 1.15;
    color: var(--text);
  }}

  .slide h2 {{
    font-size: 24px;
    font-weight: 600;
    letter-spacing: -0.3px;
    margin-bottom: 12px;
    color: var(--text);
  }}

  .slide h3 {{
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 10px;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 1px;
  }}

  .slide p {{
    font-size: 17px;
    color: var(--text-muted);
    margin-bottom: 16px;
    max-width: 640px;
    line-height: 1.7;
  }}

  .slide ul {{ list-style: none; padding: 0; margin-bottom: 16px; }}
  .slide ol {{ padding-left: 1.5em; margin-bottom: 16px; }}

  .slide ul li {{
    padding: 10px 0 10px 24px;
    position: relative;
    color: var(--text-muted);
    font-size: 16px;
    line-height: 1.6;
  }}

  .slide ul li::before {{
    content: '';
    position: absolute;
    left: 0; top: 18px;
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--accent);
    opacity: 0.6;
  }}

  .slide ol li {{
    padding: 6px 0;
    color: var(--text-muted);
    font-size: 16px;
    line-height: 1.6;
  }}

  .slide strong {{ color: var(--warning); }}
  .slide em {{ color: #a78bfa; }}
  .slide code {{
    background: var(--surface);
    padding: 0.2em 0.4em;
    border-radius: 4px;
    font-family: 'SF Mono', 'Consolas', monospace;
    font-size: 0.9em;
  }}

  .slide pre {{
    background: var(--surface);
    padding: 1rem;
    border-radius: var(--radius);
    overflow-x: auto;
    font-size: 0.85rem;
    margin: 1rem 0;
    border: 1px solid var(--border);
  }}

  .slide pre code {{ padding: 0; background: none; }}

  .slide table {{
    border-collapse: collapse;
    width: 100%;
    font-size: 0.9rem;
    margin: 1rem 0;
  }}

  .slide th, .slide td {{
    border: 1px solid var(--border);
    padding: 0.75rem;
    text-align: left;
  }}

  .slide th {{
    background: var(--surface);
    color: var(--accent);
    font-weight: 600;
  }}

  /* ── Side nav arrows ── */
  .nav-arrow {{
    position: fixed;
    top: 50%;
    transform: translateY(-50%);
    width: 44px; height: 44px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 50%;
    color: var(--text-muted);
    font-size: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: var(--transition);
    z-index: 50;
    opacity: 0.5;
  }}

  .nav-arrow:hover {{
    opacity: 1;
    background: var(--surface-2);
    border-color: var(--border-hover);
    color: var(--text);
  }}

  .nav-arrow.disabled {{
    opacity: 0.15;
    cursor: default;
    pointer-events: none;
  }}

  .nav-arrow-left {{ left: 20px; }}
  .nav-arrow-right {{ right: 20px; }}

  /* ── Bottom bar with progress pips ── */
  .bottombar {{
    position: fixed;
    bottom: 0; left: 0; right: 0;
    height: 48px;
    background: rgba(10, 10, 10, 0.92);
    backdrop-filter: blur(20px);
    border-top: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 24px;
    z-index: 100;
    gap: 12px;
  }}

  .progress-bar-track {{
    display: flex;
    gap: 6px;
    align-items: center;
  }}

  .progress-pip {{
    width: 32px; height: 4px;
    border-radius: 2px;
    background: var(--border);
    cursor: pointer;
    transition: var(--transition);
    position: relative;
  }}

  .progress-pip:hover {{
    background: var(--text-dim);
    transform: scaleY(1.5);
  }}

  .progress-pip.active {{
    background: var(--accent);
    box-shadow: 0 0 8px var(--accent-glow);
  }}

  .progress-pip.visited {{
    background: var(--text-dim);
  }}

  .progress-pip.has-comment::after {{
    content: '';
    position: absolute;
    top: -5px;
    left: 50%; transform: translateX(-50%);
    width: 5px; height: 5px;
    border-radius: 50%;
    background: var(--accent);
  }}

  /* ── Keyboard hints ── */
  .keyboard-hint {{
    position: fixed;
    bottom: 56px;
    right: 24px;
    font-size: 11px;
    color: var(--text-dim);
    display: flex;
    gap: 12px;
    z-index: 50;
    opacity: 0.5;
    transition: var(--transition);
  }}

  .keyboard-hint:hover {{ opacity: 1; }}

  kbd {{
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 3px;
    padding: 1px 5px;
    font-size: 10px;
    font-family: inherit;
    color: var(--text-muted);
  }}

  /* ── Scroll mode content (hidden by default, shown in scroll mode) ── */
  .scroll-content {{
    display: none;
    padding-top: 48px;
    padding-bottom: 2rem;
  }}

  .scroll-content .section {{
    padding: 3rem 3rem;
    border-bottom: 1px solid var(--border);
  }}

  @media (min-width: 1024px) {{
    .scroll-content .section {{
      padding: 4rem 5rem;
      max-width: 1000px;
      margin: 0 auto;
    }}
  }}

  .scroll-content h1 {{
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 1rem;
    line-height: 1.2;
  }}

  .scroll-content h2 {{
    font-size: 1.6rem;
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--accent);
  }}

  .scroll-content h3 {{
    font-size: 1.1rem;
    color: var(--accent);
    margin: 1.5rem 0 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
  }}

  .scroll-content p {{ margin-bottom: 1rem; color: var(--text-muted); font-size: 16px; line-height: 1.7; }}
  .scroll-content ul {{ list-style: none; padding: 0; margin: 1rem 0; }}
  .scroll-content ol {{ padding-left: 1.5em; margin: 1rem 0; }}

  .scroll-content ul li {{
    padding: 6px 0 6px 20px;
    position: relative;
    color: var(--text-muted);
    font-size: 15px;
  }}

  .scroll-content ul li::before {{
    content: '';
    position: absolute;
    left: 0; top: 14px;
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--accent);
    opacity: 0.6;
  }}

  .scroll-content ol li {{ padding: 4px 0; color: var(--text-muted); font-size: 15px; }}
  .scroll-content strong {{ color: var(--warning); }}
  .scroll-content em {{ color: #a78bfa; }}

  .scroll-content code {{
    background: var(--surface);
    padding: 0.2em 0.4em;
    border-radius: 4px;
    font-family: 'SF Mono', 'Consolas', monospace;
    font-size: 0.9em;
  }}

  .scroll-content pre {{
    background: var(--surface);
    padding: 1rem;
    border-radius: var(--radius);
    overflow-x: auto;
    font-size: 0.85rem;
    margin: 1rem 0;
    border: 1px solid var(--border);
  }}

  .scroll-content pre code {{ padding: 0; background: none; }}

  .scroll-content table {{
    border-collapse: collapse;
    width: 100%;
    font-size: 0.9rem;
    margin: 1rem 0;
  }}

  .scroll-content th, .scroll-content td {{
    border: 1px solid var(--border);
    padding: 0.75rem;
    text-align: left;
  }}

  .scroll-content th {{
    background: var(--surface);
    color: var(--accent);
    font-weight: 600;
  }}

  /* ── Scroll mode: floating nav pill ── */
  .scroll-nav-pill {{
    display: none;
    position: fixed;
    bottom: 24px;
    right: 24px;
    align-items: center;
    gap: 0;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 999px;
    z-index: 100;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    overflow: hidden;
  }}

  body.scroll-mode .scroll-nav-pill {{ display: flex; }}

  .scroll-nav-pill button {{
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: transparent;
    border: none;
    color: var(--accent);
    cursor: pointer;
    font-size: 1.1rem;
    font-weight: 700;
    transition: background 0.15s;
  }}

  .scroll-nav-pill button:hover {{ background: rgba(20, 184, 166, 0.12); }}

  .scroll-nav-pill .nav-counter {{
    padding: 0 4px;
    font-size: 0.75rem;
    color: var(--text-muted);
    white-space: nowrap;
    min-width: 44px;
    text-align: center;
    user-select: none;
  }}

  /* Scroll mode progress bar */
  .scroll-progress-bar {{
    display: none;
    position: fixed;
    top: 48px;
    left: 0;
    height: 3px;
    background: var(--accent);
    z-index: 200;
    transition: width 0.2s ease-out;
  }}

  body.scroll-mode .scroll-progress-bar {{ display: block; }}
</style>
</head>
<body>

<!-- Top bar -->
<div class="topbar">
  <div class="topbar-left">
    <span class="topbar-title">{title}</span>
    <div class="mode-picker">
      <button class="active" data-mode="slides" onclick="switchMode('slides')">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>
        Slides
      </button>
      <button data-mode="scroll" onclick="switchMode('scroll')">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
        Scroll
      </button>
    </div>
  </div>
  <div class="topbar-right">
    <div class="topbar-nav">
      <button onclick="goToSlide(currentSlide - 1)" id="btnPrev" title="Previous">&#8592;</button>
      <span class="slide-indicator" id="slideIndicator">1 / {num_sections}</span>
      <button onclick="goToSlide(currentSlide + 1)" id="btnNext" title="Next">&#8594;</button>
    </div>
  </div>
</div>

<!-- Side navigation arrows -->
<div class="nav-arrow nav-arrow-left" id="arrowLeft" onclick="goToSlide(currentSlide - 1)">&#8592;</div>
<div class="nav-arrow nav-arrow-right" id="arrowRight" onclick="goToSlide(currentSlide + 1)">&#8594;</div>

<!-- Slide viewport -->
<div class="slide-viewport">
  <div class="slide-track" id="slideTrack">
{slides_html}
  </div>
</div>

<!-- Bottom bar with progress -->
<div class="bottombar">
  <div class="progress-bar-track" id="progressTrack"></div>
</div>

<!-- Keyboard hints -->
<div class="keyboard-hint">
  <span><kbd>&#8592;</kbd> <kbd>&#8594;</kbd> Navigate</span>
  <span><kbd>Esc</kbd> Close popover</span>
  <span>Click sections to comment</span>
</div>

<!-- Scroll mode content (hidden by default) -->
<div class="scroll-content">
{scroll_sections_html}
</div>

<!-- Scroll mode nav pill -->
<nav class="scroll-nav-pill">
  <button onclick="scrollPrev()" aria-label="Previous section">&#x25B2;</button>
  <span class="nav-counter"><span id="scrollCurrent">1</span> / {num_sections}</span>
  <button onclick="scrollNext()" aria-label="Next section">&#x25BC;</button>
</nav>

<!-- Scroll mode progress bar -->
<div class="scroll-progress-bar" id="scrollProgressBar"></div>

<script>
  // ── State ──
  let currentSlide = 0;
  let currentModeState = 'slides';
  const slides = document.querySelectorAll('.slide');
  const totalSlides = slides.length;
  const scrollSections = document.querySelectorAll('.scroll-content .section');

  // ── Init ──
  function init() {{
    buildProgressPips();
    updateNav();
  }}

  // ── Mode switching ──
  function switchMode(mode) {{
    if (mode === currentModeState) return;
    currentModeState = mode;

    document.querySelectorAll('.mode-picker button').forEach(function(btn) {{
      btn.classList.toggle('active', btn.getAttribute('data-mode') === mode);
    }});

    if (mode === 'scroll') {{
      document.body.classList.add('scroll-mode');
    }} else {{
      document.body.classList.remove('scroll-mode');
    }}
  }}

  // ── Progress pips ──
  function buildProgressPips() {{
    const track = document.getElementById('progressTrack');
    slides.forEach(function(slide, i) {{
      const pip = document.createElement('div');
      pip.className = 'progress-pip';
      pip.title = slide.dataset.title || ('Slide ' + (i + 1));
      pip.onclick = function() {{ goToSlide(i); }};
      track.appendChild(pip);
    }});
    updateProgressPips();
  }}

  function updateProgressPips() {{
    const pips = document.querySelectorAll('.progress-pip');
    pips.forEach(function(pip, i) {{
      pip.classList.toggle('active', i === currentSlide);
      pip.classList.toggle('visited', i < currentSlide);
    }});
  }}

  // ── Slide navigation ──
  function goToSlide(index) {{
    if (index < 0 || index >= totalSlides) return;
    currentSlide = index;
    document.getElementById('slideTrack').style.transform = 'translateX(-' + (currentSlide * 100) + '%)';
    updateNav();
    updateProgressPips();
  }}

  function updateNav() {{
    document.getElementById('slideIndicator').textContent = (currentSlide + 1) + ' / ' + totalSlides;
    var prevBtn = document.getElementById('btnPrev');
    var nextBtn = document.getElementById('btnNext');
    var arrowL = document.getElementById('arrowLeft');
    var arrowR = document.getElementById('arrowRight');
    prevBtn.disabled = currentSlide === 0;
    nextBtn.disabled = currentSlide === totalSlides - 1;
    arrowL.classList.toggle('disabled', currentSlide === 0);
    arrowR.classList.toggle('disabled', currentSlide === totalSlides - 1);
  }}

  // ── Scroll mode navigation ──
  let scrollIndex = 0;

  function updateScrollCurrent() {{
    var scrollPos = window.scrollY + 100;
    for (var i = scrollSections.length - 1; i >= 0; i--) {{
      if (scrollSections[i].offsetTop <= scrollPos) {{
        scrollIndex = i;
        document.getElementById('scrollCurrent').textContent = i + 1;
        break;
      }}
    }}
    var scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    var progress = scrollHeight > 0 ? (window.scrollY / scrollHeight) * 100 : 0;
    document.getElementById('scrollProgressBar').style.width = progress + '%';
  }}

  function scrollToSection(index) {{
    index = Math.max(0, Math.min(index, scrollSections.length - 1));
    scrollSections[index].scrollIntoView({{ behavior: 'smooth' }});
  }}

  function scrollNext() {{ scrollToSection(scrollIndex + 1); }}
  function scrollPrev() {{ scrollToSection(scrollIndex - 1); }}

  window.addEventListener('scroll', updateScrollCurrent, {{ passive: true }});

  // ── Keyboard navigation ──
  document.addEventListener('keydown', function(e) {{
    if (e.target.tagName === 'TEXTAREA' || e.target.tagName === 'INPUT') return;

    if (currentModeState === 'slides') {{
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {{
        e.preventDefault();
        goToSlide(currentSlide + 1);
      }} else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {{
        e.preventDefault();
        goToSlide(currentSlide - 1);
      }}
    }} else {{
      if (e.key === 'ArrowDown' || e.key === ' ' || e.key === 'ArrowRight') {{
        e.preventDefault();
        scrollNext();
      }} else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {{
        e.preventDefault();
        scrollPrev();
      }}
    }}
  }});

  init();
</script>

</body>
</html>'''


# ── Markdown to HTML Conversion ───────────────────────────────────────────────

def split_into_sections(content: str) -> list:
    """Split markdown content into logical slide sections.

    A markdown horizontal rule on its own line (`^---+$`, the same pattern the
    renderer converts to <hr>) is a HARD slide boundary (M4): we split on it
    FIRST, run the H2/short-merge logic INDEPENDENTLY within each hard block, and
    concatenate the per-block section lists WITHOUT any cross-block merging. This
    is the shared primitive for (a) keeping deliberate short slides (per-agent
    agent-voice slides in multi-agent decks) from being merged away, and (b) the
    legacy short-slide merge-fix. A deck with NO own-line `---` yields a single
    hard block == the whole content, so its sectioning is byte-identical to the
    pre-M4 behavior (regression-safe; golden-tested). The `---` marker lines are
    consumed by the split, so they do not also render as a stray <hr>.
    """
    fence_re = re.compile(r'^\s*```')
    hr_re = re.compile(r'^---+$')
    blocks, cur, in_fence = [], [], False
    for ln in content.split('\n'):
        if fence_re.match(ln):
            in_fence = not in_fence
            cur.append(ln)
            continue
        if not in_fence and hr_re.match(ln):
            blocks.append('\n'.join(cur))
            cur = []
            continue
        cur.append(ln)
    blocks.append('\n'.join(cur))
    nonempty = [b for b in blocks if b.strip()]
    if len(nonempty) <= 1:
        return _sections_from_block(nonempty[0] if nonempty else content)
    out = []
    for hb in nonempty:
        out.extend(_sections_from_block(hb))
    return out


def _sections_from_block(content: str) -> list:
    """Section a single hard block (no own-line `---` inside): the legacy
    split_into_sections body — H2 split, >3000-char H3 split, orphan-H1/H2 merge,
    and the <200-char short-section merge. Runs per hard block so merges never
    cross a `---` boundary."""
    sections = []

    # Split by H2 headers (## )
    parts = re.split(r'\n(?=## )', content)

    for part in parts:
        if not part.strip():
            continue

        # Check if section is too long (>3000 chars) - split by H3
        if len(part) > 3000:
            subsections = re.split(r'\n(?=### )', part)
            cleaned = [s.strip() for s in subsections if s.strip()]
            # Merge orphan H2 headers (no body after splitting) into the next subsection
            merged = []
            for sub in cleaned:
                lines = sub.split('\n')
                # An orphan: only has a heading line (## ...) with no meaningful body
                body = '\n'.join(lines[1:]).strip()
                if not body and sub.lstrip().startswith('## ') and not sub.lstrip().startswith('### '):
                    # This is a bare H2 header — prepend it to the next subsection
                    if merged:
                        # Shouldn't happen (H2 comes first), but just append
                        merged.append(sub)
                    else:
                        merged.append(sub)  # Will be merged below
                elif merged and merged[-1].lstrip().startswith('## ') and '\n' not in merged[-1].strip():
                    # Previous item was an orphan H2 — merge this subsection into it
                    merged[-1] = merged[-1] + '\n\n' + sub
                else:
                    merged.append(sub)
            sections.extend(merged)
        else:
            sections.append(part.strip())

    # Post-process: merge orphan H1-only title slides with the next section
    if sections:
        final = []
        i = 0
        while i < len(sections):
            s = sections[i]
            lines = s.split('\n')
            body = '\n'.join(lines[1:]).strip()
            is_bare_h1 = s.lstrip().startswith('# ') and not s.lstrip().startswith('## ') and not body
            if is_bare_h1 and i + 1 < len(sections):
                # Merge H1 title with next section
                final.append(s + '\n\n' + sections[i + 1])
                i += 2
            else:
                final.append(s)
                i += 1
        sections = final

    # Post-process: merge short sections (< 200 chars body) with the next section
    # These are "section header" slides with just a title and one intro line
    if sections:
        merged = []
        i = 0
        while i < len(sections):
            s = sections[i]
            lines = s.split('\n')
            body = '\n'.join(lines[1:]).strip()
            body_len = len(body)
            is_h2 = s.lstrip().startswith('## ') and not s.lstrip().startswith('### ')
            # Merge short H2 sections with the next section
            if is_h2 and body_len < 200 and i + 1 < len(sections):
                merged.append(s + '\n\n' + sections[i + 1])
                i += 2
            else:
                merged.append(s)
                i += 1
        sections = merged

    return sections


def convert_md_to_html(text: str) -> str:
    """Convert markdown text to HTML."""
    # Preserve SVG blocks - extract before markdown conversion
    svg_blocks = []
    def _extract_svg(match):
        svg_blocks.append(match.group(0))
        return f'@@SVGPLACEHOLDER{len(svg_blocks) - 1}@@'
    text = re.sub(r'<svg[\s\S]*?</svg>', _extract_svg, text)

    # Preserve FENCED CODE BLOCKS the same way, and for the same reason. The
    # fence -> <pre><code> conversion used to happen mid-function, which left the
    # verbatim content exposed to every block-level pass that follows it: the
    # `- `, `1. `, `> ` and `---` regexes are all MULTILINE and none of them
    # skips <pre>. A pasted email, log or diff whose line happened to start with
    # "1. " had an <ol><li> injected INSIDE the code block, and the block
    # splitter then cut the <pre> short at the stray </ol> and spilled the rest
    # of the verbatim text out as prose paragraphs. Extracting here — before any
    # pass runs — is the only placement that protects the content from all of
    # them, and it also stops bold/italic/link markup being interpreted inside
    # what is by definition literal text. Escaped on the way in, since a fenced
    # block may legitimately contain < and >.
    code_blocks = []

    def _extract_fence(match):
        body = (match.group(2).replace('&', '&amp;')
                              .replace('<', '&lt;').replace('>', '&gt;'))
        code_blocks.append(f'<pre><code>{body}</code></pre>')
        return f'@@CODEBLOCK{len(code_blocks) - 1}@@'

    text = re.sub(r'```(\w*)\n([\s\S]*?)```', _extract_fence, text)

    # INLINE code, extracted here for exactly the reasons given above for fences —
    # it is literal text by definition, so it must be escaped, and it must be taken
    # out of the way before the emphasis/link passes can rewrite its insides.
    # Escaping is the load-bearing half: the old inline pass ran late and emitted
    # the span contents raw, so a deck that merely MENTIONED a tag in backticks
    # emitted it as real markup. `<title>` is the sharp case — the HTML parser
    # switches to raw-text mode at a start tag it never sees closed and swallows
    # the entire rest of the document, so the nav bar and the whole <script> stop
    # being markup and the deck silently loses navigation. Nothing throws: the JS
    # was never parsed, so there is no console error to find. Observed 2026-08-05
    # on the public-exposure execution plan (5 slides of 26, no nav, clean console).
    inline_codes = []

    def _extract_inline_code(match):
        body = (match.group(1).replace('&', '&amp;')
                              .replace('<', '&lt;').replace('>', '&gt;'))
        inline_codes.append(f'<code>{body}</code>')
        return f'@@INLINECODE{len(inline_codes) - 1}@@'

    text = re.sub(r'`([^`\n]+)`', _extract_inline_code, text)

    # Headers
    text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)

    # Protect markdown link TARGETS from the emphasis passes below. A real URL can
    # legitimately contain `__` or `_..._` (e.g. a gob.mx PDF ending `_final__1___1_.pdf`),
    # and the bold/italic regexes would rewrite those into <strong>/<em> INSIDE the href,
    # producing a 404 that only shows up when someone clicks it. Stash each `](url)`
    # target behind a markdown-inert sentinel and restore it just before links are
    # converted. Sentinel uses @@ (never _ or *) per the L-204 sentinel-inertness rule.
    _link_urls = []

    def _stash_link_url(m):
        _link_urls.append(m.group(1))
        return f'](@@LINKURL{len(_link_urls) - 1}@@)'

    text = re.sub(r'\]\(([^)\s]+)\)', _stash_link_url, text)

    # Bold and italic — both * and _ forms (underscore emphasis was unhandled, so
    # e.g. "*__Force-test:__ ...*" left the inner __label__ as literal underscores).
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # single _italic_ only at word boundaries (so snake_case identifiers are left alone)
    text = re.sub(r'(?<![\w])_(?=\S)(.+?)(?<=\S)_(?![\w])', r'<em>\1</em>', text)

    # The slide-1 disclosure line renders as <em> (accent/yellow), which makes the
    # whole opening slide yellow. Re-class it to a neutral white block so it reads as
    # a disclosure, not as emphasis. Matches the first "Disclosure: ..." em only.
    text = re.sub(r'<em>(Disclosure:\s.*?)</em>',
                  r'<span class="deck-disclosure"><em>\1</em></span>',
                  text, count=1, flags=re.DOTALL)

    # Metadata lines: consecutive lines starting with <strong>Key</strong>: Value
    # Convert single newlines between them to <br> so they don't run together in <p>
    text = re.sub(
        r'(<strong>[^<]+</strong>: .+)\n(?=<strong>[^<]+</strong>: )',
        r'\1<br>\n',
        text
    )

    # Code blocks
    text = re.sub(r'```(\w*)\n(.*?)```', r'<pre><code>\2</code></pre>', text, flags=re.DOTALL)

    # Inline code is extracted and escaped up-front (see _extract_inline_code).
    # Any surviving backtick pair here spans a newline, which the up-front pass
    # deliberately does not match; convert it without escaping, as before.
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)

    # Checkboxes
    text = re.sub(r'^\- \[x\] (.+)$', r'<li class="status-ok">✓ \1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'^\- \[ \] (.+)$', r'<li>☐ \1</li>', text, flags=re.MULTILINE)

    # Markdown links [text](url) -> <a>. Runs AFTER the footnote pre-pass (which has
    # already turned [^n]/[cross-*] into <sup>/removed them), so this only sees real
    # links. External links open in a new tab; internal/anchor links stay in-page.
    # Restore the stashed link targets now that every emphasis pass has run.
    if _link_urls:
        # Out-of-range index => the source text contained a LITERAL @@LINKURL<n>@@
        # (e.g. a doc describing this very mechanism). Leave it untouched rather than
        # raising IndexError — a shared renderer must not crash on prose about itself.
        def _restore_link_url(m):
            i = int(m.group(1))
            return _link_urls[i] if i < len(_link_urls) else m.group(0)

        text = re.sub(r'@@LINKURL(\d+)@@', _restore_link_url, text)

    def _md_link(m):
        label, url = m.group(1), m.group(2)
        tgt = ' target="_blank" rel="noopener"' if url.startswith(('http://', 'https://')) else ''
        return f'<a href="{url}" class="md-link"{tgt}>{label}</a>'
    text = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', _md_link, text)

    # Nested list items (indented `- ` / `1. `) — flatten with a visual indent so the
    # consecutive-<li> wrapper below keeps them inside the parent <ul> in document order.
    # Without this they survive as bare text and get silently dropped by the block splitter.
    text = re.sub(r'^[ \t]+\- (.+)$', r'<li style="margin-left:1.4em">\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'^[ \t]+(\d+)\. (.+)$', r'<li style="margin-left:1.4em;list-style:none"><strong>\1.</strong> \2</li>', text, flags=re.MULTILINE)

    # Unordered lists — convert remaining `- ` items to <li>, wrap consecutive <li> in <ul>
    text = re.sub(r'^\- (.+)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'((?:<li[^>]*>.*</li>\n?)+)', r'<ul>\1</ul>', text)

    # Numbered lists — use temp markers to avoid matching <li> already inside <ul>
    text = re.sub(r'^\d+\. (.+)$', r'<__OLI>\1</__OLI>', text, flags=re.MULTILINE)
    text = re.sub(r'((?:<__OLI>.*</__OLI>\n?)+)', r'<ol>\1</ol>', text)
    text = text.replace('<__OLI>', '<li>').replace('</__OLI>', '</li>')

    # Blockquotes — drop empty separator lines (a bare '>' with no content) so they don't render as literal '>'
    text = re.sub(r'^>[ \t]*$', '', text, flags=re.MULTILINE)
    # blockquote heading lines ("> ### Title") -> styled heading (were rendering literal ###)
    text = re.sub(r'^> #{2,6} (.+)$', r'<blockquote class="card"><div class="bq-head">\1</div></blockquote>', text, flags=re.MULTILINE)
    # blockquote BULLET runs ("> - item" lines) -> a real <ul> inside the quote, so
    # pattern-claim bullets render as a list instead of flattening into run-together prose.
    def _bq_bullets(m):
        items = re.findall(r'^> - (.+)$', m.group(0), flags=re.MULTILINE)
        return '> <ul>' + ''.join(f'<li>{it.strip()}</li>' for it in items) + '</ul>\n'
    text = re.sub(r'(?:^> - .+$\n?)+', _bq_bullets, text, flags=re.MULTILINE)
    text = re.sub(r'^> (.+)$', r'<blockquote class="card">\1</blockquote>', text, flags=re.MULTILINE)
    # merge consecutive blockquote cards (e.g. pattern-claim sub-blocks) into ONE card so
    # they read as a single grouped section instead of a stack of separate bubbles
    text = re.sub(r'</blockquote>\s*<blockquote class="card">', '<div class="bq-gap"></div>', text)

    # Horizontal rules
    text = re.sub(r'^---+$', r'<hr style="border-color: #333; margin: 2rem 0;">', text, flags=re.MULTILINE)

    # Tables
    if '|' in text:
        lines = text.split('\n')
        result_lines = []
        in_table = False
        header_done = False
        in_pre = False

        for line in lines:
            # Never table-ify content inside <pre> blocks — ASCII diagrams with
            # pipe characters would be mangled into broken table markup
            if in_pre or '<pre' in line:
                if in_table:
                    result_lines.append('</tbody></table></div>')
                    in_table = False
                    header_done = False
                result_lines.append(line)
                in_pre = '</pre>' not in line
                continue
            stripped = line.strip()
            if stripped.startswith('|') and stripped.endswith('|'):
                cells = [c.strip() for c in stripped.split('|')[1:-1]]

                if '---' in stripped:
                    # Separator row, skip but mark header done
                    header_done = True
                    continue

                if not in_table:
                    result_lines.append('<div class="table-container"><table>')
                    result_lines.append('<thead><tr>' + ''.join(f'<th>{c}</th>' for c in cells) + '</tr></thead>')
                    result_lines.append('<tbody>')
                    in_table = True
                elif header_done or in_table:
                    result_lines.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
            else:
                if in_table:
                    result_lines.append('</tbody></table></div>')
                    in_table = False
                    header_done = False
                result_lines.append(line)

        if in_table:
            result_lines.append('</tbody></table></div>')

        text = '\n'.join(result_lines)

    # Smart paragraph wrapping — split on blank lines, only wrap bare text in <p>
    # NOTE: SVG placeholders are still in place here so they don't interfere with wrapping
    block_tags = ('h1', 'h2', 'h3', 'h4', 'ul', 'ol', 'pre', 'div', 'table', 'blockquote', 'hr', 'svg', '@@SVG')
    chunks = re.split(r'\n\n+', text)
    result_chunks = []
    for chunk in chunks:
        stripped = chunk.strip()
        if not stripped:
            continue
        # If it starts with a block-level element or is an SVG placeholder, leave as-is
        if (any(stripped.startswith(f'<{tag}') for tag in block_tags)
                or stripped.startswith('@@SVGPLACEHOLDER')
                or stripped.startswith('@@CODEBLOCK')):
            result_chunks.append(stripped)
        else:
            # Wrap bare text in <p>
            result_chunks.append(f'<p>{stripped}</p>')
    text = '\n'.join(result_chunks)

    # Re-insert preserved SVG blocks AFTER paragraph wrapping to avoid <p><svg></p>
    for i, svg in enumerate(svg_blocks):
        text = text.replace(f'@@SVGPLACEHOLDER{i}@@', svg)

    # Same for fenced code, and for the same reason — a <pre> wrapped in <p> is
    # invalid and the block splitter treats the stray </p> as the end of the pre.
    for i, code in enumerate(code_blocks):
        text = text.replace(f'@@CODEBLOCK{i}@@', code)

    # Inline code goes back last. It is inline content, so unlike the two above it
    # WANTS to be inside whatever <p>/<li>/<td> the wrapping put it in.
    for i, code in enumerate(inline_codes):
        text = text.replace(f'@@INLINECODE{i}@@', code)

    return text


def _detect_brand(title: str) -> tuple:
    """Detect brand from title and return (primary_color, favicon_html, logo_letter, logo_text, accent_color)."""
    title_lower = title.lower()
    # Check service brands first — documents like "ProductBeacon for «Security Vendor»" should use
    # the service brand, not the client brand. Then «AI Platform», then others.
    if 'productbeacon' in title_lower or 'product beacon' in title_lower:
        # Beacon/lighthouse icon matching productbeacon.agency brand
        return ('#F59E0B',
                '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'><rect width=\'32\' height=\'32\' rx=\'6\' fill=\'%230F172A\'/><circle cx=\'16\' cy=\'12\' r=\'4\' fill=\'%23F59E0B\'/><path d=\'M10 18L16 28L22 18\' stroke=\'%23F59E0B\' stroke-width=\'2.5\' stroke-linecap=\'round\' stroke-linejoin=\'round\' fill=\'none\'/></svg>">',
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="28" height="28"><rect width="400" height="400" rx="48" fill="#0F172A"/><circle cx="200" cy="150" r="50" fill="#F59E0B"/><path d="M125 225 L200 350 L275 225" stroke="#F59E0B" stroke-width="28" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>',
                'ProductBeacon', '#FBBF24')
    elif 'resonance' in title_lower:
        # Resonance — warm bookish brand: ember accent on cream, the engagement/resonance curve
        # as the mark (Concept C). Renders on the LIGHT theme (see _brand_theme). Palette from
        # Resonance brand & design system doc 05: ember #BC4F28 primary, sage #6B8F5E accent.
        # Checked BEFORE 'vision to value' since Resonance docs live under that path/title family.
        return ('#BC4F28',
                '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'><rect width=\'32\' height=\'32\' rx=\'6\' fill=\'%23F4ECD8\'/><path d=\'M4 21 C9 21 9 11 14 11 C19 11 18 23 23 23 C26 23 27 16 28 13\' stroke=\'%23BC4F28\' stroke-width=\'2.5\' fill=\'none\' stroke-linecap=\'round\' stroke-linejoin=\'round\'/></svg>">',
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="28" height="28"><rect width="32" height="32" rx="6" fill="#F4ECD8"/><path d="M4 21 C9 21 9 11 14 11 C19 11 18 23 23 23 C26 23 27 16 28 13" stroke="#BC4F28" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
                'Resonance', '#6B8F5E')
    elif 'decision provenance' in title_lower:
        # Decision Provenance Standard — neutral / ISO-W3C-institutional. Renders on the
        # LIGHT theme (white ground, dark text, desaturated-blue accent) so the Standard's
        # white-ground figures embed natively. See _brand_theme() and md_to_mobile_html().
        # Mark: a record (stacked lines) with a short accent rule under the last line.
        # The seal-ring was DROPPED per GC + Design build constraint — a ringed seal reads
        # as a "certified" badge, which the Standard must not imply. The record-lines alone
        # carry the provenance meaning (a logged, ordered record) without the certification cue.
        return ('#3A5A78',
                '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'><rect width=\'32\' height=\'32\' rx=\'5\' fill=\'%231A1A1A\'/><rect x=\'8\' y=\'8\' width=\'16\' height=\'2\' fill=\'%23F5F5F5\'/><rect x=\'8\' y=\'13\' width=\'16\' height=\'2\' fill=\'%23F5F5F5\'/><rect x=\'8\' y=\'18\' width=\'16\' height=\'2\' fill=\'%23F5F5F5\'/><rect x=\'8\' y=\'23\' width=\'9\' height=\'2\' fill=\'%233A5A78\'/></svg>">',
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="28" height="28"><rect width="32" height="32" rx="5" fill="#1A1A1A"/><rect x="8" y="8" width="16" height="2" fill="#F5F5F5"/><rect x="8" y="13" width="16" height="2" fill="#F5F5F5"/><rect x="8" y="18" width="16" height="2" fill="#F5F5F5"/><rect x="8" y="23" width="9" height="2" fill="#3A5A78"/></svg>',
                'Decision Provenance Standard', '#8FA8C0')
    elif 'product org' in title_lower or 'product-org' in title_lower or 'vision to value' in title_lower:
        # Hexagon network logo matching Product Org OS landing page
        return ('#E94560',
                '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'><defs><linearGradient id=\'g\' x1=\'0\' y1=\'0\' x2=\'1\' y2=\'1\'><stop offset=\'0\' stop-color=\'%23E94560\'/><stop offset=\'1\' stop-color=\'%234ECCA3\'/></linearGradient></defs><polygon points=\'16,2 29,9 29,23 16,30 3,23 3,9\' fill=\'none\' stroke=\'url(%23g)\' stroke-width=\'1.5\'/><circle cx=\'16\' cy=\'2\' r=\'2.5\' fill=\'%234A90D9\'/><circle cx=\'29\' cy=\'9\' r=\'2.5\' fill=\'%239B59B6\'/><circle cx=\'29\' cy=\'23\' r=\'2.5\' fill=\'%234ECCA3\'/><circle cx=\'16\' cy=\'30\' r=\'2.5\' fill=\'%23FFC93C\'/><circle cx=\'3\' cy=\'23\' r=\'2.5\' fill=\'%2327AE60\'/><circle cx=\'3\' cy=\'9\' r=\'2.5\' fill=\'%23E94560\'/><circle cx=\'16\' cy=\'16\' r=\'3.5\' fill=\'url(%23g)\'/><line x1=\'16\' y1=\'2\' x2=\'16\' y2=\'16\' stroke=\'url(%23g)\' stroke-width=\'.5\' opacity=\'.5\'/><line x1=\'29\' y1=\'9\' x2=\'16\' y2=\'16\' stroke=\'url(%23g)\' stroke-width=\'.5\' opacity=\'.5\'/><line x1=\'29\' y1=\'23\' x2=\'16\' y2=\'16\' stroke=\'url(%23g)\' stroke-width=\'.5\' opacity=\'.5\'/><line x1=\'16\' y1=\'30\' x2=\'16\' y2=\'16\' stroke=\'url(%23g)\' stroke-width=\'.5\' opacity=\'.5\'/><line x1=\'3\' y1=\'23\' x2=\'16\' y2=\'16\' stroke=\'url(%23g)\' stroke-width=\'.5\' opacity=\'.5\'/><line x1=\'3\' y1=\'9\' x2=\'16\' y2=\'16\' stroke=\'url(%23g)\' stroke-width=\'.5\' opacity=\'.5\'/></svg>">',
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="28" height="28"><defs><linearGradient id="hg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#E94560"/><stop offset="100%" stop-color="#4ECCA3"/></linearGradient></defs><polygon points="100,10 178,55 178,145 100,190 22,145 22,55" fill="none" stroke="url(#hg)" stroke-width="2"/><line x1="100" y1="10" x2="100" y2="100" stroke="url(#hg)" stroke-width="1" opacity="0.5"/><line x1="178" y1="55" x2="100" y2="100" stroke="url(#hg)" stroke-width="1" opacity="0.5"/><line x1="178" y1="145" x2="100" y2="100" stroke="url(#hg)" stroke-width="1" opacity="0.5"/><line x1="100" y1="190" x2="100" y2="100" stroke="url(#hg)" stroke-width="1" opacity="0.5"/><line x1="22" y1="145" x2="100" y2="100" stroke="url(#hg)" stroke-width="1" opacity="0.5"/><line x1="22" y1="55" x2="100" y2="100" stroke="url(#hg)" stroke-width="1" opacity="0.5"/><circle cx="100" cy="10" r="8" fill="#4A90D9"/><circle cx="178" cy="55" r="8" fill="#9B59B6"/><circle cx="178" cy="145" r="8" fill="#4ECCA3"/><circle cx="100" cy="190" r="8" fill="#FFC93C"/><circle cx="22" cy="145" r="8" fill="#27AE60"/><circle cx="22" cy="55" r="8" fill="#E94560"/><circle cx="100" cy="100" r="12" fill="url(#hg)"/></svg>',
                'Product Org OS', '#4ECCA3')
    else:
        return ('#14B8A6',
                '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'><rect width=\'32\' height=\'32\' rx=\'6\' fill=\'%2314B8A6\'/><text x=\'16\' y=\'23\' font-family=\'system-ui\' font-size=\'20\' font-weight=\'700\' fill=\'white\' text-anchor=\'middle\'>Y</text></svg>">',
                'Y', 'Generic', '#22D3EE')


def _brand_theme(title: str) -> str:
    """Return the ground theme for a title's brand: 'light' or 'dark' (default).

    Scoped narrowly: only the Decision Provenance Standard renders on a white/light
    ground (so its ISO/W3C-style white-ground figures embed natively). Every other
    brand keeps the existing dark deck — this function MUST default to 'dark' so no
    other brand's rendering changes.
    """
    if 'decision provenance' in title.lower():
        return 'light'
    if 'resonance' in title.lower():
        return 'light'
    return 'dark'


# Light-theme override block. Injected before </style> ONLY for light-theme brands,
# scoped under html.theme-light so it can never affect dark-theme decks. Redefines the
# :root color variables (so everything keyed off them flips automatically) plus the
# handful of rules that hardcode dark values (grid bg, zebra rows, code/pre, nav bar,
# gradient-text headings). Targets WCAG-AA contrast on a white ground.
LIGHT_THEME_CSS = '''
/* ── Light theme (Decision Provenance Standard — white ISO/W3C-style ground) ── */
html.theme-light {
  --bg-dark: #FFFFFF;
  --bg-card: #F4F6F8;
  --bg-elevated: #ECEFF3;
  --text-primary: #1A1A1A;   /* near-black body/heading text — AA on white */
  --text-secondary: #353B43; /* darkened from dark-theme #8B949E for AA on white */
  --text-muted: #5A636E;     /* AA on white */
  --border: rgba(26,26,26,0.14);
}
/* Subtle grid uses dark hairlines on white instead of white-on-dark (which vanish) */
html.theme-light .slide::before {
  background-image:
    linear-gradient(rgba(26,26,26,0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(26,26,26,0.035) 1px, transparent 1px);
}
/* Zebra rows: dark-on-white tint */
html.theme-light tr:nth-child(even) { background: rgba(26,26,26,0.03); }
/* Code surfaces: light tints, dark text */
html.theme-light pre { background: #F4F6F8; }
html.theme-light code { background: rgba(26,26,26,0.06); color: #1A1A1A; }
html.theme-light pre code { background: none; }
/* Nav bar + jump overlay: light glass instead of dark */
html.theme-light .nav-bar { background: rgba(255,255,255,0.92); }
html.theme-light .slide-jump-overlay { background: rgba(26,26,26,0.45); }
html.theme-light .slide-jump-box { box-shadow: 0 8px 32px rgba(26,26,26,0.18); }
/* Gradient-clip text on a light ground would render light-on-light. Replace the
   gradient with a solid dark/accent fill so headings stay legible (AA). */
html.theme-light h2,
html.theme-light .hero-title,
html.theme-light .kpi-value,
html.theme-light .stat-highlight {
  background: none;
  -webkit-background-clip: initial;
  background-clip: initial;
  -webkit-text-fill-color: initial;
  color: var(--primary);
}
/* em uses --accent (desaturated blue) which is too light on white for body emphasis */
html.theme-light em { color: var(--primary); }
/* Blockquote (Standard call-outs): primary-colored text reads better than light accent */
html.theme-light blockquote p { color: var(--primary); }
/* Logo-letter mark keeps its gradient chip; ensure its glyph stays white on the chip */
html.theme-light .logo-mark.logo-letter { color: #fff; }
'''


# Footnote / References CSS — injected into the <style> block ONLY when a deck
# actually renders footnotes, so footnote-free decks stay byte-identical (mirrors
# the conditional LIGHT_THEME_CSS injection pattern). Uses single braces (it is
# string-replaced post-.format(), not passed through .format()).
FOOTNOTE_CSS = '''
/* Footnotes (label-agnostic numeric superscripts + References slide) */
.fn-ref { font-size: 0.62em; line-height: 0; vertical-align: super; }
.fn-ref a { color: var(--accent); text-decoration: none; padding: 0 0.1em; }
.fn-ref a:hover { text-decoration: underline; }
ol.references { font-size: 0.85rem; line-height: 1.5; padding-left: 1.4em; }
ol.references li { margin: 0.4rem 0; word-break: break-word; }
.fn-back { color: var(--accent); text-decoration: none; margin-left: 0.3em; }
.fn-back:hover { text-decoration: underline; }
'''


def _apply_footnotes_and_crossrefs(md_content: str) -> str:
    """Whole-document pre-pass (label-agnostic footnotes + cross-ref stripping).

    Render-only: does NOT renumber source files (renumber-footnotes.py owns that).
    Steps, all strictly additive (each fires only when its pattern is present):
      1. Strip internal cross-reference markup `[cross-front:...]` / `[cross-report:...]`
         entirely (reader-facing markup that must never show); collapse the doubled
         spaces a mid-line removal can leave.
      2. Collect footnote DEFINITIONS `^[^label]: text` (multiline), remove the
         definition lines from the body so they don't render inline.
      3. Replace inline MARKERS `[^label]` with numbered <sup> refs. Each DISTINCT
         label gets a sequential display number by order of first appearance
         (1, 2, 3 ...) regardless of the source label string (pg1/cn3/etc.).
      4. Append a synthesized `## References` section (its own slide) with a
         numbered <ol class="references"> of definitions + back-anchors. Cross-slide
         #fn-N / #fnref-N anchors resolve because all slides share one DOM.
    Orphan definitions (label never used as a marker) are still listed in
    References, after the referenced ones, so they're dropped-visible not lost.

    A document with no `[^...]` markup and no `[cross-...]` markup is returned
    byte-identical.
    """
    # Reset per-call telemetry; footnotes_rendered gates the CSS injection so a
    # footnote-free deck never gets the extra <style> rules (byte-identical).
    _apply_footnotes_and_crossrefs.footnotes_rendered = False
    _apply_footnotes_and_crossrefs.last_orphans = []
    _apply_footnotes_and_crossrefs.last_counts = {'markers': 0, 'definitions': 0, 'orphans': 0}

    # --- Step 1: strip internal cross-reference markup (additive: no-op if absent) ---
    if re.search(r'\[cross-(?:front|report):[^\]]*\]', md_content):
        md_content = re.sub(r'\[cross-(?:front|report):[^\]]*\]', '', md_content)
        # collapse doubled spaces a mid-line removal may have left (not at line start)
        md_content = re.sub(r'(?<=\S)[ \t]{2,}(?=\S)', ' ', md_content)
        # tidy a space left immediately before sentence punctuation
        md_content = re.sub(r' +([,.;:)])', r'\1', md_content)

    # --- Step 2: collect footnote definitions (^[^label]: text) ---
    def_re = re.compile(r'^\[\^([A-Za-z0-9-]+)\]:[ \t]*(.*)$', re.MULTILINE)
    definitions = []  # ordered list of (label, text)
    seen_def_labels = set()
    for m in def_re.finditer(md_content):
        lbl = m.group(1)
        if lbl not in seen_def_labels:
            seen_def_labels.add(lbl)
            definitions.append((lbl, m.group(2).strip()))
    # If there are no definitions at all, footnotes are inert -> return as-is.
    if not definitions:
        return md_content
    # Remove definition lines from the body (so they don't render where they sit).
    md_content = def_re.sub('', md_content)

    # --- Step 3: assign sequential display numbers to DISTINCT marker labels ---
    # A marker is `[^label]` that is NOT a definition (definitions already removed,
    # so any remaining `[^label]` is a marker).
    marker_re = re.compile(r'\[\^([A-Za-z0-9-]+)\]')
    label_to_num = {}
    order = []  # display order of labels (referenced ones first)

    def _assign(match):
        lbl = match.group(1)
        if lbl not in label_to_num:
            label_to_num[lbl] = len(label_to_num) + 1
            order.append(lbl)
        n = label_to_num[lbl]
        return f'<sup class="fn-ref" id="fnref-{n}"><a href="#fn-{n}">{n}</a></sup>'

    md_content = marker_re.sub(_assign, md_content)

    # --- Step 4: build References section, ordered by display number, orphans last ---
    def_map = dict(definitions)
    ref_items = []
    # referenced labels (in display order) that also have a definition
    for lbl in order:
        if lbl in def_map:
            n = label_to_num[lbl]
            ref_items.append((n, def_map[lbl]))
    # orphan definitions: defined but never referenced -> assign trailing numbers
    next_n = len(label_to_num) + 1
    orphan_labels = []
    orphan_num = {}
    for lbl, text in definitions:
        if lbl not in label_to_num:
            ref_items.append((next_n, text))
            orphan_labels.append(lbl)
            orphan_num[lbl] = next_n
            next_n += 1
    ref_items.sort(key=lambda t: t[0])

    # Render footnote markers that appear INSIDE a definition's own text
    # (e.g. "See [^wl1] and [^wl2].") so they don't survive as literal codes in
    # the References list. Map them to display numbers via the complete map.
    full_map = dict(label_to_num)
    full_map.update(orphan_num)

    def _render_inner(m):
        lbl = m.group(1)
        if lbl in full_map:
            k = full_map[lbl]
            return f'<sup class="fn-ref"><a href="#fn-{k}">{k}</a></sup>'
        return ''  # unknown label: drop the literal bracket rather than show it

    li_html = []
    for n, text in ref_items:
        text = marker_re.sub(_render_inner, text)
        # inline markdown (bold/italic/code/links) inside a definition is converted
        # by convert_md_to_html per-slide; we keep raw text but it sits inside an
        # <li> that the converter leaves untouched (block splitter preserves <ol>).
        li_html.append(
            f'<li id="fn-{n}" style="list-style:none"><strong>{n}.</strong> {text} <a href="#fnref-{n}" class="fn-back">&#8617;</a></li>'
        )
    references_block = (
        '\n\n## References\n\n'
        '<ol class="references">\n' + '\n'.join(li_html) + '\n</ol>\n'
    )
    md_content = md_content.rstrip() + references_block

    # stash orphan info on the function for the caller's report (best-effort)
    _apply_footnotes_and_crossrefs.footnotes_rendered = True
    _apply_footnotes_and_crossrefs.last_orphans = orphan_labels
    _apply_footnotes_and_crossrefs.last_counts = {
        'markers': len(label_to_num),
        'definitions': len(definitions),
        'orphans': len(orphan_labels),
    }
    return md_content


def md_to_mobile_html(md_content: str, title: str, brand_override: str = None, commenting: bool = True, font_scale: float = None) -> tuple:
    """Convert markdown to slide-based HTML presentation (Brand-Adaptive V3 style).

    brand_override: if set, forces brand/theme detection to use this string
    (e.g. "productbeacon") instead of the document title.
    commenting: when False (public-facing decks), content blocks are not wrapped
    in .commentable divs and the Review slide is replaced by a hidden ID stub
    (kept so the template JS doesn't null-deref).
    """
    import json as _json

    # --- Whole-document pre-pass: footnotes + internal cross-ref stripping ---
    # Runs on the FULL md_content BEFORE split_into_sections so that footnote
    # markers and their definitions (which can land on different slides) are
    # reconciled against one shared DOM. ADDITIVE: if no `[^...]` footnote
    # markup and no `[cross-...]` markup are present, md_content is returned
    # byte-identical and the rest of rendering is unchanged.
    md_content = _apply_footnotes_and_crossrefs(md_content)

    sections = split_into_sections(md_content)
    _brand_key = brand_override or title
    primary_color, favicon_html, logo_letter_raw, logo_text, accent_color = _detect_brand(_brand_key)
    theme = _brand_theme(_brand_key)
    logo_letter = logo_letter_raw

    # Detect RTL content (Hebrew/Arabic characters)
    hebrew_chars = sum(1 for c in md_content[:2000] if '\u0590' <= c <= '\u05FF' or '\uFB1D' <= c <= '\uFB4F')
    is_rtl = hebrew_chars > 20

    # Build slides HTML and track section groups
    slides_html_parts = []
    section_groups = []  # [{name, start, end}]
    current_group_name = None
    current_group_start = 0

    for i, section in enumerate(sections):
        # Extract section title
        heading_match = re.search(r'^#{1,3}\s+(.+)$', section, re.MULTILINE)
        section_title = heading_match.group(1) if heading_match else f'Section {i+1}'
        section_title = re.sub(r'\*\*(.+?)\*\*', r'\1', section_title)
        section_title = re.sub(r'\*(.+?)\*', r'\1', section_title)

        # Determine section group (h2 = new group)
        is_h2 = section.lstrip().startswith('## ') and not section.lstrip().startswith('### ')
        is_h1 = section.lstrip().startswith('# ') and not section.lstrip().startswith('## ')

        if is_h1 or is_h2:
            if current_group_name is not None:
                section_groups.append({
                    'name': current_group_name,
                    'start': current_group_start,
                    'end': i - 1
                })
            current_group_name = section_title[:20]
            current_group_start = i

        # Convert section content to HTML
        section_html = convert_md_to_html(section)

        # Split into normalized blocks — the splitter also repairs structure and
        # rescues bare gap text, so it runs in BOTH modes. Commentable wrappers
        # are added only when commenting is on.
        blocks = _split_html_into_blocks(section_html)
        if blocks:
            wrapped_blocks = []
            block_idx = 0
            past_leading_headings = False
            for j, (block_html, label) in enumerate(blocks):
                is_bare_heading = bool(re.match(r'^<h[1234][^>]*>.*</h[1234]>$', block_html.strip(), re.DOTALL))
                # Don't wrap leading headings in commentable divs — they duplicate
                # the section label and create empty-looking boxes at the top
                if not commenting or (not past_leading_headings and is_bare_heading):
                    if not is_bare_heading or past_leading_headings:
                        past_leading_headings = True
                    wrapped_blocks.append(block_html)
                    continue
                past_leading_headings = True
                block_idx += 1
                section_id = f"s{i+1}-{block_idx}"
                label_escaped = label.replace('"', '&quot;').replace('<', '&lt;')
                wrapped_blocks.append(
                    f'<div class="commentable" data-section="{section_id}" data-label="{label_escaped}">\n'
                    f'  {block_html}\n'
                    f'</div>'
                )
            section_html = '\n'.join(wrapped_blocks)

        # Build section label for brand bar
        label_text = section_title[:30] + ('...' if len(section_title) > 30 else '')

        # Build the slide
        active_class = ' active' if i == 0 else ''
        logo_class = 'logo-mark logo-wide' if ('<svg' in logo_letter and not logo_text) else ('logo-mark' if '<svg' in logo_letter else 'logo-mark logo-letter')

        # Title slide (first slide) gets hero treatment — vertically centered
        if i == 0:
            # Convert H1 to hero-title and first paragraph to hero-subtitle
            section_html = re.sub(
                r'<h1[^>]*>(.*?)</h1>',
                r'<div class="hero-title">\1</div>',
                section_html, count=1, flags=re.DOTALL
            )
            # Convert first <p> after hero-title to hero-subtitle
            section_html = re.sub(
                r'(</div>\s*(?:<[^p].*?)*?)(<p>)(.*?)(</p>)',
                r'\1<p class="hero-subtitle">\3</p>',
                section_html, count=1, flags=re.DOTALL
            )
            slide = f'''<div class="slide{active_class}" data-slide="{i+1}" data-title="{label_text}">
<div class="brand-bar">
<div class="brand-logo">
<div class="{logo_class}">{logo_letter}</div>
<span class="logo-text">{logo_text}</span>
</div>
<span class="section-label">{label_text}</span>
</div>
<div style="flex: 1; display: flex; flex-direction: column; justify-content: center; position: relative; z-index: 1;">
{section_html}
</div>
</div>'''
        else:
            slide = f'''<div class="slide{active_class}" data-slide="{i+1}" data-title="{label_text}">
<div class="brand-bar">
<div class="brand-logo">
<div class="{logo_class}">{logo_letter}</div>
<span class="logo-text">{logo_text}</span>
</div>
<span class="section-label">{label_text}</span>
</div>
{section_html}
</div>'''
        # Phantom-empty-slide fix: a `---` adjacent to a heading/blank line can yield
        # a section whose body is empty once tags are stripped. Drop it rather than
        # emit an empty `.slide`. The title slide (i == 0) and any slide carrying an
        # SVG/image are always kept (an SVG strips to empty text but is real content).
        if i != 0 and '<svg' not in section_html and '<img' not in section_html:
            text_only = re.sub(r'<[^>]+>', '', section_html).strip()
            if not text_only:
                continue
        slides_html_parts.append(slide)

    # Close last section group
    if current_group_name is not None:
        section_groups.append({
            'name': current_group_name,
            'start': current_group_start,
            'end': len(sections) - 1
        })

    # If no groups detected, create a single group
    if not section_groups:
        section_groups = [{'name': title[:20], 'start': 0, 'end': len(sections) - 1}]

    # Format sections JSON for JS
    sections_json = _json.dumps(section_groups)

    # Count ACTUALLY-EMITTED content slides (phantom-empty slides were skipped above),
    # so the initial counter / jump-input max match the DOM. Runtime nav JS recomputes
    # from document.querySelectorAll('.slide').length, so this only affects pre-JS text.
    num_slides = len(slides_html_parts)
    html = MOBILE_HTML_TEMPLATE.format(
        title=title,
        favicon=favicon_html,
        html_lang='he' if is_rtl else 'en',
        html_dir=' dir="rtl"' if is_rtl else '',
        html_theme_class=' class="theme-light"' if theme == 'light' else '',
        primary_color=primary_color,
        accent_color=accent_color,
        logo_letter=logo_letter,
        logo_text=logo_text,
        logo_class='logo-mark logo-wide' if ('<svg' in logo_letter and not logo_text) else ('logo-mark' if '<svg' in logo_letter else 'logo-mark logo-letter'),
        slides_html='\n'.join(slides_html_parts),
        sections_json=sections_json,
        num_sections=num_slides,
        num_slides_display=f'1 / {num_slides}'
    )

    # Inject the scoped light-theme override block (before </style>) for light brands.
    # Done post-format (not via .format()) because the CSS contains literal { } braces.
    if theme == 'light':
        html = html.replace('</style>\n</head>', f'{LIGHT_THEME_CSS}\n</style>\n</head>')

    # Inject footnote CSS ONLY when this deck actually rendered footnotes — keeps
    # footnote-free decks byte-identical to the pre-change handler.
    if getattr(_apply_footnotes_and_crossrefs, 'footnotes_rendered', False):
        html = html.replace('</style>\n</head>', f'{FOOTNOTE_CSS}\n</style>\n</head>')

    # Inject the readability scale override ONLY when --font-scale was passed.
    # Additive and opt-in, so every deck rendered without the flag stays
    # byte-identical to the pre-change handler. Scales reader-facing type
    # (body, list items, tables, blockquotes) and leaves chrome — nav bar,
    # brand mark, slide-title header — untouched so layout does not shift.
    if font_scale and abs(float(font_scale) - 1.0) > 0.001:
        s = float(font_scale)
        scale_css = f'''
/* Readability scale (--font-scale {s}) — reader-facing type only */
.slide p, .slide li {{ font-size: {round(0.95 * s, 3)}rem !important; line-height: 1.75 !important; }}
@media (min-width: 768px) {{
  .slide p, .slide li {{ font-size: {round(1.05 * s, 3)}rem !important; }}
}}
.slide table {{ font-size: {round(0.82 * s, 3)}rem !important; }}
@media (min-width: 768px) {{
  .slide table {{ font-size: {round(0.88 * s, 3)}rem !important; }}
}}
.slide blockquote, .slide blockquote p {{ font-size: {round(1.0 * s, 3)}rem !important; }}
.slide h2 {{ font-size: {round(1.4 * s, 3)}rem !important; }}
@media (min-width: 768px) {{ .slide h2 {{ font-size: {round(1.8 * s, 3)}rem !important; }} }}
@media (min-width: 1200px) {{ .slide h2 {{ font-size: {round(36 * s)}px !important; }} }}
.slide h3 {{ font-size: {round(1.1 * s, 3)}rem !important; }}
@media (min-width: 768px) {{ .slide h3 {{ font-size: {round(1.3 * s, 3)}rem !important; }} }}

/* Scaling type makes some slides taller than the viewport. The default template
   pins html/body to 100% height and hides the scrollbar, so overflowing content
   becomes unreachable. Release the height pin, restore a visible scrollbar, and
   reserve space above the fixed nav bar for scaled decks only. */
html, body {{
  height: auto !important;
  min-height: 100%;
  overflow-y: auto !important;
  scrollbar-width: thin !important;
  -ms-overflow-style: auto !important;
}}
html::-webkit-scrollbar, body::-webkit-scrollbar {{ display: block !important; width: 10px; }}
html::-webkit-scrollbar-thumb, body::-webkit-scrollbar-thumb {{
  background: rgba(255,255,255,0.30); border-radius: 5px;
}}
html::-webkit-scrollbar-track, body::-webkit-scrollbar-track {{ background: rgba(255,255,255,0.05); }}
.slide {{ padding-bottom: 104px !important; }}
'''
        html = html.replace('</style>\n</head>', f'{scale_css}\n</style>\n</head>')

    # Public mode: strip the Review slide, keeping a hidden stub with the element IDs
    # the bottom script reads at init (feedbackList/emptyState/generalFeedback/outputPreview/
    # previewToggle) so navigation JS keeps working. commentBadge stays in the nav bar
    # (renders empty with zero comments).
    if not commenting:
        start = html.find('<!-- Review Slide -->')
        end = html.find('<div class="nav-bar">')
        if start != -1 and end != -1 and end > start:
            stub = ('<div style="display:none" aria-hidden="true">'
                    '<div id="feedbackList"><div class="empty-state" id="emptyState"></div></div>'
                    '<textarea id="generalFeedback"></textarea>'
                    '<pre id="outputPreview"></pre>'
                    '<button id="previewToggle"></button>'
                    '</div>\n\n')
            html = html[:start] + stub + html[end:]
        html = html.replace('<span class="comment-badge" id="commentBadge" onclick="window.goToReview()"></span>', '')

    return html, num_slides


def _split_html_into_blocks(html: str) -> list:
    """Split HTML into individual block-level elements for granular commenting.

    Returns list of (html_block, label) tuples.
    """
    # Match top-level block elements
    block_pattern = re.compile(
        r'(<(?:h[1-4]|p|ul|ol|pre|blockquote|hr|div\s+class="table-container"|svg)[^>]*>[\s\S]*?</(?:h[1-4]|p|ul|ol|pre|blockquote|div|svg)>|<hr[^>]*>)',
        re.IGNORECASE
    )
    # Walk matches and PRESERVE bare text between blocks (lead-in lines, converter
    # quirks) as <p> blocks — findall-style collection silently dropped that text
    blocks = []
    pos = 0

    def _gap_to_block(fragment):
        # Strip stray structural open/close tags left by broken nesting; keep inline content
        cleaned = re.sub(r'</?(?:p|ul|ol|div)[^>]*>', '', fragment).strip()
        if cleaned:
            blocks.append(f'<p>{cleaned}</p>')

    for m in block_pattern.finditer(html):
        _gap_to_block(html[pos:m.start()])
        blocks.append(m.group(0))
        pos = m.end()
    _gap_to_block(html[pos:])

    if not blocks:
        # Fallback: treat the whole thing as one block
        return [(html, "Content")]

    result = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Derive a label from the block content
        label = "Content"
        if block.startswith('<h1'):
            text = re.sub(r'<[^>]+>', '', block).strip()
            label = text[:60]
        elif block.startswith('<h2'):
            text = re.sub(r'<[^>]+>', '', block).strip()
            label = text[:60]
        elif block.startswith('<h3'):
            text = re.sub(r'<[^>]+>', '', block).strip()
            label = text[:60]
        elif block.startswith('<h4'):
            text = re.sub(r'<[^>]+>', '', block).strip()
            label = text[:60]
        elif block.startswith('<pre'):
            label = "Code block"
        elif block.startswith('<p'):
            text = re.sub(r'<[^>]+>', '', block).strip()
            label = (text[:50] + '...') if len(text) > 50 else text
        elif block.startswith('<ul') or block.startswith('<ol'):
            # Get first list item text
            first_li = re.search(r'<li[^>]*>(.*?)</li>', block, re.DOTALL)
            if first_li:
                text = re.sub(r'<[^>]+>', '', first_li.group(1)).strip()
                label = (text[:40] + '... (list)') if len(text) > 40 else text
            else:
                label = "List"
        elif block.startswith('<div class="table-container"'):
            label = "Table"
        elif block.startswith('<pre'):
            label = "Code block"
        elif block.startswith('<blockquote'):
            text = re.sub(r'<[^>]+>', '', block).strip()
            label = (text[:50] + '...') if len(text) > 50 else text
        elif block.startswith('<hr'):
            continue  # Skip horizontal rules, not commentable

        # Escape label for HTML attribute (single-line, collapsed whitespace)
        label = re.sub(r'\s+', ' ', label).strip()
        label = label.replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
        result.append((block, label))

    return result if result else [(html, "Content")]


def md_to_commentable_html(md_content: str, title: str) -> tuple:
    """Convert markdown to commentable presentation (prototype-style dark slides + scroll mode).

    Uses COMMENTABLE_HTML_TEMPLATE which provides:
    - Dark slide-based presentation with topbar, progress pips, side arrows
    - Scroll/Slides mode picker in topbar
    - Both modes render the same content differently

    Each block element (heading, paragraph, list, table, etc.) within a slide
    is individually commentable.

    The commenting engine (JS/CSS) is injected inline.
    """
    sections = split_into_sections(md_content)

    # Read engine files for inline injection
    engine_css = ""
    engine_js = ""
    if COMMENTABLE_ENGINE_CSS.exists():
        with open(COMMENTABLE_ENGINE_CSS, 'r', encoding='utf-8') as f:
            engine_css = f.read()
    if COMMENTABLE_ENGINE_JS.exists():
        with open(COMMENTABLE_ENGINE_JS, 'r', encoding='utf-8') as f:
            engine_js = f.read()

    # Build slides HTML — each block element within a slide is individually commentable
    slides_parts = []
    for i, section in enumerate(sections):
        section_html = convert_md_to_html(section)
        heading_match = re.search(r'^#{1,3}\s+(.+)$', section, re.MULTILINE)
        slide_title = heading_match.group(1) if heading_match else f'Section {i+1}'
        slide_title_attr = slide_title.replace('"', '&quot;').replace('<', '&lt;')

        # Split into individual commentable blocks
        blocks = _split_html_into_blocks(section_html)
        blocks_html = []
        for j, (block_html, label) in enumerate(blocks):
            section_id = f"s{i+1}-{j+1}"
            blocks_html.append(
                f'        <div class="commentable" data-section="{section_id}" data-label="{label}">\n'
                f'          {block_html}\n'
                f'        </div>'
            )

        slides_parts.append(
            f'    <div class="slide" data-slide="{i+1}" data-title="{slide_title_attr}">\n'
            f'      <div class="slide-inner">\n'
            + '\n'.join(blocks_html) + '\n'
            f'      </div>\n'
            f'    </div>'
        )

    # Build scroll sections HTML — same granular blocks
    scroll_parts = []
    for i, section in enumerate(sections):
        section_html = convert_md_to_html(section)
        heading_match = re.search(r'^#{1,3}\s+(.+)$', section, re.MULTILINE)
        slide_title = heading_match.group(1) if heading_match else f'Section {i+1}'
        slide_title_attr = slide_title.replace('"', '&quot;').replace('<', '&lt;')

        blocks = _split_html_into_blocks(section_html)
        blocks_html = []
        for j, (block_html, label) in enumerate(blocks):
            section_id = f"s{i+1}-{j+1}"
            blocks_html.append(
                f'    <div class="commentable" data-section="{section_id}" data-label="{label}">\n'
                f'      {block_html}\n'
                f'    </div>'
            )

        scroll_parts.append(
            f'  <section class="section" id="scroll-section-{i+1}">\n'
            + '\n'.join(blocks_html) + '\n'
            f'  </section>'
        )

    # Escape title for JS string
    js_title = title.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')

    # Build the full HTML using the template
    html = COMMENTABLE_HTML_TEMPLATE.format(
        title=title,
        slides_html='\n'.join(slides_parts),
        scroll_sections_html='\n'.join(scroll_parts),
        num_sections=len(sections)
    )

    # Inject commenting engine CSS into the <style> block (before </style>)
    if engine_css:
        comment_css = f'\n/* ── Commentable Engine ── */\n{engine_css}'
        html = html.replace('</style>\n</head>', f'{comment_css}\n</style>\n</head>')

    # Inject commenting engine config + JS before </body>
    config_and_js = f'''
<script>
window.CommentableConfig = {{
  documentName: '{js_title}',
  selector: '.commentable',
  layout: 'slide',
  persistence: 'localStorage',
  showReviewSlide: true,
  enableExport: true
}};
</script>
<script>
{engine_js}
</script>'''
    html = html.replace('</body>', f'{config_and_js}\n</body>')

    return html, len(sections)


# ── Main Handler ──────────────────────────────────────────────────────────────

def is_complete_html(content: str) -> bool:
    """Check if content is already a complete HTML document (not markdown)."""
    stripped = content.strip()
    return (stripped.startswith('<!DOCTYPE html>') or stripped.startswith('<!doctype html>') or
            (stripped.startswith('<html') and '</html>' in stripped))


def extract_html_title(content: str, fallback: str) -> str:
    """Extract title from HTML <title> tag or <h1>."""
    title_match = re.search(r'<title>([^<]+)</title>', content)
    if title_match:
        return title_match.group(1)
    h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if h1_match:
        return h1_match.group(1)
    return fallback


def handle_agent_output(md_path: Path, options: dict) -> dict:
    """Process agent output file."""
    result = {
        "md_file": str(md_path),
        "html_file": None,
        "sections": 0,
        "md_drive_link": None,
        "html_drive_link": None,
        "telegram_sent": False
    }

    # Read content
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Secret-detection guard. Halt before any HTML is generated or published
    # if known API-key patterns appear in the source. Override with
    # --allow-secrets in options (legitimate cases: runbooks documenting
    # what to rotate, security post-mortems).
    if not options.get("allow_secrets"):
        findings = scan_content_for_secrets(content)
        if findings:
            print(f"\nSECRET-DETECTION GUARD HALT: {len(findings)} potential secret(s) found in {md_path}", file=sys.stderr)
            print("=" * 78, file=sys.stderr)
            for f in findings:
                print(f"  [{f['pattern_name']}] line {f['line_number']}: {f['match']}", file=sys.stderr)
                print(f"    {f['line_excerpt']}", file=sys.stderr)
            print("=" * 78, file=sys.stderr)
            print("If this is a legitimate documentation use (e.g., describing what to", file=sys.stderr)
            print("rotate), re-run with --allow-secrets. Otherwise, scrub the secret", file=sys.stderr)
            print("from the source file and rotate the credential.", file=sys.stderr)
            sys.exit(2)

    # Create presentations directory
    PRESENTATIONS_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    # Detect if input is already a complete HTML presentation
    if is_complete_html(content):
        # HTML passthrough: copy to presentations/ and open directly
        title = extract_html_title(content, md_path.stem)
        html_content = content

        # Count slides or sections for reporting
        slide_count = len(re.findall(r'data-slide=', content))
        section_count = len(re.findall(r'<section', content))
        num_sections = slide_count or section_count or 1

        # Inject commentable layer if requested
        if options.get("commentable"):
            layout = "slide" if slide_count > 0 else "scroll"
            html_content = inject_commentable_layer(html_content, title, layout)
            print(f"Commentable layer injected (layout: {layout})")

        _out = options.get("output")
        html_filename = (_out if _out.lower().endswith(".html") else _out + ".html") if _out else f"{md_path.stem}-{timestamp}.html"
        html_path = PRESENTATIONS_DIR / html_filename

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        result["html_file"] = str(html_path)
        result["sections"] = num_sections

        print(f"HTML passthrough: {html_path} ({num_sections} slides)")
    else:
        # Markdown processing: convert to HTML presentation
        # Extract title from first H1 or filename
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else md_path.stem

        if options.get("commentable"):
            # Use prototype-style commentable presentation
            html_content, num_sections = md_to_commentable_html(content, title)
            print(f"Commentable presentation created ({num_sections} slides)")
        else:
            # Standard mobile-friendly scroll presentation
            html_content, num_sections = md_to_mobile_html(content, title, brand_override=options.get("brand"), commenting=not options.get("no_comments"), font_scale=options.get("font_scale"))

        # Save presentation
        _out = options.get("output")
        html_filename = (_out if _out.lower().endswith(".html") else _out + ".html") if _out else f"{md_path.stem}-{timestamp}.html"
        html_path = PRESENTATIONS_DIR / html_filename

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        result["html_file"] = str(html_path)
        result["sections"] = num_sections

        print(f"Created presentation: {html_path} ({num_sections} sections)")

    # Get Drive links
    if not options.get("no_drive"):
        # Wait a moment for Drive sync
        time.sleep(1)

        md_link = get_drive_link(md_path)
        html_link = get_drive_link(html_path)

        if md_link:
            result["md_drive_link"] = md_link
        if html_link:
            result["html_drive_link"] = html_link

    # Open in browser
    if not options.get("no_browser"):
        open_in_browser(html_path)
        print("Opened in browser")

    # Send Telegram notification
    if not options.get("no_telegram"):
        config = load_config()

        message = f"📊 *Deliverable Ready*\n\n"
        message += f"*{title}*\n"
        message += f"Sections: {num_sections}\n\n"

        # Add Drive links
        if result["md_drive_link"] and result["md_drive_link"].startswith("http"):
            message += f"📄 [View MD]({result['md_drive_link']})\n"
        else:
            message += f"📄 MD: `{md_path.name}`\n"

        if result["html_drive_link"] and result["html_drive_link"].startswith("http"):
            message += f"📱 [View Presentation]({result['html_drive_link']})\n"
        else:
            message += f"📱 HTML: `{html_filename}`\n"

        message += "\n_Claude Code_"

        if send_telegram(message, config):
            result["telegram_sent"] = True
            print("Telegram notification sent")

    return result


# ── Commentable Layer ─────────────────────────────────────────────────────────

def inject_commentable_layer(html: str, title: str, layout: str = "scroll") -> str:
    """Inject the commentable engine into an HTML presentation.

    Reads commentable-engine.js and commentable-engine.css from the presentations
    directory, adds .commentable class to each .section div, and injects the
    engine with localStorage persistence.
    """
    # Read engine files
    if not COMMENTABLE_ENGINE_JS.exists() or not COMMENTABLE_ENGINE_CSS.exists():
        print("Warning: commentable engine files not found, skipping injection")
        return html

    with open(COMMENTABLE_ENGINE_CSS, 'r', encoding='utf-8') as f:
        engine_css = f.read()
    with open(COMMENTABLE_ENGINE_JS, 'r', encoding='utf-8') as f:
        engine_js = f.read()

    # Add .commentable class to each .section div (for scroll-based presentations)
    # Also add data-section and data-label attributes
    section_pattern = re.compile(r'<section\s+class="section"\s+id="(section-\d+)">')
    section_count = 0

    def add_commentable_class(match):
        nonlocal section_count
        section_count += 1
        section_id = match.group(1)
        return f'<section class="section commentable" id="{section_id}" data-section="{section_id}" data-label="Section {section_count}">'

    html = section_pattern.sub(add_commentable_class, html)

    # Escape title for JS string
    js_title = title.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')

    # Build config script
    config_script = f'''
<script>
window.CommentableConfig = {{
  documentName: '{js_title}',
  selector: '.commentable',
  layout: '{layout}',
  persistence: 'localStorage',
  showReviewSlide: true,
  enableExport: true
}};
</script>'''

    # Inject CSS into <head>
    css_injection = f'\n<style>\n/* Commentable Engine */\n{engine_css}\n</style>'
    html = html.replace('</head>', f'{css_injection}\n</head>')

    # Inject config + engine JS before </body>
    js_injection = f'{config_script}\n<script>\n{engine_js}\n</script>'
    html = html.replace('</body>', f'{js_injection}\n</body>')

    return html


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Process agent output into mobile-friendly presentations")
    parser.add_argument("md_file", help="Path to markdown file")
    parser.add_argument("--no-telegram", action="store_true", help="Skip Telegram notification")
    parser.add_argument("--no-browser", action="store_true", help="Don't open in browser")
    parser.add_argument("--no-drive", action="store_true", help="Skip Drive link lookup")
    parser.add_argument("--json", action="store_true", help="Output result as JSON")
    parser.add_argument("--commentable", action="store_true", help="Inject commenting layer for review/feedback")
    parser.add_argument("--allow-secrets", action="store_true", help="Bypass the secret-detection guard (use for legitimate doc cases — e.g. runbooks describing what to rotate)")
    parser.add_argument("--brand", default=None, help="Force brand detection (e.g. 'productbeacon', 'product-org-os') instead of inferring from the title")
    parser.add_argument("--output", default=None, help="Static output filename (e.g. 'my-deck.html') instead of the default timestamped name")
    parser.add_argument("--no-comments", action="store_true", help="Public mode: no commentable wrappers, no Review slide (for externally published decks)")
    parser.add_argument("--font-scale", type=float, default=None, help="Scale reader-facing type for readability (e.g. 1.2 = 20%% larger). Opt-in: omit for byte-identical default output")

    args = parser.parse_args()

    md_path = Path(args.md_file)
    if not md_path.exists():
        print(f"Error: File not found: {md_path}", file=sys.stderr)
        sys.exit(1)

    options = {
        "no_telegram": args.no_telegram,
        "no_browser": args.no_browser,
        "no_drive": args.no_drive,
        "commentable": args.commentable,
        "allow_secrets": args.allow_secrets,
        "brand": args.brand,
        "output": args.output,
        "no_comments": args.no_comments,
        "font_scale": args.font_scale,
    }

    result = handle_agent_output(md_path, options)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"\nDone! Mobile-friendly presentation ready.")


if __name__ == "__main__":
    main()
