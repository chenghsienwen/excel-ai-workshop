# ExcelViewer

Renders an `.xlsx` or `.csv` file inside a macOS-style window chrome with zoom, drag-to-pan, sheet tabs, and cell range highlight.

---

## Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `path` | `string` | — | Path to the file, relative to `public/` or `app/` |
| `sheet` | `string \| number` | first sheet | Sheet name or zero-based index to display on mount |
| `defaultZoom` | `number` | `1` | Initial zoom factor (e.g. `1.3` = 130%) |

---

## Features

### Zoom
Three controls in the title bar: **−**, a clickable zoom percentage (click to reset to 100%), and **+**. Range: 30 %–300 %.

### Drag-to-Pan
Click and drag on the empty scroll area (not on a cell) to pan the sheet in any direction.

### Sheet Tabs
When the file has more than one sheet, tabs appear below the title bar. Switching tabs clears any active highlight.

### Cell Range Highlight
Click on any cell to start a selection, then drag to extend it. The selected range is highlighted with the same orange used for card hover effects (`rgba(255, 153, 102, 0.18)` fill + `rgba(255, 153, 102, 0.55)` outline).

A badge in the title bar shows the selection size (e.g. `3×4`) and acts as a **clear** button. Click it to remove the highlight.

---

## Usage

```md
<ExcelViewer path="/app/bm_report/raw_data/CDE biz status_2024_v1.xlsx" />

<!-- start on the second sheet, 130% zoom -->
<ExcelViewer path="/data/layer1_report_sample.csv" :sheet="1" :default-zoom="1.3" />
```

---

## Highlight Color Reference

The selection color matches the default card hover in `slidev-theme-viewsonic-proav`:

```css
background: rgba(255, 153, 102, 0.18);   /* #ff9966 @ 18% — fill */
outline:    1px solid rgba(255, 153, 102, 0.55); /* #ff9966 @ 55% — border */
```

---

## File Resolution

1. Files under `app/` are bundled at build time via `import.meta.glob`.
2. Files under `public/` are fetched at runtime; the component prepends `BASE_URL` so GitHub Pages subpaths work.
