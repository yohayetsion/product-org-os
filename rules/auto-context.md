# Auto-Context Injection

Before agents produce deliverables, automatically inject relevant context from `context/index.json`.

> **Superseded for spawn-time injection by `agent-spawn-protocol.md` §7 (Context Discovery & Injection).** This rule describes the minimal keyword-match injection. At agent-spawn time the orchestrator now runs the fuller §7 procedure — multiple term sets, cross-reference follow (`context-graph.md`), recall-memory (Layer B) scan, broaden-if-thin — and the spawned agent reports it in the `[Context Injected]` Audit Block section. Treat §7 as authoritative when spawning; this rule covers the non-spawn / inline auto-context case.

## How It Works

1. Parse user's request for topic keywords
2. Query topic indexes in `context/index.json`
3. If matches found, include up to 5 brief summaries as "Auto-Context" in the agent's working context

## When to Inject

Creating decision records, PRDs, specs, strategic bets, outcome reviews, roadmaps, GTM plans — any deliverable that should be informed by organizational memory.

## When NOT to Inject

Simple Q&A, system ops, context retrieval operations (these ARE the query), or when user provides all context.

## Matching Strategies

1. **Exact ID match**: Request mentions DR-2026-003 → inject that record
2. **Keyword match**: Match against `topicIndex` in index.json
3. **Product match**: Filter by product context in multi-product orgs

> "The best context system is invisible."
