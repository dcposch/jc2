#!/usr/bin/env python3
"""Emit exact/modular terminal jobs in scale-invariant coordinates.

For N=4t+1 put z=b3/b4^(t+1) and r_i=q_i0/b4^i.  Homogeneity implies that
terminal band k>0 is b4^(N-k) F_k(z,r_2,...), so on b4 != 0 it is equivalent
to F_k=0.  This driver verifies the factorization monomial by monomial rather
than assuming it, then emits the high subsystem F_1,...,F_(2t-1).
"""

from __future__ import annotations

import argparse
import json
import pathlib

import sympy as sp


HERE = pathlib.Path("/home/ubuntu/jc2/box/k16spine-20260903")


def singular(expr):
    return str(expr).replace("**", "^")


def primitive(expr, variables):
    poly = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    _denom, cleared = poly.clear_denoms(convert=True)
    _content, answer = cleared.primitive()
    if answer.LC() < 0:
        answer = -answer
    return answer.as_expr()


def reduce_y(expr, H, y, variables):
    domain = sp.QQ[tuple(variables)]
    return sp.expand(
        sp.Poly(sp.expand(expr), y, domain=domain)
        .rem(sp.Poly(H, y, domain=domain)).as_expr()
    )


def invariant_rows(record):
    t = int(record["t"])
    N = 4*t + 1
    if isinstance(record["terminal"], dict):
        terminal_names = record["terminal"]["variables"]
        terminal_items = record["terminal"]["rows"]
    else:
        terminal_names = record["terminal_variables"]
        terminal_items = record["terminal"]
    if terminal_names != ["b3", "b4"] + ["q%d_0" % i for i in range(2, t)]:
        raise RuntimeError("record is not in canonical residual coordinates")
    b3, b4 = sp.symbols("b3 b4")
    y = sp.Symbol("q%d_1" % (2*t + 1))
    z = sp.Symbol("z")
    rs = [sp.Symbol("r%d" % i) for i in range(2, t)]
    qs = [sp.Symbol("q%d_0" % i) for i in range(2, t)]
    local = {"b3": b3, "b4": b4, str(y): y}
    local.update({str(q): q for q in qs})
    H = sp.sympify(record["H"], locals=local)
    rows = []
    for item in terminal_items:
        band = int(item["band"])
        expr = sp.sympify(item.get("expression", item.get("expr")), locals=local)
        transformed = sp.expand(expr.subs(
            {b3: z*b4**(t+1), **{q: r*b4**i for i, (q, r)
                                  in enumerate(zip(qs, rs), start=2)}}
        ))
        polynomial = sp.Poly(transformed, b4, z, *rs, y, domain=sp.QQ)
        b4_powers = {monomial[0] for monomial, _coefficient in polynomial.terms()}
        if band == 0:
            if not b4_powers <= {0, N}:
                raise AssertionError((band, b4_powers))
            continue
        if b4_powers != {N-band}:
            raise AssertionError((band, b4_powers, N-band))
        F = sp.expand(transformed / b4**(N-band))
        F = reduce_y(F, H, y, [z] + rs)
        rows.append((band, primitive(F, [z] + rs + [y])))
    if [band for band, _expr in rows] != list(range(1, 2*t)):
        raise AssertionError("high-band list differs")
    return t, y, H, z, rs, rows


def emit_exact(t, y, H, z, rs, rows, first_band=1):
    selected = [expr for band, expr in rows if band >= first_band]
    variables = [z] + rs
    lines = [
        "// exact canonical terminal high subsystem",
        "// t=%d, selected bands %d..%d" % (t, first_band, 2*t-1),
        "ring R=(0,%s),(%s),dp;" % (y, ",".join(map(str, variables))),
        "minpoly=%s;" % singular(H),
        "option(redSB);",
        'print("MAIN_START t=%d rows=%d vars=%d first_band=%d");'
        % (t, len(selected), len(variables), first_band),
        "ideal I=%s;" % ",\n".join(singular(expr) for expr in selected),
        "ideal G=std(I);",
        'print("MAIN_DONE size=");',
        "size(G);",
        'if (reduce(1,G)==0) { print("UNIT"); G; }'
        ' else { print("NONUNIT"); G; }',
        "quit;",
    ]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int)
    parser.add_argument("--first-band", type=int, default=1)
    parser.add_argument("--source", choices=("canonical", "lean"), default="canonical")
    args = parser.parse_args()
    if args.source == "canonical":
        paths = sorted(HERE.glob("terminal_t%d_canonical_*_exact.json" % args.t))
        if len(paths) != 1:
            raise RuntimeError("expected one canonical record, found %d" % len(paths))
        path = paths[0]
    else:
        path = HERE/("terminal_laurent_t%d.json" % args.t)
    record = json.loads(path.read_text(encoding="utf-8"))
    t, y, H, z, rs, rows = invariant_rows(record)
    text = emit_exact(t, y, H, z, rs, rows, args.first_band)
    suffix = "_lean" if args.source == "lean" else ""
    out = HERE / ("terminal_t%d_high_from%d%s_exact.sing"
                  % (t, args.first_band, suffix))
    out.write_text(text, encoding="utf-8")
    print(out)
    print("rows", len([1 for band, _ in rows if band >= args.first_band]))


if __name__ == "__main__":
    main()
