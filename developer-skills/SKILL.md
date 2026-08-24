---
name: developer-skills
description: Canonical snapshot of Aryan's demonstrated developer and DSA abilities. Read this single file when asked about his skills, DSA level, job fit, what to learn next, or when teaching at his current level.
---

# Developer skills

Canonical path: `knownIndie/skills/developer-skills/SKILL.md`

Last full repository scan: 2026-08-24

This is the normal read path. Read only this file unless the user explicitly asks to refresh, verify, inspect evidence, or update the skill profile.

## How to use this file

When the user says things such as:

- "read my developer skills"
- "check developer skills DSA"
- "based on my skills, teach me this"
- "am I ready for this role?"

use this file as the current compiled state. Do not rescan GitHub first.

## Rules

1. Levels are capability gates, not confidence scores.
2. A level is complete only when every required ability for that level is demonstrated.
3. Using a dependency proves exposure, not mastery.
4. Use `completed`, `developing`, `exposed`, or `not demonstrated` when a simple level would hide uncertainty.
5. Higher-pattern exposure does not skip an incomplete lower gate.
6. Prefer implementation evidence plus a short calibration question over self-rating numbers.
7. For teaching, start from the weakest relevant prerequisite, not the hardest topic previously attempted.
8. For job fit, distinguish "can build with this" from "has production-depth evidence".
9. Keep normal retrieval to this one file. `REPOSITORY_ANALYSIS.md` is evidence for refreshes only.
10. Git history is the long-term change log.

# Current snapshot

| Track | Current gate | Next gate | Main blocker |
| --- | --- | --- | --- |
| DSA | Level 0 completed, Level 1 developing | Level 1 | Two-pointer invariants, prefix sums, independent pattern recognition |
| TypeScript | Level 3 completed | Level 4 | Advanced type/API design and larger library or architecture ownership |
| JavaScript | Level 3 completed | Level 4 | Library-level API design, stronger concurrency/state correctness |
| React / Next.js | Level 2 completed | Level 3 | Frontend tests, accessibility, performance work, larger UI architecture |
| Backend | Level 2 completed, Level 3 developing | Level 3 | Idempotency, jobs/queues, observability, production failure handling |
| Databases | Level 1 completed, Level 2 developing | Level 2 | Transactions, indexes, query plans, stronger constraint/query reasoning |
| DevOps | Level 1 completed | Level 2 | Containers, image registry lifecycle, repeatable deploy/rollback |
| Testing | Level 1 completed, Level 2 developing | Level 2 | Broader integration/E2E strategy and deliberate failure coverage |
| Developer tooling | Level 2 completed, Level 3 developing | Level 3 | Extensibility/plugin architecture, cross-platform hardening |
| Browser extensions | Level 2 completed | Level 3 | Multi-tab/state concurrency, stronger automated testing and release hardening |
| Python | Level 1 completed | Level 2 | More idiomatic modules, tests and larger application ownership |
| AI application development | Level 0 completed, Level 1 developing | Level 1 | Completed end-to-end AI feature with validated structured output |
| System design | Foundations developing | Level 1 | Needs repeated implemented evidence for failures, scaling and tradeoffs |
| Swift / SwiftUI | Historical exposure | Level 0 | Archived learning project only, no current evidence |
| Go | Not demonstrated | Level 0 | No implementation evidence |
| Rust | Not demonstrated | Level 0 | No implementation evidence |

# Capability ladders

## DSA

### Level 0: foundations

Complete when the user can independently:

- traverse arrays and strings
- reason about indices without routine off-by-one mistakes
- use sets and hash maps for membership and frequency counting
- explain common `O(1)`, `O(n)`, `O(n log n)` and `O(n^2)` behavior
- solve straightforward Easy array/string problems without needing the exact operation dictated

Status: completed.

### Level 1: linear patterns

Complete only when the user can independently:

- use hash maps and sets for lookup, frequency and deduplication
- use two pointers and state what each pointer represents before coding
- state and preserve the two-pointer invariant while pointers move
- use prefix sums for cumulative/range reasoning
- use sorting when it changes the structure of a problem
- identify the appropriate pattern on unseen Easy problems without being told the pattern

Status: developing.

Current DSA Level 1 state:

