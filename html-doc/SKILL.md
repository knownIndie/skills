---
name: html-doc
description: Create and verify a standalone, self-contained HTML communication document for a human to read outside the terminal and outside the user's product codebase. Use when the user asks for an HTML plan, specification, write-up, report, findings document, summary, comparison, review, explainer, decision document, status document, implementation handoff, or collection of static UI mocks, especially when they expect a saved HTML file and a link to open it. Do not use for implementing websites, product interfaces, application pages, repository-owned HTML, email HTML, HTML snippets, or components intended to ship with a codebase.
---

# HTML Doc

Create one focused HTML document that makes work easy to understand and looks deliberately designed, not like unstyled markdown. Treat HTML as a communication format, not a product or landing page.

## Workflow

1. Inspect the source material before writing claims.
2. Identify the audience, reading level, document purpose, main conclusion, evidence, unresolved questions, and required action.
3. Choose the smallest structure that communicates the material completely (see "Structure by document type" below).
4. Create one self-contained `.html` file in the environment's user-facing output directory. If no output directory is designated, use `outputs/` in the current workspace. Name the file descriptively and, when the content is time-bound, include a date: `q3-churn-findings.html`, `auth-redesign-plan-2026-09-23.html`. Avoid generic names like `document.html` or `report.html`.
5. Apply the content, visual, interaction, safety, and UI mock rules below.
6. Run the checklist in "Verification."
7. Return a clickable link to the file and summarize its purpose in one or two sentences. Do not paste the complete HTML into chat unless requested.

### Structure by document type

Use these as starting points, not fixed templates — add or drop sections based on what the material actually needs.

- **Status update:** conclusion/status banner → what changed → evidence → open questions → next action.
- **Comparison:** conclusion (the recommendation, if there is one) → comparison table → tradeoffs and caveats → decision or next step.
- **Findings/report:** conclusion → key findings (ordered by importance, not chronology) → supporting evidence → limitations → recommendations.
- **Spec/handoff:** summary of what's being built and why → scope and non-goals → details (API, data, UI) → open questions → verification/acceptance criteria.
- **UI mock collection:** purpose and what's being evaluated → mocks in decision order, each labeled and annotated → open questions.

Most documents should read in full within 2–4 screen-heights of scrolling. If the material genuinely needs more, add in-page navigation (see JavaScript rules) rather than letting the page sprawl unstructured.

## Content rules

- Lead with the conclusion, decision, status, or purpose.
- Include enough facts, reasoning, constraints, and verification detail for the reader to evaluate the work — matched to the audience and reading level identified in step 2.
- Keep the page dense and scannable without turning it into a wall of text.
- Add a section only when it changes understanding, supports a claim, exposes a decision, or gives the reader something actionable.
- Prefer clear headings, short paragraphs, exact tables, checklists, code excerpts, diagrams, and restrained callouts when the content needs them.
- Do not add sections, cards, controls, metrics, diagrams, navigation, or interaction merely to make the document look complete or impressive.
- Do not invent facts, metrics, implementation behavior, quotations, sources, or product states.
- Distinguish verified facts, inferences, proposals, decisions, unresolved questions, and deferred work — visually as well as textually (see status badge spec below). Don't let formatting blur these categories together.
- Do not describe planned or documented behavior as implemented behavior.
- State important evidence limitations directly.
- Do not use marketing language ("cutting-edge," "seamless," "powerful") or em dashes. Both read as promotional or AI-generated filler rather than direct communication, which undercuts a document whose job is to be trusted.

## Visual system

"Restrained Vercel-like visual discipline" means a fixed, consistent system applied everywhere — not a fresh design decision on every element. Use these as concrete defaults; adjust the accent hue to fit context (e.g., a red-flagged risk doc can lean warmer) but keep the structure.

### Color

```css
:root {
  --bg: #000000;
  --surface: #0a0a0a;       /* cards, code blocks, table headers */
  --border: #262626;
  --text-primary: #f5f5f5;
  --text-secondary: #a3a3a3; /* captions, metadata, muted labels */
  --accent: #3b82f6;         /* links, focus rings, the one deliberate highlight */
  --status-success: #22c55e;
  --status-warning: #eab308;
  --status-danger: #ef4444;
  --status-neutral: #737373; /* proposed / unresolved / deferred */
}
```

