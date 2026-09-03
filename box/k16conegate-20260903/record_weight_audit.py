#!/usr/bin/env python3
"""Finite record homogeneity checks for the frozen terminal JSON records."""
from __future__ import annotations

import json
import pathlib
import re
from typing import Iterable

import sympy as sp

INPUT = pathlib.Path("/tmp/jc2-lane.JyEMIr/inputs")
OUT = pathlib.Path("/home/ubuntu/jc2/box/k16conegate-20260903")

RECORDS = [
    "terminal_laurent_t2.json",
    "terminal_laurent_t3.json",
    "terminal_laurent_t4.json",
    "terminal_laurent_t5.json",
    "chart_t3_b4_0.json",
    "chart_t5_b4_0.json",
    "chart_t6_b4_0.json",
]


def symbol_table(t: int) -> dict[str, sp.Symbol]:
    names = ["h", "s", "b1", "b2", "b3", "b4", "B0", f"q{2*t+1}_1"]
    names += [f"C{j}" for j in range(1, t)]
    names += [f"q{j}_0" for j in range(2, 2*t + 1)]
    return {name: sp.Symbol(name) for name in names}


def weight_of(name: str, t: int) -> int:
    if name in ("h", "s", "b4"):
        return 1
    if name == "B0":
        return t
    if name == "b1":
        return 3*t + 1
    if name == "b2":
        return 2*t + 1
    if name == "b3":
        return t + 1
    match = re.fullmatch(r"C(\d+)", name)
    if match:
        return int(match.group(1))
    match = re.fullmatch(r"q(\d+)_0", name)
    if match:
        return int(match.group(1))
    match = re.fullmatch(r"q(\d+)_1", name)
    if match:
        return 0
    raise KeyError(name)


def parse(expr: str, ns: dict[str, sp.Symbol]) -> sp.Expr:
    return sp.expand(sp.sympify(expr, locals=ns))


def monomial_weights(expr: sp.Expr, t: int, y: sp.Symbol) -> set[int]:
    expr = sp.expand(expr)
    if expr == 0:
        return set()
    vars_ = sorted(expr.free_symbols, key=lambda s: str(s))
    if not vars_:
        return {0}
    poly = sp.Poly(expr, *vars_, domain="QQ")
    weights: set[int] = set()
    for mon, _coeff in poly.terms():
        total = 0
        for sym, exp in zip(vars_, mon):
            if sym == y:
                continue
            total += weight_of(str(sym), t) * exp
        weights.add(total)
    return weights


def is_homogeneous(expr: sp.Expr, t: int, y: sp.Symbol, target: int) -> bool:
    weights = monomial_weights(expr, t, y)
    return not weights or weights == {target}


def mod_h(expr: sp.Expr, y: sp.Symbol, H: sp.Expr) -> sp.Expr:
    expr = sp.cancel(sp.together(sp.expand(expr)))
    numer, denom = sp.fraction(expr)
    rem = sp.rem(sp.Poly(sp.expand(numer), y), sp.Poly(H, y)).as_expr()
    return sp.expand(sp.cancel(rem / denom))


def check_record(name: str) -> dict[str, object]:
    rec = json.loads((INPUT / name).read_text(encoding="utf-8"))
    t = int(rec["t"])
    ns = symbol_table(t)
    y = ns[f"q{2*t+1}_1"]
    H = parse(str(rec["H"]), ns)
    terminal_failures = []
    terminal_rows = {int(item["band"]): parse(str(item["expr"]), ns)
                     for item in rec["terminal"]}

    c = parse(str(rec["normalizer"]["c"]), ns)
    terminal_vars = [ns[v] for v in rec.get("terminal_variables", [])]
    for band, expr in sorted(terminal_rows.items()):
        if band == 0:
            const = expr
            for var in terminal_vars:
                const = const.subs(var, 0)
            if mod_h(const - c, y, H) != 0:
                terminal_failures.append({"band": band, "reason": "constant != c"})
            tau = sp.expand(expr - c)
            if not is_homogeneous(tau, t, y, 4*t + 1):
                terminal_failures.append({
                    "band": band,
                    "reason": "tau weight",
                    "weights": sorted(monomial_weights(tau, t, y)),
                    "target": 4*t + 1,
                })
        else:
            target = 4*t + 1 - band
            if not is_homogeneous(expr, t, y, target):
                terminal_failures.append({
                    "band": band,
                    "reason": "terminal weight",
                    "weights": sorted(monomial_weights(expr, t, y)),
                    "target": target,
                })

    pivot_failures = []
    def check_rhs(label: str, expr: sp.Expr, target: int) -> None:
        if not is_homogeneous(expr, t, y, target):
            pivot_failures.append({
                "label": label,
                "weights": sorted(monomial_weights(expr, t, y)),
                "target": target,
            })

    if "B0_gauge_pivot" in rec:
        check_rhs("B0_gauge_rhs", parse(str(rec["B0_gauge_pivot"]["rhs"]), ns), t)
    if "b1_divisibility_pivot" in rec:
        check_rhs("b1_rhs", parse(str(rec["b1_divisibility_pivot"]["rhs"]), ns), 3*t + 1)
    for item in rec.get("high_pivots", []):
        var = str(item["variable"])
        check_rhs(f"{var}_rhs", parse(str(item["rhs"]), ns), weight_of(var, t))
        coeff_weights = monomial_weights(parse(str(item["coefficient"]), ns), t, y)
        if coeff_weights and coeff_weights != {0}:
            pivot_failures.append({
                "label": f"{var}_coefficient",
                "weights": sorted(coeff_weights),
                "target": 0,
            })

    return {
        "record": name,
        "t": t,
        "b4_chart": rec.get("b4_chart"),
        "terminal_rows": len(terminal_rows),
        "terminal_ok": not terminal_failures,
        "pivot_rhs_ok": not pivot_failures,
        "terminal_failures": terminal_failures,
        "pivot_failures": pivot_failures,
    }


def main() -> None:
    results = [check_record(name) for name in RECORDS]
    all_ok = all(item["terminal_ok"] and item["pivot_rhs_ok"] for item in results)
    for item in results:
        print(
            f"{item['record']}: t={item['t']} chart={item['b4_chart']} "
            f"terminal_ok={item['terminal_ok']} pivot_rhs_ok={item['pivot_rhs_ok']}"
        )
    print("RECORD_WEIGHT_AUDIT =", "PASS" if all_ok else "FAIL")
    (OUT / "record_weight_audit.json").write_text(
        json.dumps({"status": "PASS" if all_ok else "FAIL", "records": results},
                   indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
