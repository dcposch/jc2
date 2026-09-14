#!/usr/bin/env python3
"""Eliminate P for the h=y^3 subchart and analyze the residual distribution.

All work is symbolic over Q.  Q=y^6+b2(x)y^2+b1(x)y+b0(x), while P is
monic of y-degree 9.  The t^13,...,t^5 Jacobian rows determine P's
coefficients up to constants.  The remaining rows are one-forms in db0,db1,db2.
"""
import sympy as s

b0,b1,b2=s.symbols('b0 b1 b2')
d0,d1,d2=s.symbols('d0 d1 d2')
bs=(b0,b1,b2); ds=(d0,d1,d2)
t=s.symbols('t')
a8,a7,a6,k5,k4,k3,k2,k1,k0=s.symbols('a8 a7 a6 k5 k4 k3 k2 k1 k0')

def D(z):
    return s.expand(sum(s.diff(z,b)*d for b,d in zip(bs,ds)))

def primitive(form):
    """Integrate a closed polynomial one-form along coordinate axes."""
    form=s.expand(form)
    coeff=[s.expand(form.coeff(d)) for d in ds]
    pot=s.integrate(coeff[0],b0)
    rem=s.expand(coeff[1]-s.diff(pot,b1))
    pot += s.integrate(rem,b1)
    rem=s.expand(coeff[2]-s.diff(pot,b2))
    pot += s.integrate(rem,b2)
    assert s.expand(D(pot)-form)==0, s.factor(D(pot)-form)
    return s.factor(pot)

q={6:s.Integer(1),5:s.Integer(0),4:s.Integer(0),3:s.Integer(0),2:b2,1:b1,0:b0}
p={9:s.Integer(1),8:a8,7:a7,6:a6}

Q=sum(v*t**i for i,v in q.items())
def jac_with(partial_p):
    P=sum(v*t**i for i,v in partial_p.items())
    # x derivative is D; t derivative ordinary.
    return s.expand(D(Q)*s.diff(P,t)-s.diff(Q,t)*D(P))

# Descending equations determine p5..p0. Constants ki record integration.
constants={5:k5,4:k4,3:k3,2:k2,1:k1,0:k0}
for target_i in range(5,-1,-1):
    # p[target_i] enters in t^(target_i+5) as -6 D(p_i).
    p[target_i]=s.Integer(0)
    coeff=s.Poly(jac_with(p),t).coeff_monomial(t**(target_i+5))
    assert not any(s.diff(coeff,d)!=0 for d in ds) is False
    # equation coeff - 6 D(p_i)=0 => D(p_i)=coeff/6
    p[target_i]=s.expand(primitive(coeff/s.Integer(6))+constants[target_i])

J=s.expand(jac_with(p))
forms=[s.factor(s.Poly(J,t).coeff_monomial(t**i)) for i in range(4,-1,-1)]

if __name__ == '__main__':
    print('P_COEFFICIENTS')
    for i in range(8,-1,-1): print(f'p{i} = {s.factor(p[i])}')
    print('RESIDUAL_FORMS')
    for i,z in zip(range(4,-1,-1),forms): print(f'r{i} = {z}')
    M=s.Matrix([[s.expand(z).coeff(d) for d in ds] for z in forms[:4]])
    print('MATRIX_R4_TO_R1')
    print(M)
    mins=[]
    for rows in s.utilities.iterables.combinations(range(4),3):
        det=s.factor(M[list(rows),:].det())
        mins.append(det)
        print('minor',rows,'=',det)
    print('MINORS_GCD',s.factor(s.gcd_list(mins)))
