"""Tests for src/layer1.py."""

import datetime
import pathlib
import unittest

from src import layer1, loader

_FIXTURE = (
    pathlib.Path(__file__).parent / "fixtures" / "raw_report_fixture.csv"
)

_EXPECTED_COLUMNS = [
    "region", "product", "year", "rev_op_type", "sales_budget_type",
    "total", "h1", "h2", "q1", "q2", "q3", "q4", "ytd",
]

_TODAY = datetime.date(2025, 6, 15)


class TestLayer1(unittest.TestCase):
    def setUp(self):
        raw = loader.load(_FIXTURE)
        self.result = layer1.build(raw, today=_TODAY)

    def test_output_columns(self):
        self.assertEqual(list(self.result.columns), _EXPECTED_COLUMNS)

    def test_row_count(self):
        # 2 regions × 1 product × 2 years × 2 rev_op × 3 sbt = 24 cohorts
        self.assertEqual(len(self.result), 24)

    def test_total_equals_sum_of_all_months(self):
        # R1, CDE, 2024, Gross, Actual: 200 × 12 = 2400
        row = self.result[
            (self.result["region"] == "R1")
            & (self.result["product"] == "CDE")
            & (self.result["year"] == "2024")
            & (self.result["rev_op_type"] == "Gross")
            & (self.result["sales_budget_type"] == "Actual")
        ].iloc[0]
        self.assertEqual(row["total"], 2400)

    def test_h1_h2_partition(self):
        self.assertTrue(
            ((self.result["h1"] + self.result["h2"]) == self.result["total"]).all()
        )

    def test_quarter_partition(self):
        q_sum = (
            self.result["q1"]
            + self.result["q2"]
            + self.result["q3"]
            + self.result["q4"]
        )
        self.assertTrue((q_sum == self.result["total"]).all())

    def test_ytd_lte_total(self):
        self.assertTrue((self.result["ytd"] <= self.result["total"]).all())

    def test_net_actual_total(self):
        # R1, CDE, 2024, Net, Actual: 50+50+300 = 400
        row = self.result[
            (self.result["region"] == "R1")
            & (self.result["product"] == "CDE")
            & (self.result["year"] == "2024")
            & (self.result["rev_op_type"] == "Net")
            & (self.result["sales_budget_type"] == "Actual")
        ].iloc[0]
        self.assertEqual(row["total"], 400)


if __name__ == "__main__":
    unittest.main()
