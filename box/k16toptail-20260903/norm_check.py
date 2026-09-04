#!/usr/bin/env python3
"""Parse A_COEF lines (b3^2-coefficients of the top tail, r=0,1,2) from the
Singular outputs, reduce in A_t=Q[y]/(H_t), compare r=0 with -alpha_t (Opus
(4.5), sign: driver rows are the negatives of the frozen-record rows), and
print the norm Res_y(H_t, .) of every scalar coefficient (unit iff nonzero).
"""
import re, sys, sympy as sp
y, b4, q2 = sp.symbols('yy b4 q2_0')
def H(t):
    q = 2*t+1; return 12*q*q*y**2 - 12*q*(t+1)*y + (t+1)*(3*t+2)
def alpha(t):
    q = 2*t+1; d = 2*q*y-(t+1)
    return t*(3*t+1)*((27*t**3-30*t**2+t-2)*d + (6*t**3+13*t**2-3*t+2))/(12*q**2*(3*t-1)**2*(3*t+2))
def red(e, t):
    e = sp.together(sp.expand(e)); n, dn = sp.fraction(e)
    if dn.has(y): raise ValueError("denominator has y")
    return sp.expand(sp.rem(sp.Poly(sp.expand(n), y), sp.Poly(H(t), y)).as_expr()/dn)
def norm(u, t):
    u = red(u, t); n, dn = sp.fraction(sp.together(u))
    return sp.factor(sp.resultant(sp.Poly(H(t), y), sp.Poly(n, y)))/dn**2 if n != 0 else 0
for path in sys.argv[1:]:
    t = int(re.search(r'(?:toptail|stageA)_t(\d+)_', path).group(1))
    fibre = re.search(r'number yy=\(?([-\d/]+)\)?;', open(path.replace('.out','.sing')).read())
    txt = open(path).read()
    print("== t=%d %s" % (t, path))
    for m in re.finditer(r'A_COEF r=(\d+) : (.+)', txt):
        r = int(m.group(1)); expr = sp.sympify(m.group(2).replace('^','**'), locals={'yy': y, 'b4': b4, 'q2_0': q2})
        if fibre:  # split-exact: yy is a rational number already substituted
            print("  r=%d fibre y=%s : %s" % (r, fibre.group(1), expr)); continue
        P = sp.Poly(sp.expand(expr), b4, q2)
        for mon, co in P.terms():
            co = red(co, t)
            print("  r=%d monomial b4^%d q2^%d : coeff=%s  Res_y(H_t,.)=%s" % (r, mon[0], mon[1], co, norm(co, t)))
            if r == 0:
                print("     check coeff + alpha_t == 0 :", red(co + alpha(t), t) == 0)
