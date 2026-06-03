"""Tests for src/layer3_timeseries.py."""

import pathlib
import unittest

import pandas as pd

from src import layer3_timeseries, loader

_FIXTURE = (
    pathlib.Path(__file__).parent / "fixtures" / "raw_report_fixture.csv"
)


class TestLayer3Timeseries(unittest.TestCase):
    def setUp(self):
        self.raw = loader.load(_FIXTURE)
        self.result = layer3_timeseries.build(self.raw)

    def _cohort(self, region, product, year, rev_op, sbt):
        # Preserve the calendar order already applied by build()
        return self.result[
            (self.result["region"] == region)
            & (self.result["product"] == product)
            & (self.result["year"] == str(year))
            & (self.result["rev_op_type"] == rev_op)
            & (self.result["sales_budget_type"] == sbt)
        ]

    def test_output_columns(self):
        self.assertEqual(
            list(self.result.columns), layer3_timeseries.LAYER3_TS_COLUMNS
        )

    def test_row_count(self):
        # Same as raw input: 288 rows
        self.assertEqual(len(self.result), 288)

    def test_mom_growth_null_for_january(self):
        jan_rows = self.result[self.result["month"] == "Jan"]
        self.assertTrue(jan_rows["mom_growth"].isna().all())

    def test_mom_growth_one_for_uniform_cohort(self):
        # R1, CDE, 2024, Gross, Actual: 200/mo uniform → MoM ratio always 1.0
        cohort = self._cohort("R1", "CDE", "2024", "Gross", "Actual")
        non_jan = cohort[cohort["month"] != "Jan"]
        self.assertTrue((non_jan["mom_growth"] == 1.0).all())

    def test_seasonal_index_sums_to_one_per_cohort(self):
        sums = (
            self.result.groupby(layer3_timeseries.LAYER3_TS_COLUMNS[:5])
            ["seasonal_index"]
            .sum()
            .round(3)
        )
        self.assertTrue((sums == 1.0).all())

    def test_vs_budget_zero_for_budget_rows(self):
        budget_rows = self.result[self.result["sales_budget_type"] == "Budget"]
        self.assertTrue((budget_rows["vs_budget"] == 0).all())

    def test_vs_budget_actual_minus_budget(self):
        # R1, CDE, 2024, Gross, Actual: 200/mo; Budget: 100/mo → vs_budget = 100
        cohort = self._cohort("R1", "CDE", "2024", "Gross", "Actual")
        self.assertTrue((cohort["vs_budget"] == 100).all())

    def test_months_in_calendar_order(self):
        month_order = {m: i for i, m in enumerate(
            ["Jan","Feb","Mar","Apr","May","Jun",
             "Jul","Aug","Sep","Oct","Nov","Dec"]
        )}
        cohort = self._cohort("R1", "CDE", "2024", "Gross", "Actual")
        indices = cohort["month"].map(month_order).tolist()
        self.assertEqual(indices, sorted(indices))


if __name__ == "__main__":
    unittest.main()
