---
name: developer-skills
description: Read and maintain Aryan's current developer and DSA capability map. Use when asked about developer skills, DSA ability, job fit, what to learn next, or teaching based on current ability.
---

# Developer skills

This file is the canonical snapshot of Aryan's demonstrated developer ability.

Normal use must read only this file. Do not rescan source repositories unless the user explicitly asks for a refresh, verification, or weekly update.

Canonical path: `knownIndie/skills/developer-skills/SKILL.md`

Last refreshed: 2026-08-24

## Rules

1. A level is a capability gate, not a confidence score.
2. A level is complete only when every required ability in that level is demonstrated.
3. Dependency presence is evidence of exposure, not proof of ability.
4. Keep three states when useful: `completed`, `developing`, `not demonstrated`.
5. Higher-level exposure does not skip an incomplete lower gate.
6. Prefer code evidence plus a short self-check over self-rating numbers.
7. During normal teaching, use the weakest relevant prerequisite as the starting point.
8. During a weekly refresh, inspect only repositories with meaningful new activity plus repositories needed to verify a promotion.
9. Keep this file compact. Git history is the long-term history.

## Current snapshot

| Track | Current gate | Next gate | Main blocker |
| --- | --- | --- | --- |
| DSA | Level 0 completed | Level 1 | Two-pointer invariants and independent pattern recognition |
| TypeScript | Level 3 completed | Level 4 | Advanced type design and larger architectural ownership not yet verified |
| React / Next.js | Level 2 completed | Level 3 | Testing, accessibility, performance and larger frontend architecture |
| Backend | Level 2 completed | Level 3 | Background jobs, idempotency, observability and production failure handling |
| Databases | Level 1 completed | Level 2 | Transactions, indexes, query-plan reasoning and constraints need stronger proof |
| DevOps | Level 1 completed | Level 2 | Container image lifecycle, registry, deployment and rollback |
| Testing | Level 1 completed | Level 2 | Broader integration / E2E strategy and deliberate failure testing |
| Developer tooling | Level 2 completed | Level 3 | Cross-platform hardening, plugin/extensibility design and larger tool architecture |
| Python | Level 1 completed | Level 2 | More idiomatic problem solving, modules and tests |
| AI application development | Level 0 completed | Level 1 | End-to-end AI feature with validated structured output is not yet demonstrated |
| Go | Not demonstrated | Level 0 | No implementation evidence yet |
| Rust | Not demonstrated | Level 0 | No implementation evidence yet |
| System design | Developing foundations | Level 1 | Needs implemented evidence for scaling, failure and architecture tradeoffs |

## DSA

Current status: Level 0 completed, Level 1 developing.

### Level 0: foundations

Complete when Aryan can independently:

- traverse arrays and strings
- use indices without routine off-by-one errors
- use sets and hash maps for membership and frequency counting
- explain common `O(1)`, `O(n)`, `O(n log n)` and `O(n^2)` behavior
- solve straightforward Easy array/string problems without needing the pattern named

Status: completed.

### Level 1: linear patterns

Complete only when Aryan can independently:

- use hash maps and sets for lookup, frequency and deduplication
- use two pointers and state what each pointer means before coding
- state and maintain the two-pointer invariant while pointers move
- use prefix sums for range / cumulative reasoning
- use sorting as part of a solution when it changes the problem structure
- solve unseen Easy problems from these patterns without being told which pattern applies

Status: developing.

Current evidence:

- Hashing and array work is demonstrated through anagram, duplicate, group-anagram, product-except-self and longest-consecutive style submissions.
- Two-pointer exposure exists through palindrome, max-water-container, linked-list-cycle and recent segregation practice.
- The current two-pointer weakness is not the basic idea. It is maintaining the invariant and moving the correct pointer in every state.

Promotion blocker:

- Explain `l` and `r` as roles, not just positions.
- Explain why each pointer move is safe.
- Solve at least 5 unseen two-pointer problems without being told to use two pointers.
- Show correct termination and edge-case handling consistently.

### Level 2: core interview structures

Complete only when Aryan can independently:

- use sliding window for fixed and variable windows
- implement binary search and binary search on an answer space
- use stack and queue patterns
- manipulate linked lists with pointer reasoning
- use recursion for small structured problems
- traverse matrices cleanly
- recognize these patterns in unseen Easy / easier Medium problems

Status: exposed, not gate-complete.

Existing exposure includes binary search, eating-bananas style answer search, longest-substring sliding window, stock scanning, reverse-polish stack work and linked-list problems.

### Level 3: trees and structured search

Complete only when Aryan can independently:

- write DFS and BFS over trees
- reason about BST invariants
- use heaps / priority queues
- solve interval problems
- use backtracking with explicit choice, state and undo steps
- use monotonic stack when the next/previous greater-smaller structure is present
- solve normal Medium problems without a pattern hint

Status: not demonstrated.

### Level 4: graphs and optimization

Complete only when Aryan can independently:

- represent and traverse graphs with DFS/BFS
- use topological sort
- use union-find
- use shortest-path basics appropriately
- reason about greedy correctness
- derive state and transition for common 1D and 2D dynamic programming problems
- use tries when prefix structure matters

Status: not demonstrated.

### Level 5: interview ready

Complete only when Aryan can consistently:

- solve unfamiliar Medium problems under a realistic time limit
- identify the pattern without being prompted
- combine multiple patterns in one solution
- explain complexity before or while implementing
- derive edge cases rather than patching them after failures
- debug a flawed approach and explain why it fails
- produce readable code under pressure
- occasionally solve reasonable Hard problems without solution lookup

Status: not demonstrated.

## TypeScript

### Level 0: language basics

Complete when variables, functions, objects, arrays, unions, interfaces/types and basic narrowing can be used without hand-holding.

Status: completed.

### Level 1: typed application code

Complete when Aryan can type component props, API inputs/outputs, database-facing data and common async code without falling back to `any` as the normal solution.

Status: completed.

### Level 2: multi-module applications

Complete when Aryan can organize a TypeScript application across modules, define domain types, integrate libraries, validate external data and debug compiler errors across a real project.

Status: completed.

### Level 3: reusable tooling and package ownership

Complete when Aryan can build and publish a TypeScript package or CLI with a public entry point, build process, command handling, file-system work and automated tests.

Status: completed. Kontxt CLI is the primary proof.

### Level 4: advanced type and architecture work

Complete when Aryan can deliberately design generic APIs, advanced narrowing, reusable type relationships and library boundaries where the type system prevents meaningful classes of invalid states.

Status: developing, not verified as complete.

## React / Next.js

### Level 0: component basics

Can build components, pass props, render collections and handle events.

Status: completed.

### Level 1: interactive application UI

Can use state, forms, reusable UI components, client-side interactions and asynchronous data without copying a tutorial structure.

Status: completed.

### Level 2: full-stack Next.js application

Can build a routed Next.js application that integrates server/client code, authentication, forms, database-backed features and third-party services.

Status: completed. FOODIO and DevScreen are the main evidence.

### Level 3: production frontend engineering

Requires demonstrated automated frontend testing, accessibility work, performance profiling, error/loading state design, complex state boundaries and maintainable larger-scale component architecture.

Status: developing.

### Level 4: frontend architecture ownership

Requires ability to define conventions, performance budgets, design-system boundaries and migration strategy for a substantial frontend used by other developers.

Status: not demonstrated.

## Backend

### Level 0: HTTP foundations

Can explain request/response flow, JSON, methods, status codes and basic API handlers.

Status: completed.

### Level 1: persistent CRUD service

Complete when Aryan can independently build API endpoints with validation, useful errors and database persistence.

Status: completed.

### Level 2: application backend

Complete when Aryan can implement authentication, authorization boundaries where required, relational persistence, migrations, validation, external integrations and abuse controls such as rate limiting.

Status: completed. FOODIO provides strong evidence through PostgreSQL/Drizzle, auth code, Redis-backed rate-limit work and local service tooling. DevScreen adds Better Auth and Neon/Drizzle application experience.

### Level 3: production backend reliability

Complete only when Aryan has implemented and can explain:

- caching with explicit invalidation reasoning
- background jobs / queues where asynchronous work is justified
- idempotency for retryable writes
- structured logs and request correlation
- health/readiness behavior
- meaningful integration tests
- failure handling and operational debugging
- deployment and rollback behavior

