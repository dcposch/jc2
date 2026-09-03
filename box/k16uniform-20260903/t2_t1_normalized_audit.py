#!/usr/bin/env python3
"""Exact normalized-system audit for the frozen K16 t=2 driver and t=1 control.

All mathematical input is loaded from /tmp/jc2-lane.fjoTgL/inputs.  The script
uses the frozen constant-Q-pivot algorithm, derives rather than assumes a
weighted grading, finds the two-variable base relation and c row, takes the
weighted x=1 slice when justified, and then performs checked affine
elimination over the resulting number field.
"""

from __future__ import annotations

import dataclasses
import hashlib
import importlib.util
import json
import math
import pathlib
import sys
from functools import reduce

import sympy as sp


INPUTS = pathlib.Path("/tmp/jc2-lane.fjoTgL/inputs")
OUT = pathlib.Path("/home/ubuntu/jc2/box/k16uniform-20260903")


def load(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


tp = load(INPUTS / "triangular_preprocess.py", "triangular_preprocess")
generic = load(INPUTS / "t_order_system.py", "frozen_generic_order_system")
dedicated_t2 = load(INPUTS / "t2_order_system.py", "frozen_t2_order_system")
t3slice = load(INPUTS / "t3_normalized_slice.py", "frozen_t3_normalized_slice")


@dataclasses.dataclass
class SliceRow:
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    expr: sp.Expr


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primitive(expr: sp.Expr, variables: list[sp.Symbol]) -> tuple[sp.Expr, sp.Rational]:
    poly, multiplier, _denom, _content = tp.primitive_integer_polynomial(expr, variables)
    return poly.as_expr(), multiplier


def grading(rows, variables: list[sp.Symbol]):
    constraints = []
    per_row_terms = []
    for row in rows:
        terms = sp.Poly(row.expr, *variables, domain=sp.QQ).terms()
        monomials = [tuple(m) for m, _ in terms]
        per_row_terms.append(len(monomials))
        if len(monomials) > 1:
            base = monomials[0]
            constraints.extend([[m[i] - base[i] for i in range(len(variables))]
                                for m in monomials[1:]])
    matrix = sp.Matrix(constraints)
    nullspace = matrix.nullspace()
    result = {
        "constraint_count": len(constraints),
        "rank": matrix.rank(),
        "nullity": len(nullspace),
        "variable_count": len(variables),
    }
    if len(nullspace) != 1:
        result["basis"] = [[str(x) for x in vector] for vector in nullspace]
        return result, None
    vector = nullspace[0]
    lcm = sp.ilcm(*[int(sp.denom(x)) for x in vector])
    ints = [int(x*lcm) for x in vector]
    divisor = reduce(math.gcd, [abs(x) for x in ints if x])
    ints = [x // divisor for x in ints]
    if all(x < 0 for x in ints):
        ints = [-x for x in ints]
    weights = dict(zip(variables, ints))
    result["weights"] = {str(v): weights[v] for v in variables}
    result["positive"] = all(x > 0 for x in ints)
    row_degrees = []
    for row in rows:
        degrees = {
            sum(exponent * weights[variable]
                for exponent, variable in zip(monomial, variables))
            for monomial, _ in sp.Poly(row.expr, *variables, domain=sp.QQ).terms()
        }
        if len(degrees) != 1:
            raise AssertionError(f"nonhomogeneous row {row.source_index}: {degrees}")
        row_degrees.append({
            "source_index": row.source_index,
            "h_power": row.h_power,
            "monomial": list(row.monomial),
            "degree": degrees.pop(),
        })
    result["rows"] = row_degrees
    return result, weights


class NumberField:
    def __init__(self, y: sp.Symbol, H: sp.Expr, auxiliaries: list[sp.Symbol]):
        self.y = y
        self.H = sp.expand(H)
        self.auxiliaries = list(auxiliaries)
        self.domain = sp.QQ[tuple(auxiliaries)]
        self.hpoly = sp.Poly(self.H, y, domain=self.domain)

    def reduce(self, expr: sp.Expr) -> sp.Expr:
        return sp.expand(sp.Poly(sp.expand(expr), self.y,
                                 domain=self.domain).rem(self.hpoly).as_expr())

    def inverse(self, coefficient: sp.Expr) -> sp.Expr:
        coefficient = self.reduce(coefficient)
        if coefficient.free_symbols - {self.y}:
            raise AssertionError("coefficient is not in coefficient field")
        inv = sp.invert(sp.Poly(coefficient, self.y, domain=sp.QQ),
                        sp.Poly(self.H, self.y, domain=sp.QQ)).as_expr()
        inv = self.reduce(inv)
        if self.reduce(coefficient*inv - 1) != 0:
            raise AssertionError("inverse check failed")
        return inv


def deduplicate(rows: list[SliceRow], field: NumberField):
    kept = []
    dropped = []
    seen = {}
    for row in rows:
        expr = field.reduce(row.expr)
        if expr == 0:
            dropped.append({"source_index": row.source_index, "reason": "zero_mod_H"})
        elif expr in seen:
            dropped.append({"source_index": row.source_index, "reason": "duplicate_mod_H",
                            "representative": seen[expr].source_index})
        else:
            normalized = dataclasses.replace(row, expr=expr)
            seen[expr] = normalized
            kept.append(normalized)
    return kept, dropped


def affine_candidates(rows, remaining, field: NumberField):
    occurrences = {v: sum(v in row.expr.free_symbols for row in rows) for v in remaining}
    candidates = []
    for row_index, row in enumerate(rows):
        terms = sp.Add.make_args(row.expr)
        for variable_index, variable in enumerate(remaining):
            if variable not in row.expr.free_symbols:
                continue
            coefficient_terms, remainder_terms = [], []
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
            if coefficient == 0 or coefficient.free_symbols - {field.y}:
                continue
            if field.reduce(row.expr - coefficient*variable - remainder) != 0:
                raise AssertionError("affine decomposition failed")
            score = (len(str(remainder))*occurrences[variable], len(str(remainder)),
                     occurrences[variable], len(str(row.expr)), row.source_index,
                     variable_index)
            candidates.append((score, row_index, variable_index, coefficient, remainder))
    return candidates


def eliminate(rows, auxiliaries, field: NumberField):
    remaining = list(auxiliaries)
    rows, dropped = deduplicate(rows, field)
    pivots = []
    terminal_unit = None
    while True:
        constants = [row for row in rows if not (row.expr.free_symbols - {field.y})]
        if constants:
            row = min(constants, key=lambda r: (len(str(r.expr)), r.source_index))
            inv = field.inverse(row.expr)
            terminal_unit = {"source_index": row.source_index,
                             "constant": str(row.expr), "inverse": str(inv)}
            break
        candidates = affine_candidates(rows, remaining, field)
        if not candidates:
            break
        _score, row_index, variable_index, coefficient, remainder = min(candidates,
                                                                         key=lambda x: x[0])
        pivot_row = rows[row_index]
        variable = remaining[variable_index]
        inv = field.inverse(coefficient)
        rhs = field.reduce(-inv*remainder)
        if field.reduce(pivot_row.expr.subs(variable, rhs)) != 0:
            raise AssertionError("pivot substitution failed")
        del rows[row_index]
        del remaining[variable_index]
        next_rows = [dataclasses.replace(row, expr=field.reduce(row.expr.subs(variable, rhs)))
                     for row in rows]
        rows, new_dropped = deduplicate(next_rows, field)
        dropped.extend(new_dropped)
        pivots.append({
            "step": len(pivots)+1,
            "source_index": pivot_row.source_index,
            "h_power": pivot_row.h_power,
            "monomial": list(pivot_row.monomial),
            "variable": str(variable),
            "coefficient": str(coefficient),
            "inverse": str(inv),
            "rhs": str(rhs),
            "rows_after": len(rows),
            "variables_after": len(remaining),
        })
    return rows, remaining, pivots, dropped, terminal_unit


def eliminate_units(rows, auxiliaries, algebra: NumberField):
    """Affine elimination over Q[y]/(H), inverting only checked units.

    Unlike ``eliminate``, this also applies when H is squarefree reducible.
    Nonzero zero divisors are skipped rather than mistaken for field units.
    """
    remaining = list(auxiliaries)
    rows, dropped = deduplicate(rows, algebra)
    pivots = []
    terminal_unit = None
    while True:
        constants = sorted(
            [row for row in rows if not (row.expr.free_symbols - {algebra.y})],
            key=lambda r: (len(str(r.expr)), r.source_index),
        )
        for row in constants:
            try:
                inv = algebra.inverse(row.expr)
            except Exception:
                continue
            terminal_unit = {"source_index": row.source_index,
                             "constant": str(row.expr), "inverse": str(inv)}
            return rows, remaining, pivots, dropped, terminal_unit
        chosen = None
        for candidate in sorted(affine_candidates(rows, remaining, algebra),
                                key=lambda x: x[0]):
            try:
                inv = algebra.inverse(candidate[3])
            except Exception:
                continue
            chosen = (*candidate, inv)
            break
        if chosen is None:
            break
        (_score, row_index, variable_index, coefficient, remainder, inv) = chosen
        pivot_row = rows[row_index]
        variable = remaining[variable_index]
        rhs = algebra.reduce(-inv*remainder)
        if algebra.reduce(pivot_row.expr.subs(variable, rhs)) != 0:
            raise AssertionError("unit-pivot substitution failed")
        del rows[row_index]
        del remaining[variable_index]
        next_rows = [dataclasses.replace(row, expr=algebra.reduce(row.expr.subs(variable, rhs)))
                     for row in rows]
        rows, new_dropped = deduplicate(next_rows, algebra)
        dropped.extend(new_dropped)
        pivots.append({
            "step": len(pivots)+1,
            "source_index": pivot_row.source_index,
            "h_power": pivot_row.h_power,
            "monomial": list(pivot_row.monomial),
            "variable": str(variable),
            "coefficient": str(coefficient),
            "inverse": str(inv),
            "rhs": str(rhs),
            "rows_after": len(rows),
            "variables_after": len(remaining),
        })
    return rows, remaining, pivots, dropped, terminal_unit


def polynomial_degree_in(expr: sp.Expr, variables: list[sp.Symbol]):
    coefficients = sorted(expr.free_symbols - set(variables), key=str)
    domain = sp.QQ.frac_field(*coefficients) if coefficients else sp.QQ
    return sp.Poly(expr, *variables, domain=domain).total_degree()


def eliminate_record(field: NumberField, c_value: sp.Expr,
                     q_rows: list[SliceRow], auxiliaries: list[sp.Symbol],
                     unit_only: bool = False):
    c_inverse = field.inverse(c_value)
    k_input = []
    base_zero = []
    for row in q_rows:
        expr = field.reduce(row.expr)
        if expr == 0:
            base_zero.append(row.source_index)
        else:
            k_input.append(dataclasses.replace(row, expr=expr))
    elimination = eliminate_units if unit_only else eliminate
    final_rows, remaining, pivots, dropped, terminal_unit = elimination(
        k_input, auxiliaries, field)
    final = []
    for row in final_rows:
        final.append({
            "source_index": row.source_index,
            "h_power": row.h_power,
            "monomial": list(row.monomial),
            "degree_in_remaining": polynomial_degree_in(row.expr, remaining),
            "expr": str(row.expr),
        })
    return {
        "field": f"Q({field.y})/({field.H})",
        "c": str(c_value), "c_inverse_mod_relation": str(c_inverse),
        "base_zero_sources": base_zero,
        "K_input_rows": len(k_input),
        "K_input_auxiliary_unknowns": len(auxiliaries),
        "affine_pivot_count": len(pivots),
        "every_affine_coefficient_inverse_checked_mod_relation": True,
        "every_affine_substitution_checked_mod_relation": True,
        "pivots": pivots,
        "dropped": dropped,
        "remaining_unknowns": [str(v) for v in remaining],
        "remaining_rows": len(final_rows),
        "remaining_bands": [row.h_power for row in final_rows],
        "final_generators": final,
        "terminal_unit_before_Groebner": terminal_unit,
    }


def actual_pair_lines():
    return [
        "ring RAC=0,(gamma,pi),dp;",
        "poly FAC=pi;",
        "poly GAC=pi-(gamma^2)/2;",
        "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
        'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
        ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
    ]


def emit_rational_final(branch: dict) -> str:
    variables = [sp.Symbol(name) for name in branch["remaining_unknowns"]]
    locals_map = {str(v): v for v in variables}
    expressions = [sp.sympify(row["expr"], locals=locals_map)
                   for row in branch["final_generators"]]
    generators = [tp.singular_polynomial(expr, variables) for expr in expressions]
    lines = [
        "// exact normalized t=2 rational branch",
        "// x=q3_1=1, y=q5_1=%s, c=%s" % (branch["y_value"], branch["c"]),
        "// all preceding affine pivots have nonzero rational coefficients",
        *actual_pair_lines(),
        "ring R=0,(%s,u,T),dp;" % ",".join(map(str, variables)),
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); }'
        ' else { print("CONTROL_RING_FAIL"); }',
        "ideal CE=u,T*u-1;",
        "ideal GE=std(CE);",
        'if (typeof(GE)=="ideal" && nameof(basering)=="R")'
        ' { print("CONTROL_EMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); }'
        ' else { print("CONTROL_EMPTY_FAIL"); }',
        "ideal CN=u-1,T*u-1;",
        "ideal GN=std(CN);",
        'if (typeof(GN)=="ideal" && nameof(basering)=="R")'
        ' { print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); }'
        ' else { print("CONTROL_NONEMPTY_FAIL"); }',
        'print("MAIN_START t=2 y=%s rows=%d unknowns=%d");'
        % (branch["y_value"], len(generators), len(variables)),
        "ideal I=%s;" % ",\n".join(generators),
        "ideal G=std(I);",
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (reduce(1,G)==0) { print("MAIN_BRANCH_EMPTY"); G; }'
        ' else { print("MAIN_BRANCH_NONTRIVIAL"); G; }',
        "quit;",
    ]
    return "\n".join(lines) + "\n"


