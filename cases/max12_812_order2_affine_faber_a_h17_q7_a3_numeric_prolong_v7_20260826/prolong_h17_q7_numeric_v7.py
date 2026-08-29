#!/usr/bin/env python3
"""AWS-only numeric coefficient recursion for the H17/q7/a3 receiver."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V2 = ROOT / "cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v2_20260826/compute_h17_q7_g48_sparse.py"
V2_SHA = "1ee515a8da4bc86ade10a86dae6a526c57d58eea0061158b977eab2b76020cf4"
TAILS_SHA = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"
CANONICAL_SHA = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
STEPS = 25
MAX_GRADE = 51 + STEPS - 1
DEPENDENT = ("s0", "y", "d2", "dm", "d4", "d6", "kk")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if platform.system() != "Linux" or not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2" or not tag:
        fail("registered AWS lane required")
    return tag


def load_v2():
    if digest(V2) != V2_SHA:
        fail("frozen V2 source mismatch")
    spec = importlib.util.spec_from_file_location("h17_q7_v2_numeric", V2)
    if spec is None or spec.loader is None:
        fail("cannot import frozen source compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.MAX_GRADE = MAX_GRADE
    base = module.load_base()
    base.MAX_GRADE = MAX_GRADE
    return module, base


def zero_series(field):
    return tuple(field.value(0) for _ in range(MAX_GRADE + 1))


def series_from(field, terms):
    result = list(zero_series(field))
    for grade, coefficient in terms:
        if 0 <= grade <= MAX_GRADE:
            result[grade] = field.add(result[grade], field.value(coefficient))
    return tuple(result)


def add(base, field, *items):
    return base.scalar_series_add(field, *items)


def scale(base, field, item, scalar):
    return base.scalar_series_scale(field, item, scalar)


def mul(base, field, left, right):
    return base.scalar_series_mul(field, left, right)


def power(base, field, item, exponent):
    return base.scalar_series_pow(field, item, exponent)


def shift(field, coefficients, grade):
    return series_from(field, ((grade + index, coefficient) for index, coefficient in enumerate(coefficients)))


def source_series(base, field, state):
    one = field.value(1)
    a = series_from(field, ((3, one),))
    e = series_from(field, ((0, one),))
    m = series_from(field, ((0, one),))
    x = series_from(field, ((7, one),))
    y = shift(field, state["y"], 7)
    r0 = zero_series(field); r1 = zero_series(field); s1 = zero_series(field)
    s0 = shift(field, state["s0"], 14)
    kk = shift(field, state["kk"], 0)
    d6 = shift(field, state["d6"], 6)
    d2 = shift(field, state["d2"], 6)
    dm = shift(field, state["dm"], 6)
    e2 = mul(base, field, e, e); e4 = mul(base, field, e2, e2); e6 = mul(base, field, e4, e2)
    k10 = shift(field, kk, 42)
    k6_inner = add(base, field, scale(base, field, mul(base, field, kk, e2), Fraction(15, 32)), d6)
    k2_inner = add(base, field, scale(base, field, mul(base, field, kk, e4), Fraction(15, 256)), d2)
    mu2_inner = add(base, field, scale(base, field, mul(base, field, kk, e6), Fraction(-5, 4096)), dm)
    k6 = shift(field, k6_inner, 42)
    k2 = shift(field, k2_inner, 42)
    mu2 = shift(field, mu2_inner, 42)
    mu4 = shift(field, state["d4"], 48)
    mu6 = zero_series(field)
    jeff = series_from(field, ((57, Fraction(1, 4)),))
    lam = series_from(field, ((17, one),))
    abstract = {
        "J": zero_series(field), "K2": k2, "K6": k6, "K10": k10,
        "S0": s0, "S1": s1, "R0": r0, "R1": r1,
        "Y": y, "X": x, "a": a, "lambda": lam, "M": m, "E": e,
    }
    return abstract, mu2, mu4, mu6, jeff


def expand_rows(v2, base, field, abstract_rows, source):
    one = series_from(field, ((0, 1),))
    power_cache = {}

    def series_power(name, exponent):
        key = (name, exponent)
        if key not in power_cache:
            power_cache[key] = power(base, field, source[name], exponent)
        return power_cache[key]

    rows = {}
    for number in range(1, 8):
        result = zero_series(field)
        for monomial, coefficient in abstract_rows[number].items():
            term = one
            for name, exponent in zip(base.ABS_VARS, monomial):
                if exponent:
                    term = mul(base, field, term, series_power(name, exponent))
            result = add(base, field, result, scale(base, field, term, coefficient))
        rows[number] = result
    return rows


def transformed(v2, base, field, abstract_rows, state):
    source, mu2, mu4, mu6, jeff = source_series(base, field, state)
    rows = expand_rows(v2, base, field, abstract_rows, source)
    rows[2] = add(base, field, rows[2], scale(base, field, mu2, -1))
    rows[4] = add(base, field, rows[4], scale(base, field, mu4, -1))
    rows[6] = add(base, field, rows[6], scale(base, field, mu6, -1))
    rows[7] = add(base, field, rows[7], scale(base, field, jeff, -1))
    for number in range(1, 8):
        if any(rows[number][grade] for grade in range(48)):
            fail(("row below grade48", number))
    a = source["a"]; e = source["E"]
    b = scale(base, field, a, 4)
    b2 = mul(base, field, b, b); b3 = mul(base, field, b2, b); b4 = mul(base, field, b2, b2)
    e2 = mul(base, field, e, e); e3 = mul(base, field, e2, e)
    h3 = add(
        base, field, rows[3], scale(base, field, mul(base, field, b, rows[2]), Fraction(-1, 2)),
        mul(base, field, add(base, field, scale(base, field, b2, Fraction(5, 32)), scale(base, field, e, Fraction(-1, 4))), rows[1]),
    )
    h5 = add(
        base, field, rows[5], scale(base, field, mul(base, field, b, rows[4]), -1),
        mul(base, field, add(base, field, scale(base, field, b2, Fraction(21, 32)), scale(base, field, e, Fraction(-3, 4))), rows[3]),
        mul(base, field, add(base, field, scale(base, field, b3, Fraction(-5, 16)), scale(base, field, mul(base, field, b, e), Fraction(3, 4))), rows[2]),
        mul(base, field, add(base, field, scale(base, field, b4, Fraction(195, 2048)), scale(base, field, mul(base, field, b2, e), Fraction(-45, 128)), scale(base, field, e2, Fraction(5, 32))), rows[1]),
    )
    kfun = add(base, field, mul(base, field, e, h3), h5)
    hfun = add(base, field, scale(base, field, mul(base, field, e2, rows[3]), 2), scale(base, field, mul(base, field, e, rows[5]), 16), scale(base, field, rows[7], 64), scale(base, field, mul(base, field, e3, rows[1]), Fraction(-1, 2)))
    if any(kfun[grade] for grade in range(51)):
        fail(("K below grade51", [(g, kfun[g]) for g in range(51) if kfun[g]]))
    if any(hfun[grade] for grade in range(51)):
        fail(("H below grade51", [(g, hfun[g]) for g in range(51) if hfun[g]]))
    functions = (rows[1], rows[3], rows[6], rows[2], rows[4], kfun, hfun)
    shifts = (48, 48, 48, 48, 48, 51, 51)
    return rows, tuple(tuple(item[shift + n] for n in range(STEPS)) for item, shift in zip(functions, shifts))


def vector_at(functions, index):
    return tuple(item[index] for item in functions)


def vec_add(field, left, right):
    return tuple(field.add(a, b) for a, b in zip(left, right))


def vec_scale(field, vector, scalar):
    scalar = field.value(scalar)
    return tuple(field.mul(scalar, value) for value in vector)


def matrix_solve(field, matrix, rhs):
    size = len(rhs)
    aug = [list(row) + [rhs[index]] for index, row in enumerate(matrix)]
    determinant = field.value(1)
    sign = 1
    for column in range(size):
        pivot = next((row for row in range(column, size) if aug[row][column]), None)
        if pivot is None:
            fail(("singular recursion matrix", column))
        if pivot != column:
            aug[column], aug[pivot] = aug[pivot], aug[column]
            sign *= -1
        pivot_value = aug[column][column]
        determinant = field.mul(determinant, pivot_value)
        inverse = Fraction(1, 1) / pivot_value if field.p == 0 else pow(pivot_value, -1, field.p)
        aug[column] = [field.mul(value, inverse) for value in aug[column]]
        for row in range(size):
            if row == column or not aug[row][column]:
                continue
            factor = aug[row][column]
            aug[row] = [field.add(value, field.neg(field.mul(factor, pivot_value2))) for value, pivot_value2 in zip(aug[row], aug[column])]
    if sign < 0:
        determinant = field.neg(determinant)
    return tuple(aug[index][-1] for index in range(size)), determinant


def field_text(field, value):
    return field.text(value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    v2, base = load_v2()
    field = base.Field(args.characteristic)
    if digest(base.TAILS) != TAILS_SHA:
        fail("frozen tails mismatch")
    tails = json.loads(base.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != CANONICAL_SHA:
        fail("canonical tails mismatch")
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    abstract_rows = v2.build_abstract_rows(base, field, tails)
    state = {name: [field.value(0)] * STEPS for name in DEPENDENT}
    matrices = []
    determinants = []
    for index in range(STEPS):
        for name in DEPENDENT:
            state[name][index] = field.value(0)
        _, baseline_functions = transformed(v2, base, field, abstract_rows, state)
        baseline = vector_at(baseline_functions, index)
        columns = []
        for name in DEPENDENT:
            state[name][index] = field.value(1)
            _, trial_functions = transformed(v2, base, field, abstract_rows, state)
            trial = vector_at(trial_functions, index)
            columns.append(vec_add(field, trial, vec_scale(field, baseline, -1)))
            state[name][index] = field.value(0)
        matrix = tuple(tuple(columns[column][row] for column in range(len(DEPENDENT))) for row in range(len(DEPENDENT)))
        test_values = tuple(field.value(position + 2) for position in range(len(DEPENDENT)))
        for name, value in zip(DEPENDENT, test_values):
            state[name][index] = value
        _, affine_functions = transformed(v2, base, field, abstract_rows, state)
        actual = vector_at(affine_functions, index)
        predicted = baseline
        for column, value in zip(columns, test_values):
            predicted = vec_add(field, predicted, vec_scale(field, column, value))
        if actual != predicted:
            fail(("non-affine new coefficient", index, actual, predicted))
        for name in DEPENDENT:
            state[name][index] = field.value(0)
        solution, determinant = matrix_solve(field, matrix, vec_scale(field, baseline, -1))
        for name, value in zip(DEPENDENT, solution):
            state[name][index] = value
        _, solved_functions = transformed(v2, base, field, abstract_rows, state)
        if any(vector_at(solved_functions, index)):
            fail(("recursion residual", index, vector_at(solved_functions, index)))
        matrices.append(matrix); determinants.append(determinant)
        print(f"A_H17Q7_PROLONG_STEP={index}:det={field.text(determinant)}", flush=True)
    if any(matrix != matrices[0] for matrix in matrices[1:]):
        fail("recursion matrix changed")
    expected_det = field.value(Fraction(45, 2**19))
    if any(value != expected_det for value in determinants):
        fail(("wrong recursion determinant", determinants[0], expected_det))
    expected_initial = (0, 0, Fraction(1, 2), Fraction(-7, 64), Fraction(3, 32), -10, Fraction(8, 5))
    if tuple(state[name][0] for name in DEPENDENT) != tuple(field.value(value) for value in expected_initial):
        fail(("wrong initial solution", tuple(state[name][0] for name in DEPENDENT)))
    rows, final_functions = transformed(v2, base, field, abstract_rows, state)
    for index in range(STEPS):
        if any(vector_at(final_functions, index)):
            fail(("final transformed residual", index))
    common_grade = 48 + STEPS - 1
    if any(rows[number][grade] for number in range(1, 8) for grade in range(common_grade + 1)):
        bad = [(number, grade, rows[number][grade]) for number in range(1, 8) for grade in range(common_grade + 1) if rows[number][grade]]
        fail(("raw-row residual through common grade", bad[:10]))
    payload = {
        "variables": list(DEPENDENT),
        "coefficients": {name: [field.text(value) for value in state[name]] for name in DEPENDENT},
        "matrix": [[field.text(value) for value in row] for row in matrices[0]],
        "determinant": field.text(expected_det),
        "common_raw_zero_through_grade": common_grade,
    }
    payload_bytes = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "prolongation.json").write_bytes(payload_bytes)
    result = {
        "status": "PASS-A-H17-Q7-A3-NUMERIC-PROLONG-V7",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(base.TAILS),
        "steps": STEPS,
        "determinant": field.text(expected_det),
        "prolongation_sha256": sha256(payload_bytes).hexdigest(),
        "common_raw_zero_through_grade": common_grade,
        "j_first_effective_grade": 57,
        "elapsed_seconds": time.monotonic() - started,
        "scope": "ONE_FIXED_NORMALIZED_H17_Q7_A3_DX_NUMERIC_FORMAL_BRANCH_THROUGH_GRADE72_ONLY_NO_GENERAL_IFT_SOURCE_REES_TAYLOR_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H17Q7_PROLONG_STEPS=25")
    print("A_H17Q7_PROLONG_MATRIX_CONSTANT=1")
    print("A_H17Q7_PROLONG_INITIAL=1")
    print("A_H17Q7_PROLONG_J_CROSSED=1")
    print("A_H17Q7_PROLONG_RAW_ZERO_THROUGH_GRADE=72")
    print("A_H17Q7_PROLONG_SHA256=" + result["prolongation_sha256"])
    print("A_H17Q7_PROLONG_ENDPOINT=PASS_NUMERIC_FORMAL_RECURSION")
    print("A_H17Q7_PROLONG_DONE=1")
    print("A_H17Q7_PROLONG_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
