#!/usr/bin/env python3
"""First-nonzero Pade branch systems for the R3 ODE.

For P(w)=1+F_1 w+...+F_(2s)w^(2s), let
P(w)^(3/2)=sum h_i w^i.  The reciprocal R3 equation after eliminating
G_1,...,G_(3s) by Q* pivots is

    h_(3s+1)=...=h_(5s-2)=0,  h_(5s-1) != 0.

The open condition is equivalent to c != 0 because
c = -2(5s-1) h_(5s-1).  The finite cover uses the first nonzero F_r:
F_1=...=F_(r-1)=0, F_r=1.  Each division in the recurrence is by 2n in Q*.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import time

import sympy as sp


ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
ROWS = {
    "21": (21, 14, 15, 6, 4),
    "24": (24, 16, 18, 7, 4),
    "27": (27, 18, 21, 8, 4),
}


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def series_coefficients(s: int, first: int) -> tuple[list[sp.Symbol], list[sp.Expr], sp.Expr, list[sp.Expr]]:
    m = 2 * s
    n = 3 * s
    upto = 5 * s - 1
    all_f = list(sp.symbols(f"F1:{m + 1}"))
    specialized = [sp.Integer(0)] * (first - 1) + [sp.Integer(1)] + all_f[first:]
    variables = all_f[first:]
    h = [sp.Integer(1)]
    for degree in range(1, upto + 1):
        numerator = sp.Integer(0)
        for i in range(1, min(m, degree) + 1):
            coeff = specialized[i - 1]
            if coeff == 0:
                continue
            numerator += (2 * (degree - i) - 3 * i) * coeff * h[degree - i]
        h.append(sp.expand(-numerator / (2 * degree)))
    tails = h[n + 1 : 5 * s - 1]
    kappa = h[5 * s - 1]
    return variables, tails, kappa, h


def singular_polynomial(expr: sp.Expr, variables: list[sp.Symbol]) -> str:
    poly = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    den, integral = poly.clear_denoms(convert=True)
    if den == 0:
        raise AssertionError("zero denominator")
    return str(integral.as_expr()).replace("**", "^")


def emit_branch(row: tuple[int, int, int, int, int], first: int, characteristic: int, method: str) -> tuple[pathlib.Path, dict]:
    n, m, m2, s, k = row
    variables, tails, kappa, _h = series_coefficients(s, first)
    tag = f"r3_{n}_{m}_{m2}_{s}_k{k}_first{first}_{'Q' if characteristic == 0 else 'p' + str(characteristic)}_{method}"
    path = HERE / f"{tag}.sing"
    T = sp.Symbol("T")
    ring_variables = [T] + variables
    generators = tails + [T * kappa - 1]
    encoded = [singular_polynomial(expr, ring_variables) for expr in generators]
    field = "0" if characteristic == 0 else str(characteristic)
    lines = [
        f"// {tag}",
        f"// first nonzero reciprocal coefficient: F{first}=1; previous F_i=0",
        f"// open condition: h_{5 * s - 1} != 0; c=-{2 * (5 * s - 1)}*h_{5 * s - 1}",
        f"ring R={field},({','.join(map(str, ring_variables))}),dp;",
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); } else { print("CONTROL_RING_FAIL"); }',
        f'print("MAIN_START row={n}_{m}_{m2}_{s}_k{k} first={first} char={field} method={method} tails={len(tails)} vars={len(variables)}");',
        "ideal I=" + ",\n".join(encoded) + ";",
    ]
    if method == "facstd":
        lines.extend(
            [
                'LIB "standard.lib";',
                "list L=facstd(I);",
                'print("MAIN_DONE component_count=");',
                "size(L);",
                "int empty_count=0;",
                "int nonempty_seen=0;",
                "int j;",
                "for (j=1; j<=size(L); j++) {",
                "  ideal G=L[j];",
                '  print("FACSTD_COMPONENT");',
                "  j;",
                "  if (reduce(1,G)==0) { empty_count=empty_count+1; }",
                '  else { if (nonempty_seen==0) { nonempty_seen=1; print("BRANCH_NONEMPTY"); print("dim_extended="); dim(G); print("vdim="); vdim(G); G; } }',
                "}",
                'if (empty_count==size(L)) { print("BRANCH_EMPTY_UNIT"); }',
                "quit;",
            ]
        )
    else:
        lines.extend(
            [
                f"ideal G={method}(I);",
                'print("MAIN_DONE basis_size=");',
                "size(G);",
                'if (reduce(1,G)==0) { print("BRANCH_EMPTY_UNIT"); G; } else { print("BRANCH_NONEMPTY"); print("dim_extended="); dim(G); print("vdim="); vdim(G); }',
                "quit;",
            ]
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    meta = {
        "script": str(path.relative_to(ROOT)),
        "script_sha256": sha256_file(path),
        "row": [n, m, m2, s, k],
        "first": first,
        "characteristic": characteristic,
        "method": method,
        "tail_count": len(tails),
        "variable_count_after_slice": len(variables),
        "text_bytes_tails_plus_kappa": sum(len(str(expr)) for expr in tails) + len(str(kappa)),
        "kappa_index": 5 * s - 1,
        "c_factor": -2 * (5 * s - 1),
    }
    return path, meta


def run_singular(path: pathlib.Path, timeout: int) -> dict:
    started = time.monotonic()
    try:
        result = subprocess.run(
            ["Singular", "-q", "--no-rc", str(path)],
            cwd=str(ROOT),
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        status = "ok" if result.returncode == 0 else f"exit_{result.returncode}"
        stdout = result.stdout
        stderr = result.stderr
    except subprocess.TimeoutExpired as exc:
        status = "timeout"
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
    if isinstance(stdout, bytes):
        stdout = stdout.decode("utf-8", errors="replace")
    if isinstance(stderr, bytes):
        stderr = stderr.decode("utf-8", errors="replace")
    out_path = path.with_suffix(path.suffix + ".out")
    err_path = path.with_suffix(path.suffix + ".err")
    out_path.write_text(stdout, encoding="utf-8")
    err_path.write_text(stderr, encoding="utf-8")
    return {
        "status": status,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "stdout": str(out_path.relative_to(ROOT)),
        "stderr": str(err_path.relative_to(ROOT)),
        "stdout_tail": stdout.splitlines()[-30:],
        "stderr_tail": stderr.splitlines()[-30:],
        "main_done": "MAIN_DONE" in stdout,
        "empty_unit": "BRANCH_EMPTY_UNIT" in stdout,
        "nonempty": "BRANCH_NONEMPTY" in stdout,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--row", choices=sorted(ROWS), required=True)
    parser.add_argument("--first", type=int, nargs="*")
    parser.add_argument("--all-first", action="store_true")
    parser.add_argument("--char", type=int, default=32003)
    parser.add_argument("--method", choices=("std", "slimgb", "facstd"), default="slimgb")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--run", action="store_true")
    args = parser.parse_args()

    row = ROWS[args.row]
    s = row[3]
    if args.all_first:
        first_values = list(range(1, 2 * s + 1))
    elif args.first:
        first_values = args.first
    else:
        raise SystemExit("provide --first or --all-first")
    records = []
    for first in first_values:
        print(f"BRANCH_EMIT row={args.row} first={first}", flush=True)
        script, meta = emit_branch(row, first, args.char, args.method)
        record = {"meta": meta}
        if args.run:
            record["run"] = run_singular(script, args.timeout)
            print(
                f"BRANCH_RUN row={args.row} first={first} status={record['run']['status']} "
                f"done={record['run']['main_done']} empty={record['run']['empty_unit']} "
                f"nonempty={record['run']['nonempty']} elapsed={record['run']['elapsed_seconds']}",
                flush=True,
            )
        records.append(record)
    out = HERE / f"r3_pade_branches_{args.row}_{'all' if args.all_first else '_'.join(map(str, first_values))}_{'Q' if args.char == 0 else 'p' + str(args.char)}_{args.method}.json"
    out.write_text(json.dumps(records, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"records": str(out.relative_to(ROOT)), "count": len(records)}, indent=2))


if __name__ == "__main__":
    main()
