# QrCode

Renders a QR code for a given URL as an inline SVG, with configurable size and colours.

---

## Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `url` | `string` | — | **Required.** The URL (or any string) to encode. |
| `size` | `number` | `200` | Width and height of the rendered SVG in pixels. |
| `light` | `string` | `'#ffffff'` | Background (light module) colour. Accepts any CSS colour value. |
| `dark` | `string` | `'#000000'` | Foreground (dark module) colour. Accepts any CSS colour value. |

---

## Features

### SVG Output
Uses the `uqr` library to encode the URL into a boolean matrix, then renders each dark module as a `<rect>` element inside an `<svg>`. `shape-rendering="crispEdges"` ensures pixel-sharp modules at any display resolution.

### Colour Customisation
Both the background and foreground colours are fully configurable via props. This allows the QR code to blend into dark-themed slides (e.g. `light="#1a1a1a" dark="#ffffff"`).

---

## Usage

```md
<!-- Default white background, black modules, 200×200 px -->
<QrCode url="https://example.com" />

<!-- Custom size and inverted colours for dark slides -->
<QrCode url="https://example.com" :size="160" light="#171717" dark="#ececec" />
```

---

## Notes

- The `url` prop accepts any string, not just URLs. Any content encodable as a QR code (text, wifi credentials, etc.) works.
- The rendered SVG has a fixed pixel `width`/`height` matching `size`. Use CSS `transform: scale(...)` or a wrapper element if you need responsive sizing.
