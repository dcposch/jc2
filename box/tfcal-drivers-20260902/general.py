#!/usr/bin/env python3
"""Hypothesis-free knapsack: N = sum_B V_2(B) q(B), sum_B V_2(B) <= u, N in Z cap [Nlo,Nhi].
   Branches may carry DIFFERENT lower-V data (no (UNI)).  Capped groups are counted as
   SURVIVING, so the reported kill count is a floor."""
import sys, os, time
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from d1floor import Skel, census, qval

def run(degs, Nlo=4, Nhi=16, CAP=60000):
    print("  %5s %8s %10s %10s %10s" % ("D","groups","killed","capped","wall"))
    tg=tk=tc=0
    for n in degs:
        t0=time.time(); groups={}
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if S.windows_ok(): groups.setdefault((m, Ms, S.V[S.s]), []).append((S.V[2], qval(S), S.u))
        ng=nk=nc=0
        for key, items in groups.items():
            ng+=1; u=int(items[0][2])
            cand = sorted(set((v,q) for (v,q,_) in items if v*q <= Nhi))
            layer = {0: {F(0)}}; hit=False; capped=False
            for tv in range(0, u+1):
                if tv not in layer or hit: continue
                for s0 in layer[tv]:
                    for (v,q) in cand:
                        if tv+v > u: continue
                        s1 = s0+v*q
                        if s1 > Nhi: continue
                        tgt = layer.setdefault(tv+v, set())
                        if len(tgt) >= CAP: capped=True; continue
                        tgt.add(s1)
                        if s1.denominator==1 and Nlo <= s1 <= Nhi: hit=True
                    if hit: break
            if hit: continue
            if capped: nc+=1
            else: nk+=1
        tg+=ng; tk+=nk; tc+=nc
        print("  %5d %8d %10d %10d %9.1fs" % (n, ng, nk, nc, time.time()-t0)); sys.stdout.flush()
    print("  TOTAL: groups %d, KILLED %d (%.2f%%), capped/UNDECIDED %d" % (tg,tk,100.0*tk/max(1,tg),tc))

if __name__ == "__main__":
    lo = int(sys.argv[1]); hi = int(sys.argv[2])
    print("== GENERAL (no (UNI)) knapsack, D in [%d,%d] ==" % (lo,hi)); sys.stdout.flush()
    run(list(range(lo,hi+1)))
