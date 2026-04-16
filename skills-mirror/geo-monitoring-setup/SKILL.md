---
name: geo-monitoring-setup
description: Tier 0 Generative Engine Optimization monitoring. 10 queries x 4 engines x monthly cadence, CSV logging, zero vendor dependency.
argument-hint: --brand NAME [--queries FILE] [--engines LIST]
metadata:
  skill_type: task-capability
  owner: seo-specialist
  primary_consumers:
  - ext-marketing
  sensitive: false
---
# GEO Monitoring Setup (Tier 0)

**Agent**: @seo-specialist
**Version**: 1.0.0
**Status**: Active
**Pattern**: Pattern 1 Consultation (default)

---

## Purpose

Before you optimize, measure. This skill produces a reliable monitoring baseline that tells you whether your brand shows up in LLM-generated responses, how it shows up, and how that changes over time, with zero infrastructure and zero vendor dependency. It is deliberately the Tier 0 MINIMUM VIABLE setup: 10 queries, 4 engines, monthly cadence, a CSV, and roughly forty API calls a month costing under a dollar total. Everything bigger than that (dashboards, alerting, multi-market segmentation, citation graph analysis) is a future tier that you only earn the right to build after you have two or three months of Tier 0 data in hand.

The skill exists because the generative search landscape has moved faster than the tooling around it, and the majority of "AI search monitoring" vendors in market today were founded in 2023 or 2024 against a surface area that is still shifting underneath them. Buying a vendor contract before you have a baseline is expensive and premature. Writing forty API calls is cheap and honest.

---

## When to Use

- **New brand launch** — establish whether the brand registers at all in LLM answers before you invest in GEO content
- **Post-launch visibility baseline** — the first measurement that lets you say "we were at X in month 1, we are at Y in month 6"
- **Pre-investment decision on GEO tooling** — you need two to three months of baseline data before any vendor conversation is informed rather than speculative
- **Quarterly brand health review** — light-touch monitoring that sits alongside traditional SEO reporting
- **Post-campaign attribution sanity check** — after a major content push, did LLM visibility move, or did you just fill a content calendar

## When NOT to Use

- **Comprehensive SEO audit** — use `/llm-seo` (existing skill, different scope) or a traditional SEO audit skill
- **Content optimization workflow** — that is a different problem; Tier 0 is measurement, not production
- **Competitor deep-dive** — use `/competitive-intelligence`; this skill captures competitor mentions only as a side effect
- **Real-time monitoring** — Tier 0 is monthly, human-triggered. If you need real-time you are at a different tier and this skill is the wrong tool
- **Content gap analysis at scale** — wait for month 2 to month 3 data, then escalate to a future `/geo-audit` skill (currently deferred)

---

## Required Inputs

| Input | Required | Notes |
|---|---|---|
| Brand name | Yes | Canonical form as used on the brand's own site |
| Brand context | Yes | 1-2 paragraph description: what the brand sells, who it serves, what markets it targets, what differentiates it |
| Query list override | Optional | If you already have a curated query list, pass it instead of drafting new |
| Engine list override | Optional | Defaults to all 4; use override if one API key is missing this month |
| Historical CSV | Optional | If this is a re-run, pass the existing log so you can compare deltas |

If brand context is thin, stop and ask for more. A weak context produces generic queries, which produce noisy baselines, which defeat the purpose of running the skill at all.

---

## Method (7 Steps)

### Step 1: Draft 10 Target Queries

Read the brand context and draft exactly 10 queries that a real user might type into ChatGPT, Claude, Gemini, or Perplexity when they have a need the brand could plausibly satisfy. This is the most important step. Get it wrong and every downstream measurement is noise.

Apply the question-phrasing test to each draft: does this look like how a user would actually prompt an LLM, or does it look like a keyword tool export. If it looks like a keyword, rewrite it. A keyword is "best microbrand watches 2026". A query is "What are the best microbrand watches under 500 dollars in 2026?" The query has a question mark, a budget, a year, and reads like speech. Users do not type keywords into ChatGPT.

If drafting is hard because the category is unfamiliar, consult @content-strategist. If you want a competitor-aware framing, consult @competitive-intelligence. Both are Pattern 1 Consultation.

### Step 2: Validate the 10 Queries

Run each query through three criteria:

