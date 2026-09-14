#!/usr/bin/env python3
"""Resolve the OPEN_FACE mixed low/high leaves by a direct triangular solve.

For the three (delta,partition) pairs whose q is NOT p^k*(polynomial) --- the
mixed local-exponent branch --- solve the face ODE exactly over Q at a concrete
zeta_Q-stable p and report the residual.
"""
from __future__ import annotations
from fractions import Fraction as F
import json
from pathlib import Path
import sympy as sp

z = sp.Symbol("z")
HERE = Path("/home/ubuntu/jc2/box/g9966n1b3-20260903")


def triangular_solve(u, v, W, delta, p):
    """Exact top-down solve for polynomial q with deg q = W*u+1."""
    X = F(u) * delta - F(v)
    a = F(W) * X - 1 + delta
    aq = sp.Rational(a.numerator, a.denominator)
    Xq = sp.Rational(X.numerator, X.denominator)
    D = W * u + 1
    P = sp.Poly(p, z)
    DP = sp.Poly(sp.diff(p, z), z)
    lead_p = P.LC()
    rem = sp.Poly(sp.expand(sp.Integer(v - u) * p ** (W + 1)), z)
    C = sp.Symbol("Cface")
    coeffs, compat = {}, []
    for j in range(D, -1, -1):
        basis = aq * DP * sp.Poly(z ** j, z)
        if j >= 1:
            basis = basis - Xq * sp.Integer(j) * P * sp.Poly(z ** (j - 1), z)
        lead = (aq * u - Xq * j) * lead_p
        target = rem.coeff_monomial(z ** (j + u - 1))
        if lead != 0:
            val = sp.nsimplify(target / lead)
            coeffs[j] = val
            rem = rem - sp.Poly(val, z) * basis
        else:
            compat.append(sp.expand(target))
            coeffs[j] = C
            rem = rem - sp.Poly(C, z) * basis
    for _, coeff in rem.terms():
        if sp.expand(coeff) != 0:
            compat.append(sp.expand(coeff))
    q = sum(coeffs[j] * z ** j for j in range(D + 1))
    return sp.expand(q), [c for c in compat if sp.expand(c) != 0]


CASES = [
    ("S2", 4, 7, 23, F(3, 2), [2, 1, 1], z**2 * (z**2 - 1)),
    ("S3", 4, 7, 23, F(3, 2), [2, 1, 1], z**2 * (z**2 - 1)),
    ("S7", 4, 7, 13, F(3, 2), [2, 1, 1], z**2 * (z**2 - 1)),
    ("S4", 3, 8, 23, F(2),    [2, 1],    z**2 * (z + 3)),
]

out = {"schema": "jc2.g9966n1b3.face-resolve/v1",
       "note": "mixed low/high local-exponent leaves; concrete zeta_Q-stable p over Q",
       "cases": []}
for name, u, v, W, delta, part, p in CASES:
    q, compat = triangular_solve(u, v, W, delta, sp.expand(p))
    X = F(u) * delta - F(v)
    a = F(W) * X - 1 + delta
    res = sp.expand(sp.Rational(a.numerator, a.denominator) * q * sp.diff(p, z)
                    - sp.Rational(X.numerator, X.denominator) * p * sp.diff(q, z)
                    - sp.Integer(v - u) * sp.expand(sp.expand(p) ** (W + 1)))
    Cf = sp.Symbol("Cface")
    solvable = not compat
    if compat:
        sols = sp.solve(compat, [Cf], dict=True)
        solvable = bool(sols)
        if solvable:
            q = sp.expand(q.subs(sols[0]))
            res = sp.expand(res.subs(sols[0]))
    rec = {"row": name, "delta": str(delta), "partition": part, "p": str(sp.factor(p)),
           "deg_q": int(sp.degree(sp.Poly(q, z))) if q != 0 else None,
           "q_factored": str(sp.factor(q))[:220],
           "compatibility_rows": [str(c)[:120] for c in compat],
           "residual": "0" if sp.expand(res) == 0 else str(res)[:200],
           "verdict": "SOLVABLE" if (solvable and sp.expand(res) == 0) else "DEAD"}
    out["cases"].append(rec)
    print(f"{name} delta={delta} lam={part}: {rec['verdict']} deg_q={rec['deg_q']} "
          f"residual={rec['residual'][:20]} q={rec['q_factored'][:80]}", flush=True)
(HERE / "face-resolve.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
