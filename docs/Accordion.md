# Accordion

A collapsible section component for Slidev slides. Click the header to expand or collapse the content. Supports any slot content and starts open or closed via prop.

## Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `title` | `String` | *(required)* | Header label shown on the toggle button |
| `open` | `Boolean` | `false` | Whether the panel starts expanded |
| `titleClass` | `String` | `''` | Extra CSS classes applied to the title `<span>` |

## Usage

### Basic

```md
<Accordion title="What is Excel AI?">
  Excel AI combines spreadsheet automation with LLM-powered transformations.
</Accordion>
```

### Start open

```md
<Accordion title="Key Features" :open="true">
  - Formula generation
  - Data normalization
  - Report summarization
</Accordion>
```

### Multiple accordions (FAQ style)

```md
<Accordion title="What tools do we use?">
  Python · openpyxl · Claude API
</Accordion>

<Accordion title="Is my data secure?">
  Only the schema and prompt are sent to the AI — raw data stays local.
</Accordion>

<Accordion title="Do I need coding experience?">
  No. The AI generates the script; you just run it.
</Accordion>
```

### Custom title style

```md
<Accordion title="Advanced Options" titleClass="text-yellow-400">
  content here
</Accordion>
```

### On the Table of Contents slide (page 2)

```md
---
# Table of Contents

<Accordion title="Agenda" :open="true">
  <TocContainer>
    <Toc maxDepth="1" />
  </TocContainer>
</Accordion>
```

## Behaviour

- Toggle is triggered by clicking anywhere on the header bar.
- The `▲` / `▼` icon reflects open/closed state.
- Content fades and slides in/out via a CSS `Transition`.
- Header turns blue (`#1e3a5f`) when open, dark grey when closed.
- Multiple accordions on the same slide are independent — no "only one open at a time" constraint.
