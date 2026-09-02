#!/usr/bin/env python3
"""
D1-SUBTREE -- part B: the floor on N from the bottom of Moh's tower.

Inputs re-derived here, not imported as claims:
  Moh Lemma 5.2 (p.178, verbatim):  ((n-L)/d_r) lambda* = -1 + delta*,  hence at the
     general point of D_r,   lambda_g(delta_r) = ord_t g(sigma_r) = n(delta_r-1)/(n-M_r).
  Moh Def 5.1(1) (p.179, verbatim): D_i holds (n/d_{i+1})V_{i+1} roots of g and
     (-mu_j/d_{i+1})V_{i+1} roots of T_j^psi;  with -mu_1 = m this gives
     lambda_f(delta_r) = (m/n) lambda_g(delta_r).
  Moh Prop 6.1(1) (p.190-191, verbatim, r >= 2): on a minor branch, delta < 1 implies
     ord g(sigma) < 0, i.e. the g-frontier there has delta^0 >= 1.

THEOREM D1-PIN (this lane).  Put L_r := 1 - delta_r.  For a root rho of g in a
bottom-major disc D_1, with contribution c_rho = (-lambda_f(delta^0_rho))^+ to N:
    FLOOR    c_rho = 1 - delta^0_rho  >=  L_1 + lambda_g(delta_1) = L_1 m/(n+m)
             [JAC-FIBRE + lambda_g has slope >= 1 below delta_1]
    CEILING  c_rho = -lambda_f(delta^0_rho) <= -lambda_f(delta_1) = L_1 m/(n+m)
             [lambda_f nondecreasing + Def 5.1(1)]
  The two coincide -- and, as verified below, coincide at r = 1 and at NO other level,
  because -M_1 = m is exactly the leading exponent of f.  Hence c_rho is PINNED and
    N  =  sum over bottom-major discs B of  a(B) (1-delta_1(B)) d/(d+e)
       =  sum_B  V_2(B) * q(B),      q := d e K prod_{j=2}^{s} P_j/Q_j = (1-delta_1) d e/(d+e).
"""
import sys, os, time
from math import gcd
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from moh_skeleton_N import Skel, census, MOH_SURVIVORS, top_of_window_V

FAILURES = []; NCHECK=[0]
def check(name, cond, detail=""):
    NCHECK[0]+=1
    if not cond:
        FAILURES.append((name,detail)); print("  FAIL  %-56s %s" % (name, detail))
    return cond

# ------------------------------------------------------------------ per-skeleton
def qval(S):
    """q = (1-delta_1) d e/(d+e)  = the contribution of ONE unit of V_2 to N."""
    return (1 - S.delta[1]) * F(S.dd*S.e, S.dd+S.e)

def qprod(S):
    """closed product form  q = d e K prod_{j=2}^{s} [V_j(n-M_j)-d_j]/[V_j(n-M_{j-1})-d_j]."""
    n, M, d, V, s = S.n, S.M, S.d, S.V, S.s
    out = F(S.dd*S.e*S.K, 1)
    for j in range(2, s+1):
        out *= F(V[j]*(n-M[j]) - d[j], V[j]*(n-M[j-1]) - d[j])
    return out

def floor_r(S, r):   return (1 - S.delta[r]) + S.lam_g_radius(r)   # 1-delta^0 lower bd
def ceil_r(S, r):    return -F(S.m, S.n)*S.lam_g_radius(r)         # -lambda_f(delta_r)

def control_1_radius_order():
    """Moh Lemma 5.2 re-verified against an INDEPENDENT incremental integration of
       lambda_g (slope = number of g-roots still in the disc, Def 5.1(1))."""
    print("\n-- CONTROL 1: Lemma 5.2 (moh.txt p.178, read firsthand) vs incremental lambda_g --")
    seen = 0
    for n in range(48, 121):
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok(): continue
            seen += 1
            for r in range(1, S.s+1):
                if S.lam_g(r) != S.lam_g_radius(r):
                    check("Lemma5.2 n=%d m=%d %s r=%d" % (n,m,Ms,r), False,
                          "%s vs %s" % (S.lam_g(r), S.lam_g_radius(r)))
                    return
            if S.lam_g_closed(1) != S.lam_g(1):
                check("closed-form lam_g n=%d" % n, False); return
            if seen > 40000: break
        if seen > 40000: break
    check("Lemma 5.2 = incremental lambda_g on %d V-skeletons (n<=120)" % seen, True)
    print("   %d V-skeletons, 0 mismatches" % seen)

