#!/usr/bin/env python3
"""Exact small matrix/interface checks; no solver or files written."""
import json
import sympy as s
x,y,z,u,v,a,alpha=s.symbols('x y z u v a alpha')
t11,t12,t13,t22,t23,t33=s.symbols('t11 t12 t13 t22 t23 t33')
T=s.Matrix([[t11,t12,t13],[t12,t22,t23],[t13,t23,t33]])
def bordered(M,w):
    B=T+u*M
    return s.expand(-(w.T*B.adjugate()*w)[0])
d2=bordered(s.diag(1,1,0),s.Matrix([x,y,0]))
assert s.expand(d2.coeff(u,1)+(x*x+y*y)*t33)==0
assert s.expand(d2.subs(t33,0)-(x*t23-y*t13)**2)==0
d1=bordered(s.diag(1,0,0),s.Matrix([x,alpha,0]))
assert s.expand(d1.coeff(u,1)+alpha**2*t33)==0
assert s.expand(d1.subs(t33,0)-(x*t23-alpha*t13)**2)==0

p,q,r,ss,A,B,C=s.symbols('p q r ss A B C')
J=s.Matrix([[p,q],[r,ss]])
H=s.Matrix([[A,B,p,r],[B,C,q,ss],[p,q,0,0],[r,ss,0,0]])
assert s.expand(H.det()-J.det()**2)==0
M=s.Matrix([[A,B,0],[B,C,0],[0,0,0]])
w=s.Matrix([p,q,0])
assert (w.T*M.adjugate()*w)[0]==0

q0=x+y**2
G=y+q0**3
F=q0+G**2
j=s.expand(s.diff(F,x)*s.diff(G,y)-s.diff(F,y)*s.diff(G,x))
assert j==1
assert s.expand(s.hessian(G,(x,y)).det()-36*q0**3)==0
assert s.expand(s.diff(G,y)-2*y*s.diff(G,x))==1
assert s.Poly(F,x,y).total_degree()==12
assert s.Poly(G,x,y).total_degree()==6
perturbed=u*(x+y**2)+v*y+a*v**2
detpert=s.expand(s.hessian(perturbed,(x,y,u,v)).det())
assert detpert==1-4*a*u

# Rank-one inverse identities over a constant unit alpha.
Q=x**2/2+alpha*y
S=-x/alpha
D=lambda h:s.expand(x*s.diff(h,y)-alpha*s.diff(h,x))
assert D(Q)==0 and D(S)==1
assert s.expand(Q.subs({x:-alpha*z,y:(u-alpha**2*z**2/2)/alpha}, simultaneous=True)-u)==0

print(json.dumps({
    'status':'PASS_EXACT_SYMBOLIC',
    'rank_two_u_coefficient':str(d2.coeff(u,1)),
    'rank_one_u_coefficient':str(d1.coeff(u,1)),
    'pairing_hessian_determinant':'det J(F,G)^2',
    'pairing_high_coefficient':'identically zero',
    'variable_rank_control_degrees':[12,6],
    'variable_rank_control_jacobian':1,
    'det_Hess_G':str(36*q0**3),
    'added_quadratic_countercontrol':str(detpert)
},indent=2,sort_keys=True))
