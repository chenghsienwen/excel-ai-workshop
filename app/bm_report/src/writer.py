"""Writes the final consolidated DataFrame to a CSV file."""

import logging
import pathlib

import pandas as pd

_logger = logging.getLogger(__name__)


def write_report(df: pd.DataFrame, path: pathlib.Path) -> None:
    """Writes ``df`` to a UTF-8 CSV at ``path``.

    Creates parent directories if they do not already exist.

    Args:
        df: Final DataFrame to serialise.
        path: Destination file path (must end in ``.csv``).
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8")
    _logger.info("Wrote %d rows → %s", len(df), path)
