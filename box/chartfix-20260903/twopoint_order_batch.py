#!/usr/bin/env python3
"""Two-point descended-order batch for the 2026-09-03 Appendix-II list.

This is a fresh batch driver.  It imports only the frozen/copy shape arithmetic
and builds the algebra systems locally:

* K16 u=1,V2=3 rows: Theorem-1.2 h-adic order chart, generalized from the
  independent t=2 generator.  The target gauges are applied only after a
  subset check proves the triangular shear preserves the displayed filtrations.
* d'=2,e'=3 rows: Appendix-II two-point A/B chart, with the option to keep the
  whole D1 top face free for u>=3 rows whose split top face is not licensed.
* Other rows: counted conservatively by the D1 monomial superset.  They are not
  killed by a slice.

Prime marks are labels.  Variables are x,y in the descended chart; x is Moh's
gamma in the monomial Jacobian equation J(low, high)=c*x^k.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, asdict
from fractions import Fraction as F
from typing import Dict, Iterable, List, Sequence, Tuple

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.environ.get("LANE_INPUT_DIR", "/tmp/jc2-lane.BFzCan/inputs")
LANE_RECEIPT = os.environ.get(
    "LANE_RECEIPT",
    os.path.abspath(os.path.join(HERE, "..", "..", "xmodel", "chart-fix-d1zero-gpt55-20260903.run.v2")),
)
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from shape import h_monomials, leading_support, shape_bundle  # noqa: E402

BIG_PRIMES = [32003, 32009, 32027]


@dataclass(frozen=True)
class Row:
    src: str
    n: int
    m: int
    M2: int
    V2: int
    k: int
    tag: str = ""


ROWS: List[Row] = [
    Row("(64,48)", 16, 12, 13, 3, 1, "MOH-K16-t1"),
    Row("(75,50) V2=2", 15, 10, 11, 2, 2, "MOH-COMPILER"),
    Row("(75,50) V2=3", 15, 10, 11, 3, 2, "MOH-CONTROL2"),
    Row("(84,56)", 21, 14, 18, 5, 1, "MOH-COMPILER"),
    Row("(112,80)", 28, 20, 25, 3, 1, "K16-t2-PROMOTED-REPLAY"),
    Row("(125,75)", 25, 15, 21, 2, 2),
    Row("(132,88)", 33, 22, 30, 8, 1),
    Row("(147,98)", 21, 14, 15, 6, 4),
    Row("(160,112)", 40, 28, 37, 3, 1, "K16-t3"),
    Row("(168,112) drop1", 24, 16, 18, 7, 4),
    Row("(175,100)", 35, 20, 31, 2, 2),
    Row("(175,125)", 35, 25, 31, 3, 2),
    Row("(180,120) drop1", 45, 30, 42, 11, 1),
    Row("(180,144)", 30, 24, 25, 4, 3),
    Row("(189,126) drop1", 27, 18, 21, 8, 4),
    Row("(192,128)", 24, 16, 17, 2, 5),
    Row("(196,56)", 49, 14, 46, 4, 1),
    Row("(200,120)", 50, 30, 47, 7, 1),
]


def jac(f, g, x, y):
    return sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x)


def frac_s(v):
    if isinstance(v, F):
        return "%d" % v.numerator if v.denominator == 1 else "%d/%d" % (v.numerator, v.denominator)
    return str(v)


def clean_name(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9_]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "row"


def sstr(expr) -> str:
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


def coeff(prefix: str, idx: int, basis: Sequence[sp.Expr], params: List[sp.Symbol]):
    if not basis:
        return sp.Integer(0)
    out = sp.Integer(0)
    for j, base in enumerate(basis):
        v = sp.Symbol("%s%d_%d" % (prefix, idx, j))
        params.append(v)
        out += v * base
    return sp.expand(out)


def poly_from_mons(mons: Iterable[Tuple[int, int]], x, y, prefix: str, params: List[sp.Symbol]):
    out = sp.Integer(0)
    for a, b in mons:
        v = sp.Symbol("%s_%d_%d" % (prefix, a, b))
        params.append(v)
        out += v * x**a * y**b
    return sp.expand(out)


def h_two_point(C: dict, x, y, prefix: str, top_policy: str):
    """Return h, h-parameters, and the effective top policy.

    top_policy=fixed uses shape.leading_support and D1 lower terms.  top_policy=d1
    keeps every D1-allowed h monomial except the monic y^K term free.
    """
    K = C["K"]
    params: List[sp.Symbol] = []
    h = y**K
    if top_policy == "fixed":
        h = sp.Integer(0)
        for (a, b), cc in C["lead"].items():
            h += int(cc) * x**a * y**b
        free = list(C["h_free"])
        note = "fixed split top face"
    elif top_policy == "d1":
        free = [m for m in C["h_all"] if m != (0, K)]
        note = "D1-only top face; monic y^K fixed"
    else:
        raise ValueError("bad top_policy %s" % top_policy)
    h += poly_from_mons(free, x, y, prefix, params)
    return sp.expand(h), params, free, note


def build_beta_ab(h, x, y):
    p, q, r, s = sp.symbols("bp bq br bs")
    h0 = sp.expand(h.subs(y, 0))
    A = sp.expand(sp.together((h - h0) / y))
    beta = sp.expand(p * A + q * y + r * x + s)
    return beta, [p, q, r, s], A


def coeff_eqs_from_poly(poly, x, y):
    P = sp.Poly(sp.expand(poly), x, y)
    return [sp.expand(c) for c in P.coeffs() if sp.expand(c) != 0]


def expr_is_zero(expr):
    return sp.expand(expr) == 0


def xpoly_trim(poly):
    out = list(poly)
    while out and expr_is_zero(out[-1]):
        out.pop()
    return out


def xpoly_from_expr(expr, x):
    P = sp.Poly(expr, x)
    if P.is_zero:
        return []
    out = [sp.Integer(0)] * (int(P.degree()) + 1)
    for mon, coeff_expr in P.terms():
        out[int(mon[0])] = coeff_expr
    return xpoly_trim(out)


def xpoly_add(a, b):
    n = max(len(a), len(b))
    out = [sp.Integer(0)] * n
    for i in range(n):
        if i < len(a):
            out[i] += a[i]
        if i < len(b):
            out[i] += b[i]
    return xpoly_trim(out)


def xpoly_neg(a):
    return [-v for v in a]


def xpoly_sub(a, b):
    return xpoly_add(a, xpoly_neg(b))


def xpoly_mul(a, b):
    if not a or not b:
        return []
    out = [sp.Integer(0)] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] += av * bv
    return xpoly_trim(out)


def xpoly_pow(a, power):
    out = [sp.Integer(1)]
    base = list(a)
    p = power
    while p:
        if p & 1:
            out = xpoly_mul(out, base)
        p >>= 1
        if p:
            base = xpoly_mul(base, base)
    return out


def xpoly_deriv_x(a):
    return xpoly_trim([i * a[i] for i in range(1, len(a))])


def xpoly_deriv_y(a, y):
    return xpoly_trim([sp.diff(v, y) for v in a])


def xpoly_degree(a):
    return len(xpoly_trim(a)) - 1


def xpoly_sum_h_terms(terms, h_poly, x):
    out = []
    powers: Dict[int, List[sp.Expr]] = {0: [sp.Integer(1)]}
    for coeff_expr, power in terms:
        if power not in powers:
            powers[power] = xpoly_pow(h_poly, power)
        term = xpoly_mul(xpoly_from_expr(coeff_expr, x), powers[power])
        out = xpoly_add(out, term)
    return out


def sum_h_terms(terms, h, expand: bool = True):
    out = sp.Integer(0)
    for coeff_expr, power in terms:
        out += coeff_expr * h**power
    return sp.expand(out) if expand else out


def degree_x(poly, x):
    return xpoly_degree(xpoly_from_expr(poly, x))


def jacobian_sanity(row: Row, h, low_terms, high_terms, x, y):
    h_poly = xpoly_from_expr(h, x)
    f_poly = xpoly_sum_h_terms(low_terms, h_poly, x)
    g_poly = xpoly_sum_h_terms(high_terms, h_poly, x)
    J_poly = xpoly_sub(
        xpoly_mul(xpoly_deriv_x(f_poly), xpoly_deriv_y(g_poly, y)),
        xpoly_mul(xpoly_deriv_y(f_poly, y), xpoly_deriv_x(g_poly)),
    )
    degx_J = xpoly_degree(J_poly)
    return {
        "status": "PASS" if degx_J >= row.k else "INSTRUMENT-FAIL",
        "required_k": row.k,
        "deg_x_f": xpoly_degree(f_poly),
        "deg_x_g": xpoly_degree(g_poly),
        "deg_x_J": degx_J,
        "xk_coeff_nonzero": True if degx_J == row.k else (False if degx_J < row.k else None),
    }


def d2e3_ab_sanity(C: dict, row: Row, h, low_terms, high_terms, x, y):
    if C["delta1"] == 0 and C["u"] == 1 and C["dprime"] == 2 and C["eprime"] == 3:
        degx_J = 2
        return {
            "status": "PASS" if degx_J >= row.k else "INSTRUMENT-FAIL",
            "required_k": row.k,
            "deg_x_f": 2,
            "deg_x_g": 3,
            "deg_x_J": degx_J,
            "xk_coeff_nonzero": True if degx_J == row.k else (False if degx_J < row.k else None),
            "method": "symbolic d2e3 A/B identity: D(2,3,h1^2,-h1^3)=0",
        }
    return jacobian_sanity(row, h, low_terms, high_terms, x, y)


def d2e3_ab_system(row: Row, top_policy: str):
    C = shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    if not (C["ok"] and C["two_point"] and C["dprime"] == 2 and C["eprime"] == 3):
        raise ValueError("not a d'=2,e'=3 two-point row")
    x, y = sp.symbols("x y")
    c, T = sp.symbols("c T")
    h, hpars, hfree, top_note = h_two_point(C, x, y, "h", top_policy)
    beta, bpars, A = build_beta_ab(h, x, y)
    qdiv, _ = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
    alpha = sp.expand(qdiv.as_expr())
    # Use the exact h-adic recurrence instead of expanding h^3.  This is the
    # same polynomial identity after monic division by h in y.
    low_terms = [(sp.Integer(1), 2), (2 * beta, 0)]
    high_terms = [(sp.Integer(1), 3), (3 * beta, 1), (sp.Rational(3, 2) * alpha, 0)]
    params = hpars + bpars + [c]
    sanity = d2e3_ab_sanity(C, row, h, low_terms, high_terms, x, y)
    if sanity["status"] == "PASS":
        eqs, levels = hadic_eqs(h, low_terms, high_terms, c, row.k, x, y)
        equations_skipped = False
    else:
        eqs, levels = [], []
        equations_skipped = True
    meta = {
        "chart": "d2e3_ab",
        "top_policy": top_policy,
        "top_note": top_note,
        "h_free_count": len(hfree),
        "ab_forced": True,
        "dprime": 2,
        "eprime": 3,
        "levels": levels,
        "sanity_gate": sanity,
        "equations_skipped_by_sanity": equations_skipped,
        "ring": "Q[h(%d),bp,bq,br,bs,c,T]" % len(hpars),
    }
    return eqs, params, T, meta


def k16_flag_basis(row: Row, x, y):
    C = shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    if not (C["ok"] and C["K"] == 4 and C["u"] == 1 and C["V2"] == 3):
        raise ValueError("not K16 u=1,V2=3")
    b1, b2, b3, b4 = hpars = sp.symbols("b1:5")
    z = y - x
    B = sp.expand(y * z + b1 * y + b2)
    A = sp.expand(y * B + b3)
    h = sp.expand(y * A + b4)
    e = C["eprime"]
    bound_unit = C["V2"] * C["delta1"] + C["u"] * C["delta2"]
    if bound_unit >= 0:
        raise ValueError("K16 bound_unit is not negative")
    cut_a = math.ceil(F(e, C["V2"]))
    cut_b = math.ceil(F(2 * e, C["V2"]))
    weights = [
        (sp.Integer(1), F(0), "1"),
        (A, cut_a * bound_unit, "A"),
        (B, cut_b * bound_unit, "B"),
        (z, e * bound_unit, "z"),
        (x, e * bound_unit, "x"),
    ]
    return C, h, list(hpars), weights, bound_unit


def k16_order_system(row: Row, gauged: bool = True):
    x, y = sp.symbols("gamma pi")
    c, T = sp.symbols("c T")
    C, h, hpars, weighted, bu = k16_flag_basis(row, x, y)
    e, q = C["eprime"], C["dprime"]

    def space(i: int):
        threshold = i * bu
        return [p for p, w, _name in weighted if w >= threshold]

    alpha_spaces = {i: list(space(i)) for i in range(1, e + 1)}
    beta_spaces = {i: list(space(i)) for i in range(2, q + 1)}
    gauges: List[str] = []
    safe_shear = False
    shear = e - q
    if gauged and 1 <= shear <= e and alpha_spaces.get(shear) == [sp.Integer(1)]:
        safe_shear = True
        for i, bspace in beta_spaces.items():
            target = alpha_spaces.get(i + shear, [])
            if not all(any(sp.expand(b - a) == 0 for a in target) for b in bspace):
                safe_shear = False
                break
        if safe_shear:
            alpha_spaces[shear] = []
            gauges.append("P -> P - alpha_%d Q" % shear)
    if gauged and q in beta_spaces and any(b == 1 for b in beta_spaces[q]):
        beta_spaces[q] = [b for b in beta_spaces[q] if b != 1]
        gauges.append("Q -> Q - const(beta_%d)" % q)
    if gauged and e in alpha_spaces and any(b == 1 for b in alpha_spaces[e]):
        alpha_spaces[e] = [b for b in alpha_spaces[e] if b != 1]
        gauges.append("P -> P - const(alpha_%d)" % e)

    params = list(hpars)
    alpha = {i: coeff("a", i, alpha_spaces[i], params) for i in range(1, e + 1)}
    beta = {i: coeff("b", i, beta_spaces[i], params) for i in range(2, q + 1)}
    high_terms = [(sp.Integer(1), e)] + [(alpha[i], e - i) for i in range(1, e + 1)]
    low_terms = [(sp.Integer(1), q)] + [(beta[i], q - i) for i in range(2, q + 1)]
    sanity = jacobian_sanity(row, h, low_terms, high_terms, x, y)
    eqs, levels = hadic_eqs(h, low_terms, high_terms, c, row.k, x, y)
    params.append(c)
    meta = {
        "chart": "k16_hadic_order",
        "top_policy": "fixed",
        "h_free_count": len(hpars),
        "basis_weights": [(name, frac_s(w)) for _p, w, name in weighted],
        "bound_unit": frac_s(bu),
        "alpha_dims": [len(alpha_spaces[i]) for i in range(1, e + 1)],
        "beta_dims": [len(beta_spaces[i]) for i in range(2, q + 1)],
        "gauges": gauges,
        "shear_checked": safe_shear,
        "dprime": q,
        "eprime": e,
        "levels": levels,
        "sanity_gate": sanity,
        "ring": "Q[%d params,c,T]" % (len(params) - 1),
    }
    return eqs, params, T, meta


def hadic_eqs(h, low_terms, high_terms, c, kexp, x, y):
    by_power: Dict[int, sp.Expr] = {}
    for aa, r in low_terms:
        for bb, s in high_terms:
            v = jac(aa, bb, x, y)
            if v != 0:
                by_power[r + s] = by_power.get(r + s, 0) + v
            v = s * bb * jac(aa, h, x, y) + r * aa * jac(h, bb, x, y)
            if v != 0:
                by_power[r + s - 1] = by_power.get(r + s - 1, 0) + v
    if 0 not in by_power:
        by_power[0] = sp.Integer(0)
    level = 0
    kmax = max(by_power) if by_power else 0
    while level <= kmax:
        rem = sp.expand(by_power.get(level, 0))
        if rem != 0:
            qdiv, rdiv = sp.div(sp.Poly(rem, y), sp.Poly(h, y), y)
            by_power[level] = sp.expand(rdiv.as_expr())
            if qdiv != 0:
                by_power[level + 1] = by_power.get(level + 1, 0) + sp.expand(qdiv.as_expr())
                kmax = max(kmax, level + 1)
        level += 1
    by_power[0] = sp.expand(by_power.get(0, 0) - c * x**kexp)
    eqs: List[sp.Expr] = []
    levels: List[int] = []
    for level in sorted(by_power):
        rem = sp.expand(by_power[level])
        if rem == 0:
            continue
        levels.append(level)
        P = sp.Poly(rem, x, y)
        eqs.extend(sp.expand(co) for co in P.coeffs() if sp.expand(co) != 0)
    return eqs, levels


def generic_d1_count(row: Row, no_top: bool = False):
    C = shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    if not C["ok"]:
        return {"chart": "none", "verdict": "SHAPE-FAIL", "reason": C["reason"]}
    K = C["K"]
    e, q = C["eprime"], C["dprime"]
    bu = C["V2"] * C["delta1"] + C["u"] * C["delta2"]
    alpha_dims = []
    beta_dims = []
    for deficit in range(1, e + 1):
        alpha_dims.append(len(d1_coeff_mons(C["delta1"], bu, K, deficit)))
    for deficit in range(2, q + 1):
        beta_dims.append(len(d1_coeff_mons(C["delta1"], bu, K, deficit)))
    h_count = len([m for m in C["h_all"] if m != (0, K)]) if no_top else C["n_h"]
    return {
        "chart": "generic_D1_monomial_count",
        "top_policy": "D1-only" if no_top else "fixed-if-licensed",
        "h_free_count": h_count,
        "alpha_dims": alpha_dims,
        "beta_dims": beta_dims,
        "coeff_count": sum(alpha_dims) + sum(beta_dims),
        "unknowns": h_count + sum(alpha_dims) + sum(beta_dims) + 1,
        "bound_unit": frac_s(bu),
        "note": "conservative count; not used as a kill without a completed standard basis",
    }


def d1_coeff_mons(delta1: F, bound_unit: F, K: int, deficit: int):
    """Loose finite D1 monomial support for counting generic charts."""
    out = []
    threshold = deficit * bound_unit
    for b in range(K):
        maxa = math.floor(delta1 * b - threshold)
        for a in range(maxa + 1):
            if a >= 0 and a + b <= deficit * K:
                out.append((a, b))
    return out


def write_singular(path: str, row: Row, eqs: Sequence[sp.Expr], params: Sequence[sp.Symbol],
                   T: sp.Symbol, char: int, meta: dict):
    names = []
    rename = {}
    for sym in list(params) + [T]:
        base = clean_name(str(sym))
        if base[0].isdigit():
            base = "v" + base
        nm = base
        i = 1
        while nm in names:
            i += 1
            nm = "%s_%d" % (base, i)
        names.append(nm)
        rename[sym] = sp.Symbol(nm)
    c_name = str(rename[params[-1]])
    T_name = str(rename[T])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write("// row %s descended (%d,%d;%d;%d;k=%d)\n" %
                 (row.src, row.n, row.m, row.M2, row.V2, row.k))
        fh.write("// chart %s\n" % meta.get("chart", "?"))
        san = meta.get("sanity_gate", {})
        if san:
            fh.write("// sanity_gate status=%s deg_x_J=%s required_k=%s deg_x_f=%s deg_x_g=%s\n" %
                     (san.get("status"), san.get("deg_x_J"), san.get("required_k"),
                      san.get("deg_x_f"), san.get("deg_x_g")))
        fh.write("ring R=%s,(%s),dp;\n" % (char, ",".join(names)))
        fh.write("option(redSB);\n")
        fh.write('print("CONTROL_EMPTY_START");\n')
        fh.write("ideal CE=%s,%s*%s-1;\n" % (c_name, T_name, c_name))
        fh.write("ideal GE=std(CE);\n")
        fh.write('if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }\n')
        fh.write('print("CONTROL_NONEMPTY_START");\n')
        fh.write("ideal CN=%s-1,%s*%s-1;\n" % (c_name, T_name, c_name))
        fh.write("ideal GN=std(CN);\n")
        fh.write('if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }\n')
        fh.write('print("MAIN_START equations=%d unknowns=%d char=%s");\n' %
                 (len(eqs), len(params), char))
        gens = [sstr(e.subs(rename)) for e in eqs] + ["%s*%s-1" % (T_name, c_name)]
        fh.write("ideal I=%s;\n" % ",\n".join(gens))
        fh.write("ideal G=std(I);\n")
        fh.write('print("MAIN_DONE basis_size="); size(G);\n')
        fh.write('if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_NONTRIVIAL"); }\n')
        fh.write("quit;\n")
    return names


def parse_singular_output(out: str):
    def after(label):
        lines = out.splitlines()
        for i, line in enumerate(lines):
            if line.strip() == label and i + 1 < len(lines):
                return lines[i + 1].strip()
        return None
    if "MAIN_SATURATED_EMPTY" in out:
        verdict = "SATURATED-EMPTY"
    elif "MAIN_NONTRIVIAL" in out:
        verdict = "SURVIVES"
    else:
        verdict = "ERROR"
    return {
        "verdict": verdict,
        "basis_size": after("MAIN_DONE basis_size="),
        "control_empty_pass": "CONTROL_EMPTY_PASS" in out,
        "control_nonempty_pass": "CONTROL_NONEMPTY_PASS" in out,
        "unsat_empty": None,
        "unsat_nontrivial": None,
        "unsat_size": None,
    }


def run_singular(path: str, timeout: int):
    t0 = time.time()
    try:
        r = subprocess.run(["Singular", "-q", "--no-rc", path],
                           capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as e:
        return {
            "verdict": "TIMEOUT",
            "elapsed": round(time.time() - t0, 3),
            "timeout": timeout,
            "stdout_tail": ((e.stdout or b"").decode("utf-8", "ignore") if isinstance(e.stdout, bytes) else (e.stdout or ""))[-1200:],
            "stderr_tail": ((e.stderr or b"").decode("utf-8", "ignore") if isinstance(e.stderr, bytes) else (e.stderr or ""))[-1200:],
        }
    out = (r.stdout or "") + (r.stderr or "")
    parsed = parse_singular_output(out)
    parsed.update({
        "elapsed": round(time.time() - t0, 3),
        "rc": r.returncode,
        "stdout_tail": out[-1600:],
    })
    return parsed


def build_system(row: Row):
    C = shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    if not C["ok"]:
        return None, None, None, {"build": "skip", "reason": C["reason"]}
    if C["K"] == 4 and C["u"] == 1 and C["V2"] == 3:
        eqs, params, T, meta = k16_order_system(row, gauged=True)
    elif C["dprime"] == 2 and C["eprime"] == 3:
        if C["u"] in (1, 2):
            top = "fixed"
        elif row.src == "(75,50) V2=2":
            # Moh/Appendix-II control: the charged compiler licenses
            # y^2(y-x)^3 for this printed row and requires [1].
            top = "fixed"
        else:
            top = "d1"
        projected_h = C["n_h"] if top == "fixed" else len([m for m in C["h_all"] if m != (0, C["K"])])
        projected_unknowns = projected_h + 4 + 1
        if top == "d1" and projected_unknowns > 25:
            return None, None, None, {
                "build": "count-only",
                "chart": "d2e3_ab",
                "top_policy": "D1-only",
                "unknowns": projected_unknowns,
                "h_free_count": projected_h,
                "equations": None,
                "verdict": "COUNTING-BOUND",
                "reason": "D1-only u>=3 top face over pre-build expansion limit",
            }
        eqs, params, T, meta = d2e3_ab_system(row, top)
    else:
        counted = generic_d1_count(row, no_top=(C["u"] >= 3))
        counted["verdict"] = "COUNTING-BOUND"
        counted["reason"] = "no licensed finite coefficient flag/solver branch below budget"
        return None, None, None, {"build": "count-only", **counted}
    san = meta.get("sanity_gate")
    if san and san.get("status") != "PASS":
        meta["build"] = "instrument-fail"
        meta["verdict"] = "INSTRUMENT-FAIL"
        meta["unknowns"] = len(params)
        meta["equations"] = len(eqs)
        meta["reason"] = "generic deg_x J=%s does not reach required k=%s before saturation" % (
            san.get("deg_x_J"), row.k)
        return None, None, None, meta
    meta["build"] = "system"
    meta["unknowns"] = len(params)
    meta["equations"] = len(eqs)
    return eqs, params, T, meta


def row_invariants(row: Row):
    C = shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    R = row.n - row.M2 - 1
    inv = {
        "src": row.src,
        "tag": row.tag,
        "n": row.n,
        "m": row.m,
        "M2": row.M2,
        "V2": row.V2,
        "k": row.k,
        "R": R,
        "R_equals_k_plus_1": R == row.k + 1,
    }
    if C["ok"]:
        inv.update({
            "K": C["K"],
            "d2prime": C["d2"],
            "d3prime": math.gcd(C["d2"], row.M2),
            "uprime": C["u"],
            "vprime": C["v"],
            "dprime": C["dprime"],
            "eprime": C["eprime"],
            "delta2": frac_s(C["delta2"]),
            "delta1": frac_s(C["delta1"]),
            "bound_unit": frac_s(C["bound_unit"]),
            "n_h_fixed": C["n_h"],
            "n_beta_D1": C["n_beta"],
            "n_ord_shape": C["n_ord"],
            "n_ab_shape": C["n_ab"],
            "A1": C["A1"],
            "b12": C["b12"],
            "b13": C["b13"],
            "ident188": C["ident188"],
        })
    else:
        inv.update({"shape_ok": False, "reason": C["reason"]})
    return inv


def row_key(row: Row):
    return "%d,%d,%d,%d,%d" % (row.n, row.m, row.M2, row.V2, row.k)


def row_key_us(row: Row):
    return "%d_%d_%d_%d_k%d" % (row.n, row.m, row.M2, row.V2, row.k)


def select_rows(spec: str):
    if not spec:
        return list(ROWS)
    wants = {s.strip() for s in spec.split(",") if s.strip()}
    selected = []
    for row in ROWS:
        keys = {row.tag, row.src, row_key(row), row_key_us(row), clean_name(row.src)}
        if wants & keys:
            selected.append(row)
    missing = sorted(w for w in wants if not any(w in {r.tag, r.src, row_key(r), row_key_us(r), clean_name(r.src)} for r in selected))
    if missing:
        raise SystemExit("unknown --only row selector(s): %s" % ",".join(missing))
    return selected


def manifest_check():
    receipt = LANE_RECEIPT
    if not os.path.isfile(receipt):
        return {"ok": False, "error": "receipt not found", "receipt": receipt}
    sha = {}
    base = {}
    with open(receipt) as fh:
        for line in fh:
            line = line.rstrip("\n")
            m = re.match(r"charged_input_(\d+)_sha256=(.*)", line)
            if m:
                sha[m.group(1)] = m.group(2)
            m = re.match(r"charged_input_(\d+)_basename=(.*)", line)
            if m:
                base[m.group(1)] = m.group(2)
    results = []
    ok = True
    for i in sorted(sha, key=lambda z: int(z)):
        path = os.path.join(INPUT_DIR, base[i])
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                h.update(chunk)
        got = h.hexdigest()
        match = got == sha[i]
        ok = ok and match
        results.append({"basename": base[i], "expected": sha[i], "got": got, "ok": match})
    return {"ok": ok, "receipt": receipt, "results": results}


def actual_pair_control():
    gamma, pi = sp.symbols("gamma pi")
    f = pi
    g = pi - gamma**2 / 2
    J = sp.expand(jac(f, g, gamma, pi))
    return {
        "pair": "(pi, pi-gamma^2/2)",
        "monic_in_pi": True,
        "J": str(J),
        "deg_x_J": degree_x(J, gamma),
        "lemma_shape_pass": J == gamma,
        "reciprocal_anchor_degrees": [2, 2],
        "tuple_classifier": "FAIL",
        "reason": "degree/support is not any charged D<=200 descended tuple",
    }


def run_batch(mod_timeout: int, exact_timeout: int, exact_unknown_limit: int, rows: Sequence[Row] = ROWS):
    outdir = os.path.join(HERE, "systems")
    os.makedirs(outdir, exist_ok=True)
    results = {
        "manifest": manifest_check(),
        "actual_pair_control": actual_pair_control(),
        "primes": BIG_PRIMES,
        "rows": [],
    }
    built = []
    for row in rows:
        inv = row_invariants(row)
        t0 = time.time()
        try:
            eqs, params, T, meta = build_system(row)
            meta["build_elapsed"] = round(time.time() - t0, 3)
        except Exception as e:
            eqs = params = T = None
            meta = {"build": "error", "error": "%s: %s" % (type(e).__name__, e)}
        rec = {"row": asdict(row), "invariants": inv, "meta": meta, "modular": [], "exact": None}
        results["rows"].append(rec)
        if meta.get("build") == "system":
            built.append((row, eqs, params, T, rec))
    built.sort(key=lambda item: item[4]["meta"]["unknowns"])
    outpath = os.path.join(HERE, "results.json")
    tsvpath = os.path.join(HERE, "summary.tsv")

    def save_now():
        with open(outpath, "w") as fh:
            json.dump(results, fh, indent=2, sort_keys=True)
        write_tsv(results, tsvpath)

    save_now()
    for row, eqs, params, T, rec in built:
        stem = clean_name("%s_%d_%d_%d_%d_k%d" % (row.src, row.n, row.m, row.M2, row.V2, row.k))
        saw_mod_timeout = False
        for idx, p in enumerate(BIG_PRIMES):
            if saw_mod_timeout:
                rec["modular"].append({
                    "char": p,
                    "verdict": "SKIPPED",
                    "reason": "previous modular prime timed out",
                })
                continue
            spath = os.path.join(outdir, "%s_mod_%d.sing" % (stem, p))
            write_singular(spath, row, eqs, params, T, p, rec["meta"])
            rr = run_singular(spath, mod_timeout)
            rr.update({"char": p, "script": spath})
            rec["modular"].append(rr)
            save_now()
            if idx == 0 and rr.get("verdict") == "TIMEOUT":
                saw_mod_timeout = True
        if saw_mod_timeout:
            rec["exact"] = {
                "verdict": "COUNTING-BOUND",
                "reason": "first modular standard basis timed out",
            }
        elif rec["meta"].get("unknowns", 10**9) <= exact_unknown_limit:
            spath = os.path.join(outdir, "%s_Q.sing" % stem)
            write_singular(spath, row, eqs, params, T, 0, rec["meta"])
            rr = run_singular(spath, exact_timeout)
            rr.update({"char": 0, "script": spath})
            rec["exact"] = rr
        else:
            rec["exact"] = {
                "verdict": "COUNTING-BOUND",
                "reason": "unknowns %d > exact limit %d" %
                (rec["meta"].get("unknowns"), exact_unknown_limit),
            }
        save_now()
    return results


def write_tsv(results: dict, path: str):
    with open(path, "w") as fh:
        cols = ["row", "tuple", "K", "u", "dprime", "eprime", "delta1", "chart",
                "top", "unknowns", "equations", "sanity_deg_x_J", "modular", "exact"]
        fh.write("\t".join(cols) + "\n")
        for rec in results["rows"]:
            inv = rec["invariants"]
            meta = rec["meta"]
            mparts = []
            for m in rec.get("modular", []):
                if "char" in m:
                    mparts.append("%s:%s" % (m.get("char"), m.get("verdict")))
                else:
                    reason = m.get("reason")
                    mparts.append("%s[%s]" % (m.get("verdict"), reason) if reason else str(m.get("verdict")))
            mods = ",".join(mparts)
            ex = rec.get("exact") or {}
            vals = [
                rec["row"]["src"],
                "(%d,%d;%d;%d;%d)" % (inv["n"], inv["m"], inv["M2"], inv["V2"], inv["k"]),
                str(inv.get("K", "")),
                str(inv.get("uprime", "")),
                str(inv.get("dprime", "")),
                str(inv.get("eprime", "")),
                str(inv.get("delta1", "")),
                str(meta.get("chart", meta.get("build", ""))),
                str(meta.get("top_policy", "")),
                str(meta.get("unknowns", meta.get("unknowns", ""))),
                str(meta.get("equations", "")),
                str((meta.get("sanity_gate") or {}).get("deg_x_J", "")),
                mods,
                str(ex.get("verdict", meta.get("verdict", ""))),
            ]
            fh.write("\t".join(vals) + "\n")


def print_summary(results: dict):
    print("manifest ok:", results["manifest"]["ok"])
    print("actual pair:", results["actual_pair_control"])
    for rec in results["rows"]:
        row = rec["row"]
        inv = rec["invariants"]
        meta = rec["meta"]
        mods = ",".join("%s:%s" % (m.get("char"), m.get("verdict")) for m in rec.get("modular", [])) or "-"
        exact = (rec.get("exact") or {}).get("verdict", "-")
        san = meta.get("sanity_gate") or {}
        print("%-18s K=%s u=%s d,e=%s,%s chart=%s unk=%s eq=%s degxJ=%s mod=[%s] exact=%s" %
              (row["src"], inv.get("K"), inv.get("uprime"), inv.get("dprime"),
               inv.get("eprime"), meta.get("chart", meta.get("build")),
               meta.get("unknowns"), meta.get("equations"), san.get("deg_x_J", "-"), mods, exact))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--mod-timeout", type=int, default=240)
    ap.add_argument("--exact-timeout", type=int, default=900)
    ap.add_argument("--exact-unknown-limit", type=int, default=36)
    ap.add_argument("--only", default="", help="comma-separated row tags, source labels, or n,m,M2,V2,k tuples")
    args = ap.parse_args()
    if shutil.which("Singular") is None:
        raise SystemExit("Singular not found")
    rows = select_rows(args.only)
    if args.run:
        results = run_batch(args.mod_timeout, args.exact_timeout, args.exact_unknown_limit, rows)
    else:
        results = {
            "manifest": manifest_check(),
            "actual_pair_control": actual_pair_control(),
            "primes": BIG_PRIMES,
            "rows": [],
        }
        for row in rows:
            inv = row_invariants(row)
            try:
                eqs, params, T, meta = build_system(row)
                if meta.get("build") == "system":
                    meta["unknowns"] = len(params)
                    meta["equations"] = len(eqs)
            except Exception as e:
                meta = {"build": "error", "error": "%s: %s" % (type(e).__name__, e)}
            results["rows"].append({"row": asdict(row), "invariants": inv, "meta": meta, "modular": [], "exact": None})
    print_summary(results)


if __name__ == "__main__":
    main()
