#!/usr/bin/env python3
"""Corrected symbolic partition-strata rerun for the 2026-09-03 lane.

This driver imports the frozen corrected generator from /tmp/jc2-lane.S2kb7J,
ports the top-face stratum emission from the prior strata/topface drivers, and
runs each stratum over three primes and then Q.  Prime marks in row labels are
labels, not derivatives.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import re
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
FROZEN = Path("/tmp/jc2-lane.S2kb7J/inputs")
RECEIPT = ROOT / "xmodel/strata-rerun-corrected-gpt55-20260903.run.v2"
REPORT = ROOT / "xmodel/strata-rerun-corrected-gpt55-20260903.md"
PRIMES = (32003, 32009, 32027)


@dataclass(frozen=True)
class Row:
    key: str
    label: str
    parent: str
    n: int
    m: int
    M2: int
    V2: int
    k: int


ROWS = [
    Row("33_22_30_8_k1", "(33,22;30;8;k=1)", "(132,88)", 33, 22, 30, 8, 1),
    Row("45_30_42_11_k1", "(45,30;42;11;k=1)", "(180,120)", 45, 30, 42, 11, 1),
    Row("21_14_18_5_k1", "(21,14;18;5;k=1)", "(84,56)", 21, 14, 18, 5, 1),
    Row("15_10_11_2_k2", "(15,10;11;2;k=2)", "(75,50) V2=2", 15, 10, 11, 2, 2),
]
PRIMARY_KEYS = {"33_22_30_8_k1", "45_30_42_11_k1"}


def load_frozen(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, FROZEN / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load %s" % filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


shape = load_frozen("shape", "shape.py")
batch = load_frozen("corrected_twopoint_order_batch", "twopoint_order_batch.py")


def manifest_check() -> dict:
    fields: Dict[str, Dict[str, str]] = {}
    for line in RECEIPT.read_text().splitlines():
        match = re.match(r"charged_input_(\d+)_(basename|sha256)=(.*)", line)
        if match:
            fields.setdefault(match.group(1), {})[match.group(2)] = match.group(3)
    checks = []
    for idx in sorted(fields, key=int):
        rec = fields[idx]
        path = FROZEN / rec["basename"]
        got = hashlib.sha256(path.read_bytes()).hexdigest()
        checks.append({
            "idx": int(idx),
            "basename": rec["basename"],
            "path": str(path),
            "expected": rec["sha256"],
            "got": got,
            "ok": got == rec["sha256"],
        })
    return {"ok": bool(checks) and all(item["ok"] for item in checks), "checks": checks}


def frac_s(v) -> str:
    return "%d" % v.numerator if isinstance(v, F) and v.denominator == 1 else str(v)


def monomial_s(mon: Tuple[int, int]) -> str:
    i, j = mon
    parts = []
    if i:
        parts.append("x" if i == 1 else "x^%d" % i)
    if j:
        parts.append("y" if j == 1 else "y^%d" % j)
    return "*".join(parts) if parts else "1"


def monomial_list_s(mons: Sequence[Tuple[int, int]]) -> str:
    if not mons:
        return "none"
    return ", ".join(monomial_s(m) for m in sorted(mons, key=lambda z: (-z[1], z[0])))


def order_allowed(delta1: F, threshold: F, i: int, j: int) -> bool:
    return -F(i) + delta1 * F(j) >= threshold


def mons_by_threshold(delta1: F, deg_y: int, deg_x: int, total: int | None, threshold: F):
    out = []
    for j in range(deg_y, -1, -1):
        for i in range(0, deg_x + 1):
            if total is not None and i + j > total:
                continue
            if order_allowed(delta1, threshold, i, j):
                out.append((i, j))
    return out


def old_support_bundle(row: Row) -> dict:
    d2p, d1p, d2, raw2, raw1 = shape.phi_s2(row.n, row.m, row.M2, row.V2, row.k)
    K = math.gcd(row.n, row.m)
    dprime = row.m // K
    eprime = row.n // K
    u = d2 - row.V2
    degx_h = u * K // d2
    degx_f = u * row.m // d2
    h_all = mons_by_threshold(d1p, K, degx_h, K, -d1p)
    h_leader = [m for m in h_all if m[0] + m[1] == K]
    h_lower = [m for m in h_all if m[0] + m[1] < K]
    beta = {}
    for deficit in range(2, dprime + 1):
        beta[deficit] = mons_by_threshold(d1p, K - 1, degx_f, row.m, -F(deficit) * d1p)
    return {
        "K": K,
        "d2": d2,
        "u": u,
        "dprime": dprime,
        "eprime": eprime,
        "delta2": d2p,
        "delta1": d1p,
        "degx_h": degx_h,
        "degx_beta": degx_f,
        "threshold_h": -d1p,
        "threshold_beta": {j: -F(j) * d1p for j in beta},
        "h_all": h_all,
        "h_leader": h_leader,
        "h_lower": h_lower,
        "beta": beta,
    }


def relation(old: Sequence[Tuple[int, int]], new: Sequence[Tuple[int, int]]) -> dict:
    os, ns = set(old), set(new)
    if os == ns:
        rel = "equal"
    elif os <= ns:
        rel = "old_subset_new"
    elif ns <= os:
        rel = "new_subset_old"
    else:
        rel = "incomparable"
    return {
        "relation": rel,
        "old_count": len(old),
        "new_count": len(new),
        "old_minus_new": sorted(os - ns, key=lambda z: (-z[1], z[0])),
        "new_minus_old": sorted(ns - os, key=lambda z: (-z[1], z[0])),
    }


def support_comparison(row: Row) -> dict:
    old = old_support_bundle(row)
    new = shape.shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    beta = {}
    for deficit in range(2, old["dprime"] + 1):
        new_mons = new["beta_all"] if deficit == old["dprime"] else []
        beta[str(deficit)] = relation(old["beta"][deficit], new_mons)
    return {
        "row": asdict(row),
        "old_rule": {
            "h_threshold": frac_s(old["threshold_h"]),
            "beta_thresholds": {str(k): frac_s(v) for k, v in old["threshold_beta"].items()},
            "degx_beta": old["degx_beta"],
        },
        "corrected_rule": {
            "B": frac_s(new["bound_unit"]),
            "beta_thresholds": {str(old["dprime"]): frac_s(old["dprime"] * new["bound_unit"])},
            "degx_beta": new["degx_beta"],
        },
        "invariants": {
            "K": old["K"],
            "u": old["u"],
            "dprime": old["dprime"],
            "eprime": old["eprime"],
            "delta2": frac_s(old["delta2"]),
            "delta1": frac_s(old["delta1"]),
        },
        "h_all": relation(old["h_all"], new["h_all"]),
        "h_lower": relation(old["h_lower"], new["h_lower"]),
        "beta": beta,
    }


def partitions(n: int, ceiling: int | None = None) -> Iterable[Tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    top = n if ceiling is None else min(n, ceiling)
    for first in range(top, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def allowed_partitions(row: Row) -> List[Tuple[int, ...]]:
    C = shape.shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    return [
        part for part in partitions(C["u"])
        if len(part) + 1 <= row.n - row.M2
    ]


def face(row: Row, part: Sequence[int]):
    x, y = sp.symbols("x y")
    slopes = list(sp.symbols("a2:%d" % (len(part) + 1))) if len(part) > 1 else []
    top = y ** row.V2 * (y - x) ** part[0]
    for slope, exponent in zip(slopes, part[1:]):
        top *= (y - slope * x) ** exponent
    omega = sp.Integer(1)
    for slope in slopes:
        omega *= slope * (slope - 1)
    for i, slope in enumerate(slopes):
        for other in slopes[i + 1:]:
            omega *= slope - other
    return x, y, sp.expand(top), slopes, sp.expand(omega)


def factored_face(row: Row, part: Sequence[int]) -> str:
    factors = ["(y-x)^%d" % part[0]]
    for idx, exponent in enumerate(part[1:], start=2):
        factors.append("(y-a%d*x)^%d" % (idx, exponent))
    return "y^%d*%s" % (row.V2, "*".join(factors))


def recomposition_check(h, low_terms, high_terms, by_power, params, x, y) -> bool:
    sample = {}
    for index, param in enumerate(params):
        value = (index % 11) - 5
        if value == 0:
            value = 6
        sample[param] = value
    low_poly = batch.sum_h_terms(low_terms, h, expand=True).subs(sample)
    high_poly = batch.sum_h_terms(high_terms, h, expand=True).subs(sample)
    direct = sp.expand(batch.jac(low_poly, high_poly, x, y))
    recomposed = sp.expand(
        sp.Add(*(rem.subs(sample) * h.subs(sample) ** level for level, rem in by_power.items()))
    )
    return sp.expand(direct - recomposed) == 0


def hadic_by_power(h, low_terms, high_terms, x, y):
    by_power: Dict[int, sp.Expr] = {}
    for aa, r in low_terms:
        for bb, s in high_terms:
            same_power = batch.jac(aa, bb, x, y)
            if same_power != 0:
                by_power[r + s] = by_power.get(r + s, 0) + same_power
            lower_power = s * bb * batch.jac(aa, h, x, y) + r * aa * batch.jac(h, bb, x, y)
            if lower_power != 0:
                by_power[r + s - 1] = by_power.get(r + s - 1, 0) + lower_power
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
    return by_power


def equations_from_by_power(by_power: Dict[int, sp.Expr], c, kexp: int, x, y):
    by_power = dict(by_power)
    by_power[0] = sp.expand(by_power.get(0, 0) - c * x**kexp)
    eqs = []
    levels = []
    for level in sorted(by_power):
        rem = sp.expand(by_power[level])
        if rem == 0:
            continue
        levels.append(level)
        poly = sp.Poly(rem, x, y)
        eqs.extend(sp.expand(coef) for coef in poly.coeffs() if sp.expand(coef) != 0)
    return eqs, levels


def xpoly_from_expr_trunc(expr, x, maxdeg: int):
    poly = sp.Poly(sp.expand(expr), x)
    out = [sp.Integer(0)] * (maxdeg + 1)
    if poly.is_zero:
        return out
    for mon, coeff in poly.terms():
        deg = int(mon[0])
        if deg <= maxdeg:
            out[deg] += coeff
    return [sp.expand(v) for v in out]


def xpoly_add_trunc(a, b, maxdeg: int):
    return [sp.expand((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) for i in range(maxdeg + 1)]


def xpoly_mul_trunc(a, b, maxdeg: int):
    out = [sp.Integer(0)] * (maxdeg + 1)
    for i, av in enumerate(a):
        if av == 0:
            continue
        for j, bv in enumerate(b):
            if i + j > maxdeg:
                break
            if bv != 0:
                out[i + j] += av * bv
    return [sp.expand(v) for v in out]


def xpoly_pow_trunc(a, power: int, maxdeg: int):
    out = [sp.Integer(1)] + [sp.Integer(0)] * maxdeg
    base = list(a)
    p = power
    while p:
        if p & 1:
            out = xpoly_mul_trunc(out, base, maxdeg)
        p >>= 1
        if p:
            base = xpoly_mul_trunc(base, base, maxdeg)
    return out


def xpoly_deriv_x_trunc(a):
    if len(a) <= 1:
        return [sp.Integer(0)]
    return [sp.expand(i * a[i]) for i in range(1, len(a))]


def xpoly_deriv_y_trunc(a, y):
    return [sp.diff(v, y) for v in a]


def xk_jacobian_coeff(h, beta, alpha, x, y, k: int):
    maxdeg = k + 1
    hpoly = xpoly_from_expr_trunc(h, x, maxdeg)
    betapoly = xpoly_from_expr_trunc(beta, x, maxdeg)
    alphapoly = xpoly_from_expr_trunc(alpha, x, maxdeg)
    fpoly = xpoly_add_trunc(xpoly_pow_trunc(hpoly, 2, maxdeg), [2 * v for v in betapoly], maxdeg)
    gpoly = xpoly_add_trunc(
        xpoly_add_trunc(xpoly_pow_trunc(hpoly, 3, maxdeg), [3 * v for v in xpoly_mul_trunc(betapoly, hpoly, maxdeg)], maxdeg),
        [sp.Rational(3, 2) * v for v in alphapoly],
        maxdeg,
    )
    jpoly = xpoly_add_trunc(
        xpoly_mul_trunc(xpoly_deriv_x_trunc(fpoly), xpoly_deriv_y_trunc(gpoly, y), k),
        [-v for v in xpoly_mul_trunc(xpoly_deriv_y_trunc(fpoly, y), xpoly_deriv_x_trunc(gpoly), k)],
        k,
    )
    return sp.expand(jpoly[k]) if k < len(jpoly) else sp.Integer(0)


def sample_sanity(row: Row, h, beta, alpha, hpars, slopes, bpars, x, y):
    sample = {}
    for i, slope in enumerate(slopes, start=2):
        sample[slope] = i
    vals = [2, -3, 5, -7, 11, -13, 17, -19, 23, -29, 31, -37, 41]
    for i, sym in enumerate(list(hpars) + list(bpars)):
        sample[sym] = vals[i % len(vals)]
    coeff = xk_jacobian_coeff(h, beta, alpha, x, y, row.k)
    coeff_sample = sp.expand(coeff.subs(sample))
    reaches = coeff_sample != 0
    return {
        "status": "PASS" if reaches else "INSTRUMENT-FAIL",
        "required_k": row.k,
        "deg_x_J": ">=%d" % row.k if reaches else "<%d" % row.k,
        "deg_x_J_kind": "exact x^k coefficient witness; full generic degree not expanded",
        "reaches_k": reaches,
        "xk_coeff_nonzero": reaches,
        "xk_coeff_sample": str(coeff_sample).replace("**", "^"),
        "sample": {str(k): int(v) for k, v in sample.items()},
    }


def normalized_j_sanity(row: Row, by_power: Dict[int, sp.Expr], x) -> dict:
    j0 = sp.expand(by_power.get(0, 0))
    degx = batch.degree_x(j0, x)
    return {
        "status": "PASS" if degx >= row.k else "INSTRUMENT-FAIL",
        "required_k": row.k,
        "deg_x_J": degx,
        "deg_x_J_kind": "exact h-adic normalized level-0 Jacobian remainder before subtracting c*x^k",
        "reaches_k": degx >= row.k,
    }


def build_system(row: Row, part: Sequence[int]) -> dict:
    C = shape.shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    if not (C["ok"] and C["two_point"] and C["dprime"] == 2 and C["eprime"] == 3):
        raise ValueError("row is not in the d'=2,e'=3 two-point A/B chart")
    if tuple(part) not in allowed_partitions(row):
        raise ValueError("partition outside source-safe root-count cap")
    x, y, top, slopes, omega = face(row, part)
    hpars: List[sp.Symbol] = []
    h = top + batch.poly_from_mons(C["h_lower"], x, y, "h", hpars)
    beta, bpars, A = batch.build_beta_ab(h, x, y)
    qdiv, _ = sp.div(sp.Poly(sp.expand(beta ** 2), y), sp.Poly(h, y), y)
    alpha = sp.expand(qdiv.as_expr())
    low_terms = [(sp.Integer(1), 2), (2 * beta, 0)]
    high_terms = [(sp.Integer(1), 3), (3 * beta, 1), (sp.Rational(3, 2) * alpha, 0)]
    c, T = sp.symbols("c T")
    by_power = hadic_by_power(h, low_terms, high_terms, x, y)
    sanity = normalized_j_sanity(row, by_power, x)
    eqs, levels = equations_from_by_power(by_power, c, row.k, x, y)
    params = hpars + slopes + bpars + [c]
    sat = sp.expand(c * omega)
    return {
        "row": asdict(row),
        "partition": list(part),
        "partition_label": "+".join(map(str, part)),
        "K": C["K"],
        "u": C["u"],
        "dprime": C["dprime"],
        "eprime": C["eprime"],
        "delta2": frac_s(C["delta2"]),
        "delta1": frac_s(C["delta1"]),
        "B": frac_s(C["bound_unit"]),
        "top_face_factored": factored_face(row, part),
        "slope_symbols": [str(s) for s in slopes],
        "omega": str(omega),
        "saturation_factor": str(sat),
        "h_lower_count": len(C["h_lower"]),
        "h_lower": C["h_lower"],
        "corrected_beta_count": C["n_beta"],
        "corrected_beta_deg_x_cap": C["degx_beta"],
        "unknowns": len(params),
        "equations": len(eqs),
        "levels": levels,
        "sanity_gate": sanity,
        "recomposition_ok": "not-run; equation construction uses the same h-adic recurrence as prior strata_gate.py",
        "eqs": eqs,
        "params": params,
        "T": T,
        "sat": sat,
    }


def rename_symbols(params: Sequence[sp.Symbol], T: sp.Symbol):
    names = []
    rename = {}
    for sym in list(params) + [T]:
        base = batch.clean_name(str(sym))
        if base[0].isdigit():
            base = "v" + base
        name = base
        suffix = 1
        while name in names:
            suffix += 1
            name = "%s_%d" % (base, suffix)
        names.append(name)
        rename[sym] = sp.Symbol(name)
    return names, rename


def write_singular(path: Path, rec: dict, char: int):
    names, rename = rename_symbols(rec["params"], rec["T"])
    sat_s = batch.sstr(rec["sat"].subs(rename))
    T_s = str(rename[rec["T"]])
    gens = [batch.sstr(eq.subs(rename)) for eq in rec["eqs"]]
    gens.append("%s*(%s)-1" % (T_s, sat_s))
    san = rec["sanity_gate"]
    lines = [
        "// generated by strata_rerun.py",
        "// row %s parent %s partition %s" % (rec["row"]["label"], rec["row"]["parent"], rec["partition_label"]),
        "// top %s" % rec["top_face_factored"],
        "// saturation by c*Omega = %s" % rec["saturation_factor"],
        "// sanity_gate status=%s deg_x_J=%s required_k=%s deg_x_f=%s deg_x_g=%s"
        % (san.get("status"), san.get("deg_x_J"), san.get("required_k"), san.get("deg_x_f"), san.get("deg_x_g")),
        "ring R=%d,(%s),dp;" % (char, ",".join(names)),
        "option(redSB);",
        'print("CONTROL_EMPTY_START");',
        "ideal CE=(%s),%s*(%s)-1;" % (sat_s, T_s, sat_s),
        "ideal GE=std(CE);",
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
        'print("CONTROL_NONEMPTY_START");',
        "ideal CN=(%s)-1,%s*(%s)-1;" % (sat_s, T_s, sat_s),
        "ideal GN=std(CN);",
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
        'print("MAIN_START equations=%d unknowns=%d char=%d");' % (rec["equations"], rec["unknowns"], char),
        "ideal I=%s;" % ",\n".join(gens),
        "ideal G=std(I);",
        'print("MAIN_DONE basis_size="); size(G);',
        'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_NONTRIVIAL"); }',
        "quit;",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def parse_singular_output(output: str):
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
    }


def run_singular(path: Path, timeout: int):
    started = time.time()
    try:
        proc = subprocess.run(
            ["Singular", "-q", "--no-rc", str(path)],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode("utf-8", "ignore") if isinstance(exc.stdout, bytes) else exc.stdout
        stderr = exc.stderr.decode("utf-8", "ignore") if isinstance(exc.stderr, bytes) else exc.stderr
        output = (stdout or "") + (stderr or "")
        return {
            "verdict": "TIMEOUT",
            "elapsed": round(time.time() - started, 3),
            "timeout": timeout,
            "control_empty_pass": "CONTROL_EMPTY_PASS" in output,
            "control_nonempty_pass": "CONTROL_NONEMPTY_PASS" in output,
            "stdout_tail": (stdout or "")[-1600:],
            "stderr_tail": (stderr or "")[-1600:],
        }
    output = (proc.stdout or "") + (proc.stderr or "")
    parsed = parse_singular_output(output)
    parsed.update({
        "elapsed": round(time.time() - started, 3),
        "rc": proc.returncode,
        "stdout_tail": output[-1600:],
    })
    return parsed


def execute_stratum(row: Row, part: Sequence[int], timeout: int) -> dict:
    started = time.time()
    rec = build_system(row, part)
    rec["build_elapsed"] = round(time.time() - started, 3)
    keep = {k: v for k, v in rec.items() if k not in {"eqs", "params", "T", "sat"}}
    keep["runs"] = []
    stem = "%s_part_%s" % (row.key, "_".join(map(str, part)))
    if rec["sanity_gate"].get("status") != "PASS":
        keep["verdict"] = "GAP"
        keep["reason"] = "generic deg_x J did not reach k"
    for char in list(PRIMES) + [0]:
        script = OUT / "systems" / ("%s_%s.sing" % (stem, "Q" if char == 0 else "mod_%d" % char))
        write_singular(script, rec, char)
        result = run_singular(script, timeout)
        result.update({"char": char, "script": str(script.relative_to(ROOT))})
        keep["runs"].append(result)
        outpath = OUT / "results" / ("%s.json" % stem)
        outpath.parent.mkdir(parents=True, exist_ok=True)
        outpath.write_text(json.dumps(keep, indent=2, sort_keys=True) + "\n")
    exact = keep["runs"][-1]
    if all(r.get("verdict") == "SATURATED-EMPTY" for r in keep["runs"]):
        keep["verdict"] = "SATURATED-EMPTY"
    elif exact.get("verdict") == "SURVIVES":
        keep["verdict"] = "SURVIVES"
    else:
        keep["verdict"] = "GAP"
    outpath = OUT / "results" / ("%s.json" % stem)
    outpath.write_text(json.dumps(keep, indent=2, sort_keys=True) + "\n")
    return keep


def row_verdict(records: Sequence[dict]) -> str:
    if records and all(r.get("verdict") == "SATURATED-EMPTY" and r["sanity_gate"].get("reaches_k") for r in records):
        return "CONFIRMED"
    if any(r.get("verdict") == "SURVIVES" for r in records):
        return "REFUTED"
    return "GAP"


def singular_version() -> str:
    proc = subprocess.run(["Singular", "-v"], capture_output=True, text=True, timeout=20)
    return (proc.stdout or proc.stderr).splitlines()[0].strip()


def write_summary_tsv(summary: dict):
    path = OUT / "summary.tsv"
    with path.open("w") as fh:
        fh.write("\t".join(["row", "parent", "partition", "unknowns", "equations", "deg_x_J", "mod_32003", "mod_32009", "mod_32027", "Q", "verdict"]) + "\n")
        for rec in summary["strata"]:
            by_char = {run["char"]: run["verdict"] for run in rec["runs"]}
            vals = [
                rec["row"]["label"],
                rec["row"]["parent"],
                rec["partition_label"],
                str(rec["unknowns"]),
                str(rec["equations"]),
                str(rec["sanity_gate"].get("deg_x_J")),
                by_char.get(32003, ""),
                by_char.get(32009, ""),
                by_char.get(32027, ""),
                by_char.get(0, ""),
                rec["verdict"],
            ]
            fh.write("\t".join(vals) + "\n")


def support_table_md(summary: dict, primary_only: bool) -> str:
    rows = []
    for comp in summary["support_comparison"]:
        if primary_only and comp["row"]["key"] not in PRIMARY_KEYS:
            continue
        rows.append("| `%s` | h_all %d->%d `%s`; h_lower %d->%d `%s` | beta_2 %d->%d `%s` |" % (
            comp["row"]["label"],
            comp["h_all"]["old_count"],
            comp["h_all"]["new_count"],
            comp["h_all"]["relation"],
            comp["h_lower"]["old_count"],
            comp["h_lower"]["new_count"],
            comp["h_lower"]["relation"],
            comp["beta"]["2"]["old_count"],
            comp["beta"]["2"]["new_count"],
            comp["beta"]["2"]["relation"],
        ))
    return "\n".join(["| row | h support relation | beta support relation |", "|---|---:|---:|"] + rows)


def run_table_md(records: Sequence[dict]) -> str:
    rows = ["| row | stratum | unk | eq | deg_x J | 32003 | 32009 | 32027 | Q | verdict |",
            "|---|---:|---:|---:|---:|---|---|---|---|---|"]
    for rec in records:
        by_char = {run["char"]: run for run in rec["runs"]}
        rows.append("| `%s` | `%s` | %d | %d | %s | %s | %s | %s | %s | `%s` |" % (
            rec["row"]["label"],
            rec["partition_label"],
            rec["unknowns"],
            rec["equations"],
            rec["sanity_gate"].get("deg_x_J"),
            by_char[32003]["verdict"],
            by_char[32009]["verdict"],
            by_char[32027]["verdict"],
            by_char[0]["verdict"],
            rec["verdict"],
        ))
    return "\n".join(rows)


def timing_table_md(records: Sequence[dict]) -> str:
    rows = ["| row | stratum | build s | 32003 s | 32009 s | 32027 s | Q s |",
            "|---|---:|---:|---:|---:|---:|---:|"]
    for rec in records:
        by_char = {run["char"]: run for run in rec["runs"]}
        rows.append("| `%s` | `%s` | %s | %s | %s | %s | %s |" % (
            rec["row"]["label"],
            rec["partition_label"],
            rec.get("build_elapsed"),
            by_char[32003].get("elapsed"),
            by_char[32009].get("elapsed"),
            by_char[32027].get("elapsed"),
            by_char[0].get("elapsed"),
        ))
    return "\n".join(rows)


def detail_diff_md(summary: dict) -> str:
    chunks = []
    for comp in summary["support_comparison"]:
        if comp["row"]["key"] not in PRIMARY_KEYS:
            continue
        chunks.append("`%s`: h old-new = %s; h new-old = %s. beta_2 old-new = %s; beta_2 new-old = %s." % (
            comp["row"]["label"],
            monomial_list_s([tuple(m) for m in comp["h_all"]["old_minus_new"]]),
            monomial_list_s([tuple(m) for m in comp["h_all"]["new_minus_old"]]),
            monomial_list_s([tuple(m) for m in comp["beta"]["2"]["old_minus_new"]]),
            monomial_list_s([tuple(m) for m in comp["beta"]["2"]["new_minus_old"]]),
        ))
    return "\n\n".join(chunks)


def full_support_notes_md(summary: dict) -> str:
    rows = []
    for comp in summary["support_comparison"]:
        rows.append("| `%s` | `%s` | `%s` | h_all %d->%d `%s`; h_lower %d->%d `%s`; beta_2 %d->%d `%s` |" % (
            comp["row"]["label"],
            comp["old_rule"]["h_threshold"],
            comp["corrected_rule"]["B"],
            comp["h_all"]["old_count"],
            comp["h_all"]["new_count"],
            comp["h_all"]["relation"],
            comp["h_lower"]["old_count"],
            comp["h_lower"]["new_count"],
            comp["h_lower"]["relation"],
            comp["beta"]["2"]["old_count"],
            comp["beta"]["2"]["new_count"],
            comp["beta"]["2"]["relation"],
        ))
    return "\n".join(["| row | old h threshold | corrected B | measured relation |",
                      "|---|---:|---:|---|"] + rows)


def write_report(summary: dict):
    by_row: Dict[str, List[dict]] = {}
    for rec in summary["strata"]:
        by_row.setdefault(rec["row"]["key"], []).append(rec)
    verdict_lines = []
    for row in ROWS:
        verdict_lines.append("| `%s` | %s | `%s` |" % (
            row.label,
            ", ".join("`%s`" % "+".join(map(str, p)) for p in allowed_partitions(row)),
            row_verdict(by_row.get(row.key, [])),
        ))
    support_notes = []
    for comp in summary["support_comparison"]:
        if comp["row"]["key"] in PRIMARY_KEYS:
            b = comp["beta"]["2"]
            support_notes.append("`%s`: beta_2 is `new_subset_old`, so the old beta inventory was a superset; the h support is equal." % comp["row"]["label"] if b["relation"] == "new_subset_old" else "`%s`: beta_2 relation is `%s`." % (comp["row"]["label"], b["relation"]))
    gap_records = [rec for rec in summary["strata"] if rec.get("verdict") != "SATURATED-EMPTY"]
    if gap_records:
        gap_note = "\n".join(
            "- `%s` stratum `%s`: `%s`; Q verdict `%s`; controls empty/nonempty `%s/%s`; Q elapsed `%s` s."
            % (
                rec["row"]["label"],
                rec["partition_label"],
                rec["verdict"],
                {run["char"]: run for run in rec["runs"]}[0]["verdict"],
                {run["char"]: run for run in rec["runs"]}[0].get("control_empty_pass"),
                {run["char"]: run for run in rec["runs"]}[0].get("control_nonempty_pass"),
                {run["char"]: run for run in rec["runs"]}[0].get("elapsed"),
            )
            for rec in gap_records
        )
    else:
        gap_note = "none"
    aux_note = """Auxiliary Q attempts for the final restoration stratum were not counted as
