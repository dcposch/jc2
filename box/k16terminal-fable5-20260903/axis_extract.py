#!/usr/bin/env python3
"""Restrict pivots and rows to coordinate axes (b4-axis, q2-axis, b3-axis) and print the
axis coefficients as elements of A_t (exact)."""
import argparse, re
ap = argparse.ArgumentParser(); ap.add_argument("t", type=int); ap.add_argument("rows"); ap.add_argument("--fibre", default=None)
a = ap.parse_args(); t = a.t; q = 2*t+1
rows, piv = {}, []
for line in open(a.rows):
    m = re.match(r"T(\d+) = (.*);$", line.strip())
    if m: rows[int(m.group(1))] = m.group(2); continue
    m = re.match(r"PIVOT (\d+) (\S+) (\S+) (.*);$", line.strip())
    if m: piv.append((int(m.group(1)), m.group(2), m.group(3), m.group(4)))
vars_ = "b3,b4" + "".join(",q(%d)" % j for j in range(2, t))
wts = [t+1, 1] + list(range(2, t))
L = []
if a.fibre is None:
    L.append("ring R=(0,y),(%s),wp(%s);" % (vars_, ",".join(map(str, wts))))
    L.append("minpoly = %d*y^2%+d*y%+d;" % (12*q*q, -12*q*(t+1), (t+1)*(3*t+2)))
    L.append("number d = %d*y-%d;" % (2*q, t+1))
else:
    L.append("ring R=0,(%s),wp(%s);" % (vars_, ",".join(map(str, wts))))
    L.append("number d = %d*(%s)-%d;" % (2*q, a.fibre, t+1))
zero_all = "".join(", q(%d), 0" % j for j in range(2, t))
zero_q_not2 = "".join(", q(%d), 0" % j for j in range(3, t))
L.append("poly f; poly r;")
for band, var, coef, rhs in piv:
    wt = 4*t+1-band
    L.append("f = %s;" % rhs)
    L.append('r = subst(f, b3, 0%s); print("PIVOT_B4AXIS var=%s wt=%d coef=" + string(r/b4^%d));' % (zero_all, var, wt, wt))
    if t >= 3 and wt % 2 == 0:
        L.append('r = subst(f, b3, 0, b4, 0%s); print("PIVOT_Q2AXIS var=%s wt=%d coef=" + string(r/q(2)^%d));' % (zero_q_not2, var, wt, wt//2))
    if wt % (t+1) == 0:
        L.append('r = subst(f, b4, 0%s); print("PIVOT_B3AXIS var=%s wt=%d coef=" + string(r/b3^%d));' % (zero_all, var, wt, wt//(t+1)))
for k in range(2*t):
    wt = 4*t+1-k
    L.append("f = %s;" % rows[k])
    L.append('r = subst(f, b3, 0%s); print("ROW_B4AXIS k=%d wt=%d coef=" + string(r/b4^%d));' % (zero_all, k, wt, wt))
    if t >= 3 and wt % 2 == 0:
        L.append('r = subst(f, b3, 0, b4, 0%s); print("ROW_Q2AXIS k=%d wt=%d coef=" + string(r/q(2)^%d));' % (zero_q_not2, k, wt, wt//2))
L.append("quit;")
print("\n".join(L))
