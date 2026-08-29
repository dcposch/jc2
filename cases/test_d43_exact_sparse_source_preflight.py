#!/usr/bin/env python3

import os
import sys
import unittest


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import d43_exact_sparse_source_preflight as PREFLIGHT


class SparseSourcePreflightTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = PREFLIGHT.run()

    def test_verdict_is_scoped(self):
        self.assertEqual(self.report["verdict"],
                         "GO_SMALL_QUADRATIC_SOURCE_REBUILD")
        self.assertIsNone(
            self.report["claim_boundary"]["relaxed_finite_184_J_point"])
        self.assertIn(
            "relation E alone is insufficient",
            self.report["required_next_artifact"]["template_bridge"])
        self.assertIsNone(
            self.report["claim_boundary"]["exact_raw_source_point"])

    def test_common_support(self):
        audits = self.report["prime_audits"]
        self.assertEqual(
            audits[0]["floor_passing_modular_point_support"]["coordinates"],
            audits[1]["floor_passing_modular_point_support"]["coordinates"])
        for audit in audits:
            support = audit["floor_passing_modular_point_support"]
            self.assertEqual((support["count"], support["restricted_rows"],
                              support["terms"], support["max_degree"]),
                             (22, 29, 1003, 2))

    def test_not_affine_and_wrong_89_lane_rejected(self):
        for audit in self.report["prime_audits"]:
            self.assertEqual(
                (audit["slice_101_is_not_affine"]["variables"],
                 audit["slice_101_is_not_affine"]["live_rows"],
                 audit["slice_101_is_not_affine"]["terms"],
                 audit["slice_101_is_not_affine"]["max_degree"],
                 audit["slice_101_is_not_affine"]["nonlinear_rows"]),
                (101, 175, 83557, 6, 151))
            self.assertEqual(
                audit[
                    "slice_89_is_not_affine_in_full_banked_presentation"],
                {"variables": 89, "live_rows": 156, "terms": 4541,
                 "max_degree": 3, "nonlinear_rows": 102})
            self.assertIn("REJECTED",
                          audit["slice_89_is_not_a_full_source_point"]
                               ["source_floor"])

    def test_bandwise_affinity_not_global_affinity(self):
        for audit in self.report["prime_audits"]:
            blocks = audit["band_triangularity"]
            self.assertEqual([(item["band"], item["rows"],
                               item["new_variables"], item["rank"])
                              for item in blocks],
                             [(20, 10, 10, 4),
                              (30, 9, 8, 4),
                              (40, 10, 4, 4)])

    def test_exact_d21_is_source_data(self):
        exact = self.report["exact_low_source"]
        self.assertEqual(exact["row20_exact_rows"], 10)
        self.assertEqual(
            (exact["row20_tail_monomials"],
             exact["row20_W_coefficient_terms"],
             exact["max_tail_degree"]),
            (109, 119, 1))
        self.assertTrue(all(item["coefficient_rank"] == 4
                            for item in exact["modular_replays"]))
        self.assertEqual(exact["meaning"],
                         "exact R_ext source rows on the proposed lower "
                         "support; no CRT reconstruction")


if __name__ == "__main__":
    unittest.main()
