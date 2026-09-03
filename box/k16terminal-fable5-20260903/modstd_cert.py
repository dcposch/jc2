#!/usr/bin/env python3
"""Certified characteristic-zero Groebner basis over Q via modStd (exactness=1) in the ring-map
form (y a variable, H_t an ideal generator). Prints dim of <H_t, T_1..T_{2t-1}>."""
import argparse, re
ap = argparse.ArgumentParser(); ap.add_argument("t", type=int); ap.add_argument("rows")
a = ap.parse_args(); t = a.t; q = 2*t+1
rows = {}
for line in open(a.rows):
    m = re.match(r"T(\d+) = (.*);$", line.strip())
    if m: rows[int(m.group(1))] = m.group(2)
vars_ = "y,b3,b4" + "".join(",q(%d)" % j for j in range(2, t))
L = ['LIB "modstd.lib";', "ring R=0,(%s),(dp(1),wp(%s));" % (vars_, ",".join(map(str, [t+1, 1] + list(range(2, t))))),
     "poly H = %d*y^2%+d*y%+d;" % (12*q*q, -12*q*(t+1), (t+1)*(3*t+2)), "option(redSB);"]
for k in range(2*t): L.append("poly T%d = %s;" % (k, rows[k]))
L.append("ideal Jp = H," + ",".join("T%d" % k for k in range(1, 2*t)) + ";")
L.append("int tt = timer; ideal G = modStd(Jp, 1); print(\"MODSTD_EXACT t=%d dim=\" + string(dim(G)) + \" vdim=\" + string(vdim(G)) + \" size=\" + string(size(G)) + \" time=\" + string(timer-tt));" % t)
L.append("poly T0hom = T0 - subst(T0, b3,0, b4,0%s);" % "".join(", q(%d),0" % j for j in range(2, t)))
L.append('int NN; poly pw = 1; for (NN=1; NN<=6; NN++) { pw = pw*T0hom; if (reduce(pw, G) == 0) { print("MODSTD T0HOM power=" + string(NN)); break; } }')
L.append("quit;")
print("\n".join(L))
