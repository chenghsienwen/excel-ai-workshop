# TwoCols

Lays out content in two equal-width dark cards side by side, with optional titles and an orange hover effect matching the project theme.

---

## Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `leftTitle` | `string` | — | Optional heading displayed above the left column content. |
| `rightTitle` | `string` | — | Optional heading displayed above the right column content. |

---

## Slots

| Slot | Description |
|---|---|
| `left` | Content for the left card. |
| `right` | Content for the right card. |

---

## Features

### Two-Column Grid
Uses `display: grid; grid-template-columns: 1fr 1fr` with a `1.5rem` gap. Each card fills the available height (`calc(100% − 5rem)` from the top of the grid).

### Hover Effect
Hovering a card lifts it (`transform: translateY(-2px)`, `box-shadow`), darkens the background to `#5a3520`, and overlays `rgba(255, 153, 102, 0.18)` — the same orange accent used elsewhere in the theme.

### Optional Title Bar
When `leftTitle` or `rightTitle` is supplied, a bold white heading with a bottom border (`1px solid #444`) is rendered above the slot content. The title is omitted entirely when the prop is absent.

---

## Usage

```md
<!-- Without titles -->
<TwoCols>
  <template #left>
    Left content here
  </template>
  <template #right>
    Right content here
  </template>
</TwoCols>

<!-- With titles -->
<TwoCols left-title="Before" right-title="After">
  <template #left>
    Original approach
  </template>
  <template #right>
    Improved approach
  </template>
</TwoCols>
```

---

## Styling

| Token | Value | Usage |
|---|---|---|
| Card background | `#2a2a2a` | Default card fill |
| Hover background | `#5a3520` | Card fill on hover |
| Hover overlay | `rgba(255, 153, 102, 0.18)` | Orange tint via `::before` pseudo-element |
| Title colour | `#fff` | Column heading text |
| Title border | `1px solid #444` | Separator below the title |
| Border radius | `0.75rem` | Card corners |
