#!/usr/bin/env python3
"""Expose the literal raw ideal's constant same-row pivots without substitution."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def load_compiler():
    path = HERE / "compile_endpoint.py"
    spec = importlib.util.spec_from_file_location("ggv_endpoint_compiler_rref", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ce = load_compiler()
MV = ce.MV


def decode(encoded):
    return MV({tuple(mon): Q(coefficient) for mon, coefficient in encoded})


def rref_with_transform(matrix, residuals):
    row_count = len(matrix)
    column_count = len(matrix[0]) if matrix else 0
    a = [row[:] for row in matrix]
    b = list(residuals)
    transform = [[Q(int(i == j)) for j in range(row_count)] for i in range(row_count)]
    pivot_row = 0
    pivots = []
    for column in range(column_count):
        chosen = next((row for row in range(pivot_row, row_count) if a[row][column]), None)
        if chosen is None:
            continue
        a[pivot_row], a[chosen] = a[chosen], a[pivot_row]
        b[pivot_row], b[chosen] = b[chosen], b[pivot_row]
        transform[pivot_row], transform[chosen] = transform[chosen], transform[pivot_row]
        scalar = a[pivot_row][column]
        a[pivot_row] = [value / scalar for value in a[pivot_row]]
        b[pivot_row] = b[pivot_row].scale(1 / scalar)
        transform[pivot_row] = [value / scalar for value in transform[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not a[row][column]:
                continue
            scalar = a[row][column]
            a[row] = [left - scalar * right for left, right in zip(a[row], a[pivot_row])]
            b[row] = b[row] - b[pivot_row].scale(scalar)
            transform[row] = [left - scalar * right
                              for left, right in zip(transform[row], transform[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return a, b, transform, pivots


def compile_rref():
    raw_path = HERE / "RAW_DIRECT_SYSTEM.json"
    assert ce.sha256(raw_path) == RAW_SHA256
    raw = json.loads(raw_path.read_text())
    source = json.loads(ce.RAW_INPUT.read_text())
    windows = ce.raw_windows(source)
    grouped = {row: [] for row in range(4, 23)}
    for raw_index, record in enumerate(raw["generators"]):
        grouped[int(record["row"])].append({
            "raw_index": raw_index,
            "x_degree": int(record["x_degree"]),
            "poly": decode(record["terms"]),
        })
    for row in grouped:
        grouped[row].sort(key=lambda record: record["x_degree"])

    transformed = []
    pivot_names = set()
    stats = {}
    for n in range(4, 22):
        current = [windows["G"][n][degree]
                   for degree in sorted(windows["G"][n], reverse=True)]
        if n <= 14:
            current.extend(windows["F"][n][degree]
                           for degree in sorted(windows["F"][n], reverse=True))
        records = grouped[n]
        matrix = []
        residuals = []
        for record in records:
            poly = record["poly"]
            row = [poly.terms.get((name,), Q(0)) for name in current]
            linear = MV.zero()
            for name, coefficient in zip(current, row):
                linear = linear + MV.var(name).scale(coefficient)
            residual = poly - linear
            assert all(not any(name in current for name in mon) for mon in residual.terms)
            matrix.append(row)
            residuals.append(residual)

        reduced, rhs, transform, pivots = rref_with_transform(matrix, residuals)
        pivot_names.update(current[column] for column in pivots)
        retained = 0
        for output_row in range(len(records)):
            poly = rhs[output_row]
            for name, coefficient in zip(current, reduced[output_row]):
                if coefficient:
                    poly = poly + MV.var(name).scale(coefficient)
            combination = [[records[index]["raw_index"], str(coefficient)]
                           for index, coefficient in enumerate(transform[output_row]) if coefficient]
            replay = MV.zero()
            for raw_index, coefficient in combination:
                replay = replay + decode(raw["generators"][raw_index]["terms"]).scale(Q(coefficient))
            assert replay == poly
            if not poly.terms:
                continue
            encoded = poly.encode()
            transformed.append({
                "source_row": n,
                "rref_row": output_row,
                "kind": "pivot" if output_row < len(pivots) else "compatibility",
                "terms": encoded,
                "raw_combination": combination,
                "sha256": hashlib.sha256(ce.compact(encoded)).hexdigest(),
            })
            retained += 1
        stats[str(n)] = {
            "raw_generators": len(records),
            "current_variables": len(current),
            "rank": len(pivots),
            "retained_generators": retained,
            "zero_dependencies_removed": len(records) - retained,
        }

    for record in grouped[22]:
        encoded = record["poly"].encode()
        transformed.append({
            "source_row": 22,
            "rref_row": record["x_degree"],
            "kind": "endpoint",
            "terms": encoded,
            "raw_combination": [[record["raw_index"], "1"]],
            "sha256": hashlib.sha256(ce.compact(encoded)).hexdigest(),
        })

    pivot_variables = [name for name in raw["variables"] if name in pivot_names]
    free_variables = [name for name in raw["variables"] if name not in pivot_names]
    assert len(pivot_variables) == 202
    assert len(free_variables) == 101
    assert set(pivot_variables).isdisjoint(free_variables)
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-BRANCH-P-ROW-RREF-v1",
        "authoritative_raw_system_sha256": RAW_SHA256,
        "method": "invertible constant-Q row operations only; no pivot substitution",
        "variables": pivot_variables + free_variables,
        "variable_count": len(raw["variables"]),
        "pivot_variables": pivot_variables,
        "pivot_count": len(pivot_variables),
        "free_variables": free_variables,
        "free_variable_count": len(free_variables),
        "generators": transformed,
        "generator_count": len(transformed),
        "row_stats": stats,
        "D23_imposed": False,
        "G22_present": False,
    }


def singular_text(result, modulus=0, algorithm="std"):
    assert algorithm in ("std", "slimgb")
    variables = result["variables"]
    expressions = [decode(record["terms"]).expression(modulus)
                   for record in result["generators"]]
    p = result["pivot_count"]
    f = result["free_variable_count"]
    lines = [
        "// Exact row-RREF image of the pinned literal raw generators.",
        f"ring endpoint_rref={modulus},({','.join(variables)}),(lp({p}),dp({f}));",
        "option(redSB);",
        "ideal I=",
        ",\n".join(expressions) + ";",
        'print("ROW_RREF variables="+string(nvars(basering))+" generators="+string(size(I)));',
        "int start_time=timer;",
        'print("START_STD");',
        f"ideal J={algorithm}(I);",
        "int elapsed=timer-start_time;",
        'print("END_STD seconds="+string(elapsed));',
        'print("BASIS_SIZE="+string(size(J)));',
        'int is_unit=(size(J)==1 && J[1]==1);',
        'print("UNIT="+string(is_unit));',
        'if(!is_unit){print("DIM="+string(dim(J)));}',
        "J;",
        "quit;",
        "",
    ]
    return "\n".join(lines)


def tracked_raw_certificate_text(result, raw):
    variables = result["variables"]
    raw_expressions = [decode(record["terms"]).expression() for record in raw["generators"]]
    transformed_expressions = [decode(record["terms"]).expression()
                               for record in result["generators"]]
    raw_count = len(raw_expressions)
    transformed_count = len(transformed_expressions)
    p = result["pivot_count"]
    f = result["free_variable_count"]
    lines = [
        "// Tracked exact-Q certificate composed back to all authoritative raw generators.",
        f"ring endpoint_rref_tracked=0,({','.join(variables)}),(lp({p}),dp({f}));",
        "option(redSB);",
        "ideal Rraw=",
        ",\n".join(raw_expressions) + ";",
        "ideal I=",
        ",\n".join(transformed_expressions) + ";",
        f"matrix M[{raw_count}][{transformed_count}];",
    ]
    for transformed_index, record in enumerate(result["generators"], start=1):
        for raw_index, coefficient in record["raw_combination"]:
            lines.append(f"M[{raw_index + 1},{transformed_index}]={coefficient};")
    lines.extend([
        "matrix transformed_replay=matrix(Rraw)*M-matrix(I);",
        'print("TRANSFORM_REPLAY_ZERO="+string(size(module(transformed_replay))==0));',
        'print("START_LIFTSTD");',
        "int start_time=timer;",
        "matrix T; ideal J=liftstd(I,T);",
        "int elapsed=timer-start_time;",
        "matrix basis_replay=matrix(I)*T-matrix(J);",
        'print("BASIS_REPLAY_ZERO="+string(size(module(basis_replay))==0));',
        'print("END_LIFTSTD seconds="+string(elapsed));',
        'print("BASIS_SIZE="+string(size(J)));',
        'int is_unit=(size(J)==1 && J[1]==1);',
        'print("UNIT="+string(is_unit));',
        "if(is_unit){",
        "  matrix Hunit=lift(J,ideal(1));",
        "  matrix Ctrans=T*Hunit;",
        "  matrix Craw=M*Ctrans;",
        "  matrix raw_unit_replay=matrix(Rraw)*Craw-matrix(ideal(1));",
        '  print("RAW_UNIT_REPLAY_ZERO="+string(size(module(raw_unit_replay))==0));',
        '  write("raw_unit_cofactors.txt",Craw);',
        "}",
        "quit;",
        "",
    ])
    return "\n".join(lines)


def tracked_parse_text(result, raw):
    full = tracked_raw_certificate_text(result, raw)
    prefix = full.split('print("START_LIFTSTD");', 1)[0]
    return prefix + 'print("TRACKED_PARSE_PASS");\nquit;\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = compile_rref()
    raw = json.loads((HERE / "RAW_DIRECT_SYSTEM.json").read_text())
    payloads = {
        "ROW_RREF_SYSTEM.json": ce.pretty(result),
        "row_rref_q.sing": singular_text(result, 0).encode(),
        "row_rref_q_dp_slimgb.sing": singular_text(result, 0, "slimgb").encode(),
        "row_rref_p65521.sing": singular_text(result, 65521).encode(),
        "row_rref_q_tracked_raw_certificate.sing": tracked_raw_certificate_text(result, raw).encode(),
        "row_rref_q_tracked_parse.sing": tracked_parse_text(result, raw).encode(),
    }
    args.output.mkdir(parents=True, exist_ok=True)
    for name, payload in payloads.items():
        path = args.output / name
        if args.check:
            assert path.read_bytes() == payload, f"stale generated file: {path}"
        else:
            path.write_bytes(payload)
    print(json.dumps({
        "status": "PASS",
        "variables": result["variable_count"],
        "pivots": result["pivot_count"],
        "free_variables": result["free_variable_count"],
        "generators": result["generator_count"],
        "system_sha256": hashlib.sha256(payloads["ROW_RREF_SYSTEM.json"]).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
