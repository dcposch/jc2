#!/usr/bin/env python3
"""A3: extreme coefficients of the terminal rows, as candidates for uniform-in-t forms.

Prints, for each t and each band k:
  * lead_b3      = coefficient of b3^(deg_b3) in T_{t,k}|_{b4=0}   (a form in the q's)
  * c_b3top      = coefficient of b3^(max) alone when that coefficient is a scalar
  * b4-pure      = coefficient of b4^(4t+1-k) in T_{t,k}          (a scalar in A_t)
  * b3^a b4^m    = coefficient of b3^a * b4^(wt-a(t+1)) for a=1,2,3 (scalars in A_t)
Every scalar is printed as an integral primitive linear form in y with its
resultant against H_t, so unit-ness is decidable by (1.1).
"""
import sys, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16terminal-opus-20260903")
from tf_load import load

def prim(expr, y, H):
    """Primitive integral associate of a scalar in A_t, plus Res_y(H, .)."""
    e = sp.expand(expr)
    if e == 0:
        return "0", 0
    n, d = sp.fraction(sp.cancel(sp.together(e)))
    p = sp.Poly(sp.expand(n), y)
    cont = sp.gcd(list(p.all_coeffs()))
    p = sp.Poly(sp.expand(n/cont), y)
    r = sp.resultant(sp.Poly(H, y), p, y)
    return sp.factor(p.as_expr()), sp.factor(r)

for t in [int(a) for a in sys.argv[1:]]:
    D = load(t); b3, b4, y, H = D["b3"], D["b4"], D["y"], D["H"]
    qv = D["qv"]
    print("=== t=%d ===" % t)
    for k in sorted(D["rows"]):
        r = sp.expand(D["rows"][k]); w = 4*t+1-k
        line = ["k=%2d w=%2d |" % (k, w)]
        for a in (3, 2, 1):
            m = w - a*(t+1)
            if m < 0:
                continue
            co = sp.expand(r.coeff(b3, a))
            for v in qv:
                co = co.subs(v, 0)
            co = sp.expand(co).coeff(b4, m) if m > 0 else sp.expand(co.subs(b4, 0))
            f, res = prim(co, y, H)
            line.append("[b3^%d b4^%d]=%s (Res=%s)" % (a, m, f, res))
        f, res = prim(sp.expand(r.subs(b3, 0).subs({v: 0 for v in qv})).coeff(b4, w) if w > 0 else 0, y, H)
        line.append("[b4^%d]=%s (Res=%s)" % (w, f, res))
        print("  " + "  ".join(line))
