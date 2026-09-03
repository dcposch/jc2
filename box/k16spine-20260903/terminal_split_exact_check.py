#!/usr/bin/env python3
"""Exact product-algebra terminal checks for a split Laurent record.

This is deliberately small: the current exact split control is t=2.  Each
rational factor of H_t is evaluated separately, so no zero divisor is ever
inverted.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def is_unit(rows, variables):
    basis = sp.groebner(rows, *variables, domain=sp.QQ)
    return any(poly.as_expr().is_number and poly.as_expr() != 0
               for poly in basis.polys), [str(poly.as_expr()) for poly in basis.polys]


source = HERE / "terminal_laurent_t2.json"
record = json.loads(source.read_text(encoding="utf-8"))
t = int(record["t"])
y, b3, b4 = sp.symbols("q5_1 b3 b4")
H = sp.Poly(sp.sympify(record["H"]), y, domain=sp.QQ)
roots = sorted(sp.solve(H.as_expr(), y))
if roots != [sp.Rational(1, 5), sp.Rational(2, 5)]:
    raise AssertionError(roots)
rows = [(int(item["band"]), sp.sympify(item["expr"]))
        for item in record["terminal"]]
checks = []
for root in roots:
    for chart in (0, 1):
        full = [sp.expand(expr.subs({y: root, b4: chart})) for _, expr in rows]
        unit, basis = is_unit(full, [b3])
        if not unit:
            raise AssertionError((root, chart, "full", basis))
        checks.append({"y": str(root), "b4": chart, "system": "full",
                       "unit": True, "basis": basis})
    top = [sp.expand(expr.subs({y: root, b4: 1}))
           for band, expr in rows if band >= t]
    unit, basis = is_unit(top, [b3])
    if not unit:
        raise AssertionError((root, "top", basis))
    checks.append({"y": str(root), "b4": 1, "system": "top_t",
                   "unit": True, "basis": basis})

output = HERE / "terminal_laurent_t2_product_exact.json"
output.write_text(json.dumps({
    "typing": "EXACT product-algebra check; no zero-divisor inversion",
    "source": source.name,
    "t": t,
    "H_roots": [str(root) for root in roots],
    "checks": checks,
}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"TERMINAL_SPLIT_EXACT_PASS checks={len(checks)} path={output.name}")
