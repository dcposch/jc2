#!/usr/bin/env python3
"""Independent restricted-AST checks of the harvested V22R1 coefficients."""

from __future__ import annotations

import ast
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PRIME = 65521
EXPECTED_COUNTS = [133, 224, 355, 140, 585, 200, 759]
Q_ROOT = HERE / "aws_q_r1"
P_ROOT = HERE / "aws_p65521_r1"

Monomial = tuple[tuple[str, int], ...]
Polynomial = dict[Monomial, Fraction]


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def clean(polynomial: Polynomial) -> Polynomial:
    return {monomial: coefficient for monomial, coefficient in polynomial.items() if coefficient}


def const(value: int | Fraction) -> Polynomial:
    value = Fraction(value)
    return {} if not value else {(): value}


def add(left: Polynomial, right: Polynomial, sign: int = 1) -> Polynomial:
    answer = dict(left)
    for monomial, coefficient in right.items():
        answer[monomial] = answer.get(monomial, Fraction(0)) + sign * coefficient
    return clean(answer)


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            exponents: dict[str, int] = dict(left_monomial)
            for name, exponent in right_monomial:
                exponents[name] = exponents.get(name, 0) + exponent
            monomial = tuple(sorted((name, exponent) for name, exponent in exponents.items() if exponent))
            answer[monomial] = answer.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
    return clean(answer)


def power(polynomial: Polynomial, exponent: int) -> Polynomial:
    if exponent < 0:
        fail(("negative exponent", exponent))
    answer = const(1)
    base = polynomial
    while exponent:
        if exponent & 1:
            answer = multiply(answer, base)
        exponent //= 2
        if exponent:
            base = multiply(base, base)
    return answer


def scalar(polynomial: Polynomial) -> Fraction:
    if set(polynomial) != {()}:
        fail(("nonconstant scalar", polynomial))
    return polynomial[()]


def parse_node(node: ast.AST) -> Polynomial:
    if isinstance(node, ast.Expression):
        return parse_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return const(node.value)
    if isinstance(node, ast.Name):
        return {((node.id, 1),): Fraction(1)}
    if isinstance(node, ast.UnaryOp):
        item = parse_node(node.operand)
        if isinstance(node.op, ast.UAdd):
            return item
        if isinstance(node.op, ast.USub):
            return {monomial: -coefficient for monomial, coefficient in item.items()}
    if isinstance(node, ast.BinOp):
        left = parse_node(node.left)
        right = parse_node(node.right)
        if isinstance(node.op, ast.Add):
            return add(left, right)
        if isinstance(node.op, ast.Sub):
            return add(left, right, -1)
        if isinstance(node.op, ast.Mult):
            return multiply(left, right)
        if isinstance(node.op, ast.Div):
            divisor = scalar(right)
            if not divisor:
                fail("division by zero")
            return {monomial: coefficient / divisor for monomial, coefficient in left.items()}
        if isinstance(node.op, ast.Pow):
            exponent = scalar(right)
            if exponent.denominator != 1:
                fail(("nonintegral exponent", exponent))
            return power(left, int(exponent))
    fail(("unsupported syntax", ast.dump(node)))


def parse(path: Path) -> Polynomial:
    text = path.read_text().strip()
    if not text:
        fail(("empty polynomial", str(path)))
    return parse_node(ast.parse(text.replace("^", "**"), mode="eval"))


def mod_prime(coefficient: Fraction) -> int:
    denominator = coefficient.denominator % PRIME
    if not denominator:
        fail(("bad denominator modulo prime", coefficient))
    return coefficient.numerator * pow(denominator, -1, PRIME) % PRIME


def reduce_polynomial(polynomial: Polynomial) -> dict[Monomial, int]:
    return {
        monomial: reduced
        for monomial, coefficient in polynomial.items()
        if (reduced := mod_prime(coefficient))
    }


def sigma_weight(name: str) -> int:
    fixed = {
        "rho": 0, "cs": 2, "rs": 2, "k": 4,
        "a0": 5, "a1": 5, "c0": 5, "c1": 5,
        "aa0": 6, "aa1": 6, "e0": 6, "e1": 6,
        "aaa0": 7, "aaa1": 7, "ee0": 7, "ee1": 7,
        "k1": 5, "k2c": 6, "k6": 12, "k2": 20,
    }
    if name in fixed:
        return fixed[name]
    for prefix, offset in (
        ("ell", 0), ("cs", 2), ("rs", 2), ("az", 5), ("ac", 5),
        ("ez", 5), ("ec", 5), ("k10_", 4), ("k6_", 12),
    ):
        suffix = name[len(prefix):] if name.startswith(prefix) else ""
        if suffix.isdigit():
            return offset + int(suffix)
    fail(("unknown sigma weight", name))


def section(polynomial: Polynomial, one_name: str | None) -> dict[int, Fraction]:
    answer: dict[int, Fraction] = {}
    for monomial, coefficient in polynomial.items():
        rho_exponent = 0
        survives = True
        for name, exponent in monomial:
            if name == "rho":
                rho_exponent += exponent
            elif name != one_name:
                survives = False
                break
        if survives:
            answer[rho_exponent] = answer.get(rho_exponent, Fraction(0)) + coefficient
    return {exponent: coefficient for exponent, coefficient in answer.items() if coefficient}


