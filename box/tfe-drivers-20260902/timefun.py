#!/usr/bin/env python3
"""TIME-FUNCTION ENDGAME -- part D: the time function and the interpolation conditions,
tested exactly on genuine Keller pairs and on a non-Keller row.

JAC-FIBRE in the x-variable:  d/dx f(x,tau(x)) = J / g_y(x,tau(x))  on every root tau
of g - c_2.  Hence, with J = c a nonzero constant (Keller):

  (NOLOG)   the x^{-1} coefficient of  c / g_y(x,tau_i(x))  must VANISH   (else f(x,tau_i)
            has a log and is not a Puiseux series -- f is a polynomial, so this is a
            necessary condition on g);
  (TIME)    f(x,tau_i) = F_i(x) + a_i  with  F_i = int c dx / g_y(x,tau_i);
  (INTERP)  f = sum_i (F_i + a_i) prod_{j!=i} (y-tau_j)/(tau_i-tau_j), which must have
            y-degree exactly m < n and coefficients POLYNOMIAL in x.

Puiseux machinery: every branch here is either explicit (two-tower products) or comes
from a polynomial parametrisation of an automorphism fibre, so no Newton-Puiseux is
needed.  Series are Laurent series in z, with x = z^{-n}, computed exactly over Q(i,..).
"""
import sys
from fractions import Fraction as Fr
import sympy as sp

x, y, z, c1, c2, uu = sp.symbols('x y z c1 c2 u')

FAIL = []; NCHK = [0]
def check(name, cond, detail=""):
    NCHK[0] += 1
    if not cond: FAIL.append((name, detail)); print("  FAIL  %-56s %s" % (name, detail))
    return cond

# ------------------------------------------------------------------ Laurent series
def lser(expr, N):
    """Laurent expansion of expr in z about z=0, keeping exponents < N."""
    e = sp.expand(sp.series(sp.together(expr), z, 0, N).removeO())
    return sp.expand(e)

def coeff_of(expr, pw):
    return sp.expand(sp.expand(expr).coeff(z, pw))

def jac(f, g):
    return sp.expand(sp.diff(f,x)*sp.diff(g,y) - sp.diff(f,y)*sp.diff(g,x))

# ------------------------------------------------------------------ automorphisms
def inverse_auto(P, Q):
    """(P,Q) an automorphism of C^2; return (X(u,v), Y(u,v)) with P(X,Y)=u, Q(X,Y)=v."""
    u, v = sp.symbols('u v')
    sol = sp.solve([sp.Eq(P, u), sp.Eq(Q, v)], [x, y], dict=True)
    for s in sol:
        X, Y = sp.expand(s[x]), sp.expand(s[y])
        if sp.simplify(sp.expand(P.subs({x:X, y:Y}) - u)) == 0 and \
           sp.simplify(sp.expand(Q.subs({x:X, y:Y}) - v)) == 0:
            return X, Y, u, v
    return None, None, u, v

def revert(Xpoly, uvar, n, N):
    """Solve Xpoly(u) = z^{-n} for u as a Laurent series in z (branch with u ~ a/z)."""
    lc = sp.Poly(Xpoly, uvar).LC()
    a1 = sp.root(1/lc, n)
    u0 = a1/z
    for _ in range(8):
        Xu = lser(sp.expand(Xpoly.subs(uvar, u0)), N)
        num = lser(Xu - z**(-n), N)
        den = lser(sp.expand(sp.diff(Xpoly, uvar).subs(uvar, u0)), N)
        u1 = lser(sp.expand(u0 - sp.cancel(num/den)), N)
        if sp.expand(u1 - u0) == 0: break
        u0 = u1
    return sp.expand(u0)

def branch_shift(ser, zeta):
    """the conjugate branch z -> zeta*z."""
    return sp.expand(ser.subs(z, zeta*z))
