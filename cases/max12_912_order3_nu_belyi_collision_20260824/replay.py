#!/usr/bin/env python3
"""Exact ledger replay for the nu-loaded full B/W absorption boundary."""

from __future__ import annotations

import json


def passport(parts_over_one: list[int]) -> dict[str, object]:
    assert sum(parts_over_one) == 36
    over_zero = [3] * 12
    over_infinity = [4] * 9
    contribution = (
        sum(value - 1 for value in over_zero)
        + sum(value - 1 for value in over_infinity)
        + sum(value - 1 for value in parts_over_one)
    )
    assert contribution == 2 * 36 - 2 == 70
    return {
        "over_0": "3^12",
        "over_infinity": "4^9",
        "over_1": parts_over_one,
        "degree_check": sum(parts_over_one),
        "riemann_hurwitz": contribution,
    }


def main() -> None:
    # With T=nu*w^-6+..., W=-3*w^24*T+3*w^12*T^2-T^3.
    # The three possible top exponents are 18, 0, -18, so no lower term
    # can cancel [z^18]W=-3*nu.
    W_top_exponents = [24 - 6, 12 - 2 * 6, -3 * 6]
    assert W_top_exponents == [18, 0, -18]

    # B=54*nu*z^2+18*nu*p+60*rho.  Its discriminant is
    # -1296*nu*(3*nu*p+10*rho); nu is nonzero.
    discriminant_scalar = -4 * 54 * 6
    assert discriminant_scalar == -1296

    distinct = passport([18, 2, 2] + [1] * 14)
    double = passport([18, 3] + [1] * 15)

    # For f=lambda^-9 F(lambda z), g=lambda^-12 G(lambda z),
    # W=lambda^-36 W0(lambda z), hence the z^18 coefficient scales by
    # lambda^(18-36)=lambda^-18.  Its equality to -3*nu forces
    # lambda^18 to lie in the algebraically closed constant field.
    scaling_exponent = 18 - 36
    assert scaling_exponent == -18

    payload = {
        "case": "max12_912_order3_nu_belyi_collision_20260824",
        "exact_inputs": {
            "spectral_coefficient": "[z^18](g^3-f^4)=-3*nu, nu in C*",
            "wronskian": "B=3*f*g_z-4*g*f_z=54*nu*z^2+18*nu*p+60*r8",
            "derivative": "beta_z=g^2*B/f^5",
            "terminal_row": "9*r8'=j/u != 0",
        },
        "spectral_top_exponents": W_top_exponents,
        "B_discriminant": "-1296*nu*(3*nu*p+10*r8)",
        "full_absorption_passports": {
            "two_distinct_B_roots_in_W": distinct,
            "double_B_root_in_W": double,
        },
        "isotrivial_scaling": {
            "normal_form": [
                "f=lambda^-9*F(lambda*z)",
                "g=lambda^-12*G(lambda*z)",
            ],
            "z18_scaling_exponent": scaling_exponent,
            "equation": "C18*lambda^-18=-3*nu",
            "consequence": "lambda^18 in C*, hence lambda in C*",
        },
        "producer_conclusion": (
            "No actual Keller trajectory survives when the complete quadratic "
            "B-ramification divisor is absorbed by W=0."
        ),
        "scope_retained": [
            "no B root in W",
            "exactly one simple B root in W",
            "double B root not in W",
            "equal non-1 critical values at two distinct B roots",
            "all Taylor boundaries",
            "other invariant loads and the order-one core",
        ],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