- hash maps / sets: demonstrated
- frequency counting: demonstrated
- basic sorting use: demonstrated
- two-pointer exposure: demonstrated
- two-pointer invariant control: developing
- prefix sums: not sufficiently demonstrated
- unseen-pattern recognition: developing

Promotion test for Level 1:

- solve at least 5 unseen Easy problems across Level 1 patterns
- at least 2 must require two pointers
- no pattern hint before the first approach
- explain the invariant and pointer movement before implementation on the two-pointer problems

### Level 2: core interview patterns

Complete when the user can independently:

- use sliding window
- implement binary search and binary search on an answer space
- use stacks and queues
- manipulate linked lists
- use recursion for bounded search/traversal
- traverse matrices safely
- solve common Easy and easier Medium problems without pattern hints

Status: exposed to several components, but locked until Level 1 completes.

### Level 3: trees and structured search

Complete when the user can independently:

- traverse trees with DFS and BFS
- reason about BST invariants
- use heaps / priority queues
- solve interval problems
- use backtracking
- recognize monotonic-stack opportunities
- explain why the chosen traversal/state is sufficient

### Level 4: graphs and dynamic optimization

Complete when the user can independently:

- model problems as graphs
- use graph DFS/BFS
- use topological sort
- use union-find
- solve common shortest-path problems
- use greedy reasoning with a defensible invariant
- derive 1D and 2D dynamic-programming state/transitions
- use tries where prefix structure matters

### Level 5: interview ready

Complete when the user can repeatedly:

- solve unfamiliar Medium problems under interview time constraints
- combine patterns without hints
- explain complexity before coding
- derive edge cases before submission
- debug a flawed approach instead of restarting blindly
- produce clear code under pressure
- occasionally solve Hard problems without requiring the solution pattern

## Programming languages

Use this ladder for TypeScript, JavaScript, Python, Go, Rust and similar general-purpose languages.

### Level 0

Can read syntax, write small expressions/functions and modify a guided example.

### Level 1

Can independently write small programs/scripts using control flow, collections, functions, modules and normal error handling.

### Level 2

Can build a multi-file application in the language, use its ecosystem/package tooling and debug ordinary runtime/compiler errors without needing line-by-line guidance.

### Level 3

Can use the language across substantial real projects, define reusable modules/interfaces, structure code, test/build/package it and make language-specific tradeoffs rather than treating it as generic pseudocode.

### Level 4

Can design public APIs/libraries, use advanced language features correctly, reason about performance/concurrency/type-system tradeoffs and review complex code written by others.

### Level 5

Can own language-heavy infrastructure or libraries, diagnose hard compiler/runtime/performance problems and teach advanced mechanisms from first principles.

Current language assignments:

- TypeScript: Level 3 completed. Evidence includes full-stack Next.js applications, Turborepo real-time app, typed CLI/tooling, database layers and reusable interfaces.
- JavaScript: Level 3 completed. Strongest evidence is the non-trivial Manifest V3 `VoidYoutube` extension with background/content scripts, DOM injection, storage aggregation and analytics UI.
- Python: Level 1 completed. DSA use is established, but larger Python application/test/module ownership is not.
- Swift / SwiftUI: historical Level 0-type exposure through archived `WeSplit`, not current proficiency.
- Go: not demonstrated.
- Rust: not demonstrated.

## React / Next.js

### Level 0

Can build components, pass props, use basic state and render lists/forms.

### Level 1

Can independently build a small React app with routing/data fetching, reusable components, controlled state and basic loading/error handling.

### Level 2

Can build a full Next.js application using server/client boundaries, forms, auth, database-backed flows, reusable UI and deployment configuration.

### Level 3

Can own a larger frontend with automated component/integration tests, accessibility checks, performance measurement, caching/state strategy and clear feature boundaries.

### Level 4

Can design frontend architecture across teams/features, diagnose difficult performance/runtime issues and establish reliable UI engineering standards.

Current: Level 2 completed. Level 3 developing.

## Backend

### Level 0

Can explain HTTP request/response flow and implement simple handlers.

### Level 1

Can independently build CRUD APIs with validation, persistence, useful errors and correct status handling.

### Level 2

Can build real application backends with authentication/authorization, relational data, migrations, external services and multiple feature domains. Can separate responsibilities into modules/services instead of one handler file.

### Level 3

Can correctly implement and explain caching, rate limiting, background jobs or queues, idempotency, real-time/event-driven flows, structured logs/metrics, health/readiness, retries and production failure handling.