def control_2_floor_eq_ceiling():
    """floor(r) = ceiling(r) iff -M_r = m iff r = 1.  Verified on the census."""
    print("\n-- CONTROL 2: floor = ceiling AT r=1 AND NOWHERE ELSE --")
    seen = 0; both = 0
    for n in range(48, 121):
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok(): continue
            seen += 1
            if not check("floor==ceiling at r=1 (n=%d,m=%d)"%(n,m), floor_r(S,1)==ceil_r(S,1),
                         "%s vs %s" % (floor_r(S,1), ceil_r(S,1))): return
            for r in range(2, S.s+1):
                eq = (floor_r(S,r) == ceil_r(S,r))
                if eq: both += 1
                if not check("floor<ceiling at r=%d needs M_r=-m (n=%d)"%(r,n),
                             eq == (S.M[r] == -m), "M_r=%d"%S.M[r]): return
            if seen > 40000: break
        if seen > 40000: break
    check("no r>=2 level has floor = ceiling", both == 0, "%d exceptions" % both)
    print("   %d V-skeletons; r=1 equality everywhere, r>=2 equality never" % seen)

def control_3_q_forms():
    print("\n-- CONTROL 3: q = (1-delta_1)de/(d+e) = deK prod P_j/Q_j ; U = u q --")
    seen = 0
    for n in range(48, 121):
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok(): continue
            seen += 1
            if not check("q two ways n=%d"%n, qval(S)==qprod(S), "%s vs %s"%(qval(S),qprod(S))): return
            if S.delta[1] < 1 and not check("U = u q n=%d"%n, S.N_upper()==S.u*qval(S),
                                            "%s vs %s"%(S.N_upper(), S.u*qval(S))): return
            if seen > 40000: break
        if seen > 40000: break
    print("   %d V-skeletons, 0 mismatches" % seen)

def control_4_automorphism():
    """The charged N=1 control, on the skeleton side: (y, x+y^k) has m=1, n=k, s=1,
       M_1=-1, and delta_1 = -1/k;  a_1 = k; the pinned value is exactly N = 1."""
    print("\n-- CONTROL 4: the automorphism (y, x+y^k) pinned to N = 1 --")
    print("   %3s %8s %10s %10s %8s %s" % ("k","delta_1","lam_g(d1)","c_rho","a_1*c","N"))
    for k in range(2, 10):
        n, m, M1 = k, 1, -1
        delta1 = F(-1, k)                       # the k roots of g = x+y^k separate at -1/k
        lamg = -F(n*(1-delta1), n-M1)
        c = (1-delta1) + lamg
        check("automorphism k=%d floor=ceiling"%k, c == -F(m,n)*lamg)
        check("automorphism k=%d pinned N=1"%k, k*c == 1, "%s"%(k*c))
        print("   %3d %8s %10s %10s %8s %s" % (k, delta1, lamg, c, k*c, 1))

