#!/usr/bin/env python3
"""Exact checks for the source-supported node-local ODE projection.

This is deliberately *not* a global f,g realisability checker.  At r >= 2 it
checks D(P,Q,p,q)=c*p.  At the r=1 endpoint it checks Moh's different,
constant-right-hand-side equation D(n*,m*,g,f)=kappa.  All arithmetic is over
QQ with displayed algebraic relations reduced explicitly.
"""

from __future__ import annotations

import sympy as sp


x, z = sp.symbols("x z")


def D(a, b, p, q, var=x):
    return sp.expand(a * p * sp.diff(q, var) - b * q * sp.diff(p, var))


def check(label, condition):
    if condition is not True and condition != 0:
        raise AssertionError(label)
    print(f"PASS {label}")


def parent_64():
    a, lam = sp.symbols("a lam", nonzero=True)
    zz = x**4
    p = (zz - a) ** 3
    q = lam * x * (zz - a) * (zz - sp.Rational(5, 4) * a)
    c = 15 * lam * a**2
    check("64 parent ODE", sp.factor(D(12, 9, p, q) - c * p))
    check("64 parent q squarefree", sp.factor(sp.discriminant(q, x)) != 0)
    print("64 parent:", sp.factor(p), sp.factor(q), "c =", c)


def bottom_64():
    s, rho = sp.symbols("s rho", nonzero=True)
    G = (
        z**3
        + s * z**2
        + s**2 * (sp.Rational(3, 8) - rho / 24) * z
        + s**3 * (4 - rho) / 96
    )
    F = z**2 + sp.Rational(3, 4) * s * z + s**2 * (6 - rho) / 32
    g = G.subs(z, x**4)
    f = x * F.subs(z, x**4)
    kappa = sp.rem(D(4, 3, g, f), rho**2 - 6, rho)
    check("64 bottom constant after rho^2=6", sp.diff(kappa, x))
    check("64 bottom kappa nonzero", sp.factor(kappa) != 0)
    for label, value in (
        ("Disc(G)", sp.discriminant(G, z)),
        ("Disc(F)", sp.discriminant(F, z)),
        ("Res(G,F)", sp.resultant(G, F, z)),
    ):
        reduced = sp.factor(sp.rem(sp.together(value).as_numer_denom()[0], rho**2 - 6, rho))
        check("64 bottom " + label, reduced != 0)
        print("64 bottom", label, "=", sp.factor(value))
    print("64 bottom kappa =", sp.factor(kappa), "; relation rho^2=6")


def parent_75():
    a, theta, lam = sp.symbols("a theta lam", nonzero=True)
    zz = x**5
    b = (7 - 5 * theta) * a
    d = theta * a
    p = (zz - a) ** 3 * (zz - b)
    q = lam * x * (zz - a) * (zz - b) * (zz - d)
    rel = 15 * theta**2 - 35 * theta + 21
    remainder = sp.rem(sp.Poly(D(20, 16, p, q) + 20 * lam * a * b * d * p, theta), sp.Poly(rel, theta)).as_expr()
    check("75 parent ODE modulo theta relation", sp.factor(remainder))
    check("75 parent quadratic separable", sp.discriminant(rel, theta) == -35)
    print("75 parent: b =", b, "; d =", d, "; c =", -20 * lam * a * b * d)
    print("75 parent field relation:", rel, "= 0")


def bottom_75():
    s = sp.symbols("s", nonzero=True)
    G = (
        z**4
        + sp.Rational(3, 2) * s * z**3
        + sp.Rational(21, 16) * s**2 * z**2
        + sp.Rational(35, 64) * s**3 * z
        + sp.Rational(63, 512) * s**4
    )
    F = z**3 + s * z**2 + sp.Rational(5, 8) * s**2 * z + sp.Rational(3, 32) * s**3
    g = x * G.subs(z, x**2)
    f = F.subs(z, x**2)
    kappa = -sp.Rational(189, 8192) * s**7
    check("75 bottom constant ODE", sp.factor(D(3, 2, g, f) - kappa))
    for label, value in (
        ("Disc(G)", sp.discriminant(G, z)),
        ("Disc(F)", sp.discriminant(F, z)),
        ("Res(G,F)", sp.resultant(G, F, z)),
    ):
        check("75 bottom " + label, sp.factor(value) != 0)
        print("75 bottom", label, "=", sp.factor(value))
    print("75 bottom kappa =", kappa)


def parent_90():
    d = sp.symbols("d", nonzero=True)
    p = x**8
    q = x * (x**35 - d)
    c = 280 * d
    check("90 j=3 parent ODE", sp.factor(D(8, 36, p, q) - c * p))
    check("90 j=3 q squarefree", sp.factor(sp.discriminant(q, x)) != 0)
    print("90 j=3 parent: p = x^8; q = x(x^35-d); c =", c)


def parent_108():
    a, lam = sp.symbols("a lam", nonzero=True)
    zz = x**4
    R = (
        z**4
        - sp.Rational(17, 4) * a * z**3
        + sp.Rational(221, 32) * a**2 * z**2
        - sp.Rational(663, 128) * a**3 * z
        + sp.Rational(3315, 2048) * a**4
    )
    p = (zz - a) ** 7
    q = lam * x * (zz - a) * R.subs(z, zz)
    c = -sp.Rational(23205, 512) * lam * a**5
    check("108 parent ODE", sp.factor(D(28, 21, p, q) - c * p))
    disc = sp.factor(sp.discriminant(R, z))
    resa = sp.factor(R.subs(z, a))
    res0 = sp.factor(R.subs(z, 0))
    for label, value in (("Disc(R)", disc), ("R(a)", resa), ("R(0)", res0)):
        check("108 parent " + label, value != 0)
        print("108 parent", label, "=", value)
    print("108 parent R =", R)
    print("108 parent c =", c)


if __name__ == "__main__":
    parent_64()
    bottom_64()
    parent_75()
    bottom_75()
    parent_90()
    parent_108()
    print("ALL EXPLICIT FAMILY CHECKS PASSED")
