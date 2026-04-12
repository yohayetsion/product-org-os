# User Research Methods — Frameworks & Methods

## Overview

User research is the evidence layer that prevents design by assumption. It provides structured ways to understand what users need, how they behave, and where they struggle. The right research method depends on what you need to learn and when you need to learn it.

This knowledge pack covers the core methods a User Researcher applies throughout the product lifecycle. Each method has different strengths — the skill is in matching the method to the question.

---

## Frameworks

### Usability Testing

**When to use**: When you have a design (wireframe, prototype, or live product) and need to know if users can actually use it. Usability testing is the most impactful research method for iterative design.

**How it works**: Participants attempt realistic tasks using the product while a researcher observes their behavior, questions, and frustration points.

**Types:**

| Type | Setup | Best For | Sample Size |
|------|-------|----------|-------------|
| Moderated in-person | Same room, real-time | Complex flows, nuanced observation | 5-8 per round |
| Moderated remote | Video call + screen share | Geographic diversity, convenience | 5-8 per round |
| Unmoderated remote | Tool-based (Maze, UserTesting) | Scale, quick validation | 10-20 per round |

**The 5-user rule**: Jakob Nielsen's research shows that 5 users find approximately 85% of usability problems. Three rounds of 5 users (test, fix, retest) is more effective than one round of 15.

**Task design principles:**
- Frame tasks as user goals, not feature instructions: "Find a watch under $500" not "Click the filter button"
- Include edge cases: what happens when data is missing, when the user makes a mistake
- Order tasks from easy to hard to build participant confidence
- Include a baseline task the current design handles well (for calibration)

**Template for usability test plan:**
```
Objective: [What decision this test informs]
Participants: [Segment, count, recruitment criteria]
Method: [Moderated/unmoderated, remote/in-person]
Tasks:
  1. [Task description] — Success = [observable outcome]
  2. [Task description] — Success = [observable outcome]
Metrics: Task completion rate, time on task, error count, satisfaction (SUS/SEQ)
Analysis: [How findings will be synthesized]
Decision: [What we will decide based on results]
```

**Limitations**: Usability testing measures whether users can use something, not whether they will choose to. It is lab behavior, not natural behavior. Combine with analytics for the full picture.

---

### Card Sorting and Tree Testing

**When to use**: When designing information architecture — navigation structure, category systems, menu organization, or content hierarchy.

**How it works**:

**Card Sorting** (generative): Give participants cards representing content items and ask them to group the cards into categories that make sense to them.
- **Open sort**: Participants create their own category names. Reveals mental models.
- **Closed sort**: Participants sort into predefined categories. Validates proposed structure.
- **Hybrid sort**: Predefined categories plus the option to create new ones.

**Tree Testing** (evaluative): Give participants a text-only representation of your navigation hierarchy and ask them to find specific items. No visual design influence — tests pure findability.

**Template for card sort study:**
```
Objective: [What structure this informs]
Method: [Open/Closed/Hybrid], [remote/in-person]
Cards: [List of items to sort]
Categories (if closed): [Predefined categories]
Participants: [Count and segment]
Analysis: Similarity matrix, dendrogram, agreement percentage
Decision: [How results map to navigation decisions]
```

**Limitations**: Card sorting reveals grouping preferences but not task flow. Users may group items logically but still struggle to navigate a structure based on those groups. Always follow card sorting with tree testing to validate.

---

### Journey Mapping

**When to use**: When you need to understand the complete user experience across touchpoints, time, and channels. Essential before redesigning workflows or identifying opportunities for new features.

**How it works**: Journey maps visualize the end-to-end experience of a user achieving a goal, mapping their actions, thoughts, emotions, and pain points at each stage.

**Journey map components:**

1. **Persona** — Which user archetype this journey represents
2. **Scenario** — The specific goal and context
3. **Stages** — The phases of the journey (awareness, consideration, action, etc.)
4. **Actions** — What the user does at each stage
5. **Thoughts** — What the user is thinking
6. **Emotions** — How the user feels (frustration, confidence, anxiety)
7. **Touchpoints** — Channels and interfaces used
8. **Pain Points** — Where the experience breaks down
9. **Opportunities** — Where design can improve the experience

**Template for journey map:**
```
Persona: [Name and archetype]
Scenario: [Goal in context]

| Stage | Actions | Thoughts | Emotion | Touchpoint | Pain Point | Opportunity |
|-------|---------|----------|---------|------------|------------|-------------|
| [Phase 1] | [What they do] | [What they think] | [How they feel] | [Channel] | [Frustration] | [Improvement] |
| [Phase 2] | ... | ... | ... | ... | ... | ... |
```

**Current state vs. future state**: Map both. Current state reveals problems. Future state envisions solutions. The gap between them is your design brief.

**Limitations**: Journey maps are only as good as the research behind them. A journey map based on assumptions is fiction, not research. Always ground journey maps in actual user data (interviews, observations, analytics).

---

### Persona Development

**When to use**: When the team needs a shared, evidence-based understanding of who they are designing for. Personas prevent the product from being designed for "everyone" (which means no one).

**How it works**: Personas are composite archetypes representing distinct user segments. They are built from research data, not demographics or assumptions.

**Behavior-based personas**: The most useful personas are built around behaviors, goals, and pain points — not demographics like age and income. Two 35-year-olds can have completely different product needs based on their context and goals.

**Persona components:**
- **Name and photo** — Makes the persona memorable and human
- **Role/context** — What they do, where they work
- **Goals** — What they are trying to achieve
- **Behaviors** — How they currently solve the problem
- **Pain points** — What frustrates them
- **Motivations** — What drives their decisions
- **Technical comfort** — How they relate to technology
- **Quote** — A representative statement from real research