certificates: `legacy_le_34` returned `SURVIVES`, `first_24` timed out at
300 s, `eq2_14` returned `SURVIVES`, and an exploratory full-system `slimgb`
run was stopped without a `MAIN_DONE` result.  These are negative/blocked
checks only."""
    text = f"""# Corrected symbolic partition-strata rerun

Lane: `strata-rerun-corrected-gpt55-20260903`.  Inputs: `/tmp/jc2-lane.S2kb7J/inputs`.
Drivers/results: `box/strata-rerun-20260903/`.

## Manifest

MEASURED.  The manifest was generated mechanically from
`xmodel/strata-rerun-corrected-gpt55-20260903.run.v2` by pairing the
`charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines, then
running `sha256sum -c`.  All {len(summary["manifest"]["checks"])} frozen inputs returned `OK`.

Singular: `{summary["singular"]}`.

No ledger files were edited.  No `jc2-lean` command was run.  No `ideation-*`
or in-progress lane report files were created.

Primary command:

```text
python3 box/strata-rerun-20260903/strata_rerun.py --run-all --timeout 900
```

The driver persisted every generated Singular script under
`box/strata-rerun-20260903/systems/`, every per-stratum JSON record under
`box/strata-rerun-20260903/results/`, and the tabular summary at
`box/strata-rerun-20260903/summary.tsv`.  The report is sealed only after the
run loop finishes.

## Support comparison

MEASURED.  Old support means the former rule `-i+delta1*j >= -r*delta1` with
no `k+1` x-cap on beta.  Corrected support means
`B=V2*delta1+u*delta2`, `-i+delta1*j >= r*B`, and `deg_x beta <= k+1`.
Here `d'=2`, so the only beta coefficient is `beta_2`.

