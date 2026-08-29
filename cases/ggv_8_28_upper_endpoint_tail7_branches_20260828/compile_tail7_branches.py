#!/usr/bin/env python3
"""Compile the two exact field-valued branches of the reduced tail-7 seed."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / (
    "cases/ggv_8_28_upper_endpoint_tail7_reduced_20260828/"
    "TAIL7_REDUCED/TAIL7_REDUCED_SYSTEM.json"
)
SOURCE_SHA256 = "770ba6d9b312e235e491b4ad948707c41ad4a622b3a17239fdfe62f353606e11"
BRANCHES = {
    "a3_4": {68: Q(3, 4), 60: Q(0), 54: Q(0)},
    "a3_2": {68: Q(3, 2), 60: Q(0), 54: Q(0)},
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pretty(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def compact(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def add(left, right):
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, Q(0)) + coefficient
        if not out[monomial]:
            del out[monomial]
    return out


def scale(poly, coefficient):
    coefficient = Q(coefficient)
    return {monomial: coefficient * value for monomial, value in poly.items()
            if coefficient * value}


def mul(left, right):
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            monomial = tuple(sorted(a + b))
            out[monomial] = out.get(monomial, Q(0)) + ca * cb
            if not out[monomial]:
                del out[monomial]
    return out


def decode(encoded):
    return {tuple(monomial): Q(coefficient) for monomial, coefficient in encoded}


def encode(poly):
    return [[list(monomial), str(coefficient)]
            for monomial, coefficient in sorted(poly.items())]


def substitute(poly, substitutions):
    out = {}
    for monomial, coefficient in poly.items():
        term = {(): coefficient}
        for variable in monomial:
            term = mul(term, substitutions.get(variable, {(variable,): Q(1)}))
        out = add(out, term)
    return out


def degree(poly):
    return max((len(monomial) for monomial in poly), default=-1)


def rref(rows, column_count):
    rows = [([Q(value) for value in coefficients], dict(residual))
            for coefficients, residual in rows]
    rank = 0
    pivots = []
    for column in range(column_count):
        chosen = next((row for row in range(rank, len(rows))
                       if rows[row][0][column]), None)
        if chosen is None:
            continue
        rows[rank], rows[chosen] = rows[chosen], rows[rank]
        coefficients, residual = rows[rank]
        scalar = coefficients[column]
        coefficients = [value / scalar for value in coefficients]
        residual = scale(residual, Q(1) / scalar)
        rows[rank] = (coefficients, residual)
        for row in range(len(rows)):
            if row == rank or not rows[row][0][column]:
                continue
            scalar = rows[row][0][column]
            rows[row] = (
                [left - scalar * right
                 for left, right in zip(rows[row][0], coefficients)],
                add(rows[row][1], scale(residual, -scalar)),
            )
        pivots.append(column)
        rank += 1
    return rows, pivots


def linear_cleanup(constraints, substitutions, reconstruction):
    log = []
    while True:
        linear = [record for record in constraints if degree(record["poly"]) <= 1]
        if not linear:
            return constraints, log
        variables = sorted(set(
            variable for record in linear for monomial in record["poly"]
            for variable in monomial
        ))
        rows = []
        for record in linear:
            coefficients = [Q(0)] * len(variables)
            constant = Q(0)
            for monomial, coefficient in record["poly"].items():
                if monomial:
                    assert len(monomial) == 1
                    coefficients[variables.index(monomial[0])] += coefficient
                else:
                    constant += coefficient
            rows.append((coefficients, {(): constant} if constant else {}))
        reduced, pivots = rref(rows, len(variables))
        free_columns = [column for column in range(len(variables))
                        if column not in set(pivots)]
        for pivot_row, pivot_column in enumerate(pivots):
            coefficients, residual = reduced[pivot_row]
            solution = scale(residual, -1)
            for free_column in free_columns:
                if coefficients[free_column]:
                    solution = add(solution, {
                        (variables[free_column],): -coefficients[free_column]
                    })
            parameter = variables[pivot_column]
            substitutions[parameter] = solution
            reconstruction[parameter] = solution
        inconsistent = [residual for coefficients, residual in reduced[len(pivots):]
                        if not any(coefficients) and residual]
        assert not inconsistent, inconsistent
        linear_ids = {id(record) for record in linear}
        constraints = [
            {**record, "poly": substitute(record["poly"], substitutions)}
            for record in constraints if id(record) not in linear_ids
        ]
        constraints = [record for record in constraints if record["poly"]]
        log.append({
            "equation_count": len(linear),
            "candidate_parameter_count": len(variables),
            "rank": len(pivots),
            "pivot_parameters": [variables[column] for column in pivots],
        })


def compile_branch(name, fixed):
    assert sha256(SOURCE) == SOURCE_SHA256
    source = json.loads(SOURCE.read_text())
    available = set(source["remaining_parameters"])
    assert set(fixed).issubset(available)
    substitutions = {parameter: {(): value} for parameter, value in fixed.items()}
    reconstruction = {
        parameter: substitutions.get(parameter, {(parameter,): Q(1)})
        for parameter in available
    }
    constraints = []
    for record in source["constraints"]:
        poly = substitute(decode(record["terms"]), substitutions)
        if poly:
            constraints.append({
                "source_index": record["index"],
                "source_row": record["source_row"],
                "source_x_degree": record["source_x_degree"],
                "poly": poly,
            })
    constraints, cleanup_log = linear_cleanup(
        constraints, substitutions, reconstruction
    )
    remaining = sorted(available - set(substitutions))
    assert all(set(monomial).issubset(remaining)
               for record in constraints for monomial in record["poly"])

    # Compose all 88 p-coordinates and all 303 raw coordinates with this
    # branch and its newly exposed affine pivots.
    p_map = {}
    for parameter, encoded in source["p_reconstruction"].items():
        p_map[parameter] = encode(substitute(decode(encoded), substitutions))
    raw_map = {}
    for slot, encoded in source["raw_value_polynomial_map"].items():
        raw_map[slot] = encode(substitute(decode(encoded), substitutions))

    encoded_constraints = []
    for index, record in enumerate(constraints):
        encoded = encode(record["poly"])
        encoded_constraints.append({
            "index": index,
            "source_index": record["source_index"],
            "source_row": record["source_row"],
            "source_x_degree": record["source_x_degree"],
            "degree": degree(record["poly"]),
            "term_count": len(record["poly"]),
            "terms": encoded,
            "sha256": hashlib.sha256(compact(encoded)).hexdigest(),
        })
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL7-FIELD-BRANCH-v1",
        "source_reduced_system_sha256": SOURCE_SHA256,
        "branch": name,
        "fixed_parameters": {str(parameter): str(value)
                             for parameter, value in fixed.items()},
        "branch_meaning": {"p68": "a", "p60": "b", "p54": "c"},
        "linear_cleanup_log": cleanup_log,
        "remaining_parameters": remaining,
        "remaining_parameter_count": len(remaining),
        "constraints": encoded_constraints,
        "constraint_count": len(encoded_constraints),
        "maximum_degree": max((record["degree"] for record in encoded_constraints),
                              default=-1),
        "p_reconstruction": p_map,
        "raw_value_polynomial_map": raw_map,
        "raw_slot_count": len(raw_map),
        "scope": "field-valued branch of normalized tail7 only",
    }


def singular_expression(poly):
    if not poly:
        return "0"
    pieces = []
    for monomial, coefficient in sorted(poly.items()):
        atom = "*".join(f"p{variable}" for variable in monomial) or "1"
        pieces.append(f"({coefficient})*{atom}")
    return "+".join(pieces)


def singular_text(result, characteristic=0):
    operative = sorted(set(
        variable for record in result["constraints"]
        for monomial, _coefficient in record["terms"]
        for variable in monomial
    ))
    variables = [f"p{parameter}" for parameter in operative]
    polys = [decode(record["terms"]) for record in result["constraints"]]
    return "\n".join([
        f"ring branch={characteristic},({','.join(variables)}),dp;",
        "option(redSB);",
        "ideal I=",
        ",\n".join(singular_expression(poly) for poly in polys) + ";",
        f'print("BRANCH={result["branch"]} variables="+string(nvars(basering))+" generators="+string(size(I)));',
        'print("START_SLIMGB");',
        "int start_time=timer;",
        "ideal J=slimgb(I);",
        'print("END_SLIMGB seconds="+string(timer-start_time));',
        'print("BASIS_SIZE="+string(size(J)));',
        "int is_unit=(size(J)==1 && J[1]==1);",
        'print("UNIT="+string(is_unit));',
        'if(!is_unit){print("DIM="+string(dim(J)));}',
        "J;",
        "quit;",
        "",
    ])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    summary = {}
    compiled = {}
    for name, fixed in BRANCHES.items():
        result = compile_branch(name, fixed)
        compiled[name] = result
        payloads = {
            f"{name}.json": pretty(result),
            f"{name}_q.sing": singular_text(result).encode(),
            f"{name}_p65521.sing": singular_text(result, 65521).encode(),
        }
        for filename, payload in payloads.items():
            (args.output / filename).write_bytes(payload)
        summary[name] = {
            "free_parameters": result["remaining_parameter_count"],
            "operative_parameters": len(set(
                variable for record in result["constraints"]
                for monomial, _coefficient in record["terms"]
                for variable in monomial
            )),
            "constraints": result["constraint_count"],
            "maximum_degree": result["maximum_degree"],
            "json_sha256": hashlib.sha256(payloads[f"{name}.json"]).hexdigest(),
            "q_sha256": hashlib.sha256(payloads[f"{name}_q.sing"]).hexdigest(),
            "modp_sha256": hashlib.sha256(payloads[f"{name}_p65521.sing"]).hexdigest(),
        }
    block_variables = set(range(78, 86))
    block_records = [
        record for record in compiled["a3_4"]["constraints"]
        if (set(variable for monomial, _coefficient in record["terms"]
                for variable in monomial)
            and set(variable for monomial, _coefficient in record["terms"]
                    for variable in monomial).issubset(block_variables))
    ]
    other_block_records = [
        record for record in compiled["a3_2"]["constraints"]
        if (set(variable for monomial, _coefficient in record["terms"]
                for variable in monomial)
            and set(variable for monomial, _coefficient in record["terms"]
                    for variable in monomial).issubset(block_variables))
    ]
    assert [record["terms"] for record in block_records] == [
        record["terms"] for record in other_block_records
    ]
    block = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL7-SHARED-EIGHT-VARIABLE-BLOCK-v1",
        "branch": "shared_block",
        "source_branches": ["a3_4", "a3_2"],
        "remaining_parameters": sorted(block_variables),
        "remaining_parameter_count": len(block_variables),
        "constraints": block_records,
        "constraint_count": len(block_records),
        "maximum_degree": max(record["degree"] for record in block_records),
        "scope": "necessary subsystem shared by both field branches",
    }
    block_payloads = {
        "shared_block.json": pretty(block),
        "shared_block_q.sing": singular_text(block).encode(),
        "shared_block_p65521.sing": singular_text(block, 65521).encode(),
    }
    for filename, payload in block_payloads.items():
        (args.output / filename).write_bytes(payload)
    summary["shared_block"] = {
        "parameters": block["remaining_parameter_count"],
        "constraints": block["constraint_count"],
        "maximum_degree": block["maximum_degree"],
        "json_sha256": hashlib.sha256(block_payloads["shared_block.json"]).hexdigest(),
        "q_sha256": hashlib.sha256(block_payloads["shared_block_q.sing"]).hexdigest(),
        "modp_sha256": hashlib.sha256(
            block_payloads["shared_block_p65521.sing"]
        ).hexdigest(),
    }
    print(json.dumps({"status": "PASS", "branches": summary}, sort_keys=True))


if __name__ == "__main__":
    main()