def serialize_rho(polynomial: dict[int, Fraction]) -> dict[str, list[int]]:
    return {
        str(exponent): [coefficient.numerator, coefficient.denominator]
        for exponent, coefficient in sorted(polynomial.items())
    }


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: verify_harvest_v22r1.py OUTPUT.json")
    output = Path(sys.argv[1]).resolve()
    if output.exists():
        fail(("refuse overwrite", str(output)))
    q_result_path = Q_ROOT / "RESULT.json"
    p_result_path = P_ROOT / "RESULT.json"
    q_result = json.loads(q_result_path.read_text())
    p_result = json.loads(p_result_path.read_text())
    if q_result.get("characteristic") != 0 or p_result.get("characteristic") != PRIME:
        fail("result characteristic")

    q_polynomials: dict[int, Polynomial] = {}
    p_polynomials: dict[int, Polynomial] = {}
    records: dict[str, object] = {}
    for row, expected_count in enumerate(EXPECTED_COUNTS, 1):
        name = f"Tg15_{row}"
        q_path = Q_ROOT / "compiled" / f"{name}_q.poly"
        p_path = P_ROOT / "compiled" / f"{name}_p{PRIME}.poly"
        q_polynomial = parse(q_path)
        p_polynomial = parse(p_path)
        q_polynomials[row] = q_polynomial
        p_polynomials[row] = p_polynomial
        if len(q_polynomial) != expected_count or len(p_polynomial) != expected_count:
            fail(("term count", name, len(q_polynomial), len(p_polynomial), expected_count))
        if q_result["coefficient_sha256"][name] != digest(q_path):
            fail(("Q coefficient hash", name))
        if p_result["coefficient_sha256"][name] != digest(p_path):
            fail(("F coefficient hash", name))
        q_reduced = reduce_polynomial(q_polynomial)
        p_reduced = reduce_polynomial(p_polynomial)
        if len(q_reduced) != expected_count or len(p_reduced) != expected_count:
            fail(("modular coefficient vanished", name))
        if q_reduced != p_reduced:
            fail(("Q-to-F65521 mismatch", name))
        bad_weights = [
            monomial for monomial in q_polynomial
            if sum(sigma_weight(variable) * exponent for variable, exponent in monomial) != 15
        ]
        odd_rho = [
            monomial for monomial in q_polynomial
            if next((exponent for variable, exponent in monomial if variable == "rho"), 0) % 2
        ]
        if bad_weights or odd_rho:
            fail(("homogeneity/parity", name, len(bad_weights), len(odd_rho)))
        records[name] = {
            "q_sha256": digest(q_path),
            "p65521_sha256": digest(p_path),
            "term_count": expected_count,
            "q_to_p65521_support_and_coefficients": "MATCH",
            "rho_even": True,
            "sigma_weight": 15,
        }

    expected_sections = {
        "CS0": {},
        "Z00": {},
        "A00": {"6": {0: Fraction(-1, 16)}},
        "A10": {
            "3": {0: Fraction(-1, 16)},
            "5": {2: Fraction(-3, 32)},
            "7": {4: Fraction(-3, 128)},
        },
    }
    observed_sections: dict[str, dict[str, dict[int, Fraction]]] = {}
    for label, one_name in (("CS0", "cs"), ("A00", "a0"), ("A10", "a1"), ("Z00", None)):
        observed_sections[label] = {
            str(row): residual
            for row, polynomial in q_polynomials.items()
            if (residual := section(polynomial, one_name))
        }
    if observed_sections != expected_sections:
        fail(("named section mismatch", observed_sections, expected_sections))

    all_names = sorted({name for polynomial in q_polynomials.values() for monomial in polynomial for name, _ in monomial if name != "rho"})
    nonzero_one_name_sections = {
        name: {
            str(row): serialize_rho(residual)
            for row, polynomial in q_polynomials.items()
            if (residual := section(polynomial, name))
        }
        for name in all_names
    }
    nonzero_one_name_sections = {name: rows for name, rows in nonzero_one_name_sections.items() if rows}
    if not nonzero_one_name_sections:
        fail("section evaluator lacks a nonzero control")

    final = {
        "status": "PASS-INDEPENDENT-HARVEST-VERIFICATION-V22R1",
        "parser": "Python restricted AST; exact Fraction sparse polynomial",
        "q_result_sha256": digest(q_result_path),
        "p65521_result_sha256": digest(p_result_path),
        "coefficient_records": records,
        "q_to_p65521_matches": 7,
        "named_sections": {
            label: {row: serialize_rho(residual) for row, residual in rows.items()}
            for label, rows in observed_sections.items()
        },
        "nonzero_one_name_section_controls": nonzero_one_name_sections,
    }
    output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-INDEPENDENT-HARVEST-VERIFICATION-V22R1")
    print("Q_TO_F65521_SUPPORT_AND_COEFFICIENT_MATCHES=7")
    print("TERM_COUNTS=" + ",".join(map(str, EXPECTED_COUNTS)))
    print("NAMED_SECTIONS=CS0:0,Z00:0,A00:row6,A10:rows3,5,7")
    print("NONZERO_ONE_NAME_CONTROLS=" + ",".join(nonzero_one_name_sections))


if __name__ == "__main__":
    main()
