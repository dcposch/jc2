#!/usr/bin/env python3
"""Independent exact-Q replay of the p=0 cusp row-(6,12) source."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
DESIGN = ROOT / "xmodel/max12-812-order2-p0-cusp-grade12-unit-successor-design-20260826.md"
CUSP_DESIGN = ROOT / "xmodel/max12-812-order2-p0-cusp-successor-design-20260826.md"
G1011_COMPILER = ROOT / "cases/max12_812_order2_p0_cusp_g10_g11_20260826/compile_p0_cusp_g10_g11.py"
EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    DESIGN: "b426aa9e516b9c1a01e3b8510ddd5ad6415e5125523fbe3e7d409ef3e657c220",
    CUSP_DESIGN: "04ca7018ad1609dfd11839914ecbe214cf896ad78edd661cbeecc07f18614622",
    G1011_COMPILER: "9d49988213806d42ea4523881595837007fa861369f31fd18d0c83b7adf494d4",
}
EXPECTED_CANONICAL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
MAX_DEGREE = 12


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


Monomial = tuple[tuple[str, int], ...]
Polynomial = dict[Monomial, Fraction]
Series = list[Polynomial]


def monomial_product(left: Monomial, right: Monomial) -> Monomial:
    powers: dict[str, int] = {}
    for name, exponent in left + right:
        powers[name] = powers.get(name, 0) + exponent
    return tuple(sorted((name, exponent) for name, exponent in powers.items() if exponent))


def poly_const(value: Fraction | int) -> Polynomial:
    coefficient = Fraction(value)
    return {} if coefficient == 0 else {(): coefficient}


def poly_var(name: str) -> Polynomial:
    return {((name, 1),): Fraction(1)}


def poly_add(*items: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for item in items:
        for monomial, coefficient in item.items():
            value = answer.get(monomial, Fraction(0)) + coefficient
            if value:
                answer[monomial] = value
            elif monomial in answer:
                del answer[monomial]
    return answer


def poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    if not left or not right:
        return {}
    answer: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = monomial_product(left_monomial, right_monomial)
            value = answer.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
            if value:
                answer[monomial] = value
            elif monomial in answer:
                del answer[monomial]
    if len(answer) > 250000:
        fail(("independent replay polynomial term cap", len(answer)))
    return answer


def poly_scale(value: Fraction | int, polynomial: Polynomial) -> Polynomial:
    return poly_mul(poly_const(value), polynomial)


def poly_zero_variables(polynomial: Polynomial, names: set[str]) -> Polynomial:
    return {
        monomial: coefficient
        for monomial, coefficient in polynomial.items()
        if all(name not in names for name, _ in monomial)
    }


def poly_evaluate(polynomial: Polynomial, values: dict[str, Fraction]) -> Fraction:
    answer = Fraction(0)
    for monomial, coefficient in polynomial.items():
        term = coefficient
        for name, exponent in monomial:
            term *= values.get(name, Fraction(0)) ** exponent
        answer += term
    return answer


def series_zero() -> Series:
    return [{} for _ in range(MAX_DEGREE + 1)]


def series_add(*items: Series) -> Series:
    return [poly_add(*(item[degree] for item in items)) for degree in range(MAX_DEGREE + 1)]


def series_scale(value: Fraction | int, series: Series) -> Series:
    return [poly_scale(value, coefficient) for coefficient in series]


def series_shift(series: Series, amount: int) -> Series:
    answer = series_zero()
    if amount <= MAX_DEGREE:
        for degree in range(MAX_DEGREE + 1 - amount):
            answer[degree + amount] = series[degree]
    return answer


def series_mul(left: Series, right: Series) -> Series:
    answer = series_zero()
    for degree in range(MAX_DEGREE + 1):
        terms = [
            poly_mul(left[index], right[degree - index])
            for index in range(degree + 1)
            if left[index] and right[degree - index]
        ]
        answer[degree] = poly_add(*terms)
    return answer


def series_pow(series: Series, exponent: int) -> Series:
    answer = series_zero()
    answer[0] = poly_const(1)
    base = series
    power = exponent
    while power:
        if power & 1:
            answer = series_mul(answer, base)
        power //= 2
        if power:
            base = series_mul(base, base)
    return answer


def named_series(entries: list[tuple[int, str | Polynomial]]) -> Series:
    answer = series_zero()
    for degree, value in entries:
        if degree <= MAX_DEGREE:
            answer[degree] = poly_var(value) if isinstance(value, str) else value
    return answer


def serialize(polynomial: Polynomial) -> list[dict[str, object]]:
    return [
        {
            "coefficient": [coefficient.numerator, coefficient.denominator],
            "monomial": [[name, exponent] for name, exponent in monomial],
        }
        for monomial, coefficient in sorted(polynomial.items())
    ]


def primitive_series() -> tuple[dict[int, Series], dict[int, Series]]:
    k = poly_var("k")
    tau = poly_var("tau")
    dpar = poly_var("dpar")
    ktau = poly_mul(k, tau)

    p = named_series([(1, poly_scale(2, poly_var("ell1"))), (2, poly_scale(2, poly_var("ell2")))])

    cs = named_series(
        [
            (0, poly_scale(Fraction(-1, 3), dpar)),
            (1, "cs1"),
            (2, "cs2"),
        ]
    )
    c = series_shift(cs, 2)

    rs0 = poly_scale(Fraction(-96, 5), poly_mul(k, poly_mul(tau, tau)))
    rs = named_series([(0, rs0), (1, "rs1"), (2, "rs2")])
    r = series_scale(Fraction(1, 4), series_add(series_mul(p, p), series_shift(rs, 2)))

    az = named_series([(0, "a1"), (1, "aa1"), (2, "aaa1")])
    a0 = poly_mul(ktau, dpar)
    ac = named_series([(0, a0), (1, "aa0"), (2, "aaa0")])

    c1 = poly_scale(Fraction(96, 5), poly_mul(poly_mul(k, k), poly_mul(poly_mul(tau, tau), tau)))
    ez = named_series([(0, c1), (1, "e1"), (2, "ee1")])
    ec = named_series([(1, "e0"), (2, "ee0")])

    n3 = series_shift(az, 3)
    n2 = series_shift(ac, 3)
    n1 = series_shift(series_scale(Fraction(1, 2), series_add(series_mul(p, az), ez)), 3)
    n0 = series_shift(series_scale(Fraction(1, 2), series_add(series_mul(p, ac), ec)), 3)

    coefficients = {
        6: series_scale(2, p),
        5: series_scale(2, c),
        4: series_add(series_mul(p, p), series_scale(2, r)),
        3: series_add(series_scale(2, series_mul(p, c)), series_shift(n3, 2)),
        2: series_add(series_mul(c, c), series_scale(2, series_mul(p, r)), series_shift(n2, 2)),
        1: series_add(series_scale(2, series_mul(c, r)), series_shift(n1, 2)),
        0: series_add(series_mul(r, r), series_shift(n0, 2)),
    }

    k10 = named_series([(0, "k"), (1, "k1"), (2, "k2c")])
    k6 = named_series([(0, "k6_0")])
    k2 = named_series([(0, "k2_0")])
    loads = {7: series_shift(k10, 4), 8: series_shift(k6, 12), 9: series_shift(k2, 20)}
    return coefficients, loads


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag
    ):
        fail("p0 cusp grade-12 replay is restricted to registered AWS EC2")
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen source mismatch", str(path), actual, expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_CANONICAL_TAILS:
        fail("canonical all-tail digest mismatch")

    coefficients, loads = primitive_series()
    weights = [8 - index for index in range(7)] + [2, 6, 10]
    totals: dict[int, Series] = {}
    row6_contributions: list[dict[str, object]] = []
    focus_values = {"k": Fraction(-96, 5), "tau": Fraction(5, 96)}

    for ell in range(1, 8):
        total = series_zero()
        for raw_monomial, raw_coefficient in tails[str(ell)]:
            monomial = [int(value) for value in raw_monomial]
            if len(monomial) != 10 or sum(a * b for a, b in zip(monomial, weights)) != 12 + ell:
                fail(("tail contract", ell, monomial))
            term = series_zero()
            term[0] = poly_const(Fraction(str(raw_coefficient)))
            for index, exponent in enumerate(monomial[:7]):
                if exponent:
                    term = series_mul(term, series_pow(coefficients[index], exponent))
            for index, exponent in enumerate(monomial[7:], start=7):
                if exponent not in (0, 1):
                    fail(("load nonlinearity", ell, monomial))
                if exponent:
                    term = series_mul(term, loads[index])
            total = series_add(total, term)
            if ell == 6:
                focused = poly_evaluate(term[12], focus_values)
                if focused:
                    row6_contributions.append(
                        {
                            "tail_monomial": monomial,
                            "tail_coefficient": str(raw_coefficient),
                            "focused_grade12": [focused.numerator, focused.denominator],
                        }
                    )
        totals[ell] = total

    if any(totals[ell][degree] for ell in range(1, 8) for degree in range(10)):
        fail("a normalized cusp source row occurs below absolute grade ten")
    if any(totals[ell][10] for ell in range(1, 8)):
        fail(("normalized grade-ten support did not vanish", {ell: serialize(totals[ell][10]) for ell in range(1, 8)}))

    expected_g11_4 = {(('ell1', 1), ('k', 4), ('tau', 6)): Fraction(-864, 25)}
    if totals[4][11] != expected_g11_4:
        fail(("grade-eleven fourth pivot mismatch", serialize(totals[4][11]), serialize(expected_g11_4)))
    g11_3_after_ell = poly_zero_variables(totals[3][11], {"ell1"})
    expected_g11_3 = {(('e0', 1), ('k', 2), ('tau', 3)): Fraction(18, 5)}
    if g11_3_after_ell != expected_g11_3:
        fail(("grade-eleven third pivot mismatch", serialize(g11_3_after_ell), serialize(expected_g11_3)))

    row6_reduced = poly_zero_variables(totals[6][12], {"ell1", "e0"})
    expected_unit = {(('k', 5), ('tau', 8)): Fraction(18144, 125)}
    if row6_reduced != expected_unit:
        fail(("row-(6,12) unit mismatch", serialize(row6_reduced), serialize(expected_unit)))

    focused_sum = sum(
        (Fraction(item["focused_grade12"][0], item["focused_grade12"][1]) for item in row6_contributions),
        Fraction(0),
    )
    if len(row6_contributions) != 4 or focused_sum != Fraction(-21, 1024):
        fail(("focused four-tail sentinel", len(row6_contributions), focused_sum, row6_contributions))

    modular_coefficients = {
        prime: (18144 * pow(125, -1, prime)) % prime for prime in (32003, 65521)
    }
    if any(value == 0 for value in modular_coefficients.values()):
        fail(("unit coefficient vanished in a control prime", modular_coefficients))

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    result = {
        "status": "PASS-P0-CUSP-ROW6-GRADE12-INDEPENDENT-EXACT-REPLAY",
        "registered_aws_lane": tag,
        "characteristic": 0,
        "all_seven_rows_formed_through_grade12": True,
        "all_rows_zero_below_grade10": True,
        "normalized_grade10_rows_zero": True,
        "grade11_fourth_pivot": serialize(totals[4][11]),
        "grade11_third_pivot_after_fourth": serialize(g11_3_after_ell),
        "grade12_row6_before_pivot_reduction": serialize(totals[6][12]),
        "grade12_row6_after_only_ell1_e0": serialize(row6_reduced),
        "exact_identity": "row(6,12)=(18144/125)*k^5*tau^8=-(21/1024)*rs^3*u^2",
        "localized_consequence": "UNIT_ON_D(k*tau)=D(rs*k0)",
        "row6_target_absent": True,
        "first_target_grades": {"mu2": 28, "mu4": 32, "mu6": 36, "J": 38},
        "focused_tail_contribution_count": len(row6_contributions),
        "focused_tail_contributions": row6_contributions,
        "focused_sum": [focused_sum.numerator, focused_sum.denominator],
        "mod_32003_unit_coefficient": modular_coefficients[32003],
        "mod_65521_unit_coefficient": modular_coefficients[65521],
        "exact_Q_completed_before_modular_controls": True,
        "tails_sha256": digest(TAILS),
        "design_sha256": digest(DESIGN),
        "scope": "P0_POST_M0_UNIT_K0_D_RS_CUSP_ONLY_NO_GLOBAL_ORDER2_OR_JC2_VERDICT",
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("P0_CUSP_G12_SOURCE_HASHES=PASS")
    print("P0_CUSP_G12_ALL_SEVEN_ROWS=PASS")
    print("P0_CUSP_G12_G11_PIVOTS=PASS")
    print("P0_CUSP_G12_RAW_ROW6_UNIT=PASS")
    print("P0_CUSP_G12_FOCUSED_FOUR_TAILS=PASS")
    print("P0_CUSP_G12_STATUS=PASS_INDEPENDENT_EXACT_REPLAY")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
