#!/usr/bin/env python3
"""Light exact tests for the v3 producer.

Carries the complete v2 mathematical regression surface (the payload is
intended to be v2 byte-for-byte) and adds the v3 repair fixtures: literal
structural D21 gate equality with mutation refusal through the actual gate,
fail-closed lease/registration refusals, and the absence of any early
positive terminal writer in the producer.
"""

import importlib.util
import json
import sys
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
CASES = HERE.parent
sys.path.insert(0, str(CASES))
spec = importlib.util.spec_from_file_location(
    "d43_exact_sparse_rows_v3", HERE / "selected_rows_v3.py")
ROWS = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = ROWS
spec.loader.exec_module(ROWS)

import d43_common_integral_emitter as COMMON
import r1_experiment as R1


MANIFEST_PATH = HERE / "PIPELINE_MANIFEST_V3.json"


class ExactA00ppRowsV3Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest, cls.manifest_hash = ROWS.load_manifest(MANIFEST_PATH)
        _orbits, cls.names, cls.registry_hash, cls.pin42 = \
            ROWS.BASE.reconstruct_registry()

    def test_registry_targets_and_432_quotient_scope(self):
        self.assertEqual(self.registry_hash, ROWS.EXPECTED_REGISTRY_SHA256)
        self.assertEqual(len(self.names), 348)
        self.assertEqual(len(ROWS.SUPPORT), 22)
        self.assertEqual(len(ROWS.TARGETS), 184)
        self.assertEqual(ROWS.COEFFICIENT_ALGEBRA["basis_rank"], 432)
        self.assertIsNone(ROWS.COEFFICIENT_ALGEBRA["field_claim"])
        self.assertEqual(ROWS.coefficient_algebra_sha256(),
                         "a06f7c1bb75f852819b50a2ecf9e362f8209da0fe9eb71af76f66c50a6a0fcaf")
        ROWS.require_registry(self.names, self.registry_hash, self.pin42)

    def test_manifest_binds_v3_contract_and_status(self):
        self.assertEqual(self.manifest["schema"],
                         "jc2.d43.a00pp-exact-source-manifest.v3")
        self.assertEqual(self.manifest["status"],
                         "V3_REPAIRED_LAUNCH_NOT_AUTHORIZED")
        self.assertEqual(self.manifest["resource_contract"],
                         ROWS.RESOURCE_CONTRACT)
        self.assertEqual(self.manifest["resource_contract"]
                         ["memory_swap_max_bytes"], 0)
        self.assertEqual(self.manifest["resource_contract"]
                         ["maximum_memory_total_kib"], 1073741824)
        self.assertEqual(self.manifest["terminal"]["single_authority"],
                         "TERMINAL.json")
        self.assertEqual(
            self.manifest["revision_provenance"]["v2_hostile_review_sha256"],
            "4f6f6c90e0526ab07591e2ec6a97f475e477b534cb6991085764cd693a99020d")

    def test_literal_hw_collapse_and_sign_mutations(self):
        raw = R1.radd(R1.rmono(h1=1), R1.rmono(h2=1))
        correct = ROWS.collapse_r1_ring_element(raw)
        negative1 = ROWS.collapse_r1_ring_element(raw, (-1, 1))
        negative2 = ROWS.collapse_r1_ring_element(raw, (1, -1))
        h = COMMON.RadicalCoefficient.generator("h")
        self.assertEqual(correct, {
            (1, 0): h,
            (0, 1): h,
        })
        self.assertEqual(len({ROWS.semantic_cp_sha256(value) for value in
                              (correct, negative1, negative2)}), 3)

    def test_surviving_eb_is_refused(self):
        with self.assertRaisesRegex(ValueError, "EB exponent survives"):
            ROWS.collapse_r1_ring_element(R1.rmono(B=1))
        raw_orbits, _names, _registry_hash, _pin42 = \
            ROWS.BASE.sparse_registry()
        ROWS.assert_raw_b_orbits(raw_orbits)

    def test_a_orbit_is_collapsed_before_multiplication(self):
        raw_orbits, _names, _registry_hash, _pin42 = \
            ROWS.BASE.sparse_registry()
        gp1 = ROWS.convert_a_orbit(raw_orbits["Gp1"])
        h = COMMON.RadicalCoefficient.generator("h")
        self.assertEqual(gp1["series"][37],
                         {(): ROWS.cp_w(1, 0, h)})
        p1 = ROWS.convert_a_orbit(raw_orbits["P1"])
        self.assertEqual(p1["series"][37], {(): ROWS.cp_w(1, 0)})

    def test_exact_b_block_matches_postcollapse_raw_d21(self):
        raw_orbits, _names, _registry_hash, _pin42 = \
            ROWS.BASE.sparse_registry()
        raw_f = R1.gm_jet2(("B",), raw_orbits, 21, "test-B")
        raw_g = R1.gm_jet2(("GB42", "GB21"), raw_orbits, 21,
                           "test-GB")
        collapsed_f = {target: ROWS.collapse_vexpr(value)
                       for target, value in raw_f.items()}
        collapsed_g = {target: ROWS.collapse_vexpr(value)
                       for target, value in raw_g.items()}
        self.assertEqual(collapsed_f, ROWS.collapsed_b_block(6, 21))
        self.assertEqual(collapsed_g, ROWS.collapsed_b_block(9, 21))

    def test_collapsed_gm_engine_matches_postcollapse_raw_prefix(self):
        raw_orbits, _names, _registry_hash, _pin42 = \
            ROWS.BASE.sparse_registry()
        for side, orbit_names in (
                ("f", ("P1", "P2")),
                ("g", ("Gp1", "Gp2", "G0p1", "G0p2"))):
            raw = R1.gm_jet2(orbit_names, raw_orbits, 7,
                             "test-raw-prefix-%s" % side)
            expected = {target: ROWS.collapse_vexpr(value)
                        for target, value in raw.items()}
            collapsed_orbits = {
                name: ROWS.convert_a_orbit(raw_orbits[name])
                for name in orbit_names}
            actual = ROWS.collapsed_gm_jet2(
                orbit_names, collapsed_orbits, 7,
                "test-collapsed-prefix-%s" % side)
            self.assertEqual(actual, expected)

    def test_selected_component_commutes_with_collapse(self):
        raw_f = {
            (1, 2): R1.vC(R1.rmono(w1=1)),
            (0, 1): R1.vC(R1.rC(5)),
        }
        raw_g = {
            (2, 4): R1.vC(R1.rmono(h1=1)),
            (3, 5): R1.vC(R1.rC(7)),
        }
        target = ((2, 6),)
        raw_row = ROWS.BASE.selected_source_rows(
            raw_f, raw_g, target, add_target=False)
        collapsed_after = {key: ROWS.collapse_vexpr(value)
                           for key, value in raw_row.items()}
        collapsed_before = ROWS.selected_source_rows(
            {key: ROWS.collapse_vexpr(value) for key, value in raw_f.items()},
            {key: ROWS.collapse_vexpr(value) for key, value in raw_g.items()},
            target, add_target=False)
        self.assertEqual(collapsed_before, collapsed_after)

    def test_exact_collapsed_d21_literal_gate(self):
        expected = ROWS.expected_collapsed_d21_band20(
            self.manifest, self.names)
        gate = ROWS.collapsed_d21_gate(expected, self.manifest, self.names)
        self.assertEqual(gate["status"],
                         "PASS_EXACT_COLLAPSED_D21_BAND20_LITERAL_EQUALITY")
        self.assertEqual(gate["decision_basis"],
                         "LITERAL_STRUCTURAL_EQUALITY")
        self.assertTrue(gate["digests_are_receipts_only"])
        self.assertTrue(gate["all_mutations_literally_refused"])
        self.assertEqual(len(expected), 10)

    def test_each_mutation_is_refused_by_the_actual_gate(self):
        """Feed every independently mutated row set through the real gate."""
        mutations = {
            "HW1_negative": ROWS.expected_collapsed_d21_band20(
                self.manifest, self.names, (-1, 1)),
            "HW2_negative": ROWS.expected_collapsed_d21_band20(
                self.manifest, self.names, (1, -1)),
            "plus42_omitted": ROWS.expected_collapsed_d21_band20(
                self.manifest, self.names, (1, 1), add_target=False),
        }
        for name, mutated in mutations.items():
            with self.assertRaisesRegex(
                    ROWS.CustodyError, "literal equality failed", msg=name):
                ROWS.collapsed_d21_gate(mutated, self.manifest, self.names)
        # A single-coefficient structural perturbation must also be refused,
        # even though it is far too small to matter to any digest shortcut.
        perturbed = ROWS.expected_collapsed_d21_band20(
            self.manifest, self.names)
        target = (0, 20)
        row = dict(perturbed[target])
        row[()] = ROWS.cp_add(row[()], ROWS.cp_k3(1))
        perturbed[target] = row
        with self.assertRaisesRegex(ROWS.CustodyError,
                                    "literal equality failed"):
            ROWS.collapsed_d21_gate(perturbed, self.manifest, self.names)

    def test_template_bridge_symbolic_and_registered_modular_replay(self):
        spec_dict = ROWS.template_bridge_spec()
        self.assertEqual(spec_dict["one_unit_coordinate"], "uW12")
        self.assertTrue(spec_dict["literal_replay"]
                        ["E5_2_equals_unit_times_E"])
        for prime in (105337, 105673):
            point = json.loads((CASES /
                ("d43_full_certificate_p%d.json" % prime)).read_text())["point"]
            W1 = point["parked_28"]["W1"]
            W2 = point["parked_28"]["W2"]
            unit = pow(W1 * W2 % prime, -1, prime)
            result = ROWS.template_bridge_modular_gate(
                W1, W2, unit, prime, COMMON.REGISTERED_FRAMES[prime])
            self.assertEqual(result["status"],
                             "PASS_LITERAL_E5_E6_ONE_UNIT_RECONSTRUCTION")

    def test_exact_155_zero_inventory_contract(self):
        rows = {target: {} for target in ROWS.TARGETS}
        for band in (20, 30, 40):
            for target in ROWS.BAND_TARGETS[band]:
                rows[target] = {(): ROWS.CP_ONE}
        report = ROWS.validate_exact_inventory(rows)
        self.assertEqual((report["live_rows"], report["exact_zero_rows"]),
                         (29, 155))
        rows[ROWS.BAND_TARGETS[22][0]] = {(): ROWS.CP_ONE}
        with self.assertRaisesRegex(ValueError, "29/155"):
            ROWS.validate_exact_inventory(rows)

    def test_disjoint_184_cover(self):
        shards = [{"rows": {target: {}}}
                  for target in ROWS.TARGETS]
        self.assertEqual(set(ROWS.validate_cover(shards)), set(ROWS.TARGETS))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            ROWS.validate_cover(shards + [shards[0]])

    def test_review_manifest_refuses_every_compute_lane(self):
        with self.assertRaisesRegex(ValueError, "AWS-unregistered"):
            ROWS.assert_operational_registration(self.manifest)
        self.assertFalse(self.manifest["authorization"]["solve"])
        self.assertTrue(self.manifest["authorization"]
                        ["conditional_band20_then_all184"])
        with self.assertRaisesRegex(ValueError, "AWS-unregistered"):
            ROWS.finalize_candidate(MANIFEST_PATH, HERE / "absent.json",
                                    HERE / "absent_lease.json", HERE)

    def test_missing_or_unheld_lease_is_refused(self):
        with self.assertRaises(Exception):
            ROWS.load_run_lease(HERE / "no_such_lease.json", HERE)
        import tempfile, os as _os
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp).resolve()
            lock = run_dir / "host.lock"
            lock.write_text("")
            lease_path = run_dir / "RUN_LEASE.json"
            stat = _os.stat(lock)
            lease_path.write_text(json.dumps({
                "schema": ROWS.LEASE_SCHEMA,
                "run_nonce": "ab" * 32,
                "job_root": str(run_dir),
                "job_tag": run_dir.name,
                "terminal_authority": False,
                "lock_path": str(lock),
                "lock_dev_ino": [stat.st_dev, stat.st_ino],
            }))
            _os.environ["RUN_NONCE"] = "ab" * 32
            try:
                # Nobody holds the flock, so the lease must be refused.
                with self.assertRaisesRegex(ROWS.CustodyError,
                                            "no longer held"):
                    ROWS.load_run_lease(lease_path, run_dir)
            finally:
                _os.environ.pop("RUN_NONCE", None)

    def test_producer_writes_no_early_positive_authority(self):
        source = (HERE / "selected_rows_v3.py").read_text()
        for forbidden in ('"VERDICT"', "'VERDICT'", "FINAL_RECEIPT",
                          "ARTIFACTS.json", '"COMPLETE',
                          "TERMINAL\""):
            self.assertNotIn(forbidden, source, forbidden)
        self.assertNotIn("finalize_run", source)
        self.assertIn("CANDIDATE_PENDING_TERMINAL_DECISION", source)
        supervisor = (HERE / "run_conditional_pipeline_aws_v3.sh").read_text()
        self.assertNotIn("CURRENT_STAGE\" COMPLETE", supervisor)
        self.assertEqual(supervisor.count('atomic_marker "$output/CURRENT_STAGE" RUNNING_'),
                         supervisor.count('atomic_marker "$output/CURRENT_STAGE"'))

    def test_no_production_asserts_survive(self):
        import ast
        for name in ("selected_rows_v3.py", "aws_preflight_v3.py",
                     "job_contract_v3.py"):
            tree = ast.parse((HERE / name).read_text())
            asserts = [node.lineno for node in ast.walk(tree)
                       if isinstance(node, ast.Assert)]
            self.assertEqual(asserts, [], "%s has asserts at %r" %
                             (name, asserts))

    def test_single_terminal_writer_census(self):
        """Only existence-guarded shell sites may publish TERMINAL.json."""
        supervisor = (HERE / "run_conditional_pipeline_aws_v3.sh").read_text()
        launcher = (HERE / "aws_launch_v3.sh").read_text()
        # Supervisor: one emergency publisher (guarded by an early return
        # when the terminal exists) and one decision rename (guarded by
        # exit 75 when the terminal exists).
        self.assertEqual(supervisor.count('mv "$temporary" "$terminal"'), 1)
        self.assertEqual(supervisor.count('mv "$decision_tmp" "$terminal"'),
                         1)
        self.assertIn('[[ -e "$terminal" ]] && return 0', supervisor)
        self.assertIn('[[ ! -e "$terminal" ]] || exit 75', supervisor)
        # Launcher: a single guarded emergency publisher; it never
        # overwrites an existing terminal.
        self.assertEqual(launcher.count('mv "$temporary" "$terminal"'), 1)
        self.assertIn('[[ -e "$terminal" ]] && return 0', launcher)
        # The launcher pins the sealed archive digest as a 64-hex literal.
        self.assertRegex(launcher,
                         r'EXPECTED_SOURCE_ARCHIVE_SHA256="[0-9a-f]{64}"')
        # No VERDICT/FINAL_RECEIPT/ARTIFACTS legacy authorities anywhere.
        for text in (supervisor, launcher):
            self.assertNotIn("FINAL_RECEIPT", text)
            self.assertNotIn("ARTIFACTS.json", text)
            self.assertNotIn('output/VERDICT', text)

    def test_preflight_census_is_job_tag_aware(self):
        source = (HERE / "aws_preflight_v3.py").read_text()
        self.assertIn("selected_rows_v3", source)
        self.assertIn("run_conditional_pipeline_aws", source)
        self.assertIn("job_contract_v3", source)
        self.assertIn("aws_launch_v3", source)
        self.assertIn("JOB_TAG=", source)
        self.assertIn("live_ec2_identity", source)
        self.assertIn("tags/instance/", source)
        self.assertIn("memory_total_within_cap", source)
        self.assertIn("lease_lock_held", source)
        self.assertNotIn("str(run_dir) in command", source)


if __name__ == "__main__":
    unittest.main()
