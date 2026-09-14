#!/usr/bin/env python3
"""Cross-check the independently recomputed t=3 tail scalars against the charged
fable5 table (k16-toptail-quadratics-fable5-20260903.md Sec.3(b)):
      Res_y(H_3, mu_t)  = 159028943/148574272        (mu_t = [b3^2 b4] T_{3,4})
      Res_y(H_3, mu''_t)= -11399375/34603212         (mu''_t = [b3^2 q_{2,0}] T_{3,3})
      Res_y(H_3, mu'_t) = -4250137195970063/4803319854964400   ([b3^2 b4^2] T_{3,3})
Sign convention: the fable driver's rows are the negatives of ours; Res of a
linear class is quadratic, so the tabulated norms are convention-free.
"""
import json, sympy as sp
y = sp.Symbol('y'); b4, u2, b3 = sp.symbols('b4 u2 b3')
t = 3; q = 2*t+1
H = 12*q**2*y**2 - 12*q*(t+1)*y + (t+1)*(3*t+2)
Hp = sp.Poly(H, y)

def norm(s):
    s = sp.together(sp.simplify(s))
    return sp.simplify(sp.resultant(sp.Poly(sp.numer(s), y), Hp) / sp.denom(s)**2)

D = json.load(open('/home/ubuntu/jc2/box/k16hsop-20260903/tail_t3_rows.json'))
a = {int(k): sp.sympify(sp.srepr(sp.S(1)) and v) for k, v in D['a'].items()}
a = {int(k): sp.sympify(v) for k, v in D['a'].items()}
a1 = sp.expand(a[1]); a2 = sp.expand(a[2])
mu   = sp.simplify(sp.Poly(a1, b4).nth(1))
mu2  = sp.simplify(sp.Poly(a2, b4, u2).coeff_monomial(b4**2))
mu3  = sp.simplify(sp.Poly(a2, b4, u2).coeff_monomial(u2))
tab = {'mu_t (b3^2 b4)':        (mu,  sp.Rational(159028943, 148574272)),
       "mu'_t (b3^2 b4^2)":     (mu2, sp.Rational(-4250137195970063, 4803319854964400)),
       "mu''_t (b3^2 q_(2,0))": (mu3, sp.Rational(-11399375, 34603212))}
print("t=3 cross-check against charged fable5 table:")
for name, (val, ref) in tab.items():
    n = norm(val)
    print(f"  {name:24s}  Res_y(H_3,.) = {n}")
    print(f"  {'':24s}  charged      = {ref}      MATCH={sp.simplify(n-ref)==0}")
