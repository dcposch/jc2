#!/usr/bin/env python3
"""Universal symbolic check of the b3=0 Abel reduction."""
import sympy as s
x=s.symbols('x')
y,g,B,delta=s.symbols('y g B delta', nonzero=True)
C=s.Function('C')(x)
T=s.Function('T')(x)
Z=s.Function('Z')(x)
Y=Z+x*x*C*T/y
Tp=g*(5*C+3*x*s.diff(C,x))/(2*y)
u=(y*(2*x*s.diff(Z,x)-Z-g*B)/(3*g*x)+x*x*C*Tp/g)
v=u*T/y+((2*C+x*s.diff(C,x))*Y-x*C*s.diff(Y,x))/(2*y)
D2=-3*g*x*u+x*x*C*s.diff(x*T,x)-2*s.diff(x*x*C,x)*x*T+2*y*x*s.diff(Y,x)-y*Y-y*g*B
D1=2*y*x*v+x*x*C*s.diff(Y,x)-s.diff(x*x*C,x)*Y-2*u*x*T
assert s.simplify(D2.subs(s.diff(T,x),Tp))==0
assert s.simplify(D1)==0
D0=s.expand(x*x*C*v-u*Y).subs(s.diff(T,x),Tp)
w=s.Function('w')(x)
a=3*x**3*C**2/(4*y*y)
D0w=D0.subs({s.diff(Z,x):g*s.diff(w-a,x),Z:g*(w-a)})
abel=w*w+(B-2*a)*w+a*a/3-B*a-2*x*w*s.diff(w,x)
assert s.simplify(D0w-g*y*abel/(3*x))==0
print('UNIVERSAL_ABEL_IDENTITY_PASS')
print('D0 = (g*y/(3*x)) * [w²+(B−2a)w+a²/3−Ba−2xwwprime]')
print('a=3*x^3*C^2/(4*y^2), w=(Y−x^2*C*T/y)/g+a')
t,d=s.symbols('t d')
q=2*t+1
alpha=3/(4*y*y)
omega=alpha*(2*d-1)/(4*t+1)
lead=s.factor((4*t+1)*omega**2+2*alpha*omega-alpha**2/3)
assert s.factor(lead/(3*d*d-t-1))==3/(4*y**4*(4*t+1))
print('LEADING_NORMALIZATION_PASS')
print('leading residual =',lead)
A=x*C
H=(2*x*s.diff(w,x)-w-B+2*a)/x
factor_rhs=3*(x*A**4-4*B*y*y*A*A-16*y**3*delta/g)/(16*y**4)
assert s.simplify(w*H-factor_rhs + (abel-3*x*delta/(g*y))/x)==0
print('ROOT_DIVISIBILITY_IDENTITY_PASS')
