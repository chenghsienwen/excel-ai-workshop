---
name: upsert-chat-window-slide
description: Create a new ChatWindow slide OR append a new Q&A turn to an existing ChatWindow on the target page — asks for target page, title (new only), and prompt question, then generates the AI response and upserts.
metadata:
  author: simon.ch.wen
  version: "1.0"
---

Insert a new `<ChatWindow>` slide **or** append a new Q&A turn to an existing one, depending on whether the target page already contains a `<ChatWindow>` component.

---

## Step 1 — Ask the user three questions in one message

> **Upserting a ChatWindow slide — a few quick questions:**
>
> **Q1. Which page should be targeted?**
> Give a page number (e.g. `3`) or a heading to match (e.g. `# Prompt: how to do excel automation?`).
>
> **Q2. What is the slide title?**
> Only used when creating a new slide. If the target page already has a `<ChatWindow>`, this is ignored.
>
> **Q3. What is the prompt/question to show in the chat window?**
> Write the user-side question exactly as it should appear. Claude will generate the AI response.

Wait for all three answers before continuing.

---

## Step 2 — Generate the AI response for Q3

Answer Q3 yourself as the current AI model.
Keep it concise (2–4 sentences), technical, and direct.
You may use inline `<code>` and `<b>` tags for emphasis.

---

## Step 3 — Locate the target page in slides.md

Read `slides.md`.

**Finding the page:**
- If Q1 is a number N: count slide separators (`---` on their own line) to locate the Nth slide block.
- If Q1 is a heading string: find the line containing that heading text, then identify the slide block it belongs to.

**Checking for an existing ChatWindow:**
Scan the identified slide block (from its opening `---` to the next `---`) for a `<ChatWindow` tag.

---

## Step 4 — Decide: INSERT or APPEND

### Case A — No `<ChatWindow>` on the target page → INSERT a new slide

Build and insert the following block **after the closing `---`** of the target slide:

```
# <Q2 title>

<ChatWindow class="text-left mt-6">
  <template #question>
    <Q3 question>
  </template>
  
  <template #response>
    <AI-generated response>
  </template>
</ChatWindow>

---
```

Rules:
- `# <title>` is plain text.
- Blank line between the heading and `<ChatWindow>`.
- The closing `---` is the separator for the following slide.
- Do **not** add a leading `---` — the preceding slide already ends with one.

---

### Case B — `<ChatWindow>` already exists on the target page → APPEND a new turn

Count the existing named turn slots inside the `<ChatWindow>` block:
- Find `<template #question>` → that is turn 1.
- Find `<template #question2>` → that is turn 2.
- Continue up to `#question5`.

The next turn number N = (highest existing turn) + 1.

Insert the following two templates **immediately before** the closing `</ChatWindow>` tag:

```
  <template #questionN>
    <Q3 question>
  </template>

  <template #responseN>
    <AI-generated response>
  </template>
```

Where `N` is the next turn number. Use `#question` / `#response` for turn 1 (no suffix), `#question2` / `#response2` for turn 2, etc.

---

## Step 5 — Apply the edit

Use the Edit tool to make the change in `slides.md`.

Confirm to the user in one line:
- **INSERT**: `Slide "<title>" inserted after <location>.`
- **APPEND**: `Turn N appended to the ChatWindow on page <location>.`

---

## Slot naming reference

| Turn | Question slot   | Response slot   |
|------|-----------------|-----------------|
| 1    | `#question`     | `#response`     |
| 2    | `#question2`    | `#response2`    |
| 3    | `#question3`    | `#response3`    |
| 4    | `#question4`    | `#response4`    |
| 5    | `#question5`    | `#response5`    |

The `ChatWindow` component supports up to 5 turns. Beyond that, create a new slide instead.
