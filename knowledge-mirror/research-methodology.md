# Research Methodology — Frameworks & Methods

## Overview

Research is the discipline of reducing uncertainty before committing resources. Without it, decisions rest on assumptions — the most expensive kind of input. Good research does not eliminate uncertainty; it converts vague uncertainty into specific, bounded unknowns that can be managed.

This knowledge pack covers the full research cycle from question formulation to insight presentation. It applies to business analysis, market research, competitive intelligence, product discovery, and any analytical work where the output is a recommendation rather than a transaction.

**Version**: 1.0.0
**Type**: Knowledge Pack
**Primary Users**: 🗃️ Analyst, 🗂️ PA, 🧭 Coach

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - Anthropic knowledge-work-plugins (data/explore-data, data/analyze domain reference)
  - CRAAP Test (Meriam Library, California State University, Chico)
  - Adapted and expanded for Product Org OS agents.
-->

---

## Research Process Framework

**When to use**: At the start of any research engagement, before a single source is opened.

The six-step process creates a contract between the researcher and the requester: this is the question we are answering, this is how we will answer it, and this is what the output looks like.

### Step 1: Define the Research Question

A vague question produces a vague answer. Before any data gathering, convert the business need into a specific, answerable research question.

**Question formulation test**:
- Can you tell unambiguously when the question has been answered?
- Is the scope bounded? ("How do our top three competitors position their pricing?" is bounded. "What is the competitive landscape?" is not.)
- Does it distinguish between descriptive questions (what is the state of X?) and causal questions (why does X happen?) and predictive questions (what will happen if we do X?)?

**SMART criteria for research questions**:

| Criterion | Test |
|-----------|------|
| **Specific** | One main question, not five rolled into one |
| **Measurable** | The answer can be compared or quantified |
| **Answerable** | The data needed can actually be accessed |
| **Relevant** | The answer would change a pending decision |
| **Time-bound** | Needed by a specific date to inform a decision |

**Template**:
```
Research Brief

Business Need: [The decision or action this research will support]
Primary Research Question: [Single specific question]
Secondary Questions: [Sub-questions if needed, max 3]
What "Good Enough" Looks Like: [Minimum confidence level needed to act]
Deliverable Format: [Table / memo / presentation / recommendation]
Deadline: [Date — tied to decision timeline, not arbitrary]
Effort Budget: [Hours available for this research]
```

---

### Step 2: Gather Sources

Map the source landscape before committing to a data collection method. Sources fall into three tiers:

| Tier | Type | Strengths | Limitations |
|------|------|-----------|-------------|
| **Primary** | Data you collect directly (surveys, interviews, experiments) | High relevance, tailored to question | Time-intensive, costly |
| **Secondary** | Published data from others (reports, filings, databases) | Fast, often free or low cost | May not perfectly match question |
| **Tertiary** | Syntheses of secondary sources (encyclopedias, review articles) | Quick orientation | Too aggregated for analytical work |

Default to secondary sources for speed. Commission primary research only when secondary sources cannot answer the question or when the stakes are high enough to warrant custom data.

---

### Step 3: Collect Data

Structured data collection prevents gaps and bias. Before collecting:
- Define inclusion and exclusion criteria (what data counts, what does not)
- Record source metadata (publication date, author, methodology)
- Note data limitations as they are discovered — do not paper over them

---

### Step 4: Analyze

Apply the appropriate analytical method to the data type and the research question. See the Analysis Frameworks section.

---

### Step 5: Synthesize

Raw analysis produces findings. Synthesis produces insights. The distinction:
- **Finding**: "60% of surveyed users said onboarding was confusing."
- **Insight**: "Onboarding confusion is concentrated in the permissions step, which users encounter on day 1 before understanding why the permissions matter — a sequencing problem, not a clarity problem."

Apply the Insight Synthesis Template (see below) to move from findings to actionable insights.

---

### Step 6: Present

Match the format to the audience and the decision they need to make. See the Research Report Structure and Presentation of Findings sections.

---

## Data Exploration Methodology

**When to use**: When working with a dataset for the first time — before any analysis. Skipping exploration leads to analysis errors that are invisible until after the recommendation has been acted on.

### Schema Discovery

