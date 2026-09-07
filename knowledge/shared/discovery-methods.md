# Discovery Methods

**V2V OS pack on continuous discovery, JTBD, customer research, and assumption validation.**

**Adapted from**:
- Continuous Discovery (Teresa Torres, "Continuous Discovery Habits") -- public methodology
- Jobs-To-Be-Done (Clayton Christensen, Bob Moesta, Anthony Ulwick) -- public methodology
- Lean Startup customer development (Steve Blank, Eric Ries) -- public methodology
- Pretotyping (Alberto Savoia, "The Right It") -- public methodology
- April Dunford positioning research lens -- public methodology
- 2026 PM landscape per V2V refresh survey §4

**Source licence**: Public methodology references
**V2V refinements**: Discovery framed as Phase-1 Intent activity (before Decisions); explicit cross-references to assumption-map + opportunity-tree + experiment-design + interview-synthesis skills; weekly-touch + outcome-anchored cadence per Torres

---

## Purpose

This pack is the canonical V2V OS reference for the discovery side of product work. I reach for it when I'm framing a new problem, scoping a strategic bet, deciding whether a feature idea is worth the engineering bill, or designing the research that goes in front of customers next week. It sits upstream of `prioritization.md` (which ranks discovered opportunities) and feeds the assumption-map / opportunity-tree / experiment-design / interview-synthesis skills.

The pack is methodology-dense by design. The point isn't to memorize every framework — it's to know which lens fits the question I'm actually facing.

---

## 1. Discovery vs. Delivery

The single biggest failure mode I see in product organizations is running delivery without discovery. The team is shipping every sprint, the burndown charts look great, the demos are slick — and the product is going sideways because nobody asked the upstream question first.

The V2V phase model makes this explicit:

| Question | Phase | Activity |
|---|---|---|
| What problem are we solving, and is it worth solving? | **Phase 1 -- Intent** | Discovery |
| Have we committed to solving it, and how? | **Phase 2 -- Decisions** + **Phase 3 -- Commitments** | Strategic bet, PRD |
| How well do we solve it? | **Phase 4 -- Execution** | Delivery |
| Did the value land? | **Phase 5 -- Outcomes** + **Phase 6 -- Learning** | Outcome review |

Discovery is the work that happens **in Phase 1, before commitments are locked**. It is not optional. It is not a "research project" that ends. It is a continuous practice the product team runs in parallel with delivery, week after week.

Two principles I hold:
- **Discovery is continuous, not a phase you exit.** Teresa Torres's whole argument is that one-time research projects bake in stale assumptions. The market moves, customers evolve, your understanding decays. Weekly touch beats quarterly research sprints.
- **You can't out-deliver bad discovery.** No amount of engineering velocity rescues a feature solving the wrong problem. The most expensive code is code that ships and nobody uses.

---

## 2. Continuous Discovery (Teresa Torres)

Torres's *Continuous Discovery Habits* (2021) is the single most influential 2020s-era methodology for ongoing discovery practice. Its core claim: discovery is a team habit, not a research project.

### The Trio

Discovery happens in a **product trio**: PM + Designer + Engineer, working together on the same problem space. The point isn't role overlap — it's shared context. When the engineer hears the customer use the same phrase three times, that phrase shows up in the interface decisions a month later in ways no Notion doc would have carried.

### Weekly Touchpoints

Talk to at least one customer every week. Not a formal study. Not a research sprint. A 20-minute conversation with someone who lives in the problem space, every week, forever.

The argument for cadence over depth: a single deep research project gives you a snapshot. Weekly conversations give you a derivative — you see what's changing.

### Outcome-Anchored

At the top of every discovery effort sits a **Desired Outcome** — a measurable business or product outcome, NOT a feature. "Increase 30-day retention from 35% to 50%" is an outcome. "Build a notification system" is not. The discovery work asks: what opportunities, if addressed, would move this outcome?

This pack pairs with `prioritization.md`: prioritization frameworks rank work against the outcome.

