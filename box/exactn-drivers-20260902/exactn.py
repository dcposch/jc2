#!/usr/bin/env python3
"""
exactn.py -- THEOREM D1-STAR / THEOREM EXACT-N on the Moh census.

Imports the reviewed instrument box/moh_skeleton_N.py (Skel = Def 5.1(1)-(3),
RADIUS-ORDER, N-CEILING, census).  FAIL-CLOSED: every control must pass before
a filter number is printed.

THE FUNCTION Phi.   Along the path of a g-root rho,
      Phi(delta) := delta - lambda_f(delta) - lambda_g(delta),
slope 1 - a(delta) - b(delta) <= 0, so Phi is NON-INCREASING.
  (i)  DICTIONARY (Keller):  Phi(delta^0) >= 1 at the g-frontier, = 1 iff the
       branch is proper.
  (ii) RADIUS-ORDER at r=1 with M_1 = -m:  Phi(delta_1) = 1 EXACTLY, and
       Phi(delta_r) > 1 strictly for r >= 2.       <-- verified here
  ==> Phi is CONSTANT on [delta_1, delta^0], so a + b = 1 there:  D1-STAR.

THE FILTER.  Every g-root of a bottom-major disc contributes exactly
      -lambda_f(delta_1) = d(1-delta_1)/(d+e)
so, with A_bot the number of g-roots in bottom-major discs (a_1 <= A_bot <= ue),
      N = A_bot * d(1-delta_1)/(d+e),
giving for the FIRST time a FLOOR   L = a_1 d(1-delta_1)/(d+e) = e V_2 d(1-delta_1)/(d+e)
as well as the reviewed ceiling U = u d e (1-delta_1)/(d+e).
"""
import sys, os, time, argparse
from fractions import Fraction as F
from math import gcd
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import moh_skeleton_N as MS
from moh_skeleton_N import Skel, census, MOH_SURVIVORS

FAILURES = []
def check(name, cond, detail=""):
    if cond: print(f"  [ok]   {name}")
    else:    print(f"  [FAIL] {name}   {detail}"); FAILURES.append(name)

# --------------------------------------------------------------------------
def Phi(S, r):
    """Phi(delta_r) = delta_r - lambda_f(delta_r) - lambda_g(delta_r), computed
       INCREMENTALLY from the tower counts (no RADIUS-ORDER used)."""
    return S.delta[r] - S.lam_f(r) - S.lam_g(r)

def Phi_closed(S, r):
    """delta_r + (n+m)(1-delta_r)/(n-M_r)   [RADIUS-ORDER + lambda_f=(m/n)lambda_g]"""
    return S.delta[r] + F((S.n+S.m)*(1-S.delta[r]), S.n - S.M[r])

def floor_L(S):
    """L = a_1 * (-lambda_f(delta_1)) = e V_2 d (1-delta_1)/(d+e).  One tower."""
    if S.delta[1] >= 1: return F(0)
    return F(S.a[1]*S.dd, S.dd+S.e)*(1-S.delta[1])

def contrib(S):
    """per-root contribution of a bottom-major disc = -lambda_f(delta_1)."""
    return F(S.dd, S.dd+S.e)*(1-S.delta[1])