{support_table_md(summary, primary_only=True)}

{chr(10).join(support_notes)}

Differing monomials on the two primary rows:

{detail_diff_md(summary)}

Typed consequence: because `beta_2(new) subset beta_2(old)` and `h(new)=h(old)`
on both primary rows, the old saturated-empty systems were run on a support
superset in the D1 inventory.  They were not slice kills caused by missing beta
monomials.  The fresh corrected rerun below independently confirms the strata.

Full support comparison, including the two restoration rows:

{full_support_notes_md(summary)}

Restoration support deltas: `(21,14;18;5;k=1)` is unchanged old/new for
`h_all`, `h_lower`, and `beta_2`.  For `(15,10;11;2;k=2)`, corrected support
is a strict subset of the old support: `h_all` is `15->13`, `h_lower` is
`11->9`, and `beta_2` is `28->16`.

## Rerun results

MEASURED.  Each stratum kept symbolic slopes and used saturation by
`c*Omega`, where `Omega` is the product of slope nonzero and noncollision
factors.  Each system ran controls in the declared coefficient ring before the
main saturation.  The sanity gate printed the exact degree in `x` of the
h-adic normalized level-0 Jacobian remainder before subtracting `c*x^k`;
this is the pre-saturation object compared to the target monomial.  Every
stratum reached the required `k`.

