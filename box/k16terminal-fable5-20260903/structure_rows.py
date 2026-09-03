#!/usr/bin/env python3
"""Emit Singular structural extraction on terminal rows (weighted, exact).
Prints per row: weight check, b3-degree, coefficient of the pure b4 power (b4-axis),
coefficient of b3^2 in T_{2t-1} and b3^3 in T_{t-2} (axis controls vs alpha_t, beta_t),
and the rows restricted to b4=0 (their term counts and b3-degree)."""
import argparse, re
ap = argparse.ArgumentParser(); ap.add_argument("t", type=int); ap.add_argument("rows"); ap.add_argument("--fibre", default=None)
a = ap.parse_args(); t = a.t; q = 2*t+1
rows = {}
for line in open(a.rows):
    m = re.match(r"T(\d+) = (.*);$", line.strip())
    if m: rows[int(m.group(1))] = m.group(2)
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
L.append("intvec W = %s;" % ",".join(map(str, wts)))
for k in range(2*t):
    L.append("poly T%d = %s;" % (k, rows[k]))
L.append("poly tk; poly ax; int k; int dg;")
for k in range(2*t):
    L.append("tk = T%d;" % k)
    L.append('print("ROW k=%d terms=" + string(size(tk)) + " wdeg=" + string(deg(tk, W)) + " b3deg=" + string(deg(tk, intvec(1,0%s))) + " b4deg=" + string(deg(tk, intvec(0,1%s))));' % (k, ",0"*(t-2), ",0"*(t-2)))
    L.append('ax = subst(tk, b3, 0%s); print("  B4AXIS k=%d coef=" + string(ax/b4^%d));' % ("".join(", q(%d), 0" % j for j in range(2, t)), k, 4*t+1-k))
    L.append('ax = subst(tk, b4, 0); print("  B4ZERO k=%d terms=" + string(size(ax)) + " b3deg=" + string(deg(ax, intvec(1,0%s))));' % (k, ",0"*(t-2)))
# alpha, beta controls
L.append('poly a2 = subst(T%d, b4, 0%s); print("ALPHA_DATA=" + string(a2)); ' % (2*t-1, "".join(", q(%d), 0" % j for j in range(2, t))))
L.append('number alpha = -%d*(3*%d+1)*(27*d*%d^3-30*d*%d^2+d*%d-2*d+6*%d^3+13*%d^2-3*%d+2)/(12*(2*%d+1)^2*(3*%d-1)^2*(3*%d+2));' % ((t,)*11))
L.append('print("ALPHA_CHECK=" + string(a2 - alpha*b3^2));')
if t >= 3:
    L.append('poly b3c = subst(T%d, b4, 0%s); print("BETA_DATA=" + string(b3c));' % (t-2, "".join(", q(%d), 0" % j for j in range(2, t))))
    L.append('number beta = %d*(%d-2)*(3*%d+1)*(6*d*%d-%d-1)/(72*(2*%d+1)^3*(3*%d-1));' % ((t,)*7))
    L.append('print("BETA_CHECK=" + string(b3c - beta*b3^3));')
# linear coefficients at P1: coefficient of b3*b4^(3t-k) and q_j*b4^(4t+1-k-j)
for k in range(2*t):
    L.append('tk = T%d; print("  LIN k=%d mu(b3)=" + string(coeffs(subst(subst(tk,b4,1)%s, b3, b3), b3)[2,1]));' % (k, k, "".join(", q(%d), 0" % j for j in range(2, t))) if False else 'tk = subst(T%d, b4, 1); print("  LIN k=%d dTdb3|P1=" + string(subst(diff(tk, b3), b3, 0%s)));' % (k, k, "".join(", q(%d), 0" % j for j in range(2, t))))
    for j in range(2, t):
        L.append('print("  LIN k=%d dTdq%d|P1=" + string(subst(diff(tk, q(%d)), b3, 0%s)));' % (k, j, j, "".join(", q(%d), 0" % jj for jj in range(2, t))))
L.append("quit;")
print("\n".join(L))
