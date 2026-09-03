#!/usr/bin/env python3
"""RULE: delta_i' = (k+1) * Def5.1(3)(descended data, s'=2).
k = Jacobian exponent of the descended pair.
Verify all 10 printed p.207 rationals; emit G2/G3 values.
"""
from fractions import Fraction as F
from math import gcd

def def51(n, M, d, V, s, i):
    num = F(n - M[i]); den = F(n - M[s] - 1)
    for j in range(i+1, s+1):
        num *= (V[j]*(n - M[j]) - d[j])
        den *= (V[j]*(n - M[j-1]) - d[j])
    return 1 - num/den

rows = [
    # n, m, M2, V2, k, printed d2, printed d1, label
    (16, 12, 13, 3, 1, F(-1), F(1,4), "(16,12) from (64,48)"),
    (21, 14, 16, 2, 1, F(-1,2), F(7,6), "(21,14) V2=2 from (84,56) M2=64"),
    (21, 14, 18, 5, 1, F(-1), F(1,3), "(21,14) V2=5 from (84,56) M2=72"),
    (15, 10, 11, 3, 2, F(-1), F(1,2), "(15,10) V2=3 from (75,50)"),
    (15, 10, 11, 2, 2, F(-1), F(4,3), "(15,10) V2=2 from (75,50)"),
]
print("== PHI: delta' = (k+1) * Def 5.1(3) on descended (s'=2) ==")
ok = True
for n,m,M2,V2,k,pd2,pd1,lab in rows:
    d2 = gcd(n, m)
    M = {1: -m, 2: M2}
    d = {1: n, 2: d2, 3: gcd(d2, M2)}
    V = {2: V2, 3: d[3]}
    raw2, raw1 = def51(n,M,d,V,2,2), def51(n,M,d,V,2,1)
    p2, p1 = (k+1)*raw2, (k+1)*raw1
    match = (p2==pd2 and p1==pd1)
    ok = ok and match
    print("  %-44s k+1=%d  raw=(%s, %s)  Phi=(%s, %s)  printed=(%s, %s)  %s" %
          (lab, k+1, raw2, raw1, p2, p1, pd2, pd1, "MATCH" if match else "FAIL"))
print("  all 10 rationals MATCH:", ok)

print("\n== G2 / G3 under Phi ==")
for lab, n, m, M2, V2, k in [
    ("G2", 15, 10, 4, 1, 4),
    ("G3", 21, 14, 8, 1, 2),
]:
    d2 = gcd(n, m)
    M = {1: -m, 2: M2}
    d = {1: n, 2: d2, 3: gcd(d2, M2)}
    V = {2: V2, 3: d[3]}
    raw2, raw1 = def51(n,M,d,V,2,2), def51(n,M,d,V,2,1)
    print("  %s (n,m,M2,V2,d2,k)=(%d,%d,%d,%d,%d,%d)  raw=(%s,%s)  Phi delta2'=%s  delta1'=%s" %
          (lab, n,m,M2,V2,d2,k, raw2, raw1, (k+1)*raw2, (k+1)*raw1))
    u, v = d2-V2, V2
    print("      u=%d v=%d  u/(v+1)=%s  (majority-at-0 heuristic; not used for V2=1)" %
          (u, v, F(u, v+1)))
