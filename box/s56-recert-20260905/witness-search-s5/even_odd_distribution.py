#!/usr/bin/env python3
"""Eliminate the odd P coefficients for an even centered Q.

Q=F(x,z), P=y*G(x,z), z=y^2, deg_z(F,G)=(3,4).  The Jacobian is
F_x(G+2zG_z)-2zF_zG_x.  High z rows determine G's four lower
coefficients up to constants; the remaining rows define a distribution on
the three coefficients of F.
"""
import sympy as s

A,B,C=s.symbols('A B C')
dA,dB,dC=s.symbols('dA dB dC')
qs=(A,B,C); ds=(dA,dB,dC)
z=s.symbols('z')
k3,k2,k1,k0=s.symbols('k3 k2 k1 k0')

def D(w): return s.expand(sum(s.diff(w,q)*dq for q,dq in zip(qs,ds)))
def primitive(form):
    cc=[s.expand(form).coeff(dq) for dq in ds]
    pot=s.integrate(cc[0],A)
    pot+=s.integrate(s.expand(cc[1]-s.diff(pot,B)),B)
    pot+=s.integrate(s.expand(cc[2]-s.diff(pot,C)),C)
    assert s.expand(D(pot)-form)==0
    return s.factor(pot)

F=z**3+A*z**2+B*z+C
g={4:s.Integer(1)}
def jac():
    G=sum(v*z**i for i,v in g.items())
    return s.expand(D(F)*(G+2*z*s.diff(G,z))-2*z*s.diff(F,z)*D(G))

# z^6,...,z^3 determine g3,...,g0, coefficient -6 D(g_i) pattern
ks={3:k3,2:k2,1:k1,0:k0}
for i in range(3,-1,-1):
    g[i]=s.Integer(0)
    coeff=s.Poly(jac(),z).coeff_monomial(z**(i+3))
    # coefficient of D(g_i): -2*z*(3*z^2)*D(g_i)=-6 D(g_i) z^(i+3)
    g[i]=s.expand(primitive(coeff/s.Integer(6))+ks[i])

J=s.expand(jac())
forms=[s.factor(s.Poly(J,z).coeff_monomial(z**i)) for i in range(2,-1,-1)]

if __name__ == '__main__':
    print('G')
    for i in range(3,-1,-1): print(i,s.factor(g[i]))
    print('R')
    for i,rr in zip(range(2,-1,-1),forms): print(i,rr)
    M=s.Matrix([[s.expand(rr).coeff(dq) for dq in ds] for rr in forms[:2]])
    print('M',M)
    v=s.Matrix([M[0,1]*M[1,2]-M[0,2]*M[1,1],M[0,2]*M[1,0]-M[0,0]*M[1,2],M[0,0]*M[1,1]-M[0,1]*M[1,0]])
    print('KERNEL',[s.factor(w) for w in v])
    print('R0_ON_KERNEL',s.factor(forms[2].subs(dict(zip(ds,v)))))
