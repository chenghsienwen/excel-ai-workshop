#!/usr/bin/env python3
"""Copy analytics outputs into input/ for the viewer."""
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
ANALYTICS = ROOT.parent / "bm_analytics"
INPUT = ROOT / "input"
INPUT.mkdir(exist_ok=True)

SOURCES = [
    (ANALYTICS / "input" / "raw_report.csv", INPUT / "raw_report.csv"),
    (ANALYTICS / "output" / "layer1_report.csv", INPUT / "layer1_report.csv"),
    (ANALYTICS / "output" / "layer2_report.csv", INPUT / "layer2_report.csv"),
    (ANALYTICS / "output" / "layer3_segmentation.csv", INPUT / "layer3_segmentation.csv"),
    (ANALYTICS / "output" / "layer3_timeseries.csv", INPUT / "layer3_timeseries.csv"),
]

for src, dst in SOURCES:
    if not src.exists():
        print(f"skip  {src.name}  (not found in bm_analytics)")
        continue
    if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
        print(f"ok    {src.name}  (up to date)")
        continue
    shutil.copy2(src, dst)
    print(f"copy  {src.name}")