# --------------------------------------------------------------------------
def controls():
    print("== CONTROL P1: Phi(delta_1) = 1 exactly; Phi(delta_r) > 1 for r >= 2 ==")
    print(f"   {'row':22} {'Phi(d_1)':>9} {'Phi(d_2)':>12} {'Phi(d_3)':>12} {'L':>10} {'U':>10}")
    for (n,m,Ms,Vs,lab,_) in MOH_SURVIVORS:
        S = Skel(n,m,Ms,Vs)
        ph = [Phi(S,r) for r in range(1, S.s+1)]
        print(f"   {lab:22} {str(ph[0]):>9} {str(ph[1]):>12} "
              f"{str(ph[2]) if len(ph)>2 else '-':>12} "
              f"{str(floor_L(S)):>10} {str(S.N_upper()):>10}")
        check(f"P1 Phi(delta_1)=1 :: {lab}", ph[0] == 1, str(ph[0]))
        check(f"P1 Phi(delta_r)>1 for r>=2 :: {lab}", all(p > 1 for p in ph[1:]),
              str(ph))
        check(f"P1 incremental == closed form :: {lab}",
              all(Phi(S,r) == Phi_closed(S,r) for r in range(1,S.s+1)))

    print("\n== CONTROL P2: census-wide, every V-skeleton (n <= NMAX) ==")
    t0=time.time(); tot=0; bad=0; badmono=0; badL=0
    for n in range(48, ARGS.control_nmax+1):
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V); tot += 1
            if Phi(S,1) != 1: bad += 1
            if any(Phi(S,r) <= 1 for r in range(2, S.s+1)): badmono += 1
            # Phi must be non-increasing down the tower: Phi(delta_s) >= ... >= Phi(delta_1)
            ph=[Phi(S,r) for r in range(1,S.s+1)]
            if any(ph[i] > ph[i+1] for i in range(len(ph)-1)): badmono += 1
            # floor <= ceiling, and both positive
            if not (0 < floor_L(S) <= S.N_upper()): badL += 1
    print(f"   V-skeletons tested: {tot}   wall {time.time()-t0:.1f}s")
    check("P2 Phi(delta_1) = 1 on every V-skeleton", bad == 0, f"{bad} failures")
    check("P2 Phi(delta_r) > 1 for r>=2 and Phi non-increasing downward",
          badmono == 0, f"{badmono} failures")
    check("P2 0 < L <= U on every V-skeleton", badL == 0, f"{badL} failures")

    print("\n== CONTROL P3: L/U = V_2/u  and  U = (u/V_2) L  (identity) ==")
    ok = True
    for n in range(48, 61):
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if S.N_upper() * S.a[1] != floor_L(S) * S.u * S.e: ok = False
    check("P3 U*a_1 == L*u*e", ok)

    print("\n== CONTROL P4: N-CEILING recovered: A_bot = u e gives U ==")
    ok = all(Skel(n,m,Ms,Vs).u*Skel(n,m,Ms,Vs).e*contrib(Skel(n,m,Ms,Vs))
             == Skel(n,m,Ms,Vs).N_upper() for (n,m,Ms,Vs,lab,_) in MOH_SURVIVORS)
    check("P4 u*e*contrib == U on Moh's six rows", ok)

# --------------------------------------------------------------------------
def group_data(n):
    """per branch-robust group key (m, Ms, V_s):  the list of (a_1, L, U) over all
       admissible lower-V assignments, plus u*e."""
    G = {}
    for (m, Ms, V) in census(n):
        S = Skel(n, m, list(Ms), V)
        key = (m, Ms, V[S.s])
        rec = G.setdefault(key, {'ue': S.u*S.e, 'opts': set(), 'ds': S.s})
        rec['opts'].add((S.a[1], floor_L(S), S.N_upper(), contrib(S)))
    return G

def single_profile_N(rec, Nlo, Nhi):
    """EXACT-N under ONE V-profile across all major branches (conjugate branches):
       N = A*c with A = j*a_1 <= u e.  Returns the attainable integer N."""
    ue = rec['ue']; out = set()
    for (a1, L, U, c) in rec['opts']:
        j = 1
        while j*a1 <= ue:
            Nv = j*a1*c
            if Nv > Nhi: break
            if Nv.denominator == 1 and Nv >= Nlo: out.add(int(Nv))
            j += 1
    return sorted(out)

def mixed_N(rec, Nlo, Nhi, cap=20000):
    """EXACT-N allowing DIFFERENT V-profiles on different major branches:
       N = sum_k a_1^(k) c^(k),  sum_k a_1^(k) <= u e.  Unconditional given the
       theorem.  Returns (feasible?, capped?).  Early-exits on the first hit.
       Exact integer arithmetic: all L are scaled by their common denominator Q."""
    ue = rec['ue']
    best = {}
    for o in rec['opts']:
        if o[1] > Nhi: continue
        if o[1] not in best or o[0] < best[o[1]]: best[o[1]] = o[0]
    if not best: return False, False
    Q = 1
    for L in best: Q = Q*L.denominator//gcd(Q, L.denominator)
    opts = sorted((a1, int(L*Q)) for L, a1 in best.items())
    hi = Nhi*Q; lo = Nlo*Q
    seen = {(0, 0)}; cur = [(0, 0)]
    while cur:
        nxt = []
        for (a, sm) in cur:
            for (a1, l) in opts:
                if a + a1 > ue: continue
                t = sm + l
                if t > hi: continue
                st = (a + a1, t)
                if st in seen: continue
                if t >= lo and t % Q == 0: return True, False
                seen.add(st); nxt.append(st)
                if len(seen) > cap: return False, True
        cur = nxt
    return False, False

