#!/usr/bin/env python3
"""D1-SUBTREE: full run.  Controls (fail-closed) then the two filters."""
import sys, time, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import d1floor as DF
from d1floor import (Skel, census, qval, achievable, lower_V_extremes, check,
                     NCHECK, FAILURES)

def integrality_on(degs, Nlo=4, Nhi=16, label=""):
    print("\n== INTEGRALITY under (UNI):  N = k V_2 q in Z,  k V_2 <= u   %s ==" % label)
    print("   %5s %10s %12s %12s %8s %10s %10s" %
          ("D","assign","kill uncond","kill H2","groups","grp kill U","grp kill H2"))
    T = dict(a=0, ka=0, kh=0, g=0, kgu=0, kgh=0)
    for n in degs:
        na=ka=kh=0; grp={}
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok(): continue
            na += 1
            allv = achievable(S)
            h2  = [v for v in allv if Nlo <= v <= Nhi]
            unc = [v for v in allv if v >= 2]
            if not unc: ka += 1
            if not h2:  kh += 1
            key = (m, Ms, S.V[S.s]); g = grp.setdefault(key, [False, False])
            if unc: g[0] = True
            if h2:  g[1] = True
        if not na: continue
        kgu = sum(1 for k in grp if not grp[k][0]); kgh = sum(1 for k in grp if not grp[k][1])
        T['a']+=na; T['ka']+=ka; T['kh']+=kh; T['g']+=len(grp); T['kgu']+=kgu; T['kgh']+=kgh
        print("   %5d %10d %12d %12d %8d %10d %10d" % (n, na, ka, kh, len(grp), kgu, kgh))
        sys.stdout.flush()
    print("   TOTAL %s: assignments %d, killed uncond %d (%.2f%%), killed H2 %d (%.2f%%)"
          % (label, T['a'], T['ka'], 100.0*T['ka']/max(1,T['a']),
             T['kh'], 100.0*T['kh']/max(1,T['a'])))
    print("   TOTAL %s: groups %d, killed uncond %d (%.2f%%), killed H2 %d (%.2f%%)"
          % (label, T['g'], T['kgu'], 100.0*T['kgu']/max(1,T['g']),
             T['kgh'], 100.0*T['kgh']/max(1,T['g'])))
    return T

def floors_on(degs, label=""):
    """hypothesis-free: L = min over branch data of V_2 q  (a genuine floor on N)."""
    print("\n== HYPOTHESIS-FREE FLOOR  N >= L(skeleton)   %s ==" % label)
    print("   %5s %9s %10s %10s %10s %10s %10s" %
          ("D","groups","min L","max L","min U","max U","L>16 kills"))
    gmin = None; T=dict(g=0,k=0)
    for n in degs:
        groups = set()
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if S.windows_ok(): groups.add((m, Ms, S.V[S.s]))
        Ls=[]; Us=[]; kl=0
        for (m, Ms, Vs_top) in groups:
            Vlo, Vhi = lower_V_extremes(n, m, list(Ms), Vs_top)
            if Vlo is None: continue
            Slo = Skel(n, m, list(Ms), Vlo); Shi = Skel(n, m, list(Ms), Vhi)
            if not (Slo.windows_ok() and Shi.windows_ok()): continue
            L = Slo.V[2]*qval(Slo); U = Shi.u*qval(Shi)
            Ls.append(L); Us.append(U)
            if L > 16: kl += 1
        if not Ls: continue
        T['g'] += len(Ls); T['k'] += kl
        if gmin is None or min(Ls) < gmin: gmin = min(Ls)
        print("   %5d %9d %10.4f %10.4f %10.4f %10.4f %10d" %
              (n, len(Ls), float(min(Ls)), float(max(Ls)), float(min(Us)), float(max(Us)), kl))
        sys.stdout.flush()
    print("   TOTAL %s: groups %d, killed by L > 16 (H2): %d ; global min L = %s = %.5f"
          % (label, T['g'], T['k'], gmin, float(gmin) if gmin else 0))
    return T

if __name__ == "__main__":
    t0 = time.time()
    DF.control_1_radius_order(); DF.control_2_floor_eq_ceiling(); DF.control_3_q_forms()
    DF.control_4_automorphism(); DF.control_5_moh_rows(); DF.control_6_extremes()
    print("\n== %d controls, %d failures ==" % (NCHECK[0], len(FAILURES)))
    sys.stdout.flush()
    if FAILURES:
        for nm, dt in FAILURES[:10]: print("  FAILED %s %s" % (nm, dt))
        sys.exit(1)
    MOHSHARP = [d for d in range(101, 201)]
    floors_on(list(range(48, 121)), "D <= 120 (complete)")
    integrality_on(list(range(48, 121)), label="D <= 120 (complete)")
    integrality_on([105,108,112,117,120], label="MOH-SHARP-2 admissible in [101,120]")
    floors_on(MOHSHARP, "D in [101,200]")
    print("\nwall %.1f s" % (time.time()-t0))
