#!/usr/bin/env python3
"""TIME-FUNCTION ENDGAME -- part C: the bottom star, solved.

THEOREM STAR-ABC (proved in the report).  With a = e V, b = d V,
     d P_f P_g' - e P_g P_f' = kappa != 0     (BOTTOM-ODE)
 <=> P_f, P_g, C := P_f^e - rho P_g^d are pairwise coprime and squarefree with
     deg C = V(de-d-e)+1                     (Mason-Stothers equality / Davenport-Stothers)
 <=> R = P_f^e/P_g^d : P^1 -> P^1 has degree deV and is branched over exactly three
     points, with profiles [e^{dV}] over 0, [d^{eV}] over infinity and
     [(d+e)V-1, 1^{V(de-d-e)+1}] over R(infinity).

CONSTRUCTION (used here).  Take P_f monic of degree b = dV with the coefficients of
pi^{-1},...,pi^{-(b-2)} of P_f^{e/d} equal to zero, and set P_g := [P_f^{e/d}]_{>=0}.
That is b-2 equations in b-2 essential unknowns (after translation and scaling).
"""
import sys, time, itertools
import sympy as sp
from sympy import Rational as R

pi_ = sp.Symbol('pi')

def frac_power_trunc(Qexpr, b, e, d, lo):
    """[Q^{e/d}] as a Laurent series in 1/pi down to pi^{lo}; Q monic of degree b."""
    s = sp.Symbol('s')                       # s = 1/pi
    Q = sp.Poly(Qexpr, pi_)
    # Q = pi^b * (1 + sum_{j>=1} q_{b-j} s^j)
    u = sum(Q.nth(b-j)*s**j for j in range(1, b+1))
    order = (e*b//d) - lo + 2
    ser = sp.series((1+u)**R(e, d), s, 0, order).removeO()
    ser = sp.expand(ser)
    out = {}
    P = sp.Poly(ser, s)
    for j in range(0, P.degree()+1):
        cj = sp.expand(P.nth(j))
        if cj != 0: out[e*b//d - j] = cj      # coefficient of pi^{deg - j}
    return out

def star_system(d, e, V, normalise_scale=True):
    b, a = d*V, e*V
    assert (e*b) % d == 0 and e*b//d == a
    qs = sp.symbols('q0:%d' % b)             # Q = pi^b + q_{b-2} pi^{b-2} + ... + q_0
    Q = pi_**b + sum(qs[i]*pi_**i for i in range(b-1))     # q_{b-1} := 0 (translation)
    unk = list(qs[:b-1])
    coeffs = frac_power_trunc(Q, b, e, d, -(b-2) if b >= 3 else 0)
    eqs = [sp.expand(coeffs.get(-j, 0)) for j in range(1, b-1)]     # pi^-1 ... pi^-(b-2)
    Pg = sp.expand(sum(c*pi_**k for k, c in coeffs.items() if k >= 0))
    return Q, Pg, eqs, unk, a, b

def verify(d, e, V, Qsol, Pgsol):
    W = sp.expand(d*Qsol*sp.diff(Pgsol, pi_) - e*Pgsol*sp.diff(Qsol, pi_))
    ok_const = (sp.degree(sp.Poly(W, pi_), pi_) <= 0) if W != 0 else False
    kap = sp.expand(W)
    C = sp.expand(Qsol**e - Pgsol**d)
    degC = sp.degree(sp.Poly(C, pi_), pi_) if C != 0 else -1
    sqfP = sp.degree(sp.gcd(Pgsol, sp.diff(Pgsol, pi_)), pi_) == 0
    sqfQ = sp.degree(sp.gcd(Qsol, sp.diff(Qsol, pi_)), pi_) == 0
    sqfC = sp.degree(sp.gcd(C, sp.diff(C, pi_)), pi_) == 0 if C != 0 else False
    return ok_const, kap, degC, V*(d*e-d-e)+1, sqfP, sqfQ, sqfC

def symmetry_order(Pol):
    """largest A with Pol = pi^{j0} * (polynomial in pi^A)."""
    P = sp.Poly(sp.expand(Pol), pi_)
    ex = [j for j in range(P.degree()+1) if sp.expand(P.nth(j)) != 0]
    if len(ex) < 2: return 0        # monomial: any A
    from math import gcd
    g = 0
    for j in ex[1:]: g = gcd(g, j-ex[0])
    return g
