#!/usr/bin/env python3
"""Evaluate candidate rules for delta' against the five u_s=1 p.207 rows
and against Def 5.1(3) on descended data.
"""
from fractions import Fraction as F
from math import gcd, lcm
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from moh_skeleton_full import Skel, MOH_TABLE

def delta_def51(n, M, d, V, s, i):
    """Def 5.1(3) p.179."""
    num = F(n - M[i]); den = F(n - M[s] - 1)
    for j in range(i+1, s+1):
        num *= (V[j]*(n-M[j]) - d[j]); den *= (V[j]*(n-M[j-1]) - d[j])
    return 1 - num/den

print("== Def 5.1(3) on ORIGINAL p.202 rows (control) ==")
for (n,m,Ms,Vs,lab,p2,p1,err) in MOH_TABLE:
    S = Skel(n,m,Ms,Vs)
    print("  %-22s  delta3=-1? %s  delta2=%s (printed %s)  delta1=%s (printed %s)%s" %
          (lab, S.delta[S.s]==-1, S.delta[2], p2, S.delta[1], p1,
           " ERRATUM" if err else ""))

print("\n== Def 5.1(3) on DESCENDED data with s'=2, M_s'=M2'  [does NOT match p.207] ==")
P207 = [
    # n', m', M2', V2', d2', printed d2, printed d1, parent label
    (16, 12, 13, 3, 4, F(-1), F(1,4), "(64,48)"),
    (21, 14, 16, 2, 7, F(-1,2), F(7,6), "(84,56) M2=64 V2=2"),
    (21, 14, 18, 5, 7, F(-1), F(1,3), "(84,56) M2=72 V2=5"),
    (15, 10, 11, 3, 5, F(-1), F(1,2), "(75,50) V2=3"),
    (15, 10, 11, 2, 5, F(-1), F(4,3), "(75,50) V2=2"),
]
for n,m,M2,V2,d2,pd2,pd1,lab in P207:
    M = {1: -m, 2: M2}
    d = {1: n, 2: d2, 3: gcd(d2, M2)}
    V = {2: V2, 3: d[3]}
    s = 2
    d2c = delta_def51(n, M, d, V, s, 2)
    d1c = delta_def51(n, M, d, V, s, 1)
    print("  %-28s  Def51 d2=%-8s printed %-8s  Def51 d1=%-8s printed %s" %
          (lab, d2c, pd2, d1c, pd1))

print("\n== Def 5.1(3) with fake M3=n-2, V3 varying (search integer V3 in window) ==")
for n,m,M2,V2,d2,pd2,pd1,lab in P207:
    M3 = n-2
    d1_, d2_, d3 = n, d2, gcd(d2, M2)
    d4 = gcd(d3, M3)
    hits = []
    for V3 in range(1, 20):
        M = {1:-m, 2:M2, 3:M3}
        d = {1:n, 2:d2_, 3:d3, 4:d4}
        V = {2:V2, 3:V3, 4:d4}
        try:
            d2c = delta_def51(n, M, d, V, 3, 2)
            d1c = delta_def51(n, M, d, V, 3, 1)
        except ZeroDivisionError:
            continue
        if d2c == pd2 and d1c == pd1:
            hits.append(('V3=%d BOTH' % V3, d2c, d1c))
        elif d2c == pd2:
            hits.append(('V3=%d d2-only' % V3, d2c, d1c))
        elif d1c == pd1:
            hits.append(('V3=%d d1-only' % V3, d2c, d1c))
    print("  %-28s  hits=%s" % (lab, hits[:6] if hits else "NONE"))

print("\n== shift delta_i' = delta_{i+1} of the PARENT ==")
for (n,m,Ms,Vs,lab,p2,p1,err) in MOH_TABLE:
    S = Skel(n,m,Ms,Vs)
    # parent delta_s=-1, delta_2, delta_1
    print("  %-22s  parent (ds,d2,d1)=(%s, %s, %s)  vs p.207" %
          (lab, S.delta[S.s], S.delta[2], S.delta[1]))

print("\n== parameter-change law  delta_new = v_s - u_s * delta_old  (parent) ==")
for (n,m,Ms,Vs,lab,p2,p1,err) in MOH_TABLE:
    S = Skel(n,m,Ms,Vs)
    us, vs = S.d[S.s]-S.V[S.s], S.V[S.s]
    n2 = vs - us*S.delta[S.s]
    n1from2 = vs - us*S.delta[2]
    n1from1 = vs - us*S.delta[1]
    print("  %-22s  u,v=%d,%d  v-u*(-1)=%s  v-u*d2=%s  v-u*d1=%s" %
          (lab, us, vs, n2, n1from2, n1from1))

print("\n== other simple Phi candidates ==")
print("  %-28s %8s %8s %8s %8s %8s %8s %8s %8s" %
      ("row","u/d2","v/d2","1/d2","1/e","(n-M2-1)^-1","k=v-u-1","printed d2","printed d1"))
for n,m,M2,V2,d2,pd2,pd1,lab in P207:
    u, v = d2-V2, V2
    e = n//d2
    k = v-u-1
    print("  %-28s %8s %8s %8s %8s %8s %8s %8s %8s" %
          (lab, F(u,d2), F(v,d2), F(1,d2), F(1,e), F(1, n-M2-1), k, pd2, pd1))

print("\n== Jacobian-modified Lemma 5.1: delta_s = -(k+1)/(n-M_s-1)  or -1/(n-M_s-k-1) ==")
for n,m,M2,V2,d2,pd2,pd1,lab in P207:
    # k from table: first three Jac X so k=1? NO: the table Jacobian is the DESCENDED jacobian
    # (16,12) X so k=1; (21,14) X k=1; (15,10) X^2 k=2
    k = 1 if n in (16,21) else 2
    a = -F(k+1, n-M2-1)
    b = -F(1, n-M2-k-1) if (n-M2-k-1) else 'div0'
    c = -F(k, n-M2-1)
    print("  %-28s  -(k+1)/(n-M2-1)=%s  -1/(n-M2-k-1)=%s  -k/(n-M2-1)=%s  printed d2=%s" %
          (lab, a, b, c, pd2))
