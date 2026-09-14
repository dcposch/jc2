#!/usr/bin/env python3
"""Exact controls for the stage-7 nonlinear bridge lane.

The requested high-degree tame/two-infinity control is deliberately fail-closed:
such a plane automorphism does not exist.  We record separate positive controls
for high degree and for two collective coordinate points, plus the degenerate
two-factor top which the bridge must reject.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def total_leading(poly: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    degree = sp.total_degree(poly)
    return sp.expand(
        sum(term for term in sp.Add.make_args(sp.expand(poly)) if sp.total_degree(term) == degree)
    )


def jacobian(F: sp.Expr, G: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.expand(sp.diff(F, x) * sp.diff(G, y) - sp.diff(F, y) * sp.diff(G, x))


def main() -> None:
    x, y, pi, c = sp.symbols("x y pi c")

    # High-degree tame Keller control.  Its inverse is displayed and checked.
    F = x + y**6
    G = y + F**7
    inv_y = sp.Symbol("G") - sp.Symbol("F") ** 7
    inv_x = sp.Symbol("F") - inv_y**6
    X, Y = sp.symbols("F G")
    inverse_check = {
        "F_after_inverse": sp.expand((inv_x + inv_y**6).subs({sp.Symbol("F"): X, sp.Symbol("G"): Y})),
        "G_after_inverse": sp.expand(
            (inv_y + (inv_x + inv_y**6) ** 7).subs({sp.Symbol("F"): X, sp.Symbol("G"): Y})
        ),
    }

    # Affine Keller control with two distinct collective coordinate points.
    Fa = 2 * x + y
    Ga = x + y

    # Two-factor (99,66) top is not a Keller pair and must not pass vacuously.
    P = y**3 * (y - x) ** 8
    Fd = P**9
    Gd = P**6

    p = pi * (pi**2 - c)
    q1 = sp.integrate(-2 * p**3, pi)

    data = {
        "type": "EXACT-CONTROLS / FALLACY-v2",
        "us1": {
            "parent": "(64,48)",
            "reduced": "(16,12)",
            "u_s": 1,
            "bridge_rows": 0,
            "bridge_unknowns": 0,
            "status": "TRIVIAL[u_s=1] / SATISFIED",
        },
        "tame_high_degree": {
            "F": str(F),
            "G": str(G),
            "degrees": [int(sp.total_degree(F)), int(sp.total_degree(G))],
            "J": str(jacobian(F, G, x, y)),
            "leading_F": str(total_leading(F, x, y)),
            "leading_G": str(total_leading(G, x, y)),
            "inverse": ["y=G-F^7", "x=F-(G-F^7)^6"],
            "inverse_check": {key: str(value) for key, value in inverse_check.items()},
            "status": "SURVIVES[TAME-DEGREES-(6,42),J=1] / NOT-APPLICABLE[TWO-POINT-BRIDGE]",
        },
        "affine_two_collective_points": {
            "F": str(Fa),
            "G": str(Ga),
            "degrees": [1, 1],
            "J": str(jacobian(Fa, Ga, x, y)),
            "infinity_points": ["[1:-2:0]", "[1:-1:0]"],
            "status": "SURVIVES[TWO-INFINITY-AFFINE,J=1] / NOT-APPLICABLE[s=3,T2/T3]",
        },
        "requested_combined_control": {
            "exists": False,
            "reason": (
                "A non-affine tame plane automorphism has both leading coordinate forms "
                "as powers of one linear form; under Xu's stronger condition a coordinate "
                "itself cannot have two infinity points."
            ),
            "status": "OPEN[POSITIVE-TWO-INFINITY-BRIDGE-CONTROL: SPECIFICATION-INCOMPATIBLE-WITH-TAME-AUTOMORPHISMS]",
        },
        "degenerate_two_factor_top": {
            "P": "y^3*(y-x)^8",
            "degrees": [99, 66],
            "J_is_zero": jacobian(Fd, Gd, x, y) == 0,
            "G3_minus_F2_is_zero": sp.expand(Gd**3 - Fd**2) == 0,
            "status": "REJECTS[DEGENERATE-TWO-POINT-TOP,J=0]",
        },
        "source_identity": {
            "p": str(p),
            "q1_zero_constant": str(sp.factor(q1)),
            "q1_degree": int(sp.degree(q1, pi)),
            "q1_derivative_check": sp.expand(sp.diff(q1, pi) + 2 * p**3) == 0,
            "p10_q1_degree": int(sp.degree(p**10 * q1, pi)),
        },
    }
    assert data["tame_high_degree"]["J"] == "1"
    assert inverse_check == {"F_after_inverse": X, "G_after_inverse": Y}
    assert data["affine_two_collective_points"]["J"] == "1"
    assert data["degenerate_two_factor_top"]["J_is_zero"]
    assert data["source_identity"]["q1_derivative_check"]
    HERE.joinpath("controls.json").write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