All of these do not need to exist in one project, but the user must demonstrate the underlying failure and correctness reasoning across several implementations.

### Level 4

Can design service boundaries and make defensible tradeoffs around consistency, concurrency, scaling, replication, backpressure and asynchronous workflows.

### Level 5

Can own a substantial production backend, diagnose incidents, evolve architecture safely and explain tradeoffs using real operational evidence.

Current: Level 2 completed. Level 3 developing.

Level 3 evidence already present:

- Redis rate limiting in FOODIO
- Socket.IO + Redis pub/sub in RealtimeChat
- liveness/readiness and environment validation in OpsLab

Level 3 blockers:

- idempotent workflow evidence
- jobs/queue ownership
- operational logs/metrics/tracing used to diagnose real failures
- stronger retry/failure semantics

## Databases

### Level 0

Can perform basic CRUD and explain tables/rows/keys.

### Level 1

Can design ordinary relational schemas, model relationships, use migrations and query through SQL/ORMs in a real application.

### Level 2

Can choose constraints and indexes deliberately, use transactions correctly, reason about query plans/N+1 behavior and write non-trivial joins/aggregations without relying entirely on ORM abstraction.

### Level 3

Can reason about isolation, locking, contention, connection pools, replication and performance under load.

### Level 4

Can own database reliability/performance for a production system and make defensible data-model/storage tradeoffs.

Current: Level 1 completed. Level 2 developing.

## DevOps

### Level 0

Can use environment variables, build commands and basic hosted deployment.

### Level 1

Can create CI quality gates, validate configuration, add liveness/readiness checks and deploy an application with repeatable documented commands.

### Level 2

Can containerize an application, run dependent services locally, build/scan/tag/publish images and perform a documented deploy and rollback.

### Level 3

Can define cloud infrastructure as code, use least-privilege identity/secrets, operate telemetry and perform controlled failure/incident exercises.

### Level 4

Can operate orchestrated workloads, reason about capacity/failures and design reliable deployment/recovery systems.

Current: Level 1 completed. Level 2 not yet demonstrated end to end.

Note: plans inside `Devops-Learning` do not count until implemented.

## Testing

### Level 0

Can manually verify a feature and write a basic unit test with guidance.

### Level 1

Can independently write meaningful automated tests for application/tool logic and run them as part of a quality gate.

### Level 2

Can design unit + integration coverage, test API/database boundaries, create deterministic fixtures and deliberately test important failure paths.

### Level 3

Can add E2E/contract testing where appropriate, control flaky tests and design a test strategy based on risk rather than coverage percentage.

### Level 4

Can establish testing architecture for a larger codebase and diagnose difficult nondeterministic failures.

Current: Level 1 completed. Level 2 developing.

## Developer tooling

### Level 0

Can write useful local scripts/configuration.

### Level 1

Can create a reusable command-line or editor/browser utility for a focused workflow.

### Level 2

Can package a real tool with CLI parsing, file/codebase processing, build/release setup and automated tests, or build a substantial browser extension that coordinates multiple extension contexts.

### Level 3

Can design extensibility/plugin boundaries, robust configuration, cross-platform behavior, compatibility/versioning and failure-safe upgrades.

### Level 4

Can own a mature developer tool used across varied environments and evolve its public behavior without breaking users.

Current: Level 2 completed. Level 3 developing.

Strongest evidence: `kontxt-cli`, `VoidYoutube`, `project-monitor`, `voidline-zed-theme`.

## Browser extensions

### Level 0

Can modify a simple extension manifest/content script.

### Level 1

Can build a Manifest V3 extension using content scripts, popup UI, storage and background/service-worker behavior.

### Level 2

Can coordinate several extension contexts, handle SPA lifecycle changes, inject dynamic UI, aggregate local data and manage meaningful feature state.

### Level 3

Can handle multi-tab concurrency/state consistency, permissions/security, migration/versioning, automated browser tests and reliable releases.

### Level 4

Can design a complex extension platform with strong compatibility, performance and upgrade guarantees.

Current: Level 2 completed. Main blocker for Level 3 is state/concurrency correctness, explicitly visible in the known multi-tab tracking race condition.

## AI application development

### Level 0

Can integrate an AI SDK/model into an application and understand prompt/input/output flow.

### Level 1

