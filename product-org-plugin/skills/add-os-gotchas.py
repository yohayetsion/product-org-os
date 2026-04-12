"""
Phase 4: Add Gotchas to OS plugin skills + add context:fork to heavy skills.

Inserts Gotchas after the Document Intelligence section (or after frontmatter for non-document skills).
Adds context:fork to frontmatter of heavy analytical skills.
"""

import os
import re
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

SKILLS_DIR = r"G:\My Drive\Claude\Product Org OS\product-org-plugin\skills"

# Gotchas for top 30+ skills, grouped by category
SKILL_GOTCHAS = {
    # === Tier 1: Most-used document generators ===
    "prd": [
        "Never invent user counts, revenue projections, or market size — use [TBD] placeholders",
        "Success criteria must be measurable — reject vague 'improve user experience' or 'better performance'",
        "Problem statement must be from customer perspective with evidence, not internal assumptions",
        "Scope boundaries (in/out) must be explicit — ambiguity in scope is the #1 cause of scope creep",
    ],
    "feature-spec": [
        "Never invent implementation estimates (effort, timelines, sprint counts) — that's engineering's job",
        "Acceptance criteria must be testable — 'Given/When/Then' format preferred",
        "Each feature spec needs a single owner, not a committee",
    ],
    "user-story": [
        "User stories must follow 'As a [type], I want [action], so that [benefit]' — don't skip the 'so that'",
        "Acceptance criteria are mandatory — a user story without them is just a wish",
        "Don't combine multiple stories into one — split until each is independently deliverable",
    ],
    "strategic-bet": [
        "Never invent market size, growth projections, or ROI estimates — use [TBD] or cite sources",
        "Assumptions must be numbered and explicitly testable — vague assumptions are unfalsifiable",
        "Re-decision triggers must be specific and observable, not subjective ('if it doesn't work')",
        "Every bet must state what we're NOT doing (opportunity cost)",
    ],
    "decision-record": [
        "Always document at least 2-3 alternatives considered — a decision with no alternatives wasn't a decision",
        "Single accountable owner required — never 'the team' or 'leadership'",
        "Re-decision triggers must be specific events or thresholds, not calendar dates",
    ],
    "market-analysis": [
        "Never fabricate TAM/SAM/SOM numbers — use cited sources or [TBD]",
        "Market growth rates require attribution — don't present analyst projections as your own analysis",
        "Competitive positioning must be evidence-based, not aspirational",
    ],
    "competitive-landscape": [
        "Competitor information must be current — stale competitive intel is worse than none",
        "Never assume competitor pricing without verification — check their website or cite sources",
        "Feature comparison must be fact-based — don't downplay competitors or inflate own capabilities",
    ],
    "competitive-analysis": [
        "Head-to-head comparisons must be fair — use the same evaluation criteria for both sides",
        "Win/loss data must come from actual deals, not assumptions about why customers chose competitors",
        "Never fabricate market share percentages — cite sources or say 'not available'",
    ],
    "business-case": [
        "Never fabricate financial projections (revenue, costs, ROI) — provide frameworks with [TBD] inputs",
        "Sensitivity analysis must test key assumptions — a business case with only one scenario is fiction",
        "Opportunity cost must be stated — what are we NOT investing in if we do this?",
    ],
    "positioning-statement": [
        "Positioning must be based on real differentiation, not aspirational claims",
        "Target audience must be specific enough to exclude some customers — 'everyone' is not a segment",
        "Competitive frame of reference must name real alternatives the customer considers",
    ],
    "gtm-strategy": [
        "Sales motion must match customer buying behavior — don't default to 'enterprise sales' without evidence",
        "Launch timeline must be realistic — don't compress arbitrary dates without flagging risks",
        "Never invent conversion rates or CAC/LTV numbers — use industry benchmarks with attribution or [TBD]",
    ],
    "launch-plan": [
        "Launch dates should be working backward from readiness criteria, not arbitrary deadlines",
        "Cross-functional dependencies must be mapped — marketing, sales, support, engineering",
        "Success metrics must be defined before launch, not after — post-hoc metrics are cherry-picked",
    ],
    "product-roadmap": [
        "Roadmap themes must connect to strategic bets — features without strategic alignment are noise",
        "Confidence levels decrease with distance — 'Now' is high confidence, 'Later' is directional only",
        "Never commit to specific dates in the 'Later' horizon — use quarters or 'H2' at most",
    ],
    "pricing-strategy": [
        "Never fabricate willingness-to-pay data or price sensitivity analysis — use research or [TBD]",
        "Pricing must consider competitive alternatives — customers always have an alternative (including doing nothing)",
        "Price changes have irreversible effects on positioning — raising prices is easier than recovering from underpricing",
    ],

    # === Tier 2: Assessment frameworks ===
    "swot-analysis": [
        "Strengths and Weaknesses are INTERNAL — Opportunities and Threats are EXTERNAL. Don't mix them.",
        "Each item must be specific and evidence-based — reject vague entries like 'strong brand' without evidence",
        "TOWS strategy matrix must generate actionable strategies, not restatements of the SWOT items",
    ],
    "porter-five-forces": [
        "Each force must be rated with evidence, not gut feeling — cite market data or examples",
        "Don't ignore substitute threats — the biggest competitive threat often comes from outside the industry",
        "Buyer power and supplier power depend on concentration — analyze the actual numbers, not assumptions",
    ],
    "pestle-analysis": [
        "Each factor must be specific to the industry/region — generic macro trends add no value",
        "Political and Legal are different categories — don't conflate government policy with regulation",
        "Time horizon matters — state whether each factor is immediate, medium-term, or long-term",
    ],
    "blue-ocean": [
        "Value curves must be based on real customer data, not what the company thinks customers value",
        "Blue Ocean strategy is about creating new demand, not stealing share — don't confuse with competitive strategy",
        "Eliminate-Reduce-Raise-Create framework must have items in ALL four quadrants — an incomplete ERRC is a regular strategy",
    ],
    "bcg-matrix": [
        "Market growth rate and relative market share must come from data, not assumptions",
        "BCG matrix is for portfolio analysis — don't apply it to individual features or products without market data",
        "Star/Cash Cow/Question Mark/Dog labels should inform strategy, not just categorize",
    ],
    "ansoff-matrix": [
        "Market penetration strategies must be distinct from new market development — same product, new segment is development",
        "Diversification is the highest-risk quadrant — flag it explicitly and require strong justification",
        "Each quadrant should have specific initiatives, not just strategic intent",
    ],
    "lean-canvas": [
        "Problem/Solution fit must be validated, not assumed — lean canvas is a hypothesis, not a plan",
        "Key metrics should be actionable (not vanity metrics) — 'users' is vague, 'weekly active users' is better",
        "Unfair advantage must be genuinely hard to copy — 'great team' and 'passion' are not unfair advantages",
    ],
    "business-model-canvas": [
        "Revenue streams must be specific — 'subscriptions' is a model, not a stream. What subscriptions, at what price?",
        "Key partnerships must include what each party contributes and receives — one-sided partnerships fail",
        "Cost structure should distinguish fixed vs. variable costs — this affects scaling strategy",
    ],
    "dhm-analysis": [
        "Delight, Hard-to-Copy, and Margin-Enhancing must each have specific evidence — not just checkboxes",
        "Hard-to-copy must be genuinely defensible — 'first mover advantage' is rarely defensible long-term",
    ],
    "growth-model": [
        "Never fabricate growth rates, conversion funnels, or viral coefficients — use frameworks with [TBD]",
        "Growth loops are theoretical until validated — don't present models as projections",
        "Acquisition channel costs must be current — CAC on any platform changes quarter to quarter",
    ],

    # === Tier 3: Validators ===
    "commitment-check": [
        "Never approve a commitment without verifying Phase 1-2 deliverables actually exist — check file paths",
        "Single accountable owner is mandatory — escalate if ownership is shared or unclear",
        "Resource commitment without capacity verification is a promise that can't be kept",
    ],
    "ownership-map": [
        "Every deliverable must have exactly ONE owner — co-ownership is no ownership",
        "Accountability gaps (no owner) are P0 findings — flag immediately",
        "Owner must have authority to make decisions, not just responsibility to do work",
    ],
    "customer-value-trace": [
        "Value must trace from customer need to feature to outcome — breaks in the chain mean the feature may not deliver value",
        "Customer evidence must be from actual customers, not internal assumptions about what customers want",
    ],
    "collaboration-check": [
        "Cross-functional handoffs are where value leaks — focus analysis on transition points",
        "Collaboration is not 'more meetings' — look for structural alignment, not communication volume",
    ],
    "scale-check": [
        "Process recommendations must match organizational maturity — Level 1 orgs need lightweight processes",
        "Scalability is not about size — it's about whether processes work as the organization grows",
    ],
    "phase-check": [
        "Phase transitions require exit criteria from previous phase — don't skip phases without acknowledging it",
        "Phase 2→3 is the commercial filter — not everything passes. Flag questionable viability explicitly.",
    ],
    # === Other important skills ===
    "stakeholder-map": [
        "Power and influence assessments must be evidence-based, not assumptions about job titles",
        "Stakeholder positions can change — stakeholder maps need refresh dates",
    ],
    "north-star-metric": [
        "North Star must be a customer-value metric, not a revenue metric — revenue is a lagging indicator",
        "Input metrics must be actionable by teams — metrics nobody can influence are useless",
    ],
    "press-release-faq": [
        "The press release is a forcing function for clarity, not actual marketing copy",
        "Customer quotes must represent what customers would ACTUALLY say, not marketing speak",
        "FAQs should include the hard questions leadership would ask, not softball questions",
    ],
    "pretotype": [
        "Pretotypes test demand, not usability — the question is 'would anyone want this?' not 'can they use it?'",
        "Results must be quantified (conversion rate, signup count) — qualitative pretotype results are anecdotes",
    ],
    "experiment-design": [
        "Hypothesis must be falsifiable — 'users will like this' is not testable, 'signup rate will increase by 10%' is",
        "Sample size must be estimated before running — experiments without power analysis are coin flips",
        "Success criteria must be defined before the experiment, not after seeing results",
    ],
    "prioritize-features": [
        "Prioritization criteria must be stated explicitly — different frameworks (RICE, Kano, MoSCoW) give different results",
        "Never fabricate reach, impact, or confidence scores — use data or explicitly label as team estimates",
        "Prioritization without strategic alignment is just sorting — connect to strategic bets",
    ],
    "retrospective": [
        "Focus on systemic improvements, not individual blame — 'who' is less important than 'why'",
        "Action items from retros must have owners and deadlines — retros without follow-through are therapy sessions",
    ],
    "outcome-review": [
        "Distinguish outputs (what we shipped) from outcomes (what changed for customers) — shipping is not success",
        "Compare actual results to original success criteria — don't move the goalposts after the fact",
    ],
    "interview-synthesis": [
        "Direct quotes are evidence; your interpretation is analysis — keep them separate",
        "Sample size matters — always state how many interviews inform each finding",
        "Don't over-generalize from passionate outliers — frequency matters more than volume of feedback",
    ],
    "assumption-map": [
        "Assumptions must be falsifiable — 'the market will grow' is too vague, 'TAM will exceed $1B by 2027 (source: X)' is testable",
        "High-risk assumptions (high impact, low certainty) must have validation plans",
    ],
    "four-risks-check": [
        "Value risk, usability risk, feasibility risk, and viability risk must each be assessed independently",
        "Don't conflate technical feasibility with business viability — both must pass separately",
    ],
}

