#!/usr/bin/env python3
"""Moh's search conditions (8)-(11) (moh.txt p.201, OCR-damaged) RECONSTRUCTED and
   CALIBRATED against his published n<=100 table.

   (8) L_j := lcm of the reduced denominators of delta_s, ..., delta_{j+1};
       Delta_j := reduced denominator of L_j * delta_j.
   (10) [factor pi - alpha of p(pi) with alpha != 0]
            Delta_j * V_j  <=  v_j = V_{j+1} d_j / d_{j+1}      (the Def 5.1(2) window top)
   (11) [factor pi, i.e. alpha = 0]  a weaker alternative, not reconstructed.

   Calibration: Moh states his computer program at n <= 100 returns exactly
   (64,48), (84,56) [two V-rows], (75,50), (99,66).  We measure how close (10)
   alone comes."""
import sys, os
from fractions import Fraction as F
from math import gcd, lcm
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moh_skeleton_N import Skel, census, MOH_SURVIVORS

def deltas(S): return {i: S.delta[i] for i in range(1, S.s+1)}

def Delta(S, j):
    """Delta_j: reduced denominator of L_j*delta_j, L_j = lcm(den delta_s..den delta_{j+1})."""
    L = 1
    for i in range(j+1, S.s+1): L = lcm(L, S.delta[i].denominator)
    return (L*S.delta[j]).denominator

def moh10(S, upto=None):
    """(10) for j = 2..s-1 (V_1 does not exist; Delta_s = 1 is vacuous)."""
    for j in range(2, S.s):
        v = F(S.V[j+1]*S.d[j], S.d[j+1])
        if Delta(S, j)*S.V[j] > v: return False
    return True

def moh10_full(S):
    """(10) also applied at j = 1 with the 'window top' read as v_1 = V_2 d_1/d_2."""
    if not moh10(S): return False
    v1 = F(S.V[2]*S.d[1], S.d[2])
    return Delta(S,1)*1 <= v1

if __name__ == "__main__":
    print("== A. Moh's published survivors vs reconstructed (10) ==")
    print("   %-22s %-26s %-22s %s" % ("row","deltas (d_s..d_1)","Delta_j (j=2..s-1)","(10)?"))
    for (n,m,Ms,Vs,lab,_) in MOH_SURVIVORS:
        S = Skel(n,m,list(Ms),Vs)
        dl = [str(S.delta[i]) for i in range(S.s,0,-1)]
        Dj = [(j, Delta(S,j), S.V[j], F(S.V[j+1]*S.d[j],S.d[j+1])) for j in range(2,S.s)]
        print("   %-22s %-26s %-22s %s" % (lab, ",".join(dl),
              " ".join("D%d=%d V=%d<=%s"%(j,D,V,v) for (j,D,V,v) in Dj), moh10(S)))

    print("\n== B. census at 48 <= n <= 100 : effect of (10) ==")
    print("   %5s %10s %10s %10s %10s" % ("n","V-skel","pass(10)","groups","grp pass"))
    T=[0,0,0,0]; survivors=[]
    for n in range(48, 101):
        c=p=0; grp=set(); grpp=set()
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok(): continue
            c += 1; grp.add((m,Ms,S.V[S.s]))
            if moh10(S):
                p += 1; grpp.add((m,Ms,S.V[S.s]))
                survivors.append((n,m,Ms,tuple(sorted(V.items()))))
        T[0]+=c; T[1]+=p; T[2]+=len(grp); T[3]+=len(grpp)
        if c: print("   %5d %10d %10d %10d %10d" % (n,c,p,len(grp),len(grpp)))
    print("   TOTAL 48..100: V-skeletons %d -> %d ; groups %d -> %d" % tuple(T))
    print("\n   surviving (n,m,M_*) sets after (10), n<=100:")
    ss = sorted(set((n,m,Ms) for (n,m,Ms,_) in survivors))
    for r in ss: print("      n=%d m=%d M=%s" % r)
    print("   (%d distinct (n,m,M); %d V-skeletons)" % (len(ss), len(survivors)))

# ------------------------------------------------------------------ level-1 form
def star_congruence(S):
    """(10)_1  [this lane, = Moh (8)-(11) at r = 1 combined with D1-STAR(d)].
       The order-Delta_1 automorphism x^{1/Delta_1} -> omega x^{1/Delta_1} fixes
       sigma_1 (its exponents have denominators dividing L_1, by the characteristic-
       exponent structure) and multiplies pi by a primitive Delta_1-th root of unity.
       So the root set of p_1 = g_sigma1 is invariant under that multiplication.
       By Moh Prop 4.6 (r=1) / D1-STAR(d) those a_1 roots are SIMPLE, so pi = 0 is a
       root at most once:   a_1 = e V_2  ==  0 or 1  (mod Delta_1)."""
    D1 = Delta(S, 1); a1 = S.e*S.V[2]
    return (a1 % D1) in (0, 1)

def moh_all(S):
    return moh10(S) and star_congruence(S)
