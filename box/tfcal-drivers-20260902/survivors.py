#!/usr/bin/env python3
"""Groups surviving (10)+(10)_1+knapsack, per degree, D <= 120."""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moh_skeleton_N import Skel, census
from d1floor import qval
from mohcond import moh10, star_congruence
Nlo,Nhi=6,16
def knap(items,u,CAP=200000):
    cand=sorted(set((v,q) for (v,q) in items if v*q<=Nhi)); reach={0:{F(0)}}; hits=set()
    for tv in range(0,u+1):
        if tv not in reach: continue
        for s0 in list(reach[tv]):
            for (v,q) in cand:
                if tv+v>u: continue
                s1=s0+v*q
                if s1>Nhi: continue
                t=reach.setdefault(tv+v,set())
                if len(t)>=CAP: return None
                t.add(s1)
                if s1.denominator==1 and Nlo<=s1<=Nhi: hits.add(int(s1))
    return sorted(hits)
tot=0; empty=[]
for n in range(48,121):
    g={}
    for (m,Ms,V) in census(n):
        S=Skel(n,m,list(Ms),V)
        if S.windows_ok() and moh10(S) and star_congruence(S):
            g.setdefault((m,Ms,S.V[S.s]),[]).append(S)
    rows=[]
    for key,items in sorted(g.items()):
        u=int(items[0].u)
        h=knap([(S.V[2],qval(S)) for S in items],u)
        if h is None or h: rows.append((key,items,h))
    if not g: continue
    tot+=len(rows)
    if not rows: empty.append(n)
    print("D=%3d : groups after (10)+(10)_1 = %3d, knapsack-alive = %3d" % (n,len(g),len(rows)))
    if n in (105,108,112,117,120) or len(rows)<=4:
        for (key,items,h) in rows:
            S0=items[0]
            print("        m=%-4d M=%-18s V_s=%-3d s=%d u=%-3d (d,e)=(%d,%d) a_1 in %s  N in %s"
                  % (key[0],str(list(key[1])),key[2],S0.s,int(S0.u),S0.dd,S0.e,
                     sorted(set(S.e*S.V[2] for S in items))[:6], h))
print("\nTOTAL alive D<=120: %d groups ; degrees EMPTY after (10)+(10)_1: %s" %
      (tot, [n for n in range(48,121) if any(True for _ in census(n)) ] and empty))
