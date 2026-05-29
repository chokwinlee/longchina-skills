# Rendering Helpers

Use these rules when turning normalized contracts into HTML. Component snippets show structure and styling; replace example values, table rows, and SVG points with values derived from returned data.

For OHLC stock price charts, use `references/chart-engine.md` and `components/candlestick-chart.md` first. The SVG coordinate helpers below are fallback guidance for static line charts, indexed comparisons, or non-OHLC metric series.

## Row Preparation

Group time-series rows by `symbol`, then sort each group by ascending `date`. Use the latest sorted row for cards, metric snapshots, comparison matrices, and default table rows.

When joining datasets:

- Join `securities` by `symbol`.
- Join latest `prices` and `daily-metrics` rows by `symbol`; do not assume both latest dates are the same.
- Keep each source date visible when latest dates differ.
- Keep `null` for known missing values until final display.

## SVG Line Coordinates

For a single fallback line chart:

1. Choose a fixed `viewBox`, for example `0 0 640 240`.
2. Reserve margins, for example left `48`, right `36`, top `28`, bottom `44`.
3. Use only finite numeric values when computing the scale.
4. Compute:

```text
plot_width = view_width - left - right
plot_height = view_height - top - bottom
x[i] = left + i * plot_width / max(point_count - 1, 1)
y[i] = top + (max_value - value[i]) * plot_height / max(max_value - min_value, epsilon)
```

If `min_value` equals `max_value`, pad the range by a small value such as `abs(value) * 0.01` or `1` before computing `y`.

For sparse series, omit null points. If null values split an otherwise valid line, render separate `<polyline>` elements for each contiguous segment instead of connecting across missing data.

## Edge-Safe Labels

Use these rules for bubble, scatter, heatmap, benchmark, metric, and any chart with point labels near a plot boundary. The common failure mode is drawing the point at the domain maximum and then placing the marker radius or text outside the right side of the SVG or canvas.

Before computing chart coordinates, reserve plot margins for both geometry and labels:

```text
axis_padding = 12
max_bubble_radius = maximum visible marker radius, or 0 for line-only charts
max_label_width = longest visible label width in pixels
label_gap = 8
right = axis_padding + max_bubble_radius + max_label_width + label_gap
left = max(left_axis_width, y_label_width) + axis_padding
plot_width = view_width - left - right
```

For every visible point label:

1. Place the label to the right of the marker by default.
2. If `label_x + label_width` would exceed `view_width - axis_padding`, flip the label to the marker's left side.
3. After choosing a side, clamp the label inside the chart surface:

```text
label_x = clamp(label_x, axis_padding, view_width - axis_padding - label_width)
label_y = clamp(label_y, top + label_height, view_height - bottom)
```

If several labels collide on the right edge, keep the most important labels visible and move the rest into a legend, tooltip, or adjacent data table. Do not rely on `overflow: visible` alone to rescue clipped labels; reserve space in the viewBox and the chart frame.

## Multi-Series Charts

When comparing securities with different price scales, either:

- render one chart per security, or
- normalize each series to an indexed base of `100` at its first valid point and label the chart as indexed performance.

Do not plot unrelated raw scales on one axis unless units and ranges are directly comparable. When using indexed values:

```text
indexed_value = current_value / first_valid_value * 100
```

## Display Formatting

Round only for display:

- Price: `2` decimals plus `CNY` when currency context is needed.
- Percent: `2` decimals plus `%`; include a leading `+` for positive movement.
- PE/PB/PS: `2` decimals plus `x`.
- Market value in CNY: compact to `亿` or `B CNY`, matching the report language.
- Missing values: `--`.

Preserve raw numeric values in `data-value` attributes for sorting.

## Sortable Tables

Numeric sorting must keep missing values after real values in both ascending and descending directions. Treat an omitted `data-value`, empty string, `null`, or non-finite number as missing.

Use this comparator shape inside the table IIFE:

```js
const parseCellNumber = (cell) => {
  const raw = cell?.dataset.value;
  const value = raw == null || raw === "" ? NaN : Number(raw);
  return Number.isFinite(value) ? { missing: false, value } : { missing: true, value: 0 };
};

rows.sort((a, b) => {
  const av = parseCellNumber(a.querySelector(`[data-key="${key}"]`));
  const bv = parseCellNumber(b.querySelector(`[data-key="${key}"]`));
  if (av.missing && bv.missing) return 0;
  if (av.missing) return 1;
  if (bv.missing) return -1;
  return direction === "asc" ? av.value - bv.value : bv.value - av.value;
});
```

For text columns, use `localeCompare` and include stable identifiers such as `symbol` in the visible row.

## Source Notes

If a chart uses indexing, moving averages, MACD settings, omitted null points, different latest dates, or any row limit, include that in the Source Footnote.
