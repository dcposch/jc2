#!/usr/bin/env python3
"""D=48 (UNI) survivors: N = k V_2 q integral in [6,16] with k V_2 <= u,
   i.e. ALL bottom-major discs carry the same lower-V datum (one Galois orbit)."""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moh_skeleton_N import Skel, census
from d1floor import qval

D=48; Nlo,Nhi=6,16
rows=[]
for (m, Ms, V) in census(D):
    S = Skel(D, m, list(Ms), V)
    if not S.windows_ok(): continue
    q = qval(S); v = S.V[2]; u = int(S.u)
    for k in range(1, u//v + 1):
        N = k*v*q
        if N.denominator==1 and Nlo <= N <= Nhi:
            dens = max(S.delta[r].denominator for r in range(1, S.s+1))
            rows.append((3*v, k, dens, S.s, int(N), m, Ms, S.V[S.s],
                         tuple(S.V[i] for i in range(2,S.s+1)), q, S.delta[1], S.delta[2], u))
print("== D=48 (UNI)-realisable skeletons, N in [6,16] : %d ==" % len(rows))
print("   %-4s %-3s %-4s %-2s %-3s %-16s %-3s %-12s %-8s %-9s %-9s" %
      ("a_1","k","den","s","N","M_2..M_s","V_s","V_2..V_s","q","delta_1","delta_2"))
seen=set()
for r in sorted(rows)[:40]:
    a1,k,dens,s,N,m,Ms,Vs,Vasg,q,d1,d2,u = r
    print("   %-4d %-3d %-4d %-2d %-3d %-16s %-3d %-12s %-8s %-9s %-9s  (b_1=%d, u=%d, k V_2=%d)" %
          (a1,k,dens,s,N,str(list(Ms)),Vs,str(list(Vasg)),q,d1,d2,2*(a1//3),u,k*(a1//3)))
