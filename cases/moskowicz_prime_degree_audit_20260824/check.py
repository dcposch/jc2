#!/usr/bin/env python3
"""Exact regression for the Moskowicz prime-degree source audit.

This checks the cubic member of the universal rare-property control family.
The all-exponent statement is proved by UFD factor matching in the report;
the finite sweep here is deliberately labeled as regression, not proof.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


# Q[zeta]/(zeta^2+zeta+1), represented as a+b*zeta.
Cyclo = tuple[Fraction, Fraction]
Monomial = tuple[int, int]  # powers of (s,v)
Poly = dict[Monomial, Cyclo]


def cadd(x: Cyclo, y: Cyclo) -> Cyclo:
    return (x[0] + y[0], x[1] + y[1])


def cmul(x: Cyclo, y: Cyclo) -> Cyclo:
    # zeta^2=-zeta-1
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0] - x[1] * y[1])


def cpow(x: Cyclo, n: int) -> Cyclo:
    out: Cyclo = (Fraction(1), Fraction(0))
    for _ in range(n):
        out = cmul(out, x)
    return out


def padd(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = cadd(out.get(monomial, (Fraction(0), Fraction(0))), coefficient)
        if out[monomial] == (0, 0):
            del out[monomial]
    return out


def pmul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for (si, vi), a in left.items():
        for (sj, vj), b in right.items():
            key = (si + sj, vi + vj)
            out[key] = cadd(out.get(key, (Fraction(0), Fraction(0))), cmul(a, b))
    return {m: c for m, c in out.items() if c != (0, 0)}


def linear_power(s_coefficient: Cyclo, v_coefficient: int, n: int) -> Poly:
    out: Poly = {}
    for k in range(n + 1):
        # k copies of s and n-k copies of v
        coefficient = cpow(s_coefficient, k)
        coefficient = (coefficient[0] * comb(n, k) * v_coefficient ** (n - k),
                       coefficient[1] * comb(n, k) * v_coefficient ** (n - k))
        out[(k, n - k)] = coefficient
    return out


def image(i: int, j: int, zeta_power: int) -> Poly:
    zeta = cpow((Fraction(0), Fraction(1)), zeta_power)
    return pmul(linear_power(zeta, 1, i), linear_power(zeta, 2, j))


def main() -> None:
    one: Cyclo = (Fraction(1), Fraction(0))
    zeta: Cyclo = (Fraction(0), Fraction(1))

    assert cpow(zeta, 3) == one
    assert cpow(zeta, 1) != one and cpow(zeta, 2) != one

    # u=s^3 and v are fixed by both nontrivial elements of Gal(C(s,v)/C(s^3,v)).
    assert cpow(zeta, 3) == one

    tested = 0
    for i in range(25):
        for j in range(25):
            if i == j == 0:
                continue
            base = image(i, j, 0)
            for power in (1, 2):
                assert image(i, j, power) != base
                tested += 1

    # The optional extra generator x+y=2s+3v is also non-fixed.
    base_sum: Poly = {(1, 0): (Fraction(2), Fraction(0)),
                      (0, 1): (Fraction(3), Fraction(0))}
    for power in (1, 2):
        moved_sum: Poly = {(1, 0): tuple(2 * a for a in cpow(zeta, power)),
                           (0, 1): (Fraction(3), Fraction(0))}
        assert moved_sum != base_sum

    print("MOSKOWICZ-PRIME-DEGREE-AUDIT: PASS")
    print("rare_degree_three_control = C(s^3,v) subset C(s,v)")
    print("coordinates = x=s+v; y=s+2v")
    print(f"nontrivial_galois_images_checked = {tested}")
    print("universal_all_exponent_argument = UFD factor matching in report")
    print("paper_first_case_supported = false")
    print("paper_second_case_repairable = true")
    print("no_prime_degree_theorem_usable = false")
    print("jc2_inference = false")


if __name__ == "__main__":
    main()
