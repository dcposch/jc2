#!/usr/bin/env python3
"""Emit both weighted charts from a modular Laurent terminal record.

This consumes, but does not recompute, terminal_mod_t*_p*_branch*.json.
The results are discovery controls only: a modular unit is not promoted to a
characteristic-zero certificate.
"""

from __future__ import annotations

import argparse
import json
import pathlib

import sympy as sp


def singular(expr):
    return str(expr).replace("**", "^")


def emit(record, chart):
    t = int(record["t"])
    prime = int(record["prime"])
    b3, b4 = sp.symbols("b3 b4")
    qs = [sp.Symbol("q%d_0" % i) for i in range(2, t)]
    variables = [b3] + qs
    local = {str(v): v for v in [b3, b4] + qs}
    rows = [sp.sympify(item["expr"], locals=local) for item in record["terminal"]]
    if chart == "b4one":
        rows = [sp.expand(row.subs(b4, 1)) for row in rows]
    elif chart == "b4zero":
        rows = [sp.expand(row.subs(b4, 0)) for row in rows]
    else:
        raise ValueError(chart)
    # Keep nonzero rows only.  The original band number remains in the JSON.
    rows = [row for row in rows if not sp.Poly(row, *variables, modulus=prime).is_zero]
    return "\n".join([
        "// modular terminal discovery; no characteristic-zero promotion",
        "ring R=%d,(%s),dp;" % (prime, ",".join(map(str, variables))),
        "option(redSB);",
        'print("MAIN t=%d y=%s chart=%s rows=%d vars=%d");'
        % (t, record["y"], chart, len(rows), len(variables)),
        "ideal I=%s;" % ",\n".join(singular(row) for row in rows),
        "ideal G=std(I);",
        'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
        "size(G);",
        "quit;",
    ]) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("records", nargs="+")
    args = parser.parse_args()
    for name in args.records:
        path = pathlib.Path(name)
        record = json.loads(path.read_text(encoding="utf-8"))
        for chart in ("b4one", "b4zero"):
            output = path.with_name(path.stem + "_" + chart + ".sing")
            output.write_text(emit(record, chart), encoding="utf-8")
            print(output)


if __name__ == "__main__":
    main()
