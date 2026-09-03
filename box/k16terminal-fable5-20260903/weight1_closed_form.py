#!/usr/bin/env python3
"""Weight-1 linearization of the w-picture (2.1): closed form of the b4-axis value of the
first pivot, C_1 = gamma_{t,1} b4, and of the band-4t diagonal (control: = p_C(t,1)).
Exact in Q(t)[d]/(3d^2-(t+1)).  Then specialised and compared with the exact rows."""
import sympy as sp
t, d, C1, b4 = sp.symbols("t d C1 b4")
q, e = 2*t+1, 3*t+1
y = (d+t+1)/(2*q); g1 = sp.Integer(1)*e/q; g2 = e*(d+q)/(2*q**2); g = e*t*(3*d+2*(t+1))/(6*q**3)
field = sp.QQ.frac_field(t, C1, b4)
mod = sp.Poly(3*d*d-(t+1), d, domain=field)
def red(x):
    n, dn = sp.cancel(sp.together(x)).as_numer_denom()
    n = sp.Poly(sp.expand(n), d, domain=field).rem(mod); dn = sp.Poly(sp.expand(dn), d, domain=field).rem(mod)
    return sp.factor((n*sp.invert(dn, mod)).rem(mod).as_expr())
# (D3) at w^1
T1 = red(g*((3*t-1)*C1 - 3*(t-1)*b4)/(2*y*(t-1)))
# (D2) at w^1
RHS1 = (-b4*g2 + C1*g2 + T1) - ((t-1)*T1 + t*g2*(C1-2*b4)) + 2*(g2*(t-1)*(C1-b4) + t*(T1-b4*g2))
S1 = red((RHS1 + 4*t*b4*g1*y)/(y*(4*t-1)))
# (D1) at w^1
rhs = -(2*t*(S1-b4*g1) + (2*t+1)*g1*(C1-2*b4)) + (t*g1*(C1-2*b4) + (t+1)*(S1-b4*g1)) + 2*q*(T1-b4*g2)
v1 = red(b4*e + rhs/(2*y))
# (D0) at w^1
Delta1 = red(v1 + (C1-2*b4)*e - q*(S1-b4*g1))
num, den = sp.together(Delta1).as_numer_denom()
P = sp.Poly(sp.expand(num), C1, b4)
pC = red(P.coeff_monomial(C1)/den); pi1 = red(P.coeff_monomial(b4)/den)
# Sol closed form p_C(t,1)
j = 1
A_c = (9*j*j*t+18*j*j-54*j*t*t-81*j*t-26*j+72*t**3+144*t*t+88*t+16)
B_c = (-9*j*j*t-10*j*j+24*j*t*t+33*j*t+10*j-12*t**3-20*t*t-8*t)
pC_sol = 3*t*e*(A_c*d+B_c)/((t+1)*(3*t+2)**3*(4*t-2*j+1))
print("band-4t diagonal / p_C(t,1) =", red(pC/pC_sol))
gamma = red(-pi1/pC)
print("gamma_{t,1} (C_1 = gamma b4 on the b4-axis) =", gamma)
n_, d_ = sp.together(gamma).as_numer_denom()
print("  denominator factored:", sp.factor(d_))
F_c = sp.factor(-(3*B_c**2-A_c**2*(t+1))/(3*t+2)**3)
print("  F_C(t,1) =", F_c)
for tv in (3,4,5,6,7):
    gv = gamma.subs(t, tv); yv = sp.Symbol("y")
    gv = sp.simplify(gv.subs(d, 2*(2*tv+1)*yv-(tv+1)))
    print("t=%d gamma=%s" % (tv, sp.expand(gv)))
