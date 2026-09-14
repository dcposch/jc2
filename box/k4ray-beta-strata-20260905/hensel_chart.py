#!/usr/bin/env python3
"""Hensel DIV-band reduction for 1-scalar LEVEL-4 shapes (q1-cover and q1=0 slice).

The generic q0-chart has q1-dependent pivots (hensel-probe.json) and is NOT
reduced here.  G_m sets the remaining top coefficient to 1; Jacobian
nonvanishing is tau*CST-1.  That group element is the weighted scaling of
the tower, as in box/k4rayk89-20260903/hensel_reduced_sol56.py.

Pivot matrices are required to lie in Q.  A nonconstant pivot aborts.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import ceil, lcm
from pathlib import Path
import sys
import time
from typing import Any

import sympy as sp

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "k4ray-beta-strata-20260905"
RUNS = HERE / "hensel-runs"
sys.path.insert(0, str(ROOT))

from box.lib.guided_gb import (  # noqa: E402
    PromotionPolicy,
    RunConfig,
    SingularSystem,
    guided_groebner,
)


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(payload, encoding="utf-8")
    tmp.replace(path)


def monomials(total_max: int) -> list[tuple[int, int]]:
    if total_max < 0:
        return []
    return [(i, j) for j in range(total_max + 1) for i in range(total_max - j + 1)]


def product_coefficient(left, right, ti, tj, subs):
    result = sp.Integer(0)
    for (i, j), coefficient in left.items():
        other = right.get((ti - i, tj - j))
        if other is None:
            continue
        if isinstance(coefficient, sp.Symbol):
            coefficient = subs.get(coefficient, coefficient)
        if isinstance(other, sp.Symbol):
            other = subs.get(other, other)
        result += coefficient * other
    return sp.expand(result)


def rational(value: Any) -> Fraction:
    value = sp.Rational(value)
    return Fraction(int(value.p), int(value.q))


def spq(value: Fraction) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


def singular_expr(expr: sp.Expr) -> str:
    # Singular does not continue lines; sympy may wrap huge polynomials.
    text = sp.sstr(sp.expand(expr), order="lex").replace("**", "^")
    return "".join(text.split())


def exact_rref(matrix: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[list[Fraction]], list[int]]:
    row_count = len(matrix)
    column_count = len(matrix[0]) if matrix else 0
    work = [list(row) for row in matrix]
    transform = [[Fraction(int(i == j), 1) for j in range(row_count)] for i in range(row_count)]
    pivots: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        found = next((row for row in range(pivot_row, row_count) if work[row][column]), None)
        if found is None:
            continue
        if found != pivot_row:
            work[pivot_row], work[found] = work[found], work[pivot_row]
            transform[pivot_row], transform[found] = transform[found], transform[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        transform[pivot_row] = [entry / scale for entry in transform[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not work[row][column]:
                continue
            multiple = work[row][column]
            work[row] = [entry - multiple * pivot_entry for entry, pivot_entry in zip(work[row], work[pivot_row])]
            transform[row] = [
                entry - multiple * pivot_entry
                for entry, pivot_entry in zip(transform[row], transform[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return work, transform, pivots


def smin_of(K: int) -> int:
    return ceil(2 * (K - 1) / 3)


def poly_from_terms(terms, x, y):
    return sp.Add(*(c * x**i * y**j for (i, j), c in terms.items()), sp.Integer(0))


def resolved(terms, subs):
    out = {}
    for mon, c in terms.items():
        if isinstance(c, sp.Symbol):
            c = subs.get(c, c)
        out[mon] = c
    return out


def build(K: int, b: int, mode: str) -> dict[str, Any]:
    smin = smin_of(K)
    d = b - smin - 1
    rdeg = 3 * b - 2 * K
    x, y = sp.symbols("x y")
    if mode == "q1":
        Q = (x ** (d - 1) * y) if d >= 1 else sp.Integer(1)
        cover = "q0=0,q1=1"
    elif mode == "q0_q1zero":
        Q = x**d if d >= 0 else sp.Integer(1)
        cover = "q0=1,q1=0"
    else:
        raise ValueError(f"mode {mode} is not a constant-pivot 1-scalar chart")

    P = sp.expand(y**smin * (y - x) * Q)
    Hpoly = sp.expand(y ** (K - 1) * (y - x))
    Btop = sp.expand(2 * P)
    Atop = sp.div(sp.Poly(4 * P**2, x, y), sp.Poly(Hpoly, x, y))[0].as_expr()
    Rtop = sp.expand(sp.div(sp.Poly(4 * P**3, x, y), sp.Poly(Hpoly**2, x, y))[0].as_expr() / 3)

    def terms_of(expr: sp.Expr) -> dict[tuple[int, int], sp.Expr]:
        out: dict[tuple[int, int], sp.Expr] = {}
        for (i, j), c in sp.Poly(sp.expand(expr), x, y).terms():
            out[(int(i), int(j))] = sp.expand(c)
        return out

    h_terms = terms_of(Hpoly)
    B_terms = terms_of(Btop)
    A_terms = terms_of(Atop)
    symbols_by_kind_degree: dict[tuple[str, int], list[sp.Symbol]] = {}
    symbol_weights: dict[sp.Symbol, int] = {}
    all_symbols: list[sp.Symbol] = []

    def add_lower(kind: str, maximum: int, bucket: dict) -> None:
        for i, j in monomials(maximum):
            if kind == "h" and (i, j) == (0, K - 1):
                continue
            if (i, j) in bucket and not isinstance(bucket[(i, j)], sp.Symbol):
                continue
            symbol = sp.Symbol(f"{kind}_{i}_{j}")
            bucket[(i, j)] = symbol
            symbols_by_kind_degree.setdefault((kind, i + j), []).append(symbol)
            if kind == "h":
                symbol_weights[symbol] = K - i - j
            elif kind == "B":
                symbol_weights[symbol] = 2 * K - i - j
            else:
                symbol_weights[symbol] = 3 * K - i - j
            all_symbols.append(symbol)

    add_lower("h", K - 1, h_terms)
    add_lower("B", b - 1, B_terms)
    add_lower("A", max(2 * b - K - 1, -1), A_terms)

    rtop_terms = terms_of(Rtop)

    def target_r(i: int, j: int, degree: int) -> sp.Expr:
        if degree > rdeg:
            return sp.Integer(0)
        if degree == rdeg:
            return rtop_terms.get((i, j), sp.Integer(0))
        raise AssertionError("target_r below rdeg")

    substitutions: dict[sp.Symbol, sp.Expr] = {}
    compatibility: list[sp.Expr] = []
    audit = []
    original_count = len(all_symbols)

    for degree in range(2 * b - 1, rdeg - 1, -1):
        new_variables: list[sp.Symbol] = []
        for kind, component_degree in (
            ("h", degree - (2 * b - K)),
            ("A", degree - K),
            ("B", degree - b),
        ):
            new_variables.extend(symbols_by_kind_degree.get((kind, component_degree), []))
        new_variables = [v for v in new_variables if v not in substitutions]
        equations = []
        for i in range(degree + 1):
            j = degree - i
            eq = (
                product_coefficient(B_terms, B_terms, i, j, substitutions)
                - product_coefficient(A_terms, h_terms, i, j, substitutions)
                - target_r(i, j, degree)
            )
            equations.append(sp.expand(eq))
        zero_new = {v: sp.Integer(0) for v in new_variables}
        matrix: list[list[Fraction]] = []
        right: list[sp.Expr] = []
        for equation in equations:
            coeffs = [sp.expand(equation).coeff(v) for v in new_variables]
            rest = sp.expand(equation.xreplace(zero_new))
            reconstructed = sp.expand(rest + sum((c * v for c, v in zip(coeffs, new_variables)), sp.Integer(0)))
            if sp.expand(equation - reconstructed) != 0:
                raise AssertionError(f"DIV band {degree} is not linear")
            if any(c.free_symbols for c in coeffs):
                raise AssertionError(f"DIV band {degree} has a nonconstant pivot matrix")
            matrix.append([rational(c) for c in coeffs])
            right.append(-rest)
        rref, transform, pivots = exact_rref(matrix)
        transformed_right = [
            sp.expand(sum((spq(c) * e for c, e in zip(row, right)), sp.Integer(0))) for row in transform
        ]
        free_columns = [col for col in range(len(new_variables)) if col not in pivots]
        for row, pivot_column in enumerate(pivots):
            expression = transformed_right[row]
            for column in free_columns:
                if rref[row][column]:
                    expression -= spq(rref[row][column]) * new_variables[column]
            substitutions[new_variables[pivot_column]] = sp.expand(expression)
        n_compat = 0
        for row in range(len(pivots), len(equations)):
            if any(rref[row]):
                raise AssertionError("RREF zero-row accounting failed")
            expression = sp.expand(transformed_right[row])
            if expression == 0:
                continue
            compatibility.append(expression)
            n_compat += 1
        audit.append(
            {
                "degree": degree,
                "n_eq": len(equations),
                "n_new": len(new_variables),
                "rank": len(pivots),
                "compat": n_compat,
            }
        )

    free = [s for s in all_symbols if s not in substitutions]
    h_expr = sp.expand(poly_from_terms(resolved(h_terms, substitutions), x, y))
    B_expr = sp.expand(poly_from_terms(resolved(B_terms, substitutions), x, y))
    A_expr = sp.expand(poly_from_terms(resolved(A_terms, substitutions), x, y))
    R_expr = sp.expand(B_expr**2 - A_expr * h_expr)
    JJ = sp.expand(
        sp.Rational(3, 8) * (sp.diff(B_expr, x) * sp.diff(A_expr, y) - sp.diff(B_expr, y) * sp.diff(A_expr, x))
        - sp.Rational(3, 4) * (sp.diff(h_expr, x) * sp.diff(R_expr, y) - sp.diff(h_expr, y) * sp.diff(R_expr, x))
    )
    j_rows: list[tuple[int, int, str]] = []
    target = None
    polyJ = sp.Poly(JJ, x, y)
    for (i, j), coeff in polyJ.terms():
        coeff = sp.expand(coeff)
        if coeff == 0:
            continue
        if (int(i), int(j)) == (4, 0):
            target = coeff
        else:
            j_rows.append((int(i), int(j), singular_expr(coeff)))
    if target is None or target == 0:
        raise AssertionError("x^4 Jacobian coefficient vanished after Hensel reconstruction")
    names = [str(s) for s in free] + ["tau"]
    weights = [symbol_weights[s] for s in free] + [1]
    return {
        "K": K,
        "b": b,
        "mode": mode,
        "cover": cover,
        "smin": smin,
        "d": d,
        "rdeg": rdeg,
        "original": original_count,
        "pivots": len(substitutions),
        "free": len(free),
        "compat": len(compatibility),
        "audit": audit,
        "compat_exprs": [singular_expr(e) for e in compatibility],
        "j_rows": j_rows,
        "target": singular_expr(target),
        "n_j_rows": len(j_rows),
        "names": names,
        "weights": weights,
        "normalization": "G_m sets remaining top coefficient to 1; tau*CST-1",
    }


QUOY = """proc quoy(poly p, poly hh, int K)
{ poly q=0; poly ld; matrix cp; int d;
  while(1){ if(p==0){break;} cp=coeffs(p,y); d=nrows(cp)-1; if(d<K){break;}
    ld=cp[d+1,1]; q=q+ld*y^(d-K); p=p-ld*y^(d-K)*hh; } return(q); }"""


def prelude_from(data: dict[str, Any], ch: int, tk: int = 4) -> str:
    names = data["names"]
    weights = data["weights"]
    # Parameter ring only: J coefficients are already extracted over Q in sympy.
    lines = [
        "option(redSB); short=0;",
        f"// hensel 1-scalar K={data['K']} b={data['b']} mode={data['mode']} free={data['free']}",
        f"ring SS = {ch},({','.join(names)}),wp({','.join(str(w) for w in weights)});",
        "ideal I0;",
    ]
    for expr in data["compat_exprs"]:
        if expr and expr != "0":
            lines.append(f"I0 = I0 + ideal({expr});")
    lines.append('print("PRE__COMPAT "+string(size(I0)));')
    for i, j, expr in data["j_rows"]:
        if expr and expr != "0":
            lines.append(f"I0 = I0 + ideal({expr});")
    lines += [
        "I0 = simplify(I0,2);",
        'print("PRE__J_ROWS "+string(size(I0)));',
        f"poly CSTP = {data['target']};",
        'print("PRE__CST_ZERO "+string(CSTP==0));',
        'print("PRE__TARGET_FOUND 1");',
        "ideal ROWS = I0;",
        'print("PRE__NROWS "+string(size(ROWS)));',
        f'print("PRE__NPARAMS_GB {len(names)}");',
        'print("PRE__PRELUDE_DONE 1");',
    ]
    return "\n".join(lines)


def run_singular_count(prelude: str, tag: str, timeout: int) -> dict[str, Any]:
    import subprocess

    RUNS.mkdir(parents=True, exist_ok=True)
    script = RUNS / f"{tag}.count.sing"
    atomic_write(script, prelude + '\nprint("PRE__ROWS_FINAL "+string(size(ROWS)));\nquit;\n')
    t0 = time.time()
    try:
        proc = subprocess.run(
            ["stdbuf", "-oL", "-eL", "Singular", "--no-rc", "-q", str(script)],
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        stdout, stderr, timed_out, rc = proc.stdout, proc.stderr, False, proc.returncode
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", errors="replace")
        timed_out, rc = True, None
    atomic_write(RUNS / f"{tag}.count.out", stdout)
    markers = {}
    for line in stdout.splitlines():
        if line.startswith("PRE__"):
            parts = line.split(maxsplit=1)
            markers[parts[0]] = parts[1] if len(parts) > 1 else ""
    info = {
        "tag": tag,
        "wall": round(time.time() - t0, 3),
        "timed_out": timed_out,
        "returncode": rc,
        "n": int(markers["PRE__ROWS_FINAL"]) if "PRE__ROWS_FINAL" in markers else None,
        "markers": markers,
    }
    atomic_write(RUNS / f"{tag}.rowcount.json", json.dumps(info, indent=2, sort_keys=True) + "\n")
    return info


def run_chart(tag: str, K: int, b: int, mode: str, chars: tuple[int, ...], timeout: int, count_timeout: int, cores: int) -> dict[str, Any]:
    t_build = time.time()
    data = build(K, b, mode)
    data["build_wall"] = round(time.time() - t_build, 3)
    atomic_write(RUNS / tag / "reduced.json", json.dumps({k: v for k, v in data.items() if k not in ("h", "B", "compat_exprs")}, indent=2) + "\n")
    systems = []
    counts = []
    for ch in chars:
        prelude = prelude_from(data, ch)
        info = run_singular_count(prelude, f"{tag}_p{ch}", count_timeout)
        counts.append(info)
        markers = info.get("markers") or {}
        if info["n"] is None:
            continue
        if markers.get("PRE__TARGET_FOUND") != "1" or markers.get("PRE__CST_ZERO") == "1":
            # A vanished target makes tau*CSTP-1 = -1, a fake unit. Refuse.
            continue
        generators = [f"ROWS[{i}]" for i in range(1, info["n"] + 1)] + ["tau*CSTP-1"]
        systems.append(
            SingularSystem(
                name=f"{tag}_p{ch}",
                prelude=prelude,
                generators=tuple(generators),
                characteristic=ch,
                variables=tuple(data["names"]),
                homogeneous=False,
                metadata={"K": K, "b": b, "mode": mode, "free": data["free"]},
            )
        )
    if not systems:
        summary = {"tag": tag, "verdict": "PRELUDE_FAILED", "counts": counts, "data": {k: data[k] for k in ("K", "b", "mode", "free", "pivots", "compat")}}
        atomic_write(RUNS / tag / "summary.json", json.dumps(summary, indent=2) + "\n")
        print(json.dumps(summary, sort_keys=True))
        return summary
    result = guided_groebner(
        systems,
        hint=None,
        policy=PromotionPolicy.exact_q("hensel 1-scalar stratum; exact Q only"),
        config=RunConfig(RUNS / tag, timeout_seconds=timeout, total_cores=cores, max_parallel_jobs=min(len(systems), cores), run_perturbed_control=False),
    )
    summary = {
        "tag": tag,
        "K": K,
        "b": b,
        "mode": mode,
        "cover": data["cover"],
        "free": data["free"],
        "pivots": data["pivots"],
        "original": data["original"],
        "compat": data["compat"],
        "build_wall": data["build_wall"],
        "counts": counts,
        "verdict": result.verdict.value,
        "promotion_note": result.certificate["promotion_note"],
        "accepted_run_count": result.certificate["accepted_run_count"],
        "runs": [
            {
                "char": run["characteristic"],
                "unit": run["main"]["unit"],
                "dimension": run["main"]["dimension"],
                "basis_size": run["main"]["basis_size"],
                "timed_out": run["timed_out"],
                "elapsed_seconds": run["elapsed_seconds"],
                "stdout_sha256": run["stdout_sha256"],
                "script_sha256": run["script_sha256"],
            }
            for run in result.certificate["runs"]
        ],
    }
    atomic_write(RUNS / tag / "summary.json", json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, sort_keys=True))
    return summary


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    pm = sub.add_parser("meta")
    pm.add_argument("K", type=int)
    pm.add_argument("b", type=int)
    pm.add_argument("--mode", required=True, choices=("q1", "q0_q1zero"))
    pr = sub.add_parser("run")
    pr.add_argument("tag")
    pr.add_argument("K", type=int)
    pr.add_argument("b", type=int)
    pr.add_argument("--mode", required=True, choices=("q1", "q0_q1zero"))
    pr.add_argument("--chars", default="0")
    pr.add_argument("--timeout", type=int, default=600)
    pr.add_argument("--count-timeout", type=int, default=240)
    pr.add_argument("--cores", type=int, default=4)
    args = p.parse_args()
    if args.cmd == "meta":
        t0 = time.time()
        data = build(args.K, args.b, args.mode)
        data["build_wall"] = round(time.time() - t0, 3)
        slim = {k: data[k] for k in ("K", "b", "mode", "cover", "original", "pivots", "free", "compat", "rdeg", "audit", "build_wall")}
        print(json.dumps(slim, indent=2))
    else:
        chars = tuple(int(x) for x in args.chars.split(",") if x)
        run_chart(args.tag, args.K, args.b, args.mode, chars, args.timeout, args.count_timeout, args.cores)


if __name__ == "__main__":
    main()
