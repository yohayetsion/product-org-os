---
name: vision-to-value-document-map
description: 'Generate a branded Vision to Value Document Map for a product — a visual index of all strategic assets organized by the 6 Vision to Value phases, with links to both MD source and HTML presentation
  for each asset. Also resolves historical principle names (e.g., "Customer Obsession", "Strategic Clarity", "Collaborative Excellence") to their current canonical equivalents in the Vision to Value 8-principle
  set, so a query for an old name redirects cleanly to the current principle. Activate when: "document map", "vision to value map", "strategic asset map", "show all documents for [product]", "what documents
  do we have", "what happened to [old principle name]", "where did Customer Obsession go", "principle rename", "principle reconciliation". Do NOT activate for: creating individual documents (/prd, /strategic-bet,
  etc.), portfolio status (/portfolio-status), phase check (/phase-check)'
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

## Principle Name Reconciliation

The Vision to Value operating principles evolved during the v5.1 reconciliation pass against the Vision to Value book canon. Earlier OS versions used principle names that no longer exist as standalone entries. When a user searches the document map for a historical principle name, resolve it through the table below and present the current canonical equivalent rather than failing silently.

### Historical → Canonical Mapping

| Historical Name (pre-v5.1) | Current Canonical Principle | Notes |
|----------------------------|------------------------------|-------|
| Customer Obsession | Principle 2: Strategy Precedes Structure (closest substantive overlap) | The customer-obsession concern is no longer a standalone principle. Customer-value reasoning is captured operationally via `/customer-value-trace` and structurally through Phase 5 (Business & Customer Outcomes). The strategic framing — that organizations exist to create customer value — lives in the Philosophy preamble, not as a separate principle. |
| Strategic Clarity | Principle 2: Strategy Precedes Structure (closest current principle) | Folded into the broader strategic-intent and commitment chain across Principles 2, 3, and 5. The "clarity" framing was redundant with strategy-as-input across the principle set. |
| Collaborative Excellence | Principle 4: Alignment Beats Consensus | Same slot in the principle order, evolved framing. The new statement separates input from ownership, normalizes "disagree and commit," and treats consensus as a stall pattern rather than a goal. |

### Current Canonical 8-Principle Order

This is the single source of truth. The skill MUST surface this order when reconciling principle names.

| # | Principle | One-Line Statement | Vision to Value Book Reference |
|---|-----------|--------------------|--------------------------------|
| 1 | End-to-End Ownership | Product organization is accountable from strategy through outcomes. | Vision to Value, Part I — Foundations |
| 2 | Strategy Precedes Structure | Structure is an execution tool, not a starting point; roles, teams, and reporting lines reflect strategic intent. | Vision to Value, Part I — Foundations |
| 3 | Decision Quality | Decision quality is the core metric for product leadership effectiveness. | Vision to Value, Part II — Decision Systems |
| 4 | Alignment Beats Consensus | Optimize for shared understanding and commitment, not universal agreement. | Vision to Value, Part II — Decision Systems |
| 5 | GTM Is a Strategic Choice | Go-to-market is a strategic decision surface co-decided with product scope, not a downstream handoff. | Vision to Value, Part III — Commercial Architecture |
| 6 | Outcome Focus | Success is measured by results, not outputs. | Vision to Value, Part IV — Outcomes |
| 7 | Scalable Systems | Processes that work as the organization grows. | Vision to Value, Part V — Scaling |
| 8 | Continuous Learning | Systematic capture and application of learnings. | Vision to Value, Part V — Scaling |

### Resolution Behavior

When a user queries the document map with a historical principle name:

1. Look up the name in the Historical → Canonical Mapping table
2. Surface a clear redirect message: "The principle '[historical name]' was reconciled in v5.1. The closest current canonical principle is '[current name]' (Principle [N])."
3. If the historical concept is partially captured by a different mechanism (e.g., Customer Obsession → `/customer-value-trace` + Phase 5), surface that mechanism so the user can find the operational equivalent
4. Always ground the response in `PRINCIPLES.md` as the live source of truth — the table above is a navigation aid, not the authoritative principle text

### When This Path Activates

- User invokes the skill with a historical principle name as the argument: `/vision-to-value-document-map "Customer Obsession"`
- User asks "what happened to [historical principle name]" or "where did [name] go"
- User searches a product's document map for content tagged against a historical principle name
- A document or agent reference points at a historical principle name and the user is reconciling it against the current canon

The redirect should be a short, navigable answer — not a defense of the rename. The user needs to find what they were looking for; they do not need a justification of why the principle set changed.

---

## Phase-Count Reconciliation (6-phase OS ↔ 5-phase pipeline ↔ 3-phase strategic process)

The Vision to Value world uses three different phase counts at three different altitudes. A user who learned the book's 5-phase pipeline shape may search the OS for the wrong surface and not find what they expect; a user who learned the 3-phase strategic process may look for sub-divisions that do not exist at the highest altitude. This section maps the three counts to each other so navigation is unambiguous.

### Why three counts exist

