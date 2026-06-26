# Excel + AI Workshop

A Slidev-based workshop covering AI-assisted Excel automation via local Python pipelines.

---

## Slide Decks

| Deck | File | Audience |
|---|---|---|
| RD / Technical | `slides.md` | Engineers, technical reference |
| Participant Guide (EN) | `slides-workshop.md` | Workshop attendees, English |
| 學員手冊 (繁體中文) | `slides-workshop-zh.md` | Workshop attendees, Traditional Chinese |

---

## Released URLs

| URL | Description |
|---|---|
| https://chenghsienwen.github.io/excel-ai-workshop/ | RD slides |
| https://chenghsienwen.github.io/excel-ai-workshop/workshop/ | Participant Guide (EN) |
| https://chenghsienwen.github.io/excel-ai-workshop/workshop-zh/ | 學員手冊（繁體中文） |
| https://chenghsienwen.github.io/excel-ai-workshop/bm-viewer/ | BM Report Viewer demo |

---

## Local Development

### Install dependencies

```bash
pnpm install
```

### Run locally

```bash
# RD / technical slides
pnpm dev

# Participant Guide (English)
pnpm dev:workshop

# 學員手冊（繁體中文）
pnpm dev:workshop-zh
```

All decks are served at `http://localhost:3030`.

### Build

```bash
# RD slides
pnpm build

# Participant Guide (English)
pnpm build:workshop

# 學員手冊（繁體中文）
pnpm build:workshop-zh
```

---

## Exercise Repo

Hands-on exercise files for workshop participants:

```
https://reurl.cc/ovGlY5
```

---

## Deploy

All decks are deployed automatically to GitHub Pages on push to `main` when any of the slide files or shared assets change. See `.github/workflows/deploy-slides.yml`.
