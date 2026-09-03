"""Is 'every edge is the zero factor' enough for Prop 5.6's sigma_1 = pi t^{delta_1}?

The centre of D_1 is the common truncation of the roots in D_1: sum_{e<delta_1} a_e t^e.
Moh's p.201 conjugation is over k<<tbar^{A_1}>> with tbar^{L_1 A_1}=t, so the centre
lies in that fixed field, i.e. its support is contained in (1/L_1)Z.  The tower edges
only pin the coefficients at the radii delta_s,...,delta_2.  Everything else in
(1/L_1)Z cap [-1, delta_1) is a free coefficient; only the integral exponents -1 and 0
are removable by Moh's own p.190 automorphism y -> y - ax - b.
"""
import sys
sys.path.insert(0,'.')
from fractions import Fraction as F
from math import lcm
import moh_skeleton_full_frozen as B
import opus5_probe as OP

def chain_slack(T, chain):
    """chain = (V_2,...,V_s) radii along one all-zero chain."""
    dl = {i: T.delta(i, chain[i-1:]) for i in range(1, T.s+1)}
    L1 = 1
    for i in range(2, T.s+1):
        L1 = lcm(L1, dl[i].denominator)
    radii = {dl[i] for i in range(2, T.s+1)}
    free_bare, free_rec = [], []
    e = F(-1)
    step = F(1, L1)
    while e < dl[1]:
        if e not in radii:
            if e != -1:
                free_bare.append(e)
            if e != -1 and e != 0:
                free_rec.append(e)
        e += step
    return L1, dl[1], sorted(radii), free_bare, free_rec

rows = [(n,m,Ms,V) for n in range(4,101) for m,Ms,V in B.census(n,Kmin=2,full=True)]
printed = {(n,m,tuple(Ms),tuple(sorted(V.items()))) for n,m,Ms,V,*_ in B.MOH_TABLE}
n_empty_bare = n_empty_rec = 0
tot = 0
examples = []
for n,m,Ms,V in rows:
    T = OP.Tree(n,m,Ms)
    if T.s < 2: continue
    chain = tuple(V[i] for i in range(2, T.s+1))
    L1, d1, radii, fb, fr = chain_slack(T, chain)
    tot += 1
    if not fb: n_empty_bare += 1
    if not fr: n_empty_rec += 1
    k = (n,m,tuple(Ms),tuple(sorted(V.items())))
    if k in printed:
        examples.append((n,m,list(Ms),dict(sorted(V.items())),L1,str(d1),
                         [str(x) for x in radii], len(fb), len(fr),
                         [str(x) for x in fr[:6]]))
print(f"selected-path chains examined: {tot}")
print(f"  chains with NO free non-radius exponent (bare, only -1 removable): {n_empty_bare}")
print(f"  chains with NO free non-radius exponent (recentred, -1 and 0 removable): {n_empty_rec}")
print("\nthe six printed rows:")
for e in examples:
    print(f"  n={e[0]} m={e[1]} M={e[2]} V={e[3]}: L_1={e[4]} delta_1={e[5]} "
          f"radii={e[6]} free(bare)={e[7]} free(recentred)={e[8]} e.g. {e[9]}")
