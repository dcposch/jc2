#!/usr/bin/env python3
"""Exact replay of the AS109 finite-grammar obstruction.

This is not a transition enumerator.  It verifies the frozen hashes and the
parametric triangular-gauge family used by the specification verdict.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


P = 109
ROOT = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_freeze() -> dict[str, str]:
    expected = {}
    for line in (ROOT / "FREEZE.sha256").read_text().splitlines():
        sha, name = line.split()
        expected[name] = sha
    for name, sha in expected.items():
        got = digest(ROOT / name)
        assert got == sha, (name, sha, got)
    return expected


def add(*polys: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    out: dict[tuple[int, int], int] = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            out[exponent] = (out.get(exponent, 0) + coefficient) % P
            if out[exponent] == 0:
                del out[exponent]
    return out


def scale(poly: dict[tuple[int, int], int], scalar: int):
    return {
        exponent: (scalar * coefficient) % P
        for exponent, coefficient in poly.items()
        if (scalar * coefficient) % P
    }


def multiply(
    left: dict[tuple[int, int], int],
    right: dict[tuple[int, int], int],
) -> dict[tuple[int, int], int]:
    out: dict[tuple[int, int], int] = {}
    for (a, b), c1 in left.items():
        for (c, d), c2 in right.items():
            exponent = (a + c, b + d)
            out[exponent] = (out.get(exponent, 0) + c1 * c2) % P
            if out[exponent] == 0:
                del out[exponent]
    return out


def derivative(poly: dict[tuple[int, int], int], axis: int):
    out: dict[tuple[int, int], int] = {}
    for (a, b), coefficient in poly.items():
        power = (a, b)[axis]
        if power == 0:
            continue
        exponent = (a - 1, b) if axis == 0 else (a, b - 1)
        value = coefficient * power % P
        if value:
            out[exponent] = (out.get(exponent, 0) + value) % P
    return out


def delta_at_marked(poly: dict[tuple[int, int], int]) -> int:
    """poly(1,0)-poly(0,0) in F_109."""
    at_one = sum(c for (a, b), c in poly.items() if b == 0) % P
    at_zero = poly.get((0, 0), 0) % P
    return (at_one - at_zero) % P


def nonlinear_source(A, B):
    x108 = {(108, 0): 1}
    u = add(derivative(A, 0), scale(x108, -1))
    return add(
        multiply(u, derivative(B, 1)),
        scale(multiply(derivative(A, 1), derivative(B, 0)), -1),
    )


def triangular_family(m: int) -> dict:
    # Precompose the canonical first lift by G_m=(x+109*y^m,y).
    A = {(0, m): 1}
    B = {(108, 1): 1}
    first = add(derivative(A, 0), derivative(B, 1))
    assert first == {(108, 0): 1}
    assert delta_at_marked(A) == 0
    assert delta_at_marked(B) == 0

    source = nonlinear_source(A, B)
    expected = {(216, 0): P - 1}
    if m % P:
        expected[(107, m)] = m % P
    assert source == expected, (m, source, expected)

    # The same exact triangular gauge transports the canonical W_3 tower.
    # Its second layer is feasible, but only by introducing new correction
    # slots whose exponents again depend on m.
    A1 = {(108, m): P - 1}
    B1 = {(216, 1): 1, (107, m + 1): 108}
    successor = add(derivative(A1, 0), derivative(B1, 1))
    assert successor == scale(source, -1), (m, successor, source)
    assert delta_at_marked(A1) == 0
    assert delta_at_marked(B1) == 0
    first_slots = {("P", 0, m), ("Q", 108, 1)}
    successor_slots = {("P", 108, m), ("Q", 216, 1), ("Q", 107, m + 1)}
    assert first_slots.isdisjoint(successor_slots)

    # CLOSED-SUPPORT control for the five-slot union: its derivative residual
    # space contains exponents (108,0), (107,m), and (216,0). Activating the
    # allowed slot B=x^216*y alone makes N=-x^324, outside that space.
    derivative_residuals = {(108, 0), (107, m), (216, 0)}
    closure_probe = nonlinear_source({}, {(216, 1): 1})
    assert closure_probe == {(324, 0): P - 1}
    assert (324, 0) not in derivative_residuals

    # G_m is an exact integral triangular polynomial automorphism: its
    # determinant is one, inverse is (x-109*y^m,y), and it fixes both points.
    return {
        "m": m,
        "first_layer_slots": [["P", 0, m], ["Q", 108, 1]],
        "slot_count": 2,
        "E1": "PASS",
        "collision": "PASS",
        "exact_integral_gauge": "(x+109*y^m,y)",
        "nonlinear_source": [
            [a, b, coefficient] for (a, b), coefficient in sorted(source.items())
        ],
        "forces_new_x216_residual": source.get((216, 0)) == P - 1,
        "E2_with_transported_gauge": "PASS",
        "successor_slots": [list(slot) for slot in sorted(successor_slots)],
        "same_slot_cycle": False,
        "union_slot_count_through_E2": len(first_slots | successor_slots),
        "closed_support_unit_L": "FAIL-NOT-CLOSED",
        "closure_counterresidual": [324, 0, P - 1],
    }


def main() -> None:
    frozen = check_freeze()
    samples = [1, 2, 3, 108, 109, 110, 1000]
    records = [triangular_family(m) for m in samples]
    assert all(record["slot_count"] <= 8 for record in records)
    assert all(record["forces_new_x216_residual"] for record in records)
    assert all(record["union_slot_count_through_E2"] == 5 for record in records)
    print(
        json.dumps(
            {
                "verdict": "PASS-SPEC-OBSTRUCTION-CONTROL",
                "enumeration_run": False,
                "frozen_hashes": frozen,
                "parametric_identity": {
                    "family": "A0=y^m, B0=x^108*y for every integer m>=1",
                    "E1": "A0_x+B0_y=x^108",
                    "collision": "both corrections vanish on y=0",
                    "gauge": "exact triangular G_m=(x+109*y^m,y)",
                    "N": "-x^216 + (m mod 109)*x^107*y^m",
                },
                "sample_replays": records,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
