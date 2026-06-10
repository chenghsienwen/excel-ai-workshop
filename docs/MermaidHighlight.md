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

## Notes

- Works with any Mermaid diagram type (`flowchart`, `graph`, `sequenceDiagram`, etc.) as long as node IDs follow the `ID[shape]` / `ID(shape)` / `ID{shape}` syntax.
- Node parsing uses a regex on declaration order. Nodes referenced only as edge targets (without a shape bracket) are not picked up — declare all nodes explicitly if you need them in the highlight sequence.
- Internally uses `lz-string` to compress the diagram and Slidev's built-in `<Mermaid>` component for rendering.
- Click step registration: the component injects `$$slidev-clicks-context` and calls `ctx.register()` on mount so Slidev knows this slide has N click steps. Without this, `clicksTotal` would be 0 and ArrowRight would skip the slide entirely.
