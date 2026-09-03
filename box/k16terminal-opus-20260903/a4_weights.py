#!/usr/bin/env python3
"""A4: the uniform positive grading on the WHOLE second-spine chart.

Claimed weights (weight 0 for y,g,g1,g2,c and all rationals):
    wt(h) = wt(s) = wt(b4) = 1
    wt(q_{j,0}) = j          (j = 2..2t)
    wt(C_j)     = j          (j = 1..t-1)
    wt(B0)=t, wt(b3)=t+1, wt(b2)=2t+1, wt(b1)=3t+1
Consequences to be checked on the charged records:
    every solved rhs is weighted-homogeneous of the weight of its variable;
    the eliminated variables carry the distinct weights 1,2,...,2t+1;
    band 4t+1-j of -E_t is weighted-homogeneous of weight j.
"""
import json, pathlib, sys, sympy as sp

SPINE = pathlib.Path("/home/ubuntu/jc2/box/k16spine-20260903")

def wts(t):
    w = {"b4": 1, "b3": t+1, "b2": 2*t+1, "b1": 3*t+1, "B0": t}
    for j in range(2, 2*t+1):
        w["q%d_0" % j] = j
    for j in range(1, t):
        w["C%d" % j] = j
    return w

def homog(expr, w, y):
    """Return sorted list of weights present, treating y as weight 0."""
    syms = sorted(expr.free_symbols - {y}, key=str)
    if not syms:
        return [0] if sp.expand(expr) != 0 else []
    p = sp.Poly(sp.expand(expr), *syms)
    out = set()
    for mon, _ in p.terms():
        out.add(sum(w[str(v)]*a for v, a in zip(syms, mon)))
    return sorted(out)

for t in [int(a) for a in sys.argv[1:]]:
    rec = json.loads((SPINE/("terminal_laurent_t%d.json" % t)).read_text())
    w = wts(t)
    y = sp.Symbol("q%d_1" % (2*t+1))
    ns = {k: sp.Symbol(k) for k in w}; ns[str(y)] = y
    ok = True
    print("=== t=%d ===" % t)
    ew = []
    for entry in [("b1", rec["b1_divisibility_pivot"]), ("B0", rec["B0_gauge_pivot"])]:
        name, blk = entry
        e = sp.sympify(blk["rhs"], locals=ns)
        got = homog(e, w, y)
        good = got in ([w[name]], [])
        ok &= good
        print("  %-6s wt=%-3d rhs weights=%-12s %s" % (name, w[name], got, "OK" if good else "FAIL"))
    for piv in rec["high_pivots"]:
        v = piv["variable"]; band = piv["band"]
        e = sp.sympify(piv["rhs"], locals=ns)
        got = homog(e, w, y)
        good = got in ([w[v]], [])
        ok &= good
        band_wt_ok = (4*t+1-band == w[v])
        ok &= band_wt_ok
        ew.append(w[v])
        print("  %-6s wt=%-3d band=%-3d (4t+1-band=%-3d %s) rhs weights=%-12s %s"
              % (v, w[v], band, 4*t+1-band, "match" if band_wt_ok else "MISMATCH",
                 got, "OK" if good else "FAIL"))
    exp = list(range(1, 2*t+2))
    good = sorted(ew) == exp
    ok &= good
    print("  eliminated-variable weights sorted = %s  expected %s  %s"
          % (sorted(ew), exp, "OK" if good else "FAIL"))
    print("  WEIGHTS_%d = %s" % (t, "PASS" if ok else "FAIL"))
