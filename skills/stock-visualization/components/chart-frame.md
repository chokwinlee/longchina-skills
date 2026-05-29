# Chart Frame Component

## Purpose

Provide a shared shell for every chart-like visual so reports get consistent titles, actions, fullscreen viewing, source hints, and edge-safe chart surfaces.

Use this for SVG charts, Canvas charts, vendored `lightweight-charts` panes, heatmaps, matrices, bubble or scatter plots, and visual comparison tables. This component does not fetch or transform data; it wraps the actual chart component.

## Input Schema

```json
{
  "chart_frame": {
    "id": "ai-valuation-bubble",
    "title": "AI relevance vs valuation crowding",
    "subtitle": "X axis is AI relevance, Y axis is valuation crowding.",
    "source_note": "prices and daily-metrics, latest available dates shown in labels",
    "fullscreen_label": "Open chart fullscreen"
  }
}
```

Required: `id`, `title`.

Optional: `subtitle`, `source_note`, `fullscreen_label`, legend content, chart actions.

## Configuration

- Use `lc-chart-frame` on the outer section and `data-lc-chart-frame` for JavaScript targeting.
- Use `data-lc-fullscreen` on the fullscreen action button.
- Use `lc-chart-frame__surface` around the chart itself.
- The chart surface must not clip labels, bubbles, legends, or axis text. Prefer reserved plot margins from `references/rendering-helpers.md` over `overflow: hidden`.
- Keep actions compact and icon-first. Include accessible labels for icon buttons.
- One report-level IIFE may initialize all chart frames on the page.

## HTML Snippet

```html
<div class="lc-chart-frame__backdrop" data-lc-fullscreen-backdrop hidden></div>
<section class="lc-chart-frame" data-lc-chart-frame aria-labelledby="lc-chart-title-ai-valuation">
  <style>
    .lc-chart-frame { border: 1px solid oklch(34% 0.026 78); border-radius: 8px; background: oklch(17% 0.018 78); color: oklch(88% 0.018 78); padding: 16px; }
    .lc-chart-frame__header { display: flex; align-items: start; justify-content: space-between; gap: 12px; margin-bottom: 12px; }
    .lc-chart-frame__title { margin: 0; font-size: 16px; line-height: 1.25; font-weight: 700; }
    .lc-chart-frame__subtitle { margin: 5px 0 0; color: oklch(75% 0.018 78); font-size: 12px; line-height: 1.45; }
    .lc-chart-frame__actions { display: flex; gap: 6px; flex: 0 0 auto; }
    .lc-chart-frame__button { border: 1px solid oklch(40% 0.032 78); border-radius: 6px; background: oklch(22% 0.02 78); color: inherit; min-width: 32px; min-height: 32px; cursor: pointer; }
    .lc-chart-frame__button:focus-visible { outline: 2px solid oklch(68% 0.12 54); outline-offset: 2px; }
    .lc-chart-frame__surface { position: relative; overflow: visible; }
    .lc-chart-frame__backdrop[hidden] { display: none; }
    .lc-chart-frame__backdrop { position: fixed; inset: 0; z-index: 999; background: oklch(0% 0 0 / 0.55); }
    .lc-chart-frame.is-fullscreen { position: fixed; inset: 16px; z-index: 1000; display: flex; flex-direction: column; max-height: calc(100vh - 32px); box-shadow: 0 24px 80px oklch(0% 0 0 / 0.45); }
    .lc-chart-frame.is-fullscreen .lc-chart-frame__surface { flex: 1 1 auto; min-height: 0; overflow: auto; }
    body.lc-fullscreen-open { overflow: hidden; }
  </style>
  <header class="lc-chart-frame__header">
    <div>
      <h2 class="lc-chart-frame__title" id="lc-chart-title-ai-valuation">AI relevance vs valuation crowding</h2>
      <p class="lc-chart-frame__subtitle">X axis is AI relevance, Y axis is valuation crowding.</p>
    </div>
    <div class="lc-chart-frame__actions">
      <button class="lc-chart-frame__button" type="button" data-lc-fullscreen aria-label="Open chart fullscreen">[ ]</button>
    </div>
  </header>
  <div class="lc-chart-frame__surface">
    <!-- Insert the chart component here. -->
  </div>
</section>
```

## Fullscreen Behavior

Attach one small report-level script after all chart frames. The script must work offline and must not depend on a framework:

```html
<script>
(() => {
  const frames = [...document.querySelectorAll("[data-lc-chart-frame]")];
  let activeFrame = null;
  let returnFocus = null;

  function emitResize(fullscreen) {
    window.dispatchEvent(new Event("resize"));
    window.dispatchEvent(new CustomEvent("lc:chart-resize", { detail: { fullscreen } }));
  }

  function getBackdrop() {
    let backdrop = document.querySelector("[data-lc-fullscreen-backdrop]");
    if (!backdrop) {
      backdrop = document.createElement("div");
      backdrop.className = "lc-chart-frame__backdrop";
      backdrop.setAttribute("data-lc-fullscreen-backdrop", "");
      backdrop.hidden = true;
      document.body.append(backdrop);
    }
    return backdrop;
  }

  function focusableElements(frame) {
    return [...frame.querySelectorAll("button, [href], input, select, textarea, [tabindex]:not([tabindex='-1'])")]
      .filter((element) => !element.disabled && element.offsetParent !== null);
  }

  const closeActive = () => {
    if (!activeFrame) return;
    activeFrame.classList.remove("is-fullscreen");
    activeFrame.querySelector("[data-lc-fullscreen]")?.setAttribute("aria-label", "Open chart fullscreen");
    getBackdrop().hidden = true;
    document.body.classList.remove("lc-fullscreen-open");
    const focusTarget = returnFocus;
    activeFrame = null;
    returnFocus = null;
    emitResize(false);
    focusTarget?.focus();
  };
  frames.forEach((frame) => {
    const button = frame.querySelector("[data-lc-fullscreen]");
    button?.addEventListener("click", () => {
      const opening = !frame.classList.contains("is-fullscreen");
      closeActive();
      if (!opening) return;
      returnFocus = button;
      activeFrame = frame;
      getBackdrop().hidden = false;
      frame.classList.add("is-fullscreen");
      button.setAttribute("aria-label", "Close chart fullscreen");
      document.body.classList.add("lc-fullscreen-open");
      button.focus();
      emitResize(true);
    });
  });
  getBackdrop().addEventListener("click", closeActive);
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeActive();
    if (event.key === "Tab" && activeFrame) {
      const items = focusableElements(activeFrame);
      if (!items.length) return;
      const first = items[0];
      const last = items.at(-1);
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  });
  new ResizeObserver(() => {
    emitResize(Boolean(activeFrame));
  }).observe(document.body);
})();
</script>
```

Use this script rather than a partial fullscreen handler. It closes with Escape, closes on backdrop click, traps focus inside the fullscreen frame, restores focus to the opener, and emits resize events for chart engines.

## Missing Data Behavior

If a chart has no valid rows, keep the frame visible and render the component's empty state inside `lc-chart-frame__surface`. Do not fabricate chart points, labels, fullscreen content, or source notes.

## Example

Use `chart-frame.md` around `valuation-band-chart.md`, `benchmark-comparison.md`, `peer-factor-heatmap.md`, bubble or scatter SVGs, and candlestick chart panes. For bubble and scatter plots, combine this frame with the `Edge-Safe Labels` rules in `references/rendering-helpers.md`.
