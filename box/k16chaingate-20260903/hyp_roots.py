#!/usr/bin/env python3
"""Integer-root audit of the claimed A2^{(r)} d-norms, r=1..5, plus A1,A5.

These are the polynomials printed in the charged Opus (5.3) and (3.3)/(3.5).
This script does not derive them; it only classifies their positive integer
roots (unit-ness locus).  Derivation is qplane_symbolic.py.
"""
from __future__ import annotations

import sympy as sp

t = sp.symbols("t")


def pos_roots(name, expr):
    f = sp.factor(sp.expand(expr))
    found = [n for n in range(1, 80) if sp.Poly(sp.numer(sp.together(f)), t).eval(n) == 0]
    print("%s : %s" % (name, f))
    print("   pos int roots in 1..79: %s" % (found or "NONE"))
    return found


def main():
    Q4 = {
        1: 27 * t**4 + 206 * t**3 + 527 * t**2 + 540 * t + 300,
        2: 27 * t**4 + 278 * t**3 + 963 * t**2 + 1380 * t + 1100,
        3: 27 * t**4 + 350 * t**3 + 1531 * t**2 + 2800 * t + 2792,
        4: 27 * t**4 + 422 * t**3 + 2231 * t**2 + 4944 * t + 5808,
        5: 27 * t**4 + 494 * t**3 + 3063 * t**2 + 7956 * t + 10652,
    }
    A1N = -t**2 * (t - 2) * (3 * t - 1) ** 2 * (3 * t + 1) ** 2 * (3 * t + 2) * (
        27 * t**3 + 17 * t**2 + t + 2
    ) / 3
    A5N = -t**2 * (t - 2) ** 2 * (t + 1) * (3 * t - 1) * (3 * t + 1) ** 2 * (4 * t + 1)
    pos_roots("N(A1)=N(alpha)", A1N)
    pos_roots("N(A5)=N(phi)", A5N)
    cub = 27 * t**3 + 17 * t**2 + t + 2
    pos_roots("27t^3+17t^2+t+2", cub)

    A2N = {
        1: 3 * t**2 * (t - 1) ** 6 * (t + 1) * (t + 2) ** 6 * (3 * t + 1) ** 2 * (4 * t + 1)
        * (t**2 + 3 * t + 6)
        * (25 * t**2 + 12 * t - 12)
        * Q4[1] ** 3,
        2: 3 * t**2 * (t - 2) ** 6 * (t + 1) ** 2 * (t + 3) ** 6 * (3 * t + 1) ** 2 * (4 * t + 1)
        * (25 * t - 23)
        * (t**2 + 5 * t + 13)
        * Q4[2] ** 3,
        3: 3 * t**2 * (t - 3) ** 6 * (t + 1) * (t + 4) ** 6 * (3 * t + 1) ** 2 * (4 * t + 1)
        * (25 * t**2 - 8 * t - 32)
        * (t**2 + 7 * t + 22)
        * Q4[3] ** 3,
        4: 3 * t**2 * (t - 4) ** 6 * (t + 1) * (t + 5) ** 6 * (3 * t + 1) ** 2 * (4 * t + 1)
        * (25 * t**2 - 18 * t - 39)
        * (t**2 + 9 * t + 33)
        * Q4[4] ** 3,
        5: 3 * t**2 * (t - 5) ** 6 * (t + 1) * (t + 6) ** 6 * (3 * t + 1) ** 2 * (4 * t + 1)
        * (25 * t**2 - 28 * t - 44)
        * (t**2 + 11 * t + 46)
        * Q4[5] ** 3,
    }
    for r, N in A2N.items():
        pos_roots("N(A2^(%d))" % r, N)
        pos_roots("Q4^(%d)" % r, Q4[r])
        print("   CHAIN-STEP bound t>=%d; t=r is %s bound"
              % (3 * r + 3, "below" if r < 3 * r + 3 else "NOT below"))

    # extra quadratics: any integer roots?
    quads = {
        "25t^2+12t-12": 25 * t**2 + 12 * t - 12,
        "25t-23": 25 * t - 23,
        "25t^2-8t-32": 25 * t**2 - 8 * t - 32,
        "25t^2-18t-39": 25 * t**2 - 18 * t - 39,
        "25t^2-28t-44": 25 * t**2 - 28 * t - 44,
        "t^2+3t+6": t**2 + 3 * t + 6,
        "t^2+5t+13": t**2 + 5 * t + 13,
        "t^2+7t+22": t**2 + 7 * t + 22,
        "t^2+9t+33": t**2 + 9 * t + 33,
        "t^2+11t+46": t**2 + 11 * t + 46,
        "t^2+t+1": t**2 + t + 1,
    }
    for name, e in quads.items():
        pos_roots(name, e)

    # Res vs N conversion identity at a generic t: Res_y(H, Ad+B) vs 12 q^2 N
    # checked in res_identity.py


if __name__ == "__main__":
    main()
