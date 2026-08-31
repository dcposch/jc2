#!/usr/bin/env python3
"""Emit the exact Singular system for the `(mu,r,D)=(2,2,8)` cell.

Actual expansion is deliberately AWS-only. The generator writes the Singular
program to stdout; the hardened runner owns every evidence file.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import platform
import re
from pathlib import Path

import sympy as sp


LANE_RE = re.compile(r"quartic_inv_mu2_d8_[A-Za-z0-9][A-Za-z0-9_-]{0,95}")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"REFUSE: {message}")


def require_aws_route() -> str:
    require(platform.system() == "Linux", "actual generation requires Linux")
    vendor_path = Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text(encoding="utf-8").strip() if vendor_path.exists() else ""
    require(vendor == "Amazon EC2", f"actual generation requires AWS EC2, got {vendor!r}")
    lane = os.environ.get("JC2_QUARTIC_INVARIANT_ROUTE_TOKEN", "")
    require(LANE_RE.fullmatch(lane) is not None, "missing or malformed registered route token")
    return lane


def canonical_sha(expressions: list[sp.Expr], labels: list[str] | None = None) -> str:
    if labels is None:
        labels = [str(index) for index in range(len(expressions))]
    require(len(labels) == len(expressions), "canonical-hash label count drifted")
    payload = "\n".join(
        f"{label}={sp.srepr(sp.expand(expression))}"
        for label, expression in zip(labels, expressions)
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def singular_text(characteristic: int, profile: str, engine: str) -> str:
    require(characteristic >= 0, "characteristic must be nonnegative")
    require(
        characteristic == 0 or bool(sp.isprime(characteristic)),
        "positive characteristic must be prime",
    )
    require(profile in ("actual", "target3", "drop_last"), "unknown profile")
    require(engine in ("std", "slimgb"), "engine must be std or slimgb")

    params = sp.symbols("a1:11 b1:11")
    left_params = params[:10]
    right_params = params[10:]
    x, y = sp.symbols("x y")

    A = x**2
    U = x + x**3 * y
    Z = 2 * y + x**2 * y**2
    require(sp.expand(U**2 - A - A**2 * Z) == 0, "invariant-ring relation drifted")

    basis_labels = [
        "1", "A", "A2", "A3", "A4", "Z", "AZ", "A2Z", "Z2",
        "U", "AU", "A2U", "UZ",
    ]
    basis = [
        sp.Integer(1), A, A**2, A**3, A**4, Z, A * Z, A**2 * Z,
        Z**2, U, A * U, A**2 * U, U * Z,
    ]
    require(len(basis) == 13 and len(set(map(sp.srepr, basis))) == 13, "basis cardinality drifted")
    require(
        all(sp.Poly(expression, x, y).total_degree() <= 8 for expression in basis),
        "basis escaped the pullback degree bound",
    )
    require(
        [sp.Poly(expression, x, y).total_degree() for expression in basis]
        == [0, 2, 4, 6, 8, 4, 6, 8, 8, 4, 6, 8, 8],
        "basis pullback degrees drifted",
    )

    free_basis = [A, A**2, A**3, A**4, A * Z, A**2 * Z, Z**2, A * U, A**2 * U, U * Z]
    require(len(free_basis) == 10, "normalized free basis drifted")
    require(
        len(left_params) == len(right_params) == len(free_basis),
        "normalized parameter count drifted",
    )
    H1 = U + sum(coefficient * monomial for coefficient, monomial in zip(left_params, free_basis))
    H2 = Z + sum(coefficient * monomial for coefficient, monomial in zip(right_params, free_basis))
    jacobian = sp.expand(sp.diff(H1, x) * sp.diff(H2, y) - sp.diff(H1, y) * sp.diff(H2, x))
    require(sp.Poly(jacobian, x, y).coeff_monomial(1) == 2, "normalized constant Jacobian drifted")

    target = 3 if profile == "target3" else 2
    polynomial = sp.Poly(sp.expand(jacobian - target), x, y)
    raw_equations: list[sp.Expr] = []
    equations: list[sp.Expr] = []
    seen: set[str] = set()
    for _monomial, coefficient in polynomial.terms():
        normalized = sp.expand(coefficient)
        if normalized == 0:
            continue
        raw_equations.append(normalized)
        key = sp.srepr(normalized)
        if key in seen:
            continue
        seen.add(key)
        equations.append(normalized)

    if profile == "target3":
        require(
            len(raw_equations) == 58 and len(equations) == 54,
            "target-3 equation count drifted: "
            f"observed raw/unique {len(raw_equations)}/{len(equations)}, "
            "expected 58/54",
        )
        require(any(equation in (1, -1) for equation in equations), "target-3 unit mutation lost")
    else:
        require(
            len(raw_equations) == 57 and len(equations) == 53,
            "actual equation count drifted: "
            f"observed raw/unique {len(raw_equations)}/{len(equations)}, "
            "expected 57/53",
        )
        require(all(equation not in (1, -1) for equation in equations), "actual cell became trivially empty")
        require(
            all(set(equation.free_symbols) & set(params) for equation in equations),
            "unexpected parameter-independent coefficient; inspect before Groebner",
        )

    raw_equation_sha = canonical_sha(raw_equations)
    unique_equation_sha = canonical_sha(equations)
    if profile == "drop_last":
        equations = equations[:-1]
        require(len(equations) == 52, "drop-last mutation failed")

    def singular(expression: sp.Expr) -> str:
        return sp.sstr(expression, order="lex").replace("**", "^")

    variables = ",".join(str(value) for value in params)
    equation_lines = ",\n  ".join(singular(equation) for equation in equations)
    groebner_call = "std(I)" if engine == "std" else "slimgb(I)"
    basis_sha = canonical_sha(basis, basis_labels)

    return "\n".join(
        [
            "// schema=JC2_QUARTIC_INVARIANT_MU2_D8_V1",
            f"// characteristic={characteristic}",
            f"// profile={profile}",
            f"// engine={engine}",
            f"// basis_sha256={basis_sha}",
            f"// raw_equation_sha256={raw_equation_sha}",
            f"// unique_equation_sha256={unique_equation_sha}",
            f"// raw_equation_count={len(raw_equations)}",
            f"// ideal_generator_count={len(equations)}",
            f"ring r={characteristic},({variables}),dp;",
            "option(redSB);",
            "ideal I =",
            f"  {equation_lines};",
            'print("SCHEMA=JC2_QUARTIC_INVARIANT_MU2_D8_V1");',
            f'print("PROFILE={profile}");',
            f'print("BASIS_SHA256={basis_sha}");',
            f'print("RAW_EQUATION_SHA256={raw_equation_sha}");',
            f'print("UNIQUE_EQUATION_SHA256={unique_equation_sha}");',
            'print("INPUT_SIZE");',
            "size(I);",
            f"ideal G={groebner_call};",
            'print("GROEBNER_SIZE");',
            "size(G);",
            'print("DIMENSION");',
            "dim(G);",
            'print("GROEBNER_BASIS");',
            "G;",
            'print("INPUT_REMAINDER");',
            "reduce(I,G);",
            "quit;",
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, required=True)
    parser.add_argument("--profile", choices=("actual", "target3", "drop_last"), required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), required=True)
    arguments = parser.parse_args()
    require_aws_route()
    print(singular_text(arguments.characteristic, arguments.profile, arguments.engine), end="")


if __name__ == "__main__":
    main()
