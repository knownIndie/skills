# Repository evidence audit

Last full scan: 2026-08-24

Purpose: record what each tracked repository contributes to the developer-skill profile. This is evidence, not the normal read path. Normal conversations should read only `developer-skills/SKILL.md`.

## Evidence rules

- A dependency or framework in a manifest proves exposure, not mastery.
- A working feature, tests, deployment setup, or non-trivial implementation is stronger evidence.
- Tutorial clones, archived learning projects, config repositories, generated files, forks, and registries get reduced weight.
- Future plans do not count as completed work.
- Private repositories that cannot be safely or reliably inspected stay unverified instead of being guessed.
- DSA submissions prove attempted/implemented patterns. Independent pattern recognition must be verified separately.
- Repositories outside the tracked set must not contribute evidence or capability claims.

## High-signal repositories

| Repository | Weight | What it supports | Limits |
| --- | --- | --- | --- |
| `FOODIO` | high | Next.js, React, TypeScript, PostgreSQL, Drizzle, auth, Redis, rate limiting, validation, local service tooling, migrations | Does not by itself prove production observability, jobs, idempotency, query-plan work, or large-scale ownership |
| `devscreen` | high | Next.js, TypeScript, Better Auth, Neon/Postgres, Drizzle/Kysely, AI SDK exposure, forms, product architecture | Earlier project audit showed substantial product work still incomplete; dependencies do not prove completed AI flows |
| `kontxt-cli` | high | Published TypeScript CLI, codebase traversal/filtering, packaging, token tooling, build pipeline, Bun tests | Cross-platform hardening and extensibility architecture are not yet strongly verified |
| `VoidYoutube` | high | Manifest V3 browser extension, service worker/background logic, content scripts, SPA lifecycle handling, DOM injection, Chrome storage aggregation, analytics UI | Known multi-tab race condition shows concurrency/state coordination is still an active weakness |
| `opslab-next` | high | Typed environment validation, liveness/readiness checks, PostgreSQL/Drizzle, tests, CI quality gates, operational failure exercises | No verified container/image lifecycle yet |
| `project-monitor` | high | Automation/tooling repo with GitHub workflow structure, tests, scripts, project data and deployment config | Small system; does not prove large service architecture |
| `Python-DSA` | high for DSA | Arrays, hashing and Python DSA practice | Some older solutions are basic; repository presence is not independent interview fluency |
| `neetcode-submissions` | high for DSA | Hashing, arrays, binary search, two pointers, sliding window, stack, linked-list and other pattern exposure | Submission existence does not prove unseen-problem recognition |

## Strong supporting repositories

| Repository | Weight | Evidence |
| --- | --- | --- |
| `luma` | medium-high | Next.js/TypeScript application, Prisma, workspace structure, environment configuration |
| `portfolio` | medium-high | Current Next.js/TypeScript portfolio with docs/scripts/configuration |
| `backend-todo` | medium | Backend application structure with Prisma and environment setup |
| `Backend101` | medium | Express-era backend structure with routes, controllers, middleware, models and database work |
| `Backend-Basics` | medium | Express 5, JWT, bcrypt and SQLite-oriented backend practice |
| `basic-course-selling-website` | medium | Early Node/Express-style routes, middleware and database work; historical auth/backend practice |
| `Cloudline` | medium | Vite + TypeScript frontend and component tooling |
| `React-Projects` | medium | React/Vite practice across a dedicated project repo |
| `Recipes-Finder` | medium-low | React/Vite API-consumption project |
| `weather-app` | medium-low | React/Vite API-consumption project |
| `moviefetcher` | medium-low | React/Vite data-fetching project |
| `react-todo` | medium-low | React state/UI fundamentals |
| `voidline-zed-theme` | medium-low | Packaged Zed theme/extension metadata and distribution structure |
| `placement-prep-2026` | medium for DSA history | Explicit placement/DSA notes, including Two Sum and two-pointer/hash-map study |
| `placement-26` | medium-low for DSA history | Placement questions and practice archive |

## Historical or low-signal repositories

