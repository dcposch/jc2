#!/usr/bin/env python3
"""N = deg_x Res_y(P-c1, Q-c2) for generic (c1,c2): control for CONTACT-SPLIT."""
from sympy import symbols, resultant, Poly, degree, expand, Rational, gcd as sgcd
x,y = symbols('x y')
rows = [
 ("(x, y+x^3)", x, y+x**3, 1),
 ("(x, xy)",    x, x*y,    1),
 ("(x, y^2)",   x, y**2,   2),
 ("(x, xy^2)",  x, x*y**2, 2),
 ("(x, x^2y^2)",x, x**2*y**2, 2),
 ("(x^3,y^2)",  x**3, y**2, 6),
 ("psi_2 o (x,xy^2)", x+(x*y**2)**2, x*y**2, 2),
 ("psi_3 o (x,xy^3)", x+(x*y**3)**3, x*y**3, 3),
 ("(y, y^2+x)", y, y**2+x, 1),
]
print(f"{'map':22} {'deg_x Res':>10} {'#distinct':>10} {'N(pub)':>7}")
for (nm,P,Q,Npub) in rows:
    c1,c2 = Rational(7,3), Rational(-5,2)
    R = expand(resultant(Poly(expand(P-c1),y), Poly(expand(Q-c2),y), y).as_expr())
    if R == 0: print(f"{nm:22} {'RES=0':>10}"); continue
    p = Poly(R, x)
    sf = p.quo(sgcd(p, p.diff(x)))
    print(f"{nm:22} {int(degree(R,x)):10d} {int(degree(sf.as_expr(),x)):10d} {Npub:7d}")
# CONTACT-SPLIT control: two-slope leading form, l(f)=H^d, l(g)=H^e
H = (y-x)*(y-2*x)
for (d,e) in [(2,3),(2,5),(3,4)]:
    f = expand(H**d + y); g = expand(H**e + x)
    c1,c2 = Rational(7,3), Rational(-5,2)
    R = expand(resultant(Poly(expand(f-c1),y), Poly(expand(g-c2),y), y).as_expr())
    N = int(degree(R,x))
    print(f"  H=(y-x)(y-2x), d={d},e={e}: m={2*d} n={2*e} mn={4*d*e}  N=deg_x Res={N}"
          f"   2deuv={2*d*e*1*1}   sum_same ord = 2deuv-N = {2*d*e-N}")