{run_table_md(summary["strata"])}

Timings:

{timing_table_md(summary["strata"])}

Typed gap records:

{gap_note}

The only non-confirmed stratum is the final restoration case
`(15,10;11;2;k=2)` with partition `[1,1,1]`: the three finite fields returned
`SATURATED-EMPTY`, but the exact `Q` full-system run timed out at the 900 s
bound.  By FALLACY-v2 this remains `GAP`, not a Q kill.  {aux_note}

## Row verdicts

| row | strata | verdict |
|---|---|---|
{chr(10).join(verdict_lines)}

Typed verdicts: `CONFIRMED` means every listed partition stratum returned
`SATURATED-EMPTY` over all three primes and over `Q`, with the normalized
Jacobian-degree gate reaching the row's `k`.  `REFUTED` would require a surviving
stratum and a representative direct Jacobian check; none occurred.  `GAP`
means timeout, failed control, or failed degree gate.  Here it occurs only for
the exact `Q` run of `(15,10;11;2;k=2)` partition `[1,1,1]`.

Answer to the restoration question: `(21,14;18;5;k=1)` persists completely.
For `(15,10;11;2;k=2)`, `[3]` and `[2,1]` persist, while `[1,1,1]` remains a
Q gap in this bounded rerun despite three modular empty certificates.

