#!/usr/bin/env python3
"""Exact univariate-rho evaluation of the frozen V9/V17 source prefix."""

from __future__ import annotations

import ast
import hashlib
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
V9 = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/aws_q_v9/compiled"
V17 = ROOT / "cases/max12_812_order2_p0_total_rees_t_cs_row5_g14_export_v17_20260826/aws_q/compiled/Tg14_5_q.poly"


class Poly:
    """Sparse Q[rho] polynomial used only by this fail-closed replay."""

    def __init__(self, terms: dict[int, Fraction] | None = None):
        self.terms = {d: c for d, c in (terms or {}).items() if c}

    @staticmethod
    def constant(value: int | Fraction) -> "Poly":
        value = Fraction(value)
        return Poly({0: value} if value else {})

    @staticmethod
    def rho() -> "Poly":
        return Poly({1: Fraction(1)})

    def __add__(self, other: "Poly") -> "Poly":
        out = dict(self.terms)
        for degree, coefficient in other.terms.items():
            out[degree] = out.get(degree, Fraction(0)) + coefficient
        return Poly(out)

    def __neg__(self) -> "Poly":
        return Poly({degree: -coefficient for degree, coefficient in self.terms.items()})

    def __sub__(self, other: "Poly") -> "Poly":
        return self + (-other)

    def __mul__(self, other: "Poly") -> "Poly":
        out: dict[int, Fraction] = {}
        for left_degree, left_coefficient in self.terms.items():
            for right_degree, right_coefficient in other.terms.items():
                degree = left_degree + right_degree
                out[degree] = out.get(degree, Fraction(0)) + left_coefficient * right_coefficient
        return Poly(out)

    def __truediv__(self, other: "Poly") -> "Poly":
        if set(other.terms) != {0}:
            raise ValueError("division by a nonconstant polynomial")
        denominator = other.terms[0]
        if not denominator:
            raise ZeroDivisionError
        return Poly({degree: coefficient / denominator for degree, coefficient in self.terms.items()})

    def __pow__(self, exponent: int) -> "Poly":
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError(("bad exponent", exponent))
        result = Poly.constant(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def is_zero(self) -> bool:
        return not self.terms

    def display(self) -> str:
        if not self.terms:
            return "0"
        return "+".join(f"({coefficient})*rho^{degree}" for degree, coefficient in sorted(self.terms.items()))


def evaluate_node(node: ast.AST, ones: set[str], fractions: dict[str, Fraction]) -> Poly:
    if isinstance(node, ast.Expression):
        return evaluate_node(node.body, ones, fractions)
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return Poly.constant(node.value)
    if isinstance(node, ast.Name):
        if node.id in fractions:
            return Poly.constant(fractions[node.id])
        if node.id == "rho":
            return Poly.rho()
        return Poly.constant(1 if node.id in ones else 0)
    if isinstance(node, ast.UnaryOp):
        value = evaluate_node(node.operand, ones, fractions)
        if isinstance(node.op, ast.USub):
            return -value
        if isinstance(node.op, ast.UAdd):
            return value
    if isinstance(node, ast.BinOp):
        left = evaluate_node(node.left, ones, fractions)
        right = evaluate_node(node.right, ones, fractions)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.Pow):
            if set(right.terms) != {0} or right.terms[0].denominator != 1:
                raise ValueError("nonintegral exponent")
            return left ** int(right.terms[0])
    raise ValueError(("unsupported syntax", ast.dump(node)))


def evaluate(text: str, ones: set[str], fractions: dict[str, Fraction] | None = None) -> Poly:
    tree = ast.parse(text.strip().replace("^", "**"), mode="eval")
    return evaluate_node(tree, ones, fractions or {})


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    rows = [V9 / f"Tg{grade}_{row}.poly" for grade in (10, 11, 12) for row in range(1, 8)]
    rows.append(V17)
    if len(rows) != 22 or any(not path.is_file() for path in rows):
        raise RuntimeError("frozen input census")

    sections = {
        "CS0": {"cs"},
        "A00": {"a0"},
        "A10": {"a1"},
    }
    for label, ones in sections.items():
        residuals = [evaluate(path.read_text(), ones) for path in rows]
        bad = [(path.name, residual.display()) for path, residual in zip(rows, residuals) if not residual.is_zero()]
        if bad:
            raise RuntimeError((label, bad))
        print(f"{label}_ZERO_ROWS={len(residuals)}")

    witness = {"cs", "e1"}
    witness_fractions = {"k": Fraction(12, 5), "rho": Fraction(0)}
    row12_2 = evaluate((V9 / "Tg12_2.poly").read_text(), witness, witness_fractions)
    row14_5 = evaluate(V17.read_text(), witness, witness_fractions)
    if not row12_2.is_zero() or row14_5.terms != {0: Fraction(-21, 320)}:
        raise RuntimeError(("reviewed witness control", row12_2.display(), row14_5.display()))
    print("WITNESS_TG12_2=0")
    print("WITNESS_TG14_5=-21/320")

    negative = evaluate(
        (V9 / "Tg12_2.poly").read_text(), {"cs", "k"}, {"rho": Fraction(0)}
    )
    if negative.is_zero():
        raise RuntimeError("negative control unexpectedly zero")
    print(f"NEGATIVE_CONTROL_TG12_2={negative.display()}")

    for path in rows:
        print(f"INPUT_SHA256={digest(path)} {path.relative_to(ROOT)}")
    print("PREFIX_ZERO_SECTIONS=PASS")


if __name__ == "__main__":
    main()
