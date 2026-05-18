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

## Accessibility

- Meet WCAG AA contrast for text and key chart labels.
- Pair color with labels, signs, or icons for gain/loss states.
- Use `aria-label` or `role="img"` on SVG charts.
- Keep focus states visible on interactive table headers.
- Respect reduced motion and avoid decorative animation.
