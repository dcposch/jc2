#!/usr/bin/env python3
"""Replay of the charged JPLUS certificate + the weighted-homogeneity hypothesis.

Ring and generator construction are copied verbatim from the charged analyze_rows.py
(same variable order b3,b4,q(2..t-1); same weights wp(t+1,1,2,..,t-1); same minpoly).
Added: homog() assertions on every T_k, k>=1, and the T_0 = const + hom split.
Usage: jplus_hom.py t rows [--fibre r] [--modp p]
"""
import argparse, re
ap = argparse.ArgumentParser()
ap.add_argument("t", type=int); ap.add_argument("rows")
ap.add_argument("--fibre", default=None); ap.add_argument("--modp", type=int, default=None)
a = ap.parse_args(); t = a.t; q = 2*t+1
rows = {}
for line in open(a.rows):
    m = re.match(r"T(\d+) = (.*);$", line.strip())
    if m: rows[int(m.group(1))] = m.group(2)
assert sorted(rows) == list(range(2*t)), sorted(rows)
vars_ = "b3,b4" + "".join(",q(%d)" % j for j in range(2, t))
wts = [t+1, 1] + list(range(2, t))
L = []
if a.fibre is None:
    L.append("ring R=(0,y),(%s),wp(%s);" % (vars_, ",".join(map(str, wts))))
    L.append("minpoly = %d*y^2%+d*y%+d;" % (12*q*q, -12*q*(t+1), (t+1)*(3*t+2)))
else:
    L.append("ring R=%s,(%s),wp(%s);" % (a.modp if a.modp else 0, vars_, ",".join(map(str, wts))))
L.append("option(redSB);")
for k in range(2*t):
    L.append("poly T%d = %s;" % (k, rows[k]))
# --- hypothesis (H-hom): T_k weighted homogeneous of weight 4t+1-k for k>=1
L.append('print("WEIGHTS=" + string(ringlist(R)[3]));')
for k in range(1, 2*t):
    L.append('if (T%d == 0) { print("HOM k=%d ZERO"); } else { print("HOM k=%d homog=" + string(homog(T%d)) + " deg=" + string(deg(T%d)) + " expected=%d"); }'
             % (k, k, k, k, k, 4*t+1-k))
L.append("poly T0hom = T0 - subst(T0, b3,0, b4,0%s);" % "".join(", q(%d),0" % j for j in range(2, t)))
L.append('poly T0con = T0 - T0hom;')
L.append('print("T0CONST=" + string(T0con));')
L.append('if (T0con == 0) { print("T0CONST_IS_ZERO -- UNIT CLAIM FAILS"); } else { print("T0CONST_NONZERO=yes"); }')
L.append('if (T0 == 0) { print("T0 ZERO"); } else { print("T0_homog=" + string(homog(T0)) + " (expected 0: T0 is INHOMOGENEOUS)"); }')
L.append('if (T0hom == 0) { print("T0HOM ZERO"); } else { print("T0HOM_homog=" + string(homog(T0hom)) + " deg=" + string(deg(T0hom)) + " expected=%d"); }' % (4*t+1))
# --- the certificate
L.append("ideal Jp = " + ",".join("T%d" % k for k in range(1, 2*t)) + ";")
L.append('int tt = timer; ideal G = std(Jp); print("JPLUS t=%d dim=" + string(dim(G)) + " size=" + string(size(G)) + " time=" + string(timer-tt));' % t)
L.append('print("JPLUS_LEAD=" + string(lead(G)));')
L.append('print("JPLUS_HOMOG_IDEAL=" + string(homog(Jp)));')
L.append("quit;")
print("\n".join(L))