- Three grays only: `bg`, `surface`, `border`/`text-secondary` tier. Do not introduce a fourth.
- One accent color, used sparingly: link color, focus ring, a left-border on the conclusion callout, maybe one underline. Not decorative fills.
- Semantic colors (`success`/`warning`/`danger`/`neutral`) are for status badges and risk indicators only — never for decoration.
- If the document may be read in bright environments or printed, offer a light variant via `prefers-color-scheme` using the same structure (`--bg: #ffffff`, `--surface: #f5f5f5`, `--border: #e5e5e5`, `--text-primary: #171717`, `--text-secondary: #525252`, same accent and semantic colors, darkened slightly for contrast). Default to dark when the user hasn't specified.

### Typography

Fixed scale, applied consistently — do not invent sizes outside it:

```css
--text-xs: 13px;   /* metadata, captions, timestamps */
--text-sm: 15px;   /* secondary content, table cells */
--text-base: 17px; /* body copy */
--text-lg: 24px;   /* section headings */
--text-xl: 32px;   /* document title / main conclusion */
```

- System sans-serif stack for UI and body text: `-apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif`.
- System monospace stack for code: `ui-monospace, "SF Mono", Consolas, "Roboto Mono", monospace`.
- Line-height: 1.5–1.6 for body text, 1.2–1.3 for headings.
- Heading weight 600–700, body weight 400. That contrast alone does most of the hierarchy work — avoid adding size for things that only need weight.
- The title or main conclusion should read as the visual anchor of the page: largest size, tightest line-height, placed before anything else.

### Spacing

Fixed scale in px, multiples of 4: `4, 8, 16, 24, 40, 64`. Use these for all padding, margin, and gap values — no arbitrary numbers. Section breaks get the largest step (40–64px); related elements within a section get the smallest (4–8px).

### Layout widths

- Prose content: max-width 640–720px.
- Tables, code blocks, diagrams, wide comparisons: may extend to 960–1080px, in their own scroll container if they can't collapse safely (see Responsive rules).
- Center the content column; don't let it pin to one edge at desktop widths.

### Components

- **Table:** `--surface` header row, `1px solid var(--border)` row dividers, no vertical rules, 8–16px cell padding, header text in `--text-secondary` at `--text-xs` with letter-spacing.
- **Code block:** `--surface` background, `1px solid var(--border)`, 4–6px border-radius, monospace at `--text-sm`, 16px padding, horizontal scroll container rather than wrap for long lines.
- **Callout:** `--surface` background, 3–4px left border in the relevant semantic color (or `--accent` for the main conclusion), 16px padding, no full border on the other three sides.
- **Status badge:** small pill, `--text-xs`, semantic color at ~15% opacity as background with the full-strength color as text/border. One consistent shape and size across the whole document — don't vary badge style by section.

### General

- Fine 1px borders over shadows or dividers.
- Do not add a hero section, oversized title treatment beyond the type scale above, gradients, glass effects, glowing effects, decorative navigation, arbitrary card grids, fake dashboards, fake metrics, or ornamental chrome.
- Do not add animations unless motion explains a sequence or state change that static presentation cannot explain as clearly.
- Maintain WCAG AA contrast minimums and a visible keyboard focus state (use `--accent` for focus rings).

## Responsive rules

- Include `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1">`, and a descriptive `<title>`.
- Use a fluid layout that works from narrow phone screens through desktop widths.
- Respect the max-widths above; do not use a fixed-width page.
- Do not require page-level horizontal scrolling.
- Put tables, code blocks, diagrams, and mock frames in their own `overflow-x: auto` containers when they cannot collapse safely.
- Keep touch targets at least 44px tall and text readable at roughly 375px width.
- Respect `prefers-reduced-motion` when motion exists.

## Accessibility

- Use semantic landmarks: one `<main>`, `<nav>` only if in-page navigation exists, correct heading order with no skipped levels (`h1` → `h2` → `h3`).
- Give every inline SVG icon or diagram either `aria-hidden="true"` (if purely decorative) or a `<title>` element describing it (if it conveys information).
- Give every image a meaningful `alt`; empty `alt=""` only for purely decorative images.
- Ensure focus order follows visual/reading order.

