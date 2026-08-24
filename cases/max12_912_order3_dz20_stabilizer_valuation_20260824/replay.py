#!/usr/bin/env python3
"""Exact integer replay for the (9,12) order-3 DZ20 valuation exclusion."""

from __future__ import annotations

import json
from math import gcd


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def stabilizer_rows() -> list[dict[str, object]]:
    # A deck transformation fixes the unique e=20 point over 1.  After
    # depression it is a scaling.  Its order divides both deg(beta)=36 and
    # the local ramification index 20.
    orders = divisors(gcd(36, 20))
    assert orders == [1, 2, 4]

    rows: list[dict[str, object]] = []
    for e in orders:
        N = 20 // e
        # sigma(eta)=zeta^(-e) eta and sigma(u)=zeta*u.
        a = (-e) % 3
        assert a in (1, 2)
        assert (a + e) % 3 == 0
        assert (a * N + 2) % 3 == 0
        S = (a * N + 2) // 3

        # At a finite zero of h, the noncancelled ODE balance is r=1-m.
        # From R=C*h^(-S)*v^(-N), integrality of ord(v) requires
        # (S-1)m+1 == 0 mod N.
        residues = [m for m in range(N) if ((S - 1) * m + 1) % N == 0]
        assert residues == [3]

        # The residue m=3 makes the nominal leading coefficient vanish.
        r_at_three = 1 - 3
        coefficient_at_three = 9 * r_at_three + 6 * 3
        assert coefficient_at_three == 0
        # After that cancellation the next possible order is m+r=1>0,
        # so it cannot equal the nonzero constant right-hand side.
        next_order_after_cancellation = 3 + r_at_three
        assert next_order_after_cancellation == 1

        rows.append(
            {
                "a": a,
                "e": e,
                "N": N,
                "S": S,
                "character_check_mod_3": (a + e) % 3,
                "finite_zero_congruence": f"m == 3 (mod {N})",
                "m_3_leading_coefficient": coefficient_at_three,
                "m_3_next_possible_order": next_order_after_cancellation,
                "smallest_admissible_noncancelled_m": 3 + N,
            }
        )
    return rows


def universal_valuation_checks(rows: list[dict[str, object]]) -> dict[str, object]:
    # At a regular finite point of h, ord(R)=-N*ord(v).  If this is nonzero,
    # the ODE has order ord(R)-1 and can be constant only for ord(R)=1,
    # impossible because every N is at least five.
    assert all(int(row["N"]) >= 5 for row in rows)
    assert all(1 % int(row["N"]) != 0 for row in rows)

    # The cancelled local balance is r=-2m/3.  It requires 3|m and, after
    # cancellation, the next possible order is m+r=m/3>0.
    cancelled_examples = []
    for m in (3, 6, 9, 12):
        r = -2 * m // 3
        assert 9 * r + 6 * m == 0
        assert m + r == m // 3 > 0
        cancelled_examples.append(
            {"m": m, "r": r, "next_possible_order": m + r}
        )

    # For the packet's terminal-ODE positive control,
    # h=x^2(x-1)^4 and R=C*x^-1*(x-1)^-3.  Logarithmic differentiation gives
    # 9 R'/R + 6 h'/h = 3/x - 3/(x-1), while hR=C*x*(x-1).
    control_constant = 3 * (-1)  # 3*((x-1)-x)
    assert control_constant == -3
    control_differences = {
        "x=0": -1 - 6 * 2,
        "x=1": -3 - 6 * 4,
        "x=infinity": 4 - 6 * (-6),
    }
    assert control_differences == {"x=0": -13, "x=1": -27, "x=infinity": 40}
    assert control_differences["x=0"] % 20 != 0
    assert control_differences["x=1"] % 20 != 0
    assert control_differences["x=infinity"] % 20 == 0

    return {
        "cancelled_local_balances": cancelled_examples,
        "regular_point_divisor_check": (
            "constant RHS would require ord(R)=1, but ord(R) is a multiple "
            "of N in {20,10,5}"
        ),
        "infinity_balance": {
            "finite_orders_sum": "s-D",
            "ord_infinity_R": "D-s",
            "lhs_top_degree": "s-1",
            "lhs_top_coefficient": "9*(s-D)+6*D=3*(3*s-D)",
            "conclusion": (
                "all finite multiplicities m>3 imply D>3s, so the top "
                "coefficient is nonzero; constancy forces s=1; 3|D then "
                "makes h a cube"
            ),
        },
        "terminal_positive_control": {
            "h": "x^2*(x-1)^4",
            "R": "C/(x*(x-1)^3)",
            "ode_lhs_over_C": control_constant,
            "ord_R_minus_6_ord_h": control_differences,
        },
    }


def main() -> None:
    rows = stabilizer_rows()
    payload = {
        "case": "max12_912_order3_dz20_stabilizer_valuation_20260824",
        "exact_inputs": {
            "base_field": "K=C(x), L=K(u), u^3=h, sigma(u)=zeta*u",
            "passport": ["3^12", "4^9", "(20,1^16)"],
            "terminal_descent": "r8=u^2*R; 9*h*R'+6*h'*R=j!=0",
            "history_residual": "3 divides deg(h)",
        },
        "stabilizer_rows": rows,
        "valuation_checks": universal_valuation_checks(rows),
        "producer_conclusion": (
            "No coprime k=mu=nu=0 order-three trajectory with nontrivial "
            "Kummer class survives, conditional only on the passport and "
            "stabilizer-aware isotrivial descent proved in the report."
        ),
        "scope_excluded": [
            "common-factor/noncoprime spectral stratum",
            "nonzero k, mu, or nu",
            "order-one polynomial core",
            "all other maximum-12 cells",
            "JC2",
        ],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