### Opportunity Solution Tree (OST)

The durable artifact of Torres discovery. Four levels:

```
DESIRED OUTCOME: Increase 30-day retention from 35% to 50%
├── Opportunity: Users don't understand core value in first session
│   ├── Solution A: Guided walkthrough
│   │   └── Experiment: Prototype test with 5 users
│   └── Solution B: Role-based onboarding
│       └── Experiment: Concierge test with 10 users
├── Opportunity: Users lose work when session times out
│   ├── Solution C: Auto-save with visual confirmation
│   │   └── Experiment: A/B test save frequency
│   └── Solution D: Extend session timeout
│       └── Experiment: Usage analytics on session length
└── Opportunity: Users can't find features they need
    └── Solution E: Contextual help system
```

Cross-ref: `/opportunity-tree` skill instantiates the OST as a deliverable.

### Generative vs. Evaluative Research

The distinction matters because it determines what questions you ask.

| Type | Question | Methods |
|---|---|---|
| **Generative** | What problems do customers have? What opportunities exist? | Open-ended interviews, observation, diary studies |
| **Evaluative** | Does this solution actually solve the problem? | Usability tests, A/B tests, concierge MVPs |

Generative work goes upstream of solution ideas. Evaluative work tests solution ideas against discovered problems. Teams routinely confuse the two — running "usability tests" on a feature whose underlying problem was never validated.

### Story-Based Interviews

Ask about **specific past experience**, not hypotheticals. People are terrible at predicting their own future behavior and great at narrating recent past behavior in detail.

Good: "Tell me about the last time you needed to onboard a new team member. Walk me through what happened."

Bad: "Would you use a feature that helps onboard team members?"

---

## 3. Jobs-To-Be-Done (JTBD)

JTBD reframes the customer relationship. Customers don't buy products — they "hire" products to make progress in a given circumstance. The "job" is the progress sought, and it's stable over time even as the solutions that compete for it change.

### Christensen's Framing -- The Milkshake Story

The canonical example: a fast-food chain wanted to sell more milkshakes. Demographic segmentation didn't help. Then Christensen's team asked "what job is the milkshake being hired to do?" and discovered that morning commuters were hiring it for a 30-minute boring drive, where it had to last, fit in a cupholder, and not crumb on the seat. Competitors were bagels (too dry) and bananas (gone too fast). Different job for the same product later in the day (parent buying for child as a reward). Same product, different jobs, different competitive set.

The job format: **"When [situation], I want to [motivation], so I can [expected outcome]."**

### Moesta's Forces of Progress

Four forces act on a switching decision:

| Force | Direction |
|---|---|
| **Push** -- dissatisfaction with current solution | Drives switch |
| **Pull** -- attraction of new solution | Drives switch |
| **Anxiety** -- fear about new solution | Resists switch |
| **Habit** -- comfort with current solution | Resists switch |

To win a switch, push + pull must overcome anxiety + habit. Most product teams over-invest in pull (features, messaging) and ignore anxiety + habit (the actual blockers). The Switch Interview surfaces all four.

### Ulwick's Outcome-Driven Innovation

Ulwick's variant: for any job, the customer has 50-150 **desired outcomes** ("minimize the time it takes to..." / "increase the likelihood that..."). Survey customers on importance × satisfaction for each outcome. Plot. The "underserved" quadrant (high importance, low satisfaction) is where the opportunity sits.

### When to Use JTBD

| Situation | Fit |
|---|---|
| Market re-segmentation | Strong fit |
| Category creation / white space | Strong fit |
| Understanding why customers switch | Strong fit |
| Incremental feature work in a defined category | Weak fit — overkill |
| Compliance / table-stakes work | Poor fit |

---

## 4. Lean Startup Customer Development (Blank, Ries)

The Lean Startup tradition is the parent methodology of much modern discovery practice. Two founders matter:

### Steve Blank -- "Get Out of the Building"

Blank's *Four Steps to the Epiphany* (2005) argued that startups die not from execution but from failing to validate a market. His four steps:

1. **Customer Discovery** -- Validate the problem exists
2. **Customer Validation** -- Validate customers will pay
3. **Customer Creation** -- Scale demand
4. **Company Building** -- Transition to execution

Steps 1-2 are pure discovery. The instruction "get out of the building" is the single most-quoted phrase in the methodology — meaning that no amount of internal brainstorming, deck-building, or whiteboard work substitutes for talking to actual prospective customers.

### Eric Ries -- Build-Measure-Learn

Ries's *The Lean Startup* (2011) operationalized Blank with the BML loop:

- **Build** the smallest thing that tests the riskiest assumption
- **Measure** what actually happens
- **Learn** whether to persevere or pivot

The MVP is an experiment, not a half-built product. The cycle time of BML is the rate at which you learn.

### Pivot vs. Persevere

A pivot is a change in strategy without a change in vision. You learned something that invalidates the current approach but reinforces the underlying belief. Triggers:
- Engagement metrics flat despite iterations
- CAC not decreasing
- Retention not improving with product changes
- Customer feedback consistently points to a different problem
- The Sean Ellis "must-have" test (<40% would be "very disappointed" if the product went away)

### Rob Fitzpatrick -- The Mom Test

Fitzpatrick's *The Mom Test* (2013) is the small book every PM should read before their first customer interview. The thesis: anyone — even your mom — will lie to you about your business if you ask leading questions. The fix is structural:

- Talk about their life instead of your idea
- Ask about specifics in the past, not generics or opinions about the future
- Talk less and listen more

The "compliments are the fool's gold of customer research" line is worth tattooing somewhere.

---

## 5. Pretotyping (Alberto Savoia)

Savoia, ex-Google engineering director, wrote *The Right It* (2019) on the discipline of validating whether a thing should be built before you build it. Pretotyping ("pretend prototype") is upstream of prototyping. The pretotype answers "would they want it?" — the prototype answers "can we build it?"

### Eight Pretotype Types

| Type | What you do | What you learn |
|---|---|---|
| **Pinocchio** | Build a non-functional wooden version, carry it around as if it works | Personal demand signal — would I actually use this in my life? |
| **Fake Door** | Add a button/link for the feature that goes to "coming soon" | Click-through demand from real users |
| **Mechanical Turk** | The interface looks automated; humans do the work behind it | Whether the value prop holds when the experience is real |
| **Wizard of Oz** | Similar to Mechanical Turk but explicitly designed as a research tool | Same as above, more rigorous |
| **Provincial** | Test the idea in one small geography or segment before scaling | Whether the demand is general or local |
| **Pre-Sale** | Take real money for the thing before it exists | Strongest signal — payment is behavior, not opinion |
| **YouTube** | Make a demo video of the not-yet-built thing | Comprehension + interest at low cost |
| **Concierge** | Manually deliver the service to a few customers | Whether the value proposition works at all |

### TRI Metric

Savoia's framing: most ideas live in **Thoughtland** (your head, decks, strategy docs) where they cannot fail. The Thoughtland-to-Real-world Index (TRI) is the ratio of evidence-grounded data to opinion-grounded data behind an idea. Higher TRI = more validated.

The pretotyping discipline is "raise the TRI before you commit engineering capacity." A fake door + concierge + pre-sale combo can move TRI from 0.05 to 0.7 in two weeks.

### Why Pretotyping Matters More in 2026

The 2026 V2V refresh survey §4 notes that AI tooling has dramatically lowered the cost of building fake doors, demo videos, and concierge backends. A fake-door test that took two days in 2020 takes two hours in 2026. The methodology is suddenly cheap. The teams that still run quarterly research sprints are increasingly out of step with teams that ship a pretotype every week.

---

## 6. Customer Interview Techniques

Discovery interviews are a learnable craft. The technique matters more than the framework. A team running JTBD with bad interview technique will get bad data. A team running no formal framework with good technique will get usable signal.

### The Six Principles