1. **Brand-plausible** — could the brand genuinely appear in a high-quality answer to this query? If the brand sells microbrand watches and the query is about enterprise ERP systems, delete the query.
2. **User-intent-aligned** — does the query represent a real user need? Or is it an SEO vanity metric phrased as a question? "What is the best microbrand watch" is a real user need. "Is SKYMOD the best microbrand watch" is a vanity query that no real user types.
3. **Diverse coverage** — collectively, do the 10 queries cover at least 3 distinct user intents? If all 10 are variants of "what is the best X", you are measuring one thing with ten probes. Rewrite until you cover at least 3 of: purchase intent, research intent, comparison intent, gift intent, task intent, troubleshooting intent, technical intent.

If a query fails any of the three checks, rewrite or replace it. The 10-query list is the single most important artifact the skill produces. Everything downstream is mechanical.

### Step 3: Configure the 4 API Keys

You need API access to four engines. All four are real, public, and cost a fraction of a cent per call at the volumes this skill uses.

| Engine | API | Notes |
|---|---|---|
| ChatGPT | OpenAI API | Use GPT-4 or GPT-4o, not GPT-3.5. Pin the model version so month-over-month comparisons are valid |
| Claude | Anthropic API | Use a Sonnet or Opus tier, not Haiku. Pin the model version |
| Gemini | Google AI API | Use Gemini Pro or Ultra. Note whether grounding with Google Search is on or off in the Notes column, because it materially changes output |
| Perplexity | Perplexity API | Perplexity returns citations by default, which is why it is the strongest signal for the Citation URL column |

For each engine, get an API key from the engine's own developer portal (not from a reseller or a wrapper). Store keys in an environment file outside of version control. The skill does not require any orchestration framework, queue, or scheduler to run. It is a script on a laptop.

### Step 4: Run the 10-Query x 4-Engine Sample

Forty API calls. Total cost at current list pricing is well under a dollar across all four engines combined, assuming short responses and no batching. Wall-clock time is a few minutes.

For each call:
- Use a neutral system prompt ("You are a helpful assistant.") or the engine's default
- Ask the query verbatim, no preamble, no prompt engineering
- Capture the full response text
- Capture the response timestamp
- Capture any citation URLs the engine surfaces (Perplexity always, Gemini sometimes, ChatGPT rarely, Claude almost never)

Do not retry on failure during the sample run. If an engine fails, log the failure and move on. Tier 0 is fail-fast and human-triggered — a retry loop is noise masquerading as signal.

### Step 5: Parse Results

For each of the forty responses, determine the four classification values:

- **Brand Mentioned** — did the response name the brand? `yes` if the brand name appears literally. `no` if it does not appear. `partial` if the response describes the brand without naming it (e.g., "a popular microbrand watch company from Hungary" is `partial` for SKYMOD).
- **Mention Position** — if the brand is mentioned, where does it appear in an ordered list (if any)? Rank 1 is first, rank 2 is second, and so on. If the mention is in prose rather than a list, use `prose` in the Position column. If not mentioned, `null`.
- **Sentiment** — `positive` (response recommends the brand or speaks favorably), `neutral` (response names the brand factually without judgment), `negative` (response warns against or criticizes the brand), `mixed` (response includes both positive and negative framing).
- **Citation URL** — if the engine provided a citation URL for the brand mention, capture it. Otherwise `null`.

Parsing can be done manually (forty responses is tractable) or via a simple classifier prompt on one of the four models. Manual is more reliable at Tier 0 because you build mental model of how each engine talks about the brand.

### Step 6: Log to CSV

Append each of the forty rows to the monitoring CSV using the schema documented below. One file, not one file per engine or per month. One file is the archive, and month-over-month trend is a filter on the Date column.

### Step 7: Schedule the Monthly Re-Run

Create a calendar reminder, not a cron job. Tier 0 is human-triggered on purpose. The point is to force you to read each month's output before filing it, because the readings are the signal and automation robs you of that.

Pick a day of the month (first Tuesday works well) and put a 30-minute block on your calendar. Repeat monthly. The re-run itself is 10 minutes of API calls plus 20 minutes of parsing and logging.

---

## Query Design Rules

These rules are the load-bearing contribution of the skill. The quality of the 10 queries determines whether the monitoring baseline is useful or noise.

1. **Question-phrased, not keyword-phrased** — "What are the best X?" beats "best X 2026". Question phrasing matches how users actually prompt LLMs; keyword phrasing matches how users prompt Google circa 2015.

