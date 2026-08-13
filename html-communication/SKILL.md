---
name: html-communication
description: Create and verify a standalone, self-contained HTML communication document for a human to read outside the terminal and outside the user's product codebase. Use when the user asks for an HTML plan, specification, write-up, report, findings document, summary, comparison, review, explainer, decision document, status document, implementation handoff, or collection of static UI mocks, especially when they expect a saved HTML file and a link to open it. Do not use for implementing websites, product interfaces, application pages, repository-owned HTML, email HTML, HTML snippets, or components intended to ship with a codebase.
---

# HTML Communication

Create one focused HTML document that makes work easy to understand. Treat HTML as a communication format, not a product or landing page.

## Workflow

1. Inspect the source material before writing claims.
2. Identify the audience, document purpose, main conclusion, evidence, unresolved questions, and required action.
3. Choose the smallest structure that communicates the material completely.
4. Create one self-contained `.html` file in the environment's user-facing output directory. If no output directory is designated, use `outputs/` in the current workspace.
5. Apply the content, visual, interaction, safety, and UI mock rules below.
6. Run `scripts/validate_html.py <file>`.
7. Open or render the document and inspect it at desktop and roughly 375 px width when browser or rendering tools permit local-file inspection.
8. Fix inaccurate content, weak hierarchy, overflow, contrast failures, broken navigation, and unnecessary elements.
9. Return a clickable link to the file and summarize its purpose in one or two sentences. Do not paste the complete HTML into chat unless requested.

## Content rules

- Lead with the conclusion, decision, status, or purpose.
- Include enough facts, reasoning, constraints, and verification detail for the reader to evaluate the work.
- Keep the page dense and scannable without turning it into a wall of text.
- Add a section only when it changes understanding, supports a claim, exposes a decision, or gives the reader something actionable.
- Prefer clear headings, short paragraphs, exact tables, checklists, code excerpts, diagrams, and restrained callouts when the content needs them.
- Do not add sections, cards, controls, metrics, diagrams, navigation, or interaction merely to make the document look complete or impressive.
- Do not invent facts, metrics, implementation behavior, quotations, sources, or product states.
- Distinguish verified facts, inferences, proposals, decisions, unresolved questions, and deferred work.
- Do not describe planned or documented behavior as implemented behavior.
- State important evidence limitations directly.
- Do not use marketing language or em dashes.

## Visual rules

- Use a restrained Vercel-like visual discipline without copying Vercel branding or product UI.
- Default to `#000` for the page background and white or near-white for primary text.
- Use dark gray for secondary surfaces, borders, and muted text.
- Use restrained semantic colors only when they communicate status, risk, category, or data meaning.
- Use a readable system sans-serif stack and a system monospace stack when needed.
- Keep CSS simple. Use a small set of layout, spacing, typography, border, and status styles.
- Use fine borders, compact type, strong spacing, and clear hierarchy.
- Do not add a hero section, oversized title treatment, gradients, glass effects, glowing effects, decorative navigation, arbitrary card grids, fake dashboards, fake metrics, or ornamental chrome.
- Do not add animations unless motion explains a sequence or state change that static presentation cannot explain as clearly.
- Maintain sufficient contrast and visible keyboard focus states.

## Responsive rules

- Include `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- Use a fluid layout that works from narrow phone screens through desktop widths.
- Allow a readable `max-width` for the main content column. Do not use a fixed-width page.
- Do not require page-level horizontal scrolling.
- Put tables, code blocks, diagrams, and mock frames in their own overflow containers when they cannot collapse safely.
- Keep touch targets usable and text readable at roughly 375 px width.
- Respect `prefers-reduced-motion` when motion exists.

## JavaScript rules

- Use JavaScript when it materially improves the document.
- Appropriate uses include filtering a large comparison, switching between meaningful alternatives, navigating long content, revealing genuinely secondary evidence, comparing UI states, copying useful content, exporting structured content, or running a small calculation.
- Keep all essential conclusions, evidence, decisions, and instructions present in the HTML before JavaScript runs.
- Do not add JavaScript for decorative animation, fake controls, theme switching when one theme is sufficient, unnecessary collapsible sections, cosmetic hover behavior, simulated application behavior, or state management the document does not need.
- Use only an inline classic script. Do not use external scripts or module scripts.
- Do not use storage, cookies, network requests, workers, frames, forms, popups, automatic navigation, or background activity.

## UI mocks

- Use UI mocks only as explanatory material inside the communication document.
- Build mocks with semantic HTML and simple inline CSS. Use inline SVG only for useful icons, diagrams, or simple illustrations.
- Label each mock as current, proposed, exploratory, illustrative, or final.
- Do not present invented UI as implemented product state.
- Show empty, loading, error, success, disabled, mobile, or desktop states only when those states affect the decision.
- Use realistic, internally consistent labels and content. Avoid meaningless placeholder copy when source-grounded copy is available.
- Place assumptions, annotations, decisions, and unresolved questions near the relevant mock.
- Make mock frames responsive even when they represent a desktop viewport.
- Do not turn the document into a working application.
- Do not add submission, authentication, persistence, network activity, or simulated backend behavior.

## Portability and safety

- Produce exactly one self-contained HTML file capped at 512 KB.
- Use semantic HTML, inline CSS, inline SVG, and HTTPS or data-URL images.
- Do not include external or module scripts, linked stylesheets, CSS `@import`, remote fonts, analytics, telemetry, or tracking pixels.
- Do not include inline event-handler attributes such as `onclick`, `onload`, or `onerror`.
- Do not include `javascript:` URLs.
- Do not include forms, submission controls, frames, iframes, `srcdoc`, embeds, objects, applets, base elements, or meta refresh.
- Do not use storage, cookies, workers, service workers, popups, downloads, clipboard reading, automatic navigation, or browser permission APIs.
- Do not initiate network requests from JavaScript.
- Do not include secrets, credentials, tokens, signed URLs, private network addresses, sensitive internal endpoints, or local filesystem paths.
- Include authenticated workspace links only when the user supplied them or the task explicitly requires them.
- In a script-free file, give external HTTPS links `target="_blank"` and `rel="noopener noreferrer"`.
- If the file contains any script, omit `target="_blank"` from every link. Never simulate new-window behavior with JavaScript.

## Verification

Run:

```bash
python3 scripts/validate_html.py <path-to-html>
```

Then verify visually when local rendering is permitted:

- The main conclusion is obvious.
- The document contains no filler sections or unsupported claims.
- The file opens without missing resources or console errors.
- Long text, tables, code, diagrams, and mock labels do not overflow.
- The page remains usable near 375 px width.
- Every control has a clear communication purpose and works with pointer and keyboard input.
- Essential content remains available without JavaScript.
- Status labels do not blur verified, inferred, proposed, and deferred information.

If local-file browser access is blocked, report that limitation honestly. Do not claim a visual browser pass from structural validation alone.
