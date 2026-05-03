---
name: messaging-architecture
description: 'Author or critique a three-tier messaging architecture — Tier 1 category claim (CMO-owned), Tier 2 buyer shortlist claim (PMM-Dir-owned), Tier 3 evaluator capability proof points (PMM-owned with Product Manager input) — as a standalone artifact split out from positioning so the message hierarchy is auditable and ownable on its own. Activate when: "messaging architecture", "message hierarchy", "three-tier messaging", "tier 1 / tier 2 / tier 3 messaging", "category message vs buyer message", standalone message hierarchy artifact, splitting messaging out of positioning Do NOT activate for: positioning statement (/positioning-statement), launch narrative brief (/launch-narrative-brief), campaign brief (/campaign-brief), competitive battlecard (/competitive-battlecard)'
argument-hint: '[product or release name] or [update path/to/messaging.md] or [critique path/to/draft.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: product-marketing
  skill_type: task-capability
  owner: director-product-marketing
  sensitive: false
  primary_consumers:
  - pmm-dir
  - director-product-marketing
  - pmm
  - product-marketing-manager
  - cmo
  - marketing-dir
  secondary_consumers:
  - content-strategist
  - copywriter
  - pr-comms-specialist
  - sales-engineer
  - sales-dir
  - ci
  - competitive-intelligence
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Critique**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "critique", "review my messaging", "audit this" + draft path | CRITIQUE | 100% |
| "update", "revise" in input + path | UPDATE | 100% |
| File path provided (`@path/to/messaging.md`) without critique signal | UPDATE | 100% |
| "create", "new", "draft" in input | CREATE | 100% |
| "the messaging", "our message hierarchy" | UPDATE | 85% |
| Just product or release name | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user.

### Mode Behaviors

**CREATE**: Walk the user through the three tiers in canonical order. For each tier surface the prompt question, accept the answer (or explicit deferral with reason), and assess against the tier's quality bar before moving on. Output a structured artifact at `messaging/[product-or-release-slug]-architecture.md`.

**UPDATE**: Read existing artifact, identify which tier the user is updating, preserve unchanged tiers, re-assess updated tier against the quality bar, show diff and version bump. If a tier owner is changed, require explicit acceptance from the new owner before the update lands.

**CRITIQUE**: Read the supplied draft, walk Tiers 1 / 2 / 3, return a structured findings list with severity tags (P0 blocker / P1 important / P2 nice-to-have), per-tier diagnosis, and the named gap to close. Do not edit the draft.

### Search Locations for Messaging Architecture

- `messaging/`
- `marketing/messaging/`
- `gtm/messaging/`
- `positioning/`

---

## Vision to Value Phase

**Phase 2: Strategic Decisions** — messaging architecture is a strategy formulation artifact. It sits downstream of `/positioning-statement` (which establishes the category frame) and upstream of `/launch-narrative-brief` Field 2 (which consumes the three-tier shape as part of a release-shaped commitment). The architecture is also consumed by `/campaign-brief`, `/sales-enablement`, and `/competitive-battlecard` as the canonical message hierarchy those execution-altitude artifacts inherit from.

**Prerequisites**: a current `/positioning-statement` for the product. Tier 1 and Tier 2 inherit from positioning; without a positioning statement, the architecture has no anchor.

**Outputs used by**: `/launch-narrative-brief` (consumes the three tiers as Field 2 of the brief), `/campaign-brief` (inherits the message hierarchy as a constraint), `/sales-enablement` (Tier 3 capability claims become the load-bearing content of battlecards and discovery guides), `/press-release-faq` (Tier 1 category claim sets the press-release headline frame), `/competitive-battlecard` (Tier 3 evaluator claims provide the verifiable capability set).

**Operating principle**: messaging is a strategic choice, not a collateral exercise. A message hierarchy without a named owner on each tier drifts to whoever writes the collateral first — which is exactly the failure mode this artifact exists to prevent.

---

## Why messaging architecture is a separate artifact

Three-tier messaging used to live as a section inside `/positioning-statement`. That co-location had two failure modes. First, the message hierarchy was edited every time positioning was touched, even when the underlying category frame was stable — which meant the hierarchy could not be audited independently of the positioning. Second, the three tiers carried different owners (Tier 1 is CMO-owned at category altitude; Tier 2 is PMM-Dir-owned at buyer altitude; Tier 3 is PMM-owned with PM input at evaluator altitude), and bundling them inside a single positioning statement collapsed the ownership distinction. A change to Tier 1 would land without CMO sign-off, a change to Tier 3 would land without PM input, and the empowerment-tier discipline that the three altitudes are meant to enforce evaporated.