Can ship a complete feature that validates structured model output, handles model failure/timeouts and persists or consumes the result safely.

### Level 2

Can evaluate output quality, add retries/fallbacks, track cost/latency and design prompts/tools around measured failure cases.

### Level 3

Can build multi-step/tool-using AI systems with explicit state, evaluation and operational safeguards.

### Level 4

Can own production AI reliability/evaluation architecture and make model/system tradeoffs from measured data.

Current: Level 0 completed, Level 1 developing.

## System design

### Level 0

Can explain common building blocks such as APIs, databases, caches and queues in isolation.

### Level 1

Can design and implement a small multi-component system, explain data flow/failure points and justify boundaries with concrete requirements.

### Level 2

Can reason about consistency, concurrency, caching, async work, load, retries and failure recovery for a medium system.

### Level 3

Can compare multiple viable designs quantitatively and evolve a system as requirements/load change.

### Level 4

Can own architecture using real production constraints, incidents and operational data.

Current: foundations developing. RealtimeChat, FOODIO and OpsLab provide useful components, but there is not enough repeated end-to-end design evidence to mark Level 1 completed yet.

# Current evidence map

Primary repositories for normal reasoning about ability:

- `FOODIO`: strongest current full-stack/backend/database evidence
- `devscreen`: current full-stack, auth, DB and AI-app evidence
- `kontxt-cli`: strongest CLI/developer-tooling TypeScript evidence
- `RealtimeChat`: real-time backend, Redis pub/sub and monorepo evidence
- `VoidYoutube`: strongest JavaScript/browser-extension evidence
- `opslab-next`: strongest current CI/health/readiness/operations evidence
- `project-monitor`: automation/testing/tooling evidence
- `Python-DSA` and `neetcode-submissions`: DSA evidence
- `luma` and `portfolio`: supporting Next.js/TypeScript evidence

The complete 50-repository classification lives in `developer-skills/REPOSITORY_ANALYSIS.md`. Do not read it during ordinary requests.

# Current learning priorities

When no narrower goal is supplied, prioritize:

1. DSA Level 1 completion, especially two-pointer invariants and prefix sums.
2. Backend Level 3 evidence through idempotency, background jobs and observable failure handling.
3. Database Level 2 through transactions, indexes and query-plan reasoning.
4. DevOps Level 2 through containers, image lifecycle, deployment and rollback.
5. Testing Level 2 through database/API integration tests and deliberate failure tests.

Do not prioritize learning another framework simply because it is new.

# Teaching behavior

For DSA:

- Do not reveal the pattern immediately unless the user asks for the solution.
- Ask the user to define what variables/pointers represent.
- Make the invariant explicit before code when pointers/windows are involved.
- When code is wrong, target the reasoning mistake instead of replacing the whole solution.
- Track recurring mistakes as stronger evidence than one solved problem.

For development:

- Prefer changing/building a real project over isolated tutorials.
- Separate "I can follow this" from "I can build this from an empty project".
- Promote a capability only when evidence crosses the gate.

# Weekly calibration protocol

A refresh has two phases.

## Automatic evidence pass

1. Read this file.
2. Find repositories with meaningful activity since `Last full repository scan` or the previous weekly refresh.
3. Inspect only changed/high-signal files and commits.
4. Check whether new evidence satisfies a specific incomplete gate.
5. Update this file only for meaningful capability changes.
6. Never promote based only on a new dependency, generated code or tutorial copy.

## Questionnaire

Ask 4 to 7 capability questions targeted at the current blockers and new work. Avoid 1-to-10 self-ratings.

Current default questions:

1. Two pointers: "Before coding, can you state what each pointer represents and why moving one pointer cannot discard a valid answer?"
2. DSA independence: "Which problems this week did you solve without being told the pattern?"
3. Backend: "Could you make one write endpoint safe against a client retrying the same request twice? Explain the mechanism."
4. Database: "For one current query, which index would you add, and what query-plan change would you expect?"
5. Testing: "Which failure path did you intentionally test this week, not just the happy path?"
6. DevOps: "Could you build, run and roll back the current app from documented commands without using the hosting dashboard as the main workflow?"

Record answers as evidence for gates. Do not convert them into arbitrary confidence numbers.

# Refresh policy

A normal request should cost one GitHub file read.

Only a refresh/update may fan out across repositories. After the refresh, compile the result back into this file so future conversations return to the one-read path.
