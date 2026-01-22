# Product Org Plugin for Claude Code

**Your AI-Powered Product Organization at Your Fingertips**

A Claude Code plugin that gives you access to a complete virtual product organization - 13 role-based AI agents who understand product management frameworks, processes, and best practices. Whether you're a solo product professional or part of a large product org, this plugin enhances your work by providing expert assistance at every stage of the product lifecycle.

**Version**: 2.2.0 | **Codename**: V2V Operating System Enhancement

---

## What Is This?

This plugin provides:

- **The `/product` Gateway** - Single entry point to the entire product org. Send any request and the right owners respond with plans, get approval, and execute in parallel.

- **13 Role-Based Agents** - AI assistants that embody specific product org roles (CPO, VP Product, Director PM, Product Manager, Director PMM, PMM, BizOps, Value Realization, Competitive Intelligence, BizDev, Product Operations, UX Lead, Product Leadership Team)

- **56 Skills (Slash Commands)** - Quick access to create complete deliverables like PRDs, Roadmaps, Business Cases, GTM Strategies, and more

- **5 Principle Validators** - Skills that enforce the 8 Operating Principles (`/ownership-map`, `/customer-value-trace`, `/collaboration-check`, `/scale-check`, `/phase-check`)

- **V2V Phase Tracking** - Every skill and initiative maps to the 6-phase "Vision to Value" flow

- **Parallel Agent Execution** - Agents can spawn and coordinate work in parallel for faster, more efficient delivery

- **Dual Output** - Every deliverable generates both a markdown document AND a responsive HTML presentation ready for stakeholders

---

## Quick Start

### Installation

```bash
# From GitHub
claude plugins install github:yohay/product-org-plugin

# Or from the Plugin Registry (once published)
claude plugins install product-org
```

### Your First Command: Use the Gateway

```bash
# Start Claude Code in your project
claude

# Send any request to the product org - the gateway routes it automatically
> /product We need to launch a freemium tier for SMBs

# The gateway will:
# 1. Analyze your request (V2V Phase 2-3, Strategic initiative)
# 2. Identify owners (@vp-product, @bizops, @director-product-marketing)
# 3. Collect plans from each owner
# 4. Present for your approval (you can add guidance)
# 5. Execute in parallel
# 6. Synthesize results
```

### Direct Agent Access

```bash
# Or work directly with specific agents
> @product-manager Create a feature spec for user onboarding.
  See @docs/research/onboarding-interviews.md for user needs
  and @docs/technical/auth-architecture.md for system constraints.
```

The Product Manager agent reads your referenced documents and creates a feature spec that builds on your existing research and technical context.

---

## The `/product` Gateway

The gateway is the **front door** to the entire product organization. It acts like posting to a shared channel where the right people respond.

### How It Works

```
/product [your request or question]

→ Analyzes: V2V phase, RACI owners, complexity
→ Routes: To relevant owners (CPO/PLT for strategic items)
→ Collects: Plans from each owner
→ Approval: You review and can provide guidance
→ Executes: In parallel where possible
→ Synthesizes: Unified results returned
```

### Example

```
/product We need to explore entering the healthcare vertical

→ Analysis: Phase 1 (Strategic Foundation), High complexity
→ Triage: Route through @cpo for strategic alignment
→ Owners:
  - @cpo (Accountable) - Strategic alignment
  - @competitive-intelligence (Responsible) - Market analysis
  - @bizops (Responsible) - Opportunity sizing
  - @director-product-marketing (Consulted) - GTM feasibility
→ Plans collected, presented for approval
→ User: "Focus on <50 employee companies"
→ Parallel execution with guidance applied
→ Comprehensive market entry analysis delivered
```

---

## How It Works: Connecting Agents to Your Business Context

The power of this plugin is that agents work with **your organization's actual documents**. You reference files using Claude Code's `@file` syntax, and agents use that context to produce relevant outputs.

### The Pattern

```
@[agent] [task description].
  See @[path/to/context-doc-1.md] for [what it provides]
  and @[path/to/context-doc-2.md] for [what it provides].
```

### Example: Creating a Business Case

```
> @bizops Create a business case for expanding into healthcare.
  See @strategy/vertical-evaluation.md for our criteria,
  @competitive/healthcare-landscape.md for market analysis,
  and @finance/investment-thresholds.md for approval requirements.
```

**What happens:**
1. The BizOps agent reads all three referenced documents
2. It understands your evaluation criteria, market context, and financial requirements
3. It produces a business case that follows your organization's standards and incorporates your existing analysis

### Example: Coordinating a Launch

```
> @product-operations Coordinate the launch plan for v3.0.
  Feature status is in @pm/feature-readiness-tracker.md,
  marketing timeline in @pmm/q2-campaign-calendar.md,
  and CS training plan in @cs/training-schedule.md.
```

**What happens:**
1. Product Operations agent reads the current status from each team's documents
2. It identifies dependencies and potential conflicts
3. It creates a coordinated launch plan that integrates all workstreams

### Example: Making a Portfolio Decision

```
> @product-leadership-team We need to decide: accelerate mobile or API platform.
  See @decisions/portfolio-criteria.md for how we evaluate,
  @roadmap/mobile-proposal.md and @roadmap/api-proposal.md for the options,
  and @finance/resource-constraints.md for what's available.
```

**What happens:**
1. PLT agent reads your decision criteria and both proposals
2. It understands your resource constraints
3. It structures the decision using your criteria and produces a Decision Record

---

## Your Document Structure

Organize your business documents so agents can reference them effectively:

```
your-project/
├── strategy/
│   ├── strategic-intent.md
│   ├── portfolio-decisions.md
│   └── market-opportunities.md
├── research/
│   ├── customer-interviews.md
│   ├── usability-studies.md
│   └── market-analysis.md
├── roadmap/
│   ├── product-roadmap.md
│   ├── theme-definitions.md
│   └── initiative-briefs.md
├── decisions/
│   ├── decision-records/
│   ├── decision-charters/
│   └── portfolio-criteria.md
├── gtm/
│   ├── positioning.md
│   ├── pricing-strategy.md
│   └── launch-plans/
├── competitive/
│   ├── landscape-analysis.md
│   ├── competitor-profiles/
│   └── battle-cards/
└── finance/
    ├── business-cases/
    ├── financial-models/
    └── investment-criteria.md
```

