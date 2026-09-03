#!/usr/bin/env python3
"""R3 preprocessing for the three delta_1'=0 two-point rows.

The charged R3 systems use

    f(y) = y^(2s) + a_(2s-1)y^(2s-1) + ... + a_0
    g(y) = -(y^(3s) + b_(3s-1)y^(3s-1) + ... + b_0)
    2 f g' - 3 f' g = c

where s=V2'.  This driver rewrites the same coefficient equations at infinity:

    F(z) = z^(2s) f(1/z),  G(z) = -z^(3s) g(1/z),
    2 F G' - 3 F' G = c z^(5s-2).

The reciprocal coordinates are just
F_i = a_(2s-i), G_i = b_(3s-i).  The first 3s equations are affine in
G_1,...,G_(3s) with Q* pivots 2,4,...,6s.  No parameter-dependent pivot is used.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import time
from typing import Iterable

import sympy as sp


ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
RUN_RECEIPT = ROOT / "xmodel/r3-preprocess-gpt55-20260903.run.v2"
FROZEN_DIR = pathlib.Path("/tmp/jc2-lane.upiUoe/inputs")

ROWS = [
    (21, 14, 15, 6, 4),
    (24, 16, 18, 7, 4),
    (27, 18, 21, 8, 4),
]


@dataclasses.dataclass
class Pivot:
    step: int
    row_degree: int
    variable: sp.Symbol
    coefficient: sp.Rational
    rhs: sp.Expr


@dataclasses.dataclass
class R3Reduction:
    row: tuple[int, int, int, int, int]
    s: int
    fvars: list[sp.Symbol]
    gvars: list[sp.Symbol]
    c: sp.Symbol
    pivots: list[Pivot]
    residual_zero_rows: list[tuple[int, sp.Expr]]
    top_row: sp.Expr
    g_map: dict[sp.Symbol, sp.Expr]
    elapsed_seconds: float


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def expression_hash(expressions: Iterable[sp.Expr]) -> str:
    text = "\n".join(str(sp.expand(expr)) for expr in expressions) + "\n"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def verify_receipt() -> dict:
    fields: dict[str, str] = {}
    for line in RUN_RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    count = int(fields["charged_inputs"])
    lane_dir = pathlib.Path(fields["lane_inputs_dir"])
    manifest_lines = []
    checks = []
    for index in range(1, count + 1):
        base = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        path = lane_dir / base
        actual = sha256_file(path)
        ok = actual == expected
        manifest_lines.append(f"{expected}  {path}")
        checks.append(
            {
                "index": index,
                "basename": base,
                "path": str(path),
                "expected_sha256": expected,
                "actual_sha256": actual,
                "ok": ok,
            }
        )
    (HERE / "charged_inputs.sha256").write_text(
        "\n".join(manifest_lines) + "\n", encoding="utf-8"
    )
    if not all(item["ok"] for item in checks):
        raise RuntimeError("charged input SHA-256 mismatch")
    return {
        "receipt": str(RUN_RECEIPT.relative_to(ROOT)),
        "charged_inputs": count,
        "lane_inputs_dir": str(lane_dir),
        "all_ok": True,
        "checks": checks,
        "manifest_sha256": sha256_file(HERE / "charged_inputs.sha256"),
    }


def r3_w_coefficients(s: int) -> tuple[list[sp.Symbol], list[sp.Symbol], sp.Symbol, list[sp.Expr]]:
    fvars = list(sp.symbols(f"F1:{2 * s + 1}"))
    gvars = list(sp.symbols(f"G1:{3 * s + 1}"))
    c = sp.Symbol("c")
    f = [sp.Integer(1)] + fvars
    g = [sp.Integer(1)] + gvars
    rows: list[sp.Expr] = []
    for degree in range(0, 5 * s - 1):
        total = sp.Integer(0)
        for i in range(max(0, degree + 1 - 3 * s), min(2 * s, degree + 1) + 1):
            j = degree + 1 - i
            total += (2 * j - 3 * i) * f[i] * g[j]
        if degree == 5 * s - 2:
            total -= c
        rows.append(sp.expand(total))
    return fvars, gvars, c, rows


def reduce_r3(row: tuple[int, int, int, int, int]) -> R3Reduction:
    _n, _m, _M2, s, _k = row
    started = time.monotonic()
    fvars, gvars, c, rows = r3_w_coefficients(s)
    g_map: dict[sp.Symbol, sp.Expr] = {}
    pivots: list[Pivot] = []
    for degree in range(0, 3 * s):
        expr = sp.expand(rows[degree].subs(g_map, simultaneous=True))
        variable = gvars[degree]
        coefficient = sp.expand(sp.diff(expr, variable))
        if not coefficient.is_Rational or coefficient == 0:
            raise AssertionError(f"bad Q* pivot for {variable}: {coefficient}")
        remainder = sp.expand(expr - coefficient * variable)
        if variable in remainder.free_symbols:
            raise AssertionError(f"non-affine pivot for {variable}")
        rhs = sp.expand(-remainder / coefficient)
        g_map[variable] = rhs
        pivots.append(
            Pivot(
                step=len(pivots) + 1,
                row_degree=degree,
                variable=variable,
                coefficient=sp.Rational(coefficient),
                rhs=rhs,
            )
        )
        if sp.expand(expr.subs(variable, rhs)) != 0:
            raise AssertionError(f"pivot row {degree} not killed")

    residual_zero = []
    for degree in range(3 * s, 5 * s - 2):
        residual_zero.append((degree, sp.expand(rows[degree].subs(g_map, simultaneous=True))))
    top_row = sp.expand(rows[5 * s - 2].subs(g_map, simultaneous=True))
    return R3Reduction(
        row=row,
        s=s,
        fvars=fvars,
        gvars=gvars,
        c=c,
        pivots=pivots,
        residual_zero_rows=residual_zero,
        top_row=top_row,
        g_map=g_map,
        elapsed_seconds=time.monotonic() - started,
    )


def primitive_polynomial(expr: sp.Expr, variables: list[sp.Symbol]) -> tuple[sp.Poly, sp.Rational]:
    poly = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    den, cleared = poly.clear_denoms(convert=True)
    content, primitive = cleared.primitive()
    multiplier = sp.Rational(den, content)
    if primitive.LC() < 0:
        primitive = -primitive
        multiplier = -multiplier
    if sp.expand(primitive.as_expr() - multiplier * expr) != 0:
        raise AssertionError("primitive normalization failed")
    return primitive, multiplier


def singular_poly(expr: sp.Expr, variables: list[sp.Symbol]) -> str:
    poly, _multiplier = primitive_polynomial(expr, variables)
    rendered: list[str] = []
    for monomial, coefficient in poly.terms():
        coefficient = sp.Integer(coefficient)
        if coefficient == 0:
            continue
        factors = []
        for variable, exponent in zip(variables, monomial):
            if exponent == 1:
                factors.append(str(variable))
            elif exponent > 1:
                factors.append(f"{variable}^{exponent}")
        magnitude = abs(coefficient)
        body = "*".join(factors)
        if body and magnitude == 1:
            term = body
        elif body:
            term = f"{magnitude}*{body}"
        else:
            term = str(magnitude)
        if not rendered:
            rendered.append(("-" if coefficient < 0 else "") + term)
        else:
            rendered.append((" - " if coefficient < 0 else " + ") + term)
    return "".join(rendered) if rendered else "0"


def emit_singular_centered(reduction: R3Reduction, characteristic: int, c_value: int | None) -> pathlib.Path:
    n, m, M2, s, k = reduction.row
    tag = f"r3_{n}_{m}_{M2}_{s}_k{k}"
    suffix = "satc" if c_value is None else f"c{c_value}"
    field = "0" if characteristic == 0 else str(characteristic)
    path = HERE / f"{tag}_centered_{suffix}_{'Q' if characteristic == 0 else 'p' + str(characteristic)}.sing"
    variables = reduction.fvars[1:]  # F1 is killed by the translation slice.
    subs = {reduction.fvars[0]: 0}
    rows = [sp.expand(expr.subs(subs)) for _degree, expr in reduction.residual_zero_rows]
    rows.append(sp.expand(reduction.top_row.subs(subs)))
    if c_value is not None:
        rows = [sp.expand(expr.subs(reduction.c, c_value)) for expr in rows]
        ring_vars = variables
        generators = [singular_poly(expr, ring_vars) for expr in rows if expr != 0]
    else:
        ring_vars = variables + [reduction.c, sp.Symbol("T")]
        generators = [singular_poly(expr, variables + [reduction.c]) for expr in rows if expr != 0]
        generators.append("T*c-1")
    lines = [
        f"// {tag}; centered F1=0; reciprocal R3 residual",
        f"// Q* G-pivots={len(reduction.pivots)}; c_value={c_value}",
        f"ring R={field},({','.join(map(str, ring_vars))}),dp;",
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); } else { print("CONTROL_RING_FAIL"); }',
    ]
    if c_value is None:
        lines.extend(
            [
                "ideal CE=c,T*c-1; ideal GE=std(CE);",
                'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
                "ideal CN=c-1,T*c-1; ideal GN=std(CN);",
                'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
            ]
        )
    else:
        lines.append(f'print("CONTROL_C_SLICE c={c_value}");')
    lines.extend(
        [
            f'print("MAIN_START row={n}_{m}_{M2}_{s}_k{k} char={field} centered=1 c_value={c_value} rows={len(generators)} vars={len(ring_vars)}");',
            "ideal I=" + ",\n".join(generators) + ";",
            "ideal G=std(I);",
            'print("MAIN_DONE basis_size=");',
            "size(G);",
            'if (reduce(1,G)==0) { print("MAIN_UNIT"); G; } else { print("MAIN_NONTRIVIAL"); print("dim="); dim(G); print("vdim="); vdim(G); }',
            "quit;",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_audit(reductions: list[R3Reduction], custody: dict) -> pathlib.Path:
    audit = {
        "custody": custody,
        "method": "reciprocal coefficient reindex, affine Q* elimination of G_1..G_(3s)",
        "fallacy_v2": {
            "pivot_rule": "only nonzero rational constants 2*j are divided",
            "ring_map": "F_i=a_(2s-i), G_i=b_(3s-i), c fixed",
            "saturation": "Rabinowitsch T*c-1 retained for saturated systems; c=1 is a homogeneous torus slice only",
        },
        "rows": [],
    }
    for red in reductions:
        n, m, M2, s, k = red.row
        weights_ok = True
        weights = {str(red.fvars[i - 1]): i for i in range(1, 2 * s + 1)}
        weights.update({str(red.gvars[i - 1]): i for i in range(1, 3 * s + 1)})
        weights["c"] = 5 * s - 1
        residual_exprs = [expr for _degree, expr in red.residual_zero_rows] + [red.top_row]
        centered_exprs = [sp.expand(expr.subs(red.fvars[0], 0)) for expr in residual_exprs]
        variables_centered = red.fvars[1:] + [red.c]
        for expr in centered_exprs:
            poly = sp.Poly(expr, *variables_centered, domain=sp.QQ)
            term_weights = set()
            for monomial, coeff in poly.terms():
                if coeff == 0:
                    continue
                total = 0
                for var, exp in zip(variables_centered, monomial):
                    total += weights[str(var)] * exp
                term_weights.add(total)
            weights_ok = weights_ok and len(term_weights) <= 1
        frozen = []
        for char_tag in ("Q", "mod32003"):
            name = f"R3ode_{n}_{m}_{M2}_{s}_k{k}_{char_tag}.sing"
            fpath = FROZEN_DIR / name
            if fpath.is_file():
                text = fpath.read_text(encoding="utf-8")
                match = re.search(r'MAIN_START equations=" \\+ string\\(size\\(I\\)-1\\) \\+ " unknowns=', text)
                frozen.append(
                    {
                        "basename": name,
                        "sha256": sha256_file(fpath),
                        "present_in_frozen_inputs": True,
                    }
                )
            else:
                frozen.append({"basename": name, "present_in_frozen_inputs": False})
        audit["rows"].append(
            {
                "row": [n, m, M2, s, k],
                "f_degree": 2 * s,
                "g_degree": 3 * s,
                "r3_unknowns_including_c": 5 * s + 1,
                "r3_equations": 5 * s - 1,
                "pivots": [
                    {
                        "step": pivot.step,
                        "row_degree_z": pivot.row_degree,
                        "variable": str(pivot.variable),
                        "coefficient": str(pivot.coefficient),
                        "rhs": str(pivot.rhs),
                    }
                    for pivot in red.pivots
                ],
                "residual_rows_after_g_pivots": len(red.residual_zero_rows) + 1,
                "residual_variables_F_plus_c": len(red.fvars) + 1,
                "centered_c_slice_variables": len(red.fvars) - 1,
                "weights": weights,
                "centered_residual_homogeneous": weights_ok,
                "residual_hash": expression_hash(residual_exprs),
                "centered_residual_hash": expression_hash(centered_exprs),
                "preprocess_elapsed_seconds": round(red.elapsed_seconds, 6),
                "frozen_systems": frozen,
            }
        )
    path = HERE / "r3_preprocess_audit.json"
    path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


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
    out_path = path.with_suffix(path.suffix + ".out")
    err_path = path.with_suffix(path.suffix + ".err")
    if isinstance(stdout, bytes):
        stdout = stdout.decode("utf-8", errors="replace")
    if isinstance(stderr, bytes):
        stderr = stderr.decode("utf-8", errors="replace")
    out_path.write_text(stdout, encoding="utf-8")
    err_path.write_text(stderr, encoding="utf-8")
    return {
        "script": str(path.relative_to(ROOT)),
        "script_sha256": sha256_file(path),
        "stdout": str(out_path.relative_to(ROOT)),
        "stderr": str(err_path.relative_to(ROOT)),
        "status": status,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "main_unit": "MAIN_UNIT" in stdout,
        "main_nontrivial": "MAIN_NONTRIVIAL" in stdout,
        "main_done": "MAIN_DONE" in stdout,
        "stdout_tail": stdout.splitlines()[-20:],
        "stderr_tail": stderr.splitlines()[-20:],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--prime", type=int, default=32003)
    parser.add_argument(
        "--rows",
        default="all",
        help="comma-separated V2' values to process, or all",
    )
    args = parser.parse_args()

    if HERE != ROOT / "box/r3pre-20260903":
        raise RuntimeError("driver must stay in box/r3pre-20260903")

    custody = verify_receipt()
    if args.rows == "all":
        selected_rows = ROWS
    else:
        wanted = {int(part) for part in args.rows.split(",") if part}
        selected_rows = [row for row in ROWS if row[3] in wanted]
    reductions = []
    for row in selected_rows:
        print(f"REDUCE_START row={row}", flush=True)
        reductions.append(reduce_r3(row))
        print(f"REDUCE_DONE row={row} pivots={len(reductions[-1].pivots)}", flush=True)
    audit_path = write_audit(reductions, custody)
    scripts = []
    for red in reductions:
        scripts.append(emit_singular_centered(red, args.prime, c_value=1))
        scripts.append(emit_singular_centered(red, 0, c_value=1))
        scripts.append(emit_singular_centered(red, args.prime, c_value=None))
    run_records = []
    if args.run:
        for script in scripts:
            run_records.append(run_singular(script, args.timeout))
    run_path = HERE / "singular_runs.json"
    run_path.write_text(json.dumps(run_records, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"audit": str(audit_path), "scripts": [str(p) for p in scripts], "runs": str(run_path)}, indent=2))


if __name__ == "__main__":
    main()
