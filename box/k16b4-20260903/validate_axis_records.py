#!/usr/bin/env python3
"""Compare axis_exact.py with the authenticated frozen Laurent records t=2..5."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib

import sympy as sp


def reduced_pair(expr: sp.Expr, t: int, d: sp.Symbol) -> tuple[str, str]:
    num, den = sp.cancel(expr).as_numer_denom()
    modulus = sp.Poly(3 * d**2 - (t + 1), d, domain=sp.QQ)
    npoly = sp.Poly(sp.expand(num), d, domain=sp.QQ).rem(modulus)
    dpoly = sp.Poly(sp.expand(den), d, domain=sp.QQ).rem(modulus)
    value = (npoly * sp.invert(dpoly, modulus)).rem(modulus).as_expr()
    value = sp.Poly(value, d, domain=sp.QQ)
    return (str(value.coeff_monomial(d)), str(value.coeff_monomial(1)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("axis_jsonl", type=pathlib.Path)
    parser.add_argument("inputs", type=pathlib.Path)
    args = parser.parse_args()
    axes = {int(x["t"]): x for x in map(json.loads,
                                         args.axis_jsonl.read_text().splitlines())}
    summary = []
    for t in range(2, 6):
        path = args.inputs / f"terminal_laurent_t{t}.json"
        raw = path.read_bytes()
        record = json.loads(raw)
        d = sp.Symbol("d")
        y = sp.Symbol(f"q{2*t+1}_1")
        b3, b4 = sp.symbols("b3 b4")
        killed = {b3: 0, b4: 1, y: (d + t + 1) / sp.Integer(2 * (2*t+1))}
        killed.update({sp.Symbol(f"q{j}_0"): 0 for j in range(2, t)})
        checked = 0
        for frozen, exact in zip(record["terminal"], axes[t]["rows"], strict=True):
            # Frozen records store R=-E, whereas axis_exact stores T=E.
            pair = reduced_pair(-sp.sympify(frozen["expr"]).subs(killed), t, d)
            expected = (exact["d_coefficient"], exact["constant_coefficient"])
            if pair != expected:
                raise AssertionError((t, frozen["band"], pair, expected))
            checked += 1
        item = {"t": t, "rows_checked": checked, "status": "PASS",
                "record": path.name, "record_sha256": hashlib.sha256(raw).hexdigest()}
        summary.append(item)
        print(json.dumps(item, sort_keys=True))
    print(json.dumps({"status": "ALL_PASS", "records": len(summary),
                      "rows": sum(x["rows_checked"] for x in summary)}, sort_keys=True))


if __name__ == "__main__":
    main()
