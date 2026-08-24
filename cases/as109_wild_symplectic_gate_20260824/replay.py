#!/usr/bin/env python3
"""Deterministic first-Witt-digit compiler for the AS wild-symplectic gate."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


Poly = dict[tuple[int, int], int]


def norm(f: Poly, modulus: int | None = None) -> Poly:
    out: Poly = {}
    for mon, value in f.items():
        if modulus is not None:
            value %= modulus
        if value:
            out[mon] = value
    return out


def add(f: Poly, g: Poly, modulus: int | None = None) -> Poly:
    out = dict(f)
    for mon, value in g.items():
        out[mon] = out.get(mon, 0) + value
    return norm(out, modulus)


def scale(f: Poly, value: int, modulus: int | None = None) -> Poly:
    return norm({mon: value * coefficient for mon, coefficient in f.items()}, modulus)


def mul(f: Poly, g: Poly, modulus: int | None = None) -> Poly:
    out: Poly = {}
    for (i, j), a in f.items():
        for (k, ell), b in g.items():
            mon = (i + k, j + ell)
            out[mon] = out.get(mon, 0) + a * b
    return norm(out, modulus)


def power(f: Poly, exponent: int, modulus: int | None = None) -> Poly:
    out: Poly = {(0, 0): 1}
    base = norm(f, modulus)
    n = exponent
    while n:
        if n & 1:
            out = mul(out, base, modulus)
        base = mul(base, base, modulus)
        n >>= 1
    return out


def derivative(f: Poly, variable: int, modulus: int | None = None) -> Poly:
    out: Poly = {}
    for (i, j), coefficient in f.items():
        exponents = [i, j]
        if exponents[variable] == 0:
            continue
        factor = exponents[variable]
        exponents[variable] -= 1
        mon = (exponents[0], exponents[1])
        out[mon] = out.get(mon, 0) + factor * coefficient
    return norm(out, modulus)


def translate_x(f: Poly, amount: int, modulus: int) -> Poly:
    out: Poly = {}
    for (i, j), coefficient in f.items():
        for k in range(i + 1):
            mon = (k, j)
            out[mon] = out.get(mon, 0) + coefficient * math.comb(i, k) * amount ** (i - k)
    return norm(out, modulus)


def compose(f: Poly, x_image: Poly, y_image: Poly, modulus: int) -> Poly:
    out: Poly = {}
    for (i, j), coefficient in f.items():
        term = mul(power(x_image, i, modulus), power(y_image, j, modulus), modulus)
        out = add(out, scale(term, coefficient, modulus), modulus)
    return out


def divergence(a: Poly, b: Poly, modulus: int) -> Poly:
    return add(derivative(a, 0, modulus), derivative(b, 1, modulus), modulus)


def jacobian(p_coord: Poly, q_coord: Poly, modulus: int | None = None) -> Poly:
    first = mul(derivative(p_coord, 0, modulus), derivative(q_coord, 1, modulus), modulus)
    second = mul(derivative(p_coord, 1, modulus), derivative(q_coord, 0, modulus), modulus)
    return add(first, scale(second, -1, modulus), modulus)


def rref(matrix: list[list[int]], p: int, coefficient_columns: int) -> tuple[list[list[int]], list[int]]:
    rows = [[value % p for value in row] for row in matrix]
    pivot_row = 0
    pivots: list[int] = []
    for column in range(coefficient_columns):
        chosen = next((r for r in range(pivot_row, len(rows)) if rows[r][column] % p), None)
        if chosen is None:
            continue
        rows[pivot_row], rows[chosen] = rows[chosen], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], -1, p)
        rows[pivot_row] = [(inverse * value) % p for value in rows[pivot_row]]
        for r in range(len(rows)):
            if r == pivot_row:
                continue
            factor = rows[r][column] % p
            if factor:
                rows[r] = [(a - factor * b) % p for a, b in zip(rows[r], rows[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return rows, pivots


def linear_window(p: int) -> dict[str, int | bool]:
    variables = [
        (coordinate, i, j)
        for coordinate in (0, 1)
        for i in range(p + 1)
        for j in range(2)
    ]
    outputs = [(i, j) for i in range(p + 1) for j in range(2)]
    index = {variable: column for column, variable in enumerate(variables)}
    out_index = {mon: row for row, mon in enumerate(outputs)}
    matrix = [[0 for _ in variables] for _ in outputs]
    for column, (coordinate, i, j) in enumerate(variables):
        if coordinate == 0 and i:
            matrix[out_index[(i - 1, j)]][column] = i % p
        if coordinate == 1 and j:
            matrix[out_index[(i, j - 1)]][column] = j % p
    rhs = [0 for _ in outputs]
    rhs[out_index[(p - 1, 0)]] = 1

    coefficient_rref, pivots = rref(matrix, p, len(variables))
    augmented, augmented_pivots = rref(
        [row + [value] for row, value in zip(matrix, rhs)], p, len(variables)
    )
    assert pivots == augmented_pivots
    assert not any(all(value % p == 0 for value in row[:-1]) and row[-1] % p for row in augmented)

    particular = [0 for _ in variables]
    for row_number, column in enumerate(augmented_pivots):
        particular[column] = augmented[row_number][-1] % p
    free = [column for column in range(len(variables)) if column not in pivots]
    null_basis: list[list[int]] = []
    for free_column in free:
        vector = [0 for _ in variables]
        vector[free_column] = 1
        for row_number, pivot_column in enumerate(pivots):
            vector[pivot_column] = -coefficient_rref[row_number][free_column] % p
        null_basis.append(vector)

    q_cartier = index[(1, p - 1, 1)]
    forced_cartier = particular[q_cartier] == 1 and all(vector[q_cartier] == 0 for vector in null_basis)

    control = [0 for _ in variables]
    control[q_cartier] = 1
    control_ok = all(
        sum(row[column] * control[column] for column in range(len(variables))) % p == value
        for row, value in zip(matrix, rhs)
    )
    assert control_ok and forced_cartier
    return {
        "variables": len(variables),
        "equations": len(outputs),
        "divergence_rank": len(pivots),
        "affine_dimension": len(variables) - len(pivots),
        "gauge_kernel_dimension": len(null_basis),
        "affine_mod_gauge_dimension": 0,
        "cotangent_control_in_window": control_ok,
        "q1_x_pminus1_y_coefficient_forced_to_one": forced_cartier,
    }


def first_digit(p: int) -> dict[str, object]:
    field = p
    modulus = p * p
    x = {(1, 0): 1}
    y = {(0, 1): 1}
    one = {(0, 0): 1}
    c: Poly = {
        (k, 0): (math.comb(p, k) // p) % p
        for k in range(1, p)
    }
    q1 = {(p - 1, 1): 1}
    a = c
    b = scale(add(translate_x(q1, 1, p), scale(q1, -1, p), p), -1, p)
    delta_q1 = add(translate_x(q1, 1, p), scale(q1, -1, p), p)
    norm_a: Poly = {}
    norm_b: Poly = {}
    for i in range(p):
        norm_a = add(norm_a, translate_x(a, i, p), p)
        norm_b = add(norm_b, translate_x(b, i, p), p)
    assert norm_a == {(0, 0): p - 1}
    assert norm_b == {}
    assert divergence(a, b, field) == {}
    assert a == c and b == scale(delta_q1, -1, p)
    assert divergence({}, q1, field) == {(p - 1, 0): 1}

    p0 = add(x, scale(power(x, p), -1))
    q = add(y, scale(q1, p), modulus)
    tau_x = add(add(x, one, modulus), scale(a, p), modulus)
    tau_y = add(y, scale(b, p), modulus)
    assert jacobian(p0, q, modulus) == one
    assert jacobian(tau_x, tau_y, modulus) == one
    assert compose(p0, tau_x, tau_y, modulus) == norm(p0, modulus)
    assert compose(q, tau_x, tau_y, modulus) == q

    return {
        "carry_c": [[i, coefficient] for (i, _), coefficient in sorted(c.items())],
        "norm_a": -1,
        "norm_b_zero": True,
        "action_divergence_zero": True,
        "invariance_mod_p2": True,
        "action_order_p_from_norm_equations": True,
        "jacobian_map_mod_p2": 1,
        "jacobian_action_mod_p2": 1,
        "window": linear_window(p),
    }


def cotangent_tower(p: int) -> list[dict[str, object]]:
    x = {(1, 0): 1}
    y = {(0, 1): 1}
    p0 = add(x, scale(power(x, p), -1))
    derivative_g = {(0, 0): 1, (p - 1, 0): -p}
    rows: list[dict[str, object]] = []
    for depth in (2, 3, 4):
        modulus = p ** depth
        series: Poly = {
            (j * (p - 1), 0): p ** j
            for j in range(depth)
        }
        q = mul(y, series)
        exact_jacobian = jacobian(p0, q)
        expected = {(0, 0): 1, (depth * (p - 1), 0): -(p ** depth)}
        assert exact_jacobian == expected
        assert jacobian(p0, norm(q, modulus), modulus) == {(0, 0): 1}
        assert mul(derivative_g, series, modulus) == {(0, 0): 1}
        rows.append({
            "depth": depth,
            "q_support": [[j * (p - 1), 1] for j in range(depth)],
            "q_x_degree": (depth - 1) * (p - 1),
            "exact_jacobian_error": [-(p ** depth), depth * (p - 1)],
            "inverse_unit_identity_mod_p_depth": True,
        })
    return rows


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    inputs = [
        "xmodel/ideation-20260824T1205Z-event-synthesis.md",
        "xmodel/as109-hensel-global-degree-cross-gate-20260824.md",
        "xmodel/as109-degree-cross-review-grok-20260824.md",
        "xmodel/as109-ainfinity-deck-descent-gate-20260824.md",
        "xmodel/as109-ainfinity-review-grok-20260824.md",
        "xmodel/witt-tate-control-20260824.md",
        "xmodel/review-witt-tate-control-claude.md",
    ]
    input_hashes = {
        path: hashlib.sha256((root / path).read_bytes()).hexdigest()
        for path in inputs
    }
    results = {
        "schema": "as109-wild-symplectic-first-gate-v1",
        "verdict": "GAUGE-TRIVIAL/CONTROL-ONLY",
        "primes": {
            str(p): {
                "first_digit": first_digit(p),
                "cotangent_tower": cotangent_tower(p),
            }
            for p in (3, 5)
        },
        "scope": {
            "finite_etale_action_theorem_is_symbolic_not_sampled": True,
            "compiler_depths": [2, 3, 4],
            "compiler_primes": [3, 5],
            "p109_computation": False,
            "aws": False,
            "jc2_inference": False,
        },
        "input_sha256": input_hashes,
    }
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
