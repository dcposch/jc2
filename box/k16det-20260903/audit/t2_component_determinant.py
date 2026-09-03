#!/usr/bin/env python3
"""Exact componentwise t=2 control for the selected top-tail prefix.

The charged records store R=-E, whereas the lane's F_r are coefficients of
T=[E].  This script therefore negates the stored rows before forming F_0 and
F_1.  It also authenticates the source record against both charged split-job
metadata files, so no digest is copied into this driver.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
RECORD = ROOT / "box/k16spine-20260903/terminal_laurent_t2.json"
JOBS = [
    ROOT / "box/k16terminal-sol56-20260903/terminal_t2_split-exact_branch0_all.json",
    ROOT / "box/k16terminal-sol56-20260903/terminal_t2_split-exact_branch1_all.json",
]


def multiplication_matrix(f: sp.Expr, modulus: sp.Poly, x: sp.Symbol) -> sp.Matrix:
    monic = modulus.monic()
    rank = monic.degree()
    basis = [x**i for i in range(rank)]
    columns: list[list[sp.Expr]] = []
    for vector in basis:
        remainder = sp.rem(sp.Poly(sp.expand(f * vector), x), monic).as_expr()
        columns.append([sp.factor(remainder.coeff(x, i)) for i in range(rank)])
    return sp.Matrix(rank, rank, lambda i, j: columns[j][i])


def main() -> None:
    raw = RECORD.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    expected = {
        json.loads(job.read_text())["comparison_record"]["sha256"] for job in JOBS
    }
    assert expected == {digest}

    record = json.loads(raw)
    b3, b4, y = sp.symbols("b3 b4 q5_1")
    locals_ = {"b3": b3, "b4": b4, "q5_1": y}
    stored_r = {
        int(item["band"]): sp.sympify(item["expr"], locals=locals_)
        for item in record["terminal"]
    }

    payload: dict[str, object] = {"source_sha256": digest, "branches": []}
    for y_value in (sp.Rational(1, 5), sp.Rational(2, 5)):
        d_value = sp.factor(10 * y_value - 3)
        f0 = sp.factor(-stored_r[2].subs({b4: 1, y: y_value}))
        f1 = sp.factor(-stored_r[3].subs({b4: 1, y: y_value}))
        modulus = sp.Poly(f1, b3)
        matrix = multiplication_matrix(f0, modulus, b3)
        zero_rows_r = [
            sp.factor(stored_r[k].subs({b4: 0, y: y_value})) for k in range(4)
        ]
        payload["branches"].append(  # type: ignore[union-attr]
            {
                "y": str(y_value),
                "d": str(d_value),
                "F0_T_equals_E": str(f0),
                "F1_T_equals_E": str(f1),
                "monic_J_generator": str(sp.factor(modulus.monic().as_expr())),
                "basis": [str(b3**i) for i in range(modulus.degree())],
                "multiplication_matrix": [[str(x) for x in row] for row in matrix.tolist()],
                "determinant": str(sp.factor(matrix.det())),
                "stored_R_zero_chart_bands_0_to_3": [str(x) for x in zero_rows_r],
            }
        )

    assert [len(item["basis"]) for item in payload["branches"]] == [1, 2]  # type: ignore[index]
    assert all(sp.sympify(item["determinant"]) != 0 for item in payload["branches"])  # type: ignore[index]
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
