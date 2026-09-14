#!/usr/bin/env python3
"""Literal F3 identity check and quartic critical-value discriminants."""
import sympy as s
x,y,b,B,eta,C,W,Wp=s.symbols('x y b B eta C W Wp')
r=b*b/4
A=3*x**3*C**2/(4*y**2)
D=3*b*x*C/(2*y)
K=x*x*C-y*b
Z=x*W-r
Zp=W+x*Wp
rhs=W**2+(B-2*A+D)*W+A*(A-D)/3-B*(A-D)-b*eta*K/(2*y)-B*eta*x+(2*r*A-4*r*(B+W))/x
E=2*(x*W-r)*Wp-rhs
H=2*x*Zp-3*Z-B*x+3*K*(K+y*b)/(2*y**2)
Psi=3*K**3*(K+2*y*b)/(16*y**4)-3*B*x*K**2/(4*y**2)-b*eta*x*x*K/(2*y)-B*eta*x**3
res=s.factor(Z*H-Psi-x*x*E)
print('IDENTITY Z*H-Psi = x^2*(F3_LHS-F3_RHS):',res==0,'residual=',res)
assert res==0
lam,w,z,u=s.symbols('lam w z u')
phi=16*lam*w**4/3+8*lam*w**3/3+4*w*w-2*w
center=s.Poly(s.expand(phi.subs(w,u-s.Rational(1,8))),u)
print('CENTERED Phi(u-1/8)=',center.as_expr())
print('CENTERED_LINEAR=',center.coeff_monomial(u))
print('CENTERED_CUBIC=',center.coeff_monomial(u**3))
print('DERIVATIVE_DISCRIMINANT=',s.factor(s.discriminant(s.diff(phi,w),w)))
cv=s.factor(s.resultant(s.diff(phi,w),phi-z,w))
print('CRITICAL_VALUE_RESULTANT=',cv)
print('CRITICAL_VALUE_RESULTANT_DISCRIMINANT=',s.factor(s.discriminant(cv,z)))
# Discriminant of the monic cubic of critical values, legal only lam != 0.
cvmon=s.Poly(cv,z).monic().as_expr()
print('MONIC_CRITICAL_VALUE_CUBIC=',s.factor(cvmon))
print('MONIC_CRITICAL_VALUE_DISCRIMINANT=',s.factor(s.discriminant(cvmon,z)))
print('PHI_LAM36_CENTERED=',s.factor(center.as_expr().subs(lam,36)))
