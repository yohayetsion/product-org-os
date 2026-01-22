# Context Layer

The Context Layer provides **persistent memory** for your AI product organization. It enables decisions to be remembered, agents to share context, and the organization to learn from outcomes.

## Folder Structure

```
context/
├── decisions/          # Decision registry - all major decisions
│   ├── index.md        # Master list with quick lookup
│   └── [YYYY]/         # Individual records by year
├── bets/               # Strategic bet registry
│   ├── index.md        # Master list of all bets
│   └── [YYYY]/         # Individual bets by year
├── assumptions/        # Assumption tracker
│   └── registry.md     # All assumptions with validation status
├── portfolio/          # Current state
│   └── active-bets.md  # What we're currently betting on (includes V2V phase tracking)
├── learnings/          # Accumulated wisdom
│   └── index.md        # Indexed learnings from retrospectives
├── feedback/           # Customer and market feedback
│   ├── index.md        # Master feedback registry
│   ├── themes.md       # Identified feedback themes
│   └── [YYYY]/         # Individual feedback records by year
├── principles/         # Operating principles tracking
│   ├── README.md       # Principles overview and usage
│   └── scorecard.md    # Periodic principle adherence assessment
└── handoffs/           # Agent-to-agent context
    └── current-session.md  # Active session context
```

## Quick Start

### Save context after a decision
```
/context-save
```

### Recall past context before making a decision
```
/context-recall [topic]
```

### View current portfolio state
```
/portfolio-status
```

### Pass context to another agent
```
/handoff
```

### Find relevant past learnings
```
/relevant-learnings [topic]
```

### Check initiative V2V phase
```
/phase-check [initiative]
```

### Validate commitment readiness
```
/commitment-check [initiative]
```

### Capture feedback
```
/feedback-capture
```

### Query feedback history
```
/feedback-recall [topic]
```

## V2V Phase Tracking

The portfolio tracks initiatives by V2V phase:

| Phase | Name | Key Activities |
|-------|------|----------------|
| 1 | Strategic Foundation | Market analysis, competitive intelligence, vision |
| 2 | Strategic Decisions | Business case, pricing, positioning, bet formulation |
| 3 | Strategic Commitments | Roadmap, GTM, requirements, commitment validation |
| 4 | Coordinated Execution | Launch, campaigns, sales enablement |
| 5 | Business Outcomes | Value realization, customer health, outcomes |
| 6 | Learning Loop | Retrospectives, outcome reviews, learnings |

Use `/phase-check [initiative]` to assess where an initiative stands.

## Principles Tracking

The `principles/` folder tracks adherence to the 8 Operating Principles:

1. End-to-End Ownership
2. Decision Quality
3. Customer Obsession
4. Clarity and Confidence
5. Outcomes Over Outputs
6. Collaborative Excellence
7. Continuous Learning
8. Scalable Systems

Update `principles/scorecard.md` after outcome reviews to track improvement.

## How It Works

1. **After decisions/bets**: Use `/context-save` to extract key information to the registry
2. **Before new work**: Use `/context-recall` to check what's been decided before
3. **For delegation**: Use `/handoff` to brief the receiving agent
4. **For learning**: Retrospectives and outcome reviews feed into the learnings index

## Maintenance

- Index files contain summaries only (stay small)
- Full records stored separately by year
- Handoff file is overwritten each session
- Archive old records annually to `archive/[YYYY]/`
