#!/usr/bin/env python3

import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
CASES = HERE.parent
sys.path.insert(0, str(CASES))
spec = importlib.util.spec_from_file_location(
    "d43_exact_selected_rows", HERE / "selected_rows.py")
ROWS = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ROWS)

import directionb_strike as DIRECTION
import r1_experiment as R1


MANIFEST_PATH = HERE / "PILOT_MANIFEST.json"


class ExactSelectedRowsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest, cls.manifest_hash = ROWS.load_manifest(MANIFEST_PATH)
        _orbits, cls.names, cls.registry_hash, cls.pin42 = \
            ROWS.reconstruct_registry()

    def test_registry_targets_and_pins(self):
        self.assertEqual(self.registry_hash, ROWS.EXPECTED_REGISTRY_SHA256)
        self.assertEqual(len(self.names), 348)
        self.assertEqual(len(ROWS.TARGETS), 184)
        self.assertEqual(sum(map(len, ROWS.BAND_TARGETS.values())), 184)
        self.assertEqual(set(self.pin42), {
            "tf1_74", "tf2_74", "tg1_74", "tg2_74",
            "tg01_74", "tg02_74",
        })

    def test_banked_pin_support_both_primes(self):
        reports = ROWS.banked_pin_audit(self.manifest)
        self.assertEqual([item["prime"] for item in reports],
                         [105337, 105673])
        self.assertTrue(all(set(item["nonzero_source_support"])
                            == set(ROWS.SUPPORT) for item in reports))

    def test_sparse_registry_pins_exact_complement(self):
        orbits, names, registry_hash, pin42 = ROWS.sparse_registry()
        self.assertEqual(registry_hash, ROWS.EXPECTED_REGISTRY_SHA256)
        free = tuple(name for name, state in zip(names, R1.VSTAT)
                     if state is None)
        self.assertEqual(free, ROWS.SUPPORT)
        self.assertTrue(set(pin42).isdisjoint(free))
        expected_B = {12: R1.vC(R1.rmono(B=1))}
        self.assertEqual(orbits["B"]["series"], expected_B)
        self.assertEqual(orbits["GB42"]["series"], expected_B)
        self.assertEqual(orbits["GB21"]["series"], expected_B)

    def test_component_product_equals_full_jrows(self):
        R1.VDEG_CAP = 4
        jf = {
            (1, 2): R1.vC(R1.rC(R1.K3(2))),
            (0, 1): R1.vC(R1.rC(R1.K3(5))),
        }
        jg = {
            (2, 4): R1.vC(R1.rC(R1.K3(3))),
            (3, 5): R1.vC(R1.rC(R1.K3(7))),
        }
        full = DIRECTION.jrows(jf, jg, ROWS.D)
        selected = ROWS.selected_source_rows(
            jf, jg, ((2, 6),), add_target=False)
        self.assertEqual(selected[(2, 6)], full.get((2, 6), {}))
        target = ROWS.selected_source_rows(
            {}, {}, ((0, 20),), add_target=True)
        self.assertEqual(target[(0, 20)], {(): R1.rC(R1.K3(42))})

    def test_semantic_digest_ignores_dict_insertion(self):
        ring1 = {
            (0, 0, 0, 1, 0, 0, 0, 0): R1.K3(2, 3),
            (0, 0, 0, 0, 0, 4, 0, 0): R1.K3(5, 7),
        }
        ring2 = dict(reversed(list(ring1.items())))
        expression1 = {(2,): ring1, (): R1.rC(R1.K3(11))}
        expression2 = {(): R1.rC(R1.K3(11)), (2,): ring2}
        self.assertEqual(
            ROWS.semantic_vexpr_digest(expression1, self.names),
            ROWS.semantic_vexpr_digest(expression2, self.names))

    def test_specialization_and_sentinel_fail_closed(self):
        jet = {(2, 6): {(1,): R1.RONE, (2,): R1.RONE}}
        self.assertEqual(ROWS.specialize_jet(jet, {2}),
                         {(2, 6): {(2,): R1.RONE}})
        with self.assertRaises(ValueError):
            ROWS.assert_no_sentinel({(2, 6): {(R1.HIVAR,): R1.RONE}})

    def test_exact_d21_band20_fixture(self):
        expected = ROWS.expected_d21_band20(self.manifest, self.names)
        self.assertEqual(set(expected), set(ROWS.BAND_TARGETS[20]))
        self.assertEqual(len(expected), 10)
        used = {self.names[index]
                for expression in expected.values()
                for monomial in expression for index in monomial}
        self.assertEqual(used, set(ROWS.LOW_SUPPORT))
        self.assertTrue(all(max(map(len, expression), default=0) <= 1
                            for expression in expected.values()))

    def test_full_checkpoint_lane_inert(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "preregistered but inert"):
                ROWS.load_full_checkpoint_pair(
                    self.manifest, Path(directory))

    def test_hash_checked_before_unpickle(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "not-a-pickle"
            path.write_bytes(b"not a pickle")
            with self.assertRaisesRegex(ValueError, "checkpoint hash drift"):
                ROWS._load_pickle_after_hash(path, "0" * 64)

    def test_cover_contract(self):
        shards = [{"rows": {target: {}}}
                  for target in ROWS.TARGETS]
        merged = ROWS.validate_cover(shards)
        self.assertEqual(set(merged), set(ROWS.TARGETS))
        with self.assertRaisesRegex(ValueError, "duplicate target"):
            ROWS.validate_cover(shards + [shards[0]])
        with self.assertRaisesRegex(ValueError, "target cover mismatch"):
            ROWS.validate_cover(shards[:-1])

    def test_merge_requires_identical_input_custody(self):
        shards = [
            {"input_custody_sha256": "a" * 64},
            {"input_custody_sha256": "a" * 64},
        ]
        self.assertEqual(ROWS.validate_common_custody(shards), "a" * 64)
        shards[-1]["input_custody_sha256"] = "b" * 64
        with self.assertRaisesRegex(ValueError, "identical input custody"):
            ROWS.validate_common_custody(shards)

    def test_pilot_manifest_refuses_fanout(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "fanout is not authorized"):
                ROWS.emit_shard(
                    MANIFEST_PATH, Path(directory) / "band22.pkl", (22,),
                    sparse_receipt=Path(directory) / "absent.json")

    def test_review_manifest_refuses_compute(self):
        with self.assertRaisesRegex(ValueError, "review-only"):
            ROWS.assert_operational_registration(self.manifest)

    def test_atomic_json_leaves_no_temporary(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "value.json"
            ROWS.atomic_json(path, {"value": 3})
            self.assertEqual(json.loads(path.read_text()), {"value": 3})
            self.assertEqual(list(Path(directory).glob("*.tmp.*")), [])


if __name__ == "__main__":
    unittest.main()
