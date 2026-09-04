#!/usr/bin/env python3
"""Explicit ideal-membership certificate for the eliminant W_r.

Generic identity (verified symbolically in indeterminates, hence for every t,r):

  Q_0 = a0*b3^2 + b0*b3 + c0,   G = B*b3 + C
  W  := a0*C^2 - b0*B*C + c0*B^2
  IDENTITY:  W = B^2*Q_0 - G*( a0*G - 2*a0*C + b0*B ).

Consequences:  W in (Q_0,G);  and if a0 is a unit then V(Q_0,G) projects into
V(W).  Weight bookkeeping: wt W = 2*wt(G) = 2(2t+2+r) = 4t+4+2r.
"""
import sympy as sp
a0, b0, c0, B, C, b3 = sp.symbols('a0 b0 c0 B C b3')
Q0 = a0 * b3**2 + b0 * b3 + c0
G = B * b3 + C
W = a0 * C**2 - b0 * B * C + c0 * B**2
cert = sp.expand(B**2 * Q0 - G * (a0 * G - 2 * a0 * C + b0 * B))
print("W - [B^2 Q_0 - G(a0 G - 2 a0 C + b0 B)] =", sp.simplify(sp.expand(W - cert)))
print("sympy Res_b3(Q_0, G) =", sp.factor(sp.resultant(sp.Poly(Q0, b3), sp.Poly(G, b3))))
print("W                    =", sp.factor(W))
print("Res/W =", sp.cancel(sp.resultant(sp.Poly(Q0, b3), sp.Poly(G, b3)) / W))
print()
print("So sympy's Res_b3(quadratic,linear) equals W up to the recorded unit factor;")
print("the certificate above is the convention-free statement and is what is used.")
