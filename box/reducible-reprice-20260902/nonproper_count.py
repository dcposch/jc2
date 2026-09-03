#!/usr/bin/env python3
"""
REDUCIBLE-BRANCH REPRICE -- part (2)/(4): the NON-PROPER BRANCH COUNT.

D1-STAR + DETECTOR-NULL + FRONTIER-EXACT partition the D roots of a generic fibre
g - c_2 into
    PROPER      the sum_B a_1(B) = e * sum_B V_2(B) roots of the bottom-major discs
                (delta^0 < 1, contribution (1-delta^0)^+ = q/e each),
    NON-PROPER  everything else, all in minor discs (delta^0 >= 1, contribution 0).
Hence, with D = K e,
    R := # non-proper Puiseux branches of a generic fibre = D - e * sum_B V_2(B)
       = e * (K - sum_B V_2(B)) .
Each non-proper place gamma has a limit point (a_0, c_2) in A_F, so
    R  >=  Lambda (# non-proper places)  >=  n_A^Y := # (A_F cap {Y=c_2})  >=  #components
(the last step by Lemma NL: no component of A_F is a line, so every component
dominates the Y-line).  Two tests, over the (UNI) census, on the assignments that
survive the integrality filter at N >= N_MIN:
    FREE      R >= 2      <=>  sum V_2 <= K-1   (e>=3)     [reducible needs >= 2 comps]
    CHAU      R >= 2e     <=>  sum V_2 <= K-2              [every component degree a
                                                            multiple of max(d,e) = e]
CHAU carries GAP[HORIZONTAL-DEGREE]: n_A^Y = deg Abar_F - mult_{[1:0:0]} Abar_F,
so "deg >= 2e" transfers to n_A^Y only if that multiplicity is controlled.
"""
import sys, os, time
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(HERE, '..', 'd1sub-drivers-20260902'))
from moh_skeleton_N import Skel, census
from d1floor import qval

def run(nmax=120, nmin=48, NMIN=6):
    print("== NON-PROPER BRANCH COUNT R = e(K - sum V_2) over the (UNI) census ==")
    print("   surviving = some k with k*V_2 <= u and N = k*V_2*q an integer >= %d" % NMIN)
    T = dict(a=0, surv=0, free=0, chau=0, g=0, gs=0, gfree=0, gchau=0)
    rows = {}
    minR = None; minRat = None
    for n in range(nmin, nmax+1):
        na=surv=free=chau=0; grp={}
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok(): continue
            na += 1
            q = qval(S); v = S.V[2]; u = S.u; K = S.K; e = S.e
            kmax = int(u // v) if v else 0
            ok_any = ok_free = ok_chau = False
            for k in range(1, kmax+1):
                val = k*v*q
                if val.denominator != 1 or int(val) < NMIN: continue
                ok_any = True
                sV = k*v
                R = e*(K - sV)
                if minR is None or R < minR:
                    minR = R; minRat = (n, m, Ms, dict(S.V), k, sV, K, e, int(val))
                if sV <= K-1: ok_free = True
                if sV <= K-2: ok_chau = True
            key = (m, Ms, S.V[S.s])
            g = grp.setdefault(key, [False, False, False])
            if ok_any:  surv += 1; g[0] = True
            if ok_free: free += 1; g[1] = True
            if ok_chau: chau += 1; g[2] = True
        if not na: continue
        gs  = sum(1 for k in grp if grp[k][0])
        gf  = sum(1 for k in grp if grp[k][1])
        gc  = sum(1 for k in grp if grp[k][2])
        rows[n] = (na, surv, free, chau, len(grp), gs, gf, gc)
        T['a']+=na; T['surv']+=surv; T['free']+=free; T['chau']+=chau
        T['g']+=len(grp); T['gs']+=gs; T['gfree']+=gf; T['gchau']+=gc
    print("\n   %5s %9s %9s %9s %9s | %7s %7s %7s %7s" %
          ("D","assign","surv","+free","+chau","groups","surv","free","chau"))
    for n in sorted(rows):
        if n in (105,108,112,117,120) or n%25==0 or n==nmax:
            na,su,fr,ch,ng,gs,gf,gc = rows[n]
            print("   %5d %9d %9d %9d %9d | %7d %7d %7d %7d" % (n,na,su,fr,ch,ng,gs,gf,gc))
    print("   ---- totals D in [%d,%d] ----" % (nmin,nmax))
    print("   V-assignments %d ; surviving N>=%d: %d ; also R>=2 (FREE): %d ; also R>=2e (CHAU): %d"
          % (T['a'], NMIN, T['surv'], T['free'], T['chau']))
    print("   groups %d ; surviving: %d ; FREE-alive: %d ; CHAU-alive: %d"
          % (T['g'], T['gs'], T['gfree'], T['gchau']))
    print("   groups killed ONLY by the reducible test (surv but not CHAU-alive): %d"
          % (T['gs'] - T['gchau']))
    print("   groups killed ONLY by the FREE test (surv but not FREE-alive): %d"
          % (T['gs'] - T['gfree']))
    print("   min R over surviving assignments: %s   at %s" % (minR, minRat))
    return rows, T

if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv)>1 else 120
    NMIN = int(sys.argv[2]) if len(sys.argv)>2 else 6
    t0=time.time(); run(nmax, 48, NMIN); print("\n   wall %.1f s" % (time.time()-t0))
