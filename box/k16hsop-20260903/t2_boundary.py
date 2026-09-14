#!/usr/bin/env python3
"""The t=2 boundary control, on independently generated rows.

A_2 = Q[y]/((5y-1)(5y-2)) = Q x Q.  The tail is (T_{2,2}, T_{2,3}), weights 7 and 6,
in A_2[b4,b3] with wt(b4)=1, wt(b3)=3.  The two geometric fibres have IDENTICAL
weighted degree data.  Checked here on each fibre separately (no zero divisor
inverted):  factorisation of the rows, dim, length, and the predicted CI length
L_2 = 2*binom(7,1) = 14.
"""
import sympy as sp, itertools, sys
sys.path.insert(0,'/home/ubuntu/jc2/box/k16hsop-20260903')
from tail_structure import build

D = build(2, verbose=False)
y,b3,b4 = D['y'], D['b3'], D['b4']
T = D['T']
print("t=2 rows (R=-E convention, T=-[X^k]R):")
for k in range(4):
    print(f"  T[{k}] = {sp.factor(sp.simplify(T[k]))}")
print()
for yv in [sp.Rational(1,5), sp.Rational(2,5)]:
    print(f"--- fibre y = {yv} ---")
    rows = [sp.expand(sp.simplify(T[k].subs(y, yv))) for k in (2,3)]
    for k,f in zip((2,3),rows):
        print(f"   T[{k}] = {sp.factor(f)}")
    # gcd / common factor
    g = sp.gcd(rows[0], rows[1])
    print(f"   gcd(T2,T3) = {sp.factor(g)}")
    a0 = sp.Poly(rows[1], b3).nth(2)
    print(f"   a_0 = [b3^2]T_{{2,3}} = {a0}   -> {'UNIT' if a0!=0 else 'ZERO (alpha_2 vanishes)'}")
    G = sp.groebner(rows, b4, b3, order='grevlex')
    lms = [sp.Poly(f, b4, b3).monoms(order='grevlex')[0] for f in G.exprs]
    pure_b4 = [m[0] for m in lms if m[1]==0 and m[0]>0]
    pure_b3 = [m[1] for m in lms if m[0]==0 and m[1]>0]
    if not pure_b4 or not pure_b3:
        missing = 'b4' if not pure_b4 else 'b3'
        axis = 'b4' if not pure_b4 else 'b3'
        print(f"   GB leading monomials {lms}  ->  dim >= 1  (no pure power of {missing});"
              f"  V contains the {axis}-axis")
        print("   length = INFINITE\n")
        continue
    B = (min(pure_b4), min(pure_b3)); cnt=0
    for e in itertools.product(range(B[0]),range(B[1])):
        if not any(e[0]>=m[0] and e[1]>=m[1] for m in lms): cnt+=1
    print(f"   dim = 0,  vdim = {cnt},  predicted CI length L_2 = 14  -> match={cnt==14}\n")
print("Degree data are identical on both fibres (rows of weight 6,7; variables of")
print("weight 1,3), so no degree-only (Bezout/Froberg/Hilbert-numerator) argument")
print("can separate them.  The separating datum is alpha_2 = 28(5y-1)/625.")