Status: developing. Health checks, CI and Redis-related work exist, but the full gate is not complete.

### Level 4: service architecture

Requires demonstrated decisions around service boundaries, consistency, concurrency, scaling, replication, failure isolation and asynchronous workflows.

Status: not demonstrated.

## Databases

### Level 0: relational basics

Can create tables, insert/update/delete/select rows and explain primary/foreign keys.

Status: completed.

### Level 1: application database work

Can model normal relational application data, use an ORM/query builder, create migrations and write common filtered/joined queries.

Status: completed, with PostgreSQL, Neon and Drizzle used across multiple projects.

### Level 2: correctness and performance

Complete only when Aryan can independently reason about transactions, constraints, indexes, query plans, N+1 behavior, pagination and safe schema changes.

Status: developing.

### Level 3: operational database ownership

Requires isolation/locking reasoning, connection-pool behavior, backup/restore practice, performance diagnosis and replication/high-availability fundamentals.

Status: not demonstrated.

## DevOps

### Level 0: delivery basics

Can use Git branches, environment variables, hosted deployments and basic build commands.

Status: completed.

### Level 1: application operational hygiene

Complete when Aryan has implemented:

- CI quality gates
- typed / explicit environment validation
- liveness and database readiness checks
- repeatable build/test commands
- clear failure behavior for missing configuration or unavailable dependencies

Status: completed. OpsLab Next is the primary evidence.

### Level 2: containers and release artifacts

Complete only when Aryan can build a secure multi-stage container image, run locally with Compose when appropriate, use health checks, publish immutable image tags to a registry, diagnose container failures and perform a documented deployment rollback.

Status: developing.

### Level 3: cloud and observability

Requires demonstrated infrastructure-as-code, least-privilege cloud identity, metrics, structured logs, traces, dashboards and alert-driven diagnosis.

Status: not demonstrated.

### Level 4: orchestration and GitOps

Requires demonstrated Kubernetes debugging, resource/probe configuration, GitOps reconciliation, controlled promotion and incident recovery.

Status: not demonstrated.

## Testing

### Level 0: manual verification

Can verify expected behavior manually and reproduce a bug.

Status: completed.

### Level 1: automated project checks

Complete when Aryan has written automated tests and uses them with lint/type/build gates in real projects.

Status: completed. Kontxt CLI has Bun tests and OpsLab exposes a quality-gate/CI workflow.

### Level 2: test boundaries and failure coverage

Requires deliberate unit vs integration vs E2E choices, database/API integration tests, external-service mocking where appropriate and tests for important failure paths.

Status: developing.

### Level 3: test strategy

Requires ability to choose risk-based coverage, detect flaky tests, use property/load testing where justified and design testability into system boundaries.

Status: not demonstrated.

## Developer tooling

### Level 0: scripts

Can write scripts to automate repetitive developer work.

Status: completed.

### Level 1: usable CLI

Can parse command arguments, read/write files, handle configuration and produce useful terminal output.

Status: completed.

### Level 2: distributable developer tool

Can package, test, build and publish a CLI for other developers, with ignore/filter behavior and a stable command entry point.

Status: completed. Kontxt CLI is the proof.

### Level 3: robust tool architecture

Requires cross-platform hardening, backwards-compatible configuration, plugin/extensibility decisions, migration/version strategy and stronger failure-mode testing.

Status: developing.

## Python

### Level 0: language basics

Can use functions, loops, conditionals, lists, dictionaries, sets and classes when needed.

Status: completed.

### Level 1: DSA implementation

Can translate basic algorithm reasoning into Python and use core containers for problem solving.

Status: completed.

### Level 2: idiomatic reusable Python

Requires stronger use of Python idioms, modules, typing, tests and reusable abstractions beyond isolated problem solutions.

Status: developing.

## AI application development

### Level 0: integration awareness

Understands model/API integration at an application level and can wire AI-related libraries into a project.

Status: completed.

### Level 1: reliable AI feature

Complete when Aryan implements an end-to-end AI feature with structured output, validation, explicit error handling and persistence/use of the validated result.

