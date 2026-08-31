#!/usr/bin/env python3
"""Desk-small exact replay of the decisive degree-six coefficient obstruction."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    a1, a2, a3, a4, a5, b1, b2, b3, b4, b5 = sp.symbols(
        "a1 a2 a3 a4 a5 b1 b2 b3 b4 b5"
    )
    x, y = sp.symbols("x y")
    A = x**2
    U = x + x**3 * y
    Z = 2 * y + x**2 * y**2
    assert sp.expand(U**2 - A - A**2 * Z) == 0

    h1 = U + a1 * A + a2 * A**2 + a3 * A**3 + a4 * A * Z + a5 * A * U
    h2 = Z + b1 * A + b2 * A**2 + b3 * A**3 + b4 * A * Z + b5 * A * U
    jacobian = sp.Poly(
        sp.expand(sp.diff(h1, x) * sp.diff(h2, y) - sp.diff(h1, y) * sp.diff(h2, x)),
        x,
        y,
    )
    assert jacobian.coeff_monomial(x**2 * y) == 8
    assert jacobian.coeff_monomial(x**4 * y**2) == 4
    assert jacobian.coeff_monomial(1) == 2
    print("PASS: constant=2, coeff(x^2*y)=8, coeff(x^4*y^2)=4")


if __name__ == "__main__":
    main()
