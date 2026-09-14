#!/usr/bin/env python3
"""(1)-(7) and (1)-(13)-admissible Moh skeletons at (n,m) = (99,66).  Sec 0.3."""
import sys
sys.path.insert(0, '/home/ubuntu/jc2/box')
from moh_skeleton_full import census, Skel
a7 = [r for r in census(99, Kmin=2) if r[0] == 66]
a13 = [r for r in census(99, Kmin=2, full=True) if r[0] == 66]
print("n=99, m=66 :  (1)-(7) V-assignments %d ;  (1)-(13) survivors %d" % (len(a7), len(a13)))
for (m, Ms, V) in sorted(a13, key=lambda r: (r[1], sorted(r[2].items()))):
    S = Skel(99, m, list(Ms), V)
    ds, Vs = S.d[S.s], S.V[S.s]
    print("   M_2..M_s=%-12s V=%-16s d=%-22s u_s=d_s-V_s=%d  delta=%s"
          % (list(Ms), {i: V[i] for i in sorted(V)},
             {i: S.d[i] for i in sorted(S.d)}, ds - Vs,
             {i: str(S.delta[i]) for i in sorted(S.delta)}))
S = Skel(99, 66, [77, 97], {3: 8, 2: 8})
print("\np.202 (99,66) row: M=%s d=%s V=%s ; delta_3,delta_2,delta_1 = %s,%s,%s"
      % ({i: S.M[i] for i in sorted(S.M)}, {i: S.d[i] for i in sorted(S.d)},
         {i: S.V[i] for i in sorted(S.V)}, S.delta[3], S.delta[2], S.delta[1]))
print("   s=%d d_s=%d v_s=V_s=%d u_s=%d n/d_s=%d m/d_s=%d  (p.202 prints delta_2=1/3, delta_1=4/9)"
      % (S.s, S.d[S.s], S.V[S.s], S.d[S.s]-S.V[S.s], 99//S.d[S.s], 66//S.d[S.s]))
