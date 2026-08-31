#!/usr/bin/env python3
"""Emit the exact Singular system for the `(mu,r,D)=(2,2,6)` pilot.

Actual generation is deliberately AWS-only.  The script writes only to
stdout; the hardened runner owns all evidence files.
"""

from __future__ import annotations

import argparse
import os
import platform
import re
from pathlib import Path

import sympy as sp


LANE_RE = re.compile(r"quartic_inv_mu2_d6_[A-Za-z0-9][A-Za-z0-9_-]{0,95}")


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


def singular_text(characteristic: int, jacobian_target: int, engine: str) -> str:
    require(characteristic >= 0, "characteristic must be nonnegative")
    require(
        characteristic == 0 or bool(sp.isprime(characteristic)),
        "positive characteristic must be prime",
    )
    require(jacobian_target in (2, 3), "Jacobian target must be 2 or planted mutation 3")
    require(engine in ("std", "slimgb"), "engine must be std or slimgb")

    params = sp.symbols("a1 a2 a3 a4 a5 b1 b2 b3 b4 b5")
    a1, a2, a3, a4, a5, b1, b2, b3, b4, b5 = params
    x, y = sp.symbols("x y")

    A = x**2
    U = x + x**3 * y
    Z = 2 * y + x**2 * y**2
    H1 = U + a1 * A + a2 * A**2 + a3 * A**3 + a4 * A * Z + a5 * A * U
    H2 = Z + b1 * A + b2 * A**2 + b3 * A**3 + b4 * A * Z + b5 * A * U
    jacobian = sp.expand(sp.diff(H1, x) * sp.diff(H2, y) - sp.diff(H1, y) * sp.diff(H2, x))

    require(sp.expand(jacobian.subs(x, 0)) == 2, "normalized first-jet identity drifted")
    polynomial = sp.Poly(sp.expand(jacobian - jacobian_target), x, y)

    equations: list[sp.Expr] = []
    seen: set[str] = set()
    for _monomial, coefficient in polynomial.terms():
        normalized = sp.expand(coefficient)
        if normalized == 0:
            continue
        key = sp.srepr(normalized)
        if key in seen:
            continue
        seen.add(key)
        equations.append(normalized)

    require(equations, "coefficient ideal unexpectedly empty")
    if jacobian_target == 2:
        require(all(eq not in (1, -1) for eq in equations), "normal system became the unit ideal")
    else:
        require(any(eq in (1, -1) for eq in equations), "planted target-3 mutation lost its unit")

    def singular(expr: sp.Expr) -> str:
        return sp.sstr(expr, order="lex").replace("**", "^")

    variables = ",".join(str(value) for value in params)
    equation_lines = ",\n  ".join(singular(eq) for eq in equations)
    groebner_call = "std(I)" if engine == "std" else "slimgb(I)"
    field = str(characteristic)

    return "\n".join(
        [
            f"// schema=JC2_QUARTIC_INVARIANT_MU2_D6_V1",
            f"// characteristic={characteristic}",
            f"// jacobian_target={jacobian_target}",
            f"// engine={engine}",
            f"// equation_count={len(equations)}",
            f"ring r={field},({variables}),dp;",
            "option(redSB);",
            "ideal I =",
            f"  {equation_lines};",
            'print("SCHEMA=JC2_QUARTIC_INVARIANT_MU2_D6_V1");',
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
    parser.add_argument("--jacobian-target", type=int, choices=(2, 3), required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), required=True)
    args = parser.parse_args()
    require_aws_route()
    print(singular_text(args.characteristic, args.jacobian_target, args.engine), end="")


if __name__ == "__main__":
    main()
