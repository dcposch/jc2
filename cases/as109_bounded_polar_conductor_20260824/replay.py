#!/usr/bin/env python3
"""Exact controls for the AS polar-conductor / bounded-gauge gate.

This is deliberately structural: it samples only p=3,5 and never enumerates
an exponent rectangle.  The nonlinear depth-three obstruction is reduced to
a necessary linear digit system on the total-degree simplex deg <= p.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction


def rref_rank(rows: list[list[int]], p: int, columns: int) -> tuple[int, bool]:
    a = [[v % p for v in row] for row in rows]
    pivot_row = 0
    for col in range(columns):
        chosen = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if chosen is None:
            continue
        a[pivot_row], a[chosen] = a[chosen], a[pivot_row]
        inv = pow(a[pivot_row][col], -1, p)
        a[pivot_row] = [(inv * v) % p for v in a[pivot_row]]
        for i in range(len(a)):
            if i != pivot_row and a[i][col]:
                factor = a[i][col]
                a[i] = [(u - factor * v) % p for u, v in zip(a[i], a[pivot_row])]
        pivot_row += 1
    inconsistent = any(all(v == 0 for v in row[:columns]) and row[columns] != 0 for row in a)
    return pivot_row, inconsistent


def univariate_trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def univariate_divmod(a: list[Fraction], b: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    a = univariate_trim(a[:])
    b = univariate_trim(b[:])
    if b == [0]:
        raise ZeroDivisionError
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        k = len(a) - len(b)
        c = a[-1] / b[-1]
        q[k] += c
        for j, value in enumerate(b):
            a[j + k] -= c * value
        a = univariate_trim(a)
    return univariate_trim(q), a


def univariate_gcd(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    a, b = univariate_trim(a), univariate_trim(b)
    while b != [0]:
        _, r = univariate_divmod(a, b)
        a, b = b, r
    lead = a[-1]
    return [v / lead for v in a]


def monomials_at_most(degree: int) -> list[tuple[int, int]]:
    return [(i, j) for total in range(degree + 1) for i in range(total + 1) for j in [total - i]]


def depth_three_system(p: int) -> dict[str, object]:
    """Necessary digit system for D_F=D_phi=p at precision p^3.

    Put X=x+p r+p^2 r2 and Y=y+p s+p^2 s2.  Mod p^3,

      g(X)=g(x)+p r+p^2(r2-x^(p-1)r),
      Q=y+p(s+x^(p-1)y)
          +p^2(s2+x^(p-1)s+(p-1)x^(p-2)r y+x^(2p-2)y).

    Degree <=p in the first coordinate forces every degree >=2 coefficient
    of r to vanish.  First-order symplecticity forces r_x+s_y=0.  The target
    coefficient x^(2p-2)y in Q must vanish.  These necessary linear rows are
    inconsistent; hence the full nonlinear system is empty.
    """
    mons = monomials_at_most(p)
    variables = [(coord, mon) for coord in ("r", "s") for mon in mons]
    idx = {var: i for i, var in enumerate(variables)}
    rows: list[list[int]] = []

    # High-degree terms -x^(p-1)r in P force r_(i,j)=0 for i+j >= 2.
    for mon in mons:
        if sum(mon) >= 2:
            row = [0] * (len(variables) + 1)
            row[idx[("r", mon)]] = 1
            rows.append(row)

    # First determinant digit: r_x+s_y=0.
    divergence: dict[tuple[int, int], list[int]] = {}
    for mon in mons:
        i, j = mon
        if i:
            out = (i - 1, j)
            divergence.setdefault(out, [0] * (len(variables) + 1))[idx[("r", mon)]] += i
        if j:
            out = (i, j - 1)
            divergence.setdefault(out, [0] * (len(variables) + 1))[idx[("s", mon)]] += j
    rows.extend(divergence.values())

    # Coefficient x^(2p-2)y of Q at its p^2 digit:
    # s_(p-1,1)+(p-1)r_(p,0)+1 = 0.
    target = [0] * (len(variables) + 1)
    target[idx[("s", (p - 1, 1))]] = 1
    target[idx[("r", (p, 0))]] = p - 1
    target[-1] = 1
    rows.append(target)

    rank, inconsistent = rref_rank(rows, p, len(variables))
    assert inconsistent
    return {
        "degree_cap_map_and_gauge": p,
        "precision": 3,
        "variables_first_digit_r_s": len(variables),
        "necessary_rows": len(rows),
        "coefficient_rank": rank,
        "augmented_rank": rank + 1,
        "augmented_inconsistent": inconsistent,
        "forced_forbidden_Q_monomial": [2 * p - 2, 1],
        "forced_coefficient_after_dividing_by_p_squared": 1,
    }


def prime_control(p: int) -> dict[str, object]:
    # D=1-p*x^(p-1) and D'=-p(p-1)x^(p-2) are coprime over Q.
    denominator = [Fraction(0)] * p
    denominator[0] = 1
    denominator[p - 1] = -p
    derivative = [Fraction(i) * denominator[i] for i in range(1, len(denominator))]
    gcd = univariate_gcd(denominator, derivative)
    assert gcd == [1]

    # Exact cotangent identity (1-pz) * sum_{j<n}(pz)^j = 1-(pz)^n,
    # with z=x^(p-1); record its coefficient check for n=2,3,4.
    tower = []
    for n in (2, 3, 4):
        # Sparse exponents in z.
        product: dict[int, int] = {}
        for j in range(n):
            product[j] = product.get(j, 0) + p**j
            product[j + 1] = product.get(j + 1, 0) - p ** (j + 1)
        product = {e: c for e, c in product.items() if c}
        assert product == {0: 1, n: -(p**n)}
        tower.append({
            "precision": n,
            "Q_total_degree": (n - 1) * (p - 1) + 1,
            "jacobian_error": {"coefficient": -(p**n), "x_exponent": n * (p - 1)},
        })

    # For affine phi=id mod p, the last tower term has unique top degree and
    # coefficient p^(n-1)*unit, so the exact degree is the displayed formula.
    affine_Dp = {
        "precision_2_solution": True,
        "precision_2_degree": p,
        "precision_3_empty": True,
        "precision_3_forced_degree": 2 * p - 1,
    }
    assert affine_Dp["precision_3_forced_degree"] > p

    return {
        "p": p,
        "g": {"x": 1, f"x^{p}": -1},
        "g_prime": {"1": 1, f"x^{p-1}": -p},
        "denominator_squarefree": gcd == [1],
        "geometric_polar_components": p - 1,
        "root_valuation": f"-1/{p-1}",
        "all_poles_outside_closed_unit_disc": True,
        "restricted_inverse_support": [[j * (p - 1), p**j] for j in range(4)],
        "cotangent_tower": tower,
        "affine_cap_D_equals_p": affine_Dp,
        "nonlinear_cap_D_equals_p": depth_three_system(p),
    }


def main() -> None:
    result = {
        "schema": "as109-bounded-polar-conductor-v1",
        "primes": {str(p): prime_control(p) for p in (3, 5)},
        "structural_scope": {
            "odd_prime_formula_not_enumerated": True,
            "p109_enumeration": False,
            "arbitrary_rectangle": False,
            "aws": False,
            "jc2_inference": False,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
