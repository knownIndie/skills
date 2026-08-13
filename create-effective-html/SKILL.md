---
name: create-effective-html
description: Create and verify self-contained HTML artifacts that communicate better through interaction, spatial layout, comparison, diagrams, or visual hierarchy than through linear prose. Use when Codex needs to turn source material into an explorable plan, annotated code review, module map, design-system sheet, component gallery, prototype, SVG diagram, slide deck, research explainer, status or incident report, or small custom editor with an export action. Also use when the user explicitly asks for a standalone HTML deliverable, interactive document, visual explainer, or browser-openable artifact.
---

# Create Effective HTML

Create one focused `.html` file that opens directly in a modern browser. Treat HTML as a communication medium, not decoration.

## Decide whether HTML earns its cost

Use HTML when at least one of these materially improves comprehension:

- Side-by-side comparison
- Spatial relationships, flows, timelines, or call graphs
- Direct manipulation, animation, filtering, tabs, or progressive disclosure
- Live rendering of design tokens or component states
- A small task-specific editor that returns structured output

Prefer Markdown or prose when the result is linear, short, or mainly archival. Do not manufacture a dashboard for a simple answer.

## Build the artifact

1. Inspect the source material first. Preserve facts, code, terminology, file paths, uncertainty, and attribution. Never invent metrics or repository behavior to make the page look complete.
2. Choose one job and one dominant visual structure. Examples include a comparison grid, annotated diff, node-link map, timeline, contact sheet, slide sequence, or editor workspace.
3. Create a single HTML file with inline CSS and JavaScript. Avoid package managers, build steps, frameworks, CDNs, remote fonts, and remote assets unless the user explicitly requests them.
4. Use semantic HTML, clear headings, keyboard-accessible controls, visible focus states, sufficient contrast, and responsive layouts. Respect `prefers-reduced-motion`.
5. Make interaction purposeful. Controls must expose information, test a behavior, or help the user make a decision. Do not add inert filters, fake charts, decorative toggles, or meaningless animation.
6. For custom editors, include an explicit export or copy action that converts the edited state into a useful format such as Markdown, JSON, a patch, or a prompt. Persist locally only when useful, and disclose it in the interface.
7. Escape untrusted source content before inserting it into HTML. Do not embed credentials, private tokens, analytics, network calls, or executable user-provided markup.
8. Add a concise source or methodology note when the artifact depends on external material or inferred structure.

## Keep the design disciplined

Prefer a restrained palette, a readable system font stack, a consistent spacing scale, and a limited set of reusable CSS classes. Match an existing product's visual language when source styles are available. Otherwise choose a neutral visual system suited to the material.

Use inline SVG for diagrams and simple charts. Label shapes and paths in the DOM so the artifact remains inspectable and accessible. Use tables for exact comparisons. Use CSS Grid or Flexbox for layout. Keep print output legible when the artifact is report-like.

Avoid excessive gradients, glass effects, huge title treatments, arbitrary card grids, and dense dashboard chrome. The artifact is successful when the user understands or decides something faster, not when it looks expensive.

## Verify before delivery

Open the file in a browser and inspect the rendered result. When browser-control tooling is available, use it to test the artifact at desktop and narrow viewport widths.

Verify:

- The file loads without console errors or missing resources.
- Core content is visible without JavaScript.
- Every control works with pointer and keyboard input.
- Navigation, tabs, dialogs, and copy or export actions behave correctly.
- Long text, code, and labels do not overflow.
- The page remains usable at roughly 375 px width.
- Reduced-motion behavior is safe.
- Exported content is complete and machine-usable.

Fix failures before handing off. Deliver the absolute path as a clickable link and state the artifact's purpose in one sentence. Do not dump the full HTML into chat unless the user asks for it.

## Common artifact patterns

- Exploration: parallel alternatives with aligned criteria and a direct recommendation.
- Review: annotated diff or file tour with severity, rationale, and jump links.
- Understanding: module map with entry points, boundaries, and the hot path.
- Planning: milestones, dependencies, data flow, risks, and implementation checkpoints.
- Research: layered summary, collapsible detail, linked glossary, and runnable examples where possible.
- Reports: scannable status or incident timeline with evidence and explicit follow-ups.
- Editors: direct manipulation plus deterministic export back to text or structured data.