def emit_t1_unit(audit: dict) -> str:
    normal = audit["normalization"]
    field = audit["field_slice"]
    y = normal["y"]
    terminal = field["terminal_unit_before_Groebner"]
    if terminal is None:
        raise AssertionError("t=1 terminal unit missing")
    variables = field["remaining_unknowns"]
    lines = [
        "// exact normalized t=1 certificate after checked affine eliminations",
        *actual_pair_lines(),
        "ring RC=(0,%s),(u,T),dp;" % y,
        "minpoly=%s;" % normal["H"].replace("**", "^"),
        "number cbar=%s;" % normal["c_slice"].replace("**", "^"),
        "number cbar_inverse=1/cbar;",
        'if (cbar*cbar_inverse==1) { print("CONTROL_C_UNIT_PASS"); }'
        ' else { print("CONTROL_C_UNIT_FAIL"); }',
        "number terminal=%s;" % terminal["constant"].replace("**", "^"),
        "number terminal_inverse=%s;" % terminal["inverse"].replace("**", "^"),
        'if (terminal*terminal_inverse==1) { print("CONTROL_TERMINAL_UNIT_PASS"); }'
        ' else { print("CONTROL_TERMINAL_UNIT_FAIL"); }',
        "ideal CE=u,T*u-1;",
        "ideal GE=std(CE);",
        'if (typeof(GE)=="ideal" && nameof(basering)=="RC")'
        ' { print("CONTROL_EMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); }'
        ' else { print("CONTROL_EMPTY_FAIL"); }',
        "ideal CN=u-1,T*u-1;",
        "ideal GN=std(CN);",
        'if (typeof(GN)=="ideal" && nameof(basering)=="RC")'
        ' { print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); }'
        ' else { print("CONTROL_NONEMPTY_FAIL"); }',
        "ring RK=(0,%s),(%s,u,T),dp;" % (y, ",".join(variables)),
        "minpoly=%s;" % normal["H"].replace("**", "^"),
        "option(redSB);",
        'if (nameof(basering)=="RK") { print("CONTROL_RING_PASS RK"); }'
        ' else { print("CONTROL_RING_FAIL"); }',
        "ideal CE=u,T*u-1;",
        "ideal GE=std(CE);",
        'if (typeof(GE)=="ideal" && nameof(basering)=="RK")'
        ' { print("CONTROL_MAIN_RING_EMPTY_EXTRACT_PASS"); }'
        ' else { print("CONTROL_MAIN_RING_EMPTY_EXTRACT_FAIL"); }',
        'if (reduce(1,GE)==0) { print("CONTROL_MAIN_RING_EMPTY_PASS"); }'
        ' else { print("CONTROL_MAIN_RING_EMPTY_FAIL"); }',
        "ideal CN=u-1,T*u-1;",
        "ideal GN=std(CN);",
        'if (typeof(GN)=="ideal" && nameof(basering)=="RK")'
        ' { print("CONTROL_MAIN_RING_NONEMPTY_EXTRACT_PASS"); }'
        ' else { print("CONTROL_MAIN_RING_NONEMPTY_EXTRACT_FAIL"); }',
        'if (reduce(1,GN)!=0) { print("CONTROL_MAIN_RING_NONEMPTY_PASS"); }'
        ' else { print("CONTROL_MAIN_RING_NONEMPTY_FAIL"); }',
        'print("MAIN_START t=1 terminal_coefficient_field_unit");',
        "ideal I=1;",
        "ideal G=std(I);",
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (reduce(1,G)==0) { print("MAIN_T1_EMPTY"); G; }'
        ' else { print("MAIN_T1_NONTRIVIAL"); G; }',
        "quit;",
    ]
    return "\n".join(lines) + "\n"


