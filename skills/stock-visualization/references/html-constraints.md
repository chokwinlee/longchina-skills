# HTML Constraints

Generated reports should follow the repository design language in `DESIGN.md`: research-console UI for serious data work, not generic fintech styling.

## Design Register

Scene sentence: a quant developer reviews generated A-share reports on a desktop monitor in a quiet research session, focused on verification, exact values, and shareable evidence.

Theme: dark research console by default. Reports are generated artifacts and skill previews, so they should align with longchina's public showcase language while keeping dense product readability.

Color strategy: warm ink/paper neutrals, copper as the structural accent, blue as a secondary analytical/link color, and A-share semantic red/up plus green/down for market movement. Green is not a brand or UI accent. Use it only for explicit market-down or negative-market semantics, paired with text, sign, icon, or label so color is never the only signal.

## Offline Requirements

Every generated HTML report must be a single file:

- Inline CSS.
- Inline JavaScript.
- Inline the vendored `lightweight-charts.standalone.production.js` bundle when using interactive candlestick charts.
- Inline SVG or Canvas for charts.
- No `http://` or `https://` assets.
- No CDN chart libraries.
- No remote fonts.
- No remote images.
- No external scripts or stylesheets.
- License-required attribution links are allowed when they do not load remote runtime assets.

The finished report should open directly through `file://`. Prefer the built-in browser: open the `file://` URL in the Codex in-app Browser first so the user can inspect the report inside the agent workspace. Use the user's system default browser as a fallback only when the built-in browser is unavailable, cannot load the local file, or the user asks for an external browser. On macOS, fallback to `open "/absolute/path/to/report.html"`.

Do not start a local static server for normal viewing. Do not run screenshot or browser automation checks by default; reserve those checks for explicit render-debugging requests, failed opens, or shared component changes that need regression testing.

Do not call Playwright as a post-generation acceptance step. Do not run desktop/mobile screenshot passes, console-warning sweeps, or pixel checks for ordinary report delivery. If a render bug is suspected, run one targeted check only and avoid creating screenshot artifacts unless the screenshot is the debugging deliverable.

## Visual Rules

- Use OKLCH colors.
- Do not use pure `#000` or `#fff`.
- Do not use green for primary actions, navigation, brand marks, panel accents, generic success states, or decorative highlights.
- Do not use gradient text.
- Do not use decorative glassmorphism or blur panels.
- Do not use side-stripe borders as card accents.
- Do not use hero-metric layouts.
- Do not create identical decorative card grids.
- Keep body line length around 65 to 75 characters for prose.
- Use compact table and chart labels for dense data.
- Prefer system fonts: `-apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif`.
- Use system monospace for dataset names, field names, commands, and exact code-like values.
- Use tabular numerals for OHLC, indicator, valuation, volume, and table values.

## Component Composition

- Prefix component classes with `lc-`.
- Avoid global variable names. If JavaScript is needed, wrap it in an IIFE.
- Use `data-*` attributes for sortable numeric values.
- Keep snippets copyable into a larger document.
- Include visible empty states inside the component rather than failing silently.
- Use semantic HTML tables for tabular data.
- For interactive stock charts, keep the chart engine and data in the same HTML file; viewing must not require `npm`, Node.js, a frontend server, or network access.

## Chart Frame And Fullscreen

Every chart-like visual must use a shared chart frame with a visible fullscreen action. This includes SVG charts, Canvas charts, vendored `lightweight-charts` panes, heatmaps, matrix visuals, bubble or scatter plots, and visual comparison tables.

Use `components/chart-frame.md` as the outer shell:

- Put the title, subtitle, legend, source-date hint, and actions in the frame header.
- Add a button with `data-lc-fullscreen` and a clear accessible label such as `Open chart fullscreen`.
- Keep the chart surface edge-safe. Do not clip labels, bubbles, axis text, or legends at the right or bottom boundary.
- When fullscreen opens, use a fixed overlay style, preserve the same report theme, and keep the chart content inside the viewport with internal scrolling only when necessary.
- Support `Escape` to close, background click to close when safe, and a small focus trap between the close button and chart actions.
- On open and close, dispatch a `resize` event and a custom `lc:chart-resize` event so SVG, Canvas, and chart-engine components can recalculate dimensions.
- Do not write partial fullscreen handlers in recipes or examples; compose the `chart-frame.md` markup and script.
- Do not create a new browser window, load remote assets, or require a dev server for fullscreen viewing.

## Accessibility

- Meet WCAG AA contrast for text and key chart labels.
- Pair color with labels, signs, or icons for gain/loss states.
- Use `aria-label` or `role="img"` on SVG charts.
- Keep focus states visible on interactive table headers.
- Respect reduced motion and avoid decorative animation.
