#!/usr/bin/env python3
"""Print the coefficient ODEs for h=t^3 in the S5 [2] chart."""
import sympy as s

x,t=s.symbols('x t')
b=[s.Function(f'b{i}')(x) for i in range(3)]
p=[s.Function(f'p{i}')(x) for i in range(9)]
Q=t**6+b[2]*t**2+b[1]*t+b[0]
P=t**9+sum(p[i]*t**i for i in range(9))
J=s.expand(s.diff(Q,x)*s.diff(P,t)-s.diff(Q,t)*s.diff(P,x))
for i in range(s.Poly(J,t).degree(),-1,-1):
    z=s.factor(s.Poly(J,t).coeff_monomial(t**i))
    if z!=0:
        print(i, z)