**Template for persona:**
```
## [Persona Name]
**Role**: [Context and job/life role]

**Goals**: [3-5 primary goals]
**Behaviors**: [How they currently work]
**Pain Points**: [3-5 frustrations]
**Motivations**: [What drives decisions]
**Technical Comfort**: [Low/Medium/High + specifics]

**Quote**: "[Representative quote from research]"

**Implications for Design**:
- [Design decision this persona influences]
- [Feature priority this persona suggests]
```

**Limitations**: Personas lose value when they are not maintained. Update personas as new research reveals changes in user behavior. Also, personas can accidentally exclude edge cases — remember that real users are more diverse than any persona set.

---

### Contextual Inquiry

**When to use**: When you need to understand users in their natural environment — their actual workspace, tools, workflows, and workarounds. Essential for enterprise and B2B products.

**How it works**: A researcher observes and interviews users while they work in their real environment. It combines observation (what they do) with interview (why they do it).

**Four principles of contextual inquiry (Beyer & Holtzblatt):**
1. **Context** — Go to the user's workplace. Don't bring them to a lab.
2. **Partnership** — Work alongside the user. They are the expert on their job.
3. **Interpretation** — Validate your observations in real time: "I noticed you switched tabs there — why?"
4. **Focus** — Have a clear focus but stay open to surprises.

**Session structure:**
1. **Introduction** (10 min) — Explain the purpose, set expectations
2. **Observation** (40-60 min) — Watch the user work, ask clarifying questions
3. **Summary** (15 min) — Play back observations, verify interpretations
4. **Debrief** (post-session) — Synthesize notes, identify themes

**Limitations**: Contextual inquiry is time-intensive. A single session takes 2-3 hours including travel and debrief. Plan for 6-10 sessions to reach saturation. It also requires strong facilitation skills — knowing when to observe versus when to probe.

---

### Survey Design

**When to use**: When you need to quantify attitudes, preferences, or satisfaction across a large sample. Surveys answer "how many" and "how much," not "why."

**How it works**: Structured questionnaires distributed to a large sample, analyzed statistically.

**Question design principles:**
- **One concept per question** — Don't double-barrel: "How satisfied are you with speed and accuracy?"
- **Neutral framing** — Avoid leading: "Don't you think the new design is better?"
- **Appropriate scales** — 5-point Likert for opinions, binary for yes/no, NPS for loyalty
- **Required vs. optional** — Only require essential questions
- **Logical order** — General to specific, easy to sensitive

**Common scales:**
- **Likert (5-point)**: Strongly Disagree to Strongly Agree
- **SUS (System Usability Scale)**: 10 standardized questions, scored 0-100
- **NPS (Net Promoter Score)**: "How likely to recommend?" (0-10)
- **CSAT**: "How satisfied are you?" (1-5)
- **CES (Customer Effort Score)**: "How easy was this?" (1-7)

**Template for survey plan:**
```
Objective: [What decision this survey informs]
Population: [Target segment and sample size]
Distribution: [Channel and method]
Questions: [Number and estimated completion time]
Analysis plan: [Statistical methods, segmentation]
Timeline: [Distribution, collection, analysis dates]
```

**Limitations**: Surveys measure stated preferences, not actual behavior. Users say they want one thing and do another. Use surveys to complement behavioral data (analytics, usability testing), not to replace it. Low response rates can introduce selection bias.

---

### Research Synthesis

**When to use**: After completing any research study. Synthesis is what transforms raw data into actionable insights.

**How it works**: Systematic analysis of research data to identify patterns, themes, and design implications.

**Affinity mapping process:**
1. **Extract** — Pull individual observations onto sticky notes (physical or digital)
2. **Cluster** — Group related observations without predefined categories
3. **Name** — Label each cluster with a theme description
4. **Prioritize** — Rank themes by frequency, severity, and design impact
5. **Translate** — Convert themes into design implications and recommendations

**Insight format:**
```
Insight: [Clear, specific observation]
Evidence: [Data points supporting this insight]
Frequency: [How many participants exhibited this]
Severity: [Low/Medium/High/Critical]
Design Implication: [What this means for the product]
Recommendation: [Specific action to take]
```

**Limitations**: Synthesis quality depends on research quality. Biased data produces biased insights. Always note sample limitations and confidence levels. Mark insights as "strong signal" (consistent across multiple sources) vs. "weak signal" (limited evidence, needs further validation).

---

## Method Selection Framework

| Question Type | Best Method | Sample | Timeline |
|---------------|-------------|--------|----------|
| "Can users use this?" | Usability testing | 5-8 | 1-2 weeks |
| "How should we organize this?" | Card sorting + tree testing | 15-30 | 1-2 weeks |
| "What is the full experience?" | Journey mapping + interviews | 8-12 | 2-4 weeks |
| "Who are our users?" | Interviews + contextual inquiry | 12-20 | 3-6 weeks |
| "How many users feel X?" | Survey | 100+ | 1-2 weeks |
| "Why do users struggle here?" | Contextual inquiry | 6-10 | 2-4 weeks |
| "Is the new version better?" | A/B testing + usability | Varies | 2-4 weeks |

---

## References

- Steve Krug, *Don't Make Me Think* / *Rocket Surgery Made Easy*
- Erika Hall, *Just Enough Research*
- Jakob Nielsen, Nielsen Norman Group research articles
- Hugh Beyer & Karen Holtzblatt, *Contextual Design*


## Common Pitfalls

- Sample sizes matter — don't generalize from 3-5 user interviews without flagging the limitation
- Usability testing findings are not market validation — they test interaction, not demand
- Persona creation must be evidence-based, not aspirational — personas from imagination are fiction
