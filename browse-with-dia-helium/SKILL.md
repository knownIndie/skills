---
name: browse-with-dia-helium
description: Automatically route browser requests to Dia, Helium, or Codex's in-app browser without using Google Chrome. Use whenever the user says to use or open the browser, browse, navigate to a site, search the web visibly, interact with a webpage, test a web page, or specifically names Dia or Helium. Default normal visible browsing to Dia, use Helium as a health-checked fallback or when explicitly requested, and reserve the in-app browser for tasks that require DOM, Playwright, console, or network inspection.
---

# Browse With Dia and Helium

Choose the browser automatically. Do not ask the user to choose unless the choice changes which logged-in account or browser session will be used. Never substitute Google Chrome.

## Browser selection

Apply this order:

1. Honor an explicit Dia or Helium request.
2. Use Dia with bundle identifier `company.thebrowser.dia` for ordinary browsing, searches, reading, authenticated sessions, and visible page interaction.
3. Use Helium with bundle identifier `net.imput.helium` when Dia cannot expose or control the required page. Verify that Helium exposes loaded web content before proceeding.
4. Use Codex's in-app browser only when the task requires DOM queries, Playwright, console output, network inspection, or browser-based local app testing that Computer Use cannot perform. Briefly state the technical reason before switching.

Continue in the browser already used for an active multi-step task. Do not silently move an authenticated task between browsers because their cookies and login state may differ.

## Workflow

1. Read the Computer Use skill and follow its confirmation policy.
2. Discover the Computer Use tools if they are not already callable.
3. Call `get_app_state` for the selected bundle identifier before interacting with it in each turn.
4. For a separate web task, open a new tab with `super+t`. Focus the address bar with `super+l`, type the URL or search query, and press `Return`.
5. Refresh app state after navigation. Prefer accessibility element identifiers for clicks and values. Use coordinates only when the required control is not exposed.
6. Refresh app state after any action that materially changes the page before relying on element identifiers again.
7. In Helium, confirm that the loaded page exposes web content, not only the toolbar. If the page is blank or absent from the accessibility tree, continue in Dia when account state is not material. Otherwise report the limitation. Do not guess click coordinates on an invisible page.
8. Keep risky UI actions behind the confirmations required by the Computer Use skill.

## Boundaries

The bundled `browser:control-in-app-browser` skill is tied to Codex's in-app browser and cannot be redirected to Dia or Helium. Do not claim that this skill changes that protocol.

Use this skill for automatic browser routing. Dia and Helium provide screen and accessibility based control, but they do not provide the in-app browser's Playwright, DOM, console, or network inspection APIs.
