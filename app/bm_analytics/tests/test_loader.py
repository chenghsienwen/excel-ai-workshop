"""Tests for src/loader.py."""

import pathlib
import tempfile
import unittest

import pandas as pd

from src import loader

_FIXTURE = (
    pathlib.Path(__file__).parent / "fixtures" / "raw_report_fixture.csv"
)


class TestLoader(unittest.TestCase):
    def test_happy_path(self):
        df = loader.load(_FIXTURE)
        expected_cols = {
            "product", "year", "region", "rev_op_type",
            "sales_budget_type", "month", "amount",
        }
        self.assertEqual(set(df.columns), expected_cols)
        self.assertEqual(len(df), 288)

    def test_missing_column(self):
        df = pd.read_csv(_FIXTURE).drop(columns=["amount"])
        with tempfile.NamedTemporaryFile(
            suffix=".csv", mode="w", delete=False
        ) as fh:
            df.to_csv(fh.name, index=False)
            tmp = pathlib.Path(fh.name)
        with self.assertRaises(ValueError):
            loader.load(tmp)
        tmp.unlink()

    def test_amount_cast(self):
        df = loader.load(_FIXTURE)
        self.assertEqual(df["amount"].dtype.name, "int64")

    def test_year_cast(self):
        df = loader.load(_FIXTURE)
        self.assertEqual(df["year"].dtype.name, "object")


if __name__ == "__main__":
    unittest.main()
