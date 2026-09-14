#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "ops" / "frontier_gate.py"
GGHV_PDF = ROOT / "box" / "ideation-20260906T1210Z" / "ggvh-2204.14178v1.pdf"
GGHV_TEXT = ROOT / "box" / "ideation-20260906T1210Z" / "ggvh-2204.14178v1.txt"

EXPECTED_GATE_SHA256 = (
    "18367153f8b89126c57557edf8e5c53dddf8475bd617aed47848072c29516812"
)
EXPECTED_GGHV_PDF_SHA256 = (
    "ac18e80cc2391f204f73b908a6a6557eb1141d9fbb5ebdb9f6e0a22121db80bd"
)
EXPECTED_GGHV_TEXT_SHA256 = (
    "f3eca2a560b98784ec787104c8b9049ca44bc3dde4bacb38f121376736d02368"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run_gate_path(gate: Path, *args: str) -> tuple[int, dict[str, Any]]:
    proc = subprocess.run(
        [sys.executable, str(gate), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    return proc.returncode, json.loads(proc.stdout)


def run_gate(*args: str) -> tuple[int, dict[str, Any]]:
    return run_gate_path(GATE, *args)


def external_contract_errors(gate: Path) -> list[str]:
    """Return fixed-oracle failures used to demonstrate mutation sensitivity."""

    errors: list[str] = []
    cases = (
        (
            "cap107",
            ("--total-cap", "107", "--tag", "mutation-oracle-cap107"),
            3,
            "EXCLUDED_BY_EXTERNAL_LT108",
        ),
        (
            "cap108",
            ("--total-cap", "108", "--tag", "mutation-oracle-cap108"),
            0,
            "INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND",
        ),
        (
            "partial-y-unbounded",
            (
                "--partial-y-degrees",
                "99",
                "66",
                "--total-unbounded",
                "--tag",
                "mutation-oracle-partial-y",
            ),
            0,
            "OUT_OF_SCOPE_ACTUAL_TOTAL_UNBOUNDED",
        ),
    )
    for name, argv, expected_rc, expected_conclusion in cases:
        rc, result = run_gate_path(gate, *argv)
        if rc != expected_rc or result["conclusion"] != expected_conclusion:
            errors.append(name)
    return errors


class External108FrontierTests(unittest.TestCase):
    def assert_external_metadata(self, result: dict[str, Any]) -> None:
        self.assertEqual(
            result["external_theorem"]["name"],
            "GGHV-actual-max-total-degree-108",
        )
        self.assertEqual(
            result["external_theorem"]["source"],
            "https://arxiv.org/abs/2204.14178v1",
        )
        self.assertEqual(
            result["external_theorem"]["source_pdf_sha256"],
            EXPECTED_GGHV_PDF_SHA256,
        )
        self.assertEqual(result["trust"]["level"], "CITED_EXTERNAL_THEOREM")
        self.assertEqual(result["trust"]["interface"], "AUDIT17(jjjjjjjjjjjj)")
        self.assertFalse(result["trust"]["external_chain_internally_replayed"])
        self.assertEqual(
            result["actual_degree_context"]["jacobian"], "nonzero constant"
        )
        self.assertFalse(
            result["actual_degree_context"]["declaration_verified_by_gate"]
        )
        self.assertFalse(
            result["actual_degree_context"]["transformed_chart_degrees_supported"]
        )
        self.assertEqual(
            result["tool_metadata"]["review_status"],
            "UNREVIEWED_PENDING_DIFFERENT_MODEL_GATE",
        )
        self.assertTrue(result["tool_metadata"]["manual_external_check_required"])
        self.assertNotIn("OPEN", result["conclusion"])

    def test_actual_99_66_is_external_only_closure(self) -> None:
        rc, result = run_gate(
            "--total-degrees", "99", "66", "--tag", "external-99-66"
        )
        self.assertEqual(rc, 3)
        self.assertEqual(result["theorem"], "GGV-Heitmann-gcd16")
        self.assertEqual(result["source"], "https://arxiv.org/abs/1401.1784")
        self.assertEqual(result["verdict"], "NOT_CLOSED_BY_THIS_GATE")
        self.assertIn("gcd(99,66)=33", result["reason"])
        self.assertEqual(result["conclusion"], "EXCLUDED_BY_EXTERNAL_LT108")
        self.assertEqual(
            result["scope"]["registered_actual_max_total_degree"], 99
        )
        self.assertEqual(result["overall_verdict"], "REFUSE_CLASSICALLY_CLOSED")
        self.assertEqual(result["excluded_by"], ["GGHV-actual-max-total-degree-108"])
        self.assert_external_metadata(result)

    def test_actual_degree_108_boundary_is_inconclusive(self) -> None:
        for deg_p, deg_q in ((108, 72), (108, 108)):
            with self.subTest(degrees=(deg_p, deg_q)):
                rc, result = run_gate(
                    "--total-degrees",
                    str(deg_p),
                    str(deg_q),
                    "--tag",
                    f"external-{deg_p}-{deg_q}",
                )
                self.assertEqual(rc, 0)
                self.assertEqual(result["verdict"], "NOT_CLOSED_BY_THIS_GATE")
                self.assertEqual(
                    result["conclusion"], "INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND"
                )
                self.assertEqual(
                    result["scope"]["registered_actual_max_total_degree"], 108
                )
                self.assertEqual(
                    result["overall_verdict"], "NOT_CLOSED_BY_THIS_GATE"
                )
                self.assertEqual(result["excluded_by"], [])
                self.assert_external_metadata(result)

    def test_gcd_only_closure_still_drives_effective_refusal(self) -> None:
        rc, result = run_gate(
            "--total-degrees", "108", "107", "--tag", "gcd-only-108-107"
        )
        self.assertEqual(rc, 3)
        self.assertEqual(result["verdict"], "REFUSE_CLASSICALLY_CLOSED")
        self.assertEqual(
            result["conclusion"], "INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND"
        )
        self.assertEqual(result["overall_verdict"], "REFUSE_CLASSICALLY_CLOSED")
        self.assertEqual(result["excluded_by"], ["GGV-Heitmann-gcd16"])

    def test_inclusive_caps_distinguish_107_from_108(self) -> None:
        rc107, result107 = run_gate(
            "--total-cap", "107", "--tag", "external-cap-107"
        )
        rc108, result108 = run_gate(
            "--total-cap", "108", "--tag", "external-cap-108"
        )
        self.assertEqual(rc107, 3)
        self.assertEqual(result107["verdict"], "NOT_CLOSED_BY_THIS_GATE")
        self.assertEqual(result107["conclusion"], "EXCLUDED_BY_EXTERNAL_LT108")
        self.assertEqual(
            result107["scope"]["applicability"],
            "IN_SCOPE_COMMON_ACTUAL_TOTAL_DEGREE_CAP",
        )
        self.assertEqual(
            result107["scope"]["registered_actual_max_total_degree_upper_bound"],
            107,
        )
        self.assertNotIn("registered_actual_max_total_degree", result107["scope"])
        self.assertTrue(result107["scope"]["upper_bound_inclusive"])
        self.assertIn("inclusive actual-total cap 107", result107["external_reason"])
        self.assertEqual(
            result107["overall_verdict"], "REFUSE_CLASSICALLY_CLOSED"
        )
        self.assertEqual(rc108, 0)
        self.assertEqual(
            result108["conclusion"], "INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND"
        )
        self.assertEqual(
            result108["overall_verdict"], "NOT_CLOSED_BY_THIS_GATE"
        )

    def test_partial_y_99_66_with_unbounded_totals_is_out_of_scope(self) -> None:
        rc, result = run_gate(
            "--partial-y-degrees",
            "99",
            "66",
            "--total-unbounded",
            "--tag",
            "external-partial-y-99-66",
        )
        self.assertEqual(rc, 0)
        self.assertEqual(result["verdict"], "NOT_CLOSED_BY_THIS_GATE")
        self.assertEqual(
            result["conclusion"], "OUT_OF_SCOPE_ACTUAL_TOTAL_UNBOUNDED"
        )
        self.assertEqual(result["scope"]["applicability"], result["conclusion"])
        self.assertIsNone(result["scope"]["registered_actual_max_total_degree"])
        self.assertEqual(
            result["actual_degree_context"]["degree_measure"],
            "no finite actual-total bound supplied",
        )
        self.assertEqual(result["overall_verdict"], "NOT_CLOSED_BY_THIS_GATE")
        self.assertEqual(result["excluded_by"], [])
        self.assert_external_metadata(result)

    def test_external_closure_requires_explicit_method_control_purpose(self) -> None:
        rc, result = run_gate(
            "--total-degrees",
            "99",
            "66",
            "--purpose",
            "method-control",
            "--tag",
            "external-99-66-control",
        )
        self.assertEqual(rc, 0)
        self.assertEqual(result["purpose"], "method-control")
        self.assertEqual(result["verdict"], "NOT_CLOSED_BY_THIS_GATE")
        self.assertEqual(result["conclusion"], "EXCLUDED_BY_EXTERNAL_LT108")
        self.assertEqual(result["overall_verdict"], "METHOD_CONTROL_ONLY")
        self.assertIn("explicitly labelled method-control", result["overall_reason"])

    def test_legacy_gcd_controls_keep_their_verdicts(self) -> None:
        cases = (
            ("--total-degrees", "9", "12"),
            ("--total-cap", "12"),
        )
        for index, argv in enumerate(cases):
            with self.subTest(argv=argv):
                rc, result = run_gate(*argv, "--tag", f"legacy-gcd-{index}")
                self.assertEqual(rc, 3)
                self.assertEqual(result["verdict"], "REFUSE_CLASSICALLY_CLOSED")
                self.assertEqual(
                    result["overall_verdict"], "REFUSE_CLASSICALLY_CLOSED"
                )
                self.assertIn("GGV-Heitmann-gcd16", result["excluded_by"])

    def test_nonpositive_inputs_remain_argparse_errors(self) -> None:
        cases = (
            ("--total-degrees", "-1", "66"),
            ("--total-cap", "0"),
            (
                "--partial-y-degrees",
                "99",
                "-66",
                "--total-unbounded",
            ),
        )
        for index, argv in enumerate(cases):
            with self.subTest(argv=argv):
                proc = subprocess.run(
                    [sys.executable, str(GATE), *argv, "--tag", f"invalid-{index}"],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(proc.returncode, 2)
                self.assertEqual(proc.stdout, "")
                self.assertIn(
                    "all degrees and caps must be positive integers", proc.stderr
                )

    def test_pinned_implementation_and_primary_source_hashes(self) -> None:
        self.assertEqual(sha256(GATE), EXPECTED_GATE_SHA256)
        self.assertEqual(sha256(GGHV_PDF), EXPECTED_GGHV_PDF_SHA256)
        self.assertEqual(sha256(GGHV_TEXT), EXPECTED_GGHV_TEXT_SHA256)

    def test_actual_source_mutations_are_rejected_by_fixed_oracle(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        before = sha256(GATE)
        self.assertEqual(external_contract_errors(GATE), [])

        boundary_needle = (
            "return actual_max_degree < EXTERNAL_MIN_ACTUAL_MAX_DEGREE"
        )
        partial_needle = (
            "actual_max_degree = None  # Partial-y values are not actual-total bounds."
        )
        self.assertEqual(source.count(boundary_needle), 1)
        self.assertEqual(source.count(partial_needle), 1)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            boundary_mutant = temp_path / "frontier_gate_boundary_mutant.py"
            boundary_mutant.write_text(
                source.replace(
                    boundary_needle,
                    "return actual_max_degree <= EXTERNAL_MIN_ACTUAL_MAX_DEGREE",
                    1,
                ),
                encoding="utf-8",
            )
            partial_mutant = temp_path / "frontier_gate_partial_mutant.py"
            partial_mutant.write_text(
                source.replace(
                    partial_needle,
                    "actual_max_degree = max(deg_y_p, deg_y_q)  # MUTANT",
                    1,
                ),
                encoding="utf-8",
            )

            self.assertIn("cap108", external_contract_errors(boundary_mutant))
            self.assertIn(
                "partial-y-unbounded", external_contract_errors(partial_mutant)
            )

        self.assertEqual(sha256(GATE), before)


if __name__ == "__main__":
    unittest.main()
