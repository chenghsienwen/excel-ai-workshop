# QuestionForm

A Slidev component that lets audience members type questions during a presentation. Entries are persisted to `localStorage` and can be exported as a plain-text file.

## Props

None. The component is self-contained.

## Features

| Feature | Detail |
|---|---|
| Input | Textarea, max 300 characters per entry |
| Keyboard shortcut | `Ctrl+Enter` / `Cmd+Enter` to submit |
| Timestamp | Each entry is prefixed `YYYY/MM/DD hh:mm:ss \|` |
| Storage | `localStorage` key `slidev-question-log` |
| Size cap | 5 MB — oldest lines are dropped when the log exceeds the limit |
| Log display | Entries shown newest-first in a scrollable block |
| Download | Exports the full log as `questions.txt` |
| Clear | Removes all entries from storage and the view |
| Height | Log block clamps to available slide height via `ResizeObserver` (same technique as `TextLoader`) |

## Usage

```md
<QuestionForm />

<!-- with extra top margin -->
<QuestionForm class="mt-4" />
```

## Entry format

Each line in the log and the downloaded file follows this format:

```
YYYY/MM/DD hh:mm:ss | <text up to 300 chars>
```

Example:

```
2026/06/10 14:32:07 | How does the AI pipeline handle missing values in the Excel files?
```

## Storage behaviour

- Entries persist across **page reloads** in the same browser on the same machine.
- Each new entry is appended; if the total log exceeds 5 MB the oldest lines are removed until it fits.
- **Download** is the only way to get a portable copy outside the browser.

## Limitations

| Limitation | Detail |
|---|---|
| Client-side only | No server, no shared storage — each browser holds its own independent log |
| Not shared across devices | Different browsers or machines see nothing of each other's entries |
| Incognito / private mode | `localStorage` is cleared when the private session ends |
| Browser data clear | Wiping browser data removes all entries permanently |
| No real-time sync | If you need audience submissions visible to the presenter from remote devices, a backend (e.g. WebSocket server or Supabase) is required |

## Multi-device / shared use case

When the slides are deployed to GitHub Pages and two browsers open the same URL, each browser writes to its **own isolated `localStorage`** — the entries are invisible to each other. There is no cross-device synchronisation in the current implementation.

To support a shared Q&A where all submissions are visible to everyone (or at least to the presenter), a lightweight backend is required. The simplest options for a GitHub Pages deployment:

| Option | Notes |
|---|---|
| **Supabase Realtime** | Free tier; Postgres + WebSocket broadcast; add a few API calls to the component, no server to host |
| **Firebase Realtime Database** | Similar free tier; JSON synced over WebSocket |
| **Custom WebSocket server** | ~30-line Node.js server with `ws`; requires a VPS to host |

This would require a `shared` mode to be added to the component that replaces `localStorage` reads/writes with real-time database calls.

## Height clamping

The log block measures its own `offsetTop` relative to the nearest `.slidev-layout` ancestor and sets `max-height` to the remaining available space (with 16 px bottom clearance). A `ResizeObserver` keeps this value correct if the slide is resized or the presentation is zoomed.
