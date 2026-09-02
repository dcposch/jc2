#!/usr/bin/env python3
"""Focused, solver-free tests for the N>=6 encoding preflight gate."""
from __future__ import annotations

import json
import hashlib
import sys
import unittest
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from box import preflight as gate  # noqa: E402


GOOD_STACK = gate.StackObservation(
    dict(gate.EXPECTED_PACKAGES), gate.EXPECTED_MSOLVE, "/mock/msolve"
)


class EncodingPreflightTests(unittest.TestCase):
    def run_gate(
        self, manifest: gate.Manifest, solver_input: bytes | None = None
    ) -> gate.PreflightResult:
        # No test invokes msolve or imports qqideal/msolveio.
        payload = gate.render_solver_input(manifest) if solver_input is None else solver_input
        return gate.preflight(
            manifest, solver_input=payload, stack_observation=GOOD_STACK
        )

    def test_faithful_96b_emits_root_and_exact_diffs_every_condition(self) -> None:
        result = self.run_gate(gate.build_reference_manifest("96B"))
        self.assertTrue(result.ok, result.errors)
        self.assertIn("reduced-approximate-root", result.checks)
        self.assertIn("encoded-coefficient-exact-diff", result.checks)
        self.assertIn("open-factor-rabinowitsch", result.checks)
        self.assertIn("solver-input-sha256-and-rows", result.checks)
        # Corrected 96B is g_16,...,g_3=0 with g_2 open.
        manifest = gate.build_reference_manifest("96B")
        self.assertEqual(
            manifest.generator_order,
            tuple(f"g_{j}" for j in range(16, 2, -1)) + ("open_g_2",),
        )

    def test_exact_diff_rejects_root_or_ideal_coefficient_mutation(self) -> None:
        manifest = gate.build_reference_manifest("86A")
        first_root = replace(
            manifest.reduced_root[0],
            expression=manifest.reduced_root[0].expression + "+1",
        )
        bad_root = replace(
            manifest, reduced_root=(first_root,) + manifest.reduced_root[1:]
        )
        self.assertFalse(self.run_gate(bad_root).ok)

        first_condition = replace(
            manifest.ideal_generators[0],
            expression=manifest.ideal_generators[0].expression + "+1",
        )
        bad_condition = replace(
            manifest,
            ideal_generators=(first_condition,) + manifest.ideal_generators[1:],
        )
        result = self.run_gate(bad_condition)
        self.assertFalse(result.ok)
        self.assertIn("exact coefficient diff", result.errors[0])

    def test_old_8619_false_positive_is_rejected_by_corrected_86a(self) -> None:
        ok, checks = gate.run_builtin_canaries()
        self.assertTrue(ok, checks)
        self.assertIn("86A-rejects-old-(8,6,19)", checks)
        # The canary computes forced g_19=11, rather than trusting a flag.
        names, root = gate.algebra.expand_g86(gate.algebra.AUX_A)
        value = gate.algebra.subst_mv(
            gate.algebra.coeff_t(root, 19, names),
            {**gate.algebra._charged_a_point(), "a22": 4},
        ).as_constant()
        self.assertEqual(value, 11)

    def test_four_node_962_curve_passes_corrected_96b(self) -> None:
        ok, checks = gate.run_builtin_canaries()
        self.assertTrue(ok, checks)
        self.assertIn("96B-accepts-four-node-(9,6,2)", checks)

    def test_fail_closed_on_ring_map_open_and_generator_order_mismatch(self) -> None:
        manifest = gate.build_reference_manifest("96B")
        mutations = {
            "ring": replace(manifest, coefficient_field="QQbar"),
            "map": replace(
                manifest,
                map_images=(manifest.map_images[1],) + manifest.map_images[1:],
            ),
            "open": replace(
                manifest,
                open_factors=(
                    replace(
                        manifest.open_factors[0],
                        expression=manifest.open_factors[0].expression + "+1",
                    ),
                ),
            ),
            "order": replace(
                manifest, generator_order=tuple(reversed(manifest.generator_order))
            ),
        }
        for label, malformed in mutations.items():
            with self.subTest(label=label):
                result = self.run_gate(malformed)
                self.assertFalse(result.ok)
                self.assertTrue(result.errors)

    def test_source_fidelity_omitting_minus_2qE1_fails(self) -> None:
        manifest = gate.build_reference_manifest("96B")
        stale = replace(manifest.source_fidelity, encoded_eq2_even="oldEQ2")
        result = self.run_gate(replace(manifest, source_fidelity=stale))
        self.assertFalse(result.ok)
        self.assertIn("EQ2_even source-fidelity mismatch", result.errors[0])

    def test_source_fidelity_cannot_be_renamed_or_vacuous(self) -> None:
        manifest = gate.build_reference_manifest("96B")
        vacuous = gate.SourceFidelity(("x",), "0", "0", "0", "0")
        result = self.run_gate(replace(manifest, source_fidelity=vacuous))
        self.assertFalse(result.ok)
        self.assertIn("generator order", result.errors[0])

    def test_n_below_six_and_stack_drift_fail_closed(self) -> None:
        manifest = gate.build_reference_manifest("96B")
        self.assertFalse(self.run_gate(replace(manifest, degree_n=5)).ok)
        absent = gate.StackObservation(
            {"qqideal": None, "msolveio": None}, None, None
        )
        result = gate.preflight(
            manifest,
            solver_input=gate.render_solver_input(manifest),
            stack_observation=absent,
        )
        self.assertFalse(result.ok)
        self.assertIn("package version gate failed", result.errors[0])

    def test_solver_input_is_required_and_bound_beyond_its_digest(self) -> None:
        manifest = gate.build_reference_manifest("96B")
        missing = gate.preflight(manifest, stack_observation=GOOD_STACK)
        self.assertFalse(missing.ok)
        self.assertIn("solver input bytes/path are required", missing.errors[0])

        original = gate.render_solver_input(manifest).decode("utf-8").splitlines()
        mutations = {}
        variable_lines = list(original)
        variables = variable_lines[0].split(",")
        variables[0], variables[1] = variables[1], variables[0]
        variable_lines[0] = ",".join(variables)
        mutations["variable-order"] = variable_lines
        characteristic_lines = list(original)
        characteristic_lines[1] = "65521"
        mutations["characteristic"] = characteristic_lines
        closed_lines = list(original)
        closed_lines[2] = "0,"
        mutations["closed-generator"] = closed_lines
        open_lines = list(original)
        open_lines[-1] = "0"
        mutations["rabinowitsch-open"] = open_lines

        for label, lines in mutations.items():
            with self.subTest(label=label):
                payload = ("\n".join(lines) + "\n").encode("utf-8")
                # Even if a stale generator updates the manifest digest, parsed
                # ring/characteristic/row comparison must still reject it.
                digest_matched = replace(
                    manifest,
                    solver_input_sha256=hashlib.sha256(payload).hexdigest(),
                )
                result = self.run_gate(digest_matched, payload)
                self.assertFalse(result.ok)
                self.assertTrue(result.errors)

        banked_payload = (ROOT / "box" / "corrected_8611.ms").read_bytes()
        banked_manifest = replace(
            gate.build_reference_manifest("86A"),
            solver_input_sha256=hashlib.sha256(banked_payload).hexdigest(),
        )
        result = self.run_gate(banked_manifest, banked_payload)
        self.assertTrue(result.ok, result.errors)

    def test_json_contract_round_trip(self) -> None:
        manifest = gate.build_reference_manifest("86A")
        payload = json.loads(json.dumps(gate.manifest_to_dict(manifest)))
        parsed = gate.manifest_from_dict(payload)
        self.assertEqual(parsed, manifest)
        self.assertTrue(self.run_gate(parsed).ok)
        payload["misspelled_field"] = True
        with self.assertRaises(gate.PreflightError):
            gate.manifest_from_dict(payload)
        del payload["misspelled_field"]
        payload["degree_n"] = "6"
        with self.assertRaisesRegex(gate.PreflightError, "must be an integer"):
            gate.manifest_from_dict(payload)

        encoded = json.dumps(gate.manifest_to_dict(manifest))
        duplicated = encoded.replace(
            '"degree_n": 6', '"degree_n": 5, "degree_n": 6', 1
        )
        with self.assertRaisesRegex(gate.PreflightError, "duplicate JSON key"):
            gate.manifest_from_json(duplicated)


