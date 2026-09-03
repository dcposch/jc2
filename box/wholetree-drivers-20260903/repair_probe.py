"""Repaired Prop.5.6 gate.

The centre of D_j is the common truncation of the roots in D_j.  Its support in
the window [delta_{i+1}, delta_i) has denominator dividing
L_i = lcm(den delta_s, ..., den delta_{i+1})  (Moh's L of (8) at level i:
the p.201 conjugation is over k<<tbar^{A_i}>> with tbar^{L_i A_i} = t, so the
centre lies in that fixed field).  delta_s = -1 and delta_1 < 1 always, so the
integral exponents in range are exactly -1 and 0 and BOTH are removed by Moh's
own p.190 automorphism  y -> y - a x - b.  Every other lattice point that is not
one of the chain's own radii carries a coefficient the tower data never pins.
Prop.5.6 (sigma_1 = pi t^{delta_1}) is therefore available for a chain only when
that free set is empty.
"""
import sys
sys.path.insert(0,'.')
from fractions import Fraction as F
from math import lcm
import moh_skeleton_full_frozen as B
import opus5_probe as OP


def free_exponents(T, chain):
    """chain = (V_2,...,V_s).  Returns (radii, free) for that all-zero chain."""
    dl = {i: T.delta(i, chain[i-1:]) for i in range(1, T.s+1)}
    radii = {dl[i] for i in range(2, T.s+1)}
    free = []
    L = 1
    for i in range(T.s-1, 0, -1):          # window [delta_{i+1}, delta_i)
        L = lcm(L, dl[i+1].denominator)
        e = dl[i+1]
        while e < dl[i]:
            if e not in radii and e.denominator != 1:
                free.append(e)
            e += F(1, L)
    return dl, radii, sorted(set(free))


rows = [(n,m,Ms,V) for n in range(4,101) for m,Ms,V in B.census(n,Kmin=2,full=True)]
printed = {(n,m,tuple(Ms),tuple(sorted(V.items()))) for n,m,Ms,V,*_ in B.MOH_TABLE}
svals = {}
gate_ok = 0
ex = []
for n,m,Ms,V in rows:
    T = OP.Tree(n,m,Ms)
    svals[T.s] = svals.get(T.s,0)+1
    chain = tuple(V[i] for i in range(2, T.s+1))
    dl, radii, free = free_exponents(T, chain)
    if not free:
        gate_ok += 1
    k = (n,m,tuple(Ms),tuple(sorted(V.items())))
    if k in printed:
        ex.append((n,m,list(Ms),dict(sorted(V.items())),
                   [str(dl[i]) for i in range(T.s,0,-1)],
                   [str(x) for x in free]))
print("s histogram over the 658 rows:", dict(sorted(svals.items())))
print(f"selected-path chains whose Prop.5.6 gate is CLEAN (no free non-integral"
      f" non-radius exponent): {gate_ok} / {len(rows)}")
print("\nthe six printed rows (radii delta_s..delta_1, then the free set):")
for e in ex:
    print(f"  n={e[0]} m={e[1]} M={e[2]} V={e[3]}")
    print(f"      deltas = {e[4]}   free = {e[5] if e[5] else 'EMPTY -> Prop.5.6 available'}")
