#!/usr/bin/env python3
"""Residual claim: the 12 M2<=m automorphism witnesses fail Moh (4) or (6)."""
from math import gcd
from etaexp import char_data
from autoscan import (jac, deg, degy, build, gauge)
import random

# (4) M_s = n-2   (6) 3 <= s <= 5 and d_s >= 4
rnd = random.Random(7717)
seqs = [[2],[3],[4],[5],[6],[7],[2,2],[3,2],[2,3],[4,2],[2,4],[3,3],[5,2],[2,5],[4,3],[3,4],
        [2,2,2],[3,2,2],[2,3,2],[2,2,3],[3,3,2],[2,2,2,2],[4,2,2],[2,4,2],[2,2,4],[5,3],[3,5],
        [2,2,2,2,2],[3,2,3],[4,4],[2,6],[6,2]]
seen=set(); w=[]
for L in seqs:
    for rep in range(6):
        Ff,Gg=build(L,rnd)
        f2,g2=gauge(Ff,Gg,rnd)
        if f2 is None: continue
        J=jac(f2,g2)
        if len(J)!=1 or (0,0) not in J: continue
        m,n=degy(f2),degy(g2)
        if not (1<n<=30 and 0<m<n): continue
        Ms,ds,fj=char_data(f2,m,g2,n)
        if len(Ms)<2: continue
        key=(n,m,tuple(Ms))
        if key in seen: continue
        seen.add(key)
        if Ms[1]<=m:
            w.append((L,n,m,Ms,ds))

print("M2<=m witnesses:", len(w))
print("  %-16s %4s %4s %-24s %-20s %4s %4s %6s %6s" %
      ("build","n","m","M","d","s","d_s","(4)","(6)"))
for L,n,m,Ms,ds in sorted(w, key=lambda t: (t[1],t[2])):
    s=len(Ms); d_s=ds[s-1]
    c4 = (Ms[-1]==n-2)
    c6 = (3<=s<=5 and d_s>=4)
    print("  %-16s %4d %4d %-24s %-20s %4d %4d %6s %6s" %
          (str(L),n,m,str(Ms),str(ds),s,d_s, c4, c6))
    if c4 and c6:
        print("    BOTH (4) and (6) HOLD -- residual claim FAILS")
print("  all fail (4) or (6):", all(not ((r[3][-1]==r[1]-2) and (3<=len(r[3])<=5 and r[4][len(r[3])-1]>=4)) for r in w))
print("  fail (4):", sum(1 for r in w if r[3][-1] != r[1]-2), "/", len(w))
print("  fail (6):", sum(1 for r in w if not (3<=len(r[3])<=5 and r[4][len(r[3])-1]>=4)), "/", len(w))
print("  d_s>=4:", [(r[1],r[2],r[3],r[4]) for r in w if r[4][len(r[3])-1]>=4])
