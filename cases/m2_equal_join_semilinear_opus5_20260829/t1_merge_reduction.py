#!/usr/bin/env python3
"""Exact symbolic reduction of Prop 8.1(iv) at a general merge vertex.

Ground identity (BOOK-OFFAXIS.md R1.0 normal form; cases/l1_ode_check.py
lines 5-15 for the normalization):

    rho * p * q' - p' * q = C * p,     rho = deg(p)/deg(q),  C != 0,

with the merge pattern (nu >= 2, so eta || q by R1.0)

    p = eta^eps * Pfull(t),   Pfull = prod_i (t - A_i)^{n_i},   t = eta^nu
    q = eta     * Rad(t)*S(t),  Rad = prod_i (t - A_i),  deg S = lex.

THEOREM (T1-GEN, proved in the report and verified symbolically below).
Dividing by eta^eps*Pfull, the identity is EQUIVALENT to the reduced equation

    (rho - eps)*W + rho*nu*t*W_t - nu*t*S*sum_i n_i*prod_{i'!=i}(t - A_{i'}) = C
                                                                   (T1-GEN)
with W = Rad*S.  For equal multiplicities n_i = mu it collapses to

    (rho - eps)*Rad*S + nu*(rho - mu)*t*Rad_t*S + rho*nu*t*Rad*S_t = C
                                                                   (T1-EQ)

which is exactly `xmodel/sol-td7-law.md` eq. (3) at (r, mu_orbit) = (1, 1)
and exactly `cases/l1_ode_check.py` family A at (eps, mu) = (0, 1).

For the C = 0 equal-arrival family (lex = 0) (T1-EQ) further collapses to the
one-line criterion

    r*Rad(t) - t*Rad_t(t) = const   <=>   Rad(t) = t^r - A,
    C = -nu*r*(mu - eps)*A/dq  != 0  iff  A != 0.                  (T1-EQJOIN)
"""
from fractions import Fraction as Fr

from polyexact import Poly


# variable layout: 0 = eta, 1.. = symbolic coefficients
def _t_poly(n, nu):
    return Poly.var(n, 0, nu)


def build_equalmu_symbols(r, lex):
    """Symbols: eta, pi_0..pi_{r-1} (Rad monic of degree r),
    sigma_0..sigma_{lex-1} (S monic of degree lex)."""
    n = 1 + r + lex
    names = ["eta"] + ["pi%d" % j for j in range(r)] + ["sg%d" % j for j in range(lex)]
    return n, names


def rad_and_S_equalmu(n, r, lex, nu):
    """Rad(t), S(t) and their t-derivatives, as polynomials in eta."""
    t = _t_poly(n, nu)
    Rad = t.pow(r)
    Rad_t = Poly.const(n, r) * t.pow(r - 1) if r >= 1 else Poly.const(n, 0)
    for j in range(r):
        Rad = Rad + Poly.var(n, 1 + j) * t.pow(j)
        if j >= 1:
            Rad_t = Rad_t + Poly.const(n, j) * Poly.var(n, 1 + j) * t.pow(j - 1)
    S = t.pow(lex)
    S_t = Poly.const(n, lex) * t.pow(lex - 1) if lex >= 1 else Poly.const(n, 0)
    for j in range(lex):
        S = S + Poly.var(n, 1 + r + j) * t.pow(j)
        if j >= 1:
            S_t = S_t + Poly.const(n, j) * Poly.var(n, 1 + r + j) * t.pow(j - 1)
    return Rad, Rad_t, S, S_t


def verify_T1_EQ(r, mu, eps, lex, nu):
    """Symbolically verify (T1-EQ) for equal multiplicities.

    Returns (ok, residual_terms).  `ok` means the polynomial identity

        rho*p*q' - p'*q  ==  eta^eps * Rad^mu * REDUCED

    holds identically in eta AND in the symbolic pattern coefficients."""
    n, _ = build_equalmu_symbols(r, lex)
    t = _t_poly(n, nu)
    Rad, Rad_t, S, S_t = rad_and_S_equalmu(n, r, lex, nu)
    eta = Poly.var(n, 0)
    dp = eps + nu * r * mu
    dq = 1 + nu * (r + lex)
    rho = Fr(dp, dq)

    p = eta.pow(eps) * Rad.pow(mu)
    q = eta * Rad * S
    lhs = Poly.const(n, rho) * p * q.diff(0) - p.diff(0) * q

    reduced = (Poly.const(n, rho - eps) * Rad * S
               + Poly.const(n, nu) * Poly.const(n, rho - mu) * t * Rad_t * S
               + Poly.const(n, rho * nu) * t * Rad * S_t)
    rhs = eta.pow(eps) * Rad.pow(mu) * reduced
    resid = lhs - rhs
    return resid.is_zero(), len(resid.d)


