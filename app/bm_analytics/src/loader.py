"""Load and validate the raw_report.csv input."""

import logging
import pathlib

import pandas as pd

from . import config

_REQUIRED_COLUMNS = set(config.INPUT_COLUMNS)

logger = logging.getLogger(__name__)


def load(path: pathlib.Path = config.INPUT_FILE) -> pd.DataFrame:
    """Load raw_report.csv and return a validated DataFrame.

    Args:
        path: Path to the input CSV file.

    Returns:
        DataFrame with validated schema and correct dtypes.

    Raises:
        ValueError: If required columns are missing.
    """
    df = pd.read_csv(path)

    missing = _REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Input CSV missing columns: {missing}")

    df["amount"] = df["amount"].fillna(0).astype("int64")
    df["year"] = df["year"].astype(str)

    logger.info("Loaded %d rows from %s", len(df), path)
    return df
