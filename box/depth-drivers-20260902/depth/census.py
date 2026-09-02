#!/usr/bin/env python3
"""
MOH-SKELETON CENSUS.

Enumerate the *numerical characteristic skeletons* of a degree-minimal Jacobian
pair, using only conditions read firsthand in refs/moh1983 (+ GGV Cor 6.6).

Data: (n, m, [M_1=-m, M_2, ..., M_s]) with the divisor chain
      d_1 = n,  d_2 = gcd(n,m) = K,  d_{i+1} = gcd(d_i, M_i)   (i >= 2)
Conditions (source in comments):
  C1  n = deg g = deg_y g,  m = deg f < n,  M_1 = -m           [Moh, search (1)]
  C2  M_s = n-2                                                [Moh Lem 5.3 + Prop 5.4
                                                                at degree-minimality]
  C3  d_r = gcd{n, M_1, ..., M_{r-1}}, strictly decreasing     [Moh, search (5)]
  C4  d_s >= 4                                                 [Moh Cor 6.1]
  C5  s >= 3                                                   [Moh Prop 5.5]
  C6  m = K d, n = K e, gcd(d,e)=1, 2 <= d < e                 [(LF)+(MIN); Moh Prop 5.4]
  C7  K = gcd(m,n) >= 16                                       [GGV Cor 6.6; NOT in Moh]
  C8  -m < M_2 < M_3 < ... < M_s = n-2                         [Moh sec 2 expansion]
"""
import sys, math
from math import gcd
from functools import lru_cache

def divisor_chains(K, floor=4):
    """all chains K = c_0 > c_1 > ... > c_k >= floor with c_{i+1} | c_i, k>=1."""
    out = []
    def rec(cur, chain):
        for dd in range(floor, cur):
            if cur % dd == 0:
                out.append(chain + [dd])
                rec(dd, chain + [dd])
    rec(K, [])
    return out

def skeletons(n, require_K16=True, count_only=True):
    """yield / count skeletons for a given n."""
    total = 0
    rows = []
    Kmin = 16 if require_K16 else 1
    for K in range(Kmin, n//3 + 1):
        if n % K: continue
        e = n // K
        if e < 3: continue
        for d in range(2, e):
            if gcd(d, e) != 1: continue
            m = K * d
            if m >= n: continue
            # chains  d_2 = K > d_3 > ... > d_s >= 4
            for chain in divisor_chains(K, 4):
                s = 2 + len(chain)          # d_2..d_s has s-1 entries
                if s < 3: continue
                # need exponents M_2..M_s ; M_s = n-2 with gcd(d_s, M_s) = d_{s+1}
                ds = chain[-1]
                # exponent M_i must satisfy gcd(d_i, M_i) = d_{i+1}
                # d_2=K -> M_2 ; d_3=chain[1] -> M_3 ; ... ; d_s -> M_s = n-2
                dlist = [K] + chain          # d_2 .. d_s   (len = s-1)
                tgt   = chain + [gcd(ds, n-2)]   # d_3 .. d_{s+1}
                # last exponent is pinned to n-2 : consistency check
                if gcd(ds, n-2) != tgt[-1]: continue
                # enumerate M_2 .. M_{s-1} increasing in (-m, n-2)
                cnt = _count_exponents(dlist[:-1], tgt[:-1], -m, n-2)
                if cnt:
                    total += cnt
                    if not count_only:
                        rows.append((n, m, K, tuple(dlist), cnt))
    return (total, rows)

def _count_exponents(ds, tg, lo, hi):
    """# of strictly increasing (M_2..M_{s-1}) in (lo,hi) with gcd(ds[i],M)=tg[i].
       ds/tg are aligned lists for the FREE exponents only."""
    if not ds: return 1
    # dynamic programming over positions
    ways = 0
    def rec(i, start):
        nonlocal ways
        if i == len(ds):
            ways += 1
            return
        for M in range(start+1, hi):
            if gcd(ds[i], M) == tg[i]:
                rec(i+1, M)
    rec(0, lo)
    return ways

if __name__ == "__main__":
    # ---- positive control: Moh's four surviving degree pairs -----------------
    print("== positive control: Moh 1983 sec.6 table (n, m=-M_1, M_2, M_3, M_4) ==")
    moh = [(64,48,[52,62,63]), (84,56,[64,82,83]), (75,50,[55,73]), (99,66,[77,97])]
    for (n,m,Ms) in moh:
        full = [-m] + Ms
        d = [n]
        for M in full:
            d.append(gcd(d[-1], M))
        K = gcd(n,m)
        # effective pairs: drop a terminal M = n-1
        eff = [M for M in full if M != n-1]
        s = len(eff)
        print(f"  n={n:3d} m={m:3d} K=gcd={K:3d} e=n/K={n//K} d=m/K={m//K} "
              f"d-chain={d} s_eff={s} M_s={eff[-1]} (n-2={n-2}) "
              f"K>=16:{K>=16} d_s={d[len(eff)-1]}")
    print()
    print("== skeleton census (with GGV K>=16) ==")
    print("   n : #skeletons   cumulative")
    cum = 0
    for n in range(48, 241):
        t,_ = skeletons(n)
        cum += t
        if t: print(f"  {n:4d} : {t:8d}   {cum:10d}")