## JavaScript rules

- Use JavaScript when it materially improves the document.
- Appropriate uses: filtering a large comparison, switching between meaningful alternatives, in-page navigation/table-of-contents for long content, revealing genuinely secondary evidence, comparing UI states, copying useful content, exporting structured content, running a small calculation.
- Example line: filtering a 50-row comparison table by category — yes. A fake dark/light theme toggle when one theme is sufficient — no. Jumping to a section via a table of contents — yes. A collapsible section that hides content the reader needs to evaluate the conclusion — no.
- Keep all essential conclusions, evidence, decisions, and instructions present in the HTML before JavaScript runs.
- Do not add JavaScript for decorative animation, fake controls, theme switching when one theme is sufficient, unnecessary collapsible sections, cosmetic hover behavior, simulated application behavior, or state management the document does not need.
- Use only an inline classic script. Do not use external scripts or module scripts.
- Do not use storage, cookies, network requests, workers, frames, forms, popups, automatic navigation, or background activity.

## UI mocks

- Use UI mocks only as explanatory material inside the communication document.
- Build mocks with semantic HTML and simple inline CSS, using the visual system above so mocks feel native to the document rather than dropped in. Use inline SVG only for useful icons, diagrams, or simple illustrations.
- Label each mock as current, proposed, exploratory, illustrative, or final, using the status badge spec.
- Do not present invented UI as implemented product state.
- Show empty, loading, error, success, disabled, mobile, or desktop states only when those states affect the decision.
- Use realistic, internally consistent labels and content. Avoid meaningless placeholder copy when source-grounded copy is available.
- Place assumptions, annotations, decisions, and unresolved questions near the relevant mock.
- Make mock frames responsive even when they represent a desktop viewport.
- Do not turn the document into a working application.
- Do not add submission, authentication, persistence, network activity, or simulated backend behavior.

## Portability

- Produce exactly one self-contained HTML file capped at 512 KB.
- Use semantic HTML, inline CSS, inline SVG, and HTTPS or data-URL images.
- Do not include external or module scripts, linked stylesheets, CSS `@import`, remote fonts, analytics, telemetry, or tracking pixels.

## Safety

- Do not include inline event-handler attributes such as `onclick`, `onload`, or `onerror`.
- Do not include `javascript:` URLs.
- Do not include forms, submission controls, frames, iframes, `srcdoc`, embeds, objects, applets, `base` elements, or meta refresh.
- Do not use storage, cookies, workers, service workers, popups, downloads, clipboard reading, automatic navigation, or browser permission APIs.
- Do not initiate network requests from JavaScript.
- Do not include secrets, credentials, tokens, signed URLs, private network addresses, sensitive internal endpoints, or local filesystem paths.
- Include authenticated workspace links only when the user supplied them or the task explicitly requires them.
- In a script-free file, give external HTTPS links `target="_blank"` and `rel="noopener noreferrer"`.
- If the file contains any script, omit `target="_blank"` from every link. Never simulate new-window behavior with JavaScript.

## Verification

Run:

```
python3 scripts/validate_html.py <path-to-html>
```

If that script is not present in the environment or fails to run, note this limitation explicitly to the user rather than skipping verification silently, and fall back to a manual structural check against the rules above (file size, forbidden elements, single-file self-containment).

Then, when local rendering is permitted, open or render the document at desktop and roughly 375px width and confirm:

- The main conclusion is obvious within the first screen-height.
- The document contains no filler sections or unsupported claims.
- The file opens without missing resources or console errors.
- Long text, tables, code, diagrams, and mock labels do not overflow.
- The page remains usable near 375px width, including touch target size.
- The visual system is applied consistently: fixed type scale, fixed spacing scale, three-gray palette plus one accent, consistent component styling.
- Every control has a clear communication purpose and works with pointer and keyboard input, with a visible focus state.
- Essential content remains available without JavaScript.
- Status labels do not blur verified, inferred, proposed, and deferred information.

If local-file browser access is blocked, report that limitation honestly. Do not claim a visual browser pass from structural validation alone.
