#!/usr/bin/env python3
"""(10)_1 ALONE (both branches alpha != 0 and alpha = 0 handled: a_1 = 0 or 1 mod Delta_1),
   with no reliance on the OCR-damaged j>=2 clause."""
import sys, os, time
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moh_skeleton_N import Skel, census
from d1floor import qval
from mohcond import star_congruence, moh10
Nlo,Nhi=6,16
def alive(items,u,CAP=200000):
    cand=sorted(set((v,q) for (v,q) in items if v*q<=Nhi)); reach={0:{F(0)}}
    for tv in range(0,u+1):
        if tv not in reach: continue
        for s0 in list(reach[tv]):
            for (v,q) in cand:
                if tv+v>u: continue
                s1=s0+v*q
                if s1>Nhi: continue
                t=reach.setdefault(tv+v,set())
                if len(t)>=CAP: return True
                t.add(s1)
                if s1.denominator==1 and Nlo<=s1<=Nhi: return True
    return False
print("== (10)_1 ALONE, D in [48,120] ==")
print("   %5s %10s %10s %10s %10s %10s" % ("D","V-skel","V:(10)_1","groups","g:(10)_1","g:+knap"))
T=[0]*5; empty=[]
for n in range(48,121):
    t0=time.time(); g0={}; g1={}; nv=0; n1=0
    for (m,Ms,V) in census(n):
        S=Skel(n,m,list(Ms),V)
        if not S.windows_ok(): continue
        nv+=1; key=(m,Ms,S.V[S.s]); g0.setdefault(key,[]).append(S)
        if star_congruence(S): n1+=1; g1.setdefault(key,[]).append(S)
    if not nv: continue
    a=sum(1 for k,it in g1.items() if alive([(S.V[2],qval(S)) for S in it],int(it[0].u)))
    T[0]+=nv;T[1]+=n1;T[2]+=len(g0);T[3]+=len(g1);T[4]+=a
    if a==0: empty.append(n)
    print("   %5d %10d %10d %10d %10d %10d  %.0fs" % (n,nv,n1,len(g0),len(g1),a,time.time()-t0))
    sys.stdout.flush()
print("   TOTAL: V-skel %d -> %d (%.2f%% killed); groups %d -> %d -> knapsack-alive %d"
      % (T[0],T[1],100.0*(1-T[1]/T[0]),T[2],T[3],T[4]))
print("   degrees EMPTY under (10)_1 + knapsack: %s" % (empty if empty else "NONE"))
