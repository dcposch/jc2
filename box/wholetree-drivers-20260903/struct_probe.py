"""Structural facts checked at EVERY node reachable in the whole tree."""
import sys
sys.path.insert(0,'.')
from fractions import Fraction as F
from math import gcd, lcm
import moh_skeleton_full_frozen as B
import opus5_probe as OP

rows = [(n,m,Ms,V) for n in range(4,101) for m,Ms,V in B.census(n,Kmin=2,full=True)]
stats = dict(nodes=0, capfail=0, A1=0, deltas=0, delta_int=0, delta_int_nonzero=0,
             delta_out=0, delta_ge1=0, delta_le_m1=0, ex_cap=[], ex_int=[], Qle1=0)
topviol = 0
for n,m,Ms,V in rows:
    T = OP.Tree(n,m,Ms)
    s = T.s
    # (3) top-level vacuity: p at D_s has degree d_s; complement is minor
    ds, Vs = T.d[s], V[s]
    if not (ds - Vs < F(ds, T.n - T.M[s])):
        topviol += 1
    # walk every V-path with V_j in [1..P_j] (all factor multiplicities), not
    # only major ones: the congruence must hold wherever a node exists.
    def walk(j, high):
        dl,L,A,P,Q,lo = T.node(j,high)
        stats['nodes'] += 1
        if A == 1: stats['A1'] += 1
        if Q <= 1: stats['Qle1'] += 1
        if (Q-1) % A:
            stats['capfail'] += 1
            if len(stats['ex_cap'])<5: stats['ex_cap'].append((n,m,Ms,high,j,A,P,Q))
        if dl.denominator == 1:
            stats['delta_int'] += 1
            if dl != 0:
                stats['delta_int_nonzero'] += 1
                if len(stats['ex_int'])<5: stats['ex_int'].append((n,m,Ms,high,j,str(dl)))
        if not (-1 < dl < 1): stats['delta_out'] += 1
        if dl >= 1: stats['delta_ge1'] += 1
        if dl <= -1: stats['delta_le_m1'] += 1
        if j == 2: return
        # descend along every MAJOR multiplicity that can occur in a partition
        b = P % A
        seen = set()
        cand = set()
        for bb in range(b, P+1, A):
            if F(bb) > lo: cand.add(bb)
            for v in range(1, (P-bb)//A + 1):
                if F(v) > lo: cand.add(v)
        for v in sorted(cand):
            if v in seen: continue
            seen.add(v); walk(j-1, (v,)+high)
    walk(s-1, (V[s],))
print("rows", len(rows))
print("top-level vacuity violations (d_s - V_s >= threshold):", topviol)
for k in ('nodes','capfail','A1','Qle1','delta_int','delta_int_nonzero','delta_out','delta_ge1','delta_le_m1'):
    print(f"  {k:20s} {stats[k]}")
print("cap examples", stats['ex_cap'])
print("nonzero integral delta examples", stats['ex_int'])
