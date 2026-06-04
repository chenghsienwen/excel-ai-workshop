#!/usr/bin/env python3
"""
Build a self-contained stlite (Streamlit-in-browser) static site.

CSV data is base64-encoded in the JS layer and decoded into the stlite virtual
filesystem before mount — raw rows are not visible as plain text in page source.

Usage:
    python build.py            # outputs dist/index.html
    python build.py --open     # generates + opens in browser
"""

import argparse
import base64
import json
import webbrowser
from pathlib import Path

STLITE_VERSION = "1.8.0"

APP_DIR = Path(__file__).parent
DIST_DIR = APP_DIR / "dist"

PY_FILES = [
    "app.py",
    "pages/1_Period_Summary.py",
    "pages/2_KPI_Metrics.py",
    "pages/3_Segmentation.py",
    "pages/4_Timeseries.py",
    "src/__init__.py",
    "src/loader.py",
    "src/sidebar.py",
    "src/charts/__init__.py",
    "src/charts/layer1.py",
    "src/charts/layer2.py",
    "src/charts/layer3_seg.py",
    "src/charts/layer3_ts.py",
]

DATA_FILES = [
    "input/raw_report.csv",
    "input/layer1_report.csv",
    "input/layer2_report.csv",
    "input/layer3_segmentation.csv",
    "input/layer3_timeseries.csv",
]


def build():
    missing = [f for f in PY_FILES + DATA_FILES if not (APP_DIR / f).exists()]
    if missing:
        raise FileNotFoundError("Missing files:\n" + "\n".join(f"  {f}" for f in missing))

    py_files = {
        path: (APP_DIR / path).read_text(encoding="utf-8")
        for path in PY_FILES
    }

    # CSV content stored as base64 — decoded in JS before stlite mounts,
    # so raw rows don't appear as plain text anywhere in page source.
    data_b64 = {
        path: base64.b64encode((APP_DIR / path).read_bytes()).decode("ascii")
        for path in DATA_FILES
    }

    py_files_json = json.dumps(py_files, ensure_ascii=False, indent=2)
    data_b64_json = json.dumps(data_b64, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <title>BM Report Viewer</title>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/@stlite/browser@{STLITE_VERSION}/build/stlite.css"
  />
</head>
<body>
  <div id="root"></div>
  <script type="module">
    import {{ mount }} from "https://cdn.jsdelivr.net/npm/@stlite/browser@{STLITE_VERSION}/build/stlite.js";

    const pyFiles = {py_files_json};

    // Decode CSV data from base64 and merge into the files map.
    const dataB64 = {data_b64_json};
    const dataFiles = Object.fromEntries(
      Object.entries(dataB64).map(([path, b64]) => [
        path,
        new TextDecoder().decode(Uint8Array.from(atob(b64), c => c.charCodeAt(0)))
      ])
    );

    mount(
      {{
        requirements: ["plotly", "pandas"],
        entrypoint: "app.py",
        files: {{ ...pyFiles, ...dataFiles }}
      }},
      document.getElementById("root")
    );
  </script>
</body>
</html>"""

    DIST_DIR.mkdir(exist_ok=True)
    out = DIST_DIR / "index.html"
    out.write_text(html, encoding="utf-8")
    size_kb = out.stat().st_size // 1024
    print(f"Built {out.relative_to(APP_DIR)}  ({size_kb} KB)")
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--open", action="store_true", help="Open result in browser")
    args = parser.parse_args()

    out = build()
    if args.open:
        webbrowser.open(out.as_uri())
