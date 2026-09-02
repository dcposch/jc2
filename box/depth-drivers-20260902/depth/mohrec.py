#!/usr/bin/env python3
"""
MOH RECURSION -- exact reproduction of Definition 5.1(3) / Proposition 5.3
(Moh 1983, J. reine angew. Math. 340, pp.179-180; read from the page image,
 refs/moh1983...pdf sha256 6c8847a8...).

   delta_i = 1 -  (n - M_i)     prod_{j=i+1}^{s} [ V_j (n - M_j)     - d_j ]
                 -----------------------------------------------------------
                 (n - M_s - 1)  prod_{j=i+1}^{s} [ V_j (n - M_{j-1}) - d_j ]

   window (Def 5.1(2) / Prop 5.3):   V_{i+1} d_i / d_{i+1}  >=  V_i  >  d_i/(n-M_i),
                                     V_{s+1} = d_{s+1}.

POSITIVE CONTROL: reproduce the delta columns of Moh's sec.6 table.
"""
from fractions import Fraction as F
from math import gcd

def dchain(n, Ms):
    d=[n]
    for M in Ms: d.append(gcd(d[-1],M))
    return d                      # d[0]=d_1=n, d[i]=d_{i+1}

def delta(i, n, M, d, V):
    """M: dict i->M_i (1-based); d: dict i->d_i ; V: dict i->V_i ; s = max index of M"""
    s = max(M)
    num = F(n - M[i]); den = F(n - M[s] - 1)
    for j in range(i+1, s+1):
        num *= (V[j]*(n - M[j]) - d[j])
        den *= (V[j]*(n - M[j-1]) - d[j])
    return 1 - num/den

def window(i, n, M, d, V):
    lo = F(d[i], n - M[i])                    # strict lower bound
    hi = F(V[i+1]*d[i], d[i+1])               # V_i <= hi
    return lo, hi

def run(n, m, Ms, Vs, label):
    """Ms = [M_2,...,M_s] (M_1 = -m); Vs = {i: V_i} for i=2..s ; V_{s+1}=d_{s+1}"""
    full = [-m] + Ms
    s = len(full)
    M = {i+1: full[i] for i in range(s)}
    dl = dchain(n, full)                       # dl[k] = d_{k+1}
    d  = {i+1: dl[i] for i in range(len(dl))}
    V  = dict(Vs); V[s+1] = d[s+1]
    print(f"  {label}: n={n} m={m} M={[M[i] for i in range(1,s+1)]} "
          f"d={[d[i] for i in range(1,s+2)]} V={[V[i] for i in range(2,s+2)]}")
    ok=True
    for i in range(2, s+1):
        lo,hi = window(i,n,M,d,V)
        good = (V[i] > lo) and (V[i] <= hi)
        ok &= good
        print(f"     window V_{i}: {lo} < V_{i}={V[i]} <= {hi}   {'ok' if good else 'VIOLATED'}")
    for i in range(s,0,-1):
        print(f"     delta_{i} = {delta(i,n,M,d,V)}")
    return ok

if __name__=="__main__":
    print("== reproduction of Moh 1983 sec.6 table (delta columns) ==")
    print("   published: n=64: d2=1/4, d1=9/16 | n=84: 2/7,16/21 [1/4,7/12] | n=99: 1/3, 4/9")
    run(64,48,[52,62],{3:3,2:3},"n=64")
    run(84,56,[64,82],{3:3,2:2},"n=84 (M_2=64)")
    run(84,56,[72,82],{3:3,2:5},"n=84 (M_2=72)")
    run(99,66,[77,97],{3:8,2:8},"n=99")
    run(75,50,[55,73],{3:4,2:3},"n=75 (V_2=3, delta illegible in OCR)")
    run(75,50,[55,73],{3:4,2:2},"n=75 (V_2=2)")
    print()
    print("== size of the free datum per step (Def 5.1(2) window width) ==")
    print("   at the last step i=s with M_s=n-2:  d_s/2 < V_s <= d_s  ->  ceil(d_s/2) choices")
    for ds in (4,5,8,11,16,25,33):
        print(f"     d_s={ds:3d} -> V_s in ({F(ds,2)}, {ds}]  : {ds - (ds//2)} choices")
