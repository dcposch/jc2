#!/usr/bin/env python3
"""The order-nu operator of the bottom-disc Jacobian expansion.

  y = sigma_1 + pi x^{-delta_1},  f = x^A Phi(x,pi), g = x^B Gamma(x,pi),
  A = d kappa, B = e kappa, kappa = (1-delta_1)/(d+e), A + B - 1 + delta_1 = 0.
  [f,g] = A Phi Gamma' - B Phi' Gamma + x(Phi_x Gamma' - Phi' Gamma_x) = c.
  Order x^{-nu}:   L_nu(Phi_nu, Gamma_nu) = -R_nu   with
  L_nu(F,G) = (A-nu) F P' - B F' P + A Q G' - (B-nu) Q' G,  P = Gamma_0, Q = Phi_0.
  Dividing by kappa and putting nut = nu/kappa:
  Lt(F,G) = (d-nut) F P' - e F' P + d Q G' - (e-nut) Q' G.
"""
import sympy as sp
pi, nut = sp.symbols('pi nut')

def Lt(F, G, P, Q, d, e):
    return sp.expand((d-nut)*F*sp.diff(P,pi) - e*sp.diff(F,pi)*P
                     + d*Q*sp.diff(G,pi) - (e-nut)*sp.diff(Q,pi)*G)

def kernel(P, Q, d, e, degF, degG):
    aa = sp.symbols('aa0:%d' % (degF+1)); bb = sp.symbols('bb0:%d' % (degG+1))
    F = sum(aa[i]*pi**i for i in range(degF+1))
    G = sum(bb[i]*pi**i for i in range(degG+1))
    L = sp.Poly(Lt(F,G,P,Q,d,e), pi)
    eqs = [sp.expand(c) for c in L.all_coeffs()]
    unk = list(aa)+list(bb)
    M = sp.Matrix([[sp.expand(sp.diff(q,v)) for v in unk] for q in eqs])
    return M, unk, F, G

if __name__ == "__main__":
    d, e = 2, 3
    P = pi**3 + 3*pi; Q = pi**2 + 2          # the V=1 solution of (BOTTOM)
    gam = sp.expand(d*Q*sp.diff(P,pi) - e*sp.diff(Q,pi)*P)
    print("(BOTTOM) check: d Q P' - e Q' P =", gam, " (P=%s, Q=%s)" % (P,Q))
    for (degF, degG) in [(3,4)]:
        M, unk, F, G = kernel(P,Q,d,e,degF,degG)
        print("\n-- kernel of Lt on deg F <= %d, deg G <= %d (%d unknowns) --" % (degF,degG,len(unk)))
        ns = M.nullspace()
        print("   generic nut: nullity =", len(ns))
        for v in ns:
            Fv = sp.simplify(F.subs(dict(zip(unk, list(v)))))
            Gv = sp.simplify(G.subs(dict(zip(unk, list(v)))))
            print("     F =", sp.factor(sp.simplify(Fv)), "   G =", sp.factor(sp.simplify(Gv)))
        # where does the rank drop?
        r = M.rank()
        print("   generic rank =", r, "of", M.shape)
        mins = set()
        for c in sp.Matrix(M).minor_submatrix(0,0).shape and []: pass
        # find special nut by det of a maximal square submatrix system
        import itertools
        rows = list(range(M.shape[0]))
        specials = set()
        for cols in itertools.combinations(range(M.shape[1]), r):
            for rws in itertools.combinations(rows, r):
                sub = M[list(rws), list(cols)]
                dt = sp.factor(sp.expand(sub.det()))
                if dt != 0:
                    for f_, _m in sp.factor_list(dt)[1]:
                        if nut in f_.free_symbols:
                            for s in sp.solve(f_, nut): specials.add(sp.nsimplify(s))
                    break
            else:
                continue
            break
        print("   nut values where the rank can drop (from one maximal minor):", sorted(specials, key=str))
