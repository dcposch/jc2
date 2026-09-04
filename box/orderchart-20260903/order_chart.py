#!/usr/bin/env python3
"""General two-point Theorem-1.2 order-chart generator.

This is intentionally standalone for the 2026-09-03 lane.  Prime marks in
labels are descended-data labels, never derivatives.  Variables are
``x=gamma`` and ``y=pi``; the target equation is ``J(Q,P)=c*x^k``.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import time
from dataclasses import asdict, dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
INPUTS = Path("/tmp/jc2-lane.YtvJBb/inputs")
RECEIPT = ROOT / "xmodel/order-chart-general-gpt55-20260903.run.v2"
PRIMES = (32003, 32009, 32027)


@dataclass(frozen=True)
class Row:
    key: str
    label: str
    n: int
    m: int
    M2: int
    V2: int
    k: int


ROWS: Dict[str, Row] = {
    "16_12_13_3_k1": Row("16_12_13_3_k1", "(16,12;13;3;k=1)", 16, 12, 13, 3, 1),
    "28_20_25_3_k1": Row("28_20_25_3_k1", "(28,20;25;3;k=1)", 28, 20, 25, 3, 1),
    "33_22_30_8_k1": Row("33_22_30_8_k1", "(33,22;30;8;k=1)", 33, 22, 30, 8, 1),
    "45_30_42_11_k1": Row("45_30_42_11_k1", "(45,30;42;11;k=1)", 45, 30, 42, 11, 1),
    "15_10_11_3_k2": Row("15_10_11_3_k2", "(15,10;11;3;k=2)", 15, 10, 11, 3, 2),
    "21_14_18_5_k1": Row("21_14_18_5_k1", "(21,14;18;5;k=1)", 21, 14, 18, 5, 1),
    "25_15_21_2_k2": Row("25_15_21_2_k2", "(25,15;21;2;k=2)", 25, 15, 21, 2, 2),
    "21_14_15_6_k4": Row("21_14_15_6_k4", "(21,14;15;6;k=4)", 21, 14, 15, 6, 4),
}


def jac(f: sp.Expr, g: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x)


def frac_s(v: F | int | sp.Expr) -> str:
    if isinstance(v, F):
        return str(v.numerator) if v.denominator == 1 else "%d/%d" % (v.numerator, v.denominator)
    return str(v)


def clean_name(name: str) -> str:
    out = re.sub(r"[^A-Za-z0-9_]+", "_", name)
    out = re.sub(r"_+", "_", out).strip("_")
    if not out:
        out = "v"
    if out[0].isdigit():
        out = "v" + out
    return out


def sstr(expr: sp.Expr) -> str:
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


def manifest_check() -> dict:
    fields: Dict[str, Dict[str, str]] = {}
    for line in RECEIPT.read_text().splitlines():
        m = re.match(r"charged_input_(\d+)_(basename|sha256)=(.*)", line)
        if m:
            fields.setdefault(m.group(1), {})[m.group(2)] = m.group(3)
    checks = []
    for idx in sorted(fields, key=int):
        rec = fields[idx]
        path = INPUTS / rec["basename"]
        got = hashlib.sha256(path.read_bytes()).hexdigest()
        checks.append({
            "idx": int(idx),
            "basename": rec["basename"],
            "path": str(path),
            "expected": rec["sha256"],
            "got": got,
            "ok": got == rec["sha256"],
        })
    return {"receipt": str(RECEIPT), "input_dir": str(INPUTS), "ok": bool(checks) and all(c["ok"] for c in checks), "checks": checks}


def closed_form(row: Row) -> dict:
    K = math.gcd(row.n, row.m)
    if K <= 0:
        raise ValueError("bad gcd")
    e = row.n // K
    q = row.m // K
    u = K - row.V2
    R = row.n - row.M2 - 1
    if R == 0:
        raise ZeroDivisionError("n-M2-1 is zero")
    Pi = e + q
    delta2 = -F(row.k + 1, R)
    delta1 = F((row.k + 1) * (Pi * u - R), R * (Pi * row.V2 - 1))
    bound = row.V2 * delta1 + u * delta2
    return {
        "K": K,
        "d2prime": K,
        "d3prime": math.gcd(K, row.M2),
        "uprime": u,
        "V2": row.V2,
        "eprime": e,
        "dprime": q,
        "R": R,
        "Pi": Pi,
        "delta2": delta2,
        "delta1": delta1,
        "bound_unit": bound,
        "lambda_P": e * bound,
        "lambda_Q": q * bound,
    }


def order_allowed(delta1: F, threshold: F, i: int, j: int) -> bool:
    return -F(i) + delta1 * F(j) >= threshold


def h_lower_monomials(row: Row, C: dict) -> List[Tuple[int, int]]:
    """Corrected D1 support for lower terms of h, with fixed top removed."""
    K = C["K"]
    u = C["uprime"]
    if u < 0:
        raise ValueError("u'=K-V2 is negative")
    degx_h = u
    out = []
    for j in range(K, -1, -1):
        for i in range(0, degx_h + 1):
            if i + j >= K:
                continue
            if order_allowed(C["delta1"], C["bound_unit"], i, j):
                out.append((i, j))
    return out


def partitions(n: int, ceiling: int | None = None) -> Iterable[Tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    top = n if ceiling is None else min(n, ceiling)
    for first in range(top, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def parse_partition(text: str) -> Tuple[int, ...]:
    vals = tuple(int(v) for v in re.split(r"[+,]", text.strip()) if v)
    if not vals or any(v <= 0 for v in vals) or tuple(sorted(vals, reverse=True)) != vals:
        raise argparse.ArgumentTypeError("use a descending partition such as 3 or 2+1")
    return vals


def allowed_partitions(row: Row) -> List[Tuple[int, ...]]:
    C = closed_form(row)
    u = C["uprime"]
    return [p for p in partitions(u) if len(p) + 1 <= row.n - row.M2]


def top_face(row: Row, part: Sequence[int], x: sp.Symbol, y: sp.Symbol) -> dict:
    if sum(part) != math.gcd(row.n, row.m) - row.V2:
        raise ValueError("partition sum is not u'")
    slopes = list(sp.symbols("s2:%d" % (len(part) + 1))) if len(part) > 1 else []
    factors: List[sp.Expr] = []
    factor_names: List[str] = []
    for _ in range(part[0]):
        factors.append(y - x)
        factor_names.append("y-x")
    for slope, exponent in zip(slopes, part[1:]):
        for _ in range(exponent):
            factors.append(y - slope * x)
            factor_names.append("y-%s*x" % slope)
    for _ in range(row.V2):
        factors.append(y)
        factor_names.append("y")
    top = sp.Integer(1)
    for factor in factors:
        top *= factor
    omega = sp.Integer(1)
    for slope in slopes:
        omega *= slope * (slope - 1)
    for i, slope in enumerate(slopes):
        for other in slopes[i + 1:]:
            omega *= slope - other
    pieces = ["(y-x)^%d" % part[0]]
    for index, exponent in enumerate(part[1:], start=2):
        pieces.append("(y-s%d*x)^%d" % (index, exponent))
    return {
        "top": sp.expand(top),
        "slopes": slopes,
        "omega": sp.expand(omega),
        "factors": factors,
        "factor_names": factor_names,
        "factored": "y^%d*%s" % (row.V2, "*".join(pieces)),
    }


def monomial_expr(mon: Tuple[int, int], x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    i, j = mon
    return x**i * y**j


def monomial_label(mon: Tuple[int, int]) -> str:
    i, j = mon
    parts = []
    if i:
        parts.append("x" if i == 1 else "x^%d" % i)
    if j:
        parts.append("y" if j == 1 else "y^%d" % j)
    return "*".join(parts) if parts else "1"


def build_tower(row: Row, part: Sequence[int], C: dict, x: sp.Symbol, y: sp.Symbol) -> dict:
    face = top_face(row, part, x, y)
    K = C["K"]
    factors = face["factors"]
    if len(factors) != K:
        raise AssertionError("factor sequence length mismatch")
    h_params = [sp.Symbol("b%d" % i) for i in range(1, K + 1)]
    prefix = sp.Integer(1)
    tower: Dict[int, sp.Expr] = {}
    weights: Dict[int, F] = {}
    noncenter_count = 0
    center_count = 0
    for degree, factor in enumerate(factors, start=1):
        prefix = sp.expand(prefix * factor)
        if factor == y:
            center_count += 1
        else:
            noncenter_count += 1
        weights[degree] = noncenter_count * C["delta2"] + center_count * C["delta1"]
        if degree == 1:
            tower[degree] = prefix
        elif degree == 2:
            tower[degree] = sp.expand(factor * tower[degree - 1] + h_params[0] * y + h_params[1])
        else:
            tower[degree] = sp.expand(factor * tower[degree - 1] + h_params[degree - 1])
    h = tower[K]
    weights[K] = C["bound_unit"]
    support_allowed = set(h_lower_monomials(row, C))
    lower_expr = sp.expand(h - face["top"])
    h_support: List[Tuple[int, int]] = []
    if lower_expr != 0:
        for mon, coef in sp.Poly(lower_expr, x, y).terms():
            if coef != 0:
                h_support.append((int(mon[0]), int(mon[1])))
    h_support = sorted(set(h_support), key=lambda mon: (-mon[1], mon[0]))
    return {
        "face": face,
        "h": h,
        "h_lower": h_support,
        "lemma21_h_support": sorted(support_allowed, key=lambda mon: (-mon[1], mon[0])),
        "lemma21_support_ok": set(h_support) <= support_allowed,
        "h_params": h_params,
        "tower": tower,
        "tower_weights": weights,
    }


def same_expr(a: sp.Expr, b: sp.Expr) -> bool:
    return sp.expand(a - b) == 0


def space_for(deficit: int, weighted: Sequence[Tuple[sp.Expr, F, str]], bound: F) -> List[sp.Expr]:
    threshold = deficit * bound
    return [expr for expr, weight, _name in weighted if weight >= threshold]


def basis_name_map(items: Sequence[Tuple[sp.Expr, F, str]]) -> Dict[str, str]:
    return {name: frac_s(weight) for _expr, weight, name in items}


def build_spaces(row: Row, part: Sequence[int], C: dict, tower_data: dict, gauged: bool) -> dict:
    x, _y = sp.symbols("x y")
    weighted: List[Tuple[sp.Expr, F, str]] = [(sp.Integer(1), F(0), "1")]
    for degree in range(C["K"] - 1, 0, -1):
        weighted.append((tower_data["tower"][degree], tower_data["tower_weights"][degree], "H%d" % degree))
    weighted.append((x, C["delta2"], "x"))
    # Remove exact duplicate expressions, keeping the first and therefore the
    # largest tower degree at a given polynomial expression.
    deduped: List[Tuple[sp.Expr, F, str]] = []
    for item in weighted:
        if not any(same_expr(item[0], old[0]) for old in deduped):
            deduped.append(item)
    weighted = sorted(deduped, key=lambda item: (-item[1], item[2]))

    e, q = C["eprime"], C["dprime"]
    alpha_spaces = {i: list(space_for(i, weighted, C["bound_unit"])) for i in range(1, e + 1)}
    beta_spaces = {i: list(space_for(i, weighted, C["bound_unit"])) for i in range(2, q + 1)}
    alpha_pre = {i: len(alpha_spaces[i]) for i in alpha_spaces}
    beta_pre = {i: len(beta_spaces[i]) for i in beta_spaces}
    gauges: List[str] = []
    gauge_notes: List[str] = []

    if gauged:
        shear = e - q
        safe_shear = False
        if 1 <= shear <= e and alpha_spaces.get(shear) == [sp.Integer(1)]:
            safe_shear = True
            for deficit, bspace in beta_spaces.items():
                target = alpha_spaces.get(deficit + shear, [])
                for basis in bspace:
                    if not any(same_expr(basis, candidate) for candidate in target):
                        safe_shear = False
                        break
                if not safe_shear:
                    break
        if safe_shear:
            alpha_spaces[shear] = []
            gauges.append("P -> P - alpha_%d Q" % shear)
        else:
            gauge_notes.append("alpha_%d shear omitted; forcing it would be a slice" % shear)

        if q in beta_spaces and any(same_expr(basis, sp.Integer(1)) for basis in beta_spaces[q]):
            beta_spaces[q] = [basis for basis in beta_spaces[q] if not same_expr(basis, sp.Integer(1))]
            gauges.append("Q -> Q - const(beta_%d)" % q)
        if e in alpha_spaces and any(same_expr(basis, sp.Integer(1)) for basis in alpha_spaces[e]):
            alpha_spaces[e] = [basis for basis in alpha_spaces[e] if not same_expr(basis, sp.Integer(1))]
            gauges.append("P -> P - const(alpha_%d)" % e)

    return {
        "weighted": weighted,
        "basis_weights": basis_name_map(weighted),
        "alpha_spaces": alpha_spaces,
        "beta_spaces": beta_spaces,
        "alpha_dims_pre_gauge": [alpha_pre[i] for i in range(1, e + 1)],
        "beta_dims_pre_gauge": [beta_pre[i] for i in range(2, q + 1)],
        "alpha_dims": [len(alpha_spaces[i]) for i in range(1, e + 1)],
        "beta_dims": [len(beta_spaces[i]) for i in range(2, q + 1)],
        "gauges": gauges,
        "gauge_notes": gauge_notes,
    }


def coeff(prefix: str, deficit: int, basis: Sequence[sp.Expr], params: List[sp.Symbol]) -> sp.Expr:
    out = sp.Integer(0)
    for idx, item in enumerate(basis):
        var = sp.Symbol("%s%d_%d" % (prefix, deficit, idx))
        params.append(var)
        out += var * item
    return sp.expand(out)


def hadic_by_power(h: sp.Expr, low_terms, high_terms, x: sp.Symbol, y: sp.Symbol) -> Dict[int, sp.Expr]:
    by_power: Dict[int, sp.Expr] = {}
    for aa, r in low_terms:
        for bb, s in high_terms:
            same_power = jac(aa, bb, x, y)
            if same_power != 0:
                by_power[r + s] = by_power.get(r + s, 0) + same_power
            lower_power = s * bb * jac(aa, h, x, y) + r * aa * jac(h, bb, x, y)
            if lower_power != 0:
                by_power[r + s - 1] = by_power.get(r + s - 1, 0) + lower_power
    if 0 not in by_power:
        by_power[0] = sp.Integer(0)
    level = 0
    max_level = max(by_power) if by_power else 0
    h_poly = sp.Poly(h, y)
    while level <= max_level:
        rem = sp.expand(by_power.get(level, 0))
        if rem != 0:
            qdiv, rdiv = sp.div(sp.Poly(rem, y), h_poly, y)
            by_power[level] = sp.expand(rdiv.as_expr())
            if qdiv != 0:
                by_power[level + 1] = by_power.get(level + 1, 0) + sp.expand(qdiv.as_expr())
                max_level = max(max_level, level + 1)
        level += 1
    return by_power


def equations_from_by_power(by_power: Dict[int, sp.Expr], c: sp.Symbol, kexp: int, x: sp.Symbol, y: sp.Symbol):
    rows = []
    eqs = []
    adjusted = dict(by_power)
    adjusted[0] = sp.expand(adjusted.get(0, 0) - c * x**kexp)
    for level in sorted(adjusted):
        rem = sp.expand(adjusted[level])
        if rem == 0:
            continue
        poly = sp.Poly(rem, x, y)
        for mon, coef in poly.terms():
            coef = sp.expand(coef)
            if coef != 0:
                rows.append({"h_power": level, "monomial": [int(mon[0]), int(mon[1])], "expr": coef})
                eqs.append(coef)
    return eqs, rows


def degree_x(expr: sp.Expr, x: sp.Symbol) -> int:
    expr = sp.expand(expr)
    if expr == 0:
        return -1
    return int(sp.Poly(expr, x).degree())


def recomposition_check(h, low_terms, high_terms, by_power, params, x, y) -> bool:
    sample = {}
    values = [2, -3, 5, -7, 11, -13, 17, -19, 23, -29, 31, -37]
    for idx, param in enumerate(params):
        sample[param] = values[idx % len(values)]
    hs = h.subs(sample)
    low = sp.Add(*(coef * h**power for coef, power in low_terms)).subs(sample)
    high = sp.Add(*(coef * h**power for coef, power in high_terms)).subs(sample)
    direct = sp.expand(jac(low, high, x, y))
    reconstructed = sp.expand(sp.Add(*(rem.subs(sample) * hs**level for level, rem in by_power.items())))
    return sp.expand(direct - reconstructed) == 0


def build_chart(row: Row, part: Sequence[int], gauged: bool = True) -> dict:
    C = closed_form(row)
    if C["uprime"] < 0:
        raise ValueError("u' is negative")
    if sum(part) != C["uprime"]:
        raise ValueError("partition sum does not equal u'")
    if tuple(part) not in allowed_partitions(row):
        raise ValueError("partition violates source-safe root-count cap")
    if C["bound_unit"] >= 0:
        raise ValueError("nonnegative common bound; order chart is degenerate here")

    x, y = sp.symbols("x y")
    c, T = sp.symbols("c T")
    tower = build_tower(row, part, C, x, y)
    spaces = build_spaces(row, part, C, tower, gauged)
    e, q = C["eprime"], C["dprime"]
    params: List[sp.Symbol] = list(tower["h_params"]) + list(tower["face"]["slopes"])
    alpha = {i: coeff("A", i, spaces["alpha_spaces"][i], params) for i in range(1, e + 1)}
    beta = {i: coeff("B", i, spaces["beta_spaces"][i], params) for i in range(2, q + 1)}
    high_terms = [(sp.Integer(1), e)] + [(alpha[i], e - i) for i in range(1, e + 1)]
    low_terms = [(sp.Integer(1), q)] + [(beta[i], q - i) for i in range(2, q + 1)]
    by_power = hadic_by_power(tower["h"], low_terms, high_terms, x, y)
    j0 = sp.expand(by_power.get(0, 0))
    sanity = {
        "status": "PASS" if degree_x(j0, x) >= row.k else "INSTRUMENT-FAIL",
        "required_k": row.k,
        "deg_x_J0": degree_x(j0, x),
        "kind": "h-adic normalized level-0 remainder before subtracting c*x^k",
    }
    eqs, tagged = equations_from_by_power(by_power, c, row.k, x, y)
    params.append(c)
    reco = recomposition_check(tower["h"], low_terms, high_terms, by_power, params[:-1], x, y)
    if not reco:
        raise AssertionError("numeric h-adic recomposition failed")
    sat = sp.expand(c * tower["face"]["omega"])
    meta = {
        "row": asdict(row),
        "partition": list(part),
        "partition_label": "+".join(map(str, part)),
        "K": C["K"],
        "d2prime": C["d2prime"],
        "d3prime": C["d3prime"],
        "uprime": C["uprime"],
        "dprime_q": q,
        "eprime_e": e,
        "R": C["R"],
        "Pi": C["Pi"],
        "delta2": frac_s(C["delta2"]),
        "delta1": frac_s(C["delta1"]),
        "bound_unit": frac_s(C["bound_unit"]),
        "lambda_P_over_e": frac_s(C["lambda_P"] / e),
        "lambda_Q_over_q": frac_s(C["lambda_Q"] / q),
        "top_face_factored": tower["face"]["factored"],
        "omega": sstr(tower["face"]["omega"]),
        "saturation_factor": sstr(sat),
        "h_parameter_count": len(tower["h_params"]),
        "h_lower_support_count": len(tower["h_lower"]),
        "h_lower_count": len(tower["h_params"]),
        "h_lower": [list(mon) for mon in tower["h_lower"]],
        "lemma21_h_support_count": len(tower["lemma21_h_support"]),
        "lemma21_support_ok": tower["lemma21_support_ok"],
        "slope_count": len(tower["face"]["slopes"]),
        "tower_factor_order": tower["face"]["factor_names"],
        "tower_weights": {str(i): frac_s(tower["tower_weights"][i]) for i in range(1, C["K"] + 1)},
        "basis_weights": spaces["basis_weights"],
        "alpha_dims_pre_gauge": spaces["alpha_dims_pre_gauge"],
        "beta_dims_pre_gauge": spaces["beta_dims_pre_gauge"],
        "alpha_dims": spaces["alpha_dims"],
        "beta_dims": spaces["beta_dims"],
        "gauges": spaces["gauges"],
        "gauge_notes": spaces["gauge_notes"],
        "gauge_policy": "const(beta_q) and const(alpha_e) are target translations; alpha_(e-q) shear only when scalar and beta spaces embed after the shift",
        "unknowns": len(params),
        "params_without_T": len(params),
        "equations": len(eqs),
        "h_levels": sorted(k for k, v in by_power.items() if sp.expand(v) != 0),
        "tagged_rows": [{"h_power": r["h_power"], "monomial": r["monomial"]} for r in tagged],
        "sanity_gate": sanity,
        "recomposition_ok": reco,
        "actual_pair_control": actual_pair_control(),
    }
    return {
        "meta": meta,
        "eqs": eqs,
        "tagged": tagged,
        "params": params,
        "T": T,
        "sat": sat,
        "x": x,
        "y": y,
    }


def build_native_spec(row: Row, part: Sequence[int], gauged: bool = True) -> dict:
    """Build only the compact declarations needed for Singular row emission."""
    C = closed_form(row)
    if C["uprime"] < 0:
        raise ValueError("u' is negative")
    if sum(part) != C["uprime"]:
        raise ValueError("partition sum does not equal u'")
    if tuple(part) not in allowed_partitions(row):
        raise ValueError("partition violates source-safe root-count cap")
    if C["bound_unit"] >= 0:
        raise ValueError("nonnegative common bound; order chart is degenerate here")

    x, y = sp.symbols("x y")
    c, T = sp.symbols("c T")
    tower = build_tower(row, part, C, x, y)
    spaces = build_spaces(row, part, C, tower, gauged)
    e, q = C["eprime"], C["dprime"]
    params: List[sp.Symbol] = list(tower["h_params"]) + list(tower["face"]["slopes"])
    alpha = {i: coeff("A", i, spaces["alpha_spaces"][i], params) for i in range(1, e + 1)}
    beta = {i: coeff("B", i, spaces["beta_spaces"][i], params) for i in range(2, q + 1)}
    params.append(c)
    sat = sp.expand(c * tower["face"]["omega"])
    setup = ["poly h = %s;" % sstr(tower["h"])]
    for degree in range(1, C["K"]):
        setup.append("poly Hbasis%d = %s;" % (degree, sstr(tower["tower"][degree])))
    for i in range(1, e + 1):
        setup.append("poly AA%d = %s;" % (i, sstr(alpha[i])))
    for i in range(2, q + 1):
        setup.append("poly BB%d = %s;" % (i, sstr(beta[i])))
    low_terms = [("1", q)] + [("BB%d" % i, q - i) for i in range(2, q + 1)]
    high_terms = [("1", e)] + [("AA%d" % i, e - i) for i in range(1, e + 1)]
    meta = {
        "row": asdict(row),
        "partition": list(part),
        "partition_label": "+".join(map(str, part)),
        "K": C["K"],
        "d2prime": C["d2prime"],
        "d3prime": C["d3prime"],
        "uprime": C["uprime"],
        "dprime_q": q,
        "eprime_e": e,
        "R": C["R"],
        "Pi": C["Pi"],
        "delta2": frac_s(C["delta2"]),
        "delta1": frac_s(C["delta1"]),
        "bound_unit": frac_s(C["bound_unit"]),
        "lambda_P_over_e": frac_s(C["lambda_P"] / e),
        "lambda_Q_over_q": frac_s(C["lambda_Q"] / q),
        "top_face_factored": tower["face"]["factored"],
        "omega": sstr(tower["face"]["omega"]),
        "saturation_factor": sstr(sat),
        "h_parameter_count": len(tower["h_params"]),
        "h_lower_support_count": len(tower["h_lower"]),
        "h_lower_count": len(tower["h_params"]),
        "h_lower": [list(mon) for mon in tower["h_lower"]],
        "lemma21_h_support_count": len(tower["lemma21_h_support"]),
        "lemma21_support_ok": tower["lemma21_support_ok"],
        "slope_count": len(tower["face"]["slopes"]),
        "tower_factor_order": tower["face"]["factor_names"],
        "tower_weights": {str(i): frac_s(tower["tower_weights"][i]) for i in range(1, C["K"] + 1)},
        "basis_weights": spaces["basis_weights"],
        "alpha_dims_pre_gauge": spaces["alpha_dims_pre_gauge"],
        "beta_dims_pre_gauge": spaces["beta_dims_pre_gauge"],
        "alpha_dims": spaces["alpha_dims"],
        "beta_dims": spaces["beta_dims"],
        "gauges": spaces["gauges"],
        "gauge_notes": spaces["gauge_notes"],
        "gauge_policy": "const(beta_q) and const(alpha_e) are target translations; alpha_(e-q) shear only when scalar and beta spaces embed after the shift",
        "unknowns": len(params),
        "params_without_T": len(params),
        "actual_pair_control": actual_pair_control(),
        "native_low_terms": [{"coefficient": a, "h_power": r} for a, r in low_terms],
        "native_high_terms": [{"coefficient": a, "h_power": r} for a, r in high_terms],
    }
    return {
        "meta": meta,
        "setup": setup,
        "low_terms": low_terms,
        "high_terms": high_terms,
        "params": params,
        "T": T,
        "sat": sat,
    }


def native_builder_text(spec: dict, rows_path: Path) -> str:
    meta = spec["meta"]
    e = meta["eprime_e"]
    q = meta["dprime_q"]
    level_cap = e + q + 2 * meta["K"] + 12
    params_without_c = [str(p) for p in spec["params"] if str(p) != "c"]
    coeff_field = ",".join(params_without_c + ["c"])
    lines = [
        "// generated by order_chart.py --native-builder",
        "// row %s partition %s" % (meta["row"]["label"], meta["partition_label"]),
        "ring R=(0,%s),(y,x),dp;" % coeff_field,
        "option(redSB);",
        "string rowsfile = \"%s\";" % str(rows_path.resolve()),
        "write(\":w \" + rowsfile, \"source_index|h_power|x_power|y_power|expr\");",
        "int source_idx = 0;",
        "int max_nf_deg = -1;",
        "intvec WY = 1,0;",
        "intvec WX = 0,1;",
        r"""