# Skills that should get context:fork in frontmatter
CONTEXT_FORK_SKILLS = [
    "market-analysis",
    "competitive-landscape",
    "competitive-analysis",
    "business-case",
    "prd",
    "pestle-analysis",
    "porter-five-forces",
    "business-plan",
    "competitive-battlecard",
]


def add_gotchas_to_skill(content, gotchas):
    """Insert Gotchas after Document Intelligence section, or after frontmatter if no DI."""
    # Try after Document Intelligence
    # Look for the end of DI section (usually ends with "---" before the template)
    di_end = re.search(r'(### Search Locations.+?\n---)', content, re.DOTALL)
    if di_end:
        insert_at = di_end.end()
    else:
        # Try after Mode Behaviors section
        di_end2 = re.search(r'(### Mode Behaviors.+?\n---)', content, re.DOTALL)
        if di_end2:
            insert_at = di_end2.end()
        else:
            # Try after the first --- after Document Intelligence
            di_start = re.search(r'## Document Intelligence', content)
            if di_start:
                next_sep = re.search(r'\n---\n', content[di_start.end():])
                if next_sep:
                    insert_at = di_start.end() + next_sep.end()
                else:
                    insert_at = None
            else:
                # No Document Intelligence — insert after frontmatter
                fm_end = content.find('---\n', content.find('---\n') + 4)
                if fm_end > 0:
                    insert_at = fm_end + 4
                else:
                    insert_at = None

    if insert_at is None:
        return content, False

    gotchas_md = "\n## Gotchas\n\n"
    for g in gotchas:
        gotchas_md += f"- {g}\n"
    gotchas_md += "\n"

    content = content[:insert_at] + gotchas_md + content[insert_at:]
    return content, True


