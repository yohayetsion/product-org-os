---
name: vision-to-value-document-map
description: 'Generate a branded Vision to Value Document Map for a product — a visual index of all strategic assets organized by the 6 Vision to Value phases, with links to both MD source and HTML presentation
  for each asset. Activate when: "document map", "vision to value map", "strategic asset map", "show all documents for [product]", "what documents do we have" Do NOT activate for: creating individual documents
  (/prd, /strategic-bet, etc.), portfolio status (/portfolio-status), phase check (/phase-check)'
argument-hint: '[product name] — e.g., "AXIA", "Legionis"'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: cross-phase
  owner: product-operations
  skill_type: task-capability
  primary_consumers:
  - vp-product
---
## Purpose

Creates a per-product visual index of all strategic documents organized by Vision to Value phase. The output is both a markdown registry and a branded HTML page where each asset is a card with links to its MD source and HTML presentation.

This is the "table of contents" for a product's strategic documentation.

## When to Use

- After completing a wave of strategic document creation/updates
- During onboarding to understand a product's strategic state
- As a living reference page that gets updated as documents evolve
- During portfolio reviews to see completeness across Vision to Value phases

## Process

### Step 1: Inventory Strategic Assets

For the target product, scan for documents across the Vision to Value phases:

| Phase | What to Look For | Typical Locations |
|-------|-----------------|-------------------|
| 1. Strategic Foundation | Vision, strategic intent, market analysis, competitive landscape, market segment | `{Product}/Product/` |
| 2. Strategic Decisions | Positioning, pricing, business case, strategic bets, decision records | `{Product}/Product/`, `{Product}/Marketing/` |
| 3. Strategic Commitments | PRD, roadmap, GTM strategy, launch plan | `{Product}/Product/`, `{Product}/Marketing/` |
| 4. Coordinated Execution | Website (live), brand guide, campaigns, sales enablement | `{Product}/Marketing/`, live URLs |
| 5. Business Outcomes | Onboarding playbook, value realization, customer health | `{Product}/Product/` |
| 6. Learning & Adaptation | Feedback, retrospectives, outcome reviews | `{Product}/Product/` |

**Rules:**
- Only include the **latest version** of each asset (no old PRD versions)
- Remove supporting/superseded documents
- Include live websites as Phase 4 assets
- Note registered IDs (DOC-YYYY-NNN, SB-YYYY-NNN, DR-YYYY-NNN)

### Step 2: Verify HTML Presentations Exist

For each strategic asset found:
1. Check if a corresponding HTML presentation exists (in the product folder or `C:\dev\presentations\`)
2. If missing, generate it: `python "G:\My Drive\Claude\agent-output-handler.py" "<md-path>" --no-telegram --no-browser`
3. Record the HTML path for linking

### Step 3: Generate Markdown Registry

Create `{Product}/Product/vision-to-value-document-map.md` with:
- Table per phase listing: Document name, version, date, registry ID, location
- Bottom sections: Active Assumptions, Active Decisions, Active Bets

### Step 4: Generate Branded HTML Map

Use the Vision to Value document map generator script at:
```
G:\My Drive\Claude\vision-to-value-document-map-generator.py
```

The HTML must include:
- **Product branding**: Logo, favicon, and color theme from the product's live website
- **Vertical Vision to Value flow**: 6 phase boxes stacked vertically with downward arrows
- **Labeled transitions**: "Commercial Filter" between Phase 2-3, "Point of No Return" between Phase 3-4
- **Asset cards**: Each document is a card with title, version badge, registry ID badge, and MD/HTML link buttons
- **Live website cards**: Green "LIVE" badge with clickable URL
- **Sidebars**: Operating Principles (left), Organizational Structure (right)
- **Bottom sections**: Assumptions, Decisions, Bets
- **No commenting engine** — this is a reference page, not a deliverable presentation
- **Responsive**: Sidebars collapse on mobile

### Step 5: Open in Browser

Open the HTML for review. The map should be a clean, branded reference page.

## Brand Configuration

Each product needs a brand config:

| Property | Description | Example (AXIA) | Example (Legionis) |
|----------|-------------|-----------------|---------------------|
| `primary` | Main brand color | `#0D9488` (teal) | `#6366F1` (indigo) |
| `primary_light` | Lighter variant | `#14B8A6` | `#818CF8` |
| `accent` | Secondary color | `#22D3EE` (cyan) | `#d97706` (amber) |
| `bg` | Page background | `#0D1117` | `#1c1917` |
| `bg_card` | Card background | `#161B22` | `#292524` |
| `favicon` | From live website | axiasecurity.io favicon | legionis.ai favicon |
| `logo` | From live website | axiasecurity.io apple-touch-icon | legionis.ai SVG icon |

**To extract brand assets from a live website:**
```bash
curl -s https://example.com/ | python3 -c "
import sys, re
html = sys.stdin.read()
for m in re.finditer(r'<link[^>]*rel=\"(icon|apple-touch-icon)\"[^>]*href=\"(data:[^\"]+)\"', html):
    print(f'{m.group(1)}: {m.group(2)[:80]}...')
"
```

## Card Types

| Card Type | CSS Class | Left Border | Used For |
|-----------|-----------|-------------|----------|
| Registered DOC | `reg` | Brand primary | Documents with DOC-YYYY-NNN IDs |
| Strategic Bet | `reg-sb` | Amber `#f59e0b` | Documents with SB-YYYY-NNN IDs |
| Decision Record | `reg-dr` | Blue `#3b82f6` | Documents with DR-YYYY-NNN IDs |
| Live Website | `live` | Green `#10b981` | Production websites |
| Unregistered | (none) | Default border | Supporting documents without registry IDs |

## Link Buttons

Each asset card has up to two link buttons:
- **MD** (brand-colored pill): Links to the markdown source file
- **HTML** (amber pill): Links to the HTML presentation

Live website cards get a green **link pill** with the URL.

## Output Files

| File | Location | Purpose |
|------|----------|---------|
| Markdown registry | `{Product}/Product/vision-to-value-document-map.md` | Source of truth, text-searchable |
| Branded HTML map | `{Product}/Product/vision-to-value-document-map.html` | Visual reference, shareable |

## Update Protocol

When documents are added, updated, or removed:
1. Update the markdown registry
2. If new document lacks HTML presentation, generate one
3. Re-run the generator to update the HTML map
4. The HTML is the visual layer; the MD is the data layer

## Vision to Value Operating Principle

> "A product without a document map is navigating without a compass. The map doesn't create the territory — but it makes the territory navigable."
