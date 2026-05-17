# HTML Constraints

Generated reports should feel like product UI for research work: quiet, dense, and easy to verify.

## Design Register

Scene sentence: a quant developer reviews generated A-share reports on a desktop monitor in a quiet research session, focused on verification and comparison.

Theme: light. These reports need high legibility for inspection, export, and printed review.

Color strategy: restrained product UI with tinted neutrals, one green action/accent, semantic red and green for movement, and text or symbols so color is never the only signal.

## Offline Requirements

Every generated HTML report must be a single file:

- Inline CSS.
- Inline JavaScript.
- Inline SVG or Canvas for charts.
- No `http://` or `https://` assets.
- No CDN chart libraries.
- No remote fonts.
- No remote images.
- No external scripts or stylesheets.

## Visual Rules

- Use OKLCH colors.
- Do not use pure `#000` or `#fff`.
- Do not use gradient text.
- Do not use decorative glassmorphism or blur panels.
- Do not use side-stripe borders as card accents.
- Do not use hero-metric layouts.
- Do not create identical decorative card grids.
- Keep body line length around 65 to 75 characters for prose.
- Use compact table and chart labels for dense data.
- Prefer system fonts: `-apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif`.

## Component Composition

- Prefix component classes with `lc-`.
- Avoid global variable names. If JavaScript is needed, wrap it in an IIFE.
- Use `data-*` attributes for sortable numeric values.
- Keep snippets copyable into a larger document.
- Include visible empty states inside the component rather than failing silently.
- Use semantic HTML tables for tabular data.

## Accessibility

- Meet WCAG AA contrast for text and key chart labels.
- Pair color with labels, signs, or icons for gain/loss states.
- Use `aria-label` or `role="img"` on SVG charts.
- Keep focus states visible on interactive table headers.
- Respect reduced motion and avoid decorative animation.
