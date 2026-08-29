#!/usr/bin/env python3
"""Independent exact compiler and desk analysis for the cutoff-three tail."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
RAW_INPUT = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"
PREREGISTRATION = HERE / "PREREGISTRATION.md"

RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
RAW_INPUT_SHA256 = "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876"

A_CARRIER = 32
C_CARRIER = 86
D_CARRIER = 91
B_CARRIER = 189

# Synthetic coefficients for the independently rederived field-radical
# parameterizations. Their ranges are disjoint from the 256 literal prefix
# coordinates.
TV = tuple(range(3000, 3006))
FW = tuple(range(3100, 3109))
FR = tuple(range(3200, 3205))
FS = tuple(range(3300, 3308))
FQ = tuple(range(3400, 3404))
FU = tuple(range(3500, 3507))
FL = tuple(range(3600, 3603))
FM = tuple(range(3700, 3706))
FN = tuple(range(3800, 3802))
TAU = 3900
Q0_INVERSE = 3901
BBAR_INVERSE = 3902


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def pretty(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


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
            term = mul(term, substitutions.get(variable,
                                                {(variable,): Q(1)}))
        out = add(out, term)
    return out


def compose_substitutions(substitutions, extra):
    out = {variable: substitute(poly, extra)
           for variable, poly in substitutions.items()}
    out.update(extra)
    return out


def encode(poly):
    return [[list(monomial), str(coefficient)]
            for monomial, coefficient in sorted(poly.items())]


def decode(encoded):
    return {tuple(monomial): Q(coefficient)
            for monomial, coefficient in encoded}


def rref(matrix):
    matrix = [[Q(value) for value in row] for row in matrix]
    rank = 0
    pivots = []
    for column in range(len(matrix[0]) if matrix else 0):
        chosen = next((row for row in range(rank, len(matrix))
                       if matrix[row][column]), None)
        if chosen is None:
            continue
        matrix[rank], matrix[chosen] = matrix[chosen], matrix[rank]
        scalar = matrix[rank][column]
        matrix[rank] = [value / scalar for value in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or not matrix[row][column]:
                continue
            scalar = matrix[row][column]
            matrix[row] = [left - scalar * right
                           for left, right in zip(matrix[row], matrix[rank])]
        pivots.append(column)
        rank += 1
        if rank == len(matrix):
            break
    return matrix, pivots


def polynomial_rref(rows, column_count, provenance=False):
    count = len(rows)
    tracked = []
    for index, (coefficients, residual) in enumerate(rows):
        source = [Q(index == j) for j in range(count)] if provenance else None
        tracked.append(([Q(value) for value in coefficients], dict(residual),
                        source))
    rank = 0
    pivots = []
    for column in range(column_count):
        chosen = next((row for row in range(rank, count)
                       if tracked[row][0][column]), None)
        if chosen is None:
            continue
        tracked[rank], tracked[chosen] = tracked[chosen], tracked[rank]
        coefficients, residual, source = tracked[rank]
        scalar = coefficients[column]
        coefficients = [value / scalar for value in coefficients]
        residual = scale(residual, Q(1) / scalar)
        if provenance:
            source = [value / scalar for value in source]
        tracked[rank] = coefficients, residual, source
        for row in range(count):
            if row == rank or not tracked[row][0][column]:
                continue
            scalar = tracked[row][0][column]
            other_coefficients, other_residual, other_source = tracked[row]
            other_coefficients = [left - scalar * right
                                  for left, right in zip(other_coefficients,
                                                        coefficients)]
            other_residual = add(other_residual, scale(residual, -scalar))
            if provenance:
                other_source = [left - scalar * right
                                for left, right in zip(other_source, source)]
            tracked[row] = other_coefficients, other_residual, other_source
        pivots.append(column)
        rank += 1
    return tracked, pivots


def span_basis_with_witness(polys):
    monomials = sorted({monomial for poly in polys for monomial in poly})
    rows = [([poly.get(monomial, Q(0)) for monomial in monomials], {})
            for poly in polys]
    reduced, pivots = polynomial_rref(rows, len(monomials), provenance=True)
    basis = []
    witnesses = []
    for row in range(len(pivots)):
        basis.append({monomial: coefficient
                      for monomial, coefficient
                      in zip(monomials, reduced[row][0]) if coefficient})
        witnesses.append(reduced[row][2])
    return basis, witnesses


def span_basis(polys):
    return span_basis_with_witness(polys)[0]


def linear_combination_witness(polys, target):
    monomials = sorted({monomial for poly in polys + [target]
                        for monomial in poly})
    rows = [([poly.get(monomial, Q(0)) for monomial in monomials], {})
            for poly in polys]
    reduced, pivots = polynomial_rref(rows, len(monomials), provenance=True)
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
    assert not any(vector)
    reconstruction = {}
    for coefficient, poly in zip(witness, polys):
        reconstruction = add(reconstruction, scale(poly, coefficient))
    assert reconstruction == target
    return witness


def sparse_span_witness(polys, target):
    """Return an exact sparse witness, or None, without a dense monomial matrix."""
    basis = {}
    for index, source_poly in enumerate(polys):
        poly = dict(source_poly)
        provenance = {index: Q(1)}
        while poly:
            pivot = min(poly)
            if pivot not in basis:
                scalar = poly[pivot]
                poly = scale(poly, Q(1) / scalar)
                provenance = {key: value / scalar
                              for key, value in provenance.items() if value}
                basis[pivot] = poly, provenance
                break
            scalar = poly[pivot]
            pivot_poly, pivot_provenance = basis[pivot]
            poly = add(poly, scale(pivot_poly, -scalar))
            for key, value in pivot_provenance.items():
                provenance[key] = provenance.get(key, Q(0)) - scalar * value
                if not provenance[key]:
                    del provenance[key]
    remainder = dict(target)
    witness = {}
    while remainder:
        pivot = min(remainder)
        if pivot not in basis:
            return None
        scalar = remainder[pivot]
        pivot_poly, pivot_provenance = basis[pivot]
        remainder = add(remainder, scale(pivot_poly, -scalar))
        for key, value in pivot_provenance.items():
            witness[key] = witness.get(key, Q(0)) + scalar * value
            if not witness[key]:
                del witness[key]
    reconstruction = {}
    for index, coefficient in witness.items():
        reconstruction = add(reconstruction, scale(polys[index], coefficient))
    assert reconstruction == target
    return witness


def same_span(left, right):
    return (len(span_basis(left)) == len(span_basis(right)) ==
            len(span_basis(left + right)))


def span_intersection(polys, allowed):
    forbidden = sorted({monomial for poly in polys for monomial in poly
                        if any(variable not in allowed for variable in monomial)})
    # Sparse forward elimination of the forbidden-coefficient matrix.  The
    # matrix can have many monomial rows but only tens of compatibility
    # columns; keeping it sparse avoids a broad local dense-rational job.
    pivot_rows = {}
    for monomial in forbidden:
        row = {column: poly[monomial]
               for column, poly in enumerate(polys) if monomial in poly}
        while row:
            pivot = min(row)
            if pivot not in pivot_rows:
                scalar = row[pivot]
                row = {column: value / scalar
                       for column, value in row.items() if value / scalar}
                pivot_rows[pivot] = row
                break
            scalar = row[pivot]
            for column, value in pivot_rows[pivot].items():
                row[column] = row.get(column, Q(0)) - scalar * value
                if not row[column]:
                    del row[column]
    pivots = sorted(pivot_rows)
    free = [column for column in range(len(polys))
            if column not in pivot_rows]
    intersection = []
    for free_column in free:
        sparse_vector = {free_column: Q(1)}
        for pivot in reversed(pivots):
            value = -sum(coefficient * sparse_vector.get(column, Q(0))
                         for column, coefficient
                         in pivot_rows[pivot].items() if column != pivot)
            if value:
                sparse_vector[pivot] = value
        poly = {}
        for column, coefficient in sparse_vector.items():
            poly = add(poly, scale(polys[column], coefficient))
        if poly:
            intersection.append(poly)
    return span_basis(intersection)


def dense_mul(left, right):
    out = [{} for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = add(out[i + j], mul(a, b))
    return out


def mod_a(poly):
    out = [{} for _ in range(4)]
    for degree, coefficient in enumerate(poly):
        out[degree % 4] = add(out[degree % 4], coefficient)
    return out


def mod_h(poly):
    poly = [dict(item) for item in poly]
    if len(poly) < 8:
        poly.extend({} for _ in range(8 - len(poly)))
    for degree in range(len(poly) - 1, 7, -1):
        leading = poly[degree]
        poly[degree] = {}
        poly[degree - 4] = add(poly[degree - 4], scale(leading, 2))
        poly[degree - 8] = add(poly[degree - 8], scale(leading, -1))
    return poly[:8]


def span_inclusion(source, targets):
    return [[str(value) for value in linear_combination_witness(source, target)]
            for target in targets]


def a_times_parameter(source_variables, output_degree):
    """Coefficient map for (X^4-1)*source."""
    out = {}
    maximum = len(source_variables) - 1
    for degree in range(output_degree + 1):
        poly = {}
        if 0 <= degree - 4 <= maximum:
            poly[(source_variables[degree - 4],)] = Q(1)
        if 0 <= degree <= maximum:
            poly[(source_variables[degree],)] = (
                poly.get((source_variables[degree],), Q(0)) - 1
            )
        out[degree] = {monomial: coefficient
                       for monomial, coefficient in poly.items() if coefficient}
    return out


def compile_cutoff3():
    assert sha256(RAW) == RAW_SHA256
    assert sha256(RAW_INPUT) == RAW_INPUT_SHA256
    raw = json.loads(RAW.read_text())
    source = json.loads(RAW_INPUT.read_text())
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

    retained = [name for name in raw["variables"] if weight(name) >= 3]
    retained_index = {name: index for index, name in enumerate(retained)}
    prefix_records = [record for record in raw["generators"]
                      if int(record["row"]) <= 5]
    matrix = []
    for record in prefix_records:
        row = [Q(0)] * len(retained)
        for monomial, coefficient in record["terms"]:
            kept = [name for name in monomial if name in retained_index]
            if len(kept) != len(monomial):
                continue
            assert len(kept) == 1
            row[retained_index[kept[0]]] += Q(coefficient)
        matrix.append(row)
    reduced, pivots = rref(matrix)
    free = [column for column in range(len(retained))
            if column not in set(pivots)]
    basis = []
    for free_column in free:
        vector = [Q(0)] * len(retained)
        vector[free_column] = Q(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column]
        assert all(sum(a * b for a, b in zip(source_row, vector)) == 0
                   for source_row in matrix)
        basis.append(vector)
    forms = {}
    for column, name in enumerate(retained):
        forms[name] = {(parameter,): basis[parameter][column]
                       for parameter in range(len(basis))
                       if basis[parameter][column]}
    constraints = []
    for source_index, record in enumerate(raw["generators"]):
        if int(record["row"]) <= 5:
            continue
        poly = {}
        for monomial, coefficient in record["terms"]:
            if any(name not in forms for name in monomial):
                continue
            term = {(): Q(coefficient)}
            for name in monomial:
                term = mul(term, forms[name])
            poly = add(poly, term)
        constraints.append({
            "source_generator_index": source_index,
            "row": int(record["row"]),
            "x_degree": int(record["x_degree"]),
            "terms": encode(poly),
            "sha256": hashlib.sha256(compact(encode(poly))).hexdigest(),
        })
    result = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL3-INDEPENDENT-COMPILE-v1",
        "authoritative_raw_system_sha256": RAW_SHA256,
        "raw_slot_inventory_sha256": RAW_INPUT_SHA256,
        "cutoff": 3,
        "linear_last_row": 5,
        "prefix_generator_count": len(prefix_records),
        "retained_variables": retained,
        "retained_variable_count": len(retained),
        "prefix_rank": len(pivots),
        "nullity": len(basis),
        "nullspace_basis": [[[retained[column], str(value)]
                              for column, value in enumerate(vector) if value]
                             for vector in basis],
        "raw_value_linear_map": {
            name: encode(forms.get(name, {})) for name in raw["variables"]
        },
        "constraints": constraints,
        "constraint_generator_count": len(constraints),
        "D23_imposed": False,
        "G22_present": False,
    }
    assert (len(retained), len(prefix_records), len(pivots), len(basis),
            len(constraints)) == (296, 71, 40, 256, 442)
    endpoint = next(record for record in constraints
                    if record["row"] == 22 and record["x_degree"] == 0)
    assert endpoint["terms"] == [
        [[], "-1"], [[A_CARRIER, B_CARRIER], "-1"],
        [[C_CARRIER, D_CARRIER], "1"],
    ]
    return result


def parameter_stage(vector):
    stages = []
    for name, _coefficient in vector:
        if name.startswith("tt_"):
            stages.append(3)
            continue
        assert not name.startswith("z_")
        kind, x_degree, y_degree = name.split("_")
        offset = 8 if kind == "f" else 12
        stages.append(offset + 3 * int(x_degree) - int(y_degree))
    return min(stages)


def triangular_stage(data, row_number, candidates, substitutions):
    indexed = [(index, record) for index, record in enumerate(data["constraints"])
               if int(record["row"]) == row_number]
    original = [substitute(decode(record["terms"]), substitutions)
                for _index, record in indexed]
    rows = []
    for poly in original:
        coefficients = [Q(0)] * len(candidates)
        residual = {}
        for monomial, coefficient in poly.items():
            hits = [variable for variable in monomial if variable in candidates]
            if hits:
                assert len(hits) == 1 and monomial == (hits[0],)
                coefficients[candidates.index(hits[0])] += coefficient
            else:
                residual[monomial] = coefficient
        rows.append((coefficients, residual))
    reduced, pivots = polynomial_rref(rows, len(candidates), provenance=True)
    free = [column for column in range(len(candidates))
            if column not in set(pivots)]
    for pivot_row, pivot_column in enumerate(pivots):
        coefficients, residual, _source = reduced[pivot_row]
        solution = scale(residual, -1)
        for free_column in free:
            if coefficients[free_column]:
                solution = add(solution, {
                    (candidates[free_column],): -coefficients[free_column]
                })
        substitutions[candidates[pivot_column]] = solution
    compatibility = []
    details = []
    for coefficients, residual, source_vector in reduced[len(pivots):]:
        assert not any(coefficients)
        if not residual:
            continue
        reconstructed = {}
        source_rows = []
        for local_index, coefficient in enumerate(source_vector):
            if not coefficient:
                continue
            reconstructed = add(reconstructed,
                                scale(original[local_index], coefficient))
            global_index, record = indexed[local_index]
            source_rows.append({
                "constraint_index": global_index,
                "source_generator_index": record["source_generator_index"],
                "row": row_number,
                "x_degree": int(record["x_degree"]),
                "coefficient": str(coefficient),
            })
        assert reconstructed == residual
        compatibility.append(residual)
        details.append({
            "terms": encode(residual),
            "source_row_combination_after_stage_entry_substitutions": source_rows,
        })
    return compatibility, {
        "row": row_number,
        "equation_count": len(indexed),
        "candidate_count": len(candidates),
        "rank": len(pivots),
        "free_parameters": [candidates[column] for column in free],
        "displayed_compatibility_count": len(compatibility),
        "compatibility_span_rank": len(span_basis(compatibility)),
    }, details


def compile_analysis(data):
    stages = {}
    for parameter, vector in enumerate(data["nullspace_basis"]):
        stages.setdefault(parameter_stage(vector), []).append(parameter)
    expected_counts = {3: 10, 4: 14, 5: 12, 6: 30, 7: 28, 8: 26,
                       9: 23, 10: 21, 11: 19, 12: 16, 13: 13, 14: 11,
                       15: 9, 16: 7, 17: 6, 18: 5, 19: 3, 20: 2, 21: 1}
    assert {stage: len(parameters) for stage, parameters in stages.items()} == expected_counts
    substitutions = {}

    # D6 is automatically compatible. The retained weight-three polynomial
    # is T=sum(tt_i X^i), with tt_i=p(255-i).
    row6, row6_log, row6_details = triangular_stage(
        data, 6, stages[6], substitutions
    )
    assert not row6
    t_poly = [{(255 - degree,): Q(1)} for degree in range(10)]

    # D7 contains T^2 mod A. Since A is squarefree, every field point has
    # T=A*V, deg(V)<=5. All D7 compatibilities vanish on that parameterization.
    row7, row7_log, row7_details = triangular_stage(
        data, 7, [parameter for parameter in stages[7]
                  if parameter != B_CARRIER], substitutions
    )
    row7_model = mod_a(dense_mul(t_poly, t_poly))
    row7_model_witness = span_inclusion(row7, row7_model)
    t_to_v = {
        255 - degree: poly
        for degree, poly in a_times_parameter(TV, 9).items()
    }
    substitutions = compose_substitutions(substitutions, t_to_v)
    assert not [substitute(poly, t_to_v) for poly in row7
                if substitute(poly, t_to_v)]

    # D8 contains (F4-V/16)^2 mod A. Parameterize F4=V/16+A*W.
    row8, row8_log, row8_details = triangular_stage(
        data, 8, stages[8], substitutions
    )
    f4_minus_v = []
    for degree in range(13):
        poly = {(245 - degree,): Q(1)}
        if degree < len(TV):
            poly[(TV[degree],)] = Q(-1, 16)
        f4_minus_v.append(poly)
    row8_model = mod_a(dense_mul(f4_minus_v, f4_minus_v))
    row8_model_witness = span_inclusion(row8, row8_model)
    f4_to_w = {}
    a_w = a_times_parameter(FW, 12)
    for degree in range(13):
        poly = dict(a_w[degree])
        if degree < len(TV):
            poly = add(poly, {(TV[degree],): Q(1, 16)})
        f4_to_w[245 - degree] = poly
    substitutions = compose_substitutions(substitutions, f4_to_w)
    row8_on_w = [substitute(poly, f4_to_w) for poly in row8]
    row8_on_w = [poly for poly in row8_on_w if poly]
    row8_on_w_basis = span_basis(row8_on_w)
    assert len(row8_on_w_basis) == 1
    e8 = {
        (208,): Q(1), (219,): Q(-3, 2), (231,): Q(-3, 4),
        (232,): Q(-1, 4), (TV[0],): Q(3, 64),
        (TV[0], TV[0]): Q(-3, 512), (FW[0],): Q(-3, 8),
    }
    assert row8_on_w_basis == [e8]
    # Exact monic elimination of noncarrier p232; no localization.
    p232_solution = scale(add(e8, {(232,): Q(1, 4)}), 4)
    substitutions = compose_substitutions(substitutions, {232: p232_solution})

    # D9 contains W^2 mod A, hence W=A*R on field points. All other D9
    # compatibilities vanish after this parameterization.
    row9, row9_log, row9_details = triangular_stage(
        data, 9, stages[9], substitutions
    )
    w_poly = [{(variable,): Q(1)} for variable in FW]
    row9_model = mod_a(dense_mul(w_poly, w_poly))
    row9_model_witness = span_inclusion(row9, row9_model)
    w_to_r = {FW[degree]: poly
              for degree, poly in a_times_parameter(FR, 8).items()}
    substitutions = compose_substitutions(substitutions, w_to_r)
    assert not [substitute(poly, w_to_r) for poly in row9
                if substitute(poly, w_to_r)]

    # D10 contains (F5-R/2)^2 mod A, hence F5=R/2+A*S.
    row10, row10_log, row10_details = triangular_stage(
        data, 10, stages[10], substitutions
    )
    f5_minus_r = []
    for degree in range(12):
        poly = {(231 - degree,): Q(1)}
        if degree < len(FR):
            poly[(FR[degree],)] = Q(-1, 2)
        f5_minus_r.append(poly)
    row10_model = mod_a(dense_mul(f5_minus_r, f5_minus_r))
    row10_model_witness = span_inclusion(row10, row10_model)
    f5_to_s = {}
    a_s = a_times_parameter(FS, 11)
    for degree in range(12):
        poly = dict(a_s[degree])
        if degree < len(FR):
            poly = add(poly, {(FR[degree],): Q(1, 2)})
        f5_to_s[231 - degree] = poly
    substitutions = compose_substitutions(substitutions, f5_to_s)
    assert not [substitute(poly, f5_to_s) for poly in row10
                if substitute(poly, f5_to_s)]

    # D11 is compiled with both literal endpoint carriers c,d protected. Its
    # radical structure is analyzed below without selecting a carrier chart.
    row11, row11_log, row11_details = triangular_stage(
        data, 11, [parameter for parameter in stages[11]
                   if parameter not in (C_CARRIER, D_CARRIER)], substitutions
    )
    s_poly = [{(variable,): Q(1)} for variable in FS]
    row11_model = mod_a(dense_mul(s_poly, s_poly))
    row11_model_witness = span_inclusion(row11, row11_model)
    s_to_q = {FS[degree]: poly
              for degree, poly in a_times_parameter(FQ, 7).items()}
    row11_on_q = [substitute(poly, s_to_q) for poly in row11]
    row11_on_q = [poly for poly in row11_on_q if poly]
    row11_on_q_basis = span_basis(row11_on_q)
    assert len(row11_on_q_basis) == 2
    c_relation = next(poly for poly in row11_on_q_basis
                      if poly.get((C_CARRIER,)) == 1)
    p106_relation = next(poly for poly in row11_on_q_basis
                         if poly.get((106,)) == 1)
    c_formula = scale(add(c_relation, {(C_CARRIER,): Q(-1)}), -1)
    p106_formula = scale(add(p106_relation, {(106,): Q(-1)}), -1)
    substitutions = compose_substitutions(substitutions, s_to_q)
    substitutions = compose_substitutions(substitutions, {
        C_CARRIER: c_formula,
        106: p106_formula,
    })

    # Square-root prediction for D12, tested against literal compatibilities
    # before promoting any further radical step.
    row12, row12_log, row12_details = triangular_stage(
        data, 12, stages[12], substitutions
    )
    f6_minus_predicted = []
    v_square = dense_mul([{(variable,): Q(1)} for variable in TV],
                         [{(variable,): Q(1)} for variable in TV])
    for degree in range(11):
        poly = {(219 - degree,): Q(1)}
        if degree < len(FQ):
            poly[(FQ[degree],)] = Q(-1, 2)
        if degree < len(v_square):
            poly = add(poly, scale(v_square[degree], Q(-1, 256)))
        f6_minus_predicted.append(poly)
    row12_predicted_mod_a = mod_a(dense_mul(f6_minus_predicted,
                                            f6_minus_predicted))
    row12_predicted_membership = [
        len(span_basis(row12 + [poly])) == len(span_basis(row12))
        for poly in row12_predicted_mod_a
    ]
    assert all(row12_predicted_membership)
    row12_model_witness = span_inclusion(row12,
                                         row12_predicted_mod_a)
    f6_to_u = {}
    a_u = a_times_parameter(FU, 10)
    for degree in range(11):
        poly = dict(a_u[degree])
        if degree < len(FQ):
            poly = add(poly, {(FQ[degree],): Q(1, 2)})
        if degree < len(v_square):
            poly = add(poly, scale(v_square[degree], Q(1, 256)))
        f6_to_u[219 - degree] = poly
    row12_on_u = [substitute(poly, f6_to_u) for poly in row12]
    row12_on_u = [poly for poly in row12_on_u if poly]
    row12_on_u_basis = span_basis(row12_on_u)
    assert not row12_on_u_basis
    substitutions = compose_substitutions(substitutions, f6_to_u)

    row13, row13_log, row13_details = triangular_stage(
        data, 13, stages[13], substitutions
    )
    u_poly = [{(variable,): Q(1)} for variable in FU]
    row13_model = mod_a(dense_mul(u_poly, u_poly))
    row13_model_witness = span_inclusion(row13, row13_model)
    u_to_l = {FU[degree]: poly
              for degree, poly in a_times_parameter(FL, 6).items()}
    row13_on_l = [substitute(poly, u_to_l) for poly in row13]
    row13_on_l = [poly for poly in row13_on_l if poly]
    row13_on_l_basis = span_basis(row13_on_l)
    assert len(row13_on_l_basis) == 1

    # Corrected scalar coordinates expose an exact copy of the tail core,
    # but are derived here directly from the literal cutoff-three rows.
    v0 = {(TV[0],): Q(1)}
    r0 = {(FR[0],): Q(1)}
    q0 = {(FQ[0],): Q(1)}
    l0 = {(FL[0],): Q(1)}
    b_literal = {(B_CARRIER,): Q(1)}
    e_literal = {(152,): Q(1)}
    g6_constant = {(208,): Q(1)}
    b_bar = add(b_literal, scale(mul(v0, r0), Q(-1, 16)))
    e_bar = e_literal
    for term in (
        scale(mul(g6_constant, v0), Q(-1, 4)),
        scale(mul(g6_constant, r0), -4),
        scale(mul(mul(v0, v0), v0), Q(3, 1024)),
        scale(mul(mul(v0, v0), r0), Q(3, 64)),
        scale(mul(v0, q0), Q(15, 64)),
        scale(mul(v0, l0), Q(3, 8)),
        scale(mul(r0, r0), Q(3, 4)),
        scale(mul(r0, q0), 6),
        scale(mul(r0, l0), 6),
    ):
        e_bar = add(e_bar, term)
    e13_core = add(
        add(mul(e_bar, q0), scale(mul(b_bar, q0), Q(-3, 4))),
        add(scale(mul(b_bar, l0), Q(3, 2)),
            scale(mul(l0, l0), Q(-3, 8))),
    )
    assert row13_on_l_basis == [e13_core]
    substitutions = compose_substitutions(substitutions, u_to_l)

    # D14 square prediction for the corrected F7 coefficient.
    row14, row14_log, row14_details = triangular_stage(
        data, 14, stages[14], substitutions
    )
    v_times_r = dense_mul([{(variable,): Q(1)} for variable in TV],
                          [{(variable,): Q(1)} for variable in FR])
    f7_minus_predicted = []
    for degree in range(10):
        poly = {(B_CARRIER - degree,): Q(1)}
        if degree < len(FL):
            poly[(FL[degree],)] = Q(-1, 2)
        if degree < len(v_times_r):
            poly = add(poly, scale(v_times_r[degree], Q(-1, 16)))
        f7_minus_predicted.append(poly)
    row14_model = mod_a(dense_mul(f7_minus_predicted,
                                  f7_minus_predicted))
    row14_membership = [
        len(span_basis(row14 + [poly])) == len(span_basis(row14))
        for poly in row14_model
    ]
    assert all(row14_membership)
    row14_model_witness = span_inclusion(row14, row14_model)

    def m_form(degree):
        if degree == 0:
            return add(add(scale(l0, Q(1, 2)),
                           scale(mul(v0, r0), Q(1, 16))),
                       scale(b_literal, -1))
        if 1 <= degree < len(FM):
            return {(FM[degree],): Q(1)}
        return {}

    f7_to_m = {}
    for degree in range(1, 10):
        poly = {}
        if degree < len(FL):
            poly = add(poly, {(FL[degree],): Q(1, 2)})
        if degree < len(v_times_r):
            poly = add(poly, scale(v_times_r[degree], Q(1, 16)))
        if 0 <= degree - 4 < len(FM):
            poly = add(poly, m_form(degree - 4))
        if degree < len(FM):
            poly = add(poly, scale(m_form(degree), -1))
        f7_to_m[B_CARRIER - degree] = poly
    substitutions = compose_substitutions(substitutions, f7_to_m)
    row14_on_m = [substitute(poly, f7_to_m) for poly in row14]
    row14_on_m = [poly for poly in row14_on_m if poly]
    row14_on_m_basis = span_basis(row14_on_m)
    e14_core = add(
        add(mul(e_bar, l0), scale(mul(b_bar, b_bar), Q(3, 4))),
        add(scale(mul(b_bar, l0), Q(-3, 2)),
            scale(mul(l0, l0), Q(3, 16))),
    )
    assert len(row14_on_m_basis) == 2
    assert row14_on_m_basis[0] == e13_core
    e14_actual = row14_on_m_basis[1]
    e14_shift_residual = add(e14_actual, scale(e14_core, -1))
    assert e14_shift_residual == {
        tuple(sorted((TV[0], FQ[0], FL[0]))): Q(-3, 64),
        tuple(sorted((FR[0], FQ[0], FQ[0]))): Q(-3, 8),
    }

    row15, row15_log, row15_details = triangular_stage(
        data, 15, [parameter for parameter in stages[15]
                   if parameter != A_CARRIER], substitutions
    )
    cumulative_d14_d15 = row14_on_m + row15
    m_poly = [m_form(degree) for degree in range(6)]
    row15_model = mod_a(dense_mul(m_poly, m_poly))
    row15_model_witness = span_inclusion(cumulative_d14_d15,
                                         row15_model)
    n0 = add(b_bar, scale(l0, Q(-1, 2)))
    m_to_n = {
        FM[1]: {(FN[1],): Q(-1)},
        FM[2]: {},
        FM[3]: {},
        FM[4]: n0,
        FM[5]: {(FN[1],): Q(1)},
    }
    substitutions = compose_substitutions(substitutions, m_to_n)
    post_d15 = [substitute(poly, m_to_n)
                for poly in cumulative_d14_d15]
    post_d15 = [poly for poly in post_d15 if poly]
    post_d15_basis = span_basis(post_d15)
    assert len(post_d15_basis) == 4
    assert post_d15_basis[2] == e13_core
    assert post_d15_basis[3] == e14_actual
    e15_actual = post_d15_basis[1]
    e15_tail5_form = add(
        add(mul(e_bar, b_bar), scale(mul(b_bar, b_bar), Q(-3, 4))),
        scale(mul(mul(q0, q0), q0), Q(-1, 8)),
    )
    e15_shift_residual = add(e15_actual, scale(e15_tail5_form, -1))

    # The F8 constant is the same exact additive determinant gauge encountered
    # independently at larger cutoffs. Verify absence rather than assume it.
    assert all(161 not in monomial
               for record in data["constraints"]
               for monomial, _coefficient in record["terms"])
    substitutions = compose_substitutions(substitutions, {161: {}})

    row16, row16_log, row16_details = triangular_stage(
        data, 16, stages[16], substitutions
    )
    row17, row17_log, row17_details = triangular_stage(
        data, 17, stages[17], substitutions
    )
    through_d17 = post_d15 + row16 + row17
    core_allowed = {B_CARRIER, 152, 208, TV[0], FR[0], FQ[0], FL[0]}
    d17_core = span_intersection(through_d17, core_allowed)

    row18, row18_log, row18_details = triangular_stage(
        data, 18, stages[18], substitutions
    )
    through_d18 = through_d17 + row18
    d18_core = span_intersection(through_d18, core_allowed)
    row19, row19_log, row19_details = triangular_stage(
        data, 19, stages[19], substitutions
    )
    row20, row20_log, row20_details = triangular_stage(
        data, 20, stages[20], substitutions
    )
    row21, row21_log, row21_details = triangular_stage(
        data, 21, stages[21], substitutions
    )
    row22, row22_log, row22_details = triangular_stage(
        data, 22, [], substitutions
    )
    zero_rows_through_d21 = through_d18 + row19 + row20 + row21
    v_only_by_row = {}
    cumulative = list(post_d15)
    for row_number, polys in ((16, row16), (17, row17), (18, row18),
                              (19, row19), (20, row20), (21, row21)):
        cumulative.extend(polys)
        v_only_by_row[f"D{row_number}"] = span_intersection(cumulative,
                                                             set(TV))
    root_allowed = set(TV + FR + FQ + FL) | {B_CARRIER, 152, 208}
    root_core_d21 = span_intersection(zero_rows_through_d21, root_allowed)

    # Quotient the later root core by the degree-one ideal module generated by
    # E13,E14,E15. This isolates one genuinely new invariant, rather than the
    # many displayed polynomial multiples of the old core.
    old_core = [e13_core, e14_actual, e15_actual]
    module_polys = list(old_core)
    module_labels = ["E13", "E14", "E15"]
    for core_name, core_poly in zip(("E13", "E14", "E15"), old_core):
        for variable in sorted(root_allowed):
            module_polys.append(mul(core_poly, {(variable,): Q(1)}))
            module_labels.append(f"p{variable}*{core_name}")
    corrected_k = mul(q0, add(mul(b_bar, q0), mul(l0, l0)))
    module_rank = len(span_basis(module_polys))
    module_plus_root_rank = len(span_basis(module_polys + root_core_d21))
    module_plus_k_rank = len(span_basis(module_polys + [corrected_k]))
    assert (module_rank, module_plus_root_rank, module_plus_k_rank) == (
        66, 67, 67
    )
    # Live sign mutation: changing the L0^2 sign is not the quotient class
    # supplied by the literal rows.
    mutated_k = mul(q0, add(mul(b_bar, q0), scale(mul(l0, l0), -1)))
    assert len(span_basis(module_polys + root_core_d21 + [mutated_k])) == 68
    cumulative_records = [
        {"row": "D14_D15", "compatibility_index": index, "poly": poly}
        for index, poly in enumerate(post_d15)
    ]
    k_membership_by_row = {}
    earliest_k_witness = None
    for row_number, polys in ((16, row16), (17, row17), (18, row18),
                              (19, row19), (20, row20), (21, row21)):
        cumulative_records.extend({
            "row": f"D{row_number}", "compatibility_index": index,
            "poly": poly,
        } for index, poly in enumerate(polys))
        source = module_polys + [record["poly"] for record in cumulative_records]
        witness = sparse_span_witness(source, corrected_k)
        k_membership_by_row[f"D{row_number}"] = witness is not None
        if witness is not None and earliest_k_witness is None:
            entries = []
            for index, coefficient in sorted(witness.items()):
                if index < len(module_polys):
                    entries.append({"kind": "old_core_module",
                                    "label": module_labels[index],
                                    "coefficient": str(coefficient)})
                else:
                    record = cumulative_records[index - len(module_polys)]
                    entries.append({
                        "kind": "literal_staged_compatibility",
                        "row": record["row"],
                        "compatibility_index": record["compatibility_index"],
                        "coefficient": str(coefficient),
                    })
            earliest_k_witness = {"first_row": f"D{row_number}",
                                  "entries": entries}
    assert earliest_k_witness is not None

    # Preserve the literal endpoint carriers in the AWS successor.  All
    # other coordinates remain in the exact monic/radical coordinate system
    # above.  Replacing the already-substituted D22[X0] row by the pair
    # c=c_formula and -1-a*b+c*d=0 is ideal-theoretically equivalent and
    # keeps a,b,c,d inspectable; no carrier is normalized.
    final_c_formula = substitutions[C_CARRIER]
    c_preserved_relation = add({(C_CARRIER,): Q(1)},
                               scale(final_c_formula, -1))
    literal_endpoint = {
        (): Q(-1),
        tuple(sorted((A_CARRIER, B_CARRIER))): Q(-1),
        tuple(sorted((C_CARRIER, D_CARRIER))): Q(1),
    }
    endpoint_after_c_elimination = substitute(
        literal_endpoint, {C_CARRIER: final_c_formula}
    )
    assert row22[0] == endpoint_after_c_elimination
    d22_nonendpoint = row22[1:]

    stage_bases = {
        "D14_D15": post_d15_basis,
        "D16": span_basis(row16),
        "D17": span_basis(row17),
        "D18": span_basis(row18),
        "D19": span_basis(row19),
        "D20": span_basis(row20),
        "D21": span_basis(row21),
    }
    full_prefix = [poly for row in stage_bases.values() for poly in row]
    target_core = (root_core_d21 + [c_preserved_relation, literal_endpoint]
                   + d22_nonendpoint)
    target_full = (full_prefix + [c_preserved_relation, literal_endpoint]
                   + d22_nonendpoint)
    target_variables = sorted({variable for poly in target_full + target_core
                               for monomial in poly for variable in monomial})
    assert all(variable in target_variables
               for variable in (A_CARRIER, B_CARRIER, C_CARRIER, D_CARRIER))
    assert all(variable in target_variables for variable in TV)
    assert (len(d22_nonendpoint), len(target_variables)) == (17, 56)

    # A staged root-core diagnostic precedes the 56-variable D22 run.  It is
    # deliberately kept separate from the endpoint target.  The three field
    # branches cover K=Q0*(b_bar*Q0+L0^2): Q0=0 with the exact E13 factor
    # L0*(4*b_bar-L0), and Q0!=0 with tau=L0/Q0.  These are additions to the
    # literal 17-polynomial root ideal, never replacements for it.
    tau = {(TAU,): Q(1)}
    q0_inverse = {(Q0_INVERSE,): Q(1)}
    bbar_inverse = {(BBAR_INVERSE,): Q(1)}
    q0_branch_l0 = [q0, l0, b_bar]
    q0_branch_4b_minus_l = [
        q0,
        add(l0, scale(b_bar, -4)),
        add(mul(bbar_inverse, b_bar), {(): Q(-1)}),
        add(e_bar, scale(b_bar, Q(-9, 16))),
        add(v0, {(): Q(1, 4)}),
    ]
    qnonzero_b = add(b_bar, mul(mul(tau, tau), q0))
    desired_e = scale(mul(mul(q0, mul(tau, tau)),
                          add(scale(tau, 4), {(): Q(-1)})), Q(3, 8))
    qnonzero_e = add(e_bar, scale(desired_e, -1))
    tau2 = mul(tau, tau)
    tau4 = mul(tau2, tau2)
    tau5 = mul(tau4, tau)
    qnonzero_e14 = add(
        add(scale(mul(tau2,
                      add(scale(tau2, 12), add(scale(tau, 6), {(): Q(1)}))), 4),
            scale(mul(v0, tau), -1)),
        scale(r0, -8),
    )
    qnonzero_e15 = add(
        add(scale(q0, 2), add(scale(tau5, 24), scale(tau4, 6))),
        scale(mul(r0, add({(): Q(1)}, scale(tau, 4))), 3),
    )
    qnonzero_branch = [
        add(mul(q0_inverse, q0), {(): Q(-1)}),
        add(l0, scale(mul(tau, q0), -1)),
        qnonzero_b,
        qnonzero_e,
        qnonzero_e14,
        qnonzero_e15,
    ]
    # Direct exact regression of the two simplified equations: after the
    # b_bar/e_bar/tau substitutions, actual E14 and E15 are respectively
    # (3/64)Q0^2 times the displayed E14 expression and
    # -(1/16)Q0^2 times the displayed E15 expression.
    qnonzero_substitutions = {
        FL[0]: mul(tau, q0),
        B_CARRIER: add(scale(mul(v0, r0), Q(1, 16)),
                       scale(mul(tau2, q0), -1)),
    }
    e_without_literal = add(e_bar, scale(e_literal, -1))
    qnonzero_substitutions[152] = add(
        desired_e, scale(substitute(e_without_literal,
                                    qnonzero_substitutions), -1)
    )
    assert not substitute(corrected_k, qnonzero_substitutions)
    assert not substitute(e13_core, qnonzero_substitutions)
    assert substitute(e14_actual, qnonzero_substitutions) == scale(
        mul(mul(q0, q0), qnonzero_e14), Q(3, 64)
    )
    assert substitute(e15_actual, qnonzero_substitutions) == scale(
        mul(mul(q0, q0), qnonzero_e15), Q(-1, 16)
    )
    q0_l0_substitutions = {
        FQ[0]: {}, FL[0]: {},
        B_CARRIER: scale(mul(v0, r0), Q(1, 16)),
    }
    assert not substitute(e13_core, q0_l0_substitutions)
    assert not substitute(e14_actual, q0_l0_substitutions)
    assert not substitute(e15_actual, q0_l0_substitutions)
    x_minus_quarter = {(): Q(-1, 4)}
    b_rankone = substitute(b_bar, {TV[0]: x_minus_quarter})
    q0_rankone_substitutions = {
        FQ[0]: {}, TV[0]: x_minus_quarter,
        FL[0]: scale(b_rankone, 4),
    }
    e_rankone = scale(b_rankone, Q(9, 16))
    e_rest_rankone = substitute(add(e_bar, scale(e_literal, -1)),
                                q0_rankone_substitutions)
    q0_rankone_substitutions[152] = add(e_rankone,
                                        scale(e_rest_rankone, -1))
    assert not substitute(e13_core, q0_rankone_substitutions)
    assert not substitute(e14_actual, q0_rankone_substitutions)
    assert not substitute(e15_actual, q0_rankone_substitutions)

    aws_target = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL3-VNONZERO-D22-AWS-TARGET-v1",
        "authoritative_raw_system_sha256": RAW_SHA256,
        "raw_slot_inventory_sha256": RAW_INPUT_SHA256,
        "source_tail_compile_sha256": hashlib.sha256(pretty(data)).hexdigest(),
        "producer_script_sha256": sha256(Path(__file__)),
        "semantics": (
            "field-valued necessary subsystem after independently verified "
            "squarefree radical parameterizations; core-unit is sufficient "
            "for emptiness, core-nonunit is inconclusive"
        ),
        "variable_ids": target_variables,
        "variable_names": {str(variable): f"p{variable}"
                           for variable in target_variables},
        "synthetic_branch_variable_names": {
            str(TAU): "tau", str(Q0_INVERSE): "q0inv",
            str(BBAR_INVERSE): "bbarinv",
        },
        "endpoint_carriers": {
            "a": A_CARRIER, "b": B_CARRIER,
            "c": C_CARRIER, "d": D_CARRIER,
        },
        "nonzero_cover": {
            "polynomial": "V",
            "coefficient_ids": list(TV),
            "charts": [
                {"chart": index, "localized_variable": TV[index],
                 "equation": f"u*p{TV[index]}-1"}
                for index in range(len(TV))
            ],
            "coverage": "V!=0 iff at least one V_i!=0",
            "normalization": "none; u*V_i-1 is localization only",
        },
        "aws_execution_custody": {
            "exact_host_chart_pairs": {
                "i-02cb2b4a379ffcc64": [0, 1],
                "i-040b7a1c2ed72d4cc": [2, 3],
                "i-07eeaf8ba6f0bc419": [4, 5],
            },
            "exact_all_mode": "forbidden",
            "coverage_complete_only_after": "validated disjoint union 0..5",
            "singular_sha256": (
                "90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4"
            ),
            "live_mem_available_floor_gib": 150,
            "live_disk_available_floor_gib": 50,
            "swap": "must remain unconfigured and unused",
        },
        "groups": {
            "old_core": [encode(poly) for poly in old_core],
            "new_D17_invariant": [encode(corrected_k)],
            "D21_root_core": [encode(poly) for poly in root_core_d21],
            "D16_D21_full_stage_bases": {
                row: [encode(poly) for poly in polys]
                for row, polys in stage_bases.items()
            },
            "c_preserved_relation": [encode(c_preserved_relation)],
            "literal_endpoint": [encode(literal_endpoint)],
            "D22_nonendpoint": [encode(poly) for poly in d22_nonendpoint],
        },
        "scopes": {
            "root": [encode(poly) for poly in root_core_d21],
            "core": [encode(poly) for poly in target_core],
            "full": [encode(poly) for poly in target_full],
        },
        "root_branches": {
            "q0_l0": [encode(poly) for poly in q0_branch_l0],
            "q0_4b_minus_l": [encode(poly)
                               for poly in q0_branch_4b_minus_l],
            "qnonzero_simplified": [encode(poly)
                                     for poly in qnonzero_branch],
        },
        "root_branch_semantics": {
            "q0_l0": "Q0=0, L0=0, and field-radical consequence b_bar=0",
            "q0_4b_minus_l": (
                "Q0=0, L0=4*b_bar, b_bar inverted, "
                "e_bar=9*b_bar/16, V0=-1/4"
            ),
            "qnonzero_simplified": (
                "Q0 inverted, tau=L0/Q0, plus exact consequences solving "
                "b_bar/e_bar and the verified E14/E15 scalar equations"
            ),
            "endpoint_status": "not included; diagnostic only",
        },
        "census": {
            "operative_variable_count_before_chart_inverse": len(target_variables),
            "D22_nonendpoint_polynomial_count": len(d22_nonendpoint),
            "D22_nonendpoint_term_count": sum(len(poly)
                                               for poly in d22_nonendpoint),
            "core_generator_count_before_localization": len(target_core),
            "core_term_count_before_localization": sum(len(poly)
                                                       for poly in target_core),
            "full_generator_count_before_localization": len(target_full),
            "full_term_count_before_localization": sum(len(poly)
                                                       for poly in target_full),
            "stage_basis_counts": {row: len(polys)
                                   for row, polys in stage_bases.items()},
        },
        "firewalls": [
            "each of six localization charts must be retained",
            "modular output is reconnaissance only",
            "a nonunit or timeout is not evidence",
            "exact-Q replay is required for every empty chart used",
            "no endpoint carrier is set to one or divided out",
            "core scope is a necessary subsystem: unit proves emptiness; "
            "nonunit does not prove existence",
            "external five-mode/full-fixture reductions are not imported; "
            "literal forced coefficients c14,c16,c18,c20 remain in the "
            "authoritative staged D-row input",
            "exact AWS runs require host-pinned ordered chart pairs; no "
            "single exact artifact covers V!=0",
        ],
    }

    raw_lifts = {
        f"p{parameter}": data["nullspace_basis"][parameter]
        for parameter in (A_CARRIER, B_CARRIER, C_CARRIER, D_CARRIER)
    }
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL3-DESK-ANALYSIS-PRELIMINARY-v2",
        "source_tail_compile_sha256": hashlib.sha256(pretty(data)).hexdigest(),
        "prefix": {
            "retained_variables": 296,
            "generator_count_through_D5": 71,
            "rank": 40,
            "nullity": 256,
            "remaining_D6_through_D22_generators": 442,
        },
        "literal_endpoint": {
            "equation": "D22[X^0]-1=-1-p32*p189+p86*p91",
            "determinant_form": "1+p32*p189-p86*p91=0",
            "individual_unit_conclusion": "none",
        },
        "raw_endpoint_lifts": raw_lifts,
        "stage_parameter_counts": {str(stage): len(parameters)
                                   for stage, parameters in stages.items()},
        "stage_logs": [row6_log, row7_log, row8_log, row9_log, row10_log,
                       row11_log, row12_log, row13_log, row14_log, row15_log,
                       row16_log, row17_log, row18_log, row19_log, row20_log,
                       row21_log, row22_log],
        "field_radical_cascade": [
            "D6: automatically compatible",
            "D7: A divides T^2, hence T=A*V",
            "D8: A divides (F4-V/16)^2, hence F4=V/16+A*W",
            "D9: A divides W^2, hence W=A*R",
            "D10: A divides (F5-R/2)^2, hence F5=R/2+A*S",
            "D11 test: A divides S^2, hence S=A*Q",
            "D12: A divides (F6-Q/2-V^2/256)^2, hence that remainder=A*U",
            "D13: A divides U^2, hence U=A*L",
            "D14-D15: A divides the corrected F7 remainder squared, hence M=A*N",
        ],
        "branch_routing": {
            "identity": "T=A*V with A=X^4-1 nonzero",
            "exact_zero_equivalence": "T=0 iff V0=...=V5=0",
            "T_zero_branch": (
                "identifies exactly with cutoff four; any inherited cutoff-four "
                "closure remains external and review-dependent"
            ),
            "new_branch": "V polynomial nonzero, covered by six localizations",
        },
        "structural_certificates": {
            "D7_T_square_mod_A": {
                "model": [encode(poly) for poly in row7_model],
                "source_witness": row7_model_witness,
                "all_compatibilities_vanish_after_T_equals_AV": True,
            },
            "D8_F4_minus_V_over_16_square_mod_A": {
                "model": [encode(poly) for poly in row8_model],
                "source_witness": row8_model_witness,
                "residual_E8": encode(e8),
                "p232_monic_solution": encode(p232_solution),
            },
            "D9_W_square_mod_A": {
                "model": [encode(poly) for poly in row9_model],
                "source_witness": row9_model_witness,
                "all_compatibilities_vanish_after_W_equals_AR": True,
            },
            "D10_F5_minus_R_over_2_square_mod_A": {
                "model": [encode(poly) for poly in row10_model],
                "source_witness": row10_model_witness,
                "all_compatibilities_vanish_after_F5_parameterization": True,
            },
            "D11_S_square_mod_A": {
                "model": [encode(poly) for poly in row11_model],
                "source_witness": row11_model_witness,
                "post_S_equals_AQ_basis": [encode(poly)
                                           for poly in row11_on_q_basis],
            },
            "D11_endpoint_carrier_formula": {
                "c_relation": encode(c_relation),
                "c_formula": encode(c_formula),
                "p106_relation": encode(p106_relation),
                "p106_formula": encode(p106_formula),
            },
            "D12_square_root_prediction_diagnostic": {
                "model": [encode(poly) for poly in row12_predicted_mod_a],
                "coefficient_membership": row12_predicted_membership,
                "row_span_rank": len(span_basis(row12)),
                "combined_span_rank": len(span_basis(row12 +
                                                      row12_predicted_mod_a)),
                "source_witness": row12_model_witness,
                "post_F6_parameterization_basis": [encode(poly)
                                                    for poly in row12_on_u_basis],
            },
            "D13_U_square_mod_A": {
                "model": [encode(poly) for poly in row13_model],
                "source_witness": row13_model_witness,
                "post_U_equals_AL_basis": [encode(poly)
                                           for poly in row13_on_l_basis],
            },
            "D13_corrected_scalar_core": {
                "b_bar": encode(b_bar),
                "e_bar": encode(e_bar),
                "E13": encode(e13_core),
                "literal_row_basis_matches": True,
            },
            "D14_corrected_F7_square_prediction": {
                "model": [encode(poly) for poly in row14_model],
                "coefficient_membership": row14_membership,
                "row_span_rank": len(span_basis(row14)),
                "combined_span_rank": len(span_basis(row14 + row14_model)),
                "source_witness": row14_model_witness,
                "post_F7_parameterization_basis": [encode(poly)
                                                    for poly in row14_on_m_basis],
                "tail5_form_E14_test": encode(e14_core),
                "actual_E14": encode(e14_actual),
                "first_shift_map_residual": encode(e14_shift_residual),
            },
            "D14_D15_M_square_mod_A": {
                "model": [encode(poly) for poly in row15_model],
                "source_witness_in_post_D14_then_D15": row15_model_witness,
                "post_M_equals_AN_basis": [encode(poly)
                                           for poly in post_d15_basis],
                "tail5_form_E15_test": encode(e15_tail5_form),
                "actual_E15": encode(e15_actual),
                "E15_shift_map_residual": encode(e15_shift_residual),
            },
            "D17_invariant_core": {
                "allowed_variables": sorted(core_allowed),
                "rank": len(d17_core),
                "basis": [encode(poly) for poly in d17_core],
            },
            "D18_invariant_core": {
                "allowed_variables": sorted(core_allowed),
                "rank": len(d18_core),
                "basis": [encode(poly) for poly in d18_core],
            },
            "D16_D21_V_only_intersections": {
                row: {"rank": len(polys),
                      "basis": [encode(poly) for poly in polys]}
                for row, polys in v_only_by_row.items()
            },
            "D21_full_root_core_intersection": {
                "allowed_variables": sorted(root_allowed),
                "rank": len(root_core_d21),
                "basis": [encode(poly) for poly in root_core_d21],
            },
            "later_core_module_quotient": {
                "old_core": ["E13", "E14", "E15"],
                "module_factors": [f"p{variable}"
                                   for variable in sorted(root_allowed)],
                "old_core_degree_one_module_rank": module_rank,
                "module_plus_D21_root_core_rank": module_plus_root_rank,
                "quotient_dimension": module_plus_root_rank - module_rank,
                "new_invariant": encode(corrected_k),
                "formula": "Q0*(b_bar*Q0+L0^2)",
                "membership_by_row": k_membership_by_row,
                "earliest_exact_ideal_witness": earliest_k_witness,
                "live_sign_mutation": {
                    "mutated_formula": "Q0*(b_bar*Q0-L0^2)",
                    "module_plus_root_plus_mutation_rank": 68,
                    "caught": True,
                },
            },
            "D22_post_substitution_span": {
                "displayed_count": len(row22),
                "polynomials": [encode(poly) for poly in row22],
                "rank": "not densely reduced locally",
            },
        },
        "compatibility_source_provenance": {
            "D6": row6_details, "D7": row7_details,
            "D8": row8_details, "D9": row9_details,
            "D10": row10_details, "D11": row11_details,
            "D12": row12_details,
            "D13": row13_details,
            "D14": row14_details,
            "D15": row15_details,
            "D16": row16_details,
            "D17": row17_details,
            "D18": row18_details,
            "D19": row19_details,
            "D20": row20_details,
            "D21": row21_details,
            "D22": row22_details,
        },
        "parameter_substitutions_through_D10": {
            f"p{variable}": encode(poly)
            for variable, poly in sorted(substitutions.items())
        },
        "D11_post_radical_basis_rank": len(row11_on_q_basis),
        "D12_post_radical_basis_rank": len(row12_on_u_basis),
        "D13_post_radical_basis_rank": len(row13_on_l_basis),
        "D15_post_radical_basis_rank": len(post_d15_basis),
        "status": "PRELIMINARY_EXACT_REDUCTION_THROUGH_D22_AWS_SUCCESSOR_FROZEN",
        "firewalls": [
            "fixed branch-P square baseline and cutoff-three tail only",
            "no endpoint carrier normalized",
            "D23 is not imposed and G22 is absent",
            "the T=0 to cutoff-four handoff is exact, but its closure is external "
            "and review-dependent",
            "no full branch-P, Keller-pair, counterexample, or JC2 conclusion",
        ],
    }, aws_target


def build_payloads():
    data = compile_cutoff3()
    analysis, aws_target = compile_analysis(data)
    aws_target["producer_analysis_sha256"] = hashlib.sha256(
        pretty(analysis)
    ).hexdigest()
    static_sources = [
        PREREGISTRATION,
        HERE / "RESULT.md",
        Path(__file__),
        HERE / "TARGETS/render_singular.py",
        HERE / "TARGETS/preflight_aws.sh",
        HERE / "TARGETS/run_aws.sh",
        HERE / "TARGETS/stop_aws.sh",
        HERE / "TARGETS/job_worker.sh",
        HERE / "TARGETS/process_group_guard.sh",
        HERE / "TARGETS/regress_process_group_control.sh",
        HERE / "TARGETS/validate_results.py",
        HERE / "TARGETS/README.md",
    ]
    source_manifest = (
        f"{RAW_SHA256}  ../ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json\n"
        f"{RAW_INPUT_SHA256}  ../ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json\n"
        + "".join(
            f"{sha256(path)}  {path.relative_to(HERE)}\n"
            for path in static_sources
        )
    ).encode()
    payloads = {
        "TAIL3/TAIL_DEFORMATION_SYSTEM.json": pretty(data),
        "TAIL3_DESK_ANALYSIS.json": pretty(analysis),
        "TARGETS/tail3_v_nonzero_d22_target.json": compact(aws_target),
        "SOURCE.sha256": source_manifest,
    }
    payloads["EVIDENCE.sha256"] = "".join(
        f"{hashlib.sha256(payload).hexdigest()}  {name}\n"
        for name, payload in sorted(payloads.items())
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
        "payload_sha256": {
            name: hashlib.sha256(payload).hexdigest()
            for name, payload in sorted(payloads.items())
        },
        "local_CAS_used": False,
        "AWS_used": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
