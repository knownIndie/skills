---
name: better-html-doc
description: Create or remake standalone HTML reading documents using the approved compact layout, right outline panel, collapsible reading settings, font and theme controls, and whole-section copying. Use for HTML reports, plans, specifications, handoffs, study guides, and long write-ups that should follow the Better HTML Doc design.
---

# Better HTML Doc

Build a self-contained HTML document using the compact reader design approved in this repository. The document has a separate reading area and an inset outline panel on the right. The header stays reachable while the document scrolls. Reading controls belong inside the panel, behind their own disclosure button.

Use this design for communication documents. Adapt the subject, section count, content structure and title to the task. The portfolio handoff in the example is sample content, not a required outline or a statement about the portfolio's current state.

## Working reference

Use [assets/reader-example.html](assets/reader-example.html) as the executable reference. It contains the approved CSS, behavior and embedded Schibsted Grotesk font. Copy and adapt it when creating a document rather than rebuilding the controls from memory. Replace the sample content, metadata, section IDs, copy labels and outline together.

For study guides or remaking an existing handbook, use [assets/javascript-interview-prep.html](assets/javascript-interview-prep.html). It demonstrates the same reader with topic completion buttons, self-checks, revision notes, code examples and interview drills. Its JavaScript subject matter is sample content, not a required subject for this skill.

This Markdown records the final design. Earlier image mockups are exploratory and may show superseded choices, including Serif and an expanded settings panel.

## Document structure

Use one `main` with a single `h1`, meaningful `h2` sections and `h3` subheadings. Each section has a stable ID, a heading row with its Copy section button, and a separate `.section-body` containing all copyable content. Keep the button outside that body.

Start with the title, useful metadata and a brief lead that states the purpose or conclusion. Add an evidence limitation or status note only when the material needs one. Use paragraphs, lists, tables and code according to the content. Main document sections stay expanded and available in one continuous page.

The right panel is an `aside` containing, in order:

1. Reading menu heading and Close button.
2. Reading settings disclosure button.
3. Collapsible text size, font, theme and reset controls.
4. Contents navigation with nested subheading links.

The settings disclosure and header menu toggle control different things. The header toggle shows or hides the entire panel. The disclosure shows or hides only its settings; the outline stays visible.

## Remaking existing documents and study guides

When the user asks to remake an existing document, preserve its material while replacing the presentation. Keep the sections, explanations, code, questions, answers, tables and useful study interactions. Do not silently summarize the material or execute its code examples. Compare the source and finished document's section text and code-block content to catch omissions and accidental changes.

Move the old contents list into the right outline instead of repeating it in the article. Generate unique IDs for every section and useful subheading. Headings containing operators can produce identical slugs, such as `== vs ===` and `|| vs ??`. Use distinct IDs and verify every outline target resolves.

Use the study example's patterns when the source contains completion tracking:

- Put a topic completion button beside its section's copy button, outside the copyable body.
- Use a 44px square toggle with an outlined checkbox icon and a visible check when pressed. Set `aria-pressed` and an accessible name identifying the topic or self-check. Keep self-check text beside its toggle.
- Show a checked-item count that updates in a polite live region. Keep study state in memory and state that progress resets on reload. If the source saved progress, disclose this change when delivering the remake. Preserve persistent progress only when the user requests it.
- Keep study controls out of copied text. Include the full self-check wording, questions and answers in section copies. Do not add the progress counter or control labels to the copy payload.
- Keep explanations and answers expanded. Use restrained, theme-aware callouts for rules, traps, interview answers and memory notes. Labels carry the meaning across all themes.
- Present revision summaries as clearly separated subsections. Wrap tables in their own horizontal scroll regions and preserve code whitespace in scrollable `pre` blocks.

Hide study buttons without JavaScript while leaving their text readable. Hide interactive study controls when printing. These additions belong in study documents that need them, not every report or handoff.

## Layout and scrolling

### Desktop, above 820px

| Element | Approved default |
| --- | --- |
| Header | Sticky at the top, with document label left and Reading menu button right |
| Header interior | Maximum width 1200px, minimum height 56px, 16px corner radius |
| Layout | Maximum outer width 1248px, 24px side padding, 24px column gap |
| Columns | Flexible document column and 304px right panel |
| Reading area | 40px padding, 18px corner radius, 1px border |
| Prose | Maximum width 680px, centered inside the reading area |
| Right panel | Sticky 104px from the top, 24px padding, 18px corner radius |
| Panel height | Maximum `calc(100dvh - 128px)`, with its own vertical scroll |
| Panel closed | One document column, maximum outer width 936px |

The desktop panel starts open. Closing it removes its column and centers the document. Keep the prose width bounded; filling a wider reading area must not create very long lines.

The document scrolls with the page. The panel scrolls independently when its contents exceed the available height. Use `overscroll-behavior: contain` in the panel. The header toggle remains available after scrolling down the document.

