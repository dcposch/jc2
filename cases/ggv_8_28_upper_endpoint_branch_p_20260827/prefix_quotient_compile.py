#!/usr/bin/env python3
"""Compile the exact reviewed-prefix quotient of the raw endpoint ideal.

Only original raw generators are retained.  Exact polynomial cofactor traces
prove that the 47 omitted D4--D6 coefficients belong to the retained ideal.
This is a small deterministic compiler, not a Groebner-basis computation.
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
RAW = HERE / "RAW_DIRECT_SYSTEM.json"
RREF = HERE / "ROW_RREF/ROW_RREF_SYSTEM.json"
OUT_DIR = HERE / "PREFIX_QUOTIENT"
OUT_JSON = OUT_DIR / "PREFIX_QUOTIENT_SYSTEM.json"
OUT_SING = OUT_DIR / "prefix_quotient_q.sing"
OUT_SING_SLIMGB = OUT_DIR / "prefix_quotient_q_slimgb.sing"

RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
RREF_SHA256 = "9b1d9f83e369bbd43a329d98f450a525052ec526fcd72fbd40195ccc43849759"
KEEP_COUNTS = {4: 20, 5: 20, 6: 18}
OMITTED_DEGREES = {
    4: list(range(20, 36)),
    5: list(range(20, 35)),
    6: list(range(18, 34)),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_endpoint_compiler():
    path = HERE / "compile_endpoint.py"
    spec = importlib.util.spec_from_file_location("ggv_prefix_endpoint_compiler", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ce = load_endpoint_compiler()
MV = ce.MV


def decode(encoded) -> MV:
    return MV({tuple(monomial): Q(coefficient) for monomial, coefficient in encoded})


def mv_pow(poly: MV, exponent: int) -> MV:
    out = MV.const(1)
    base = poly
    while exponent:
        if exponent & 1:
            out = out * base
        base = base * base
        exponent //= 2
    return out


def add_to_map(target, key, poly: MV, scalar=Q(1)):
    value = target.get(key, MV.zero()) + poly.scale(scalar)
    if value.terms:
        target[key] = value
    elif key in target:
        del target[key]


def reduce_one(poly: MV, variable: str, replacement: MV):
    """Return f|_(v=e), q with f=f|_(v=e)+q*(v-e)."""
    normal = MV.zero()
    quotient = MV.zero()
    v = MV.var(variable)
    for monomial, coefficient in poly.terms.items():
        exponent = monomial.count(variable)
        if not exponent:
            normal = normal + MV({monomial: coefficient})
            continue
        rest = tuple(name for name in monomial if name != variable)
        base = MV({rest: coefficient})
        normal = normal + base * mv_pow(replacement, exponent)
        for power in range(exponent):
            quotient = quotient + base * mv_pow(v, exponent - 1 - power) * mv_pow(replacement, power)
    return normal, quotient


def reduce_with_trace(poly: MV, replacements):
    """Reduce by closed monic graphs, preserving every division quotient."""
    normal = poly
    trace = {}
    for variable, replacement in replacements.items():
        normal, quotient = reduce_one(normal, variable, replacement)
        if quotient.terms:
            trace[variable] = quotient
    replay = normal
    for variable, quotient in trace.items():
        replay = replay + quotient * (MV.var(variable) - replacements[variable])
    assert replay == poly
    return normal, trace


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


def replay_representation(representation, raw_polynomials):
    out = MV.zero()
    for raw_index, cofactor in representation.items():
        out = out + cofactor * raw_polynomials[raw_index]
    return out


def compile_quotient():
    assert sha256(RAW) == RAW_SHA256
    assert sha256(RREF) == RREF_SHA256
    raw = json.loads(RAW.read_text())
    rref = json.loads(RREF.read_text())
    source = json.loads(ce.RAW_INPUT.read_text())
    assert ce.sha256(ce.RAW_INPUT) == ce.PINS["raw_input"]
    windows = ce.raw_windows(source)
    raw_polynomials = [decode(record["terms"]) for record in raw["generators"]]

    grouped = {row: [] for row in KEEP_COUNTS}
    for raw_index, record in enumerate(raw["generators"]):
        row = int(record["row"])
        if row in grouped:
            grouped[row].append({
                "raw_index": raw_index,
                "x_degree": int(record["x_degree"]),
                "poly": raw_polynomials[raw_index],
            })
    for row in grouped:
        grouped[row].sort(key=lambda record: record["x_degree"])

    omitted_indices = set()
    for row, keep_count in KEEP_COUNTS.items():
        assert [record["x_degree"] for record in grouped[row][keep_count:]] == OMITTED_DEGREES[row]
        omitted_indices.update(record["raw_index"] for record in grouped[row][keep_count:])
    retained_indices = [index for index in range(len(raw_polynomials)) if index not in omitted_indices]
    retained_set = set(retained_indices)
    assert len(retained_indices) == 466
    assert len(omitted_indices) == 47

    replacements = {}
    graph_representations = {}
    omitted_certificates = []
    prefix_rows = {}

    for row in (4, 5, 6):
        current = [windows["G"][row][degree]
                   for degree in sorted(windows["G"][row], reverse=True)]
        current.extend(windows["F"][row][degree]
                       for degree in sorted(windows["F"][row], reverse=True))
        selected = grouped[row][:KEEP_COUNTS[row]]
        normals = []
        traces = []
        matrix = []
        residuals = []
        for record in selected:
            normal, trace = reduce_with_trace(record["poly"], replacements)
            normals.append(normal)
            traces.append(trace)
            coefficients = [normal.terms.get((name,), Q(0)) for name in current]
            linear = MV.zero()
            for name, coefficient in zip(current, coefficients):
                linear = linear + MV.var(name).scale(coefficient)
            residual = normal - linear
            assert all(not any(name in current for name in monomial)
                       for monomial in residual.terms)
            matrix.append(coefficients)
            residuals.append(residual)

        reduced, rhs, transform, pivots = rref_with_transform(matrix, residuals)
        assert len(pivots) == KEEP_COUNTS[row]
        pivot_set = set(pivots)
        nonpivots = [column for column in range(len(current)) if column not in pivot_set]
        row_pivots = []
        for output_row, column in enumerate(pivots):
            expression = -rhs[output_row]
            for free_column in nonpivots:
                coefficient = reduced[output_row][free_column]
                if coefficient:
                    expression = expression - MV.var(current[free_column]).scale(coefficient)
            pivot = current[column]
            graph = MV.var(pivot) - expression
            transformed = MV.zero()
            for source_row, coefficient in enumerate(transform[output_row]):
                if coefficient:
                    transformed = transformed + normals[source_row].scale(coefficient)
            assert transformed == graph

            representation = {}
            for source_row, coefficient in enumerate(transform[output_row]):
                if not coefficient:
                    continue
                raw_index = selected[source_row]["raw_index"]
                add_to_map(representation, raw_index, MV.const(1), coefficient)
                for old_pivot, quotient in traces[source_row].items():
                    for retained_raw_index, old_cofactor in graph_representations[old_pivot].items():
                        add_to_map(
                            representation,
                            retained_raw_index,
                            quotient * old_cofactor,
                            -coefficient,
                        )
            assert set(representation) <= retained_set
            assert replay_representation(representation, raw_polynomials) == graph
            replacements[pivot] = expression
            graph_representations[pivot] = representation
            row_pivots.append(pivot)

        omitted_for_row = 0
        for record in grouped[row][KEEP_COUNTS[row]:]:
            normal, trace = reduce_with_trace(record["poly"], replacements)
            assert not normal.terms, (row, record["x_degree"])
            representation = {}
            for pivot, quotient in trace.items():
                for retained_raw_index, graph_cofactor in graph_representations[pivot].items():
                    add_to_map(representation, retained_raw_index, quotient * graph_cofactor)
            assert representation
            assert set(representation) <= retained_set
            assert replay_representation(representation, raw_polynomials) == record["poly"]
            cofactors = []
            for retained_raw_index in sorted(representation):
                encoded = representation[retained_raw_index].encode()
                cofactors.append({
                    "retained_raw_index": retained_raw_index,
                    "terms": encoded,
                    "sha256": hashlib.sha256(ce.compact(encoded)).hexdigest(),
                })
            omitted_certificates.append({
                "raw_index": record["raw_index"],
                "row": row,
                "x_degree": record["x_degree"],
                "raw_generator_sha256": raw["generators"][record["raw_index"]]["sha256"],
                "cofactors": cofactors,
            })
            omitted_for_row += 1

        prefix_rows[str(row)] = {
            "raw_generators": len(grouped[row]),
            "retained_generators": len(selected),
            "omitted_generators": omitted_for_row,
            "current_variables": len(current),
            "rank": len(pivots),
            "pivot_variables": row_pivots,
            "free_current_variables": [current[column] for column in nonpivots],
        }

    all_pivots = set(replacements)
    assert len(all_pivots) == 58
    assert all(not any(name in all_pivots for name in monomial)
               for expression in replacements.values() for monomial in expression.terms)
    assert len(omitted_certificates) == 47
    assert {record["raw_index"] for record in omitted_certificates} == omitted_indices

    retained_generators = []
    for quotient_index, raw_index in enumerate(retained_indices):
        record = raw["generators"][raw_index]
        retained_generators.append({
            "quotient_index": quotient_index,
            "raw_index": raw_index,
            "row": int(record["row"]),
            "x_degree": int(record["x_degree"]),
            "raw_generator_sha256": record["sha256"],
        })

    cofactor_entries = sum(len(record["cofactors"]) for record in omitted_certificates)
    cofactor_terms = sum(
        len(cofactor["terms"])
        for record in omitted_certificates for cofactor in record["cofactors"]
    )
    result = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-BRANCH-P-PREFIX-QUOTIENT-v1",
        "field": "Q",
        "authoritative_raw_system_sha256": RAW_SHA256,
        "method": "retain original raw generators; exact monic D4-D6 graph cofactors prove every omission",
        "variable_count": raw["variable_count"],
        "variables": raw["variables"],
        "raw_generator_count": raw["generator_count"],
        "retained_generator_count": len(retained_generators),
        "retained_generators": retained_generators,
        "omitted_generator_count": len(omitted_certificates),
        "omitted_certificates": omitted_certificates,
        "cofactor_entry_count": cofactor_entries,
        "cofactor_term_count": cofactor_terms,
        "prefix_rows": prefix_rows,
        "decision_order": {
            "source_row_rref_sha256": RREF_SHA256,
            "ordering": "(lp(202),dp(101))",
            "variables": rref["variables"],
            "pivot_count": rref["pivot_count"],
            "free_variable_count": rref["free_variable_count"],
        },
        "charged_rows": raw["charged_rows"],
        "D23_imposed": False,
        "G22_present": False,
        "endpoint_generator_count": sum(
            int(raw["generators"][index]["row"] == 22) for index in retained_indices
        ),
    }
    return result, raw


def singular_text(result, raw, algorithm="std"):
    assert algorithm in {"std", "slimgb"}
    marker = algorithm.upper()
    variables = result["decision_order"]["variables"]
    expressions = [
        decode(raw["generators"][record["raw_index"]]["terms"]).expression()
        for record in result["retained_generators"]
    ]
    return "\n".join([
        "// Exact-Q decision lane for the replayed reviewed-prefix quotient.",
        f"ring endpoint_prefix=0,({','.join(variables)}),(lp(202),dp(101));",
        "option(redSB);",
        "ideal I=",
        ",\n".join(expressions) + ";",
        'print("PREFIX_QUOTIENT variables="+string(nvars(basering))+" generators="+string(size(I)));',
        "int start_time=timer;",
        f'print("START_{marker}");',
        f"ideal J={algorithm}(I);",
        "int elapsed=timer-start_time;",
        f'print("END_{marker} seconds="+string(elapsed));',
        'print("BASIS_SIZE="+string(size(J)));',
        'int is_unit=(size(J)==1 && J[1]==1);',
        'print("UNIT="+string(is_unit));',
        'if(!is_unit){print("DIM="+string(dim(J)));}',
        "J;",
        "quit;",
        "",
    ])


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()

    result, raw = compile_quotient()
    payloads = {
        OUT_JSON: ce.pretty(result),
        OUT_SING: singular_text(result, raw).encode(),
        OUT_SING_SLIMGB: singular_text(result, raw, algorithm="slimgb").encode(),
    }
    if args.write:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        for path, payload in payloads.items():
            path.write_bytes(payload)
    else:
        for path, payload in payloads.items():
            assert path.read_bytes() == payload, f"stale generated file: {path}"
    print(json.dumps({
        "status": "PASS",
        "variables": result["variable_count"],
        "raw_generators": result["raw_generator_count"],
        "retained_generators": result["retained_generator_count"],
        "omitted_generators": result["omitted_generator_count"],
        "cofactor_entries": result["cofactor_entry_count"],
        "cofactor_terms": result["cofactor_term_count"],
        "endpoint_generators": result["endpoint_generator_count"],
        "system_sha256": hashlib.sha256(payloads[OUT_JSON]).hexdigest(),
        "singular_sha256": hashlib.sha256(payloads[OUT_SING]).hexdigest(),
        "singular_slimgb_sha256": hashlib.sha256(payloads[OUT_SING_SLIMGB]).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
