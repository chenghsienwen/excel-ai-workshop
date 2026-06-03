"""Tests for src/layer2.py."""

import datetime
import pathlib
import unittest

import pandas as pd

from src import layer1, layer2, loader

_FIXTURE = (
    pathlib.Path(__file__).parent / "fixtures" / "raw_report_fixture.csv"
)

_TODAY = datetime.date(2025, 6, 15)


class TestLayer2(unittest.TestCase):
    def setUp(self):
        self.raw = loader.load(_FIXTURE)
        l1 = layer1.build(self.raw, today=_TODAY)
        self.result = layer2.build(l1, self.raw)

    def _row(self, region, product, year, rev_op, sbt):
        return self.result[
            (self.result["region"] == region)
            & (self.result["product"] == product)
            & (self.result["year"] == str(year))
            & (self.result["rev_op_type"] == rev_op)
            & (self.result["sales_budget_type"] == sbt)
        ].iloc[0]

    def test_output_columns(self):
        self.assertEqual(list(self.result.columns), layer2.LAYER2_COLUMNS)

    def test_ytd_gap_actual_minus_budget(self):
        # R1, CDE, 2024, Gross, Actual: ytd(Actual)=1200 - ytd(Budget)=600 = 600
        # today=Jun → ytd = Jan-Jun = 6 months; Actual=200/mo, Budget=100/mo
        row = self._row("R1", "CDE", "2024", "Gross", "Actual")
        self.assertEqual(row["ytd_gap"], 600)

    def test_budget_hit_rate_100_when_equal(self):
        # R1, CDE, 2025, Net: Actual == Budget == 100/mo
        row = self._row("R1", "CDE", "2025", "Net", "Actual")
        self.assertEqual(row["budget_hit_rate"], 100)

    def test_yoy_zero_when_no_prior_year(self):
        # All 2024 rows have no 2023 data → yoy_total = 0
        rows_2024 = self.result[self.result["year"] == "2024"]
        self.assertTrue((rows_2024["yoy_total"] == 0).all())

    def test_yoy_ratio(self):
        # R1, CDE, 2025, Gross, Actual: 300/mo (3600 total) vs 2024: 200/mo (2400)
        row = self._row("R1", "CDE", "2025", "Gross", "Actual")
        self.assertAlmostEqual(float(row["yoy_total"]), 1.5, places=3)

    def test_breakeven_month_actual_only(self):
        non_actual = self.result[self.result["sales_budget_type"] != "Actual"]
        self.assertTrue(non_actual["breakeven_month"].isna().all())

    def test_breakeven_correct_month(self):
        # R1, CDE, 2024, Net, Actual: cumsum 50,100,400 vs Budget 100,200,300
        # First crossing: month 3 (Mar), where 400 >= 300
        row = self._row("R1", "CDE", "2024", "Net", "Actual")
        self.assertEqual(row["breakeven_month"], 3)

    def test_breakeven_january_when_immediately_above(self):
        # R1, CDE, 2024, Gross, Actual: 200/mo vs Budget 100/mo → crosses in Jan
        row = self._row("R1", "CDE", "2024", "Gross", "Actual")
        self.assertEqual(row["breakeven_month"], 1)

    def test_breakeven_null_when_never_crosses(self):
        # R2, CDE, 2024, Gross, Actual: 10/mo vs Budget 1000/mo → never crosses
        row = self._row("R2", "CDE", "2024", "Gross", "Actual")
        self.assertTrue(pd.isna(row["breakeven_month"]))


if __name__ == "__main__":
    unittest.main()
