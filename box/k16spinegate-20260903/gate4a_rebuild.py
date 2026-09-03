#!/usr/bin/env python3
"""GATE 4a: independently re-run the Laurent/Euler model at t=2,3,4 and
compare every terminal row and every high pivot with the charged records."""
from __future__ import annotations
import json, pathlib, sys
import sympy as sp

sys.path.insert(0, "/tmp/jc2-lane.nglVmb/inputs")
import terminal_laurent_model as M

BOX = pathlib.Path("/home/ubuntu/jc2/box/k16spine-20260903")
OUT = pathlib.Path("/home/ubuntu/jc2/box/k16spinegate-20260903")
summary = {}
for t in (2, 3, 4):
    rec = M.build(t)
    (OUT / ("regen_terminal_laurent_t%d.json" % t)).write_text(
        json.dumps(rec, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ref_path = BOX / ("terminal_laurent_t%d.json" % t)
    entry = {"t": t, "rows": len(rec["terminal"]),
             "variables": rec["terminal_variables"],
             "pivots": len(rec["high_pivots"]) + 2,
             "seconds": rec["elapsed_seconds"]}
    if ref_path.exists():
        ref = json.loads(ref_path.read_text())
        yv = sp.Symbol("q%d_1" % (2 * t + 1))
        H = sp.Poly(sp.sympify(rec["H"]), yv, domain=sp.QQ)

        def red(expr_str):
            ex = sp.sympify(expr_str)
            pol = sp.Poly(sp.expand(ex), yv)
            return sp.expand(sp.Poly(pol.rem(sp.Poly(H.as_expr(), yv,
                                                     domain=pol.domain))).as_expr())
        same_terminal = all(
            sp.expand(sp.sympify(a["expr"]) - sp.sympify(b["expr"])) == 0
            and a["band"] == b["band"]
            for a, b in zip(rec["terminal"], ref["terminal"]))
        same_piv = all(
            sp.expand(sp.sympify(a["coefficient"]) - sp.sympify(b["coefficient"])) == 0
            and a["variable"] == b["variable"] and a["band"] == b["band"]
            for a, b in zip(rec["high_pivots"], ref["high_pivots"]))
        entry["matches_charged_terminal"] = bool(
            same_terminal and len(rec["terminal"]) == len(ref["terminal"]))
        entry["matches_charged_pivots"] = bool(
            same_piv and len(rec["high_pivots"]) == len(ref["high_pivots"]))
        entry["matches_normalizer"] = (rec["normalizer"] == ref["normalizer"])
        entry["matches_H"] = (rec["H"] == ref["H"])
    summary[t] = entry
    print(json.dumps(entry, sort_keys=True), flush=True)
(OUT / "gate4a_summary.json").write_text(
    json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("GATE4A_DONE")
