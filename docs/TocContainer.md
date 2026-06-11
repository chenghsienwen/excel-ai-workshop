# TocContainer

Wraps `<Toc>` (or any content) in a height-clamped, vertically scrollable container that tracks the `.slidev-layout` ancestor size via `ResizeObserver`.

---

## Props

No props. All content is provided via the default slot.

---

## Slots

| Slot | Description |
|---|---|
| `default` | Content to wrap — typically a Slidev `<Toc>` component. |

---

## Features

### Height Clamping
On mount and on every resize of the nearest `.slidev-layout` ancestor, the component calculates the available vertical space (`slide.offsetHeight − component.offsetTop − 24 px`) and sets that as `max-height`. This prevents the TOC from overflowing the slide boundary.

### Vertical Scroll
`overflow-y: auto` lets the content scroll when it exceeds the clamped height. A 6 px scrollbar appears on hover (`#555` thumb, transparent track).

### ResizeObserver Cleanup
The observer is disconnected in `onBeforeUnmount` to prevent memory leaks.

---

## Usage

```md
<TocContainer>
  <Toc />
</TocContainer>

<!-- With custom indent -->
<TocContainer>
  <Toc :max-depth="2" />
</TocContainer>
```
