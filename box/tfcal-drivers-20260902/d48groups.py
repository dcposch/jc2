#!/usr/bin/env python3
"""TIME-FUNCTION CALIBRATION at D = 48: enumerate the groups, run the
   hypothesis-free knapsack at N in [Nlo,Nhi], print the survivors with their
   full skeleton data, and rank them by total root budget u*e and by the number
   of tame coefficients that the Puiseux computation will carry."""
import sys, os, time
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moh_skeleton_N import Skel, census
from d1floor import qval

D = 48
Nlo = int(sys.argv[1]) if len(sys.argv) > 1 else 6
Nhi = int(sys.argv[2]) if len(sys.argv) > 2 else 16

groups = {}
for (m, Ms, V) in census(D):
    S = Skel(D, m, list(Ms), V)
    if not S.windows_ok(): continue
    groups.setdefault((m, Ms, S.V[S.s]), []).append((S.V[2], qval(S), S.u, dict(S.V), S))

print("== D = %d : %d V-assignments in %d groups ==" % (
      D, sum(len(v) for v in groups.values()), len(groups)))

def knap(items, u, Nlo, Nhi, CAP=200000):
    """exact knapsack: reachable N = sum V_2(B) q(B), sum V_2(B) <= u.
       returns (hit_list, capped)"""
    cand = sorted(set((v, q) for (v, q, _, _, _) in items if v*q <= Nhi))
    reach = {0: {F(0): ()}}
    hits = []; capped = False
    for tv in range(0, u+1):
        if tv not in reach: continue
        for s0, path in list(reach[tv].items()):
            for (v, q) in cand:
                if tv+v > u: continue
                s1 = s0 + v*q
                if s1 > Nhi: continue
                tgt = reach.setdefault(tv+v, {})
                if len(tgt) >= CAP: capped = True; continue
                if s1 not in tgt: tgt[s1] = path + ((v,q),)
                if s1.denominator == 1 and Nlo <= s1 <= Nhi:
                    hits.append((int(s1), tgt[s1]))
    return hits, capped

rows = []
for key, items in sorted(groups.items()):
    m, Ms, Vs = key
    u = int(items[0][2]); S0 = items[0][4]
    hits, capped = knap(items, u, Nlo, Nhi)
    seen = {}
    for (N, path) in hits:
        if N not in seen: seen[N] = path
    rows.append((key, items, u, S0, sorted(seen.items()), capped))

alive = [r for r in rows if r[4]]
dead  = [r for r in rows if not r[4] and not r[5]]
cap   = [r for r in rows if not r[4] and r[5]]
print("   N in [%d,%d]:  ALIVE %d   KILLED %d   CAPPED %d" % (Nlo,Nhi,len(alive),len(dead),len(cap)))

print("\n-- SURVIVING groups (m, M_2..M_s, V_s), sorted by budget u*e then #V-assignments --")
hdr = "   %-4s %-14s %-4s %-3s %-3s %-6s %-5s %-5s %-6s %-8s %s"
print(hdr % ("m","M_2..M_s","V_s","K","s","(d,e)","u","u*e","#asg","minN","N reachable"))
def budget(r): return r[3].u * r[3].e
for r in sorted(alive, key=lambda r: (budget(r), len(r[1]), r[0])):
    key, items, u, S0, hits, capped = r
    m, Ms, Vs = key
    Ns = [N for (N, p) in hits]
    print(hdr % (m, str(list(Ms)), Vs, S0.K, S0.s, "(%d,%d)"%(S0.dd,S0.e), u,
                 int(S0.u*S0.e), len(items), min(Ns), Ns[:8]))

print("\n-- KILLED groups (no integer N in [%d,%d]) --" % (Nlo,Nhi))
for r in sorted(dead, key=lambda r: (budget(r), r[0])):
    key, items, u, S0, hits, capped = r
    print("   m=%-4d M=%-14s V_s=%-3d K=%-3d (d,e)=(%d,%d) u=%d  #asg=%d  qs=%s" % (
        key[0], str(list(key[1])), key[2], S0.K, S0.dd, S0.e, u, len(items),
        sorted(set(str(q) for (v,q,_,_,_) in items))[:6]))
if cap:
    print("\n-- CAPPED (undecided) --")
    for r in cap:
        print("   %s" % (r[0],))
