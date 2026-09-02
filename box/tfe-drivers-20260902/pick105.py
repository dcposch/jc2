#!/usr/bin/env python3
"""TIME-FUNCTION ENDGAME -- part 0: pick the skeleton.

Enumerate all Moh skeletons at D = 105 (census from box/moh_skeleton_N.py),
apply the (UNI) integrality filter of D1-SUBTREE (N = k V_2 q in Z, k V_2 <= u)
with the frontier floor N >= 6, and print the survivors sorted by a stated
"smallest" order.  FAIL-CLOSED: aborts if the imported controls do not agree
with the charged closed forms.
"""
import sys, os
from fractions import Fraction as F
from math import gcd
sys.path.insert(0, '/Users/dc/code/math/jc2/box')
from moh_skeleton_N import Skel, census

def qval(S):  return (1 - S.delta[1]) * F(S.dd*S.e, S.dd+S.e)

def achievable(S, Nlo=6, Nhi=None):
    q = qval(S); v = S.V[2]; u = S.u
    out = []
    for k in range(1, int(u//v)+1):
        val = k*v*q
        if val.denominator == 1 and val >= Nlo and (Nhi is None or val <= Nhi):
            out.append((k, int(val)))
    return out

D = 105
rows = []
tot = 0
for (m, Ms, V) in census(D):
    S = Skel(D, m, list(Ms), V)
    if not S.windows_ok(): continue
    tot += 1
    hits = achievable(S, 6, None)
    hits16 = [h for h in hits if h[1] <= 16]
    if hits:
        rows.append((S, m, Ms, tuple(sorted(V.items())), qval(S), hits, hits16))

print("D = %d : %d admissible V-skeletons; %d admit an integer N >= 6 under (UNI)"
      % (D, tot, len(rows)))
print("   of those, %d admit N in [6,16]" % sum(1 for r in rows if r[6]))

# "smallest" order: tower depth s, then n-m (= size of interpolation gap is n-m),
# then smallest achievable N, then K, then lexicographic on (M, V)
def key(r):
    S, m, Ms, V, q, hits, h16 = r
    Nmin = min(h[1] for h in hits)
    return (S.s, Nmin, S.e, m, Ms, V)

rows.sort(key=key)
print("\n%-3s %-4s %-4s %-14s %-16s %-3s %-4s %-6s %-7s %-9s %-22s"
      % ("s","m","K","(d,e)","M_2..M_s","u","V_s","V-pkt","q","delta_1","N (k=#bottom discs)"))
for r in rows[:25]:
    S, m, Ms, V, q, hits, h16 = r
    Vp = tuple(S.V[i] for i in range(2, S.s+1))
    print("%-3d %-4d %-4d %-14s %-16s %-3s %-4d %-6s %-7s %-9s %-22s"
          % (S.s, m, S.K, "(%d,%d)"%(S.dd,S.e), str(list(Ms)), S.u, S.V[S.s], str(Vp),
             str(q), str(S.delta[1]), str(hits)))
print("\n... %d rows total" % len(rows))

# full detail on the winner
S, m, Ms, V, q, hits, h16 = rows[0]
print("\n== SELECTED SKELETON ==")
print("  n = D = %d ,  m = %d ,  K = gcd = %d ,  (d,e) = (%d,%d) ,  s = %d"
      % (S.n, S.m, S.K, S.dd, S.e, S.s))
print("  M_1 = -m = %d ; M_2..M_s = %s ; M_s = n-2 = %d" % (S.M[1], [S.M[i] for i in range(2,S.s+1)], S.n-2))
print("  d_i = %s   (d_1=n, d_2=K, ..., d_{s+1})" % [S.d[i] for i in sorted(S.d)])
print("  V_i = %s  (i = 2..s+1)" % {i: S.V[i] for i in sorted(S.V)})
print("  delta_i = %s" % {i: str(S.delta[i]) for i in range(1, S.s+1)})
print("  a_i (# g-roots in D_i) = %s" % {i: S.a[i] for i in range(1, S.s+1)})
print("  b_i (# f-roots in D_i) = %s" % {i: S.b[i] for i in range(1, S.s+1)})
print("  lambda_g(delta_i) = %s" % {i: str(S.lam_g(i)) for i in range(1, S.s+1)})
print("  lambda_f(delta_i) = %s" % {i: str(S.lam_f(i)) for i in range(1, S.s+1)})
print("  u = %s , v = %s , q = %s , U = u q = %s" % (S.u, S.v, q, S.u*q))
print("  achievable N (k, N): %s" % hits)
print("  windows Def 5.1(2): %s" % [(i, str(F(S.d[i],S.n-S.M[i])), S.V[i], str(F(S.V[i+1]*S.d[i],S.d[i+1]))) for i in range(2,S.s+1)])
