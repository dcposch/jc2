#!/usr/bin/env python3
"""Repaired AWS-only positive-index recursion around the exact V6 point."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V7 = ROOT / "cases/max12_812_order2_affine_faber_a_h17_q7_a3_numeric_prolong_v7_20260826/prolong_h17_q7_numeric_v7.py"
V7_SHA = "f93805c5e5820a1ea16526667fbb2cefac366d9e8924ea118177fd8307d12f8c"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v7():
    if digest(V7) != V7_SHA:
        fail("frozen V7 source mismatch")
    spec = importlib.util.spec_from_file_location("h17_q7_numeric_v7_frozen", V7)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V7 engine")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    v7 = load_v7()
    tag = v7.require_aws()
    v2, base = v7.load_v2()
    field = base.Field(args.characteristic)
    if digest(base.TAILS) != v7.TAILS_SHA:
        fail("frozen tails mismatch")
    tails = json.loads(base.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v7.CANONICAL_SHA:
        fail("canonical tails mismatch")
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    abstract_rows = v2.build_abstract_rows(base, field, tails)
    state = {name: [field.value(0)] * v7.STEPS for name in v7.DEPENDENT}
    initial = (0, 0, Fraction(1, 2), Fraction(-7, 64), Fraction(3, 32), -10, Fraction(8, 5))
    for name, value in zip(v7.DEPENDENT, initial):
        state[name][0] = field.value(value)
    _, initial_functions = v7.transformed(v2, base, field, abstract_rows, state)
    if any(v7.vector_at(initial_functions, 0)):
        fail(("exact leading solution failed", v7.vector_at(initial_functions, 0)))
    matrices = []
    determinants = []
    for index in range(1, v7.STEPS):
        for name in v7.DEPENDENT:
            state[name][index] = field.value(0)
        _, baseline_functions = v7.transformed(v2, base, field, abstract_rows, state)
        baseline = v7.vector_at(baseline_functions, index)
        columns = []
        for name in v7.DEPENDENT:
            state[name][index] = field.value(1)
            _, trial_functions = v7.transformed(v2, base, field, abstract_rows, state)
            trial = v7.vector_at(trial_functions, index)
            columns.append(v7.vec_add(field, trial, v7.vec_scale(field, baseline, -1)))
            state[name][index] = field.value(0)
        matrix = tuple(tuple(columns[column][row] for column in range(len(v7.DEPENDENT))) for row in range(len(v7.DEPENDENT)))
        test_values = tuple(field.value(position + 2) for position in range(len(v7.DEPENDENT)))
        for name, value in zip(v7.DEPENDENT, test_values):
            state[name][index] = value
        _, affine_functions = v7.transformed(v2, base, field, abstract_rows, state)
        actual = v7.vector_at(affine_functions, index)
        predicted = baseline
        for column, value in zip(columns, test_values):
            predicted = v7.vec_add(field, predicted, v7.vec_scale(field, column, value))
        if actual != predicted:
            fail(("non-affine positive-index coefficient", index, actual, predicted))
        for name in v7.DEPENDENT:
            state[name][index] = field.value(0)
        solution, determinant = v7.matrix_solve(field, matrix, v7.vec_scale(field, baseline, -1))
        for name, value in zip(v7.DEPENDENT, solution):
            state[name][index] = value
        _, solved_functions = v7.transformed(v2, base, field, abstract_rows, state)
        if any(v7.vector_at(solved_functions, index)):
            fail(("recursion residual", index, v7.vector_at(solved_functions, index)))
        matrices.append(matrix); determinants.append(determinant)
        print(f"A_H17Q7_PROLONG_V8_STEP={index}:det={field.text(determinant)}", flush=True)
    if any(matrix != matrices[0] for matrix in matrices[1:]):
        fail("positive-index recursion matrix changed")
    expected_det = field.value(Fraction(45, 2**19))
    if any(value != expected_det for value in determinants):
        fail(("wrong recursion determinant", determinants[0], expected_det))
    rows, final_functions = v7.transformed(v2, base, field, abstract_rows, state)
    for index in range(v7.STEPS):
        if any(v7.vector_at(final_functions, index)):
            fail(("final transformed residual", index))
    common_grade = 48 + v7.STEPS - 1
    bad = [(number, grade, rows[number][grade]) for number in range(1, 8) for grade in range(common_grade + 1) if rows[number][grade]]
    if bad:
        fail(("raw-row residual through common grade", bad[:10]))
    payload = {
        "variables": list(v7.DEPENDENT),
        "coefficients": {name: [field.text(value) for value in state[name]] for name in v7.DEPENDENT},
        "matrix": [[field.text(value) for value in row] for row in matrices[0]],
        "determinant": field.text(expected_det),
        "common_raw_zero_through_grade": common_grade,
    }
    payload_bytes = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "prolongation.json").write_bytes(payload_bytes)
    result = {
        "status": "PASS-A-H17-Q7-A3-NUMERIC-PROLONG-V8",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v7_sha256": digest(V7),
        "tails_sha256": digest(base.TAILS),
        "steps": v7.STEPS,
        "determinant": field.text(expected_det),
        "prolongation_sha256": sha256(payload_bytes).hexdigest(),
        "common_raw_zero_through_grade": common_grade,
        "j_first_effective_grade": 57,
        "elapsed_seconds": time.monotonic() - started,
        "scope": "ONE_FIXED_NORMALIZED_H17_Q7_A3_DX_NUMERIC_FORMAL_BRANCH_THROUGH_GRADE72_ONLY_NO_GENERAL_IFT_SOURCE_REES_TAYLOR_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H17Q7_PROLONG_V8_STEPS=25")
    print("A_H17Q7_PROLONG_V8_MATRIX_CONSTANT=1")
    print("A_H17Q7_PROLONG_V8_INITIAL=1")
    print("A_H17Q7_PROLONG_V8_J_CROSSED=1")
    print("A_H17Q7_PROLONG_V8_RAW_ZERO_THROUGH_GRADE=72")
    print("A_H17Q7_PROLONG_V8_SHA256=" + result["prolongation_sha256"])
    print("A_H17Q7_PROLONG_V8_ENDPOINT=PASS_NUMERIC_FORMAL_RECURSION")
    print("A_H17Q7_PROLONG_V8_DONE=1")
    print("A_H17Q7_PROLONG_V8_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
