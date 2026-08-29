#!/usr/bin/env python3
"""Exact affine family of budget-fitting formal routes at the td=8 entry.

The unique off-axis header is type (2,3) with two identical
``(Lambda,a,b,nu)=(4,1,2,3)`` poles.  Each pole takes the priced (21,15)
step to ``(w,M)=(2/3,3)``.  The two equal arrivals merge in an affine family
indexed by ``t>=0`` and feed one uniform (85,35) trunk step to a legal
terminal.  This is a theorem inside the recorded book grammar, not a
realizability or landing theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from typing import Iterable


SCHEMA = "m2-td8-equal-join-route-family-r1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def ft(x: Fraction | int) -> str:
    q = Fraction(x)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def validate_A_step() -> dict[str, object]:
    w_parent = Fraction(3, 2)
    M_parent = 2
    l, nu, eps, k, Sm, lex = 2, 7, 0, 1, 1, 0
    dp = eps + nu * (l + Sm)
    dq = 1 + nu * (1 + k + lex)
    E = l * dq - dp
    kbar = l * w_parent * dq / E
    X = kbar * Fraction(dp, dq)
    w_child = l * w_parent * (dq - 1) / (nu * E)
    M_child = math.gcd(dp, dq)
    price = max(1, math.ceil(X - kbar))
    require((dp, dq, E) == (21, 15, 9), "A-step degree mismatch")
    require((kbar, X, w_child, M_child, price) ==
            (5, 7, Fraction(2, 3), 3, 2), "A-step frame mismatch")
    rho = kbar / dq
    require((kbar - rho) / nu == w_child, "A-step w definition failed")
    return {
        "shape": {"l": l, "nu": nu, "eps": eps, "k": k,
                  "Sm": Sm, "lex": lex, "dp": dp, "dq": dq, "E": E},
        "frame": {"nu": nu, "kbar": ft(kbar), "X": ft(X),
                  "rho": ft(rho), "w": ft(w_child), "M": M_child},
        "lambda_lower_bound": price,
    }


def validate_route(t: int) -> dict[str, object]:
    require(isinstance(t, int) and t >= 0, "t must be a nonnegative integer")
    incoming = validate_A_step()
    mu = 3
    w = Fraction(2, 3)
    nu_H = 7
    kbar_H = 5
    rho_H = Fraction(1, 3)

    # Equal-(mu,w) merge family.  nu_G == 1 mod 3 is the exact integrality
    # progression; starting at 4 keeps the family in the nu_G>=2 regime.
    nu_G = 4 + 3 * t
    dp_G = 2 * mu * nu_G
    dq_G = 2 * nu_G + 1
    E_edge = mu * dq_G - dp_G
    kbar_G = w * dq_G
    X_G = mu * (kbar_G - w)
    rho_G = X_G / dp_G
    M_G = math.gcd(dp_G, dq_G)
    w_tr = (kbar_G - rho_G) / nu_G
    T_G = 2 * mu

    require(E_edge == mu, "equal-join E mismatch")
    require(kbar_G.denominator == 1, "merge kbar is not integral")
    require(X_G / kbar_G == Fraction(dp_G, dq_G), "merge ratio mismatch")
    require((rho_G, M_G, w_tr) == (w, 3, Fraction(4, 3)),
            "merge reduced successor mismatch")
    require(M_G == math.gcd(dp_G, dq_G) and T_G % M_G == 0,
            "merge gcd/T law mismatch")
    require(math.gcd(M_G, nu_G) == 1, "merge gcd(M,nu) mismatch")
    require(mu * dq_G > dp_G and dp_G != mu * dq_G,
            "merge searrow/root law mismatch")

    # Full incoming case-II labels, not merely reduced-state equality.
    n_arr = nu_H * int(kbar_G) - kbar_H
    require(n_arr >= 1, "incoming edge label is not positive")
    require(Fraction(kbar_H + n_arr, nu_H) == kbar_G,
            "incoming kbar handshake mismatch")
    require(Fraction(mu * (rho_H + n_arr), nu_H) == X_G,
            "incoming X handshake mismatch")

    # Uniform dirty trunk step from (w,M)=(4/3,3).
    l, nu_F, eps, k, Sm, lex = 3, 17, 0, 1, 2, 0
    dp_F = eps + nu_F * (l + Sm)
    dq_F = 1 + nu_F * (1 + k + lex)
    E_F = l * dq_F - dp_F
    kbar_F = l * w_tr * dq_F / E_F
    X_F = kbar_F * Fraction(dp_F, dq_F)
    rho_F = kbar_F / dq_F
    w_terminal = (kbar_F - rho_F) / nu_F
    M_F = math.gcd(dp_F, dq_F)
    lambda_F = max(1, math.ceil(X_F / 2 - kbar_F))
    require((dp_F, dq_F, E_F, kbar_F, X_F, rho_F) ==
            (85, 35, 20, 7, 17, Fraction(1, 5)),
            "trunk step frame mismatch")
    require((w_terminal, M_F, lambda_F) == (Fraction(2, 5), 5, 2),
            "trunk terminal mismatch")

    # The parent-dependent label is affine and integral for every t.
    n_trunk = nu_G * int(kbar_F) - int(kbar_G)
    require(n_trunk == 22 + 17 * t and n_trunk >= 1,
            "trunk edge-label progression mismatch")
    require(Fraction(int(kbar_G) + n_trunk, nu_G) == kbar_F,
            "trunk kbar handshake mismatch")
    require(Fraction(rho_G + n_trunk, int(kbar_G) + n_trunk) ==
            Fraction(dp_F, l * dq_F), "trunk proportion mismatch")

    j = M_F * (1 - w_terminal)
    require(j == 3, "terminal j mismatch")
    psi = math.ceil(Fraction(M_F, int(j))) - 1
    lambda_total = 2 + 2 + 0 + lambda_F
    budget = 8 - 1 - psi
    require((psi, lambda_total, budget) == (1, 6, 6),
            "terminal budget mismatch")

    return {
        "t": t,
        "entry": {"type": [2, 3], "td": 8, "m": 2,
                  "poles": [[4, 1, 2, 3], [4, 1, 2, 3]]},
        "incoming_each": incoming,
        "merge": {
            "nu_G": nu_G, "dp": dp_G, "dq": dq_G, "M": M_G,
            "kbar": int(kbar_G), "X": int(X_G), "rho": ft(rho_G),
            "w_tr": ft(w_tr), "T": T_G,
            "incoming_edge_label_each": n_arr,
            "lambda_lower_bound": 0,
        },
        "trunk": {
            "dp": dp_F, "dq": dq_F, "nu": nu_F, "M": M_F,
            "kbar": int(kbar_F), "X": int(X_F), "rho": ft(rho_F),
            "parent_edge_label": n_trunk, "lambda_lower_bound": lambda_F,
        },
        "terminal": {"w": ft(w_terminal), "M": M_F,
                     "j": int(j), "psi": psi},
        "lambda_lower_bound_total": lambda_total,
        "lambda_budget_ceiling": budget,
        "recorded_budget_fit_at_equality": lambda_total == budget,
        "formal_route_verdict":
            "RECORDED_LOWER_BOUND_BUDGET_FITTING_SUPERSET_ALIVE",
    }


def family_certificate() -> dict[str, object]:
    samples = [validate_route(t) for t in (0, 1, 10)]
    payload: dict[str, object] = {
        "schema": SCHEMA,
        "parameter": "t in Z>=0",
        "merge_family": {
            "nu_G": "4+3*t",
            "dp": "24+18*t",
            "dq": "9+6*t",
            "M": 3,
            "kbar": "6+4*t",
            "X": "16+12*t",
            "rho": "2/3",
            "w_tr": "4/3",
            "incoming_edge_label_each": "37+28*t",
            "trunk_edge_label": "22+17*t",
        },
        "fixed_recorded_lambda_lower_bounds": {
            "two_incoming_chains": [2, 2],
            "merge": 0, "trunk": 2,
            "total": 6, "terminal_psi": 1,
            "td8_budget_ceiling": 6,
        },
        "samples": samples,
        "consequence": (
            "the fixed td=8 entry has infinitely many formal cells fitting "
            "all recorded lambda lower-bound filters but one reduced merge "
            "successor; a semilinear record and parametric equation are required"
        ),
        "firewall": {
            "prop_8_1_iv_solved": False,
            "configuration_realizable": False,
            "source_landing": False,
            "degree_bound": False,
            "jc2": False,
        },
    }
    body = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["certificate_sha256"] = hashlib.sha256(body).hexdigest()
    return payload


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    blob = json.dumps(family_certificate(), indent=2, sort_keys=True) + "\n"
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(blob)
    else:
        print(blob, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
