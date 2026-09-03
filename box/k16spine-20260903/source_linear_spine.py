#!/usr/bin/env python3
"""Read-only discovery of second-spine Schur pivots from charged band rows.

This constructs the exact differential of the frozen gauged chart at the
proved normalized corner, performs the proved Q-constant first spine, and
then applies the explicit band/tag second-spine schedule.  It reports only
primitive Q-associates of pivot coefficients in Q[y]/(H_t).  The script is a
discovery aid: identifying these Schur pivots with the full nonlinear affine
pivots still requires the triangular band-induction argument.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import pathlib
import re
import sys

import sympy as sp


INPUT = pathlib.Path("/tmp/jc2-lane.jRo7RD/inputs")
EXPECTED = {
    "t_order_system.py":
        "e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28",
}


def load(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def primitive_linear(expr: sp.Expr, y: sp.Symbol) -> sp.Expr:
    poly = sp.Poly(sp.cancel(expr), y, domain=sp.QQ)
    denominator, cleared = poly.clear_denoms(convert=True)
    del denominator
    _content, primitive = cleared.primitive()
    if primitive.LC() < 0:
        primitive = -primitive
    return sp.factor(primitive.as_expr())


class Algebra:
    def __init__(self, t: int, y: sp.Symbol):
        self.t = t
        self.y = y
        q = 2*t+1
        self.H = sp.expand(12*q*q*y**2 - 12*q*(t+1)*y + (t+1)*(3*t+2))
        self.hpoly = sp.Poly(self.H, y, domain=sp.QQ)

    def reduce(self, expr: sp.Expr) -> sp.Expr:
        numerator, denominator = sp.cancel(expr).as_numer_denom()
        numerator = sp.Poly(numerator, self.y, domain=sp.QQ).rem(self.hpoly)
        denominator = sp.Poly(denominator, self.y, domain=sp.QQ).rem(self.hpoly)
        inverse = sp.invert(denominator, self.hpoly)
        return sp.factor((numerator*inverse).rem(self.hpoly).as_expr())

    def inverse(self, expr: sp.Expr) -> sp.Expr:
        poly = sp.Poly(self.reduce(expr), self.y, domain=sp.QQ)
        return self.reduce(sp.invert(poly, self.hpoly).as_expr())


def name_key(variable: sp.Symbol):
    name = str(variable)
    match = re.fullmatch(r"([aq])(\d+)_(\d+)", name)
    if match:
        return (0 if match.group(1) == "a" else 1,
                int(match.group(2)), int(match.group(3)))
    match = re.fullmatch(r"b(\d+)", name)
    if match:
        return (2, int(match.group(1)), 0)
    return (3, 0, 0)


def scheduled_pivots(t: int):
    e, q = 3*t+1, 2*t+1
    yield 2*t, (0, 1), sp.Symbol(f"a{2*t+1}_0"), "top_endpoint"
    yield 2*t, (0, 0), sp.Symbol(f"a{t+1}_0"), "scalar_chain"
    for k in range(2*t-1, -1, -1):
        scalar = (sp.Symbol("b1") if k == 0 else
                  sp.Symbol("b2") if k == t else
                  sp.Symbol(f"a{e-k}_0"))
        qvar = (sp.Symbol(f"q{2*t-k}_0") if k <= t else
                sp.Symbol(f"q{e-k}_1"))
        yield k, (1, 2), qvar, "Q_chain"
        if k == 0:
            yield k, (1, 1), sp.Symbol(f"q{q}_0"), "endpoint_A"
        elif k < t:
            yield k, (1, 1), sp.Symbol(f"a{t-k}_0"), "low_P_chain"
        yield k, (0, 0), scalar, "scalar_chain"


def run(t: int, show_matrix: bool = False):
    if t < 2:
        raise ValueError("this stable schedule begins at t=2")
    chart = load(INPUT/"t_order_system.py", f"source_linear_chart_t{t}")
    data = chart.build(t=t, gauged=True)
    variables = list(data["params"]) + [data["c"]]
    y = sp.Symbol(f"q{2*t+1}_1")
    x = sp.Symbol(f"q{t+1}_1")
    e, q = 3*t+1, 2*t+1
    algebra = Algebra(t, y)

    g1 = sp.Rational(e, q)
    g2 = sp.Rational(e, q)*y + sp.Rational(e*t, 2*q*q)
    g3 = sp.Rational(e*t, q*q)*y - sp.Rational(e*t*(t+1), 6*q**3)
    cbar = sp.Rational(t*e, 6*q**3)*y*((t+1)-6*q*y)
    base = {v: sp.Integer(0) for v in variables}
    base.update({x: 1, y: y, data["c"]: cbar,
                 sp.Symbol(f"a{t+1}_1"): g1,
                 sp.Symbol(f"a{q}_2"): g2,
                 sp.Symbol(f"a{e}_3"): g3})

    # A row is its coefficient dictionary in the tangent variables.  Constants
    # are irrelevant to Schur pivots and deliberately omitted.
    rows = {}
    for source, (band, tag, expr) in enumerate(data["tagged"]):
        coeffs = {}
        for variable in variables:
            value = algebra.reduce(sp.diff(expr, variable).subs(base, simultaneous=True))
            if value != 0:
                coeffs[variable] = value
        rows[(band, tuple(tag))] = [source, coeffs]

    def pivot(band: int, tag: tuple[int, int], variable: sp.Symbol, family: str):
        key = (band, tag)
        if key not in rows:
            raise AssertionError((t, key, "missing row"))
        source, prow = rows.pop(key)
        coefficient = algebra.reduce(prow.get(variable, 0))
        if coefficient == 0:
            raise AssertionError((t, key, variable, "zero coefficient"))
        try:
            inverse = algebra.inverse(coefficient)
        except Exception as error:
            raise RuntimeError({"coefficient": str(coefficient),
                                "primitive": str(primitive_linear(coefficient, y))}) from error
        for other_source, other in rows.values():
            del other_source
            multiplier = algebra.reduce(other.get(variable, 0)*inverse)
            if multiplier != 0:
                for v in set(other) | set(prow):
                    value = algebra.reduce(other.get(v, 0)-multiplier*prow.get(v, 0))
                    if value == 0:
                        other.pop(v, None)
                    else:
                        other[v] = value
            other.pop(variable, None)
        u = primitive_linear(coefficient, y)
        resultant = sp.factor(sp.resultant(algebra.H, u, y))
        return source, u, resultant

    # Proved first spine, in its frozen deterministic order.
    for i in range(t+1, 2*t+1):
        pivot(5*t+2-i, (0, 1), sp.Symbol(f"a{i}_1"), "first_A")
    for i in range(2*t+1, e+1):
        band = 5*t+2-i
        pivot(band, (0, 0), sp.Symbol(f"a{i}_2"), "first_B")
        pivot(band, (0, 1), sp.Symbol(f"a{i}_1"), "first_A")
    pivot(2*t, (0, 3), sp.Symbol(f"a{e}_0"), "first_gamma")
    pivot(2*t, (1, 2), sp.Symbol(f"a{e}_3"), "first_z")

    if show_matrix:
        d = sp.Symbol("d")
        scheduled = list(scheduled_pivots(t))
        scheduled_variables = [item[2] for item in scheduled]
        print(f"MATRIX T {t}; d=2q*y-(t+1); columns in scheduled order")
        print("COLS", *map(str, scheduled_variables))
        for band, tag, pivot_variable, family in scheduled:
            del pivot_variable, family
            source, coefficients = rows[(band, tag)]
            entries = []
            for position, variable in enumerate(scheduled_variables):
                value = coefficients.get(variable, 0)
                if value != 0:
                    value = sp.factor(value.subs(
                        y, (d+t+1)/sp.Integer(2*q)))
                    entries.append(f"{position}:{value}")
            print(f"R {band} {tag[0]}{tag[1]} src={source}", *entries)

    output = []
    pending = [list(item) + [0] for item in scheduled_pivots(t)]
    while pending:
        chosen = None
        for position, (band, tag, variable, family, defers) in enumerate(pending):
            coefficient = algebra.reduce(rows[(band, tag)][1].get(variable, 0))
            try:
                algebra.inverse(coefficient)
            except Exception:
                pending[position][4] += 1
                continue
            chosen = position
            break
        if chosen is None:
            raise RuntimeError((t, "no unit Schur pivot", pending))
        band, tag, variable, family, defers = pending.pop(chosen)
        source, u, resultant = pivot(band, tag, variable, family)
        output.append((band, tag, variable, family, defers, source, u, resultant))
    print(f"T {t} H={algebra.H}")
    classified = 0
    open_count = 0
    for band, tag, variable, family, defers, source, u, resultant in output:
        d = 2*q*y-(t+1)
        expected = None
        label = "OPEN_LOWER_SCHUR"
        if defers:
            label = "OPEN_DEFERRED_SPLIT"
        elif family == "top_endpoint":
            expected, label = sp.Integer(1), "ONE"
        elif family == "Q_chain" and band > t:
            expected, label = d, "D"
        elif family == "Q_chain" and band == t:
            expected, label = 3*d+1, "THREE_D_PLUS_ONE"
        elif family == "scalar_chain" and band > t:
            expected, label = d+(band-t), "D_PLUS_S"
        elif family == "scalar_chain" and band == t:
            expected, label = 2*d+1, "TWO_D_PLUS_ONE"
        elif family == "scalar_chain" and 0 < band < t:
            expected, label = y, "Y"
        elif family == "scalar_chain" and band == 0:
            expected, label = 5*d+2*t+3, "G5_FACTOR"
        elif family == "endpoint_A":
            expected, label = 3*d+2*(t+1), "G3_FACTOR"
        if expected is not None:
            U = sp.Poly(u, y, domain=sp.QQ)
            E = sp.Poly(expected, y, domain=sp.QQ)
            ratio = sp.Rational(U.LC(), E.LC())
            if not (U-ratio*E).is_zero:
                raise AssertionError((t, band, family, u, expected))
            classified += 1
        else:
            open_count += 1
        print(f"P\t{band}\t{tag[0]}{tag[1]}\t{family}\t{variable}\t{u}\t{resultant}\t{source}\t{defers}\t{label}")
    deferred = sum(item[4] > 0 for item in output)
    if classified != 3*t+3-deferred or open_count != 2*t-1+deferred:
        raise AssertionError((t, classified, open_count, deferred))
    print(f"CLASSIFICATION_PASS t={t} classified={classified} open={open_count}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int, nargs="+")
    parser.add_argument("--matrix", action="store_true")
    args = parser.parse_args()
    for name, expected in EXPECTED.items():
        actual = hashlib.sha256((INPUT/name).read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError((name, actual))
    for t in args.t:
        run(t, show_matrix=args.matrix)


if __name__ == "__main__":
    main()
