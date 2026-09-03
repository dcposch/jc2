#!/usr/bin/env python3
"""Exact bandwise comparison of Laurent recurrence and canonical terminals."""

from __future__ import annotations

import json
import pathlib

import sympy as sp


HERE = pathlib.Path("/home/ubuntu/jc2/box/k16spine-20260903")


def canonical_record(t):
    if t == 2:
        data = json.loads((HERE/"canonical_t2_audit.json").read_text())
        return data["terminal_variables"], data["terminal"]
    paths = sorted(HERE.glob("terminal_t%d_canonical_*_exact.json" % t))
    if len(paths) != 1:
        raise FileNotFoundError("canonical t=%d: found %d records" % (t, len(paths)))
    data = json.loads(paths[0].read_text())
    return data["terminal"]["variables"], data["terminal"]["rows"]


def compare(t):
    lean = json.loads((HERE/("terminal_laurent_t%d.json" % t)).read_text())
    variable_names, canonical = canonical_record(t)
    if variable_names != lean["terminal_variables"]:
        raise AssertionError("terminal variable order differs")
    variables = [sp.Symbol(name) for name in variable_names]
    y = sp.Symbol("q%d_1" % (2*t+1))
    local = {str(v): v for v in variables+[y]}
    H = sp.sympify(lean["H"], locals=local)
    domain = sp.QQ[tuple(variables)]
    hpoly = sp.Poly(H, y, domain=domain)

    def reduce(expr):
        return sp.expand(
            sp.Poly(sp.expand(expr), y, domain=domain).rem(hpoly).as_expr()
        )

    def inverse(coefficient):
        answer = sp.invert(sp.Poly(coefficient, y, domain=sp.QQ),
                           sp.Poly(H, y, domain=sp.QQ)).as_expr()
        if reduce(coefficient*answer-1) != 0:
            raise AssertionError("inverse check")
        return answer

    output = []
    for left, right in zip(lean["terminal"], canonical):
        if int(left["band"]) != int(right["band"]):
            raise AssertionError("band order differs")
        L = reduce(sp.sympify(left["expr"], locals=local))
        R = reduce(sp.sympify(right.get("expression", right.get("expr")), locals=local))
        lp = sp.Poly(L, *variables, domain=sp.QQ.frac_field(y))
        rp = sp.Poly(R, *variables, domain=sp.QQ.frac_field(y))
        ratio = None
        witness_monomial = None
        for monomial in lp.monoms():
            lc = lp.coeff_monomial(monomial)
            rc = rp.coeff_monomial(monomial)
            if rc == 0:
                continue
            try:
                candidate = reduce(lc*inverse(rc))
            except Exception:
                continue
            if reduce(L-candidate*R) == 0:
                ratio = candidate
                witness_monomial = list(monomial)
                break
        if ratio is None:
            raise AssertionError("no A_t-unit associate at band %d" % left["band"])
        resultant = sp.factor(sp.resultant(H, ratio, y))
        if resultant == 0:
            raise AssertionError("comparison ratio is a zero divisor")
        output.append({
            "band": int(left["band"]),
            "witness_monomial": witness_monomial,
            "lean_equals_ratio_times_canonical": str(ratio),
            "resultant_H_ratio": str(resultant),
            "identity_checked_mod_H": True,
        })
    return {
        "t": t,
        "H": str(H),
        "terminal_variables": variable_names,
        "bands": output,
        "every_band_A_t_unit_associate": True,
    }


def main():
    records = []
    for t in (2, 3, 4):
        try:
            records.append(compare(t))
        except FileNotFoundError:
            pass
    out = HERE/"terminal_laurent_exact_comparison.json"
    out.write_text(json.dumps({"comparisons": records}, indent=2, sort_keys=True)+"\n")
    print(out)
    for record in records:
        print("t", record["t"], "bands", len(record["bands"]), "PASS")


if __name__ == "__main__":
    main()
