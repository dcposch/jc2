#!/usr/bin/env python3
"""Reconstruct normalized K=16 terminal systems from the frozen drivers.

The only mathematical inputs are the frozen ``t_order_system.py`` and
``triangular_preprocess.py``.  The latter performs the charged Q-constant
spine.  This file implements the subsequently documented operations:

* set x=q_(t+1),A to one and replace c by the closed normalizer image;
* take primitive Q-associates, then reduce canonically modulo H_t;
* delete only zero rows or literal equal canonical representatives;
* make affine substitutions only when the coefficient is a proved unit of
  A_t=Q[y]/(H_t).  This remains valid on split fibres: a nonzero zero divisor
  is skipped, never inverted.

The affine candidate score is the deterministic score printed in the frozen
``t2_t1_normalized_audit.py``.  Thus this is an independent reconstruction,
not an import of the unavailable second-stage helper.
"""

from __future__ import annotations

import argparse
import dataclasses
import importlib.util
import json
import pathlib
import sys
import time

import sympy as sp


INPUT = pathlib.Path("/tmp/jc2-lane.jRo7RD/inputs")
OUT = pathlib.Path("/home/ubuntu/jc2/box/k16spine-20260903")


def load(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@dataclasses.dataclass
class Row:
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    expr: sp.Expr


class QuadraticAlgebra:
    def __init__(self, t: int, y: sp.Symbol, auxiliary: list[sp.Symbol]):
        self.t = t
        self.y = y
        self.auxiliary = list(auxiliary)
        self.H = sp.expand(
            12 * (2*t + 1)**2 * y**2
            - 12 * (2*t + 1) * (t + 1) * y
            + (t + 1) * (3*t + 2)
        )
        self.domain = sp.QQ[tuple(auxiliary)]
        self.hpoly = sp.Poly(self.H, y, domain=self.domain)

    def reduce(self, expr: sp.Expr) -> sp.Expr:
        poly = sp.Poly(sp.expand(expr), self.y, domain=self.domain)
        return sp.expand(poly.rem(self.hpoly).as_expr())

    def inverse(self, coefficient: sp.Expr) -> sp.Expr:
        coefficient = self.reduce(coefficient)
        if coefficient == 0 or coefficient.free_symbols - {self.y}:
            raise ZeroDivisionError("coefficient is not an A_t scalar unit")
        try:
            inverse = sp.invert(
                sp.Poly(coefficient, self.y, domain=sp.QQ),
                sp.Poly(self.H, self.y, domain=sp.QQ),
            ).as_expr()
        except Exception as exc:
            raise ZeroDivisionError("zero divisor in A_t") from exc
        inverse = self.reduce(inverse)
        if self.reduce(coefficient * inverse - 1) != 0:
            raise AssertionError("inverse identity failed")
        return inverse


def primitive(tp, expr: sp.Expr, variables: list[sp.Symbol]):
    poly, multiplier, _denom, _content = tp.primitive_integer_polynomial(
        expr, variables
    )
    return poly.as_expr(), multiplier


def deduplicate(rows: list[Row], algebra: QuadraticAlgebra):
    kept: list[Row] = []
    dropped: list[dict] = []
    seen: dict[sp.Expr, Row] = {}
    for row in rows:
        expr = algebra.reduce(row.expr)
        if expr == 0:
            dropped.append({"source": row.source_index, "reason": "zero_mod_H"})
        elif expr in seen:
            dropped.append({
                "source": row.source_index,
                "reason": "literal_duplicate_mod_H",
                "representative": seen[expr].source_index,
            })
        else:
            normalized = dataclasses.replace(row, expr=expr)
            seen[expr] = normalized
            kept.append(normalized)
    return kept, dropped


def affine_candidates(
    rows: list[Row], remaining: list[sp.Symbol], algebra: QuadraticAlgebra
):
    occurrences = {
        variable: sum(variable in row.expr.free_symbols for row in rows)
        for variable in remaining
    }
    candidates = []
    for row_index, row in enumerate(rows):
        terms = sp.Add.make_args(row.expr)
        for variable_index, variable in enumerate(remaining):
            if variable not in row.expr.free_symbols:
                continue
            coefficient_terms = []
            remainder_terms = []
            nonlinear = False
            for term in terms:
                exponent = term.as_powers_dict().get(variable, 0)
                if exponent == 0:
                    remainder_terms.append(term)
                elif exponent == 1:
                    coefficient_terms.append(term / variable)
                else:
                    nonlinear = True
                    break
            if nonlinear:
                continue
            coefficient = sp.Add(*coefficient_terms)
            remainder = sp.Add(*remainder_terms)
            if coefficient == 0 or coefficient.free_symbols - {algebra.y}:
                continue
            if algebra.reduce(row.expr - coefficient*variable - remainder) != 0:
                raise AssertionError("affine decomposition failed")
            score = (
                len(str(remainder))*occurrences[variable],
                len(str(remainder)),
                occurrences[variable],
                len(str(row.expr)),
                row.source_index,
                variable_index,
            )
            candidates.append(
                (score, row_index, variable_index, coefficient, remainder)
            )
    return candidates


def eliminate(rows, auxiliary, algebra, max_seconds, max_bytes):
    started = time.monotonic()
    remaining = list(auxiliary)
    rows, dropped = deduplicate(rows, algebra)
    pivots = []
    terminal_unit = None
    while True:
        if time.monotonic() - started > max_seconds:
            raise RuntimeError("second-stage time bound exceeded")
        constants = sorted(
            [r for r in rows if not (r.expr.free_symbols - {algebra.y})],
            key=lambda r: (len(str(r.expr)), r.source_index),
        )
        for row in constants:
            try:
                inverse = algebra.inverse(row.expr)
            except ZeroDivisionError:
                continue
            terminal_unit = {
                "source": row.source_index,
                "band": row.h_power,
                "constant": str(row.expr),
                "inverse": str(inverse),
            }
            return rows, remaining, pivots, dropped, terminal_unit

        chosen = None
        for candidate in sorted(
            affine_candidates(rows, remaining, algebra), key=lambda item: item[0]
        ):
            try:
                inverse = algebra.inverse(candidate[3])
            except ZeroDivisionError:
                continue
            chosen = (*candidate, inverse)
            break
        if chosen is None:
            break
        (_score, row_index, variable_index, coefficient, remainder, inverse) = chosen
        pivot_row = rows[row_index]
        variable = remaining[variable_index]
        rhs = algebra.reduce(-inverse*remainder)
        if algebra.reduce(pivot_row.expr.subs(variable, rhs)) != 0:
            raise AssertionError("pivot substitution failed")
        del rows[row_index]
        del remaining[variable_index]
        next_rows = [
            dataclasses.replace(
                row, expr=algebra.reduce(row.expr.subs(variable, rhs))
            )
            for row in rows
        ]
        rows, newly_dropped = deduplicate(next_rows, algebra)
        dropped.extend(newly_dropped)
        resultant = sp.factor(sp.resultant(algebra.H, coefficient, algebra.y))
        pivots.append({
            "step": len(pivots) + 1,
            "source": pivot_row.source_index,
            "band": pivot_row.h_power,
            "monomial": list(pivot_row.monomial),
            "variable": str(variable),
            "coefficient": str(algebra.reduce(coefficient)),
            "inverse": str(inverse),
            "resultant_H_coefficient": str(resultant),
            "rhs": str(rhs),
            "rows_after": len(rows),
            "variables_after": len(remaining),
        })
        expression_bytes = sum(len(str(row.expr)) for row in rows)
        if expression_bytes > max_bytes:
            raise RuntimeError(
                "second-stage expression byte bound exceeded: %d" % expression_bytes
            )
    return rows, remaining, pivots, dropped, terminal_unit


def canonical_schedule(t: int, order: str = "side-first"):
    """The band/tag/variable schedule conjectured from the frozen systems."""
    e, q = 3*t + 1, 2*t + 1
    schedule = []
    for band in range(2*t, -1, -1):
        if band == 2*t:
            schedule.append((band, (0, 1), sp.Symbol("a%d_0" % (2*t + 1))))
        middle = []
        if band < 2*t:
            if band <= t:
                middle.append((band, (1, 2), sp.Symbol("q%d_0" % (2*t-band))))
            elif band < 2*t:
                middle.append((band, (1, 2), sp.Symbol("q%d_1" % (e-band))))
            if band == 0:
                middle.append((band, (1, 1), sp.Symbol("q%d_0" % q)))
            elif band < t:
                middle.append((band, (1, 1), sp.Symbol("a%d_0" % (t-band))))
        if band == 0:
            variable = sp.Symbol("b1")
        elif band == t:
            variable = sp.Symbol("b2")
        else:
            variable = sp.Symbol("a%d_0" % (e-band))
        constant_entry = (band, (0, 0), variable)
        if order == "side-first" or band == 2*t:
            schedule.extend(middle)
            schedule.append(constant_entry)
        elif order == "constant-first":
            schedule.append(constant_entry)
            schedule.extend(middle)
        else:
            raise ValueError(order)
    return schedule


def canonical_eliminate(rows, auxiliary, algebra, t, max_seconds, max_bytes,
                        order="side-first"):
    """Apply a prescribed high-to-low schedule, checking every assertion.

    Rows are not opportunistically deduplicated during the pass.  This keeps
    the advertised (0,2) companions available for a separate terminal audit
    and makes the schedule independent of representative choices.
    """
    started = time.monotonic()
    remaining = list(auxiliary)
    current = [dataclasses.replace(row, expr=algebra.reduce(row.expr)) for row in rows]
    pivots = []
    for step, (band, monomial, variable) in enumerate(canonical_schedule(t, order), 1):
        if time.monotonic() - started > max_seconds:
            raise RuntimeError("canonical second-stage time bound exceeded")
        matches = [
            (index, row) for index, row in enumerate(current)
            if row.h_power == band and row.monomial == monomial and row.expr != 0
        ]
        if len(matches) != 1:
            raise AssertionError(
                "canonical row multiplicity at band/tag %s: %d"
                % ((band, monomial), len(matches))
            )
        row_index, pivot_row = matches[0]
        if variable not in remaining:
            raise AssertionError("scheduled variable absent: %s" % variable)
        terms = sp.Add.make_args(pivot_row.expr)
        coefficient_terms = []
        remainder_terms = []
        for term in terms:
            exponent = term.as_powers_dict().get(variable, 0)
            if exponent == 0:
                remainder_terms.append(term)
            elif exponent == 1:
                coefficient_terms.append(term/variable)
            else:
                raise AssertionError(
                    "scheduled row is nonlinear in %s at step %d" % (variable, step)
                )
        coefficient = algebra.reduce(sp.Add(*coefficient_terms))
        remainder = algebra.reduce(sp.Add(*remainder_terms))
        if coefficient == 0 or coefficient.free_symbols - {algebra.y}:
            raise AssertionError(
                "scheduled coefficient is not an A_t scalar: %s" % coefficient
            )
        try:
            inverse = algebra.inverse(coefficient)
        except ZeroDivisionError as exc:
            raise ZeroDivisionError(
                "canonical nonunit at step %d band=%d tag=%s variable=%s "
                "coefficient=%s" % (step, band, monomial, variable, coefficient)
            ) from exc
        rhs = algebra.reduce(-inverse*remainder)
        if algebra.reduce(pivot_row.expr.subs(variable, rhs)) != 0:
            raise AssertionError("canonical pivot substitution failed")
        del current[row_index]
        remaining.remove(variable)
        current = [
            dataclasses.replace(row, expr=algebra.reduce(row.expr.subs(variable, rhs)))
            for row in current
        ]
        resultant = sp.factor(sp.resultant(algebra.H, coefficient, algebra.y))
        pivots.append({
            "step": step,
            "source": pivot_row.source_index,
            "band": band,
            "monomial": list(monomial),
            "variable": str(variable),
            "coefficient": str(coefficient),
            "inverse": str(inverse),
            "resultant_H_coefficient": str(resultant),
            "rhs": str(rhs),
        })
        expression_bytes = sum(len(str(row.expr)) for row in current)
        if expression_bytes > max_bytes:
            raise RuntimeError(
                "canonical expression byte bound exceeded: %d" % expression_bytes
            )

    expected_remaining = [sp.Symbol("b3"), sp.Symbol("b4")]
    expected_remaining.extend(sp.Symbol("q%d_0" % j) for j in range(2, t))
    if remaining != expected_remaining:
        raise AssertionError(
            "canonical residual variable order differs: %s != %s"
            % (remaining, expected_remaining)
        )
    terminal = [
        row for row in current
        if row.h_power < 2*t and row.monomial == (0, 1)
    ]
    terminal.sort(key=lambda row: row.h_power)
    if [row.h_power for row in terminal] != list(range(2*t)):
        raise AssertionError("terminal band list differs")
    companions = [
        row for row in current
        if row.h_power < 2*t and row.monomial == (0, 2)
    ]
    companions.sort(key=lambda row: row.h_power)
    if [row.h_power for row in companions] != list(range(2*t)):
        raise AssertionError("companion band list differs")
    extras = [row for row in current if row not in terminal and row not in companions]
    if extras:
        raise AssertionError(
            "unexpected rows after canonical schedule: %s"
            % [(r.h_power, r.monomial, r.source_index) for r in extras]
        )

    companion_audit = []
    for companion in companions:
        status = "nonzero_unmatched"
        representative = None
        scalar = None
        if companion.expr == 0:
            status = "zero"
        else:
            for candidate in terminal:
                # Test proportionality by a scalar in A_t using one nonzero
                # coefficient in the common residual polynomial ring.
                p = sp.Poly(companion.expr, *remaining,
                            domain=sp.QQ.frac_field(algebra.y))
                q = sp.Poly(candidate.expr, *remaining,
                            domain=sp.QQ.frac_field(algebra.y))
                if p.is_zero or q.is_zero or set(p.monoms()) != set(q.monoms()):
                    continue
                monomial = p.monoms()[0]
                ratio = algebra.reduce(p.coeff_monomial(monomial)
                                       / q.coeff_monomial(monomial))
                if algebra.reduce(companion.expr-ratio*candidate.expr) == 0:
                    status = "A_scalar_associate"
                    representative = candidate.h_power
                    scalar = str(ratio)
                    break
        companion_audit.append({
            "source": companion.source_index,
            "band": companion.h_power,
            "status": status,
            "representative_terminal_band": representative,
            "scalar": scalar,
            "expression": str(companion.expr),
        })
    if any(item["status"] == "nonzero_unmatched" for item in companion_audit):
        raise AssertionError("a (0,2) companion is neither zero nor terminal associate")
    return terminal, remaining, pivots, companion_audit


def reconstruct(t: int, max_seconds: float, max_bytes: int, canonical: bool,
                canonical_order: str):
    chart = load(INPUT / "t_order_system.py", "terminal_chart_%d" % t)
    tp = load(INPUT / "triangular_preprocess.py", "terminal_tp_%d" % t)
    started = time.monotonic()
    data = chart.build(t=t, gauged=True)
    first = tp.reduce_chart(
        data,
        max_pivots=4*t + 32,
        max_seconds=max_seconds,
        max_expression_bytes=max_bytes,
    )
    variables = first.remaining_variables + [first.c]
    by_name = {str(v): v for v in variables}
    x = by_name["q%d_1" % (t + 1)]
    y = by_name["q%d_1" % (2*t + 1)]
    c = first.c
    H = sp.expand(
        12*(2*t + 1)**2*y**2
        - 12*(2*t + 1)*(t + 1)*y
        + (t + 1)*(3*t + 2)
    )
    cbar = sp.factor(
        sp.Rational(t*(3*t + 1), 6*(2*t + 1)**3)
        * y * ((t + 1) - 6*(2*t + 1)*y)
    )
    c_rows = [row for row in first.rows if c in row.expr.free_symbols]
    if len(c_rows) != 1:
        raise AssertionError("not exactly one c row")
    c_row = c_rows[0]
    c_coeff = sp.diff(c_row.expr, c)
    solved_c = sp.expand(-(c_row.expr-c_coeff*c)/c_coeff)
    if sp.expand(solved_c.subs(x, 1) - cbar) != 0:
        raise AssertionError("closed c image disagrees with frozen system")

    auxiliary = [v for v in first.remaining_variables if v not in (x, y)]
    q_variables = auxiliary + [y]
    sliced = []
    for row in first.rows:
        if row is c_row:
            continue
        expr = sp.expand(row.expr.subs({x: 1, c: cbar}, simultaneous=True))
        sliced.append(Row(row.source_index, row.h_power, row.monomial, expr))

    q_rows = []
    q_dropped = []
    q_seen = {}
    for row in sliced:
        expr, multiplier = primitive(tp, row.expr, q_variables)
        key = str(expr)
        if key in q_seen:
            q_dropped.append({
                "source": row.source_index,
                "reason": "rational_associate_duplicate_over_Q",
                "representative": q_seen[key],
                "multiplier": str(multiplier),
            })
        else:
            q_seen[key] = row.source_index
            q_rows.append(dataclasses.replace(row, expr=expr))

    algebra = QuadraticAlgebra(t, y, auxiliary)
    if algebra.reduce(H) != 0:
        raise AssertionError("H_t does not vanish in A_t")
    k_rows, base_dropped = deduplicate(q_rows, algebra)
    if canonical:
        rows, remaining, pivots, companion_audit = canonical_eliminate(
            k_rows, auxiliary, algebra, t,
            max_seconds=max_seconds, max_bytes=max_bytes, order=canonical_order,
        )
        dropped = companion_audit
        terminal_unit = None
    else:
        rows, remaining, pivots, dropped, terminal_unit = eliminate(
            k_rows, auxiliary, algebra, max_seconds=max_seconds, max_bytes=max_bytes
        )
    terminal = []
    for row in rows:
        primitive_expr, multiplier = primitive(tp, row.expr, [y] + remaining)
        terminal.append({
            "source": row.source_index,
            "band": row.h_power,
            "monomial": list(row.monomial),
            "degree": sp.Poly(
                row.expr, *remaining, domain=sp.QQ.frac_field(y)
            ).total_degree(),
            "term_count_over_A": len(
                sp.Poly(row.expr, *remaining, domain=sp.QQ.frac_field(y)).terms()
            ),
            "expression": str(row.expr),
            "primitive_Q_associate": str(primitive_expr),
            "primitive_multiplier": str(multiplier),
        })
    record = {
        "typing": "exact frozen-driver reconstruction; A_t-unit pivots only",
        "t": t,
        "H": str(H),
        "H_factorization_Q": str(sp.factor(H)),
        "H_discriminant": str(sp.discriminant(H, y)),
        "A_t_split": not sp.Poly(H, y, domain=sp.QQ).is_irreducible,
        "cbar": str(cbar),
        "first_stage": {
            "original_rows": len(data["tagged"]),
            "original_unknowns_including_c": len(data["params"]) + 1,
            "Q_constant_pivots": len(first.pivots),
            "rows": len(first.rows),
            "unknowns_including_c": len(first.remaining_variables) + 1,
        },
        "post_H_c": {
            "Q_rows_after_associate_dedup": len(q_rows),
            "Q_dropped": q_dropped,
            "A_rows": len(k_rows),
            "auxiliary_variables": len(auxiliary),
            "base_dropped": base_dropped,
        },
        "affine": {
            "schedule": (("canonical_band_tag_" + canonical_order)
                         if canonical else "documented_score"),
            "pivot_count": len(pivots),
            "pivots": pivots,
            "dropped": dropped,
            "terminal_unit": terminal_unit,
        },
        "terminal": {
            "row_count": len(rows),
            "variables": list(map(str, remaining)),
            "bands": [row.h_power for row in rows],
            "rows": terminal,
        },
        "elapsed_seconds": time.monotonic() - started,
    }
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int, nargs="+")
    parser.add_argument("--max-seconds", type=float, default=1800.0)
    parser.add_argument("--max-bytes", type=int, default=500_000_000)
    parser.add_argument("--stdout-only", action="store_true")
    parser.add_argument("--canonical", action="store_true")
    parser.add_argument("--canonical-order", choices=("side-first", "constant-first"),
                        default="side-first")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    for t in args.t:
        if t < 1:
            parser.error("t must be positive")
        record = reconstruct(t, args.max_seconds, args.max_bytes, args.canonical,
                             args.canonical_order)
        if not args.stdout_only:
            suffix = (("_canonical_" + args.canonical_order)
                      if args.canonical else "")
            path = OUT / ("terminal_t%d%s_exact.json" % (t, suffix))
            path.write_text(
                json.dumps(record, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
        summary = {
            "t": t,
            "first_stage": record["first_stage"],
            "post_H_c": {
                key: value for key, value in record["post_H_c"].items()
                if key in ("Q_rows_after_associate_dedup", "A_rows", "auxiliary_variables")
            },
            "affine_pivots": record["affine"]["pivot_count"],
            "terminal_unit": record["affine"]["terminal_unit"],
            "terminal_rows": record["terminal"]["row_count"],
            "terminal_variables": record["terminal"]["variables"],
            "terminal_bands": record["terminal"]["bands"],
            "elapsed_seconds": record["elapsed_seconds"],
        }
        print(json.dumps(summary, indent=2, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
