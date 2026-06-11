# LastModifiedDate

Injects a "Last updated: YYYY.MM.DD" label into the cover slide, sourced from the most recent git commit date at build time.

---

## Props

No props. The date value is injected at build time via the `__GIT_DATE__` global defined in `vite.config.ts`.

---

## Features

### Build-Time Date Injection
`vite.config.ts` runs `git log -1 --format="%cd" --date=format:"%Y.%m.%d"` at build time and exposes the result as the compile-time constant `__GIT_DATE__`. The component reads this constant directly — there is no runtime date calculation.

### Cover-Slide Teleport
The label is rendered via `<Teleport to=".slidev-layout.cover">`, so it physically moves into the cover slide's DOM node regardless of where `<LastModifiedDate />` is placed in the markup. The `defer` attribute ensures the teleport target exists before insertion. The label is only visible on slides that use the `cover` layout.

### Positioning
The label is absolutely positioned at the bottom-right of the cover layout (`bottom: 0.4rem; right: 2.4rem`), sits above other content with `z-index: 10`, and never wraps (`white-space: nowrap`).

---

## Usage

Place the component once anywhere in `slides.md` (conventionally near the top, on or after the cover slide):

```md
---
layout: cover
---

# My Presentation

<LastModifiedDate />
```

The label will appear at the bottom-right of the cover slide at build time.

---

## Notes

- The date reflects the **last git commit** at the time of build, not the current date. Running the dev server without a new commit will show the date of the most recent commit in the repo.
- The component has no visible output outside of a `.slidev-layout.cover` element — the teleport silently no-ops if no cover slide exists.