2. **Intent-diverse** — cover at least 3 distinct user intents across the 10 queries. The intent categories to choose from: purchase intent ("where can I buy..."), research intent ("what are the differences between..."), comparison intent ("compare X vs Y"), task intent ("I need to... what should I use"), troubleshooting intent ("my X is broken, what should I do"), gift intent ("I want to buy a gift for..."), technical intent ("what movement does X use").

3. **Brand-plausible** — every query must be one where the brand could plausibly appear in a good answer. If you draft a query where the brand has no business appearing, you are measuring the engine's refusal behavior rather than your brand's visibility.

4. **Regional where relevant** — if the brand targets specific markets, include at least 2 queries with regional scoping. "Best microbrand watches available in Germany" is a valid query for a brand that ships to Germany. This catches engines that default to a US-centric answer.

5. **Competitor-inclusive but not hostile** — "compare X vs Y" is a valid comparison query. "Why is X worse than Y" is a leading query that will produce leading output. Don't ask questions that assume an answer.

6. **Avoid SEO jargon inside the query** — no "SERP," "SEO," "rank," "keyword", "organic" in the query text itself. Users do not phrase questions that way. The question "what SERP rank does X have" is a query a marketer would type, not a query a buyer would type.

7. **One query per intent, not ten** — resist the urge to draft ten variants of the same question. Ten variants of "what is the best X" measure the same thing ten times. Draft ten different things.

---

## CSV Schema

Eight columns. One row per API call. Appended, never overwritten.

| Column | Type | Rules |
|---|---|---|
| **Date** | ISO 8601 | `2026-04-11` format. The date the sample was run, not the date the log was written |
| **Engine** | enum | `chatgpt`, `claude`, `gemini`, `perplexity`. Lowercase, no variants |
| **Query** | string | The literal query text sent to the engine. Must match exactly across months for longitudinal validity |
| **Brand Mentioned** | enum | `yes`, `no`, `partial`. `partial` means the brand was referenced descriptively but not named |
| **Mention Position** | integer or enum or null | Integer rank if the mention was in an ordered list. `prose` if the mention was in prose without an explicit rank. `null` if not mentioned |
| **Sentiment** | enum | `positive`, `neutral`, `negative`, `mixed`. `null` if not mentioned |
| **Citation URL** | URL or null | The citation URL the engine provided for the brand mention, if any |
| **Notes** | free text | Anomalies: refused to answer, hedged, incorrect information about the brand, grounding on/off for Gemini, any edge case worth capturing |

Save as `geo-monitoring-log.csv` in the brand's marketing folder. Do not split by month or engine — one file, filtered in analysis.

---

## Script Template

A minimal Python script to run the 40-call sample. Roughly 60 lines. Exits on first API failure; there is no retry loop. Model versions are pinned to make month-over-month comparisons valid.

```python
#!/usr/bin/env python3
"""
geo-monitoring-sample.py
Tier 0 GEO monitoring: run 10 queries x 4 engines, print results.
Logging to CSV is a separate manual step (Step 6).
"""

import os
import csv
import sys
import json
from datetime import date
from pathlib import Path

# Real client libraries. Install with:
#   pip install openai anthropic google-generativeai requests
from openai import OpenAI
from anthropic import Anthropic
import google.generativeai as genai
import requests

# Pin model versions for month-over-month validity.
CHATGPT_MODEL = "gpt-4o"                 # not gpt-3.5
CLAUDE_MODEL = "claude-sonnet-4-20250514"
GEMINI_MODEL = "gemini-1.5-pro"
PERPLEXITY_MODEL = "sonar-pro"

SYSTEM_PROMPT = "You are a helpful assistant."

def load_queries(path: Path) -> list[str]:
    queries = [line.strip() for line in path.read_text().splitlines() if line.strip()]
    if len(queries) != 10:
        sys.exit(f"Expected exactly 10 queries, got {len(queries)}")
    return queries

def ask_chatgpt(client: OpenAI, query: str) -> str:
    r = client.chat.completions.create(
        model=CHATGPT_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ],
    )
    return r.choices[0].message.content

def ask_claude(client: Anthropic, query: str) -> str:
    r = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": query}],
    )
    return r.content[0].text

def ask_gemini(query: str) -> str:
    # Note: grounding with search is OFF in this config.
    # If you flip it on, log the change in the CSV Notes column.
    model = genai.GenerativeModel(GEMINI_MODEL)
    r = model.generate_content(query)
    return r.text

def ask_perplexity(api_key: str, query: str) -> dict:
    r = requests.post(
        "https://api.perplexity.ai/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": PERPLEXITY_MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": query},
            ],
        },
        timeout=60,
    )
    r.raise_for_status()
    return r.json()

def main():
    queries_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("queries.txt")
    queries = load_queries(queries_path)

    openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    anthropic_client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    perplexity_key = os.environ["PERPLEXITY_API_KEY"]

    today = date.today().isoformat()
    results = []

    for q in queries:
        results.append(("chatgpt", q, ask_chatgpt(openai_client, q)))
        results.append(("claude", q, ask_claude(anthropic_client, q)))
        results.append(("gemini", q, ask_gemini(q)))
        pplx = ask_perplexity(perplexity_key, q)
        results.append(("perplexity", q, json.dumps(pplx)))

    out_path = Path(f"geo-sample-{today}.json")
    out_path.write_text(json.dumps(
        [{"date": today, "engine": e, "query": q, "response": r} for e, q, r in results],
        indent=2,
    ))
    print(f"Wrote {len(results)} responses to {out_path}")
    print("Next: parse manually (Step 5) and append to geo-monitoring-log.csv (Step 6).")

if __name__ == "__main__":
    main()
```

