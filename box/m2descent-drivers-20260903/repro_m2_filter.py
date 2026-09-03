#!/usr/bin/env python3
"""M2-DESCENT step (1a): REPRODUCE the Fable measurement of the predicate M_2 > m.

FAIL-CLOSED: the six printed p.202 rows must all be kept, or nothing is printed.
Imports box/moh_skeleton_full.py (tracked, unmodified).
"""
import sys, os
from fractions import Fraction as F
from math import gcd, lcm
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import moh_skeleton_full as MS
from moh_skeleton_full import Skel, census, groups_of, uni_hits, mixed_hit, MOH_TABLE

M2_above_m = lambda S: S.M[2] > S.m
u_s        = lambda S: S.d[S.s] - S.V[S.s]

def am_semigroup(S):
    Ms=[S.M[i] for i in range(1,S.s+1)]; ds=[S.d[i] for i in range(1,S.s+2)]
    if ds[-1]>1: Ms.append(S.n-1); ds.append(1)
    nn=[ds[i]//ds[i+1] for i in range(len(Ms))]; r=[S.n,-Ms[0]]
    for j in range(2,len(Ms)+1): r.append(nn[j-2]*r[j-1]-(Ms[j-1]-Ms[j-2]))
    def rec(i,rem): return rem>=0 and rem%r[0]==0 if i==0 else \
        any(rec(i-1,rem-c*r[i]) for c in range(nn[i-1]) if rem-c*r[i]>=0)
    return all(rec(j-1,nn[j-1]*r[j]) and (j==len(Ms) or r[j+1]<nn[j-1]*r[j]) for j in range(1,len(Ms)+1))

# ---------- CONTROL: printed rows kept -------------------------------------
print("== CONTROL P: the six printed p.202 rows under M_2 > m ==")
kept = 0
for (n,m,Ms,Vs,lab,_,_,_) in MOH_TABLE:
    S = Skel(n,m,Ms,Vs)
    ok = M2_above_m(S)
    kept += ok
    print("   %-24s n=%3d m=%3d M_2=%3d  M_2>m: %-5s  u_s=%d  sg=%s"
          % (lab, n, m, S.M[2], ok, u_s(S), am_semigroup(S)))
print("   printed kept: %d/6" % kept)
assert kept == 6, "FAIL-CLOSED: printed rows lost"

# ---------- the 658-row space (Moh's own space, n <= 100, K >= 2) ----------
print("\n== the (1)-(13) rows at n <= 100, Kmin=2 (Moh's space) ==")
rows = []
for n in range(1, 101):
    for (m, Msx, V) in census(n, Kmin=2, full=True):
        rows.append(Skel(n, m, list(Msx), V))
cls = lambda R: set((S.n, S.m) for S in R)
print("   (1)-(13) baseline            rows=%4d  classes=%3d" % (len(rows), len(cls(rows))))
sg = [S for S in rows if am_semigroup(S)]
print("   + Abhyankar-Moh semigroup    rows=%4d  classes=%3d   (AUTOMATIC: %s)"
      % (len(sg), len(cls(sg)), len(sg)==len(rows)))
f2 = [S for S in rows if M2_above_m(S)]
print("   + M_2 > m                    rows=%4d  classes=%3d" % (len(f2), len(cls(f2))))
fall = [S for S in rows if all(S.M[i] > S.m for i in range(2, S.s+1))]
print("   + all M_i > m (i>=2)         rows=%4d  classes=%3d" % (len(fall), len(cls(fall))))
print("   (M_2>m) == (all M_i>m):      %s" % (set(map(id,f2))==set(map(id,fall))))

# ---------- the (75,50) residue -------------------------------------------
print("\n== (75,50) under M_2 > m ==")
r75 = [S for S in rows if (S.n, S.m) == (75, 50)]
r75f = [S for S in r75 if M2_above_m(S)]
print("   (1)-(13) rows at (75,50): %d ; with M_2>m: %d ; M_2 values %s"
      % (len(r75), len(r75f), sorted(set(S.M[2] for S in r75f))))
for S in r75f:
    Ns = sorted(uni_hits([(S.V[2], S.q(), S.u)], 6, None))
    print("      M=%s V=%s u=%s q=%s  N(int,>=6)=%s"
          % ([S.M[i] for i in range(2,S.s+1)], {i:S.V[i] for i in range(2,S.s+1)},
             S.u, S.q(), Ns))

# ---------- + integral pinned N >= 6 (UNI) --------------------------------
print("\n== M_2 > m AND integral pinned N >= 6 (UNI) ==")
res = [S for S in f2 if uni_hits([(S.V[2], S.q(), S.u)], 6, None)]
print("   rows=%d  classes=%d" % (len(res), len(cls(res))))
printed_keys = set()
for (n,m,Ms,Vs,lab,_,_,_) in MOH_TABLE:
    printed_keys.add((n, m, tuple(Ms), tuple(sorted(Vs.items()))))
def key(S): return (S.n, S.m, tuple(S.M[i] for i in range(2,S.s+1)),
                    tuple(sorted((i,S.V[i]) for i in range(2,S.s+1))))
pk = [S for S in res if key(S) in printed_keys]
print("   printed rows surviving this stage: %d/6" % len(pk))
resid = [S for S in res if key(S) not in printed_keys]
print("   residual rows beyond Moh's table: %d  (u_s=1: %d)"
      % (len(resid), sum(1 for S in resid if u_s(S)==1)))
from collections import Counter
print("   residual by class:", sorted(Counter((S.n,S.m) for S in resid).items()))