def verify_T1_GEN(mults, eps, lex, nu):
    """Symbolically verify (T1-GEN) with symbolic roots A_1..A_len(mults)
    and arbitrary multiplicities `mults`."""
    nroots = len(mults)
    n = 1 + nroots + lex
    t = _t_poly(n, nu)
    eta = Poly.var(n, 0)
    A = [Poly.var(n, 1 + i) for i in range(nroots)]
    Rad = Poly.const(n, 1)
    for i in range(nroots):
        Rad = Rad * (t - A[i])
    Pfull = Poly.const(n, 1)
    for i in range(nroots):
        Pfull = Pfull * (t - A[i]).pow(mults[i])
    S = t.pow(lex)
    S_t = Poly.const(n, lex) * t.pow(lex - 1) if lex >= 1 else Poly.const(n, 0)
    for j in range(lex):
        S = S + Poly.var(n, 1 + nroots + j) * t.pow(j)
        if j >= 1:
            S_t = S_t + Poly.const(n, j) * Poly.var(n, 1 + nroots + j) * t.pow(j - 1)
    W = Rad * S
    # W_t  =  Rad_t*S + Rad*S_t
    Rad_t = Poly.const(n, 0)
    for i in range(nroots):
        term = Poly.const(n, 1)
        for i2 in range(nroots):
            if i2 != i:
                term = term * (t - A[i2])
        Rad_t = Rad_t + term
    W_t = Rad_t * S + Rad * S_t
    # sum_i n_i prod_{i'!=i}(t - A_{i'})
    dlog = Poly.const(n, 0)
    for i in range(nroots):
        term = Poly.const(n, mults[i])
        for i2 in range(nroots):
            if i2 != i:
                term = term * (t - A[i2])
        dlog = dlog + term

    dp = eps + nu * sum(mults)
    dq = 1 + nu * (nroots + lex)
    rho = Fr(dp, dq)
    p = eta.pow(eps) * Pfull
    q = eta * W
    lhs = Poly.const(n, rho) * p * q.diff(0) - p.diff(0) * q
    reduced = (Poly.const(n, rho - eps) * W
               + Poly.const(n, rho * nu) * t * W_t
               - Poly.const(n, nu) * t * S * dlog)
    rhs = eta.pow(eps) * Pfull * reduced
    resid = lhs - rhs
    return resid.is_zero(), len(resid.d)


def eqjoin_T1_solution(r, mu, eps, nu):
    """Closed-form T1 verdict on the C = 0 equal-arrival family (lex = 0).

    Returns a dict with the exact forced pattern and the constant C as a
    multiple of A := -pi_0.  Cap-free and parametric: the coefficient list is
    derived, not searched."""
    dp = eps + nu * r * mu
    dq = 1 + nu * r
    rho = Fr(dp, dq)
    # coefficient of t^j in  (rho-eps)*Rad + nu*(rho-mu)*t*Rad_t
    coeffs = {}
    for j in range(r + 1):
        coeffs[j] = (rho - eps) + Fr(nu) * j * (rho - mu)
    forced_zero = [j for j in range(1, r) if coeffs[j] != 0]
    return {
        "dp": dp, "dq": dq, "rho": rho,
        "top_coeff_r": coeffs[r],                 # must vanish identically
        "coeff_j": {j: coeffs[j] for j in range(r + 1)},
        "forced_zero_pi": forced_zero,            # pi_j must vanish for these j
        "C_over_A": -coeffs[0],                   # C = coeffs[0]*pi_0 = -coeffs[0]*A
        "forced_Rad": "t^%d - A" % r,
        "alive": coeffs[0] != 0,
    }


def eqjoin_T1_symbolic_criterion(r, mu, eps, nu):
    """Verify symbolically that dq*REDUCED == nu*(mu-eps)*(r*Rad - t*Rad_t)
    for the lex = 0 equal-arrival shape, i.e. that the whole T1 content is the
    single elementary criterion `r*Rad - t*Rad_t = const`."""
    n, _ = build_equalmu_symbols(r, 0)
    t = _t_poly(n, nu)
    Rad, Rad_t, S, S_t = rad_and_S_equalmu(n, r, 0, nu)
    dp = eps + nu * r * mu
    dq = 1 + nu * r
    rho = Fr(dp, dq)
    reduced = (Poly.const(n, rho - eps) * Rad
               + Poly.const(n, nu) * Poly.const(n, rho - mu) * t * Rad_t)
    target = (Poly.const(n, Fr(nu * (mu - eps), dq))
              * (Poly.const(n, r) * Rad - t * Rad_t))
    return (reduced - target).is_zero()