Splitting messaging architecture out of positioning solves both. The hierarchy is now its own auditable, ownable artifact. Each tier names its owner explicitly. A change to a tier requires re-sign-off from that tier's owner, not from positioning's author. And the architecture can be consumed by downstream skills (`/launch-narrative-brief`, `/campaign-brief`, `/sales-enablement`) as a single source of truth for the message hierarchy without dragging the full positioning document along with it.

The relationship to `/positioning-statement` is upstream. Positioning establishes the category frame, the differentiation axis, and the target customer characteristics. Messaging architecture takes those as input and operationalises them as three altitude-calibrated messages with three named owners. Positioning is the strategic context; messaging architecture is the audience-altitude commitment. Both artifacts must exist before any execution-altitude collateral can be authored.

---

## The three tiers

Canonical order: Tier 1, Tier 2, Tier 3. The order is the order they are authored in, top-down from category altitude to evaluator altitude. Each tier inherits constraint from the tier above it. A Tier 3 claim that contradicts the Tier 1 category frame is a Tier 3 claim that needs to be revised — or a signal that the Tier 1 frame itself is the one to revisit.

---

### Tier 1 — Market-level category claim

**What it captures.** One sentence describing the category move the product is making. The audience is trade press, analyst community, and corporate brand. The message lands in headlines, in analyst category-definition reports, and in the buyer's pre-shortlist mental category map. Owned by the Chief Marketing Officer, because the category frame is the corporate brand commitment, not a release-level commitment.

**Why it matters.** Without a Tier 1 category claim, the product has no defensible position at trade-press altitude. Reporters and analysts categorise products by the category claims their marketing makes; absent a Tier 1 message, they categorise by whatever they pattern-match the product to, which is rarely the category the product wants to be in. The Tier 1 claim is also what shapes the buyer's pre-shortlist category map — the mental sorting that happens before any specific product is even evaluated. A product that is not pre-sorted into the buyer's intended category is a product that does not get shortlisted at all.

**Prompt question.** "What is the one-sentence Tier 1 message that lands at category altitude — the message a trade-press reporter would put in the headline and an analyst would put in the category-definition report? Who is the named owner (typically the Chief Marketing Officer)?"

**Quality bar.** A strong Tier 1 makes a category claim that is specific enough to be defensible. "Compliance posture is the new buying criterion in mid-market healthcare software" is a Tier 1 — it names a category move and a market segment. A weak Tier 1 says "we are the leader in our space" (no defensible category claim), or says "we are better at X" (a Tier 2 buyer message dressed up as a category claim), or says "our customers love us" (no claim at all). The single most common Tier 1 failure is collapsing it into a Tier 2 buyer claim, which loses the category-altitude frame.

**Example output.**
> *Tier 1 — Category altitude.*
> Owner: [Chief Marketing Officer name].
> Message: "Compliance posture is the new buying criterion in mid-market healthcare software."

---

### Tier 2 — Differentiation versus the named alternative

**What it captures.** One sentence describing why the buyer should shortlist this product against the named alternatives identified in `/positioning-statement` Step 1 and in `/launch-narrative-brief` Field 3. The audience is the buyer authoring the procurement memo. The message lands in the evaluation memo's shortlist rationale paragraph. Owned by the Director of Product Marketing, because differentiation against named alternatives is Product Marketing's positioning commitment.

**Why it matters.** Buyers do not shortlist on Tier 1 category claims; they shortlist on Tier 2 differentiation claims. The Tier 2 message is what survives first contact with the buyer's procurement memo. A product whose Tier 2 message is generic ("we are the most innovative") gets cut from the shortlist on the first comparison question. A Tier 2 message that names the alternative and the differentiation axis explicitly — "the only X platform that ships Y without Z" — is a message a buyer can defend in their internal shortlist conversation.

**Prompt question.** "What is the one-sentence Tier 2 message a buyer should carry into their procurement memo's shortlist rationale? Name the alternative and the differentiation axis explicitly. Who is the named owner (typically the Director of Product Marketing)?"

**Quality bar.** A strong Tier 2 makes a shortlist claim that explicitly names or implies the alternative being differentiated against, and names the axis on which differentiation is claimed. "[Product] is the only [category] platform that ships HIPAA-attested controls without a six-week security review cycle" is a Tier 2 — it names the differentiation axis (attestation depth + security-review compression) and implies the alternative (the platforms that require the six-week cycle). A weak Tier 2 makes a generic claim ("the most innovative platform"), claims differentiation on an axis the alternative is actually stronger on, or claims differentiation on every axis (which collapses to no axis).

