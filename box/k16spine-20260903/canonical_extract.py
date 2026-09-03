#!/usr/bin/env python3
"""Canonical exact post-H/c extraction for the K=16 ray, t=2,...,6.

Mathematical input is restricted to the frozen charged chart builder and the
frozen charged Q-constant reducer.  The second pass is deliberately simple:

* bands: descending h-band, with an explicit tag/variable schedule;
* variables: the schedule uses only numerical a(i,j), q(i,j), b names;
* a scheduled pivot is accepted only when its row is affine in the named
  variable and its coefficient is a unit of Q[y]/(H_t);
* after every substitution reduce modulo H_t and replace each row by its
  primitive integral Q-associate before zero/duplicate deletion.

Thus the output is independent of SymPy's expression traversal order.  It is
an extraction/audit driver, not a proof that this pivot order is uniform in t.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import importlib.util
import json
import pathlib
import re
import sys
import time
from typing import Iterable

import sympy as sp


ROOT = pathlib.Path("/home/ubuntu/jc2")
OUT = ROOT / "box/k16spine-20260903"
INPUT = pathlib.Path("/tmp/jc2-lane.jRo7RD/inputs")
CHART = INPUT / "t_order_system.py"
PREPROCESS = INPUT / "triangular_preprocess.py"
EXPECTED = {
    "t_order_system.py":
        "e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28",
    "triangular_preprocess.py":
        "f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93",
}


@dataclasses.dataclass(frozen=True)
class CRow:
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    expr: sp.Expr


@dataclasses.dataclass
class LazyRow:
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    expr: sp.Expr
    substitutions_applied: int = 0


def digest(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def vector_digest(expressions: Iterable[sp.Expr]) -> str:
    text = "\n".join(str(sp.expand(expr)) for expr in expressions) + "\n"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def variable_key(variable: sp.Symbol) -> tuple[int, int, int, str]:
    name = str(variable)
    match = re.fullmatch(r"a(\d+)_(\d+)", name)
    if match:
        return (0, int(match.group(1)), int(match.group(2)), name)
    match = re.fullmatch(r"q(\d+)_(\d+)", name)
    if match:
        return (1, int(match.group(1)), int(match.group(2)), name)
    match = re.fullmatch(r"b(\d+)", name)
    if match:
        return (2, int(match.group(1)), 0, name)
    return (3, 0, 0, name)


def row_key(row: CRow) -> tuple[int, int, int, int]:
    return (-row.h_power, row.monomial[0], row.monomial[1], row.source_index)


POST_TAG_PRIORITY = {
    (1, 2): 0,
    (1, 1): 1,
    (0, 2): 2,
    (0, 1): 3,
    (0, 0): 4,
}


def normalization_row_key(row: CRow):
    """Prefer the five uniform tag families when choosing Q associates."""
    return (-row.h_power, POST_TAG_PRIORITY.get(row.monomial, 10),
            row.monomial[0], row.monomial[1], row.source_index)


class QuadraticAlgebra:
    """Exact arithmetic in A_t=Q[y]/(H_t), including split fibers."""

    def __init__(self, t: int, y: sp.Symbol, auxiliaries: list[sp.Symbol]):
        self.t = t
        self.y = y
        self.auxiliaries = list(auxiliaries)
        q = 2*t + 1
        self.H_raw = sp.expand(
            12*q*q*y**2 - 12*q*(t+1)*y + (t+1)*(3*t+2)
        )
        raw_poly = sp.Poly(self.H_raw, y, domain=sp.QQ)
        _content, primitive = raw_poly.primitive()
        if primitive.LC() < 0:
            primitive = -primitive
        self.H = primitive.as_expr()
        self.hpoly_qq = sp.Poly(self.H, y, domain=sp.QQ)
        self.domain = sp.QQ[tuple(auxiliaries)]
        self.hpoly = sp.Poly(self.H, y, domain=self.domain)

    def reduce(self, expr: sp.Expr) -> sp.Expr:
        poly = sp.Poly(sp.expand(expr), self.y, domain=self.domain)
        return sp.expand(poly.rem(self.hpoly).as_expr())

    def inverse(self, coefficient: sp.Expr) -> sp.Expr:
        coefficient = self.reduce(coefficient)
        if coefficient == 0 or coefficient.free_symbols - {self.y}:
            raise sp.NotInvertible("not a coefficient-algebra unit")
        inv = sp.invert(sp.Poly(coefficient, self.y, domain=sp.QQ),
                       self.hpoly_qq).as_expr()
        inv = self.reduce(inv)
        if self.reduce(coefficient*inv - 1) != 0:
            raise AssertionError("inverse identity failed")
        return inv

    def resultant(self, coefficient: sp.Expr, raw: bool = True) -> sp.Expr:
        h = self.H_raw if raw else self.H
        return sp.factor(sp.resultant(h, coefficient, self.y))


def primitive_expr(expr: sp.Expr, variables: list[sp.Symbol]) -> tuple[sp.Expr, sp.Rational]:
    """Canonical primitive integral Q-associate, with positive leading term."""
    expr = sp.expand(expr)
    poly = sp.Poly(expr, *variables, domain=sp.QQ)
    denominator, cleared = poly.clear_denoms(convert=True)
    content, primitive = cleared.primitive()
    multiplier = sp.Rational(denominator, content)
    if primitive.LC() < 0:
        primitive = -primitive
        multiplier = -multiplier
    ans = primitive.as_expr()
    if sp.expand(ans - multiplier*expr) != 0:
        raise AssertionError("primitive normalization identity failed")
    return ans, multiplier


def canonical_row(row: CRow, algebra: QuadraticAlgebra,
                  remaining: list[sp.Symbol]) -> tuple[CRow | None, sp.Rational | None]:
    expr = algebra.reduce(row.expr)
    if expr == 0:
        return None, None
    expr, multiplier = primitive_expr(expr, remaining + [algebra.y])
    # A rational rescale preserves the already degree-<2 y representative.
    return dataclasses.replace(row, expr=expr), multiplier


def canonicalize_rows(rows: list[CRow], algebra: QuadraticAlgebra,
                      remaining: list[sp.Symbol], stage: str,
                      order_key=row_key):
    kept: list[CRow] = []
    dropped: list[dict] = []
    seen: dict[str, CRow] = {}
    for row in sorted(rows, key=order_key):
        normalized, multiplier = canonical_row(row, algebra, remaining)
        if normalized is None:
            dropped.append({"stage": stage, "source": row.source_index,
                            "band": row.h_power, "reason": "zero_mod_H"})
            continue
        key = str(normalized.expr)
        if key in seen:
            representative = seen[key]
            dropped.append({"stage": stage, "source": row.source_index,
                            "band": row.h_power, "reason": "duplicate_mod_H_Qstar",
                            "representative_source": representative.source_index,
                            "representative_band": representative.h_power,
                            "primitive_multiplier": str(multiplier)})
            continue
        seen[key] = normalized
        kept.append(normalized)
    return kept, dropped


def rational_associate(left: sp.Expr, right: sp.Expr,
                       variables: list[sp.Symbol]) -> sp.Rational | None:
    L = sp.Poly(left, *variables, domain=sp.QQ)
    R = sp.Poly(right, *variables, domain=sp.QQ)
    if L.is_zero or R.is_zero:
        return None
    ratio = sp.Rational(L.LC(), R.LC())
    return ratio if (L-ratio*R).is_zero else None


def normalize_post_hc(tp, reduction, t: int):
    variables = reduction.remaining_variables + [reduction.c]
    by_name = {str(v): v for v in variables}
    x = by_name[f"q{t+1}_1"]
    y = by_name[f"q{2*t+1}_1"]
    c = reduction.c
    q = 2*t + 1
    Hhom = sp.expand(
        12*q*q*y**2 - 12*q*(t+1)*x**2*y + (t+1)*(3*t+2)*x**4
    )
    c_image = sp.expand(
        sp.Rational(t*(3*t+1), 6*q**3) * x*y * ((t+1)*x**2 - 6*q*y)
    )

    c_rows = [row for row in reduction.rows if c in row.expr.free_symbols]
    if len(c_rows) != 1:
        raise AssertionError((t, "expected one c row", len(c_rows)))
    c_row = c_rows[0]
    c_coefficient = sp.diff(c_row.expr, c)
    if not c_coefficient.is_Rational or c_coefficient == 0:
        raise AssertionError("c row lacks Q* coefficient")
    solved_c = sp.expand(-(c_row.expr-c_coefficient*c)/c_coefficient)
    if sp.expand(solved_c-c_image) != 0:
        raise AssertionError((t, "closed c image mismatch", solved_c, c_image))

    h_matches = []
    for row in reduction.rows:
        if row is c_row or not row.expr.free_symbols <= {x, y}:
            continue
        ratio = rational_associate(row.expr, Hhom, variables)
        if ratio is not None:
            h_matches.append((row, ratio))
    if len(h_matches) != 1:
        raise AssertionError((t, "expected one H row", h_matches))
    h_row, h_ratio = h_matches[0]

    auxiliaries = sorted(
        [v for v in reduction.remaining_variables if v not in (x, y)],
        key=variable_key,
    )
    algebra = QuadraticAlgebra(t, y, auxiliaries)
    if algebra.reduce(Hhom.subs(x, 1)) != 0:
        raise AssertionError("closed H does not vanish")
    c_slice = sp.expand(c_image.subs(x, 1))
    c_inverse = algebra.inverse(c_slice)

    # First expose Q-associates exactly as in the charged normalization.
    raw: list[CRow] = []
    for old in reduction.rows:
        if old is c_row:
            continue
        expr = sp.expand(old.expr.subs({x: 1, c: c_slice}, simultaneous=True))
        raw.append(CRow(old.source_index, old.h_power, old.monomial, expr))
    q_variables = auxiliaries + [y]
    q_rows: list[CRow] = []
    q_dropped: list[dict] = []
    q_seen: dict[str, CRow] = {}
    for row in sorted(raw, key=normalization_row_key):
        expr, multiplier = primitive_expr(row.expr, q_variables)
        key = str(expr)
        if key in q_seen:
            rep = q_seen[key]
            q_dropped.append({"source": row.source_index, "band": row.h_power,
                              "reason": "duplicate_Qstar_before_H",
                              "representative_source": rep.source_index,
                              "multiplier": str(multiplier)})
        else:
            normalized = dataclasses.replace(row, expr=expr)
            q_seen[key] = normalized
            q_rows.append(normalized)

    post_rows, h_dropped = canonicalize_rows(
        q_rows, algebra, auxiliaries, "initial_mod_H",
        order_key=normalization_row_key,
    )
    checks = {
        "x": str(x), "y": str(y),
        "H_raw": str(algebra.H_raw), "H_primitive": str(algebra.H),
        "H_raw_content": str(sp.Poly(algebra.H_raw, y).content()),
        "H_discriminant_raw": str(sp.discriminant(algebra.H_raw, y)),
        "H_squarefree": bool(sp.gcd(sp.Poly(algebra.H, y),
                                      sp.Poly(sp.diff(algebra.H, y), y)).degree() == 0),
        "H_factorization_Q": str(sp.factor(algebra.H)),
        "H_source": h_row.source_index, "H_band": h_row.h_power,
        "H_row_associate_ratio": str(h_ratio),
        "c_source": c_row.source_index, "c_band": c_row.h_power,
        "c_coefficient": str(c_coefficient),
        "c_slice": str(c_slice), "c_inverse": str(c_inverse),
        "c_inverse_checked": algebra.reduce(c_slice*c_inverse-1) == 0,
        "raw_rows_excluding_c": len(raw),
        "rows_after_Qstar_dedup": len(q_rows),
        "post_Hc_rows": len(post_rows),
        "post_Hc_auxiliaries": len(auxiliaries),
        "Qstar_dropped": q_dropped,
        "initial_mod_H_dropped": h_dropped,
    }
    return post_rows, auxiliaries, algebra, checks


def affine_decomposition(row: CRow, variable: sp.Symbol,
                         algebra: QuadraticAlgebra):
    if variable not in row.expr.free_symbols:
        return None
    coefficient = algebra.reduce(sp.diff(row.expr, variable))
    if variable in coefficient.free_symbols or coefficient.free_symbols - {algebra.y}:
        return None
    remainder = algebra.reduce(row.expr-coefficient*variable)
    if variable in remainder.free_symbols:
        return None
    if algebra.reduce(row.expr-coefficient*variable-remainder) != 0:
        raise AssertionError("affine decomposition failed")
    try:
        inverse = algebra.inverse(coefficient)
    except Exception:
        return None
    return coefficient, remainder, inverse


def primitive_coefficient(coefficient: sp.Expr, y: sp.Symbol):
    u, multiplier = primitive_expr(coefficient, [y])
    return u, multiplier


def eliminate_canonical(rows: list[CRow], auxiliaries: list[sp.Symbol],
                        algebra: QuadraticAlgebra):
    remaining = list(auxiliaries)
    rows, dropped = canonicalize_rows(rows, algebra, remaining, "affine_start")
    pivots: list[dict] = []
    terminal_unit = None
    while True:
        # A coefficient-algebra unit row proves immediate inconsistency.
        constants = [r for r in rows if not (r.expr.free_symbols-{algebra.y})]
        for row in sorted(constants, key=row_key):
            try:
                inv = algebra.inverse(row.expr)
            except Exception:
                continue
            terminal_unit = {
                "source": row.source_index, "band": row.h_power,
                "coefficient": str(row.expr), "inverse": str(inv),
                "resultant_H_raw": str(algebra.resultant(row.expr, raw=True)),
            }
            return rows, remaining, pivots, dropped, terminal_unit

        chosen = None
        for row_index, row in sorted(enumerate(rows), key=lambda z: row_key(z[1])):
            for variable_index, variable in enumerate(remaining):
                decomposition = affine_decomposition(row, variable, algebra)
                if decomposition is not None:
                    chosen = (row_index, row, variable_index, variable, decomposition)
                    break
            if chosen is not None:
                break
        if chosen is None:
            return rows, remaining, pivots, dropped, terminal_unit

        row_index, pivot_row, variable_index, variable, decomposition = chosen
        coefficient, remainder, inverse = decomposition
        rhs = algebra.reduce(-inverse*remainder)
        if algebra.reduce(pivot_row.expr.subs(variable, rhs)) != 0:
            raise AssertionError("pivot substitution does not kill row")
        u, u_multiplier = primitive_coefficient(coefficient, algebra.y)
        res_raw = algebra.resultant(u, raw=True)
        res_primitive = algebra.resultant(u, raw=False)
        if res_raw == 0 or res_primitive == 0:
            raise AssertionError("accepted pivot has zero resultant")

        del rows[row_index]
        del remaining[variable_index]
        substituted = []
        for row in rows:
            expr = row.expr
            if variable in expr.free_symbols:
                expr = algebra.reduce(expr.subs(variable, rhs))
            substituted.append(dataclasses.replace(row, expr=expr))
        rows, new_dropped = canonicalize_rows(
            substituted, algebra, remaining, f"after_pivot_{len(pivots)+1}"
        )
        dropped.extend(new_dropped)
        pivots.append({
            "step": len(pivots)+1,
            "source": pivot_row.source_index,
            "band": pivot_row.h_power,
            "monomial": list(pivot_row.monomial),
            "variable": str(variable),
            "coefficient": str(coefficient),
            "coefficient_inverse": str(inverse),
            "u_primitive_Q_associate": str(u),
            "u_equals_multiplier_times_coefficient": str(u_multiplier),
            "resultant_H_raw_u": str(res_raw),
            "resultant_H_primitive_u": str(res_primitive),
            "rhs": str(rhs),
            "inverse_checked": algebra.reduce(coefficient*inverse-1) == 0,
            "substitution_checked": True,
            "rows_after": len(rows),
            "variables_after": len(remaining),
            "expression_bytes_after": sum(len(str(r.expr)) for r in rows),
        })
        print(json.dumps({"phase": "affine_pivot", "t": algebra.t,
                          "step": len(pivots), "band": pivot_row.h_power,
                          "variable": str(variable), "rows": len(rows),
                          "variables": len(remaining),
                          "bytes": pivots[-1]["expression_bytes_after"]},
                         sort_keys=True), flush=True)


def scheduled_pivots_at_band(t: int, k: int):
    """The fixed second-spine schedule, high band to low band."""
    e, q = 3*t+1, 2*t+1
    if k == 2*t:
        return [
            ((0, 1), sp.Symbol(f"a{2*t+1}_0"), "top_endpoint"),
            ((0, 0), sp.Symbol(f"a{e-k}_0"), "scalar_chain"),
        ]
    if k < 0 or k >= 2*t:
        raise ValueError(k)
    if k == 0:
        scalar = sp.Symbol("b1")
    elif k == t:
        scalar = sp.Symbol("b2")
    else:
        scalar = sp.Symbol(f"a{e-k}_0")
    if k <= t:
        qvar = sp.Symbol(f"q{2*t-k}_0")
    else:
        qvar = sp.Symbol(f"q{e-k}_1")
    answer = [((1, 2), qvar, "Q_chain")]
    if k == 0:
        answer.append(((1, 1), sp.Symbol(f"q{q}_0"), "endpoint_A"))
    elif 1 <= k <= t-1:
        answer.append(((1, 1), sp.Symbol(f"a{t-k}_0"), "low_P_chain"))
    answer.append(((0, 0), scalar, "scalar_chain"))
    return answer


def eliminate_scheduled(rows: list[CRow], auxiliaries: list[sp.Symbol],
                        algebra: QuadraticAlgebra):
    """Apply the explicit 5t+2 pivot schedule and 2t row syzygy drops."""
    t = algebra.t
    remaining = sorted(auxiliaries, key=variable_key)
    current: list[CRow] = list(sorted(rows, key=normalization_row_key))
    dropped: list[dict] = []
    pivots: list[dict] = []

    def locate(k: int, tag: tuple[int, int]) -> tuple[int, CRow]:
        matches = [(i, row) for i, row in enumerate(current)
                   if row.h_power == k and row.monomial == tag]
        if len(matches) != 1:
            available = [list(row.monomial) for row in current if row.h_power == k]
            raise AssertionError({"t": t, "band": k, "wanted_tag": list(tag),
                                  "matches": len(matches), "available": available})
        return matches[0]

    def apply(k: int, tag: tuple[int, int], variable: sp.Symbol,
              family: str, deferral_history: list[dict]):
        nonlocal current, remaining
        if variable not in remaining:
            raise AssertionError({"t": t, "band": k, "tag": tag,
                                  "variable_not_remaining": str(variable),
                                  "remaining": list(map(str, remaining))})
        row_index, pivot_row = locate(k, tag)
        decomposition = affine_decomposition(pivot_row, variable, algebra)
        if decomposition is None:
            coefficient = algebra.reduce(sp.diff(pivot_row.expr, variable))
            remainder = algebra.reduce(pivot_row.expr-coefficient*variable)
            raise AssertionError({"t": t, "band": k, "tag": tag,
                                  "variable": str(variable),
                                  "coefficient": str(coefficient),
                                  "coefficient_symbols": sorted(map(str,
                                      coefficient.free_symbols)),
                                  "variable_in_remainder": variable in remainder.free_symbols,
                                  "reason": "scheduled coefficient is not a proved A_t unit"})
        coefficient, remainder, inverse = decomposition
        rhs = algebra.reduce(-inverse*remainder)
        if algebra.reduce(pivot_row.expr.subs(variable, rhs)) != 0:
            raise AssertionError("scheduled pivot substitution failed")
        u, u_multiplier = primitive_coefficient(coefficient, algebra.y)
        res_raw = algebra.resultant(u, raw=True)
        res_primitive = algebra.resultant(u, raw=False)
        if res_raw == 0 or res_primitive == 0:
            raise AssertionError("scheduled pivot resultant vanishes")

        del current[row_index]
        remaining.remove(variable)
        next_rows: list[CRow] = []
        zero_drops = []
        for row in current:
            expr = row.expr
            if variable in expr.free_symbols:
                expr = algebra.reduce(expr.subs(variable, rhs))
                candidate, multiplier = canonical_row(
                    dataclasses.replace(row, expr=expr), algebra, remaining
                )
            else:
                candidate, multiplier = row, sp.Integer(1)
            if candidate is None:
                record = {"stage": f"after_pivot_{len(pivots)+1}",
                          "source": row.source_index, "band": row.h_power,
                          "monomial": list(row.monomial),
                          "reason": "zero_mod_H"}
                dropped.append(record)
                zero_drops.append(record)
            else:
                next_rows.append(candidate)
        current = next_rows

        pivots.append({
            "step": len(pivots)+1,
            "family": family,
            "source": pivot_row.source_index,
            "band": pivot_row.h_power,
            "monomial": list(pivot_row.monomial),
            "variable": str(variable),
            "coefficient": str(coefficient),
            "coefficient_inverse": str(inverse),
            "u_primitive_Q_associate": str(u),
            "u_equals_multiplier_times_coefficient": str(u_multiplier),
            "resultant_H_raw_u": str(res_raw),
            "resultant_H_primitive_u": str(res_primitive),
            "rhs": str(rhs),
            "inverse_checked": algebra.reduce(coefficient*inverse-1) == 0,
            "substitution_checked": True,
            "rows_after": len(current),
            "variables_after": len(remaining),
            "zero_rows_created": zero_drops,
            "nonunit_deferral_history": deferral_history,
            "expression_bytes_after": sum(len(str(r.expr)) for r in current),
        })
        print(json.dumps({"phase": "scheduled_pivot", "t": t,
                          "step": len(pivots), "band": k, "tag": list(tag),
                          "family": family, "variable": str(variable),
                          "rows": len(current), "variables": len(remaining),
                          "bytes": pivots[-1]["expression_bytes_after"]},
                         sort_keys=True), flush=True)

    # The priority is the closed descending-band schedule.  A currently
    # nonunit coefficient is deferred, never inverted; after each valid pivot
    # the scan restarts at the highest-priority pending item.  This is needed
    # in split A_t fibers (already t=2), where a transient coefficient can be
    # a nonzero zero divisor before lower-chain substitutions are made.
    pending = []
    priority = 0
    for k in range(2*t, -1, -1):
        for tag, variable, family in scheduled_pivots_at_band(t, k):
            pending.append({"priority": priority, "band": k, "tag": tag,
                            "variable": variable, "family": family,
                            "defer_count": 0, "deferral_history": []})
            priority += 1
    while pending:
        chosen_position = None
        for position, item in enumerate(pending):
            try:
                _row_index, row = locate(item["band"], item["tag"])
            except AssertionError:
                continue
            if item["variable"] not in remaining:
                continue
            if affine_decomposition(row, item["variable"], algebra) is not None:
                chosen_position = position
                break
            item["defer_count"] += 1
            coefficient = algebra.reduce(sp.diff(row.expr, item["variable"]))
            record = {
                "attempt": item["defer_count"],
                "coefficient": str(coefficient),
                "coefficient_symbols": sorted(map(str, coefficient.free_symbols)),
                "reason": "not_affine_over_A_t",
            }
            if coefficient != 0 and coefficient.free_symbols <= {algebra.y}:
                u, multiplier = primitive_coefficient(coefficient, algebra.y)
                record.update({
                    "u_primitive_Q_associate": str(u),
                    "u_equals_multiplier_times_coefficient": str(multiplier),
                    "resultant_H_raw_u": str(algebra.resultant(u, raw=True)),
                    "resultant_H_primitive_u": str(
                        algebra.resultant(u, raw=False)),
                    "reason": "nonunit_or_zero_divisor_in_A_t",
                })
            if not item["deferral_history"] or (
                    item["deferral_history"][-1]["coefficient"] != str(coefficient)):
                item["deferral_history"].append(record)
        if chosen_position is None:
            diagnostics = []
            for item in pending:
                matches = [row for row in current
                           if row.h_power == item["band"] and row.monomial == item["tag"]]
                coefficient = None
                if len(matches) == 1:
                    coefficient = algebra.reduce(sp.diff(matches[0].expr,
                                                         item["variable"]))
                diagnostics.append({"band": item["band"], "tag": list(item["tag"]),
                                    "variable": str(item["variable"]),
                                    "coefficient": str(coefficient),
                                    "defer_count": item["defer_count"]})
            raise AssertionError({"t": t, "reason": "no scheduled unit pivot",
                                  "pending": diagnostics})
        item = pending.pop(chosen_position)
        family = item["family"]
        if item["defer_count"]:
            family += "_after_unit_deferral"
            print(json.dumps({"phase": "scheduled_unit_deferral_resolved", "t": t,
                              "band": item["band"], "tag": list(item["tag"]),
                              "variable": str(item["variable"]),
                              "defer_count": item["defer_count"],
                              "skipped_pending": chosen_position},
                             sort_keys=True), flush=True)
        apply(item["band"], item["tag"], item["variable"], family,
              item["deferral_history"])

    # The (0,2) rows are the uniform within-band zero/duplicate syzygies.
    # Zero instances have already been recorded by apply(); remove any literal
    # canonical duplicates that survive.
    for k in range(2*t-1, -1, -1):
        matches = [(i, row) for i, row in enumerate(current)
                   if row.h_power == k and row.monomial == (0, 2)]
        if matches:
            if len(matches) != 1:
                raise AssertionError("multiple scheduled (0,2) rows")
            row_index, row = matches[0]
            duplicates = [other for i, other in enumerate(current)
                          if i != row_index and other.expr == row.expr]
            if not duplicates:
                raise AssertionError({"t": t, "band": k,
                                      "tag": [0, 2],
                                      "reason": "scheduled syzygy row remains unique",
                                      "expression": str(row.expr)})
            representative = min(duplicates, key=normalization_row_key)
            dropped.append({"stage": "after_all_scheduled_pivots",
                            "source": row.source_index, "band": k,
                            "monomial": [0, 2],
                            "reason": "duplicate_mod_H_after_band",
                            "representative_source": representative.source_index,
                            "representative_monomial": list(representative.monomial)})
            del current[row_index]

    expected_remaining = [sp.Symbol("b3"), sp.Symbol("b4")] + [
        sp.Symbol(f"q{i}_0") for i in range(2, t)
    ]
    expected_remaining = sorted(expected_remaining, key=variable_key)
    if remaining != expected_remaining:
        raise AssertionError({"t": t,
                              "remaining": list(map(str, remaining)),
                              "expected": list(map(str, expected_remaining))})
    unexpected = [row for row in current
                  if not (0 <= row.h_power < 2*t and row.monomial == (0, 1))]
    if unexpected:
        raise AssertionError({"t": t, "unexpected_terminal_tags": [
            [r.source_index, r.h_power, list(r.monomial)] for r in unexpected]})
    return current, remaining, pivots, dropped, None


def eliminate_scheduled_lazy(rows: list[CRow], auxiliaries: list[sp.Symbol],
                             algebra: QuadraticAlgebra,
                             materialize_terminal: bool = True):
    """Same canonical schedule, with substitutions materialized row-by-row.

    A row is reduced only when it is inspected as a pivot or emitted at the
    end.  This avoids the quadratic eager pass over all untouched rows while
    giving exactly the chronological substitution map.
    """
    t = algebra.t
    remaining = sorted(auxiliaries, key=variable_key)
    active = [LazyRow(r.source_index, r.h_power, r.monomial, r.expr)
              for r in sorted(rows, key=normalization_row_key)]
    substitutions: list[tuple[sp.Symbol, sp.Expr]] = []
    pivots: list[dict] = []
    dropped: list[dict] = []

    def materialize(row: LazyRow) -> sp.Expr:
        while row.substitutions_applied < len(substitutions):
            variable, rhs = substitutions[row.substitutions_applied]
            if variable in row.expr.free_symbols:
                row.expr = algebra.reduce(row.expr.subs(variable, rhs))
            row.substitutions_applied += 1
        return row.expr

    def locate(k: int, tag: tuple[int, int]):
        matches = [row for row in active
                   if row.h_power == k and row.monomial == tag]
        if len(matches) != 1:
            raise AssertionError({"t": t, "band": k, "tag": list(tag),
                                  "matches": len(matches)})
        return matches[0]

    pending = []
    priority = 0
    for k in range(2*t, -1, -1):
        for tag, variable, family in scheduled_pivots_at_band(t, k):
            pending.append({"priority": priority, "band": k, "tag": tag,
                            "variable": variable, "family": family,
                            "defer_count": 0, "deferral_history": []})
            priority += 1

    while pending:
        chosen_position = None
        chosen_decomposition = None
        chosen_row = None
        for position, item in enumerate(pending):
            row = locate(item["band"], item["tag"])
            materialize(row)
            if item["variable"] not in remaining:
                continue
            decomposition = affine_decomposition(
                CRow(row.source_index, row.h_power, row.monomial, row.expr),
                item["variable"], algebra,
            )
            if decomposition is not None:
                chosen_position = position
                chosen_decomposition = decomposition
                chosen_row = row
                break
            item["defer_count"] += 1
            coefficient = algebra.reduce(sp.diff(row.expr, item["variable"]))
            record = {
                "attempt": item["defer_count"],
                "after_substitution_count": len(substitutions),
                "coefficient": str(coefficient),
                "coefficient_symbols": sorted(map(str, coefficient.free_symbols)),
                "reason": "not_affine_over_A_t",
            }
            if coefficient != 0 and coefficient.free_symbols <= {algebra.y}:
                u, multiplier = primitive_coefficient(coefficient, algebra.y)
                record.update({
                    "u_primitive_Q_associate": str(u),
                    "u_equals_multiplier_times_coefficient": str(multiplier),
                    "resultant_H_raw_u": str(algebra.resultant(u, raw=True)),
                    "resultant_H_primitive_u": str(
                        algebra.resultant(u, raw=False)),
                    "reason": "nonunit_or_zero_divisor_in_A_t",
                })
            if not item["deferral_history"] or (
                    item["deferral_history"][-1]["coefficient"] != str(coefficient)):
                item["deferral_history"].append(record)

        if chosen_position is None or chosen_decomposition is None or chosen_row is None:
            raise AssertionError({"t": t, "reason": "no scheduled lazy unit pivot",
                                  "pending": [{"band": x["band"],
                                               "tag": list(x["tag"]),
                                               "variable": str(x["variable"]),
                                               "deferrals": x["deferral_history"]}
                                              for x in pending]})
        item = pending.pop(chosen_position)
        variable = item["variable"]
        coefficient, remainder, inverse = chosen_decomposition
        rhs = algebra.reduce(-inverse*remainder)
        if algebra.reduce(chosen_row.expr.subs(variable, rhs)) != 0:
            raise AssertionError("lazy scheduled pivot substitution failed")
        u, u_multiplier = primitive_coefficient(coefficient, algebra.y)
        res_raw = algebra.resultant(u, raw=True)
        res_primitive = algebra.resultant(u, raw=False)
        if res_raw == 0 or res_primitive == 0:
            raise AssertionError("lazy scheduled pivot resultant vanishes")
        active.remove(chosen_row)
        remaining.remove(variable)
        substitutions.append((variable, rhs))
        family = item["family"]
        if item["defer_count"]:
            family += "_after_unit_deferral"
        pivots.append({
            "step": len(pivots)+1,
            "priority": item["priority"],
            "family": family,
            "source": chosen_row.source_index,
            "band": chosen_row.h_power,
            "monomial": list(chosen_row.monomial),
            "variable": str(variable),
            "coefficient": str(coefficient),
            "coefficient_inverse": str(inverse),
            "u_primitive_Q_associate": str(u),
            "u_equals_multiplier_times_coefficient": str(u_multiplier),
            "resultant_H_raw_u": str(res_raw),
            "resultant_H_primitive_u": str(res_primitive),
            "rhs": str(rhs),
            "inverse_checked": algebra.reduce(coefficient*inverse-1) == 0,
            "substitution_checked": True,
            "rows_after_before_lazy_zero_detection": len(active),
            "variables_after": len(remaining),
            "nonunit_deferral_history": item["deferral_history"],
        })
        print(json.dumps({"phase": "lazy_scheduled_pivot", "t": t,
                          "step": len(pivots), "priority": item["priority"],
                          "band": item["band"], "tag": list(item["tag"]),
                          "variable": str(variable),
                          "deferred": item["defer_count"],
                          "rows": len(active), "variables": len(remaining),
                          "rhs_bytes": len(str(rhs))}, sort_keys=True), flush=True)

    if not materialize_terminal:
        return [], remaining, pivots, dropped, {
            "status": "NOT_MATERIALIZED",
            "reason": "exact pivot-only bounded run",
            "latent_rows": len(active),
            "substitutions": len(substitutions),
        }

    for row in active:
        materialize(row)
    nonzero = [row for row in active if row.expr != 0]
    for row in active:
        if row.expr == 0:
            dropped.append({"stage": "lazy_final_materialization",
                            "source": row.source_index, "band": row.h_power,
                            "monomial": list(row.monomial), "reason": "zero_mod_H"})

    terminal = sorted(
        [row for row in nonzero
         if 0 <= row.h_power < 2*t and row.monomial == (0, 1)],
        key=lambda row: row.h_power,
    )
    companions = sorted(
        [row for row in nonzero
         if 0 <= row.h_power < 2*t and row.monomial == (0, 2)],
        key=lambda row: row.h_power,
    )
    extras = [row for row in nonzero if row not in terminal and row not in companions]
    if extras:
        raise AssertionError({"t": t, "unexpected_lazy_rows": [
            [r.source_index, r.h_power, list(r.monomial)] for r in extras]})
    for companion in companions:
        p = sp.Poly(companion.expr, *remaining,
                    domain=sp.QQ.frac_field(algebra.y))
        matched = None
        scalar = None
        for candidate in terminal:
            qpoly = sp.Poly(candidate.expr, *remaining,
                            domain=sp.QQ.frac_field(algebra.y))
            if p.is_zero or qpoly.is_zero or set(p.monoms()) != set(qpoly.monoms()):
                continue
            monomial = p.monoms()[0]
            left = algebra.reduce(p.coeff_monomial(monomial))
            right = algebra.reduce(qpoly.coeff_monomial(monomial))
            try:
                ratio = algebra.reduce(left*algebra.inverse(right))
            except Exception:
                continue
            if algebra.reduce(companion.expr-ratio*candidate.expr) == 0:
                matched, scalar = candidate, ratio
                break
        if matched is None:
            raise AssertionError({"t": t, "band": companion.h_power,
                                  "reason": "nonzero unmatched companion",
                                  "expr": str(companion.expr)})
        dropped.append({"stage": "lazy_final_materialization",
                        "source": companion.source_index,
                        "band": companion.h_power,
                        "monomial": list(companion.monomial),
                        "reason": "A_t_scalar_duplicate",
                        "representative_source": matched.source_index,
                        "representative_band": matched.h_power,
                        "scalar": str(scalar)})

    expected_remaining = sorted(
        [sp.Symbol("b3"), sp.Symbol("b4")]
        + [sp.Symbol(f"q{i}_0") for i in range(2, t)],
        key=variable_key,
    )
    if remaining != expected_remaining:
        raise AssertionError({"t": t, "remaining": list(map(str, remaining)),
                              "expected": list(map(str, expected_remaining))})
    if [row.h_power for row in terminal] != list(range(2*t)):
        raise AssertionError({"t": t, "terminal_bands": [r.h_power for r in terminal]})
    result = [CRow(r.source_index, r.h_power, r.monomial, r.expr)
              for r in terminal]
    return result, remaining, pivots, dropped, None


def row_record(row: CRow, variables: list[sp.Symbol], y: sp.Symbol) -> dict:
    polynomial = sp.Poly(row.expr, *variables, domain=sp.QQ.frac_field(y))
    return {
        "source": row.source_index,
        "band": row.h_power,
        "monomial": list(row.monomial),
        "degree_in_auxiliaries": polynomial.total_degree(),
        "terms_over_Qy": len(polynomial.terms()),
        "expression": str(row.expr),
    }


def write_tsv(path: pathlib.Path, header: list[str], records: list[dict]):
    def clean(value):
        if isinstance(value, (list, dict)):
            value = json.dumps(value, sort_keys=True, separators=(",", ":"))
        return str(value).replace("\t", " ").replace("\n", " ")
    lines = ["\t".join(header)]
    for record in records:
        lines.append("\t".join(clean(record.get(key, "")) for key in header))
    path.write_text("\n".join(lines)+"\n", encoding="utf-8")


def process_t(chart, tp, t: int, max_seconds: float, max_bytes: int,
              materialize_terminal: bool) -> dict:
    started = time.monotonic()
    data = chart.build(t=t, gauged=True)
    print(json.dumps({"phase": "chart_built", "t": t,
                      "rows": len(data["tagged"]),
                      "seconds": time.monotonic()-started}, sort_keys=True), flush=True)
    constant = tp.reduce_chart(data, max_pivots=1024,
                               max_seconds=max_seconds,
                               max_expression_bytes=max_bytes)
    print(json.dumps({"phase": "constant_reduced", "t": t,
                      "pivots": len(constant.pivots), "rows": len(constant.rows),
                      "seconds": time.monotonic()-started}, sort_keys=True), flush=True)
    post_rows, auxiliaries, algebra, normal = normalize_post_hc(tp, constant, t)
    print(json.dumps({"phase": "post_hc", "t": t,
                      "rows": len(post_rows), "variables": len(auxiliaries),
                      "seconds": time.monotonic()-started}, sort_keys=True), flush=True)
    post_records = [row_record(r, auxiliaries, algebra.y)
                    for r in sorted(post_rows, key=row_key)]
    final_rows, remaining, pivots, dropped, terminal_unit = eliminate_scheduled_lazy(
        post_rows, auxiliaries, algebra, materialize_terminal=materialize_terminal,
    )
    terminal_records = [row_record(r, remaining, algebra.y)
                        for r in sorted(final_rows,
                                        key=lambda z: (z.h_power, z.monomial,
                                                       z.source_index))]

    prefix = f"canonical_t{t}"
    post_path = OUT / f"{prefix}_post_hc_rows.tsv"
    pivots_path = OUT / f"{prefix}_pivots.tsv"
    terminal_path = OUT / f"{prefix}_terminal_rows.tsv"
    write_tsv(post_path,
              ["source", "band", "monomial", "degree_in_auxiliaries",
               "terms_over_Qy", "expression"], post_records)
    write_tsv(pivots_path,
              ["step", "family", "source", "band", "monomial", "variable", "coefficient",
               "coefficient_inverse", "u_primitive_Q_associate",
               "u_equals_multiplier_times_coefficient", "resultant_H_raw_u",
               "resultant_H_primitive_u", "nonunit_deferral_history", "rhs", "inverse_checked",
               "substitution_checked", "rows_after", "variables_after",
               "expression_bytes_after"], pivots)
    write_tsv(terminal_path,
              ["source", "band", "monomial", "degree_in_auxiliaries",
               "terms_over_Qy", "expression"], terminal_records)

    expected = {
        "full_rows": 14*t+9,
        "full_unknowns": 9*t+9,
        "constant_pivots": 3*t+4,
        "constant_rows": 11*t+4,
        "constant_unknowns_including_c": 6*t+5,
        "post_rows": 9*t+2,
        "post_auxiliaries": 6*t+2,
        "affine_pivots": 5*t+2,
        "terminal_rows": 2*t,
        "terminal_variables": t,
        "terminal_bands": list(range(2*t)),
        "terminal_degrees": list(range(4*t+1, 2*t+1, -1)),
    }
    measured = {
        "full_rows": len(data["tagged"]),
        "full_unknowns": len(data["params"])+1,
        "constant_pivots": len(constant.pivots),
        "constant_rows": len(constant.rows),
        "constant_unknowns_including_c": len(constant.remaining_variables)+1,
        "post_rows": len(post_rows),
        "post_auxiliaries": len(auxiliaries),
        "affine_pivots": len(pivots),
        "terminal_rows": len(final_rows),
        "terminal_variables": len(remaining),
        "terminal_bands": [r["band"] for r in terminal_records],
        "terminal_degrees": [r["degree_in_auxiliaries"] for r in terminal_records],
    }
    checks = {key: measured[key] == expected[key] for key in expected}
    if not materialize_terminal:
        for key in ("terminal_rows", "terminal_variables", "terminal_bands",
                    "terminal_degrees"):
            checks[key] = None
    audit = {
        "t": t,
        "typing": "EXACT fixed-t quotient-algebra extraction",
        "canonical_order": {
            "row": "descending band 2t,...,0 with explicit within-band tag schedule",
            "within_band": "at 2t: (0,1),(0,0); below: (1,2),(1,1 if present),(0,0); retain (0,1); reduce (0,2) syzygy",
            "nonunit_policy": "defer without inversion; restart at first pending unit in the same fixed priority order",
            "variable": "closed indexed schedule in scheduled_pivots_at_band",
            "row_normalization": "primitive integral Q-associate after reduction mod H_t",
            "terminal_output": "ascending band, then remainder tag and source index",
        },
        "normalization": normal,
        "expected_pattern": expected,
        "measured": measured,
        "pattern_checks": checks,
        "constant_pivot_variables": [str(p.variable) for p in constant.pivots],
        "constant_pivot_bands": [p.h_power for p in constant.pivots],
        "post_Hc_variables": [str(v) for v in auxiliaries],
        "post_Hc_vector_sha256": vector_digest(r.expr for r in post_rows),
        "pivots": pivots,
        "drop_count_during_affine": len(dropped),
        "drops_during_affine": dropped,
        "terminal_unit": terminal_unit,
        "terminal_materialized_exactly": materialize_terminal,
        "terminal_variables": [str(v) for v in remaining],
        "terminal": terminal_records,
        "terminal_vector_sha256": vector_digest(r.expr for r in final_rows),
        "all_pivot_inverse_checks": all(p["inverse_checked"] for p in pivots),
        "all_pivot_substitution_checks": all(p["substitution_checked"] for p in pivots),
        "all_pivot_resultants_nonzero": all(
            sp.sympify(p["resultant_H_raw_u"]) != 0 for p in pivots
        ),
        "elapsed_seconds": time.monotonic()-started,
        "artifacts": {},
    }
    for path in (post_path, pivots_path, terminal_path):
        audit["artifacts"][path.name] = {"sha256": digest(path),
                                                "bytes": path.stat().st_size}
    audit_path = OUT / f"{prefix}_audit.json"
    audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True)+"\n",
                          encoding="utf-8")
    audit["artifacts"][audit_path.name] = {"sha256": digest(audit_path),
                                            "bytes": audit_path.stat().st_size}
    return audit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, nargs="+", default=[2, 3, 4, 5, 6])
    parser.add_argument("--max-seconds", type=float, default=1800.0)
    parser.add_argument("--max-expression-bytes", type=int, default=500_000_000)
    parser.add_argument("--pivots-only", action="store_true")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    for name, expected in EXPECTED.items():
        actual = digest(INPUT/name)
        if actual != expected:
            raise RuntimeError(f"frozen source mismatch: {name}: {actual}")
    chart = load(CHART, "canonical_frozen_chart")
    tp = load(PREPROCESS, "canonical_frozen_preprocess")
    summary = {
        "typing": "EXACT fixed-t extractions; finite checks are not an all-t proof",
        "source_hashes": {name: digest(INPUT/name) for name in EXPECTED},
        "canonical_driver_sha256_at_start": digest(pathlib.Path(__file__)),
        "runs": {},
    }
    for t in args.t:
        audit = process_t(chart, tp, t, args.max_seconds,
                          args.max_expression_bytes,
                          materialize_terminal=not args.pivots_only)
        summary["runs"][str(t)] = {
            "measured": audit["measured"],
            "all_pattern_checks": all(value for value in audit["pattern_checks"].values()
                                          if value is not None),
            "terminal_variables": audit["terminal_variables"],
            "all_pivot_resultants_nonzero": audit["all_pivot_resultants_nonzero"],
            "elapsed_seconds": audit["elapsed_seconds"],
        }
        print(json.dumps({"t": t, **summary["runs"][str(t)]}, sort_keys=True),
              flush=True)
    summary_path = OUT / "canonical_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True)+"\n",
                            encoding="utf-8")
    print(json.dumps({"summary": str(summary_path),
                      "sha256": digest(summary_path)}, sort_keys=True))


if __name__ == "__main__":
    main()
