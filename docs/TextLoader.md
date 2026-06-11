# TextLoader

Displays a plain-text or Markdown file inside a macOS-style terminal window with font-size zoom controls and automatic height clamping to the slide boundary.

---

## Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `path` | `string` | — | **Required.** Path to the file to display. Resolved against `app/` (bundled) or `public/` (runtime fetch). |
| `defaultFontSize` | `number` | `0.68` | Initial font size in `rem`. Range: `0.30`–`1.40`. |

---

## Features

### Font-Size Zoom
**A−** and **A+** buttons in the title bar adjust the font size in 0.04 rem steps. The range is **0.30 rem – 1.40 rem**. The current value is applied via inline style on the `<pre>` element.

### File Resolution
1. Files under `app/` are bundled at build time via `import.meta.glob('/app/**/*.md', { query: '?raw' })`.
2. If not found in the bundle, the component falls back to a `fetch()` against `public/`, prepending `BASE_URL` so GitHub Pages subpaths work correctly.

### Loading and Error States
- While loading: displays "Loading…" inside the window body.
- On fetch failure or missing file: displays a red error message (`File not found: <path>` or the caught exception string).

### Height Clamping
On mount (and on slide resize via `ResizeObserver`), the component measures the vertical space from its top edge to the `.slidev-layout` ancestor's bottom and sets `max-height` accordingly (minus 24 px breathing room). The content area scrolls vertically when text overflows.

### Title Bar
Displays the file name (last path segment) centred in the title bar, truncated with an ellipsis if it overflows.

---

## Usage

```md
<!-- Display a bundled markdown file -->
<TextLoader path="/app/bm_report/README.md" />

<!-- Start at a larger font size -->
<TextLoader path="/app/bm_report/README.md" :default-font-size="0.9" />
```

---

## File Resolution

| Location | Mechanism |
|---|---|
| `app/**/*.md` | Bundled via `import.meta.glob` at build time |
| `public/**` | Fetched at runtime via `fetch(BASE_URL + path)` |