The three phase counts are not contradictions — they are the same shape viewed at different altitudes. The 6-phase OS terminology is the operational surface (the level at which a Product Org executes day-to-day). The 5-phase pipeline is the executable backbone described in the Vision to Value book (the level at which the methodology is taught). The 3-phase strategic process is the highest altitude (the level at which executive sponsors think about a bet from intent to commitment). Each altitude is correct for its scope; the OS chose the 6-phase operational surface because that is the level a Product Org actually runs at.

### Canonical 6-phase OS surface (this is the live OS)

This is the single source of truth for the OS today. All `/phase-check`, `/portfolio-status`, and gate-firing logic in v5.0 and v5.1 use this 6-phase surface.

| Phase | Name | Key Question |
|-------|------|--------------|
| 1 | Strategic Foundation | "Where should we play?" |
| 2 | Strategic Decisions | "Is this viable?" |
| 3 | Strategic Commitments | "Are we committed?" |
| 4 | Coordinated Execution | "Are we ready to execute?" |
| 5 | Business & Customer Outcomes | "Did it work?" |
| 6 | Learning Loop | "What did we learn?" |

### 5-phase pipeline ↔ 6-phase OS mapping

The Vision to Value book describes an executable 5-phase pipeline that integrates the Learning Loop cross-phase rather than as a discrete terminal phase. Mapping the 5 to the 6:

| 5-phase Pipeline | 6-phase OS | Notes |
|------------------|------------|-------|
| Strategy | Phase 1: Strategic Foundation | Direct map. Where should we play? — vision, market analysis, competitive landscape, target segments. |
| Decisions | Phase 2: Strategic Decisions | Direct map. Is this viable? — business case, pricing, positioning, decision records, the commercial filter. |
| Commitments | Phase 3: Strategic Commitments | Direct map. Are we committed? — roadmap, GTM, PRDs, commitment-check, the point of no return. |
| Execution | Phase 4: Coordinated Execution | Direct map. Are we ready to execute? — campaign brief, sales enablement, readiness check, stakeholder briefs. |
| Realization | Phase 5: Business & Customer Outcomes | Direct map. Did it work? — onboarding, value-realization tracking, customer health, success metrics. |
| (cross-phase Learning Loop) | Phase 6: Learning Loop | The pipeline integrates learning continuously across all five phases; the OS surfaces it as an explicit Phase 6 (outcome reviews, retrospectives, context-save) so the loop has a named home for assets. |

The 5-phase pipeline reader looking for "Realization" should land on Phase 5 in the OS. The 5-phase reader looking for the Learning Loop should land on Phase 6 (the OS surfaces it discretely; the book describes it cross-phase — both are correct).

### 3-phase strategic process ↔ 6-phase OS mapping

The 3-phase strategic process is the executive-altitude shape of the same flow — the level at which a sponsor thinks "from strategic intent through bets through commitments." Mapping the 3 to the 6:

| 3-phase Strategic Process | 6-phase OS Coverage | Notes |
|---------------------------|----------------------|-------|
| Strategic Intent | Phase 1: Strategic Foundation | The "where should we play" altitude. Vision, market shape, target segments. |
| Strategic Bets | Phase 2: Strategic Decisions | The "is this viable" altitude. Business case, strategic-bet formulation, named re-decision triggers, continuation threshold declaration. |
| Strategic Commitments | Phase 3: Strategic Commitments | The "are we committed" altitude. Five Signals checklist, point-of-no-return commitment-check, capital envelope locked. |

The 3-phase reader looking for the executive altitude lands at Phases 1-3 of the OS. Phases 4-6 (Execution, Outcomes, Learning Loop) are below the 3-phase strategic process altitude — they are the operational follow-through that the executive process commits to but does not directly own at the strategic level.

### Quick-reference cross-walk

| If you learned … | Look in OS Phase … |
|------------------|--------------------|
| "Realization" (5-phase) | Phase 5: Business & Customer Outcomes |
| "Strategic Bets" (3-phase) | Phase 2: Strategic Decisions |
| "Strategic Commitments" (3-phase) | Phase 3: Strategic Commitments |
| "Learning Loop" (5-phase or 3-phase) | Phase 6: Learning Loop (operational home) — also surfaced cross-phase in feedback / context skills |
| "Decisions" (5-phase) | Phase 2: Strategic Decisions |

### v6.0 revisit note

The 6-phase OS terminology may be revisited in v6.0 based on production usage. Specifically: if v5.2 production data shows the 6-phase schema is creating navigation friction (users searching for the book's 5-phase terms not finding the right OS surfaces, or searching for the executive 3-phase shape not landing at Phases 1-3 cleanly), v6.0 could collapse the OS to the 5-phase pipeline shape with the Learning Loop integrated cross-phase rather than as a discrete Phase 6. For now (v5.x), the 6-phase apparatus is canonical and the 5-phase / 3-phase mappings live here for navigation only.

The reason this question is parked rather than resolved in v5.1 is that the cost of changing the operational phase count is high (every `/phase-check`, every gate, every audit reference re-anchors) and the evidence base is currently thin — production usage of v5.0 and v5.1 will tell us whether the friction is real. If v5.2 ships and the mapping table above is the destination users keep landing on, the 6-phase shape is doing its job and the question stays parked. If users keep getting lost between the surfaces, v6.0 reopens the schema.

---

## Vision to Value Operating Principle

> "A product without a document map is navigating without a compass. The map doesn't create the territory — but it makes the territory navigable."