1. **Open-ended over close-ended.** "Tell me about the last time..." beats "Do you...?" every time.
2. **Past behavior over future intent.** Humans are bad at predicting their own behavior and good at narrating recent past behavior. Anchor every question in something that actually happened.
3. **5-Whys to root cause.** When the surface answer is "it's annoying," keep asking why. Five levels deep is usually the buried reason.
4. **"What else?" as a follow-up.** This is the single highest-leverage prompt in interviewing. People list the easy answers first. The third or fourth thing they say is usually the interesting one.
5. **Silence is a tool.** After a question, wait. The pause feels awkward. Hold it. The interviewee will fill it with the real answer.
6. **Take notes on quotes and emotion.** Verbatim quotes are gold for synthesis. So is energy — when did the interviewee lean forward? When did they get tired?

### What NOT to Ask

| Bad question | Why it fails | Better alternative |
|---|---|---|
| "Would you use a product that...?" | Future intent, leading, no signal | "Tell me about the last time you tried to solve..." |
| "How much would you pay for...?" | Anchors on number, no commitment | "What did you spend on the current solution? What did it get you?" |
| "What features should we build?" | Outsources your job, not customer's expertise | "What's the most frustrating part of your current workflow?" |
| "Do you like this design?" | Politeness bias, no behavioral signal | "Show me how you'd use this to accomplish [task]." |

### Switch Interview Template (Moesta JTBD)

```
1. When did you first start looking for a solution?
2. What was happening in your life/work that made you start looking?
3. What other solutions did you consider? Why those?
4. What made you choose this solution over the alternatives?
5. What almost stopped you from switching?
6. Now that you're using it, what's different? What's the same?
```

Cross-ref: `/interview-synthesis` skill — synthesizes interview corpus into themes, opportunities, and assumption-list outputs.

---

## 7. Survey + Quantitative Methods

Surveys are the most overused and most mis-used research method in product organizations. The rule of thumb: surveys validate, they don't generate.

### When Surveys Work

- **Large-N validation of qualitative-discovered hypotheses.** Interviews surface five problems; a survey of 500 ranks them by frequency.
- **Sizing known opportunities.** "How often does this happen?" "What percentage do X?" Specific behavioral questions with bounded answers.
- **Tracking change over time.** NPS, CSAT, feature satisfaction — measured the same way over quarters reveal trend even if absolute numbers are squishy.

### When Surveys Fail

- **Novel-concept evaluation.** "Would you use a feature that...?" gets you noise. People can't evaluate hypothetical concepts in 30-second survey questions.
- **Willingness-to-pay.** Direct "how much would you pay?" questions are worthless. Use Van Westendorp Price Sensitivity Meter or Gabor-Granger instead, and pair with behavioral data.
- **Causal attribution.** Surveys can show correlation; they can't establish that A caused B.

### Common Survey Biases

| Bias | What happens | Mitigation |
|---|---|---|
| **Acquiescence** | Respondents tend to agree with statements | Mix positively and negatively framed items |
| **Central tendency** | Respondents avoid extreme answers | Use even-numbered scales (4 or 6) to force a side |
| **Social desirability** | People answer to look good | Anonymous responses; ask about behavior not attitude |
| **Leading questions** | Wording presupposes the answer | Pilot-test wording with 5 colleagues before launch |
| **Sample bias** | Respondents differ from population | Quota sampling; weight responses; flag in analysis |

### Quantitative Methods for Pricing

Worth a callout because PMs reach for it often:

- **Van Westendorp Price Sensitivity Meter** -- Four questions (too cheap, cheap, expensive, too expensive) reveal acceptable price range
- **Gabor-Granger** -- Randomized price points test buy-likelihood at each
- **Conjoint Analysis** -- Trade-off matrix reveals feature value relative to price

Cross-ref: `pricing-frameworks.md` pack covers these in depth.

---

## 8. Assumption Mapping

Every product idea is a tower of assumptions. The leap-of-faith assumptions are the load-bearing ones — if they're wrong, the whole idea collapses regardless of execution quality.

