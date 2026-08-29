#!/usr/bin/env python3

import sys
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import d43_exact_sparse_source_preflight_v2 as PREFLIGHT


class SparseSourcePreflightV2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = PREFLIGHT.run()

    def test_revision_and_launch_boundary(self):
        self.assertEqual(
            self.report["verdict"],
            "GO_AFTER_FRESH_HOSTILE_PASS_AND_AWS_REGISTRATION")
        self.assertFalse(
            self.report["one_immutable_pipeline"]["aws_registered"])
        self.assertIn("superseded",
                      self.report["revision_provenance"]["meaning"])

    def test_literal_rank432_a00pp_scope(self):
        algebra = self.report["coefficient_algebra"]
        self.assertEqual(algebra["basis_rank"], 432)
        self.assertEqual(algebra["literal_a00pp_substitution"],
                         ["HW1=h*W1", "HW2=h*W2"])
        self.assertIsNone(algebra["field_claim"])
        self.assertIn("REFUSED", algebra["EB"])

    def test_collapsed_d21_gate_has_required_mutations(self):
        gate = self.report["exact_collapsed_d21_fixture_gate"]
        self.assertEqual(gate["status"],
                         "PASS_EXACT_COLLAPSED_D21_BAND20_EQUALITY")
        self.assertEqual(set(gate["required_mutation_digests"]), {
            "HW1_negative", "HW2_negative", "plus42_omitted"})
        self.assertTrue(gate["all_mutations_distinct"])

    def test_E_one_unit_bridge_and_literal_replay(self):
        bridge = self.report["template_bridge"]
        self.assertEqual(bridge["one_unit_coordinate"], "uW12")
        self.assertTrue(bridge["literal_replay"]
                        ["E5_2_equals_unit_times_E"])
        self.assertTrue(all(item["status"] ==
            "PASS_LITERAL_E5_E6_ONE_UNIT_RECONSTRUCTION"
            for item in self.report[
                "registered_modular_template_bridge_replays"]))

    def test_same_manifest_conditional_all184_no_solve(self):
        pipeline = self.report["one_immutable_pipeline"]
        self.assertIn("same-manifest conditional 184-row emission and merge",
                      pipeline["stages"])
        self.assertFalse(pipeline["solve"])
        self.assertEqual(self.report["required_real_run_checks"]
                         ["exact_zero_rows"], 155)

    def test_claim_tiers_remain_separate(self):
        tiers = self.report["claim_tiers"]
        self.assertIn("raw-J", tiers["tier1"])
        self.assertIn("E and one", tiers["tier2"])
        self.assertIn("literal", tiers["tier2_replay"])
        self.assertIsNone(tiers["NF_all_depth_Keller_JC2"])


if __name__ == "__main__":
    unittest.main()
