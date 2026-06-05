---
name: add-chat-window-slide
description: Add a new ChatWindow slide to slides.md — asks for injection point, slide title, and prompt question, then generates the AI response and inserts the slide.
metadata:
  author: simon.ch.wen
  version: "1.0"
---

Insert a new slide into `slides.md` that contains a heading and a `<ChatWindow>` component showing a question and an AI-generated response.

---

## Step 1 — Ask the user three questions in one message

Ask all three questions together:

> **Adding a ChatWindow slide — a few quick questions:**
>
> **Q1. Where should the slide be inserted?**
> Give a page number (e.g. `3`) or a heading to insert after (e.g. `# Who am I`).
>
> **Q2. What is the slide title?**
> This becomes the `# Heading` at the top of the slide.
>
> **Q3. What is the prompt/question to show in the chat window?**
> Write the user-side question exactly as it should appear. Claude will generate the AI response.

Wait for the user to answer all three before continuing.

---

## Step 2 — Generate the AI response for Q3

Take the Q3 prompt question and answer it yourself as the current AI model.
The response should be concise (2–4 sentences), technical, and directly address the question.
It may include inline `<code>` tags and `<b>` tags for emphasis, matching the style of the example below.

---

## Step 3 — Find the insertion point in slides.md

Read `slides.md` to locate the correct position:

- **If Q1 is a number N**: count slide separators (`---` on their own line) to find the Nth slide boundary, and insert the new slide block after it.
- **If Q1 is a heading string** (e.g. `# Who am I`): find the line containing that heading, then scan forward to the next `---` slide separator — insert the new slide block after that `---`.

---

## Step 4 — Build the slide block

Construct the block using the answers:

```
# <Q2 title>

<ChatWindow class="text-left mt-6">
  <template #question>
    <Q3 question — may use <code> and <b> tags>
  </template>
  
  <template #response>
    <AI-generated response — may use <code> and <b> tags>
  </template>
</ChatWindow>

---
```

Rules:
- The `# <title>` line is plain text (no HTML tags).
- Preserve the blank line between `# title` and `<ChatWindow>`.
- The closing `---` is the slide separator for the slide that follows.
- Do not add a leading `---` before `# <title>` — the preceding slide already ends with one.
- To append additional Q&A turns to an **existing** ChatWindow (rather than creating a new slide), add `#question2`/`#response2` slots inside the same `<ChatWindow>` block. The component renders them only when the slots are present.

---

## Step 5 — Insert into slides.md

Use the Edit tool to insert the block at the located position.

Confirm to the user with a one-line summary:
> Slide "**\<title\>**" inserted after \<location description\>.