### The Discipline

1. **Surface every assumption** the idea requires to succeed. "We assume customers..." / "We assume the market..." / "We assume our team..."
2. **Score each by Impact × Uncertainty** on a 2×2 matrix.
3. **The top-right quadrant is the test list.** High impact + high uncertainty = riskiest assumptions. Test these first.
4. **Stop testing assumptions once they're validated or invalidated**, not after a calendar deadline.

### Assumption Categories (Marty Cagan's Four Risks)

| Risk | Question |
|---|---|
| **Value** | Will customers buy / use it? |
| **Usability** | Can they figure out how to use it? |
| **Feasibility** | Can we build it? |
| **Viability** | Does it work for our business? |

Most failed features fail on **value risk** — the team built something usable, feasible, and viable that no customer wanted. That's also the assumption category that's cheapest to test (interviews, fake doors, concierge MVPs) before commitment.

Cross-ref: `/assumption-map` skill instantiates the 2×2 + test plan as a deliverable. `/four-risks-check` skill applies Cagan's four-risk framing to a feature.

---

## 9. Experiment Design

Once you've mapped assumptions, the high-priority ones need experiments.

### Hypothesis Format

```
We believe that [user segment] will [behavior]
because [underlying reason / mechanism].

We will know this is true when we see [observable signal]
above [threshold] within [timeframe].
```

The "we will know" clause is the falsifiability test. If you can't name an observable signal and a threshold, you don't have an experiment — you have an opinion you'll defend regardless of data.

### Falsifiability

A real hypothesis can be wrong. "Customers value good design" is not a hypothesis. "30% of free-tier users will click a 'Pro' upgrade CTA when shown after creating their fifth document" is a hypothesis. The latter could be wrong; the former cannot be tested.

### Stop Conditions

Set them before you start. At what evidence threshold do you stop the experiment and act? Two failure modes:
- **No stop condition** -- experiments run forever, results get re-interpreted to match preference
- **Sunk-cost continuation** -- you've already invested two weeks, so you keep going even though early signal is clear

### Multiple-Treatment Designs

Single-variant tests reveal whether A works. Multi-variant tests reveal which of A/B/C works best — at the cost of needing more sample and longer runtime. Use multi-variant when you have three real options worth comparing; don't use it as a fishing expedition.

Cross-ref: `/experiment-design` skill formalizes hypothesis + falsifiability + stop conditions into an experiment plan. `/pretotype` skill picks a pretotype type for the experiment.

---

## 10. Common Discovery Failures

The five failure patterns I see most often:

### "We talked to 5 customers and they all loved it."

Three problems with this sentence:
- **Small sample** — 5 is enough for thematic generative work, not enough for evaluative claims
- **Confirmation bias** — you remember the customers who validated, forget the ones who didn't
- **Salesman-customer dynamic** — if the PM ran the interview, the customer was being polite

The "customer love" answer should always trigger a follow-up: what specific past behavior demonstrates this love? If the answer is "they said so," the love is hypothetical.

### "We know our customers — we don't need discovery."

Deep-domain knowledge is real, but it decays. Markets shift. New entrants change buyer expectations. The customer you onboarded three years ago is a different person now. "We know our customers" is almost always shorthand for "we don't want to invest in re-validating our assumptions."

### Discovery as deliverable, not practice.

A one-time research project, executive deck, then back to feature factory. The output gets cited for a quarter, then the data ages out and nobody updates it. Continuous discovery is the antidote, but it requires organizational commitment to customer access — which most orgs don't fund.

### PM doing discovery solo.

If discovery happens entirely in the PM's head and Notion docs, the eng team and design team get the conclusion without the raw signal. When implementation decisions come up later, the team has no shared context to draw from. The Torres trio (PM + Designer + Eng) is the structural fix.

### Surveying when you should be interviewing.

The most common cargo-cult mistake. The team has a feature idea, they want validation, they send a survey, they get aggregate noise, they ship the feature, it fails. Surveys validate; interviews generate. Use the right method for the question.

