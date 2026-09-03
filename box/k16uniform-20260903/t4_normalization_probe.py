#!/usr/bin/env python3
"""Exact t=4 normalization probe from the frozen charged drivers.

This is an audit/probing driver, not a theorem promoter.  It reconstructs the
correctly gauged t=4 order chart, applies only the charged Q-constant triangular
pivots, extracts the one-dimensional positive grading, normalizes q5_1=1 on
c != 0, and passes to Q(v)/(486*v**2-270*v+35), v=q9_1.

All mathematical source files are read from the frozen lane-input directory.
Artifacts are confined to box/k16uniform-20260903 and use the t4_ prefix.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import importlib.util
import json
import pathlib
import sys
import time

import sympy as sp


INPUT = pathlib.Path("/tmp/jc2-lane.fjoTgL/inputs")
OUT = pathlib.Path("/home/ubuntu/jc2/box/k16uniform-20260903")
EXPECTED = {
    "t4_order_system.py": "db5e54450444f27c56f00bbec287aea284c8dc190e0e549c2fea51e0dbdd6cee",
    "triangular_preprocess.py": "f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93",
}


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@dataclasses.dataclass
class NRow:
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    expr: sp.Expr


class QuadraticField:
    def __init__(self, v: sp.Symbol, auxiliary: list[sp.Symbol]):
        self.v = v
        self.auxiliary = list(auxiliary)
        self.H = 486*v**2 - 270*v + 35
        self.domain = sp.QQ[tuple(self.auxiliary)]
        self.hpoly = sp.Poly(self.H, v, domain=self.domain)

    def reduce(self, expr: sp.Expr) -> sp.Expr:
        poly = sp.Poly(sp.expand(expr), self.v, domain=self.domain)
        return sp.expand(poly.rem(self.hpoly).as_expr())

    def inverse(self, coefficient: sp.Expr) -> sp.Expr:
        coefficient = self.reduce(coefficient)
        if coefficient.free_symbols - {self.v}:
            raise AssertionError("coefficient contains chart variables")
        if coefficient == 0:
            raise ZeroDivisionError
        inverse = sp.invert(
            sp.Poly(coefficient, self.v, domain=sp.QQ),
            sp.Poly(self.H, self.v, domain=sp.QQ),
        ).as_expr()
        inverse = self.reduce(inverse)
        if self.reduce(coefficient*inverse - 1) != 0:
            raise AssertionError("bad inverse")
        return inverse


def grading(rows, variables):
    differences = set()
    for row in rows:
        terms = sp.Poly(row.expr, *variables, domain=sp.QQ).terms()
        if not terms:
            continue
        anchor = terms[0][0]
        for monomial, _coefficient in terms[1:]:
            diff = tuple(a-b for a, b in zip(anchor, monomial))
            if any(diff):
                # Sign-normalize for a stable distinct-constraint count.
                first = next(x for x in diff if x)
                if first < 0:
                    diff = tuple(-x for x in diff)
                differences.add(diff)
    M = sp.Matrix(sorted(differences))
    ns = M.nullspace()
    if len(ns) != 1:
        raise AssertionError("grading nullity is not one")
    vector = ns[0]
    by_name = {str(v): i for i, v in enumerate(variables)}
    vector /= vector[by_name["b1"]]
    weights = {str(v): int(vector[i]) for i, v in enumerate(variables)}
    if any(sp.Rational(vector[i]).q != 1 for i in range(len(variables))):
        raise AssertionError("nonintegral primitive normalization")
    if min(weights.values()) <= 0:
        raise AssertionError("grading not positive")
    degrees = []
    for row in rows:
        ds = {
            sum(e*weights[str(v)] for e, v in zip(m, variables))
            for m, _coefficient in sp.Poly(row.expr, *variables, domain=sp.QQ).terms()
        }
        if len(ds) != 1:
            raise AssertionError((row.source_index, ds))
        degrees.append(next(iter(ds)))
    return differences, M.rank(), weights, degrees


def rational_associate(left, right, variables):
    L = sp.Poly(left, *variables, domain=sp.QQ)
    R = sp.Poly(right, *variables, domain=sp.QQ)
    if L.is_zero or R.is_zero:
        return None
    ratio = sp.Rational(L.LC(), R.LC())
    return ratio if (L-ratio*R).is_zero else None


def normalize(tp, reduction):
    variables = reduction.remaining_variables + [reduction.c]
    differences, rank, weights, row_degrees = grading(reduction.rows, variables)
    by_name = {str(v): v for v in variables}
    x, v, c = by_name["q5_1"], by_name["q9_1"], reduction.c
    Hhom = 35*x**4 - 270*x**2*v + 486*v**2
    cimage = x*v*(130*x**2 - 1404*v)/sp.Integer(2187)

    crows = [r for r in reduction.rows if c in r.expr.free_symbols]
    if len(crows) != 1:
        raise AssertionError("not one c row")
    crow = crows[0]
    cc = sp.diff(crow.expr, c)
    solved = sp.expand(-(crow.expr-cc*c)/cc)
    if sp.expand(solved-cimage) != 0:
        raise AssertionError((solved, cimage))

    hmatches = []
    for r in reduction.rows:
        if r is crow:
            continue
        if r.expr.free_symbols <= {x, v}:
            a = rational_associate(r.expr, Hhom, variables)
            if a is not None:
                hmatches.append((r, a))
    if len(hmatches) != 1:
        raise AssertionError("not one base row")
    hrow, hassociate = hmatches[0]

    auxiliary = [z for z in reduction.remaining_variables if z not in (x, v)]
    K = QuadraticField(v, auxiliary)
    if K.reduce(Hhom.subs(x, 1)) != 0:
        raise AssertionError("H does not reduce to zero")
    cbar = sp.expand(cimage.subs(x, 1))
    cinv = K.inverse(cbar)
    vinv = K.inverse(v)
    lin = 130-1404*v
    linv = K.inverse(lin)

    raw = []
    for r in reduction.rows:
        if r is crow:
            continue
        expr = sp.expand(r.expr.subs({x: 1, c: cbar}, simultaneous=True))
        raw.append(NRow(r.source_index, r.h_power, r.monomial, expr))

    # First replace every Q-row by its canonical primitive integral associate;
    # this is the charged t=3 normalization convention and exposes rational
    # associates before passage to K.  Then reduce modulo H and drop exact
    # zero/literal duplicate rows.  Equality in K uses the canonical degree-<2
    # representative.
    qvariables = auxiliary + [v]
    qcanonical = []
    qseen = {}
    qdropped = []
    for r in raw:
        primitive, multiplier, _denominator, _content = (
            tp.primitive_integer_polynomial(r.expr, qvariables)
        )
        expr = primitive.as_expr()
        if expr in qseen:
            qdropped.append({"source_index": r.source_index,
                             "reason": "rational_associate_duplicate_over_Q",
                             "representative_source_index": qseen[expr],
                             "integer_row_multiplier": str(multiplier)})
        else:
            qseen[expr] = r.source_index
            qcanonical.append(dataclasses.replace(r, expr=expr))

    rows = []
    representatives = {}
    dropped = []
    for r in qcanonical:
        expr = K.reduce(r.expr)
        if expr == 0:
            dropped.append({"source_index": r.source_index, "reason": "zero_mod_H"})
        elif expr in representatives:
            dropped.append({"source_index": r.source_index,
                            "reason": "literal_duplicate_mod_H",
                            "representative_source_index": representatives[expr]})
        else:
            representatives[expr] = r.source_index
            rows.append(dataclasses.replace(r, expr=expr))

    audit = {
        "typing": "EXACT-SYMBOLIC-NORMALIZATION; no Groebner result claimed",
        "source_hashes": EXPECTED,
        "triangular": tp.audit_record(reduction),
        "grading": {
            "distinct_monomial_difference_constraints": len(differences),
            "constraint_matrix_rank": rank,
            "variables": len(variables),
            "nullity": len(variables)-rank,
            "weights": weights,
            "row_weighted_degrees": row_degrees,
        },
        "scaling": {
            "x": str(x), "x_weight": weights[str(x)],
            "v": str(v), "v_weight": weights[str(v)],
            "c_weight": weights["c"],
            "c_nonzero_forces_x_nonzero": True,
            "slice": "q5_1=1",
        },
        "base": {
            "source_index": hrow.source_index,
            "h_power": hrow.h_power,
            "monomial": list(hrow.monomial),
            "homogeneous": str(Hhom),
            "associate_multiplier": str(hassociate),
            "H4": str(K.H),
            "degree": 2,
            "discriminant": int(sp.discriminant(K.H, v)),
            "factorization_discriminant": str(sp.factorint(int(sp.discriminant(K.H, v)))),
            "irreducible_over_Q": bool(sp.Poly(K.H, v, domain=sp.QQ).is_irreducible),
        },
        "c_row": {
            "source_index": crow.source_index,
            "h_power": crow.h_power,
            "monomial": list(crow.monomial),
            "coefficient": str(cc),
            "homogeneous_image": str(cimage),
            "slice_image": str(cbar),
        },
        "unit_checks": {
            "v_inverse": str(vinv),
            "130_minus_1404v_inverse": str(linv),
            "cbar_inverse": str(cinv),
            "all_identities_verified_mod_H": True,
        },
        "normalized": {
            "raw_rows_excluding_c_row": len(raw),
            "rows_after_primitive_Q_associate_deduplication": len(qcanonical),
            "Q_associate_duplicates": qdropped,
            "rows_over_K_after_zero_duplicate_removal": len(rows),
            "auxiliary_unknowns": len(auxiliary),
            "unknowns_with_v_as_coefficient_parameter": len(auxiliary)+1,
            "dropped": dropped,
            "remaining_variables": [str(z) for z in auxiliary],
            "rows": [{
                "source_index": r.source_index,
                "h_power": r.h_power,
                "monomial": list(r.monomial),
                "total_degree_in_auxiliary": sp.Poly(r.expr, *auxiliary,
                    domain=sp.QQ.frac_field(v)).total_degree(),
                "text_bytes": len(str(r.expr)),
            } for r in rows],
        },
    }
    return audit, rows, auxiliary, K


def write_rows(path, rows):
    with path.open("w", encoding="utf-8") as f:
        f.write("source_index\th_power\tgamma_power\tpi_power\texpression\n")
        for r in rows:
            f.write(f"{r.source_index}\t{r.h_power}\t{r.monomial[0]}\t"
                    f"{r.monomial[1]}\t{r.expr}\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-row-text", action="store_true")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    for name, expected in EXPECTED.items():
        actual = sha256(INPUT/name)
        if actual != expected:
            raise RuntimeError(f"hash mismatch {name}: {actual}")
    tp = load(INPUT/"triangular_preprocess.py", "t4_frozen_triangular")
    drv = load(INPUT/"t4_order_system.py", "t4_frozen_driver")
    data = drv.build(gauged=True)
    reduction = tp.reduce_chart(data, 256, 600.0, 5_000_000)
    audit, rows, auxiliary, K = normalize(tp, reduction)
    audit["elapsed_seconds"] = None
    path = OUT/"t4_normalization_audit.json"
    path.write_text(json.dumps(audit, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    if not args.no_row_text:
        write_rows(OUT/"t4_normalized_rows.tsv", rows)
    print(json.dumps({
        "audit": str(path),
        "audit_sha256": sha256(path),
        "rows": len(rows),
        "auxiliary": len(auxiliary),
        "H": str(K.H),
        "cbar": audit["c_row"]["slice_image"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
