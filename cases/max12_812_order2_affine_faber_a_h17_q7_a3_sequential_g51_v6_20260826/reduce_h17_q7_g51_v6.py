#!/usr/bin/env python3
"""AWS-only exact Laurent reduction of the frozen H17/q7 V5 rows."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V5 = ROOT / "cases/max12_812_order2_affine_faber_a_h17_q7_a3_through_g51_sparse_v5_20260826"
INPUTS = {
    0: (
        V5 / "evidence/Box03/aws_qg51/output/rows_g48_g51.json",
        V5 / "evidence/Box03/aws_qg51/output/functionals_g51.json",
        "1e626d0832d511a2bea5936eb1d687084f51a58f7f44062af23c3f71e88318ee",
        "71ff2027b1d17c421bb84738a7298eed3f8136d8f488b39ab5f9414767c2542a",
    ),
    65521: (
        V5 / "evidence/Box02/aws_pg51/output/rows_g48_g51.json",
        V5 / "evidence/Box02/aws_pg51/output/functionals_g51.json",
        "f33ab36df9f3a2db2684de2feab0195420926729a8cb8a1bcf43b2b4842d857e",
        "70ffdc19efde934dde590fa5b475b0a73df5b709ded8de9a9a878d9bca41c1a0",
    ),
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


class Field:
    def __init__(self, characteristic: int):
        self.p = characteristic

    def value(self, item: int | Fraction | str):
        if isinstance(item, str):
            item = Fraction(item)
        elif isinstance(item, int):
            item = Fraction(item)
        if self.p == 0:
            return item
        return (item.numerator % self.p) * pow(item.denominator % self.p, -1, self.p) % self.p

    def add(self, left, right):
        value = left + right
        return value if self.p == 0 else value % self.p

    def mul(self, left, right):
        value = left * right
        return value if self.p == 0 else value % self.p

    def neg(self, item):
        return -item if self.p == 0 else (-item) % self.p

    def inv(self, item):
        if not item:
            fail("attempt to invert zero coefficient")
        return 1 / item if self.p == 0 else pow(item, -1, self.p)

    def text(self, item) -> str:
        return str(item)


Monomial = tuple[tuple[str, int], ...]
Poly = dict[Monomial, object]


def canonical_monomial(items) -> Monomial:
    exponents = {}
    for name, exponent in items:
        exponents[name] = exponents.get(name, 0) + exponent
    return tuple(sorted((name, exponent) for name, exponent in exponents.items() if exponent))


def const(field: Field, coefficient) -> Poly:
    coefficient = field.value(coefficient)
    return {} if not coefficient else {(): coefficient}


def monomial(field: Field, coefficient, *items: tuple[str, int]) -> Poly:
    coefficient = field.value(coefficient)
    return {} if not coefficient else {canonical_monomial(items): coefficient}


def add(field: Field, *polys: Poly) -> Poly:
    result: Poly = {}
    for poly in polys:
        for term, coefficient in poly.items():
            value = field.add(result.get(term, field.value(0)), coefficient)
            if value:
                result[term] = value
            elif term in result:
                del result[term]
    return result


def scale(field: Field, poly: Poly, coefficient) -> Poly:
    coefficient = field.value(coefficient)
    if not coefficient:
        return {}
    return {term: field.mul(value, coefficient) for term, value in poly.items() if field.mul(value, coefficient)}


def mul(field: Field, left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for left_term, left_coefficient in left.items():
        for right_term, right_coefficient in right.items():
            term = canonical_monomial((*left_term, *right_term))
            value = field.mul(left_coefficient, right_coefficient)
            total = field.add(result.get(term, field.value(0)), value)
            if total:
                result[term] = total
            elif term in result:
                del result[term]
    return result


def power(field: Field, poly: Poly, exponent: int) -> Poly:
    if exponent < 0:
        fail("negative polynomial power")
    result = const(field, 1)
    factor = poly
    while exponent:
        if exponent & 1:
            result = mul(field, result, factor)
        exponent >>= 1
        if exponent:
            factor = mul(field, factor, factor)
    return result


def parse_poly(field: Field, payload) -> Poly:
    result: Poly = {}
    for term in payload["terms"]:
        parsed = monomial(field, term["coefficient"], *((name, int(exponent)) for name, exponent in term["monomial"]))
        result = add(field, result, parsed)
    return result


def substitute(field: Field, poly: Poly, variable: str, replacement: Poly) -> Poly:
    result: Poly = {}
    for term, coefficient in poly.items():
        exponent = 0
        remainder = []
        for name, degree in term:
            if name == variable:
                exponent = degree
            else:
                remainder.append((name, degree))
        if exponent < 0:
            fail(("solved variable occurs with negative exponent", variable, term))
        piece = monomial(field, coefficient, *remainder)
        if exponent:
            piece = mul(field, piece, power(field, replacement, exponent))
        result = add(field, result, piece)
    return result


def solve_linear_monomial(field: Field, equation: Poly, variable: str) -> Poly:
    coefficient: Poly = {}
    remainder: Poly = {}
    for term, value in equation.items():
        exponent = dict(term).get(variable, 0)
        if exponent > 1 or exponent < 0:
            fail(("nonlinear pivot variable", variable, exponent, term))
        if exponent == 1:
            stripped = tuple((name, degree) for name, degree in term if name != variable)
            coefficient = add(field, coefficient, {stripped: value})
        else:
            remainder = add(field, remainder, {term: value})
    if len(coefficient) != 1:
        fail(("pivot coefficient is not one Laurent monomial", variable, coefficient))
    (pivot_term, pivot_coefficient), = coefficient.items()
    inverse_term = tuple((name, -degree) for name, degree in pivot_term)
    inverse = monomial(field, field.inv(pivot_coefficient), *inverse_term)
    solution = scale(field, mul(field, inverse, remainder), -1)
    if substitute(field, equation, variable, solution):
        fail(("pivot substitution failed", variable))
    return solution


def canonical_poly(field: Field, poly: Poly):
    return {
        "terms": [
            {
                "coefficient": field.text(coefficient),
                "monomial": [[name, exponent] for name, exponent in term],
            }
            for term, coefficient in sorted(poly.items())
        ]
    }


def expected_h(field: Field) -> Poly:
    return add(
        field,
        monomial(field, -2, ("m", 3), ("p", 2)),
        monomial(field, Fraction(5, 4), ("kk0", 1), ("a3", 3), ("p", 7)),
    )


def expected_d60(field: Field) -> Poly:
    return add(
        field,
        monomial(field, 36, ("r00", 1), ("m", 2), ("p", -4)),
        monomial(field, -36, ("y0", 2), ("p", -4)),
        monomial(field, -5, ("kk0", 1), ("a3", 2), ("p", 1)),
        monomial(field, -2, ("m", 3), ("a3", -1), ("p", -4)),
    )


def reduce_chart(field: Field, raw_rows, raw_k: Poly, raw_h: Poly, chart: str):
    rows = {grade: {number: dict(poly) for number, poly in block.items()} for grade, block in raw_rows.items()}
    kfun = dict(raw_k)
    hfun = dict(raw_h)
    solutions: dict[str, Poly] = {}
    lower_residuals = {}
    cross_prefix = "y" if chart == "x" else "x"

    def apply_solution(variable: str, solution: Poly) -> None:
        nonlocal kfun, hfun
        for old_name in tuple(solutions):
            solutions[old_name] = substitute(field, solutions[old_name], variable, solution)
        solutions[variable] = solution
        for grade in range(48, 52):
            for number in range(1, 8):
                rows[grade][number] = substitute(field, rows[grade][number], variable, solution)
        kfun = substitute(field, kfun, variable, solution)
        hfun = substitute(field, hfun, variable, solution)

    for grade in range(48, 52):
        jet = grade - 48
        pivots = ((1, f"s0{jet}"), (3, f"{cross_prefix}{jet}"), (6, f"d2{jet}"), (2, f"dm{jet}"), (4, f"d4{jet}"))
        for number, variable in pivots:
            solution = solve_linear_monomial(field, rows[grade][number], variable)
            apply_solution(variable, solution)
            if rows[grade][number]:
                fail(("pivot row did not vanish globally", chart, grade, number, variable))
        for number in (1, 2, 3, 4, 6):
            if rows[grade][number]:
                fail(("nonzero pivot row after grade reduction", chart, grade, number))
        if grade < 51:
            if rows[grade][5] or rows[grade][7]:
                fail(("unexpected lower compatibility", chart, grade, rows[grade][5], rows[grade][7]))
            lower_residuals[str(grade)] = {"P5": 0, "P7": 0}

    p_poly = monomial(field, 1, ("p", 1))
    row5 = rows[51][5]
    row7 = rows[51][7]
    if kfun != row5:
        fail(("K51 is not reduced P5_51", chart, add(field, kfun, scale(field, row5, -1))))
    h_from_rows = add(field, scale(field, mul(field, p_poly, row5), 16), scale(field, row7, 64))
    if hfun != h_from_rows:
        fail(("H51 row identity failed", chart, add(field, hfun, scale(field, h_from_rows, -1))))
    if hfun != expected_h(field):
        fail(("wrong H51 before K solve", chart, hfun, expected_h(field)))

    d60_solution = solve_linear_monomial(field, kfun, "d60")
    expected = expected_d60(field)
    for variable, solution in solutions.items():
        expected = substitute(field, expected, variable, solution)
    if d60_solution != expected:
        fail(("wrong d60 solution", chart, d60_solution, expected))
    apply_solution("d60", d60_solution)
    row5 = rows[51][5]
    row7 = rows[51][7]
    if kfun or row5:
        fail(("K/P5 did not vanish after d60 solve", chart, kfun, row5))
    if hfun != expected_h(field):
        fail(("H changed after d60 solve", chart, hfun))
    if scale(field, row7, 64) != hfun:
        fail(("extra or wrong P7 residual", chart, row7, hfun))

    return {
        "chart": f"D({chart}0*p*m*a3)",
        "solutions": {name: canonical_poly(field, solution) for name, solution in sorted(solutions.items())},
        "lower_residuals": lower_residuals,
        "K51_after_d60": canonical_poly(field, kfun),
        "P5_51_after_d60": canonical_poly(field, row5),
        "H51": canonical_poly(field, hfun),
        "P7_51": canonical_poly(field, row7),
        "solution_count": len(solutions),
    }


def require_aws() -> str:
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("missing registered AWS lane")
    if platform.system() != "Linux":
        fail("AWS-only engine")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.exists() or "Amazon EC2" not in vendor.read_text():
        fail("AWS-only engine")
    return tag


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    rows_path, functions_path, rows_sha, functions_sha = INPUTS[args.characteristic]
    if digest(rows_path) != rows_sha or digest(functions_path) != functions_sha:
        fail("frozen V5 input mismatch")
    field = Field(args.characteristic)
    rows_payload = json.loads(rows_path.read_text())
    functions_payload = json.loads(functions_path.read_text())
    raw_rows = {
        int(grade): {int(number): parse_poly(field, payload) for number, payload in block.items()}
        for grade, block in rows_payload.items()
    }
    raw_k = parse_poly(field, functions_payload["K51"])
    raw_h = parse_poly(field, functions_payload["Hseries51"])
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    charts = {chart: reduce_chart(field, raw_rows, raw_k, raw_h, chart) for chart in ("x", "y")}
    chart_bytes = (json.dumps(charts, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "chart_reductions.json").write_bytes(chart_bytes)
    result = {
        "status": "PASS-A-H17-Q7-A3-SEQUENTIAL-G51-V6",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "rows_sha256": rows_sha,
        "functionals_sha256": functions_sha,
        "chart_reductions_sha256": sha256(chart_bytes).hexdigest(),
        "charts": ["D(x0*p*m*a3)", "D(y0*p*m*a3)"],
        "pivots_per_chart": 21,
        "lower_compatibilities_zero": 12,
        "K51_solves_d60": 1,
        "sole_residual_H51": 1,
        "elapsed_seconds": time.monotonic() - started,
        "scope": "FIXED_H17_Q7_A3_NORMALIZED_GRAPH_FINITE_REDUCTION_THROUGH_GRADE51_ONLY_NO_ALL_ORDERS_SOURCE_REES_TERMINAL_TAYLOR_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H17Q7G51V6_CHARTS=2")
    print("A_H17Q7G51V6_LOWER_COMPATIBILITIES_ZERO=12")
    print("A_H17Q7G51V6_K51_SOLVES_D60=1")
    print("A_H17Q7G51V6_SOLE_RESIDUAL_H51=1")
    print("A_H17Q7G51V6_REDUCTIONS_SHA256=" + result["chart_reductions_sha256"])
    print("A_H17Q7G51V6_ENDPOINT=PASS_SEQUENTIAL_REDUCTION_THROUGH_GRADE51")
    print("A_H17Q7G51V6_DONE=1")
    print("A_H17Q7G51V6_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
