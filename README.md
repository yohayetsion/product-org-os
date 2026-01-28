# Product Org OS

**An entire product organization that becomes your superpower.**

> Intent → Decisions → Commitments → Execution → Outcomes → Learning

13 agents • 65 skills • 11 strategic documents • Context layer

[**View the Interactive Presentation →**](https://yohayetsion.github.io/product-org-os)

---

## Quick Start

```bash
# Install in Claude Code
claude plugins install github:yohayetsion/product-org-os

# Initialize in your project
/setup

# Start using
/product Launch freemium tier for SMBs. Context: pricing-research.md
```

---

## Three Ways to Work

### /product Gateway (Recommended)
Route any request to the right owners. Best for cross-functional work.
```
/product Respond to Acme RFP due Friday. See: rfp-acme.pdf, our-capabilities.md
```

### Direct to Agents
Delegate to a specific role when you know who should handle it.
```
/cpo Portfolio tradeoff: mobile app vs API expansion
/product-manager Break down checkout redesign into user stories
/bizops Build financial model for enterprise tier
```

### Direct to Skills
Get a specific deliverable when you know exactly what you need.
```
/prd SSO integration for enterprise. Requirements in slack-thread.md
/competitive-analysis Deep dive on Competitor X
/decision-record Document our build vs buy choice
```

---

## What's Included

### 13 Role-Based Agents
CPO, VP Product, Director PM, Director PMM, Product Manager, PMM, BizOps, BizDev, Competitive Intelligence, Product Operations, Value Realization, UX Lead, Product Leadership Team

### 65 Production Skills
PRDs, roadmaps, business cases, GTM strategies, pricing models, launch plans, QBR decks, competitive analyses, decision records, launch strategies, competitor alternatives, analytics tracking, marketing psychology, and more

### Context Layer
Organizational memory that persists decisions, feedback, learnings, and strategic bets across sessions.
**New: Interaction history** — full conversation logging with `/interaction-recall` for cross-session continuity.

### V2V Framework
Six phases from strategic intent to learning loop, with skills mapped to each phase

### Optional: Memory MCP Integration
Supercharge your context layer with a **persistent knowledge graph**. Memory MCP enables Claude to remember entities, relationships, and observations across all sessions.

```json
// Add to your .mcp.json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        "MEMORY_FILE_PATH": "./context/memory/knowledge-graph.json"
      }
    }
  }
}
```

**What it adds:**
- **Entities**: Track people, products, competitors, decisions as graph nodes
- **Relations**: Map connections ("owns", "decided", "competes_with")
- **Observations**: Store facts that persist across sessions

Works alongside the file-based context layer — use both for maximum organizational memory.

---

## Use Cases

| Who | What You Get |
|-----|--------------|
| **Solo PM** | Senior-level guidance on every deliverable |
| **Product Team** | Consistent standards, shared memory |
| **Product Org** | Decision frameworks, institutional knowledge |

---

## Documentation

- [Interactive Presentation](https://yohayetsion.github.io/product-org-os) - Visual overview
- [Full Documentation](./PRODUCT-ORG-CLAUDE.md) - Complete skill reference

---

## License

MIT

---

**Free & Open Source.** World-class product capabilities shouldn't be locked behind enterprise software.

Based on the Vision to Value Executive Manifesto by Yohay Etsion.
