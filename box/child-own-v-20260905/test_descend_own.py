#!/usr/bin/env python3
"""Source controls for own-disc descent, not implementation-mirroring tests."""
import importlib.util
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True
from box.lib.descend_own import descend_own, exact_int, inverse_top

spec = importlib.util.spec_from_file_location(
    "own_test_frozen", "/tmp/jc2-lane.wwyG4k/inputs/moh_skeleton_full.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)


class SourceControls(unittest.TestCase):
    def test_moh_five_printed_descents_every_column(self):
        # p207, independently transcribed from the checked page image.
        expected = [
            (16, 12, -12, 13, 3, Q(-1), Q(1, 4), 1),
            (21, 14, -14, 16, 2, Q(-1, 2), Q(7, 6), 1),
            (21, 14, -14, 18, 5, Q(-1), Q(1, 3), 1),
            (15, 10, -10, 11, 3, Q(-1), Q(1, 2), 2),
            (15, 10, -10, 11, 2, Q(-1), Q(4, 3), 2),
        ]
        for row, want in zip(B.MOH_TABLE[:5], expected):
            with self.subTest(row=row[4]):
                child = descend_own(B.Skel(*row[:4]))
                self.assertEqual(child["V_vectors"], [(Q(want[4]),)])
                radii = child["child_radii"][0]["delta"]
                got = (child["n"], child["m"], child["raw_M"][1],
                       child["raw_M"][2], child["V_vectors"][0][0],
                       radii[2], radii[1], child["ell"])
                self.assertEqual(got, want)

    def test_gate_180_own_jet_and_fifteen_plus_fifteen(self):
        for v2 in (2, 3):
            child = descend_own(B.Skel(180, 120, [132, 150, 178],
                                      {2: v2, 3: 4, 4: 5}))
            self.assertEqual(list(child["raw_M"].values()), [-20, 22, 25])
            self.assertEqual(list(child["raw_d"].values()), [30, 10, 2, 1])
            self.assertEqual(child["quasi_root_pi_degrees"], {1: 20, 2: 18, 3: 87})
            self.assertEqual(child["V_vectors"], [(Q(v2), Q(1))])
        split = inverse_top(180, 6, 12, 1, 5, Q(1, 6), 4, (1,))
        self.assertEqual([g["roots"] for g in split["inverse_groups"]], [15, 15])
        self.assertEqual(split["child_growth"], 1)

    def test_gate_96_top_does_not_claim_source_realization(self):
        child = descend_own(B.Skel(96, 72, [36, 78, 94], {2: 4, 3: 3, 4: 5}))
        self.assertEqual(list(child["raw_M"].values()), [-12, 6, 13])
        self.assertEqual(list(child["raw_d"].values()), [16, 4, 2, 1])
        self.assertEqual(child["local_V"][3]["values"], [Q(1)])
        self.assertEqual(child["level2_identity"]["values"], [Q(4)])
        self.assertEqual(child["V_vectors"], [])
        split = inverse_top(96, 6, 12, 1, 5, Q(1, 7), 3, (1,))
        self.assertEqual([g["roots"] for g in split["inverse_groups"]], [8, 8])

    def test_inversion_numerator_creates_separate_discs(self):
        # p207's (21,14,M2=16), source delta=2/7: two child coefficients
        # per source orbit. Merging them would incorrectly produce V'=4.
        split = inverse_top(84, 4, 28, 1, 3, Q(2, 7), 0, (2, 1))
        self.assertEqual([g["roots"] for g in split["inverse_groups"]],
                         [3, 6, 6, 3, 3])
        self.assertEqual(split["child_growth"], Q(1, 2))

    def test_99_source_labels_and_conditional_retained_child(self):
        source = B.Skel(99, 66, [77, 97], {2: 8, 3: 8})
        child = descend_own(source)
        self.assertEqual(list(child["source"]["M"].values()), [-66, 77, 97])
        self.assertEqual((child["n"], child["m"]), (27, 18))
        self.assertEqual(list(child["raw_M"].values()), [-18, 21])
        self.assertEqual(list(child["raw_d"].values()), [27, 9, 3])
        self.assertEqual(child["characteristic_scope"], "retained prefix only")
        self.assertEqual(child["descent_license"], "CONDITIONAL_PROP6.3_RADIUS")
        self.assertEqual(list(source.M.values()), [-66, 77, 97])

    def test_own_D1_contradiction_is_not_an_empty_set_value(self):
        child = descend_own(B.Skel(108, 72, [-18, 60, 106], {2: 11, 3: 15, 4: 5}))
        self.assertEqual(child["level2_identity"]["values"], [Q(11)])
        self.assertEqual(child["d"][2], 6)
        self.assertTrue(child["u_negative"]["value"])
        self.assertEqual(child["V_vectors"], [])
        self.assertEqual(child["V"][2]["type"], "SET-VALUED")

    def test_dropped_tail_cannot_silently_use_old_radius_formula(self):
        child = descend_own(B.Skel(108, 72, [84, 104, 106], {2: 8, 3: 8, 4: 3}))
        self.assertEqual(list(child["raw_d"].values()), [27, 9, 3, 1])
        self.assertEqual(list(child["d"].values()), [27, 9, 3])
        self.assertEqual(child["diagnostic_radii"][0]["delta"], {1: Q(1, 3), 2: Q(0)})
        self.assertFalse(child["diagnostic_radii"][0]["effective_formula_agrees"])
        self.assertEqual(child["V_vectors"], [])
        self.assertEqual(child["route_state"], "EMPTY_PROP6.3_FINITE_POLE")

    def test_wrong_projection_input_and_noninteger_data_rejected(self):
        with self.assertRaises(ValueError):
            inverse_top(180, 6, 12, 1, 5, Q(1, 6), 3, (1,))
        with self.assertRaises(ValueError):
            exact_int(Q(3, 2))
        with self.assertRaises(ValueError):
            descend_own(B.Skel(*B.MOH_TABLE[0][:4]), reduced_source=False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