proc native_coeff_y(poly rem, int wanty, intvec WY)
{
  matrix CY = coef(rem, y);
  int j;
  for (j = 1; j <= ncols(CY); j++)
  {
    if (deg(CY[1,j], WY) == wanty)
    {
      return(CY[2,j]);
    }
  }
  return(0);
}

proc native_coeff_xy(poly rem, int wantx, int wanty, intvec WX, intvec WY)
{
  matrix CX = coef(rem, x);
  int i;
  int j;
  for (i = 1; i <= ncols(CX); i++)
  {
    if (deg(CX[1,i], WX) == wantx)
    {
      matrix CY = coef(CX[2,i], y);
      for (j = 1; j <= ncols(CY); j++)
      {
        if (deg(CY[1,j], WY) == wanty)
        {
          return(CY[2,j]);
        }
      }
    }
  }
  return(0);
}

proc native_y_div(poly dividend, poly divisor, int y_degree, intvec WY)
{
  poly q = 0;
  poly r = dividend;
  int d;
  poly lc;
  poly term;
  while (r != 0 && deg(r, WY) >= y_degree)
  {
    d = deg(r, WY);
    lc = native_coeff_y(r, d, WY);
    term = lc * y^(d - y_degree);
    q = q + term;
    r = r - term * divisor;
  }
  list out = q, r;
  return(out);
}