def run(nmax, Nlo, Nhi, exact=True, verbose_upto=0, degrees=(), mixed_nmax=10**9, only=()):
    print(f"\n== EXACT-N FILTER,  N in [{Nlo},{Nhi}],  D <= {nmax} ==")
    print(f"   L = a_1 c (FLOOR, new) ; U = u e c (CEILING, reviewed) ; c = d(1-delta_1)/(d+e)")
    print(f"   {'D':>5} {'#groups':>9} {'kL':>5} {'kU':>6} {'k(L|U)':>7} "
          f"{'kSINGLE':>8} {'kMIXED':>7} {'minL':>9} {'maxL':>9}")
    T = dict(groups=0, kL=0, kU=0, kEither=0, kS=0, kM=0)
    emptied=[]; emptiedM=[]; capped=0
    t0=time.time()
    for n in (only if only else range(48, nmax+1)):
        G = group_data(n)
        if not G: continue
        kL=kU=kEither=kS=kM=0
        mnL=None; mxL=F(0)
        for key, rec in G.items():
            Lmin = min(o[1] for o in rec['opts'])
            Umax = max(o[2] for o in rec['opts'])
            if mnL is None or Lmin < mnL: mnL = Lmin
            if Lmin > mxL: mxL = Lmin
            dead_L = Lmin > Nhi; dead_U = Umax < Nlo
            if dead_L: kL += 1
            if dead_U: kU += 1
            if dead_L or dead_U:
                kEither += 1; kS += 1; kM += 1; continue
            if not exact: continue
            if not single_profile_N(rec, Nlo, Nhi):
                kS += 1
                if n > mixed_nmax: continue
                feas, cp = mixed_N(rec, Nlo, Nhi)
                if cp: capped += 1
                elif not feas: kM += 1
        T['groups'] += len(G); T['kL'] += kL; T['kU'] += kU
        T['kEither'] += kEither; T['kS'] += kS; T['kM'] += kM
        if kEither == len(G): emptied.append(n)
        if exact and n <= mixed_nmax and kM == len(G): emptiedM.append(n)
        print(f"   {n:5} {len(G):9} {kL:5} {kU:6} {kEither:7} {kS:8} {kM:7} "
              f"{str(mnL):>9} {str(mxL):>9}   [{time.time()-t0:.0f}s]", flush=True)
    print(f"\n   TOTAL D<={nmax}: branch-robust groups = {T['groups']}")
    print(f"   killed by the FLOOR    L > {Nhi}          : {T['kL']}")
    print(f"   killed by the CEILING  U < {Nlo}           : {T['kU']}")
    print(f"   killed by either                        : {T['kEither']}")
    if exact:
        print(f"   killed by EXACT-N, one V-profile        : {T['kS']}")
        print(f"   killed by EXACT-N, mixed V-profiles     : {T['kM']}   (cap hits {capped})")
    print(f"   degrees EMPTIED by L|U                  : {emptied if emptied else 'NONE'}")
    if exact:
        print(f"   degrees EMPTIED by EXACT-N (mixed)      : {emptiedM if emptiedM else 'NONE'}")
    print(f"   wall {time.time()-t0:.1f}s")
    return T, emptied

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--nmax', type=int, default=200)
    ap.add_argument('--control-nmax', type=int, default=100)
    ap.add_argument('--Nlo', type=int, default=6)
    ap.add_argument('--Nhi', type=int, default=16)
    ap.add_argument('--exact', action='store_true')
    ap.add_argument('--verbose-upto', type=int, default=0)
    ap.add_argument('--mixed-nmax', type=int, default=10**9)
    ap.add_argument('--only', type=str, default='')
    ARGS = ap.parse_args()
    controls()
    if FAILURES:
        print(f"\nFAIL-CLOSED: {len(FAILURES)} control failures, no filter output.")
        sys.exit(1)
    print("\n  ALL CONTROLS PASSED\n")
    run(ARGS.nmax, ARGS.Nlo, ARGS.Nhi, exact=ARGS.exact,
        verbose_upto=ARGS.verbose_upto, degrees=(105,108,112,117,120),
        mixed_nmax=ARGS.mixed_nmax,
        only=tuple(int(v) for v in ARGS.only.split(',') if v))
