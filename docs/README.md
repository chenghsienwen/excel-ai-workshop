# Component Docs

Documentation for custom Slidev components in this project.

For a use-case-oriented adoption guide with usage snippets for every component, see [GUIDE.md](GUIDE.md).

## Components

| Component | Doc | Summary |
|---|---|---|
| `Accordion` | [Accordion.md](Accordion.md) | A collapsible section component for Slidev slides. Click the header to expand or collapse the content. Supports any slot content and starts open or closed via prop. |
| `ChatWindow` | [ChatWindow.md](ChatWindow.md) | Displays a mock ChatGPT-style conversation window with up to five Q&A turns, zoom controls, and automatic height clamping to the slide boundary. |
| `Counter` | [Counter.md](Counter.md) | An interactive increment/decrement counter with an optional starting value. |
| `CurrentDate` | [CurrentDate.md](CurrentDate.md) | Injects today's date (`YYYY.MM.DD`) into the cover slide at runtime, evaluated when the page loads. |
| `ExcelViewer` | [ExcelViewer.md](ExcelViewer.md) | Renders an `.xlsx` or `.csv` file inside a macOS-style window chrome with zoom, drag-to-pan, sheet tabs, and cell range highlight. |
| `FileTree` | [FileTree.md](FileTree.md) | Renders a static directory listing with a folder path header and a list of files, each decorated with a type-specific emoji icon. |
| `LastModifiedDate` | [LastModifiedDate.md](LastModifiedDate.md) | Injects a "Last updated: YYYY.MM.DD" label into the cover slide, sourced from the most recent git commit date at build time. |
| `MermaidHighlight` | [MermaidHighlight.md](MermaidHighlight.md) | Renders a Mermaid diagram and highlights one node per click in declaration order. Auto-detects node count to register click steps with Slidev. |
| `QrCode` | [QrCode.md](QrCode.md) | Renders a QR code for a given URL as an inline SVG, with configurable size and colours. |
| `QuestionForm` | [QuestionForm.md](QuestionForm.md) | Audience Q&A form. Persists entries to `localStorage` with a 5 MB ring-buffer cap. Supports download as `.txt`. Height clamps to the slide boundary. |
| `TextLoader` | [TextLoader.md](TextLoader.md) | Displays a plain-text or Markdown file inside a macOS-style terminal window with font-size zoom controls and automatic height clamping to the slide boundary. |
| `TocContainer` | [TocContainer.md](TocContainer.md) | Wraps `<Toc>` (or any content) in a height-clamped, vertically scrollable container that tracks the `.slidev-layout` ancestor size via `ResizeObserver`. |
| `TwoCols` | [TwoCols.md](TwoCols.md) | Lays out content in two equal-width dark cards side by side, with optional titles and an orange hover effect matching the project theme. |

## Layouts

| Layout | Doc | Summary |
|---|---|---|
| `cards` | [cards.md](cards.md) | A Slidev layout that renders a grid of themed cards, each supporting an image, title, text, bullet list, and tags. |
