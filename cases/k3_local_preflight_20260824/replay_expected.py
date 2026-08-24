#!/usr/bin/env python3
"""Fail-closed replay for the frozen K3 local preflight summary.

This wrapper does not trust the hand-written summary.  It reruns preflight.py,
pins its canonical stdout to the digest frozen in the producer report, derives
the Stage-B routing verdict from the preregistered limits, and reconstructs
every field of result.json before requiring exact equality.
"""

from __future__ import annotations

import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
PREFLIGHT = HERE / "preflight.py"
PREREGISTRATION = HERE / "PREREGISTRATION.md"
EXPECTED_RESULT = HERE / "result.json"
PRODUCER_REPORT = REPO / "xmodel/k3-local-preflight-20260824.md"

EXPECTED_STDOUT_SHA256 = (
    "64704d211aad05766f4f75b39f44e66c1370ca718495a45d3387917c5e9c8a40"
)

NUMBER_WORDS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{label} is not a JSON object")
    return value


def require_bool(value: Any, label: str) -> bool:
    if type(value) is not bool:
        fail(f"{label} is not a JSON boolean")
    return value


def parse_limit(token: str) -> int:
    if token.isdigit():
        return int(token)
    if token not in NUMBER_WORDS:
        fail(f"unrecognized preregistered numeric limit {token!r}")
    return NUMBER_WORDS[token]


def preregistered_limits() -> tuple[int, int, int]:
    text = PREREGISTRATION.read_text(encoding="utf-8")
    size_match = re.search(
        r"leaving\s+\*\*at most ([a-z0-9]+)\*\*\s+local parameters"
        r"\s+and\s+\*\*at most ([a-z0-9]+)\*\*\s+residual nonlinear equations",
        text,
        flags=re.IGNORECASE,
    )
    term_match = re.search(
        r"no\s+more than\s+(\d+)\s+total residual terms", text,
        flags=re.IGNORECASE,
    )
    if size_match is None or term_match is None:
        fail("could not parse all Stage-B limits from PREREGISTRATION.md")
    return (
        parse_limit(size_match.group(1).lower()),
        parse_limit(size_match.group(2).lower()),
        int(term_match.group(1)),
    )


def report_stdout_sha256() -> str:
    text = PRODUCER_REPORT.read_text(encoding="utf-8")
    match = re.search(
        r"\|\s*canonical stdout of `preflight\.py`\s*"
        r"\|\s*`([0-9a-f]{64})`\s*\|",
        text,
    )
    if match is None:
        fail("producer report has no uniquely parseable canonical stdout digest")
    return match.group(1)


MONOMIAL_RE = re.compile(r"x\^(\d+)y\^(\d+)$")


def monomial_text(label: str) -> str:
    match = MONOMIAL_RE.fullmatch(label)
    if match is None:
        fail(f"invalid Jacobian monomial label {label!r}")
    x_degree, y_degree = map(int, match.groups())
    factors: list[str] = []
    if x_degree:
        factors.append("x" if x_degree == 1 else f"x^{x_degree}")
    if y_degree:
        factors.append("y" if y_degree == 1 else f"y^{y_degree}")
    return "*".join(factors) or "1"


def polynomial_text(coefficients: Any, labels: Any, name: str) -> str:
    if not isinstance(coefficients, list) or not isinstance(labels, list):
        fail(f"{name} is not represented by parallel JSON lists")
    if len(coefficients) != len(labels):
        fail(f"{name} coefficient and monomial lists have different lengths")

    terms: list[tuple[int, str]] = []
    for coefficient, label in zip(coefficients, labels):
        if type(coefficient) is not int or not isinstance(label, str):
            fail(f"{name} has a nonintegral coefficient or invalid monomial")
        if coefficient:
            terms.append((coefficient, monomial_text(label)))
    if not terms:
        return "0"

    rendered = ""
    for index, (coefficient, monomial) in enumerate(terms):
        magnitude = abs(coefficient)
        if monomial == "1":
            body = str(magnitude)
        elif magnitude == 1:
            body = monomial
        else:
            body = f"{magnitude}*{monomial}"
        if index == 0:
            rendered = ("-" if coefficient < 0 else "") + body
        else:
            rendered += (" - " if coefficient < 0 else " + ") + body
    return rendered


