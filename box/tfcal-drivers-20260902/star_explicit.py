#!/usr/bin/env python3
"""Explicit solutions of (BOTTOM) d Q P' - e Q' P = gamma != 0 at (d,e)=(2,3),
   V = 1 and V = 2, with the zeta_e-equivariant ansatz suggested by the dessin."""
import sympy as sp
pi = sp.symbols('pi')
def test(V,P,Q,d=2,e=3):
    W = sp.expand(d*Q*sp.diff(P,pi) - e*sp.diff(Q,pi)*P)
    const = (sp.Poly(W,pi).degree() <= 0)
    dp = sp.simplify(sp.discriminant(sp.Poly(P,pi),pi))
    dq = sp.simplify(sp.discriminant(sp.Poly(Q,pi),pi))
    res = sp.simplify(sp.resultant(P,Q,pi))
    print("  V=%d  deg P=%d deg Q=%d   d Q P' - e Q' P = %s" %
          (V, sp.degree(P,pi), sp.degree(Q,pi), sp.simplify(W)))
    print("       constant=%s nonzero=%s  simple(P)=%s simple(Q)=%s coprime=%s"
          % (const, sp.simplify(W)!=0, dp!=0, dq!=0, res!=0))
    assert const and sp.simplify(W)!=0 and dp!=0 and dq!=0 and res!=0
    # dessin data
    a1=sp.degree(P,pi); b1=sp.degree(Q,pi)
    print("       dessin: deg phi = %d, over 0: %d pts of index %d, over inf: %d pts of index %d,"
          % (d*e*V, b1, e, a1, d))
    print("               over 1: one point (pi=infty) of index %d + %d simple"
          % ((d+e)*V-1, d*e*V-(d+e)*V+1))
    num = sp.expand(Q**e - P**d)
    print("       deg(Q^e - P^d) = %d  (predicted %d)" % (sp.degree(num,pi), d*e*V-(d+e)*V+1))
    assert sp.degree(num,pi) == d*e*V-(d+e)*V+1
print("== explicit (BOTTOM) solutions at (d,e) = (2,3) ==")
test(1, pi**3+3*pi, pi**2+2)
test(2, pi**6+3*pi**3+sp.Rational(3,2), pi**4+2*pi)
print("  ALL OK")
