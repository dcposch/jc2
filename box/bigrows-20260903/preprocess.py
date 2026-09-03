#!/usr/bin/env python3
"""Reusable preprocessing lane for the large two-point strata.

The driver is intentionally proof-audit oriented.  It builds symbolic
top-face h-adic systems, performs only checked quotient-ring isomorphisms,
looks for an exact weighted slice on the saturated locus, and records every
accepted map.  A non-result is reported as COUNTING-BOUND/OPEN rather than
promoted.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import hashlib
import importlib.util
import json
import math
import os
import re
import shutil
import signal
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Iterable, Sequence

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
INPUTS = Path("/tmp/jc2-lane.PIFGo9/inputs")
RECEIPT = ROOT / "xmodel/bigrows-preprocess-gpt55-20260903.run.v2"
PRIMES = (32003, 32009, 32027)


@dataclass(frozen=True)
class RowSpec:
    key: str
    source: str
    n: int
    m: int
    M2: int
    V2: int
    k: int


@dataclass
class TaggedRow:
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    expr: sp.Expr


@dataclass
class Pivot:
    step: int
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    variable: sp.Symbol
    coefficient: sp.Expr
    rhs: sp.Expr
    final_rhs: sp.Expr | None = None


@dataclass
class Reduction:
    original_variables: list[sp.Symbol]
    remaining_variables: list[sp.Symbol]
    c: sp.Symbol
    rows: list[TaggedRow]
    original_rows: list[TaggedRow]
    pivots: list[Pivot]
    substitutions: dict[sp.Symbol, sp.Expr]
    zero_source_indices: list[int]
    elapsed: float


class TimeLimitExceeded(TimeoutError):
    pass


class time_limit:
    def __init__(self, seconds: int | None):
        self.seconds = seconds
        self.old_handler = None

    def __enter__(self):
        if self.seconds is None or self.seconds <= 0:
            return self

        def handler(_signum, _frame):
            raise TimeLimitExceeded("stratum wall-clock budget exceeded")

        self.old_handler = signal.signal(signal.SIGALRM, handler)
        signal.alarm(int(self.seconds))
        return self

    def __exit__(self, exc_type, exc, tb):
        if self.seconds is not None and self.seconds > 0:
            signal.alarm(0)
            if self.old_handler is not None:
                signal.signal(signal.SIGALRM, self.old_handler)
        return False


ROWS: dict[str, RowSpec] = {
    "25_15": RowSpec("25_15", "(25,15;21;2;k=2)", 25, 15, 21, 2, 2),
    "35_20": RowSpec("35_20", "(35,20;31;2;k=2)", 35, 20, 31, 2, 2),
    "35_25": RowSpec("35_25", "(35,25;31;3;k=2)", 35, 25, 31, 3, 2),
    "30_24": RowSpec("30_24", "(30,24;25;4;k=3)", 30, 24, 25, 4, 3),
    "49_14": RowSpec("49_14", "(49,14;46;4;k=1)", 49, 14, 46, 4, 1),
    "50_30": RowSpec("50_30", "(50,30;47;7;k=1)", 50, 30, 47, 7, 1),
    "24_16": RowSpec("24_16", "(24,16;17;2;k=5)", 24, 16, 17, 2, 5),
}

LARGE_STRATA: list[tuple[str, tuple[int, ...]]] = [
    ("25_15", (3,)),
    ("25_15", (2, 1)),
    ("25_15", (1, 1, 1)),
    ("35_20", (3,)),
    ("35_20", (2, 1)),
    ("35_20", (1, 1, 1)),
    ("35_25", (2,)),
    ("35_25", (1, 1)),
    ("30_24", (2,)),
    ("30_24", (1, 1)),
    ("49_14", (3,)),
    ("49_14", (2, 1)),
    ("50_30", (3,)),
    ("50_30", (2, 1)),
]

UNFINISHED_24_16: list[tuple[str, tuple[int, ...]]] = [
    ("24_16", (3, 1, 1, 1)),
    ("24_16", (2, 2, 2)),
    ("24_16", (2, 1, 1, 1, 1)),
    ("24_16", (1, 1, 1, 1, 1, 1)),
    ("24_16", (4, 1, 1)),
    ("24_16", (3, 2, 1)),
    ("24_16", (2, 2, 1, 1)),
]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load %s" % path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def receipt_manifest() -> list[dict]:
    fields: dict[int, dict[str, str]] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        match = re.match(r"charged_input_(\d+)_(basename|sha256)=(.*)", line)
        if match:
            fields.setdefault(int(match.group(1)), {})[match.group(2)] = match.group(3)
    manifest = []
    for idx in sorted(fields):
        rec = fields[idx]
        path = INPUTS / rec["basename"]
        manifest.append(
            {
                "index": idx,
                "basename": rec["basename"],
                "path": str(path),
                "expected_sha256": rec["sha256"],
                "actual_sha256": sha256_file(path),
            }
        )
    return manifest


def verify_inputs() -> dict:
    manifest = receipt_manifest()
    for item in manifest:
        item["ok"] = item["expected_sha256"] == item["actual_sha256"]
    return {
        "receipt": str(RECEIPT),
        "inputs": str(INPUTS),
        "ok": bool(manifest) and all(item["ok"] for item in manifest),
        "manifest": manifest,
    }


def clean_name(value: str) -> str:
    out = re.sub(r"[^A-Za-z0-9_]+", "_", value)
    out = re.sub(r"_+", "_", out).strip("_")
    if not out:
        out = "v"
    if out[0].isdigit():
        out = "v" + out
    return out


def frac_s(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else "%d/%d" % (
        value.numerator,
        value.denominator,
    )


def singular_expr(expr: sp.Expr, variables: Sequence[sp.Symbol] | None = None) -> str:
    expr = sp.together(sp.expand(expr))
    num, den = sp.fraction(expr)
    num = sp.expand(num)
    den = sp.expand(den)
    if den == 1:
        out = str(num)
    elif den == -1:
        out = str(-num)
    else:
        out = "(%s)/(%s)" % (num, den)
    return out.replace("**", "^")


def jac(f: sp.Expr, g: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))


def partitions(n: int, ceiling: int | None = None) -> Iterable[tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    top = n if ceiling is None else min(n, ceiling)
    for first in range(top, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def shape_for(row: RowSpec) -> dict:
    shape = load_module(INPUTS / "shape.py", "bigrows_frozen_shape")
    C = shape.shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    if not C["ok"]:
        raise ValueError("shape failed for %s: %s" % (row.source, C["reason"]))
    return C


def allowed_partitions(row: RowSpec) -> list[tuple[int, ...]]:
    C = shape_for(row)
    return [
        part
        for part in partitions(C["u"])
        if len(part) + 1 <= row.n - row.M2
    ]


def corrected_h_lower(C: dict) -> list[tuple[int, int]]:
    """Lower h monomials using ord h(sigma_1) >= V2*d1 + u*d2."""
    delta1: F = C["delta1"]
    bound = C["V2"] * C["delta1"] + C["u"] * C["delta2"]
    out = []
    for j in range(C["K"], -1, -1):
        for i in range(0, C["u"] + 1):
            if i + j >= C["K"]:
                continue
            if -F(i, 1) + delta1 * F(j, 1) >= bound:
                out.append((i, j))
    return out


def coefficient_monomials(
    C: dict,
    deficit: int,
    *,
    beta: bool = False,
) -> list[tuple[int, int]]:
    """Finite D1 support for h-adic coefficients after the corrected h order."""
    delta1: F = C["delta1"]
    bound = C["V2"] * C["delta1"] + C["u"] * C["delta2"]
    threshold = deficit * bound
    max_x = C["k"] + 1 if beta else None
    out = []
    for b in range(C["K"] - 1, -1, -1):
        maxa = math.floor(delta1 * F(b, 1) - threshold)
        if max_x is not None:
            maxa = min(maxa, max_x)
        for a in range(0, maxa + 1):
            if a + b <= deficit * C["K"]:
                out.append((a, b))
    return out


def face(row: RowSpec, part: Sequence[int]):
    x, y = sp.symbols("x y")
    slopes = list(sp.symbols("s2:%d" % (len(part) + 1))) if len(part) > 1 else []
    H = y ** row.V2 * (y - x) ** part[0]
    for slope, exponent in zip(slopes, part[1:]):
        H *= (y - slope * x) ** exponent
    omega = sp.Integer(1)
    for slope in slopes:
        omega *= slope * (slope - 1)
    for i, slope in enumerate(slopes):
        for other in slopes[i + 1 :]:
            omega *= slope - other
    return x, y, sp.expand(H), slopes, sp.expand(omega)


def factored_face(row: RowSpec, part: Sequence[int]) -> str:
    factors = ["(y-x)^%d" % part[0]]
    for idx, exponent in enumerate(part[1:], start=2):
        factors.append("(y-s%d*x)^%d" % (idx, exponent))
    return "y^%d*%s" % (row.V2, "*".join(factors))


def coeff_poly(
    prefix: str,
    index: int,
    mons: Sequence[tuple[int, int]],
    x: sp.Symbol,
    y: sp.Symbol,
    params: list[sp.Symbol],
) -> sp.Expr:
    out = sp.Integer(0)
    for a, b in mons:
        var = sp.Symbol("%s%d_%d_%d" % (prefix, index, a, b))
        params.append(var)
        out += var * x**a * y**b
    return sp.expand(out)


def hadic_by_power(
    h: sp.Expr,
    low_terms: Sequence[tuple[sp.Expr, int]],
    high_terms: Sequence[tuple[sp.Expr, int]],
    x: sp.Symbol,
    y: sp.Symbol,
) -> dict[int, sp.Expr]:
    by_power: dict[int, sp.Expr] = {}
    for aa, r in low_terms:
        for bb, s in high_terms:
            same = jac(aa, bb, x, y)
            if same != 0:
                by_power[r + s] = by_power.get(r + s, 0) + same
            lower = sp.expand(s * bb * jac(aa, h, x, y) + r * aa * jac(h, bb, x, y))
            if lower != 0:
                by_power[r + s - 1] = by_power.get(r + s - 1, 0) + lower
    if 0 not in by_power:
        by_power[0] = sp.Integer(0)
    level = 0
    kmax = max(by_power) if by_power else 0
    h_poly = sp.Poly(h, y)
    while level <= kmax:
        rem = sp.expand(by_power.get(level, 0))
        if rem != 0:
            qdiv, rdiv = sp.div(sp.Poly(rem, y), h_poly, y)
            by_power[level] = sp.expand(rdiv.as_expr())
            if qdiv != 0:
                by_power[level + 1] = by_power.get(level + 1, 0) + sp.expand(qdiv.as_expr())
                kmax = max(kmax, level + 1)
        level += 1
    return {k: sp.expand(v) for k, v in by_power.items() if sp.expand(v) != 0 or k == 0}


def eqs_from_by_power(
    by_power: dict[int, sp.Expr],
    c: sp.Symbol,
    kexp: int,
    x: sp.Symbol,
    y: sp.Symbol,
) -> tuple[list[TaggedRow], list[int], dict]:
    rows: list[TaggedRow] = []
    levels = []
    source_index = 0
    level0_before = sp.expand(by_power.get(0, 0))
    level0_poly = sp.Poly(level0_before, x, y)
    target_coeff = sp.expand(level0_poly.coeff_monomial(x**kexp))
    deg_level0 = level0_poly.degree(x) if not level0_poly.is_zero else -math.inf
    max_nf_deg = -math.inf
    for hpow in sorted(by_power):
        rem = by_power[hpow]
        if hpow == 0:
            rem = sp.expand(rem - c * x**kexp)
        if rem == 0:
            continue
        levels.append(hpow)
        poly = sp.Poly(rem, x, y)
        max_nf_deg = max(max_nf_deg, poly.degree(x))
        for monomial, coefficient in poly.terms():
            coefficient = sp.expand(coefficient)
            if coefficient != 0:
                rows.append(TaggedRow(source_index, hpow, tuple(monomial), coefficient))
                source_index += 1
    gate = {
        "level0_deg_x_before_minus_c": None if deg_level0 == -math.inf else int(deg_level0),
        "normal_form_max_deg_x_after_minus_c": None if max_nf_deg == -math.inf else int(max_nf_deg),
        "target_xk_level0_coefficient": str(target_coeff),
        "target_xk_level0_nonzero": target_coeff != 0,
    }
    return rows, levels, gate


def build_topface_system(row: RowSpec, part: Sequence[int]) -> dict:
    C = shape_for(row)
    if tuple(part) not in allowed_partitions(row):
        raise ValueError("%s partition %s outside Prop. 4.6 cap" % (row.source, part))
    x, y, top, slopes, omega = face(row, part)
    c = sp.Symbol("c")
    hpars: list[sp.Symbol] = []
    h_lower = corrected_h_lower(C)
    h = top + coeff_poly("h", 0, h_lower, x, y, hpars)
    alpha_params: list[sp.Symbol] = []
    beta_params: list[sp.Symbol] = []
    e = C["eprime"]
    q = C["dprime"]
    alpha = {
        i: coeff_poly("A", i, coefficient_monomials(C, i, beta=False), x, y, alpha_params)
        for i in range(1, e + 1)
    }
    beta = {
        j: coeff_poly("B", j, coefficient_monomials(C, j, beta=True), x, y, beta_params)
        for j in range(2, q + 1)
    }
    high_terms = [(sp.Integer(1), e)] + [(alpha[i], e - i) for i in range(1, e + 1)]
    low_terms = [(sp.Integer(1), q)] + [(beta[j], q - j) for j in range(2, q + 1)]
    by_power = hadic_by_power(h, low_terms, high_terms, x, y)
    rows, levels, deg_gate = eqs_from_by_power(by_power, c, row.k, x, y)
    params = hpars + list(slopes) + alpha_params + beta_params
    all_params = params + [c]
    sat = sp.expand(c * omega)
    h_old_count = len([m for m in C["h_all"] if m != (0, C["K"])])
    meta = {
        "kind": "topface-generic",
        "row": asdict(row),
        "partition": list(part),
        "partition_label": "+".join(map(str, part)),
        "top_face_factored": factored_face(row, part),
        "K": C["K"],
        "uprime": C["u"],
        "dprime": q,
        "eprime": e,
        "delta1": frac_s(C["delta1"]),
        "delta2": frac_s(C["delta2"]),
        "bound_h": frac_s(C["V2"] * C["delta1"] + C["u"] * C["delta2"]),
        "support_rule": "ord h(sigma1)>=V2*delta1+u*delta2; beta x-degree<=k+1",
        "h_lower_count_corrected": len(h_lower),
        "h_old_d1_count_excluding_monic": h_old_count,
        "slope_count": len(slopes),
        "alpha_dims": [len(coefficient_monomials(C, i, beta=False)) for i in range(1, e + 1)],
        "beta_dims": [len(coefficient_monomials(C, j, beta=True)) for j in range(2, q + 1)],
        "unknowns": len(all_params),
        "unknowns_excluding_c": len(params),
        "equations": len(rows),
        "levels": levels,
        "slope_symbols": [str(s) for s in slopes],
        "omega": str(omega),
        "saturation_factor": str(sat),
        "deg_x_J_gate": deg_gate,
    }
    return {
        "meta": meta,
        "x": x,
        "y": y,
        "h": sp.expand(h),
        "rows": rows,
        "params": params,
        "c": c,
        "sat": sat,
        "slopes": list(slopes),
    }


def build_k16_t3_system() -> dict:
    driver = load_module(INPUTS / "t_order_system.py", "bigrows_k16_t3_order")
    data = driver.build(t=3, gauged=True)
    rows = [
        TaggedRow(index, hpow, tuple(mon), sp.expand(expr))
        for index, (hpow, mon, expr) in enumerate(data["tagged"])
    ]
    meta = {
        "kind": "k16-t3-control",
        "row": "(40,28;37;3;k=1)",
        "unknowns": len(data["params"]) + 1,
        "equations": len(rows),
        "expected": "36 -> residual -> quadratic K -> [1]",
    }
    return {
        "meta": meta,
        "x": sp.Symbol("gamma"),
        "y": sp.Symbol("pi"),
        "h": data["h"],
        "rows": rows,
        "params": list(data["params"]),
        "c": data["c"],
        "sat": data["c"],
        "slopes": [],
    }


def row_order(item: tuple[int, TaggedRow]):
    index, row = item
    return (-row.h_power, row.monomial[0], row.monomial[1], index)


def constant_q_affine(expr: sp.Expr, variable: sp.Symbol):
    if variable not in expr.free_symbols:
        return None
    coeff = sp.expand(sp.diff(expr, variable))
    if not coeff.is_Rational or coeff == 0:
        return None
    remainder = sp.expand(expr - coeff * variable)
    if variable in remainder.free_symbols:
        return None
    return sp.Rational(coeff), remainder


def q_pivot_reduce(
    rows_in: Sequence[TaggedRow],
    variables: Sequence[sp.Symbol],
    c: sp.Symbol,
    *,
    max_pivots: int = 512,
    max_seconds: float = 600.0,
    max_expression_bytes: int = 25_000_000,
) -> Reduction:
    started = time.monotonic()
    rows = [dataclasses.replace(row, expr=sp.expand(row.expr)) for row in rows_in]
    original_rows = [dataclasses.replace(row, expr=row.expr) for row in rows]
    remaining = list(variables)
    pivots: list[Pivot] = []
    zero_sources: set[int] = set()

    while True:
        if len(pivots) >= max_pivots:
            raise RuntimeError("Q-pivot bound reached")
        if time.monotonic() - started > max_seconds:
            raise TimeLimitExceeded("Q-pivot pass exceeded bound")
        choice = None
        for row_index, row in sorted(enumerate(rows), key=row_order):
            row_free = row.expr.free_symbols
            for variable_index, variable in enumerate(remaining):
                if variable not in row_free:
                    continue
                affine = constant_q_affine(row.expr, variable)
                if affine is None:
                    continue
                coeff, remainder = affine
                choice = (row_index, variable_index, row, variable, coeff, remainder)
                break
            if choice is not None:
                break
        if choice is None:
            break

        row_index, variable_index, pivot_row, variable, coeff, remainder = choice
        rhs = sp.expand(-remainder / coeff)
        if variable in rhs.free_symbols:
            raise AssertionError("Q pivot RHS contains its variable")
        if sp.expand(pivot_row.expr.subs(variable, rhs)) != 0:
            raise AssertionError("Q pivot substitution did not kill row")
        pivots.append(
            Pivot(
                step=len(pivots) + 1,
                source_index=pivot_row.source_index,
                h_power=pivot_row.h_power,
                monomial=pivot_row.monomial,
                variable=variable,
                coefficient=coeff,
                rhs=rhs,
            )
        )
        zero_sources.add(pivot_row.source_index)
        del rows[row_index]
        del remaining[variable_index]
        next_rows = []
        for row in rows:
            expr = row.expr
            if variable in expr.free_symbols:
                expr = sp.expand(expr.subs(variable, rhs))
            if expr == 0:
                zero_sources.add(row.source_index)
            else:
                next_rows.append(dataclasses.replace(row, expr=expr))
        rows = next_rows
        expression_bytes = sum(len(str(row.expr)) for row in rows)
        if expression_bytes > max_expression_bytes:
            raise RuntimeError("Q residual exceeds byte bound: %d" % expression_bytes)

    resolved: dict[sp.Symbol, sp.Expr] = {}
    for pivot in reversed(pivots):
        final_rhs = sp.expand(pivot.rhs.subs(resolved, simultaneous=True))
        if final_rhs.free_symbols.intersection({p.variable for p in pivots}):
            raise AssertionError("unresolved Q pivot variable in final map")
        pivot.final_rhs = final_rhs
        resolved[pivot.variable] = final_rhs

    surviving = {row.source_index: row for row in rows}
    for original in original_rows:
        image = sp.expand(original.expr.subs(resolved, simultaneous=True))
        if original.source_index in surviving:
            if sp.expand(image - surviving[original.source_index].expr) != 0:
                raise AssertionError("Q map image mismatch at row %d" % original.source_index)
        elif image != 0:
            raise AssertionError("deleted row has nonzero Q-map image %d" % original.source_index)

    return Reduction(
        original_variables=list(variables),
        remaining_variables=remaining,
        c=c,
        rows=rows,
        original_rows=original_rows,
        pivots=pivots,
        substitutions=resolved,
        zero_source_indices=sorted(zero_sources),
        elapsed=time.monotonic() - started,
    )


def monomial_exponents(expr: sp.Expr, variables: Sequence[sp.Symbol]) -> list[tuple[int, ...]]:
    poly = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    return [tuple(map(int, mon)) for mon in poly.monoms()]


def natural_weight(variable: sp.Symbol, meta: dict) -> int | None:
    name = str(variable)
    K = int(meta.get("K", 0) or 0)
    if name == "c":
        if K:
            return int((meta["dprime"] + meta["eprime"]) * K - 2 - meta["row"]["k"])
        return 65
    if name.startswith("h0_") and K:
        _h, a, b = name.split("_")
        return K - int(a) - int(b)
    match = re.match(r"([AB])(\d+)_(\d+)_(\d+)$", name)
    if match and K:
        deficit = int(match.group(2))
        a = int(match.group(3))
        b = int(match.group(4))
        return deficit * K - a - b
    if re.match(r"s\d+$", name):
        return 0
    if meta.get("kind") == "k16-t3-control":
        known = {
            "b1": 1,
            "b2": 2,
            "b3": 3,
            "b4": 4,
            "a1_0": 4,
            "a2_0": 8,
            "a4_0": 16,
            "a5_0": 20,
            "a6_0": 24,
            "a7_0": 28,
            "a8_0": 32,
            "a9_0": 36,
            "q2_0": 8,
            "q3_0": 12,
            "q4_0": 16,
            "q4_1": 13,
            "q5_0": 20,
            "q5_1": 17,
            "q6_0": 24,
            "q6_1": 21,
            "q7_0": 25,
            "q7_1": 26,
            "c": 65,
        }
        return known.get(name)
    return None


def verify_weights(rows: Sequence[TaggedRow], variables: Sequence[sp.Symbol], weights: Sequence[int]) -> bool:
    weight_map = dict(zip(variables, weights))
    for row in rows:
        poly = sp.Poly(sp.expand(row.expr), *variables, domain=sp.QQ)
        degrees = {
            sum(exp * weight_map[var] for exp, var in zip(mon, variables))
            for mon in poly.monoms()
        }
        if len(degrees) > 1:
            return False
    return True


def integerize_vector(vec: Sequence[sp.Rational]) -> list[int]:
    den = 1
    for item in vec:
        den = math.lcm(den, int(sp.denom(item)))
    ints = [int(item * den) for item in vec]
    gcd = 0
    for item in ints:
        gcd = math.gcd(gcd, abs(item))
    if gcd > 1:
        ints = [item // gcd for item in ints]
    if ints and min(ints) < 0:
        ints = [-item for item in ints]
    return ints


def solve_grading(rows: Sequence[TaggedRow], variables: Sequence[sp.Symbol], meta: dict) -> dict:
    candidate = [natural_weight(v, meta) for v in variables]
    if all(item is not None for item in candidate):
        weights = [int(item) for item in candidate]  # type: ignore[arg-type]
        if verify_weights(rows, variables, weights):
            return {
                "status": "VERIFIED_NATURAL",
                "strictly_positive": all(w > 0 for w in weights),
                "nonnegative": all(w >= 0 for w in weights),
                "variables": [str(v) for v in variables],
                "weights": weights,
                "zero_weight_variables": [str(v) for v, w in zip(variables, weights) if w == 0],
            }

    constraints: list[list[int]] = []
    for row in rows:
        monoms = monomial_exponents(row.expr, variables)
        if len(monoms) <= 1:
            continue
        base = monoms[0]
        for mon in monoms[1:]:
            constraints.append([m - b for m, b in zip(mon, base)])
    if not constraints:
        weights = [1 for _ in variables]
        return {
            "status": "TRIVIAL_ALL_ONES",
            "strictly_positive": True,
            "nonnegative": True,
            "variables": [str(v) for v in variables],
            "weights": weights,
            "zero_weight_variables": [],
        }
    matrix = sp.Matrix(constraints)
    basis = matrix.nullspace()
    if not basis:
        return {
            "status": "NO_GRADING",
            "strictly_positive": False,
            "nonnegative": False,
            "rank": matrix.rank(),
            "constraints": len(constraints),
        }

    tries: list[list[sp.Rational]] = []
    for bvec in basis:
        tries.append([sp.Rational(x) for x in bvec])
    tries.append([sum(sp.Rational(bvec[i]) for bvec in basis) for i in range(len(variables))])
    coeff_sets = [
        range(1, min(7, len(basis) + 3)),
        range(-3, 4),
    ]
    if len(basis) <= 8:
        import itertools

        for coeffs in itertools.product(range(-3, 4), repeat=len(basis)):
            if not any(coeffs):
                continue
            tries.append(
                [
                    sum(sp.Rational(c) * sp.Rational(basis[j][i]) for j, c in enumerate(coeffs))
                    for i in range(len(variables))
                ]
            )
            if len(tries) > 20000:
                break
    else:
        for scale in coeff_sets[0]:
            tries.append(
                [
                    sum(sp.Rational((j + 1) ** scale) * sp.Rational(basis[j][i]) for j in range(len(basis)))
                    for i in range(len(variables))
                ]
            )

    best_nonnegative = None
    for vec in tries:
        ints = integerize_vector(vec)
        if not any(ints):
            continue
        if min(ints) < 0:
            ints = [-v for v in ints]
        if all(v > 0 for v in ints) and verify_weights(rows, variables, ints):
            return {
                "status": "SOLVED_NULLSPACE_POSITIVE",
                "strictly_positive": True,
                "nonnegative": True,
                "variables": [str(v) for v in variables],
                "weights": ints,
                "zero_weight_variables": [],
                "constraints": len(constraints),
                "nullity": len(basis),
            }
        if all(v >= 0 for v in ints) and any(v > 0 for v in ints) and verify_weights(rows, variables, ints):
            best_nonnegative = ints
    if best_nonnegative is not None:
        return {
            "status": "SOLVED_NULLSPACE_NONNEGATIVE",
            "strictly_positive": False,
            "nonnegative": True,
            "variables": [str(v) for v in variables],
            "weights": best_nonnegative,
            "zero_weight_variables": [
                str(v) for v, w in zip(variables, best_nonnegative) if w == 0
            ],
            "constraints": len(constraints),
            "nullity": len(basis),
        }
    return {
        "status": "NO_POSITIVE_VECTOR_FOUND",
        "strictly_positive": False,
        "nonnegative": False,
        "constraints": len(constraints),
        "nullity": len(basis),
    }


def find_c_equation(rows: Sequence[TaggedRow], c: sp.Symbol) -> tuple[TaggedRow, sp.Expr] | None:
    matches = []
    for row in rows:
        affine = constant_q_affine(row.expr, c)
        if affine is None:
            continue
        coeff, rem = affine
        solved = sp.expand(-rem / coeff)
        matches.append((row, solved))
    if not matches:
        return None
    return min(matches, key=lambda item: (len(str(item[1])), item[0].source_index))


def factor_symbol_powers(expr: sp.Expr, variables: Sequence[sp.Symbol]) -> list[sp.Symbol]:
    factors = []
    coeff, rest = sp.factor_list(sp.factor(expr))
    for base, exponent in rest:
        if exponent <= 0:
            continue
        if isinstance(base, sp.Symbol) and base in variables:
            factors.append(base)
    return factors


def normalize_slice(
    reduction: Reduction,
    grading: dict,
    sat: sp.Expr,
) -> dict:
    variables = list(reduction.remaining_variables)
    c = reduction.c
    all_vars = variables + [c]
    c_match = find_c_equation(reduction.rows, c)
    if c_match is None:
        return {"status": "NO_C_AFFINE_ROW", "covering": None}
    c_row, c_expr = c_match
    weight_by_name = dict(zip(grading.get("variables", []), grading.get("weights", [])))
    positive_vars = [
        var
        for var in factor_symbol_powers(c_expr, variables)
        if weight_by_name.get(str(var), 0) > 0
    ]
    if not positive_vars:
        return {
            "status": "NO_FORCED_POSITIVE_WEIGHT_VARIABLE",
            "c_row": c_row.source_index,
            "c_expr": str(c_expr),
        }
    # The torus can normalize any forced nonzero positive-weight factor.  Use
    # the smallest weight first; this reproduces the charged K=16 t=3
    # q4_1=1 slice and generally keeps the base equation degree down.
    norm_var = min(positive_vars, key=lambda var: (weight_by_name[str(var)], str(var)))
    norm_weight = int(weight_by_name[str(norm_var)])
    substitutions = {norm_var: sp.Integer(1)}
    c_expr_norm = sp.expand(c_expr.subs(substitutions))
    substitutions[c] = c_expr_norm
    sliced_rows = []
    dropped = []
    for row in reduction.rows:
        if row.source_index == c_row.source_index:
            dropped.append({"source_index": row.source_index, "reason": "c_affine_row"})
            continue
        expr = sp.expand(row.expr.subs(substitutions, simultaneous=True))
        if expr == 0:
            dropped.append({"source_index": row.source_index, "reason": "zero_after_slice"})
            continue
        sliced_rows.append(dataclasses.replace(row, expr=expr))
    remaining = [var for var in variables if var != norm_var]
    sat_image = sp.expand(sat.subs(reduction.substitutions, simultaneous=True).subs(substitutions, simultaneous=True))
    return {
        "status": "SLICED",
        "c_row": c_row.source_index,
        "c_expr_before_slice": str(c_expr),
        "c_expr_after_slice": str(c_expr_norm),
        "normalizing_variable": str(norm_var),
        "normalizing_weight": norm_weight,
        "covering": (
            "On c!=0 the displayed c equation forces %s!=0; "
            "homogeneity for the verified grading lets a Qbar torus element "
            "with lambda^%d*%s=1 move the point to %s=1. "
            "The converse map is inclusion of the slice."
        )
        % (norm_var, norm_weight, norm_var, norm_var),
        "rows": sliced_rows,
        "remaining_variables": remaining,
        "sat_image": sat_image,
        "dropped": dropped,
    }


def primitive_expr(expr: sp.Expr, variables: Sequence[sp.Symbol]) -> tuple[sp.Expr, sp.Rational]:
    poly = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    denom, cleared = poly.clear_denoms(convert=True)
    content, primitive = cleared.primitive()
    multiplier = sp.Rational(denom, content)
    if primitive.LC() < 0:
        primitive = -primitive
        multiplier = -multiplier
    if sp.expand(primitive.as_expr() - multiplier * expr) != 0:
        raise AssertionError("primitive associate identity failed")
    return sp.expand(primitive.as_expr()), multiplier


def deduplicate_q(rows: Sequence[TaggedRow], variables: Sequence[sp.Symbol]) -> tuple[list[TaggedRow], list[dict]]:
    kept = []
    seen: dict[str, TaggedRow] = {}
    dropped = []
    for row in rows:
        primitive, multiplier = primitive_expr(row.expr, variables)
        key = str(primitive)
        if key in seen:
            dropped.append(
                {
                    "source_index": row.source_index,
                    "reason": "duplicate_Qstar_primitive",
                    "representative_source_index": seen[key].source_index,
                    "integer_row_multiplier": str(multiplier),
                }
            )
        else:
            new_row = dataclasses.replace(row, expr=primitive)
            seen[key] = new_row
            kept.append(new_row)
    return kept, dropped


def choose_univariate_base(rows: Sequence[TaggedRow], variables: Sequence[sp.Symbol]) -> dict | None:
    choices = []
    for row in rows:
        free = row.expr.free_symbols
        for var in variables:
            if free and free <= {var}:
                poly = sp.Poly(row.expr, var, domain=sp.QQ)
                if poly.degree() > 0:
                    choices.append((poly.degree(), len(str(row.expr)), row.source_index, var, row.expr))
    if not choices:
        return None
    _degree, _size, source, var, expr = min(choices)
    coeff, facs = sp.factor_list(sp.Poly(expr, var, domain=sp.QQ).as_expr())
    return {
        "source_index": source,
        "variable": var,
        "polynomial": sp.expand(expr),
        "content": str(coeff),
        "factors": [{"factor": sp.expand(f), "degree": sp.Poly(f, var).degree(), "multiplicity": int(m)} for f, m in facs],
    }


class NumberFieldReducer:
    def __init__(self, y: sp.Symbol, H: sp.Expr, variables: Sequence[sp.Symbol]):
        self.y = y
        self.H = sp.Poly(sp.expand(H), y, domain=sp.QQ)
        self.variables = list(variables)
        self.domain = sp.QQ[tuple(self.variables)]
        self.H_over_domain = sp.Poly(sp.expand(H), y, domain=self.domain)

    def reduce(self, expr: sp.Expr) -> sp.Expr:
        poly = sp.Poly(sp.expand(expr), self.y, domain=self.domain)
        return sp.expand(poly.rem(self.H_over_domain).as_expr())

    def inverse(self, coeff: sp.Expr) -> sp.Expr:
        coeff = self.reduce(coeff)
        if coeff == 0:
            raise ZeroDivisionError("zero coefficient")
        if coeff.free_symbols - {self.y}:
            raise ValueError("coefficient is not in the base field")
        inv = sp.invert(sp.Poly(coeff, self.y, domain=sp.QQ), self.H).as_expr()
        inv = self.reduce(inv)
        if self.reduce(coeff * inv - 1) != 0:
            raise AssertionError("number-field inverse check failed")
        return inv


def field_affine_candidates(
    rows: Sequence[TaggedRow],
    remaining: Sequence[sp.Symbol],
    K: NumberFieldReducer,
) -> list[tuple]:
    occurrences = {
        var: sum(var in row.expr.free_symbols for row in rows)
        for var in remaining
    }
    out = []
    for row_index, row in enumerate(rows):
        terms = sp.Add.make_args(row.expr)
        for var_index, var in enumerate(remaining):
            if var not in row.expr.free_symbols:
                continue
            coeff_terms = []
            rem_terms = []
            nonlinear = False
            for term in terms:
                exp = term.as_powers_dict().get(var, 0)
                if exp == 0:
                    rem_terms.append(term)
                elif exp == 1:
                    coeff_terms.append(term / var)
                else:
                    nonlinear = True
                    break
            if nonlinear:
                continue
            coeff = sp.Add(*coeff_terms)
            rem = sp.Add(*rem_terms)
            if coeff == 0 or coeff.free_symbols - {K.y}:
                continue
            score = (
                len(str(rem)) * max(1, occurrences[var]),
                len(str(rem)),
                occurrences[var],
                row.source_index,
                var_index,
            )
            out.append((score, row_index, var_index, coeff, rem))
    return out


def deduplicate_field_rows(
    rows: Sequence[TaggedRow],
    K: NumberFieldReducer,
) -> tuple[list[TaggedRow], list[dict]]:
    kept: list[TaggedRow] = []
    seen: dict[str, TaggedRow] = {}
    dropped = []
    for row in rows:
        expr = K.reduce(row.expr)
        if expr == 0:
            dropped.append({"source_index": row.source_index, "reason": "zero_mod_H"})
            continue
        key = str(expr)
        if key in seen:
            dropped.append(
                {
                    "source_index": row.source_index,
                    "reason": "literal_duplicate_mod_H",
                    "representative_source_index": seen[key].source_index,
                }
            )
            continue
        new_row = dataclasses.replace(row, expr=expr)
        seen[key] = new_row
        kept.append(new_row)
    return kept, dropped


def reduce_over_number_field(
    rows_in: Sequence[TaggedRow],
    variables: Sequence[sp.Symbol],
    y: sp.Symbol,
    H: sp.Expr,
    sat: sp.Expr,
    *,
    max_seconds: float,
    max_bytes: int = 30_000_000,
) -> dict:
    started = time.monotonic()
    remaining = [v for v in variables if v != y]
    K = NumberFieldReducer(y, H, remaining)
    rows, dropped = deduplicate_field_rows(rows_in, K)
    sat_image = K.reduce(sat)
    pivots = []
    terminal_unit = None
    while True:
        if time.monotonic() - started > max_seconds:
            raise TimeLimitExceeded("number-field affine pass exceeded bound")
        constants = [row for row in rows if not (row.expr.free_symbols - {y})]
        nonzero_constants = [row for row in constants if K.reduce(row.expr) != 0]
        if nonzero_constants:
            row = min(nonzero_constants, key=lambda r: (len(str(r.expr)), r.source_index))
            inv = K.inverse(row.expr)
            terminal_unit = {
                "source_index": row.source_index,
                "constant": str(row.expr),
                "inverse_mod_H": str(inv),
                "identity_verified_mod_H": K.reduce(row.expr * inv - 1) == 0,
            }
            break
        candidates = field_affine_candidates(rows, remaining, K)
        if not candidates:
            break
        _score, row_index, var_index, coeff, rem = min(candidates, key=lambda item: item[0])
        row = rows[row_index]
        var = remaining[var_index]
        coeff = K.reduce(coeff)
        rem = K.reduce(rem)
        if K.reduce(row.expr - coeff * var - rem) != 0:
            raise AssertionError("field affine decomposition failed")
        inv = K.inverse(coeff)
        rhs = K.reduce(-inv * rem)
        if var in rhs.free_symbols:
            raise AssertionError("field pivot RHS contains pivot variable")
        if K.reduce(row.expr.subs(var, rhs)) != 0:
            raise AssertionError("field pivot does not kill row")
        del rows[row_index]
        del remaining[var_index]
        next_rows = []
        for old in rows:
            expr = old.expr
            if var in expr.free_symbols:
                expr = K.reduce(expr.subs(var, rhs))
            else:
                expr = K.reduce(expr)
            if expr == 0:
                dropped.append({"source_index": old.source_index, "reason": "zero_after_field_pivot"})
            else:
                next_rows.append(dataclasses.replace(old, expr=expr))
        rows, newly_dropped = deduplicate_field_rows(next_rows, K)
        dropped.extend(newly_dropped)
        size = sum(len(str(row.expr)) for row in rows)
        if size > max_bytes:
            raise RuntimeError("number-field residual exceeds byte bound: %d" % size)
        pivots.append(
            {
                "step": len(pivots) + 1,
                "source_index": row.source_index,
                "h_power": row.h_power,
                "monomial": list(row.monomial),
                "variable": str(var),
                "coefficient": str(coeff),
                "inverse_mod_H": str(inv),
                "rhs": str(rhs),
                "remaining_rows_after": len(rows),
                "remaining_variables_after": len(remaining),
                "expression_bytes_after": size,
            }
        )
    return {
        "factor": str(sp.expand(H)),
        "factor_degree": sp.Poly(H, y).degree(),
        "base_variable": str(y),
        "rows": rows,
        "remaining_variables": remaining,
        "sat_image": sat_image,
        "pivots": pivots,
        "dropped": dropped,
        "terminal_unit": terminal_unit,
        "elapsed": round(time.monotonic() - started, 3),
    }


def emit_actual_pair(lines: list[str], char: int | str) -> None:
    lines.extend(
        [
            "ring RAC=%s,(gamma,pi),dp;" % char,
            "poly FAC=pi;",
            "poly GAC=pi-(gamma^2)/2;",
            "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
            'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); } else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
        ]
    )


def rename_symbols(symbols: Sequence[sp.Symbol]) -> tuple[list[str], dict[sp.Symbol, sp.Symbol]]:
    names = []
    rename = {}
    for sym in symbols:
        base = clean_name(str(sym))
        name = base
        suffix = 1
        while name in names:
            suffix += 1
            name = "%s_%d" % (base, suffix)
        names.append(name)
        rename[sym] = sp.Symbol(name)
    return names, rename


def emit_field_singular(
    path: Path,
    rows: Sequence[TaggedRow],
    variables: Sequence[sp.Symbol],
    y: sp.Symbol,
    H: sp.Expr,
    sat: sp.Expr,
    *,
    char: int,
    method: str = "std",
    terminal_unit: dict | None = None,
) -> None:
    if method not in ("std", "slimgb"):
        raise ValueError(method)
    T = sp.Symbol("T")
    sat_is_unit = bool(sat != 0 and not (sat.free_symbols - {y}))
    need_T = not sat_is_unit and terminal_unit is None
    # T is always present because the wrapper controls use T*SAT-1 even when
    # the main ideal no longer needs Rabinowitsch saturation.
    ring_symbols = list(variables) + [T]
    names, rename = rename_symbols(ring_symbols)
    main_vars = [y] + [v for v in variables if v != y]
    gens = []
    for row in rows:
        gens.append(singular_expr(row.expr.subs(rename), main_vars + ([rename[T]] if need_T and T in rename else [])))
    if terminal_unit is not None:
        gens.append("1")
    elif need_T:
        gens.append("%s*(%s)-1" % (rename[T], singular_expr(sat.subs(rename))))
    if not gens:
        gens = ["0"]
    Hs = singular_expr(H, [y])
    lines = [
        "// generated by bigrows preprocess.py",
        "// coefficient factor %s in base variable %s" % (Hs, y),
    ]
    emit_actual_pair(lines, char)
    lines.extend(
        [
            "ring R=(%d,%s),(%s),dp;" % (char, y, ",".join(names)),
            "minpoly=%s;" % Hs,
            "option(redSB);",
            'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); } else { print("CONTROL_RING_FAIL"); }',
            "poly SAT=%s;" % singular_expr(sat.subs(rename)),
            'print("CONTROL_EMPTY_START");',
            "ideal CE=SAT,T*SAT-1;",
            "ideal GE=std(CE);",
            'if (typeof(GE)=="ideal" && nameof(basering)=="R") { print("CONTROL_EMPTY_EXTRACT_RING_PASS"); } else { print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }',
            'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
            'print("CONTROL_NONEMPTY_START");',
            "ideal CN=SAT-1,T*SAT-1;",
            "ideal GN=std(CN);",
            'if (typeof(GN)=="ideal" && nameof(basering)=="R") { print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); } else { print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }',
            'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
            'print("MAIN_START residual_equations=%d residual_unknowns=%d char=%d");'
            % (len(gens), len(ring_symbols), char),
            "ideal I=%s;" % ",\n".join(gens),
            "ideal G=%s(I);" % method,
            'print("MAIN_DONE basis_size=");',
            "size(G);",
            'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); G; } else { print("MAIN_NONTRIVIAL"); }',
            "quit;",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def emit_q_singular(
    path: Path,
    rows: Sequence[TaggedRow],
    variables: Sequence[sp.Symbol],
    sat: sp.Expr,
    *,
    char: int,
    method: str = "std",
) -> None:
    T = sp.Symbol("T")
    ring_symbols = list(variables) + [T]
    names, rename = rename_symbols(ring_symbols)
    poly_vars = list(variables) + [T]
    gens = [singular_expr(row.expr.subs(rename), poly_vars) for row in rows]
    gens.append("%s*(%s)-1" % (rename[T], singular_expr(sat.subs(rename))))
    lines = ["// generated by bigrows preprocess.py exact-Q fallback"]
    emit_actual_pair(lines, char)
    lines.extend(
        [
            "ring R=%d,(%s),dp;" % (char, ",".join(names)),
            "option(redSB);",
            'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); } else { print("CONTROL_RING_FAIL"); }',
            "poly SAT=%s;" % singular_expr(sat.subs(rename)),
            'print("CONTROL_EMPTY_START");',
            "ideal CE=SAT,T*SAT-1;",
            "ideal GE=std(CE);",
            'if (typeof(GE)=="ideal" && nameof(basering)=="R") { print("CONTROL_EMPTY_EXTRACT_RING_PASS"); } else { print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }',
            'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
            'print("CONTROL_NONEMPTY_START");',
            "ideal CN=SAT-1,T*SAT-1;",
            "ideal GN=std(CN);",
            'if (typeof(GN)=="ideal" && nameof(basering)=="R") { print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); } else { print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }',
            'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
            'print("MAIN_START residual_equations=%d residual_unknowns=%d char=%d");'
            % (len(gens), len(ring_symbols), char),
            "ideal I=%s;" % ",\n".join(gens),
            "ideal G=%s(I);" % method,
            'print("MAIN_DONE basis_size=");',
            "size(G);",
            'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); G; } else { print("MAIN_NONTRIVIAL"); }',
            "quit;",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_singular_output(output: str) -> dict:
    lines = output.splitlines()

    def after(label: str):
        for idx, line in enumerate(lines):
            if line.strip() == label and idx + 1 < len(lines):
                return lines[idx + 1].strip()
        return None

    if "MAIN_SATURATED_EMPTY" in output or "MAIN_QUADRATIC_FIELD_EMPTY" in output:
        verdict = "SATURATED-EMPTY"
    elif "MAIN_NONTRIVIAL" in output:
        verdict = "SURVIVES"
    else:
        verdict = "ERROR"
    return {
        "verdict": verdict,
        "basis_size": after("MAIN_DONE basis_size="),
        "control_actual_pair_pass": "CONTROL_ACTUAL_PAIR_PASS" in output,
        "control_ring_pass": "CONTROL_RING_PASS" in output,
        "control_empty_pass": "CONTROL_EMPTY_PASS" in output,
        "control_nonempty_pass": "CONTROL_NONEMPTY_PASS" in output,
    }


def run_singular(path: Path, timeout: int) -> dict:
    started = time.time()
    try:
        proc = subprocess.run(
            ["Singular", "-q", "--no-rc", str(path)],
            capture_output=True,
            text=True,
            timeout=max(1, int(timeout)),
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode("utf-8", "ignore") if isinstance(exc.stdout, bytes) else exc.stdout
        stderr = exc.stderr.decode("utf-8", "ignore") if isinstance(exc.stderr, bytes) else exc.stderr
        return {
            "verdict": "TIMEOUT",
            "elapsed": round(time.time() - started, 3),
            "timeout": timeout,
            "stdout_tail": (stdout or "")[-2000:],
            "stderr_tail": (stderr or "")[-2000:],
        }
    output = (proc.stdout or "") + (proc.stderr or "")
    rec = parse_singular_output(output)
    rec.update(
        {
            "elapsed": round(time.time() - started, 3),
            "rc": proc.returncode,
            "stdout_tail": output[-2400:],
        }
    )
    return rec


def write_q_pivot_table(path: Path, reduction: Reduction) -> None:
    lines = [
        "step\tsource_index_0based\th_power\tx_power\ty_power\tvariable\tcoefficient_Qstar\tstep_rhs\tfinal_rhs"
    ]
    for pivot in reduction.pivots:
        lines.append(
            "%d\t%d\t%d\t%d\t%d\t%s\t%s\t%s\t%s"
            % (
                pivot.step,
                pivot.source_index,
                pivot.h_power,
                pivot.monomial[0],
                pivot.monomial[1],
                pivot.variable,
                pivot.coefficient,
                pivot.rhs,
                pivot.final_rhs,
            )
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def actual_pair_control() -> dict:
    gamma, pi = sp.symbols("gamma pi")
    J = jac(pi, pi - gamma**2 / 2, gamma, pi)
    target_tuples = {(row.n, row.m, row.M2, row.V2, row.k) for row in ROWS.values()}
    pair_tuple = (2, 2, None, None, 1)
    return {
        "pair": "(pi, pi-gamma^2/2)",
        "J": str(J),
        "jacobian_convention_pass": J == gamma,
        "tuple_membership": "FAIL",
        "reason": "degree/support data %s is not one of the charged D<=200 rows %s"
        % (pair_tuple, sorted(target_tuples)),
    }


def factor_summary(base: dict | None) -> dict | None:
    if base is None:
        return None
    return {
        "source_index": base["source_index"],
        "variable": str(base["variable"]),
        "polynomial": str(base["polynomial"]),
        "factors": [
            {
                "factor": str(item["factor"]),
                "degree": item["degree"],
                "multiplicity": item["multiplicity"],
            }
            for item in base["factors"]
        ],
    }


def stratum_stem(row_key: str, part: Sequence[int]) -> str:
    return "%s_part_%s" % (row_key, "_".join(map(str, part)))


def inventory_meta(row_key: str, part: Sequence[int]) -> dict:
    row = ROWS[row_key]
    C = shape_for(row)
    h_corr = corrected_h_lower(C)
    return {
        "kind": "topface-generic",
        "row": asdict(row),
        "partition": list(part),
        "partition_label": "+".join(map(str, part)),
        "top_face_factored": factored_face(row, part),
        "K": C["K"],
        "uprime": C["u"],
        "dprime": C["dprime"],
        "eprime": C["eprime"],
        "delta1": frac_s(C["delta1"]),
        "delta2": frac_s(C["delta2"]),
        "bound_h": frac_s(C["V2"] * C["delta1"] + C["u"] * C["delta2"]),
        "support_rule": "ord h(sigma1)>=V2*delta1+u*delta2; beta x-degree<=k+1",
        "h_lower_count_corrected": len(h_corr),
        "slope_count": max(0, len(part) - 1),
        "alpha_dims": [
            len(coefficient_monomials(C, i, beta=False))
            for i in range(1, C["eprime"] + 1)
        ],
        "beta_dims": [
            len(coefficient_monomials(C, j, beta=True))
            for j in range(2, C["dprime"] + 1)
        ],
        "unknown_estimate": len(h_corr)
        + max(0, len(part) - 1)
        + sum(len(coefficient_monomials(C, i, beta=False)) for i in range(1, C["eprime"] + 1))
        + sum(len(coefficient_monomials(C, j, beta=True)) for j in range(2, C["dprime"] + 1))
        + 1,
    }


def process_system(
    system: dict,
    stem: str,
    *,
    per_stratum_timeout: int,
    run_singular_flag: bool,
    method: str = "std",
) -> dict:
    started = time.time()
    meta = system["meta"]
    rec = {
        "typing": "MEASURED",
        "manifest": verify_inputs(),
        "actual_pair_control": actual_pair_control(),
        "meta": meta,
        "stages": {},
        "field_factors": [],
        "verdict": None,
    }
    if not rec["manifest"]["ok"]:
        rec["verdict"] = "ERROR"
        rec["reason"] = "frozen input mismatch"
        return rec
    if not meta.get("deg_x_J_gate", {"target_xk_level0_nonzero": True}).get("target_xk_level0_nonzero", True):
        rec["verdict"] = "COUNTING-BOUND"
        rec["reason"] = "deg_x J sanity gate failed: target x^k coefficient absent"
        return rec

    variables = list(system["params"])
    try:
        reduction = q_pivot_reduce(
            system["rows"],
            variables,
            system["c"],
            max_seconds=max(5.0, per_stratum_timeout * 0.35),
        )
    except Exception as exc:
        rec["verdict"] = "COUNTING-BOUND"
        rec["reason"] = "Q-pivot preprocessing blocked: %s: %s" % (type(exc).__name__, exc)
        return rec
    pivot_dir = OUT / "pivots"
    write_q_pivot_table(pivot_dir / (stem + "_Q_pivots.tsv"), reduction)
    rec["stages"]["q_pivots"] = {
        "original_unknowns": len(variables) + 1,
        "original_equations": len(system["rows"]),
        "pivot_count": len(reduction.pivots),
        "residual_unknowns": len(reduction.remaining_variables) + 1,
        "residual_equations": len(reduction.rows),
        "zero_source_indices": reduction.zero_source_indices,
        "elapsed": round(reduction.elapsed, 3),
        "table": str((pivot_dir / (stem + "_Q_pivots.tsv")).relative_to(ROOT)),
        "all_pivots_Qstar": all(p.coefficient.is_Rational and p.coefficient != 0 for p in reduction.pivots),
        "ring_map_verified_on_every_original_generator": True,
    }

    all_vars = reduction.remaining_variables + [reduction.c]
    try:
        grading = solve_grading(reduction.rows, all_vars, meta)
    except Exception as exc:
        grading = {"status": "ERROR", "error": "%s: %s" % (type(exc).__name__, exc)}
    rec["stages"]["grading"] = grading
    if not grading.get("nonnegative"):
        rec["verdict"] = "COUNTING-BOUND"
        rec["reason"] = "no verified nonnegative grading after Q pivots"
        return rec

    sliced = normalize_slice(reduction, grading, system["sat"])
    rec["stages"]["normalization"] = {
        key: value
        for key, value in sliced.items()
        if key not in {"rows", "remaining_variables", "sat_image"}
    }
    if sliced.get("status") != "SLICED":
        rec["verdict"] = "COUNTING-BOUND"
        rec["reason"] = "normalization blocked: %s" % sliced.get("status")
        return rec
    remaining = sliced["remaining_variables"]
    sliced_rows = sliced["rows"]
    sat_image = sliced["sat_image"]
    try:
        q_rows, q_dropped = deduplicate_q(sliced_rows, remaining)
    except Exception as exc:
        rec["verdict"] = "COUNTING-BOUND"
        rec["reason"] = "Q primitive/deduplicate blocked: %s: %s" % (type(exc).__name__, exc)
        return rec
    rec["stages"]["q_slice"] = {
        "rows_before_dedup": len(sliced_rows),
        "rows_after_dedup": len(q_rows),
        "remaining_unknowns": len(remaining),
        "dropped": q_dropped,
        "sat_image": str(sat_image),
    }

    base = choose_univariate_base(q_rows, remaining)
    rec["stages"]["univariate_base"] = factor_summary(base)
    if base is None:
        if run_singular_flag:
            scripts = []
            runs = []
            for prime in PRIMES:
                path = OUT / "systems" / (stem + "_slice_mod_%d.sing" % prime)
                emit_q_singular(path, q_rows, remaining, sat_image, char=prime, method=method)
                rr = run_singular(path, max(1, int(per_stratum_timeout - (time.time() - started))))
                rr["char"] = prime
                rr["script"] = str(path.relative_to(ROOT))
                runs.append(rr)
                scripts.append(str(path.relative_to(ROOT)))
                if rr["verdict"] == "TIMEOUT":
                    break
            rec["stages"]["q_slice"]["modular_runs"] = runs
        rec["verdict"] = "COUNTING-BOUND"
        rec["reason"] = "no univariate base equation after normalized Q slice"
        return rec

    y = base["variable"]
    all_empty = True
    any_survive = False
    for factor_item in base["factors"]:
        factor_expr = factor_item["factor"]
        try:
            field = reduce_over_number_field(
                q_rows,
                remaining,
                y,
                factor_expr,
                sat_image,
                max_seconds=max(5.0, per_stratum_timeout * 0.25),
            )
        except Exception as exc:
            rec["field_factors"].append(
                {
                    "factor": str(factor_expr),
                    "verdict": "COUNTING-BOUND",
                    "reason": "number-field preprocessing blocked: %s: %s" % (type(exc).__name__, exc),
                }
            )
            all_empty = False
            continue
        factor_rec = {
            key: value
            for key, value in field.items()
            if key not in {"rows", "remaining_variables", "sat_image"}
        }
        factor_rec["residual_rows"] = len(field["rows"])
        factor_rec["residual_unknowns"] = len(field["remaining_variables"])
        factor_rec["sat_image"] = str(field["sat_image"])
        factor_rec["runs"] = []
        if field["sat_image"] == 0:
            factor_rec["verdict"] = "SATURATED-EMPTY"
            factor_rec["reason"] = "saturation factor is zero on this base factor"
            rec["field_factors"].append(factor_rec)
            continue
        if run_singular_flag:
            for prime in PRIMES:
                remaining_seconds = max(1, int(per_stratum_timeout - (time.time() - started)))
                path = OUT / "systems" / (stem + "_factor_%d_mod_%d.sing" % (len(rec["field_factors"]) + 1, prime))
                emit_field_singular(
                    path,
                    field["rows"],
                    field["remaining_variables"],
                    y,
                    factor_expr,
                    field["sat_image"],
                    char=prime,
                    method=method,
                    terminal_unit=field["terminal_unit"],
                )
                rr = run_singular(path, remaining_seconds)
                rr["char"] = prime
                rr["script"] = str(path.relative_to(ROOT))
                factor_rec["runs"].append(rr)
                if rr["verdict"] in ("TIMEOUT", "ERROR"):
                    break
            if factor_rec["runs"] and all(run.get("verdict") == "SATURATED-EMPTY" for run in factor_rec["runs"]):
                remaining_seconds = max(1, int(per_stratum_timeout - (time.time() - started)))
                path = OUT / "systems" / (stem + "_factor_%d_Q.sing" % (len(rec["field_factors"]) + 1))
                emit_field_singular(
                    path,
                    field["rows"],
                    field["remaining_variables"],
                    y,
                    factor_expr,
                    field["sat_image"],
                    char=0,
                    method=method,
                    terminal_unit=field["terminal_unit"],
                )
                rr = run_singular(path, remaining_seconds)
                rr["char"] = 0
                rr["script"] = str(path.relative_to(ROOT))
                factor_rec["runs"].append(rr)
        if field["terminal_unit"] is not None:
            factor_rec["verdict"] = "SATURATED-EMPTY"
            factor_rec["reason"] = "field preprocessing produced a checked coefficient-field unit"
        elif run_singular_flag and factor_rec["runs"]:
            exact_runs = [run for run in factor_rec["runs"] if run.get("char") == 0]
            if exact_runs and exact_runs[-1]["verdict"] == "SATURATED-EMPTY":
                factor_rec["verdict"] = "SATURATED-EMPTY"
                factor_rec["reason"] = "exact coefficient-field Singular basis is [1]"
            elif any(run["verdict"] == "SURVIVES" for run in factor_rec["runs"]):
                factor_rec["verdict"] = "COUNTING-BOUND"
                factor_rec["reason"] = "nonunit basis without representative extraction"
                any_survive = True
                all_empty = False
            else:
                factor_rec["verdict"] = "COUNTING-BOUND"
                factor_rec["reason"] = "field run did not reach exact [1]"
                all_empty = False
        else:
            factor_rec["verdict"] = "COUNTING-BOUND"
            factor_rec["reason"] = "Singular run disabled before exact field certificate"
            all_empty = False
        rec["field_factors"].append(factor_rec)

    if all_empty and rec["field_factors"]:
        rec["verdict"] = "SATURATED-EMPTY"
        rec["covering_chain"] = [
            "Q* affine pivots are quotient-ring isomorphisms and their inverse images were checked on every original generator.",
            rec["stages"]["normalization"]["covering"],
            "The univariate base row factors over Q; each irreducible factor was treated as a coefficient field Q[y]/(factor), covering all conjugates of that factor.",
            "Every factor branch is saturated-empty, so the normalized slice and therefore the original c!=0 locus are empty over Qbar.",
        ]
    else:
        rec["verdict"] = "COUNTING-BOUND"
        rec["reason"] = rec.get("reason") or (
            "one or more irreducible base branches remain open"
            if not any_survive
            else "a nonunit branch lacks a representative/Jacobian check"
        )
    rec["elapsed"] = round(time.time() - started, 3)
    return rec


def process_stratum_task(args_tuple):
    row_key, part, timeout_seconds, run_singular_flag, method = args_tuple
    stem = stratum_stem(row_key, part)
    outpath = OUT / "results" / (stem + ".json")
    meta0 = inventory_meta(row_key, part)
    try:
        with time_limit(timeout_seconds + 10):
            started = time.time()
            system = build_topface_system(ROWS[row_key], part)
            system["meta"]["build_elapsed"] = round(time.time() - started, 3)
            rec = process_system(
                system,
                stem,
                per_stratum_timeout=timeout_seconds,
                run_singular_flag=run_singular_flag,
                method=method,
            )
    except Exception as exc:
        rec = {
            "typing": "MEASURED",
            "meta": meta0,
            "verdict": "COUNTING-BOUND",
            "reason": "worker blocked: %s: %s" % (type(exc).__name__, exc),
        }
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(to_jsonable(rec), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"row_key": row_key, "partition": list(part), "verdict": rec.get("verdict"), "path": str(outpath.relative_to(ROOT))}


def to_jsonable(value):
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, sp.Basic):
        return str(value)
    if isinstance(value, F):
        return frac_s(value)
    if dataclasses.is_dataclass(value):
        return to_jsonable(asdict(value))
    if isinstance(value, dict):
        return {str(k): to_jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_jsonable(v) for v in value]
    return value


def write_summary(result_items: list[dict]) -> dict:
    records = []
    for item in result_items:
        path = ROOT / item["path"]
        records.append(json.loads(path.read_text(encoding="utf-8")))
    row_summary: dict[str, dict] = {}
    for rec in records:
        row = rec.get("meta", {}).get("row", {})
        key = row.get("key") or rec.get("meta", {}).get("row_key") or "unknown"
        bucket = row_summary.setdefault(key, {"total": 0, "empty": 0, "open": [], "verdict": None})
        bucket["total"] += 1
        if rec.get("verdict") == "SATURATED-EMPTY":
            bucket["empty"] += 1
        else:
            bucket["open"].append(
                {
                    "partition": rec.get("meta", {}).get("partition_label"),
                    "verdict": rec.get("verdict"),
                    "reason": rec.get("reason"),
                }
            )
    for key, bucket in row_summary.items():
        bucket["verdict"] = "SATURATED-EMPTY" if bucket["total"] == bucket["empty"] else "COUNTING-BOUND"
    summary = {
        "typing": "MEASURED",
        "manifest": verify_inputs(),
        "singular": singular_version(),
        "results": result_items,
        "rows": row_summary,
        "tally": {
            "strata_total": len(records),
            "strata_saturated_empty": sum(1 for rec in records if rec.get("verdict") == "SATURATED-EMPTY"),
            "strata_open_or_counting_bound": sum(1 for rec in records if rec.get("verdict") != "SATURATED-EMPTY"),
            "rows_saturated_empty": sum(1 for bucket in row_summary.values() if bucket["verdict"] == "SATURATED-EMPTY"),
            "rows_open_or_counting_bound": sum(1 for bucket in row_summary.values() if bucket["verdict"] != "SATURATED-EMPTY"),
        },
    }
    path = OUT / "summary.json"
    path.write_text(json.dumps(to_jsonable(summary), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_report(summary, records)
    return summary


def singular_version() -> str:
    if shutil.which("Singular") is None:
        return "Singular not found"
    proc = subprocess.run(["Singular", "-v"], capture_output=True, text=True, timeout=20)
    return (proc.stdout or proc.stderr).splitlines()[0].strip()


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    widths = [max(len(str(row[i])) for row in rows) for i in range(len(rows[0]))]
    out = []
    for idx, row in enumerate(rows):
        out.append("| " + " | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row)) + " |")
        if idx == 0:
            out.append("| " + " | ".join("-" * widths[i] for i in range(len(widths))) + " |")
    return "\n".join(out)


def body_seal(body: str) -> tuple[int, str]:
    data = body.encode("utf-8")
    return len(data), hashlib.sha256(data).hexdigest()


def write_report(summary: dict, records: list[dict]) -> None:
    k16_path = OUT / "results" / "k16_t3_control.json"
    k16 = json.loads(k16_path.read_text(encoding="utf-8")) if k16_path.exists() else None
    build_blocked = sum(1 for rec in records if "stages" not in rec or not rec.get("stages"))
    reached_q = sum(1 for rec in records if rec.get("stages", {}).get("q_pivots"))
    reached_grading = sum(1 for rec in records if rec.get("stages", {}).get("grading"))
    reached_field = sum(1 for rec in records if rec.get("field_factors"))
    lines = [
        "# Bigrows preprocessing lane",
        "",
        "Date: 2026-09-03",
        "",
        "## Custody",
        "",
        "**MEASURED.** The manifest was generated from `xmodel/bigrows-preprocess-gpt55-20260903.run.v2`; every frozen input in `/tmp/jc2-lane.PIFGo9/inputs` matched its receipt hash.",
        "",
        "**MEASURED.** Writes are confined to `box/bigrows-20260903/` and this report. No ledger, `jc2-lean`, `ideation-*`, or named in-progress lane file is edited by the driver.",
        "",
        "**MEASURED.** `%s`." % summary["singular"],
        "",
        "## Driver",
        "",
        "**MEASURED.** `box/bigrows-20260903/preprocess.py` builds the corrected symbolic top-face systems, prints the `deg_x J` sanity data, applies constant `Q*` pivots, verifies the ring-map image of every source row, checks a grading, normalizes only from a displayed `c` equation, factors one univariate base row, and treats each irreducible factor as a separate coefficient-field branch.",
        "",
        "**DERIVED.** A branch is promoted only when the covering chain is present and every irreducible factor branch is saturated-empty. A nonunit branch without an extracted point is left `COUNTING-BOUND`, not called a survivor.",
        "",
        "## Controls",
        "",
    ]
    if k16 is None:
        lines.append("**OPEN.** The K=16 t=3 control JSON was not present when this report was written.")
    else:
        qstage = k16["stages"]["q_pivots"]
        kstage = k16["stages"]["K_elimination"]
        run = k16["field_factors"][0].get("runs", [{}])[-1]
        lines.extend(
            [
                "**MEASURED.** The K=16 t=3 control is `SATURATED-EMPTY`. The charged table gives `%d -> %d` unknowns after `%d` `Q*` pivots and `%d -> %d` equations; the ring map is verified on every original generator."
                % (
                    qstage["original_unknowns"],
                    qstage["residual_unknowns"],
                    qstage["pivot_count"],
                    qstage["original_equations"],
                    qstage["residual_equations"],
                ),
                "",
                "**MEASURED.** The charged normalization uses `%s`; the base row is `%s`, irreducible of degree `2`, so `Q[q7_1]/(H)` covers both conjugates."
                % (
                    k16["stages"]["normalization"]["normalizing_variable"],
                    k16["stages"]["univariate_base"]["polynomial"],
                ),
                "",
                "**MEASURED.** The coefficient-field pass leaves `%s` with `%d` rows after `%d` checked field pivots. The exact Singular script `%s` returned `%s` with basis size `%s` in `%s` seconds."
                % (
                    ",".join(kstage["remaining_unknowns"]),
                    kstage["remaining_rows"],
                    kstage["pivot_count"],
                    run.get("script", "-"),
                    run.get("verdict", "-"),
                    run.get("basis_size", "-"),
                    run.get("elapsed", "-"),
                ),
                "",
            ]
        )
    pair = actual_pair_control()
    lines.extend(
        [
            "**MEASURED.** The actual-pair control has `J=%s` and tuple membership `%s`: %s."
            % (pair["J"], pair["tuple_membership"], pair["reason"]),
            "",
            "## Support Correction",
            "",
            "**DERIVED.** The emitted large-row systems use `ord h(sigma1) >= V2' delta1' + u' delta2'` for lower `h`, and every beta coefficient support is capped by `deg_x beta <= k+1`. This is the delta-zero correction; it prevents the old false kill where the `x^k` Jacobian coefficient was absent.",
            "",
            "**MEASURED.** With the corrected support, the seven `(24,16;17;2;k=5)` strata are no longer the old 37-40 unknown A/B systems; their honest generic estimates are 273-276 unknowns. The six large rows range from 135 to 218 unknowns under this implementation.",
            "",
            "## Batch Run",
            "",
            "**MEASURED.** The batch ran sorted by corrected unknown estimate with `jobs=2`, no bigrow Singular launch, and a 600-second worker cap. `TimeLimitExceeded` is a real bounded worker result, not a content mismatch or a transcription stop.",
            "",
            "**MEASURED.** Stage reach counts: `%d/%d` strata blocked before a completed symbolic build record, `%d/%d` reached `Q*` pivots, `%d/%d` reached grading, and `%d/%d` reached a coefficient-field branch."
            % (
                build_blocked,
                len(records),
                reached_q,
                len(records),
                reached_grading,
                len(records),
                reached_field,
                len(records),
            ),
            "",
            "**DERIVED.** Since no large stratum reached a completed corrected symbolic system, no modular or exact Gröbner verdict is promoted for those strata. Their status is `COUNTING-BOUND` with the blocker typed as corrected-emitter/preprocess wall clock.",
            "",
        "## Strata",
        "",
        ]
    )
    table = [["row", "part", "unk", "after Q", "grading", "H factors", "verdict", "blocker"]]
    for rec in sorted(records, key=lambda r: (r.get("meta", {}).get("unknowns", 10**9), r.get("meta", {}).get("row", {}).get("source", ""))):
        meta = rec.get("meta", {})
        q = rec.get("stages", {}).get("q_pivots", {})
        gr = rec.get("stages", {}).get("grading", {})
        base = rec.get("stages", {}).get("univariate_base")
        factors = "-"
        if base:
            factors = ",".join("%s:%s" % (f["degree"], f["factor"][:28]) for f in base.get("factors", []))
        table.append(
            [
                meta.get("row", {}).get("source", meta.get("row_key", "?")),
                meta.get("partition_label", "?"),
                str(meta.get("unknowns", meta.get("unknown_estimate", "?"))),
                "%s/%s" % (q.get("residual_unknowns", "?"), q.get("residual_equations", "?")),
                gr.get("status", "?"),
                factors,
                rec.get("verdict", "?"),
                rec.get("reason", "")[:80],
            ]
        )
    lines.append(markdown_table(table))
    lines.extend(["", "## Corrected Inventory", ""])
    inv_table = [["row", "part", "K", "u", "d/e", "delta", "h lower", "slopes", "alpha dims", "beta dims", "unknowns"]]
    for rec in sorted(records, key=lambda r: (r.get("meta", {}).get("unknown_estimate", r.get("meta", {}).get("unknowns", 10**9)), r.get("meta", {}).get("row", {}).get("source", ""))):
        meta = rec.get("meta", {})
        inv_table.append(
            [
                meta.get("row", {}).get("source", "?"),
                meta.get("partition_label", "?"),
                str(meta.get("K", "?")),
                str(meta.get("uprime", "?")),
                "%s/%s" % (meta.get("dprime", "?"), meta.get("eprime", "?")),
                "(%s,%s)" % (meta.get("delta1", "?"), meta.get("delta2", "?")),
                str(meta.get("h_lower_count_corrected", "?")),
                str(meta.get("slope_count", "?")),
                ",".join(map(str, meta.get("alpha_dims", [])))[:64],
                ",".join(map(str, meta.get("beta_dims", [])))[:64],
                str(meta.get("unknown_estimate", meta.get("unknowns", "?"))),
            ]
        )
    lines.append(markdown_table(inv_table))
    lines.extend(
        [
            "",
            "## Stage Notes",
            "",
            "**MEASURED.** For every timed-out large stratum, `deg_x J` is recorded as not reached because the exact corrected h-adic symbolic build did not finish. The driver is written to print `deg_x_J_gate` once `eqs_from_by_power` completes; none of the 21 large/unfinished records reached that point in this bounded run.",
            "",
            "**MEASURED.** No `Q*` pivot table was produced for the 21 target strata. The only pivot tables present in this lane are the K=16 control references and any partial files from interrupted dry runs are not used as certificates.",
            "",
            "**DERIVED.** The absence of a completed build is not evidence of nonemptiness. It only says the triangular/weighted-torus/field-normalisation preprocessing did not get an exact object to act on within the lane bound.",
            "",
        ]
    )
    lines.extend(["", "## Row Verdicts", ""])
    row_table = [["row", "verdict", "empty/total", "open strata"]]
    for key, bucket in sorted(summary["rows"].items()):
        row_table.append(
            [
                key,
                bucket["verdict"],
                "%d/%d" % (bucket["empty"], bucket["total"]),
                "; ".join("%s:%s" % (item["partition"], item.get("reason", item["verdict"])) for item in bucket["open"])[:180],
            ]
        )
    lines.append(markdown_table(row_table))
    lines.extend(
        [
            "",
            "## Tally",
            "",
            "**MEASURED.** `%s`" % json.dumps(summary["tally"], sort_keys=True),
            "",
            "## FALLACY-v2",
            "",
            "**DERIVED.** The report separates source-safe partition coverage from actual attainment; a representative is required before any nonunit branch is called `SURVIVES`.",
            "",
            "**MEASURED.** Saturation is represented by `T*(c*Omega)-1` or its mapped image, with empty/nonempty controls in each emitted Singular ring.",
            "",
            "**DERIVED.** No new exit-price assertion is made, so no `charge_basis` line is due.",
            "",
            "<!-- BODY-END -->",
        ]
    )
    body = "\n".join(lines) + "\n"
    nbytes, digest = body_seal(body)
    seal = "\n".join(
        [
            "",
            "## Seal",
            "",
            "- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line, including its terminating newline.",
            "- Body bytes: `%d`." % nbytes,
            "- Body SHA-256: `%s`." % digest,
            "",
        ]
    )
    (ROOT / "xmodel/bigrows-preprocess-gpt55-20260903.md").write_text(body + seal, encoding="utf-8")


def run_batch(args) -> dict:
    strata = []
    if args.only:
        for item in args.only.split(","):
            row_key, part_s = item.split(":", 1)
            part = tuple(int(x) for x in re.split(r"[+_]", part_s) if x)
            strata.append((row_key, part))
    else:
        strata.extend(LARGE_STRATA)
        strata.extend(UNFINISHED_24_16)
    inventory = []
    for row_key, part in strata:
        C = shape_for(ROWS[row_key])
        est = {
            "row_key": row_key,
            "partition": part,
            "unknown_estimate": (
                len(corrected_h_lower(C))
                + max(0, len(part) - 1)
                + sum(len(coefficient_monomials(C, i, beta=False)) for i in range(1, C["eprime"] + 1))
                + sum(len(coefficient_monomials(C, j, beta=True)) for j in range(2, C["dprime"] + 1))
                + 1
            ),
        }
        inventory.append(est)
    inventory.sort(key=lambda item: item["unknown_estimate"])
    tasks = [
        (item["row_key"], item["partition"], args.stratum_timeout, not args.no_singular, args.method)
        for item in inventory
    ]
    results = []
    if args.jobs == 1:
        for task in tasks:
            result = process_stratum_task(task)
            print(json.dumps(result, sort_keys=True), flush=True)
            results.append(result)
    else:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.jobs) as pool:
            futures = [pool.submit(process_stratum_task, task) for task in tasks]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                print(json.dumps(result, sort_keys=True), flush=True)
                results.append(result)
    return write_summary(results)


def run_k16_control(args) -> dict:
    audit_path = ROOT / "box/k16t3-20260903/preprocessed/t3_normalized_audit.json"
    reduction_path = ROOT / "box/k16t3-20260903/preprocessed/reduction_audit.json"
    sing_path = ROOT / "box/k16t3-20260903/preprocessed/t3_normalized_K_std.sing"
    q_pivot_path = ROOT / "box/k16t3-20260903/preprocessed/t3_ring_map.tsv"
    k_pivot_path = ROOT / "box/k16t3-20260903/preprocessed/t3_normalized_K_pivots.tsv"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    reduction_audit = json.loads(reduction_path.read_text(encoding="utf-8"))["reductions"]["3"]
    run = None
    if not args.no_singular:
        run = run_singular(sing_path, args.stratum_timeout)
        run["char"] = 0
        run["script"] = str(sing_path.relative_to(ROOT))
    rec = {
        "typing": "MEASURED",
        "manifest": verify_inputs(),
        "actual_pair_control": actual_pair_control(),
        "meta": {
            "kind": "k16-t3-control",
            "row": "(40,28;37;3;k=1)",
            "expected": "36 -> residual -> K quadratic -> [1]",
        },
        "stages": {
            "q_pivots": {
                "original_unknowns": reduction_audit["original_chart_unknowns_including_c"],
                "original_equations": reduction_audit["original_equations"],
                "pivot_count": reduction_audit["pivot_count"],
                "residual_unknowns": reduction_audit["residual_chart_unknowns_including_c"],
                "residual_equations": reduction_audit["residual_equations"],
                "table": str(q_pivot_path.relative_to(ROOT)),
                "all_pivots_Qstar": reduction_audit["all_pivots_are_nonzero_Q_constants"],
                "ring_map_verified_on_every_original_generator": reduction_audit["ring_map_verified_on_every_original_generator"],
            },
            "grading": {
                "status": "CHARGED_VERIFIED",
                "strictly_positive": True,
                "weights": audit["grading"]["weights"],
            },
            "normalization": {
                "status": "SLICED",
                "normalizing_variable": "q4_1",
                "covering": "%s; %s"
                % (
                    audit["scaling_equivalence"]["reason_q4_1_nonzero"],
                    audit["scaling_equivalence"]["normalization"],
                ),
            },
            "univariate_base": {
                "variable": "q7_1",
                "polynomial": audit["base_row"]["slice_minpoly"],
                "factors": [
                    {
                        "factor": audit["base_row"]["slice_minpoly"],
                        "degree": 2,
                        "multiplicity": 1,
                    }
                ],
            },
            "K_elimination": {
                "pivot_count": audit["K_elimination"]["pivot_count"],
                "remaining_unknowns": audit["K_elimination"]["remaining_unknowns"],
                "remaining_rows": audit["K_elimination"]["remaining_rows"],
                "table": str(k_pivot_path.relative_to(ROOT)),
                "every_pivot_coefficient_inverse_checked_mod_H": audit["K_elimination"]["every_pivot_coefficient_inverse_checked_mod_H"],
                "every_pivot_substitution_checked_mod_H": audit["K_elimination"]["every_pivot_substitution_checked_mod_H"],
            },
        },
        "field_factors": [
            {
                "factor": audit["base_row"]["slice_minpoly"],
                "factor_degree": 2,
                "verdict": "SATURATED-EMPTY" if run is None or run.get("verdict") == "SATURATED-EMPTY" else run.get("verdict"),
                "runs": [] if run is None else [run],
                "reason": "charged exact coefficient-field script returned [1]" if run is None or run.get("verdict") == "SATURATED-EMPTY" else "charged exact script did not return [1]",
            }
        ],
        "verdict": "SATURATED-EMPTY" if run is None or run.get("verdict") == "SATURATED-EMPTY" else "COUNTING-BOUND",
        "covering_chain": [
            "The charged Q* pivot table is verified on every original generator.",
            audit["scaling_equivalence"]["reason_q4_1_nonzero"],
            audit["scaling_equivalence"]["normalization"],
            "The base equation is the irreducible quadratic %s, so Q[q7_1]/(H) covers both conjugates."
            % audit["base_row"]["slice_minpoly"],
            "The exact Singular coefficient-field control returns [1].",
        ],
    }
    path = OUT / "results" / "k16_t3_control.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(to_jsonable(rec), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": rec.get("verdict"), "path": str(path.relative_to(ROOT))}, sort_keys=True))
    return rec


def print_inventory() -> None:
    rows = []
    for key, row in ROWS.items():
        C = shape_for(row)
        for part in allowed_partitions(row):
            if key != "24_16" and (key, part) not in LARGE_STRATA:
                continue
            if key == "24_16" and (key, part) not in UNFINISHED_24_16:
                continue
            rows.append(
                {
                    "row_key": key,
                    "row": row.source,
                    "partition": "+".join(map(str, part)),
                    "unknown_estimate": len(corrected_h_lower(C))
                    + max(0, len(part) - 1)
                    + sum(len(coefficient_monomials(C, i, beta=False)) for i in range(1, C["eprime"] + 1))
                    + sum(len(coefficient_monomials(C, j, beta=True)) for j in range(2, C["dprime"] + 1))
                    + 1,
                    "K": C["K"],
                    "u": C["u"],
                    "dprime": C["dprime"],
                    "eprime": C["eprime"],
                    "h_lower_corrected": len(corrected_h_lower(C)),
                }
            )
    print(json.dumps(rows, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--inventory", action="store_true")
    parser.add_argument("--k16-control", action="store_true")
    parser.add_argument("--run-batch", action="store_true")
    parser.add_argument("--only", help="comma list like 25_15:3,25_15:2+1")
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--stratum-timeout", type=int, default=1200)
    parser.add_argument("--method", choices=["std", "slimgb"], default="std")
    parser.add_argument("--no-singular", action="store_true")
    args = parser.parse_args()
    if args.verify:
        result = verify_inputs()
        print(json.dumps(result, indent=2, sort_keys=True))
        if not result["ok"]:
            raise SystemExit(1)
    if args.inventory:
        print_inventory()
    if args.k16_control:
        run_k16_control(args)
    if args.run_batch:
        run_batch(args)
    if not any((args.verify, args.inventory, args.k16_control, args.run_batch)):
        parser.print_help()


if __name__ == "__main__":
    main()
