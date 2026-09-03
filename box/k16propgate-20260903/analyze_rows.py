#!/usr/bin/env python3
"""Emit Singular tests on a terminal-row file produced by laurent_spine.py.

Tests (all in the weighted ring wt b3=t+1, wt b4=1, wt q_j=j):
  JPLUS: dim of <T_1..T_{2t-1}>  (0 <=> only the origin, which implies (8.1))
  T0HOM: T_0 - T_0(0) in radical(J_+) (checked by powers when dim>0)
  RESZ : dim of <T_1..T_{2t-1}, b4>  (RESIDUAL-ZERO <=> 0)
  TOPT : minimal N with b4^N in <T_t..T_{2t-1}>  (TOP-TAIL-UNIT <=> exists)
  CHARTS: exact b4=0 and (optionally) b4=1 full-chart unit tests
"""
import argparse, re
ap = argparse.ArgumentParser()
ap.add_argument("t", type=int); ap.add_argument("rows")
ap.add_argument("--fibre", default=None); ap.add_argument("--modp", type=int, default=None)
ap.add_argument("--b4one", action="store_true", help="also run the inhomogeneous b4=1 full chart")
ap.add_argument("--nmax", type=int, default=80)
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
L.append("poly T0hom = T0 - subst(T0, b3,0, b4,0%s);" % "".join(", q(%d),0" % j for j in range(2, t)))
L.append('print("T0CONST=" + string(T0 - T0hom));')
L.append("ideal Jp = " + ",".join("T%d" % k for k in range(1, 2*t)) + ";")
L.append("int tt = timer; ideal G = std(Jp); print(\"JPLUS t=%d dim=\" + string(dim(G)) + \" size=\" + string(size(G)) + \" time=\" + string(timer-tt));" % t)
L.append('print("JPLUS_LEAD=" + string(lead(G)));')
L.append('int NN; poly pw = 1; int found = 0; for (NN=1; NN<=%d; NN++) { pw = pw*T0hom; if (reduce(pw, G) == 0) { print("T0HOM_IN_RADICAL power=" + string(NN)); found = 1; break; } } if (found == 0) { print("T0HOM_NOT_FOUND_UP_TO=%d"); }' % (a.nmax, a.nmax))
L.append("ideal Jr = Jp, b4; tt = timer; ideal Gr = std(Jr); print(\"RESZ t=%d dim=\" + string(dim(Gr)) + \" time=\" + string(timer-tt)); print(\"RESZ_LEAD=\" + string(lead(Gr)));" % t)
L.append("ideal Jt = " + ",".join("T%d" % k for k in range(t, 2*t)) + ";")
L.append("tt = timer; ideal Gt = std(Jt); print(\"TOPT t=%d dim=\" + string(dim(Gt)) + \" time=\" + string(timer-tt));" % t)
L.append('pw = 1; found = 0; for (NN=1; NN<=%d; NN++) { pw = pw*b4; if (reduce(pw, Gt) == 0) { print("TOPT_B4_POWER=" + string(NN)); found = 1; break; } } if (found == 0) { print("TOPT_B4_NOT_FOUND_UP_TO=%d"); }' % (a.nmax, a.nmax))
L.append("ideal Jz = " + ",".join("subst(T%d, b4, 0)" % k for k in range(2*t)) + ";")
L.append("tt = timer; ideal Gz = std(Jz); if (reduce(1,Gz)==0) { print(\"CHART_B4_0=UNIT\"); } else { print(\"CHART_B4_0=NONUNIT dim=\" + string(dim(Gz))); }")
if a.b4one:
    L.append("ideal Jo = " + ",".join("subst(T%d, b4, 1)" % k for k in range(2*t)) + ";")
    L.append("tt = timer; ideal Go = std(Jo); if (reduce(1,Go)==0) { print(\"CHART_B4_1=UNIT time=\" + string(timer-tt)); } else { print(\"CHART_B4_1=NONUNIT\"); }")
L.append("quit;")
print("\n".join(L))
