#!/usr/bin/env python3
"""Solve the diagonal quasi-homogeneity equations for the Q8 quotient rows."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"


def load_compiler():
    assert sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256
    spec = importlib.util.spec_from_file_location("q8_weight_compiler", COMPILER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def rref_nullspace(matrix: list[list[int]], columns: int):
    work = [[Fraction(value) for value in row] for row in matrix]
    pivot_columns = []
    pivot_row = 0
    for column in range(columns):
        found = next((row for row in range(pivot_row, len(work)) if work[row][column]), None)
        if found is None:
            continue
        work[pivot_row], work[found] = work[found], work[pivot_row]
        pivot = work[pivot_row][column]
        work[pivot_row] = [value / pivot for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            multiplier = work[row][column]
            work[row] = [
                left - multiplier * right
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    free_columns = [column for column in range(columns) if column not in pivot_columns]
    basis = []
    for free in free_columns:
        vector = [Fraction(0) for _ in range(columns)]
        vector[free] = 1
        for row, pivot in enumerate(pivot_columns):
            vector[pivot] = -work[row][free]
        basis.append(vector)
    return pivot_columns, basis


def show(value: Fraction):
    return value.numerator if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    compiler = load_compiler()
    _, rows, imposed, names = compiler.compile_quotient("approx")
    constraints = []
    row_stats = {}
    for ell in imposed:
        support = sorted(rows[ell])
        anchor = support[0]
        for monomial in support[1:]:
            constraints.append([left - right for left, right in zip(monomial, anchor)])
        row_stats[str(ell)] = {
            "terms": len(support),
            "contains_constant": tuple(0 for _ in names) in support,
        }
    pivots, nullspace = rref_nullspace(constraints, len(names))
    payload = {
        "status": "PASS",
        "compiler_sha256": COMPILER_SHA256,
        "variables": names,
        "constraint_count": len(constraints),
        "rank": len(pivots),
        "nullity": len(nullspace),
        "pivot_columns": pivots,
        "nullspace_basis": [[show(value) for value in vector] for vector in nullspace],
        "row_stats": row_stats,
        "interpretation": (
            "diagonal coordinate weights making each of the six imposed rows "
            "semi-invariant; zero nullity means no nontrivial such scaling"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
