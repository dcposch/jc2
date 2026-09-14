#!/usr/bin/env python3
"""Universal all-b3 Laurent Abel reduction, coefficient-exact."""
import sympy as s
x=s.symbols('x')
y,g,B,b,b1,kappa=s.symbols('y g B b b1 kappa', nonzero=False)
C=s.Function('C')(x)
T=s.Function('T')(x)
Z=s.Function('Z')(x)
K=x*x*C-y*b
F=x*T-g*b
Tp=g*(5*C+3*x*s.diff(C,x))/(2*y)
Y=Z+K*F/(y*x)
u=K*(3*x*s.diff(K,x)-K+y*b)/(2*y*x*x)+y*(2*x*s.diff(Z,x)-Z-g*B)/(3*g*x)
v=(y*g*b1-K*s.diff(Y,x)+s.diff(K,x)*Y+2*u*F)/(2*y*x)
D2=-3*g*x*u+K*s.diff(F,x)-2*s.diff(K,x)*F+2*y*x*s.diff(Y,x)-y*Y-y*g*B
assert s.simplify(D2.subs(s.diff(T,x),Tp))==0
D0=s.expand(K*v-u*Y).subs(s.diff(T,x),Tp)
w=s.Function('w')(x)
a=3*K*K/(4*y*y*x)
d0=3*b*K/(2*y*x)
D0w=D0.subs({s.diff(Z,x):g*s.diff(w-a,x),Z:g*(w-a)})
rhs=w*w+(B-2*a-d0)*w+a*(a+d0)/3-B*a+3*b1*K/(2*y)-2*x*w*s.diff(w,x)
assert s.simplify(D0w-g*y*rhs/(3*x))==0
print('ALL_B3_LAURENT_ABEL_PASS')
P=s.Function('P')(x)
E=s.expand(rhs.subs({s.diff(w,x):s.diff(P-b*b/(4*x),x),w:P-b*b/(4*x)})-3*x*kappa/y)
print('POLYNOMIAL_EQUATION_TIMES_X =')
print(s.collect(s.cancel(x*E),[s.diff(P,x),P]))
print('REGULAR_LAURENT_FORM_PASS')
r=b*b/4
AA=3*x**3*C*C/(4*y*y)
DD=3*b*x*C/(2*y)
parent_rhs=P*P+(B-2*AA+DD)*P+AA*(AA-DD)/3-B*(AA-DD)+3*b1*K/(2*y)-3*x*kappa/y+(2*r*AA-4*r*(B+P))/x
assert s.simplify(E-parent_rhs+2*(x*P-r)*s.diff(P,x))==0
print('PARENT_POLE_ELIMINATION_PASS')
z_regular=g*(P-AA+DD-b*b/x)
u_regular=s.simplify(u.subs({s.diff(Z,x):s.diff(z_regular,x),Z:z_regular}))
u_claim=y*(2*x*s.diff(P,x)-P-B)/(3*x)+x*x*C*(5*C+2*x*s.diff(C,x))/(4*y)-b*C-b*x*s.diff(C,x)/2
assert s.simplify(u_regular-u_claim)==0
Y_regular=s.simplify(Y.subs(Z,z_regular))
S_claim=g*(P+B)/x-3*g*x*x*C*C/(4*y*y)+g*b*C/(2*y)+x*C*T/y
assert s.simplify(Y_regular-(x*S_claim-b*T-g*B))==0
print('POLYNOMIAL_RECONSTRUCTION_PASS')
tt,dd=s.symbols('tt dd')
qq=2*tt+1
ee=3*tt+1
yy=(dd+tt+1)/(2*qq)
gg=ee*tt*(3*dd+2*tt+2)/(6*qq**3)
wwlead=3*(2*dd-1)/(4*yy**2*(4*tt+1))
tle=gg*(3*tt+2)/(2*yy*tt)
sle=gg*wwlead-3*gg/(4*yy**2)+tle/yy
vle=(-tt*sle+2*qq*tle)/(2*yy)
targets=[tle-ee*(dd+qq)/(2*qq**2),sle-ee/qq,vle-ee]
for item in targets:
    num=s.together(item).as_numer_denom()[0]
    assert s.factor(s.rem(num,3*dd**2-tt-1,dd))==0
print('ALL_NORMALIZED_LEADING_COEFFICIENTS_PASS')