Agents understand this structure and can reference documents across folders to synthesize information.

---

## Who Is This For?

### For Individual Product Professionals

**You're a PM working solo or on a small team.** You need to wear many hats - strategy, requirements, GTM, pricing, competitive analysis. This plugin gives you expert assistance for every aspect of product work.

**Use Case: Creating a Complete PRD**
```
> @product-manager I need to create a PRD for a new dashboard feature

The PM agent will:
1. Ask clarifying questions about the feature
2. Guide you through problem statement, users, requirements
3. Generate a complete PRD document
4. Create an HTML presentation for stakeholders
```

**Use Case: Preparing for a Pricing Discussion**
```
> @vp-product Help me develop a pricing strategy for our new enterprise tier

The VP Product agent will:
1. Invoke @competitive-intelligence for competitive pricing data
2. Invoke @bizops for financial modeling
3. Create a comprehensive pricing strategy document
4. Generate a presentation deck for the pricing committee
```

### For Product Teams

**You're a Director or VP leading a product team.** You need to scale your impact, maintain consistency, and ensure your team follows best practices.

**Use Case: Quarterly Planning**
```
> @product-leadership-team Let's prepare for Q3 planning. We need to review Q2 outcomes and set Q3 priorities.

The PLT agent will:
1. Invoke @value-realization for Q2 outcome data
2. Invoke @bizops for business performance data
3. Invoke @competitive-intelligence for market updates
4. Create a comprehensive Q3 planning package
5. Generate a QBR presentation
```

**Use Case: New Product Launch**
```
> @cpo We're launching a new product line. Coordinate the full GTM preparation.

The CPO agent will:
1. Invoke @director-product-management for roadmap
2. Invoke @director-product-marketing for GTM strategy
3. Invoke @product-operations for launch plan
4. Coordinate all inputs into a comprehensive launch package
```

### For Entire Product Organizations

**You're building or scaling a product organization.** You need frameworks, consistency, and a way to embed best practices across teams.

**Use Case: Establishing Decision Frameworks**
```
> @product-leadership-team We need to establish a Decision Interface Charter for our monthly portfolio reviews.

The PLT agent will:
1. Create a Decision Interface Charter template
2. Define required inputs from each function
3. Set escalation rules and success criteria
4. Document re-decision triggers
```

**Use Case: Maturity Assessment**
```
> /maturity-check for our product organization

This skill will:
1. Assess your org against the 4 maturity levels
2. Identify gaps and improvement areas
3. Provide specific recommendations
4. Create a maturity roadmap
```

---

## Usage Examples by V2V Phase

The plugin follows the Vision to Value (V2V) System - a 6-phase flow from strategic intent to business outcomes. **These examples show how you reference your organization's documents using Claude Code's `@file` syntax** to give agents the business context they need.

### Phase 1: Strategic Foundation

**Setting Strategic Direction**
```
> @cpo Define our strategic intent for 2025.
  See @strategy/board-feedback-dec-2024.md for board input,
  @strategy/offsite-notes.md for leadership discussion,
  and @competitive/market-shifts-q4.md for market changes to address.

> @cpo Review and update our strategic intent.
  Current version: @strategy/2024-strategic-intent.md
  Q3 results: @finance/q3-performance-summary.md
  Competitive moves: @competitive/q3-landscape-update.md

> /strategic-intent for our AI product line.
  Align with @strategy/company-ai-strategy.md
  and address gaps in @competitive/ai-feature-comparison.md
```

**Creating Product Vision**
```
> @vp-product Create a product vision for our collaboration platform.
  Customer needs: @research/collaboration-needs-study.md
  Technical capabilities: @technical/platform-architecture.md
  Competitive position: @competitive/collaboration-landscape.md

> @vp-product Update our product vision based on the pivot.
  PLT decision: @decisions/pivot-decision-record.md
  Gap analysis: @strategy/market-gap-analysis.md
  Core differentiators: @strategy/competitive-advantages.md

> /vision-statement for ProjectHub.
  Positioning: @gtm/async-first-positioning.md
  Capabilities: @roadmap/platform-capabilities.md
```

**Market Analysis**
```
> @competitive-intelligence Comprehensive market analysis for SMB segment.
  Preliminary sizing: @bizops/tam-analysis-2024.md
  Win/loss data: @sales/win-loss-h2-2024.md
  Customer feedback: @research/smb-interviews.md

> @competitive-intelligence Update competitive landscape.
  Current analysis: @competitive/feature-matrix.md
  Pricing changes: @competitive/competitor-pricing-update.md
  Win/loss patterns: @sales/competitive-losses-q4.md

> /market-analysis for project management tools market.
  Entry proposal: @strategy/pm-market-entry.md
  Regulatory requirements: @legal/compliance-requirements.md
```

### Phase 2: Strategic Decisions

**Business Case Development**
```
> @bizops Create business case for European expansion.
  Market research: @strategy/emea-opportunity.md
  Localization costs: @engineering/localization-estimate.md
  Phased approach: @strategy/emea-phasing-options.md

> @bizops Build business case for mobile app investment.
  Customer demand: @research/mobile-nps-feedback.md
  Competitive gap: @competitive/mobile-comparison.md
  Engineering capacity: @engineering/q1-capacity-plan.md

> /business-case for healthcare vertical.
  Compliance: @legal/hipaa-checklist.md
  Partnership: @bizdev/healthcorp-proposal.md
  Market size: @competitive/healthcare-market-sizing.md
```

**Pricing Strategy**
```
> @vp-product Develop pricing strategy for freemium-to-paid conversion.
  Positioning decision: @decisions/positioning-decision-record.md
  GTM approach: @gtm/conversion-strategy.md
  Competitive pricing: @competitive/pricing-analysis.md

> @vp-product Revisit enterprise pricing.
  Win/loss analysis: @sales/enterprise-win-loss.md
  Value metrics: @cs/customer-value-data.md
  Margin requirements: @finance/q4-margin-guidance.md

> /pricing-strategy for professional tier.
  Packaging recommendations: @gtm/packaging-options.md
  WTP data: @research/conjoint-study-results.md
  Competitive benchmarks: @competitive/tier-pricing-comparison.md
```

