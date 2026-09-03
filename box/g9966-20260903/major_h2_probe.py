#!/usr/bin/env python3
"""Exact projected D2-to-D1 count for Moh's degree-33 approximate root.

This is deliberately a projection: it proves the finite support count and the
seven independent first-child rows for h2, but does not claim that the h2
coefficients have been tied to h3 or to global f99,g66 coefficient arrays.
JSON is written to stdout; the driver itself writes no files.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from math import comb
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RECEIPT = ROOT / "xmodel/g9966-global-design-sol56-20260903.run.v2"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def verify_frozen_inputs() -> dict:
    fields = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    count = int(fields["charged_inputs"])
    source = Path(fields["lane_inputs_dir"])
    checked = []
    for index in range(1, count + 1):
        name = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        assert Path(name).name == name
        actual = digest(source / name)
        assert actual == expected, f"frozen input mismatch: {name}"
        checked.append({"basename": name, "sha256": actual})
    assert len(checked) == count == 14
    return {
        "receipt": str(RECEIPT),
        "lane_inputs_dir": str(source),
        "charged_inputs": count,
        "all_hashes_match": True,
        "files": checked,
    }


def qstar_reduce(rows, variables):
    rows = [(tag, sp.expand(row)) for tag, row in rows if row != 0]
    variables = list(variables)
    pivots = []
    substitutions = {}
    while True:
        selected = None
        for row_index, (tag, row) in enumerate(rows):
            for variable_index, variable in enumerate(variables):
                coefficient = sp.diff(row, variable)
                remainder = sp.expand(row - coefficient * variable)
                if coefficient.is_Rational and coefficient != 0 and variable not in remainder.free_symbols:
                    selected = (row_index, variable_index, tag, variable, coefficient, remainder)
                    break
            if selected:
                break
        if not selected:
            break
        row_index, variable_index, tag, variable, coefficient, remainder = selected
        rhs = sp.expand(-remainder / coefficient)
        substitutions[variable] = rhs
        pivots.append((tag, variable, coefficient, rhs))
        del rows[row_index]
        del variables[variable_index]
        rows = [
            (tag0, image)
            for tag0, row0 in rows
            if (image := sp.expand(row0.subs(variable, rhs))) != 0
        ]
    return rows, variables, pivots, substitutions


def main() -> None:
    frozen = verify_frozen_inputs()
    Pi = sp.Symbol("Pi")

    # K=t^33 h2(t^-1,w/t).  Its fixed homogeneous form is
    # w^9(w-1)^24.  At w=1+pi*t^(4/3), the D2 equality face is
    # (pi^3-1)^8, so the eight r>0 equality coefficients are fixed.
    equality = [
        {"r": 4 * k, "q": 24 - 3 * k, "coefficient": (-1) ** k * comb(8, k)}
        for k in range(1, 9)
    ]
    strict_support = []
    variables = []
    for r in range(1, 34):
        for q in range(0, 34 - r):
            if 3 * r + 4 * q >= 97:
                variable = sp.Symbol(f"c_{r}_{q}")
                variables.append(variable)
                strict_support.append((r, q, variable))
    assert len(variables) == 169

    # Recenter t=u^9, w=1+u^12+Pi*u^13.  Below the D1 threshold u^296,
    # the fixed equality face cancels identically; a strict term contributes
    # c*u^(9r+12q)*(1+Pi*u)^q.
    rows = []
    row_counts = Counter()
    for exponent in range(289, 296):
        coefficient = sp.Integer(0)
        for r, q, variable in strict_support:
            base = 9 * r + 12 * q
            j = exponent - base
            if 0 <= j <= q:
                coefficient += variable * comb(q, j) * Pi**j
        for pi_power, scalar in sp.Poly(sp.expand(coefficient), Pi).terms():
            if scalar != 0:
                tag = (exponent, pi_power[0])
                rows.append((tag, scalar))
                row_counts[exponent] += 1

    residual, free, pivots, substitutions = qstar_reduce(rows, variables)
    assert not residual
    assert len(rows) == len(pivots) == 7
    assert len(free) == 162
    assert dict(sorted(row_counts.items())) == {291: 1, 292: 1, 293: 1, 294: 2, 295: 2}

    # Positive/negative controls for the actual row map.
    positive = {variable: sp.Integer(0) for variable in variables}
    assert all(sp.expand(row.subs(positive)) == 0 for _tag, row in rows)
    negative = dict(positive)
    negative[pivots[0][1]] = 1
    assert any(sp.expand(row.subs(negative)) != 0 for _tag, row in rows)

    output = {
        "type": "PROJECTED-MAJOR-h2-D2-D1 / EXACT-COUNT",
        "not_claimed": [
            "compatibility with h3",
            "a common global f99,g66 coefficient map",
            "the Jacobian equation",
        ],
        "frozen_input_verification": frozen,
        "coordinates": {
            "K": "t^33*h2(t^-1,w/t)",
            "fixed_top": "w^9*(w-1)^24",
            "D2_substitution": "w=1+pi*t^(4/3)",
            "D2_face": "(pi^3-1)^8",
            "strict_filter": "3*r+4*q>=97",
            "D1_recenter": "t=u^9, w=1+u^12+Pi*u^13",
            "D1_vanishing": "coefficients of u^e vanish for e<296",
        },
        "fixed_equality_coefficients": equality,
        "strict_coefficient_count": len(variables),
        "raw_nonzero_scalar_rows": len(rows),
        "rows_by_u_power": dict(sorted(row_counts.items())),
        "Qstar_rank": len(pivots),
        "free_dimension": len(free),
        "pivot_ledger": [
            {
                "u_power": tag[0],
                "Pi_power": tag[1],
                "pivot": str(variable),
                "coefficient": str(coefficient),
            }
            for tag, variable, coefficient, _rhs in pivots
        ],
        "controls": {
            "zero_positive_point_kills_every_row": True,
            "single_pivot_perturbation_is_rejected": True,
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