Before analyzing data, understand what it contains:

```
Data Exploration Checklist

1. What is the unit of analysis? (Each row = one what?)
2. What is the time range?
3. How many records are there?
4. What are the key identifier fields?
5. What are the quantitative fields? What are their ranges?
6. What are the categorical fields? What are their unique values?
7. Are there any fields whose names or values are ambiguous?
8. Are there related tables/datasets? How do they join?
```

### Data Profiling

For each field of interest:

| Profile Check | What to Look For |
|--------------|-----------------|
| **Completeness** | % of non-null values. Fields with >5% nulls need investigation before use |
| **Uniqueness** | % of distinct values. Identifier fields should be 100% unique |
| **Range** | Min, max, mean, median. Are there implausible values (negative ages, future dates)? |
| **Distribution** | Is the distribution as expected? Heavy skew or bimodal distributions need explanation |
| **Freshness** | When was the data last updated? Is the lag acceptable for the question? |

### Data Quality Assessment

Before drawing conclusions, assess data quality across five dimensions:

| Dimension | Definition | Red Flag |
|-----------|-----------|----------|
| **Completeness** | Required fields are populated | >5% nulls on key fields |
| **Accuracy** | Values match reality | Outliers that cannot be explained, values outside valid range |
| **Consistency** | Same concept encoded the same way across the dataset | Same entity appears with different names (e.g., "US" and "United States") |
| **Timeliness** | Data is current enough for the question | Data older than the decision timeframe |
| **Validity** | Values conform to defined rules | Dates in the wrong format, codes that do not match the reference list |

**Quality Assessment Template**:
```
Field: [Field name]
Completeness: [X]% populated ([Y] nulls)
Range: Min=[X], Max=[Y], Mean=[Z], Median=[W]
Anomalies: [Describe any suspicious values]
Quality Verdict: [Usable as-is / Requires cleaning / Insufficient quality]
Cleaning Steps Needed: [If applicable]
```

### Pattern Discovery

After profiling, look for patterns before testing hypotheses:
- Distribution shape: normal, skewed, bimodal, uniform?
- Temporal patterns: trends, seasonality, step changes at specific dates?
- Correlation candidates: pairs of variables that seem to move together?
- Outlier clusters: groups of records that behave differently from the majority?
- Missing data patterns: are nulls random or systematic (e.g., all nulls from a specific source)?

---

## Analysis Frameworks

### Quantitative Analysis Methods

| Method | When to Use | Output |
|--------|-------------|--------|
| **Descriptive statistics** | Summarize what the data shows | Mean, median, mode, standard deviation, percentiles |
| **Trend analysis** | Understand direction over time | Growth rates, trend lines, seasonality-adjusted figures |
| **Correlation analysis** | Identify relationships between variables | Correlation coefficient, scatter plot, regression |
| **Segmentation** | Find meaningful groups within a population | Cohort tables, segment performance comparisons |
| **Forecasting** | Project future values based on historical patterns | Time series forecasts with confidence intervals |
| **A/B test analysis** | Compare outcomes between two conditions | Statistical significance, effect size, confidence intervals |
| **Funnel analysis** | Identify where a process loses participants | Stage-by-stage conversion rates, drop-off identification |

**Descriptive Statistics Quick Reference**:
- **Mean**: Average value. Sensitive to outliers. Use when distribution is roughly normal.
- **Median**: Middle value. Robust to outliers. Use when distribution is skewed (income, time, prices).
- **Mode**: Most common value. Use for categorical data and identifying dominant patterns.
- **Standard deviation**: Spread around the mean. One standard deviation = ~68% of observations in a normal distribution.
- **Percentiles**: More informative than mean/median for performance data. P50 (median), P95, P99 are standard for latency and time-based metrics.

---

### Qualitative Analysis Methods

| Method | Best For | Process |
|--------|----------|---------|
| **Thematic analysis** | Interview data, open-ended survey responses, customer feedback | Code responses → group codes into themes → identify patterns across themes |
| **Content analysis** | Large text corpora (reviews, support tickets, social media) | Define categories → code systematically → count frequency → interpret patterns |
| **Grounded theory** | Generating theory from data when no prior framework exists | Collect → code → memo → iterate until saturation |
| **Narrative analysis** | Understanding how people make sense of their experience | Map story arcs, turning points, and meaning-making language |

