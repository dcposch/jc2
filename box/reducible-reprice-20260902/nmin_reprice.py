#!/usr/bin/env python3
"""
REDUCIBLE-BRANCH REPRICE -- part (3): the (UNI) integrality filter at a
variable N_min, with and without an upper window.

Consumes, WITHOUT modification:
  box/moh_skeleton_N.py            (census, Skel)          3022020435c8...
  box/d1sub-drivers-20260902/d1floor.py  (qval, achievable) cf0780cc7dd7...

The only change from d1floor.run_integrality is that (Nlo, Nhi) are swept:
  (2,  None)  hypothesis-free, pre-frontier          [record: 55.13% groups]
  (4,  None)  N>=4 (Orevkov N<=3), no upper window
  (6,  None)  N>=6 (the 01:10Z frontier), no upper window   <-- REDUCIBLE BRANCH
  (4,  16)    the record's "H2" run                   [record: 60.04% groups]
  (6,  16)    the H2 branch after the frontier
"N in [Nlo,Nhi]" kills a V-assignment when no achievable pinned N lies in it.
A group (n, m, M_2..M_s, V_s) dies when every one of its V-assignments dies.
"""
import sys, os, time
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(HERE, '..', 'd1sub-drivers-20260902'))
from moh_skeleton_N import Skel, census
from d1floor import qval, achievable

WINDOWS = [(2, None), (4, None), (6, None), (4, 16), (6, 16)]

def run(nmax, nmin=48, windows=WINDOWS, per_degree=(105,108,112,117,120)):
    tot = {w: dict(a=0, k=0, g=0, kg=0) for w in windows}
    rows = {}
    t0 = time.time()
    for n in range(nmin, nmax+1):
        na = 0
        kill = {w: 0 for w in windows}
        grp = {}                      # key -> {w: alive?}
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok(): continue
            na += 1
            allv = achievable(S)      # the pinned integers k*V_2*q, k*V_2 <= u
            key = (m, Ms, S.V[S.s])
            g = grp.setdefault(key, {w: False for w in windows})
            for (lo, hi) in windows:
                ok = [x for x in allv if x >= lo and (hi is None or x <= hi)]
                if ok: g[(lo, hi)] = True
                else:  kill[(lo, hi)] += 1
        if not na: continue
        rows[n] = (na, dict(kill), len(grp),
                   {w: sum(1 for k in grp if not grp[k][w]) for w in windows})
        for w in windows:
            tot[w]['a'] += na; tot[w]['k'] += kill[w]
            tot[w]['g'] += len(grp); tot[w]['kg'] += rows[n][3][w]
    print("== (UNI) INTEGRALITY at variable N_min, D in [%d,%d] ==" % (nmin, nmax))
    print("   %-11s %10s %10s %8s %9s %8s %8s" %
          ("window", "assign", "kill", "%", "groups", "grpkill", "%"))
    for (lo, hi) in windows:
        T = tot[(lo, hi)]
        lab = "N>=%d" % lo + ("" if hi is None else " <=%d" % hi)
        print("   %-11s %10d %10d %7.2f%% %9d %8d %7.2f%%" %
              (lab, T['a'], T['k'], 100.0*T['k']/max(1, T['a']),
               T['g'], T['kg'], 100.0*T['kg']/max(1, T['g'])))
    print("\n   per-degree groups / group-kills, MOH-SHARP-2 admissible degrees")
    print("   %5s %8s %s" % ("D", "groups", "  ".join("N>=%d%s" % (lo, "" if hi is None else "<=%d" % hi)
                                                      for (lo, hi) in windows)))
    for n in sorted(rows):
        if n in per_degree:
            na, kill, ng, kg = rows[n]
            print("   %5d %8d   %s" % (n, ng, "   ".join("%6d" % kg[w] for w in windows)))
    dead = {}
    for (lo, hi) in windows:
        dead[(lo, hi)] = [n for n in rows if rows[n][3][(lo, hi)] == rows[n][2]]
    print("\n   degrees with EVERY group killed:")
    for (lo, hi) in windows:
        lab = "N>=%d" % lo + ("" if hi is None else " <=%d" % hi)
        print("     %-11s %s" % (lab, dead[(lo, hi)] if dead[(lo, hi)] else "NONE"))
    print("\n   wall %.1f s" % (time.time()-t0))
    return rows, tot

if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    nmin = int(sys.argv[2]) if len(sys.argv) > 2 else 48
    run(nmax, nmin)
