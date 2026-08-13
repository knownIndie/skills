---
name: run-deep-parallel-research
description: Conduct quality-first, comprehensive research with multiple capable subagents, broad evidence coverage, follow-up investigation, independent verification, contradiction resolution, and one integrated synthesis without a preset cost, search-cycle, source-count, or output-length budget. Use only when the user explicitly invokes this skill or clearly requests unrestricted, exhaustive, no-cost-limit, maximum-depth, or quality-over-usage parallel research. Do not use for ordinary wide searches, simple lookups, narrow questions, or cost-sensitive work.
---

# Run Deep Parallel Research

Conduct one comprehensive investigation. Optimize for evidence quality and coverage rather than model cost or minimum token use. Do not interpret the absence of a preset budget as permission to search forever. Stop when the coverage criteria are satisfied and additional work no longer changes the conclusion.

## Establish the Research Contract

Extract or infer:

- the exact question or decision the research must support;
- scope boundaries, including geography, time period, audience, and exclusions;
- freshness and evidentiary requirements;
- the required depth and coverage dimensions;
- the desired deliverable, such as a recommendation, comparison, resource map, risk assessment, or prioritized shortlist.

Ask a question only when an unresolved choice would materially change the investigation. Otherwise, state the assumption and proceed.

Keep research read-only unless the user separately authorizes external writes, submissions, purchases, messages, or other mutations.

## Build a Coverage Map

Before delegation, list the distinct questions that must be answered for the result to be complete. Convert them into independent lanes that can run concurrently within the available agent slots.

Divide by evidence surface, hypothesis, stakeholder, geography, technical layer, source class, or failure mode. Useful lanes include:

1. Primary and official evidence
2. Practitioner, implementation, or market evidence
3. Counterevidence, limitations, and adversarial verification

Use two or three subagents initially. Add follow-up work only when a lane exposes a consequential gap, contradiction, or new branch that cannot be resolved during synthesis. Avoid redundant prompts and unnecessary recursive fan-out.

## Use Capable Models

Favor the strongest available model with high reasoning for research lanes that require judgment, complex source reconciliation, or ambiguous inclusion decisions. Do not downgrade research agents merely to reduce usage.

Use explicit model overrides when the runtime supports them. Prefer `gpt-5.6-sol` with `high` reasoning for demanding research and final synthesis. A simpler lane may use another capable model when quality is unaffected, but cost is not the deciding factor for this skill.

Reserve the coordinating agent for coverage management, cross-lane reconciliation, and final judgment. If the coordinator is not already using a strong high-reasoning model, use one strong synthesis agent after research and pass it the evidence, conflicts, and decision criteria.

## Delegate with Independent Contracts

Before spawning subagents, tell the user how the investigation is divided. Give every agent a bounded, non-overlapping assignment containing:

- the lane question and boundaries;
- inclusion and exclusion rules;
- freshness requirements;
- preferred source types;
- claims that require direct verification;
- the expected return structure;
- a requirement to report weak evidence, rejected candidates, failed searches, and uncertainty.

Require each agent to return:

```text
Lane conclusion:
Coverage completed:
Key findings:
- Claim | direct supporting evidence | source URL | publication or update date | confidence
Contradictory or weak evidence:
Rejected candidates and reason:
Open questions and recommended follow-up:
```

Tell subagents to open every retained source, trace important claims to primary evidence, and avoid treating search-result snippets or repeated secondary claims as proof.

Run independent lanes concurrently. While they work, define the comparison rubric and investigate the highest-risk assumption directly.

## Apply a Strong Evidence Standard

Prefer official documentation, direct employer or institution pages, original datasets, standards, filings, public records, and research papers. Use reputable secondary sources when they contribute analysis that primary sources do not provide.

For technical research, rely on official documentation and original research for factual claims. For current listings, products, pricing, laws, schedules, specifications, or other unstable facts, verify against a live authoritative page.

For each decision-driving claim, establish:

- what the source directly proves;
- the source date and whether freshness affects validity;
- whether the conclusion is fact, inference, disputed, or unresolved;
- whether another independent source confirms or contradicts it;
- what evidence would falsify or materially weaken it.

Reject inaccessible, stale, circularly cited, geography-ambiguous, purely promotional, fabricated, or unsupported evidence when it cannot meet the research contract.

## Inspect Coverage and Run Follow-Ups

After the initial lanes finish, compare their results against the coverage map. Do not synthesize prematurely when a decision-critical question remains unanswered.

Run a focused follow-up when:

- primary and secondary sources materially disagree;
- a surprising claim lacks direct evidence;
- a retained candidate has uncertain eligibility, freshness, or scope;
- two agents reached incompatible conclusions;
- a missing evidence surface could reverse the recommendation.

Do not run follow-ups merely to accumulate more sources. Stop expanding a lane when new searches repeat existing evidence, only surface lower-quality material, or cannot plausibly alter the conclusion.

## Reconcile the Evidence

Do not concatenate agent reports. Build a single evidence set and:

1. Deduplicate repeated findings and sources.
2. Rank evidence by authority, directness, recency, independence, and relevance.
3. Independently open and verify every source that materially drives the conclusion.
4. Trace unusually strong or consequential claims to primary evidence.
5. Resolve contradictions through evidence quality, not agent majority.
6. Preserve disagreement when available evidence remains inconclusive.
7. Remove findings that fail the original inclusion rules.
8. Separate established facts, reasonable inferences, contested claims, and unknowns.

## Deliver One Integrated Answer

Lead with the answer, recommendation, or strongest supported conclusion. Then provide the structure needed to evaluate it, including:

- the most important findings;
- a comparison matrix or prioritized shortlist when useful;
- the evidence behind each decision-driving conclusion;
- material contradictions, counterarguments, and limitations;
- rejected options when their rejection prevents wasted effort;
- remaining unknowns and the next verification step.

Place citations next to the claims they support and link directly to source pages. Do not expose raw agent transcripts, internal agent identifiers, repeated notes, or an unedited link dump.

End with a concise scope note stating the lanes used, important follow-ups performed, what was independently verified, and any unresolved coverage limitation.

## Quality Gate

Before finishing, confirm that:

- every coverage-map question was answered or explicitly marked unresolved;
- research lanes were genuinely distinct;
- models were selected for quality rather than lowest cost;
- retained sources satisfy the requested scope and freshness;
- all decision-driving sources were checked by the coordinator;
- contradictions were resolved or preserved transparently;
- facts and inferences are clearly separated;
- additional searching is unlikely to change the conclusion materially;
- the synthesis answers the user's decision rather than merely summarizing sources.