**Positioning**
```
> @director-product-marketing Develop positioning for AI features.
  Competitive announcement: @competitive/competitor-ai-launch.md
  Our foundation: @gtm/enterprise-positioning.md
  Security concerns: @research/analyst-briefing-feedback.md

> @director-product-marketing Create positioning for security module.
  Technical differentiators: @product/security-architecture.md
  Compliance story: @gtm/compliance-messaging.md
  CISO feedback: @research/ciso-roundtable-notes.md

> /positioning-statement for API platform.
  Developer competitors: @competitive/api-landscape.md
  Enterprise ICP: @gtm/enterprise-icp.md
  Technical advantages: @product/api-differentiators.md
```

### Phase 3: Strategic Commitments

**Roadmap Development**
```
> @director-product-management Create the H2 2025 roadmap.
  Strategic bets: @decisions/h2-portfolio-decisions.md
  Customer commitments: @sales/customer-commitments-tracker.md
  Technical debt: @engineering/tech-debt-priorities.md

> @director-product-management Update roadmap for scope change.
  Decision record: @decisions/analytics-scope-change.md
  Acme commitments: @sales/acme-contract-requirements.md
  GlobalTech commitments: @sales/globaltech-timeline.md

> /product-roadmap for platform modernization.
  Dependency analysis: @engineering/platform-dependencies.md
  Revenue impact: @bizops/modernization-revenue-model.md
  Resource plan: @engineering/h2-staffing.md
```

**GTM Strategy**
```
> @director-product-marketing Develop GTM strategy for Q2 launch.
  Segmentation: @gtm/segment-analysis.md
  Sales capacity: @sales/q2-capacity-plan.md
  Partner feedback: @bizdev/partner-summit-notes.md

> @director-product-marketing Create GTM strategy for healthcare.
  Market analysis: @competitive/healthcare-market-analysis.md
  Compliance requirements: @legal/healthcare-compliance.md
  Pilot structure: @bizdev/healthcare-pilot-proposal.md

> /gtm-strategy for enterprise push.
  ABM approach: @sales/abm-strategy.md
  Demand gen campaigns: @marketing/q2-campaigns.md
  Target accounts: @sales/enterprise-target-list.md
```

**Strategy Communication**
```
> @cpo Prepare strategy communication for all-hands.
  Pivot rationale: @decisions/pivot-decision-record.md
  Market data: @competitive/market-shift-analysis.md
  Company values: @company/values-and-principles.md

> @cpo Create board update on product strategy.
  Key decisions: @decisions/q4-decision-summary.md
  OKR progress: @strategy/okr-tracker.md
  Investment asks: @finance/2025-investment-proposal.md

> /strategy-communication for product direction change.
  Engineering angle: @product/technical-opportunity.md
  Sales angle: @gtm/competitive-positioning.md
  Customer angle: @cs/value-delivery-narrative.md
```

### Phase 4: Coordinated Execution

**PRD Creation**
```
> @product-manager Create PRD for reporting dashboard.
  Customer discovery: @research/reporting-interviews.md
  Data architecture: @engineering/data-architecture-decisions.md
  Analytics positioning: @gtm/analytics-positioning.md

> @product-manager Write PRD for authentication overhaul.
  Security audit: @security/auth-audit-findings.md
  Enterprise SSO requirements: @sales/sso-requirements-top10.md
  Identity roadmap: @engineering/identity-platform-roadmap.md

> /prd for bulk import feature.
  Acme requirements: @sales/acme-import-requirements.md
  Architecture constraints: @engineering/import-architecture-adr.md
  Scale requirements: @product/enterprise-scale-targets.md
```

**Feature Specifications**
```
> @product-manager Feature spec for bulk import.
  Ingestion architecture: @engineering/data-ingestion-spec.md
  Error handling: @support/import-error-patterns.md
  Customer pain points: @research/data-migration-feedback.md

> @product-manager Feature spec for notification redesign.
  UX research: @research/notification-fatigue-study.md
  Mobile-first approach: @product/mobile-first-principles.md
  Enterprise integrations: @engineering/notification-integrations.md

> /feature-spec for search improvements.
  Usability study: @research/search-usability-findings.md
  Performance SLAs: @engineering/search-sla-requirements.md
  Priority use cases: @product/search-use-case-ranking.md
```

**Launch Planning**
```
> @product-operations Coordinate launch plan for v3.0.
  Feature readiness: @pm/feature-readiness-tracker.md
  Marketing calendar: @pmm/q2-launch-calendar.md
  CS training: @cs/training-schedule.md
  Rollout strategy: @engineering/rollout-plan.md

> @product-operations Create launch plan for mobile app.
  App store timeline: @engineering/app-store-submission.md
  PR announcement: @marketing/conference-pr-plan.md
  Support projections: @cs/mobile-support-forecast.md

> /launch-plan for enterprise tier.
  Sales enablement: @pmm/enterprise-enablement-plan.md
  Customer migration: @cs/migration-playbook.md
  Marketing announcement: @marketing/enterprise-launch-plan.md
```

**Sales Enablement**
```
> @director-product-marketing Create sales enablement for enterprise.
  Pilot validation: @cs/pilot-value-validation.md
  Win/loss objections: @sales/enterprise-objections.md
  Sales methodology: @sales/new-methodology-guide.md

> @director-product-marketing Update sales enablement for AI features.
  ROI calculator: @bizops/ai-roi-calculator.md
  Beta proof points: @cs/ai-beta-results.md
  Competitive responses: @competitive/ai-battle-card.md

> /sales-enablement for security module.
  Compliance certs: @security/certification-summary.md
  Technical deep-dive: @engineering/security-architecture.md
  SE requirements: @sales/se-content-requests.md
```