def registered_solution_text(raw: dict[str, Any]) -> str:
    first = require_dict(raw.get("first_obstruction"), "first_obstruction")
    controls = require_dict(raw.get("controls"), "controls")
    correction = require_dict(
        controls.get("registered_correction_mod3"),
        "controls.registered_correction_mod3",
    )
    registered = require_dict(
        first.get("registered_solution"),
        "first_obstruction.registered_solution",
    )
    vector = require_dict(
        correction.get("vector"),
        "controls.registered_correction_mod3.vector",
    )
    if registered != vector or len(registered) != 1:
        fail("registered obstruction solutions disagree or are not one-coordinate")
    name, value = next(iter(registered.items()))
    if not isinstance(name, str) or type(value) is not int:
        fail("registered obstruction solution has an invalid coordinate")
    correction_q = correction.get("Q")
    if not isinstance(correction_q, str):
        fail("registered Q correction is not a string")
    return f"delta_{name}={value}, i.e. B={correction_q}"


def derive_summary(raw: dict[str, Any], stdout_digest: str) -> dict[str, Any]:
    if raw.get("verdict") != "STAGE-A-PASS":
        fail(f"preflight verdict is {raw.get('verdict')!r}, not STAGE-A-PASS")

    scheme = require_dict(raw.get("scheme"), "scheme")
    controls = require_dict(raw.get("controls"), "controls")
    tangent = require_dict(raw.get("tangent"), "tangent")
    first = require_dict(raw.get("first_obstruction"), "first_obstruction")
    stage = require_dict(raw.get("stage_b_metrics"), "stage_b_metrics")

    parameter_limit, equation_limit, term_limit = preregistered_limits()
    if stage.get("launch_threshold_parameters") != parameter_limit:
        fail("preflight parameter limit disagrees with preregistration")
    if stage.get("launch_threshold_residual_equations") != equation_limit:
        fail("preflight equation limit disagrees with preregistration")
    if term_limit != 120:
        fail(f"unexpected frozen residual-term limit {term_limit}")

    remaining = stage.get("remaining_local_parameters")
    residual_equations = stage.get("zero_linear_part_equations")
    if type(remaining) is not int or type(residual_equations) is not int:
        fail("Stage-B size metrics are not integers")
    parameters_fail = remaining > parameter_limit
    equations_fail = residual_equations > equation_limit
    if not parameters_fail or not equations_fail:
        fail(
            "frozen run no longer fails both size limits; residual-term and "
            "transformation-data gates require a new preregistered computation"
        )
    launched = False
    verdict = "COMPILER-READY/HEAVY"

    equation_order = scheme.get("jacobian_equation_order")
    seed_values = controls.get("seed_equation_values_over_Z")
    divided_error = first.get("divided_error_vector_mod3")
    required_image = first.get("required_linear_image_mod3")

    seed_pass = require_bool(controls.get("seed_mod3_pass"), "controls.seed_mod3_pass")
    lift_pass = require_bool(controls.get("lift_mod9_pass"), "controls.lift_mod9_pass")
    promoted_pass = require_bool(
        controls.get("promoted_mod9_pass"), "controls.promoted_mod9_pass"
    )
    obstruction_zero = require_bool(
        first.get("class_vanishes"), "first_obstruction.class_vanishes"
    )
    marked_images = controls.get("promoted_marked_images_mod9")
    marked_pass = marked_images == [[0, 0], [0, 0]]

    return {
        "verdict": verdict,
        "stdout_sha256": stdout_digest,
        "scheme": {
            "raw_coefficients": scheme.get("raw_coefficient_count"),
            "collision_linear_eliminations": len(
                scheme.get("collision_eliminations", [])
            ),
            "normalized_variables": len(scheme.get("normalized_variables", [])),
            "jacobian_equations": scheme.get("equation_count"),
            "total_nonzero_equation_terms": scheme.get("total_nonzero_terms"),
            "maximum_terms_per_equation": scheme.get("max_terms_in_equation"),
        },
        "controls": {
            "special_fibre_mod3": "PASS" if seed_pass else "FAIL",
            "promoted_mod9_lift": (
                "PASS" if lift_pass and promoted_pass else "FAIL"
            ),
            "normalized_mod9_determinant": controls.get(
                "normalized_lift_determinant"
            ),
            "promoted_mod9_determinant": controls.get(
                "promoted_representative_determinant"
            ),
            "marked_collision_mod9": "PASS" if marked_pass else "FAIL",
        },
        "tangent": {
            "field": tangent.get("field"),
            "rank": tangent.get("rank"),
            "dimension": tangent.get("dimension"),
            "pivot_columns": tangent.get("pivot_columns"),
            "free_columns": tangent.get("free_columns"),
        },
        "first_obstruction": {
            "integer_seed_jacobian_error": polynomial_text(
                seed_values, equation_order, "integer seed Jacobian error"
            ),
            "divided_error_mod3": polynomial_text(
                divided_error, equation_order, "divided error"
            ),
            "required_tangent_image_mod3": polynomial_text(
                required_image, equation_order, "required tangent image"
            ),
            "class": "zero" if obstruction_zero else "nonzero",
            "registered_solution": registered_solution_text(raw),
        },
        "stage_b": {
            "remaining_local_parameters": remaining,
            "equations_with_zero_linear_part": residual_equations,
            "parameter_threshold": parameter_limit,
            "residual_equation_threshold": equation_limit,
            "launched": launched,
            "reason": (
                "both preregistered size thresholds fail; no "
                "transformation-tracking mixed-characteristic local "
                "standard-basis run was licensed"
            ),
        },
    }


