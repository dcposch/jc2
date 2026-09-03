#!/usr/bin/env python3
"""Audit the natural grading and sparse normalizer rows at fixed K=16-ray t.

This is a read-only analysis driver.  It imports the frozen charged general
chart and constant-pivot implementation, constructs the gauged chart, applies
only the audited Q-constant affine eliminations, and prints residual rows whose
support is contained in {x,y} or {x,y,c}, where

    x = coefficient of A in beta_(t+1),
    y = coefficient of B in beta_(2t+1).

No CAS basis is run and no input artifact is modified.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import pathlib
import sys

import sympy as sp


INPUTS = pathlib.Path("/tmp/jc2-lane.fjoTgL/inputs")
CHART = INPUTS / "t_order_system.py"
PREPROCESS = INPUTS / "triangular_preprocess.py"
EXPECTED = {
    CHART: "e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28",
    PREPROCESS: "f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93",
}


def digest(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import %s" % path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def intrinsic_weight(basis: sp.Expr, data: dict) -> int:
    if basis == 1:
        return 0
    if basis == data["A"]:
        return 3
    if basis == data["B"]:
        return 2
    if basis == data["z"] or basis == sp.Symbol("gamma"):
        return 1
    raise AssertionError("unknown basis element %s" % basis)


def natural_weights(data: dict) -> dict[sp.Symbol, int]:
    weights: dict[sp.Symbol, int] = {}
    for index, b in enumerate(sp.symbols("b1:5"), start=1):
        weights[b] = index
    for prefix, spaces in (("a", data["alpha_spaces"]),
                           ("q", data["beta_spaces"])):
        for deficit, basis_space in spaces.items():
            for coordinate, basis in enumerate(basis_space):
                variable = sp.Symbol("%s%d_%d" % (prefix, deficit, coordinate))
                weights[variable] = 4 * deficit - intrinsic_weight(basis, data)
    weights[data["c"]] = 20 * data["t"] + 5
    return weights


def row_weight(expr: sp.Expr, variables: list[sp.Symbol], weights: dict) -> int:
    seen = {
        sum(power * weights[variable]
            for power, variable in zip(monomial, variables))
        for monomial, _coefficient in sp.Poly(expr, *variables, domain=sp.QQ).terms()
    }
    if len(seen) != 1:
        raise AssertionError("inhomogeneous row: %s" % sorted(seen))
    return seen.pop()


def primitive(expr: sp.Expr, variables: list[sp.Symbol]) -> sp.Expr:
    poly = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    _denom, cleared = poly.clear_denoms(convert=True)
    _content, ans = cleared.primitive()
    if ans.LC() < 0:
        ans = -ans
    return ans.as_expr()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int, nargs="+", help="positive integer parameters")
    args = parser.parse_args()
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            raise RuntimeError("charged hash mismatch: %s" % path)
        print("HASH_OK", path.name, actual)

    chart = load(CHART, "uniform_charged_chart")
    preprocess = load(PREPROCESS, "uniform_charged_preprocess")
    for t in args.t:
        data = chart.build(t=t, gauged=True)
        reduction = preprocess.reduce_chart(
            data, max_pivots=512, max_seconds=900.0,
            max_expression_bytes=80_000_000,
        )
        weights = natural_weights(data)
        residual_variables = reduction.remaining_variables + [reduction.c]
        if set(residual_variables) != set(weights).intersection(residual_variables):
            raise AssertionError("missing residual weights")
        degrees = [row_weight(row.expr, residual_variables, weights)
                   for row in reduction.rows]
        x = sp.Symbol("q%d_1" % (t + 1))
        y = sp.Symbol("q%d_1" % (2 * t + 1))
        if x not in residual_variables or y not in residual_variables:
            raise AssertionError("normalizer coordinates absent")
        sparse = []
        for row in reduction.rows:
            if row.expr.free_symbols <= {x, y, reduction.c}:
                sparse.append((row.source_index, row.h_power, row.monomial,
                               primitive(row.expr, [reduction.c, x, y])))
        print("T", t)
        print("DIMS", len(data["tagged"]), len(data["params"]) + 1,
              len(reduction.pivots), len(reduction.rows),
              len(reduction.remaining_variables) + 1)
        print("WEIGHTS", x, weights[x], y, weights[y], reduction.c,
              weights[reduction.c], "ALL_POSITIVE", min(weights.values()) > 0,
              "ROWS_HOMOGENEOUS", len(degrees))
        print("PIVOT_BANDS", min(p.h_power for p in reduction.pivots),
              max(p.h_power for p in reduction.pivots))
        for item in sparse:
            print("SPARSE", *item)


if __name__ == "__main__":
    main()