def add_context_fork(content):
    """Add context: fork to frontmatter."""
    if 'context: fork' in content or 'context:fork' in content:
        return content, False

    # Insert before the closing --- of frontmatter
    # Find the second --- (end of frontmatter)
    first = content.find('---')
    if first < 0:
        return content, False
    second = content.find('---', first + 3)
    if second < 0:
        return content, False

    # Insert context: fork before the second ---
    insert = "context: fork\n"
    content = content[:second] + insert + content[second:]
    return content, True


def main():
    skills = sorted([d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))])
    print(f"Found {len(skills)} OS skill directories\n")

    gotchas_added = 0
    fork_added = 0
    gotcha_items = 0

    for skill_name in skills:
        skill_path = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
        if not os.path.exists(skill_path):
            continue

        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()

        changes = []

        # Skip if already has Gotchas
        if '## Gotchas' not in content:
            gotchas = SKILL_GOTCHAS.get(skill_name)
            if gotchas:
                content, success = add_gotchas_to_skill(content, gotchas)
                if success:
                    gotchas_added += 1
                    gotcha_items += len(gotchas)
                    changes.append(f"Added {len(gotchas)} gotchas")
                else:
                    changes.append("FAILED to find insertion point for gotchas")

        # Add context:fork
        if skill_name in CONTEXT_FORK_SKILLS:
            content, success = add_context_fork(content)
            if success:
                fork_added += 1
                changes.append("Added context:fork")

        if changes:
            with open(skill_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {skill_name}: {'; '.join(changes)}")

    print(f"\n{'='*60}")
    print(f"Gotchas added to: {gotchas_added} skills ({gotcha_items} items)")
    print(f"context:fork added to: {fork_added} skills")


if __name__ == "__main__":
    main()
