#!/usr/bin/env python3
"""Fast Singular-backed emitter for corrected two-point order charts.

Python enumerates the finite supports and writes a concrete Singular builder.
Singular performs the polynomial arithmetic: it constructs h, the coefficient
polynomials, the h-adic Jacobian remainders, and the coefficient rows.  Python
then assembles runnable standard-basis scripts and optional preprocessing
records.
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
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
INPUTS = Path(os.environ.get("LANE_INPUT_DIR", "/tmp/jc2-lane.wRUQfg/inputs"))
RECEIPT = ROOT / "xmodel/emitter-native-gpt55-20260903.run.v2"
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


ROWS: dict[str, RowSpec] = {
    "16_12": RowSpec("16_12", "(16,12;13;3;k=1)", 16, 12, 13, 3, 1),
    "28_20": RowSpec("28_20", "(28,20;25;3;k=1)", 28, 20, 25, 3, 1),
    "33_22": RowSpec("33_22", "(33,22;30;8;k=1)", 33, 22, 30, 8, 1),
    "25_15": RowSpec("25_15", "(25,15;21;2;k=2)", 25, 15, 21, 2, 2),
    "24_16": RowSpec("24_16", "(24,16;17;2;k=5)", 24, 16, 17, 2, 5),
}

UNFINISHED_24_16: list[tuple[int, ...]] = [
    (2, 2, 2),
    (4, 1, 1),
    (3, 2, 1),
    (3, 1, 1, 1),
    (2, 2, 1, 1),
    (2, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1),
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_inputs() -> dict:
    fields: dict[int, dict[str, str]] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        match = re.match(r"charged_input_(\d+)_(basename|sha256)=(.*)", line)
        if match:
            fields.setdefault(int(match.group(1)), {})[match.group(2)] = match.group(3)
    manifest = []
    for idx in sorted(fields):
        rec = fields[idx]
        path = INPUTS / rec["basename"]
        actual = sha256_file(path)
        manifest.append(
            {
                "index": idx,
                "basename": rec["basename"],
                "path": str(path),
                "expected_sha256": rec["sha256"],
                "actual_sha256": actual,
                "ok": actual == rec["sha256"],
            }
        )
    return {
        "receipt": str(RECEIPT),
        "inputs": str(INPUTS),
        "ok": bool(manifest) and all(item["ok"] for item in manifest),
        "manifest": manifest,
    }


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load %s" % path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def shape_module():
    return load_module(INPUTS / "shape.py", "emitter_frozen_shape")


def shape_for(row: RowSpec) -> dict:
    shape = shape_module()
    C = shape.shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    if not C.get("ok"):
        raise ValueError("shape failed for %s: %s" % (row.source, C.get("reason")))
    return C


def frac_s(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else "%d/%d" % (
        value.numerator,
        value.denominator,
    )


def parse_partition(value: str) -> tuple[int, ...]:
    part = tuple(int(v) for v in re.split(r"[+,]", value) if v)
    if not part or any(v <= 0 for v in part) or tuple(sorted(part, reverse=True)) != part:
        raise argparse.ArgumentTypeError("use a descending partition, e.g. 3 or 2+1")
    return part


def partitions(n: int, ceiling: int | None = None) -> Iterable[tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    top = n if ceiling is None else min(n, ceiling)
    for first in range(top, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def allowed_partitions(row: RowSpec) -> list[tuple[int, ...]]:
    C = shape_for(row)
    return [
        part
        for part in partitions(C["u"])
        if len(part) + 1 <= row.n - row.M2
    ]


def corrected_h_lower(C: dict) -> list[tuple[int, int]]:
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


def coefficient_monomials(C: dict, deficit: int, *, beta: bool = False) -> list[tuple[int, int]]:
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


def singular_power(base: str, exponent: int) -> str:
    if exponent == 0:
        return "1"
    if exponent == 1:
        return base
    return "%s^%d" % (base, exponent)


def xy_monomial(a: int, b: int) -> str:
    parts = []
    if a:
        parts.append(singular_power("x", a))
    if b:
        parts.append(singular_power("y", b))
    return "*".join(parts) if parts else "1"


def coeff_poly_terms(prefix: str, index: int | None, mons: Sequence[tuple[int, int]]) -> tuple[str, list[str]]:
    terms = []
    names = []
    for a, b in mons:
        if index is None:
            name = "%s_%d_%d" % (prefix, a, b)
        else:
            name = "%s%d_%d_%d" % (prefix, index, a, b)
        names.append(name)
        mon = xy_monomial(a, b)
        terms.append(name if mon == "1" else "%s*%s" % (name, mon))
    return (" + ".join(terms) if terms else "0"), names


def top_face_expr(row: RowSpec, part: Sequence[int], slope_prefix: str) -> tuple[str, list[str], str, str]:
    slopes = ["%s%d" % (slope_prefix, i) for i in range(2, len(part) + 1)]
    factors = ["(y-x)^%d" % part[0]]
    expr = "y^%d*(y-x)^%d" % (row.V2, part[0])
    omega_terms = []
    for slope, exponent in zip(slopes, part[1:]):
        expr += "*(y-%s*x)^%d" % (slope, exponent)
        factors.append("(y-%s*x)^%d" % (slope, exponent))
        omega_terms.extend([slope, "(%s-1)" % slope])
    for i, slope in enumerate(slopes):
        for other in slopes[i + 1 :]:
            omega_terms.append("(%s-%s)" % (slope, other))
    omega = "*".join(omega_terms) if omega_terms else "1"
    return expr, slopes, "y^%d*%s" % (row.V2, "*".join(factors)), omega


def clean_name(value: str) -> str:
    out = re.sub(r"[^A-Za-z0-9_]+", "_", value)
    out = re.sub(r"_+", "_", out).strip("_")
    if not out:
        out = "v"
    if out[0].isdigit():
        out = "v" + out
    return out


@dataclass
class BuildSpec:
    row: RowSpec
    chart: str
    partition: tuple[int, ...] | None
    stem: str
    variables: list[str]
    params_without_c: list[str]
    sat: str
    meta: dict
    builder_lines: list[str]


def k16_build_spec(row: RowSpec, *, beta_prefix: str) -> BuildSpec:
    C = shape_for(row)
    if not (C["K"] == 4 and C["u"] == 1 and C["V2"] == 3):
        raise ValueError("%s is not a K=16 u=1,V2=3 chart" % row.source)
    e = C["eprime"]
    q = C["dprime"]
    bu = C["V2"] * C["delta1"] + C["u"] * C["delta2"]
    cut_a = math.ceil(F(e, C["V2"]))
    cut_b = math.ceil(F(2 * e, C["V2"]))
    weighted = [
        ("1", F(0), "1"),
        ("A", cut_a * bu, "A"),
        ("B", cut_b * bu, "B"),
        ("z", e * bu, "z"),
        ("x", e * bu, "x"),
    ]

    def space(i: int) -> list[str]:
        threshold = i * bu
        return [poly for poly, weight, _name in weighted if weight >= threshold]

    alpha_spaces = {i: list(space(i)) for i in range(1, e + 1)}
    beta_spaces = {i: list(space(i)) for i in range(2, q + 1)}
    gauges = []
    shear = e - q
    if 1 <= shear <= e and alpha_spaces.get(shear) == ["1"]:
        safe_shear = True
        for i, bspace in beta_spaces.items():
            target = alpha_spaces.get(i + shear, [])
            if not all(base in target for base in bspace):
                safe_shear = False
                break
        if safe_shear:
            alpha_spaces[shear] = []
            gauges.append("P -> P - alpha_%d Q" % shear)
    if q in beta_spaces and "1" in beta_spaces[q]:
        beta_spaces[q] = [base for base in beta_spaces[q] if base != "1"]
        gauges.append("Q -> Q - const(beta_%d)" % q)
    if e in alpha_spaces and "1" in alpha_spaces[e]:
        alpha_spaces[e] = [base for base in alpha_spaces[e] if base != "1"]
        gauges.append("P -> P - const(alpha_%d)" % e)

    params = ["b1", "b2", "b3", "b4"]
    lines = [
        "poly z = y - x;",
        "poly B = y*z + b1*y + b2;",
        "poly A = y*B + b3;",
        "poly h = y*A + b4;",
    ]
    alpha_dims = []
    beta_dims = []
    for i in range(1, e + 1):
        terms = []
        for j, base in enumerate(alpha_spaces[i]):
            name = "a%d_%d" % (i, j)
            params.append(name)
            terms.append(name if base == "1" else "%s*(%s)" % (name, base))
        lines.append("poly AA%d = %s;" % (i, " + ".join(terms) if terms else "0"))
        alpha_dims.append(len(alpha_spaces[i]))
    for i in range(2, q + 1):
        terms = []
        for j, base in enumerate(beta_spaces[i]):
            name = "%s%d_%d" % (beta_prefix, i, j)
            params.append(name)
            terms.append(name if base == "1" else "%s*(%s)" % (name, base))
        lines.append("poly BB%d = %s;" % (i, " + ".join(terms) if terms else "0"))
        beta_dims.append(len(beta_spaces[i]))

    low_terms = [("1", q)] + [("BB%d" % i, q - i) for i in range(2, q + 1)]
    high_terms = [("1", e)] + [("AA%d" % i, e - i) for i in range(1, e + 1)]
    stem = "k16_%s_%s" % (row.key, beta_prefix)
    meta = {
        "typing": "DERIVED",
        "chart": "k16_hadic_order_native",
        "row": asdict(row),
        "partition": None,
        "partition_label": None,
        "K": C["K"],
        "uprime": C["u"],
        "dprime": q,
        "eprime": e,
        "delta1": frac_s(C["delta1"]),
        "delta2": frac_s(C["delta2"]),
        "bound_h": frac_s(bu),
        "support_rule": "K16 flag basis; h-adic Jacobian arithmetic in Singular",
        "h_lower_count_corrected": 4,
        "slope_count": 0,
        "alpha_dims": alpha_dims,
        "beta_dims": beta_dims,
        "gauges": gauges,
        "omega": "1",
        "saturation_factor": "c",
    }
    return finalize_spec(row, "k16", None, stem, params, "c", meta, lines, low_terms, high_terms)


def generic_build_spec(row: RowSpec, part: Sequence[int]) -> BuildSpec:
    C = shape_for(row)
    if tuple(part) not in allowed_partitions(row):
        raise ValueError("%s partition %s outside Prop. 4.6 cap" % (row.source, part))
    h_lower = corrected_h_lower(C)
    top, slopes, top_factored, omega = top_face_expr(row, part, "s")
    h_terms, h_params = coeff_poly_terms("h0", None, h_lower)
    params = h_params + slopes
    lines = ["poly h = (%s) + (%s);" % (top, h_terms)]
    alpha_dims = []
    beta_dims = []
    e = C["eprime"]
    q = C["dprime"]
    for i in range(1, e + 1):
        mons = coefficient_monomials(C, i, beta=False)
        expr, names = coeff_poly_terms("A", i, mons)
        params.extend(names)
        lines.append("poly AA%d = %s;" % (i, expr))
        alpha_dims.append(len(mons))
    for j in range(2, q + 1):
        mons = coefficient_monomials(C, j, beta=True)
        expr, names = coeff_poly_terms("B", j, mons)
        params.extend(names)
        lines.append("poly BB%d = %s;" % (j, expr))
        beta_dims.append(len(mons))
    low_terms = [("1", q)] + [("BB%d" % j, q - j) for j in range(2, q + 1)]
    high_terms = [("1", e)] + [("AA%d" % i, e - i) for i in range(1, e + 1)]
    stem = "%s_part_%s_generic" % (row.key, "_".join(map(str, part)))
    bu = C["V2"] * C["delta1"] + C["u"] * C["delta2"]
    meta = {
        "typing": "DERIVED",
        "chart": "topface_generic_native",
        "row": asdict(row),
        "partition": list(part),
        "partition_label": "+".join(map(str, part)),
        "top_face_factored": top_factored,
        "K": C["K"],
        "uprime": C["u"],
        "dprime": q,
        "eprime": e,
        "delta1": frac_s(C["delta1"]),
        "delta2": frac_s(C["delta2"]),
        "bound_h": frac_s(bu),
        "support_rule": "ord h(sigma1)>=V2*delta1+u*delta2; beta x-degree<=k+1",
        "h_lower_count_corrected": len(h_lower),
        "slope_count": len(slopes),
        "alpha_dims": alpha_dims,
        "beta_dims": beta_dims,
        "omega": omega,
        "saturation_factor": "c*(%s)" % omega if omega != "1" else "c",
        "compute_direct_j": False,
        "division_mode": "singular_lead_y",
        "coefficient_mode": "hadic_normal_form",
        "coefficient_ring_params": True,
    }
    return finalize_spec(row, "generic", tuple(part), stem, params, meta["saturation_factor"], meta, lines, low_terms, high_terms)


def ab_build_spec(row: RowSpec, part: Sequence[int]) -> BuildSpec:
    C = shape_for(row)
    if not (C["dprime"] == 2 and C["eprime"] == 3):
        raise ValueError("%s is not a d'=2,e'=3 A/B chart" % row.source)
    if tuple(part) not in allowed_partitions(row):
        raise ValueError("%s partition %s outside Prop. 4.6 cap" % (row.source, part))
    top, slopes, top_factored, omega = top_face_expr(row, part, "a")
    h_lower = list(C["h_lower"])
    h_terms, h_params = coeff_poly_terms("h", None, h_lower)
    params = h_params + slopes + ["bp", "bq", "br", "bs"]
    lines = [
        "poly h = (%s) + (%s);" % (top, h_terms),
        "poly h0 = subst(h, y, 0);",
        "poly Aab = (h - h0) div y;",
        "poly beta = bp*Aab + bq*y + br*x + bs;",
        "list AD = native_y_div(beta^2, h, %d, WY);" % C["K"],
        "poly alpha = AD[1];",
    ]
    low_terms = [("1", 2), ("2*beta", 0)]
    high_terms = [("1", 3), ("3*beta", 1), ("(3/2)*alpha", 0)]
    stem = "%s_part_%s_ab" % (row.key, "_".join(map(str, part)))
    meta = {
        "typing": "DERIVED",
        "chart": "d2e3_ab_native",
        "row": asdict(row),
        "partition": list(part),
        "partition_label": "+".join(map(str, part)),
        "top_face_factored": top_factored,
        "K": C["K"],
        "uprime": C["u"],
        "dprime": 2,
        "eprime": 3,
        "delta1": frac_s(C["delta1"]),
        "delta2": frac_s(C["delta2"]),
        "support_rule": "A/B ansatz with source-safe top-face partition",
        "h_lower_count_corrected": len(h_lower),
        "slope_count": len(slopes),
        "alpha_dims": [],
        "beta_dims": [],
        "omega": omega,
        "saturation_factor": "c*(%s)" % omega if omega != "1" else "c",
        "compute_direct_j": True,
        "division_mode": "explicit_univariate_y",
        "coefficient_mode": "hadic_normal_form",
    }
    return finalize_spec(row, "ab", tuple(part), stem, params, meta["saturation_factor"], meta, lines, low_terms, high_terms)


def finalize_spec(
    row: RowSpec,
    chart: str,
    part: tuple[int, ...] | None,
    stem: str,
    params_without_c: list[str],
    sat: str,
    meta: dict,
    setup_lines: list[str],
    low_terms: Sequence[tuple[str, int]],
    high_terms: Sequence[tuple[str, int]],
) -> BuildSpec:
    variables = params_without_c + ["c"]
    meta["unknowns"] = len(variables)
    meta["unknowns_excluding_c"] = len(params_without_c)
    meta["native_low_terms"] = [{"coefficient": c, "h_power": p} for c, p in low_terms]
    meta["native_high_terms"] = [{"coefficient": c, "h_power": p} for c, p in high_terms]
    lines = list(setup_lines)
    if meta.get("coefficient_mode") == "direct_xy":
        def direct_sum(terms: Sequence[tuple[str, int]]) -> str:
            pieces = []
            for coeff, power in terms:
                if power == 0:
                    pieces.append("(%s)" % coeff)
                elif coeff == "1":
                    pieces.append("h^%d" % power)
                else:
                    pieces.append("(%s)*h^%d" % (coeff, power))
            return " + ".join(pieces) if pieces else "0"

        lines.append("poly Fpoly = %s;" % direct_sum(low_terms))
        lines.append("poly Gpoly = %s;" % direct_sum(high_terms))
        lines.append("poly JD = diff(Fpoly,x)*diff(Gpoly,y) - diff(Fpoly,y)*diff(Gpoly,x);")
        lines.append("poly level0_before = JD;")
        lines.append("poly target_xk = native_coeff_xy(level0_before, %d, 0, WX, WY);" % row.k)
        lines.append("int direct_deg_x = deg(JD, WX);")
        lines.append("int level0_deg_x = direct_deg_x;")
        lines.append("JD = JD - c*x^%d;" % row.k)
        lines.append("native_append_coeffs(JD, 0, rowsfile, WX, WY);")
        lines.append('print("NATIVE_GATE direct_deg_x=" + string(direct_deg_x));')
        lines.append('print("NATIVE_GATE level0_deg_x_before_minus_c=" + string(level0_deg_x));')
        lines.append('if (target_xk != 0) { print("NATIVE_GATE target_xk_level0_nonzero=1"); }'
                     ' else { print("NATIVE_GATE target_xk_level0_nonzero=0"); }')
        lines.append('print("NATIVE_DONE equations=" + string(source_idx));')
        lines.append('print("NATIVE_DONE max_nf_deg_x_after_minus_c=" + string(max_nf_deg));')
        return BuildSpec(row, chart, part, stem, variables, params_without_c, sat, meta, lines)

    max_initial = max([r + s for _a, r in low_terms for _b, s in high_terms] + [0])
    level_cap = max_initial + 2 * int(meta.get("K", 1)) + 12
    for level in range(level_cap + 1):
        lines.append("poly H%d = 0;" % level)
    lines.append("poly tmpSame;")
    lines.append("poly tmpLower;")
    for aa, r in low_terms:
        for bb, s in high_terms:
            lines.append(
                "tmpSame = diff((%s),x)*diff((%s),y) - diff((%s),y)*diff((%s),x);"
                % (aa, bb, aa, bb)
            )
            lines.append("if (tmpSame != 0) { H%d = H%d + tmpSame; }" % (r + s, r + s))
            if r + s - 1 >= 0 and (r != 0 or s != 0):
                lines.append(
                    "tmpLower = (%d)*(%s)*(diff((%s),x)*diff(h,y)-diff((%s),y)*diff(h,x))"
                    " + (%d)*(%s)*(diff(h,x)*diff((%s),y)-diff(h,y)*diff((%s),x));"
                    % (s, bb, aa, aa, r, aa, bb, bb)
                )
                lines.append("if (tmpLower != 0) { H%d = H%d + tmpLower; }" % (r + s - 1, r + s - 1))
    for level in range(level_cap):
        lines.append("if (H%d != 0) {" % level)
        if meta.get("division_mode") == "singular_lead_y":
            lines.append("  list LD%d = division(H%d, ideal(h));" % (level, level))
            lines.append("  H%d = LD%d[2][1];" % (level, level))
            lines.append("  vector LQ%d = LD%d[1][1];" % (level, level))
            lines.append("  if (LQ%d[1] != 0) { H%d = H%d + LQ%d[1]; }" % (level, level + 1, level + 1, level))
        else:
            lines.append("  list LD%d = native_y_div(H%d, h, %d, WY);" % (level, level, int(meta.get("K", 1))))
            lines.append("  H%d = LD%d[2];" % (level, level))
            lines.append("  if (LD%d[1] != 0) { H%d = H%d + LD%d[1]; }" % (level, level + 1, level + 1, level))
        lines.append("}")
    lines.append("poly level0_before = H0;")
    lines.append("poly target_xk = native_coeff_xy(level0_before, %d, 0, WX, WY);" % row.k)
    if meta.get("compute_direct_j", True):
        lines.append("poly JD = 0;")
        for level in range(level_cap + 1):
            lines.append("if (H%d != 0) { JD = JD + H%d*h^%d; }" % (level, level, level))
        lines.append("int direct_deg_x = deg(JD, WX);")
    else:
        lines.append("int direct_deg_x = -2;")
    lines.append("int level0_deg_x = deg(level0_before, WX);")
    lines.append("H0 = H0 - c*x^%d;" % row.k)
    for level in range(level_cap + 1):
        lines.append("native_append_coeffs(H%d, %d, rowsfile, WX, WY);" % (level, level))
    lines.append('print("NATIVE_GATE direct_deg_x=" + string(direct_deg_x));')
    lines.append('print("NATIVE_GATE level0_deg_x_before_minus_c=" + string(level0_deg_x));')
    lines.append('if (target_xk != 0) { print("NATIVE_GATE target_xk_level0_nonzero=1"); }'
                 ' else { print("NATIVE_GATE target_xk_level0_nonzero=0"); }')
    lines.append('print("NATIVE_DONE equations=" + string(source_idx));')
    lines.append('print("NATIVE_DONE max_nf_deg_x_after_minus_c=" + string(max_nf_deg));')
    return BuildSpec(row, chart, part, stem, variables, params_without_c, sat, meta, lines)


def write_builder(spec: BuildSpec, builder_path: Path, rows_path: Path) -> None:
    if spec.meta.get("coefficient_ring_params"):
        nvars = 2
        wx = ["0", "1"]
        wy = ["1", "0"]
        ring_line = "ring R=(0,%s),(y,x),dp;" % ",".join(spec.variables)
    else:
        nvars = 2 + len(spec.variables)
        wx = ["0"] * nvars
        wy = ["0"] * nvars
        wy[0] = "1"
        wx[1] = "1"
        ring_vars = ["y", "x"] + spec.variables
        ring_line = "ring R=0,(%s),dp;" % ",".join(ring_vars)
    lines = [
        "// generated by emit_chart.py; polynomial arithmetic is executed by Singular",
        ring_line,
        "option(redSB);",
        "execute(read(\"%s\"));" % str((OUT / "emit_chart.sing").resolve()),
        "string rowsfile = \"%s\";" % str(rows_path.resolve()),
        "write(\":w \" + rowsfile, \"source_index|h_power|x_power|y_power|expr\");",
        "int source_idx = 0;",
        "int max_nf_deg = -1;",
        "intvec WY = %s;" % ",".join(wy),
        "intvec WX = %s;" % ",".join(wx),
    ]
    lines.extend(spec.builder_lines)
    lines.append("quit;")
    builder_path.parent.mkdir(parents=True, exist_ok=True)
    rows_path.parent.mkdir(parents=True, exist_ok=True)
    builder_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_native_stdout(stdout: str) -> dict:
    data: dict[str, int | str | bool] = {}
    for line in stdout.splitlines():
        if line.startswith("NATIVE_GATE ") or line.startswith("NATIVE_DONE "):
            _head, rest = line.split(" ", 1)
            if "=" in rest:
                key, value = rest.split("=", 1)
                try:
                    data[key] = int(value)
                except ValueError:
                    data[key] = value
    if "target_xk_level0_nonzero" in data:
        data["target_xk_level0_nonzero"] = bool(data["target_xk_level0_nonzero"])
    return data


def iter_rows(rows_path: Path):
    with rows_path.open("r", encoding="utf-8") as handle:
        header = next(handle, None)
        if header is None:
            return
        for line in handle:
            line = line.rstrip("\n")
            if not line:
                continue
            source, hpow, xp, yp, expr = line.split("|", 4)
            yield {
                "source_index": int(source),
                "h_power": int(hpow),
                "monomial": [int(xp), int(yp)],
                "expr": expr,
            }


def read_rows(rows_path: Path) -> list[dict]:
    return list(iter_rows(rows_path))


def row_file_stats(rows_path: Path) -> dict:
    digest = hashlib.sha256()
    row_count = 0
    byte_count = 0
    with rows_path.open("rb") as handle:
        header = handle.readline()
        digest.update(header)
        byte_count += len(header)
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
            byte_count += len(block)
            row_count += block.count(b"\n")
    return {"rows_sha256": digest.hexdigest(), "rows_bytes": byte_count, "rows_count": row_count}


def _write_ideal(handle, equations: Iterable[str], sat: str, T: str) -> None:
    handle.write("ideal I=")
    first = True
    for eq in equations:
        if first:
            first = False
        else:
            handle.write(",\n")
        handle.write(eq)
    if not first:
        handle.write(",\n")
    handle.write("%s*(%s)-1;\n" % (T, sat))


def write_system_script(path: Path, variables: Sequence[str], equations: Iterable[str], sat: str, char: int, meta: dict) -> None:
    T = "T"
    all_vars = list(variables) + [T]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        handle.write("// generated by emit_chart.py from Singular-emitted coefficient rows\n")
        handle.write("// row %s chart %s\n" % (meta["row"]["source"], meta["chart"]))
        if meta.get("partition_label"):
            handle.write("// partition %s top %s\n" % (meta["partition_label"], meta.get("top_face_factored", "")))
        gate = meta.get("deg_x_J_gate", {})
        if gate:
            handle.write(
                "// deg_x_J_gate direct=%s level0=%s target_xk_nonzero=%s normal_form_max=%s\n"
                % (
                    gate.get("direct_deg_x"),
                    gate.get("level0_deg_x_before_minus_c"),
                    gate.get("target_xk_level0_nonzero"),
                    gate.get("max_nf_deg_x_after_minus_c"),
                )
            )
        handle.write("ring R=%d,(%s),dp;\n" % (char, ",".join(all_vars)))
        handle.write("option(redSB);\n")
        handle.write('if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); } else { print("CONTROL_RING_FAIL"); }\n')
        handle.write('print("CONTROL_EMPTY_START");\n')
        handle.write("ideal CE=(%s),%s*(%s)-1;\n" % (sat, T, sat))
        handle.write("ideal GE=std(CE);\n")
        handle.write(
            'if (typeof(GE)=="ideal" && nameof(basering)=="R") { print("CONTROL_EMPTY_EXTRACT_RING_PASS"); }'
            ' else { print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }\n'
        )
        handle.write('if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }\n')
        handle.write('print("CONTROL_NONEMPTY_START");\n')
        handle.write("ideal CN=(%s)-1,%s*(%s)-1;\n" % (sat, T, sat))
        handle.write("ideal GN=std(CN);\n")
        handle.write(
            'if (typeof(GN)=="ideal" && nameof(basering)=="R") { print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); }'
            ' else { print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }\n'
        )
        handle.write('if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }\n')
        handle.write('print("MAIN_START equations=%d unknowns=%d char=%d");\n' % (meta["equations"], len(variables), char))
        _write_ideal(handle, equations, sat, T)
        handle.write("ideal G=std(I);\n")
        handle.write('print("MAIN_DONE basis_size=");\n')
        handle.write("size(G);\n")
        handle.write('if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_NONTRIVIAL"); }\n')
        handle.write("quit;\n")


def emit(spec: BuildSpec, *, timeout: int) -> dict:
    if shutil.which("Singular") is None:
        raise RuntimeError("Singular not found")
    stem = spec.stem
    build_dir = OUT / "build"
    rows_dir = OUT / "rows"
    systems_dir = OUT / "systems"
    meta_dir = OUT / "meta"
    builder_path = build_dir / (stem + "_build.sing")
    rows_path = rows_dir / (stem + "_rows.tsv")
    write_builder(spec, builder_path, rows_path)
    started = time.time()
    try:
        proc = subprocess.run(
            ["Singular", "-q", "--no-rc", str(builder_path)],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        elapsed = time.time() - started
    except subprocess.TimeoutExpired as exc:
        out = (exc.stdout or "") if isinstance(exc.stdout, str) else (exc.stdout or b"").decode("utf-8", "ignore")
        err = (exc.stderr or "") if isinstance(exc.stderr, str) else (exc.stderr or b"").decode("utf-8", "ignore")
        meta = dict(spec.meta)
        meta.update(
            {
                "emit_status": "TIMEOUT",
                "emit_elapsed": round(time.time() - started, 3),
                "emit_timeout": timeout,
                "stdout_tail": out[-1600:],
                "stderr_tail": err[-1600:],
            }
        )
        return {"meta": meta, "paths": {"builder": str(builder_path), "rows": str(rows_path)}}
    stdout = (proc.stdout or "") + (proc.stderr or "")
    gate = parse_native_stdout(stdout)
    rows = read_rows(rows_path) if rows_path.is_file() else []
    equations = [row["expr"] for row in rows]
    row_stats = row_file_stats(rows_path) if rows_path.is_file() else {"rows_sha256": None, "rows_bytes": 0, "rows_count": 0}
    meta = dict(spec.meta)
    meta.update(
        {
            "typing": "MEASURED",
            "emit_status": "OK" if proc.returncode == 0 else "ERROR",
            "emit_elapsed": round(elapsed, 3),
            "emit_rc": proc.returncode,
            "equations": len(rows),
            "deg_x_J_gate": {
                "direct_deg_x": None if gate.get("direct_deg_x") == -2 else gate.get("direct_deg_x"),
                "direct_deg_x_status": "SKIPPED_FOR_GENERIC_EMIT" if gate.get("direct_deg_x") == -2 else "MEASURED",
                "level0_deg_x_before_minus_c": gate.get("level0_deg_x_before_minus_c"),
                "target_xk_level0_nonzero": gate.get("target_xk_level0_nonzero"),
                "max_nf_deg_x_after_minus_c": gate.get("max_nf_deg_x_after_minus_c"),
            },
            "builder_stdout_tail": stdout[-1600:],
        }
    )
    meta_dir.mkdir(parents=True, exist_ok=True)
    meta_path = meta_dir / (stem + ".json")
    record = {
        "manifest": verify_inputs(),
        "meta": meta,
        "variables": spec.variables,
        "params_without_c": spec.params_without_c,
        "sat": spec.sat,
        "rows_path": str(rows_path.relative_to(ROOT)),
        "row_file": row_stats,
        "builder": str(builder_path.relative_to(ROOT)),
        "systems": {},
    }
    for char in (0,) + PRIMES:
        suffix = "Q" if char == 0 else "p%d" % char
        system_path = systems_dir / ("%s_%s.sing" % (stem, suffix))
        write_system_script(system_path, spec.variables, equations, spec.sat, char, meta)
        record["systems"][str(char)] = str(system_path.relative_to(ROOT))
    meta_path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return record


def parse_singular_output(output: str) -> dict:
    def after(label: str) -> str | None:
        lines = output.splitlines()
        for i, line in enumerate(lines):
            if line.strip() == label and i + 1 < len(lines):
                return lines[i + 1].strip()
        return None

    if "MAIN_SATURATED_EMPTY" in output:
        verdict = "SATURATED-EMPTY"
    elif "MAIN_NONTRIVIAL" in output:
        verdict = "SURVIVES"
    elif "error occurred" in output or "?" in output:
        verdict = "ERROR"
    else:
        verdict = "ERROR"
    return {
        "verdict": verdict,
        "basis_size": after("MAIN_DONE basis_size="),
        "control_ring_pass": "CONTROL_RING_PASS R" in output,
        "control_empty_pass": "CONTROL_EMPTY_PASS" in output,
        "control_nonempty_pass": "CONTROL_NONEMPTY_PASS" in output,
    }


def run_singular(path: Path, timeout: int) -> dict:
    started = time.time()
    out_path = path.with_suffix(path.suffix + ".out")
    err_path = path.with_suffix(path.suffix + ".err")
    try:
        proc = subprocess.run(
            ["Singular", "-q", "--no-rc", str(path)],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = (exc.stdout or "") if isinstance(exc.stdout, str) else (exc.stdout or b"").decode("utf-8", "ignore")
        stderr = (exc.stderr or "") if isinstance(exc.stderr, str) else (exc.stderr or b"").decode("utf-8", "ignore")
        out_path.write_text(stdout, encoding="utf-8")
        err_path.write_text(stderr, encoding="utf-8")
        return {
            "verdict": "TIMEOUT",
            "elapsed": round(time.time() - started, 3),
            "timeout": timeout,
            "stdout_tail": stdout[-1600:],
            "stderr_tail": stderr[-1600:],
            "out": str(out_path.relative_to(ROOT)),
            "err": str(err_path.relative_to(ROOT)),
        }
    stdout = proc.stdout or ""
    stderr = proc.stderr or ""
    out_path.write_text(stdout, encoding="utf-8")
    err_path.write_text(stderr, encoding="utf-8")
    parsed = parse_singular_output(stdout + stderr)
    parsed.update(
        {
            "elapsed": round(time.time() - started, 3),
            "rc": proc.returncode,
            "stdout_tail": (stdout + stderr)[-1600:],
            "out": str(out_path.relative_to(ROOT)),
            "err": str(err_path.relative_to(ROOT)),
        }
    )
    return parsed


def run_modular(record: dict, *, timeout: int, jobs: int) -> dict:
    systems = record["systems"]
    results = []

    def one(char: int) -> dict:
        path = ROOT / systems[str(char)]
        item = run_singular(path, timeout)
        item["char"] = char
        item["script"] = systems[str(char)]
        return item

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, min(jobs, len(PRIMES)))) as pool:
        futures = {pool.submit(one, prime): prime for prime in PRIMES}
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda item: item["char"])
    return {"modular": results}


def system_parts(path: Path) -> tuple[list[str], str]:
    text = path.read_text(encoding="utf-8")
    rings = re.findall(r"ring R=[^,]+,\((.*?)\),dp;", text)
    if not rings:
        raise ValueError("no ring R line in %s" % path)
    match = re.search(r"\nideal I=(.*?);\nideal G=std\(I\);", text, re.S)
    if not match:
        raise ValueError("no main ideal in %s" % path)
    return [v.strip() for v in rings[-1].split(",")], match.group(1).strip()


def compare_systems(native: Path, baseline: Path, outpath: Path, timeout: int = 600) -> dict:
    native_vars, native_ideal = system_parts(native)
    base_vars, base_ideal = system_parts(baseline)
    if native_vars != base_vars:
        return {
            "verdict": "ERROR",
            "reason": "variable order differs",
            "native_variables": native_vars,
            "baseline_variables": base_vars,
        }
    lines = [
        "// mutual normal-form ideal comparison generated by emit_chart.py",
        "ring R=0,(%s),dp;" % ",".join(native_vars),
        "option(redSB);",
        "ideal INA=%s;" % native_ideal,
        "ideal IBA=%s;" % base_ideal,
        "ideal GN=std(INA);",
        "ideal GB=std(IBA);",
        "int okNB=1;",
        "int okBN=1;",
        "int i;",
        "for (i=1; i<=size(INA); i++) { if (reduce(INA[i],GB) != 0) { okNB=0; } }",
        "for (i=1; i<=size(IBA); i++) { if (reduce(IBA[i],GN) != 0) { okBN=0; } }",
        'if (okNB==1 && okBN==1) { print("COMPARE_PASS"); } else { print("COMPARE_FAIL"); }',
        'print("COMPARE_NATIVE_BASIS_SIZE");',
        "size(GN);",
        'print("COMPARE_BASELINE_BASIS_SIZE");',
        "size(GB);",
        "quit;",
    ]
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text("\n".join(lines) + "\n", encoding="utf-8")
    rr = run_singular(outpath, timeout)
    output = (ROOT / rr["out"]).read_text(encoding="utf-8") + (ROOT / rr["err"]).read_text(encoding="utf-8")
    if "?" in output or "error occurred" in output:
        rr["verdict"] = "ERROR"
    else:
        rr["verdict"] = "PASS" if "COMPARE_PASS" in output else "FAIL"
    rr["native"] = str(native.relative_to(ROOT))
    rr["baseline"] = str(baseline.relative_to(ROOT))
    rr["compare_script"] = str(outpath.relative_to(ROOT))
    return rr


def parse_native_for_preprocess(record: dict):
    import sympy as sp
    from sympy.parsing.sympy_parser import parse_expr

    pre = load_module(INPUTS / "preprocess.py", "emitter_frozen_preprocess")
    pre.OUT = OUT
    pre.ROOT = ROOT
    pre.INPUTS = INPUTS
    pre.RECEIPT = RECEIPT
    symbols = {name: sp.Symbol(name) for name in record["variables"]}
    rows = []
    row_source = record.get("rows")
    if row_source is None:
        row_source = iter_rows(ROOT / record["rows_path"])
    for item in row_source:
        expr_text = item["expr"].replace("^", "**")
        expr = parse_expr(expr_text, local_dict=symbols, evaluate=True)
        rows.append(
            pre.TaggedRow(
                item["source_index"],
                item["h_power"],
                tuple(item["monomial"]),
                sp.expand(expr),
            )
        )
    variables = [symbols[name] for name in record["params_without_c"]]
    c = symbols["c"]
    return pre, {
        "meta": record["meta"],
        "params": variables,
        "rows": rows,
        "c": c,
        "sat": parse_expr(record["sat"].replace("^", "**"), local_dict=symbols, evaluate=True),
    }


def run_preprocess(record: dict, *, timeout: int, run_singular_flag: bool = True) -> dict:
    pre, system = parse_native_for_preprocess(record)
    stem = record["meta"]["chart"] + "_" + record["meta"]["row"]["key"]
    if record["meta"].get("partition_label"):
        stem += "_part_" + "_".join(map(str, record["meta"]["partition"]))
    return pre.process_system(
        system,
        clean_name(stem),
        per_stratum_timeout=timeout,
        run_singular_flag=run_singular_flag,
        method="std",
    )


def spec_from_args(args: argparse.Namespace) -> BuildSpec:
    row = ROWS[args.row]
    if args.chart == "k16":
        return k16_build_spec(row, beta_prefix=args.beta_prefix)
    part = args.partition
    if part is None:
        raise SystemExit("--partition is required for generic/ab charts")
    if args.chart == "generic":
        return generic_build_spec(row, part)
    if args.chart == "ab":
        return ab_build_spec(row, part)
    raise SystemExit("unknown chart %s" % args.chart)


def cmd_emit(args: argparse.Namespace) -> None:
    checked = verify_inputs()
    if not checked["ok"]:
        raise SystemExit("frozen input mismatch")
    spec = spec_from_args(args)
    record = emit(spec, timeout=args.emit_timeout)
    print(json.dumps(record, indent=2, sort_keys=True))


def cmd_run(args: argparse.Namespace) -> None:
    checked = verify_inputs()
    if not checked["ok"]:
        raise SystemExit("frozen input mismatch")
    spec = spec_from_args(args)
    record = emit(spec, timeout=args.emit_timeout)
    if record["meta"].get("emit_status") != "OK":
        print(json.dumps(record, indent=2, sort_keys=True))
        return
    record.update(run_modular(record, timeout=args.mod_timeout, jobs=args.jobs))
    pre_started = time.time()
    try:
        record["preprocess"] = run_preprocess(record, timeout=args.pre_timeout, run_singular_flag=True)
    except Exception as exc:
        record["preprocess"] = {
            "verdict": "COUNTING-BOUND",
            "reason": "native rows could not complete preprocessing: %s: %s" % (type(exc).__name__, exc),
        }
    record["preprocess_elapsed_outer"] = round(time.time() - pre_started, 3)
    outpath = OUT / "results" / (spec.stem + "_run.json")
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(record, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True, default=str))
    print("result:", outpath.relative_to(ROOT))


def cmd_preprocess_meta(args: argparse.Namespace) -> None:
    checked = verify_inputs()
    if not checked["ok"]:
        raise SystemExit("frozen input mismatch")
    record = json.loads(Path(args.meta).read_text(encoding="utf-8"))
    started = time.time()
    try:
        result = run_preprocess(record, timeout=args.pre_timeout, run_singular_flag=not args.no_exact)
    except Exception as exc:
        result = {
            "verdict": "COUNTING-BOUND",
            "reason": "native rows could not complete preprocessing: %s: %s" % (type(exc).__name__, exc),
        }
    result["outer_elapsed"] = round(time.time() - started, 3)
    outpath = OUT / "results" / (Path(args.meta).stem + "_preprocess.json")
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(result, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    print("result:", outpath.relative_to(ROOT))


def cmd_validate(args: argparse.Namespace) -> None:
    validations = []
    cases = [
        ("16_12", "k16", None, "b", ROOT / "box/chartfix-20260903/systems/64_48_16_12_13_3_k1_Q.sing"),
        ("28_20", "k16", None, "b", ROOT / "box/chartfix-20260903/systems/112_80_28_20_25_3_k1_Q.sing"),
        ("33_22", "ab", (3,), "b", ROOT / "box/topface-20260903/systems/132_88_part_3_Q.sing"),
        ("33_22", "ab", (2, 1), "b", ROOT / "box/topface-20260903/systems/132_88_part_2_1_Q.sing"),
    ]
    for row_key, chart, part, beta_prefix, baseline in cases:
        if chart == "k16":
            spec = k16_build_spec(ROWS[row_key], beta_prefix=beta_prefix)
        elif chart == "ab":
            spec = ab_build_spec(ROWS[row_key], part or ())
        else:
            raise AssertionError(chart)
        record = emit(spec, timeout=args.emit_timeout)
        native = ROOT / record["systems"]["0"]
        compare_path = OUT / "comparisons" / (spec.stem + "_compare.sing")
        cmp = compare_systems(native, baseline, compare_path, timeout=args.compare_timeout)
        validations.append(
            {
                "case": row_key,
                "chart": chart,
                "partition": None if part is None else list(part),
                "emit_elapsed": record["meta"].get("emit_elapsed"),
                "unknowns": record["meta"].get("unknowns"),
                "equations": record["meta"].get("equations"),
                "deg_x_J_gate": record["meta"].get("deg_x_J_gate"),
                "baseline": str(baseline.relative_to(ROOT)),
                "comparison": cmp,
            }
        )
    outpath = OUT / "validation.json"
    outpath.write_text(json.dumps({"manifest": verify_inputs(), "validations": validations}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"validations": validations}, indent=2, sort_keys=True))


def cmd_inventory(args: argparse.Namespace) -> None:
    rows = []
    for key in ("25_15", "24_16"):
        row = ROWS[key]
        C = shape_for(row)
        parts = [(3,), (2, 1), (1, 1, 1)] if key == "25_15" else UNFINISHED_24_16
        for part in parts:
            spec = generic_build_spec(row, part)
            rows.append(spec.meta)
    print(json.dumps(rows, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    def add_chart_args(p: argparse.ArgumentParser) -> None:
        p.add_argument("--row", choices=sorted(ROWS), required=True)
        p.add_argument("--chart", choices=("generic", "ab", "k16"), required=True)
        p.add_argument("--partition", type=parse_partition)
        p.add_argument("--beta-prefix", choices=("b", "q"), default="b")
        p.add_argument("--emit-timeout", type=int, default=900)

    p_emit = sub.add_parser("emit")
    add_chart_args(p_emit)
    p_emit.set_defaults(func=cmd_emit)

    p_run = sub.add_parser("run")
    add_chart_args(p_run)
    p_run.add_argument("--mod-timeout", type=int, default=1200)
    p_run.add_argument("--pre-timeout", type=int, default=1800)
    p_run.add_argument("--jobs", type=int, default=3)
    p_run.set_defaults(func=cmd_run)

    p_pre = sub.add_parser("preprocess-meta")
    p_pre.add_argument("--meta", required=True)
    p_pre.add_argument("--pre-timeout", type=int, default=1800)
    p_pre.add_argument("--no-exact", action="store_true")
    p_pre.set_defaults(func=cmd_preprocess_meta)

    p_val = sub.add_parser("validate")
    p_val.add_argument("--emit-timeout", type=int, default=900)
    p_val.add_argument("--compare-timeout", type=int, default=600)
    p_val.set_defaults(func=cmd_validate)

    p_inv = sub.add_parser("inventory")
    p_inv.set_defaults(func=cmd_inventory)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
