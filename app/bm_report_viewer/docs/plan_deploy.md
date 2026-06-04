# BM Report Viewer — Static Deployment Plan

## Goal

Deploy the Streamlit dashboard as a fully interactive static web page on GitHub Pages —
no server required. All Python logic, charts, and CSV data are bundled into a single
`dist/index.html` that runs entirely in the visitor's browser.

---

## Mechanism: stlite (Streamlit in WebAssembly)

**stlite** ports Streamlit to run inside the browser via
[Pyodide](https://pyodide.org) (CPython compiled to WebAssembly).

```
Browser
 └─ index.html
     ├─ stlite.js   (loads Pyodide + Streamlit runtime from CDN)
     ├─ stlite.css
     └─ inline JS   (mounts virtual filesystem + entrypoint config)
         ├─ app.py  (embedded as text)
         ├─ pages/  (embedded as text)
         ├─ src/    (embedded as text)
         └─ input/  (CSV data embedded as text)
```

- **No Python server needed** — Streamlit runs in a Pyodide WASM thread
- **No backend calls** — pandas, plotly, all deps downloaded from PyPI by Pyodide at load time
- **Fully interactive** — sidebar filters, charts, multipage navigation all work
- **One file** — everything bundled into `dist/index.html`

> Note: first load is slow (~10–20 s) while Pyodide bootstraps and pulls packages.
> Subsequent visits are fast due to browser/CDN caching.

---

## What Gets Built

### `build.py` (new)

A pure-stdlib Python script placed at `app/bm_report_viewer/build.py`.

**What it does:**
1. Reads every `.py` source file (listed explicitly)
2. Reads all 5 CSV files from `input/`
3. Serialises them as a JSON `files` object
4. Injects into an HTML template that calls `stlite.mount()`
5. Writes `dist/index.html`

```
Input (read from disk)          Output
──────────────────────────      ─────────────
app.py                    ──┐
pages/*.py                  │
src/**/*.py                 ├─► dist/index.html  (~500–800 KB)
src/charts/**/*.py          │
input/*.csv               ──┘
```

Run locally:
```bash
cd app/bm_report_viewer
python build.py          # generates dist/index.html
python build.py --open   # generates + opens in browser
```

---

### `.github/workflows/deploy-bm-viewer.yml` (new)

GitHub Actions workflow that:
1. Checks out the repo
2. Runs `build.py` (no pip install needed — stdlib only)
3. Uploads `dist/` as a GitHub Pages artifact
4. Deploys to GitHub Pages

---

## Trigger Conditions

| Event | Behaviour |
|---|---|
| Push to `main` touching `app/bm_report_viewer/**` | Auto-build and deploy |
| Push to `main` touching `.github/workflows/deploy-bm-viewer.yml` | Auto-build and deploy |
| **Workflow Dispatch** (manual) | Trigger build from GitHub UI → Actions tab → Run workflow |

Manual trigger is useful when you update only the CSV data locally and push,
or when you want to force a redeploy without a code change.

---

## GitHub Pages Setup (one-time, manual)

Before the first deploy, enable GitHub Pages in the repo:

1. Go to **Settings → Pages**
2. Set **Source** to **GitHub Actions** (not a branch)
3. Save

The workflow uses the official `actions/deploy-pages@v4` action which handles
branch/artifact management automatically.

---

## File Plan

```
app/bm_report_viewer/
├── build.py                     ← NEW: build script
├── dist/                        ← NEW: generated output (gitignored)
│   └── index.html
└── docs/
    └── plan_deploy.md           ← this file

.github/
└── workflows/
    └── deploy-bm-viewer.yml     ← NEW: CI/CD workflow
```

Add `dist/` to `.gitignore` — it is generated on CI and published via artifact,
not committed to the branch.

---

## stlite Virtual Filesystem

stlite maps the `files` keys directly onto a virtual POSIX filesystem with
`/work/` as the working directory. The app runs as if `app.py` is at `/work/app.py`.

| Virtual path | Source |
|---|---|
| `/work/app.py` | `app.py` |
| `/work/pages/1_Period_Summary.py` | `pages/1_Period_Summary.py` |
| `/work/src/loader.py` | `src/loader.py` |
| `/work/input/layer1_report.csv` | `input/layer1_report.csv` |
| … | … |

`src/loader.py` resolves CSV paths as:
```python
INPUT_DIR = Path(__file__).parent.parent / "input"
# → /work/src/../input → /work/input   ✓
```
This works as-is — no code changes needed.

---

## Dependency Loading

stlite pulls Python packages at runtime via Pyodide's micropip.
The `requirements` array in `stlite.mount()` controls what is installed:

```javascript
requirements: ["plotly", "pandas"]
```

`streamlit` itself is bundled in stlite and does not need to be listed.

---

## Updating the Live Site

To update data:
1. Run `bm_analytics` pipeline → new CSVs land in `input/`
2. `git add input/ && git commit && git push`  (after removing `input/` from .gitignore, OR)
3. Push triggers the workflow → `build.py` re-embeds the latest CSVs → redeploy

Alternatively, keep `input/` gitignored and trigger a **manual workflow dispatch**
after copying fresh CSVs to the runner — but that requires the workflow to source
data from somewhere (e.g., a GitHub release asset or LFS). The simpler path is to
commit the CSVs for the published version (they are small).

---

## Data Protection: `data` Branch + Base64 Obfuscation

### Problem

Two concerns with the original design:

| Concern | Root cause |
|---|---|
| CI build fails | `input/` is gitignored → `actions/checkout` gives CI an empty directory → `build.py` aborts |
| Raw CSV readable in page source | CSV rows embedded as plain JSON strings in `index.html` → anyone can View Source and copy the data |

GitHub Actions Secrets cannot be used here because the total CSV size is ~1.8 MB,
well above the 64 KB per-secret limit.

---

### Solution 1 — `data` Orphan Branch (CI access to CSVs)

An **orphan branch** named `data` holds only the CSV files. It has no shared
history with `main` and never appears in the main commit log.

```
main branch   →  source code only  (no input/ data)
data branch   →  app/bm_report_viewer/input/*.csv only
```

**One-time setup:**

```bash
git checkout --orphan data
git rm -rf .
mkdir -p app/bm_report_viewer/input
cp /path/to/output/*.csv app/bm_report_viewer/input/
git add app/bm_report_viewer/input/
git commit -m "data: initial CSV files"
git push origin data
git checkout main
```

**How the workflow uses it:**

```yaml
- name: Checkout main (source)
  uses: actions/checkout@v4
  with:
    ref: main

- name: Fetch CSV data from data branch
  run: |
    git fetch origin data
    git checkout origin/data -- app/bm_report_viewer/input/
```

The runner starts with `main` checked out, then overlays only the `input/` directory
from the `data` branch. `build.py` then runs with all files present.

**Updating data (no code change needed):**

```bash
git checkout data
cp /new/output/*.csv app/bm_report_viewer/input/
git add app/bm_report_viewer/input/
git commit -m "data: refresh CSVs YYYY-MM-DD"
git push origin data    # triggers workflow → redeploy automatically
git checkout main
```

**Trigger matrix:**

| Push to | Effect |
|---|---|
| `main` | Rebuilds with latest code + current `data` branch CSVs |
| `data` | Rebuilds with current `main` code + new CSVs |
| Manual dispatch | Force rebuild on demand |

---

### Solution 2 — Base64 Obfuscation in HTML

`build.py` separates CSV data from Python source in the generated HTML:

```
index.html
├── pyFiles  (JSON)   — Python source, plain text
└── dataB64  (JSON)   — CSV content, base64-encoded
```

The JS layer decodes `dataB64` into the stlite virtual filesystem before mount:

```javascript
const dataFiles = Object.fromEntries(
  Object.entries(dataB64).map(([path, b64]) => [
    path,
    new TextDecoder().decode(Uint8Array.from(atob(b64), c => c.charCodeAt(0)))
  ])
);

stlite.mount({ ..., files: { ...pyFiles, ...dataFiles } }, element);
```

**Effect:** raw CSV rows (`region,product,year,...`) never appear as plain text
anywhere in the HTML source. A viewer sees only base64 blobs like:

```
"input/layer1_report.csv": "cmVnaW9uLHByb2R1Y3QseWVhci..."
```

Encoded sizes (base64 is ~33% larger than binary):

| File | Raw | Base64 |
|---|---|---|
| `raw_report.csv` | 575 KB | 784 KB |
| `layer3_timeseries.csv` | 884 KB | 1,207 KB |
| others | ~300 KB total | ~420 KB total |
| **Total HTML** | — | **~2.4 MB** |

> Note: this is obfuscation, not encryption. A determined viewer can still decode
> the base64 in browser DevTools. For stronger protection, host the app on a
> server with authentication instead of a public static site.

---

## Known Limitations

| Limitation | Detail |
|---|---|
| First-load latency | ~10–20 s to download Pyodide + packages (~30 MB) |
| No server-side logic | All computation runs in-browser; fine for this app |
| No file upload/write | `st.file_uploader` works; writing to disk does not persist |
| CDN dependency | stlite JS/CSS loaded from jsDelivr; offline use requires local hosting |
| Browser support | Modern Chromium/Firefox; Safari 15.2+; no IE |
