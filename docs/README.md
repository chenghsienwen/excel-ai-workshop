# Component Docs

Documentation for custom Slidev components in this project.

## Components

| Component | Doc | Summary |
|---|---|---|
| `MermaidHighlight` | [MermaidHighlight.md](MermaidHighlight.md) | Renders a Mermaid diagram and highlights one node per click in declaration order. Auto-detects node count to register click steps with Slidev. |
| `QuestionForm` | [QuestionForm.md](QuestionForm.md) | Audience Q&A form. Persists entries to `localStorage` with a 5 MB ring-buffer cap. Supports download as `.txt`. Height clamps to the slide boundary. |
| `TocContainer` | — | Wraps `<Toc>` in a height-clamped, Y-scrollable container. Uses ResizeObserver so `max-height` tracks the `.slidev-layout` ancestor reliably. |
