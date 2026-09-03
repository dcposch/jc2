#!/usr/bin/env python3
"""CENSUS-REBASE driver: all report numbers, one core.  Writes the full survivor
   listing to survivors-D48-120.txt next to this file."""
import sys, os, time
from fractions import Fraction as F
from math import gcd
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import moh_skeleton_full as M

HERE = os.path.dirname(os.path.abspath(__file__))
t00 = time.time()

print("="*78); print("CENSUS-REBASE (opus5 2026-09-02): Moh (1)-(13), rebased census"); print("="*78)
M.run_controls()

# ---------------------------------------------------------------- A. baselines
print("\n== A. (1)-(7) baseline (the campaign's current census) ==")
b7 = {}
for n in range(48, 121):
    G = M.groups_of(n, full=False)
    if G: b7[n] = (sum(len(v) for v in G.values()), len(G))
print("   TOTAL 48<=D<=120: V-assignments %d, groups %d"
      % (sum(v[0] for v in b7.values()), sum(v[1] for v in b7.values())))

# ------------------------------------------- B. cross-check the calibration lane
print("\n== B. cross-check of the TIME-FUNCTION CALIBRATION lane's numbers ==")
print("   its pipeline: (1)-(7) -> reconstructed (10) at j>=2 with NO branch (11)")
print("   -> (10)_1 [= Moh (12)/(13)].  Claimed 902893 -> 3760 -> 329 V-assignments,")
print("   10637 -> 1012 -> 287 groups.")
c = dict(a10=0, g10=0, a11=0, g11=0)
for n in range(48, 121):
    G10 = {}; G11 = {}
    for (m, Ms, V) in M.census(n):
        S = M.Skel(n, m, list(Ms), V)
        if not all(S.cond1011(j)[1] for j in range(S.s-1, 1, -1)): continue   # (10) only
        G10.setdefault((m, Ms, S.V[S.s]), []).append(V)
        if S.cond1213()[0]: G11.setdefault((m, Ms, S.V[S.s]), []).append(V)
    c['a10'] += sum(len(v) for v in G10.values()); c['g10'] += len(G10)
    c['a11'] += sum(len(v) for v in G11.values()); c['g11'] += len(G11)
print("   reproduced: (10) only  -> V-assignments %d, groups %d" % (c['a10'], c['g10']))
print("   reproduced: (10)+(12)/(13) -> V-assignments %d, groups %d" % (c['a11'], c['g11']))
M.check("calibration lane's (10) count 3760/1012 reproduced",
        (c['a10'], c['g10']) == (3760, 1012), str((c['a10'], c['g10'])))
M.check("calibration lane's (10)+(10)_1 count 329/287 reproduced",
        (c['a11'], c['g11']) == (329, 287), str((c['a11'], c['g11'])))

# ------------------------------------------------------- C. the rebased census
T, empty, surv = M.rerun(48, 120, listing=(105, 108, 112, 117, 120))

print("\n== C2. per-degree comparison, (1)-(7) vs (1)-(13) ==")
print("   %5s %11s %8s %11s %8s %8s %8s %8s" %
      ("D", "V7", "grp7", "V13", "grp13", "uni>=6", "uni6-16", "mix6-16"))
tot = [0]*6
for n in sorted(b7):
    G = M.groups_of(n, full=True)
    na = sum(len(v) for v in G.values())
    a1 = sum(1 for it in G.values() if M.uni_hits(it, 6, None))
    a2 = sum(1 for it in G.values() if M.uni_hits(it, 6, 16))
    am = sum(1 for it in G.values() if M.mixed_hit(it)[0] or M.mixed_hit(it)[1])
    print("   %5d %11d %8d %11d %8d %8d %8d %8d"
          % (n, b7[n][0], b7[n][1], na, len(G), a1, a2, am))
    for i, v in enumerate((b7[n][0], b7[n][1], na, len(G), a1, a2)): tot[i] += v
print("   TOTAL %9d %8d %11d %8d %8d %8d" % tuple(tot))

# ------------------------------------------------------ D. Moh's published rows
print("\n== D. Moh's six published rows on the rebased pipeline ==")
print("   %-24s %8s %8s %6s %6s %-28s" % ("row","delta_2","delta_1","q","u","achievable N (UNI, N>=6)"))
for (n, m, Ms, Vs, lab, p2, p1, err) in M.MOH_TABLE:
    S = M.Skel(n, m, Ms, Vs)
    items = [(S.V[2], S.q(), S.u)]
    print("   %-24s %8s %8s %6s %6s %-28s" %
          (lab, S.delta[2], S.delta[1], S.q(), S.u, sorted(M.uni_hits(items, 6, None))))
    M.check("Moh row passes (1)-(13): %s" % lab, S.full_ok())

# ------------------------------------------------------------- E. D <= 200
print("\n== E. extension to D <= 200 ==")
a2, g2 = M.count_only(121, 200, full=True)
print("   D<=200 TOTAL: V-assignments %d, groups %d" % (T['a']+a2, T['g']+g2))
T2, empty2, _ = M.rerun(121, 200, listing=(), do_mixed=True)
print("   degrees 121..200 emptied by the knapsack: %s" % (empty2 if empty2 else "NONE"))

# ------------------------------------------------- F. full survivor listing file
path = os.path.join(HERE, "survivors-D48-120.txt")
with open(path, "w") as fh:
    fh.write("CENSUS-REBASE: every group surviving Moh (1)-(13) + the pinned-N\n"
             "knapsack (N integral, 6 <= N <= 16, mixed form) at 48 <= D <= 120.\n"
             "columns: D | m | M_2..M_s | V_s | K | (d,e) | u | per-branch (V_2, q, delta_1)"
             " | achievable N under (UNI) in [6,16]\n\n")
    for n in sorted(surv):
        fh.write("---- D = %d : %d surviving groups ----\n" % (n, len(surv[n])))
        for (key, items, capped) in sorted(surv[n]):
            (m, Ms, Vs) = key; K = gcd(n, m)
            br = []
            for (v, q, u) in sorted(items):
                Vd = {2: v}
                # recover the full V-assignment carrying this (V_2, q)
                for (mm, MM, VV) in M.census(n, full=True):
                    if mm != m or MM != Ms or VV[2] != v: continue
                    SS = M.Skel(n, m, list(MM), VV)
                    if SS.V[SS.s] == Vs and SS.q() == q: Vd = VV; break
                S = M.Skel(n, m, list(Ms), Vd)
                br.append("(V=%s,q=%s,d1=%s)" % (dict(sorted(Vd.items())), q, S.delta[1]))
            fh.write("D=%d m=%d M=%s V_s=%d K=%d (d,e)=(%d,%d) u=%s | %s | N=%s%s\n"
                     % (n, m, list(Ms), Vs, K, m//K, n//K, items[0][2], " ".join(br),
                        sorted(M.uni_hits(items, 6, 16)), " CAPPED" if capped else ""))
        fh.write("\n")
print("\n   full survivor listing written to %s" % path)

print("\n" + "="*78)
if M.FAILURES: print("FAILURES: %s" % M.FAILURES); sys.exit(1)
print("ALL CONTROLS PASSED.  total wall %.1f s" % (time.time()-t00))