**Thematic Analysis Process**:
```
1. Familiarize: Read all material without coding
2. Generate initial codes: Tag interesting segments
3. Search for themes: Group related codes
4. Review themes: Check themes against data; split or merge as needed
5. Define themes: Write a clear definition for each theme
6. Produce report: Tell the story using themes as the structure
```

**When to trust qualitative data**:
- Consistent themes appearing across independent sources (triangulation)
- Vivid, specific examples that are hard to fabricate
- Themes that surprise — if the qualitative data only confirms what you already believed, the analysis may be confirmation-biased

---

### Mixed Methods Design

Use mixed methods when neither quantitative nor qualitative data alone can answer the question.

| Design | Approach | Use Case |
|--------|----------|----------|
| **Explanatory sequential** | Quantitative first → qualitative explains | Analytics shows a drop; interviews explain why |
| **Exploratory sequential** | Qualitative first → quantitative validates | Interviews reveal a problem; survey measures its scale |
| **Convergent parallel** | Both simultaneously → compare | Survey and interviews run in parallel; findings are merged |
| **Embedded** | One method nested inside the other | Experiment with qualitative component embedded in treatment group |

---

## Source Evaluation Framework (CRAAP Test)

Apply to every source before including it in analysis. One weak source can undermine an otherwise solid piece of work.

| Criterion | Questions to Ask | Red Flags |
|-----------|-----------------|-----------|
| **Currency** | When was this published? Has it been updated? | >3 years old for fast-moving topics; >5 years for slower ones |
| **Relevance** | Does this directly address the research question? Is the scope aligned? | Tangentially related; different geography, industry, or time period |
| **Authority** | Who wrote this? What are their credentials? Who published it? | Anonymous authorship; no methodology disclosure; publication with commercial interest |
| **Accuracy** | Is the methodology described? Are claims backed by evidence? Can the data be verified elsewhere? | No methodology; unsourced statistics; results not replicated |
| **Purpose** | Why was this created? Is there a commercial or advocacy agenda? | Funded by parties with a stake in the conclusion; designed to persuade |

**Source quality tiers**:

| Tier | Examples | Use |
|------|---------|-----|
| **High** | Peer-reviewed research, government statistics, audited financial filings | Primary evidence |
| **Medium** | Industry analyst reports (Gartner, Forrester), reputable journalism, company investor relations materials | Supporting evidence with caveats |
| **Low** | Blog posts, press releases, self-reported survey aggregations from vendors | Context only; never as primary evidence |
| **Avoid** | Unsourced statistics, content marketing disguised as research | Do not use |

---

## Literature Review Methodology

**When to use**: Before primary research, to understand what is already known, avoid duplication, and position new findings in context.

**Process**:
```
1. Define scope boundaries
   - Topic: [exact keywords and synonyms]
   - Time range: [e.g., last 5 years]
   - Geography: [global / specific region]
   - Source types: [academic / practitioner / both]

2. Search systematically
   - Use at least 3 different source databases
   - Record search terms and hit counts for reproducibility
   - Apply CRAAP evaluation before including any source

3. Extract structured information from each source
   - Key findings
   - Methodology
   - Sample size and context
   - Limitations acknowledged by the authors
   - Relevance to your question

4. Map the landscape
   - What is the consensus view?
   - Where do sources disagree?
   - What questions remain open?
   - What is the most recent thinking?

5. Identify gaps
   - What does the existing literature NOT address that your question requires?
   - This is the justification for primary research.
```

---

## Data Collection Methods Matrix

