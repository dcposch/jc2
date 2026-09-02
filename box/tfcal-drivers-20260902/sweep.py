#!/usr/bin/env python3
"""Census sweep with Moh (10) at j>=2 and the level-1 star congruence (10)_1,
   then the pinned-N knapsack (hypothesis-free) at N in [Nlo,Nhi]."""
import sys, os, time
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moh_skeleton_N import Skel, census
from d1floor import qval
from mohcond import moh10, star_congruence, Delta

Nlo, Nhi = 6, 16
def knap_alive(items, u, CAP=200000):
    cand = sorted(set((v,q) for (v,q) in items if v*q <= Nhi))
    reach = {0:{F(0)}}
    for tv in range(0,u+1):
        if tv not in reach: continue
        for s0 in list(reach[tv]):
            for (v,q) in cand:
                if tv+v>u: continue
                s1=s0+v*q
                if s1>Nhi: continue
                tgt=reach.setdefault(tv+v,set())
                if len(tgt)>=CAP: return True   # capped -> count as ALIVE (floor on kills)
                tgt.add(s1)
                if s1.denominator==1 and Nlo<=s1<=Nhi: return True
    return False

lo=int(sys.argv[1]); hi=int(sys.argv[2])
print("== sweep D in [%d,%d]: base census -> Moh(10) -> +(10)_1 -> +knapsack N in [%d,%d] ==" % (lo,hi,Nlo,Nhi))
print("   %5s %10s %10s %10s %10s %10s %10s %10s" %
      ("D","V-skel","grp","g:(10)","g:+(10)_1","g:+knap","V:(10)","V:+(10)_1"))
T=[0]*7
for n in range(lo,hi+1):
    t0=time.time()
    g0={}; g1={}; g2={}; nv=0; n1=0; n2=0
    for (m,Ms,V) in census(n):
        S=Skel(n,m,list(Ms),V)
        if not S.windows_ok(): continue
        nv+=1; key=(m,Ms,S.V[S.s]); g0.setdefault(key,[]).append((S.V[2],qval(S),S.u))
        if moh10(S):
            n1+=1; g1.setdefault(key,[]).append((S.V[2],qval(S),S.u))
            if star_congruence(S):
                n2+=1; g2.setdefault(key,[]).append((S.V[2],qval(S),S.u))
    if not nv: continue
    alive=0
    for key,items in g2.items():
        u=int(items[0][2])
        if knap_alive([(v,q) for (v,q,_) in items], u): alive+=1
    T[0]+=nv; T[1]+=len(g0); T[2]+=len(g1); T[3]+=len(g2); T[4]+=alive; T[5]+=n1; T[6]+=n2
    print("   %5d %10d %10d %10d %10d %10d %10d %10d   %.0fs" %
          (n,nv,len(g0),len(g1),len(g2),alive,n1,n2,time.time()-t0)); sys.stdout.flush()
print("   TOTAL: V-skel %d ; groups %d -> (10) %d -> (10)_1 %d -> knapsack-alive %d"
      % (T[0],T[1],T[2],T[3],T[4]))
print("   V-assignments: %d -> (10) %d -> (10)_1 %d" % (T[0],T[5],T[6]))