### Mobile, at or below 820px

Use one document column. The header has 8px vertical and 16px horizontal padding. The document has 16px side margins and 24px inner padding. At widths at or below 380px, reduce document side margins to 8px and inner padding to 16px.

The menu starts closed. Opening it displays an inset right drawer with `right: 16px`, `top: 88px`, `bottom: 16px` and `width: min(320px, calc(100vw - 32px))`. The drawer has its own vertical scroll and a dimmed backdrop. It does not create a permanent second column on the phone.

Move focus to Close when the drawer opens. Make the background document and header inert. Apply `role="dialog"` and `aria-modal="true"` only while it is open on mobile. Keep Tab and Shift+Tab within visible, enabled drawer controls and links. Collapsed settings must not enter that focus loop.

Close the drawer through Close, Escape or the backdrop, then return focus to the header toggle. Selecting a contents link closes it and moves focus to the destination heading instead. All document content remains reachable after dismissal.

When crossing the breakpoint, restore the desktop-open or mobile-closed default and clear any stale modal state. If a focused panel element becomes hidden, return focus to the header toggle. Preserve the selected reading settings during these layout changes.

## Reading settings

### Disclosure

Use a full-width Reading settings button with a downward chevron, `aria-controls` pointing to the settings container, and `aria-expanded` reflecting its state. Settings start collapsed on both desktop and mobile. Use the `hidden` attribute to remove the collapsed controls from layout and keyboard navigation.

Click once to show all settings and again to hide them. Hiding settings or closing the menu retains the chosen text size, font and theme. Keep the Contents heading and links outside the settings container.

### Text size

- Start at 18px, shown as 100% with an 18 px detail.
- Provide A− and A+ buttons with accessible names describing the text-size action.
- Change document text by 2px per click, with a minimum of 10px and maximum of 28px.
- Clamp values at the limits and disable the corresponding button.
- Display the rounded percentage relative to 18px and the current pixel value in a polite live output.
- Scale prose and its relative heading sizes through `--reader-size`. Keep menu labels and buttons at their interface sizes.
- Preserve the reader's position when size or font changes. Record a visible text element's vertical offset, update the style, and compensate for the new offset.
- Leave native browser zoom available. The A controls change document text size, not browser zoom.

### Fonts

Use three matching small buttons in one equal-width row, with 8px gaps and at least 44px height:

| Button | Font | Behavior |
| --- | --- | --- |
| Grotesk | Schibsted Grotesk, with system sans fallback | Applies to document prose and headings; accessible name and tooltip use the full font name |
| Sans | System sans stack | Default prose and heading style |
| Mono | System monospace stack | Applies to prose; headings retain the system sans style |

Use the same interface typography, padding and border treatment for all three buttons. Grotesk does not span the row or use a larger button. Do not include Serif. Code remains monospace regardless of the selected reading font.

Embed Schibsted Grotesk through a data-URL `@font-face`, with weights from 400 to 900 and a system fallback. Preserve its copyright and SIL Open Font License included in the reference HTML. This makes the document work offline without a remote font request.

### Themes

Offer White, Paper and Dark as three equal-width buttons in one row. Theme changes affect document and interface colors together. Keep font selection independent; Paper does not select a serif font or replace the reader's chosen font.

Use `aria-pressed` for font and theme choices. The active button has accent-colored text and border with a lightly tinted background. Keep visible keyboard focus on every control.

### Initial state and reset

Default to Sans and 18px. An explicit `?theme=white`, `?theme=paper` or `?theme=dark` sets the initial theme. Otherwise use Dark when the operating system requests dark mode and White when it does not. The reference resolves this preference on page load.

Reset text settings returns to Sans and 18px while retaining the current theme. Settings are held in memory for the open page and reset on reload. Do not add persistent storage as part of this design unless the user requests it.

## Visual tokens

| CSS token | White | Paper | Dark |
| --- | --- | --- | --- |
| `--page` | `#f5f5f7` | `#eee6d8` | `#181a1d` |
| `--surface` | `#ffffff` | `#f6f1e7` | `#24282e` |
| `--ink` | `#1d1d1f` | `#302b25` | `#e7e9ed` |
| `--muted` | `#52525b` | `#62594f` | `#b3bac4` |
| `--line` | `#e4e4e7` | `#d9cfc0` | `#3b424b` |
| `--accent` | `#005bb5` | `#175b8b` | `#8abfff` |
| `--selected` | `#e8f1fb` | `#e1e8eb` | `#263b50` |
| `--code` | `#f5f5f7` | `#eee6d8` | `#202328` |
| Backdrop | Black at 35% | Black at 35% | Black at 60% |

Keep the reading area and panel distinct from the page background. Use fine borders and restrained fills rather than ornamental shadows, gradients or card grids. Paper is a warm color option, not a claim that it improves comprehension.