---

## 11. 2026 Discovery Tooling Landscape

Per the V2V refresh survey §4, the discovery tooling space has shifted meaningfully in 2025-2026:

- **AI-assisted interview synthesis.** Tools that transcribe interviews and auto-cluster themes. Dovetail, Reduct, EnjoyHQ have shipped AI-native features. The bottleneck is shifting from "synthesizing 20 hours of interview audio" to "running enough interviews to feed the synthesis." Cross-ref: `/interview-synthesis` skill.
- **In-product behavioral platforms with AI insight layers.** Pendo, Userpilot, Amplitude — adding AI summaries of funnel drop-off, segment behavior, feature adoption. Useful for evaluative work, weak for generative.
- **Reforge + Lenny's Newsletter playbooks.** Practitioner content has shifted from "frameworks" to "specific plays." The 2026 PM reads more case studies than methodology books.
- **Pretotyping renaissance.** As AI tooling lowers the cost of building fake-doors and concierge backends, pretotyping is having a moment. A fake-door test that took two days in 2020 takes two hours in 2026 with a Claude/Cursor + landing-page-builder stack.

A practical implication: the team that runs a pretotype every two weeks beats the team that runs a research sprint every quarter, because the pretotype generates behavioral signal (clicks, pre-orders, concierge usage) while the survey generates only attitudinal signal.

---

## 11.1 AI-Moderated Interviewing and the Cadence Ceiling (added 2026-06-24)

**Adapted from**:
- 2026 generative-user-research vendor landscape — Marvin (heymarvin.com, "AI-moderated interviewer / scale interviews 1000X"), Perspective AI (getperspective.ai), Conveo (conveo.ai), Qualitati (qualitati.com) — public product/marketing positioning, *verify per vendor before quoting in customer-facing work*
- Teresa Torres, public 2026 commentary on AI-powered continuous discovery (producttalk.org / LinkedIn) — public practitioner commentary

**Source licence**: Public / factual (vendor positioning + public practitioner commentary)
**V2V refinements**: the cadence-ceiling reframing (what the 2026 tooling actually moves vs. what it does not); the generative-judgment + trio-shared-context caveat that keeps the V2V differentiator load-bearing.

§11 framed the 2026 bottleneck as shifting from "synthesizing 20 hours of interview audio" to "running enough interviews to feed the synthesis." As of mid-2026 that framing is already being overtaken. The development is **AI-moderated (conversational) interviewers** — AI that *conducts* the interview itself: asks your questions, probes open-endedly, adapts follow-ups, and runs asynchronously at scale without a human moderator in the loop. Multiple independent vendors now ship this (Marvin, Perspective AI, Conveo, Qualitati), so it is a category development, not a single tool.

**What this actually moves: the cadence ceiling.** Torres's continuous-discovery method assumes a human constraint — "talk to at least one customer every week" (§2). That weekly-touch ceiling exists because a human PM/researcher can only sit in so many conversations. AI moderation removes that specific constraint: interviews run in parallel, asynchronously, at volumes a human team cannot staff. One cited 2026 continuous-discovery benchmark (Perspective AI) reports teams using conversational AI averaging ~47 customer conversations in a period where the human ceiling would cap them far lower. **Treat that figure, and all vendor "scale 1000X"-class claims, as cited-not-claimed** — they are vendor-reported benchmarks circa 2026, directionally credible and corroborated across vendors, but not independently audited here. Verify the specific number against the source before repeating it to a customer or in a deliverable.

**The load-bearing V2V caveat — what does NOT transfer.** Cadence was never the only constraint, and removing it does not make discovery free:

1. **The generative "what problem?" leap is still human judgment.** AI-moderated interviews scale *evaluative/confirmatory* volume well (does this problem recur? how often? in what words?) and can run Mom-Test-disciplined structured probes (§6) at scale. But the generative jump — noticing that five customers are circling the *same unstated* problem, reframing the opportunity, knowing which thread to pull next — is interpretation, not transcription. More interviews give you more raw signal; they do not give you the synthesis insight. The risk is a team that runs 47 AI conversations and mistakes interview *volume* for discovery *understanding*.