class TypedTransitionTests(unittest.TestCase):
    def run_gate(self, manifest: gate.Manifest) -> gate.PreflightResult:
        return gate.preflight(
            manifest,
            solver_input=gate.render_solver_input(manifest),
            stack_observation=GOOD_STACK,
        )

    def test_two_field_output_rejects_impossible_pair(self) -> None:
        with self.assertRaises(gate.PreflightError):
            gate.validate_typed_output(
                gate.TypedOutput(
                    gate.Artifact.NUMERICAL_PROFILE, gate.Attainment.ACTUAL_MAP
                )
            )

    def test_rejects_a2_cell_to_b3_kill(self) -> None:
        transition = gate.Transition(
            gate.TypedOutput(gate.Artifact.SUBSYSTEM_POINT, gate.Attainment.REALIZED),
            gate.TypedOutput(gate.Artifact.REPRESENTATION, gate.Attainment.NECESSARY),
            "A2", "B3", claim="KILL",
        )
        with self.assertRaisesRegex(gate.PreflightError, "A2 cell -> B3 kill"):
            gate.validate_transition(transition)

    def test_rejects_local_torsion_to_global_torsion(self) -> None:
        state = gate.TypedOutput(
            gate.Artifact.REPRESENTATION, gate.Attainment.NECESSARY
        )
        transition = gate.Transition(
            state, state, "B3", "B3", "LOCAL", "GLOBAL", "TORSION_ORDER"
        )
        with self.assertRaisesRegex(
            gate.PreflightError, "local torsion -> global torsion"
        ):
            gate.validate_transition(transition)
        with self.assertRaisesRegex(gate.PreflightError, "non-canonical.*scope"):
            gate.validate_transition(replace(transition, source_scope="LOCAL "))

    def test_subsystem_to_full_eo_requires_equations_and_quotient(self) -> None:
        transition = gate.Transition(
            gate.TypedOutput(gate.Artifact.SUBSYSTEM_POINT, gate.Attainment.REALIZED),
            gate.TypedOutput(gate.Artifact.FULL_EO_POINT, gate.Attainment.REALIZED),
            "A2", "A2", arrows=(gate.Arrow.FULL_EO_EQUATIONS,),
        )
        with self.assertRaisesRegex(gate.PreflightError, "DECLARED_QUOTIENT"):
            gate.validate_transition(transition)
        gate.validate_transition(
            replace(transition, arrows=tuple(gate._FULL_EO_ARROWS))
        )

    def test_full_eo_to_actual_map_requires_every_declared_arrow(self) -> None:
        source = gate.TypedOutput(
            gate.Artifact.FULL_EO_POINT, gate.Attainment.REALIZED
        )
        target = gate.TypedOutput(
            gate.Artifact.POLYNOMIAL_PAIR, gate.Attainment.ACTUAL_MAP
        )
        missing_source_chart = gate.Transition(
            source, target, "A2", "A2", arrows=tuple(gate._PULLBACK_ARROWS)
        )
        with self.assertRaisesRegex(gate.PreflightError, "SOURCE_CHART"):
            gate.validate_transition(missing_source_chart)
        complete = replace(missing_source_chart, arrows=tuple(gate._MAP_ARROWS))
        gate.validate_transition(complete)

    def test_advanced_output_must_end_a_checked_provenance_path(self) -> None:
        manifest = gate.build_reference_manifest("96B")
        actual = gate.TypedOutput(
            gate.Artifact.POLYNOMIAL_PAIR, gate.Attainment.ACTUAL_MAP
        )
        uncertified = self.run_gate(replace(manifest, output=actual))
        self.assertFalse(uncertified.ok)
        self.assertIn("no checked provenance path", uncertified.errors[0])

        subsystem = gate.TypedOutput(
            gate.Artifact.SUBSYSTEM_POINT, gate.Attainment.REALIZED
        )
        full_eo = gate.TypedOutput(
            gate.Artifact.FULL_EO_POINT, gate.Attainment.REALIZED
        )
        pullback = gate.TypedOutput(
            gate.Artifact.FULL_EO_POINT, gate.Attainment.ADMISSIBLE_PULLBACK
        )
        transitions = (
            gate.Transition(
                subsystem, full_eo, "A2", "A2",
                arrows=tuple(gate._FULL_EO_ARROWS),
            ),
            gate.Transition(
                full_eo, pullback, "A2", "A2",
                arrows=tuple(gate._PULLBACK_ARROWS),
            ),
            gate.Transition(
                pullback, actual, "A2", "A2",
                arrows=(gate.Arrow.SOURCE_CHART,),
            ),
        )
        certified = self.run_gate(
            replace(manifest, output=actual, transitions=transitions)
        )
        self.assertTrue(certified.ok, certified.errors)

        self_loop = gate.Transition(actual, actual, "A2", "A2")
        result = self.run_gate(
            replace(manifest, output=actual, transitions=(self_loop,))
        )
        self.assertFalse(result.ok)
        self.assertIn("identical", result.errors[0])

        late_start = transitions[-1:]
        result = self.run_gate(
            replace(manifest, output=actual, transitions=late_start)
        )
        self.assertFalse(result.ok)
        self.assertIn("complete subsystem-to-output ladder", result.errors[0])

        counterexample = gate.TypedOutput(
            gate.Artifact.POLYNOMIAL_PAIR,
            gate.Attainment.COUNTEREXAMPLE_CERTIFIED,
        )
        result = self.run_gate(replace(manifest, output=counterexample))
        self.assertFalse(result.ok)
        self.assertIn("no checked provenance path", result.errors[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