| Repository | Classification | Reason |
| --- | --- | --- |
| `RMP-ColorChanger` | historical React practice | Small Vite/React learning project; committed `node_modules` reduces repository hygiene signal |
| `RMP-Currency` | historical React practice | Small Vite/React learning project |
| `RMP-Password-Generator` | historical React practice | Small Vite/React learning project |
| `w3school-clone` | historical HTML/CSS | Static clone; useful only for early HTML/CSS history |
| `YT_coffe-clone` | historical HTML/CSS | Static clone; useful only for early HTML/CSS history |
| `WEB-DEV-PORTFOLIO` | historical portfolio | README-only current root, low implementation signal |
| `WeSplit` | historical Swift/SwiftUI exposure | Archived Xcode/Swift learning project with test targets; not evidence of current Swift proficiency |
| `Mac-OS-Setup` | config/docs | README-only setup notes |
| `vscode-config` | config/docs | Editor configuration documentation |
| `zed` | config | Zed settings, keymaps, tasks and prompts |
| `zedConfig` | config | Zed settings, prompts, themes and embeddings config |
| `knownIndie` | profile | GitHub profile README only |
| `skills` | AI workflow/tooling support | Reusable skill definitions including research, HTML docs and writing rules; supports AI-workflow customization, not software proficiency by itself |
| `extensions` | registry/fork-like low-authorship signal | Large Zed extensions registry with many submodules. Repository size must not be treated as authored engineering output |
| `failedAttemptAtChatApp` | abandoned experiment | Minimal package manifest, intentionally failed/unfinished project |
| `Learning-Notes` | archived notes | Private archived learning notes, no reliable code signal from current scan |
| `obsidan-docs` | notes | Private documentation workspace, not counted as code evidence |
| `obsidian` | empty/notes | Empty private repository by current metadata |
| `aryan` | execution/docs | Job-search and execution workspace, not code evidence |
| `personal` | private low-signal | Tiny private repository, not used for skill inference |
| `private-env-for-projects` | excluded sensitive config | Intentionally not inspected for skill analysis because it may contain environment-related material |
| `aryan-0` | unverified private | Large private repository but no safe root manifest/README was resolved in this scan; do not infer skills from size |

## Additional current application repositories

| Repository | Classification | Notes |
| --- | --- | --- |
| `architectx` | supporting Next.js | Next.js/TypeScript structure is present, but README is still default scaffold text, so evidence weight is limited |
| `learn-from-this` | supporting Next.js | Next.js/TypeScript app structure; useful as supporting frontend evidence |
| `Devops-Learning` | learning roadmap + app | Valuable for intent and verified baselines. Planned Docker/Kubernetes/Cloud work does not count until implemented |

## Skill conclusions from the full scan

### Strongest demonstrated areas

- TypeScript application development
- React and Next.js product development
- Node.js backend development
- API and authentication work
- PostgreSQL integration through Drizzle/Prisma/Neon
- Redis exposure through rate limiting
- Developer tooling and CLI work
- Browser extension development
- Basic CI, health checks and environment validation

### Developing areas with real evidence

- Operational engineering through CI, liveness/readiness and failure exercises
- Testing through CLI tests, OpsLab quality gates and project-monitor tests
- AI application development through AI SDK usage in DevScreen, without enough completed end-to-end evidence for a higher gate
- System design reasoning through application architecture, Redis and service boundaries, but without enough production-scale evidence for a completed system-design gate

### Do not claim yet

- Advanced SQL/query optimization
- Reliable transaction design across non-trivial workflows
- Production observability/tracing ownership
- Queue/background-job architecture
- Idempotent distributed workflows
- Kubernetes or cloud infrastructure proficiency
- Strong Go or Rust ability
- Current Swift proficiency
- Advanced TypeScript type-level programming
- Consistent unseen Medium DSA performance

## Repository hygiene observations

Older repositories sometimes commit `.DS_Store` and, in a few cases, `node_modules`. Current repositories are materially cleaner and use lint/typecheck/build/test scripts more consistently. This is evidence of improved engineering hygiene over time, but it is not a separate capability promotion by itself.

## Scan coverage

The tracked repository set visible to the connected GitHub account was classified in this audit. Public repositories were inspected at the root and high-signal repositories received deeper reads. Private repositories were inspected only through safe documentation/manifests where available. Environment/secret-oriented repositories were not opened for content analysis.