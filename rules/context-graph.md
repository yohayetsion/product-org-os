# Context Cross-Reference Graph

Context entries are linked to each other in `context/index.json` under `crossReferences`, turning flat records into a navigable knowledge graph.

## Link Types

Decision↔Bet, Bet↔Assumption, Feedback↔Decision, Learning↔Decision, Document↔Decision/Bet, Feedback↔Theme.

## Auto-Linking

When `/context-save` or `/feedback-capture` creates entries:
1. Scan for ID references (DR-*, SB-*, FB-*, A-*, L-*, DOC-*)
2. Create bidirectional links in `crossReferences` section of context/index.json
3. For feedback: check for theme matches, update theme strength

## Query Enhancement

When `/context-recall` runs: find direct matches → follow cross-references one level (max 3 per match) → attribute links with `[via: DR-YYYY-NNN]`.

## Maintenance

Prune when decisions are superseded, bets closed, or themes resolved. Verify linked IDs still exist during `/portfolio-status` or `/context-recall`.

> "Context without connections is just data."
