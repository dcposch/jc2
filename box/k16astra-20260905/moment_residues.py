#!/usr/bin/env python3
"""Cech-de Rham moments on the O(-3) torsor, exact symbolic low jets.

All coefficients are in translated L=h-b4 coordinates. This derives
necessary identities only; it does not assume or test the K16 atom.
"""
import sympy as s

L,x,r=s.symbols('L x r')
b1,b2,b3,c,tau,y,g=s.symbols('b1 b2 b3 c tau y g')
U=s.symbols('U0:9')
C=s.symbols('C0:7')
V=s.symbols('V0:9')
A=s.symbols('A0:8')
B=s.symbols('B0:7')

pol=lambda seq:sum(a*L**i for i,a in enumerate(seq))
Q=pol(U)+(L**2*pol(C)-y*b3)*x+y*L*x**2
P=pol(V)+pol(A)*x+pol(B)*x**2+g*L*x**3
J=tau+c*b1*x+c*b2*x**2+c*b3*x**3-c*L*x**4
Lzero=b3*r+b2*r**2+b1*r**3


def moment(H):
    out=0
    for (m,j), coeff in s.Poly(s.expand(H*J),L,x).terms():
        if m>j:
            continue
        required=j+1
        # The primitive is L^(m+1)/(m+1); x^j=r^-j.
        out += coeff*s.Poly(s.expand(Lzero**(m+1)),r).nth(required)/s.Integer(m+1)
    return s.factor(out)


for name,H in [('1',s.Integer(1)),('Q',Q),('P',P),('Q2',Q**2)]:
    raw=moment(H)
    print(f'MOMENT_{name} = {raw}',flush=True)
    if name!='1':
        # Subtract the moment of the constant H(b4,0).
        const=H.subs({L:0,x:0})
        centered=s.factor(raw-const*moment(s.Integer(1)))
        print(f'CENTERED_{name} = {centered}',flush=True)
print('MOMENT_RESIDUES_DONE',flush=True)
