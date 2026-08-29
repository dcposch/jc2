#!/usr/bin/env python3
"""Exact replay of the ordered-a1, rho=0 branch closure through grade 19.

This is deliberately a small pure-Python/Fraction replay.  It imports only
the hash-pinned V37 row loader, then performs sparse Laurent-polynomial
arithmetic itself.  No CAS is used.
"""

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
INPUTS = {
    ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-radical-cascade-hostile-review-sol-20260827.md":
        "ede6b287bab76c00ac8d5b8e99e630a2006fcb7f252db0fa865764ad9dddb133",
    ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-first-occurrence-symbol-spencer-design-sol-20260827.md":
        "a049794b885b0bd49d79228d47790aa5466a33c29e8ba4057509b939e4af922e",
    ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-w19-tg19-7-compatibility-v39-producer-sol-20260827.md":
        "dbec09d2021e81549c8305bc19d0a46a00cf9721aade9a7e530b6daeec77bfd6",
    ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_radical_cascade_review_v41_20260827/replay_cascade_review.py":
        "e82811f46d8dac635201935b34748d4ffc278010c3256feb1207216711a3f009",
}

Monomial = tuple[tuple[str, int], ...]
Polynomial = dict[Monomial, Fraction]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> None:
    raise RuntimeError(message)


def load_v37():
    if digest(V37) != V37_SHA256:
        fail(("V37 hash", digest(V37)))
    for path, expected in INPUTS.items():
        if digest(path) != expected:
            fail(("input hash", str(path), digest(path), expected))
    spec = importlib.util.spec_from_file_location("a1_closure_v42_v37", V37)
    if spec is None or spec.loader is None:
        fail("V37 import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical_monomial(exponents: dict[str, int]) -> Monomial:
    return tuple(sorted((name, exponent) for name, exponent in exponents.items() if exponent))


def const(value) -> Polynomial:
    value = Fraction(value)
    return {(): value} if value else {}


def variable(name: str, exponent: int = 1) -> Polynomial:
    return {((name, exponent),): Fraction(1)} if exponent else const(1)


def add(*polynomials: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            value = answer.get(monomial, Fraction(0)) + coefficient
            if value:
                answer[monomial] = value
            else:
                answer.pop(monomial, None)
    return answer


def scale(polynomial: Polynomial, value) -> Polynomial:
    value = Fraction(value)
    return {monomial: value * coefficient for monomial, coefficient in polynomial.items()
            if value * coefficient}


def multiply(*polynomials: Polynomial) -> Polynomial:
    answer = const(1)
    for polynomial in polynomials:
        product: Polynomial = {}
        for left, left_coefficient in answer.items():
            for right, right_coefficient in polynomial.items():
                exponents = dict(left)
                for name, exponent in right:
                    exponents[name] = exponents.get(name, 0) + exponent
                monomial = canonical_monomial(exponents)
                product[monomial] = product.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
        answer = {monomial: coefficient for monomial, coefficient in product.items() if coefficient}
    return answer


def power(polynomial: Polynomial, exponent: int) -> Polynomial:
    if exponent < 0:
        if len(polynomial) != 1:
            fail(("negative power of nonmonomial", exponent, polynomial))
        monomial, coefficient = next(iter(polynomial.items()))
        inverse = {canonical_monomial({name: -degree for name, degree in monomial}): 1 / coefficient}
        return power(inverse, -exponent)
    answer = const(1)
    for _ in range(exponent):
        answer = multiply(answer, polynomial)
    return answer


def substitute(polynomial: Polynomial, replacements: dict[str, Polynomial]) -> Polynomial:
    answer: Polynomial = {}
    for monomial, coefficient in polynomial.items():
        term = const(coefficient)
        for name, exponent in monomial:
            term = multiply(term, power(replacements.get(name, variable(name)), exponent))
        answer = add(answer, term)
    return answer


def divided_difference(polynomial: Polynomial, name: str, value: Polynomial) -> Polynomial:
    """Return Q with P-P|_(name=value)=(name-value)Q."""
    answer: Polynomial = {}
    for monomial, coefficient in polynomial.items():
        exponents = dict(monomial)
        exponent = exponents.pop(name, 0)
        if exponent < 0:
            fail(("negative divided-difference exponent", name, exponent))
        if not exponent:
            continue
        other = {canonical_monomial(exponents): coefficient}
        for index in range(exponent):
            answer = add(answer, multiply(other, variable(name, exponent - 1 - index), power(value, index)))
    return answer


def assert_equal(label: str, actual: Polynomial, expected: Polynomial) -> None:
    residual = add(actual, scale(expected, -1))
    if residual:
        fail((label, canonical_polynomial(residual)))


def encoded_polynomial(polynomial: Polynomial):
    return [
        {
            "monomial": [[name, exponent] for name, exponent in monomial],
            "coefficient": [coefficient.numerator, coefficient.denominator],
        }
        for monomial, coefficient in sorted(polynomial.items())
    ]


def canonical_polynomial(polynomial: Polynomial) -> str:
    return json.dumps(encoded_polynomial(polynomial), sort_keys=True, separators=(",", ":"))


def polynomial_hash(polynomial: Polynomial) -> str:
    return sha256(canonical_polynomial(polynomial).encode()).hexdigest()


def weights(polynomial: Polynomial, sigma_weight) -> list[int]:
    return sorted({sum(sigma_weight(name) * exponent for name, exponent in monomial)
                   for monomial in polynomial})


def main() -> None:
    v37 = load_v37()
    parser, row_items, row_hashes, _ = v37.load_rows()
    rows = {item["name"]: {tuple(monomial): coefficient
                           for monomial, coefficient in item["polynomial"].items()}
            for item in row_items}
    if len(row_hashes) != 70:
        fail(("row count", len(row_hashes)))

    a1 = variable("a1")
    aa0 = variable("aa0")
    ee1 = variable("ee1")
    cs1 = variable("cs1")
    ell2 = variable("ell2")
    rs1 = variable("rs1")
    k = variable("k")

    # Replay the exact branch-cover row after the prior cascade has forced
    # e0=e1=ee0=ell1=0.  Passing from the product to A1 union A2 is the one
    # radical/field-point step used below.
    split_base = {name: {} for name in ("e0", "e1", "ee0", "ell1")}
    branch_cover = substitute(rows["Tg14_3"], split_base)
    branch_cover_expected = scale(multiply(a1, aa0, rs1), Fraction(-3, 16))
    assert_equal("branch-cover Tg14_3", branch_cover, branch_cover_expected)

    # The prior independently reviewed cascade is consumed, not reproved.
    # First close its D(rs1) branch A2 by a two-row identity.
    a2 = {name: {} for name in ("e0", "e1", "ee0", "ell1", "aa0")}
    a2_g13 = substitute(rows["Tg13_2"], a2)
    a2_g16 = substitute(rows["Tg16_6"], a2)
    expected_g13 = multiply(
        rs1,
        add(scale(power(a1, 2), Fraction(-3, 32)),
            scale(multiply(k, power(rs1, 2)), Fraction(5, 1024))),
    )
    expected_g16 = add(
        scale(multiply(power(a1, 2), power(rs1, 2)), Fraction(3, 256)),
        scale(multiply(k, power(rs1, 4)), Fraction(15, 32768)),
    )
    assert_equal("A2 Tg13_2", a2_g13, expected_g13)
    assert_equal("A2 Tg16_6", a2_g16, expected_g16)
    a2_combination = add(a2_g16, scale(multiply(rs1, a2_g13), Fraction(-3, 32)))
    a2_obstruction = scale(multiply(power(a1, 2), power(rs1, 2)), Fraction(21, 1024))
    assert_equal("A2 terminal combination", a2_combination, a2_obstruction)

    # On A1, Tg13_1 and Tg14_2 have unit leading coefficients on D(a1),
    # so they eliminate ec3 and rs2 exactly in the Laurent ring.
    a1_branch = {name: {} for name in ("e0", "e1", "ee0", "ell1", "rs1")}
    ec3_value = add(multiply(a1, cs1), scale(multiply(variable("a1", -1), aa0, ee1), -1))
    rs2_value = add(
        scale(multiply(variable("a1", -3), power(aa0, 2), ee1), -4),
        multiply(variable("a1", -2), power(ee1, 2)),
        scale(multiply(variable("a1", -1), aa0, cs1), -4),
        scale(multiply(variable("a1", -1), ee1, ell2), -4),
    )
    eliminations = {"ec3": ec3_value, "rs2": rs2_value}
    p13 = substitute(rows["Tg13_1"], a1_branch)
    p14 = substitute(rows["Tg14_2"], a1_branch)
    assert_equal("A1 Tg13_1 elimination", substitute(p13, {"ec3": ec3_value}), {})
    assert_equal("A1 Tg14_2 elimination", substitute(p14, eliminations), {})

    diagonal_names = {15: "Tg15_3", 17: "Tg17_5", 18: "Tg18_6", 19: "Tg19_7"}
    raw_diagonal = {grade: substitute(rows[name], a1_branch)
                    for grade, name in diagonal_names.items()}
    reduced = {grade: substitute(polynomial, eliminations)
               for grade, polynomial in raw_diagonal.items()}
    expected_terms = {15: 7, 17: 9, 18: 10, 19: 24}
    if {grade: len(polynomial) for grade, polynomial in reduced.items()} != expected_terms:
        fail(("reduced term census", {grade: len(polynomial) for grade, polynomial in reduced.items()}))

    # Compact homogeneous Laurent certificate in the eliminated quotient.
    h15 = add(
        scale(multiply(power(aa0, 3), ee1, variable("a1", -8)), -96),
        scale(multiply(aa0, power(ee1, 2), variable("a1", -7)), 24),
        scale(multiply(power(aa0, 2), cs1, variable("a1", -6)), -96),
        scale(multiply(aa0, ee1, ell2, variable("a1", -6)), -192),
        scale(multiply(aa0, power(ell2, 2), variable("a1", -5)), 144),
        scale(multiply(ee1, cs1, variable("a1", -5)), 48),
        scale(multiply(cs1, ell2, variable("a1", -4)), 48),
        scale(variable("a1", -3), -16),
    )
    h17 = add(
        scale(multiply(aa0, ee1, variable("a1", -6)), -192),
        scale(multiply(aa0, ell2, variable("a1", -5)), 192),
        scale(multiply(cs1, variable("a1", -4)), 96),
    )
    h18 = scale(multiply(ee1, variable("a1", -5)), 192)
    h19 = scale(multiply(aa0, variable("a1", -5)), 384)
    quotient_multipliers = {15: h15, 17: h17, 18: h18, 19: h19}
    quotient_sum: Polynomial = {}
    for grade, multiplier in quotient_multipliers.items():
        if weights(multiplier, parser.sigma_weight) != [-grade]:
            fail(("multiplier weight", grade, weights(multiplier, parser.sigma_weight)))
        quotient_sum = add(quotient_sum, multiply(multiplier, reduced[grade]))
    assert_equal("A1 compact quotient unit certificate", quotient_sum, const(1))

    # Lift the quotient identity back through the two monic eliminations.
    # This constructs explicit Laurent multipliers for Tg13_1 and Tg14_2
    # instead of relying on an implicit substitution argument.
    raw_sum: Polynomial = {}
    for grade, multiplier in quotient_multipliers.items():
        raw_sum = add(raw_sum, multiply(multiplier, raw_diagonal[grade]))
    difference = add(raw_sum, scale(const(1), -1))
    q3 = divided_difference(difference, "ec3", ec3_value)
    after_ec3 = substitute(difference, {"ec3": ec3_value})
    q2 = divided_difference(after_ec3, "rs2", rs2_value)
    l3 = add(variable("ec3"), scale(ec3_value, -1))
    l2 = add(variable("rs2"), scale(rs2_value, -1))
    assert_equal("two-step divided-difference lift", difference,
                 add(multiply(l3, q3), multiply(l2, q2)))
    h13 = add(
        scale(multiply(variable("a1", -1), q3), Fraction(-8, 3)),
        scale(multiply(aa0, variable("a1", -3), q2), Fraction(-32, 3)),
    )
    h14 = scale(multiply(variable("a1", -2), q2), Fraction(32, 3))
    direct_multipliers = {13: h13, 14: h14, **quotient_multipliers}
    direct_rows = {13: p13, 14: p14, **raw_diagonal}
    direct_sum: Polynomial = {}
    for grade, multiplier in direct_multipliers.items():
        if weights(multiplier, parser.sigma_weight) != [-grade]:
            fail(("direct multiplier weight", grade, weights(multiplier, parser.sigma_weight)))
        direct_sum = add(direct_sum, multiply(multiplier, direct_rows[grade]))
    assert_equal("A1 direct Laurent unit certificate", direct_sum, const(1))

    # Clear the only negative exponents (powers of a1) and replay an
    # ordinary-polynomial ideal certificate a1^N in the six raw rows.
    clear_exponent = max(
        -min(dict(monomial).get("a1", 0) for monomial in multiplier)
        for multiplier in direct_multipliers.values()
    )
    cleared_multipliers = {
        grade: multiply(power(a1, clear_exponent), multiplier)
        for grade, multiplier in direct_multipliers.items()
    }
    if any(exponent < 0 for multiplier in cleared_multipliers.values()
           for monomial in multiplier for _, exponent in monomial):
        fail("negative exponent survived clearing")
    cleared_sum: Polynomial = {}
    for grade, multiplier in cleared_multipliers.items():
        cleared_sum = add(cleared_sum, multiply(multiplier, direct_rows[grade]))
    assert_equal("A1 cleared ordinary ideal certificate", cleared_sum, power(a1, clear_exponent))

    # Fixed-certificate mutation control: change one Tg19_7 coefficient.
    mutated = dict(raw_diagonal[19])
    mutated_monomial = sorted(mutated)[0]
    mutated[mutated_monomial] += 1
    mutated_sum = add(direct_sum, multiply(h19, add(mutated, scale(raw_diagonal[19], -1))))
    mutation_residual = add(mutated_sum, scale(const(1), -1))
    if not mutation_residual:
        fail("mutation was not detected")

    result = {
        "status": "PASS-ORDERED-A1-RHO0-RAW-D-A1-EMPTY-THROUGH-G19",
        "scope": (
            "frozen raw ordered-a1 rho-zero rows through grade19 over Q; "
            "A1 has an ordinary a1-saturation certificate, while the prior "
            "A1/A2 split is radical/field-point"
        ),
        "v37_sha256": V37_SHA256,
        "named_row_count": len(row_hashes),
        "branch_cover": {
            "identity": "Tg14_3=-(3/16)*a1*aa0*rs1 after e0=e1=ee0=ell1=0",
            "sha256": polynomial_hash(branch_cover),
            "interpretation": "on D(a1), field points lie in V(rs1) union V(aa0)",
        },
        "a2": {
            "identity": "Tg16_6-(3/32)*rs1*Tg13_2=(21/1024)*a1^2*rs1^2",
            "combination_sha256": polynomial_hash(a2_combination),
            "obstruction_sha256": polynomial_hash(a2_obstruction),
        },
        "a1": {
            "row_names": ["Tg13_1", "Tg14_2", "Tg15_3", "Tg17_5", "Tg18_6", "Tg19_7"],
            "reduced_term_counts": {str(grade): len(polynomial) for grade, polynomial in reduced.items()},
            "reduced_sha256": {str(grade): polynomial_hash(polynomial)
                               for grade, polynomial in reduced.items()},
            "quotient_multiplier_term_counts": {str(grade): len(polynomial)
                                                 for grade, polynomial in quotient_multipliers.items()},
            "quotient_multiplier_sha256": {str(grade): polynomial_hash(polynomial)
                                            for grade, polynomial in quotient_multipliers.items()},
            "direct_multiplier_term_counts": {str(grade): len(polynomial)
                                               for grade, polynomial in direct_multipliers.items()},
            "direct_multiplier_sha256": {str(grade): polynomial_hash(polynomial)
                                          for grade, polynomial in direct_multipliers.items()},
            "clear_exponent": clear_exponent,
            "ordinary_certificate": f"a1^{clear_exponent} lies in the six-row A1 branch ideal",
        },
        "mutation": {
            "row": "Tg19_7",
            "monomial": [[name, exponent] for name, exponent in mutated_monomial],
            "residual_term_count": len(mutation_residual),
            "residual_sha256": polynomial_hash(mutation_residual),
        },
        "conclusion": (
            "The prior radical split has no surviving field point: A2 is killed "
            "at grade16 and A1 is killed by grade19."
        ),
        "firewalls": [
            "rho was specialized to zero",
            "raw frozen source rows only",
            "no unspecialized-rho, Rees-chart, Gate-T, or JC2 conclusion",
        ],
        "localizers": {
            "inherited_cascade": "D(a1); its discarded Case B used D(ell1)",
            "branch_cover": "D(a1), then the field-point split aa0*rs1=0",
            "A2": "D(a1*rs1); no division is needed to form the exact two-row identity",
            "A1": "D(a1) only; Laurent powers stop at a1^-8 and clear to a1^8",
        },
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
