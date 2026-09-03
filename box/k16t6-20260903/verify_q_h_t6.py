#!/usr/bin/env python3
"""Hash-anchored verification of the reused t=6 Q spine and H/c units."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import pathlib
import sys

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
FROZEN = pathlib.Path("/tmp/jc2-lane.Gp5PbG/inputs/k16t56_pipeline.py")


def check_q_tsv() -> None:
    expected_digest = None
    for line in (HERE / "SHA256SUMS.reused").read_text().splitlines():
        digest, name = line.split(None, 1)
        if name.strip() == "t6_Q_pivots.tsv":
            expected_digest = digest
            break
    if expected_digest is None:
        raise AssertionError("Q-pivot digest absent from reuse manifest")
    data = (HERE / "t6_Q_pivots.tsv").read_bytes()
    if hashlib.sha256(data).hexdigest() != expected_digest:
        raise AssertionError("Q-pivot TSV digest mismatch")

    expected = []
    for step in range(1, 7):
        expected.append((step, 93-step, 26-step, 0, 1,
                         f"a{step+6}_1", "13"))
    for step in range(7, 21):
        index = 13 + (step-7)//2
        if (step-7) % 2 == 0:
            expected.append((step, 93-step, 32-index, 0, 0,
                             f"a{index}_2", "26"))
        else:
            expected.append((step, 93-step, 32-index, 0, 1,
                             f"a{index}_1", "13"))
    expected.extend([
        (21, 69, 12, 0, 3, "a19_0", "-52"),
        (22, 68, 12, 1, 2, "a19_3", "-39/4"),
    ])

    with (HERE / "t6_Q_pivots.tsv").open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    actual = [
        (int(row["step"]), int(row["source"]), int(row["band"]),
         int(row["gamma"]), int(row["pi"]), row["variable"],
         row["coefficient"])
        for row in rows
    ]
    if actual != expected or len({row[5] for row in actual}) != 22:
        raise AssertionError("Q-pivot field mismatch")
    print(f"Q_TSV_PASS sha256={expected_digest} rows=22 unique=22 "
          "coefficients_Qstar=true bands=25..12")


def load_frozen_pipeline():
    spec = importlib.util.spec_from_file_location("frozen_k16t56_pipeline", FROZEN)
    if spec is None or spec.loader is None:
        raise AssertionError("cannot load frozen pipeline")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def check_h_units() -> None:
    pipeline = load_frozen_pipeline()
    y = sp.Symbol("y")
    algebra = pipeline.AtAlgebra(6, y)
    if algebra.content != 4:
        raise AssertionError("unexpected H content")
    if sp.expand(algebra.H_primitive-(507*y**2-273*y+35)) != 0:
        raise AssertionError("primitive H mismatch")
    if sp.discriminant(algebra.H_primitive, y) != 3549:
        raise AssertionError("primitive discriminant mismatch")
    if not algebra.irreducible:
        raise AssertionError("H is not irreducible")
    cbar_expr = pipeline.c_polynomial(6, y)
    if sp.expand(cbar_expr-sp.Rational(19, 2197)*y*(7-78*y)) != 0:
        raise AssertionError("cbar formula mismatch")

    elements = [
        ("y", pipeline.AtCoeff(sp.Rational(0), sp.Rational(1)),
         sp.Rational(140)),
        ("linear", algebra.reduce_poly(7-78*y), sp.Rational(354900)),
        ("cbar", algebra.reduce_poly(cbar_expr),
         sp.Rational(8844500, 4826809)),
    ]
    one = pipeline.AtCoeff(sp.Rational(1), sp.Rational(0))
    for label, element, expected_resultant in elements:
        resultant = algebra.resultant(element)
        inverse = algebra.inverse(element)
        if resultant != expected_resultant or resultant == 0:
            raise AssertionError(f"{label} resultant mismatch: {resultant}")
        if algebra.mul(element, inverse) != one:
            raise AssertionError(f"{label} inverse mismatch")
        print(f"UNIT_PASS {label} resultant={resultant} "
              f"inverse={inverse.as_expr(y)}")
    print("H6_PASS primitive=507*y^2-273*y+35 "
          "disc=13^2*21 field=Q(sqrt(21)) "
          "cbar=19*y*(7-78*y)/2197")


if __name__ == "__main__":
    check_q_tsv()
    check_h_units()
