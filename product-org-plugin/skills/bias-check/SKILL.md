---
name: bias-check
description: |
  Scan a decision, plan, or document for cognitive biases and provide debiasing recommendations. Improves decision quality by surfacing blind spots.
  Activate when: "bias check", "cognitive bias", "am I biased", "decision bias", "blind spots", "reality check", "thinking errors"
  Do NOT activate for: decision quality audits (/decision-quality-audit), retrospectives (/retrospective)
argument-hint: [decision, plan, or document to check] or [update path/to/bias-check.md]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: decision-quality
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "recheck", "rescan" in input | UPDATE | 100% |
| File path provided | UPDATE | 100% |
| "create", "new", "check", "scan" in input | CREATE | 100% |
| "find", "search", "list bias checks" | FIND | 100% |
| "the bias check", "last check" | UPDATE | 85% |
| Just a decision/topic | CREATE | 80% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Analyze the provided decision/document for biases using the framework below.

**UPDATE**:
1. Check document registry first, then search user's structure
2. Preserve prior bias findings
3. Re-scan with new information or after changes
4. Show which biases were addressed and which remain

**FIND**: Check registry, then search user's folders for bias check reports.

### Search Locations

- `{Product}/Product/decisions/`
- `{Product}/Product/bias-checks/`
- `context/documents/index.md`

---

## Vision to Value Phase

**Phase 6: Learning & Adaptation** -- Improving decision quality by detecting cognitive biases. Can also be applied proactively during Phase 2 (Strategic Decisions) before committing.

## Methodology

### Bias Detection Framework

<!-- Source: Daniel Kahneman, "Thinking, Fast and Slow" (2011). System 1 (fast, intuitive) vs System 2 (slow, deliberate) thinking. Most biases stem from System 1 shortcuts applied to decisions that require System 2 analysis. Kahneman's key insight: we are not only blind to our biases, we are blind to our blindness. -->

<!-- Source: Chip Heath & Dan Heath, "Decisive: How to Make Better Decisions in Life and Work" (2013). WRAP framework: Widen your options, Reality-test your assumptions, Attain distance before deciding, Prepare to be wrong. Each step counters specific biases. -->

<!-- Source: Anti-pattern detection approach inspired by deanpeters/Product-Manager-Skills (GitHub, 2024) — skills that identify common PM thinking traps. -->

Scan for the following 10 cognitive biases, organized by decision phase:

#### Biases in Problem Framing

**1. Confirmation Bias**
- What it is: Seeking/interpreting evidence that confirms existing beliefs while ignoring contradictory evidence
- Detection signals: One-sided evidence cited, disconfirming data absent, "everyone agrees" language, cherry-picked metrics
- Debiasing: Assign a "red team" to argue the opposite. Ask: "What evidence would change our mind?"

<!-- Source: Peter Wason's selection task experiments (1960). Kahneman, "Thinking, Fast and Slow" (2011), Chapter 7. -->

**2. Anchoring**
- What it is: Over-relying on the first piece of information encountered
- Detection signals: First number mentioned dominates analysis, insufficient adjustment from initial estimate, reference point never questioned
- Debiasing: Generate estimates independently before sharing. Start from multiple reference points.

<!-- Source: Tversky & Kahneman, "Judgment under Uncertainty: Heuristics and Biases" (1974). Anchoring effect demonstrated via random number + estimation experiments. -->

**3. Availability Heuristic**
- What it is: Overweighting recent, vivid, or emotionally charged events
- Detection signals: Recent customer complaint drives strategy, single dramatic failure overshadows data, "I just saw/heard" as primary evidence
- Debiasing: Ask: "What does the full dataset say?" Look at trends, not incidents.

<!-- Source: Tversky & Kahneman (1973). Events are judged as more probable when they are easy to recall. -->

#### Biases in Option Evaluation

**4. Sunk Cost Fallacy**
- What it is: Continuing investment because of past spend rather than future value
- Detection signals: "We've already invested X", "We can't waste what we built", past effort as justification for continuing
- Debiasing: Ask: "If we were starting fresh today, would we make this same choice?" Ignore past investment.