def main() -> None:
    recorded_report_digest = report_stdout_sha256()
    if recorded_report_digest != EXPECTED_STDOUT_SHA256:
        fail(
            "producer report stdout digest changed: "
            f"{recorded_report_digest} != {EXPECTED_STDOUT_SHA256}"
        )

    completed = subprocess.run(
        [sys.executable, str(PREFLIGHT)],
        cwd=REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        fail(
            f"preflight.py exited {completed.returncode}: "
            f"{completed.stderr.decode('utf-8', errors='replace').strip()}"
        )
    if completed.stderr:
        fail(
            "preflight.py emitted stderr: "
            + completed.stderr.decode("utf-8", errors="replace").strip()
        )

    stdout_digest = sha256(completed.stdout)
    if stdout_digest != recorded_report_digest:
        fail(
            "canonical stdout digest mismatch: "
            f"{stdout_digest} != {recorded_report_digest}"
        )
    try:
        raw = require_dict(json.loads(completed.stdout), "preflight stdout")
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        fail(f"preflight stdout is not canonical JSON: {error}")

    expected = require_dict(
        json.loads(EXPECTED_RESULT.read_text(encoding="utf-8")), "result.json"
    )
    derived = derive_summary(raw, stdout_digest)
    if expected != derived:
        expected_text = json.dumps(expected, indent=2, sort_keys=True).splitlines()
        derived_text = json.dumps(derived, indent=2, sort_keys=True).splitlines()
        difference = "\n".join(
            difflib.unified_diff(
                expected_text,
                derived_text,
                fromfile="result.json",
                tofile="freshly derived summary",
                lineterm="",
            )
        )
        fail("result.json differs from the freshly derived summary:\n" + difference)

    print(
        f"PASS {derived['verdict']} stdout_sha256={stdout_digest} "
        "summary=EXACT-MATCH"
    )


if __name__ == "__main__":
    main()
