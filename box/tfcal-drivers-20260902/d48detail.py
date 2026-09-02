#!/usr/bin/env python3
"""Full per-assignment detail for the surviving D=48 groups: delta chain, q, a_1, b_1,
   the realising bottom-disc multiset, and the Puiseux ramification denominators."""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moh_skeleton_N import Skel, census
from d1floor import qval

D = 48; Nlo, Nhi = 6, 16
groups = {}
for (m, Ms, V) in census(D):
    S = Skel(D, m, list(Ms), V)
    if not S.windows_ok(): continue
    groups.setdefault((m, Ms, S.V[S.s]), []).append(S)

def knap_sols(items, u):
    cand = sorted(set((S.V[2], qval(S)) for S in items if S.V[2]*qval(S) <= Nhi))
    reach = {0: {F(0): ()}}
    sols = {}
    for tv in range(0, u+1):
        if tv not in reach: continue
        for s0, path in list(reach[tv].items()):
            for (v, q) in cand:
                if tv+v > u: continue
                s1 = s0+v*q
                if s1 > Nhi: continue
                tgt = reach.setdefault(tv+v, {})
                if s1 not in tgt: tgt[s1] = path+((v,q),)
                if s1.denominator == 1 and Nlo <= s1 <= Nhi and int(s1) not in sols:
                    sols[int(s1)] = tgt[s1]
    return sols

print("== D=48 surviving groups: per-assignment detail (only assignments used by some N) ==")
print("   %-16s %-3s %-14s %-10s %-10s %-8s %-4s %-4s %-4s" %
      ("M-chain","Vs","V-assign","delta_1","delta_2","q","a_1","b_1","den"))
best = []
for key in sorted(groups):
    m, Ms, Vs = key
    items = groups[key]; u = int(items[0].u)
    sols = knap_sols(items, u)
    if not sols: continue
    used = set()
    for N, path in sols.items():
        for (v,q) in path: used.add((v,q))
    for S in sorted(items, key=lambda S: (S.V[2], qval(S))):
        if (S.V[2], qval(S)) not in used: continue
        dens = set()
        for r in range(1, S.s+1): dens.add(S.delta[r].denominator)
        print("   %-16s %-3s %-14s %-10s %-10s %-8s %-4d %-4d %-4s   N=%s x%s" % (
            str(list(Ms)), Vs, str([S.V[i] for i in range(2, S.s+1)]),
            S.delta[1], S.delta[2], qval(S), 3*S.V[2], 2*S.V[2],
            max(dens), sorted(sols), len(sols[min(sols)])))
        best.append((3*S.V[2], max(dens), S.s, len(sols[min(sols)]), min(sols),
                     (m, Ms, Vs), tuple(S.V[i] for i in range(2,S.s+1)), S))
print("\n-- ranked by (a_1, ramification denominator, tower length s, #bottom discs) --")
for r in sorted(best, key=lambda r: r[:5])[:14]:
    a1, den, s, nb, N, key, Vasg, S = r
    print("   a_1=%-3d den=%-4d s=%d  #discs=%d  N=%d   M=%-16s V_s=%-2d V=%s  q=%s d1=%s d2=%s" %
          (a1, den, s, nb, N, str(list(key[1])), key[2], list(Vasg), qval(S), S.delta[1], S.delta[2]))
