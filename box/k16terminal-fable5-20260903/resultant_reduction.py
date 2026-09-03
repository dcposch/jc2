#!/usr/bin/env python3
"""Section-7 reduction check: with alpha_t a unit, TOP-TAIL-UNIT <=> the resultants
Res_b3(T_{2t-1}, T_k)|_{b4=1}, k=t..2t-2, generate [1] in A_t[q]; RESIDUAL-ZERO <=>
the resultants at b4=0 (k=1..2t-2) have only the trivial zero in weighted q-space."""
import argparse, re
ap = argparse.ArgumentParser(); ap.add_argument("t", type=int); ap.add_argument("rows")
a = ap.parse_args(); t = a.t; q = 2*t+1
rows = {}
for line in open(a.rows):
    m = re.match(r"T(\d+) = (.*);$", line.strip())
    if m: rows[int(m.group(1))] = m.group(2)
vars_ = "b3,b4" + "".join(",q(%d)" % j for j in range(2, t))
wts = [t+1, 1] + list(range(2, t))
L = ["ring R=(0,y),(%s),wp(%s);" % (vars_, ",".join(map(str, wts))),
     "minpoly = %d*y^2%+d*y%+d;" % (12*q*q, -12*q*(t+1), (t+1)*(3*t+2)), "option(redSB);"]
for k in range(2*t): L.append("poly T%d = %s;" % (k, rows[k]))
L.append('print("b3-degree of T%d: " + string(deg(T%d, intvec(1,0%s))));' % (2*t-1, 2*t-1, ",0"*(t-2)))
L.append("ideal Rtop; int k;")
for k in range(t, 2*t-1):
    L.append("Rtop[%d] = resultant(subst(T%d,b4,1), subst(T%d,b4,1), b3);" % (k-t+1, 2*t-1, k))
L.append('ideal Gtop = std(Rtop); if (reduce(1,Gtop)==0) { print("TOPTAIL_RESULTANTS_UNIT t=%d"); } else { print("TOPTAIL_RESULTANTS_NONUNIT t=%d dim=" + string(dim(Gtop))); }' % (t, t))
L.append("ideal Rres; ")
for k in range(1, 2*t-1):
    L.append("Rres[%d] = resultant(subst(T%d,b4,0), subst(T%d,b4,0), b3);" % (k, 2*t-1, k))
L.append('ideal Gres = std(Rres); print("RESIDUAL_RESULTANTS t=%d dim=" + string(dim(Gres)) + " lead=" + string(lead(Gres)));' % t)
L.append("quit;")
print("\n".join(L))
