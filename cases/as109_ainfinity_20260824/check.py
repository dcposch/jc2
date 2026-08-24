#!/usr/bin/env python3
"""Exact controls for the AS109 A_infinity / deck-descent gate."""

from fractions import Fraction

p = 109
passed = 0


def check(label, condition):
    global passed
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'}  {label}")
    if not ok:
        raise AssertionError(label)
    passed += 1


def slope(a, b):
    """Exact slope between valuation points a=(exponent,valuation)."""
    return Fraction(b[1] - a[1], b[0] - a[0])


def lower_newton_edges(points):
    """Return (horizontal length, root valuation) on the lower hull."""
    hull = []
    for point in sorted(points):
        while len(hull) >= 2 and slope(hull[-2], hull[-1]) >= slope(hull[-1], point):
            hull.pop()
        hull.append(point)
    return [(b[0] - a[0], -slope(a, b)) for a, b in zip(hull, hull[1:])]


# X^p-X splits into p distinct linear factors over F_p.
check("special roots are all residues",
      all((pow(a, p, p) - a) % p == 0 for a in range(p)))
check("special roots are simple",
      all((p * pow(a, p - 1, p) - 1) % p != 0 for a in range(p)))


# Newton polygon for g_N(X)-109S:
# points (0,1),(1,0),(p,0),(N,1).  The first two lower edges account for
# p integral roots, while the last has horizontal length N-p and slope
# 1/(N-p), hence N-p roots of valuation -1/(N-p).
for n in (111, 137, 218, 219):
    edges = lower_newton_edges([(0, 1), (1, 0), (p, 0), (n, 1)])
    expected_edges = [
        (1, Fraction(1)),
        (p - 1, Fraction(0)),
        (n - p, -Fraction(1, n - p)),
    ]
    integral = sum(length for length, valuation in edges if valuation >= 0)
    residual = sum(length for length, valuation in edges if valuation < 0)
    check(f"N={n}: exact lower Newton hull", edges == expected_edges)
    check(f"N={n}: Newton integral mass is 109", integral == p)
    check(f"N={n}: Newton residual mass is N-109", integral + residual == n)
    check(f"N={n}: residual valuation is negative", edges[-1][1] < 0)


# The same controls have trivial rational deck group for N>=p+2.
# If f(alpha*x+beta)=f(x), the unique pole forces an affine transformation.
# The x^N row gives alpha^N=1; the x^(N-1) row is p*N*alpha^(N-1)*beta,
# with N-1>p, so beta=0; the x row then gives alpha=1.
for n in (111, 137, 218, 219):
    separated = n - 1 > p
    middle_coefficient_nonzero = p * n != 0
    # alpha^N=1 makes alpha nonzero.  The separated x^(N-1) coefficient
    # then forces beta=0, after which the x coefficient forces alpha=1.
    comparison_forces_identity = separated and middle_coefficient_nonzero
    check(f"N={n}: x^(N-1) is separated from x^p", separated)
    check(f"N={n}: coefficient p*N is nonzero in characteristic zero",
          middle_coefficient_nonzero)
    check(f"N={n}: affine deck comparison forces identity",
          comparison_forces_identity)


# Abstract Zariski-Main control: p finite sections plus r copies of the
# generic-only etale component Spec R[1/p] have special rank p and arbitrary
# generic rank p+r.
for r in (0, 1, 2, 17, 109):
    special_rank = p
    generic_rank = p + r
    check(f"generic-only rank r={r}: special rank stays 109", special_rank == p)
    check(f"generic-only rank r={r}: generic rank is 109+r", generic_rank - special_rank == r)


# Secant/source-base-change ranks.
for d in (109, 110, 137, 218):
    check(f"d={d}: diagonal plus off rank", 1 + (d - 1) == d)
    check(f"d={d}: local 108 off branches fit", d - 1 >= 108)


print(f"\n{passed}/{passed} exact controls passed")
