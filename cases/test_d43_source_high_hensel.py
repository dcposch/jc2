#!/usr/bin/env python3
"""Light, dependency-free tests for d43_source_high_hensel.py."""

import json
import os
import sys
import tempfile
import unittest
from copy import deepcopy
from unittest import mock


HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import d43_common_integral_emitter as INTEGRAL
import d43_source_high_hensel as H


class LinearAlgebraTests(unittest.TestCase):
    def test_left_cokernel_and_compatible_solve(self):
        prime = 7
        matrix = [[1, 0], [0, 1], [1, 1]]
        factor = H.factor_matrix(matrix, prime)
        self.assertEqual(factor["rank"], 2)
        self.assertEqual(len(factor["left_cokernel"]), 1)
        witness = factor["left_cokernel"][0]
        for column in range(2):
            self.assertEqual(sum(witness[row] * matrix[row][column]
                                 for row in range(3)) % prime, 0)
        solved = H.solve_factored(factor, [2, 3, 5])
        self.assertTrue(solved["solvable"])
        self.assertEqual(solved["solution"], [2, 3])
        self.assertEqual(solved["nonzero_syndrome_entries"], 0)

    def test_explicit_obstruction_witness(self):
        prime = 7
        matrix = [[1, 0], [0, 1], [1, 1]]
        factor = H.factor_matrix(matrix, prime)
        rhs = [2, 3, 6]
        solved = H.solve_factored(factor, rhs)
        self.assertFalse(solved["solvable"])
        obstruction = solved["obstruction"]
        witness = obstruction["left_kernel_vector"]
        pairing = sum(a * b for a, b in zip(witness, rhs)) % prime
        self.assertEqual(pairing, obstruction["pairing_mod_p"])
        self.assertNotEqual(pairing, 0)

    def test_overdetermined_newton_fixture_through_p6(self):
        # F=(x^2-2,3(x^2-2)); x=3 is the selected root modulo 7.
        prime = 7
        x = 3
        factor = H.factor_matrix([[6], [4]], prime)
        self.assertEqual(factor["rank"], 1)
        self.assertEqual(len(factor["left_cokernel"]), 1)
        for exponent in range(1, 6):
            step = prime ** exponent
            modulus = step * prime
            values = [x * x - 2, 3 * (x * x - 2)]
            self.assertTrue(all(value % step == 0 for value in values))
            rhs = [(-value // step) % prime for value in values]
            solved = H.solve_factored(factor, rhs)
            self.assertTrue(solved["solvable"])
            x = (x + step * solved["solution"][0]) % modulus
            self.assertEqual((x * x - 2) % modulus, 0)


class RadicalAndCoordinateTests(unittest.TestCase):
    def test_registered_radicals_reconstruct_p2_and_continue(self):
        frame = INTEGRAL.REGISTERED_FRAMES[H.PRIME]
        frame, _meta = H.lift_root_frame_digit(frame, H.PRIME, 1)
        self.assertEqual(frame, INTEGRAL.REGISTERED_P2_FRAME_105337)
        for exponent in (2, 3):
            frame, _meta = H.lift_root_frame_digit(
                frame, H.PRIME, exponent)
            INTEGRAL.validate_specialization(
                H.PRIME ** (exponent + 1), frame,
                INTEGRAL.SOURCE_NEWTON_DENOMINATORS)

    def test_exact_coordinate_census(self):
        census = H.tail_census()
        self.assertEqual(census["nominal_tail_coordinates"], 180)
        self.assertEqual(census["effective_tail_coordinates"], 172)
        self.assertEqual(census["nominal_total_coordinates"], 190)
        self.assertEqual(census["essential_total_coordinates"], 182)
        self.assertEqual(len(H.DEAD_TAIL_LABELS), 8)

    def test_structural_dead_tail_gate(self):
        gate = H.structural_dead_tail_gate([6, 8, 10, 42])
        self.assertEqual(gate["dead_plus_minimum_odd"],
                         {"39": 44, "41": 46})
        with self.assertRaises(ValueError):
            H.structural_dead_tail_gate([6, 7, 42])

    def test_coordinate_digit_application(self):
        labels = [("tf1", 6), ("FIX", "W1"), ("X", "alpha")]
        values = {H.coordinate_key(label): value
                  for label, value in zip(labels, (1, 2, 3))}
        got = H.apply_digits(values, labels, [4, 5, 6], 7, 49)
        self.assertEqual(got, {"tf1:6": 29, "FIX:W1": 37,
                               "X:alpha": 45})

    def test_registered_p2_template_relation_and_units_exactly(self):
        modulus = H.PRIME ** 2
        gate = H.template_relation_gate(
            {"FIX:W1": H.REGISTERED_P2_W1,
             "FIX:W2": H.REGISTERED_P2_W2},
            INTEGRAL.REGISTERED_P2_FRAME_105337, modulus)
        self.assertTrue(gate["pass"])
        self.assertEqual(gate["E_residue_modulus"], 0)
        self.assertTrue(gate["W1_unit"] and gate["W2_unit"])
        self.assertEqual(gate["first_term_modulus"], 4315102731)
        self.assertEqual(gate["second_term_modulus"], 6780780838)
        self.assertEqual(H.sha256_json(gate),
                         H.REGISTERED_P2_TEMPLATE_GATE_SHA256)

    def test_template_relation_gate_fails_closed(self):
        frame = INTEGRAL.RootFrame(1, 1, 1, 1, 1)
        relation_failure = H.template_relation_gate(
            {"FIX:W1": 1, "FIX:W2": 1}, frame, 7)
        self.assertFalse(relation_failure["pass"])
        nonunit_failure = H.template_relation_gate(
            {"FIX:W1": 0, "FIX:W2": 1},
            INTEGRAL.RootFrame(1, 1, 0, 0, 1), 7)
        self.assertTrue(nonunit_failure["E_zero"])
        self.assertFalse(nonunit_failure["pass"])


class StateTests(unittest.TestCase):
    def test_atomic_authenticated_roundtrip_and_tamper_rejection(self):
        payload = {"schema": "fixture", "exponent": 2,
                   "coordinates": {"x": 17}}
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "state.json")
            digest = H.write_state(path, payload)
            self.assertEqual(digest, H.sha256_json(payload))
            self.assertEqual(H.load_state(path), payload)
            with open(path, encoding="utf-8") as handle:
                envelope = json.load(handle)
            envelope["payload"]["exponent"] = 3
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(envelope, handle)
            with self.assertRaises(ValueError):
                H.load_state(path)


class SemanticChainHostileTests(unittest.TestCase):
    @staticmethod
    def fixture_context():
        digest = "0" * 64
        return {
            "prime": H.PRIME,
            # Use the registered lightweight E/W data so the mock transition
            # can exercise the exact p -> p^2 template gate without loading
            # the 184-row evaluator.
            "initial_frame": INTEGRAL.REGISTERED_FRAMES[H.PRIME],
            "initial_coordinates": {
                "fixture:x": 3,
                "FIX:W1": H.REGISTERED_P2_W1 % H.PRIME,
                "FIX:W2": H.REGISTERED_P2_W2 % H.PRIME},
            "essential_labels": [
                ("fixture", "x"), ("FIX", "W1"), ("FIX", "W2")],
            "dependency_hashes": {"fixture": {"path": "fixture",
                                                 "sha256": digest}},
            "expected_p2_rhs_sha256": "1" * 64,
            "expected_p2_correction_sha256": "2" * 64,
            "expected_p2_point_sha256": "3" * 64,
            "expected_p2_frame_sha256": "4" * 64,
            "invariants": {
                "essential_labels_sha256": "5" * 64,
                "source_row_labels_sha256": "6" * 64,
                "source_jacobian_sha256": "7" * 64,
                "source_jacobian_rref_sha256": "8" * 64,
                "left_cokernel_basis_sha256": "9" * 64,
                "base_point_coordinates_sha256": "a" * 64,
            },
        }

    @staticmethod
    def successful_transition(_context, payload):
        exponent = payload["exponent"]
        prime = _context["prime"]
        step = prime ** exponent
        modulus = step * prime
        if exponent != 1:
            raise AssertionError("semantic hostile fixture only defines p^2")
        record = {
            "from_exponent": exponent,
            "to_exponent": exponent + 1,
            "result": "SOLVABLE_AND_REPLAYED",
            "input_coordinate_point_sha256": H.sha256_json(
                payload["coordinates"]),
            "correction_sha256": H.sha256_json([1]),
            "coordinate_point_sha256": H.sha256_json({
                "fixture:x": (payload["coordinates"]["fixture:x"] + step)
                % modulus}),
        }
        record, history_hash = H._seal_history_record(payload, record)
        updated = deepcopy(payload)
        updated.update({
            "status": H.STATUS_FINITE,
            "exponent": exponent + 1,
            "modulus": modulus,
            "coordinates": {
                "fixture:x": (payload["coordinates"]["fixture:x"] + step)
                % modulus,
                "FIX:W1": H.REGISTERED_P2_W1,
                "FIX:W2": H.REGISTERED_P2_W2,
            },
            "root_frame": H._frame_dict(
                INTEGRAL.REGISTERED_P2_FRAME_105337),
            "history": list(payload["history"]) + [record],
            "history_sha256": history_hash,
            "finite_conclusion": "fixture",
        })
        updated["template_relation_gate"] = H.template_relation_gate(
            updated["coordinates"], H._frame_from_payload(updated), modulus)
        return updated

    @staticmethod
    def obstructed_transition(_context, payload):
        record = {"from_exponent": payload["exponent"],
                  "to_exponent": payload["exponent"] + 1,
                  "result": H.STATUS_OBSTRUCTED,
                  "obstruction": {"pairing_mod_p": 1}}
        record, history_hash = H._seal_history_record(payload, record)
        updated = deepcopy(payload)
        updated.update({
            "status": H.STATUS_OBSTRUCTED,
            "obstruction_attempted_to_exponent": payload["exponent"] + 1,
            "history": list(payload["history"]) + [record],
            "history_sha256": history_hash,
            "obstruction_scope": "fixture obstruction",
        })
        return updated

    def test_deterministic_initial_and_complete_chain_accept(self):
        context = self.fixture_context()
        initial = H._initial_payload(context)
        with mock.patch.object(H, "lift_one_point_digit",
                               side_effect=self.successful_transition):
            H.validate_resume_payload(initial, context)
            p2 = self.successful_transition(context, initial)
            H.validate_resume_payload(p2, context)

    def test_kernel_shifted_point_with_stale_history_is_rejected(self):
        context = self.fixture_context()
        initial = H._initial_payload(context)
        p2 = self.successful_transition(context, initial)
        shifted = deepcopy(p2)
        # This is the hostile shape: add p times a tangent-kernel digit while
        # retaining the deterministic transition record and its point hash.
        shifted["coordinates"]["fixture:x"] = (
            shifted["coordinates"]["fixture:x"] + context["prime"])
        with mock.patch.object(H, "lift_one_point_digit",
                               side_effect=self.successful_transition):
            with self.assertRaisesRegex(ValueError, "semantic state-chain"):
                H.validate_resume_payload(shifted, context)

    def test_history_scope_claim_status_and_p2_anchor_tampering_rejected(self):
        context = self.fixture_context()
        initial = H._initial_payload(context)
        p2 = self.successful_transition(context, initial)
        mutations = []
        changed = deepcopy(p2)
        changed["history_sha256"] = "f" * 64
        mutations.append(changed)
        changed = deepcopy(p2)
        changed["scope"] = "broader scope"
        mutations.append(changed)
        changed = deepcopy(p2)
        changed["claims"]["forbidden"] = []
        mutations.append(changed)
        changed = deepcopy(p2)
        changed["status"] = H.STATUS_TEMPLATE_FAILED
        mutations.append(changed)
        changed = deepcopy(p2)
        changed["p2_anchor"]["correction_sha256"] = "e" * 64
        mutations.append(changed)
        changed = deepcopy(p2)
        changed["template_relation_gate"]["E_zero"] = False
        mutations.append(changed)
        with mock.patch.object(H, "lift_one_point_digit",
                               side_effect=self.successful_transition):
            for payload in mutations:
                with self.subTest(payload=payload):
                    with self.assertRaises(ValueError):
                        H.validate_resume_payload(payload, context)

    def test_forged_obstruction_rejected_and_real_exponent1_obstruction_accepts(self):
        context = self.fixture_context()
        initial = H._initial_payload(context)
        forged = self.obstructed_transition(context, initial)
        with mock.patch.object(H, "lift_one_point_digit",
                               side_effect=self.successful_transition):
            with self.assertRaisesRegex(ValueError, "not reproduced"):
                H.validate_resume_payload(forged, context)
        with mock.patch.object(H, "lift_one_point_digit",
                               side_effect=self.obstructed_transition):
            H.validate_resume_payload(forged, context)

    @unittest.skipUnless(os.environ.get("JC2_D43_HOSTILE_REAL") == "1",
                         "set JC2_D43_HOSTILE_REAL=1 for bounded real-D43 hostile replay")
    def test_real_d43_free_column67_kernel_shift_is_rejected(self):
        certificate = os.path.join(HERE, "d43_full_certificate_p105337.json")
        reference = os.path.join(HERE, "d43_char0_lift_p105337.json")
        context = H.prepare_d43_context(certificate, reference)
        initial = H._initial_payload(context)
        p2 = H.lift_one_point_digit(context, initial)
        self.assertEqual(p2["status"], H.STATUS_FINITE)
        free_column = 67
        self.assertIn(free_column, context["factor"]["free_columns"])
        kernel = [0] * len(context["essential_labels"])
        kernel[free_column] = 1
        for row, pivot in enumerate(context["factor"]["pivot_columns"]):
            kernel[pivot] = -context["factor"]["rref"][row][free_column] \
                % H.PRIME
        direct = [sum(matrix_row[index] * kernel[index]
                      for index in range(len(kernel))) % H.PRIME
                  for matrix_row in context["essential_jacobian"]]
        self.assertEqual(direct, [0] * 184)
        shifted = deepcopy(p2)
        shifted["coordinates"] = H.apply_digits(
            shifted["coordinates"], context["essential_labels"], kernel,
            H.PRIME, H.PRIME ** 2)
        rows = H.source_rows_with_x(
            context, shifted["coordinates"], H._frame_from_payload(shifted),
            H.PRIME ** 2)
        self.assertEqual(rows, [0] * 184)
        with self.assertRaisesRegex(ValueError, "semantic state-chain"):
            H.validate_resume_payload(shifted, context)


if __name__ == "__main__":
    unittest.main()