<!-- Source: Arkes & Blumer, "The Psychology of Sunk Cost" (1985). Also: Kahneman & Tversky's loss aversion from Prospect Theory (1979). -->

**5. Bandwagon Effect**
- What it is: Following trends or competitors without independent evidence
- Detection signals: "Everyone is doing AI/blockchain/etc.", competitor moves as primary justification, fear of missing out
- Debiasing: Ask: "Why is this right for OUR customers, regardless of what competitors do?"

<!-- Source: Leibenstein, "Bandwagon, Snob, and Veblen Effects in the Theory of Consumers' Demand" (1950). Applied to product decisions by Marty Cagan, "Inspired" (2018). -->

**6. IKEA Effect**
- What it is: Overvaluing things you built yourself, regardless of objective quality
- Detection signals: Internal solution preferred over better alternatives, "not invented here" resistance, reluctance to kill own features
- Debiasing: Get external perspective. Ask: "Would we buy/adopt this if someone else built it?"

<!-- Source: Norton, Mochon & Ariely, "The IKEA Effect: When Labor Leads to Love" (2012). Harvard Business School. -->

#### Biases in Estimation

**7. Planning Fallacy**
- What it is: Underestimating time, cost, and risk while overestimating benefits
- Detection signals: Best-case timelines presented as expected, no risk buffer, optimistic assumptions treated as baseline
- Debiasing: Use reference class forecasting. Ask: "How long did similar projects actually take?"

<!-- Source: Kahneman & Tversky (1979). Expanded by Bent Flyvbjerg, "Survival of the Unfittest" (2009) — systematic analysis of planning fallacy in large projects. -->

**8. Survivorship Bias**
- What it is: Learning only from successes while ignoring failures
- Detection signals: Case studies only from successful companies, "Company X did this and succeeded", no analysis of companies that tried and failed
- Debiasing: Ask: "Who else tried this and failed? Why?" Seek disconfirming examples.

<!-- Source: Abraham Wald's WWII aircraft armor analysis (1943) — examining bullet holes on returning planes, realizing you need to armor where there AREN'T holes. Applied to business by Nassim Taleb, "Fooled by Randomness" (2001). -->

#### Biases in Decision-Making

**9. Status Quo Bias**
- What it is: Preferring the current state simply because it's familiar, even when change would be beneficial
- Detection signals: "It's working fine", resistance framed as risk avoidance, change requires justification but inaction doesn't
- Debiasing: Ask: "If we weren't already doing it this way, would we choose to start?" Apply same scrutiny to inaction as to action.

<!-- Source: Samuelson & Zeckhauser, "Status Quo Bias in Decision Making" (1988). Related to loss aversion: losses from change loom larger than gains. -->

**10. Dunning-Kruger Effect**
- What it is: Overestimating competence in areas where you have limited expertise
- Detection signals: High confidence despite limited domain experience, dismissing expert input, "how hard can it be" attitude
- Debiasing: Identify domain experts and defer to their estimates. Ask: "Who has done this before? What do they think?"

<!-- Source: Kruger & Dunning, "Unskilled and Unaware of It" (1999). Cornell University. The gap between perceived and actual competence is widest at low competence levels. -->

### Severity Scoring

<!-- Source: Risk assessment matrix approach adapted from ISO 31000 risk management standard. Impact x Likelihood applied to cognitive bias detection. -->

| Severity | Criteria | Action |
|----------|----------|--------|
| **Critical** | Bias likely distorting the core decision; could lead to significant resource waste or missed opportunity | Must address before proceeding |
| **Moderate** | Bias present but affects secondary aspects; decision is still directionally sound | Address within current cycle |
| **Low** | Bias detected but impact is minimal; mainly a thinking hygiene issue | Note for awareness |

### The WRAP Debiasing Protocol

<!-- Source: Chip Heath & Dan Heath, "Decisive" (2013). WRAP is a practical four-step process that directly counters the four most common decision-making villains: narrow framing, confirmation bias, short-term emotion, and overconfidence. -->

After detecting biases, apply the WRAP framework:

1. **Widen Your Options**: Are we trapped in a narrow frame? Have we considered at least 3 options? (Counters: Confirmation Bias, Status Quo Bias)
2. **Reality-Test Your Assumptions**: Have we sought disconfirming evidence? Have we consulted outside experts? (Counters: Anchoring, Availability, Survivorship)
3. **Attain Distance Before Deciding**: Are short-term emotions driving us? What would our successor do? (Counters: Sunk Cost, IKEA Effect)
4. **Prepare to Be Wrong**: Do we have a pre-mortem? Are re-decision triggers defined? (Counters: Planning Fallacy, Dunning-Kruger, Bandwagon)

## Output Structure

```markdown
# Bias Check: [Decision/Document Title]

**Date**: [YYYY-MM-DD]
**Analyst**: [Name/Role]
**Subject**: [What was analyzed — decision record, PRD, strategy doc, etc.]
**Related**: [DR-YYYY-NNN, SB-YYYY-NNN, or document path]

## Summary

**Biases detected**: [N] ([N critical, N moderate, N low])
**Overall risk**: [High / Medium / Low] — [One sentence on the biggest concern]
**WRAP score**: [X/4 steps adequately covered in the original decision]

## Bias Findings

### [Bias Name] -- [Severity: Critical/Moderate/Low]

**Where detected**: [Quote or reference to specific section/claim]
**Evidence**: [Why this looks like [bias name]]
**Impact**: [What could go wrong if this bias goes unchecked]
**Debiasing recommendation**: [Specific action to counter this bias]

### [Bias Name] -- [Severity: Critical/Moderate/Low]

...

## Biases NOT Detected

| Bias | Status | Notes |
|------|--------|-------|
| Confirmation Bias | Not detected | [Brief reason — e.g., "Multiple viewpoints cited"] |
| Anchoring | Not detected | [Brief reason] |
| ... | ... | ... |

## WRAP Assessment

| Step | Status | Finding |
|------|--------|---------|
| **W**iden Options | [Adequate / Weak / Missing] | [Were multiple options genuinely considered?] |
| **R**eality-Test | [Adequate / Weak / Missing] | [Was disconfirming evidence sought?] |
| **A**ttain Distance | [Adequate / Weak / Missing] | [Was emotional distance maintained?] |
| **P**repare to Be Wrong | [Adequate / Weak / Missing] | [Are failure modes and re-decision triggers defined?] |

## Recommendations

### Critical Actions (Before Proceeding)
1. [Action to address critical biases]

### Improvements (This Cycle)
1. [Action to address moderate biases]

### Awareness Items
1. [Notes on low-severity findings]

## Decision Owner Action

- [ ] Review critical bias findings
- [ ] Apply debiasing recommendations
- [ ] Update decision record if warranted
- [ ] Consider `/decision-quality-audit` for systematic review
```

## Instructions

1. **This skill analyzes an existing decision or document.** It does not make decisions. The output is a diagnostic, not a prescription.
2. Require the user to provide the decision/document to check. Accept inline text, `@file.md` references, or decision record IDs.
3. Be specific about WHERE each bias appears. Quote or reference exact claims.
4. Not every bias will be present. Report "not detected" for biases you checked but didn't find. This builds trust in the findings.
5. Severity must be justified, not arbitrary. Explain the potential impact.
6. The WRAP assessment provides a holistic view beyond individual biases.
7. Save bias checks alongside the decision they analyze (e.g., `decisions/bias-check-DR-2026-003.md`).
8. Offer to update the original decision record if critical biases are found.

## Integration

- Feeds from: `/decision-record`, `/strategic-bet`, `/prd`, any decision document
- Feeds into: `/decision-quality-audit` (systematic quality improvement), `/compound` (learning from bias patterns)
- Related to: `/commitment-check` (pre-commitment validation), `/context-recall` (finding past decisions for comparison)
- Can trigger: Updates to decision records, additional stakeholder consultation

## Vision to Value Operating Principle

> "The most dangerous biases are the ones you don't know you have. A bias check is not a judgment on the decision-maker -- it's a gift of perspective."
