#!/usr/bin/env python3
"""Light exact checks for the repaired constant corner of Sigray Prop. 4.2.

Standard library only.  Polynomials are coefficient tuples in increasing
eta-degree.  This is a mutation/control checker for the paper proof, not a
substitute for the fiber-origin lemma deg(p_F) >= 1.
"""

from fractions import Fraction as Q
from itertools import product
from math import gcd, lcm


def trim(p):
    p = list(map(Q, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def zero(p):
    return all(c == 0 for c in p)


def degree(p):
    p = trim(p)
    return -1 if zero(p) else len(p) - 1


def deriv(p):
    return trim([i * p[i] for i in range(1, len(p))] or [0])


def add(p, q):
    n = max(len(p), len(q))
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0) for i in range(n)])


def scale(a, p):
    return trim([Q(a) * c for c in p])


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def power(p, n):
    out = (Q(1),)
    for _ in range(n):
        out = mul(out, p)
    return out


def bracket_coefficient(d, p, e, q):
    """d*p*q' - e*p'*q, the eta coefficient of the leading bracket."""
    return add(scale(d, mul(p, deriv(q))),
               scale(-e, mul(deriv(p), q)))


def polynomials(max_degree):
    for n in range(max_degree + 1):
        for coeffs in product((-1, 0, 1), repeat=n + 1):
            p = trim(coeffs)
            if not zero(p) and degree(p) == n:
                yield p


def check_negative_and_zero_order():
    ps = [p for p in polynomials(3) if degree(p) >= 1]
    qs = list(polynomials(3))
    positive_orders = (Q(1, 2), Q(1), Q(3, 2), Q(2))
    negative_orders = (Q(-1, 2), Q(-1), Q(-3, 2), Q(-2))
    negative_checks = 0
    zero_checks = 0
    for p in ps:
        for q in qs:
            for d in positive_orders:
                for e in negative_orders:
                    assert not zero(bracket_coefficient(d, p, e, q)), (
                        "forbidden inverse dependence", d, p, e, q)
                    negative_checks += 1
                got_zero = zero(bracket_coefficient(d, p, Q(0), q))
                assert got_zero == (degree(q) == 0), (
                    "e=0 classification failed", d, p, q)
                zero_checks += 1
    return negative_checks, zero_checks


def check_positive_controls():
    checks = 0
    mutations = 0
    bases = ((0, 1), (1, 1), (1, -1, 1))
    for r in bases:
        for k, ell in ((1, 1), (2, 1), (3, 2), (4, 3)):
            assert gcd(k, ell) == 1
            # p=r^k, q=r^ell and e/d=ell/k give zero bracket.
            p, q = power(r, k), power(r, ell)
            d, e = Q(k), Q(ell)
            assert zero(bracket_coefficient(d, p, e, q))
            assert power(q, k) == power(p, ell)
            checks += 1

            # A coefficient mutation destroys the dependence in these controls.
            qm = add(q, (1,))
            if qm != q:
                assert not zero(bracket_coefficient(d, p, e, qm))
                mutations += 1
    return checks, mutations


def check_constant_step_arithmetic():
    legality = 0
    for k in range(1, 25):
        assert (gcd(k, 0) == 1) == (k == 1)
        legality += 1

    # Exact (mu,a,d,u) samples satisfying terminal b>=0 integral and e<0.
    mus = (Q(0), Q(1, 2), Q(1), Q(3, 2), Q(2), Q(5, 2))
    ds = (Q(1, 3), Q(1, 2), Q(1), Q(3, 2), Q(2), Q(3))
    us = tuple(Q(i, 3) for i in range(0, 10))
    terminal = 0
    for mu in mus:
        for a in range(1, 13):
            b = (mu - 1) * a + 1
            if b.denominator != 1 or b < 0:
                continue
            for d in ds:
                for u in us:
                    e = (mu - 1) * d + 1 - u
                    if e >= 0:
                        continue
                    kap = lcm(d.denominator, e.denominator, u.denominator,
                              mu.denominator)
                    delta_before = Q(kap) * (d - mu * d - 1 + u)
                    delta_after = Q(kap) * (d + e - mu * d - 1 + u)
                    assert delta_before == -Q(kap) * e > 0
                    assert delta_before.denominator == 1
                    assert delta_after == 0
                    assert d * b - e * a > 0  # no top eta-degree cancellation
                    assert d > (1 - u) * a    # forced T_a^nearrow
                    terminal += 1
    assert terminal > 0
    return legality, terminal


def check_inverse_firewall_control():
    # Abstract Laurent inverse dependence exists when p is constant.
    p = q = (Q(1),)
    assert zero(bracket_coefficient(Q(1), p, Q(-1), q))
    assert degree(p) == 0
    # Mutating to a genuine fiber-style nonconstant p kills it.
    p = (Q(1), Q(1))
    assert not zero(bracket_coefficient(Q(1), p, Q(-1), q))
    return 2


def main():
    neg, zer = check_negative_and_zero_order()
    pos, mut = check_positive_controls()
    legal, terminal = check_constant_step_arithmetic()
    controls = check_inverse_firewall_control()
    total = neg + zer + pos + mut + legal + terminal + controls
    print("Sigray Prop. 4.2 constant-shift checker: PASS")
    print(f"negative-order nonvanishing checks: {neg}")
    print(f"zero-order classification checks:   {zer}")
    print(f"positive dependence/mutations:       {pos}/{mut}")
    print(f"(k,0) legality checks:               {legal}")
    print(f"terminal delta/degree/scope checks:  {terminal}")
    print(f"inverse-firewall controls:           {controls}")
    print(f"total exact assertions grouped:      {total}")


if __name__ == "__main__":
    main()

