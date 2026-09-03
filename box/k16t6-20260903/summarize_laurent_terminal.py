#!/usr/bin/env python3
"""Validate and losslessly tabulate the exact t=6 Laurent terminal record."""

from __future__ import annotations

import csv
import hashlib
import json
import pathlib

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "terminal_laurent_t6.json"
TSV = HERE / "t6_laurent_terminal.tsv"
SUMMARY = HERE / "t6_laurent_terminal_summary.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def monomial_text(variables: list[sp.Symbol], powers: tuple[int, ...]) -> str:
    pieces = []
    for variable, power in zip(variables, powers):
        if power == 1:
            pieces.append(str(variable))
        elif power:
            pieces.append(f"{variable}^{power}")
    return "*".join(pieces) if pieces else "1"


def primitive_section(expr: sp.Expr, y: sp.Symbol,
                      variables: list[sp.Symbol]) -> sp.Expr:
    poly_q = sp.Poly(sp.expand(expr), y, *variables, domain=sp.QQ)
    _denominator, cleared = poly_q.clear_denoms(convert=True)
    _content, primitive = cleared.primitive()
    result = sp.expand(primitive.as_expr())
    section = sp.Poly(result, *variables, domain=sp.QQ.poly_ring(y))
    lc_y = sp.Poly(section.LC(), y, domain=sp.QQ)
    if lc_y.LC() < 0:
        result = -result
    return sp.expand(result)


def main() -> None:
    source_bytes = SOURCE.read_bytes()
    record = json.loads(source_bytes)
    if record.get("t") != 6:
        raise AssertionError("not a t=6 record")
    if sp.expand(sp.sympify(record["H"])-(2028*sp.Symbol("q13_1")**2
                                           -1092*sp.Symbol("q13_1")+140)) != 0:
        raise AssertionError("H mismatch")
    expected_names = ["b3", "b4", "q2_0", "q3_0", "q4_0", "q5_0"]
    if record.get("terminal_variables") != expected_names:
        raise AssertionError("terminal variable order mismatch")
    if [item["band"] for item in record["terminal"]] != list(range(12)):
        raise AssertionError("terminal band order mismatch")

    y = sp.Symbol("q13_1")
    variables = list(sp.symbols("b3 b4 q2_0 q3_0 q4_0 q5_0"))
    allowed = {y, *variables}
    output_rows = []
    compact_rows = []
    for item in record["terminal"]:
        band = int(item["band"])
        expr = sp.expand(sp.sympify(item["expr"]))
        if expr.free_symbols - allowed:
            raise AssertionError(f"band {band}: unexpected variables")
        ypoly = sp.Poly(expr, y, domain=sp.QQ.frac_field(*variables))
        if ypoly.degree() > 1:
            raise AssertionError(f"band {band}: not reduced modulo H")
        primitive = primitive_section(expr, y, variables)
        section = sp.Poly(primitive, *variables,
                          domain=sp.QQ.poly_ring(y))
        degree = int(section.total_degree())
        expected_degree = 25-band
        if degree != expected_degree:
            raise AssertionError(
                f"band {band}: degree {degree}, expected {expected_degree}")
        monomial = section.monoms()[0]
        lc = sp.expand(section.LC())
        text = str(primitive)
        digest = sha256_bytes((text+"\n").encode())
        row = {
            "band": band,
            "degree": degree,
            "nterms": len(section.terms()),
            "leading_monomial": monomial_text(variables, monomial),
            "leading_coefficient": str(lc),
            "sha256": digest,
            "primitive_A6_section": text,
        }
        output_rows.append(row)
        compact_rows.append({key: value for key, value in row.items()
                             if key != "primitive_A6_section"})

    with TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0]),
                                delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)
    summary = {
        "typing": "primitive integral degree-<2 sections in A_6",
        "source": SOURCE.name,
        "source_sha256": sha256_bytes(source_bytes),
        "t": 6,
        "H_primitive": "507*q13_1^2-273*q13_1+35",
        "coefficient_algebra": "A_6=Q[q13_1]/(H_6)",
        "generator_order": expected_names,
        "terminal_rows": compact_rows,
        "pattern": {
            "rows": 12,
            "variables": 6,
            "bands": list(range(12)),
            "degrees": list(range(25, 13, -1)),
        },
    }
    SUMMARY.write_text(json.dumps(summary, indent=2, sort_keys=True)+"\n")
    print("LAURENT_TERMINAL_SUMMARY_PASS rows=12 vars=6 "
          "bands=0..11 degrees=25..14")
    print(f"source_sha256={summary['source_sha256']}")
    print(f"tsv_sha256={sha256_bytes(TSV.read_bytes())}")
    print(f"summary_sha256={sha256_bytes(SUMMARY.read_bytes())}")


if __name__ == "__main__":
    main()
