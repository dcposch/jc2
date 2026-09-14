#!/usr/bin/env python3
import sympy as s
x=s.symbols('x')
L=3*x**2+2*x+1
Z=(x-1)*(x-2)
H=2*x*s.diff(Z,x)-3*Z+L
Psi=s.expand(Z*H)
R=lambda z,p,l:s.rem(2*x*s.diff(z,x)**2+l*s.diff(z,x)-s.diff(p,x),z,x)
assert R(Z,Psi,L)==0
assert s.rem(Psi,Z,x)==0
mutated=Psi+Z
assert R(Z,mutated,L)!=0
print('SQUAREFREE: exact differential factor passes; same-leading quotient mutation rejected.')
Z=(x-1)**2
H=2*x*s.diff(Z,x)-3*Z+L
D=x-1
Psi=s.expand(Z*(H+D))
assert R(Z,Psi,L)==0
assert s.rem(s.div(Psi,Z,x)[0]-H,Z,x)==x-1
print('REPEATED-ROOT NEGATIVE CONTROL: simple residue condition passes but quotient jet fails.')
print('This is a countercontrol to dropping collision jets, not a K16 point.')
