#!/usr/bin/env python3
"""Exact polynomial-identity replay for Opus5's ordered-a1 cascade."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V37 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/solve_graded_ladder_v37.py"
V37_SHA256 = "ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> None:
    raise RuntimeError(message)


def load_v37():
    if digest(V37) != V37_SHA256:
        fail(("V37 compiler hash", digest(V37)))
    spec = importlib.util.spec_from_file_location("cascade_review_v37", V37)
    if spec is None or spec.loader is None:
        fail("V37 import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    v37 = load_v37()
    parser, row_items, row_hashes, _ = v37.load_rows()
    rows = {item["name"]: item["polynomial"] for item in row_items}

    def const(value):
        value = Fraction(value)
        return {(): value} if value else {}

    def variable(name):
        return {((name, 1),): Fraction(1)}

    def scale(polynomial, value):
        value = Fraction(value)
        return {monomial: value * coefficient for monomial, coefficient in polynomial.items() if value * coefficient}

    def add(*polynomials):
        answer = {}
        for polynomial in polynomials:
            answer = parser.add(answer, polynomial)
        return answer

    def product(*polynomials):
        answer = const(1)
        for polynomial in polynomials:
            answer = parser.multiply(answer, polynomial)
        return answer

    def substitute(polynomial, replacements):
        answer = {}
        for monomial, coefficient in polynomial.items():
            term = const(coefficient)
            for name, exponent in monomial:
                term = parser.multiply(term, parser.power(replacements.get(name, variable(name)), exponent))
                if not term:
                    break
            answer = parser.add(answer, term)
        return answer

    def assert_equal(label, actual, expected):
        residual = add(actual, scale(expected, -1))
        if residual:
            fail((label, parser.polynomial_text(residual)))

    a1 = variable("a1")
    ell1 = variable("ell1")
    ell2 = variable("ell2")
    aa0 = variable("aa0")
    e0 = variable("e0")
    e1 = variable("e1")
    ee0 = variable("ee0")
    ee1 = variable("ee1")
    ec3 = variable("ec3")
    ec4 = variable("ec4")
    ez3 = variable("ez3")
    cs1 = variable("cs1")
    cs2 = variable("cs2")
    rs1 = variable("rs1")
    rs2 = variable("rs2")
    k = variable("k")

    assertions = []

    def check(label, actual, expected):
        assert_equal(label, actual, expected)
        assertions.append(label)

    check("Tg11_1", rows["Tg11_1"], scale(product(a1, e0), Fraction(3, 8)))
    check(
        "Tg12_2 after e0=0",
        substitute(rows["Tg12_2"], {"e0": {}}),
        scale(product(e1, add(e1, scale(product(a1, ell1), -4))), Fraction(3, 32)),
    )

    e1_branch = scale(product(a1, ell1), 4)
    check(
        "Tg12_1 on e1=4*a1*ell1",
        substitute(rows["Tg12_1"], {"e0": {}, "e1": e1_branch}),
        scale(product(a1, add(ee0, scale(product(aa0, ell1), 4))), Fraction(3, 8)),
    )
    ee0_branch = scale(product(aa0, ell1), -4)
    check(
        "Tg13_4 on second branch",
        substitute(rows["Tg13_4"], {"e0": {}, "e1": e1_branch, "ee0": ee0_branch}),
        scale(product(parser.power(a1, 2), parser.power(ell1, 3)), Fraction(-3, 2)),
    )

    base = {"e0": {}, "e1": {}, "ee0": {}}
    check(
        "Tg14_4 after e0=e1=ee0=0",
        substitute(rows["Tg14_4"], base),
        scale(product(parser.power(a1, 2), ell1, rs1), Fraction(3, 32)),
    )
    check(
        "Tg14_3 plus half ell1 Tg13_1",
        add(
            substitute(rows["Tg14_3"], base),
            scale(product(ell1, substitute(rows["Tg13_1"], base)), Fraction(1, 2)),
        ),
        add(
            scale(product(parser.power(a1, 2), cs1, ell1), Fraction(3, 8)),
            scale(product(a1, aa0, rs1), Fraction(-3, 16)),
        ),
    )

    case_b = {**base, "rs1": {}, "cs1": {}}
    check(
        "case B Tg13_2",
        substitute(rows["Tg13_2"], case_b),
        scale(product(a1, ee1, ell1), Fraction(-3, 8)),
    )
    case_b["ee1"] = {}
    check(
        "case B Tg13_1",
        substitute(rows["Tg13_1"], case_b),
        scale(product(a1, ec3), Fraction(3, 8)),
    )
    case_b["ec3"] = {}
    check(
        "case B Tg15_4",
        substitute(rows["Tg15_4"], case_b),
        scale(product(parser.power(a1, 2), ell1, rs2), Fraction(3, 32)),
    )
    case_b["rs2"] = {}
    check(
        "case B Tg14_2",
        substitute(rows["Tg14_2"], case_b),
        scale(product(a1, ell1, ez3), Fraction(-3, 8)),
    )
    case_b["ez3"] = {}
    check(
        "case B Tg14_1",
        substitute(rows["Tg14_1"], case_b),
        scale(product(a1, add(ec4, scale(product(a1, cs2), -1))), Fraction(3, 8)),
    )
    case_b["ec4"] = product(a1, cs2)
    check(
        "case B Tg15_3",
        substitute(rows["Tg15_3"], case_b),
        add(
            scale(product(parser.power(a1, 2), cs2, ell1), Fraction(3, 8)),
            scale(parser.power(a1, 3), Fraction(-1, 16)),
        ),
    )
    case_b["a1"] = scale(product(cs2, ell1), 6)
    # Substitution is simultaneous, so update the already-derived ec4=a1*cs2
    # relation after replacing a1.
    case_b["ec4"] = scale(product(parser.power(cs2, 2), ell1), 6)
    check(
        "case B terminal Tg16_5",
        substitute(rows["Tg16_5"], case_b),
        scale(product(parser.power(cs2, 3), parser.power(ell1, 4)), Fraction(27, 2)),
    )

    case_a2 = {**base, "ell1": {}, "aa0": {}}
    check(
        "case A2 Tg13_2",
        substitute(rows["Tg13_2"], case_a2),
        product(
            rs1,
            add(
                scale(parser.power(a1, 2), Fraction(-3, 32)),
                scale(product(k, parser.power(rs1, 2)), Fraction(5, 1024)),
            ),
        ),
    )
    check(
        "case A2 Tg15_4",
        substitute(rows["Tg15_4"], case_a2),
        scale(product(a1, rs1, add(product(a1, ell2), scale(ee1, -1))), Fraction(3, 32)),
    )

    result = {
        "status": "PASS-ORDERED-A1-RADICAL-CASCADE-INDEPENDENT-REPLAY",
        "scope": (
            "field-point/radical deductions from frozen raw ordered-a1 rho-zero "
            "rows through grade16 on D(a1), in characteristic not 2,3,5"
        ),
        "v37_compiler_sha256": V37_SHA256,
        "named_row_count": len(row_hashes),
        "assertion_count": len(assertions),
        "assertions": assertions,
        "conclusion": (
            "e0=e1=ee0=ell1=0 and aa0*rs1=0; on D(rs1), "
            "aa0=0, k*rs1^2=(96/5)*a1^2, ee1=a1*ell2"
        ),
        "firewalls": [
            "no polynomial ideal-membership certificate",
            "no full-rho chart statement",
            "no saturated-Rees, base-change, Gate-T, or JC2 inference",
        ],
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