proc native_append_coeffs(poly rem, int hpow, string rowsfile, intvec WX, intvec WY)
{
  if (rem == 0)
  {
    return();
  }
  int dx = deg(rem, WX);
  if (dx > max_nf_deg)
  {
    max_nf_deg = dx;
  }
  matrix CX = coef(rem, x);
  int i;
  int j;
  int xp;
  int yp;
  matrix CY;
  poly cc;
  for (i = 1; i <= ncols(CX); i++)
  {
    xp = deg(CX[1,i], WX);
    CY = coef(CX[2,i], y);
    for (j = 1; j <= ncols(CY); j++)
    {
      cc = CY[2,j];
      if (cc != 0)
      {
        yp = deg(CY[1,j], WY);
        write(":a " + rowsfile,
          string(source_idx) + "|" + string(hpow) + "|" +
          string(xp) + "|" + string(yp) + "|" + string(cc));
        source_idx = source_idx + 1;
      }
    }
  }
}
""".strip(),
    ]
    lines.extend(spec["setup"])
    for level in range(level_cap + 1):
        lines.append("poly H%d = 0;" % level)
    lines.append("poly tmpSame;")
    lines.append("poly tmpLower;")
    for aa, r in spec["low_terms"]:
        for bb, s in spec["high_terms"]:
            lines.append(
                "tmpSame = diff((%s),x)*diff((%s),y)-diff((%s),y)*diff((%s),x);"
                % (aa, bb, aa, bb)
            )
            lines.append("if (tmpSame != 0) { H%d = H%d + tmpSame; }" % (r + s, r + s))
            if r + s - 1 >= 0 and (r != 0 or s != 0):
                lines.append(
                    "tmpLower = (%d)*(%s)*(diff((%s),x)*diff(h,y)-diff((%s),y)*diff(h,x))"
                    "+(%d)*(%s)*(diff(h,x)*diff((%s),y)-diff(h,y)*diff((%s),x));"
                    % (s, bb, aa, aa, r, aa, bb, bb)
                )
                lines.append("if (tmpLower != 0) { H%d = H%d + tmpLower; }" % (r + s - 1, r + s - 1))
    for level in range(level_cap):
        lines.append("if (H%d != 0) {" % level)
        lines.append("  list LD%d = native_y_div(H%d, h, %d, WY);" % (level, level, meta["K"]))
        lines.append("  H%d = LD%d[2];" % (level, level))
        lines.append("  if (LD%d[1] != 0) { H%d = H%d + LD%d[1]; }" % (level, level + 1, level + 1, level))
        lines.append("}")
    lines.append("poly level0_before = H0;")
    lines.append("poly target_xk = native_coeff_xy(level0_before, %d, 0, WX, WY);" % meta["row"]["k"])
    lines.append("int level0_deg_x = deg(level0_before, WX);")
    lines.append("H0 = H0 - c*x^%d;" % meta["row"]["k"])
    for level in range(level_cap + 1):
        lines.append("native_append_coeffs(H%d, %d, rowsfile, WX, WY);" % (level, level))
    lines.append('print("NATIVE_GATE level0_deg_x_before_minus_c=" + string(level0_deg_x));')
    lines.append('if (target_xk != 0) { print("NATIVE_GATE target_xk_level0_nonzero=1"); } else { print("NATIVE_GATE target_xk_level0_nonzero=0"); }')
    lines.append('print("NATIVE_DONE equations=" + string(source_idx));')
    lines.append('print("NATIVE_DONE max_nf_deg_x_after_minus_c=" + string(max_nf_deg));')
    lines.append("quit;")
    return "\n".join(lines) + "\n"


def write_native_builder(row: Row, part: Sequence[int]) -> dict:
    spec = build_native_spec(row, part, gauged=True)
    stem = stem_for(row, part)
    rows_path = OUT / "rows" / ("%s_rows.tsv" % stem)
    builder_path = OUT / "builders" / ("%s_builder.sing" % stem)
    meta_path = OUT / "meta" / ("%s_native.json" % stem)
    builder_path.parent.mkdir(parents=True, exist_ok=True)
    rows_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    builder_path.write_text(native_builder_text(spec, rows_path), encoding="utf-8")
    payload = {
        "manifest_ok": manifest_check()["ok"],
        "meta": spec["meta"],
        "variables": [str(p) for p in spec["params"]],
        "sat": sstr(spec["sat"]),
        "builder": str(builder_path.relative_to(ROOT)),
        "rows_path": str(rows_path.relative_to(ROOT)),
    }
    meta_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload


def parse_native_builder_log(text: str) -> dict:
    out: dict = {}
    for line in text.splitlines():
        if line.startswith("NATIVE_GATE ") or line.startswith("NATIVE_DONE "):
            _, rest = line.split(" ", 1)
            if "=" in rest:
                key, value = rest.split("=", 1)
                try:
                    out[key] = int(value)
                except ValueError:
                    out[key] = value
    return out


def read_native_rows(path: Path) -> List[dict]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        header = next(handle, None)
        if header is None:
            return rows
        for line in handle:
            line = line.rstrip("\n")
            if not line:
                continue
            src, hpow, xp, yp, expr = line.split("|", 4)
            rows.append({
                "source_index": int(src),
                "h_power": int(hpow),
                "monomial": [int(xp), int(yp)],
                "expr": expr,
            })
    return rows


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def write_native_system(meta_json: Path, chars: Sequence[int], algorithm: str) -> dict:
    payload = json.loads(meta_json.read_text(encoding="utf-8"))
    rows_path = ROOT / payload["rows_path"]
    rows = read_native_rows(rows_path)
    log_path = Path(str(ROOT / payload["builder"]) + ".out")
    gate = parse_native_builder_log(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}
    payload["meta"]["equations"] = len(rows)
    payload["meta"]["sanity_gate"] = {
        "status": "PASS" if gate.get("level0_deg_x_before_minus_c", -1) >= payload["meta"]["row"]["k"] else "INSTRUMENT-FAIL",
        "required_k": payload["meta"]["row"]["k"],
        "deg_x_J0": gate.get("level0_deg_x_before_minus_c"),
        "target_xk_level0_nonzero": bool(gate.get("target_xk_level0_nonzero", 0)),
        "max_nf_deg_x_after_minus_c": gate.get("max_nf_deg_x_after_minus_c"),
        "kind": "native h-adic normalized level-0 remainder before subtracting c*x^k",
    }
    payload["row_file"] = {
        "rows": len(rows),
        "bytes": rows_path.stat().st_size,
        "sha256": file_sha256(rows_path),
    }
    scripts = {}
    for char in chars:
        suffix = "Q" if char == 0 else "mod_%d" % char
        script = OUT / "systems" / ("%s_%s_%s.sing" % (Path(payload["rows_path"]).stem.replace("_rows", ""), suffix, algorithm))
        write_system_from_rows(script, payload, rows, char, algorithm)
        scripts[str(char)] = str(script.relative_to(ROOT))
    payload["systems"] = scripts
    meta_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload


def write_system_from_rows(path: Path, payload: dict, rows: Sequence[dict], char: int, algorithm: str) -> None:
    meta = payload["meta"]
    variables = payload["variables"]
    if "T" not in variables:
        all_vars = variables + ["T"]
    else:
        all_vars = variables
    T = "T"
    sat = payload["sat"]
    alg_call = "std(I)" if algorithm == "std" else "slimgb(I)"
    lines = [
        "// generated by order_chart.py --native-system",
        "// row %s partition %s" % (meta["row"]["label"], meta["partition_label"]),
        "// top %s" % meta["top_face_factored"],
        "// saturation by %s" % sat,
        "// gauges %s" % ("; ".join(meta["gauges"]) if meta["gauges"] else "none"),
        "// sanity_gate status=%s deg_x_J0=%s required_k=%s" % (
            meta.get("sanity_gate", {}).get("status"),
            meta.get("sanity_gate", {}).get("deg_x_J0"),
            meta["row"]["k"],
        ),
        "ring R=%d,(%s),dp;" % (char, ",".join(all_vars)),
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); } else { print("CONTROL_RING_FAIL"); }',
        'print("CONTROL_EMPTY_START");',
        "ideal CE=(%s),%s*(%s)-1;" % (sat, T, sat),
        "ideal GE=std(CE);",
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
        'print("CONTROL_NONEMPTY_START");',
        "ideal CN=(%s)-1,%s*(%s)-1;" % (sat, T, sat),
        "ideal GN=std(CN);",
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
        'print("MAIN_START equations=%d unknowns=%d char=%d algorithm=%s");' % (
            len(rows), len(variables), char, algorithm),
        "ideal I=%s;" % ",\n".join([row["expr"] for row in rows] + ["%s*(%s)-1" % (T, sat)]),
        "ideal G=%s;" % alg_call,
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_NONTRIVIAL"); }',
        "quit;",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def rename_symbols(params: Sequence[sp.Symbol], T: sp.Symbol):
    names: List[str] = []
    rename: Dict[sp.Symbol, sp.Symbol] = {}
    for sym in list(params) + [T]:
        base = clean_name(str(sym))
        name = base
        suffix = 1
        while name in names:
            suffix += 1
            name = "%s_%d" % (base, suffix)
        names.append(name)
        rename[sym] = sp.Symbol(name)
    return names, rename


def write_singular(path: Path, rec: dict, char: int, algorithm: str = "std") -> None:
    meta = rec["meta"]
    names, rename = rename_symbols(rec["params"], rec["T"])
    sat_s = sstr(rec["sat"].subs(rename))
    T_s = str(rename[rec["T"]])
    gens = [sstr(eq.subs(rename)) for eq in rec["eqs"]]
    gens.append("%s*(%s)-1" % (T_s, sat_s))
    alg_call = "std(I)" if algorithm == "std" else "slimgb(I)"
    lines = [
        "// generated by order_chart.py",
        "// row %s partition %s" % (meta["row"]["label"], meta["partition_label"]),
        "// top %s" % meta["top_face_factored"],
        "// gauges %s" % ("; ".join(meta["gauges"]) if meta["gauges"] else "none"),
        "// saturation by %s" % sat_s,
        "// sanity_gate status=%s deg_x_J0=%s required_k=%s" % (
            meta["sanity_gate"]["status"],
            meta["sanity_gate"]["deg_x_J0"],
            meta["sanity_gate"]["required_k"],
        ),
        "ring R=%d,(%s),dp;" % (char, ",".join(names)),
        "option(redSB);",
        'print("CONTROL_RING R");',
        "nameof(basering);",
        'print("CONTROL_EMPTY_START");',
        "ideal CE=(%s),%s*(%s)-1;" % (sat_s, T_s, sat_s),
        "ideal GE=std(CE);",
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
        'print("CONTROL_NONEMPTY_START");',
        "ideal CN=(%s)-1,%s*(%s)-1;" % (sat_s, T_s, sat_s),
        "ideal GN=std(CN);",
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
        'print("MAIN_START equations=%d unknowns=%d char=%d algorithm=%s");' % (
            meta["equations"], meta["unknowns"], char, algorithm),
        "ideal I=%s;" % ",\n".join(gens),
        "ideal G=%s;" % alg_call,
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_NONTRIVIAL"); }',
        "quit;",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def write_json(path: Path, rec: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = dict(rec["meta"])
    payload["equation_text_bytes"] = sum(len(str(e)) for e in rec["eqs"])
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def parse_singular_output(output: str) -> dict:
    lines = output.splitlines()

    def after(label: str):
        for index, line in enumerate(lines):
            if line.strip() == label and index + 1 < len(lines):
                return lines[index + 1].strip()
        return None

    if "MAIN_SATURATED_EMPTY" in output:
        verdict = "SATURATED-EMPTY"
    elif "MAIN_NONTRIVIAL" in output:
        verdict = "SURVIVES"
    else:
        verdict = "ERROR"
    return {
        "verdict": verdict,
        "basis_size": after("MAIN_DONE basis_size="),
        "control_empty_pass": "CONTROL_EMPTY_PASS" in output,
        "control_nonempty_pass": "CONTROL_NONEMPTY_PASS" in output,
        "ring": after("CONTROL_RING R"),
    }


def singular_version() -> str:
    proc = subprocess.run(["Singular", "-v"], capture_output=True, text=True, timeout=20)
    return (proc.stdout or proc.stderr).splitlines()[0].strip()


def actual_pair_control() -> dict:
    x, y = sp.symbols("x y")
    low = y
    high = y - x**2 / 2
    J = sp.expand(jac(low, high, x, y))
    return {
        "pair": "(pi, pi-gamma^2/2)",
        "J_low_high": str(J),
        "monic_pi_degrees": [1, 1],
        "tuple_classifier": "FAIL",
        "reason": "pi-degrees are 1,1 and do not match any requested descended tuple",
    }


def row_from_args(args) -> Row:
    if args.row:
        if args.row not in ROWS:
            raise SystemExit("unknown row key %s" % args.row)
        return ROWS[args.row]
    if None in (args.n, args.m, args.M2, args.V2, args.k):
        raise SystemExit("supply --row or all of --n --m --M2 --V2 --k")
    return Row("%d_%d_%d_%d_k%d" % (args.n, args.m, args.M2, args.V2, args.k),
               "(%d,%d;%d;%d;k=%d)" % (args.n, args.m, args.M2, args.V2, args.k),
               args.n, args.m, args.M2, args.V2, args.k)


def stem_for(row: Row, part: Sequence[int]) -> str:
    return "%s_part_%s" % (row.key, "_".join(map(str, part)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--row", choices=sorted(ROWS))
    parser.add_argument("--n", type=int)
    parser.add_argument("--m", type=int)
    parser.add_argument("--M2", type=int)
    parser.add_argument("--V2", type=int)
    parser.add_argument("--k", type=int)
    parser.add_argument("--partition", type=parse_partition)
    parser.add_argument("--all-partitions", action="store_true")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--native-builder", action="store_true")
    parser.add_argument("--native-system")
    parser.add_argument("--algorithm", choices=["std", "slimgb"], default="std")
    parser.add_argument("--chars", default="0")
    parser.add_argument("--manifest", action="store_true")
    parser.add_argument("--actual-pair", action="store_true")
    args = parser.parse_args()

    if args.manifest:
        print(json.dumps(manifest_check(), indent=2, sort_keys=True))
        return
    if args.actual_pair:
        print(json.dumps(actual_pair_control(), indent=2, sort_keys=True))
        return

    if args.native_system:
        chars = [int(c) for c in args.chars.split(",") if c]
        result = write_native_system(ROOT / args.native_system, chars, args.algorithm)
        print(json.dumps(result, indent=2, sort_keys=True))
        return

    row = row_from_args(args)
    parts = allowed_partitions(row) if args.all_partitions else [args.partition]
    if not parts or parts == [None]:
        raise SystemExit("supply --partition or --all-partitions")
    summary = {
        "manifest_ok": manifest_check()["ok"],
        "singular": singular_version(),
        "row": asdict(row),
        "parts": [],
    }
    for part in parts:
        if args.native_builder:
            payload = write_native_builder(row, part)
            summary["parts"].append(payload["meta"] | {
                "builder": payload["builder"],
                "rows_path": payload["rows_path"],
                "native_meta_path": str((OUT / "meta" / ("%s_native.json" % stem_for(row, part))).relative_to(ROOT)),
            })
            continue
        started = time.time()
        rec = build_chart(row, part, gauged=True)
        rec["meta"]["build_elapsed"] = round(time.time() - started, 3)
        stem = stem_for(row, part)
        if args.write:
            meta_path = OUT / "meta" / ("%s.json" % stem)
            write_json(meta_path, rec)
            rec["meta"]["meta_path"] = str(meta_path.relative_to(ROOT))
            for char_s in [c for c in args.chars.split(",") if c]:
                char = int(char_s)
                suffix = "Q" if char == 0 else "mod_%d" % char
                script = OUT / "systems" / ("%s_%s_%s.sing" % (stem, suffix, args.algorithm))
                write_singular(script, rec, char, args.algorithm)
                rec["meta"].setdefault("scripts", {})[suffix] = str(script.relative_to(ROOT))
            write_json(meta_path, rec)
        summary["parts"].append(rec["meta"])
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
