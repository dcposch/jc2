#!/usr/bin/env python3
"""Exact arithmetic controls for the repaired Sigray Proposition 5.1.

This uses only Python's standard library.  It checks the coefficient-level
leading-bracket lemma and finite integer-slope models used in the proof.  It
does not claim to construct an Eggers--Wall tree.
"""

from fractions import Fraction
from itertools import product


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def derivative(p):
    return trim(tuple(i * p[i] for i in range(1, len(p))) or (0,))


def scale(c, p):
    return trim(tuple(c * a for a in p))


def multiply(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def subtract(p, q):
    n = max(len(p), len(q))
    out = [0] * n
    for i in range(n):
        out[i] = (p[i] if i < len(p) else 0) - (q[i] if i < len(q) else 0)
    return trim(out)


def bracket_coefficient(d, p, e, q):
    # d*p*q' - e*p'*q, the eta coefficient of the leading Jacobian.
    return subtract(scale(d, multiply(p, derivative(q))),
                    scale(e, multiply(derivative(p), q)))


def is_zero(p):
    return trim(p) == (0,)


def check_constant_q_classification():
    checks = 0
    # Nonconstant p with nonzero leading coefficient; nonzero constant q.
    for degree in range(1, 5):
        for lower in product(range(-1, 2), repeat=degree):
            for lead in (-1, 1):
                p = tuple(lower) + (lead,)
                for q0 in (-2, -1, 1, 2):
                    q = (q0,)
                    for d in range(-3, 4):
                        for e in range(-3, 4):
                            got = is_zero(bracket_coefficient(d, p, e, q))
                            assert got == (e == 0), (d, p, e, q, got)
                            checks += 1
    return checks


def first_zero(values):
    for i, value in enumerate(values):
        if value == 0:
            return i
    return None


def check_piecewise_threshold_profiles():
    """Sweep discrete integer-slope shadows of the continuous proof.

    While rho>0, p-degree>=1 and the bracket/condition-(7) lemma gives
    q-degree>=1, hence Delta rho=1-r_p-r_q<=-1.  At rho=0,
    nonincrease plus nonnegativity forces Delta rho=0.
    """
    checks = 0
    for rho0 in range(1, 13):
        for prefix_len in range(1, 8):
            for rp, rq in product(range(1, 5), repeat=2):
                rho = Fraction(rho0)
                values = [rho]
                for _ in range(prefix_len):
                    if rho > 0:
                        rho += 1 - rp - rq
                        # The geometric theorem forbids crossing below zero;
                        # profiles that would cross are stopped at their exact
                        # affine zero and checked separately below.
                        if rho < 0:
                            break
                    values.append(rho)
                assert all(values[i + 1] <= values[i] for i in range(len(values) - 1))
                if len(values) > 1 and values[-1] > 0:
                    assert values[-1] <= rho0 - (len(values) - 1)
                checks += 1

    # Rational affine pieces hit zero at a rational time no later than rho0.
    for rho0 in range(1, 31):
        for rp, rq in product(range(1, 8), repeat=2):
            slope = 1 - rp - rq
            assert slope <= -1
            hit = Fraction(rho0, -slope)
            assert hit > 0 and hit <= rho0
            assert Fraction(rho0) + slope * hit == 0
            checks += 1
    return checks


def check_stable_tail_and_negative_controls():
    checks = 0
    # r is -d_{g-b}>0.  The shifted profile is exactly zero; an unshifted
    # finite nonzero constant dominates and leaves rho=r>0.
    for r in range(1, 101):
        for v in range(r + 2, r + 52):
            d_a = Fraction(r + 1 - v)
            d_shifted = Fraction(-r)
            rho_shifted = d_a + d_shifted + v - 1
            rho_unshifted = d_a + 0 + v - 1
            assert rho_shifted == 0
            assert rho_unshifted == r > 0
            # shifted leading q is eta-constant but has e=-r !=0, so its
            # bracket with any nonconstant p is nonzero; wrong shift has e=0.
            p = (1, -2, 1)  # (eta-1)^2
            q = (3,)
            assert not is_zero(bracket_coefficient(d_a, p, d_shifted, q))
            assert is_zero(bracket_coefficient(d_a, p, 0, q))
            checks += 1
    return checks


def main():
    groups = {
        "constant-q bracket classification": check_constant_q_classification(),
        "piecewise threshold profiles": check_piecewise_threshold_profiles(),
        "forced-shift tail and negative controls": check_stable_tail_and_negative_controls(),
    }
    total = sum(groups.values())
    print("SIGRAY_PROP51_FORCED_PUNCTURE_SHIFT_PASS")
    for name, count in groups.items():
        print(f"{name}: {count}")
    print(f"total grouped checks: {total}")


if __name__ == "__main__":
    main()
