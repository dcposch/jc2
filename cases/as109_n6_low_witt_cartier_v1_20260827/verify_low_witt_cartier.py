#!/usr/bin/env python3
"""Exact replay for the AS109 residual n=6 low-Witt Cartier gate.

Uses only Python stdlib integer and finite-field sparse arithmetic.  It is a
control/replay program, not a search for a lift.
"""

from __future__ import annotations

import json
import random


PRIME = 109


def clean(poly):
    return {mon: c for mon, c in poly.items() if c}


def add(a, b):
    out = dict(a)
    for mon, c in b.items():
        out[mon] = out.get(mon, 0) + c
    return clean(out)


def scale(c, a):
    return clean({mon: c * v for mon, v in a.items()})


def mul(a, b):
    out = {}
    for (i, j), c in a.items():
        for (k, ell), d in b.items():
            mon = (i + k, j + ell)
            out[mon] = out.get(mon, 0) + c * d
    return clean(out)


def dx(a):
    return clean({(i - 1, j): i * c for (i, j), c in a.items() if i})


def dy(a):
    return clean({(i, j - 1): j * c for (i, j), c in a.items() if j})


ONE = {(0, 0): 1}
X = {(1, 0): 1}
Y = {(0, 1): 1}
X109 = {(109, 0): 1}
X108 = {(108, 0): 1}


def determinant_minus_one(A, B):
    P = add(add(X, scale(-1, X109)), scale(PRIME, A))
    Q = add(Y, scale(PRIME, B))
    return add(add(mul(dx(P), dy(Q)), scale(-1, mul(dy(P), dx(Q)))), scale(-1, ONE))


def packed_rhs(A, B):
    linear = add(add(dx(A), dy(B)), scale(-1, X108))
    nonlinear = add(mul(add(dx(A), scale(-1, X108)), dy(B)), scale(-1, mul(dy(A), dx(B))))
    return add(scale(PRIME, linear), scale(PRIME * PRIME, nonlinear))


def umod(a):
    return {e: c % PRIME for e, c in a.items() if c % PRIME}


def uadd(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = (out.get(e, 0) + c) % PRIME
    return umod(out)


def uscale(c, a):
    return umod({e: c * v for e, v in a.items()})


def umul(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            out[e + f] = (out.get(e + f, 0) + c * d) % PRIME
    return umod(out)


def upow(a, n):
    out = {0: 1}
    base = umod(a)
    while n:
        if n & 1:
            out = umul(out, base)
        base = umul(base, base)
        n >>= 1
    return out


def uderivative(a):
    return umod({e - 1: e * c for e, c in a.items() if e})


def derivative_obstructions(a):
    return {e: c for e, c in umod(a).items() if (e + 1) % PRIME == 0}


def antiderivative(a):
    obs = derivative_obstructions(a)
    if obs:
        raise ValueError(f"Cartier obstruction: {obs}")
    out = {}
    for e, c in umod(a).items():
        out[e + 1] = c * pow((e + 1) % PRIME, -1, PRIME) % PRIME
    return umod(out)


def uint(poly):
    """Lift a univariate finite-field polynomial to integer coefficients."""
    return {(e, 0): c for e, c in umod(poly).items()}


def uy(poly, y_degree):
    return {(e, y_degree): c for e, c in umod(poly).items()}


def upow_integer(a, n):
    out = {0: 1}
    base = dict(a)
    while n:
        if n & 1:
            tmp = {}
            for e, c in out.items():
                for f, d in base.items():
                    tmp[e + f] = tmp.get(e + f, 0) + c * d
            out = clean(tmp)
        tmp = {}
        for e, c in base.items():
            for f, d in base.items():
                tmp[e + f] = tmp.get(e + f, 0) + c * d
        base = clean(tmp)
        n >>= 1
    return out


def uderivative_integer(a):
    return clean({e - 1: e * c for e, c in a.items() if e})


def umul_integer(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            out[e + f] = out.get(e + f, 0) + c * d
    return clean(out)


def wronskian(m, d, h):
    a = m // d
    b = 6 // d
    pm = {e: PRIME * c for e, c in upow_integer(h, a).items()}
    q6 = {e: PRIME * c for e, c in upow_integer(h, b).items()}
    left = {e: 6 * c for e, c in umul_integer(uderivative_integer(pm), q6).items()}
    right = {e: -m * c for e, c in umul_integer(pm, uderivative_integer(q6)).items()}
    return clean({e: left.get(e, 0) + right.get(e, 0) for e in set(left) | set(right)})


def y_coefficient(poly, degree):
    return umod({i: c for (i, j), c in poly.items() if j == degree})


def main():
    rng = random.Random(20260827)
    determinant_controls = []
    for idx in range(12):
        A = {}
        B = {}
        for _ in range(5):
            A[(rng.randrange(0, 9), rng.randrange(0, 8))] = rng.randrange(-7, 8)
            B[(rng.randrange(0, 9), rng.randrange(0, 8))] = rng.randrange(-7, 8)
        A = clean(A)
        B = clean(B)
        ok = determinant_minus_one(A, B) == packed_rhs(A, B)
        assert ok
        determinant_controls.append(ok)

    h_d6_bad = {108: 1}
    h_d3_bad = {54: 1}
    bad_d6 = derivative_obstructions(upow(h_d6_bad, 1))
    bad_d3 = derivative_obstructions(upow(h_d3_bad, 2))
    assert bad_d6 == {108: 1}
    assert bad_d3 == {108: 1}

    h_good = {0: 1, 109: 1}
    good_rows = {}
    for b in (1, 2):
        b6 = upow(h_good, b)
        assert derivative_obstructions(b6) == {}
        a5 = uscale(-6, antiderivative(b6))
        A = uy(a5, 5)
        B = add({(108, 1): 1}, uy(b6, 6))
        first_witt = add(dx(A), dy(B))
        first_witt_mod = {(i, j): c % PRIME for (i, j), c in first_witt.items() if c % PRIME}
        assert first_witt_mod == X108
        assert y_coefficient(first_witt, 5) == {}
        good_rows[str(b)] = {
            "b6_support": sorted(b6),
            "a5_support": sorted(a5),
            "y5_row_zero": True,
        }

    assert wronskian(12, 6, {0: 1, 109: 1}) == {}
    assert wronskian(15, 3, {0: 1, 54: 1}) == {}

    top_a_control = upow(h_good, 2)
    assert uderivative(top_a_control) == {}
    assert derivative_obstructions(upow(h_good, 1)) == {}

    result = {
        "verdict": "PASS-LOW-WITT-CARTIER",
        "prime": PRIME,
        "packed_determinant_controls": len(determinant_controls),
        "packed_determinant_identity": all(determinant_controls),
        "d6_Hbar_108_obstruction": bad_d6,
        "d3_Hbar_54_squared_obstruction": bad_d3,
        "frobenius_pattern_positive_controls": good_rows,
        "common_core_wronskian_d6": "ZERO",
        "common_core_wronskian_d3": "ZERO",
        "top_a_frobenius_derivative": "ZERO",
        "scope": "valuation-one q6 content branch only; no lift existence/nonexistence inference",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