2. **The trio's shared context does not survive async AI moderation.** §2's whole argument for the PM+Designer+Engineer trio is shared raw context — "when the engineer hears the customer use the same phrase three times, that phrase shows up in the interface decisions a month later." An AI-moderated async interview delivers a transcript and an auto-cluster to the PM; the engineer and designer were never in the room. You can re-distribute the synthesis, but you cannot re-distribute the *having-been-there*. Teams adopting AI moderation should deliberately re-create trio exposure (shared listening to a sample of recordings, trio synthesis sessions) rather than assume the tooling preserved it.

**The differentiator shift.** In the pre-AI-moderation world, the scarce, differentiating resource in discovery was *cadence* — the discipline to talk to customers every week. In the 2026 AI-moderation world, cadence is cheap; the scarce, differentiating resources become **interpretation** (the generative synthesis leap) and **trio shared-context** (keeping eng + design genuinely exposed to the raw signal, not just the conclusion). A V2V team should adopt AI-moderated interviewing to break the cadence ceiling *and* explicitly invest the freed capacity into the two things the tooling does not do — otherwise it has automated the easy half of discovery and starved the hard half. Cross-ref: `/interview-synthesis` (the synthesis the AI does not own) and §10's "PM doing discovery solo" failure (which async AI moderation can silently amplify).

---

## 12. V2V Cross-References

This pack composes with the following V2V OS surfaces:

| Skill / Pack | What it does | When I reach for it |
|---|---|---|
| `/assumption-map` | Surfaces and scores assumptions on Impact × Uncertainty | After discovery surfaces a strategic option |
| `/opportunity-tree` | Structures the OST as a deliverable | When I need a durable artifact for the trio |
| `/experiment-design` | Designs hypothesis + falsifiability + stop conditions | When an assumption needs testing |
| `/pretotype` | Picks a pretotype type for the experiment | Cheap validation before engineering capacity is committed |
| `/interview-synthesis` | Synthesizes interview corpus into themes + opportunities | After 5-10 interviews are run |
| `/four-risks-check` | Cagan's value/usability/feasibility/viability lens | Before requesting engineering capacity |
| `/customer-value-trace` | Traces feature work to measurable customer value | Validates that delivery work is anchored in real value |
| `prioritization.md` (sibling pack) | Frameworks to rank discovered opportunities | After discovery surfaces a list of opportunities |
| `user-research.md` (sibling pack) | Research design and rigor depth | When the question requires formal study, not weekly conversation |
| `/strategic-bet` | Phase-2 conversion of opportunity to commitment | When discovery has validated enough to commit |

---

## Sources

- Teresa Torres, *Continuous Discovery Habits* (2021)
- Clayton Christensen, *Competing Against Luck* (2016) -- JTBD theory
- Bob Moesta and Chris Spiek, *Demand-Side Sales 101* (2020) -- Switch interviews
- Anthony Ulwick, *Jobs to Be Done: Theory to Practice* (2016) -- Outcome-Driven Innovation
- Steve Blank, *The Four Steps to the Epiphany* (2005) -- Customer Development
- Eric Ries, *The Lean Startup* (2011) -- Build-Measure-Learn
- Rob Fitzpatrick, *The Mom Test* (2013) -- Interview technique
- Alberto Savoia, *The Right It* (2019) -- Pretotyping
- Marty Cagan, *Inspired* (2nd ed., 2017) -- Four risks framework
- April Dunford, *Obviously Awesome* (2019) -- Positioning research lens
- V2V refresh survey §4 (2026) -- Tooling landscape

---

*This pack is a V2V OS knowledge reference, not a sensitive skill. Discovery work produces opinions, hypotheses, and prioritized assumption lists — not regulated outputs. Apply standard PM judgment and consult `/four-risks-check` before commitment.*
