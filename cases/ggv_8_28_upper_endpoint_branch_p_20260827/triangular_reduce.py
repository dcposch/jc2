#!/usr/bin/env python3
"""Exact row-by-row linear reduction of the authoritative raw endpoint ideal.

At weight n the D5G row is affine-linear in the new raw F_n/G_n slots with
a constant rational coefficient matrix.  This program performs only those
auditable Gaussian eliminations.  It neither factors nor computes a
Groebner basis.  The resulting nonlinear compatibility ideal is exactly
equivalent to the raw direct system after adjoining the recorded pivot
definitions.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_compiler():
    path = HERE / "compile_endpoint.py"
    spec = importlib.util.spec_from_file_location("ggv_endpoint_compiler", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ce = load_compiler()
MV = ce.MV


def mv_from(encoded):
    return MV({tuple(mon): Q(coefficient) for mon, coefficient in encoded})


def substitute(poly, replacements):
    """Simultaneously substitute variables; replacement values are closed."""
    out = MV.zero()
    for mon, coefficient in poly.terms.items():
        term = MV.const(coefficient)
        for name in mon:
            term = term * replacements.get(name, MV.var(name))
        out = out + term
    return out


def rref_with_rhs(matrix, rhs):
    a = [row[:] for row in matrix]
    b = list(rhs)
    row_count = len(a)
    column_count = len(a[0]) if a else 0
    pivot_row = 0
    pivots = []
    for column in range(column_count):
        chosen = next((row for row in range(pivot_row, row_count) if a[row][column]), None)
        if chosen is None:
            continue
        a[pivot_row], a[chosen] = a[chosen], a[pivot_row]
        b[pivot_row], b[chosen] = b[chosen], b[pivot_row]
        scale = a[pivot_row][column]
        a[pivot_row] = [value / scale for value in a[pivot_row]]
        b[pivot_row] = b[pivot_row].scale(1 / scale)
        for row in range(row_count):
            if row == pivot_row or not a[row][column]:
                continue
            scale = a[row][column]
            a[row] = [left - scale * right for left, right in zip(a[row], a[pivot_row])]
            b[row] = b[row] - b[pivot_row].scale(scale)
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return a, b, pivots


def encode_poly(poly):
    return poly.encode()


def reduce_system():
    system = json.loads((HERE / "RAW_DIRECT_SYSTEM.json").read_text())
    source = json.loads(ce.RAW_INPUT.read_text())
    windows = ce.raw_windows(source)
    grouped = {n: [] for n in range(4, 23)}
    for generator in system["generators"]:
        grouped[int(generator["row"])].append((int(generator["x_degree"]), mv_from(generator["terms"])))
    for n in grouped:
        grouped[n].sort()

    replacements = {}
    pivot_records = []
    compatibility = []
    row_stats = {}
    free_variables = set(system["variables"])

    for n in range(4, 22):
        current = []
        # Pivot raw G slots first.  This leaves every raw F slot free and,
        # at m=4,6,8,10,12, one G coordinate for the characteristic mode.
        current.extend(windows["G"][n][degree] for degree in sorted(windows["G"][n], reverse=True))
        if n <= 14:
            current.extend(windows["F"][n][degree] for degree in sorted(windows["F"][n], reverse=True))

        equations = [substitute(poly, replacements) for _, poly in grouped[n]]
        matrix = []
        rhs = []
        for poly in equations:
            row = [poly.terms.get((name,), Q(0)) for name in current]
            linear = MV.zero()
            for name, coefficient in zip(current, row):
                linear = linear + MV.var(name).scale(coefficient)
            residual = poly - linear
            # New-row variables must occur only in their fixed linear block.
            for mon in residual.terms:
                assert not any(name in current for name in mon), (n, mon)
            matrix.append(row)
            rhs.append(residual)

        reduced_matrix, reduced_rhs, pivot_columns = rref_with_rhs(matrix, rhs)
        pivot_set = set(pivot_columns)
        nonpivots = [column for column in range(len(current)) if column not in pivot_set]
        new_replacements = {}
        for row, column in enumerate(pivot_columns):
            expression = -reduced_rhs[row]
            for free_column in nonpivots:
                if reduced_matrix[row][free_column]:
                    expression = expression - MV.var(current[free_column]).scale(reduced_matrix[row][free_column])
            new_replacements[current[column]] = expression
            free_variables.discard(current[column])
            pivot_records.append({
                "row": n,
                "pivot": current[column],
                "expression": encode_poly(expression),
                "sha256": hashlib.sha256(ce.compact(encode_poly(expression))).hexdigest(),
            })

        # RREF zero rows are the complete left-cokernel conditions.
        row_compatibility = []
        for row in range(len(pivot_columns), len(reduced_matrix)):
            assert all(not value for value in reduced_matrix[row])
            condition = reduced_rhs[row]
            if condition.terms:
                record = {
                    "source_row": n,
                    "index": len(row_compatibility),
                    "terms": encode_poly(condition),
                    "sha256": hashlib.sha256(ce.compact(encode_poly(condition))).hexdigest(),
                }
                row_compatibility.append(record)
                compatibility.append(record)

        replacements.update(new_replacements)
        row_stats[str(n)] = {
            "equations": len(equations),
            "current_variables": len(current),
            "rank": len(pivot_columns),
            "kernel_dimension": len(nonpivots),
            "formal_cokernel_dimension": len(equations) - len(pivot_columns),
            "nonzero_compatibility_count": len(row_compatibility),
            "free_current_variables": [current[column] for column in nonpivots],
        }
        print(json.dumps({
            "event": "ROW_REDUCED",
            "row": n,
            "pivots_so_far": len(pivot_records),
            "compatibility_so_far": len(compatibility),
            **row_stats[str(n)],
        }, sort_keys=True), flush=True)

    endpoint = []
    for degree, poly in grouped[22]:
        condition = substitute(poly, replacements)
        if condition.terms:
            endpoint.append({
                "source_row": 22,
                "x_degree": degree,
                "terms": encode_poly(condition),
                "sha256": hashlib.sha256(ce.compact(encode_poly(condition))).hexdigest(),
            })

    constraints = compatibility + endpoint
    actually_used = sorted({name for record in constraints for mon, _ in record["terms"] for name in mon})
    assert set(actually_used) <= free_variables
    result = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-BRANCH-P-TRIANGULAR-v1",
        "authoritative_raw_system_sha256": ce.sha256(HERE / "RAW_DIRECT_SYSTEM.json"),
        "method": "constant-Q RREF of each same-weight raw block; exact pivot substitution",
        "row_stats": row_stats,
        "pivot_count": len(pivot_records),
        "pivots": pivot_records,
        "free_variables": [name for name in system["variables"] if name in free_variables],
        "free_variable_count": len(free_variables),
        "active_free_variables": actually_used,
        "active_free_variable_count": len(actually_used),
        "compatibility": compatibility,
        "compatibility_count": len(compatibility),
        "endpoint": endpoint,
        "endpoint_count": len(endpoint),
        "constraints": constraints,
        "constraint_count": len(constraints),
        "D23_imposed": False,
    }
    return result


def singular_text(result, modulus=0, tracked=False):
    variables = result["active_free_variables"]
    expressions = [mv_from(record["terms"]).expression(modulus) for record in result["constraints"]]
    ordering = "lp"
    lines = [
        f"ring endpoint_reduced={modulus},({','.join(variables)}),{ordering};",
        "option(redSB);",
        "ideal I=",
        ",\n".join(expressions) + ";",
        'print("TRIANGULAR variables="+string(nvars(basering))+" generators="+string(size(I)));',
        "int start_time=timer;",
        'print("START_STD");',
    ]
    if tracked:
        lines.extend([
            "matrix T; ideal J=liftstd(I,T);",
            "matrix basis_replay=matrix(I)*T-matrix(J);",
            'print("BASIS_REPLAY_ZERO="+string(basis_replay==0));',
        ])
    else:
        lines.append("ideal J=std(I);")
    lines.extend([
        "int elapsed=timer-start_time;",
        'print("END_STD seconds="+string(elapsed));',
        'print("BASIS_SIZE="+string(size(J)));',
        'int is_unit=(size(J)==1 && J[1]==1);',
        'print("UNIT="+string(is_unit));',
    ])
    if tracked:
        lines.extend([
            "if(is_unit){",
            "  matrix Hunit=lift(J,ideal(1));",
            "  matrix Cunit=T*Hunit;",
            "  matrix unit_replay=matrix(I)*Cunit-matrix(ideal(1));",
            '  print("UNIT_REPLAY_ZERO="+string(unit_replay==0));',
            '  write("unit_cofactors.txt",Cunit);',
            "}",
        ])
    lines.extend(["quit;", ""])
    return "\n".join(lines)


def msolve_text(result, modulus):
    variables = result["active_free_variables"]
    expressions = [mv_from(record["terms"]).expression(modulus) for record in result["constraints"]]
    return f"{', '.join(variables)}\n{modulus}\n" + ",\n".join(expressions) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    result = reduce_system()
    payloads = {
        "TRIANGULAR_REDUCTION.json": ce.pretty(result),
        "reduced_q.sing": singular_text(result).encode(),
        "reduced_q_tracked.sing": singular_text(result, tracked=True).encode(),
        "reduced_p65521.sing": singular_text(result, 65521).encode(),
        "reduced_q.ms": msolve_text(result, 0).encode(),
        "reduced_p65521.ms": msolve_text(result, 65521).encode(),
    }
    for name, payload in payloads.items():
        (args.output / name).write_bytes(payload)
    manifest = {name: hashlib.sha256(payload).hexdigest() for name, payload in payloads.items()}
    (args.output / "GENERATED.sha256.json").write_bytes(ce.pretty(manifest))
    print(json.dumps({
        "status": "PASS",
        "pivots": result["pivot_count"],
        "free_variables": result["free_variable_count"],
        "active_free_variables": result["active_free_variable_count"],
        "compatibility": result["compatibility_count"],
        "endpoint": result["endpoint_count"],
        "constraints": result["constraint_count"],
        "reduction_sha256": manifest["TRIANGULAR_REDUCTION.json"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
