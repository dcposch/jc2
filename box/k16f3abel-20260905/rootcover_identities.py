#!/usr/bin/env python3
"""Universal characteristic-zero checks for the K16 ordered-root contacts.

Run in the foreground with:
timeout 60s stdbuf -oL python3 box/k16f3abel-20260905/rootcover_identities.py
All identities are over Q(x,y,b,B,eta,C,P,Pprime). No numeric promotion.
"""
import sympy as s

x, y, b, B, eta, C, P, Pprime, K = s.symbols(
    "x y b B eta C P Pprime K"
)
r = b**2 / 4
A = 3*x**3*C**2/(4*y**2)
D = 3*b*x*C/(2*y)
W = (P+r)/x
Wprime = Pprime/x-(P+r)/x**2
k = x*x*C-y*b
F = 2*(x*W-r)*Wprime-(
    W*W+(B-2*A+D)*W+A*(A-D)/3-B*(A-D)
    -b*eta*k/(2*y)-B*eta*x+(2*r*A-4*r*(B+W))/x
)
H = 2*x*Pprime-3*P-B*x+3*K*(K+y*b)/(2*y**2)
R = (3*K**2*(K*(K+2*y*b)-4*B*y*y*x)/(16*y**4)
     -eta*x*x*(b*K/(2*y)+B*x))
assert s.cancel(x*x*F-(P*H-R).subs(K,k)) == 0
print("POLYNOMIAL_PH_IDENTITY_PASS", flush=True)

assert s.expand(R).subs(K,0) == -B*eta*x**3
E0 = 2*x*P*Pprime-3*P**2-B*x*P+B*eta*x**3
target = E0+b*K*(3*P+eta*x*x)/(2*y)
assert s.Poly(s.cancel(target-(P*H-R)),K).rem(s.Poly(K*K,K)).is_zero
print("K_SQUARED_CONTACT_PASS", flush=True)

Qc = 16*B*eta*x**3-8*b*b*eta*x*x+12*B*b*b*x+3*b**4
Q1 = 3*b*b+12*B*x-4*eta*x*x
Rc = s.expand(R.subs(K,k))
assert s.expand(Rc.subs(C,0)+Qc/16) == 0
assert s.Poly(s.expand(Rc+Qc/16-b*x*x*Q1*C/(8*y)),C).rem(s.Poly(C*C,C)).is_zero
print("C_CUBIC_AND_SQUARED_CONTACT_PASS", flush=True)

disc_expected = 768*eta*b**6*(-144*B**4-177*B*B*eta*b*b+8*eta*eta*b**4)
assert s.expand(s.discriminant(Qc,x)-disc_expected) == 0
print("C_EXCEPTION_CUBIC_DISCRIMINANT_PASS", flush=True)

# A repeated-root exact control for the resultant multiplicativity argument:
# K=(x^2-1)^2, y=1, b=-1. This tests nonreduced K; no F3 solution is asserted.
kr = (x*x-1)**2
rr = R.subs({K:kr,y:1,b:-1,B:2,eta:3})
assert s.expand(s.rem(rr,kr,x)+6*x**3) == 0
assert s.resultant(kr,rr,x) == -6**4*(-1)**3
print("REPEATED_K_RESULTANT_CONTROL_PASS", flush=True)

# A repeated-root C control for the norm identity; again this only tests
# the universal R congruence, not a normalized F3 solution.
cr = (x-1)**3*(x+2)**2
rcr = Rc.subs({C:cr,y:2,b:3,B:5,eta:7})
qcr = Qc.subs({b:3,B:5,eta:7})
assert s.rem(s.expand(rcr+qcr/16),cr,x) == 0
assert s.resultant(cr,rcr,x) == (-s.Rational(1,16))**5*s.resultant(cr,qcr,x)
print("REPEATED_C_RESULTANT_CONTROL_PASS", flush=True)

# Exceptional failure of J to be a unit in k[x]/(P): elimination is exact.
J = b*K/(2*y)+B*x
Q = K*(K+2*y*b)-4*B*y*y*x
assert s.cancel(Q.subs(x,-b*K/(2*y*B))-K*(K+4*y*b)) == 0
print("J_EXCEPTION_ELIMINATION_PASS", flush=True)
print("ALL_ROOTCOVER_IDENTITIES_PASS", flush=True)
