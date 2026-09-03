#!/usr/bin/env python3
"""Check E4 = 4e*phi_4 for general x (not only the x=1 slice), symbolically in t."""
import sympy as sp
t, x, y, r = sp.symbols('t x y r'); N = 7
def mul(a,b): return [sp.expand(sum(a[i]*b[k-i] for i in range(k+1))) for k in range(N)]
def pw(a,s):
    c=[sp.Integer(1)]+[None]*(N-1)
    for k in range(1,N):
        c[k]=sp.cancel(sp.expand(sum((s*j-(k-j))*a[j]*c[k-j] for j in range(1,k+1)))/k)
    return c
F=[sp.Integer(1),x,y]+[sp.Integer(0)]*(N-3); Fr=pw(F,r)
G=[sp.Integer(1),Fr[1],Fr[2],Fr[3]]+[sp.Integer(0)]*(N-4)
Phi=mul(F,pw(G,-1/r))
e,q=3*t+1,2*t+1; sub={r:sp.Rational(1,1)*e/q}
E4=sp.cancel(sp.expand(((e-3*q)*x*Fr[3]+(2*e-2*q)*y*Fr[2]).subs(sub)))
p4=sp.cancel(sp.together(Phi[4].subs(sub)))
print("  E4 - 4*e*phi_4 (general x,y,t) =", sp.simplify(sp.cancel(E4 - 4*e*p4)))
print("  phi_4 (general x) =", sp.factor(p4))
Hhat = 12*q**2*y**2 - 12*q*(t+1)*x**2*y + (t+1)*(3*t+2)*x**4
print("  phi_4 / Hhat =", sp.factor(sp.cancel(p4/Hhat)))
