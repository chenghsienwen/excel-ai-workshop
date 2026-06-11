# Counter

An interactive increment/decrement counter with an optional starting value.

---

## Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `count` | `number` | `0` | Initial counter value. |

---

## Features

### Increment / Decrement
Two buttons (`−` and `+`) flanking the current value. Each click adjusts the internal reactive counter by 1. The displayed value updates immediately; the `count` prop is only used to seed the initial state and is not kept in sync afterward.

---

## Usage

```md
<!-- Default starting at 0 -->
<Counter />

<!-- Start at a specific value -->
<Counter :count="5" />
```

---

## Notes

- The counter state is local to the component instance and resets when the slide is unmounted.
- Styling inherits UnoCSS utility classes (`border`, `p`, `font-mono`, `hover:bg`) from the Slidev theme — appearance may vary across themes.