def control_5_moh_rows():
    print("\n-- CONTROL 5: Moh's four n<=100 survivors, pinned --")
    print("   %-22s %3s %6s %5s %8s %10s %10s" % ("row","u","q","r(q)","p(q)","U=u q","N in"))
    for (n, m, Ms, Vs, lab, _) in MOH_SURVIVORS:
        S = Skel(n, m, list(Ms), Vs)
        check("Moh row %s windows"%lab, S.windows_ok())
        q = qval(S); u = S.u
        p, r = q.numerator, q.denominator
        vals = [k*p for k in range(1, int(u)//r + 1)]
        check("Moh row %s q=U/u"%lab, S.N_upper() == u*q)
        print("   %-22s %3s %6s %5d %8d %10s %s" % (lab, u, q, r, p, u*q, vals))

# ------------------------------------------------------------------ the filter
def lower_V_extremes(n, m, Ms, Vs_top):
    """Return (V_min_assignment, V_max_assignment) for V_2..V_{s-1} with V_s = Vs_top.
       q is strictly increasing in every V_j (d/dV (P/Q) = d_j(M_j-M_{j-1})/Q^2 > 0),
       and V_2*q is strictly increasing in V_2, so the min of V_2*q is at the bottom of
       every window and the max of q at the top."""
    full = [-m]+list(Ms); s = len(full)
    M = {i+1: full[i] for i in range(s)}
    d = [n]
    for Mi in full: d.append(gcd(d[-1], Mi))
    d = {i+1: d[i] for i in range(len(d))}
    # top of window (max q)
    Vhi = {s+1: d[s+1], s: Vs_top}
    for i in range(s-1, 1, -1):
        hi = F(Vhi[i+1]*d[i], d[i+1]); Vhi[i] = hi.numerator//hi.denominator
        if Vhi[i]*(n-M[i]) <= d[i]: return None, None
    # bottom of window (min V_2*q), top-down: V_i as small as its own window allows
    Vlo = {s+1: d[s+1], s: Vs_top}
    for i in range(s-1, 1, -1):
        lo = F(d[i], n-M[i]); v = lo.numerator//lo.denominator + 1
        hi = F(Vlo[i+1]*d[i], d[i+1])
        if v > hi: return None, None
        Vlo[i] = v
    return ({i: Vlo[i] for i in range(2, s+1)}, {i: Vhi[i] for i in range(2, s+1)})

def brute_extremes(n, m, Ms, Vs_top):
    """exhaustive cross-check of lower_V_extremes."""
    best_lo, best_hi = None, None
    for (mm, MM, V) in census(n):
        if mm != m or MM != tuple(Ms): continue
        S = Skel(n, m, list(Ms), V)
        if not S.windows_ok() or S.V[S.s] != Vs_top: continue
        q = qval(S); lo = S.V[2]*q
        if best_lo is None or lo < best_lo[0]: best_lo = (lo, V)
        if best_hi is None or q > best_hi[0]: best_hi = (q, V)
    return best_lo, best_hi

def control_6_extremes():
    print("\n-- CONTROL 6: closed-form window extremes vs brute force (n <= 72) --")
    tested = 0
    for n in range(48, 73):
        groups = set()
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if S.windows_ok(): groups.add((m, Ms, S.V[S.s]))
        for (m, Ms, Vs_top) in sorted(groups):
            Vlo, Vhi = lower_V_extremes(n, m, list(Ms), Vs_top)
            blo, bhi = brute_extremes(n, m, list(Ms), Vs_top)
            if Vlo is None or blo is None: continue
            Slo = Skel(n, m, list(Ms), Vlo); Shi = Skel(n, m, list(Ms), Vhi)
            tested += 1
            if not check("min V_2 q  n=%d m=%d %s Vs=%d"%(n,m,Ms,Vs_top),
                         Slo.V[2]*qval(Slo) == blo[0], "%s vs %s"%(Slo.V[2]*qval(Slo), blo[0])): return
            if not check("max q     n=%d m=%d %s Vs=%d"%(n,m,Ms,Vs_top),
                         qval(Shi) == bhi[0], "%s vs %s"%(qval(Shi), bhi[0])): return
    print("   %d groups, 0 mismatches" % tested)

def run_filter(nmax, nmin=48, Nlo_H2=4, Nhi_H2=16):
    print("\n== TWO-SIDED FILTER:  L(skeleton) <= N <= U(skeleton),  N integral ==")
    print("   %5s %9s %9s %9s %9s %9s %9s %9s" %
          ("D","groups","minL","maxL","medL","kill L>16","kill U<4","kill window"))
    tot = dict(g=0, kl=0, ku=0, kw=0, ku2=0, kl2=0)
    percD = {}
    for n in range(nmin, nmax+1):
        groups = set()
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if S.windows_ok(): groups.add((m, Ms, S.V[S.s]))
        Ls = []; kl=ku=kw=0; kl2=ku2=0; ng=0
        for (m, Ms, Vs_top) in groups:
            Vlo, Vhi = lower_V_extremes(n, m, list(Ms), Vs_top)
            if Vlo is None: continue
            Slo = Skel(n, m, list(Ms), Vlo); Shi = Skel(n, m, list(Ms), Vhi)
            if not (Slo.windows_ok() and Shi.windows_ok()): continue
            ng += 1
            L = Slo.V[2]*qval(Slo)                       # FLOOR   N >= L
            U = Shi.u*qval(Shi)                          # CEILING N <= U  (= U_rob)
            Ls.append(L)
            if L > Nhi_H2: kl += 1
            if U < Nlo_H2: ku += 1
            if L > 2:      kl2 += 1                      # unconditional floor beats N>=2
            if U < 2:      ku2 += 1
            lo_i = -(-L.numerator//L.denominator)        # ceil(L)
            hi_i = U.numerator//U.denominator            # floor(U)
            if lo_i > hi_i or hi_i < Nlo_H2 or lo_i > Nhi_H2: kw += 1
        Ls.sort()
        if ng:
            med = Ls[len(Ls)//2]
            percD[n] = (ng, Ls[0], Ls[-1], med, kl, ku, kw, kl2, ku2)
            tot['g']+=ng; tot['kl']+=kl; tot['ku']+=ku; tot['kw']+=kw
            tot['kl2']+=kl2; tot['ku2']+=ku2
    for n in sorted(percD):
        ng, lo, hi, med, kl, ku, kw, kl2, ku2 = percD[n]
        if n in (105,108,112,117,120) or n % 25 == 0 or n == nmax:
            print("   %5d %9d %9.3f %9.3f %9.3f %9d %9d %9d" %
                  (n, ng, float(lo), float(hi), float(med), kl, ku, kw))
    print("   ---- totals over D in [%d,%d] ----" % (nmin, nmax))
    print("   groups %d ; kill by L>16 (H2): %d ; kill by U<4 (H2): %d ; kill by empty window: %d"
          % (tot['g'], tot['kl'], tot['ku'], tot['kw']))
    print("   unconditional: floor L > 2 on %d groups (N>=2 is then not binding); U<2 on %d"
          % (tot['kl2'], tot['ku2']))
    allL = []
    for n in percD: allL += [percD[n][1]]
    if allL:
        print("   global min of the per-degree minimal floors: %s = %.4f" % (min(allL), float(min(allL))))
    empty = [n for n in percD if percD[n][6] == percD[n][0]]
    print("   degrees D with EVERY group killed by the two-sided window: %s" % (empty if empty else "NONE"))
    return percD

if __name__ == "__main__":
    t0 = time.time()
    control_1_radius_order()
    control_2_floor_eq_ceiling()
    control_3_q_forms()
    control_4_automorphism()
    control_5_moh_rows()
    control_6_extremes()
    print("\n== %d controls, %d failures ==" % (NCHECK[0], len(FAILURES)))
    if FAILURES:
        for nm, dt in FAILURES[:10]: print("   FAILED: %s %s" % (nm, dt))
        sys.exit(1)
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    run_filter(nmax)
    print("\nwall %.1f s" % (time.time()-t0))

# ------------------------------------------------------- INTEGRALITY (pinned N)
def achievable(S, Nlo=None, Nhi=None):
    """Under (UNI) -- all bottom-major discs carry the same lower-V datum -- the pinned
       value is  N = k * V_2 * q  with k = #bottom-major discs and  k*V_2 <= u.
       Return the integers so achievable (optionally clipped to [Nlo,Nhi])."""
    q = qval(S); v = S.V[2]; u = S.u
    out = []
    kmax = int(u // v) if v else 0
    for k in range(1, kmax+1):
        val = k*v*q
        if val.denominator == 1:
            iv = int(val)
            if (Nlo is None or iv >= Nlo) and (Nhi is None or iv <= Nhi): out.append(iv)
    return out

def run_integrality(nmax, nmin=48, Nlo=4, Nhi=16):
    print("\n== INTEGRALITY FILTER under (UNI):  N = k V_2 q in Z, k V_2 <= u ==")
    print("   %5s %9s %9s %9s %9s %9s" %
          ("D","assign","kill(uncond)","kill(H2)","groups","grp kill(H2)"))
    T = dict(a=0, ka=0, kh=0, g=0, kg=0); rows={}
    for n in range(nmin, nmax+1):
        na=ka=kh=0; grp={}
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok(): continue
            na += 1
            allv = achievable(S)
            h2   = [x for x in allv if Nlo <= x <= Nhi]
            unc  = [x for x in allv if x >= 2]
            if not unc: ka += 1
            if not h2:  kh += 1
            key = (m, Ms, S.V[S.s])
            grp.setdefault(key, [False, False])
            if unc: grp[key][0] = True
            if h2:  grp[key][1] = True
        kg = sum(1 for k in grp if not grp[k][1])
        if na:
            rows[n] = (na, ka, kh, len(grp), kg)
            T['a']+=na; T['ka']+=ka; T['kh']+=kh; T['g']+=len(grp); T['kg']+=kg
    for n in sorted(rows):
        if n in (105,108,112,117,120) or n % 25 == 0 or n == nmax:
            na, ka, kh, ng, kg = rows[n]
            print("   %5d %9d %9d %9d %9d %9d" % (n, na, ka, kh, ng, kg))
    print("   ---- totals over D in [%d,%d] ----" % (nmin, nmax))
    print("   V-assignments %d ; killed unconditionally (no integer N>=2): %d (%.2f%%)"
          % (T['a'], T['ka'], 100.0*T['ka']/max(1,T['a'])))
    print("   V-assignments killed under H2 (no integer N in [4,16]): %d (%.2f%%)"
          % (T['kh'], 100.0*T['kh']/max(1,T['a'])))
    print("   groups (n,m,M_*,V_s) %d ; killed under H2 (every assignment dead): %d (%.2f%%)"
          % (T['g'], T['kg'], 100.0*T['kg']/max(1,T['g'])))
    dead = [n for n in rows if rows[n][4] == rows[n][3]]
    print("   degrees D with EVERY group killed under (UNI)+H2: %s" % (dead if dead else "NONE"))
    return rows

def run_general(nmax, nmin=48, Nlo=4, Nhi=16, CAP=40000):
    """HYPOTHESIS-FREE version: bottom-major discs may carry DIFFERENT lower-V data.
       N = sum_B V_2(B) q(B) with sum_B V_2(B) <= u.  Exact knapsack over Fractions,
       pruned to sums <= Nhi; CAP guards the state count (capped groups -> UNDECIDED,
       counted as SURVIVING, so the reported kill is a floor)."""
    print("\n== GENERAL (no (UNI)) knapsack:  N = sum_B V_2(B) q(B), sum V_2(B) <= u ==")
    tot=dict(g=0,k=0,c=0)
    rows={}
    for n in range(nmin, nmax+1):
        groups={}
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok(): continue
            groups.setdefault((m, Ms, S.V[S.s]), []).append((S.V[2], qval(S), S.u))
        ng=nk=nc=0
        for key, items in groups.items():
            ng += 1
            u = int(items[0][2])
            cand = sorted(set((v, q) for (v, q, _) in items if v*q <= Nhi))
            reach = {0: {F(0)}}
            capped = False; hit = False
            for tv in range(0, u+1):
                if tv not in reach: continue
                for s0 in list(reach[tv]):
                    for (v, q) in cand:
                        if tv+v > u: continue
                        s1 = s0 + v*q
                        if s1 > Nhi: continue
                        reach.setdefault(tv+v, set())
                        if len(reach[tv+v]) >= CAP: capped=True; continue
                        reach[tv+v].add(s1)
                        if s1.denominator == 1 and Nlo <= s1 <= Nhi: hit = True
                if hit: break
            if hit: continue
            if capped: nc += 1; continue
            nk += 1
        rows[n]=(ng,nk,nc); tot['g']+=ng; tot['k']+=nk; tot['c']+=nc
    print("   %5s %9s %12s %10s" % ("D","groups","killed(H2)","capped"))
    for n in sorted(rows):
        ng,nk,nc = rows[n]
        if n in (105,108,112,117,120) or n%25==0 or n==nmax:
            print("   %5d %9d %12d %10d" % (n,ng,nk,nc))
    print("   totals D in [%d,%d]: groups %d, killed %d (%.2f%%), capped/UNDECIDED %d"
          % (nmin,nmax,tot['g'],tot['k'],100.0*tot['k']/max(1,tot['g']),tot['c']))
    return rows
