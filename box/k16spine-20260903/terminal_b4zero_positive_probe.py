#!/usr/bin/env python3
"""Emit exact probes for the positive-band terminal ideal on b4=0.

This is a discovery aid.  It asks whether bands 1,...,2t-1 already cut out
the residual origin; if so, band zero reduces to the uniform g5 obstruction.
"""

from __future__ import annotations

import argparse
import json
import pathlib

import sympy as sp


def render(expr):
    return str(expr).replace("**", "^")


def primitive(expr, variables):
    poly = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    _den, cleared = poly.clear_denoms(convert=True)
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
        y = sp.Symbol(f"q{2*t+1}_1")
        H = sp.sympify(record["H"], locals={str(y): y})
        if not sp.Poly(H, y, domain=sp.QQ).is_irreducible:
            raise RuntimeError(f"split t={t} is not supported by this emitter")
        b3, b4 = sp.symbols("b3 b4")
        qs = [sp.Symbol(f"q{i}_0") for i in range(2, t)]
        variables = [b3] + qs
        local = {str(v): v for v in [y, b3, b4] + qs}
        rows = [
            sp.sympify(item["expr"], locals=local).subs(b4, 0)
            for item in record["terminal"] if int(item["band"]) > 0
        ]
        rows = [primitive(row, [y] + variables) for row in rows if row != 0]
        lines = [
            "// exact positive-band b4=0 discovery probe",
            f"ring R=(0,{y}),({','.join(map(str, variables))}),dp;",
            f"minpoly={render(H)};",
            "option(redSB);",
            f'print("MAIN t={t} b4=0 positive rows={len(rows)}");',
            "ideal I=" + ",\n".join(render(row) for row in rows) + ";",
            "ideal G=std(I);",
            'print("BASIS_SIZE"); size(G);',
            'print("BASIS"); G;',
            'print("VARIABLE_REMAINDERS");',
        ]
        for variable in variables:
            lines.append(f'print("{variable}"); reduce({variable},G);')
        lines.append("quit;")
        output = source.with_name(source.stem + "_b4_0_positive.sing")
        output.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(output)


if __name__ == "__main__":
    main()
