---
name: index-folder
description: 'Index a folder''s contents into the context system for fast retrieval and discovery. Activate when: "index this folder", "catalog these files", folder contents indexed, build file index, scan
  folder Do NOT activate for: saving decisions to context (/context-save), recalling context (/context-recall)'
model: haiku
allowed-tools:
- Read
- Write
- Edit
- Glob
user-invocable: true
metadata:
  author: Product Org OS
  category: context-layer
  skill_type: task-capability
  owner: analyst
  primary_consumers:
  - prodops
  - pa
  - analyst
  secondary_consumers:
  - cs-ops
---
# Index Folder

Scan a folder and add its contents to `context/index.json` for fast topic-based retrieval.

## Trigger Patterns

- `/index-folder [path]` - Index all supported files in path
- `/index-folder [path] --recursive` - Include subfolders
- `/index-folder [path] --type [type]` - Only index specific type

## Behavior

### 1. Validate Path

Confirm the path exists and is accessible:
- Accept relative paths from project root
- Accept absolute paths
- Reject paths outside the project

### 2. Scan for Supported Files

**Supported file types:**
- `.md` - Markdown documents
- `.json` - JSON data files (skip `the package manifest`, `node_modules`)

**Always skip:**
- `node_modules/`
- `.git/`
- `__pycache__/`
- `.venv/`, `venv/`
- `dist/`, `build/`
- Files starting with `.`
- Files over 100KB (likely not documents)

### 3. Extract Metadata

For each file, extract:

```json
{
  "id": "DOC-YYYY-NNN",
  "title": "[H1 or filename]",
  "type": "[detected type]",
  "path": "[relative path]",
  "topics": ["topic1", "topic2"],
  "phase": "[Vision to Value phase if detectable]",
  "created": "[file creation date]",
  "lastAccessed": "[current date]",
  "size": "[file size]"
}
```

**Type Detection:**
| Pattern | Type |
|---------|------|
| Contains "PRD" or in `prd/` | prd |
| Contains "Decision Record" or `DR-` | decision |
| Contains "Strategic Bet" or `SB-` | bet |
| Contains "Roadmap" | roadmap |
| Contains "GTM" or "Go-to-Market" | gtm |
| Contains "Analysis" | analysis |
| Contains "Feedback" or `FB-` | feedback |
| Contains "Learning" or `L-` | learning |

**Topic Extraction:**
- Extract from document headers (H1, H2)
- Extract from tags if present in frontmatter
- Extract key nouns from first paragraph
- Limit to 5-10 topics per document

**Phase Detection:**
Look for Vision to Value phase indicators:
- "Strategic Foundation" → phase1
- "Strategic Decision" → phase2
- "Commitment" or "Roadmap" → phase3
- "Execution" or "Launch" → phase4
- "Outcome" or "Value" → phase5
- "Learning" or "Retrospective" → phase6

### 4. Update Index

Read `context/index.json` and:

1. **Add new entries** - Files not already indexed
2. **Update existing entries** - Files that have changed (by path)
3. **Update topicIndex** - Add document IDs to topic arrays
4. **Update typeIndex** - Add document IDs to type arrays
5. **Update phaseIndex** - Add document IDs to phase arrays
6. **Update lastUpdated** - Set to current date

### 5. Output Report

```markdown
# Folder Indexed: [path]

**Scanned**: [N] files
**Added**: [N] new entries
**Updated**: [N] existing entries
**Skipped**: [N] (already indexed, unchanged)

## New Entries

| ID | Title | Type | Topics |
|----|-------|------|--------|
| DOC-2026-015 | Authentication PRD | prd | auth, security, login |
| DOC-2026-016 | Pricing Decision | decision | pricing, enterprise |

## Topic Summary

| Topic | Documents |
|-------|-----------|
| authentication | 5 |
| pricing | 3 |
| enterprise | 3 |
| security | 2 |

---

*Index updated at context/index.json*
```

## Index Format

The `context/index.json` structure:

```json
{
  "version": "1.0",
  "lastUpdated": "2026-01-25",
  "entries": [
    {
      "id": "DOC-2026-001",
      "title": "Authentication PRD",
      "type": "prd",
      "path": "documents/prd-auth.md",
      "topics": ["authentication", "security", "login", "oauth"],
      "phase": "phase3",
      "created": "2026-01-15",
      "lastAccessed": "2026-01-25",
      "size": 4520
    }
  ],
  "topicIndex": {
    "authentication": ["DOC-2026-001", "DOC-2026-005"],
    "pricing": ["DOC-2026-003", "DOC-2026-007"]
  },
  "typeIndex": {
    "prd": ["DOC-2026-001"],
    "decision": ["DOC-2026-003"],
    "bet": ["DOC-2026-002"]
  },
  "phaseIndex": {
    "phase1": ["DOC-2026-010"],
    "phase2": ["DOC-2026-003"],
    "phase3": ["DOC-2026-001", "DOC-2026-005"]
  }
}
```

## ID Generation

Format: `DOC-YYYY-NNN` (YYYY = current year).

**Reserve each ID with the allocator — never by checking existing entries and adding one:**

```bash
python tools/allocate-id.py --ns DOC --note "<short reason>"
```

Use the printed id verbatim. **If it exits non-zero, do NOT guess a number** — re-run it; it refuses exactly when it cannot prove the id is free. "Check existing entries to avoid collisions" is precisely the read-then-write race that collided five ids across five namespaces on 2026-08-02 — it does not avoid collisions, it causes them, because two concurrent sessions both read the same maximum before either wrote. **This skill indexes a whole folder, so it mints many ids in one run** — call the allocator once per document, at the moment you write that row.

(Collision-safe across concurrent sessions on one machine, not across machines. If `tools/allocate-id.py` is absent from this workspace, fall back to reading the index — and verify each id is free immediately before **and after** the write.)

## Notes

- Indexing is additive - existing entries are preserved
- To remove stale entries, edit the index file directly - a dedicated cleanup skill does not exist yet
- Large folders may take time - provide progress updates
- Topics are normalized to lowercase
- Duplicate entries (same path) are updated, not duplicated
