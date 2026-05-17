# Sortable Table Component

## Purpose

Render a bounded stock pool or constrained market subset as a sortable metric table. Use it for light exploration, not unbounded full-market exports.

## Input Schema

```json
{
  "columns": [
    { "key": "name", "label": "Name", "type": "text" },
    { "key": "pe_ttm", "label": "PE TTM", "type": "number", "unit": "x" },
    { "key": "pb", "label": "PB", "type": "number", "unit": "x" },
    { "key": "turnover_rate", "label": "Turnover", "type": "number", "unit": "%" }
  ],
  "rows": [
    { "ts_code": "000001.SZ", "name": "Example Bank", "pe_ttm": 5.94, "pb": 0.62, "turnover_rate": 0.81 }
  ]
}
```

Required: `columns`, `rows`, and a stable security identifier such as `ts_code`.

Optional: `unit`, `description`, `trade_date`.

## Configuration

- `max_rows`: default 50 for generated HTML.
- `default_sort`: optional column key.
- `empty_label`: default `No rows returned for the selected stock pool.`

## HTML Snippet

```html
<section class="lc-sortable-table" aria-labelledby="lc-sortable-table-title">
  <style>
    .lc-sortable-table { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-sortable-table__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-sortable-table__wrap { overflow-x: auto; border: 1px solid oklch(88% 0.018 165); border-radius: 8px; background: oklch(99% 0.005 165); }
    .lc-sortable-table table { border-collapse: collapse; min-width: 680px; width: 100%; }
    .lc-sortable-table th, .lc-sortable-table td { border-bottom: 1px solid oklch(90% 0.012 165); padding: 9px 11px; font-size: 12px; text-align: right; }
    .lc-sortable-table th:first-child, .lc-sortable-table td:first-child { text-align: left; }
    .lc-sortable-table th { background: oklch(96% 0.008 165); color: oklch(42% 0.018 165); }
    .lc-sortable-table button { appearance: none; border: 0; background: transparent; color: inherit; font: inherit; font-weight: 650; cursor: pointer; padding: 0; }
    .lc-sortable-table button:focus-visible { outline: 2px solid oklch(54% 0.12 165); outline-offset: 3px; }
  </style>
  <h2 class="lc-sortable-table__title" id="lc-sortable-table-title">Metric table</h2>
  <div class="lc-sortable-table__wrap">
    <table data-lc-sortable>
      <thead>
        <tr><th><button data-key="name" data-type="text">Name</button></th><th><button data-key="pe_ttm" data-type="number">PE TTM</button></th><th><button data-key="pb" data-type="number">PB</button></th><th><button data-key="turnover_rate" data-type="number">Turnover</button></th></tr>
      </thead>
      <tbody>
        <tr><td data-key="name">Example Bank <span>000001.SZ</span></td><td data-key="pe_ttm" data-value="5.94">5.94x</td><td data-key="pb" data-value="0.62">0.62x</td><td data-key="turnover_rate" data-value="0.81">0.81%</td></tr>
        <tr><td data-key="name">Example Peer <span>600000.SH</span></td><td data-key="pe_ttm" data-value="6.38">6.38x</td><td data-key="pb" data-value="0.54">0.54x</td><td data-key="turnover_rate" data-value="0.66">0.66%</td></tr>
      </tbody>
    </table>
  </div>
  <script>
    (() => {
      document.querySelectorAll("[data-lc-sortable]").forEach((table) => {
        const parseCellNumber = (cell) => {
          const raw = cell?.dataset.value;
          const value = raw == null || raw === "" ? NaN : Number(raw);
          return Number.isFinite(value) ? { missing: false, value } : { missing: true, value: 0 };
        };
        table.querySelectorAll("button[data-key]").forEach((button) => {
          button.addEventListener("click", () => {
            const key = button.dataset.key;
            const type = button.dataset.type;
            const tbody = table.querySelector("tbody");
            const rows = Array.from(tbody.querySelectorAll("tr"));
            const direction = button.dataset.direction === "asc" ? "desc" : "asc";
            button.dataset.direction = direction;
            rows.sort((a, b) => {
              const aCell = a.querySelector(`[data-key="${key}"]`);
              const bCell = b.querySelector(`[data-key="${key}"]`);
              if (type === "number") {
                const av = parseCellNumber(aCell);
                const bv = parseCellNumber(bCell);
                if (av.missing && bv.missing) return 0;
                if (av.missing) return 1;
                if (bv.missing) return -1;
                return direction === "asc" ? av.value - bv.value : bv.value - av.value;
              }
              const av = aCell?.textContent ?? "";
              const bv = bCell?.textContent ?? "";
              return direction === "asc" ? av.localeCompare(bv) : bv.localeCompare(av);
            });
            rows.forEach((row) => tbody.appendChild(row));
          });
        });
      });
    })();
  </script>
</section>
```

## Missing Data Behavior

Render missing numeric values as `--` and omit `data-value`. Missing numeric values sort after real numeric values in ascending order.

## Example

Use in `recipes/metric-table.md` with a user-specified stock pool or an explicitly bounded industry subset.
