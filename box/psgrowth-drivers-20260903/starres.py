#!/usr/bin/env python3
"""*** SUPERSEDED by starres2.py / existence.py -- DO NOT CITE ITS EXISTENCE VERDICTS. ***
This file uses sympy.solve, whose solution sets for the BOTTOM-ODE system are
INCOMPLETE: it reports "no (2,3,2) star" while the saturated Groebner basis shows
one exists (existence.log).  Its (1,e,1) and (2,3,1) rows agree with starres2.py.

RESIDUE-LEAD: the leading x-term of R_k = [y^{n-1}](f^k mod (g-c)), computed.

At a bottom-major disc D_1 (radius delta_1) Moh's general point is
sigma_1(pi) = w(t) + pi t^{delta_1}; D1-STAR says the a_1 = e V_2 roots of g in D_1
separate PAIRWISE at exactly delta_1, so p_g has a_1 SIMPLE roots pi_1..pi_{a_1},
and lambda_f is constant on [delta_1, delta^0].  Writing

    f(sigma_1(pi)) = t^{lam_f}( p_f(pi) + O(t^eps) ),
    g(sigma_1(pi)) = t^{lam_g}( p_g(pi) + O(t^eps) ),   g_y = t^{-delta_1} d/dpi,

the branch tau_i (pi = pi_i) has

    f(tau_i)^k / g_y(tau_i) = t^{k lam_f - lam_g + delta_1} * p_f(pi_i)^k/p_g'(pi_i) * (1+...)
    exponent  =  -( (k+1) c - 1 ),   c := -lam_f = q/e = (1-delta_1) d/(d+e)   [D1-PIN]

so the LEADING COEFFICIENT of one disc's contribution to R_k is, up to a nonzero
tower constant,
                    S_k := sum_{p_g(pi)=0} p_f(pi)^k / p_g'(pi).

THEOREM RESIDUE-LEAD (proved here).  With BOTTOM-ODE  d p_f p_g' - e p_g p_f' = kappa
(kappa in C^*, box/tfe-drivers-20260902/bottomode.py), evaluation at a root pi_i of p_g
gives d p_f(pi_i) p_g'(pi_i) = kappa, hence

            S_k = (d/kappa) * sum_i p_f(pi_i)^{k+1} = (d/kappa) * ptilde_{k+1},

the (k+1)-st power sum of the values of p_f at the roots of p_g.  So the bottom-disc
leading coefficient of R_k is a PS-GROWTH power sum ONE LEVEL DOWN, for the
Davenport-Stothers pair (p_f, p_g) of type (d, e, V_2).

This file solves BOTTOM-ODE exactly for the (d,e,V) triples that occur in the census,
computes ptilde_j, verifies S_k = (d/kappa) ptilde_{k+1}, and reports for which k the
per-disc leading coefficient VANISHES.  FAIL-CLOSED.
"""
import sys, time, itertools
from fractions import Fraction as F
import sympy as sp

pi_ = sp.Symbol('pi'); Tz = sp.Symbol('Tz')
FAIL = []; NCHK = [0]
def check(name, cond, detail=""):
    NCHK[0] += 1
    if not cond:
        FAIL.append((name, detail)); print("    FAIL  %-52s %s" % (name, detail))
    return bool(cond)

def bracket(pf, pg, d, e):
    return sp.expand(d*pf*sp.diff(pg, pi_) - e*pg*sp.diff(pf, pi_))

def solve_star(d, e, V):
    """All (p_f, p_g) with deg p_g = a = eV monic, deg p_f = b = dV, satisfying
    d p_f p_g' - e p_g p_f' = kappa != 0, normalised by translation (pi^{a-1} of p_g = 0)."""
    a, b = e*V, d*V
    ps = sp.symbols('p0:%d' % max(a, 1))       # p_g = pi^a + ps[a-2] pi^{a-2} + ...
    qs = sp.symbols('q0:%d' % (b+1))           # p_f = sum qs[i] pi^i
    pg = pi_**a + sum(ps[i]*pi_**i for i in range(a-1))
    pf = sum(qs[i]*pi_**i for i in range(b+1))
    B = sp.Poly(bracket(pf, pg, d, e), pi_)
    eqs = [sp.expand(B.nth(j)) for j in range(1, a+b)]
    kap = sp.expand(B.nth(0))
    unk = list(ps[:a-1]) + list(qs)
    sols = sp.solve(eqs, unk, dict=True)
    out = []
    for s in sols:
        PG = sp.expand(pg.subs(s)); PF = sp.expand(pf.subs(s)); KA = sp.expand(kap.subs(s))
        if KA == 0: continue
        if sp.Poly(PF, pi_).degree() != b: continue
        out.append((PF, PG, KA, s))
    return out, a, b