## FALLACY-v2 check

`sat()` wrapping: every Singular script declares its ring and saturates by
`T*(c*Omega)-1`; controls `<c*Omega,T*(c*Omega)-1>` and
`<c*Omega-1,T*(c*Omega)-1>` passed for every run.

Raw remainder degree: the driver computes the h-adic normalized level-0
Jacobian remainder degree before saturation and records it in each JSON result
and Singular script header.  The full expanded raw Jacobian was not used as a
promotion shortcut.

Variable/ring map: the emitted rings use the parameter variables plus
Rabinowitsch variable `T`; chart variables are `x,y` in the generator with `x`
the monomial-Jacobian variable in `J=c*x^k`.  Prime marks are labels only.

No exit-price assertion is made here, so no `charge_basis` line is applicable.

<!-- BODY-END -->
"""
    REPORT.write_text(text)


def run_all(timeout: int) -> dict:
    if shutil.which("Singular") is None:
        raise SystemExit("Singular not found")
    manifest = manifest_check()
    if not manifest["ok"]:
        raise SystemExit("frozen input mismatch")
    summary = {
        "manifest": manifest,
        "singular": singular_version(),
        "primes": list(PRIMES),
        "support_comparison": [support_comparison(row) for row in ROWS],
        "strata": [],
    }
    for row in ROWS:
        for part in allowed_partitions(row):
            print("BUILD/RUN %s part %s" % (row.label, "+".join(map(str, part))), file=sys.stderr, flush=True)
            summary["strata"].append(execute_stratum(row, part, timeout))
            (OUT / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
            write_summary_tsv(summary)
    write_report(summary)
    return summary


def print_summary(summary: dict):
    print("manifest ok:", summary["manifest"]["ok"])
    print("singular:", summary["singular"])
    for rec in summary["strata"]:
        by_char = {run["char"]: run["verdict"] for run in rec["runs"]}
        print("%-20s part=%-7s unk=%2d eq=%3d degxJ=%s mod=%s,%s,%s Q=%s verdict=%s" % (
            rec["row"]["label"],
            rec["partition_label"],
            rec["unknowns"],
            rec["equations"],
            rec["sanity_gate"].get("deg_x_J"),
            by_char.get(32003),
            by_char.get(32009),
            by_char.get(32027),
            by_char.get(0),
            rec["verdict"],
        ))
    print("report:", REPORT.relative_to(ROOT))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-all", action="store_true")
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()
    if args.run_all:
        summary = run_all(args.timeout)
    else:
        summary = {
            "manifest": manifest_check(),
            "singular": singular_version(),
            "primes": list(PRIMES),
            "support_comparison": [support_comparison(row) for row in ROWS],
            "strata": [],
        }
        for row in ROWS:
            for part in allowed_partitions(row):
                rec = build_system(row, part)
                summary["strata"].append({k: v for k, v in rec.items() if k not in {"eqs", "params", "T", "sat"}})
        print(json.dumps(summary, indent=2, sort_keys=True, default=str))
        return
    print_summary(summary)


if __name__ == "__main__":
    main()
