"""Tests for src/layer3_segmentation.py."""

import datetime
import pathlib
import unittest

from src import layer1, layer3_segmentation, loader

_FIXTURE = (
    pathlib.Path(__file__).parent / "fixtures" / "raw_report_fixture.csv"
)
_TODAY = datetime.date(2025, 6, 15)


class TestLayer3Segmentation(unittest.TestCase):
    def setUp(self):
        raw = loader.load(_FIXTURE)
        l1 = layer1.build(raw, today=_TODAY)
        self.result = layer3_segmentation.build(l1)

    def test_output_columns(self):
        self.assertEqual(
            list(self.result.columns), layer3_segmentation.LAYER3_SEG_COLUMNS
        )

    def test_row_count(self):
        # Same number of rows as layer1 (24 cohorts)
        self.assertEqual(len(self.result), 24)

    def test_rank_total_starts_at_one(self):
        self.assertEqual(self.result["rank_total"].min(), 1)

    def test_share_pct_sums_to_100_per_segment(self):
        segment_key = ["product", "year", "rev_op_type", "sales_budget_type"]
        sums = self.result.groupby(segment_key)["share_pct"].sum().round(1)
        self.assertTrue((sums == 100.0).all())

    def test_rank_total_r1_beats_r2_gross_actual(self):
        # R1 Gross Actual total=2400, R2 Gross Actual total=120 → R1 rank 1
        seg = self.result[
            (self.result["product"] == "CDE")
            & (self.result["year"] == "2024")
            & (self.result["rev_op_type"] == "Gross")
            & (self.result["sales_budget_type"] == "Actual")
        ].set_index("region")
        self.assertLess(seg.loc["R1", "rank_total"], seg.loc["R2", "rank_total"])

    def test_ytd_gap_positive_when_actual_exceeds_budget(self):
        # R1, CDE, 2024, Gross, Actual: ytd(Actual)=1200 > ytd(Budget)=600
        row = self.result[
            (self.result["region"] == "R1")
            & (self.result["product"] == "CDE")
            & (self.result["year"] == "2024")
            & (self.result["rev_op_type"] == "Gross")
            & (self.result["sales_budget_type"] == "Actual")
        ].iloc[0]
        self.assertGreater(row["ytd_gap"], 0)

    def test_rank_ytd_gap_worst_is_rank_one(self):
        # R2 Actual ytd_gap is very negative vs R1; R2 should have rank 1
        seg = self.result[
            (self.result["product"] == "CDE")
            & (self.result["year"] == "2024")
            & (self.result["rev_op_type"] == "Gross")
            & (self.result["sales_budget_type"] == "Actual")
        ].set_index("region")
        self.assertLess(
            seg.loc["R2", "rank_ytd_gap"], seg.loc["R1", "rank_ytd_gap"]
        )


if __name__ == "__main__":
    unittest.main()
