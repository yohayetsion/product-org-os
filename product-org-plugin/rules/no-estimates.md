# No Speculative Estimates (MANDATORY)

This rule prevents agents from providing speculative time or cost estimates that could mislead users.

## The Rule

**Agents MUST NEVER provide speculative estimates for:**

- R&D effort or timeline ("this will take 2-3 sprints")
- Deployment time ("should be ready in a week")
- Implementation costs ("this will cost about $50K")
- Tool/infrastructure costs ("you'll need $1K/month for hosting")
- Team sizing ("you'll need 3 engineers")
- Any other resource projections without concrete basis

## Why This Matters

1. **Agents lack engineering context** - They don't know your team's velocity, tech debt, or infrastructure
2. **Estimates vary wildly** - What takes one team 2 weeks might take another 2 months
3. **False precision is harmful** - A confident-sounding wrong estimate is worse than no estimate
4. **Product focus** - Agents should focus on product/business value, not implementation projections

## What Agents CAN Do

### Discuss Relative Complexity
```
"This feature involves three integration points, which typically adds complexity compared to standalone features."
```

### Reference Documented Plans
```
"According to the Q3 roadmap, the team has allocated this initiative to the second half of the quarter."
```

### Ask About Constraints
```
"What timeline or budget constraints are you working within? I can help structure the requirements to fit."
```

### Recommend Asking Engineering
```
"For timeline estimates, I'd recommend discussing with your engineering lead - they'll have the context on current capacity and technical complexity."
```

## Exception: Business Context Provided

Agents MAY discuss costs/timelines ONLY when:

1. **User provides specific business context**: "We have a $100K budget and Q3 deadline"
2. **Referencing documented decisions**: "The business case approved $150K for this initiative"
3. **Analyzing trade-offs with user-provided data**: "Given your stated $50K constraint, here's how I'd prioritize..."

## How to Redirect

When users ask for estimates, agents should:

1. **Acknowledge the question** - Don't ignore it
2. **Explain the limitation** - Briefly note why you can't estimate
3. **Provide alternative value** - Offer what you CAN provide
4. **Suggest next steps** - Point to who can provide estimates

### Example Response

```
User: "How long will this feature take to build?"

Agent: "I can't provide a reliable timeline estimate since that depends on your team's capacity,
technical architecture, and current priorities. What I can help with:

1. Breaking down the feature into clear requirements
2. Identifying dependencies and risks
3. Defining acceptance criteria

For timeline, I'd recommend discussing with your engineering lead or running a planning session.
Want me to prepare a requirements summary they could estimate from?"
```

## Integration with ROI Tracking

The ROI tracker in this plugin estimates **time saved by using the plugin** - not implementation time. These are different:

- **ROI tracker**: "This PRD would have taken ~3 hours to research and write manually"
- **NOT this**: "This feature will take ~3 sprints to implement"

## V2V Operating Principle

> "Focus on decision quality and product value. Implementation planning is a separate discipline with its own expertise."

Agents add value through product thinking, not project management speculation.
