#!/usr/bin/env python3
"""PS-GROWTH on the D = 105 trio, and the size of the FORCED-VANISHING range
across the census.

For a Keller pair in Moh's gauge with a tower, D1-PIN gives the per-root frontier
contribution at a bottom-major disc B:
      c(B) = (1 - delta_1(B)) d/(d+e) = q(B)/e ,   q(B) = (1-delta_1)de/(d+e) ,
and DETECTOR-NULL/MINOR-FRONTIER give 0 at every other root.  Hence
      cmax = max_B q(B)/e ,   and  (PS-3)  deg_x R_k <= (k+1) cmax - 1 .
Consequences, per group:
      R_k == 0                for all k <= K0 := ceil(1/cmax) - 2
      R_k is x-INDEPENDENT    for all k <= K1 := ceil(2/cmax) - 2
This file prints K0, K1 for the D = 105 trio and measures how K0 grows with D over
the (1)-(13) census (the question "is PS-GROWTH a ceiling route").
"""
import sys
from fractions import Fraction as F
from math import ceil
sys.path.insert(0, '/home/ubuntu/jc2/box')
from moh_skeleton_N import Skel, census

def qval(S): return (1 - S.delta[1]) * F(S.dd*S.e, S.dd+S.e)
def ranges(cmax):
    """largest k with (k+1)cmax < 1  and  largest k with (k+1)cmax - 1 < 1."""
    K0 = -1; K1 = -1
    k = 0
    while F(k+1)*cmax < 1: K0 = k; k += 1
    k = 0
    while F(k+1)*cmax - 1 < 1: K1 = k; k += 1
    return K0, K1

TRIO = [(70, [28, 103], {2:1, 3:5}), (70, [28, 103], {2:1, 3:6}),
        (70, [40, 103], {2:1, 3:4})]

if __name__ == "__main__":
    print("trio105.py -- PS-GROWTH forced-vanishing ranges")
    print("="*96)
    print("\n## the D = 105 trio (V_2 = 1 throughout; the MAJOR-MULT hostages)")
    print("%-34s %-7s %-8s %-6s %-6s %-8s %-5s %-5s %-6s" %
          ("group", "q", "delta_1", "d", "e", "cmax=q/e", "K0", "K1", "u"))
    for (m, Ms, V) in TRIO:
        S = Skel(105, m, list(Ms), V)
        q = qval(S); cm = q/S.e; K0, K1 = ranges(cm)
        print("%-34s %-7s %-8s %-6s %-6s %-8s %-5s %-5s %-6s" %
              ("m=%d M=%s V=%s" % (m, Ms, sorted(V.items())), q, S.delta[1],
               S.dd, S.e, cm, K0, K1, S.u))
        print("     R_k == 0 for k = 0..%d ; R_k in C[c_2] for k = %d..%d ;"
              "  first k with deg_x R_k possibly > 0 : %d" % (K0, K0+1, K1, K1+1))
        print("     trivial (degree) vanishing range: k*m <= n-2  <=>  k <= %d"
              % ((105-2)//m))
        print("     bottom star (d,e,V_2) = (%d,%d,%d) ; a_1 = %d, b_1 = %d ; "
              "N = k_B*q for k_B = #bottom discs" % (S.dd, S.e, S.V[2], S.a[1], S.b[1]))
    print("\n## how K0 grows with D over the (1)-(13) census (single-profile / (UNI) reading:")
    print("   cmax = q, i.e. all bottom discs share one profile, so cmax = q/e)")
    print("%-6s %-8s %-10s %-10s %-10s %-10s" %
          ("D", "#groups", "max K0", "median K0", "max K1", "#K0>=2"))
    import statistics
    for D in [48, 60, 72, 84, 96, 105, 108, 112, 117, 120]:
        K0s = []
        for (m, Ms, V) in census(D, Kmin=1):
            S = Skel(D, m, list(Ms), V)
            if not S.windows_ok(): continue
            cm = qval(S)/S.e
            if cm <= 0: continue
            K0, K1 = ranges(cm)
            K0s.append((K0, K1))
        if not K0s: print("%-6s %-8s (no admissible skeleton)" % (D, 0)); continue
        print("%-6s %-8s %-10s %-10s %-10s %-10s" %
              (D, len(K0s), max(k for k,_ in K0s),
               statistics.median([k for k,_ in K0s]),
               max(k for _,k in K0s), sum(1 for k,_ in K0s if k >= 2)))
