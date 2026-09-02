#!/usr/bin/env python3
"""MOH-SKELETON CENSUS v2 -- DP counting, growth measurement, depth statistics."""
from math import gcd, log2

def divisor_chains(K, floor=4):
    out=[]
    def rec(cur, ch):
        for dd in range(floor, cur):
            if cur % dd == 0:
                out.append(ch+[dd]); rec(dd, ch+[dd])
    rec(K,[]); return out

def count_increasing(dlist, tgt, lo, hi):
    """# strictly increasing tuples (M_2..M_{s-1}) with lo < M_2 < ... < hi and
       gcd(dlist[i], M_i) == tgt[i].  DP from the right."""
    L = len(dlist)
    if L == 0: return 1
    vals = list(range(lo+1, hi))
    ok = [[gcd(dlist[i], M) == tgt[i] for M in vals] for i in range(L)]
    # suffix DP: g[i][j] = #ways using positions i..L-1 with M_i = vals[j]
    nxt = [1 if ok[L-1][j] else 0 for j in range(len(vals))]
    for i in range(L-2, -1, -1):
        # suffix sums of nxt
        suf = [0]*(len(vals)+1)
        for j in range(len(vals)-1, -1, -1):
            suf[j] = suf[j+1] + nxt[j]
        cur = [ (suf[j+1] if ok[i][j] else 0) for j in range(len(vals)) ]
        nxt = cur
    return sum(nxt)

def census(n, Kmin=16):
    tot=0; maxs=0; rows=[]
    for K in range(Kmin, n//3+1):
        if n % K: continue
        e = n//K
        if e < 3: continue
        chains = divisor_chains(K,4)
        if not chains: continue
        for d in range(2, e):
            if gcd(d,e)!=1: continue
            m = K*d
            for ch in chains:
                s = 2 + len(ch)
                ds = ch[-1]
                dlist = ([K]+ch)[:-1]          # d_2..d_{s-1}
                tg    = ch                      # d_3..d_s
                c = count_increasing(dlist, tg, -m, n-2)
                if c:
                    tot += c; maxs=max(maxs,s)
                    rows.append((K,d,e,tuple([K]+ch),c))
    return tot, maxs, rows

if __name__=="__main__":
    print("== calibration against Moh sec.6 (n=75): ==")
    t,ms,rows = census(75)
    print("   skeletons:", t, " rows:", rows, " max s:", ms)
    print("   Moh's stated count of admissible M_2 at (75,50): 25")
    print("   multiples of d_3=5 in [-50,74):", len([M for M in range(-50,74) if M%5==0]))
    print("   of these, with gcd(25,M)=5 exactly:", len([M for M in range(-50,74) if gcd(25,M)==5]))
    print()
    print("== growth of the skeleton census (K>=16) ==")
    print(f"{'n':>5} {'#skel(n)':>10} {'cum':>12} {'max s':>6} {'log2 Kmax':>10}")
    cum=0; series=[]
    for n in range(48, 421):
        t,ms,_ = census(n)
        cum+=t
        if t:
            Kmax = max([K for K in range(16, n//3+1) if n%K==0], default=0)
            series.append((n,t,cum,ms))
    for (n,t,cum,ms) in series:
        if n in (48,64,75,84,96,99,100,120,128,144,160,180,192,200,240,256,288,300,320,336,360,384,400,420) or n<=100 and t>500:
            Kmax = max([K for K in range(16, n//3+1) if n%K==0], default=0)
            print(f"{n:5d} {t:10d} {cum:12d} {ms:6d} {log2(Kmax):10.2f}")
    print()
    # cumulative at Moh's cutoff and beyond
    for cut in (100,120,150,200,250,300,400,420):
        c = max([cum for (n,t,cum,ms) in series if n<=cut], default=0)
        print(f"  cumulative skeletons with n <= {cut:4d} : {c}")
    print()
    print("== observed maximum depth s vs the DEPTH-LOG bound s <= log2(K) ==")
    for n in [64,96,128,192,256,320,384,400]:
        t,ms,_=census(n)
        Ks=[K for K in range(16,n//3+1) if n%K==0]
        if Ks: print(f"  n={n:4d}  max s observed={ms}   max floor(log2 K)={max(int(log2(K)) for K in Ks)}")
