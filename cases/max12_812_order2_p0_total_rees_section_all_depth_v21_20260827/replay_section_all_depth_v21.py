#!/usr/bin/env python3
"""Untruncated exact Q[sigma,rho] replay of four named source sections."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
EMITTER = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/export_allrows_g13_g14_v20.py"
V20_Q = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/aws_q_v20/RESULT.json"
V20_P = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/aws_p65521_v20/RESULT.json"
EXPECTED_HASHES = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    EMITTER: "5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587",
    V20_Q: "b23ffacd1e4e26abccaeb94a5e83f301cd98a9918a3a84e207fc462a880fe68d",
    V20_P: "266130872a10983724a7f9a080b36fef33981ff52192cbdf6c713a75bb7cd07a",
}

# Sparse Q[sigma,rho]: (sigma exponent, rho exponent) -> coefficient.
Polynomial = dict[tuple[int, int], Fraction]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def const(value: int | Fraction) -> Polynomial:
    value = Fraction(value)
    return {} if not value else {(0, 0): value}


def monomial(coefficient: int | Fraction, sigma: int = 0, rho: int = 0) -> Polynomial:
    coefficient = Fraction(coefficient)
    return {} if not coefficient else {(sigma, rho): coefficient}


def add(*items: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for item in items:
        for key, coefficient in item.items():
            value = answer.get(key, Fraction(0)) + coefficient
            if value:
                answer[key] = value
            elif key in answer:
                del answer[key]
    return answer


def scale(value: int | Fraction, item: Polynomial) -> Polynomial:
    value = Fraction(value)
    return {key: value * coefficient for key, coefficient in item.items() if value * coefficient}


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for (sigma_left, rho_left), coefficient_left in left.items():
        for (sigma_right, rho_right), coefficient_right in right.items():
            key = sigma_left + sigma_right, rho_left + rho_right
            answer[key] = answer.get(key, Fraction(0)) + coefficient_left * coefficient_right
    return {key: coefficient for key, coefficient in answer.items() if coefficient}


def power(item: Polynomial, exponent: int) -> Polynomial:
    answer = const(1)
    base = item
    while exponent:
        if exponent & 1:
            answer = multiply(answer, base)
        exponent //= 2
        if exponent:
            base = multiply(base, base)
    return answer


def shift(item: Polynomial, amount: int) -> Polynomial:
    return {(sigma + amount, rho): coefficient for (sigma, rho), coefficient in item.items()}


def section_coefficients(section: str) -> dict[int, Polynomial]:
    # These are the literal V20 emitter formulas after the named assignment.
    # p=-2*rho^2, r=p^2/4; c is sigma^2 only on CS0.  The a0/a1
    # perturbations enter n2/n0 or n3/n1 and are shifted by 3 and then 2.
    p = monomial(-2, rho=2)
    r = scale(Fraction(1, 4), multiply(p, p))
    c = monomial(1, sigma=2) if section == "CS0" else {}
    ac = const(1) if section == "A00" else {}
    az = const(1) if section == "A10" else {}
    n3 = shift(az, 3)
    n2 = shift(ac, 3)
    n1 = shift(scale(Fraction(1, 2), multiply(p, az)), 3)
    n0 = shift(scale(Fraction(1, 2), multiply(p, ac)), 3)
    return {
        6: scale(2, p),
        5: scale(2, c),
        4: add(multiply(p, p), scale(2, r)),
        3: add(scale(2, multiply(p, c)), shift(n3, 2)),
        2: add(multiply(c, c), scale(2, multiply(p, r)), shift(n2, 2)),
        1: add(scale(2, multiply(c, r)), shift(n1, 2)),
        0: add(multiply(r, r), shift(n0, 2)),
    }


def serialize(polynomial: Polynomial) -> list[dict[str, object]]:
    return [
        {
            "sigma_exponent": sigma,
            "rho_exponent": rho,
            "coefficient": [coefficient.numerator, coefficient.denominator],
        }
        for (sigma, rho), coefficient in sorted(polynomial.items())
    ]


def reduce_mod(polynomial: Polynomial, prime: int) -> dict[str, int]:
    return {
        f"sigma^{sigma}*rho^{rho}":
            (coefficient.numerator * pow(coefficient.denominator, -1, prime)) % prime
        for (sigma, rho), coefficient in sorted(polynomial.items())
    }


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: replay_section_all_depth_v21.py OUTPUT.json")
    output = Path(sys.argv[1]).resolve()
    if output.exists():
        fail(("refuse overwrite", str(output)))
    for path, expected in EXPECTED_HASHES.items():
        observed = digest(path)
        if observed != expected:
            fail(("frozen input hash", str(path), observed, expected))

    for path, characteristic in ((V20_Q, 0), (V20_P, 65521)):
        result = json.loads(path.read_text())
        sections = result.get("section_nonzero_residuals_exact_qrho")
        if (
            result.get("status") != "PASS-TOTAL-REES-ALLROWS-G13-G14-EXPORT-V20"
            or result.get("characteristic") != characteristic
            or sections != {"A00": {}, "A10": {}, "CS0": {}, "Z00": {}}
        ):
            fail(("V20 section bridge", str(path)))

    tails = json.loads(TAILS.read_text())
    if sorted(tails) != [str(row) for row in range(1, 8)]:
        fail("seven-row tail census")
    weights = [8 - index for index in range(7)] + [2, 6, 10]
    expected = {
        "CS0": {},
        "Z00": {},
        "A00": {"6": {(15, 0): Fraction(-1, 16)}},
        "A10": {
            "3": {(15, 0): Fraction(-1, 16)},
            "5": {(15, 2): Fraction(-3, 32)},
            "7": {(15, 4): Fraction(-3, 128)},
        },
    }
    section_results: dict[str, dict[str, Polynomial]] = {}
    contribution_records: dict[str, dict[str, list[dict[str, object]]]] = {}
    for section in ("CS0", "A00", "A10", "Z00"):
        coefficients = section_coefficients(section)
        rows: dict[str, Polynomial] = {}
        row_contributions: dict[str, list[dict[str, object]]] = {}
        for row in range(1, 8):
            total: Polynomial = {}
            contributions: list[dict[str, object]] = []
            for raw_monomial, raw_coefficient in tails[str(row)]:
                exponents = [int(value) for value in raw_monomial]
                if len(exponents) != 10 or sum(a * b for a, b in zip(exponents, weights)) != 12 + row:
                    fail(("tail weight contract", row, exponents))
                # Every load series is zero on each named section.
                if any(exponents[7:]):
                    continue
                term = const(Fraction(str(raw_coefficient)))
                for index, exponent in enumerate(exponents[:7]):
                    if exponent:
                        term = multiply(term, power(coefficients[index], exponent))
                if term:
                    contributions.append({
                        "tail_monomial": exponents,
                        "tail_coefficient": str(raw_coefficient),
                        "section_contribution": serialize(term),
                    })
                total = add(total, term)
            if total:
                rows[str(row)] = total
            row_contributions[str(row)] = contributions
        if rows != expected[section]:
            fail(("frozen expected answer", section, rows, expected[section]))
        section_results[section] = rows
        contribution_records[section] = row_contributions

    modular = {}
    for prime in (32003, 65521):
        modular[str(prime)] = {
            section: {row: reduce_mod(polynomial, prime) for row, polynomial in rows.items()}
            for section, rows in section_results.items()
        }
        if any(value == 0 for sections in modular[str(prime)].values() for row in sections.values() for value in row.values()):
            fail(("displayed coefficient vanishes modulo control prime", prime))

    final = {
        "status": "PASS-TOTAL-REES-NAMED-SECTIONS-ALL-DEPTH-V21",
        "tails_sha256": EXPECTED_HASHES[TAILS],
        "emitter_sha256": EXPECTED_HASHES[EMITTER],
        "v20_q_result_sha256": EXPECTED_HASHES[V20_Q],
        "v20_p65521_result_sha256": EXPECTED_HASHES[V20_P],
        "tail_rows_checked": 7,
        "tail_terms_checked": sum(len(tails[str(row)]) for row in range(1, 8)),
        "ring": "Q[sigma,rho] (untruncated sparse)",
        "section_nonzero_rows": {
            section: {row: serialize(polynomial) for row, polynomial in rows.items()}
            for section, rows in section_results.items()
        },
        "nonzero_tail_contributions": {
            section: {
                row: contributions
                for row, contributions in rows.items()
                if section_results[section].get(row)
            }
            for section, rows in contribution_records.items()
        },
        "modular_reductions": modular,
        "first_nonzero_grade": {"A00": 15, "A10": 15, "CS0": None, "Z00": None},
        "all_depth_zero_sections": ["CS0", "Z00"],
        "scope": "FROZEN_569_CANONICAL_TAIL_SOURCE_UNDER_FOUR_NAMED_ASSIGNMENTS",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("V21_FROZEN_HASHES=PASS")
    print("V21_ALL_569_TAILS_EXACT_QSIGMARHO=PASS")
    print("V21_V20_G13_G14_BRIDGES=PASS")
    print("V21_A00_FIRST_NONZERO_GRADE=15")
    print("V21_A10_FIRST_NONZERO_GRADE=15")
    print("V21_CS0_ALL_DEPTH_ZERO=1")
    print("V21_Z00_ALL_DEPTH_ZERO=1")
    print("PASS_TOTAL_REES_NAMED_SECTIONS_ALL_DEPTH_V21")


if __name__ == "__main__":
    main()
