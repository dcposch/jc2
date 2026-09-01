#!/usr/bin/env python3
"""bmfact_selfcheck.py

Sage-free (sympy) self-checks for the realized (9,6,2) curve
    q = t^6 + 8 t^2
    p = t^9 + 12 t^5 + 24 t
and its implicit equation F(x,y) = Res_t(p(t)-x, q(t)-y).

This is desk algebra, not SIROCCO and not the Hurwitz enumeration.
Run:  python3 box/bmfact_selfcheck.py
"""
from __future__ import annotations

import sys

import sympy as sp


def main() -> int:
    t, x, y, z, u = sp.symbols("t x y z u")
    poly_p = t**9 + 12 * t**5 + 24 * t
    poly_q = t**6 + 8 * t**2

    print("=== (9,6,2) curve identity ===")
    ident = sp.expand(poly_p**2 - poly_q**3 - 64 * poly_q - 64 * t**2)
    print("p^2 - q^3 - 64 q - 64 t^2 =", ident)
    assert ident == 0, "identity failed"

    deriv_p = sp.diff(poly_p, t)
    deriv_q = sp.diff(poly_q, t)
    print("p' =", sp.factor(deriv_p))
    print("gcd(p, p') =", sp.gcd(poly_p, deriv_p))
    print("gcd(p', q') =", sp.gcd(deriv_p, deriv_q))
    assert sp.gcd(poly_p, deriv_p) == 1
    assert sp.gcd(deriv_p, deriv_q) == 1

    print()
    print("=== resultant F = Res_t(p-x, q-y) ===")
    # Ring map, declared: coefficients QQ; eliminate param_t from
    # (p(t)-x, q(t)-y) in QQ[x,y][t]. Matching names are not a proof.
    poly_F_raw = sp.resultant(poly_p - x, poly_q - y, t)
    poly_F = sp.Poly(sp.expand(poly_F_raw), x, y, domain=sp.QQ)
    print("content(F) =", poly_F.content())
    print("deg_x =", poly_F.degree(x), "deg_y =", poly_F.degree(y),
          "total_degree =", poly_F.total_degree())
    print("is_irreducible over QQ =", poly_F.is_irreducible)
    F_expr = poly_F.as_expr()
    print("F =")
    print(" ", F_expr)
    assert poly_F.content() == 1
    assert poly_F.degree(x) == 6
    assert poly_F.degree(y) == 9
    assert poly_F.total_degree() == 9
    assert poly_F.is_irreducible is True

    print()
    print("=== identity substitution cross-check ===")
    # On the curve, x^2 - y^3 - 64 y = 64 t^2. Set
    #   w = x^2 - y^3 - 64 y
    # and eliminate t via y = t^6 + 8 t^2 = u^3 + 8 u with u = t^2 = w/64:
    #   (w/64)^3 + 8 (w/64) - y = 0
    #   w^3 + 32768 w - 262144 y = 0.
    w_expr = x**2 - y**3 - 64 * y
    G_expr = sp.expand(w_expr**3 + 32768 * w_expr - 262144 * y)
    poly_G = sp.Poly(G_expr, x, y, domain=sp.QQ)
    print("G := (x^2-y^3-64y)^3 + 32768(x^2-y^3-64y) - 262144 y")
    print("content(G) =", poly_G.content())
    print("F == G is", poly_F == poly_G)
    assert poly_F == poly_G, "resultant does not match the identity substitution"

    print()
    print("=== leading coefficient in y (vertical asymptotes?) ===")
    poly_F_in_y = sp.Poly(F_expr, y, domain=sp.QQ[x])
    print("lc_y(F) =", poly_F_in_y.LC())
    assert poly_F_in_y.LC() == -1
    print("lc_y(F) is the nonzero constant -1: no vertical asymptotes.")
    print("Sage braid_monodromy therefore projects over the first variable")
    print("without a linear change of coordinates.")

    print()
    print("=== F(0,y): the unique affine fibre carrying the four nodes ===")
    F_at_zero = sp.factor(F_expr.subs(x, 0))
    print("F(0,y) =", F_at_zero)
    # -y (y^4 + 96 y^2 + 1536)^2
    # y=0 is the smooth point t=0; the quartic-squared is four double roots.
    u_roots = sp.solve(u**2 + 96 * u + 1536, u)
    print("y^2-values of the four nodes:", u_roots)
    for u_val in u_roots:
        print("  y^2 =", u_val, "=", sp.simplify(u_val),
              "numerical", complex(u_val))
    assert F_at_zero == -y * (y**4 + 96 * y**2 + 1536) ** 2

    print()
    print("=== disc_y F  (affine discriminant of the x-projection) ===")
    disc_expr = sp.discriminant(poly_F_in_y)
    disc_poly = sp.Poly(sp.together(disc_expr), x, domain=sp.QQ)
    print("content(disc_y F) =", disc_poly.content())
    print("deg(disc_y F) =", disc_poly.degree())
    factored = sp.factor(disc_poly.as_expr())
    print("disc_y F =", factored)
    sqf = sp.sqf_list(disc_poly.as_expr())
    print("sqf_list =", sqf)
    assert disc_poly.degree() == 16
    # 2^108 * 3^9 * x^8 * (3^9 x^8 + 2^{24}*5*43 x^4 + 2^{47})
    C_const = disc_poly.content()
    print("content factorization:", sp.factorint(int(C_const)))
    octic = 19683 * x**8 + 3607101440 * x**4 + 140737488355328
    print("octic = 3^9 x^8 + 3607101440 x^4 + 140737488355328")
    print("  19683 =", sp.factorint(19683))
    print("  3607101440 =", sp.factorint(3607101440))
    print("  140737488355328 =", sp.factorint(140737488355328))
    reconstructed = sp.Integer(C_const) * x**8 * octic
    assert sp.expand(reconstructed - disc_poly.as_expr()) == 0

    print()
    print("=== every root of disc_y F, including infinity ===")
    print("Finite roots:")
    print("  (N) x = 0 with multiplicity 8.")
    print("      Geometric cause: four ordinary nodes, all on the line x=0.")
    print("      Each node is two smooth branches with non-vertical tangents,")
    print("      local model y^2 ~ x^2, disc valuation 2 per node, total 8.")
    print("      Square-free support still includes x=0 (once).")
    u_tang = sp.solve(19683 * u**2 + 3607101440 * u + 140737488355328, u)
    print("  (T) the eight simple vertical-tangency values: x^4 in")
    for u_val in u_tang:
        print("        ", u_val)
        print("          numerical", complex(u_val), "is_zero", u_val == 0)
        assert u_val != 0
    print("      Two distinct nonzero (negative real) values of x^4, each with")
    print("      four distinct fourth roots: eight distinct nonzero x.")
    print("      Multiplicity 1 each. Square-free. Confirmed by")
    print("      Res_t(p', x-p) = 19683 * octic, degree 8.")
    res_tang = sp.resultant(deriv_p, x - poly_p, t)
    print("      Res_t(p', x-p) =", sp.factor(sp.expand(res_tang)))
    print("  No other finite roots: deg disc = 8 + 8 = 16 = 2 delta_aff + d - 1.")
    print("Infinity:")
    print("  lc_y(F) = -1 does not vanish, so x=infinity is not a root of")
    print("  the affine polynomial disc_y F.")
    Fhom = sp.expand(z**9 * F_expr.subs({x: x / z, y: y / z}))
    print("  F_hom(X,Y,Z) |_{Z=0} =", sp.factor(Fhom.subs(z, 0)))
    print("  Dbar meets L_infty only at [1:0:0], intersection multiplicity 9.")
    print("  (Place multiplicity a = 3; this is not an affine discriminant root.)")
    print("  The ramification of t |-> p(t) at t=infinity is 8, realised as")
    print("  the product of the nine finite geometric-basis braids (rho_inf),")
    print("  not as an extra finite critical value.")
    print()
    print("verbatim table:")
    print("  root                multiplicity   geometric type")
    print("  ------------------- -------------- ------------------------------")
    print("  x = 0               8              four A1 nodes, one fibre")
    print("  eight roots of      1 each         simple vertical tangencies")
    print("  3^9 x^8 + 2^{24}*5*43 x^4 + 2^{47}")
    print("  x = infinity        (not a root)   lc_y(F)=-1; accounted in rho_inf")
    print("  total affine degree 16             = 8*1 + 4*2")
    print()
    print("SELFCHECK-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
