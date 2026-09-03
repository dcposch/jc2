#!/usr/bin/env python3
"""Verify the universal four-polynomial remainder decomposition.

This is independent of a fixed band length.  It regards U,R,V,S,T as
polynomials in the h-coordinate X and writes

    Q = U(X) + A R(X) + y B,
    P = V(X) + A S(X) + B T(X) + g z.

The symbols Up,...,Tp stand for X-derivatives.  The calculation expands the
Jacobian through the six brackets among h,A,B,z, then reduces modulo the
monic relation h(pi,gamma)-X.  It is a compact audit of the row tags and of
the duplicate-row identities used by the middle-spine analysis.
"""

from __future__ import annotations

import sympy as sp


gamma, pi, X = sp.symbols("gamma pi X")
b1, b2, b3, b4 = sp.symbols("b1 b2 b3 b4")
U, Up, R, Rp = sp.symbols("U Up R Rp")
V, Vp, S, Sp, T, Tp = sp.symbols("V Vp S Sp T Tp")
y, g = sp.symbols("y g")

z = pi - gamma
B = pi * z + b1 * pi + b2
A = pi * B + b3
h = pi * A + b4

Qh = Up + A * Rp
Ph = Vp + A * Sp + B * Tp

# The six nonzero brackets, with h replaced by the independent symbol X.
J_hA = pi * (X - b4)
J_hB = 2 * (X - b4) - b3 * pi
J_hz = 3 * A - 2 * b3 - b2 * pi
J_AB = A - b3
J_Az = 2 * B - b2
J_Bz = z + b1

raw = sp.expand(
    J_hA * (Qh * S - R * Ph)
    + J_hB * (Qh * T - y * Ph)
    + J_hz * (g * Qh)
    + J_AB * (R * T - y * S)
    + J_Az * (g * R)
    + J_Bz * (g * y)
)

coefficient_domain = sp.QQ[
    gamma, X, b1, b2, b3, b4,
    U, Up, R, Rp, V, Vp, S, Sp, T, Tp, y, g,
]
remainder = sp.rem(
    sp.Poly(raw, pi, domain=coefficient_domain),
    sp.Poly(h - X, pi, domain=coefficient_domain),
).as_expr()
coefficients = dict(sp.Poly(sp.expand(remainder), gamma, pi).terms())

expected_tags = {
    (1, 2), (1, 1), (1, 0),
    (0, 3), (0, 2), (0, 1), (0, 0),
}
assert set(coefficients) == expected_tags

C12 = coefficients[(1, 2)]
C11 = coefficients[(1, 1)]
C10 = coefficients[(1, 0)]
C03 = coefficients[(0, 3)]
C02 = coefficients[(0, 2)]
C01 = coefficients[(0, 1)]
C00 = coefficients[(0, 0)]

# These are polynomial identities, before any band specialization.
assert sp.expand(C03 + C12) == 0
assert sp.expand(C02 + b1 * C12 + C11) == 0
assert sp.expand(C10 + y * g) == 0


def show(name: str, expression: sp.Expr) -> None:
    print(f"{name}={sp.factor(expression)}")


print("COMPACT_REMAINDER_IDENTITIES_PASS")
show("C12", C12)
show("C11", C11)
show("C01", C01)
show("C00", C00)
print("C03=-C12")
print("C02=-b1*C12-C11")
print("C10=-y*g")
