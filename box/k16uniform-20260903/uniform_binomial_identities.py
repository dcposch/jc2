#!/usr/bin/env python3
"""Exact Q(t) checks for the K=16-ray normalizer identities.

The high-side constant-pivot recurrence is the coefficient recurrence for
G(U)=F(U)^(e/q), F(U)=1+x*U+y*U^2.  This script checks the first four
coefficients, the closed H_t and c_t formulas, the discriminant, and the two
resultants needed to see that c_t is a unit after x=1.
"""

import sympy as sp


t, U, x, y = sp.symbols("t U x y")
q = 2*t + 1
e = 3*t + 1
r = e/q

C2 = r*(r-1)/2
C3 = r*(r-1)*(r-2)/6
C4 = r*(r-1)*(r-2)*(r-3)/24
g1 = r*x
g2 = r*y + C2*x**2
g3 = 2*C2*x*y + C3*x**3
g4 = C2*y**2 + 3*C3*x**2*y + C4*x**4

Hhom = 12*q**2*y**2 - 12*q*(t+1)*x**2*y + (t+1)*(3*t+2)*x**4
cimage = t*e*x*y*((t+1)*x**2 - 6*q*y)/(6*q**3)

checks = {
    "g1": sp.factor(g1 - e*x/q),
    "g2": sp.factor(g2 - (e*y/q + e*t*x**2/(2*q**2))),
    "g3": sp.factor(g3 - (-e*t*(t+1)*x**3/(6*q**3)
                              + e*t*x*y/q**2)),
    "H_from_g4": sp.factor(g4 - C2*Hhom/(12*q**2)),
    "c_from_g3": sp.factor(cimage + y*g3),
    "band_4t_plus_1_E1": sp.factor(q*g1-e*x),
    "band_3t_plus_1_E2": sp.factor(
        2*q*g2-(e-q)*x*g1-2*e*y),
    "band_2t_E3": sp.factor(
        3*q*g3-(e-2*q)*x*g2-(2*e-q)*y*g1),
}
E4 = sp.factor((e-3*q)*x*g3+(2*e-2*q)*y*g2)

H = sp.Poly(Hhom.subs(x, 1), y, domain=sp.QQ.frac_field(t))
disc = sp.factor(sp.discriminant(H.as_expr(), y))
H0 = sp.factor(H.as_expr().subs(y, 0))
root_linear = (t+1)/(6*q)
Hatroot = sp.factor(H.as_expr().subs(y, root_linear))
res_y = sp.factor(sp.resultant(H.as_expr(), y, y))
linear = (t+1)-6*q*y
res_linear = sp.factor(sp.resultant(H.as_expr(), linear, y))

if any(value != 0 for value in checks.values()):
    raise AssertionError(checks)
if disc != 48*q**2*(t+1):
    raise AssertionError(disc)
if H0 != (t+1)*(3*t+2):
    raise AssertionError(H0)
if Hatroot != (t+1)*(4*t+1)/3:
    raise AssertionError(Hatroot)
if sp.factor(E4 - t*e*Hhom/(6*q**3)) != 0:
    raise AssertionError(E4)

print("ALL_BINOMIAL_IDENTITIES_PASS")
print("q=", q, "e=", e, "r=", r)
print("g1=", sp.factor(g1))
print("g2=", sp.factor(g2))
print("g3=", sp.factor(g3))
print("Hhom=", Hhom)
print("c=", sp.factor(cimage))
print("band_t_E4=", E4)
print("disc_y(Hhom)=", disc)
print("Hhom(0)=", H0)
print("Hhom((t+1)/(6q))=", Hatroot)
print("Res_y(Hhom,y)=", res_y)
print("Res_y(Hhom,(t+1)-6q*y)=", res_linear)
for value in range(1, 5):
    specialized = sp.Poly(H.as_expr().subs(t, value), y, domain=sp.QQ)
    _content, primitive = specialized.primitive()
    print("t=%d Hprimitive=%s disc=%s factor=%s c=%s" % (
        value, primitive.as_expr(), sp.discriminant(primitive.as_expr(), y),
        sp.factor(primitive.as_expr()), sp.factor(cimage.subs({t: value, x: 1}))))
