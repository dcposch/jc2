#!/usr/bin/env python3
"""Independent AWS-only exact replay of the p=0 odd row-(5,14) source."""

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
DESIGN = ROOT / "xmodel/max12-812-order2-p0-odd-sheet-terminal-taylor-pullback-design-20260826.md"
EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    DESIGN: "68ccd9f24318473039ce56e969915663df6bf538c5fcf72a98055f605daab4a0",
}
EXPECTED_CANONICAL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
MAX_DEGREE = 14


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
    if len(answer) > 200000:
        fail(("independent replay polynomial term cap", len(answer)))
    return answer


def poly_scale(value: Fraction | int, polynomial: Polynomial) -> Polynomial:
    return poly_mul(poly_const(value), polynomial)


def series_zero() -> Series:
    return [{} for _ in range(MAX_DEGREE + 1)]


def series_add(*items: Series) -> Series:
    return [poly_add(*(item[degree] for item in items)) for degree in range(MAX_DEGREE + 1)]


def series_scale(value: Fraction | int, series: Series) -> Series:
    return [poly_scale(value, coefficient) for coefficient in series]


def series_shift(series: Series, amount: int) -> Series:
    answer = series_zero()
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
        answer[degree] = poly_var(value) if isinstance(value, str) else value
    return answer


def range_series(prefix: str, first: int, last: int) -> Series:
    return named_series([(degree, f"{prefix}{degree}") for degree in range(first, last + 1)])


def serialize(polynomial: Polynomial) -> list[dict[str, object]]:
    return [
        {
            "coefficient": [coefficient.numerator, coefficient.denominator],
            "monomial": [[name, exponent] for name, exponent in monomial],
        }
        for monomial, coefficient in sorted(polynomial.items())
    ]


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
        fail("independent row-(5,14) replay is restricted to registered AWS EC2")
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("frozen source mismatch", str(path), digest(path), expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_CANONICAL_TAILS:
        fail("canonical all-tail digest mismatch")

    # Independent reconstruction of the normalized primitive coefficient series.
    p = series_zero()
    p[2] = poly_scale(2, poly_var("ell2"))
    for degree in range(3, MAX_DEGREE + 1):
        p[degree] = poly_scale(2, poly_var(f"ell{degree}"))

    cs = range_series("cs", 1, 12)
    cs[0] = poly_var("b")
    c = series_shift(cs, 2)

    rs = range_series("rs", 1, 12)
    r = series_scale(Fraction(1, 4), series_add(series_mul(p, p), series_shift(rs, 2)))

    az = range_series("az", 2, 11)
    az[0] = poly_var("a1")
    az[1] = poly_var("aa1")
    ac = range_series("ac", 2, 11)
    ac[1] = poly_var("aa0")

    ez = range_series("ez", 3, 11)
    ez[1] = poly_mul(poly_mul(poly_var("b"), poly_var("b")), poly_var("w"))
    ez[2] = poly_var("ee1")
    ec = range_series("ec", 3, 11)
    ec[2] = poly_var("ee0")

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

    k10 = range_series("k10_", 1, 10)
    k10[0] = poly_scale(Fraction(12, 5), poly_mul(poly_var("w"), poly_var("w")))
    k6 = range_series("k6_", 0, 2)
    k2 = range_series("k2_", 0, 0)
    loads = {7: series_shift(k10, 4), 8: series_shift(k6, 12), 9: series_shift(k2, 20)}

    total = series_zero()
    contributions = []
    weights = [8 - index for index in range(7)] + [2, 6, 10]
    for raw_monomial, raw_coefficient in tails["5"]:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != 10 or sum(a * b for a, b in zip(monomial, weights)) != 17:
            fail(("row-five tail contract", monomial))
        term = series_zero()
        term[0] = poly_const(Fraction(str(raw_coefficient)))
        for index, exponent in enumerate(monomial[:7]):
            if exponent:
                term = series_mul(term, series_pow(coefficients[index], exponent))
        for index, exponent in enumerate(monomial[7:], start=7):
            if exponent not in (0, 1):
                fail(("load nonlinearity", monomial))
            if exponent:
                term = series_mul(term, loads[index])
        total = series_add(total, term)
        if term[14]:
            contributions.append(
                {
                    "tail_monomial": monomial,
                    "tail_coefficient": str(raw_coefficient),
                    "grade14_contribution": serialize(term[14]),
                }
            )

    expected = {(('b', 5), ('w', 2)): Fraction(-21, 320)}
    if total[14] != expected:
        fail(("row-(5,14) identity mismatch", serialize(total[14]), serialize(expected)))
    if any(total[degree] for degree in range(14)):
        fail(("row five unexpectedly starts below grade 14", [len(total[d]) for d in range(14)]))
    modular_coefficients = {
        prime: (-21 * pow(320, -1, prime)) % prime for prime in (32003, 65521)
    }
    if any(coefficient == 0 for coefficient in modular_coefficients.values()):
        fail(("control-prime coefficient vanished", modular_coefficients))

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    result = {
        "status": "PASS-P0-ODD-ROW5-GRADE14-INDEPENDENT-REPLAY",
        "registered_aws_lane": tag,
        "characteristic": 0,
        "tail_row": 5,
        "absolute_grade": 14,
        "tail_terms_checked": len(tails["5"]),
        "nonzero_grade14_contribution_count": len(contributions),
        "contributions": contributions,
        "collected_polynomial": serialize(total[14]),
        "exact_identity": "row(5,14)=-(21/320)*b^5*w^2",
        "exact_Q_identity_proved_before_modular_controls": True,
        "mod_32003_coefficient": modular_coefficients[32003],
        "mod_65521_coefficient": modular_coefficients[65521],
        "control_prime_coefficients_nonzero": True,
        "localized_consequence": "UNIT_ON_D(b*w)",
        "scope": "INDEPENDENT_ARITHMETIC_REPLAY_FROM_FROZEN_CANONICAL_TAILS",
        "nonclaims": [
            "does not independently regenerate canonical tails from the Faber source",
            "does not audit terminal chart completeness",
            "does not use Gate A or Taylor pullbacks",
            "does not claim JC2",
        ],
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("P0_ODD_ROW5_G14_SOURCE_HASHES=PASS")
    print("P0_ODD_ROW5_G14_ALL_89_TAILS=PASS")
    print("P0_ODD_ROW5_G14_EXACT_IDENTITY=PASS")
    print("P0_ODD_ROW5_G14_STATUS=PASS_INDEPENDENT_REPLAY")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