**Campaign Briefs**
```
> @product-marketing-manager Campaign brief for product launch.
  Messaging framework: @gtm/messaging-framework.md
  Demand gen timeline: @marketing/demand-gen-calendar.md
  Analyst quotes: @pr/analyst-briefing-quotes.md

> @product-marketing-manager Campaign brief for thought leadership.
  Positioning: @gtm/future-of-work-positioning.md
  Research study: @research/commissioned-study-findings.md
  Speaking slots: @marketing/conference-schedule.md

> /campaign-brief for customer upgrade campaign.
  Segmentation: @marketing/upgrade-segmentation.md
  Success stories: @cs/early-adopter-case-studies.md
  Offer structure: @gtm/upgrade-offer-options.md
```

### Phase 5: Business Outcomes

**Onboarding Playbooks**
```
> @value-realization Create onboarding playbook for enterprise customers.
  Best practices: @cs/successful-implementations.md
  Common blockers: @cs/implementation-retrospective.md
  CSM structure: @cs/csm-team-model.md

> @value-realization Update self-serve onboarding playbook.
  Funnel analysis: @product/onboarding-funnel-data.md
  A/B test results: @product/tour-ab-test-results.md
  High-NPS patterns: @cs/high-nps-customer-analysis.md

> /onboarding-playbook for healthcare customers.
  Compliance checkpoints: @legal/healthcare-onboarding-compliance.md
  EHR integration patterns: @engineering/ehr-integration-guide.md
  Success criteria: @cs/healthcare-success-metrics.md
```

**Value Realization**
```
> @value-realization Generate Q2 value realization report.
  Value hypotheses: @product/launch-value-hypotheses.md
  ROI data: @cs/customer-roi-collection.md
  At-risk accounts: @cs/value-gap-accounts.md

> @value-realization Create value report for Acme Corp.
  Success plan: @cs/acme-success-plan.md
  Account metrics: @cs/acme-usage-dashboard.md
  Benchmark data: @cs/enterprise-benchmarks.md

> /value-realization-report for enterprise segment.
  Adoption metrics: @product/enterprise-adoption-data.md
  Renewal rates: @finance/enterprise-renewal-analysis.md
  CS prioritization: @cs/account-tier-criteria.md
```

**Customer Health**
```
> @value-realization Build customer health scorecard.
  Usage signals: @product/usage-instrumentation-spec.md
  Churn predictors: @cs/churn-pattern-analysis.md
  Community engagement: @marketing/community-metrics.md

> @value-realization Create health scorecard for enterprise.
  Churn analysis: @cs/enterprise-churn-factors.md
  Expansion indicators: @cs/expansion-signal-study.md
  Engagement weighting: @cs/health-score-weights.md

> /customer-health-scorecard for strategic accounts.
  Custom success metrics: @cs/strategic-account-kpis.md
  Relationship health: @sales/executive-engagement-tracker.md
  Contract terms: @legal/strategic-account-slas.md
```

### Phase 6: Learning Loop

**Outcome Reviews**
```
> @product-leadership-team Outcome review for mobile app launch.
  Success criteria: @decisions/mobile-launch-decision.md
  Actual results: @product/mobile-launch-metrics.md
  Assumption tracking: @product/mobile-assumptions-log.md

> @product-leadership-team Review Q2 pricing experiment outcomes.
  Experiment design: @product/pricing-experiment-plan.md
  Conversion data: @finance/pricing-conversion-analysis.md
  Win rate changes: @sales/competitive-win-rate-trend.md

> /outcome-review for enterprise push initiative.
  Original business case: @bizops/enterprise-business-case.md
  Actual performance: @finance/enterprise-performance.md
  Learnings template: @decisions/outcome-review-template.md
```

**Retrospectives**
```
> @product-leadership-team Retrospective on delayed feature launch.
  Timeline: @pm/feature-x-timeline.md
  Blockers: @pm/feature-x-blockers.md
  Team feedback: @pm/feature-x-team-survey.md

> @product-leadership-team Retrospective on Q3 planning cycle.
  Process documentation: @process/planning-process.md
  Team feedback: @process/planning-feedback-survey.md
  Alignment issues: @process/planning-misalignment-log.md

> /retrospective for partnership integration project.
  Project timeline: @bizdev/partner-integration-timeline.md
  Collaboration notes: @bizdev/cross-company-collaboration.md
  Technical learnings: @engineering/integration-lessons.md
```

**Decision Quality Audits**
```
> @product-leadership-team Audit H1 strategic decisions.
  Decision records: @decisions/h1-decision-records/
  Outcome data: @finance/h1-initiative-outcomes.md
  Decision framework: @decisions/decision-quality-criteria.md

> @product-leadership-team Review portfolio decisions this quarter.
  Portfolio decisions: @decisions/q4-portfolio-decisions.md
  Ownership tracking: @decisions/decision-ownership-log.md
  Re-decision triggers: @decisions/re-decision-tracker.md

> /decision-quality-audit for prioritization decisions.
  Prioritization framework: @product/prioritization-framework.md
  Decision outcomes: @product/prioritization-outcomes.md
  Framework effectiveness: @product/framework-evaluation.md
```

---

## Multi-Agent Workflows

The power of this plugin is in how agents collaborate **using your documents as shared context**. Here are complete workflows showing how agents reference and build on your organization's knowledge.

### Complete Product Launch Workflow

```
You: @cpo We're launching the new analytics product in Q2. Guide me through
  the complete process.
  Strategic bet: @decisions/analytics-bet.md
  Architecture: @technical/analytics-architecture.md
  Market sizing: @competitive/q4-analytics-market.md

CPO Agent:
"I'll coordinate the full launch process, building on the approved strategic
bet and existing analysis. Let me gather inputs from the team."

[CPO invokes @director-product-management]
→ "Create the analytics product roadmap.
   Strategic bet: @decisions/analytics-bet.md
   Platform dependencies: @roadmap/platform-roadmap.md
   MVP scope: @engineering/analytics-mvp-scope.md"
→ Creates product roadmap with clear phase gates

[CPO invokes @director-product-marketing]
→ "Develop GTM strategy for analytics launch.
   Market positioning: @gtm/platform-positioning.md
   Competitive gaps: @competitive/q4-analytics-market.md
   Sales targets: @sales/q2-targets.md"
→ Develops GTM strategy with segment-specific approaches

[CPO invokes @bizops]
→ "Create business case for analytics investment.
   Market sizing: @competitive/q4-analytics-market.md
   Development costs: @engineering/analytics-cost-estimate.md
   Revenue scenarios: @finance/analytics-revenue-model.md"
→ Creates business case with sensitivity analysis

[CPO invokes @competitive-intelligence]
→ "Update competitive positioning for analytics market.
   Current landscape: @competitive/analytics-competitors.md
   Win/loss data: @sales/analytics-win-loss.md
   Feature gaps: @product/analytics-gap-analysis.md"
→ Provides competitive analysis and battle cards

[CPO invokes @product-operations]
→ "Coordinate launch plan integrating all streams.
   Conference timing: @marketing/conference-calendar.md
   CS training: @cs/training-schedule.md
   Beta customers: @cs/analytics-beta-customers.md"
→ Develops comprehensive launch plan with RACI

Result:
- Product roadmap aligned to strategic bet (MD + HTML)
- GTM strategy with competitive positioning (MD + HTML)
- Business case with financial projections (MD + HTML)
- Competitive analysis and battle cards (MD + HTML)
- Launch plan with cross-functional RACI (MD + HTML)
- Executive summary presentation for board review
```

