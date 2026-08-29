#!/usr/bin/env python3
"""Bounded homogeneous modular endpoint-syzygy search with exact replay."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import time
from collections import defaultdict
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def poly_mod(item, prime):
    out = {}
    for monomial, coefficient in item["terms"]:
        if "/" in coefficient:
            numerator, denominator = map(int, coefficient.split("/"))
        else:
            numerator, denominator = int(coefficient), 1
        value = numerator % prime * pow(denominator % prime, -1, prime) % prime
        if value:
            out[tuple(monomial)] = value
    return out


def degree(poly):
    degrees = {len(monomial) for monomial in poly}
    assert len(degrees) == 1, degrees
    return next(iter(degrees))


def monomials(variables, degree_value):
    if degree_value == 0:
        yield ()
        return
    for indices in itertools.combinations_with_replacement(range(len(variables)), degree_value):
        yield tuple(variables[index] for index in indices)


def multiply_monomial(poly, monomial):
    return {tuple(sorted(term + monomial)): coefficient for term, coefficient in poly.items()}


def add_scaled(target, source, scalar, prime):
    for key, value in source.items():
        updated = (target.get(key, 0) + scalar * value) % prime
        if updated:
            target[key] = updated
        elif key in target:
            del target[key]


def solve(rows, right_hand_sides, column_count, prime):
    order = sorted(rows, key=lambda key: (len(rows[key]), key))
    pivots = {}
    pivot_order = []
    for row_name in order:
        row = dict(rows[row_name])
        rhs = right_hand_sides.get(row_name, 0)
        while row:
            column = min(row)
            coefficient = row[column]
            if column not in pivots:
                inverse = pow(coefficient, -1, prime)
                row = {key: value * inverse % prime for key, value in row.items()}
                rhs = rhs * inverse % prime
                pivots[column] = (row, rhs)
                pivot_order.append(column)
                break
            pivot_row, pivot_rhs = pivots[column]
            factor = coefficient
            for key, value in pivot_row.items():
                updated = (row.get(key, 0) - factor * value) % prime
                if updated:
                    row[key] = updated
                elif key in row:
                    del row[key]
            rhs = (rhs - factor * pivot_rhs) % prime
        if not row and rhs:
            return None, {"rank": len(pivots), "inconsistent_row": list(row_name)}
    solution = [0] * column_count
    for column in reversed(pivot_order):
        row, rhs = pivots[column]
        value = rhs
        for other, coefficient in row.items():
            if other != column and solution[other]:
                value = (value - coefficient * solution[other]) % prime
        solution[column] = value
    return solution, {"rank": len(pivots), "inconsistent_row": None}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dedup", type=Path, required=True)
    parser.add_argument("--dedup-sha256", required=True)
    parser.add_argument("--subset", choices=("g15", "g13_g15", "g14", "full"), required=True)
    parser.add_argument("--multiplier-vars", choices=("target", "active"), required=True)
    parser.add_argument("--total-degree", type=int, required=True)
    parser.add_argument("--saturation-power", type=int, default=0)
    parser.add_argument("--prime", type=int, choices=(65521, 65519, 65497), required=True)
    parser.add_argument("--max-columns", type=int, default=20000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert sha256(args.dedup) == args.dedup_sha256
    source = json.loads(args.dedup.read_text())
    assert source["schema"] == "GGV-8_28-ORIGIN-Q15-EXACT-RECEIVER-DEDUP-v1"
    generators = [item for item in source["subsets"][args.subset]
                  if item["constraint_id"] != "c2_open"]
    target = poly_mod(source["endpoint_value"], args.prime)
    if args.saturation_power:
        target = multiply_monomial(target, ("c2",) * args.saturation_power)
    assert degree(target) == args.total_degree
    target_support = sorted({name for monomial in target for name in monomial})
    active = sorted({name for item in generators + [source["endpoint_value"]]
                     for monomial, _ in item["terms"] for name in monomial
                     if name != "invc2"})
    variables = target_support if args.multiplier_vars == "target" else active
    columns = []
    column_polys = []
    for generator_index, item in enumerate(generators):
        poly = poly_mod(item, args.prime)
        multiplier_degree = args.total_degree - degree(poly)
        if multiplier_degree < 0:
            continue
        for monomial in monomials(variables, multiplier_degree):
            columns.append({
                "generator_index": generator_index,
                "constraint_id": item["constraint_id"],
                "multiplier_monomial": list(monomial),
            })
            column_polys.append(multiply_monomial(poly, monomial))
            if len(columns) > args.max_columns:
                raise RuntimeError(f"column cap exceeded: {len(columns)} > {args.max_columns}")
    rows = defaultdict(dict)
    for column, poly in enumerate(column_polys):
        for monomial, coefficient in poly.items():
            rows[monomial][column] = coefficient
    rhs = dict(target)
    all_rows = set(rows) | set(rhs)
    for monomial in all_rows:
        rows.setdefault(monomial, {})
    started = time.monotonic()
    solution, linear = solve(rows, rhs, len(columns), args.prime)
    elapsed = time.monotonic() - started
    result = {
        "schema": "GGV-8_28-ORIGIN-Q15-BOUNDED-MODULAR-SYZYGY-v1",
        "source_dedup_sha256": args.dedup_sha256,
        "subset": args.subset,
        "prime": args.prime,
        "total_degree": args.total_degree,
        "saturation_power": args.saturation_power,
        "multiplier_variable_profile": args.multiplier_vars,
        "multiplier_variables": variables,
        "generator_count": len(generators),
        "column_count": len(columns),
        "coefficient_row_count": len(all_rows),
        "rank": linear["rank"],
        "solve_seconds": elapsed,
        "scope": {
            "certificate_is_over_prime_field_only": True,
            "bounded_failure_is_not_ideal_nonmembership": True,
            "exact_Q_claimed": False,
        },
    }
    if solution is None:
        result["status"] = "NO_CERTIFICATE_IN_BOUNDED_ANSATZ"
        result["inconsistent_row"] = linear["inconsistent_row"]
    else:
        replay = {}
        certificate = []
        for column, coefficient in enumerate(solution):
            if not coefficient:
                continue
            add_scaled(replay, column_polys[column], coefficient, args.prime)
            certificate.append({**columns[column], "coefficient": coefficient})
        assert replay == target, (len(replay), len(target))
        result["status"] = "MODULAR_SYZYGY_FOUND_WITH_REPLAY"
        result["certificate"] = certificate
        result["certificate_term_count"] = len(certificate)
        result["replay_zero"] = True
        result["target_term_count"] = len(target)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"], "subset": args.subset, "prime": args.prime,
        "columns": len(columns), "rows": len(all_rows), "rank": linear["rank"],
        "certificate_terms": result.get("certificate_term_count"),
        "output_sha256": sha256(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