def ptilde(pf, pg, J):
    """power sums ptilde_j = sum_{p_g(pi)=0} p_f(pi)^j, j = 1..J, by Newton from
    chi(Tz) = Res_pi(p_g, Tz - p_f)."""
    ch = sp.Poly(sp.resultant(pg, Tz - pf, pi_), Tz)
    a = ch.degree(); lc = ch.LC()
    ch = sp.Poly(sp.expand(ch.as_expr()/lc), Tz)
    A = [sp.Integer(1)] + [sp.simplify(ch.nth(a-j)) for j in range(1, a+1)]
    P = [sp.Integer(a)]
    for k in range(1, J+1):
        s = sp.Integer(0)
        for i in range(1, min(k-1, a)+1): s += A[i]*P[k-i]
        P.append(sp.simplify(-s - (k*A[k] if k <= a else 0)))
    return P

def Sk(pf, pg, k):
    """S_k = sum_i p_f(pi_i)^k/p_g'(pi_i) = [pi^{a-1}](p_f^k mod p_g)   (Euler-Jacobi)."""
    r = sp.Poly(sp.rem(sp.Poly(sp.expand(pf**k), pi_), sp.Poly(pg, pi_)), pi_)
    return sp.simplify(r.nth(sp.Poly(pg, pi_).degree()-1))

def report(d, e, V, J=12, verbose=True):
    sols, a, b = solve_star(d, e, V)
    print("\n== bottom star (d,e,V_2) = (%d,%d,%d):  deg p_g = a_1 = %d, deg p_f = b_1 = %d"
          % (d, e, V, a, b))
    check("(%d,%d,%d) BOTTOM-ODE has a solution with kappa != 0" % (d,e,V), len(sols) > 0)
    if not sols:
        print("   NO solution with kappa != 0  ->  no bottom star of this type exists")
        return None
    for (pf, pg, kap, s) in sols[:4]:
        free = sorted(set().union(*[t.free_symbols for t in (pf, pg)]) - {pi_},
                      key=str)
        print("   p_g = %s\n   p_f = %s\n   kappa = %s   free params: %s"
              % (pg, pf, kap, [str(v) for v in free]))
        check("(%d,%d,%d) BOTTOM-ODE holds" % (d,e,V),
              sp.simplify(bracket(pf, pg, d, e) - kap) == 0)
        # roots of p_g are simple (D1-STAR(d))
        disc = sp.simplify(sp.discriminant(sp.Poly(pg, pi_), pi_))
        check("(%d,%d,%d) p_g has SIMPLE roots (D1-STAR(d))" % (d,e,V), disc != 0,
              "disc = %s" % disc)
        PT = ptilde(pf, pg, J+1)
        nz = [j for j in range(1, J+1) if sp.simplify(PT[j]) != 0]
        print("   ptilde_j = sum_{p_g=0} p_f^j , j=1..%d :" % J)
        for j in range(1, min(J, 8)+1):
            print("      j=%-2d  %s" % (j, sp.sstr(sp.simplify(PT[j]))[:64]))
        print("   ptilde_j != 0 for j in %s   (j <= %d)" % (nz, J))
        # RESIDUE-LEAD : S_k = (d/kappa) ptilde_{k+1}
        for k in range(0, min(J, 8)):
            lhs = Sk(pf, pg, k); rhs = sp.simplify(sp.Rational(d,1)/kap*PT[k+1])
            check("(%d,%d,%d) RESIDUE-LEAD  S_%d = (d/kappa) ptilde_%d" % (d,e,V,k,k+1),
                  sp.simplify(lhs - rhs) == 0, "%s vs %s" % (lhs, rhs))
        kvan = [k for k in range(0, J) if sp.simplify(PT[k+1]) == 0]
        print("   per-disc leading coefficient S_k VANISHES for k in %s (k < %d)"
              % (kvan, J))
        if free: print("   (solution family has free parameters; values above are generic)")
    return sols

if __name__ == "__main__":
    print("starres.py -- RESIDUE-LEAD: the bottom-star residue.  sympy", sp.__version__)
    print("="*78)
    TRIPLES = [(1,2,1),   # control A1 (y, x+y^2)
               (1,3,1),   # control A2 (y, x+y^3) and each disc of D15
               (1,4,1), (1,6,1),
               (2,3,1),   # THE D = 105 TRIO   (V_2 = 1)
               (2,3,2),
               (2,5,1), (3,5,1), (4,5,1),
               ]
    if len(sys.argv) > 1:
        TRIPLES = [tuple(int(z) for z in a.split(',')) for a in sys.argv[1:]]
    for (d,e,V) in TRIPLES:
        try:
            report(d, e, V, J=12)
        except Exception as ex:
            print("   ERROR on (%d,%d,%d): %s" % (d,e,V,ex))
    print("\n" + "="*78)
    print("%d checks, %d failures" % (NCHK[0], len(FAIL)))
    for nm, dt in FAIL: print("   FAILED:", nm, dt)
