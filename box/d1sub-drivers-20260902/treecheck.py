#!/usr/bin/env python3
"""
D1-SUBTREE -- part C: the TREE-level control.

For a polynomial automorphism in Moh's gauge the curves {f=0} and {g=0} are lines,
each with ONE place at infinity, so all n roots of g (resp. all m roots of f) in C<t>
are CONJUGATE.  Then the per-root contact multisets are the full multisets divided by
n, and both are computable EXACTLY by resultants + Newton polygon:

    Res_y( g(x,y), g(x,y+z) ) = prod_{i,j} (rho_i + z - rho_j)   -> {ord_t(rho_i-rho_j)}
    Res_y( g(x,y), f(x,y+z) ) = prod_{i,k} (rho_i + z - phi_k)   -> {ord_t(rho_i-phi_k)}

so  lambda_g(delta) = sum_j min(delta, ord(rho_1-rho_j)),
    lambda_f(delta) = sum_k min(delta, ord(rho_1-phi_k))
are exact piecewise-linear functions.  We check, on the tree and not on the resultant:

  (T1)  JAC-ARC        lambda_f(delta) + lambda_g(delta) <= delta - 1 for every delta
  (T2)  at the frontier delta^0 (lambda_g = 0):  lambda_f(delta^0) = delta^0 - 1
  (T3)  FRONTIER-N     N = n * (1 - delta^0)^+       (= 1 for an automorphism)
  (T4)  the D_1 pinning: with delta_1 the LAST level at which lambda_g still has
        slope > 1 (the bottom major disc of the degenerate tower),
        floor = (1-delta_1) + lambda_g(delta_1)  =  -(m/n) lambda_g(delta_1) = ceiling
        and  N = a_1 * that value.
  (T5)  NEGATIVE: for non-Keller pairs (T1) is VIOLATED.
"""
import sys
from fractions import Fraction as F
import sympy as sp
from jacfibre import (x, y, z, c1, c2, newton_orders, gauge, in_gauge, jac,
                      geometric_degree, build_auto, AUTO_WORDS, check, NCHECK, FAILURES)

def contact_multiset(g, h):
    """{ord_t(rho_i - eta_k)} over roots rho_i of g and eta_k of h, both monic in y."""
    R = sp.expand(sp.resultant(sp.expand(g), sp.expand(h).subs(y, y+z), y))
    return newton_orders(R, z, x)          # None entries = the exact coincidences (ord = +oo)

def lam(delta, ords, n):
    """(1/n) * sum over the multiset of min(delta, o); None means o = +infinity."""
    s = F(0)
    for o in ords: s += delta if o is None else min(delta, o)
    return s / n

def frontier(ords, n, lo=F(-2), hi=F(4)):
    """the delta with lam(delta) = 0, by bisection on the piecewise-linear function."""
    brk = sorted(set([o for o in ords if o is not None]))
    pts = [lo] + brk + [hi]
    for i in range(len(pts)-1):
        a, b = pts[i], pts[i+1]
        va, vb = lam(a, ords, n), lam(b, ords, n)
        if va <= 0 <= vb and vb != va:
            sl = (vb-va)/(b-a)
            return a + (0-va)/sl
        if va == 0: return a
    return None

