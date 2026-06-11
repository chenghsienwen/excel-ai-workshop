# ChatWindow

Displays a mock ChatGPT-style conversation window with up to five Q&A turns, zoom controls, and automatic height clamping to the slide boundary.

---

## Props

No props. All content is provided via named slots.

---

## Slots

| Slot | Description |
|---|---|
| `question` | User message for turn 1. |
| `response` | AI response for turn 1. |
| `question2` / `response2` | User message and AI response for turn 2. |
| `question3` / `response3` | User message and AI response for turn 3. |
| `question4` / `response4` | User message and AI response for turn 4. |
| `question5` / `response5` | User message and AI response for turn 5. |

Turns are rendered in order. A turn is only included when its `questionN` slot is present; the corresponding `responseN` slot is optional (renders an empty AI bubble if absent).

---

## Features

### Multi-Turn Rendering
The component checks slots `question`, `question2` … `question5` and renders only the turns that have content. This means you can show a single exchange or a back-and-forth thread of up to five turns using the same component.

### Zoom
The title bar contains **−** and **+** buttons that scale the message area in 10% steps. The range is **50%–200%**. The current percentage is shown between the two buttons.

### Height Clamping
On mount (and whenever the `.slidev-layout` ancestor resizes), the component measures the vertical space available below its top edge and sets its `max-height` to fill that space minus 24 px of bottom breathing room. This prevents the window from overflowing the slide.

### Scrollable Message Area
When content exceeds the clamped height, the message area scrolls vertically. A narrow 4 px scrollbar appears on hover.

---

## Usage

```md
<!-- Single Q&A turn -->
<ChatWindow>
  <template #question>
    What is a pivot table?
  </template>
  <template #response>
    A <b>pivot table</b> summarises rows of data into a cross-tabulated grid,
    letting you group, aggregate, and filter without writing formulas.
  </template>
</ChatWindow>

<!-- Two turns — add class for alignment within the slide -->
<ChatWindow class="text-left mt-6">
  <template #question>
    How do I freeze the top row in Excel?
  </template>
  <template #response>
    Go to <code>View → Freeze Panes → Freeze Top Row</code>.
    The first row stays visible as you scroll down.
  </template>

  <template #question2>
    Can I freeze a column at the same time?
  </template>
  <template #response2>
    Yes — click the cell <b>below and to the right</b> of the rows/columns
    you want frozen, then choose <code>Freeze Panes</code> (not the sub-options).
  </template>
</ChatWindow>
```

---

## Styling

The component uses a fixed dark theme and is not configurable via props:

| Token | Value | Usage |
|---|---|---|
| Background | `#171717` | Window, title bar, footer |
| Border | `#2f2f2f` | Window outline, title-bar separator |
| User bubble | `#2f2f2f` fill, `#3e3e3e` border | User message background |
| User avatar | `#ab5cf0` | Purple circle with "U" |
| AI avatar | `#19c37d` | Green circle with OpenAI-style icon |
| Body text | `#ececec` | Message text |
| Max width | `max-w-3xl` (48 rem) | Centered with `mx-auto` |
