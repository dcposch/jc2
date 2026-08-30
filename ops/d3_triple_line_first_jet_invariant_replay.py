#!/usr/bin/env python3
"""Exact first-jet invariant gate for a normal triple-line cubic fibre.

This is a small symbolic replay.  It derives c4 and c6 from Fisher's Hessian
identity, rather than trusting hand-copied Aronhold formulae.  It proves only
a necessary first-jet condition; it does not construct a surface or a map.
"""

from __future__ import annotations

import ast
import json
import sys

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def coefficient(form, variables, powers):
    return sp.Poly(form, *variables).coeff_monomial(powers)


def hessian_covariant(form, variables):
    # Fisher normalization H'(F)=-1/2 det(d^2 F).
    return sp.expand(-sp.det(sp.hessian(form, variables)) / 2)


def derive(mutate_disc_sign: bool = False):
    x, y, z, t, u = sp.symbols("x y z t u")
    q0, q1, q2 = sp.symbols("q0 q1 q2")
    b0, b1, b2, b3 = sp.symbols("b0 b1 b2 b3")
    xyz = (x, y, z)

    # Fix the Hessian/invariant normalization on the split cubic.  Here
    # H(xyz)=-xyz, so the two pencil coefficients in (2.2) give c4=1,
    # c6=-1.
    xyz_form = x * y * z
    xyz_hessian = hessian_covariant(xyz_form, xyz)
    require(xyz_hessian == -xyz_form, "split-cubic Hessian normalization drifted")
    xyz_pencil = sp.Poly(
        hessian_covariant(xyz_form + u * xyz_hessian, xyz), u
    )
    require(
        sp.expand(xyz_pencil.coeff_monomial(u) - 3 * xyz_form) == 0,
        "split-cubic c4 normalization drifted",
    )
    require(
        sp.expand(xyz_pencil.coeff_monomial(u**2) + 3 * xyz_form) == 0,
        "split-cubic c6 normalization drifted",
    )

    quadratic = q0 * y**2 + q1 * y * z + q2 * z**2
    binary_cubic = b0 * y**3 + b1 * y**2 * z + b2 * y * z**2 + b3 * z**3
    first_jet = x * quadratic + binary_cubic
    form = x**3 + t * first_jet

    hessian = hessian_covariant(form, xyz)
    pencil_hessian = sp.Poly(
        hessian_covariant(form + u * hessian, xyz), u
    )
    pencil_linear = sp.expand(pencil_hessian.coeff_monomial(u))
    pencil_quadratic = sp.expand(pencil_hessian.coeff_monomial(u**2))

    form_x3 = coefficient(form, xyz, (3, 0, 0))
    hessian_x3 = coefficient(hessian, xyz, (3, 0, 0))
    linear_x3 = coefficient(pencil_linear, xyz, (3, 0, 0))
    quadratic_x3 = coefficient(pencil_quadratic, xyz, (3, 0, 0))
    require(form_x3 == 1, "rank-one central coefficient drifted")

    # From H'(lambda F+mu H'):
    # [mu] = 3 c4 F and [mu^2] = 6 c6 F - 3 c4 H'.
    c4 = sp.expand(linear_x3 / (3 * form_x3))
    c6 = sp.expand(
        (quadratic_x3 + 3 * c4 * hessian_x3) / (6 * form_x3)
    )
    require(not sp.denom(c4).has(x, y, z, t), "c4 acquired a variable denominator")
    require(not sp.denom(c6).has(x, y, z, t), "c6 acquired a variable denominator")

    c4_poly = sp.Poly(c4, t)
    c6_poly = sp.Poly(c6, t)
    require(
        all(c4_poly.coeff_monomial(t**degree) == 0 for degree in range(3)),
        "c4 rank-one vanishing order fell below three",
    )
    require(
        all(c6_poly.coeff_monomial(t**degree) == 0 for degree in range(4)),
        "c6 rank-one vanishing order fell below four",
    )

    mixed = sp.expand(
        6 * b0 * b2 * q2
        - 9 * b0 * b3 * q1
        - 2 * b1**2 * q2
        + b1 * b2 * q1
        + 6 * b1 * b3 * q0
        - 2 * b2**2 * q0
    )
    binary_discriminant = sp.expand(
        b1**2 * b2**2
        - 4 * b0 * b2**3
        - 4 * b1**3 * b3
        - 27 * b0**2 * b3**2
        + 18 * b0 * b1 * b2 * b3
    )
    c4_t3 = sp.expand(c4_poly.coeff_monomial(t**3))
    c6_t4 = sp.expand(c6_poly.coeff_monomial(t**4))
    require(sp.expand(c4_t3 - 24 * mixed) == 0, "c4 first-jet formula failed")
    expected_c6 = (216 if mutate_disc_sign else -216) * binary_discriminant
    require(
        sp.expand(c6_t4 - expected_c6) == 0,
        "binary discriminant sign/control failed",
    )

    squarefree = {b0: 0, b1: 1, b2: -1, b3: 0}
    double_root = {b0: 0, b1: 1, b2: 0, b3: 0}
    triple_root = {b0: 1, b1: 0, b2: 0, b3: 0}
    squarefree_disc = sp.expand(binary_discriminant.subs(squarefree))
    require(squarefree_disc != 0, "squarefree binary control lost discriminant")
    require(
        sp.expand(c6_t4.subs(squarefree)) != 0,
        "squarefree first jet was not eliminated",
    )
    require(
        sp.expand(c4_t3.subs(double_root) + 48 * q2) == 0,
        "double-root c4 specialization drifted",
    )
    require(
        sp.expand(c6_t4.subs(double_root)) == 0,
        "double-root discriminant specialization drifted",
    )
    require(
        sp.expand(c4_t3.subs(triple_root)) == 0
        and sp.expand(c6_t4.subs(triple_root)) == 0,
        "triple-root leading specialization drifted",
    )

    # Fail closed if a future edit introduces Python asserts.
    source_tree = ast.parse(open(__file__, encoding="utf-8").read())
    assert_count = sum(isinstance(node, ast.Assert) for node in ast.walk(source_tree))
    require(assert_count == 0, "replay contains optimization-sensitive asserts")

    return {
        "schema": "D3-TRIPLE-LINE-FIRST-JET/v1",
        "sympy_version": sp.__version__,
        "hessian_normalization": "-det(second derivatives)/2",
        "normalization_control_xyz": {"hessian": "-x*y*z", "c4": "1", "c6": "-1"},
        "central_form": "x^3",
        "normalized_first_jet": "x*(q0*y^2+q1*y*z+q2*z^2)+b0*y^3+b1*y^2*z+b2*y*z^2+b3*z^3",
        "c4_rank_one_vanishing_order": 3,
        "c6_rank_one_vanishing_order": 4,
        "c4_t3": str(sp.factor(c4_t3)),
        "c6_t4": str(sp.factor(c6_t4)),
        "binary_discriminant": str(sp.factor(binary_discriminant)),
        "controls": {
            "squarefree_yz_y_minus_z": {
                "binary_discriminant": str(squarefree_disc),
                "c6_t4": str(sp.expand(c6_t4.subs(squarefree))),
                "level_positive_possible": False,
            },
            "double_root_y2z": {
                "c4_t3": str(sp.factor(c4_t3.subs(double_root))),
                "necessary_condition": "q2=0",
            },
            "triple_root_y3": {
                "c4_t3": "0",
                "c6_t4": "0",
                "survives_first_jet_gate": True,
            },
        },
        "ast_assert_nodes": assert_count,
        "status": "PASS",
    }


def main() -> None:
    mutate = sys.argv[1:] == ["--mutate-disc-sign"]
    require(mutate or not sys.argv[1:], "unknown command-line argument")
    result = derive(mutate_disc_sign=mutate)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        print("FAIL:" + str(error), file=sys.stderr)
        raise SystemExit(1)
