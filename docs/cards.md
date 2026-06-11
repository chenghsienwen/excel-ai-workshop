# cards (layout)

A Slidev layout that renders a grid of themed cards, each supporting an image, title, text, bullet list, and tags. Data can be supplied via frontmatter or props.

---

## Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `background` | `string` | theme grid bg | Background image path or CSS value passed to `bgStyle`. |
| `cards` | `Card[]` | `[]` | Array of card objects (see Card fields below). Falls back to `$frontmatter.cards`. |
| `cols` | `number` | `cards.length` | Number of grid columns. Falls back to `$frontmatter.cols`. |
| `fill` | `boolean` | `false` | When `true`, columns use `1fr` (stretch to fill width) instead of `minmax(0, 18rem)`. Falls back to `$frontmatter.fill`. |

All four props are also readable from the slide's YAML frontmatter. The prop value takes precedence over frontmatter when both are present.

---

## Card Fields

Each entry in the `cards` array is a `Card` object:

| Field | Type | Description |
|---|---|---|
| `image` | `string` | Image path. Resolved via `themeImage` + `BASE_URL` prefix for absolute paths (GitHub Pages safe). |
| `title` | `string` | Card heading, rendered as `<h3>`. |
| `text` | `string` | Short paragraph below the title. |
| `items` | `string[]` | Bullet list rendered as `<ul>`. |
| `tags` | `string[]` | Tag chips displayed below `items`. Prefixed with `#`, styled in monospace blue. |

All fields are optional. A card with only `image` and no text fields renders as image-only (full-height image, no body panel). A card with no `image` renders as text-only (body panel fills the full card).

---

## Slots

| Slot | Description |
|---|---|
| `default` | Heading and optional subtitle rendered above the card grid. Typically `# Title` and a paragraph. |

---

## Features

### Frontmatter-Driven Data
`cards`, `cols`, and `fill` are resolved from `$frontmatter` when not passed as props. This means the full card set can be declared in YAML without any inline template code.

### Responsive Grid
The grid uses CSS custom properties `--cols`, `--rows`, and `--col-size`. Card min/max height is divided by `--rows` so cards scale proportionally when multiple rows are present.

### Column Width Modes
- **Default**: columns are `minmax(0, 18rem)` — cards have a maximum width and the grid is centred.
- **`fill: true`**: columns are `1fr` — cards stretch to fill the available width.

### Clipped Image and Body
An inline `<svg>` defines two `<clipPath>` shapes (unique per instance via `useId()`):
- **Image**: bottom-right chamfer (top-left corner cut).
- **Body**: top-left chamfer (bottom-right corner cut).

These two shapes interlock when a card has both an image and a body panel.

### Hover Effect
Hovering a card lifts it (`translateY(-2px)`, drop shadow), overlays `rgba(255, 153, 102, 0.18)` orange tint via `::before`, and darkens the body to `#5a3520`.

### Image Resolution
`resolveImage()` patches absolute user paths (e.g. `/images/foo.jpg`) by prepending `BASE_URL` so images load correctly when the site is served from a GitHub Pages subpath.

### Theme Chrome
`ConfidentialMark`, `PageNumber`, and the ViewSonic logo mark are included automatically and require no extra markup.

---

## Usage

```md
---
layout: cards
cols: 3
cards:
  - image: /images/excel-icon.png
    title: Import Data
    text: Load .xlsx files directly into the sheet.
  - title: Pivot Tables
    items:
      - Group rows by category
      - Aggregate with SUM / COUNT
    tags:
      - excel
      - data
  - title: Charts
    text: Visualise trends with one click.
    tags:
      - visualisation
---

# Workshop Overview
Three things you will learn today.
```

```md
<!-- fill mode: cards stretch to full width -->
---
layout: cards
fill: true
cols: 2
cards:
  - title: Before
    text: Manual copy-paste every morning.
  - title: After
    text: Automated report in 30 seconds.
---

# The Difference
```

---

## Notes

- `cols` defaults to `cards.length` when omitted, producing a single-row layout.
- When `rows > 1`, card heights shrink proportionally (`min-height: calc(27rem / rows)`). For more than two rows, reduce card content or set a larger `cols` value.
- Tags are purely decorative — they carry no interactive behaviour.
