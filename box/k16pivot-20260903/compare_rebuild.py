#!/usr/bin/env python3
"""Compare the t=2,3 Laurent rebuilds against the charged JSON records."""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

CHARGED = pathlib.Path("/tmp/jc2-lane.nw1i08/inputs")
HERE = pathlib.Path(__file__).resolve().parent
fails: list[str] = []


def check(name: str, cond) -> None:
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        fails.append(name)


def reduce_in_At(expr, y, H, gens):
    domain = sp.QQ[tuple(gens)] if gens else sp.QQ
    numerator, denominator = sp.cancel(sp.sympify(expr)).as_numer_denom()
    hpoly = sp.Poly(H, y, domain=domain)
    nrem = sp.Poly(sp.expand(numerator), y, domain=domain).rem(hpoly)
    drem = sp.Poly(sp.expand(denominator), y, domain=domain).rem(hpoly)
    if drem.degree() > 0:
        dinv = sp.invert(
            sp.Poly(drem.as_expr(), y, domain=sp.QQ),
            sp.Poly(H, y, domain=sp.QQ),
        ).as_expr()
        answer = nrem.as_expr() * dinv
    else:
        answer = nrem.as_expr() / drem.as_expr()
    return sp.expand(
        sp.Poly(sp.expand(answer), y, domain=domain).rem(hpoly).as_expr()
    )


for tval in (2, 3):
    c = json.loads((CHARGED / ("terminal_laurent_t%d.json" % tval)).read_text())
    o = json.loads((HERE / ("terminal_laurent_t%d.json" % tval)).read_text())
    y = sp.Symbol("q%d_1" % (2 * tval + 1))
    H = sp.sympify(c["H"])
    gens = [sp.symbols("b3"), sp.symbols("b4")]
    if tval >= 3:
        gens.append(sp.symbols("q2_0"))
    check("t=%d H" % tval, c["H"] == o["H"])
    check("t=%d d" % tval, c["d"] == o["d"])
    check("t=%d normalizer" % tval, c["normalizer"] == o["normalizer"])
    check("t=%d n high_pivots" % tval, len(c["high_pivots"]) == len(o["high_pivots"]))
    check("t=%d terminal_variables" % tval,
          c["terminal_variables"] == o["terminal_variables"])
    check("t=%d n terminal" % tval, len(c["terminal"]) == len(o["terminal"]))
    for i, (a, b) in enumerate(zip(c["high_pivots"], o["high_pivots"])):
        check("t=%d pivot[%d] var" % (tval, i), a["variable"] == b["variable"])
        check("t=%d pivot[%d] band" % (tval, i), a["band"] == b["band"])
        ca = reduce_in_At(a["coefficient"], y, H, [])
        cb = reduce_in_At(b["coefficient"], y, H, [])
        check("t=%d pivot[%d] %s coeff" % (tval, i, a["variable"]),
              sp.expand(ca - cb) == 0)
        check("t=%d pivot[%d] resultant" % (tval, i),
              a["resultant"] == b["resultant"])
    for i, (a, b) in enumerate(zip(c["terminal"], o["terminal"])):
        check("t=%d terminal[%d] band" % (tval, i), a["band"] == b["band"])
        ca = reduce_in_At(a["expr"], y, H, gens)
        cb = reduce_in_At(b["expr"], y, H, gens)
        check("t=%d terminal[%d] expr" % (tval, i), sp.expand(ca - cb) == 0)
    check("t=%d b1 coeff" % tval,
          sp.expand(
              reduce_in_At(c["b1_divisibility_pivot"]["coefficient"], y, H, [])
              - reduce_in_At(o["b1_divisibility_pivot"]["coefficient"], y, H, [])
          ) == 0)
    check("t=%d B0 coeff" % tval,
          sp.expand(
              reduce_in_At(c["B0_gauge_pivot"]["coefficient"], y, H, [])
              - reduce_in_At(o["B0_gauge_pivot"]["coefficient"], y, H, [])
          ) == 0)

print("REBUILD_COMPARE_DONE fails=%d" % len(fails))
if fails:
    print("FAILED:", fails)
    sys.exit(1)
print("REBUILD_COMPARE_PASS")