| Method | Best For | Strengths | Weaknesses | Typical Timeline |
|--------|----------|-----------|------------|-----------------|
| **Online survey** | Measuring attitudes, behaviors at scale | Fast, cheap, quantifiable | Self-report bias, low response rates | 1-2 weeks |
| **In-depth interview** | Understanding motivations, context, decision processes | Rich nuance, unexpected directions | Slow, expensive, small N | 2-4 weeks |
| **Focus group** | Exploring reactions, testing concepts with a group | Group dynamics surface issues | Dominant voices, harder to schedule | 2-3 weeks |
| **Observation / ethnography** | Understanding actual behavior vs. stated behavior | Ground truth | Very time-intensive | Weeks to months |
| **Secondary data** | Benchmarking, trend analysis, market sizing | Fast, low cost | May not match exact question | Hours to days |
| **Experiment / A/B test** | Establishing causal relationships | Only method for true causality | Requires traffic/volume, setup complexity | 2-6 weeks |
| **Diary study** | Longitudinal behavior patterns | Captures real behavior over time | High participant burden, dropout risk | 2-4 weeks |
| **Usability test** | Identifying friction in a specific flow | Directly observable behavior | Lab effect, small sample | 1-2 weeks |

---

## Survey Design Best Practices

**Question types**:

| Type | Best For | Avoid When |
|------|----------|------------|
| **Likert scale** (1-5 or 1-7 agree/disagree) | Measuring attitudes and agreement | Measuring frequency or behavior — use a frequency scale instead |
| **Net Promoter Score** (0-10 recommend) | Loyalty benchmark | Diagnostic purposes — it tells you there is a problem, not what it is |
| **Multiple choice (single select)** | Categorical variables | Options are not mutually exclusive |
| **Multiple choice (multi-select)** | Everything that applies | When you need to understand priorities (use ranking instead) |
| **Ranking** | Understanding relative preference | More than 5-7 items — respondent fatigue |
| **Open-ended** | Generating hypotheses, capturing nuance | When you need quantifiable data at scale |

**Bias avoidance**:
- **Leading questions**: "How much do you enjoy using our product?" → "How would you describe your experience using our product?"
- **Double-barreled questions**: "Is the product easy to use and affordable?" → Split into two questions
- **Social desirability bias**: For sensitive topics, use indirect framing ("How do people in your industry typically...?")
- **Acquiescence bias**: Include reversed-polarity items ("I find this easy to use" + "I find this confusing") to catch respondents who agree with everything
- **Order effects**: Randomize answer choices; randomize question order within sections

**Sampling strategies**:

| Strategy | Best For | Limitation |
|----------|----------|------------|
| **Random sampling** | Generalizable results for large populations | Requires a complete population list |
| **Stratified sampling** | Ensuring representation of key subgroups | More complex to execute |
| **Purposive sampling** | Qualitative research targeting specific profiles | Not statistically generalizable |
| **Convenience sampling** | Quick exploratory research | Selection bias; not representative |
| **Snowball sampling** | Hard-to-reach populations | Self-selection bias, can drift from target |

**Sample size guidance** (for surveys with ±5% margin of error at 95% confidence):

| Population Size | Required Sample |
|----------------|----------------|
| 100 | 80 |
| 500 | 218 |
| 1,000 | 278 |
| 10,000 | 370 |
| 100,000+ | ~384 |

---

## Statistical Analysis Quick Reference

**Choosing the right test**:

| Question | Data Type | Test |
|----------|-----------|------|
| Is this sample mean different from a known value? | Continuous, one group | One-sample t-test |
| Are these two group means different? | Continuous, two groups | Independent samples t-test |
| Did this group change over time? | Continuous, paired measurements | Paired t-test |
| Are three or more group means different? | Continuous, 3+ groups | ANOVA |
| Is there a relationship between two continuous variables? | Two continuous variables | Pearson correlation + regression |
| Is there an association between two categorical variables? | Two categorical variables | Chi-square test |
| Does a categorical variable predict a binary outcome? | Mixed | Logistic regression |

**When to use mean vs. median**:
- Use **mean** when the distribution is roughly symmetric and outliers are legitimate data points
- Use **median** when the distribution is skewed or outliers are extreme (income, prices, time-to-complete tasks)
- Always report both for datasets where the gap between them is large — the gap itself is informative

