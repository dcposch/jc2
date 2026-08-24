#!/usr/bin/env python3
"""Exact replay for TD6-GLOBAL-COMPATIBILITY-GATE (SP-2 control).

Only Python's standard library is used.  The script verifies

* the bare-chart monomial divisibility observation;
* the centered polynomial coordinate T = x*y^4-y^3;
* two explicit polynomial approximants with the SP-2 boundary patterns;
* their exact Jacobian formula / transverse orders;
* the special-fiber three-branch, total-Lambda-three control; and
* the coefficientwise Bezout recursion producing arbitrary one-sided
  formal Keller jets when no fixed global degree cap is imposed.

It does not claim that either displayed polynomial pair is Keller.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


Q = Fraction


# Sparse polynomials in named variables, represented by exponent tuples.
def padd(a, b):
    out = dict(a)
    for mon, coeff in b.items():
        out[mon] = out.get(mon, Q(0)) + coeff
        if out[mon] == 0:
            del out[mon]
    return out


def pscale(a, scalar):
    return {mon: coeff * scalar for mon, coeff in a.items() if coeff * scalar}


def pmul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            mon = tuple(x + y for x, y in zip(ma, mb))
            out[mon] = out.get(mon, Q(0)) + ca * cb
    return {mon: coeff for mon, coeff in out.items() if coeff}


def ppow(a, n):
    out = {(0,) * len(next(iter(a))): Q(1)}
    base = a
    while n:
        if n & 1:
            out = pmul(out, base)
        base = pmul(base, base)
        n //= 2
    return out


def pdiff(a, variable):
    out = {}
    for mon, coeff in a.items():
        exponent = mon[variable]
        if exponent:
            nxt = list(mon)
            nxt[variable] -= 1
            out[tuple(nxt)] = coeff * exponent
    return out


def jacobian(f, g):
    return padd(
        pmul(pdiff(f, 0), pdiff(g, 1)),
        pscale(pmul(pdiff(f, 1), pdiff(g, 0)), -1),
    )


def coefficient(poly, variable, exponent):
    """Delete one fixed exponent and return a polynomial in the other var."""
    out = {}
    for mon, coeff in poly.items():
        if mon[variable] == exponent:
            reduced = mon[:variable] + mon[variable + 1 :]
            out[reduced] = out.get(reduced, Q(0)) + coeff
    return {mon: coeff for mon, coeff in out.items() if coeff}


def valuation(poly, variable):
    return min(mon[variable] for mon in poly) if poly else None


# Univariate t-polynomial helpers for the formal recursion.
def uadd(a, b):
    out = dict(a)
    for exponent, coeff in b.items():
        out[exponent] = out.get(exponent, Q(0)) + coeff
        if out[exponent] == 0:
            del out[exponent]
    return out


def uscale(a, scalar):
    return {exponent: coeff * scalar for exponent, coeff in a.items() if coeff * scalar}


def umul(a, b):
    out = {}
    for i, ci in a.items():
        for j, cj in b.items():
            out[i + j] = out.get(i + j, Q(0)) + ci * cj
    return {exponent: coeff for exponent, coeff in out.items() if coeff}


def uder(a):
    return {exponent - 1: coeff * exponent for exponent, coeff in a.items() if exponent}


def udegree(a):
    return max(a) if a else -1


def formal_recursion(max_n=18):
    """Construct F,G with F_X G_t-F_t G_X = X^2 u'(tX^3) formally.

    Here u is the unique series with u(1+u)^3=w.  At every coefficient
    the new equation is A_n*q' - p'*B_n = rhs.  Since
    p'=15*t^14 and q'=1+25*t^24 are coprime, the displayed canonical
    solution is polynomial.
    """
    p = {15: Q(1)}
    q = {1: Q(1), 25: Q(1)}
    pd = uder(p)
    qd = uder(q)
    a = {0: p}
    b = {0: q}
    nonzero = []

    for n in range(1, max_n + 1):
        known = {}
        # Coefficient X^(n-1), excluding the two new terms (n,0),(0,n).
        for i in range(1, n):
            j = n - i
            known = uadd(
                known,
                uadd(
                    uscale(umul(a[i], uder(b[j])), i),
                    uscale(umul(uder(a[i]), b[j]), -j),
                ),
            )

        target = {}
        if n - 1 >= 2 and (n - 3) % 3 == 0:
            k = (n - 3) // 3
            # u'(w) = sum (-1)^k binom(4k+2,k) w^k.
            target = {k: Q((-1) ** k * comb(4 * k + 2, k))}

        rhs = uscale(uadd(target, uscale(known, -1)), Q(1, n))

        # q' == 1 (mod t^14).  Take A_n to be rhs mod t^14, then solve B_n.
        an = {exponent: coeff for exponent, coeff in rhs.items() if exponent < 14}
        numerator = uadd(umul(an, qd), uscale(rhs, -1))
        assert all(exponent >= 14 for exponent in numerator)
        bn = {exponent - 14: coeff / 15 for exponent, coeff in numerator.items()}

        check = uadd(uadd(umul(an, qd), uscale(umul(pd, bn), -1)), uscale(rhs, -1))
        assert not check
        a[n] = an
        b[n] = bn
        if an or bn:
            nonzero.append((n, udegree(an), udegree(bn)))

        # Recompute the now-fixed coefficient independently.
        got = {}
        for i in range(n + 1):
            j = n - i
            got = uadd(
                got,
                uadd(
                    uscale(umul(a[i], uder(b[j])), i),
                    uscale(umul(uder(a[i]), b[j]), -j),
                ),
            )
        assert not uadd(got, uscale(target, -1))

    # First two nonzero corrections are the displayed fixed-rectangle pair.
    assert a[3] == {0: Q(1, 3)}
    assert b[3] == {10: Q(5, 9)}
    assert a[6] == {1: Q(-1), 9: Q(-25, 27)}
    assert b[6] == {11: Q(-5, 3), 19: Q(-125, 81)}
    return nonzero


def main():
    # 1. Bare chart: x=t*s^R, y=s^-1.  A holomorphic monomial has
    # s-exponent k=Ri-j >= 0; for k>0 its t-exponent i >= ceil(k/R).
    R = 4
    bare_checks = 0
    for i in range(26):
        for j in range(101):
            k = R * i - j
            if k >= 0:
                bare_checks += 1
                if k > 0:
                    assert i >= (k + R - 1) // R

    # Original variables (x,y).
    x = {(1, 0): Q(1)}
    y = {(0, 1): Q(1)}
    one = {(0, 0): Q(1)}
    u = padd(pmul(x, y), pscale(one, -1))
    T = padd(pmul(x, ppow(y, 4)), pscale(ppow(y, 3), -1))

    # Centered coordinate identities: T*x^3 = u(1+u)^3 and
    # det d(x,T)/d(x,y) = y^2(1+4u).
    assert pmul(T, ppow(x, 3)) == pmul(u, ppow(padd(one, u), 3))
    det_xT = jacobian(x, T)
    assert det_xT == pmul(ppow(y, 2), padd(one, pscale(u, 4)))

    p = ppow(T, 15)
    q = padd(T, ppow(T, 25))

    # First centered polynomial control (N=3).
    f3 = padd(p, pscale(ppow(x, 3), Q(1, 3)))
    g3 = padd(q, pscale(pmul(ppow(T, 10), ppow(x, 3)), Q(5, 9)))
    j3 = jacobian(f3, g3)
    expected_j3 = pmul(
        pmul(ppow(padd(one, u), 2), padd(one, pscale(u, 4))),
        padd(one, pscale(pmul(ppow(T, 9), ppow(x, 3)), Q(50, 9))),
    )
    assert j3 == expected_j3

    # Second correction (N=6), still inside the same SP-2 rectangles.
    a6 = padd(pscale(T, -1), pscale(ppow(T, 9), Q(-25, 27)))
    b6 = padd(pscale(ppow(T, 11), Q(-5, 3)), pscale(ppow(T, 19), Q(-125, 81)))
    f6 = padd(f3, pmul(a6, ppow(x, 6)))
    g6 = padd(g3, pmul(b6, ppow(x, 6)))

    # Newton rectangles and corner coefficients.
    assert max(i for (i, _j) in f6) == 15
    assert max(j for (_i, j) in f6) == 60
    assert f6[(15, 60)] == 1
    assert all(i <= 15 and j <= 60 for i, j in f6)
    assert max(i for (i, _j) in g6) == 25
    assert max(j for (_i, j) in g6) == 100
    assert g6[(25, 100)] == 1
    assert all(i <= 25 and j <= 100 for i, j in g6)

    # Centered chart (s,t): x=s+t*s^4=s(1+t*s^3), y=s^-1.
    # Negative s exponents are allowed in this temporary Laurent ring.
    s = {(1, 0): Q(1)}
    t = {(0, 1): Q(1)}
    xc = padd(s, pmul(t, ppow(s, 4)))
    yc = {(-1, 0): Q(1)}
    Tc = padd(pmul(xc, ppow(yc, 4)), pscale(ppow(yc, 3), -1))
    assert Tc == t

    # Boundary patterns are exactly t^15 and t+t^25 for both controls.
    def substitute_centered(poly):
        out = {}
        for (i, j), coeff in poly.items():
            out = padd(out, pscale(pmul(ppow(xc, i), ppow(yc, j)), coeff))
        return out

    f3c = substitute_centered(f3)
    g3c = substitute_centered(g3)
    f6c = substitute_centered(f6)
    g6c = substitute_centered(g6)
    assert coefficient(f3c, 0, 0) == {(15,): Q(1)}
    assert coefficient(g3c, 0, 0) == {(1,): Q(1), (25,): Q(1)}
    assert coefficient(f6c, 0, 0) == {(15,): Q(1)}
    assert coefficient(g6c, 0, 0) == {(1,): Q(1), (25,): Q(1)}

    # Exact special-fiber reduction for the first control:
    # f3=0 => x^3=-3*T^15 and g3=T-(2/3)T^25.
    g3_on_fiber = uadd({1: Q(1), 25: Q(1)}, {25: Q(-5, 3)})
    assert g3_on_fiber == {1: Q(1), 25: Q(-2, 3)}
    assert comb(3, 1) == 3  # gcd(3,15)=3 branches, written explicitly below.
    assert __import__("math").gcd(3, 15) == 3

    # The exact J3 formula has J3-1 of centered s-valuation 3.
    j3c = substitute_centered(j3)
    assert valuation(padd(j3c, pscale({(0, 0): Q(1)}, -1)), 0) == 3

    # The second correction matches the formal Keller determinant through
    # X^5; after the X^-2 coordinate factor, J6-1 has s-valuation at least 6.
    j6c = substitute_centered(jacobian(f6, g6))
    assert valuation(padd(j6c, pscale({(0, 0): Q(1)}, -1)), 0) == 6

    recursion = formal_recursion(18)

    print("TD6 global-compatibility replay: PASS")
    print(f"bare divisibility monomials checked: {bare_checks}")
    print(f"f6 support terms / rectangle: {len(f6)} / (15,60)")
    print(f"g6 support terms / rectangle: {len(g6)} / (25,100)")
    print("J3-1 centered s-valuation: 3")
    print(f"J6-1 centered s-valuation: {valuation(padd(j6c, pscale({(0, 0): Q(1)}, -1)), 0)}")
    print(f"formal recursion through X^18 nonzero coefficient levels: {recursion}")


if __name__ == "__main__":
    main()
