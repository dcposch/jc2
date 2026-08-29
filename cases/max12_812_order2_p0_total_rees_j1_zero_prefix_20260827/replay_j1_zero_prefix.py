#!/usr/bin/env python3
"""Exact sparse specialization of the frozen 22-row prefix to J1=0."""

from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
V9 = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/aws_q_v9/compiled"
V17 = ROOT / "cases/max12_812_order2_p0_total_rees_t_cs_row5_g14_export_v17_20260826/aws_q/compiled/Tg14_5_q.poly"
J1 = frozenset({"rs", "cs", "c0", "c1"})

Monomial = tuple[str, ...]
Polynomial = dict[Monomial, Fraction]


def clean(polynomial: Polynomial) -> Polynomial:
    return {monomial: coefficient for monomial, coefficient in polynomial.items() if coefficient}


def constant(value: int | Fraction) -> Polynomial:
    value = Fraction(value)
    return {(): value} if value else {}


def add(left: Polynomial, right: Polynomial, scale: Fraction = Fraction(1)) -> Polynomial:
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, Fraction(0)) + scale * coefficient
    return clean(out)


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            out[monomial] = out.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
    return clean(out)


def power(polynomial: Polynomial, exponent: int) -> Polynomial:
    if exponent < 0:
        raise ValueError(("negative exponent", exponent))
    result = constant(1)
    base = polynomial
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent >>= 1
    return result


def scalar_value(polynomial: Polynomial) -> Fraction:
    if set(polynomial) != {()}:
        raise ValueError(("nonconstant scalar", polynomial))
    return polynomial[()]


def parse_node(node: ast.AST, killed: frozenset[str]) -> Polynomial:
    if isinstance(node, ast.Expression):
        return parse_node(node.body, killed)
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return constant(node.value)
    if isinstance(node, ast.Name):
        return {} if node.id in killed else {(node.id,): Fraction(1)}
    if isinstance(node, ast.UnaryOp):
        value = parse_node(node.operand, killed)
        if isinstance(node.op, ast.UAdd):
            return value
        if isinstance(node.op, ast.USub):
            return {monomial: -coefficient for monomial, coefficient in value.items()}
    if isinstance(node, ast.BinOp):
        left = parse_node(node.left, killed)
        right = parse_node(node.right, killed)
        if isinstance(node.op, ast.Add):
            return add(left, right)
        if isinstance(node.op, ast.Sub):
            return add(left, right, Fraction(-1))
        if isinstance(node.op, ast.Mult):
            return multiply(left, right)
        if isinstance(node.op, ast.Div):
            divisor = scalar_value(right)
            if not divisor:
                raise ZeroDivisionError
            return {monomial: coefficient / divisor for monomial, coefficient in left.items()}
        if isinstance(node.op, ast.Pow):
            exponent = scalar_value(right)
            if exponent.denominator != 1:
                raise ValueError(("nonintegral exponent", exponent))
            return power(left, int(exponent))
    raise ValueError(("unsupported syntax", ast.dump(node)))


def parse(text: str, killed: frozenset[str] = frozenset()) -> Polynomial:
    return parse_node(ast.parse(text.strip().replace("^", "**"), mode="eval"), killed)


def names(text: str) -> frozenset[str]:
    tree = ast.parse(text.strip().replace("^", "**"), mode="eval")
    return frozenset(node.id for node in ast.walk(tree) if isinstance(node, ast.Name))


def canonical(polynomial: Polynomial) -> str:
    lines = []
    for monomial, coefficient in sorted(polynomial.items()):
        lines.append(
            f"{monomial!r}\t{coefficient.numerator}\t{coefficient.denominator}"
        )
    return "\n".join(lines) + ("\n" if lines else "")


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def evaluate_point(polynomial: Polynomial, one: str) -> Fraction:
    total = Fraction(0)
    for monomial, coefficient in polynomial.items():
        if all(variable == one for variable in monomial):
            total += coefficient
    return total


def main() -> None:
    rows = [V9 / f"Tg{grade}_{row}.poly" for grade in (10, 11, 12) for row in range(1, 8)]
    rows.append(V17)
    if len(rows) != 22 or any(not path.is_file() for path in rows):
        raise RuntimeError("frozen input census")

    restricted: dict[str, Polynomial] = {}
    row_grade: dict[str, int] = {}
    all_source_names: set[str] = set()
    for path in rows:
        text = path.read_text()
        all_source_names.update(names(text))
        polynomial = parse(text, J1)
        restricted[path.stem] = polynomial
        grade = 14 if path == V17 else int(path.stem[2:4])
        row_grade[path.stem] = grade
        variables = sorted({variable for monomial in polynomial for variable in monomial})
        degree = max(map(len, polynomial), default=-1)
        print(
            f"ROW={path.stem};grade={grade};terms={len(polynomial)};degree={degree};"
            f"variables={','.join(variables) if variables else '-'};"
            f"restricted_sha256={digest_bytes(canonical(polynomial).encode())};"
            f"input_sha256={digest_bytes(path.read_bytes())}"
        )

    forced_zero = {"Tg10_1", "Tg10_2", "Tg10_3", "Tg10_4", "Tg12_6"}
    if any(restricted[label] for label in forced_zero):
        raise RuntimeError(("stage-one row survived", sorted(label for label in forced_zero if restricted[label])))
    print("STAGE_ONE_CONSUMED_ROWS_ZERO=5")

    text_12_2 = (V9 / "Tg12_2.poly").read_text()
    e1_only = parse(text_12_2, frozenset(names(text_12_2) - {"e1"}))
    if e1_only != {("e1", "e1"): Fraction(3, 32)}:
        raise RuntimeError(("e1 control", e1_only))
    print("TG12_2_E1_ONLY=3/32*e1^2")

    for label, one in (("A00", "a0"), ("A10", "a1")):
        residuals = {row: evaluate_point(polynomial, one) for row, polynomial in restricted.items()}
        bad = {row: value for row, value in residuals.items() if value}
        if bad:
            raise RuntimeError((label, bad))
        print(f"{label}_ZERO_ROWS=22")

    surviving = [label for label, polynomial in restricted.items() if polynomial]
    first_grade = min(row_grade[label] for label in surviving)
    a0_rows = [label for label in surviving if any("a0" in monomial for monomial in restricted[label])]
    a1_rows = [label for label in surviving if any("a1" in monomial for monomial in restricted[label])]
    print(f"SURVIVING_ROWS={len(surviving)}")
    print("SURVIVING_LABELS=" + ",".join(surviving))
    print(f"FIRST_SURVIVING_GRADE={first_grade}")
    print("A0_SUPPORT_ROWS=" + (",".join(a0_rows) if a0_rows else "-"))
    print("A1_SUPPORT_ROWS=" + (",".join(a1_rows) if a1_rows else "-"))
    print("SPECIALIZED_VARIABLES=" + ",".join(sorted(all_source_names - set(J1))))
    print("A0_NOT_IN_PREFIX_RADICAL_BY_A00=true")
    print("A1_NOT_IN_PREFIX_RADICAL_BY_A10=true")
    print("J1_ZERO_PREFIX_SPECIALIZATION=PASS")


if __name__ == "__main__":
    main()
