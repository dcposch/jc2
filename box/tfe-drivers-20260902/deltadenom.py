#!/usr/bin/env python3
"""Denominators of the tower radii delta_i.  delta_i is by Moh's Prop 5.3 the MINIMUM of
ord_t(tau - tau') over the roots of g * prod T_j^psi in D_i, so its reduced denominator
must divide the lcm of the ramification indices of the branches involved -- an arithmetic
constraint on Def 5.1(3) that the numerical census does not impose.  Measured here."""
import sys
from fractions import Fraction as F
sys.path.insert(0,'/Users/dc/code/math/jc2/box')
from moh_skeleton_N import Skel, census, MOH_SURVIVORS

def qv(S): return (1 - S.delta[1]) * F(S.dd*S.e, S.dd+S.e)
def hits(S):
    q=qv(S); v=S.V[2]; u=S.u
    return [int(k*v*q) for k in range(1,int(u//v)+1) if (k*v*q).denominator==1 and k*v*q>=6]

nmax = int(sys.argv[1]) if len(sys.argv)>1 else 120
tot=0; d1n=0; d1a=0; surv=0; s1n=0
rows={}
for n in range(48, nmax+1):
    for (m, Ms, V) in census(n):
        S = Skel(n, m, list(Ms), V)
        if not S.windows_ok(): continue
        tot += 1
        A1 = S.delta[1].denominator
        ok1 = (n % A1 == 0)
        okAny = (n % A1 == 0) or (m % A1 == 0)
        d1n += ok1; d1a += okAny
        if hits(S):
            surv += 1; s1n += ok1
        rows.setdefault(n, [0,0,0,0])
        rows[n][0]+=1; rows[n][1]+=ok1
        if hits(S): rows[n][2]+=1; rows[n][3]+=ok1
print("D in [48,%d]: %d admissible V-skeletons" % (nmax, tot))
print("  denom(delta_1) divides n : %d (%.2f%%)" % (d1n, 100.0*d1n/tot))
print("  denom(delta_1) divides n or m : %d (%.2f%%)" % (d1a, 100.0*d1a/tot))
print("  of the %d admitting an integer N >= 6 under (UNI): denom(delta_1) | n on %d (%.2f%%)"
      % (surv, s1n, 100.0*s1n/max(1,surv)))
print("\n  Moh's own six published rows:")
print("   %-24s %-9s %-9s %-8s %-8s" % ("row","delta_1","denom","n","denom | n"))
for (n,m,Ms,Vs,lab,_) in MOH_SURVIVORS:
    S = Skel(n,m,list(Ms),Vs); A1=S.delta[1].denominator
    print("   %-24s %-9s %-9d %-8d %-8s" % (lab, S.delta[1], A1, n, n % A1 == 0))
print("\n  per-degree (D, #skel, denom|n, #surv, surv&denom|n):")
for n in sorted(rows):
    if n in (105,108,112,117,120) or n % 20 == 0:
        print("   %5d %8d %8d %8d %8d" % (n, rows[n][0], rows[n][1], rows[n][2], rows[n][3]))
