# MermaidHighlight

A Slidev component that renders a Mermaid diagram and highlights one node per click, in declaration order. The number of click steps is derived automatically from the number of nodes in the diagram (N nodes → N+1 steps).

## Props

| Prop      | Type   | Default | Description                                |
|-----------|--------|---------|--------------------------------------------|
| `diagram` | String | —       | Raw Mermaid diagram code (required)        |
| `color`   | String | `#f96`  | Fill color applied to the highlighted node |

## Behavior

| Click index | Effect                              |
|-------------|-------------------------------------|
| 0 (initial) | Full diagram rendered, no highlight |
| 1           | First declared node highlighted     |
| 2           | Second declared node highlighted    |
| …           | …                                   |
| N           | Last declared node highlighted      |

Node IDs are parsed from the diagram string in declaration order. The following Mermaid keywords are excluded from detection: `flowchart`, `graph`, `subgraph`, `end`, `style`, `classDef`, `class`, `click`, `LR`, `RL`, `TD`, `TB`, `BT`.

## Usage

Define the diagram in a per-slide `<script setup>` block to keep the template clean:

```md
<script setup>
const flow = `flowchart LR
    A[Define\\nExcel Structure] --> B[Describe\\nTransformation]
    B --> C[Generate Python\\nCode via AI]
    C --> D[Run Script\\nLocally]
    D --> E[Validate\\nOutput]`
</script>

<MermaidHighlight :diagram="flow" />
```

Add `style` or a wrapper `<div>` for zoom/positioning as needed:

```md
<div style="zoom: 2.5; margin-top: 5rem">
  <MermaidHighlight :diagram="flow" />
</div>
```

Custom highlight color:

```md
<MermaidHighlight :diagram="flow" color="#4af" />
```

## How click registration works

Slidev determines a slide's total click count by scanning `v-click` directives at compile time. Because `MermaidHighlight` uses no `v-click` directives, it must register its steps programmatically at runtime:

1. On mount the component injects `$$slidev-clicks-context` — Slidev's per-slide `Ref<ClicksContext>`.
2. It calls `ctx.register(key, { delta: N, max: N })` where N is the number of parsed nodes.
3. This sets `clicksTotal = N`, so Slidev keeps the slide active for N presses before advancing.
4. On unmount it calls `ctx.unregister(key)` to clean up.

The `codeLz` computed reads `ctx.current` directly. Because `ctx.current` is a getter that internally reads a reactive `Ref`, Vue tracks it as a dependency and re-renders on every click.

Without step 2, `clicksTotal` stays 0 and ArrowRight skips the slide entirely — no highlight effect fires.

## Notes

- Works with any Mermaid diagram type (`flowchart`, `graph`, `sequenceDiagram`, etc.) as long as node IDs follow the `ID[shape]` / `ID(shape)` / `ID{shape}` syntax.
- Node parsing uses a regex on declaration order. Nodes referenced only as edge targets (without a shape bracket) are not picked up — declare all nodes explicitly if you need them in the highlight sequence.
- Internally uses `lz-string` to compress the diagram string and Slidev's built-in `<Mermaid :code-lz="...">` component for rendering.
