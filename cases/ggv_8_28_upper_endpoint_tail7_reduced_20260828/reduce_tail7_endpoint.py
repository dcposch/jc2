#!/usr/bin/env python3
"""Exact triangular reduction of the first endpoint-capable square tail.

The weight-7 tail is compiled by ``tail_deformation.py``.  Its constant
endpoint coordinate is ``-1-p32*p87``.  This reducer selects the reduced
chart

    p87 = F_7[X^0] = 1,   p32 = G_15[X^1] = -1,

then eliminates, row by row, every constant-coefficient pivot in weights
14 through 21.  Only compatibility equations and the transformed row-22
target are emitted.  All arithmetic is over Q and all reconstruction maps
are serialized.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
TAIL7 = HERE / "TAIL7_REDUCED/TAIL_DEFORMATION_SYSTEM.json"
TAIL7_SHA256 = "7edd5ccd471e9eb3e27f0f163b0b337e0fb5057126ec69869f988093defba7aa"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact(value) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def pretty(value) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def add(left, right):
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, Q(0)) + coefficient
        if not out[monomial]:
            del out[monomial]
    return out


def scale(poly, coefficient):
    coefficient = Q(coefficient)
    return {
        monomial: coefficient * value
        for monomial, value in poly.items()
        if coefficient * value
    }


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
    return [
        [list(monomial), str(coefficient)]
        for monomial, coefficient in sorted(poly.items())
    ]


def substitute(poly, substitutions):
    out = {}
    for monomial, coefficient in poly.items():
        term = {(): coefficient}
        for variable in monomial:
            term = mul(term, substitutions.get(variable, {(variable,): Q(1)}))
        out = add(out, term)
    return out


def parameter_weight(basis_vector):
    weights = set()
    for name, _coefficient in basis_vector:
        kind, x_degree, y_degree = name.split("_")
        offset = 8 if kind == "f" else 12
        weights.add(offset + 3 * int(x_degree) - int(y_degree))
    # The frozen square baseline has positive coefficients through weight 3.
    # A free F-coordinate can therefore carry forced G-coordinates one or
    # more rows later.  Its triangular stage is the first raw weight in its
    # basis vector, not the last displayed slot.
    assert max(weights) - min(weights) <= 3, (basis_vector, weights)
    return min(weights)


def rref_rows(rows, column_count):
    """RREF constant columns while carrying polynomial right sides."""
    rows = [([Q(value) for value in coefficients], dict(residual))
            for coefficients, residual in rows]
    pivot_row = 0
    pivots = []
    for column in range(column_count):
        chosen = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][0][column]),
            None,
        )
        if chosen is None:
            continue
        rows[pivot_row], rows[chosen] = rows[chosen], rows[pivot_row]
        coefficients, residual = rows[pivot_row]
        scalar = coefficients[column]
        coefficients = [value / scalar for value in coefficients]
        residual = scale(residual, Q(1) / scalar)
        rows[pivot_row] = (coefficients, residual)
        for row in range(len(rows)):
            if row == pivot_row or not rows[row][0][column]:
                continue
            scalar = rows[row][0][column]
            rows[row] = (
                [left - scalar * right
                 for left, right in zip(rows[row][0], coefficients)],
                add(rows[row][1], scale(residual, -scalar)),
            )
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return rows, pivots


def polynomial_degree(poly):
    return max((len(monomial) for monomial in poly), default=-1)


def singular_expression(poly):
    if not poly:
        return "0"
    pieces = []
    for monomial, coefficient in sorted(poly.items()):
        atom = "*".join(f"p{variable}" for variable in monomial) or "1"
        pieces.append(f"({coefficient})*{atom}")
    return "+".join(pieces)


def compile_reduced():
    assert sha256(TAIL7) == TAIL7_SHA256
    tail = json.loads(TAIL7.read_text())
    assert tail["cutoff"] == 7
    assert tail["nullity"] == 88

    weights = {
        parameter: parameter_weight(vector)
        for parameter, vector in enumerate(tail["nullspace_basis"])
    }
    assert weights[87] == 7
    assert weights[32] == 15

    substitutions = {
        87: {(): Q(1)},
        32: {(): Q(-1)},
    }
    reconstruction = {
        parameter: substitutions.get(parameter, {(parameter,): Q(1)})
        for parameter in range(88)
    }
    constraints_by_row = {}
    for record in tail["constraints"]:
        constraints_by_row.setdefault(int(record["row"]), []).append({
            "x_degree": int(record["x_degree"]),
            "poly": decode(record["terms"]),
        })

    reduced_constraints = []
    elimination_log = []
    free_high_parameters = []

    for row_number in range(14, 22):
        records = constraints_by_row[row_number]
        new_parameters = sorted(
            parameter for parameter, weight in weights.items()
            if weight == row_number and parameter not in substitutions
        )
        matrix_rows = []
        for record in records:
            poly = substitute(record["poly"], substitutions)
            coefficients = [Q(0)] * len(new_parameters)
            residual = {}
            for monomial, coefficient in poly.items():
                hits = [variable for variable in monomial if variable in new_parameters]
                if not hits:
                    residual[monomial] = coefficient
                    continue
                assert len(hits) == 1 and monomial == (hits[0],), (
                    row_number, record["x_degree"], monomial
                )
                coefficients[new_parameters.index(hits[0])] += coefficient
            matrix_rows.append((coefficients, residual))

        reduced_rows, pivot_columns = rref_rows(matrix_rows, len(new_parameters))
        pivot_set = set(pivot_columns)
        free_columns = [
            column for column in range(len(new_parameters)) if column not in pivot_set
        ]
        free_parameters = [new_parameters[column] for column in free_columns]
        free_high_parameters.extend(free_parameters)

        for pivot_row, pivot_column in enumerate(pivot_columns):
            coefficients, residual = reduced_rows[pivot_row]
            solution = scale(residual, -1)
            for free_column in free_columns:
                if coefficients[free_column]:
                    solution = add(
                        solution,
                        {(new_parameters[free_column],): -coefficients[free_column]},
                    )
            parameter = new_parameters[pivot_column]
            substitutions[parameter] = solution
            reconstruction[parameter] = solution

        compatibility_count = 0
        for coefficients, residual in reduced_rows[len(pivot_columns):]:
            assert not any(coefficients)
            if not residual:
                continue
            reduced_constraints.append({
                "source_row": row_number,
                "source_kind": "left_cokernel",
                "poly": residual,
            })
            compatibility_count += 1
        elimination_log.append({
            "row": row_number,
            "equation_count": len(records),
            "new_parameter_count": len(new_parameters),
            "rank": len(pivot_columns),
            "free_parameters": free_parameters,
            "nonzero_compatibility_count": compatibility_count,
        })

    for record in constraints_by_row[22]:
        poly = substitute(record["poly"], substitutions)
        if not poly:
            continue
        reduced_constraints.append({
            "source_row": 22,
            "source_x_degree": record["x_degree"],
            "source_kind": "endpoint",
            "poly": poly,
        })

    # A compatibility equation can become genuinely linear after the fixed
    # endpoint chart and triangular substitutions.  Remove every such exact
    # affine pivot before asking a nonlinear engine to work.
    linear_cleanup_log = []
    while True:
        linear_records = [
            record for record in reduced_constraints
            if polynomial_degree(record["poly"]) <= 1
        ]
        if not linear_records:
            break
        candidate_parameters = sorted(
            set(variable for record in linear_records
                for monomial in record["poly"] for variable in monomial)
        )
        matrix_rows = []
        for record in linear_records:
            coefficients = [Q(0)] * len(candidate_parameters)
            constant = Q(0)
            for monomial, coefficient in record["poly"].items():
                if not monomial:
                    constant += coefficient
                else:
                    assert len(monomial) == 1
                    coefficients[candidate_parameters.index(monomial[0])] += coefficient
            matrix_rows.append((coefficients, {(): constant} if constant else {}))
        reduced_rows, pivot_columns = rref_rows(matrix_rows, len(candidate_parameters))
        pivot_set = set(pivot_columns)
        free_columns = [
            column for column in range(len(candidate_parameters))
            if column not in pivot_set
        ]
        for pivot_row, pivot_column in enumerate(pivot_columns):
            coefficients, residual = reduced_rows[pivot_row]
            solution = scale(residual, -1)
            for free_column in free_columns:
                if coefficients[free_column]:
                    solution = add(
                        solution,
                        {(candidate_parameters[free_column],): -coefficients[free_column]},
                    )
            parameter = candidate_parameters[pivot_column]
            substitutions[parameter] = solution
            reconstruction[parameter] = solution
        inconsistent = [
            residual for coefficients, residual in reduced_rows[len(pivot_columns):]
            if not any(coefficients) and residual
        ]
        assert not inconsistent, inconsistent
        linear_ids = {id(record) for record in linear_records}
        reduced_constraints = [
            {**record, "poly": substitute(record["poly"], substitutions)}
            for record in reduced_constraints if id(record) not in linear_ids
        ]
        reduced_constraints = [
            record for record in reduced_constraints if record["poly"]
        ]
        linear_cleanup_log.append({
            "equation_count": len(linear_records),
            "candidate_parameter_count": len(candidate_parameters),
            "rank": len(pivot_columns),
            "pivot_parameters": [candidate_parameters[column]
                                 for column in pivot_columns],
        })

    eliminated = set(substitutions)
    remaining = sorted(
        parameter for parameter in range(88) if parameter not in eliminated
    )
    assert free_high_parameters == [43], free_high_parameters
    assert len(remaining) == 41, remaining
    assert {67, 76, 86}.issubset(eliminated), eliminated
    assert 43 in remaining and 87 not in remaining and 32 not in remaining
    assert all(
        set(monomial).issubset(remaining)
        for record in reduced_constraints for monomial in record["poly"]
    )

    # Reconstruct every initial p-parameter and then every literal raw slot.
    p_reconstruction = {
        str(parameter): encode(substitute(reconstruction[parameter], substitutions))
        for parameter in range(88)
    }
    raw_reconstruction = {}
    for name, linear_form in tail["raw_value_linear_map"].items():
        poly = {}
        for parameter, coefficient in linear_form:
            poly = add(poly, scale(reconstruction[int(parameter)], Q(coefficient)))
        raw_reconstruction[name] = encode(substitute(poly, substitutions))

    encoded_constraints = []
    for index, record in enumerate(reduced_constraints):
        encoded = encode(record["poly"])
        encoded_constraints.append({
            "index": index,
            "source_row": record["source_row"],
            "source_x_degree": record.get("source_x_degree"),
            "source_kind": record["source_kind"],
            "degree": polynomial_degree(record["poly"]),
            "term_count": len(record["poly"]),
            "terms": encoded,
            "sha256": hashlib.sha256(compact(encoded)).hexdigest(),
        })

    result = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-BRANCH-P-TAIL7-REDUCED-v1",
        "tail7_system_sha256": TAIL7_SHA256,
        "field": "Q",
        "fixed_chart": {
            "p87": "1",
            "p87_meaning": "F7[X^0]",
            "p32": "-1",
            "p32_meaning": "G15[X^1]",
            "endpoint_constant_identity": "D22[X^0]=-p32*p87=1",
        },
        "elimination_log": elimination_log,
        "linear_cleanup_log": linear_cleanup_log,
        "remaining_parameters": remaining,
        "remaining_parameter_count": len(remaining),
        "p_reconstruction": p_reconstruction,
        "raw_value_polynomial_map": raw_reconstruction,
        "constraints": encoded_constraints,
        "constraint_count": len(encoded_constraints),
        "maximum_constraint_degree": max(
            (record["degree"] for record in encoded_constraints), default=-1
        ),
        "D0_through_D13": "eliminated by exact tail nullspace",
        "D14_through_D21": "constant-Q triangular pivots plus displayed cokernels",
        "D22_constant": "identically 1 on fixed chart",
        "D23_imposed": False,
        "G22_present": False,
        "result_scope": "positive discovery section; negative result is specialization-only",
    }
    return result


def singular_text(result, characteristic=0):
    variables = [f"p{parameter}" for parameter in result["remaining_parameters"]]
    polys = [decode(record["terms"]) for record in result["constraints"]]
    lines = [
        f"ring tail7r={characteristic},({','.join(variables)}),dp;",
        "option(redSB);",
        "ideal I=",
        ",\n".join(singular_expression(poly) for poly in polys) + ";",
        'print("TAIL7R variables="+string(nvars(basering))+" generators="+string(size(I)));',
        'print("START_SLIMGB");',
        "int start_time=timer;",
        "ideal J=slimgb(I);",
        "int elapsed=timer-start_time;",
        'print("END_SLIMGB seconds="+string(elapsed));',
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
    args = parser.parse_args()
    result = compile_reduced()
    payloads = {
        "TAIL7_REDUCED_SYSTEM.json": pretty(result),
        "tail7_reduced_q.sing": singular_text(result).encode(),
        "tail7_reduced_p65521.sing": singular_text(result, 65521).encode(),
    }
    args.output.mkdir(parents=True, exist_ok=True)
    for name, payload in payloads.items():
        (args.output / name).write_bytes(payload)
    print(json.dumps({
        "status": "PASS",
        "remaining_parameters": result["remaining_parameter_count"],
        "constraints": result["constraint_count"],
        "maximum_degree": result["maximum_constraint_degree"],
        "system_sha256": hashlib.sha256(payloads["TAIL7_REDUCED_SYSTEM.json"]).hexdigest(),
        "singular_sha256": hashlib.sha256(payloads["tail7_reduced_q.sing"]).hexdigest(),
        "modp_singular_sha256": hashlib.sha256(
            payloads["tail7_reduced_p65521.sing"]
        ).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
