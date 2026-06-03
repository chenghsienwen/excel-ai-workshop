"""Tests for src/periods.py."""

import datetime
import pathlib
import unittest

from src import loader, periods

_FIXTURE = (
    pathlib.Path(__file__).parent / "fixtures" / "raw_report_fixture.csv"
)


class TestPeriodMonths(unittest.TestCase):
    def test_quarters_cover_all_months(self):
        all_months = set(
            periods.PERIOD_MONTHS["q1"]
            + periods.PERIOD_MONTHS["q2"]
            + periods.PERIOD_MONTHS["q3"]
            + periods.PERIOD_MONTHS["q4"]
        )
        self.assertEqual(all_months, set(periods.PERIOD_MONTHS["total"]))

    def test_halves_equal_quarter_pairs(self):
        self.assertEqual(
            set(periods.PERIOD_MONTHS["h1"]),
            set(periods.PERIOD_MONTHS["q1"] + periods.PERIOD_MONTHS["q2"]),
        )
        self.assertEqual(
            set(periods.PERIOD_MONTHS["h2"]),
            set(periods.PERIOD_MONTHS["q3"] + periods.PERIOD_MONTHS["q4"]),
        )

    def test_total_equals_h1_plus_h2(self):
        self.assertEqual(
            set(periods.PERIOD_MONTHS["total"]),
            set(periods.PERIOD_MONTHS["h1"] + periods.PERIOD_MONTHS["h2"]),
        )


class TestYtdMonths(unittest.TestCase):
    def test_june(self):
        result = periods.ytd_months(datetime.date(2025, 6, 15))
        self.assertEqual(
            result, ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        )

    def test_january(self):
        result = periods.ytd_months(datetime.date(2025, 1, 1))
        self.assertEqual(result, ["Jan"])

    def test_december(self):
        result = periods.ytd_months(datetime.date(2025, 12, 31))
        self.assertEqual(result, periods.PERIOD_MONTHS["total"])


class TestAggregatePeriods(unittest.TestCase):
    def setUp(self):
        self.raw = loader.load(_FIXTURE)
        self.today = datetime.date(2025, 6, 15)
        self.result = periods.aggregate_periods(self.raw, today=self.today)

    def test_total_equals_sum_of_months(self):
        # R1, CDE, 2024, Gross, Actual: 200/mo × 12 = 2400
        row = self.result[
            (self.result["region"] == "R1")
            & (self.result["product"] == "CDE")
            & (self.result["year"] == "2024")
            & (self.result["rev_op_type"] == "Gross")
            & (self.result["sales_budget_type"] == "Actual")
        ].iloc[0]
        self.assertEqual(row["total"], 2400)

    def test_h1_plus_h2_equals_total(self):
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

    def test_ytd_is_h1_for_june(self):
        # today=Jun → ytd = Jan-Jun = h1
        self.assertTrue((self.result["ytd"] == self.result["h1"]).all())

    def test_ytd_lte_total(self):
        self.assertTrue((self.result["ytd"] <= self.result["total"]).all())


if __name__ == "__main__":
    unittest.main()
