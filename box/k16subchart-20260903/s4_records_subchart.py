#!/usr/bin/env python3
"""S4: restrict exact terminal records to the sub-chart R={q_{t-r,0}, b3}.

For every record this prints the surviving terminal rows, their monomials in
(x,b3) with x=q_{t-r,0}, and for each coefficient the norm
   N(u) = Res_y(H_t, u)      (u is a unit of A_t  <=>  N(u) != 0),
so the exceptional small indices are read off the records themselves.
"""
import sys, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16subchart-20260903")
from sq_load import load

RV = int(sys.argv[1])
for arg in sys.argv[2:]:
    tv, chart = (arg.split(":") + ["spine"])[:2]
    tv = int(tv)
    if tv - RV < 2:
        print("=== t=%d r=%d : no residual q_{t-r,0} (t-r<2), skipped" % (tv, RV))
        continue
    D = load(tv, chart)
    y, b3, H = D["y"], D["b3"], D["H"]
    Q = sp.Symbol("q%d_0" % (tv-RV))
    zero = {v: 0 for v in D["variables"] if v not in (Q, b3)}
    print("=== t=%d chart=%s  R={%s, b3}  weights (%d, %d) ==="
          % (tv, chart, Q, tv-RV, tv+1))
    for k in sorted(D["rows"], reverse=True):
        e = sp.expand(D["rows"][k].subs(zero))
        if e == 0:
            print("   k=%-3d : 0" % k); continue
        P = sp.Poly(e, Q, b3)
        out = []
        for mon, co in P.terms():
            N = sp.factor(sp.resultant(sp.Poly(H, y), sp.Poly(sp.expand(co), y)))
            out.append("x^%d b3^%d [wt %d] N=%s" %
                       (mon[0], mon[1], mon[0]*(tv-RV)+mon[1]*(tv+1), N))
        print("   k=%-3d wt=%-3d : %s" % (k, 4*tv+1-k, " ; ".join(out)))
