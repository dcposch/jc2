#!/usr/bin/env python3
"""Emit exact b4=1 and b4=0 terminal tests from Laurent JSON records.

Use only when H_t is irreducible over Q.  Split t must instead be evaluated
in both factors of the product algebra.
"""

from __future__ import annotations

import argparse
import json
import pathlib

import sympy as sp


def render(expr):
    return str(expr).replace("**", "^")


def primitive(expr, variables):
    polynomial = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    _denominator, cleared = polynomial.clear_denoms(convert=True)
    _content, answer = cleared.primitive()
    if answer.LC() < 0:
        answer = -answer
    return answer.as_expr()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("records", nargs="+")
    args = parser.parse_args()
    for name in args.records:
        source = pathlib.Path(name)
        record = json.loads(source.read_text(encoding="utf-8"))
        t = int(record["t"])
        y = sp.Symbol("q%d_1" % (2*t+1))
        H = sp.sympify(record["H"], locals={str(y): y})
        if not sp.Poly(H, y, domain=sp.QQ).is_irreducible:
            raise RuntimeError("split H_t needs product-factor jobs: t=%d" % t)
        b3, b4 = sp.symbols("b3 b4")
        qs = [sp.Symbol("q%d_0" % i) for i in range(2, t)]
        variables = [b3] + qs
        local = {str(v): v for v in [y, b3, b4] + qs}
        rows = [sp.sympify(item["expr"], locals=local)
                for item in record["terminal"]]
        for value in (1, 0):
            specialized = [primitive(row.subs(b4, value), [y] + variables)
                           for row in rows]
            specialized = [row for row in specialized if row != 0]
            lines = [
                "// exact Laurent terminal chart",
                "// source=%s t=%d b4=%d" % (source.name, t, value),
                "ring R=(0,%s),(%s),dp;" % (y, ",".join(map(str, variables))),
                "minpoly=%s;" % render(H),
                "option(redSB);",
                'print("MAIN t=%d b4=%d rows=%d vars=%d");'
                % (t, value, len(specialized), len(variables)),
                "ideal I=%s;" % ",\n".join(render(row) for row in specialized),
                "ideal G=std(I);",
                'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
                'print("BASIS_SIZE");',
                "size(G);",
                "quit;",
            ]
            output = source.with_name(source.stem+"_b4_%d_exact.sing" % value)
            output.write_text("\n".join(lines)+"\n", encoding="utf-8")
            print(output)


if __name__ == "__main__":
    main()
