#!/usr/bin/env python3
"""S6: restriction of the terminal rows to each coordinate axis of the cone.

Axis of v: all other residual variables set to 0.  By the grading each row
restricts to  mu_k * v^((4t+1-k)/wt(v))  when wt(v) | 4t+1-k, and to 0 otherwise.
V(I_{t,+}) contains the v-axis  <=>  every mu_k (1<=k<=2t-1) vanishes.
"""
import sys, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16subchart-20260903")
from sq_load import load

for arg in sys.argv[1:]:
    tv, chart = (arg.split(":") + ["spine"])[:2]
    tv = int(tv)
    D = load(tv, chart)
    y, H = D["y"], D["H"]
    print("=== t=%d chart=%s ===" % (tv, chart))
    for v in D["variables"]:
        zero = {u: 0 for u in D["variables"] if u is not v}
        live = []
        for k in sorted(D["rows"], reverse=True):
            if k == 0:
                continue
            e = sp.expand(D["rows"][k].subs(zero))
            if e == 0:
                continue
            for mon, co in sp.Poly(e, v).terms():
                N = sp.resultant(sp.Poly(H, y), sp.Poly(sp.expand(co), y))
                live.append("k=%d:%s^%d N%s0" % (k, v, mon[0], "!=" if N else "=="))
        print("   %-6s axis : %s" % (v, ", ".join(live) if live
                                     else "ALL POSITIVE BANDS VANISH  <-- axis in V(I)"))
