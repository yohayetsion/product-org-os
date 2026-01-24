# Product Org OS

**An entire product organization that becomes your superpower.**

> Intent → Decisions → Commitments → Execution → Outcomes → Learning

13 agents • 56 skills • 11 strategic documents • Context layer

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

### /product Gateway
Your single entry point. Routes requests to the right agents automatically.
```
/product Launch freemium for SMBs. Context: pricing-research.md
/product Q2 planning. Inputs: customer-interviews/, eng-capacity.md
```

**Response Depth** (`+`/`-` modifiers):
| Modifier | Effect | Example |
|----------|--------|---------|
| `-` | Brief - executive summary | `/product What's launch status? -` |
| *(none)* | Standard - balanced depth | `/product What's launch status?` |
| `+` | Deep - full analysis | `/product What's launch status? +` |

**Meeting Mode**: When you use `/product` or `/plt`, you'll see responses from *individual agents* speaking in their own voice - like walking into a meeting room. You'll see who's engaged, their perspectives, agreements, and tensions. This isn't a monolithic AI response - it's your product org thinking together.

**Multi-Product Organizations**: Filter context by product:
```
/context-recall pricing product:AXIA
/feedback-recall onboarding product:SKYMOD
/portfolio-status product:AXIA
```

### Talk to Agents
Delegate to specific roles. Use shortcuts for faster access.
```
/cpo review board-feedback.pdf and update /strategic-intent
/pm break down epic.md into /user-story items
/plt review portfolio-health.md and run /portfolio-tradeoff
/bizops analyze pricing-data.xlsx and create /pricing-model
```

**Agent Shortcuts:**
| Shortcut | Full Agent |
|----------|------------|
| `/pm` | `/product-manager` |
| `/plt` | `/product-leadership-team` |
| `/pm-dir` | `/director-product-management` |
| `/pmm-dir` | `/director-product-marketing` |
| `/pmm` | `/product-marketing-manager` |
| `/vpp` | `/vp-product` |
| `/prodops` | `/product-operations` |

### Use Skills Directly
Create, update, or find specific deliverables.
```
Create a /prd for SSO integration - see slack-thread.md
Run /competitive-analysis on Acme - their-demo-notes.md
Update the /roadmap-theme for Growth with mobile initiatives
Find all authentication PRDs using /prd find
```

### Conversational Commands
Mix agents, skills, and documents naturally.
```
/pm-dir review launch-data.xlsx and update the /gtm-strategy
/cpo review board-feedback.pdf and update /strategic-intent
/vp-product review sales-feedback.md and update /positioning-statement
```

---

## What's Included

### 13 Role-Based Agents
CPO, VP Product, Director PM, Director PMM, Product Manager, PMM, BizOps, BizDev, Competitive Intelligence, Product Operations, Value Realization, UX Lead, Product Leadership Team

### 56 Production Skills
PRDs, roadmaps, business cases, GTM strategies, pricing models, launch plans, QBR decks, competitive analyses, decision records, and more

### Context Layer
Organizational memory that persists across sessions:
- **Auto-registration**: All skill outputs automatically tracked in `context/documents/`
- **Decisions & Bets**: Strategic choices with assumptions and re-decision triggers
- **Feedback**: Customer and market signals linked to decisions
- **Learnings**: Accumulated wisdom from retrospectives and outcomes

Query anytime with `/context-recall [topic]`

### V2V Framework
Six phases from strategic intent to learning loop, with skills mapped to each phase

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
