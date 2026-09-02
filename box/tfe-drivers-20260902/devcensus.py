#!/usr/bin/env python3
"""Which bottom-star data (d, e, V_2) occur in the Moh census?  The bottom disc's
leading polynomials p_g, p_f depend on the skeleton ONLY through (d, e, V_2)
(degrees a_1 = e V_2, b_1 = d V_2) -- so the star problem is indexed by this triple."""
import sys
from fractions import Fraction as F
sys.path.insert(0,'/Users/dc/code/math/jc2/box')
from moh_skeleton_N import Skel, census

def qval(S): return (1 - S.delta[1]) * F(S.dd*S.e, S.dd+S.e)
def hits(S, Nlo=6, Nhi=None):
    q = qval(S); v = S.V[2]; u = S.u; out=[]
    for k in range(1, int(u//v)+1):
        val = k*v*q
        if val.denominator==1 and val>=Nlo and (Nhi is None or val<=Nhi): out.append(int(val))
    return out

nmax = int(sys.argv[1]) if len(sys.argv)>1 else 120
allt = {}; survt = {}
for n in range(48, nmax+1):
    for (m, Ms, V) in census(n):
        S = Skel(n, m, list(Ms), V)
        if not S.windows_ok(): continue
        key = (S.dd, S.e, S.V[2])
        allt[key] = allt.get(key,0)+1
        if hits(S): survt[key] = survt.get(key,0)+1
print("D in [48,%d]" % nmax)
print("  distinct (d,e,V_2) over ALL admissible V-skeletons: %d" % len(allt))
print("  distinct (d,e,V_2) over those admitting an integer N>=6 under (UNI): %d" % len(survt))
print("\n  %-12s %-10s %-10s %-8s %-8s" % ("(d,e,V_2)","a_1=eV_2","b_1=dV_2","#all","#surv"))
for k in sorted(survt, key=lambda z:(z[0]*z[2]+z[1]*z[2], z)):
    d,e,V = k
    print("  %-12s %-10d %-10d %-8d %-8d" % (str(k), e*V, d*V, allt[k], survt[k]))
print("\n  (d,e) pairs occurring:", sorted(set((d,e) for (d,e,V) in allt)))
print("  V_2 range per (d,e):")
for (d,e) in sorted(set((d,e) for (d,e,V) in allt)):
    vs = sorted(V for (dd,ee,V) in allt if (dd,ee)==(d,e))
    vss = sorted(V for (dd,ee,V) in survt if (dd,ee)==(d,e))
    print("    (%d,%d): all V_2 in %s ; surviving V_2 in %s" % (d,e,vs,vss))
