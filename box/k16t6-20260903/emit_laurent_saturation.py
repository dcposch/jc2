#!/usr/bin/env python3
"""Emit nfmodStd / modular jobs for a terminal_laurent_t6.json record.

Ring map: A_6 = Q[q13_1]/(H_6) with remaining (b3,b4,q2_0,q3_0,q4_0,q5_0)
in that order; generators are primitive integer associates of the 12 band
rows.  W is the Rabinowitsch variable used only in wrapper controls.
"""

from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import k16t56_pipeline as P  # noqa: E402


def primitive(expr, variables):
    polynomial = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    _den, cleared = polynomial.clear_denoms(convert=True)
    _content, answer = cleared.primitive()
    if answer.LC() < 0:
        answer = -answer
    return answer.as_expr()


def main() -> None:
    source = HERE / "terminal_laurent_t6.json"
    record = json.loads(source.read_text(encoding="utf-8"))
    t = int(record["t"])
    y = sp.Symbol("q%d_1" % (2 * t + 1))
    H = sp.sympify(record["H"], locals={str(y): y})
    remaining = [sp.Symbol(name) for name in record["terminal_variables"]]
    local = {str(y): y, **{str(v): v for v in remaining}}
    generators = []
    meta = []
    for item in record["terminal"]:
        expr = sp.sympify(item["expr"], locals=local)
        prim = primitive(expr, [y] + remaining)
        sing = str(prim).replace("**", "^")
        generators.append(sing)
        poly = sp.Poly(prim, *remaining, domain=sp.QQ.frac_field(y))
        meta.append({
            "band": item["band"],
            "nterms": len(poly.terms()),
            "total_degree": int(poly.total_degree()),
            "LM": str(poly.LM()),
            "LC": str(sp.factor(poly.LC())),
        })
    cbar = record["normalizer"]["c"]
    (HERE / "t6_laurent_terminal_meta.json").write_text(
        json.dumps({"variables": list(map(str, remaining)), "rows": meta},
                   indent=2, sort_keys=True) + "\n")
    exact_nf = HERE / "t6_laurent_exact_At_nfmodStd.sing"
    exact_nf.write_text(P.emit_extension(
        t, H, y, remaining, generators, cbar, "nfmodStd").replace(
            "setcores(1);", "setcores(4);", 1))
    exact_qhy = HERE / "t6_laurent_exact_QHy_std.sing"
    exact_qhy.write_text(P.emit_qhy(
        t, H, y, remaining, generators, cbar, 0, "std"))
    for prime in P.DEFAULT_PRIMES:
        path = HERE / ("t6_laurent_mod_p%d_std.sing" % prime)
        path.write_text(P.emit_qhy(
            t, H, y, remaining, generators, cbar, prime, "std"))
        print(path.name, path.stat().st_size)
    print(exact_nf.name, exact_nf.stat().st_size)
    print(exact_qhy.name, exact_qhy.stat().st_size)


if __name__ == "__main__":
    main()