Use these typography and spacing defaults:

- Body text at 18px with line-height 1.65; interface text at 15px with line-height 1.5.
- Headings at weight 600, line-height 1.25 and letter-spacing `-.02em`.
- `h1` at 1.8em on desktop and 1.55em on mobile; section headings at 1.35em; subheadings at 1.1em.
- Metadata at 14px; copy buttons and compact choice labels at 13px.
- Section breaks with 40px top margin, 24px top padding and a 1px border.
- Paragraph spacing of 16px; list-item spacing of 8px.
- Buttons at least 44px high with 8px corner radius. Icon buttons are 44px square with 18px inline SVG icons.
- Visible focus uses a 2px accent outline with 4px offset.

Let section headings and copy buttons wrap on narrow screens. Keep table text at roughly .9em with 16px cell padding, row dividers and a tinted header. Put wide tables and code blocks in their own horizontal scroll containers. Never make the entire page scroll horizontally.

## Contents navigation

Build the outline from the actual sections and useful subheadings. Use nested lists with a 16px indent for children and meaningful text labels. Each link has a 44px minimum target height and resolves to a stable section or heading ID.

Track the section or subheading reached during page scrolling. Mark the current link with `aria-current="location"` and the same selected fill used by the controls. Update the marker through a scroll listener scheduled with `requestAnimationFrame`.

A link click scrolls the destination below the sticky header and focuses its heading with `tabindex="-1"`. On desktop, keep the panel open. On mobile, close it first. Use immediate scrolling as in the reference. Coordinate header height, scroll padding and target scroll margin; the reference uses 96px page scroll padding and 8px target margin.

## Whole-section copying

Every main section has its own Copy section button with an accessible name identifying that section. Copy the `h2` text, a blank line and all plain text inside `.section-body`. Include nested subheadings, paragraphs, lists, table text and code. Copy only the selected section, not adjacent sections, menu labels or copy-button text.

Write to the clipboard only after the reader activates the button. Disable it while the write is pending. On success show Copied and announce the section name through a polite status region. Restore Copy section after about 2.5 seconds and clear the status after about 7 seconds.

When clipboard writing is unavailable or denied, select the section, show Selected and tell the reader to use the browser's Copy command. A one-time copy handler supplies the same clean plain-text payload. Do not claim success after a denied write or read the clipboard to check it.

## Portability and graceful fallback

Produce one self-contained HTML file with UTF-8, a viewport meta tag, a descriptive title, inline CSS, inline SVG and one inline classic script. Keep document content in the HTML before the script runs. Use embedded assets and fonts so it can open offline. Aim to stay within the existing HTML document validator's 512 KB cap.

The reader controls do not require a framework, backend, storage, tracking or external scripts. Use `addEventListener` rather than inline event-handler attributes. Keep font-license text in the artifact when embedding the font.

Without JavaScript, show the complete document and static outline, and hide controls that cannot work. On mobile, the static outline follows the article. Use a skip link and semantic table headers. Decorative icons are `aria-hidden`.

Printing hides the header, menu, backdrop, copy controls and status. Print a single white document column with dark text, no outer border, and a 12pt body size. Preserve the content's reading order.

## Creating and checking a document

Inspect the source material, write the document for its audience, and adapt the reference HTML. Maintain matching IDs and links when replacing sections. Keep document claims separate from implementation tests; recorded historical status is not evidence of a new audit.

Save the artifact under the task's output directory with a descriptive filename. Run the bundled validator from this skill's directory to check structural constraints:

```sh
python3 scripts/validate_html.py <path-to-document.html>
```

Validate the actual final artifact, not only the reference. The validator checks mechanical constraints; inspect content preservation and browser behavior separately.

Verify observable behavior in the browser:

- Desktop panel open, close and reopen; document and panel scroll independently.
- Mobile at 320px and a typical phone width, plus desktop, with no page-level horizontal overflow.
- Settings expand and collapse while Contents remains visible and selected settings remain applied.
- Size reaches 10px and 28px, limits disable correctly, reset returns to 18px Sans, and theme stays selected.
- Grotesk loads, all font buttons match in size, and font and theme choices work independently.
- Mobile focus enters the drawer, loops through visible controls, and returns correctly on Escape, dismissal and heading navigation.
- Outline targets exist, subheadings are reachable below the header, and the current-link marker updates.
- Section copying includes the full body and excludes interface labels; denied writes use the fallback. A test double verifies payloads, not an operating-system paste.
- Script-free and print views retain all essential content.
- For a remake, source section text and code examples are preserved. For study guides, topic and self-check toggles update the counter and do not contaminate copied sections.

Return a link to the finished HTML and state any material verification limits. Generate new image mockups only when the user asks for them. This skill's approved design comes from the working HTML.