### Quarterly Business Review Workflow

```
You: @product-leadership-team Prepare materials for Q3 QBR.
  Strategic bets: @strategy/2024-strategic-bets.md
  Enterprise cohort: @cs/enterprise-customer-list.md
  Competitor announcement: @competitive/competitor-q3-launch.md

PLT Agent:
"I'll prepare a comprehensive QBR package that evaluates our strategic bets
and incorporates the latest competitive intelligence."

[PLT invokes @value-realization]
→ "Compile Q3 outcomes for the enterprise cohort.
   Success criteria: @bizops/enterprise-success-criteria.md
   Health scores: @cs/enterprise-health-scores.md
   NPS trends: @cs/enterprise-nps-tracker.md"
→ Collects enterprise customer metrics with trend analysis

[PLT invokes @bizops]
→ "Prepare Q3 financial performance summary.
   Annual targets: @finance/2024-annual-plan.md
   Q3 actuals: @finance/q3-financial-close.md
   Driver analysis: @finance/revenue-driver-breakdown.md"
→ Compiles financial KPIs with variance analysis

[PLT invokes @competitive-intelligence]
→ "Summarize competitive landscape changes.
   Last QBR baseline: @competitive/q2-landscape.md
   Competitor launch: @competitive/competitor-q3-launch.md
   Win rate trends: @sales/competitive-win-rates.md"
→ Provides competitive update with strategic implications

[PLT synthesizes all inputs]
→ Evaluates each bet against @strategy/2024-strategic-bets.md
→ Identifies what's working and what needs adjustment
→ Prepares recommended decisions for Q4

Result:
- Strategic bet scorecard with go/no-go recommendations
- Enterprise customer outcomes vs targets
- Financial performance with full-year forecast update
- Competitive landscape changes and implications
- Q4 priorities and resource reallocation needs
- Full QBR presentation deck (responsive HTML)
```

### Strategic Decision Workflow

```
You: @product-leadership-team We need to decide: build or buy reporting solution.
  Customer demand: @research/reporting-needs.md
  Build estimate: @engineering/reporting-build-estimate.md
  Vendor quotes: @procurement/reporting-vendor-quotes.md

PLT Agent:
"I'll structure this as a formal Decision Interface, gathering required inputs
and creating a decision record for accountability."

[PLT invokes @bizops]
→ "Build financial comparison of build vs buy.
   Build costs: @engineering/reporting-build-estimate.md
   Vendor quotes: @procurement/reporting-vendor-quotes.md
   Maintenance projections: @engineering/maintenance-cost-model.md"
→ Creates financial analysis with 3-year TCO comparison

[PLT invokes @product-manager]
→ "Assess technical requirements and integration.
   Customer needs: @research/reporting-needs.md
   Data architecture: @engineering/data-architecture.md
   Integration requirements: @engineering/integration-checklist.md"
→ Provides technical assessment with risk analysis

[PLT invokes @competitive-intelligence]
→ "Analyze the reporting vendor landscape.
   Competitor tools: @competitive/competitor-tech-stack.md
   Vendor comparison: @procurement/vendor-evaluation.md
   Market trends: @competitive/bi-market-trends.md"
→ Delivers vendor analysis with market perspective

[PLT creates Decision Interface Charter]
→ Using template: @decisions/decision-charter-template.md
→ Defines decision owner, required inputs, success criteria
→ Documents re-decision triggers

[PLT creates Decision Record]
→ Using template: @decisions/decision-record-template.md
→ Captures all options with pros/cons
→ Documents recommendation with rationale

Result:
- Decision Interface Charter for ongoing decisions
- Decision Record with clear recommendation
- 3-year financial comparison (build vs buy vs hybrid)
- Technical assessment with integration analysis
- Vendor landscape analysis
- Decision presentation for exec staff (HTML)
```

### Annual Planning Workflow

```
You: @cpo Kick off annual planning for next year.
  Offsite strategy: @strategy/offsite-synthesis.md
  Market analysis: @competitive/annual-market-analysis.md
  Resource constraints: @finance/2025-resource-envelope.md

CPO Agent:
"I'll coordinate annual planning across the product organization, ensuring
alignment from strategy through resource allocation."

[CPO invokes @competitive-intelligence]
→ "Finalize market analysis for annual planning.
   Draft analysis: @competitive/annual-market-analysis.md
   Segment framework: @strategy/segment-prioritization.md
   Threat assessment: @competitive/threat-matrix.md"
→ Delivers comprehensive market context for planning

[CPO invokes @director-product-management]
→ "Develop product roadmap scenarios for next year.
   Strategic themes: @strategy/offsite-synthesis.md
   Resource scenarios: @finance/2025-resource-envelope.md
   Current roadmap: @roadmap/2024-roadmap.md"
→ Creates three roadmap scenarios with tradeoff analysis

[CPO invokes @director-product-marketing]
→ "Outline GTM strategy options for each roadmap scenario.
   Current GTM: @gtm/2024-gtm-strategy.md
   Market opportunities: @competitive/annual-market-analysis.md
   Marketing budget: @finance/2025-marketing-envelope.md"
→ Develops GTM scenarios aligned to roadmap options

[CPO invokes @bizops]
→ "Build financial models for each scenario.
   Resource scenarios: @finance/2025-resource-envelope.md
   Revenue models: @finance/revenue-model-assumptions.md
   Investment criteria: @finance/investment-hurdle-rates.md"
→ Creates financial models with risk-adjusted returns

[CPO synthesizes and prepares for leadership review]
→ Integrated planning package with recommendations
→ Decision framework for resource allocation
→ Presentation for exec team and board

Result:
- Market analysis and opportunity framework
- Three roadmap scenarios with tradeoffs
- GTM strategy options by scenario
- Financial models with ROI analysis
- Integrated planning recommendation
- Board presentation deck (responsive HTML)
```

