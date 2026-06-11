# CurrentDate

Injects today's date (`YYYY.MM.DD`) into the cover slide at runtime, evaluated when the page loads.

---

## Props

No props. The date is computed from `new Date()` at component initialisation time.

---

## Features

### Runtime Date
The date is derived from `new Date()` when the component first runs in the browser — it reflects the visitor's local date, not a build-time value. Format is always `YYYY.MM.DD` (zero-padded month and day).

### Cover-Slide Teleport
Rendered via `<Teleport to=".slidev-layout.cover" defer>`, so the label physically moves into the cover slide's DOM regardless of where `<CurrentDate />` appears in the markup. The `defer` attribute ensures the target exists before insertion. Only visible on slides using the `cover` layout.

### Positioning
Absolutely positioned at bottom-right of the cover layout (`bottom: 2rem; right: 2.4rem`), with `z-index: 10` and `white-space: nowrap`.

---

## Usage

```md
---
layout: cover
---

# My Presentation

<CurrentDate />
```

---

## Notes

- Compare with `LastModifiedDate`, which shows the last git commit date (build-time) rather than the current date.
- The component has no visible output outside a `.slidev-layout.cover` element.