**Correlation cautions**:
- Correlation measures association, not causation
- A correlation of r=0.3 is weak; r=0.5 is moderate; r=0.7+ is strong
- Always plot the data — identical correlation coefficients can describe very different relationships (Anscombe's quartet)
- Beware of spurious correlations in large datasets — with enough variables, some will correlate by chance

**Statistical significance vs. practical significance**:
- A result can be statistically significant (p<0.05) but practically meaningless if the effect size is trivially small
- Always report effect size alongside p-values: Cohen's d for means, Pearson r for correlations, odds ratio for categorical outcomes
- A p-value does not tell you the probability your hypothesis is true — it tells you the probability of observing this result if the null hypothesis were true

---

## Insight Synthesis Template

**When to use**: After analysis is complete, to convert findings into recommendations.

```markdown
## Research Synthesis: [Topic]

**Research Question**: [The original question]
**Data Sources**: [What was analyzed]
**Period Covered**: [Date range]

---

### Key Findings

| Finding | Supporting Evidence | Confidence |
|---------|-------------------|------------|
| [Finding 1] | [Data point / quote / statistic] | High / Medium / Low |
| [Finding 2] | [Data point / quote / statistic] | High / Medium / Low |
| [Finding 3] | [Data point / quote / statistic] | High / Medium / Low |

---

### So What? (Interpretation)

[For each key finding: what does this mean? What is the implication?]

Finding 1 means: [Interpretation]
Finding 2 means: [Interpretation]
Finding 3 means: [Interpretation]

---

### Now What? (Recommendations)

| Recommendation | Priority | Rationale | Who Needs to Act |
|---------------|----------|-----------|-----------------|
| [Action 1] | High | [Why, based on findings] | [Team/person] |
| [Action 2] | Medium | [Why, based on findings] | [Team/person] |

---

### What We Don't Know (Limitations)

- [Gap 1: what this research cannot answer]
- [Gap 2: assumption that could not be validated]

### Suggested Next Steps for Further Research

- [If the above recommendations are adopted, what should be measured next?]
```

---

## Research Report Structure

**Standard structure for a research deliverable**:

```
1. Executive Summary (1 page)
   - Research question
   - Methodology in one sentence
   - 3-5 key findings
   - Top 2-3 recommendations
   - Confidence level

2. Background & Objectives
   - Business context
   - Specific research questions answered
   - Scope and boundaries

3. Methodology
   - Data sources and collection methods
   - Analytical approach
   - Limitations and caveats

4. Findings
   - One section per key finding
   - Evidence first, interpretation second
   - Quantitative and qualitative data integrated

5. Synthesis & Implications
   - So-what layer
   - Cross-finding patterns
   - Strategic implications

6. Recommendations
   - Specific, actionable
   - Prioritized
   - Owner and timeline indicated

7. Appendix
   - Raw data tables
   - Full methodology details
   - Source list
   - Survey instrument (if applicable)
```

**Length calibration**:
- Decision-support memo: 1-2 pages
- Standard research report: 5-10 pages
- Deep research study: 15-30 pages with full appendix
- Executive briefing deck: 8-12 slides

---

## Presentation of Findings

**Data visualization selection**:

| Chart Type | Best For | Avoid When |
|-----------|----------|------------|
| **Bar chart** | Comparing categories at one point in time | More than 8-10 categories |
| **Line chart** | Trends over time | Comparing categories without a time dimension |
| **Scatter plot** | Showing relationship between two variables | Non-technical audiences without annotation |
| **Pie / donut** | Part-to-whole for 3-5 categories | More than 5 slices; precise comparison needed |
| **Table** | Exact values matter; multiple dimensions | When a chart would communicate the pattern faster |
| **Heat map** | Two-dimensional patterns across a matrix | When the audience needs precise values |
| **Waterfall** | Cumulative change (contributions to a total) | Simple before/after comparison (use bar) |

**Storytelling with data — the three-act structure**:

```
Act 1: Here is the situation (context)
"We set out to understand why retention dropped in Q3."

Act 2: Here is the complication (finding)
"The data shows retention dropped 12 points, concentrated entirely in the
second week of onboarding — specifically, users who did not complete the
first integration step."

Act 3: Here is the resolution (recommendation)
"If we intervene at the integration step with a guided setup flow,
we estimate we can recover [X] of the lost retention. Here is what
that intervention looks like."
```

**Design principles for research presentations**:
- One message per slide. The headline should state the finding, not the topic.
  - Weak headline: "Retention Analysis"
  - Strong headline: "Retention drops in week 2 for users who skip integration"
- Annotate charts directly. Do not make the audience decode the legend and then find the point you want them to see.
- Show the data, then the interpretation. Audiences are more persuaded when they see the evidence before the conclusion.
- Acknowledge limitations proactively. Researchers who hide limitations lose credibility when they are discovered.

---

## Competitive Research Toolkit

**Public sources by type**:

| Source | What You Can Find |
|--------|-----------------|
| **Company website** | Positioning, messaging, product surface, pricing (if public), team size signals from About/Careers |
| **Job postings** | Investment areas, technology stack, org structure, growth plans, pain points in current setup |
| **LinkedIn** | Headcount trends, team composition, executive backgrounds, recent hires, departures |
| **G2 / Capterra / Trustpilot** | Customer complaints, praise patterns, feature gaps, use case adoption |
| **SEC filings (10-K, 10-Q, S-1)** | Revenue, segment performance, risk factors, strategic priorities (public companies only) |
| **Patent databases (USPTO, Google Patents)** | Proprietary technology, R&D investment areas, future product direction signals |
| **Crunchbase / PitchBook** | Funding history, investor composition, valuation signals, M&A activity |
| **Press releases / news** | Product launches, partnerships, executive changes, customer wins |
| **Web traffic (SimilarWeb, SEMrush)** | Traffic volume, traffic sources, keyword strategy, top pages |
| **App store reviews** | Mobile product quality, feature gaps, user frustration, NPS signals |
| **GitHub** | Open-source activity, technology choices, engineering team engagement |
| **Wayback Machine** | Historical positioning, pricing, and messaging evolution |

**Job posting as competitive signal** — a practical technique:
When a competitor posts 5 data science roles and 3 ML engineer roles, they are likely building a new AI capability. When they post 8 customer success roles, they may have a retention problem. When they stop posting engineering roles, they may be in cost-cutting mode. Read job postings not for what they say about the job, but for what they reveal about the company's priorities and gaps.

**Competitive intelligence compilation template**:
```markdown
## Competitor Profile: [Company Name]

**Updated**: [Date]
**Analyst**: [Name]

### Overview
- Founded / HQ / Funding stage / Employee count
- Primary product / ICP / Core value proposition

### Positioning
- Primary message (from homepage hero)
- How they differentiate (from their "Why Us" / comparison pages)
- Target persona signals

### Product
- Core capabilities
- Recent launches / changes
- Known gaps (from reviews, support forums, sales battlecard intel)

### Go-to-Market
- Pricing model (if public)
- Primary acquisition channels (traffic sources, paid keywords)
- Partnership model

### Financial Signals
- Revenue estimates / disclosed ARR
- Recent funding / valuation signals
- Burn indicators

### Strategic Watch Items
- [What to monitor — e.g., product area they are investing in, market they are entering]
```

---

## Desk Research Efficiency Techniques

**Time-boxing**: Assign a maximum time to each source category before starting. Without limits, research expands to fill the time available.

**Progressive refinement**: Do a 30-minute scan before a 3-hour deep dive. The scan tells you which areas need depth.

**Search string construction**:
```
Specific term: "competitor pricing" site:g2.com
Exact phrase: "customer acquisition cost" "SaaS" 2024
Exclude noise: market size -forbes -"business wire"
Related terms: pricing OR "price" OR "subscription" "company name"
File type: filetype:pdf "annual report" "company name"
```

**Research log** — maintain a running log while researching to avoid re-visiting sources and to make the methodology reproducible:
```
| Time | Source | URL | Key Finding | Quality (H/M/L) |
|------|--------|-----|-------------|----------------|
| 09:10 | G2 reviews | [URL] | 23% of reviews mention slow reporting | High |
```

**Triangulation rule**: Any finding that will appear in a recommendation must be supported by at least two independent sources. Single-source findings should be labeled as preliminary or unconfirmed.

**When to stop**: Research follows the law of diminishing returns — each additional hour produces fewer new insights. Stop when:
- New sources are repeating findings you already have
- The remaining gaps cannot be closed with available sources
- The confidence level is sufficient for the decision at hand

---

## Operating Principle

> "Research is not about finding the answer you expect. It is about building enough evidence to make a confident decision and knowing precisely where the remaining uncertainty lives."
