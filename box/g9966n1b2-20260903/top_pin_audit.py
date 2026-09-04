#!/usr/bin/env python3
"""Exact corrected S5 top-pin derivation and branch-cover certificate."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b2-20260903"


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def sha256_text(payload: str) -> str:
    return hashlib.sha256(payload.encode()).hexdigest()


def recurrence(a: sp.Expr, b: sp.Expr) -> tuple[dict[int, sp.Expr], sp.Expr]:
    """Solve coefficients 0..13 in 3*h*theta'-13*h'*theta=h^2.

    Here h=z^3-a*z^2+b*z.  The coefficient of z^k is
      3(k-15)t[k-2] + a(29-3k)t[k-1] + b(3k-13)t[k].
    Since b is localized and 3k-13 is never zero for integral k, rows
    k=0..13 solve successively without a nonunit pivot.  Row k=14 is the
    sole compatibility row; k=15 vanishes identically.
    """
    rhs = {
        2: b**2,
        3: -2 * a * b,
        4: a**2 + 2 * b,
        5: -2 * a,
        6: sp.Integer(1),
    }
    solved: dict[int, sp.Expr] = {-2: sp.Integer(0), -1: sp.Integer(0)}
    for k in range(14):
        numerator = (
            rhs.get(k, 0)
            - 3 * (k - 15) * solved.get(k - 2, 0)
            - a * (29 - 3 * k) * solved.get(k - 1, 0)
        )
        solved[k] = sp.factor(numerator / (b * (3 * k - 13)))
    compatibility = sp.factor(
        -3 * solved[12] + a * (29 - 42) * solved[13]
    )
    return solved, compatibility


def main() -> None:
    z, s = sp.symbols("z s")

    one_solved, one_compat = recurrence(sp.Integer(2), sp.Integer(1))
    theta_one = sp.factor(sum(one_solved[k] * z**k for k in range(14)))
    h_one = z * (z - 1) ** 2
    one_identity = sp.expand(
        3 * h_one * sp.diff(theta_one, z)
        - 13 * sp.diff(h_one, z) * theta_one
        - h_one**2
    )
    if one_identity != 0 or one_compat != 0:
        raise AssertionError("[2] top-pin recurrence failed")

    split_solved, split_compat = recurrence(s + 1, s)
    split_num, split_den = map(sp.factor, sp.together(split_compat).as_numer_denom())
    expected_quadratic = s**2 - s + 1
    expected_sextic = (
        11 * s**6 - 33 * s**5 + 12 * s**4 + 31 * s**3
        + 12 * s**2 - 33 * s + 11
    )
    expected_num = -65 * (s - 1) ** 4 * expected_quadratic * expected_sextic
    if sp.expand(split_num - expected_num) != 0 or split_den != 8602 * s**10:
        raise AssertionError("unexpected [1,1] compatibility factorization")

    theta_split = sum(split_solved[k] * z**k for k in range(14))
    h_split = z * (z - 1) * (z - s)
    residual = sp.Poly(sp.together(
        3 * h_split * sp.diff(theta_split, z)
        - 13 * sp.diff(h_split, z) * theta_split
        - h_split**2
    ), z)
    residual_coefficients = {
        str(k): str(sp.factor(residual.coeff_monomial(z**k)))
        for k in range(16)
        if residual.coeff_monomial(z**k) != 0
    }
    if set(residual_coefficients) != {"14"}:
        raise AssertionError("the split top pin has an unrecorded compatibility row")

    q_irreducible = sp.factor(expected_quadratic) == expected_quadratic
    s_irreducible = sp.factor(expected_sextic) == expected_sextic
    branch_product = sp.expand(expected_quadratic * expected_sextic)
    payload = {
        "schema": "jc2.g9966n1b2.s5-top-pin/v1",
        "source": {
            "descent_target": "J_(gamma,pi)(G,F)=c*gamma^8",
            "citation": "Moh 1983 Proposition 6.3(3), printed p.197",
            "map": {"x": "gamma", "y": "pi"},
        },
        "identity": "3*h*d(theta)/dz-13*d(h)/dz*theta=h^2",
        "derivative_variable": "z",
        "partition_2": {
            "h": str(sp.expand(h_one)),
            "theta": str(theta_one),
            "theta_sha256": sha256_text(str(theta_one)),
            "identity_residual": str(one_identity),
            "compatibility": str(one_compat),
            "status": "UNIQUE_TOP_PIN",
        },
        "partition_1_1": {
            "h": str(sp.expand(h_split)),
            "solved_coefficients": {str(k): str(split_solved[k]) for k in range(14)},
            "constant_pivots": [str(3 * k - 13) for k in range(14)],
            "localized_factor": "s*(s-1)",
            "residual_coefficients": residual_coefficients,
            "compatibility_numerator": str(split_num),
            "compatibility_denominator": str(split_den),
            "nonlocalized_branch_product": str(branch_product),
            "branches": [str(expected_quadratic), str(expected_sextic)],
            "quadratic_irreducible_Q": q_irreducible,
            "sextic_irreducible_Q": s_irreducible,
            "quadratic_squarefree": sp.gcd(expected_quadratic, sp.diff(expected_quadratic, s)) == 1,
            "sextic_squarefree": sp.gcd(expected_sextic, sp.diff(expected_sextic, s)) == 1,
            "branch_cover": "V(q2*q6)=V(q2) union V(q6); neither q2 nor q6 is inverted",
        },
        "fallacy_controls": {
            "no_division_by_branch_factor": True,
            "only_s_and_s_minus_1_are_localized": True,
            "prime_symbol_is_not_used_for_derivative": True,
        },
    }
    output = HERE / "top-pin-audit.json"
    atomic_write(output, json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "PASS",
        "output": str(output.relative_to(ROOT)),
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "branches": payload["partition_1_1"]["branches"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
