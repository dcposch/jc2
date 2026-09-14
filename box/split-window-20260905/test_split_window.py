#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "box" / "lib"))
import split_window as SW  # noqa: E402


FROZEN = Path("/tmp/jc2-lane.D5nDdq/inputs/moh_skeleton_full.py")


def frozen_module():
    spec = importlib.util.spec_from_file_location("moh_skeleton_full_frozen_split_test", FROZEN)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class SplitWindowTests(unittest.TestCase):
    def test_exact_windows(self):
        self.assertEqual(
            SW.radius_window(3, 8),
            [F(4, 3), F(3, 2), F(5, 3), F(2), F(7, 3), F(5, 2)],
        )
        self.assertEqual(SW.radius_window(2, 7), [F(3, 2), F(2), F(5, 2), F(3)])
        self.assertEqual(SW.radius_window(2, 3), [])
        self.assertEqual(SW.radius_count_formula(3, 8), 6)

    def test_partition_count(self):
        for u in range(2, 14):
            self.assertEqual(len(SW.genuine_partitions(u)), SW.partition_number(u) - 1)
            for orbit in range(1, u + 1):
                measured = sum(
                    SW.galois_condition(part, F(1, orbit), u)["passes"]
                    for part in SW.genuine_partitions(u)
                )
                self.assertEqual(measured, SW.galois_partition_count(u, orbit), (u, orbit))

    def test_galois_partition_and_conjugated_normalization(self):
        dead = SW.galois_condition((2, 1), F(5, 2), 3)
        live = SW.galois_condition((1, 1, 1), F(5, 2), 3)
        self.assertFalse(dead["passes"])
        self.assertTrue(live["passes"])
        self.assertEqual(live["allowed_coefficient_degrees"], [1, 3])
        self.assertIn("w=h(z)=alpha*z+beta", live["conjugated_action"])
        self.assertIn("omega*w+(1-omega)*beta", live["conjugated_action"])

        # P=z^3-z, omega=-1, w=2z+3.  The monic transform is
        # P_tilde(w)=(w-3)^3-4(w-3), gamma_h(w)=-w+6.
        p_tilde = lambda w: (w - 3) ** 3 - 4 * (w - 3)
        for w in range(-4, 9):
            self.assertEqual(p_tilde(-w + 6), -p_tilde(w))

    def test_negative_k_is_not_discarded_in_all_degree_screen(self):
        # t=23/4 > W=5.  A W-independent test would wrongly call all four
        # simple roots low; the actual low multiplicity would be negative.
        local = SW.local_exponent_condition((1, 1, 1, 1), F(27, 4), 4, 28, 5)
        self.assertEqual(local["k"], "-3/4")
        self.assertFalse(local["passes"])
        self.assertEqual(len(local["forced_high_roots"]), 4)

    def test_9966_calibration(self):
        moh = frozen_module()
        rows = []
        for m, Ms, V in moh.census(99, Kmin=2, full=True):
            if m != 66:
                continue
            skel = moh.Skel(99, m, list(Ms), V)
            if skel.d[skel.s] - skel.V[skel.s] >= 2:
                rows.append((skel, SW.screen_skeleton(skel)))
        self.assertEqual(len(rows), 6)
        lookup = {
            (result["skeleton"]["M"][1], result["skeleton"]["V"]["2"],
             result["skeleton"]["V"]["3"]): result
            for _, result in rows
        }
        expected = {
            (-22, 1, 9): [("4", [1, 1])],
            (22, 1, 7): [("3/2", [2, 2]), ("3/2", [2, 1, 1]), ("5/3", [1, 1, 1, 1])],
            (22, 5, 7): [("3/2", [2, 2]), ("3/2", [2, 1, 1]), ("5/3", [1, 1, 1, 1])],
            (22, 1, 8): [("2", [2, 1]), ("5/2", [1, 1, 1])],
            (77, 8, 7): [("3/2", [2, 2]), ("3/2", [2, 1, 1]), ("5/3", [1, 1, 1, 1])],
            (77, 8, 8): [("2", [2, 1]), ("5/2", [1, 1, 1])],
        }
        self.assertEqual(set(lookup), set(expected))
        for key, wanted in expected.items():
            got = [(item["rho"], item["partition"]) for item in lookup[key]["survivors"]]
            self.assertEqual(got, wanted, key)
        open_five = [value for key, value in lookup.items() if key != (77, 8, 8)]
        self.assertEqual(sum(row["finite_window"]["raw_pair_count"] for row in open_five), 66)
        self.assertEqual(sum(row["killed_count"] for row in open_five), 54)
        self.assertEqual(sum(row["survivor_count"] for row in open_five), 12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