---

## Working with Individual Agents

Each agent has specific expertise and can be addressed directly. **Reference your documents using `@file` syntax** to give agents the context they need.

### @cpo - Chief Product Officer
```
> @cpo Review our product strategy in light of board feedback.
  Board notes: @strategy/board-meeting-dec-2024.md
  Current strategy: @strategy/2024-product-strategy.md
  Enterprise metrics: @finance/enterprise-performance.md

> @cpo The market has shifted. Recommend portfolio adjustments.
  Market analysis: @competitive/market-shift-analysis.md
  Current portfolio: @strategy/portfolio-allocation.md
  Resource constraints: @finance/2025-budget-guidance.md

> @cpo Help me prepare for the board meeting.
  Strategic bets progress: @strategy/bet-scorecard.md
  Competitive response: @competitive/competitor-response-plan.md
  Investment ask: @finance/ai-investment-proposal.md
```

### @vp-product - VP of Product
```
> @vp-product Create a product vision for the new platform.
  Advisory board feedback: @research/cab-dec-2024.md
  Competitor direction: @competitive/competitor-conference-notes.md
  Technical capabilities: @engineering/platform-capabilities.md

> @vp-product Develop pricing strategy for enterprise tier.
  Pilot value metrics: @cs/pilot-value-validation.md
  Competitive pricing: @competitive/enterprise-pricing-analysis.md
  Margin requirements: @finance/pricing-margin-guidance.md

> @vp-product How should we evolve our product org structure?
  Current org: @org/product-team-structure.md
  Growth plan: @hr/pm-hiring-plan.md
  Best practices: @org/product-org-benchmarks.md
```

### @director-product-management - Director of PM
```
> @director-product-management Build our H2 roadmap.
  Strategic bets: @decisions/h1-portfolio-review.md
  Customer commitments: @sales/customer-commitments.md
  Platform dependencies: @engineering/platform-roadmap.md

> @director-product-management Improve our requirements process.
  Retro feedback: @process/q3-retro-themes.md
  Cycle time data: @process/requirements-cycle-time.md
  Current process: @process/requirements-process.md

> @director-product-management Help me coach Alex on stakeholder management.
  Project context: @pm/enterprise-project-status.md
  Stakeholder map: @pm/enterprise-stakeholders.md
  Training frameworks: @training/stakeholder-management.md
```

### @product-manager - Product Manager
```
> @product-manager Write a PRD for the search feature.
  User research: @research/search-usability-study.md
  Platform capabilities: @engineering/indexing-architecture.md
  Performance requirements: @engineering/enterprise-sla.md

> @product-manager Prioritize our backlog for the sprint.
  Acme escalation: @support/acme-escalation.md
  Tech debt items: @engineering/tech-debt-backlog.md
  Q2 launch dependencies: @roadmap/q2-launch-dependencies.md

> @product-manager Create user stories for checkout improvements.
  Funnel analysis: @product/checkout-funnel-analysis.md
  Usability issues: @research/checkout-session-recordings.md
  Success criteria: @product/checkout-success-metrics.md
```

### @director-product-marketing - Director of PMM
```
> @director-product-marketing Develop GTM strategy for AI features.
  Competitor announcement: @competitive/competitor-ai-launch.md
  Enterprise sales motion: @sales/enterprise-sales-playbook.md
  Analyst briefings: @pr/analyst-briefing-schedule.md

> @director-product-marketing Create positioning for security module.
  Architecture advantages: @technical/security-whitepaper.md
  Lost deal objections: @sales/security-lost-deals.md
  Compliance story: @gtm/compliance-messaging.md

> @director-product-marketing Plan Q2 launch campaign.
  Conference keynote: @marketing/conference-keynote-plan.md
  Customer references: @cs/reference-customer-pipeline.md
  Analyst report: @pr/analyst-report-timeline.md
```

### @product-marketing-manager - PMM
```
> @product-marketing-manager Create campaign brief for AI webinar series.
  Thought leadership positioning: @gtm/ai-thought-leadership.md
  Research study: @research/ai-adoption-study.md
  Target audience: @marketing/webinar-audience-profile.md

> @product-marketing-manager Update competitive battle cards.
  Competitor announcement: @competitive/competitor-pricing-update.md
  Current battle cards: @sales/competitive-battle-cards.md
  Sales feedback: @sales/competitive-feedback.md

> @product-marketing-manager Develop case study template.
  ROI metrics: @cs/roi-metrics-framework.md
  Buyer personas: @gtm/buyer-personas.md
  Existing case studies: @marketing/case-study-examples.md
```

### @bizops - Business Operations
```
> @bizops Create business case for mobile app investment.
  Customer demand: @research/mobile-nps-feedback.md
  Development estimate: @engineering/mobile-estimate.md
  Competitive gap: @competitive/mobile-gap-analysis.md

> @bizops Build 3-year financial projections for new product line.
  Market sizing: @competitive/new-market-sizing.md
  Cost structure: @finance/product-cost-model.md
  Investment phases: @strategy/product-investment-phases.md

> @bizops Prepare QBR materials.
  KPI targets: @finance/2024-kpi-targets.md
  Q3 performance: @finance/q3-performance.md
  Reallocation proposal: @finance/resource-reallocation.md
```

