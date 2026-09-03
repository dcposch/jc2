#!/usr/bin/env python3
"""SOURCE CONTROL: reproduce Moh p.209's explicit t=1 formula from the uniform bridge.

Moh (p.209, frozen PDF p.70), after the gauges (f,g)->(f-(3/4)a3, g-a1 f-a4):
   g = h^4 + (4/3)(B2 h^2 + B3 h) + (2/9)(B2^2 + 2*gam) - (4/81)*del + a2 h^2
   with B2 B3 = gam*h + gam*,  B2^3 = del*h^2 + del*,
        deg_y gam* < deg h = 4,  deg_y del* < deg h^2 = 8.
Here (B2,B3) = Moh's (beta_2,beta_3); 'gam','del' are his gamma,delta (NOT our x).
"""
import sympy as sp
g, p = sp.symbols('g p')
b1, b2, b3, b4, a2 = sp.symbols('b1 b2 b3 b4 a2')
c3, c4, c8, c9, c10 = sp.symbols('c3 c4 c8 c9 c10')
h = sp.expand(p**4 + (b1-g)*p**3 + b2*p**2 + b3*p + b4)
B = sp.expand(p*(p-g) + b1*p + b2); A = sp.expand(p*B + b3)
B2 = c3*A + c4                      # Moh (3)
B3 = c8*A + c9*B + c10              # Moh (4)
H = sp.Poly(h, p); H2 = sp.Poly(sp.expand(h**2), p)
gam = sp.div(sp.Poly(sp.expand(B2*B3), p), H)[0].as_expr()
del_ = sp.div(sp.Poly(sp.expand(B2**3), p), H2)[0].as_expr()
gstar = sp.div(sp.Poly(sp.expand(B2*B3), p), H)[1]
dstar = sp.div(sp.Poly(sp.expand(B2**3), p), H2)[1]
print("  deg_y gam* =", gstar.degree(), "(< 4 required);  deg_y del* =", dstar.degree(), "(< 8 required)")
moh = sp.expand(h**4 + sp.Rational(4,3)*(B2*h**2 + B3*h)
                + sp.Rational(2,9)*(B2**2 + 2*gam) - sp.Rational(4,81)*del_ + a2*h**2)

# --- uniform bridge construction, t=1: e=4, q=3, a1=a3=a4=0 ---
import importlib.util, sys
sys.argv = ['x', '1']
spec = importlib.util.spec_from_file_location("bc", "box/k16spine-opus-20260903/bridge_chart.py")
bc = importlib.util.module_from_spec(spec); spec.loader.exec_module(bc)
sub = {sp.Symbol('q2_1'): c4, sp.Symbol('q2_A'): c3,
       sp.Symbol('q3_1'): c10, sp.Symbol('q3_A'): c8, sp.Symbol('q3_B'): c9}
mine = sp.expand(bc.Pbr.subs(sub))
d = sp.expand(mine - moh)
print("  uniform-bridge P  ==  Moh p.209 formula :", d == 0)
if d != 0: print("   residual:", sp.simplify(d))
