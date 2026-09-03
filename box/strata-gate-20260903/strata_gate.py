#!/usr/bin/env python3
"""Symbolic top-face strata gate for the 2026-09-03 audit.

The generated systems use the two-point (d',e')=(2,3) A/B chart with a
partitioned top face

    H = y^V (y-x)^e1 prod_i (y-a_i x)^e_i.

All extra slopes remain ring variables.  Saturation is by c*Omega where Omega
is the product of the slope nonzero and noncollision factors.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
import time
from dataclasses import asdict, dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
FROZEN = Path("/tmp/jc2-lane.LR0om9/inputs")
RECEIPT = ROOT / "xmodel/strata-gate-gpt55-20260903.run.v2"
REPLAY_DIR = ROOT / "box/topface-20260903"


@dataclass(frozen=True)
class Row:
    key: str
    source: str
    parent: str
    n: int
    m: int
    M2: int
    V2: int
    k: int


REPLAY_ROWS = [
    Row("132_88", "(33,22;30;8;k=1)", "(132,88)", 33, 22, 30, 8, 1),
    Row("180_120", "(45,30;42;11;k=1)", "(180,120)", 45, 30, 42, 11, 1),
]

PRIOR_ROWS = [
    Row("75_50_v2", "(15,10;11;2;k=2)", "(75,50) V2=2", 15, 10, 11, 2, 2),
    Row("84_56", "(21,14;18;5;k=1)", "(84,56)", 21, 14, 18, 5, 1),
]

INDEPENDENT_CHECKS = [
    (REPLAY_ROWS[0], (2, 1)),
    (REPLAY_ROWS[1], (3, 1)),
]

CERTIFICATE_75_SIMPLE = [1, 2, 3, 4, 5, 9, 18, 29, 30, 31, 32, 33, 34, 35, 39, 42, 7]


def verify_receipt() -> dict:
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
        checks.append(
            {
                "basename": rec["basename"],
                "path": str(path),
                "expected": rec["sha256"],
                "got": got,
                "ok": got == rec["sha256"],
            }
        )
    return {"ok": bool(checks) and all(item["ok"] for item in checks), "checks": checks}


def jac(f, g, x, y):
    return sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x)


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


def clean_name(value: str) -> str:
    out = re.sub(r"[^A-Za-z0-9_]+", "_", value)
    out = re.sub(r"_+", "_", out).strip("_")
    return out or "v"


def frac_s(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def row_shape(row: Row) -> dict:
    K = math.gcd(row.n, row.m)
    dprime = row.m // K
    eprime = row.n // K
    u = K - row.V2
    R = row.n - row.M2 - 1
    if R <= 0:
        raise ValueError("bad R")
    delta2 = F(-(row.k + 1), R)
    delta1 = F(row.k + 1, 1) * F((dprime + eprime) * u - R, R * ((dprime + eprime) * row.V2 - 1))
    h_all = h_monomials(delta1, K, u, K)
    h_lower = [mon for mon in h_all if mon[0] + mon[1] < K]
    return {
        "K": K,
        "dprime": dprime,
        "eprime": eprime,
        "u": u,
        "R": R,
        "q_degree": row.n - row.M2,
        "delta2": delta2,
        "delta1": delta1,
        "h_all": h_all,
        "h_lower": h_lower,
    }


def h_monomials(delta1: F, deg_y: int, deg_x: int, total: int):
    out = []
    for j in range(deg_y, -1, -1):
        for i in range(0, deg_x + 1):
            if i + j > total:
                continue
            if F(i, 1) <= delta1 * F(j + 1, 1):
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


def allowed_partitions(row: Row) -> List[Tuple[int, ...]]:
    shape = row_shape(row)
    return [
        part
        for part in partitions(shape["u"])
        if len(part) + 1 <= shape["q_degree"]
    ]


def face(row: Row, part: Sequence[int]):
    x, y = sp.symbols("x y")
    slopes = list(sp.symbols("a2:%d" % (len(part) + 1))) if len(part) > 1 else []
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


def factored_face(row: Row, part: Sequence[int]) -> str:
    factors = [f"(y-x)^{part[0]}"]
    for index, exponent in enumerate(part[1:], start=2):
        factors.append(f"(y-a{index}*x)^{exponent}")
    return "y^%d*%s" % (row.V2, "*".join(factors))


def poly_from_mons(mons: Iterable[Tuple[int, int]], x, y, prefix: str, params: List[sp.Symbol]):
    out = sp.Integer(0)
    for a, b in mons:
        var = sp.Symbol("%s_%d_%d" % (prefix, a, b))
        params.append(var)
        out += var * x**a * y**b
    return sp.expand(out)


def build_beta_ab(h, x, y):
    bp, bq, br, bs = sp.symbols("bp bq br bs")
    h0 = sp.expand(h.subs(y, 0))
    A = sp.expand(sp.together((h - h0) / y))
    beta = sp.expand(bp * A + bq * y + br * x + bs)
    return beta, [bp, bq, br, bs], A


def hadic_by_power(h, low_terms, high_terms, x, y):
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


def eqs_from_by_power(by_power: Dict[int, sp.Expr], c, kexp: int, x, y):
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


def build_system(row: Row, part: Sequence[int]) -> dict:
    shape = row_shape(row)
    if shape["dprime"] != 2 or shape["eprime"] != 3:
        raise ValueError("only the A/B d'=2,e'=3 chart is implemented")
    if tuple(part) not in allowed_partitions(row):
        raise ValueError("partition is outside Prop. 4.6 cap")
    x, y, top, slopes, omega = face(row, part)
    hpars: List[sp.Symbol] = []
    h = top + poly_from_mons(shape["h_lower"], x, y, "h", hpars)
    beta, bpars, _A = build_beta_ab(h, x, y)
    qdiv, _ = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
    alpha = sp.expand(qdiv.as_expr())
    low_terms = [(sp.Integer(1), 2), (2 * beta, 0)]
    high_terms = [(sp.Integer(1), 3), (3 * beta, 1), (sp.Rational(3, 2) * alpha, 0)]
    by_power = hadic_by_power(h, low_terms, high_terms, x, y)
    c, T = sp.symbols("c T")
    eqs, levels = eqs_from_by_power(by_power, c, row.k, x, y)
    params = hpars + slopes + bpars + [c]
    sat = sp.expand(c * omega)
    recomposition_ok = recomposition_check(h, low_terms, high_terms, by_power, params, x, y)
    return {
        "row": asdict(row),
        "partition": list(part),
        "partition_label": "+".join(map(str, part)),
        "cap": shape["q_degree"],
        "cap_condition": "1+len(partition)<=n-M2",
        "cap_ok": len(part) + 1 <= shape["q_degree"],
        "K": shape["K"],
        "uprime": shape["u"],
        "dprime": shape["dprime"],
        "eprime": shape["eprime"],
        "delta2": frac_s(shape["delta2"]),
        "delta1": frac_s(shape["delta1"]),
        "top_face_factored": factored_face(row, part),
        "slope_symbols": [str(item) for item in slopes],
        "omega": str(omega),
        "saturation_factor": str(sat),
        "h_lower_count": len(shape["h_lower"]),
        "unknowns": len(params),
        "equations": len(eqs),
        "levels": levels,
        "recomposition_ok": recomposition_ok,
        "eqs": eqs,
        "params": params,
        "T": T,
        "sat": sat,
    }


def recomposition_check(h, low_terms, high_terms, by_power, params, x, y) -> bool:
    sample = {}
    for index, param in enumerate(params):
        value = (index % 11) - 5
        if value == 0:
            value = 6
        sample[param] = value
    low_poly = sp.Add(*(coef * h**power for coef, power in low_terms))
    high_poly = sp.Add(*(coef * h**power for coef, power in high_terms))
    direct = sp.expand(jac(low_poly.subs(sample), high_poly.subs(sample), x, y))
    recomposed = sp.expand(
        sp.Add(*(rem.subs(sample) * h.subs(sample) ** level for level, rem in by_power.items()))
    )
    return sp.expand(direct - recomposed) == 0


def rename_symbols(params: Sequence[sp.Symbol], T: sp.Symbol):
    names = []
    rename = {}
    for sym in list(params) + [T]:
        base = clean_name(str(sym))
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


def write_singular(path: Path, rec: dict, char: int = 0):
    names, rename = rename_symbols(rec["params"], rec["T"])
    sat_s = sstr(rec["sat"].subs(rename))
    T_s = str(rename[rec["T"]])
    gens = [sstr(eq.subs(rename)) for eq in rec["eqs"]]
    gens.append("%s*(%s)-1" % (T_s, sat_s))
    lines = [
        "// generated by strata_gate.py",
        "// row %s partition %s" % (rec["row"]["source"], rec["partition_label"]),
        "// top %s" % rec["top_face_factored"],
        "// saturation %s" % rec["saturation_factor"],
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
        'print("MAIN_START equations=%d unknowns=%d char=%d");'
        % (rec["equations"], rec["unknowns"], char),
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
    start = time.time()
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
        return {
            "verdict": "TIMEOUT",
            "elapsed": round(time.time() - start, 3),
            "timeout": timeout,
            "stdout_tail": (stdout or "")[-1600:],
            "stderr_tail": (stderr or "")[-1600:],
        }
    output = (proc.stdout or "") + (proc.stderr or "")
    parsed = parse_singular_output(output)
    parsed.update(
        {
            "elapsed": round(time.time() - start, 3),
            "rc": proc.returncode,
            "stdout_tail": output[-1600:],
        }
    )
    return parsed


def run_generated(row: Row, part: Sequence[int], label: str, timeout: int):
    start = time.time()
    rec = build_system(row, part)
    rec["build_elapsed"] = round(time.time() - start, 3)
    stem = "%s_%s_part_%s_Q.sing" % (label, row.key, "_".join(map(str, part)))
    script = OUT / "systems" / stem
    write_singular(script, rec, char=0)
    result = run_singular(script, timeout)
    keep = {k: v for k, v in rec.items() if k not in {"eqs", "params", "T", "sat"}}
    keep["script"] = str(script.relative_to(ROOT))
    keep["exact"] = result
    outpath = OUT / "results" / stem.replace(".sing", ".json")
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(keep, indent=2, sort_keys=True) + "\n")
    return keep


def run_subset_certificate_75_simple(timeout: int) -> dict:
    row = PRIOR_ROWS[0]
    part = (1, 1, 1)
    rec = build_system(row, part)
    sub = dict(rec)
    sub["eqs"] = [rec["eqs"][index - 1] for index in CERTIFICATE_75_SIMPLE]
    sub["equations"] = len(sub["eqs"])
    script = OUT / "systems" / "certificate_75_50_v2_part_1_1_1_Q.sing"
    write_singular(script, sub, char=0)
    result = run_singular(script, timeout)
    keep = {k: v for k, v in rec.items() if k not in {"eqs", "params", "T", "sat"}}
    keep["certificate_type"] = "subset-of-full-ideal"
    keep["full_equations"] = len(rec["eqs"])
    keep["subset_equations"] = len(CERTIFICATE_75_SIMPLE)
    keep["subset_indices_1_based"] = CERTIFICATE_75_SIMPLE
    keep["script"] = str(script.relative_to(ROOT))
    keep["exact"] = result
    outpath = OUT / "results" / "certificate_75_50_v2_part_1_1_1_Q.json"
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(keep, indent=2, sort_keys=True) + "\n")
    return keep


def replay_result_json(row: Row, part: Sequence[int]) -> dict:
    path = REPLAY_DIR / ("%s_part_%s_result.json" % (row.key, "_".join(map(str, part))))
    return json.loads(path.read_text())


def replay_script(row: Row, part: Sequence[int], timeout: int) -> dict:
    src = REPLAY_DIR / "systems" / ("%s_part_%s_Q.sing" % (row.key, "_".join(map(str, part))))
    old = replay_result_json(row, part)
    result = run_singular(src, timeout)
    rec = {
        "row": asdict(row),
        "partition": list(part),
        "partition_label": "+".join(map(str, part)),
        "script": str(src.relative_to(ROOT)),
        "unknowns": old["meta"]["unknowns"],
        "equations": old["meta"]["equations"],
        "top_face_factored": old["meta"]["top_face_factored"],
        "saturation_factor": old["meta"]["saturation_factor"],
        "charged_exact": old["exact"],
        "replay_exact": result,
    }
    outpath = OUT / "results" / ("replay_%s_part_%s.json" % (row.key, "_".join(map(str, part))))
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
    return rec


def run_all(timeout: int) -> dict:
    if shutil.which("Singular") is None:
        raise SystemExit("Singular not found")
    manifest = verify_receipt()
    if not manifest["ok"]:
        raise SystemExit("frozen input mismatch")
    summary = {
        "manifest": manifest,
        "singular": singular_version(),
        "replay": [],
        "prior": [],
        "independent_checks": [],
    }
    for row in REPLAY_ROWS:
        for part in allowed_partitions(row):
            summary["replay"].append(replay_script(row, part, timeout))
    for row in PRIOR_ROWS:
        for part in allowed_partitions(row):
            summary["prior"].append(run_generated(row, part, "prior", timeout))
    for row, part in INDEPENDENT_CHECKS:
        summary["independent_checks"].append(run_generated(row, part, "independent", timeout))
    summary["subset_certificates"] = [run_subset_certificate_75_simple(timeout)]
    path = OUT / "summary.json"
    path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    return summary


def singular_version() -> str:
    proc = subprocess.run(["Singular", "-v"], capture_output=True, text=True, timeout=20)
    return (proc.stdout or proc.stderr).splitlines()[0].strip()


def print_summary(summary: dict):
    print("manifest ok:", summary["manifest"]["ok"])
    print("singular:", summary["singular"])
    for key in ("replay", "prior", "independent_checks"):
        print(key)
        for rec in summary[key]:
            verdict = rec.get("replay_exact", rec.get("exact", {})).get("verdict")
            basis = rec.get("replay_exact", rec.get("exact", {})).get("basis_size")
            print(
                "  %-12s %-14s unk=%s eq=%s verdict=%s basis=%s"
                % (rec["row"]["key"], rec["partition_label"], rec["unknowns"], rec["equations"], verdict, basis)
            )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-all", action="store_true")
    parser.add_argument("--certificate-75-simple", action="store_true")
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()
    if args.certificate_75_simple:
        summary = {"manifest": verify_receipt(), "singular": singular_version()}
        summary["subset_certificates"] = [run_subset_certificate_75_simple(args.timeout)]
        print(json.dumps(summary, indent=2, sort_keys=True))
        return
    if args.run_all:
        summary = run_all(args.timeout)
    else:
        summary = {"manifest": verify_receipt(), "singular": singular_version()}
        for row in REPLAY_ROWS + PRIOR_ROWS:
            shape = row_shape(row)
            print(row.key, shape["K"], shape["u"], allowed_partitions(row))
        return
    print_summary(summary)


if __name__ == "__main__":
    main()