def audit_t(t: int):
    data = generic.build(t=t, gauged=True)
    comparison = None
    if t == 2:
        comparison = tp.assert_same_chart(data, dedicated_t2.build(gauged=True),
                                          "frozen generic t=2 vs dedicated t=2")
    reduction = tp.reduce_chart(data, 256, 600.0, 10_000_000)
    variables = reduction.remaining_variables + [reduction.c]
    grade, weights = grading(reduction.rows, variables)
    by_name = {str(v): v for v in variables}
    x_name, y_name = f"q{t+1}_1", f"q{2*t+1}_1"
    if x_name not in by_name or y_name not in by_name:
        return {"t": t, "comparison": comparison,
                "triangular": tp.audit_record(reduction), "grading": grade,
                "normalization": {"status": "OPEN", "reason": "expected x/y absent"}}
    x, y, c = by_name[x_name], by_name[y_name], reduction.c
    small_rows = [{
        "source_index": row.source_index,
        "h_power": row.h_power,
        "monomial": list(row.monomial),
        "expr": str(sp.factor(row.expr)),
    } for row in reduction.rows if row.expr.free_symbols <= {x, y, c}]
    c_rows = [row for row in reduction.rows if c in row.expr.free_symbols]
    base_rows = [row for row in reduction.rows
                 if row.expr.free_symbols <= {x, y} and row.expr != 0]
    if len(c_rows) != 1 or not base_rows:
        return {"t": t, "comparison": comparison,
                "triangular": tp.audit_record(reduction), "grading": grade,
                "small_rows": small_rows,
                "normalization": {"status": "OPEN", "reason": "c/base row count"}}
    c_row = c_rows[0]
    c_coefficient = sp.diff(c_row.expr, c)
    if not c_coefficient.is_Rational or c_coefficient == 0:
        raise AssertionError("c coefficient is not rational constant")
    c_image = sp.factor(-(c_row.expr-c_coefficient*c)/c_coefficient)

    # Choose the primitive base relation of least text length.  Verify every
    # additional x,y row lies in its principal ideal before discarding it.
    base_candidates = []
    for row in base_rows:
        p, multiplier = primitive(row.expr, [x, y])
        base_candidates.append((len(str(p)), row, p, multiplier))
    _length, base_row, Hhom, Hmult = min(base_candidates, key=lambda item: item[0])
    for _length, row, candidate, _mult in base_candidates:
        quotient, rem = sp.div(candidate, Hhom, x, y)
        if rem != 0:
            raise AssertionError(f"independent x,y row {row.source_index}: {candidate}")

    H = sp.expand(Hhom.subs(x, 1))
    Hpoly = sp.Poly(H, y, domain=sp.QQ)
    discriminant = sp.discriminant(Hpoly)
    irreducible = bool(Hpoly.is_irreducible)
    x_divides_c = sp.rem(sp.Poly(sp.together(c_image), x, y), sp.Poly(x, x, y)) == 0
    normalization = {
        "status": "READY" if (weights and grade.get("positive") and x_divides_c) else "OPEN",
        "x": str(x), "y": str(y),
        "x_weight": weights[x] if weights else None,
        "y_weight": weights[y] if weights else None,
        "c_weight": weights[c] if weights else None,
        "c_row": {"source_index": c_row.source_index, "h_power": c_row.h_power,
                  "monomial": list(c_row.monomial), "coefficient": str(c_coefficient),
                  "solved": str(c_image)},
        "base_row": {"source_index": base_row.source_index, "h_power": base_row.h_power,
                     "monomial": list(base_row.monomial), "Hhom": str(Hhom),
                     "associate_multiplier": str(Hmult)},
        "H": str(H), "H_degree": Hpoly.degree(), "H_discriminant": str(discriminant),
        "H_irreducible_Q": irreducible,
        "c_slice": str(sp.factor(c_image.subs(x, 1))),
        "c_image_divisible_by_x": bool(x_divides_c),
    }
    result = {"t": t, "comparison": comparison,
              "triangular": tp.audit_record(reduction), "grading": grade,
              "small_rows": small_rows, "normalization": normalization}
    if normalization["status"] != "READY":
        return result
    c_slice = sp.factor(c_image.subs(x, 1))
    auxiliaries = [v for v in reduction.remaining_variables if v not in (x, y)]
    q_variables = auxiliaries + [y]
    sliced = []
    for row in reduction.rows:
        if row is c_row:
            continue
        expr = sp.expand(row.expr.subs({x: 1, c: c_slice}, simultaneous=True))
        sliced.append(SliceRow(row.source_index, row.h_power, row.monomial, expr))
    # Canonical Q* associates and literal duplicate removal.
    q_rows, q_map, seen = [], [], {}
    for row in sliced:
        expr, multiplier = primitive(row.expr, q_variables)
        key = str(expr)
        if key in seen:
            q_map.append({"source_index": row.source_index, "status": "duplicate_Q",
                          "representative": seen[key].source_index,
                          "multiplier": str(multiplier)})
        else:
            normalized_row = dataclasses.replace(row, expr=expr)
            seen[key] = normalized_row
            q_rows.append(normalized_row)
            q_map.append({"source_index": row.source_index, "status": "kept",
                          "multiplier": str(multiplier)})
    common = {
        "raw_rows_after_c": len(sliced),
        "Q_rows_after_duplicates": len(q_rows),
        "Q_row_map": q_map,
    }
    if not irreducible:
        normalization["status"] = "SPECIAL_REDUCIBLE_BASE"
        normalization["H_factorization"] = str(sp.factor(H))
        roots = sp.roots(Hpoly)
        if sum(roots.values()) != Hpoly.degree() or not all(root.is_Rational for root in roots):
            result["split_slices"] = {"status": "OPEN", "reason": "non-rational roots"}
            return result
        etale = NumberField(y, H, auxiliaries)
        etale_record = eliminate_record(etale, c_slice, q_rows, auxiliaries,
                                        unit_only=True)
        etale_record["typing"] = "squarefree etale Q-algebra; only checked units inverted"
        branches = []
        for root in sorted(roots, key=sp.default_sort_key):
            relation = y-root
            field = NumberField(y, relation, auxiliaries)
            c_root = sp.factor(c_slice.subs(y, root))
            branch = eliminate_record(field, c_root, q_rows, auxiliaries)
            branch["y_value"] = str(root)
            branch["multiplicity"] = roots[root]
            branches.append(branch)
        result["split_slices"] = {**common, "etale_slice": etale_record,
                                   "branches": branches}
        return result

    field = NumberField(y, H, auxiliaries)
    if field.reduce(H) != 0:
        raise AssertionError("minimal polynomial failed")
    result["field_slice"] = {**common, **eliminate_record(field, c_slice, q_rows,
                                                           auxiliaries)}
    return result


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    audits = {str(t): audit_t(t) for t in (1, 2)}
    record = {
        "input_hashes": {name: sha256(INPUTS/name) for name in [
            "t_order_system.py", "t2_order_system.py", "triangular_preprocess.py",
            "t3_normalized_slice.py", "k16_symbolic.py", "FALLACY-v2.md"]},
        "audits": audits,
    }
    path = OUT / "t2_t1_normalized_audit.json"
    path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for branch in audits["2"]["split_slices"]["branches"]:
        suffix = str(branch["y_value"]).replace("/", "_")
        (OUT / f"t2_normalized_y_{suffix}.sing").write_text(
            emit_rational_final(branch), encoding="utf-8")
    (OUT / "t1_normalized_unit.sing").write_text(emit_t1_unit(audits["1"]),
                                                  encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
