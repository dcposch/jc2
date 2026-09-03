#!/usr/bin/env python3
"""Exact algebra checks for the h-adic ramification-absorption receiver.

All Groebner calculations are over QQ.  Saturation is encoded only through
an explicit Rabinowitsch generator; no ``sat()`` wrapper is used.
"""
from __future__ import annotations

import sympy as sp


gamma, pi = sp.symbols("gamma pi")


def jac(f, g):
    """[f,g] = f_gamma*g_pi - f_pi*g_gamma."""
    return sp.expand(sp.diff(f, gamma)*sp.diff(g, pi)
                     - sp.diff(f, pi)*sp.diff(g, gamma))


def identity_checks():
    h = sp.Function("h")(gamma, pi)
    beta = sp.Function("beta")(gamma, pi)
    aa = sp.Function("A")(gamma, pi)
    bb = sp.Function("B")(gamma, pi)
    alpha = sp.Function("alpha")(gamma, pi)
    rho = sp.Function("rho")(gamma, pi)
    rr = sp.Function("R")(gamma, pi)
    P = h**3 + aa*h + bb
    Q = h**2 + 2*beta
    U = 2*jac(h, 3*beta-aa)
    V = 2*(jac(aa, beta)-jac(h, bb))
    W = 2*(aa*jac(h, beta)+jac(bb, beta))
    raw_ok = sp.simplify(sp.expand(jac(P, Q) - (h**2*U+h*V+W))) == 0

    # The second identity uses beta^2=alpha*h+rho only through its bracket
    # consequence 2*beta*[h,beta]=h*[h,alpha]+[h,rho].
    lhs = jac((h**3 + 3*beta*h + sp.Rational(3, 2)*alpha + rr), Q)
    rhs_before_relation = (-2*h*jac(h, rr) + 6*beta*jac(h, beta)
                           - 3*h*jac(h, alpha) + 3*jac(alpha, beta)
                           + 2*jac(rr, beta))
    expanded_ok = sp.simplify(sp.expand(lhs-rhs_before_relation)) == 0
    rhs_after_relation = (-2*h*jac(h, rr) + 3*(jac(alpha, beta)+jac(h, rho))
                          + 2*jac(rr, beta))
    relation_residual = sp.factor(sp.expand(rhs_before_relation-rhs_after_relation))
    print("RAW_BLOCK_IDENTITY", raw_ok)
    print("NORMALIZED_PRE_RELATION_IDENTITY", expanded_ok)
    print("NORMALIZED_RELATION_RESIDUAL", relation_residual)
    print("  (zero when beta^2-alpha*h-rho=0, after bracketing with h)")


def primitive_control():
    a, c, T = sp.symbols("a c T")
    Q0 = pi**2 + a*gamma**2
    P0 = pi**3 + sp.Rational(3, 2)*a*gamma**2*pi
    J0 = sp.factor(jac(P0, Q0))
    equations = [c+3*a**2, T*a-1]
    G = sp.groebner(equations, a, c, T, order="lex")
    point = {a: 1, c: -3, T: 1}
    matrix = sp.Matrix([[sp.diff(e, v).subs(point) for v in (a,c,T)] for e in equations])
    print("PRIMITIVE_J", J0)
    print("PRIMITIVE_RING", "QQ[a,c,T], lex")
    print("PRIMITIVE_IDEAL", equations)
    print("PRIMITIVE_BASIS_SIZE", len(list(G)))
    print("PRIMITIVE_CONTAINS_ONE", list(G) == [1])
    print("PRIMITIVE_POINT", point, "equations_zero", [sp.expand(e.subs(point)) for e in equations])
    print("PRIMITIVE_POINT_JACOBIAN_RANK", matrix.rank())


def inflation_control():
    a, s, c, T = sp.symbols("a s c T")
    h = pi**6 + s*pi + gamma
    beta = a*gamma**2/2
    aa = 3*beta
    bb = 0
    Q = sp.expand(h**2 + 2*beta)
    P = sp.expand(h**3 + aa*h + bb)
    J = sp.factor(jac(P, Q))
    W = sp.expand(2*(aa*jac(h, beta)+jac(bb, beta)))
    quo, rem = sp.Poly(W, pi, domain="EX").div(sp.Poly(h, pi, domain="EX"))
    target = sp.Poly(sp.expand(J-c*gamma**3), gamma, pi)
    equations = [sp.factor(v) for v in target.coeffs()]
    unique = []
    for equation in equations:
        if equation not in unique:
            unique.append(equation)
    sat_equations = unique + [T*a-1]
    G = sp.groebner(sat_equations, a, s, c, T, order="lex")
    lead = -18*a**2
    certificate = sp.expand((-T**2/sp.Integer(18))*lead - (T*a+1)*(T*a-1))
    print("INFLATION_h", h)
    print("INFLATION_J", J)
    print("INFLATION_U", 0, "INFLATION_V", 0)
    print("INFLATION_W_QUOTIENT_BY_h", quo.as_expr())
    print("INFLATION_W_REMAINDER", sp.factor(rem.as_expr()))
    print("INFLATION_RING", "QQ[a,s,c,T], lex")
    print("INFLATION_TARGET_GENERATORS", unique)
    print("INFLATION_SATURATION_GENERATOR", T*a-1)
    print("INFLATION_BASIS_SIZE", len(list(G)))
    print("INFLATION_CONTAINS_ONE", list(G) == [1])
    print("INFLATION_TWO_GENERATOR_CERTIFICATE", certificate)


def main():
    identity_checks()
    primitive_control()
    inflation_control()


if __name__ == "__main__":
    main()
