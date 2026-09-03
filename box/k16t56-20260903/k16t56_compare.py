#!/usr/bin/env python3
"""Side-by-side comparison of canonical (and heuristic) terminal systems t=2..6."""

from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent


def load(t: int, order: str):
    path = HERE / ("t%d_%s_audit.json" % (t, order))
    if not path.is_file():
        return None
    return json.loads(path.read_text())


def leading_data(audit):
    y = sp.Symbol(audit["grading"]["y"])
    remaining = [sp.Symbol(n) for n in audit["terminal"]["variables"]]
    out = []
    for rec in audit["terminal"]["rows"]:
        expr = sp.sympify(rec["primitive"])
        if remaining:
            poly = sp.Poly(expr, *remaining, domain=sp.QQ.frac_field(y))
            lm = poly.LM()
            lc = poly.LC()
        else:
            lm, lc = 1, expr
        out.append({
            "band": rec["h_power"],
            "tag": rec["monomial"],
            "degree": rec["total_degree"],
            "nterms": rec["nterms"],
            "LM": str(lm),
            "LC": str(sp.together(lc)),
            "support": rec["support"],
        })
    return out


def main() -> None:
    rows = []
    for order in ("canonical", "heuristic"):
        print("=" * 72)
        print("ORDER", order)
        print("%3s %8s %8s %22s %20s %s" % (
            "t", "A-piv", "term", "variables", "deg multiset", "bands"))
        for t in range(2, 7):
            a = load(t, order)
            if a is None:
                print("%3d  -- missing --" % t)
                continue
            degs = [r["total_degree"] for r in a["terminal"]["rows"]]
            bands = [r["h_power"] for r in a["terminal"]["rows"]]
            print("%3d %8d %4d x %-2d %-22s %-20s %s" % (
                t, a["a_pivots"]["count"],
                len(a["terminal"]["rows"]), len(a["terminal"]["variables"]),
                ",".join(a["terminal"]["variables"]),
                str(sorted(degs, reverse=True)),
                bands,
            ))
            lead = leading_data(a)
            for item in lead:
                print("     band=%s tag=%s deg=%s LM=%s LC=%s" % (
                    item["band"], item["tag"], item["degree"],
                    item["LM"], item["LC"][:80]))
            q = 2 * t + 1
            print("  Q-coeffs", a["q_pivots"]["coefficients"])
            print("  expected first-t q=%d then (2q,q)* then endpoint -4q,-3q/4" % q)
            print("  H", a["normalizer"]["H_primitive"],
                  "irr", a["normalizer"]["irreducible_over_Q"])
            print("  A-resultants", [p["resultant"] for p in a["a_pivots"]["pivots"]])
            rows.append({"t": t, "order": order, "audit": a, "lead": lead})
    out = HERE / "comparison.json"
    # JSON-safe subset
    slim = []
    for item in rows:
        a = item["audit"]
        slim.append({
            "t": item["t"], "order": item["order"],
            "variables": a["terminal"]["variables"],
            "degrees": [r["total_degree"] for r in a["terminal"]["rows"]],
            "bands": [r["h_power"] for r in a["terminal"]["rows"]],
            "tags": [r["monomial"] for r in a["terminal"]["rows"]],
            "lead": item["lead"],
            "q_coefficients": a["q_pivots"]["coefficients"],
            "a_resultants": [p["resultant"] for p in a["a_pivots"]["pivots"]],
            "a_variables": [p["variable"] for p in a["a_pivots"]["pivots"]],
            "H_primitive": a["normalizer"]["H_primitive"],
            "irreducible": a["normalizer"]["irreducible_over_Q"],
        })
    out.write_text(json.dumps(slim, indent=2, sort_keys=True) + "\n")
    print("WROTE", out)


if __name__ == "__main__":
    main()
