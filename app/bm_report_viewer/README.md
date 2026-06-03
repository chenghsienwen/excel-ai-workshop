# BM Report Viewer

Streamlit dashboard for visualising BM analytics layer reports.

## Setup

```bash
cd app/bm_report_viewer
python3 -m venv .venv
source .venv/bin/activate      # macOS / Linux
pip install -r requirements.txt
```

## Populate input data

**Option A — manual copy (primary):**
```bash
cp ../bm_analytics/input/raw_report.csv input/
cp ../bm_analytics/output/layer*.csv input/
```

**Option B — sync helper:**
```bash
python sync_input.py
```

## Run

```bash
streamlit run app.py
```

Opens at http://localhost:8501

## Pages

| Page | Source data | Charts |
|---|---|---|
| Period Summary | layer1_report.csv | Period grouped bar, total by region |
| KPI Metrics | layer2_report.csv | YTD gap, budget hit rate heatmap, YoY, breakeven |
| Segmentation | layer3_segmentation.csv | Revenue ranking, share treemap |
| Timeseries | layer3_timeseries.csv | Monthly line, MoM growth, seasonal heatmap |

## Sidebar filters

Year, Region, Product, Rev Op Type, and Sales Budget Type filters are global and
persist across all pages via `st.session_state`.
