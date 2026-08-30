#!/usr/bin/env python3
"""Hardened replay for the D3 triple-line first-jet invariant gate.

Version 2 preserves the sealed v1 calculation and adds the two checks requested
by the independent hostile review: full Hessian-pencil membership and a
classical Weierstrass normalization anchor.
"""

from __future__ import annotations

import ast
import json
import sys

import sympy as sp

from d3_triple_line_first_jet_invariant_replay import (
    coefficient,
    derive as derive_v1,
    hessian_covariant,
    require,
)


def pencil_invariants(form, variables):
    """Recover c4,c6 from one nonzero cubic coefficient of the pencil."""

    u = sp.symbols("invariant_pencil_u")
    hessian = hessian_covariant(form, variables)
    pencil = sp.Poly(hessian_covariant(form + u * hessian, variables), u)
    control = next(
        monomial
        for monomial, value in sp.Poly(form, *variables).terms()
        if value != 0
    )
    form_control = coefficient(form, variables, control)
    hessian_control = coefficient(hessian, variables, control)
    linear = sp.expand(pencil.coeff_monomial(u))
    quadratic = sp.expand(pencil.coeff_monomial(u**2))
    c4 = sp.expand(coefficient(linear, variables, control) / (3 * form_control))
    c6 = sp.expand(
        (
            coefficient(quadratic, variables, control)
            + 3 * c4 * hessian_control
        )
        / (6 * form_control)
    )
    return hessian, linear, quadratic, c4, c6


def derive(mutate_membership_scale: bool = False):
    result = derive_v1(mutate_disc_sign=False)

    x, y, z, t = sp.symbols("x y z t")
    q0, q1, q2 = sp.symbols("q0 q1 q2")
    b0, b1, b2, b3 = sp.symbols("b0 b1 b2 b3")
    variables = (x, y, z)
    gate_form = x**3 + t * (
        x * (q0 * y**2 + q1 * y * z + q2 * z**2)
        + b0 * y**3
        + b1 * y**2 * z
        + b2 * y * z**2
        + b3 * z**3
    )
    hessian, linear, quadratic, c4, c6 = pencil_invariants(gate_form, variables)
    linear_scale = 2 if mutate_membership_scale else 3
    require(
        sp.expand(linear - linear_scale * c4 * gate_form) == 0,
        "linear Hessian-pencil membership failed",
    )
    require(
        sp.expand(quadratic - (6 * c6 * gate_form - 3 * c4 * hessian)) == 0,
        "quadratic Hessian-pencil membership failed",
    )

    # Classical anchor for Fisher's normalization.
    weierstrass_a, weierstrass_b = sp.symbols("weierstrass_a weierstrass_b")
    weierstrass = (
        y**2 * z
        - x**3
        - weierstrass_a * x * z**2
        - weierstrass_b * z**3
    )
    (
        weierstrass_hessian,
        weierstrass_linear,
        weierstrass_quadratic,
        weierstrass_c4,
        weierstrass_c6,
    ) = pencil_invariants(weierstrass, variables)
    require(
        sp.expand(weierstrass_c4 + 48 * weierstrass_a) == 0,
        "Weierstrass c4 normalization drifted",
    )
    require(
        sp.expand(weierstrass_c6 + 864 * weierstrass_b) == 0,
        "Weierstrass c6 normalization drifted",
    )
    require(
        sp.expand(weierstrass_linear - 3 * weierstrass_c4 * weierstrass) == 0,
        "Weierstrass linear pencil membership failed",
    )
    require(
        sp.expand(
            weierstrass_quadratic
            - (
                6 * weierstrass_c6 * weierstrass
                - 3 * weierstrass_c4 * weierstrass_hessian
            )
        )
        == 0,
        "Weierstrass quadratic pencil membership failed",
    )

    source_tree = ast.parse(open(__file__, encoding="utf-8").read())
    assert_count = sum(isinstance(node, ast.Assert) for node in ast.walk(source_tree))
    require(assert_count == 0, "v2 replay contains optimization-sensitive asserts")

    result["schema"] = "D3-TRIPLE-LINE-FIRST-JET/v2"
    result["pencil_membership"] = {
        "gate_linear": True,
        "gate_quadratic": True,
        "weierstrass_linear": True,
        "weierstrass_quadratic": True,
    }
    result["weierstrass_anchor"] = {"c4": "-48*a", "c6": "-864*b"}
    result["ast_assert_nodes"] = assert_count
    return result


def main() -> None:
    mutate = sys.argv[1:] == ["--mutate-membership-scale"]
    require(mutate or not sys.argv[1:], "unknown command-line argument")
    result = derive(mutate_membership_scale=mutate)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        print("FAIL:" + str(error), file=sys.stderr)
        raise SystemExit(1)
