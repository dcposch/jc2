#!/usr/bin/env python3
"""Exact sparse polynomials over Q. Degree is the true support, not a cap."""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


class Poly:
    """Polynomial with Fraction coefficients, lowest degree first."""

    __slots__ = ("c",)

    def __init__(self, coeffs=None):
        if coeffs is None:
            self.c = (Fraction(0),)
            return
        raw = tuple(Fraction(x) for x in coeffs)
        i = len(raw) - 1
        while i > 0 and raw[i] == 0:
            i -= 1
        self.c = raw[: i + 1]

    def __repr__(self) -> str:
        return f"Poly({list(self.c)!r})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Poly) and self.c == other.c

    def __hash__(self) -> int:
        return hash(self.c)

    def is_zero(self) -> bool:
        return self.c == (Fraction(0),)

    def degree(self) -> int:
        if self.is_zero():
            return -1
        return len(self.c) - 1

    def __add__(self, other: "Poly") -> "Poly":
        n = max(len(self.c), len(other.c))
        out = [Fraction(0)] * n
        for i, x in enumerate(self.c):
            out[i] += x
        for i, x in enumerate(other.c):
            out[i] += x
        return Poly(out)

    def __sub__(self, other: "Poly") -> "Poly":
        return self + other.scale(-1)

    def scale(self, scalar) -> "Poly":
        s = Fraction(scalar)
        return Poly(tuple(s * x for x in self.c))

    def __mul__(self, other: "Poly") -> "Poly":
        if self.is_zero() or other.is_zero():
            return Poly()
        out = [Fraction(0)] * (len(self.c) + len(other.c) - 1)
        for i, x in enumerate(self.c):
            if x == 0:
                continue
            for j, y in enumerate(other.c):
                out[i + j] += x * y
        return Poly(out)

    def deriv(self) -> "Poly":
        if self.degree() <= 0:
            return Poly()
        return Poly(tuple(self.c[i] * i for i in range(1, len(self.c))))

    def shift(self) -> "Poly":
        """Multiply by t."""
        return Poly((Fraction(0),) + self.c)

    def eval(self, x) -> Fraction:
        v = Fraction(0)
        xx = Fraction(x)
        for coeff in reversed(self.c):
            v = v * xx + coeff
        return v

    @staticmethod
    def monic_linear(root) -> "Poly":
        return Poly((-Fraction(root), Fraction(1)))

    def as_list(self) -> list[str]:
        return [str(x) for x in self.c]
