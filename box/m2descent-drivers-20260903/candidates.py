#!/usr/bin/env python3
"""M2-DESCENT (1d): the candidate (1)-(13) skeletons with M_2 <= m that survive
every other necessary condition the campaign owns (integral pinned N >= 6)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from moh_skeleton_full import Skel, census, uni_hits, mixed_hit
rows=[]
for n in range(1,101):
    for (m,Ms,V) in census(n, Kmin=2, full=True):
        rows.append(Skel(n,m,list(Ms),V))
le=[S for S in rows if S.M[2] <= S.m]
print("  (1)-(13) rows at n<=100 with M_2 <= m :", len(le), " classes:", len(set((S.n,S.m) for S in le)))
liveU=[S for S in le if uni_hits([(S.V[2],S.q(),S.u)],6,None)]
print("  ... with an integral pinned N >= 6 (UNI)     :", len(liveU),
      " classes:", len(set((S.n,S.m) for S in liveU)))
us1=[S for S in liveU if S.d[S.s]-S.V[S.s]==1]
print("  ... of those with u_s = 1 (Prop 6.3 applies) :", len(us1))
print("\n  the smallest six by (n,m):")
for S in sorted(liveU, key=lambda T:(T.n,T.m,T.M[2]))[:6]:
    print("    n=%3d m=%3d M=%s V=%s u_s=%d q=%s N=%s"
          % (S.n,S.m,[S.M[i] for i in range(1,S.s+1)],{i:S.V[i] for i in range(2,S.s+1)},
             S.d[S.s]-S.V[S.s], S.q(), sorted(uni_hits([(S.V[2],S.q(),S.u)],6,None))))
# D = 105
print("\n  at D = 105 (the trio):")
for (m,Ms,V) in census(105, Kmin=16, full=True):
    S=Skel(105,m,list(Ms),V)
    N=sorted(uni_hits([(S.V[2],S.q(),S.u)],6,16))
    if N and S.M[2]<=S.m:
        print("    m=%d M=%s V=%s M_2=%d <= m=%d  u_s=%d  N=%s"
              % (m,[S.M[i] for i in range(1,S.s+1)],{i:S.V[i] for i in range(2,S.s+1)},
                 S.M[2],S.m,S.d[S.s]-S.V[S.s],N))
