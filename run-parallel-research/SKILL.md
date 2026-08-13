---
name: run-parallel-research
description: Coordinate cost-aware, source-backed research by assigning narrow discovery and evidence-sifting lanes to inexpensive subagent models, then handing a compact evidence ledger to one strong model for verification, reconciliation, and synthesis. Use when the user explicitly asks for agents, parallel research, a wide search, multiple independent investigations, combined results, or a cheap-research-then-strong-analysis workflow. Do not use for a simple lookup, a narrow factual question, or work that cannot benefit from independent lanes.
---

# Run Parallel Research

Conduct one coordinated investigation. Treat subagents as independent researchers, not as extra votes for the same answer.

## Route Models by Job

Use a cost-first two-tier architecture whenever model overrides are available:

1. Assign discovery, browsing, extraction, filtering, and evidence normalization to `gpt-5.6-luna` with `low` reasoning effort.
2. Assign final verification, contradiction resolution, prioritization, and synthesis to exactly one `gpt-5.6-sol` agent with `high` reasoning effort.

Prefer the personal custom agent named `research_scout` when it is available. Its configuration pins Luna, low reasoning, read-only access, compact output, and no recursive delegation. Otherwise, set the same model and effort explicitly on each research spawn.

If the coordinating agent is already running `gpt-5.6-sol` with high reasoning, perform synthesis there instead of spawning another Sol agent. If Luna is unavailable, use `gpt-5.6-terra` with low reasoning, then the cheapest available tool-capable model. Never silently let research scouts inherit an expensive Sol configuration.

If no inexpensive subagent model can be selected, avoid multi-agent fan-out. Run one bounded research pass in the coordinator and disclose that the requested cost routing was unavailable.

Treat model routing as best effort because model availability can vary by client, account, and runtime. Do not claim a specific price or usage reduction unless the runtime exposes measured usage.

Give research agents minimal task-local context. When the spawn interface supports it, use no conversation fork or the smallest useful recent-turn fork. Do not send the full conversation, unrelated history, other agents' reports, or the intended conclusion.

## Establish the Research Contract

Extract or infer:

- the exact question or decision the research must support;
- scope boundaries, including geography, time period, audience, and exclusions;
- the required freshness and evidentiary standard;
- the desired deliverable, such as a recommendation, comparison, resource list, or evidence map.

Ask a question only when an unresolved choice would materially change the research. Otherwise, state the assumption briefly and proceed.

Keep research read-only unless the user separately authorizes external writes, purchases, submissions, messages, or other mutations.

Set an effort bound before delegation. Use two research lanes by default. Give each lane at most two focused search cycles, retain at most five strong sources, and request no more than 700 words of output. Stop a lane when every assigned subquestion has adequate evidence or when two consecutive searches add no material evidence. If the requested scope cannot fit that bound, prioritize the decision-critical areas and disclose the omitted coverage.

Add a third lane only when the user explicitly requests exhaustive coverage or a third evidence surface is essential and the increased usage is justified. Never allow research scouts to spawn their own agents.

## Design Independent Lanes

Create two bounded lanes that can run independently within the available agent slots. Divide by evidence surface, stakeholder, geography, technical layer, hypothesis, or source class. Do not give multiple agents the same generic prompt.

Prefer lanes such as:

1. Primary and official evidence
2. Market, practitioner, or implementation evidence
3. Counterevidence, limitations, and current verification

Adapt the lanes to the question. For example, a job search can use role families or geographies; a technical comparison can use architecture, operating evidence, and failure modes; a resource search can use official materials, strong community resources, and quality verification.

Reserve the coordinating agent for synthesis and the highest-risk verification. Do not use recursive delegation.

## Delegate with Explicit Contracts

Before spawning subagents, tell the user how the investigation is divided. Give every subagent a concrete, non-overlapping assignment containing:

- the lane question and boundaries;
- inclusion and exclusion rules;
- freshness requirements;
- preferred source types;
- the expected return structure;
- a requirement to report uncertainty and failed searches.

Require each research subagent to return a compact evidence ledger:

```text
Lane conclusion: 3 sentences maximum
Evidence: 5 rows maximum
- Claim | direct support | source URL | date | confidence | caveat
Rejected: 3 entries maximum, each with reason
Open questions: 3 maximum
```

Tell subagents not to hide uncertainty, invent citations, or treat search-result snippets as evidence. Ask them to open and inspect retained sources.

Tell subagents to honor a stop or time-box request by returning their best currently verified evidence immediately, even if the lane is incomplete.

Run independent lanes concurrently. While they work, define the comparison criteria and synthesis rubric. Do not duplicate their broad searches in the coordinating agent.

If subagents are unavailable, execute the same lanes sequentially and disclose that limitation. Do not pretend that parallel validation occurred.

## Apply the Evidence Standard

Prefer primary sources: official documentation, direct employer or institution pages, original datasets, standards, filings, and research papers. Use reputable secondary sources when they add analysis unavailable from primary material.

For technical research, rely on official documentation and original research for factual claims. For current listings, products, pricing, laws, schedules, or other unstable facts, verify against a live authoritative page.

For every retained decision-driving claim, record:

- what the source directly establishes;
- the source date and whether freshness matters;
- whether the conclusion is evidence, a reasonable inference, or unresolved;
- any material conflict with another source.

Reject inaccessible, stale, geography-ambiguous, circularly cited, purely promotional, or unsupported evidence when it cannot meet the research contract.

## Reconcile the Agent Results

Pass the strong synthesis model only the user's decision, the comparison criteria, the compact evidence ledgers, and clearly marked conflicts. Do not pass raw agent transcripts, search logs, discarded snippets, or the full conversation when a smaller handoff is sufficient.

Do not concatenate agent reports. Build a single evidence set and:

1. Deduplicate repeated findings and sources.
2. Compare conflicting claims against source authority, directness, and recency.
3. Independently open and verify the two or three most consequential sources and every source involved in a material conflict.
4. Trace surprising or unusually strong claims back to primary evidence.
5. Separate consensus, disagreement, inference, and missing evidence.
6. Remove findings that fail the original inclusion rules.

Do not resolve disagreement by majority vote. Explain why one claim is better supported, or preserve the disagreement when evidence remains inconclusive.

## Deliver One Synthesized Answer

Lead with the answer, recommendation, or strongest supported conclusion. Then provide only the structure the decision needs, typically:

- the most important findings;
- a compact comparison or prioritized shortlist when useful;
- meaningful contradictions and caveats;
- rejected options when their rejection prevents wasted effort;
- remaining unknowns and the next verification step.

Place citations next to the claims they support. Link directly to source pages, not search results. Never expose internal agent identifiers, raw agent transcripts, duplicated notes, or an unedited dump of links.

End with a short scope note stating how many research lanes were used, what was independently verified, and any important coverage limitation. Do not imply that agent count guarantees correctness or completeness.

Do not include agent-by-agent prose or a long methodology section in the final response. The expensive synthesis pass should spend its budget on judgment, not on restating the research process.

## Quality Gate

Before finishing, confirm that:

- the lanes were genuinely distinct;
- inexpensive models handled research and only one strong-model synthesis pass was used;
- research outputs stayed within the compact evidence-ledger contract;
- retained sources satisfy the requested scope and freshness;
- decision-driving claims were checked by the coordinator;
- contradictions were resolved or made explicit;
- the answer distinguishes fact from inference;
- the synthesis answers the user's real decision rather than merely summarizing sources.
