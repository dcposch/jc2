import sympy as sp
from sympy import symbols
import sys; sys.path.insert(0,'/tmp/nvm')
from ident import analyse
x, y = symbols('x y')
print("--- (A) fixed N, satellite mass -> infinity:  F = (x, x^c y^Nn) ---")
for Nn in (1,2,3):
    for c in (1,2,3,4):
        analyse("(x, x^%d y^%d)" % (c,Nn), x, x**c*y**Nn)
print("--- (B) fixed N, deg A_F -> infinity:  psi_k o (x, x y^Nn),  psi_k=(u+v^k, v) ---")
for Nn in (1,2):
    for k in (1,2,3,4):
        P = x + (x*y**Nn)**k
        Q = x*y**Nn
        analyse("psi_%d o (x,x y^%d)" % (k,Nn), P, Q)
