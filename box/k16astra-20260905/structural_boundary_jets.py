#!/usr/bin/env python3
"""Exact universal L=0 jets; no fitted t-values, one SymPy process."""
import sympy as s

x = s.symbols('x')
y, g, b1, b2, b3, T0 = s.symbols('y g b1 b2 b3 T0', nonzero=False)
cs = s.symbols('C0:5')
us = s.symbols('u0:6')  # ui = (d/dx)^i U'(0)
C = sum(cs[i]*x**i/s.factorial(i) for i in range(len(cs)))
u = sum(us[i]*x**i/s.factorial(i) for i in range(len(us)))
T = T0 + s.integrate(g*(5*C+3*x*s.diff(C,x))/(2*y), x)
K = x*x*C-y*b3
F = x*T-g*b3
yn = s.symbols('Y1:6')
Y = -b3*T0-g*b2 + sum(yn[i-1]*x**i/s.factorial(i) for i in range(1,6))
D2 = s.expand(-3*g*x*u+K*s.diff(F,x)-2*s.diff(K,x)*F+2*y*x*s.diff(Y,x)-y*Y-y*g*b2)
ymap = {}
for n in range(1,6):
    eq = s.expand(D2.subs(ymap)).coeff(x,n)
    ymap[yn[n-1]] = s.factor(s.solve(eq,yn[n-1])[0])
Y = s.expand(Y.subs(ymap))
vn = s.symbols('v0:4')
v = sum(vn[i]*x**i/s.factorial(i) for i in range(4))
D1 = s.expand(2*y*x*v+K*s.diff(Y,x)-s.diff(K,x)*Y-2*u*F-y*g*b1)
b1sol = s.factor(s.solve(D1.coeff(x,0),b1)[0])
vmap = {}
for n in range(1,5):
    eq = s.expand(D1.subs(vmap)).coeff(x,n)
    vmap[vn[n-1]] = s.factor(s.solve(eq,vn[n-1])[0])
v = s.expand(v.subs(vmap))
D0 = s.expand(K*v-u*Y)
R0 = us[0]+b3*cs[0]
assert s.factor(b1sol+b3*R0/y)==0
assert s.factor(D0.coeff(x,0)-g*b2*R0)==0
assert s.factor(vmap[vn[0]]-(us[0]*T0-g*b2*cs[0])/y)==0
expected_d1 = g*(b2*(us[1]+s.Rational(3,2)*b3*cs[1])
                 +b3*b3*(us[2]+2*b3*cs[2])/20
                 -R0*(3*us[0]+2*b3*cs[0])/y)
assert s.factor(D0.coeff(x,1)-expected_d1)==0
print('UNIVERSAL_BOUNDARY_JETS_PASS')
print('b1 =', b1sol)
print('minus_D0_at_L0 =',s.factor(-D0.coeff(x,0)))
print('Vprime_at_L0 =',vmap[vn[0]])
print('D0prime_at_L0 =',s.factor(D0.coeff(x,1)))
print('D0prime_b3zero =',s.factor(D0.coeff(x,1).subs(b3,0)))
print('D0second_b3zero =',s.factor(2*D0.coeff(x,2).subs(b3,0)))
print('D0third_b3zero =',s.factor(6*D0.coeff(x,3).subs(b3,0)))
