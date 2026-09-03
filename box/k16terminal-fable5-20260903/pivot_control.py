#!/usr/bin/env python3
"""Control: pivot coefficients printed by laurent_spine.py vs Sol closed forms (5.10),(5.13),(5.15)
and the b1/B0 pivots (coefficients yg and q/y). Exact in A_t (or on a rational fibre)."""
import re, sys, sympy as sp
t = int(sys.argv[1]); path = sys.argv[2]; fibre = sys.argv[3] if len(sys.argv) > 3 else None
q, e = 2*t+1, 3*t+1
y = sp.Symbol("y")
H = sp.Poly(12*q*q*y**2 - 12*q*(t+1)*y + (t+1)*(3*t+2), y, domain=sp.QQ)
def red(expr):
    expr = sp.sympify(expr, locals={"y": y})
    if fibre is not None:
        return sp.nsimplify(expr.subs(y, sp.Rational(fibre)))
    num, den = sp.together(expr).as_numer_denom()
    n = sp.Poly(sp.expand(num), y, domain=sp.QQ).rem(H); dd = sp.Poly(sp.expand(den), y, domain=sp.QQ).rem(H)
    return (n*sp.invert(dd, H)).rem(H).as_expr()
d = 2*q*y-(t+1)
g3 = sp.Rational(e*t, q*q)*y - sp.Rational(e*t*(t+1), 6*q**3)
def pC(j):
    A = 9*j*j*t+18*j*j-54*j*t*t-81*j*t-26*j+72*t**3+144*t*t+88*t+16
    B = -9*j*j*t-10*j*j+24*j*t*t+33*j*t+10*j-12*t**3-20*t*t-8*t
    return sp.Rational(3*t*e, (t+1)*(3*t+2)**3*(4*t-2*j+1))*(A*d+B)
def pQ(j):
    A = 12*t*t+16*t+4-j*(3*t+4); B = 2*(t+1)*(j-t)
    return -sp.Rational(3*t*e*(q-j), (t+1)*q*(3*t+2)**2*(4*t-2*j+1))*(A*d+B)
pb2 = g3*d/(2*y)
ok = True
for line in open(path):
    m = re.match(r"PIVOT (\d+) (\S+) (\S+) (.*);$", line.strip())
    if not m: 
        m2 = re.match(r"B(1|0)COEF=(.*)$", line.strip())
        continue
    band, var, coef = int(m.group(1)), m.group(2), m.group(3)
    j = 4*t+1-band
    if var.startswith("C("): formula = pC(j)
    elif var.startswith("q("): formula = pQ(j)
    else: formula = pb2
    ratio = red(red(coef)/red(formula))
    print("t=%d band=%d var=%s weight=%d ratio_to_closed_form=%s" % (t, band, var, j, ratio))
    ok = ok and (ratio == 1)
print("PIVOT_CONTROL_t%d=%s" % (t, "PASS" if ok else "FAIL"))
