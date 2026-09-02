#!/usr/bin/env python3
"""D=48 skeletons passing Moh (10) AND the pinned-N knapsack at N in [6,16]."""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moh_skeleton_N import Skel, census
from d1floor import qval
from mohcond import moh10, Delta

D=48; Nlo,Nhi=6,16
groups={}
for (m,Ms,V) in census(D):
    S=Skel(D,m,list(Ms),V)
    if not S.windows_ok(): continue
    if not moh10(S): continue
    groups.setdefault((m,Ms,S.V[S.s]),[]).append(S)
print("== D=48, groups surviving Moh (10): %d  (V-assignments %d) ==" %
      (len(groups), sum(len(v) for v in groups.values())))

def knap(items,u):
    cand=sorted(set((S.V[2],qval(S)) for S in items if S.V[2]*qval(S)<=Nhi))
    reach={0:{F(0):()}}; sols={}
    for tv in range(0,u+1):
        if tv not in reach: continue
        for s0,path in list(reach[tv].items()):
            for (v,q) in cand:
                if tv+v>u: continue
                s1=s0+v*q
                if s1>Nhi: continue
                tgt=reach.setdefault(tv+v,{})
                if s1 not in tgt: tgt[s1]=path+((v,q),)
                if s1.denominator==1 and Nlo<=s1<=Nhi and int(s1) not in sols: sols[int(s1)]=tgt[s1]
    return sols

print("\n   %-16s %-3s %-3s %-8s %-9s %-9s %-4s %-4s %-4s %-3s %s" %
      ("M_2..M_s","Vs","s","q(V_2=?)","delta_1","delta_2","a_1","b_1","u*e","D2","N reachable"))
rows=[]
for key in sorted(groups):
    m,Ms,Vs=key; items=groups[key]; u=int(items[0].u)
    sols=knap(items,u)
    if not sols: continue
    used=set()
    for N,p in sols.items():
        for vq in p: used.add(vq)
    for S in sorted(items,key=lambda S:(S.V[2],qval(S))):
        if (S.V[2],qval(S)) not in used: continue
        rows.append((3*S.V[2],S.s,max(S.delta[r].denominator for r in range(1,S.s+1)),
                     min(sols),len(sols[min(sols)]),key,tuple(S.V[i] for i in range(2,S.s+1)),S,sols))
        print("   %-16s %-3d %-3d %-8s %-9s %-9s %-4d %-4d %-4d %-3d %s   V=%s k=%d" %
              (str(list(Ms)),Vs,S.s,qval(S),S.delta[1],S.delta[2],3*S.V[2],2*S.V[2],
               int(S.u*S.e),Delta(S,2),sorted(sols),[S.V[i] for i in range(2,S.s+1)],
               len(sols[min(sols)])))
print("\n-- ranked by (u*e, a_1+b_1, tower length s, ramification denominator) --")
for r in sorted(rows,key=lambda r:(int(r[7].u*r[7].e), r[0], r[1], r[2]))[:10]:
    a1,s,den,N,k,key,V,S,sols=r
    print("   u*e=%-3d a_1=%-3d b_1=%-3d s=%d den=%-3d  m=%d M=%-14s V=%s  q=%s  d1=%s d2=%s  N=%s"
          % (int(S.u*S.e),a1,2*(a1//3),s,den,key[0],str(list(key[1])),list(V),qval(S),
             S.delta[1],S.delta[2],sorted(sols)))
