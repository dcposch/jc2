#!/usr/bin/env python3
"""Specialise the claimed r=1 closed forms at t=6..14 vs charged fixed_r1.json.

Ring map: engine and closed forms live in Q(t)[d]/(3d^2-(t+1)); the charged
fixed_r1.json stores the same encoding at integer t.  Matching names is not
the test: we subtract in Q[d]/(3d^2-(t+1)).
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

t, d = sp.symbols("t d")
Q4 = 27 * t**4 + 206 * t**3 + 527 * t**2 + 540 * t + 300

c1 = (t + 2) * (
    -9 * d * t**3 - 12 * d * t**2 - 9 * d * t + 30 * d
    + 27 * t**4 + 153 * t**3 + 283 * t**2 + 247 * t + 90
) / ((2 * t + 1) * Q4)
c2 = -(6 * d * t - 3 * d + 9 * t**2 + 2 * t - 1) / (6 * t * (3 * t - 1))
A1 = (
    t
    * (3 * t + 1)
    * ((27 * t**3 - 30 * t**2 + t - 2) * d + (6 * t**3 + 13 * t**2 - 3 * t + 2))
    / (12 * (2 * t + 1) ** 2 * (3 * t - 1) ** 2 * (3 * t + 2))
)
A5 = -t * (t - 2) * (3 * t + 1) * (6 * d * t - t - 1) / (72 * (2 * t + 1) ** 3 * (3 * t - 1))
Q4e = 27 * t**4 + 206 * t**3 + 527 * t**2 + 540 * t + 300
A2N = (
    3
    * t**2
    * (t - 1) ** 6
    * (t + 1)
    * (t + 2) ** 6
    * (3 * t + 1) ** 2
    * (4 * t + 1)
    * (t**2 + 3 * t + 6)
    * (25 * t**2 + 12 * t - 12)
    * Q4e**3
)
A1N = (
    -t**2
    * (t - 2)
    * (3 * t - 1) ** 2
    * (3 * t + 1) ** 2
    * (3 * t + 2)
    * (27 * t**3 + 17 * t**2 + t + 2)
    / 3
)
A5N = -t**2 * (t - 2) ** 2 * (t + 1) * (3 * t - 1) * (3 * t + 1) ** 2 * (4 * t + 1)

FIX = json.loads(Path("/tmp/jc2-lane.SxWsoD/inputs/fixed_r1.json").read_text())
dS = sp.Symbol("d")


def N_of(co, tv):
    """N(Du)=B^2-A^2(t+1)/3 at integer t, co a string in d."""
    e = sp.together(sp.sympify(co).subs(d, dS))
    n, den = sp.fraction(e)
    P = sp.Poly(sp.expand(n), dS)
    A, B = P.nth(1), P.nth(0)
    return sp.expand(B**2 - A**2 * (tv + 1) / 3), sp.expand(den)


def red_at(expr, tv):
    val = sp.simplify(expr.subs(t, tv))
    # reduce d^2
    P = sp.Poly(sp.expand(sp.together(val) * sp.denom(sp.together(val))), d)
    # just cancel
    return sp.together(val.subs(d, dS))


def same(a, b, tv):
    diff = sp.together(sp.sympify(a).subs(d, dS) - sp.sympify(b).subs(d, dS))
    n, den = sp.fraction(diff)
    n = sp.expand(n.subs(dS**2, (tv + 1) / 3))
    # iterate
    n = sp.expand(n)
    P = sp.Poly(n, dS)
    tot = 0
    for (k,), co in P.terms():
        pw, kk = 1, k
        while kk >= 2:
            pw = pw * (tv + 1) / 3
            kk -= 2
        tot += co * pw * dS**kk
    return sp.expand(tot) == 0


def main():
    ok = True
    for ts, rec in sorted(FIX.items(), key=lambda kv: int(kv[0])):
        tv = int(ts)
        cfix = rec["c"]
        rows = rec["rows"]
        tests = []
        tests.append(("c1", c1.subs(t, tv), cfix["c1"]))
        tests.append(("c2", c2.subs(t, tv), cfix["c2"]))
        # A1 = k=2t-1, x^0 b3^2
        a1row = rows[str(2 * tv - 1)]["x^0*b3^2"][0]
        tests.append(("A1", A1.subs(t, tv), a1row))
        # A5 = k=t-2, x^0 b3^3  (for t>=6 this band is terminal and unmerged)
        a5row = rows[str(tv - 2)]["x^0*b3^3"][0]
        tests.append(("A5", A5.subs(t, tv), a5row))
        print("=== t=%d ===" % tv)
        for name, closed, engine in tests:
            hit = same(closed, engine, tv)
            ok &= hit
            print("  %s %s" % (name, "OK" if hit else "FAIL"))
            if not hit:
                print("    closed", closed)
                print("    engine", engine)
        # A2 lives at band t+4, monomial x^3
        a2co = rows[str(tv + 4)]["x^3*b3^0"][0]
        Nn, den = N_of(a2co, tv)
        claimed = sp.Integer(A2N.subs(t, tv))
        # charged (3.5) is N(den * A2) with den = (2t+1)^3 (t^2+3t+6) Q4^3,
        # while N_of returns N(numer(A2)) = N(den A2) only if A2=numer/den
        # Compare vanishing and the ratio N(A2)=Nn/den^2 vs claimed/den_form^2.
        den_form = ((2 * t + 1) ** 3 * (t**2 + 3 * t + 6) * Q4e**3).subs(t, tv)
        # N(den_form * A2) = den_form^2 * N(A2) = den_form^2 * Nn / den^2
        lhs = sp.expand(den_form**2 * Nn / den**2)
        hitN = sp.expand(lhs - claimed) == 0
        ok &= hitN
        print("  A2_NORM %s  Nnum=%s den=%s" % ("OK" if hitN else "FAIL", Nn, den))
        if not hitN:
            print("    lhs", lhs)
            print("    claimed", claimed)
        for label, co_key, claimedN in (
            ("A1_NORM", (str(2 * tv - 1), "x^0*b3^2"), A1N.subs(t, tv)),
            ("A5_NORM", (str(tv - 2), "x^0*b3^3"), A5N.subs(t, tv)),
        ):
            co = rows[co_key[0]][co_key[1]][0]
            Nn, den = N_of(co, tv)
            NA = sp.together(Nn / den**2)
            hitn = sp.expand(sp.together(NA - claimedN)) == 0
            # A1/A5 closed forms already matched; this checks the printed N vs N(u)
            print("  %s raw_N(u) vs printed : match=%s N(u)=%s printed=%s"
                  % (label, hitn, NA, claimedN))
        # all eight unit-ness at this t
        vanished = []
        for kb, mons in rows.items():
            if kb == "0":
                continue
            for mon, pair in mons.items():
                Nn, den = N_of(pair[0], tv)
                if Nn == 0:
                    vanished.append((kb, mon))
        print("  vanished_positive_norms %s" % (vanished or "NONE"))
        ok &= not vanished
    print("SPEC_FIXED_R1 =", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
