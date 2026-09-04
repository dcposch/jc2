#!/usr/bin/env python3
"""Re-derive the r-chart scalars and terminal (band, monomial) coefficients.

Uses the charged sq_engine (h-exponents as (a,b,c) for a t + b r + c) with
set_r(R).  No sp.factor/sp.simplify on the intermediate spine — only red()
and a final factor of the d-norm polynomial.  Prints the five (or four)
high-band pivots, then every surviving terminal monomial and the positive
integer roots of its norm.
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


def dnorm(u: sp.Expr) -> sp.Expr:
    """N(Du) = B^2 - A^2 (t+1)/3 for u = (Ad+B)/D, as a polynomial in t."""
    e = sp.together(u)
    n, den = sp.fraction(e)
    n = S._dred(n)
    P = sp.Poly(n, d)
    A, B = P.nth(1), P.nth(0)
    return sp.expand(B**2 - A**2 * (t + 1) / sp.Integer(3)), sp.expand(den)


def pos_int_roots(poly: sp.Expr):
    poly = sp.together(poly)
    num, _ = sp.fraction(sp.together(poly))
    num = sp.expand(num)
    if num == 0:
        return ["IDENTICALLY_ZERO"]
    f = sp.factor(num)
    roots = []
    for r, _m in sp.roots(sp.Poly(sp.numer(sp.together(f)), t)).items():
        if r.is_integer and r >= 1:
            roots.append(int(r))
    # rational-root fallback for factors sympy.roots misses
    try:
        for rr in sp.real_roots(sp.Poly(sp.integer_nthroot and 0, t)):
            pass
    except Exception:
        pass
    P = sp.Poly(sp.numer(sp.together(f)), t, domain="QQ")
    for rr in sp.rational_nthroot if False else P.real_roots():
        pass
    rats = sp.solve(sp.Eq(P.as_expr(), 0), t)
    out = []
    for r in rats:
        if getattr(r, "is_integer", False) and r >= 1:
            out.append(int(r))
    return sorted(set(out + roots))


def integer_roots_via_factor(N: sp.Expr):
    N = sp.factor(sp.expand(N))
    P = sp.Poly(sp.numer(sp.together(N)), t, domain="ZZ")
    found = []
    # try t=1..40
    for tv in range(1, 41):
        if P.eval(tv) == 0:
            found.append(tv)
    return N, found


def is_high(k, rfix):
    # k >= 2t  iff a>2 or (a==2 and b*r+c >= 0)
    return k[0] > 2 or (k[0] == 2 and k[1] * rfix + k[2] >= 0)


def main() -> None:
    RV = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    only = sys.argv[2:]  # optional: only these band names, e.g. A1 A2
    S.set_r(RV)
    T0 = time.time()
    print("# r=%d start" % RV, flush=True)
    O = spine(has_b1=(RV == 1))
    print("# spine built in %.1fs" % (time.time() - T0), flush=True)
    Phi = O["Phi"]
    print("# Phi bands:", [(sp.expand(ex(k)), sp.expand(4 * t + 1 - ex(k))) for k in sorted(Phi, reverse=True)], flush=True)
    high = {k: v for k, v in Phi.items() if is_high(k, RV)}
    print("# high keys", [sp.expand(ex(k)) for k in sorted(high, reverse=True)], flush=True)
    if RV == 1:
        print("# c5 raw", red(O["extra"]["b1"]), flush=True)
    else:
        print("# b1_condition", red(O["extra"]["b1_condition"]), flush=True)

    order = [(E(3, 1, 1), c1), (E(3, 0, 0), c2), (E(2, 2, 1), c3), (E(2, 1, 0), c4)]
    SOL = {}
    scalars = {}
    for key, var in order:
        t1 = time.time()
        row = red(high[key].subs(SOL))
        P = sp.Poly(row, var)
        assert P.degree() == 1, (var, P.degree())
        lead, rem = red(P.nth(1)), red(P.nth(0))
        Nlead, _ = dnorm(lead)
        Nlead_f, roots = integer_roots_via_factor(Nlead)
        val = red(-rem / lead)
        SOL[var] = val
        scalars[str(var)] = str(val)
        print(
            "PIVOT %s k=%s N(lead)=%s pos_int_roots=%s val=%s (%.1fs)"
            % (var, sp.expand(ex(key)), Nlead_f, roots, val, time.time() - t1),
            flush=True,
        )
    if RV == 1:
        C5 = red(O["extra"]["b1"].subs(SOL))
        scalars["c5"] = str(C5)
        print("PIVOT c5 val=%s" % C5, flush=True)
    for k in sorted(high, reverse=True):
        chk = red(high[k].subs(SOL))
        print("HIGH_VANISH k=%s %s" % (sp.expand(ex(k)), "OK" if chk == 0 else chk), flush=True)

    want = {
        "A1": None,
        "A2": None,
        "A3": None,
        "A4": None,
        "A5": None,
        "A6": None,
        "A7": None,
        "A8": None,
    }
    rows_out = {}
    for k in sorted(Phi, reverse=True):
        if is_high(k, RV):
            continue
        t1 = time.time()
        v = red(Phi[k].subs(SOL))
        kk = sp.expand(ex(k))
        if v == 0:
            print("TERM k=%s : 0 (%.1fs)" % (kk, time.time() - t1), flush=True)
            continue
        P = sp.Poly(v, x, b3)
        rows_out[str(kk)] = {}
        for mon, co in P.terms():
            co = red(co)
            Nn, den = dnorm(co)
            Nf, roots = integer_roots_via_factor(Nn)
            tag = "x^%d*b3^%d" % mon
            rows_out[str(kk)][tag] = {"coeff": str(co), "N": str(Nf), "roots": roots, "den": str(den)}
            print(
                "TERM k=%s wt=%s %s roots=%s N=%s coeff=%s (%.1fs)"
                % (kk, sp.expand(4 * t + 1 - ex(k)), tag, roots, Nf, co, time.time() - t1),
                flush=True,
            )
    out = {"r": RV, "c": scalars, "rows": rows_out, "elapsed": time.time() - T0}
    (HERE / ("qplane_r%d.json" % RV)).write_text(json.dumps(out, indent=2, sort_keys=True))
    print("# elapsed %.1fs wrote qplane_r%d.json" % (time.time() - T0, RV), flush=True)


if __name__ == "__main__":
    main()