**Example output.**
> *Tier 2 — Buyer altitude.*
> Owner: [Director of Product Marketing name].
> Message: "[Product] is the only [category] platform that ships HIPAA-attested controls without a six-week security review cycle."

---

### Tier 3 — Capability proof points

**What it captures.** Three to five sentences enumerating the specific capabilities an evaluator can verify during a bake-off. The audience is the technical evaluator running the proof-of-concept or the request-for-proposal response. The messages land in the evaluator's capability checklist and in the comparison matrix the evaluator builds. Owned by Product Marketing, with input from Product Management — because the capability claims are Product Marketing's positioning commitment, but the underlying capabilities are Product Management's delivery commitment.

**Why it matters.** Evaluators choose products based on Tier 3 capability claims, not on Tier 1 category claims or Tier 2 shortlist claims. The Tier 3 messages are what survive the bake-off. A product that wins on Tier 1 and Tier 2 but loses on Tier 3 capability claims is a product that loses the deal at the proof-of-concept stage. The three-to-five count is deliberate: more than five claims dilutes the load-bearing ones; fewer than three leaves gaps in the comparison matrix the evaluator builds. The Product Management input is structural: capability claims that Product Management has not signed off on are claims that will collapse the first time the evaluator asks the engineering team to verify them.

**Prompt question.** "Name three to five specific capability claims an evaluator can verify during a bake-off. Each claim should be tied to a unique attribute from `/positioning-statement` Step 2. Name the Product Marketing owner and the Product Manager who signs off on the underlying capability."

**Quality bar.** A strong Tier 3 has three to five claims, each tied to a unique attribute from the positioning statement, each verifiable by the evaluator without sales involvement, and each signed off on by the Product Manager who owns the capability. "Native HIPAA Business Associate Agreement signing in the workspace, with a 14-day onboarding window" is a Tier 3 claim — specific, verifiable, tied to an attribute. A weak Tier 3 has more than five claims (dilution), claims that are not verifiable without Sales-led demos (which means they are Tier 2 claims dressed up as Tier 3), or claims that Product Management has not signed off on (which means they will collapse on engineering verification).

**Example output.**
> *Tier 3 — Evaluator altitude.*
> Owner: [Product Marketing Manager name], with input from [Product Manager name].
> 1. Native HIPAA Business Associate Agreement signing in the workspace, with a 14-day onboarding window.
> 2. Audit log export to evaluator's existing Security Information and Event Management system in CEF format, no integration work required.
> 3. Single-sign-on through the evaluator's existing identity provider via SAML 2.0, configurable in the workspace administration console.
> 4. [Optional fourth claim if the release warrants.]
> 5. [Optional fifth claim — do not exceed five.]

---

## Output Structure

```markdown
# Messaging Architecture: [Product or Release Name]

**Architecture ID**: MA-[YYYY]-[NNN]
**Product**: [Product name]
**Status**: Draft / In Review / Signed / In Effect
**Date authored**: [YYYY-MM-DD]
**Upstream positioning**: [Path to /positioning-statement output]
**Downstream consumers**: [List of skills consuming this architecture — typically /launch-narrative-brief, /campaign-brief, /sales-enablement]

---

## Tier 1 — Category altitude

**Owner**: [Chief Marketing Officer name]
**Sign-off date**: [YYYY-MM-DD]
**Message**: "[One sentence category claim.]"
**Source attribute** (from `/positioning-statement` Step 5): [Category name]
**Quality bar pass**: yes / weak / fail

## Tier 2 — Buyer altitude

**Owner**: [Director of Product Marketing name]
**Sign-off date**: [YYYY-MM-DD]
**Message**: "[One sentence shortlist claim, naming the differentiation axis.]"
**Source alternative** (from `/positioning-statement` Step 1): [Named alternative]
**Source attribute** (from `/positioning-statement` Step 2): [Unique attribute]
**Quality bar pass**: yes / weak / fail

## Tier 3 — Evaluator altitude

**Owner**: [Product Marketing Manager name], with input from [Product Manager name]
**Sign-off date** (PMM): [YYYY-MM-DD]
**Sign-off date** (PM): [YYYY-MM-DD]
**Capability claims**:
1. [Claim 1 — tied to attribute X from `/positioning-statement` Step 2]
2. [Claim 2 — tied to attribute Y]
3. [Claim 3 — tied to attribute Z]
4. [Optional claim 4]
5. [Optional claim 5 — do not exceed five]
**Quality bar pass**: yes / weak / fail

---

## Cross-tier integrity check

- [ ] Tier 1 makes a defensible category claim (not a Tier 2 buyer claim dressed up)
- [ ] Tier 2 names or implies the alternative and the differentiation axis
- [ ] Tier 3 has three to five claims, each tied to a unique attribute from positioning
- [ ] Tier 1, 2, 3 do not contradict each other (a Tier 3 claim that undermines the Tier 1 frame is a signal one of the two needs to be revised)
- [ ] All three tiers have named owners with explicit sign-off
```

