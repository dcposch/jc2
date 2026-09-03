#!/usr/bin/env python3
"""Emit modular b4=0 probes using terminal bands 1,...,2t-1 only."""

from __future__ import annotations

import argparse
import json
import pathlib

import sympy as sp


def render(expr):
    return str(expr).replace("**", "^")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("records", nargs="+")
    args = parser.parse_args()
    for name in args.records:
        source = pathlib.Path(name)
        record = json.loads(source.read_text(encoding="utf-8"))
        t, prime = int(record["t"]), int(record["prime"])
        b3, b4 = sp.symbols("b3 b4")
        qs = [sp.Symbol(f"q{i}_0") for i in range(2, t)]
        variables = [b3] + qs
        local = {str(v): v for v in [b3, b4] + qs}
        rows = [
            sp.expand(sp.sympify(item["expr"], locals=local).subs(b4, 0))
            for item in record["terminal"] if int(item["band"]) > 0
        ]
        rows = [row for row in rows
                if not sp.Poly(row, *variables, modulus=prime).is_zero]
        lines = [
            "// modular positive-band b4=0 discovery probe",
            f"ring R={prime},({','.join(map(str, variables))}),dp;",
            "option(redSB);",
            f'print("MAIN t={t} y={record["y"]} rows={len(rows)}");',
            "ideal I=" + ",\n".join(render(row) for row in rows) + ";",
            "ideal G=std(I);",
            'print("BASIS_SIZE"); size(G);',
            'print("LEAD_IDEAL"); lead(G);',
            "quit;",
        ]
        output = source.with_name(source.stem + "_b4_0_positive.sing")
        output.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(output)


if __name__ == "__main__":
    main()
