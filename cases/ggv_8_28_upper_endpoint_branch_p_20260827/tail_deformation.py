#!/usr/bin/env python3
"""Compile an exact weight-11 square-tail witness specialization."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW_PATH = HERE / "RAW_DIRECT_SYSTEM.json"
SOURCE_PATH = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def pretty(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def rref(matrix):
    a = [row[:] for row in matrix]
    row_count = len(a)
    column_count = len(a[0]) if a else 0
    pivot_row = 0
    pivots = []
    for column in range(column_count):
        chosen = next((row for row in range(pivot_row, row_count) if a[row][column]), None)
        if chosen is None:
            continue
        a[pivot_row], a[chosen] = a[chosen], a[pivot_row]
        scalar = a[pivot_row][column]
        a[pivot_row] = [value / scalar for value in a[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not a[row][column]:
                continue
            scalar = a[row][column]
            a[row] = [left - scalar * right for left, right in zip(a[row], a[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return a, pivots


def add(left, right):
    out = dict(left)
    for mon, coefficient in right.items():
        out[mon] = out.get(mon, Q(0)) + coefficient
        if not out[mon]:
            del out[mon]
    return out


def mul(left, right):
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            mon = tuple(sorted(a + b))
            out[mon] = out.get(mon, Q(0)) + ca * cb
            if not out[mon]:
                del out[mon]
    return out


def scale(poly, coefficient):
    return {mon: coefficient * value for mon, value in poly.items() if coefficient * value}


def encode(poly):
    return [[list(mon), str(coefficient)] for mon, coefficient in sorted(poly.items())]


def expression(poly):
    if not poly:
        return "0"
    pieces = []
    for mon, coefficient in sorted(poly.items()):
        atom = "*".join(f"p{index}" for index in mon) if mon else "1"
        pieces.append(f"({coefficient})*{atom}")
    return "+".join(pieces)


def compile_tail(cutoff):
    assert 4 <= cutoff <= 11
    assert sha256(RAW_PATH) == RAW_SHA256
    raw = json.loads(RAW_PATH.read_text())
    source = json.loads(SOURCE_PATH.read_text())
    slot_weights = {
        slot["slot"]: int(slot["weight"])
        for kind in ("F", "G")
        for slot in source["raw_slots_through_weight_22"][kind]
    }

    def weight(name):
        if name.startswith("z_"):
            return 2
        if name.startswith("tt_"):
            return 3
        return slot_weights[name]

    retained = [name for name in raw["variables"] if weight(name) >= cutoff]
    retained_index = {name: index for index, name in enumerate(retained)}
    linear_last = min(21, 2 * cutoff - 1)
    prefix_records = [record for record in raw["generators"]
                      if int(record["row"]) <= linear_last]
    matrix = []
    for record in prefix_records:
        row = [Q(0)] * len(retained)
        for mon, coefficient in record["terms"]:
            coefficient = Q(coefficient)
            kept = [name for name in mon if name in retained_index]
            if len(kept) != len(mon):
                continue
            assert len(kept) == 1, (record["row"], record["x_degree"], mon)
            row[retained_index[kept[0]]] += coefficient
        matrix.append(row)

    reduced, pivots = rref(matrix)
    free = [column for column in range(len(retained)) if column not in set(pivots)]
    basis = []
    for free_column in free:
        vector = [Q(0)] * len(retained)
        vector[free_column] = Q(1)
        for row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[row][free_column]
        assert all(sum(a * b for a, b in zip(matrix_row, vector)) == 0
                   for matrix_row in matrix)
        basis.append(vector)

    parameter_forms = {}
    for column, name in enumerate(retained):
        parameter_forms[name] = {
            (parameter,): basis[parameter][column]
            for parameter in range(len(basis)) if basis[parameter][column]
        }

    constraints = []
    nonlinear_records = [record for record in raw["generators"]
                         if linear_last < int(record["row"]) <= 22]
    for record in nonlinear_records:
        poly = {}
        for mon, coefficient in record["terms"]:
            coefficient = Q(coefficient)
            if not mon:
                poly = add(poly, {(): coefficient})
                continue
            if any(name not in parameter_forms for name in mon):
                continue
            term = {(): Q(1)}
            for name in mon:
                term = mul(term, parameter_forms[name])
            poly = add(poly, scale(term, coefficient))
        constraints.append({
            "row": int(record["row"]),
            "x_degree": int(record["x_degree"]),
            "terms": encode(poly),
            "sha256": hashlib.sha256(compact(encode(poly))).hexdigest(),
        })

    values = {}
    for name in raw["variables"]:
        form = parameter_forms.get(name, {})
        values[name] = [[index, str(form.get((index,), Q(0)))]
                        for index in range(len(basis)) if form.get((index,), Q(0))]
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-BRANCH-P-TAIL-DEFORMATION-v1",
        "authoritative_raw_system_sha256": RAW_SHA256,
        "cutoff": cutoff,
        "specialization": f"all raw parameters of weight below {cutoff} are zero",
        "linear_last_row": linear_last,
        "prefix_generator_count": len(prefix_records),
        "retained_variables": retained,
        "retained_variable_count": len(retained),
        "prefix_rank": len(pivots),
        "nullity": len(basis),
        "nullspace_basis": [[[retained[column], str(value)]
                              for column, value in enumerate(vector) if value]
                             for vector in basis],
        "raw_value_linear_map": values,
        "constraints": constraints,
        "constraint_generator_count": len(constraints),
        "D23_imposed": False,
        "G22_present": False,
        "negative_result_scope": "specialization_only_non_evidence",
    }


def singular_text(result):
    variables = [f"p{index}" for index in range(result["nullity"])] or ["dummy"]
    constraints = [
        {tuple(mon): Q(coefficient) for mon, coefficient in record["terms"]}
        for record in result["constraints"]
    ]
    lines = [
        f"ring tail=0,({','.join(variables)}),dp;",
        "option(redSB);",
        "ideal I=",
        ",\n".join(expression(poly) for poly in constraints) + ";",
        'print("TAIL variables="+string(nvars(basering))+" generators="+string(size(I)));',
        'print("START_STD");',
        "int start_time=timer;",
        "ideal J=slimgb(I);",
        "int elapsed=timer-start_time;",
        'print("END_STD seconds="+string(elapsed));',
        'print("BASIS_SIZE="+string(size(J)));',
        "int is_unit=(size(J)==1 && J[1]==1);",
        'print("UNIT="+string(is_unit));',
        'if(!is_unit){print("DIM="+string(dim(J)));}',
        "J;",
        "quit;",
        "",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--cutoff", type=int, default=11)
    args = parser.parse_args()
    result = compile_tail(args.cutoff)
    payloads = {
        "TAIL_DEFORMATION_SYSTEM.json": pretty(result),
        "tail_q.sing": singular_text(result).encode(),
    }
    args.output.mkdir(parents=True, exist_ok=True)
    for name, payload in payloads.items():
        (args.output / name).write_bytes(payload)
    print(json.dumps({
        "status": "PASS",
        "retained_variables": result["retained_variable_count"],
        "prefix_rank": result["prefix_rank"],
        "nullity": result["nullity"],
        "cutoff": result["cutoff"],
        "linear_last_row": result["linear_last_row"],
        "constraint_generators": result["constraint_generator_count"],
        "system_sha256": hashlib.sha256(payloads["TAIL_DEFORMATION_SYSTEM.json"]).hexdigest(),
        "singular_sha256": hashlib.sha256(payloads["tail_q.sing"]).hexdigest(),
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
