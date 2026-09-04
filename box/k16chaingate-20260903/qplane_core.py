#!/usr/bin/env python3
"""Symbolic-in-t derivation of the r=1 high-band scalars and of A1, A2, A5.

Skips A3,A4,A6,A7,A8 (not needed for (3.6)).  No intermediate factor/simplify.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sq_engine as S  # noqa: E402
from sq_engine import (  # noqa: E402
    E,
    b3,
    c1,
    c2,
    c3,
    c4,
    d,
    ex,
    red,
    spine,
    t,
    x,
)


def scalar_At(u):
    """A_t-coefficient of a single (x,b3)-monomial; unit-ness ignores the monomial."""
    u = red(u)
    if u == 0:
        return u
    P = sp.Poly(u, x, b3)
    terms = P.terms()
    assert len(terms) == 1, terms
    return red(terms[0][1])


def dnorm(u):
    u = scalar_At(u)
    e = sp.together(u)
    n, den = sp.fraction(e)
    n = S._dred(n)
    P = sp.Poly(n, d)
    A, B = P.nth(1), P.nth(0)
    return sp.expand(B**2 - A**2 * (t + 1) / sp.Integer(3)), sp.expand(den)


def roots_1_40(N):
    Nf = sp.factor(sp.expand(N))
    num = sp.numer(sp.together(Nf))
    num = sp.expand(num.subs({x: 1, b3: 1}))
    P = sp.Poly(num, t, domain="QQ")
    found = [tv for tv in range(1, 41) if P.eval(tv) == 0]
    return Nf, found


def is_high(k, rfix):
    return k[0] > 2 or (k[0] == 2 and k[1] * rfix + k[2] >= 0)


def main():
    RV = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    S.set_r(RV)
    T0 = time.time()
    print("# r=%d core start" % RV, flush=True)
    O = spine(has_b1=(RV == 1))
    print("# spine %.1fs" % (time.time() - T0), flush=True)
    Phi = O["Phi"]
    print("# bands", [sp.expand(ex(k)) for k in sorted(Phi, reverse=True)], flush=True)
    high = {k: v for k, v in Phi.items() if is_high(k, RV)}
    order = [(E(3, 1, 1), c1), (E(3, 0, 0), c2), (E(2, 2, 1), c3), (E(2, 1, 0), c4)]
    SOL = {}
    outc = {}
    for key, var in order:
        t1 = time.time()
        row = red(high[key].subs(SOL))
        P = sp.Poly(row, var)
        assert P.degree() == 1, (var, P.degree())
        lead, rem = red(P.nth(1)), red(P.nth(0))
        Nlead, _ = dnorm(lead)
        Nf, rts = roots_1_40(Nlead)
        val = red(-rem / lead)
        SOL[var] = val
        outc[str(var)] = str(val)
        print("PIVOT %s k=%s roots=%s N=%s" % (var, sp.expand(ex(key)), rts, Nf), flush=True)
        print("  val=%s (%.1fs)" % (val, time.time() - t1), flush=True)
    if RV == 1:
        C5 = red(O["extra"]["b1"].subs(SOL))
        outc["c5"] = str(C5)
        print("PIVOT c5 val=%s" % C5, flush=True)
    else:
        print("b1_condition", red(O["extra"]["b1_condition"].subs(SOL)), flush=True)
    for k in sorted(high, reverse=True):
        chk = red(high[k].subs(SOL))
        print("HIGH_VANISH k=%s %s" % (sp.expand(ex(k)), "OK" if chk == 0 else chk), flush=True)

    # A1: 2t-1 = E(2,-1) after set_r?  2t-1 = (2,0,-1)
    # A2: t+3r+1 = E(1,3,1)
    # A5: t-2 = E(1,0,-2)
    want = [("A1", E(2, 0, -1), (0, 2)), ("A2", E(1, 3, 1), (3, 0)), ("A5", E(1, 0, -2), (0, 3))]
    rows = {}
    for name, key, mon in want:
        t1 = time.time()
        if key not in Phi:
            print("%s key %s missing; keys=%s" % (name, key, list(Phi)), flush=True)
            continue
        v = red(Phi[key].subs(SOL))
        P = sp.Poly(v, x, b3)
        terms = {m: red(c) for m, c in P.terms()}
        extra = [m for m in terms if m != mon]
        co = terms.get(mon)
        if co is None:
            print("%s missing mon %s present=%s" % (name, mon, list(terms)), flush=True)
            continue
        Nn, den = dnorm(co)
        Nf, rts = roots_1_40(Nn)
        rows[name] = {"coeff": str(co), "N": str(Nf), "roots": rts, "den": str(den), "extra": str(extra)}
        print("%s extra=%s roots=%s N=%s" % (name, extra, rts, Nf), flush=True)
        print("  coeff=%s den=%s (%.1fs)" % (co, den, time.time() - t1), flush=True)
    payload = {"r": RV, "c": outc, "rows": rows, "elapsed": time.time() - T0}
    (HERE / ("qplane_core_r%d.json" % RV)).write_text(json.dumps(payload, indent=2, sort_keys=True))
    print("# elapsed %.1fs" % (time.time() - T0), flush=True)


if __name__ == "__main__":
    main()