---

## Critique-mode output structure

When invoked in Critique mode against a draft, return:

```markdown
# Critique: [Architecture title or path]

**Verdict**: GO / GO WITH CHANGES / NEEDS REWORK

## P0 Findings (Blocker — architecture cannot be signed without resolving)
- **Tier [N]**: [What is missing or weak.] [Why it blocks sign-off.] [The named gap to close.]

## P1 Findings (Important — should be resolved before sign-off)
- **Tier [N]**: [Diagnosis.] [Suggested close.]

## P2 Findings (Nice-to-have — author's discretion)
- **Tier [N]**: [Diagnosis.]

## Cross-tier integrity
- Tier 1 ↔ Tier 2: [aligned / weak / contradictory]
- Tier 2 ↔ Tier 3: [aligned / weak / contradictory]
- Tier 1 ↔ Tier 3: [aligned / weak / contradictory]

## Quality bar score
- Tier 1: pass / weak / missing
- Tier 2: pass / weak / missing
- Tier 3: pass / weak / missing
- **Total**: [N]/3 passing
```

---

## Cross-references

| Skill | Relationship |
|-------|--------------|
| `/positioning-statement` | Upstream — provides the category, alternatives, and unique attributes the three tiers inherit from |
| `/launch-narrative-brief` | Downstream — Field 2 of the brief consumes the three-tier shape as a release-shaped commitment |
| `/campaign-brief` | Downstream — inherits the message hierarchy as a campaign constraint |
| `/sales-enablement` | Downstream — Tier 3 capability claims become the load-bearing content of battlecards and discovery guides |
| `/competitive-battlecard` | Downstream — Tier 3 capability claims provide the verifiable capability set on the battlecard |
| `/press-release-faq` | Downstream — Tier 1 category claim sets the press-release headline frame |
| `/decision-record` | Adjacent — used to record sign-off reasoning when a tier owner change sets precedent |

---

## Instructions

1. **Detect the mode** (Create / Update / Critique) using the table above. If confidence is below 70 percent, ask.
2. **In Create mode**, walk Tier 1 → Tier 2 → Tier 3 in canonical order. Surface the prompt question. Accept the answer or explicit deferral with reason. Assess against the quality bar before moving on.
3. **Read `/positioning-statement` first** if a positioning artifact exists. Tier 1 inherits from positioning's category (Step 5); Tier 2 inherits from positioning's differentiation (Step 2) against named alternatives (Step 1); Tier 3 inherits from positioning's unique attributes (Step 2). If positioning does not exist, surface that as a prerequisite gap and ask whether to author positioning first.
4. **Each tier requires a named owner.** Do not accept a tier without an owner. The empowerment-tier discipline only holds when each altitude has a named accountable signatory.
5. **In Update mode**, preserve unchanged tiers exactly. If a tier's owner is changing, require explicit acceptance from the new owner — old sign-off does not transfer.
6. **In Critique mode**, do not edit. Produce structured findings with severity tags. Verdict at top.
7. **Save outputs** to `messaging/[product-or-release-slug]-architecture.md`.
8. **Tag with an Architecture ID** of the form `MA-[YYYY]-[NNN]` for context-graph linkage.
9. **Cross-reference upstream positioning** by file path or document identifier in the artifact's metadata. An architecture without an upstream positioning trace is an architecture without context.

---

## Gotchas

- This is not positioning. `/positioning-statement` establishes category, alternatives, attributes, value, target customer; messaging architecture operationalises three of those (category, alternatives, attributes) as audience-altitude messages.
- Tier 1 is not a tagline. Taglines are corporate brand artifacts; Tier 1 is a category claim with defensible content.
- Tier 2 must name or imply the alternative. A Tier 2 message that does not differentiate against a named alternative is a Tier 2 message that will not survive the buyer's procurement memo.
- Tier 3 caps at five claims. More than five dilutes the load-bearing ones; aim for three or four unless the release genuinely warrants five.
- Each tier has one owner. Co-ownership across tiers is the path to no ownership in practice. The empowerment-tier discipline depends on a single named accountable signatory per altitude.
- A Tier 3 claim that Product Management has not signed off on is a claim that will collapse on engineering verification. Always name the Product Manager input, not just the Product Marketing owner.
