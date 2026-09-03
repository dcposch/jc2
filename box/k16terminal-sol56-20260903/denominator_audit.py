#!/usr/bin/env python3
"""Exact symbolic audit of every unit class used by the terminal recurrence."""

from __future__ import annotations

import sympy as sp


t, j, n, d, y, aa, bb = sp.symbols("t j n d y aa bb")
q, e = 2*t+1, 3*t+1
H = 12*q*q*y*y-12*q*(t+1)*y+(t+1)*(3*t+2)
modulus = 3*d*d-(t+1)


def reduce_d(expression: sp.Expr) -> sp.Expr:
    field = sp.QQ.frac_field(t, j, n, aa, bb)
    polynomial = sp.Poly(modulus, d, domain=field)
    numerator, denominator = sp.cancel(expression).as_numer_denom()
    nr = sp.Poly(numerator, d, domain=field).rem(polynomial)
    dr = sp.Poly(denominator, d, domain=field).rem(polynomial)
    return sp.factor((nr*sp.invert(dr, polynomial)).rem(polynomial).as_expr())


assert sp.factor(H.subs(y, (d+t+1)/(2*q))) == modulus
assert sp.factor(sp.resultant(H, aa*(2*q*y-(t+1))+bb, y)
                 - 4*q*q*(3*bb*bb-aa*aa*(t+1))) == 0

y_d = (d+t+1)/(2*q)
g = e*t*(3*d+2*(t+1))/(6*q**3)
y_inverse = 6*q*((t+1)-d)/((t+1)*(3*t+2))
g_inverse = 6*q**3*(2*(t+1)-3*d)/(t*(t+1)*e*(4*t+1))
linear_inverse = 3*(bb-aa*d)/(3*bb*bb-aa*aa*(t+1))
assert reduce_d(y_d*y_inverse-1) == 0
assert reduce_d(g*g_inverse-1) == 0
assert reduce_d((aa*d+bb)*linear_inverse-1) == 0

A_C = (9*j*j*t+18*j*j-54*j*t*t-81*j*t-26*j
       +72*t**3+144*t*t+88*t+16)
B_C = (-9*j*j*t-10*j*j+24*j*t*t+33*j*t+10*j
       -12*t**3-20*t*t-8*t)
F_C = sp.factor(-(3*B_C**2-A_C**2*(t+1))/(3*t+2)**3)
F_C_positive = (
    3*n**4+24*n**3*t+42*n**3+66*n**2*t**2+146*n**2*t+119*n**2
    +72*n*t**3+238*n*t**2+234*n*t+104*n
    +27*t**4+134*t**3+223*t**2+136*t+32
)
assert sp.expand(F_C.subs(j, t-n)-F_C_positive) == 0

A_Q = 12*t*t+16*t+4-j*(3*t+4)
B_Q = 2*(t+1)*(j-t)
F_Q = sp.factor(-(3*B_Q**2-A_Q**2*(t+1))/((t+1)*(3*t+2)**2))
F_Q_positive = n*n+4*n*t+6*n+4*t*t-3
assert sp.expand(F_Q.subs(j, q-n)-F_Q_positive) == 0

p_b2 = g*d/(2*y_d)
p_b2_inverse = 6*q*q*(3*q*d-(t+1))/(t*(t+1)*e*(4*t+1))
assert reduce_d(p_b2*p_b2_inverse-1) == 0

p_C = 3*t*e*(A_C*d+B_C)/((t+1)*(3*t+2)**3*(4*t-2*j+1))
p_Q = -3*t*e*(q-j)*(A_Q*d+B_Q)/(
    (t+1)*q*(3*t+2)**2*(4*t-2*j+1)
)
actual_g_resultant = sp.factor(sp.resultant(H, g.subs(d, 2*q*y-(t+1)), y))
actual_C_resultant = sp.factor(sp.resultant(H, p_C.subs(d, 2*q*y-(t+1)), y))
actual_Q_resultant = sp.factor(sp.resultant(H, p_Q.subs(d, 2*q*y-(t+1)), y))
p_b2_polynomial = t*e*(3*q*d+t+1)/(6*q**2*(3*t+2))
assert reduce_d(p_b2-p_b2_polynomial) == 0
actual_b2_resultant = sp.factor(
    sp.resultant(H, p_b2_polynomial.subs(d, 2*q*y-(t+1)), y)
)
assert sp.factor(
    actual_g_resultant-t**2*e**2*(t+1)*(4*t+1)/(3*q**4)
) == 0
assert sp.factor(
    actual_C_resultant
    + 36*q**2*t**2*e**2*F_C/
      ((t+1)**2*(3*t+2)**3*(4*t-2*j+1)**2)
) == 0
assert sp.factor(
    actual_Q_resultant
    + 36*t**2*e**2*(q-j)**2*F_Q/
      ((t+1)*(3*t+2)**2*(4*t-2*j+1)**2)
) == 0
assert sp.factor(
    actual_b2_resultant
    + t**2*e**2*(t+1)*(4*t+1)/(3*q**2*(3*t+2))
) == 0

A_b = 27*t**3-30*t**2+t-2
B_b = 6*t**3+13*t**2-3*t+2
axis_resultant = sp.factor(
    sp.resultant(H, A_b*(2*q*y-(t+1))+B_b, y)
)
axis_expected = sp.factor(
    -4*q**2*(t-2)*(3*t-1)**2*(3*t+2)*(27*t**3+17*t**2+t+2)
)
assert sp.factor(axis_resultant-axis_expected) == 0

print("DENOMINATOR_AUDIT_PASS")
print("H_IN_D=", modulus)
print("GENERAL_RESULTANT=", sp.factor(4*q*q*(3*bb*bb-aa*aa*(t+1))))
print("Y_RESULTANT=", sp.factor(sp.resultant(H, y, y)))
print("G_PRIMITIVE_RESULTANT=", sp.factor(
    sp.resultant(H, 3*(2*q*y-(t+1))+2*(t+1), y)))
print("C_PRIMITIVE_RESULTANT=", sp.factor(-4*q*q*(3*t+2)**3*F_C))
print("C_POSITIVE_FORM=", F_C_positive)
print("Q_PRIMITIVE_RESULTANT=", sp.factor(-4*q*q*(t+1)*(3*t+2)**2*F_Q))
print("Q_POSITIVE_FORM=", F_Q_positive)
print("B2_PRIMITIVE_RESULTANT=", sp.factor(-12*q*q*(t+1)*(3*t+2)*(4*t+1)))
print("G_ACTUAL_RESULTANT=", actual_g_resultant)
print("C_ACTUAL_RESULTANT=", actual_C_resultant)
print("Q_ACTUAL_RESULTANT=", actual_Q_resultant)
print("B2_ACTUAL_RESULTANT=", actual_b2_resultant)
print("B3_AXIS_PRIMITIVE_RESULTANT=", axis_resultant)
print("Y_INVERSE=", y_inverse)
print("G_INVERSE=", g_inverse)
print("B2_PIVOT_INVERSE=", p_b2_inverse)
