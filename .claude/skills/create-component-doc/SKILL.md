---
name: create-component-doc
description: Create a docs/xxx.md for a xxx component — reads the component source, generates a user guide, and registers it in docs/README.md.
metadata:
  author: simon.ch.wen
  version: "1.0"
---

Generate a user-guide markdown file under `docs/` for a component in `components/`, then register it in `docs/README.md`.

---

## Step 1 — Ask the user which component to document

Ask in one message:

> **Creating a component doc — which component?**
>
> Name the component (e.g. `ChatWindow`, `FileTree`, `Counter`).
> Leave blank to list all undocumented components and let you pick.

If the user leaves it blank, list every `.vue` file under `components/` that does **not** already have a matching `.md` in `docs/`, then ask again.

Wait for the user to name a single component before continuing.

---

## Step 2 — Read the component source

Read `components/<ComponentName>.vue` in full.

Also check whether `docs/<ComponentName>.md` already exists — if it does, tell the user it already exists and ask if they want to **overwrite** it. Proceed only if they confirm.

---

## Step 3 — Generate the doc content

Write a doc that mirrors the style of the existing docs (see `docs/ExcelViewer.md` as the canonical reference).

Required sections (skip any that genuinely do not apply):

1. **`# ComponentName`** — one-sentence summary of what the component does.
2. **`## Props`** — table with columns `Prop | Type | Default | Description`. Derive from `defineProps` / `withDefaults`.
3. **`## Slots`** — table with columns `Slot | Description`. Derive from `<slot>` elements or `useSlots()`.
4. **`## Features`** — one subsection (`###`) per notable runtime behaviour (e.g. zoom, scroll-clamping, click interactions).
5. **`## Usage`** — fenced `md` code block(s) showing minimal and illustrative in-slide usage.
6. Optional extra sections (`## Notes`, `## Styling`, `## File Resolution`, etc.) only when meaningful content exists.

Rules:
- Use `---` horizontal rules between top-level sections (matching `ExcelViewer.md` style).
- Keep descriptions factual and terse — no marketing language.
- Derive every claim from the source code read in Step 2.

---

## Step 4 — Write the doc file

Write the generated content to `docs/<ComponentName>.md`.

---

## Step 5 — Update docs/README.md

Read `docs/README.md`.

In the `## Components` table, add a new row for this component (alphabetical order by component name):

```
| `ComponentName` | [ComponentName.md](ComponentName.md) | <one-line summary> |
```

Use the same one-sentence summary from the `# ComponentName` heading in the doc.

If a row for this component already exists (e.g. it had a `—` placeholder), replace that row instead of adding a duplicate.

---

## Step 6 — Confirm

Reply with a one-line summary:

> Doc created: **`docs/<ComponentName>.md`** — `docs/README.md` updated.