### @value-realization - Value Realization
```
> @value-realization Analyze Q3 feature adoption patterns.
  Feature releases: @product/q3-feature-releases.md
  Adoption data: @product/feature-adoption-dashboard.md
  Renewal correlation: @cs/adoption-renewal-analysis.md

> @value-realization Create enterprise health scorecard.
  Usage metrics: @product/enterprise-usage-metrics.md
  Support patterns: @support/enterprise-ticket-analysis.md
  Engagement signals: @cs/executive-engagement-tracker.md

> @value-realization Analyze time-to-value for enterprise.
  Business case targets: @bizops/enterprise-ttv-targets.md
  Implementation data: @cs/implementation-timeline-data.md
  Success patterns: @cs/fast-ttv-patterns.md
```

### @competitive-intelligence - Competitive Intelligence
```
> @competitive-intelligence Analyze competitor acquisition.
  Announcement: @competitive/competitor-acquisition-news.md
  Their product strategy: @competitive/competitor-strategy-analysis.md
  Our positioning: @gtm/competitive-positioning.md

> @competitive-intelligence Size healthcare vertical opportunity.
  Preliminary analysis: @strategy/vertical-evaluation.md
  Competitor presence: @competitive/healthcare-competitors.md
  Regulatory landscape: @legal/healthcare-regulations.md

> @competitive-intelligence Create enterprise battle cards.
  Current cards: @sales/enterprise-battle-cards.md
  Sales objections: @sales/competitive-objections-log.md
  Our proof points: @cs/enterprise-proof-points.md
```

### @bizdev - Business Development
```
> @bizdev Evaluate TechCorp partnership opportunity.
  Partnership criteria: @strategy/partnership-framework.md
  TechCorp proposal: @bizdev/techcorp-proposal.md
  Integration assessment: @engineering/techcorp-integration.md

> @bizdev Develop SI partnership strategy.
  Implementation capacity: @cs/implementation-capacity.md
  SI landscape: @bizdev/si-partner-landscape.md
  Partner program: @bizdev/partner-program-design.md

> @bizdev Analyze APAC expansion opportunity.
  Market research: @competitive/apac-market-analysis.md
  Localization requirements: @engineering/apac-localization.md
  Entry models: @strategy/market-entry-models.md
```

### @product-operations - Product Operations
```
> @product-operations Identify and fix process bottlenecks.
  Cycle time data: @process/development-cycle-time.md
  Retro themes: @process/h1-retros.md
  Current process: @process/product-development-process.md

> @product-operations Coordinate v3.0 launch plan.
  Feature readiness: @pm/v3-feature-status.md
  Marketing calendar: @pmm/v3-marketing-calendar.md
  CS training: @cs/v3-training-plan.md
  Rollout strategy: @engineering/v3-rollout-plan.md

> @product-operations Evaluate roadmapping tools.
  Requirements: @process/tool-requirements.md
  Current pain points: @process/tool-survey-results.md
  Evaluation criteria: @process/tool-eval-criteria.md
```

### @ux-lead - UX Lead
```
> @ux-lead Plan user research for dashboard feature.
  PM hypothesis: @pm/dashboard-hypothesis.md
  Research questions: @research/dashboard-research-questions.md
  User segments: @research/dashboard-user-segments.md

> @ux-lead Review checkout redesign for usability.
  Current flow: @design/checkout-current-flow.md
  Conversion data: @product/checkout-conversion-data.md
  UX principles: @design/ux-principles.md

> @ux-lead Create enterprise onboarding journey map.
  CS learnings: @cs/implementation-learnings.md
  Friction points: @cs/onboarding-friction-points.md
  Success patterns: @cs/successful-onboarding-patterns.md
```

### @product-leadership-team - Product Leadership Team
```
> @product-leadership-team Portfolio tradeoff: mobile app vs API platform.
  Mobile proposal: @roadmap/mobile-app-proposal.md
  API proposal: @roadmap/api-platform-proposal.md
  Resource constraints: @finance/q2-resource-allocation.md
  Decision criteria: @decisions/portfolio-decision-criteria.md

> @product-leadership-team Outcome review for Q2 pricing experiment.
  Experiment design: @product/pricing-experiment-design.md
  Results data: @finance/pricing-experiment-results.md
  Success criteria: @decisions/pricing-success-criteria.md

> @product-leadership-team Create Decision Interface Charters.
  Decision charter template: @decisions/charter-template.md
  Portfolio review process: @process/portfolio-review.md
  Launch readiness process: @process/launch-readiness.md
  Pricing change process: @process/pricing-changes.md
```

---

## Using Skills Directly

Skills are slash commands that create specific deliverables. Use them when you know exactly what you need:

### Document Deliverables
```
/prd for [feature name]
/product-roadmap for [time period or initiative]
/business-case for [opportunity]
/business-plan for [product/market]
/gtm-strategy for [launch]
/pricing-strategy for [product/tier]
/competitive-landscape for [market]
/market-analysis for [segment]
/launch-plan for [release]
/qbr-deck for [quarter]
```

### Decision Documents
```
/decision-record for [decision topic]
/decision-charter for [recurring decision type]
/strategic-bet for [opportunity]
/commitment-check for [initiative]
/portfolio-tradeoff for [competing priorities]
```

### Execution Documents
```
/feature-spec for [feature]
/user-story for [capability]
/campaign-brief for [campaign]
/sales-enablement for [product/feature]
/launch-readiness for [release]
```

### Outcomes & Learning
```
/outcome-review for [initiative]
/retrospective for [project/period]
/value-realization-report for [customer segment]
/customer-health-scorecard for [segment]
/onboarding-playbook for [customer type]
```

### Assessment
```
/maturity-check for [dimension]
/pm-level-check for [person/role]
/decision-quality-audit for [decision area]
```

### Presentation
```
/present [path/to/document.md]
```

---

## HTML Presentations

Every major deliverable automatically generates a responsive HTML presentation:

- **Desktop optimized** - Full-screen presentations with navigation
- **Mobile friendly** - Touch gestures, readable text, scrollable tables
- **Print ready** - Export to PDF for distribution
- **Dark mode** - Automatically adapts to system preference
- **Share ready** - Hash-based URLs for direct linking to slides

### Example Output

When you run:
```
> @director-product-marketing Create a GTM strategy for our Q2 launch
```

You get:
1. `gtm-strategy-q2-launch.md` - Full markdown document
2. `gtm-strategy-q2-launch.html` - Presentation-ready HTML

