#!/usr/bin/env python3
"""Count and run source-safe top-face partition strata.

This is a bounded wrapper around the frozen charged batch generator.  It does
not alter that generator.  A top face with non-centre multiplicity partition
``parts`` is parameterised as

    y^V (y-x)^parts[0] product_i (y-a_i*x)^parts[i].

The a_i are retained as variables.  The executable A/B charts saturate by the
Jacobian scalar and by all noncollision factors.  Counts follow the charged
convention and exclude the Rabinowitsch variable T.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
import re
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence, Tuple

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
FROZEN = Path("/tmp/jc2-lane.xsKKst/inputs")
RECEIPT = ROOT / "xmodel/topface-license-sol56-20260903.run.v2"
OUT = Path(__file__).resolve().parent


def load_frozen(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, FROZEN / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen %s" % filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# The charged driver imports `shape` by name.
shape = load_frozen("shape", "shape.py")
sys.modules["shape"] = shape
batch = load_frozen("charged_twopoint_order_batch", "twopoint_order_batch.py")


@dataclass(frozen=True)
class Target:
    key: str
    source: str
    original_M: Tuple[int, ...]
    original_V: Tuple[int, ...]
    ds: int
    Vs: int
    row: object


TARGETS = [
    Target("125_75", "(125,75)", (-75, 105, 123), (2, 4), 5, 4,
           batch.Row("(125,75)", 25, 15, 21, 2, 2)),
    Target("132_88", "(132,88)", (-88, 120, 130), (8, 3), 4, 3,
           batch.Row("(132,88)", 33, 22, 30, 8, 1)),
    Target("175_100", "(175,100)", (-100, 155, 173), (2, 4), 5, 4,
           batch.Row("(175,100)", 35, 20, 31, 2, 2)),
    Target("175_125", "(175,125)", (-125, 155, 173), (3, 4), 5, 4,
           batch.Row("(175,125)", 35, 25, 31, 3, 2)),
    Target("180_120", "(180,120) drop1", (-120, 168, 176, 178), (11, 9, 3), 4, 3,
           batch.Row("(180,120) drop1", 45, 30, 42, 11, 1)),
    Target("180_144", "(180,144)", (-144, 150, 178), (4, 5), 6, 5,
           batch.Row("(180,144)", 30, 24, 25, 4, 3)),
    Target("192_128", "(192,128)", (-128, 136, 190), (2, 7), 8, 7,
           batch.Row("(192,128)", 24, 16, 17, 2, 5)),
    Target("196_56", "(196,56)", (-56, 184, 194), (4, 3), 4, 3,
           batch.Row("(196,56)", 49, 14, 46, 4, 1)),
    Target("200_120", "(200,120)", (-120, 188, 198), (7, 3), 4, 3,
           batch.Row("(200,120)", 50, 30, 47, 7, 1)),
]


def verify_receipt():
    fields = {}
    for line in RECEIPT.read_text().splitlines():
        match = re.match(r"charged_input_(\d+)_(basename|sha256)=(.*)", line)
        if match:
            fields.setdefault(match.group(1), {})[match.group(2)] = match.group(3)
    checks = []
    for idx in sorted(fields, key=int):
        rec = fields[idx]
        path = FROZEN / rec["basename"]
        got = hashlib.sha256(path.read_bytes()).hexdigest()
        checks.append({"basename": rec["basename"], "ok": got == rec["sha256"],
                       "expected": rec["sha256"], "got": got})
    return {"ok": bool(checks) and all(item["ok"] for item in checks), "checks": checks}


def partitions(n: int, ceiling: int | None = None) -> Iterable[Tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    top = n if ceiling is None else min(n, ceiling)
    for first in range(top, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def case_data(target: Target, parts: Sequence[int]):
    row = target.row
    C = shape.shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    if sum(parts) != C["u"]:
        raise ValueError("partition sum is not u'")
    if len(parts) + 1 > row.n - row.M2:
        raise ValueError("Prop. 4.6 root-count cap fails")
    ab = C["dprime"] == 2 and C["eprime"] == 3
    if ab:
        fixed_base = C["n_h"] + 4 + 1
        d1_count = len([m for m in C["h_all"] if m != (0, C["K"])]) + 4 + 1
        chart = "d2e3_ab"
    else:
        fixed = batch.generic_d1_count(row, no_top=False)
        d1 = batch.generic_d1_count(row, no_top=True)
        fixed_base = fixed["unknowns"]
        d1_count = d1["unknowns"]
        chart = fixed["chart"]
    minor_cap = math.floor(C["K"] / (row.n - row.M2))
    return {
        "partition": list(parts),
        "partition_label": "+".join(map(str, parts)),
        "length": len(parts),
        "slope_parameters": max(0, len(parts) - 1),
        "unknowns": fixed_base + max(0, len(parts) - 1),
        "fixed_numeric_base": fixed_base,
        "charged_d1_count": d1_count,
        "chart": chart,
        "executable": ab,
        "conditional_inverse_minor": min(parts) <= minor_cap,
        "minor_cap": minor_cap,
    }


def face(target: Target, parts: Sequence[int]):
    row = target.row
    x, y = sp.symbols("x y")
    slopes = list(sp.symbols("a2:%d" % (len(parts) + 1))) if len(parts) > 1 else []
    expr = y ** row.V2 * (y - x) ** parts[0]
    for aa, ee in zip(slopes, parts[1:]):
        expr *= (y - aa * x) ** ee
    omega = sp.Integer(1)
    for aa in slopes:
        omega *= aa * (aa - 1)
    for i, aa in enumerate(slopes):
        for bb in slopes[i + 1:]:
            omega *= aa - bb
    return x, y, sp.expand(expr), slopes, sp.expand(omega)


def inventory():
    rows = []
    for target in TARGETS:
        C = shape.shape_bundle(target.row.n, target.row.m, target.row.M2,
                               target.row.V2, target.row.k)
        cases = []
        for part in partitions(C["u"]):
            if len(part) + 1 > target.row.n - target.row.M2:
                continue
            rec = case_data(target, part)
            _x, _y, top, slopes, omega = face(target, part)
            rec.update({"top_face": str(top), "top_face_factored": factored_face(target, part),
                        "slope_symbols": [str(s) for s in slopes], "open_factor": str(omega)})
            cases.append(rec)
        rows.append({
            "key": target.key,
            "source": target.source,
            "original_M": list(target.original_M),
            "original_V": list(target.original_V),
            "ds_Vs_us": [target.ds, target.Vs, target.ds - target.Vs],
            "descended": asdict(target.row),
            "K": C["K"], "uprime": C["u"], "dprime": C["dprime"],
            "eprime": C["eprime"], "q_degree": target.row.n - target.row.M2,
            "cases": cases,
        })
    return {"manifest": verify_receipt(), "count_convention": "unknowns exclude T", "rows": rows}


def factored_face(target: Target, parts: Sequence[int]):
    factors = ["(y-x)^%d" % parts[0]]
    for idx, exponent in enumerate(parts[1:], start=2):
        factors.append("(y-a%d*x)^%d" % (idx, exponent))
    return "y^%d*%s" % (target.row.V2, "*".join(factors))


def parse_partition(value: str) -> Tuple[int, ...]:
    vals = tuple(int(v) for v in re.split(r"[+,]", value) if v)
    if not vals or any(v <= 0 for v in vals) or tuple(sorted(vals, reverse=True)) != vals:
        raise argparse.ArgumentTypeError("use a descending partition such as 3 or 2+1")
    return vals


def build_ab(target: Target, parts: Sequence[int]):
    row = target.row
    C = shape.shape_bundle(row.n, row.m, row.M2, row.V2, row.k)
    if not (C["dprime"] == 2 and C["eprime"] == 3):
        raise ValueError("the charged generator only executes d'=2,e'=3 here")
    x, y, top, slopes, omega = face(target, parts)
    c, T = sp.symbols("c T")
    hpars = []
    h = top + batch.poly_from_mons(C["h_lower"], x, y, "h", hpars)
    beta, bpars, A = batch.build_beta_ab(h, x, y)
    qdiv, _ = sp.div(sp.Poly(sp.expand(beta ** 2), y), sp.Poly(h, y), y)
    alpha = sp.expand(qdiv.as_expr())
    low_terms = [(sp.Integer(1), 2), (2 * beta, 0)]
    high_terms = [(sp.Integer(1), 3), (3 * beta, 1),
                  (sp.Rational(3, 2) * alpha, 0)]
    eqs, levels = batch.hadic_eqs(h, low_terms, high_terms, c, row.k, x, y)
    params = hpars + slopes + bpars + [c]
    meta = case_data(target, parts)
    meta.update({"equations": len(eqs), "unknowns": len(params), "levels": levels,
                 "ring": "params=%d plus T" % len(params), "top_face": str(top),
                 "top_face_factored": factored_face(target, parts),
                 "saturation_factor": str(sp.expand(c * omega))})
    return eqs, params, T, sp.expand(c * omega), meta


def write_singular(path: Path, target: Target, eqs, params, T, sat, meta, char: int):
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
    sat_s = batch.sstr(sat.subs(rename))
    T_s = str(rename[T])
    gens = [batch.sstr(eq.subs(rename)) for eq in eqs] + ["%s*(%s)-1" % (T_s, sat_s)]
    lines = [
        "// source-safe parametric top-face stratum",
        "// row %s partition %s" % (target.source, meta["partition_label"]),
        "// top %s" % meta["top_face_factored"],
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
        'print("MAIN_START equations=%d unknowns=%d char=%d");' % (len(eqs), len(params), char),
        "ideal I=%s;" % ",\n".join(gens),
        "ideal G=std(I);",
        'print("MAIN_DONE basis_size="); size(G);',
        'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_NONTRIVIAL"); }',
        "quit;",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def run_singular(path: Path, timeout: int):
    started = time.time()
    try:
        proc = subprocess.run(["Singular", "-q", "--no-rc", str(path)],
                              capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        tail = exc.stdout or ""
        if isinstance(tail, bytes):
            tail = tail.decode("utf-8", "ignore")
        return {"verdict": "TIMEOUT", "elapsed": round(time.time() - started, 3),
                "timeout": timeout, "stdout_tail": tail[-1200:]}
    output = (proc.stdout or "") + (proc.stderr or "")
    parsed = batch.parse_singular_output(output)
    parsed.update({"elapsed": round(time.time() - started, 3), "rc": proc.returncode,
                   "stdout_tail": output[-1600:]})
    return parsed


def execute(target: Target, parts: Sequence[int], timeout: int, primes: Sequence[int]):
    started = time.time()
    eqs, params, T, sat, meta = build_ab(target, parts)
    meta["build_elapsed"] = round(time.time() - started, 3)
    result = {"manifest": verify_receipt(), "target": target.key, "row": asdict(target.row),
              "meta": meta, "modular": [], "exact": None}
    stem = "%s_part_%s" % (target.key, "_".join(map(str, parts)))
    systems = OUT / "systems"
    for prime in primes:
        path = systems / (stem + "_mod_%d.sing" % prime)
        write_singular(path, target, eqs, params, T, sat, meta, prime)
        item = run_singular(path, timeout)
        item.update({"char": prime, "script": str(path.relative_to(ROOT))})
        result["modular"].append(item)
        if item["verdict"] == "TIMEOUT":
            result["exact"] = {"verdict": "COUNTING-BOUND",
                               "reason": "modular timeout; Q not launched"}
            break
    else:
        path = systems / (stem + "_Q.sing")
        write_singular(path, target, eqs, params, T, sat, meta, 0)
        item = run_singular(path, timeout)
        item.update({"char": 0, "script": str(path.relative_to(ROOT))})
        result["exact"] = item
    outpath = OUT / (stem + "_result.json")
    outpath.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result, outpath


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", action="store_true", help="write/print all source-safe strata")
    parser.add_argument("--row", choices=[t.key for t in TARGETS])
    parser.add_argument("--partition", type=parse_partition)
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--primes", default="32003,32009,32027")
    args = parser.parse_args()
    checked = verify_receipt()
    if not checked["ok"]:
        raise SystemExit("frozen input mismatch")
    if args.count or not args.run:
        data = inventory()
        path = OUT / "case_counts.json"
        path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
        print(json.dumps(data, indent=2, sort_keys=True))
    if args.run:
        if not args.row or not args.partition:
            parser.error("--run needs --row and --partition")
        target = next(t for t in TARGETS if t.key == args.row)
        allowed = [tuple(c["partition"]) for c in inventory()["rows"]
                   if c["key"] == target.key for c in c["cases"]]
        if args.partition not in allowed:
            parser.error("partition is not in the source-safe Prop. 4.6 overcover")
        primes = tuple(int(v) for v in args.primes.split(",") if v)
        result, path = execute(target, args.partition, args.timeout, primes)
        print(json.dumps(result, indent=2, sort_keys=True))
        print("result:", path)


if __name__ == "__main__":
    main()
