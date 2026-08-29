#!/usr/bin/env python3
"""Desk-scale exact analysis of the cutoff-six square tail.

This compiler uses only Python's standard library and rational arithmetic.
It never invokes Singular.  It proves directly that the necessary row-14/15
endpoint systems for both field-radical branches contain 1, and emits the
otherwise-unrun Singular inputs only as exact coefficient custody artifacts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / "TAIL6/TAIL_DEFORMATION_SYSTEM.json"
SOURCE_SHA256 = "c038fd929d8c11cf8465dd72edb5fc4cca430140d11199f3c6fbd2f968e1b389"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
TAIL_COMPILER = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/tail_deformation.py"

# Synthetic variable labels, disjoint from the nullspace parameters p0,...,p121.
B_VARS = tuple(range(1000, 1007))
V_VARS = tuple(range(1100, 1103))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact(value) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def pretty(value) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def decode(encoded):
    return {tuple(monomial): Q(coefficient) for monomial, coefficient in encoded}


def encode(poly):
    return [[list(monomial), str(coefficient)]
            for monomial, coefficient in sorted(poly.items())]


def add(left, right):
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, Q(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in out.items()
            if coefficient}


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
    return {monomial: coefficient for monomial, coefficient in out.items()
            if coefficient}


def substitute(poly, substitutions):
    out = {}
    for monomial, coefficient in poly.items():
        term = {(): coefficient}
        for variable in monomial:
            term = mul(term, substitutions.get(variable, {(variable,): Q(1)}))
        out = add(out, term)
    return out


def compose_substitutions(substitutions, extra):
    out = {variable: substitute(poly, extra)
           for variable, poly in substitutions.items()}
    out.update(extra)
    return out


def rref_rows(rows, column_count):
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


def rref_rows_with_provenance(rows, column_count):
    """RREF while recording each output row as a Q-combination of inputs."""
    row_count = len(rows)
    tracked = [
        ([Q(value) for value in coefficients], dict(residual),
         [Q(index == source) for source in range(row_count)])
        for index, (coefficients, residual) in enumerate(rows)
    ]
    rank = 0
    pivots = []
    for column in range(column_count):
        chosen = next((row for row in range(rank, row_count)
                       if tracked[row][0][column]), None)
        if chosen is None:
            continue
        tracked[rank], tracked[chosen] = tracked[chosen], tracked[rank]
        coefficients, residual, provenance = tracked[rank]
        scalar = coefficients[column]
        coefficients = [value / scalar for value in coefficients]
        residual = scale(residual, Q(1) / scalar)
        provenance = [value / scalar for value in provenance]
        tracked[rank] = (coefficients, residual, provenance)
        for row in range(row_count):
            if row == rank or not tracked[row][0][column]:
                continue
            scalar = tracked[row][0][column]
            tracked[row] = (
                [left - scalar * right
                 for left, right in zip(tracked[row][0], coefficients)],
                add(tracked[row][1], scale(residual, -scalar)),
                [left - scalar * right
                 for left, right in zip(tracked[row][2], provenance)],
            )
        pivots.append(column)
        rank += 1
    return tracked, pivots


def span_basis(polys):
    monomials = sorted({monomial for poly in polys for monomial in poly})
    if not monomials:
        return [], []
    matrix = [[poly.get(monomial, Q(0)) for monomial in monomials]
              for poly in polys]
    reduced, pivots = rref_rows([(row, {}) for row in matrix], len(monomials))
    basis = [
        {monomial: coefficient
         for monomial, coefficient in zip(monomials, reduced[row][0])
         if coefficient}
        for row in range(len(pivots))
    ]
    return basis, monomials


def linear_combination_witness(polys, target):
    """Return exact c_i with target=sum(c_i*polys[i]), or fail."""
    monomials = sorted({monomial for poly in polys + [target]
                        for monomial in poly})
    matrix = [[poly.get(monomial, Q(0)) for monomial in monomials]
              for poly in polys]
    reduced, pivots = rref_rows_with_provenance(
        [(row, {}) for row in matrix], len(monomials)
    )
    vector = [target.get(monomial, Q(0)) for monomial in monomials]
    witness = [Q(0)] * len(polys)
    for row, pivot in enumerate(pivots):
        scalar = vector[pivot]
        if not scalar:
            continue
        vector = [left - scalar * right
                  for left, right in zip(vector, reduced[row][0])]
        witness = [left + scalar * right
                   for left, right in zip(witness, reduced[row][2])]
    assert not any(vector), "target is not in the stated Q-row span"
    reconstructed = {}
    for coefficient, poly in zip(witness, polys):
        reconstructed = add(reconstructed, scale(poly, coefficient))
    assert reconstructed == target
    return witness


def same_span(left, right):
    left_basis, _ = span_basis(left)
    right_basis, _ = span_basis(right)
    combined_basis, _ = span_basis(left + right)
    return (len(left_basis) == len(right_basis) == len(combined_basis))


def reduce_by_span(poly, basis):
    monomials = sorted({monomial for item in basis + [poly] for monomial in item})
    matrix = [[item.get(monomial, Q(0)) for monomial in monomials]
              for item in basis]
    reduced, pivots = rref_rows([(row, {}) for row in matrix], len(monomials))
    vector = [poly.get(monomial, Q(0)) for monomial in monomials]
    for row, pivot in enumerate(pivots):
        if vector[pivot]:
            scalar = vector[pivot]
            vector = [left - scalar * right
                      for left, right in zip(vector, reduced[row][0])]
    return {monomial: coefficient
            for monomial, coefficient in zip(monomials, vector) if coefficient}


def dense_mul(left, right):
    out = [{} for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = add(out[i + j], mul(a, b))
    return out


def dense_add(left, right):
    out = [{} for _ in range(max(len(left), len(right)))]
    for index in range(len(out)):
        if index < len(left):
            out[index] = add(out[index], left[index])
        if index < len(right):
            out[index] = add(out[index], right[index])
    return out


def dense_scale(poly, coefficient):
    return [scale(item, coefficient) for item in poly]


def mod_h(poly):
    """Remainder modulo H=(X^4-1)^2=X^8-2X^4+1."""
    poly = [dict(item) for item in poly]
    if len(poly) < 8:
        poly.extend({} for _ in range(8 - len(poly)))
    for degree in range(len(poly) - 1, 7, -1):
        leading = poly[degree]
        poly[degree] = {}
        poly[degree - 4] = add(poly[degree - 4], scale(leading, 2))
        poly[degree - 8] = add(poly[degree - 8], scale(leading, -1))
    return poly[:8]


def parameter_stage(vector):
    weights = []
    for name, _coefficient in vector:
        kind, x_degree, y_degree = name.split("_")
        offset = 8 if kind == "f" else 12
        weights.append(offset + 3 * int(x_degree) - int(y_degree))
    return min(weights)


def triangular_stage(data, row_number, candidates, substitutions,
                     track_source=False):
    indexed_records = [
        (index, record) for index, record in enumerate(data["constraints"])
        if int(record["row"]) == row_number
    ]
    records = [record for _index, record in indexed_records]
    original_polys = []
    rows = []
    for record in records:
        poly = substitute(decode(record["terms"]), substitutions)
        original_polys.append(poly)
        coefficients = [Q(0)] * len(candidates)
        residual = {}
        for monomial, coefficient in poly.items():
            hits = [variable for variable in monomial if variable in candidates]
            if hits:
                assert len(hits) == 1 and monomial == (hits[0],), (
                    row_number, record["x_degree"], monomial, hits
                )
                coefficients[candidates.index(hits[0])] += coefficient
            else:
                residual[monomial] = coefficient
        rows.append((coefficients, residual))
    if track_source:
        reduced, pivots = rref_rows_with_provenance(rows, len(candidates))
    else:
        reduced, pivots = rref_rows(rows, len(candidates))
    free_columns = [column for column in range(len(candidates))
                    if column not in set(pivots)]
    for pivot_row, pivot_column in enumerate(pivots):
        coefficients, residual = reduced[pivot_row][:2]
        solution = scale(residual, -1)
        for free_column in free_columns:
            if coefficients[free_column]:
                solution = add(solution, {
                    (candidates[free_column],): -coefficients[free_column]
                })
        substitutions[candidates[pivot_column]] = solution
    compatibility = [item[1] for item in reduced[len(pivots):] if item[1]]
    log = {
        "row": row_number,
        "equation_count": len(records),
        "candidate_count": len(candidates),
        "rank": len(pivots),
        "free_parameters": [candidates[column] for column in free_columns],
        "displayed_compatibility_count": len(compatibility),
        "compatibility_span_rank": len(span_basis(compatibility)[0]),
    }
    if not track_source:
        return compatibility, log

    details = []
    for item in reduced[len(pivots):]:
        residual, provenance = item[1], item[2]
        if not residual:
            continue
        reconstructed = {}
        source_combination = []
        for source_index, coefficient in enumerate(provenance):
            if not coefficient:
                continue
            reconstructed = add(
                reconstructed, scale(original_polys[source_index], coefficient)
            )
            global_index, record = indexed_records[source_index]
            source_combination.append({
                "constraint_index": global_index,
                "row": row_number,
                "x_degree": int(record["x_degree"]),
                "coefficient": str(coefficient),
            })
        assert reconstructed == residual
        details.append({
            "terms": encode(residual),
            "source_row_combination_after_stage_entry_substitutions": (
                source_combination
            ),
        })
    assert [decode(item["terms"]) for item in details] == compatibility
    return compatibility, log, details


def a_equals_c_times_b():
    # F6=A=(X^4-1)B, deg B<=6; A_i=p_(121-i).
    substitutions = {}
    for degree in range(11):
        coefficient = {}
        if 0 <= degree - 4 <= 6:
            coefficient[(B_VARS[degree - 4],)] = Q(1)
        if 0 <= degree <= 6:
            coefficient[(B_VARS[degree],)] = (
                coefficient.get((B_VARS[degree],), Q(0)) - 1
            )
        substitutions[121 - degree] = {
            monomial: value for monomial, value in coefficient.items() if value
        }
    return substitutions


def a_equals_h_times_v():
    # F6=A=H V, H=X^8-2X^4+1, deg V<=2.
    substitutions = {}
    for degree in range(11):
        coefficient = {}
        if 0 <= degree <= 2:
            coefficient[(V_VARS[degree],)] = Q(1)
        if 0 <= degree - 4 <= 2:
            coefficient[(V_VARS[degree - 4],)] = (
                coefficient.get((V_VARS[degree - 4],), Q(0)) - 2
            )
        if 0 <= degree - 8 <= 2:
            coefficient[(V_VARS[degree - 8],)] = (
                coefficient.get((V_VARS[degree - 8],), Q(0)) + 1
            )
        substitutions[121 - degree] = {
            monomial: value for monomial, value in coefficient.items() if value
        }
    return substitutions


def row12_remainders():
    coefficients = [{(121 - degree,): Q(1)} for degree in range(11)]
    return mod_h(dense_mul(coefficients, coefficients))


def row13_model_remainders():
    b = [{(variable,): Q(1)} for variable in B_VARS]
    p = [{(110 - degree,): Q(1)} for degree in range(10)]
    c_times_p = [{} for _ in range(14)]
    for degree, coefficient in enumerate(p):
        c_times_p[degree] = add(c_times_p[degree], scale(coefficient, -1))
        c_times_p[degree + 4] = add(c_times_p[degree + 4], coefficient)
    return mod_h(dense_add(
        dense_scale(dense_mul(b, c_times_p), 4),
        dense_scale(dense_mul(b, b), -1),
    ))


def row13_extra():
    b0, b1, b2, b3, b4, b5, b6 = B_VARS
    return {
        (110, b0): Q(1),
        tuple(sorted((b0, b4))): Q(-1, 2),
        tuple(sorted((b1, b3))): Q(-1, 2),
        (b2, b2): Q(-1, 4),
        tuple(sorted((b2, b6))): Q(-1, 2),
        tuple(sorted((b3, b5))): Q(-1, 2),
        (b4, b4): Q(-1, 4),
        (b6, b6): Q(-1, 4),
    }


def b_equals_c_times_v():
    substitutions = {}
    for degree in range(7):
        coefficient = {}
        if 0 <= degree - 4 <= 2:
            coefficient[(V_VARS[degree - 4],)] = Q(1)
        if 0 <= degree <= 2:
            coefficient[(V_VARS[degree],)] = (
                coefficient.get((V_VARS[degree],), Q(0)) - 1
            )
        substitutions[B_VARS[degree]] = {
            monomial: value for monomial, value in coefficient.items() if value
        }
    return substitutions


def variable_name(variable):
    if variable < 1000:
        return f"p{variable}"
    if variable in B_VARS:
        return f"b{B_VARS.index(variable)}"
    if variable in V_VARS:
        return f"v{V_VARS.index(variable)}"
    raise AssertionError(variable)


def singular_expression(poly):
    pieces = []
    for monomial, coefficient in sorted(poly.items()):
        atom = "*".join(variable_name(variable) for variable in monomial) or "1"
        pieces.append(f"({coefficient})*{atom}")
    return "+".join(pieces) or "0"


def singular_text(target, characteristic=0):
    variables = [variable_name(variable) for variable in target["operative_variables"]]
    constraints = [decode(record["terms"]) for record in target["constraints"]]
    branch = target.get("branch", target.get("source_branch", "diagnostic"))
    return "\n".join([
        f"ring tail6={characteristic},({','.join(variables)}),dp;",
        "option(redSB);",
        "ideal I=",
        ",\n".join(singular_expression(poly) for poly in constraints) + ";",
        f'print("TAIL6_{branch.upper()} variables="+string(nvars(basering))+" generators="+string(size(I)));',
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


def encode_constraints(polys):
    out = []
    for index, poly in enumerate(polys):
        encoded = encode(poly)
        out.append({
            "index": index,
            "degree": max((len(monomial) for monomial in poly), default=-1),
            "term_count": len(poly),
            "terms": encoded,
            "sha256": hashlib.sha256(compact(encoded)).hexdigest(),
        })
    return out


def combine_source_provenance(details, coefficients):
    """Compose a compatibility-space witness with tracked source-row RREF."""
    combined = {}
    metadata = {}
    for detail, outer_coefficient in zip(details, coefficients):
        if not outer_coefficient:
            continue
        for record in detail[
                "source_row_combination_after_stage_entry_substitutions"]:
            key = int(record["constraint_index"])
            combined[key] = combined.get(key, Q(0)) + (
                outer_coefficient * Q(record["coefficient"])
            )
            metadata[key] = {
                "constraint_index": key,
                "row": int(record["row"]),
                "x_degree": int(record["x_degree"]),
            }
    return [
        {**metadata[key], "coefficient": str(combined[key])}
        for key in sorted(combined) if combined[key]
    ]


def compile_branch_target(data, stages, branch):
    substitutions = a_equals_h_times_v()
    row12, log12 = triangular_stage(data, 12, stages[12], substitutions)
    row13, log13 = triangular_stage(data, 13, stages[13], substitutions)
    assert not row12
    branch_substitution = {
        V_VARS[0]: {} if branch == "v0_zero" else {(110,): Q(4)}
    }
    substitutions = compose_substitutions(substitutions, branch_substitution)
    row13 = [substitute(poly, branch_substitution) for poly in row13]
    assert not [poly for poly in row13 if poly]

    row14, log14, row14_details = triangular_stage(
        data, 14, stages[14], substitutions, track_source=True
    )
    row14_basis, _ = span_basis(row14)
    assert len(row14) == 16 and len(row14_basis) == 8

    # The endpoint factor makes p32 and p110 units.  Keep both polynomially:
    # withhold p32 from the row-15 pivots and append 1+p32*p110=0.
    row15_candidates = [parameter for parameter in stages[15] if parameter != 32]
    row15, log15, row15_details = triangular_stage(
        data, 15, row15_candidates, substitutions, track_source=True
    )
    row15_basis, _ = span_basis(row15)
    assert len(row15) == len(row15_basis) == 17
    endpoint = {(): Q(1), (32, 110): Q(1)}
    cumulative_basis, _ = span_basis(row14 + row15)
    assert len(cumulative_basis) == 19
    constraints = cumulative_basis + [endpoint]

    # This was first noticed in the emitted RREF basis.  Reconstruct it from
    # the pre-span row-14/15 compatibility list to rule out an emission
    # artifact, then prove the two-generator unit identity without a GB.
    p110_square = {(110, 110): Q(1)}
    compatibility = row14 + row15
    square_witness = linear_combination_witness(compatibility, p110_square)
    expected_nonzero = {
        "v0_zero": {
            1: Q(1, 12), 13: Q(1, 9),
            19: Q(-2, 9), 23: Q(-2, 9),
            27: Q(-2, 9), 31: Q(-2, 9),
        },
        "v0_four_p110": {
            9: Q(-1), 13: Q(-37, 9),
            19: Q(16, 9), 23: Q(32, 9),
            27: Q(256, 45), 31: Q(512, 63),
        },
    }[branch]
    assert {index: coefficient for index, coefficient
            in enumerate(square_witness) if coefficient} == expected_nonzero
    assert p110_square in cumulative_basis

    endpoint_multiplier = {(): Q(1), (32, 110): Q(-1)}
    square_multiplier = {(32, 32): Q(1)}
    unit = add(
        mul(endpoint_multiplier, endpoint),
        mul(square_multiplier, p110_square),
    )
    assert unit == {(): Q(1)}

    witness_records = []
    all_details = row14_details + row15_details
    for index, coefficient in enumerate(square_witness):
        if not coefficient:
            continue
        stage_row = 14 if index < len(row14) else 15
        compatibility_index = index if stage_row == 14 else index - len(row14)
        witness_records.append({
            "combined_compatibility_index": index,
            "stage_row": stage_row,
            "stage_compatibility_index": compatibility_index,
            "coefficient": str(coefficient),
            "compatibility_sha256": hashlib.sha256(
                compact(all_details[index]["terms"])
            ).hexdigest(),
        })

    unit_certificate = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL6-TWO-GENERATOR-UNIT-v1",
        "branch": branch,
        "p110_square_generator": encode(p110_square),
        "p110_square_pre_span_witness": witness_records,
        "source_row_provenance": {
            "interpretation": (
                "Each list is a Q-combination of literal source equations "
                "after the exact substitutions present on entry to that "
                "triangular stage; row 15 therefore also follows the row-14 "
                "constant-pivot substitutions."
            ),
            "row14": combine_source_provenance(
                row14_details, square_witness[:len(row14)]
            ),
            "row15": combine_source_provenance(
                row15_details, square_witness[len(row14):]
            ),
        },
        "endpoint_generator": encode(endpoint),
        "identity": {
            "formula": (
                "1=(1-p32*p110)*(1+p32*p110)+p32^2*(p110^2)"
            ),
            "endpoint_multiplier": encode(endpoint_multiplier),
            "p110_square_multiplier": encode(square_multiplier),
            "exact_expansion": encode(unit),
        },
        "method": "standard-library exact Q arithmetic; no Groebner basis",
        "conclusion": "the localized row14+15 branch target ideal is the unit ideal",
    }
    operative = sorted({variable for poly in constraints
                        for monomial in poly for variable in monomial})

    result = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL6-ROW14-15-LOCALIZED-v2",
        "source_tail6_sha256": SOURCE_SHA256,
        "branch": branch,
        "field_radical_branch": (
            "V0=0" if branch == "v0_zero" else "V0=4*p110"
        ),
        "F6_parameterization": "F6=(X^4-1)^2*(V0+V1*X+V2*X^2)",
        "endpoint_localization": "1+p32*p110=0; neither carrier normalized",
        "triangular_log": [log12, log13, log14, log15],
        "row14_displayed_count": len(row14),
        "row14_span_rank": len(row14_basis),
        "row15_displayed_count": len(row15),
        "row15_span_rank": len(row15_basis),
        "row14_15_cumulative_span_rank": len(cumulative_basis),
        "operative_variables": operative,
        "operative_variable_count": len(operative),
        "constraint_count": len(constraints),
        "maximum_degree": max(len(monomial) for poly in constraints for monomial in poly),
        "constraints": encode_constraints(constraints),
        "unit_certificate": unit_certificate,
        "scope": (
            "unit necessary subsystem of one field-radical cutoff-six "
            "square-tail branch; excludes that branch scheme after the "
            "field-radical parameterization"
        ),
    }
    return result


def dehom_diagnostic(target):
    substitutions = {110: {(): Q(1)}, 32: {(): Q(-1)}}
    polys = [substitute(decode(record["terms"]), substitutions)
             for record in target["constraints"]]
    polys = [poly for poly in polys if poly]
    operative = sorted({variable for poly in polys
                        for monomial in poly for variable in monomial})
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL6-P110-ONE-DIAGNOSTIC-v1",
        "source_branch": target["branch"],
        "specialization": "p110=1,p32=-1",
        "warning": (
            "diagnostic slice only; no whole-stratum scaling or homogeneity theorem is claimed"
        ),
        "operative_variables": operative,
        "operative_variable_count": len(operative),
        "constraint_count": len(polys),
        "constraints": encode_constraints(polys),
        "scope": "non-covering diagnostic specialization",
    }


def compile_analysis():
    assert sha256(SOURCE) == SOURCE_SHA256
    data = json.loads(SOURCE.read_text())
    assert data["authoritative_raw_system_sha256"] == RAW_SHA256
    assert data["cutoff"] == 6
    assert data["linear_last_row"] == 11
    assert data["retained_variable_count"] == 220
    assert data["prefix_generator_count"] == 260
    assert data["prefix_rank"] == 98
    assert data["nullity"] == 122
    assert data["constraint_generator_count"] == 253

    stages = {}
    for parameter, vector in enumerate(data["nullspace_basis"]):
        stages.setdefault(parameter_stage(vector), []).append(parameter)
    assert stages[12] == list(range(57, 73))
    assert stages[13] == list(range(44, 57))
    assert stages[14] == list(range(33, 44))
    assert stages[15] == list(range(24, 33))

    endpoint_record = next(record for record in data["constraints"]
                           if record["row"] == 22 and record["x_degree"] == 0)
    assert endpoint_record["terms"] == [[[], "-1"], [[32, 110], "-1"]]

    substitutions = {}
    row12, log12 = triangular_stage(data, 12, stages[12], substitutions)
    row12_model = row12_remainders()
    assert len(row12) == 16
    assert len(span_basis(row12)[0]) == 8
    assert same_span(row12, row12_model)

    substitutions = a_equals_c_times_b()
    row12_on_b, _ = triangular_stage(data, 12, stages[12], substitutions)
    assert not row12_on_b
    row13, log13 = triangular_stage(data, 13, stages[13], substitutions)
    row13_model = row13_model_remainders()
    extra = row13_extra()
    assert len(row13) == 16
    assert len(span_basis(row13)[0]) == 9
    assert same_span(row13, row13_model + [extra])

    b_to_v = b_equals_c_times_v()
    extra_on_v = substitute(extra, b_to_v)
    expected_extra = {
        (V_VARS[0], V_VARS[0]): Q(1, 4),
        (110, V_VARS[0]): Q(-1),
    }
    assert extra_on_v == expected_extra

    targets = {}
    diagnostics = {}
    for branch in ("v0_zero", "v0_four_p110"):
        target = compile_branch_target(data, stages, branch)
        targets[branch] = target
        diagnostics[branch] = dehom_diagnostic(target)

    summary = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL6-DESK-ANALYSIS-v2",
        "source_tail6_sha256": SOURCE_SHA256,
        "authoritative_raw_system_sha256": RAW_SHA256,
        "tail_compiler_sha256": sha256(TAIL_COMPILER),
        "cutoff": 6,
        "prefix": {
            "retained_variables": 220,
            "generator_count_through_D11": 260,
            "rank": 98,
            "nullity": 122,
        },
        "endpoint_constant": {
            "literal_equation": "D22[X^0]-1=-1-p32*p110",
            "p32": "G15[X^1]",
            "p110": "F7[X^0]",
            "field_consequence": "p32 and p110 are nonzero, p32=-p110^(-1)",
        },
        "row12": {
            **log12,
            "independent_identity": (
                "compatibility row space equals the eight coefficients of "
                "F6(X)^2 modulo H=(X^4-1)^2"
            ),
            "field_radical_consequence": "F6=(X^4-1)*B, deg(B)<=6",
            "model_remainders": [encode(poly) for poly in row12_model],
        },
        "row13": {
            **log13,
            "independent_identity": (
                "after F6=(X^4-1)B, the rank-nine compatibility row space "
                "equals the eight coefficients of B*(4*(X^4-1)*F7-B) "
                "modulo H plus the displayed scalar E"
            ),
            "field_radical_consequence": "B=(X^4-1)*V, deg(V)<=2",
            "extra_E": encode(extra),
            "extra_after_B_equals_CV": encode(extra_on_v),
            "field_branches": ["V0=0", "V0=4*p110"],
            "model_remainders": [encode(poly) for poly in row13_model],
        },
        "localized_targets": targets,
        "field_level_conclusion": (
            "Both row-13 field-radical branches have unit row14+15 endpoint "
            "targets, so the fixed cutoff-six square-tail endpoint system "
            "has no characteristic-zero field-valued point."
        ),
        "dehom_diagnostics": diagnostics,
        "firewalls": [
            "fixed branch-P square baseline and cutoff-six tail only",
            "field-radical reductions do not preserve nonreduced scheme structure",
            "no upstream scheme-unit claim is made across the row12/13 field-radical cover",
            "the two row14+15 branch target ideals are unit by direct identities",
            "p110=1 diagnostics are not covers",
            "D23 is not imposed and G22 is absent",
            "no branch-P family, Keller-pair, counterexample, or JC2 claim",
        ],
    }
    return summary


def build_payloads():
    analysis = compile_analysis()
    payloads = {}
    for branch, target in analysis["localized_targets"].items():
        payloads[f"TARGETS/{branch}_row14_15_localized_q.sing"] = (
            singular_text(target).encode()
        )
        payloads[f"TARGETS/{branch}_row14_15_localized_p65521.sing"] = (
            singular_text(target, 65521).encode()
        )
    for branch, target in analysis["dehom_diagnostics"].items():
        payloads[f"TARGETS/{branch}_p110_one_diagnostic_q.sing"] = (
            singular_text(target).encode()
        )
    analysis["emitted_target_sha256"] = {
        name: hashlib.sha256(payload).hexdigest()
        for name, payload in sorted(payloads.items())
    }
    unit_certificate = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL6-UNIT-CERTIFICATES-v1",
        "source_tail6_sha256": SOURCE_SHA256,
        "authoritative_raw_system_sha256": RAW_SHA256,
        "emitted_target_sha256": analysis["emitted_target_sha256"],
        "certificates": {
            branch: target["unit_certificate"]
            for branch, target in analysis["localized_targets"].items()
        },
        "coverage_scope": (
            "The certificates make each post-row13 field-radical branch "
            "target scheme empty.  Together the two branches exclude all "
            "characteristic-zero field-valued points of the fixed cutoff-six "
            "square-tail endpoint system.  They are not a lifted unit "
            "certificate for the upstream nonreduced row12/13 ideal."
        ),
    }
    unit_payload = pretty(unit_certificate)
    analysis["unit_certificate_sha256"] = hashlib.sha256(unit_payload).hexdigest()
    payloads["UNIT_CERTIFICATE.json"] = unit_payload
    payloads["TAIL6_DESK_ANALYSIS.json"] = pretty(analysis)
    payloads["SOURCE.sha256"] = (
        f"{SOURCE_SHA256}  TAIL6/TAIL_DEFORMATION_SYSTEM.json\n"
        f"{RAW_SHA256}  ../ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json\n"
        f"{sha256(TAIL_COMPILER)}  ../ggv_8_28_upper_endpoint_branch_p_20260827/tail_deformation.py\n"
    ).encode()
    return payloads


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payloads = build_payloads()
    if args.check:
        mismatches = [name for name, payload in payloads.items()
                      if not (args.output / name).is_file()
                      or (args.output / name).read_bytes() != payload]
        assert not mismatches, mismatches
    else:
        for name, payload in payloads.items():
            path = args.output / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
    print(json.dumps({
        "status": "PASS",
        "check": args.check,
        "source_sha256": SOURCE_SHA256,
        "direct_unit_certificate": "PASS_BOTH_ROW13_BRANCHES_NO_GB",
        "payload_sha256": {
            name: hashlib.sha256(payload).hexdigest()
            for name, payload in sorted(payloads.items())
        },
    }, sort_keys=True))


if __name__ == "__main__":
    main()