The HTML presentation includes:
- Title slide with launch details
- Target market & personas slide
- Positioning & value prop slide
- Key messages slide
- Pricing strategy slide
- Sales motion slide
- Launch timeline slide
- Success metrics slide
- Summary & next steps slide

---

## Best Practices

### 1. Start with the Right Agent
Choose the agent whose role matches your task. Need a PRD? Start with @product-manager. Need GTM strategy? Start with @director-product-marketing.

### 2. Let Agents Collaborate
For complex tasks, start with a senior agent (like @cpo or @product-leadership-team) and let them coordinate with other agents.

### 3. Be Specific
The more context you provide, the better the output:
```
# Less effective
> @product-manager Write a PRD

# More effective
> @product-manager Write a PRD for a bulk data import feature.
  Target users are data admins at enterprise companies.
  The feature should support CSV and Excel files up to 100MB.
  We need to launch in Q2.
```

### 4. Use Skills for Quick Output
When you know exactly what format you need, use skills directly:
```
/decision-record for choosing between AWS and GCP
```

### 5. Review and Iterate
Treat outputs as excellent first drafts. Review, refine, and ask for revisions:
```
> @product-manager This is great, but can you add more detail on the API requirements?
```

---

## The V2V Framework

This plugin is built on the Vision to Value (V2V) System - a proven framework for product organizations:

### The 6 Phases
1. **Strategic Foundation** - Strategic intent, market analysis, product vision
2. **Strategic Decisions** - Business cases, pricing, positioning (the "commercial filter")
3. **Strategic Commitments** - Roadmaps, GTM establishment (the "point of no return")
4. **Coordinated Execution** - Product development, marketing, sales participation
5. **Business Outcomes** - Customer onboarding, value realization, behavior tracking
6. **Learning Loop** - Outcome reviews, retrospectives, continuous improvement

### Skills by V2V Phase

| Phase | Skills |
|-------|--------|
| **1. Strategic Foundation** | `/strategic-intent`, `/vision-statement`, `/market-analysis`, `/competitive-landscape`, `/competitive-analysis`, `/market-segment` |
| **2. Strategic Decisions** | `/business-case`, `/business-plan`, `/pricing-strategy`, `/pricing-model`, `/positioning-statement`, `/decision-record`, `/strategic-bet`, `/decision-charter`, `/escalation-rule` |
| **3. Strategic Commitments** | `/product-roadmap`, `/roadmap-theme`, `/roadmap-item`, `/gtm-strategy`, `/gtm-brief`, `/launch-plan`, `/strategy-communication`, `/commitment-check`, `/prd`, `/prd-outline`, `/feature-spec`, `/user-story` |
| **4. Coordinated Execution** | `/launch-readiness`, `/stakeholder-brief`, `/campaign-brief`, `/sales-enablement` |
| **5. Business Outcomes** | `/onboarding-playbook`, `/value-realization-report`, `/customer-health-scorecard` |
| **6. Learning Loop** | `/outcome-review`, `/retrospective`, `/decision-quality-audit`, `/context-save`, `/relevant-learnings`, `/feedback-capture` |
| **Cross-Phase** | `/context-recall`, `/feedback-recall`, `/portfolio-status`, `/portfolio-tradeoff`, `/handoff`, `/setup`, `/present`, `/qbr-deck`, `/maturity-check`, `/pm-level-check` |

### Principle Validators

These skills enforce the 8 Operating Principles:

| Skill | Principle | Purpose |
|-------|-----------|---------|
| `/ownership-map` | #1 End-to-End Ownership | Map accountability chain across all V2V phases |
| `/customer-value-trace` | #3 Customer Obsession | Validate decisions trace to customer value |
| `/collaboration-check` | #6 Collaborative Excellence | Validate RACI and stakeholder consultation |
| `/scale-check` | #8 Scalable Systems | Assess scalability at 2x, 10x, 100x |
| `/phase-check` | V2V Flow | Assess which V2V phase an initiative is in |

### The Two Pillars
- **Operating Principles** - Decision quality under pressure ("cultural guardrails")
- **Organizational Structure** - Decision durability over time ("who supports the what")

### The 8 Operating Principles
1. End-to-end ownership is non-negotiable
2. Strategy precedes structure
3. Product leadership is about decision quality
4. Alignment beats consensus
5. Go-to-market is a strategic choice, not a handoff
6. Execution is a leadership discipline
7. Scale changes the nature of the work
8. Organizations learn through outcomes

---

## Parallel Agent Execution

Agents can spawn multiple sub-agents simultaneously for efficient, coordinated work.

### When Parallel Execution Happens

- Portfolio reviews (gather inputs from BizOps, CI, Value Realization simultaneously)
- Launch decisions (check Product, Marketing, Operations readiness in parallel)
- Strategic planning (collect market, competitive, financial data concurrently)

### Example: Portfolio Review

```
/product Prepare materials for Q3 portfolio review

→ Spawns in parallel:
  - @bizops: Financial performance data
  - @competitive-intelligence: Market updates
  - @value-realization: Customer outcome data
  - @product-operations: Delivery status

→ Collects all results
→ Synthesizes into unified portfolio review
```

### Configuration

Parallel execution is enabled by default with a maximum of 4 concurrent agents. The gateway automatically determines optimal parallelization based on task dependencies.

---

## Customization

### Adding Your Context

Create a `CLAUDE.md` file in your project root to add organization-specific context:

```markdown
# Company Context

## Our Product
[Description of your product]

## Our Market
[Description of your target market]

## Current Priorities
[What's most important right now]

## Team Structure
[How your product org is organized]
```

The plugin agents will use this context to provide more relevant outputs.

### Extending the Plugin

You can add your own agents and skills that work alongside the plugin:

```bash
# Add a custom agent
mkdir -p .claude/agents/my-custom-agent
# Create SKILL.md with your agent definition
```

---

## Support

- **Issues**: Report bugs or request features on GitHub
- **Documentation**: Full implementation details in IMPLEMENTATION_PLAN.md
- **Framework**: Based on "Vision to Value" by Yohay Etsion

---

## License

MIT License - Use freely in your product work.

---

**Built on the Vision to Value framework. Designed to help product professionals and organizations work more effectively.**