def run():
    print("\n-- CONTROL T: the tree of a Keller pair (automorphisms, all roots conjugate) --")
    print("   %-24s %3s %3s %8s %8s %10s %8s %6s" %
          ("word","m","n","delta^0","1-d^0","N=n(1-d0)","delta_1","a_1"))
    for w in AUTO_WORDS:
        P, Q = build_auto(w)
        if sp.total_degree(P) > sp.total_degree(Q): P, Q = Q, P
        f, g = gauge(P, Q)
        if f is None: check("gauge %s" % w, False); continue
        m = sp.degree(sp.Poly(f, y), y); n = sp.degree(sp.Poly(g, y), y)
        N = geometric_degree(f, g)
        gg = contact_multiset(g, g)        # n^2 entries, n of them None (i=j)
        gf = contact_multiset(g, f)        # n*m entries
        check("gg size %s" % w, len(gg) == n*n, "%d" % len(gg))
        check("gf size %s" % w, len(gf) == n*m, "%d" % len(gf))
        check("lam_g(-1) = -n  %s" % w, lam(F(-1), gg, n) == -n, "%s" % lam(F(-1), gg, n))
        check("lam_f(-1) = -m  %s" % w, lam(F(-1), gf, n) == -m, "%s" % lam(F(-1), gf, n))
        d0 = frontier(gg, n)
        check("frontier exists %s" % w, d0 is not None)
        if d0 is None: continue
        # (T1) JAC-ARC everywhere, sampled at every breakpoint and midpoint
        brk = sorted(set([o for o in gg+gf if o is not None])) + [d0]
        samples = sorted(set(brk + [(-1+b)/2 for b in brk] + [F(-1)]))
        bad = [d for d in samples if lam(d, gf, n) + lam(d, gg, n) > d - 1]
        check("JAC-ARC on the tree %s" % w, not bad, "violated at %s" % bad[:3])
        # (T2) equality at the frontier
        check("lambda_f(delta^0) = delta^0 - 1  %s" % w,
              lam(d0, gf, n) == d0 - 1, "%s vs %s" % (lam(d0, gf, n), d0-1))
        # (T3) FRONTIER-N
        check("N = n(1-delta^0)^+  %s" % w, n*max(F(0), 1-d0) == N,
              "%s vs %s" % (n*max(F(0),1-d0), N))
        # (T4) D_1, INTRINSICALLY: the unique level where the floor  (1-delta)+lambda_g
        #      and the ceiling  -(m/n) lambda_g  cross, i.e. lambda_g(delta) = -n(1-delta)/(n+m).
        #      That is exactly Moh's Lemma 5.2 at r = 1 (M_1 = -m) -- no Def 5.1(3) needed.
        brkg = sorted(set([o for o in gg if o is not None]))
        d1 = None
        pts = [F(-1)] + brkg + [d0]
        for i in range(len(pts)-1):
            a, b = pts[i], pts[i+1]
            fa = lam(a, gg, n) + F(n, n+m)*(1-a); fb = lam(b, gg, n) + F(n, n+m)*(1-b)
            if fa <= 0 <= fb and fb != fa:
                d1 = a + (0-fa)*(b-a)/(fb-fa); break
            if fa == 0: d1 = a; break
        check("delta_1 exists %s" % w, d1 is not None)
        if d1 is None: continue
        lg1 = lam(d1, gg, n); lf1 = lam(d1, gf, n)
        floor = (1-d1) + lg1; ceil = -F(m, n)*lg1
        check("Lemma 5.2 at r=1 (intrinsic) %s" % w, lg1 == -F(n*(1-d1), n+m), "%s" % lg1)
        check("floor = ceiling at delta_1 %s" % w, floor == ceil, "%s vs %s" % (floor, ceil))
        check("PROPORTIONALITY lambda_f(delta_1)=(m/n)lambda_g %s" % w,
              lf1 == F(m, n)*lg1, "%s vs %s" % (lf1, F(m, n)*lg1))
        check("pinned c_rho = 1-delta^0 = floor %s" % w, (1-d0) == floor,
              "%s vs %s" % (1-d0, floor))
        # D1-STAR: below delta_1 the slope of lambda_g is 1 and lambda_f is CONSTANT
        mid = (d1 + d0)/2
        check("D1-STAR slope(lambda_g)=1 below delta_1 %s" % w,
              lam(d0, gg, n) - lam(mid, gg, n) == d0 - mid, "")
        check("D1-STAR lambda_f constant below delta_1 %s" % w,
              lam(d0, gf, n) == lam(d1, gf, n), "%s vs %s" % (lam(d0,gf,n), lam(d1,gf,n)))
        a1 = sum(1 for o in gg if o is None or o >= d1)//n
        check("N = (n/a_1) discs * a_1 * floor %s" % w, n*floor == N,
              "a_1=%s floor=%s N=%s" % (a1, floor, N))
        print("   %-24s %3d %3d %8s %8s %10s %8s %6s" %
              (str(w), m, n, d0, 1-d0, n*max(F(0),1-d0), d1, a1))

    print("\n-- CONTROL T5 (NEGATIVE): N = sum(1-delta^0)^+ must FAIL off the Keller locus,")
    print("   and the general law  c = 1 - delta^0 - ord_t J(tau)  must hold there --")
    print("   %-24s %-10s %5s %8s %10s %10s %s" %
          ("(f,g)","J","N","delta^0","sum(1-d0)+","ord J(tau)","corrected"))
    negs = [(y, sp.expand(x**2 + y**3)), (y, sp.expand(x**3 + y**4)),
            (sp.expand(y**2 - x), sp.expand(y**3 - x**2*y + x)),
            (sp.expand(y**2 + x*y + 1), sp.expand(y**3 + x**2))]
    for (f, g) in negs:
        if not (in_gauge(f) and in_gauge(g)):
            print("   %-24s   (skipped: not in gauge)" % str((f, g))); continue
        m = sp.degree(sp.Poly(f, y), y); n = sp.degree(sp.Poly(g, y), y)
        J = jac(f, g); keller = (J.free_symbols == set())
        N = geometric_degree(f, g)
        gg = contact_multiset(g, g)
        d0 = frontier(gg, n)
        naive = n*max(F(0), 1-d0)
        oJ = newton_orders(sp.expand(sp.resultant(sp.expand(g)-c2, z - J, y)), z, x)
        oJ = sorted(set(oJ))
        corr = n*max(F(0), 1 - d0 - oJ[0]) if len(oJ) == 1 else None
        check("Keller-characterisation (%s,%s)" % (f, g), (naive == N) == keller,
              "N=%s naive=%s keller=%s" % (N, naive, keller))
        if corr is not None:
            check("general law c = 1-delta^0-ord J (%s,%s)" % (f, g), corr == N,
                  "corr=%s N=%s" % (corr, N))
        print("   %-24s %-10s %5s %8s %10s %10s %s" %
              (str((f, g))[:24], str(J)[:10], N, d0, naive, oJ, corr))

if __name__ == "__main__":
    run()
    print("\n== %d checks, %d failures ==" % (NCHECK[0], len(FAILURES)))
    if FAILURES:
        for nm, dt in FAILURES: print("   FAILED: %s  %s" % (nm, dt))
        sys.exit(1)
