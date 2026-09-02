#!/usr/bin/env python3
"""(BOTTOM) / STAR condition at level 1 of Moh's tower:
      d Q P' - e Q' P = gamma  (nonzero constant),  deg P = eV, deg Q = dV.
   P = p_g = leading form of g at the general point of D_1 (a_1 = eV roots),
   Q = p_f = leading form of f there (b_1 = dV roots).
   Solve exactly (Groebner) for small (d,e,V); report #solutions mod the
   pi -> alpha pi scaling, and whether P, Q have simple roots."""
import sys, time
import sympy as sp

pi = sp.symbols('pi')

def solve_star(d, e, V, verbose=True):
    dP, dQ = e*V, d*V
    # P monic, no pi^{dP-1} term (translation used); Q monic.
    a = sp.symbols('a0:%d' % (dP-1))      # P = pi^dP + a_{dP-2} pi^{dP-2} + ... + a_0
    b = sp.symbols('b0:%d' % dQ)          # Q = pi^dQ + b_{dQ-1} pi^{dQ-1} + ... + b_0
    P = pi**dP + sum(a[i]*pi**i for i in range(dP-1))
    Q = pi**dQ + sum(b[i]*pi**i for i in range(dQ))
    W = sp.expand(d*Q*sp.diff(P,pi) - e*sp.diff(Q,pi)*P)
    Wp = sp.Poly(W, pi)
    eqs = [sp.expand(Wp.nth(j)) for j in range(1, (d+e)*V-1)]
    gamma = sp.expand(Wp.nth(0))
    unk = list(a)+list(b)
    t0 = time.time()
    sols = sp.solve(eqs, unk, dict=True)
    el = time.time()-t0
    out = []
    for s in sols:
        Ps = sp.expand(P.subs(s)); Qs = sp.expand(Q.subs(s)); gs = sp.expand(gamma.subs(s))
        free = sorted((Ps.free_symbols | Qs.free_symbols) - {pi}, key=str)
        out.append((Ps, Qs, gs, free))
    if verbose:
        print("  (d,e,V)=(%d,%d,%d): deg P=%d deg Q=%d, %d eqs, %d unknowns -> %d solution branches (%.1fs)"
              % (d,e,V,dP,dQ,len(eqs),len(unk),len(out),el))
    return out

def report(d, e, V):
    out = solve_star(d, e, V)
    good = 0
    for (Ps, Qs, gs, free) in out:
        # specialise remaining free parameters (the pi->alpha pi scaling) to 1
        sub = {f: 1 for f in free}
        P1 = sp.expand(Ps.subs(sub)); Q1 = sp.expand(Qs.subs(sub)); g1 = sp.simplify(gs.subs(sub))
        if g1 == 0:
            print("     branch gamma = 0  (DEGENERATE, not admissible)   free=%s" % free); continue
        dp = sp.degree(sp.Poly(P1,pi),pi); dq = sp.degree(sp.Poly(Q1,pi),pi)
        simpP = sp.simplify(sp.discriminant(sp.Poly(P1,pi),pi)) != 0
        simpQ = sp.simplify(sp.discriminant(sp.Poly(Q1,pi),pi)) != 0
        res = sp.simplify(sp.resultant(P1,Q1,pi))
        good += 1
        print("     ADMISSIBLE: gamma=%s  P=%s  Q=%s  simple(P)=%s simple(Q)=%s res(P,Q)=%s free=%s"
              % (g1, sp.factor(P1), sp.factor(Q1), simpP, simpQ, res!=0, free))
    print("     => %d admissible branch(es) with gamma != 0\n" % good)

if __name__ == "__main__":
    print("== (BOTTOM): d Q P' - e Q' P = gamma, gamma != 0 ==")
    for V in [1,2,3]:
        report(2,3,V)
