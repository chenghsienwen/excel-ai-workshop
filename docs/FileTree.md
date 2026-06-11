# FileTree

Renders a static directory listing with a folder path header and a list of files, each decorated with a type-specific emoji icon.

---

## Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `path` | `string` | — | Directory path displayed as the folder header (e.g. `app/data`). The last segment is used as the visible folder name. |
| `files` | `string[]` | — | List of file names to display under the folder. |

---

## Features

### File Icons
Each file name is matched against its extension and assigned an emoji:

| Extension | Icon |
|---|---|
| `.xls`, `.xlsx` | 📊 |
| `.csv` | 📄 |
| `.json` | 📋 |
| anything else | 📄 |

### Layout
The folder row is bold and white. Child files are indented under a left border (`2px solid #555`), giving a visual tree branch. The component uses `display: inline-block` so it sizes to its content rather than stretching to full width.

---

## Usage

```md
<FileTree path="app/bm_report/raw_data" :files="[
  'CDE biz status_2024_v1.xlsx',
  'summary.csv',
  'config.json',
  'notes.txt',
]" />
```

---

## Styling

The component uses a fixed dark theme and is not configurable via props:

| Token | Value | Usage |
|---|---|---|
| Font | `monospace`, `1.15rem` | All text |
| Line height | `2` | Row spacing |
| Folder label colour | `#fff` | Folder path text |
| Path colour | `#a8b4c8` | Muted blue-grey for the path string |
| File name colour | `#d4d5da` | Light grey for file names |
| Tree branch | `2px solid #555` | Left border on the children container |
