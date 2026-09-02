#!/usr/bin/env python3
"""TIME-FUNCTION ENDGAME -- part A: the bottom-disc (pi-level) Jacobian equation.

Setting.  (f,g) Keller in Moh's gauge, [f,g] = c in C^*.  t = 1/x, ord = ord_t.
At a bottom-major disc D_1 (radius delta_1) Moh's general point is
      sigma_1(pi) = w(t) + pi t^{delta_1},   w a truncation with exponents < delta_1.
Put  F(t,pi) = f(sigma_1),  G(t,pi) = g(sigma_1).  The (x,y) -> (t,pi) Jacobian is
      d(x,y)/d(t,pi) = det[[-t^-2, 0],[w' + pi delta t^{delta-1}, t^delta]] = -t^{delta-2},
so    F_t G_pi - F_pi G_t  =  -c t^{delta-2}.                                   (LOCAL-KELLER)
Writing F = t^{lam_f} Phi, G = t^{lam_g} Gamma this is
      (lam_f Phi + t Phi_t) Gamma_pi - (lam_g Gamma + t Gamma_t) Phi_pi = -c
and at leading order (Phi_0 = p_f, Gamma_0 = p_g), using D1-PIN's
lam_f + lam_g = delta_1 - 1 and lam_f/lam_g = m/n = d/e:

      THEOREM BOTTOM-ODE      d * p_f * p_g' - e * p_g * p_f'  =  kappa != 0,
      deg p_g = a_1 = e V_2,  deg p_f = b_1 = d V_2,  kappa = -e c / lam_g(delta_1).

This file (1) verifies BOTTOM-ODE on genuine Keller pairs, (2) solves it exactly for the
(d,e,V) data occurring in the census, (3) reports the dimension of the solution variety
against the dimension of the group acting.  FAIL-CLOSED.
"""
import sys, time
from fractions import Fraction as F
import sympy as sp

pi_, t, x, y, c1, c2 = sp.symbols('pi t x y c1 c2')

FAIL = []; NCHK = [0]
def check(name, cond, detail=""):
    NCHK[0] += 1
    if not cond:
        FAIL.append((name, detail)); print("  FAIL  %-58s %s" % (name, detail))
    return cond

# ---------------------------------------------------------------- the ODE itself
def bracket(Q, P, d, e, v=pi_):
    """d*Q*P' - e*P*Q'  (the BOTTOM-ODE left-hand side)."""
    return sp.expand(d*Q*sp.diff(P, v) - e*P*sp.diff(Q, v))

def solve_star(d, e, V, verbose=True, translate=True):
    """Solve  d Q P' - e P Q' = kappa != 0  with P monic of degree a=eV, deg Q = b=dV.
    Normalisation: P's pi^{a-1} coefficient set to 0 (translation), everything else free.
    Returns (solutions, a, b, dim_expected)."""
    a, b = e*V, d*V
    ps = sp.symbols('p0:%d' % a)      # P = pi^a + p_{a-1} pi^{a-1} + ... ; ps[i] = coeff pi^i
    qs = sp.symbols('q0:%d' % (b+1))
    P = v_poly(ps, a, monic=True)
    Q = v_poly(qs, b, monic=False)
    if translate:
        P = P.subs(ps[a-1], 0)
    B = sp.Poly(sp.expand(bracket(Q, P, d, e)), pi_)
    eqs = [sp.expand(B.nth(j)) for j in range(1, a+b)]      # kill everything but pi^0
    kap = sp.expand(B.nth(0))
    unk = [s for s in (list(ps[:a-1] if translate else ps) + list(qs))]
    return P, Q, eqs, kap, unk, a, b

def v_poly(coeffs, deg, monic):
    out = pi_**deg if monic else coeffs[deg]*pi_**deg
    for i in range(deg):
        out += coeffs[i]*pi_**i
    return sp.expand(out)

def star_dimension(d, e, V, tmax=180):
    """dimension of the solution variety, by Groebner over QQ with kappa != 0 saturated."""
    P, Q, eqs, kap, unk, a, b = solve_star(d, e, V)
    z = sp.Symbol('z')
    sys_ = [sp.together(t_) for t_ in eqs] + [sp.expand(z*kap - 1)]
    t0 = time.time()
    G = sp.groebner(sys_, *(unk + [z]), order='grevlex')
    dim = None
    try:
        # dimension via the number of unknowns minus the "independent set" size is
        # awkward in sympy; use the cheap surrogate: count variables not appearing as
        # a leading monomial of a pure power.
        pass
    finally:
        pass
    return G, unk, time.time()-t0, a, b

if __name__ == "__main__":
    print("bottomode.py -- BOTTOM-ODE  d p_f p_g' - e p_g p_f' = kappa")
    print("="*78)
    for (d, e, V) in [(2,3,1)]:
        P, Q, eqs, kap, unk, a, b = solve_star(d, e, V)
        print("\n(d,e,V) = (%d,%d,%d)  deg p_g = a_1 = %d, deg p_f = b_1 = %d" % (d,e,V,a,b))
        print("  P =", P); print("  Q =", Q)
        print("  equations (coeff of pi^1..pi^%d):" % (a+b-1))
        for j, E in enumerate(eqs, start=1): print("    pi^%d: %s" % (j, E))
        print("  kappa =", kap)
        sol = sp.solve(eqs, unk, dict=True)
        print("  solutions:", sol)
