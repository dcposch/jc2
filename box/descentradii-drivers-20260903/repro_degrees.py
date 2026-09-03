#!/usr/bin/env python3
"""M2-DESCENT step (1b): reproduce the 48<=D<=120 group counts under M_2 > m,
and print the D=105 trio with its descent data."""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from moh_skeleton_full import Skel, census, uni_hits, mixed_hit

def groups_m2(n, filt):
    G = {}
    for (m, Ms, V) in census(n, Kmin=16, full=True):
        S = Skel(n, m, list(Ms), V)
        if filt and not (S.M[2] > S.m): continue
        G.setdefault((m, Ms, S.V[S.s]), []).append((S.V[2], S.q(), S.u))
    return G

print("   %5s %7s %7s %9s %11s" % ("D","groups","M2>m","aliveN>=6","alive[6,16]"))
tg=tf=ta=tb=0
for n in range(48, 121):
    G0 = groups_m2(n, False); G1 = groups_m2(n, True)
    a = sum(1 for k,v in G1.items() if uni_hits(v, 6, None))
    b = sum(1 for k,v in G1.items() if mixed_hit(v, 6, 16)[0])
    tg+=len(G0); tf+=len(G1); ta+=a; tb+=b
    if len(G0):
        print("   %5d %7d %7d %9d %11d %s" % (n, len(G0), len(G1), a, b,
            "<- EMPTIED" if (len(G0) and not len(G1)) else ""))
print("   TOTAL %5d %7d %9d %11d" % (tg, tf, ta, tb))

print("\n== D = 105: the trio, full skeleton + descent data ==")
for (m, Ms, V) in census(105, Kmin=16, full=True):
    S = Skel(105, m, list(Ms), V)
    us = S.d[S.s] - S.V[S.s]
    Ns = sorted(uni_hits([(S.V[2], S.q(), S.u)], 6, 16))
    print("   m=%3d M=%s d=%s V=%s  delta=%s  u_s=%d  q=%s  u=%s  M_2>m:%s N=%s"
          % (m, [S.M[i] for i in range(1,S.s+1)], [S.d[i] for i in range(1,S.s+2)],
             {i:S.V[i] for i in range(2,S.s+2)},
             {i:str(S.delta[i]) for i in range(1,S.s+1)}, us, S.q(), S.u,
             S.M[2] > S.m, Ns))
