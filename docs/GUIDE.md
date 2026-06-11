# Developer Guide — Custom Components & Layouts

This guide groups every custom component and layout by use-case and provides the minimal snippet needed to drop each one into a slide. For full prop/slot references, follow the linked doc.

---

## Quick-Reference

| Name | Kind | When to reach for it |
|---|---|---|
| [`cards`](#cards-layout) | layout | Grid of image+text cards on a slide |
| [`TwoCols`](#twocols) | component | Side-by-side comparison of any two blocks |
| [`ExcelViewer`](#excelviewer) | component | Show a live `.xlsx` / `.csv` file |
| [`TextLoader`](#textloader) | component | Render a raw text or Markdown file |
| [`FileTree`](#filetree) | component | Show a folder + file listing |
| [`MermaidHighlight`](#mermaidhighlight) | component | Step-through Mermaid diagram with click highlights |
| [`ChatWindow`](#chatwindow) | component | Mock ChatGPT conversation (up to 5 turns) |
| [`Accordion`](#accordion) | component | Collapsible section hiding detail until clicked |
| [`QuestionForm`](#questionform) | component | Live audience Q&A input with local persistence |
| [`Counter`](#counter) | component | Clickable +/− number widget |
| [`QrCode`](#qrcode) | component | QR code SVG from a URL |
| [`TocContainer`](#toccontainer) | component | Height-safe wrapper for `<Toc>` |
| [`CurrentDate`](#currentdate) | component | Today's date on the cover slide (runtime) |
| [`LastModifiedDate`](#lastmodifieddate) | component | Last git commit date on the cover slide (build-time) |

---

## Layouts

### `cards` layout

**Use when** you want a visual grid of cards on a slide — feature overviews, step lists, team bios, before/after comparisons.

Data is declared in YAML frontmatter, so the slide body stays clean. `cols` and `fill` control the grid shape.

```md
---
layout: cards
cols: 3
cards:
  - image: /images/step1.png
    title: Import
    text: Load your .xlsx file.
  - title: Analyse
    items:
      - Pivot by category
      - Filter by date
    tags:
      - excel
  - title: Share
    text: Export or publish to the web.
---

# Three Steps
Follow along in today's workshop.
```

**Key props** — `cards` (array), `cols` (number), `fill` (boolean, stretch columns to full width), `background` (image path or CSS value).  
Full reference: [cards.md](cards.md)

---

## Layout Components

### `TwoCols`

**Use when** you need a left / right comparison inside any slide layout.

```md
<TwoCols left-title="Before" right-title="After">
  <template #left>
    Manual copy-paste every day.
  </template>
  <template #right>
    Automated report in 30 seconds.
  </template>
</TwoCols>
```

Both `leftTitle` and `rightTitle` are optional — omit them for an untitled two-panel layout.  
Full reference: [TwoCols.md](TwoCols.md)

---

## Data Display

### `ExcelViewer`

**Use when** you want to show the actual contents of a spreadsheet — not a screenshot.

Supports zoom (30–300%), drag-to-pan, sheet tabs, and click-drag cell range highlight.

```md
<ExcelViewer path="/app/bm_report/raw_data/report.xlsx" />

<!-- Start on sheet 2, 130% zoom -->
<ExcelViewer path="/app/data/sales.xlsx" :sheet="1" :default-zoom="1.3" />
```

Files under `app/` are bundled at build time; files under `public/` are fetched at runtime.  
Full reference: [ExcelViewer.md](ExcelViewer.md)

---

### `TextLoader`

**Use when** you want to display the raw content of a `.md` or `.txt` file inside a terminal-style window — useful for showing config files, reports, or code snippets from disk without copy-pasting.

```md
<TextLoader path="/app/bm_report/README.md" />

<!-- Larger initial font -->
<TextLoader path="/app/config.txt" :default-font-size="0.85" />
```

Font size is adjustable at runtime via **A−** / **A+** buttons. Height clamps automatically to the slide.  
Full reference: [TextLoader.md](TextLoader.md)

---

### `FileTree`

**Use when** you want to orient the audience to a project's folder structure without leaving the slide.

```md
<FileTree path="app/bm_report/raw_data" :files="[
  'CDE biz status_2024_v1.xlsx',
  'summary.csv',
  'config.json',
]" />
```

Icons are assigned automatically by extension (`.xlsx`/`.xls` → 📊, `.csv` / others → 📄, `.json` → 📋).  
Full reference: [FileTree.md](FileTree.md)

---

## Diagrams & Visuals

### `MermaidHighlight`

**Use when** you want to walk through a diagram one node at a time using Slidev click steps.

```md
<MermaidHighlight>
flowchart LR
  A[Raw Data] --> B[Pivot Table] --> C[Chart]
</MermaidHighlight>
```

Each presenter click highlights the next node in declaration order. The component auto-counts nodes and registers the correct number of click steps.  
Full reference: [MermaidHighlight.md](MermaidHighlight.md)

---

### `QrCode`

**Use when** you want the audience to scan a URL directly from the slide.

```md
<QrCode url="https://example.com" />

<!-- Dark-slide friendly -->
<QrCode url="https://example.com" :size="180" light="#171717" dark="#ececec" />
```

Rendered as a crisp inline SVG — no external service, no network request.  
Full reference: [QrCode.md](QrCode.md)

---

## Interaction

### `ChatWindow`

**Use when** you want to show a scripted AI conversation — useful for demonstrating prompt engineering, AI output examples, or Q&A scenarios.

Supports up to 5 turns. Add pairs of `#questionN` / `#responseN` named slots to extend the conversation.

```md
<ChatWindow class="text-left mt-6">
  <template #question>
    Summarise this Excel sheet in one sentence.
  </template>
  <template #response>
    The sheet tracks monthly sales by region across
    <b>12 product categories</b> for FY2024.
  </template>

  <template #question2>
    Which region had the highest growth?
  </template>
  <template #response2>
    <b>APAC</b> grew <code>+34%</code> YoY, outpacing all other regions.
  </template>
</ChatWindow>
```

Full reference: [ChatWindow.md](ChatWindow.md)

---

### `Accordion`

**Use when** you want to hide supplementary detail (e.g. an explanation, a caveat, a long list) behind a click, keeping the slide uncluttered.

```md
<Accordion title="Why does this formula work?">
  `XLOOKUP` scans the lookup array and returns the corresponding value
  from the return array — no need to know column indices.
</Accordion>

<!-- Start open -->
<Accordion title="Prerequisites" :open="true">
  - Excel 2021 or Microsoft 365
  - The sample file from the repo
</Accordion>
```

Full reference: [Accordion.md](Accordion.md)

---

### `QuestionForm`

**Use when** you want to collect live questions from the audience during a presentation. Entries persist in `localStorage` so nothing is lost on refresh, and the audience can download a `.txt` copy.

```md
<QuestionForm />
```

No configuration needed. Height clamps to the slide boundary automatically.  
Full reference: [QuestionForm.md](QuestionForm.md)

---

### `Counter`

**Use when** you need a simple interactive counter on a slide — useful for live tallies or audience participation demos.

```md
<Counter />           <!-- starts at 0 -->
<Counter :count="5" /> <!-- starts at 5 -->
```

Full reference: [Counter.md](Counter.md)

---

## Slide Utilities

### `TocContainer`

**Use when** the built-in `<Toc>` overflows the slide. Wrap it to get automatic height clamping and a scrollbar.

```md
<TocContainer>
  <Toc :max-depth="2" />
</TocContainer>
```

Full reference: [TocContainer.md](TocContainer.md)

---

### `CurrentDate`

**Use when** you want today's date shown on the cover slide at presentation time (reflects the viewer's local clock).

```md
---
layout: cover
---

# My Presentation
<CurrentDate />
```

Teleports into `.slidev-layout.cover` — invisible on non-cover slides.  
Full reference: [CurrentDate.md](CurrentDate.md)

---

### `LastModifiedDate`

**Use when** you want to show the last git commit date (build-time) on the cover slide rather than today's runtime date.

```md
---
layout: cover
---

# My Presentation
<LastModifiedDate />
```

Value is fixed at build time via `vite.config.ts` (`git log -1 --format="%cd"`). Use `CurrentDate` instead if you want a live clock.  
Full reference: [LastModifiedDate.md](LastModifiedDate.md)