**Runtime**: ~3-5 minutes wall-clock for the full 40 calls. **Cost**: well under $1 at current API pricing, dominated by Perplexity and GPT-4o. **Dependencies**: four API client libraries, one plain-text queries file, four environment variables. No orchestration framework, no queue, no scheduler.

---

## Engine-Specific Notes

Pointer-only. The engines move fast and any specific advice older than a quarter should be re-verified against the engine's own docs.

- **ChatGPT (OpenAI)** — Use GPT-4 or GPT-4o. Do not use GPT-3.5, it is a different generation and not representative of current ChatGPT UX. System prompt should be the neutral default. Browsing is off unless you explicitly enable it; if you enable it, log that in the Notes column because it materially changes output.

- **Claude (Anthropic)** — Use a Sonnet or Opus tier. Do not use Haiku for this skill, it is a different capability class and its answers will not track what a user in the consumer Claude app sees. No system prompt beyond the neutral default.

- **Gemini (Google)** — Gemini Pro or Ultra. **Critical**: Gemini's default grounding with Google Search can flip results dramatically from run to run. Either pin grounding to OFF for consistency, or log the grounding state in the Notes column for every row. Inconsistency here is the most common source of false month-over-month "drift."

- **Perplexity** — Perplexity returns citation URLs by default, which makes it the strongest signal for the Citation URL column. It is also the engine most likely to surface the brand if the brand has any web presence at all, because Perplexity's grounding is always on. This means Perplexity's baseline will diverge from the other three, and that is a feature, not a bug — it tells you what your web presence looks like to a grounded engine.

---

## Interpretation Guide

How to read the CSV at each milestone.

### Month 1: Baseline

Count `yes` + `partial` rows out of the 40. That is your raw visibility score. Typical ranges:

- 0-5 mentions out of 40: the brand is effectively invisible in LLM answers. This is the starting point for many early-stage brands. Not a failure, just a baseline.
- 5-15 mentions out of 40: the brand has partial visibility, usually concentrated in 1-2 engines (often Perplexity plus one other). Understand which engines are working and why.
- 15-30 mentions out of 40: strong visibility. Focus shifts to sentiment and position rather than presence.
- 30+ mentions out of 40: dominant. The interesting question is whether competitors are being surfaced alongside, which you can see in the raw responses.

Also look at: which engines are silent, which queries produced zero mentions across all four engines (these are your content gaps), and whether any engine produced an incorrect fact about the brand (note in the Notes column and address directly).

### Month 3: Trend

Compare month 1, 2, and 3 side by side on three dimensions:

- **Total mention count** — increasing, stable, decreasing
- **Engine distribution** — is one engine consistently silent? Is one engine consistently strong? Why
- **Query-level stability** — which queries are producing consistent mentions and which are flickering on and off? Flickering queries indicate low signal and may be due for replacement

If month 3 shows no change from month 1, and no content or positioning work was done between them, that is expected and the baseline is stable. If month 3 shows change without any intervention, that is the engines drifting, which is useful information in itself.

### Month 6: Pattern Recognition

Six months of data (240 rows) is enough to make confident statements. At month 6 you can:

- Identify which queries are structurally working and which are structurally not (retire the non-performers)
- Identify which engines are stable and which are drifting
- Surface content gaps: queries where the brand SHOULD appear (brand-plausible, high intent) but doesn't
- Decide whether to invest in a `/geo-audit` skill or a vendor tool, with data to back the decision

The `/geo-audit` skill is currently deferred. At month 6, revisit that decision with actual Tier 0 data in hand.

---

## Quality Gates

Run through this checklist before declaring the setup complete.

- [ ] Exactly 10 queries drafted (not 9, not 12)
- [ ] Each query passes the question-phrasing test (reads like speech, not like a keyword)
- [ ] Intent diversity check passed (at least 3 distinct user intents across the 10)
- [ ] Brand-plausibility check passed (every query could plausibly surface the brand in a good answer)
- [ ] 4 API keys configured and tested with a single sanity call
- [ ] CSV schema matches the 8-column spec
- [ ] Monthly calendar reminder created (calendar, not cron)
- [ ] No vendor tool anywhere in the pipeline
- [ ] Pipeline runs on a laptop with no infrastructure beyond the four API keys

If any check fails, the setup is not complete. Tier 0 is rigorous even though it is minimal.

---

## Anti-Patterns

Seven common GEO monitoring failures. If the setup is drifting toward any of these, stop and reset.

1. **SEO keywords disguised as queries** — "best microbrand watches 2026" is a keyword. "What are the best microbrand watches under 500 dollars in 2026?" is a query. Users do not type keywords into ChatGPT. If the query list reads like a keyword tool export, it is wrong.

2. **Single-engine monitoring** — running only against ChatGPT because it is the one you personally use misses drift in Claude, Gemini, and Perplexity, which can move independently and in different directions. All four engines are required to call the setup Tier 0.

3. **Daily cadence** — more is not better. Daily sampling produces noise that drowns the signal, burns API budget, and creates a false sense of motion. Monthly is the floor and also the ceiling for Tier 0.

4. **Vendor tool bought before baseline exists** — signing a vendor contract for an "AI search monitoring" tool before you have two or three months of Tier 0 data means you are paying to confirm a hypothesis you have not formed yet. The Tier 0 data is the input to the vendor decision, not a replacement for it.

5. **Optimizing before measuring** — writing GEO-optimized content before the baseline exists means you have no way to attribute outcomes to interventions. You'll convince yourself it worked; you won't know.

6. **Counting mentions without sentiment or citation** — a `negative` mention is not a win, and a mention without a citation URL has different strategic value from one with. The schema is 8 columns for a reason; a 3-column schema (date / engine / mentioned) is not Tier 0, it is pre-Tier 0.

7. **Query drift month to month** — rephrasing the queries between runs makes the month-over-month trend meaningless, because you are no longer measuring the same thing. Once the 10 queries are locked, they are locked. Retire queries at explicit review points (month 6 is the first), not in response to a bad month.

---

## Related Skills + Hand-Off

| Skill | Relationship |
|---|---|
| `/llm-seo` | Adjacent. Untouched by this skill. Different scope — `/llm-seo` is about making content visible to LLMs; `/geo-monitoring-setup` is about measuring whether it already is |
| `/geo-audit` | Future. Deferred until 2+ months of Tier 0 data exist. A `/geo-audit` skill without baseline data would be speculation dressed as analysis |
| `/competitive-intelligence` | Cross-reference. Use for structured competitor research. This skill captures competitor mentions only as a side effect of the 10 queries |
| `/content-strategy` | Cross-reference. When month 3+ data surfaces content gaps (queries where the brand should appear but doesn't), hand off to `/content-strategy` to plan the fill |
| `/market-researcher` consultation | Use when drafting the 10 queries for a brand in an unfamiliar category |

---

## ROI Framing

Time saved on drafting and triage of the monitoring setup, compared to researching GEO monitoring methodology from scratch and writing the scripts manually.

Base time to produce Tier 0 setup manually: ~6-8 hours (research + query drafting + schema design + script writing + documentation). Complexity: standard (1.0x). Time saved: ~7 hours at a marketing blended rate of $150/hr = ~$1,050 value per setup.

Per monthly re-run, the skill saves an additional ~1 hour of re-research ("how did I do this last time") and lookup, because the method is documented and repeatable. That is ~$150/month in marginal value after the first setup.

---

## Version History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-04-11 | Initial. Tier 0 only. 10 queries x 4 engines x monthly. Phase 5C of the execution plan |
