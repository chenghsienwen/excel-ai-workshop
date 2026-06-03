import streamlit as st
import pandas as pd
from pathlib import Path

INPUT_DIR = Path(__file__).parent.parent / "input"

_FILES = {
    "raw": "raw_report.csv",
    "layer1": "layer1_report.csv",
    "layer2": "layer2_report.csv",
    "layer3_seg": "layer3_segmentation.csv",
    "layer3_ts": "layer3_timeseries.csv",
}


@st.cache_data
def load_all() -> dict[str, pd.DataFrame]:
    missing = [fname for fname in _FILES.values() if not (INPUT_DIR / fname).exists()]
    if missing:
        raise FileNotFoundError(
            f"Missing files in input/: {', '.join(missing)}\n"
            "Copy CSVs to input/ or run: python sync_input.py"
        )
    return {key: pd.read_csv(INPUT_DIR / fname) for key, fname in _FILES.items()}


def load_all_safe() -> tuple[dict | None, str | None]:
    try:
        return load_all(), None
    except FileNotFoundError as e:
        return None, str(e)