Status: developing. DevScreen has AI SDK dependencies and a planned evaluation flow, but the existing project evidence does not prove the full gate yet.

### Level 2: production AI behavior

Requires evals, retries/timeouts, cost/latency handling, observability, prompt/version management and fallback behavior.

Status: not demonstrated.

## Go and Rust

Current state: interest and learning intent exist, but implementation ability is not demonstrated by the tracked repositories. Do not infer proficiency from translated examples or discussion alone.

### Level 0 for either language

Complete when Aryan can independently write small programs using variables, control flow, functions, core collections, error handling and the language's normal project/tooling workflow.

Status: not demonstrated.

## System design

Current state: conceptual interest and architecture discussion exist, but production implementation evidence is limited.

### Level 1: application architecture

Complete when Aryan can take a normal product requirement and justify data model, API boundaries, sync vs async work, caching choices, failure handling and deployment shape, then implement enough of the design to validate the decisions.

Status: developing.

### Level 2: scale and reliability

Requires reasoning about load, bottlenecks, replication, consistency, queues, retries, idempotency and failure isolation with concrete tradeoffs.

Status: not demonstrated.

## Evidence anchors

Use these repositories during refreshes, not during ordinary reads:

- `knownIndie/FOODIO`: Next.js/TypeScript application, PostgreSQL/Drizzle, auth, Redis/rate limiting, local service scripts.
- `knownIndie/devscreen`: Next.js/TypeScript, Better Auth, Neon/Drizzle, AI SDK integration work.
- `knownIndie/kontxt-cli`: published TypeScript developer CLI with build and automated tests.
- `knownIndie/opslab-next`: CI, environment validation, liveness/readiness, tests, PostgreSQL/Drizzle operational-learning project.
- `knownIndie/Python-DSA`: Python DSA practice.
- `knownIndie/neetcode-submissions`: problem submissions covering hashing, binary search, sliding window, two pointers, stacks and linked lists.
- `knownIndie/Devops-Learning`: DevOps learning plan and progress context.

## Teaching behavior

When this skill is used for teaching:

- Start from the relevant current gate and blocker.
- Do not reteach demonstrated prerequisites unless the user is failing them in the current problem.
- For DSA, do not reveal the pattern immediately when the goal is pattern recognition.
- Ask for the invariant before helping with pointer movement.
- Prefer one concrete correction over a long theory dump.
- Distinguish "I have seen this" from "I can solve this independently".
- When a user asks what to learn next, prioritize the next incomplete gate rather than a random new topic.

## Weekly refresh protocol

A weekly refresh may do the expensive work. Ordinary reads must not.

1. Read this file first.
2. Inspect meaningful GitHub activity since `Last refreshed` in the evidence-anchor repositories and any newly relevant repository.
3. Look for implemented behavior, tests and architecture changes. Do not promote a skill because a dependency was added.
4. Update objective evidence and candidate gate progress.
5. Ask at most 6 short capability questions, focused on current blockers and possible promotions.
6. Questions must test a concrete ability, never ask for a 1-10 confidence rating.
7. Promote a gate only after code evidence and/or a convincing self-check demonstrates every required ability.
8. Update `Last refreshed` and this current snapshot. Keep old history in Git commits, not appended prose.

### Preferred questionnaire format

Use questions like:

- "Before coding a two-pointer solution, can you state what `l` and `r` represent and what must remain true after each move?"
- "Did you solve an unseen two-pointer problem this week without being told the pattern? Which one?"
- "Can you explain when a database transaction is required in one of your current apps?"
- "If a readiness endpoint returns 503 while liveness stays 200, can you explain what that tells you?"
- "Could you rebuild the relevant feature from an empty file without copying the existing implementation?"

Avoid questions like:

- "How good are you at React from 1 to 10?"
- "How confident are you in DSA?"

## Update behavior after questionnaire answers

When Aryan answers a weekly questionnaire:

1. Read this file once.
2. Interpret the answers against the exact gate requirements.
3. Update this file if the answers change demonstrated/developing status or clarify a blocker.
4. Do not rescan all repositories unless the answer requires verification.
5. Report only meaningful changes and the next blocker.
