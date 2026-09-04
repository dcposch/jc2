#!/usr/bin/env python3
"""Load a charged terminal_laurent_tN.json into sympy (ring map declared).

Coefficient field: Q.  Generator order: residual variables of the record
plus the chart coordinate y = q_{2t+1,1}.  Image check: H and d strings
must match the closed forms H_t, d=2qy-(t+1).
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

INP = Path("/tmp/jc2-lane.SxWsoD/inputs")


def H_poly(t: int, y: sp.Symbol) -> sp.Expr:
    q = 2 * t + 1
    return 12 * q**2 * y**2 - 12 * q * (t + 1) * y + (t + 1) * (3 * t + 2)


def load(t: int) -> dict:
    D = json.loads((INP / f"terminal_laurent_t{t}.json").read_text())
    assert int(D["t"]) == t
    vs = [sp.Symbol(name) for name in D["terminal_variables"]]
    names = {s.name: s for s in vs}
    H_expr = sp.sympify(D["H"], locals=names)
    extra = [s for s in H_expr.free_symbols if s.name not in names]
    assert len(extra) == 1, extra
    y = extra[0]
    names[y.name] = y
    H_chk = sp.expand(H_expr - H_poly(t, y))
    assert H_chk == 0, H_chk
    d_expr = sp.expand(sp.sympify(D["d"], locals=names))
    d_chk = sp.expand(d_expr - (2 * (2 * t + 1) * y - (t + 1)))
    assert d_chk == 0, d_chk
    rows = {}
    for rec in D["terminal"]:
        k = int(rec["band"])
        rows[k] = sp.expand(sp.sympify(rec["expr"], locals=names))
    return {
        "t": t,
        "y": y,
        "H": H_expr,
        "d": d_expr,
        "variables": vs,
        "b3": names["b3"],
        "b4": names["b4"],
        "rows": rows,
        "names": names,
    }


def qsym(D: dict, j: int) -> sp.Symbol:
    name = f"q{j}_0"
    if name not in D["names"]:
        raise KeyError(name)
    return D["names"][name]
