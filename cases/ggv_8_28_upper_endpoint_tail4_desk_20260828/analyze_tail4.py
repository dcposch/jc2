#!/usr/bin/env python3
"""Independent exact desk compiler for the cutoff-four square tail.

The script recompiles the prefix nullspace directly from the two pinned raw
JSON sources, tracks literal source-row provenance through every RREF, and
uses no CAS or non-standard Python package.
"""

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

RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
RAW_INPUT_SHA256 = "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876"

# Synthetic coordinates used only after licensed field-radical steps.
B = tuple(range(3000, 3009))       # F4=C*B, deg B<=8
V = tuple(range(3100, 3105))       # B=C*V, deg V<=4
W = tuple(range(3200, 3208))       # F5=V/2+C*W, deg W<=7
R = tuple(range(3300, 3304))       # W=C*R, deg R<=3
T = tuple(range(3400, 3407))       # F6=R/2+C*T, deg T<=6
U = tuple(range(3500, 3503))       # T=C*U, deg U<=2
S = tuple(range(3600, 3606))       # F7=U/2+C*S, deg S<=5
Q7 = tuple(range(3700, 3702))      # S=C*Q7, deg Q7<=1
TAU = 3800                         # r/v on the nonzero D18 branch

# Literal cutoff-four nullspace coordinates.
A_CARRIER = 32                    # G15[X^1]
C_CARRIER = 86                    # G11[X^0]
D_CARRIER = 91                    # F11[X^1]
B_CARRIER = 171                   # F7[X^0]
CHAR4 = 196
CHAR8 = 152
F4_CONSTANT = 209
F5_CONSTANT = 195
F6_CONSTANT = 183


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


def power(poly, exponent):
    out = {(): Q(1)}
    for _ in range(exponent):
        out = mul(out, poly)
    return out


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


def encode(poly):
    return [[list(monomial), str(coefficient)]
            for monomial, coefficient in sorted(poly.items())]


def decode(encoded):
    return {tuple(monomial): Q(coefficient)
            for monomial, coefficient in encoded}


def rref(matrix, provenance=False):
    a = [[Q(value) for value in row] for row in matrix]
    source = [[Q(i == j) for j in range(len(a))]
              for i in range(len(a))] if provenance else None
    rank = 0
    pivots = []
    for column in range(len(a[0]) if a else 0):
        chosen = next((row for row in range(rank, len(a))
                       if a[row][column]), None)
        if chosen is None:
            continue
        a[rank], a[chosen] = a[chosen], a[rank]
        if provenance:
            source[rank], source[chosen] = source[chosen], source[rank]
        scalar = a[rank][column]
        a[rank] = [value / scalar for value in a[rank]]
        if provenance:
            source[rank] = [value / scalar for value in source[rank]]
        for row in range(len(a)):
            if row == rank or not a[row][column]:
                continue
            scalar = a[row][column]
            a[row] = [left - scalar * right
                      for left, right in zip(a[row], a[rank])]
            if provenance:
                source[row] = [left - scalar * right
                               for left, right in zip(source[row], source[rank])]
        pivots.append(column)
        rank += 1
        if rank == len(a):
            break
    return (a, pivots, source) if provenance else (a, pivots)


def polynomial_rref(rows, column_count, provenance=False):
    count = len(rows)
    tracked = []
    for index, (coefficients, residual) in enumerate(rows):
        source = [Q(index == j) for j in range(count)] if provenance else None
        tracked.append(([Q(value) for value in coefficients], dict(residual), source))
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
        tracked[rank] = (coefficients, residual, source)
        for row in range(count):
            if row == rank or not tracked[row][0][column]:
                continue
            scalar = tracked[row][0][column]
            old_coefficients, old_residual, old_source = tracked[row]
            old_coefficients = [left - scalar * right
                                for left, right in zip(old_coefficients,
                                                      coefficients)]
            old_residual = add(old_residual, scale(residual, -scalar))
            if provenance:
                old_source = [left - scalar * right
                              for left, right in zip(old_source, source)]
            tracked[row] = (old_coefficients, old_residual, old_source)
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


def span_contains(polys, target):
    return len(span_basis(polys)) == len(span_basis(polys + [target]))


def same_span(left, right):
    return (len(span_basis(left)) == len(span_basis(right)) ==
            len(span_basis(left + right)))


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
    if any(vector):
        raise ValueError("target not in span")
    reconstruction = {}
    for coefficient, poly in zip(witness, polys):
        reconstruction = add(reconstruction, scale(poly, coefficient))
    assert reconstruction == target
    return witness


def span_intersection(polys, allowed):
    forbidden = sorted({monomial for poly in polys for monomial in poly
                        if any(variable not in allowed for variable in monomial)})
    matrix = [[poly.get(monomial, Q(0)) for poly in polys]
              for monomial in forbidden]
    reduced, pivots = rref(matrix)
    free = [column for column in range(len(polys))
            if column not in set(pivots)]
    intersection = []
    for free_column in free:
        vector = [Q(0)] * len(polys)
        vector[free_column] = Q(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column]
        poly = {}
        for coefficient, source in zip(vector, polys):
            poly = add(poly, scale(source, coefficient))
        assert all(all(variable in allowed for variable in monomial)
                   for monomial in poly)
        if poly:
            intersection.append(poly)
    return span_basis(intersection)


def dense_mul(left, right):
    out = [{} for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = add(out[i + j], mul(a, b))
    return out


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


def mod_c(poly):
    """Remainder modulo C=X^4-1."""
    out = [{} for _ in range(4)]
    for degree, coefficient in enumerate(poly):
        out[degree % 4] = add(out[degree % 4], coefficient)
    return out


def c_times_parameter(source_variables, output_degree):
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


def parameter_stage(vector):
    stages = []
    for name, _coefficient in vector:
        kind, x_degree, y_degree = name.split("_")
        offset = 8 if kind == "f" else 12
        stages.append(offset + 3 * int(x_degree) - int(y_degree))
    return min(stages)


def compile_cutoff4():
    assert sha256(RAW) == RAW_SHA256
    assert sha256(RAW_INPUT) == RAW_INPUT_SHA256
    raw = json.loads(RAW.read_text())
    source = json.loads(RAW_INPUT.read_text())
    weights = {
        slot["slot"]: int(slot["weight"])
        for kind in ("F", "G")
        for slot in source["raw_slots_through_weight_22"][kind]
    }

    def weight(name):
        if name.startswith("z_"):
            return 2
        if name.startswith("tt_"):
            return 3
        return weights[name]

    retained = [name for name in raw["variables"] if weight(name) >= 4]
    retained_index = {name: index for index, name in enumerate(retained)}
    prefix_records = [(index, record)
                      for index, record in enumerate(raw["generators"])
                      if int(record["row"]) <= 7]
    matrix = []
    for _source_index, record in prefix_records:
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
        if int(record["row"]) <= 7:
            continue
        poly = {}
        for monomial, coefficient in record["terms"]:
            if any(name not in forms for name in monomial):
                continue
            term = {(): Q(coefficient)}
            for name in monomial:
                term = mul(term, forms[name])
            poly = add(poly, term)
        encoded = encode(poly)
        constraints.append({
            "source_generator_index": source_index,
            "row": int(record["row"]),
            "x_degree": int(record["x_degree"]),
            "terms": encoded,
            "sha256": hashlib.sha256(compact(encoded)).hexdigest(),
        })
    data = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL4-INDEPENDENT-COMPILE-v1",
        "authoritative_raw_system_sha256": RAW_SHA256,
        "raw_slot_inventory_sha256": RAW_INPUT_SHA256,
        "cutoff": 4,
        "specialization": "all raw deformation parameters of weight below four are zero",
        "linear_last_row": 7,
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
            len(constraints)) == (286, 138, 76, 210, 375)
    endpoint = next(record for record in constraints
                    if record["row"] == 22 and record["x_degree"] == 0)
    assert endpoint["terms"] == [
        [[], "-1"], [[A_CARRIER, B_CARRIER], "-1"],
        [[C_CARRIER, D_CARRIER], "1"],
    ]
    return data


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
    for coefficients, residual, source in reduced[len(pivots):]:
        assert not any(coefficients)
        if not residual:
            continue
        reconstructed = {}
        source_rows = []
        for local_index, coefficient in enumerate(source):
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


def transform_details(details, substitutions):
    out = []
    for detail in details:
        poly = substitute(decode(detail["terms"]), substitutions)
        if not poly:
            continue
        out.append({
            "terms": encode(poly),
            "source_row_combination_after_stage_entry_substitutions": detail[
                "source_row_combination_after_stage_entry_substitutions"
            ],
            "additional_substitution_applied": True,
        })
    return out


def combine_source_provenance(details, coefficients):
    combined = {}
    metadata = {}
    for detail, outer in zip(details, coefficients):
        if not outer:
            continue
        for record in detail["source_row_combination_after_stage_entry_substitutions"]:
            key = int(record["constraint_index"])
            combined[key] = combined.get(key, Q(0)) + outer * Q(record["coefficient"])
            metadata[key] = {
                "constraint_index": key,
                "source_generator_index": int(record["source_generator_index"]),
                "row": int(record["row"]),
                "x_degree": int(record["x_degree"]),
            }
    return [{**metadata[key], "coefficient": str(combined[key])}
            for key in sorted(combined) if combined[key]]


def model_certificate(compatibility, details, targets):
    records = []
    for degree, target in enumerate(targets):
        witness = linear_combination_witness(compatibility, target)
        records.append({
            "remainder_degree": degree,
            "target": encode(target),
            "compatibility_cofactors": [str(value) for value in witness],
            "literal_source_row_cofactors": combine_source_provenance(details, witness),
        })
    return records


def nullspace(matrix):
    reduced, pivots = rref(matrix)
    free = [column for column in range(len(matrix[0]))
            if column not in set(pivots)]
    basis = []
    for free_column in free:
        vector = [Q(0)] * len(matrix[0])
        vector[free_column] = Q(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column]
        basis.append(vector)
    return basis


def stage_map(data):
    stages = {}
    for parameter, vector in enumerate(data["nullspace_basis"]):
        stages.setdefault(parameter_stage(vector), []).append(parameter)
    return stages


def s_form(degree):
    if degree == 0:
        return {(U[0],): Q(1, 2), (B_CARRIER,): Q(-1)}
    if 1 <= degree <= 5:
        return {(S[degree],): Q(1)}
    return {}


def compile_analysis(data):
    stages = stage_map(data)
    expected_stages = {
        4: list(range(196, 210)), 5: list(range(184, 196)),
        6: list(range(172, 184)), 7: list(range(162, 172)),
        8: list(range(136, 162)), 9: list(range(113, 136)),
        10: list(range(92, 113)), 11: list(range(73, 92)),
        12: list(range(57, 73)), 13: list(range(44, 57)),
        14: list(range(33, 44)), 15: list(range(24, 33)),
    }
    for row, expected in expected_stages.items():
        assert stages[row] == expected

    endpoint_source = next(record for record in data["constraints"]
                           if record["row"] == 22 and record["x_degree"] == 0)
    endpoint = {(): Q(1), (A_CARRIER, B_CARRIER): Q(1),
                (C_CARRIER, D_CARRIER): Q(-1)}

    # D8: seven pure equations leave F4^2 mod H on the C line.
    substitutions = {}
    row8_plain, log8_plain, details8_plain = triangular_stage(
        data, 8, stages[8], substitutions
    )
    f4 = [{(F4_CONSTANT - degree,): Q(1)} for degree in range(13)]
    f4_square_mod_h = mod_h(dense_mul(f4, f4))
    pure8 = span_intersection(row8_plain, set(range(197, 210)))
    assert len(pure8) == 7
    pure_in_model = [linear_combination_witness(f4_square_mod_h, poly)
                     for poly in pure8]
    remainder_kernel = nullspace(pure_in_model)
    assert remainder_kernel == [[Q(-1), Q(0), Q(0), Q(0),
                                 Q(1), Q(0), Q(0), Q(0)]]
    pure8_cert = model_certificate(row8_plain, details8_plain, pure8)

    # Licensed field-radical parameterization F4=C*B; the mixed D8 row
    # becomes one scalar compatibility.
    f4_to_b = {F4_CONSTANT - degree: poly
               for degree, poly in c_times_parameter(B, 12).items()}
    substitutions = dict(f4_to_b)
    row8, log8, details8 = triangular_stage(data, 8, stages[8], substitutions)
    scalar8_b = {
        (172,): Q(1), (F6_CONSTANT,): Q(-3, 2),
        (F5_CONSTANT,): Q(-3, 4), (CHAR4,): Q(-1, 4),
        (B[0],): Q(-3, 8),
    }
    assert span_basis(row8) == [scalar8_b]

    # D9: B^2 mod C, then B=C*V.  D8 and D9 leave the same scalar.
    row9, log9, details9 = triangular_stage(data, 9, stages[9], substitutions)
    b_square_mod_c = mod_c(dense_mul(
        [{(variable,): Q(1)} for variable in B],
        [{(variable,): Q(1)} for variable in B],
    ))
    cert9 = model_certificate(row9, details9, b_square_mod_c)
    b_to_v = {B[degree]: poly
              for degree, poly in c_times_parameter(V, 8).items()}
    scalar8_v = substitute(scalar8_b, b_to_v)
    row9_on_v = [substitute(poly, b_to_v) for poly in row9]
    row9_on_v = [poly for poly in row9_on_v if poly]
    assert span_basis(row9_on_v) == [scalar8_v]
    substitutions = compose_substitutions(substitutions, b_to_v)
    char6_formula = {
        (F6_CONSTANT,): Q(3, 2), (F5_CONSTANT,): Q(3, 4),
        (CHAR4,): Q(1, 4), (V[0],): Q(-3, 8),
    }
    substitutions = compose_substitutions(substitutions, {172: char6_formula})
    assert not substitute(scalar8_v, substitutions)

    # D10: (F5-V/2)^2 mod H, then F5=V/2+C*W.
    row10, log10, details10 = triangular_stage(data, 10, stages[10], substitutions)
    f5_minus_half_v = []
    for degree in range(12):
        poly = {(F5_CONSTANT - degree,): Q(1)}
        if degree <= 4:
            poly[(V[degree],)] = Q(-1, 2)
        f5_minus_half_v.append(poly)
    model10 = mod_h(dense_mul(f5_minus_half_v, f5_minus_half_v))
    assert same_span(row10, model10)
    cert10 = model_certificate(row10, details10, model10)
    c_w = c_times_parameter(W, 11)
    f5_to_w = {}
    for degree in range(12):
        poly = dict(c_w[degree])
        if degree <= 4:
            poly = add(poly, {(V[degree],): Q(1, 2)})
        f5_to_w[F5_CONSTANT - degree] = poly
    substitutions = compose_substitutions(substitutions, f5_to_w)
    assert not [substitute(poly, f5_to_w) for poly in row10
                if substitute(poly, f5_to_w)]

    # D11: preserve c=p86.  W^2 mod C is literally present.
    row11, log11, details11 = triangular_stage(
        data, 11, [parameter for parameter in stages[11]
                   if parameter != C_CARRIER], substitutions
    )
    w_square_mod_c = mod_c(dense_mul(
        [{(variable,): Q(1)} for variable in W],
        [{(variable,): Q(1)} for variable in W],
    ))
    cert11 = model_certificate(row11, details11, w_square_mod_c)
    w_to_r = {W[degree]: poly
              for degree, poly in c_times_parameter(R, 7).items()}
    row11_on_r = [substitute(poly, w_to_r) for poly in row11]
    row11_on_r = [poly for poly in row11_on_r if poly]
    row11_on_r_basis = span_basis(row11_on_r)
    c_initial = {
        (B_CARRIER, CHAR4): Q(1), (B_CARRIER, V[0]): Q(-3, 4),
        (F6_CONSTANT, R[0]): Q(3, 4), (R[0], R[0]): Q(-3, 16),
    }
    g10_initial = {
        (F6_CONSTANT, CHAR4): Q(1), (F6_CONSTANT, V[0]): Q(-3, 4),
        (R[0], R[0]): Q(3, 8),
    }
    expected11 = [
        add({(C_CARRIER,): Q(1)}, scale(c_initial, -1)),
        add({(106,): Q(1)}, scale(g10_initial, -1)),
    ]
    assert same_span(row11_on_r_basis, expected11)
    substitutions = compose_substitutions(substitutions, w_to_r)
    substitutions = compose_substitutions(substitutions, {
        C_CARRIER: c_initial, 106: g10_initial,
    })

    # D12: (F6-R/2)^2 mod H, then F6=R/2+C*T.
    row12, log12, details12 = triangular_stage(data, 12, stages[12], substitutions)
    f6_minus_half_r = []
    for degree in range(11):
        poly = {(F6_CONSTANT - degree,): Q(1)}
        if degree <= 3:
            poly[(R[degree],)] = Q(-1, 2)
        f6_minus_half_r.append(poly)
    model12 = mod_h(dense_mul(f6_minus_half_r, f6_minus_half_r))
    assert same_span(row12, model12)
    cert12 = model_certificate(row12, details12, model12)
    c_t = c_times_parameter(T, 10)
    f6_to_t = {}
    for degree in range(11):
        poly = dict(c_t[degree])
        if degree <= 3:
            poly = add(poly, {(R[degree],): Q(1, 2)})
        f6_to_t[F6_CONSTANT - degree] = poly
    substitutions = compose_substitutions(substitutions, f6_to_t)
    assert not [substitute(poly, f6_to_t) for poly in row12
                if substitute(poly, f6_to_t)]

    # D13: T^2 mod C, then T=C*U.  One scalar remains.
    row13, log13, details13 = triangular_stage(data, 13, stages[13], substitutions)
    t_square_mod_c = mod_c(dense_mul(
        [{(variable,): Q(1)} for variable in T],
        [{(variable,): Q(1)} for variable in T],
    ))
    cert13 = model_certificate(row13, details13, t_square_mod_c)
    t_to_u = {T[degree]: poly
              for degree, poly in c_times_parameter(U, 6).items()}
    post13 = [substitute(poly, t_to_u) for poly in row13]
    post13 = [poly for poly in post13 if poly]
    e13 = {
        (CHAR8, R[0]): Q(1), (B_CARRIER, R[0]): Q(-3, 4),
        (B_CARRIER, U[0]): Q(3, 2), (CHAR4, V[0], R[0]): Q(-1),
        (V[0], V[0], R[0]): Q(3, 4), (U[0], U[0]): Q(-3, 8),
    }
    assert span_basis(post13) == [e13]
    substitutions = compose_substitutions(substitutions, t_to_u)

    # D14: (F7-U/2)^2 mod C.  Parameterize F7=U/2+C*S while
    # preserving b=p171 exactly.
    row14, log14, details14 = triangular_stage(data, 14, stages[14], substitutions)
    f7_minus_half_u = []
    for degree in range(10):
        poly = {(B_CARRIER - degree,): Q(1)}
        if degree <= 2:
            poly[(U[degree],)] = Q(-1, 2)
        f7_minus_half_u.append(poly)
    model14 = mod_c(dense_mul(f7_minus_half_u, f7_minus_half_u))
    cert14 = model_certificate(row14, details14, model14)
    f7_to_s = {}
    for degree in range(1, 10):
        poly = {(U[degree],): Q(1, 2)} if degree <= 2 else {}
        if 0 <= degree - 4 <= 5:
            poly = add(poly, s_form(degree - 4))
        if degree <= 5:
            poly = add(poly, scale(s_form(degree), -1))
        f7_to_s[B_CARRIER - degree] = poly
    substitutions = compose_substitutions(substitutions, f7_to_s)
    post14 = [substitute(poly, f7_to_s) for poly in row14]
    post14 = [poly for poly in post14 if poly]
    e14 = {
        (CHAR8, U[0]): Q(1), (B_CARRIER, B_CARRIER): Q(3, 4),
        (B_CARRIER, U[0]): Q(-3, 2), (CHAR4, V[0], U[0]): Q(-1),
        (V[0], V[0], U[0]): Q(3, 4),
        (V[0], R[0], R[0]): Q(-3, 8), (U[0], U[0]): Q(3, 16),
    }
    assert same_span(post13 + post14, [e13, e14])

    # D14+D15 force S^2 mod C.  Preserve a=p32 in D15.
    row15, log15, details15 = triangular_stage(
        data, 15, [parameter for parameter in stages[15]
                   if parameter != A_CARRIER], substitutions
    )
    s_poly = [s_form(degree) for degree in range(6)]
    s_square_mod_c = mod_c(dense_mul(s_poly, s_poly))
    cumulative14_15 = post14 + row15
    details14_post = transform_details(details14, f7_to_s)
    assert len(details14_post) == len(post14)
    cumulative_details = details14_post + details15
    cert15 = model_certificate(cumulative14_15, cumulative_details,
                               s_square_mod_c)
    s_to_q = {
        S[0]: s_form(0), S[1]: {(Q7[1],): Q(-1)},
        S[2]: {}, S[3]: {},
        S[4]: {(B_CARRIER,): Q(1), (U[0],): Q(-1, 2)},
        S[5]: {(Q7[1],): Q(1)},
    }
    substitutions = compose_substitutions(substitutions, s_to_q)
    post15 = [substitute(poly, s_to_q) for poly in cumulative14_15]
    post15 = [poly for poly in post15 if poly]
    post15_details = transform_details(cumulative_details, s_to_q)
    assert len(post15_details) == len(post15)
    post15_basis = span_basis(post15)
    assert len(post15_basis) == 4
    e15 = {
        (CHAR8, B_CARRIER): Q(1),
        (B_CARRIER, B_CARRIER): Q(-3, 4),
        (B_CARRIER, CHAR4, V[0]): Q(-1),
        (B_CARRIER, V[0], V[0]): Q(3, 4),
        (V[0], R[0], R[0]): Q(-3, 16),
        (V[0], R[0], U[0]): Q(-3, 4),
        (R[0], R[0], R[0]): Q(-1, 8),
    }
    invariant = span_intersection(
        post15, {CHAR8, CHAR4, B_CARRIER, V[0], R[0], U[0]}
    )
    assert same_span(invariant, [e15, e13, e14])
    a_partner = next(poly for poly in post15_basis
                     if any(A_CARRIER in monomial for monomial in poly))

    c_formula = substitute(c_initial, substitutions)
    expected_c_formula = {
        (B_CARRIER, CHAR4): Q(1), (B_CARRIER, V[0]): Q(-3, 4),
        (R[0], U[0]): Q(3, 4), (R[0], R[0]): Q(3, 16),
    }
    assert c_formula == expected_c_formula
    c_relation = add({(C_CARRIER,): Q(1)}, scale(c_formula, -1))

    # Exact additive F -> F+mu*t^8 gauge; no endpoint carrier is touched.
    assert all(161 not in monomial
               for record in data["constraints"]
               for monomial, _coefficient in record["terms"])

    # Bounded shifted-tail diagnostic: enter the licensed additive-gauge
    # slice and reduce only D16 and D17.  This tests whether the cutoff-five
    # K17 mechanism transports literally; no ideal/radical inference is made.
    continuation_substitutions = compose_substitutions(substitutions, {161: {}})
    row16, log16, details16 = triangular_stage(
        data, 16, stages[16], continuation_substitutions
    )
    row17, log17, details17 = triangular_stage(
        data, 17, stages[17], continuation_substitutions
    )
    row18, log18, details18 = triangular_stage(
        data, 18, stages[18], continuation_substitutions
    )
    row19, log19, details19 = triangular_stage(
        data, 19, stages[19], continuation_substitutions
    )
    row20, log20, details20 = triangular_stage(
        data, 20, stages[20], continuation_substitutions
    )
    invariant_symbols = {CHAR8, CHAR4, B_CARRIER, V[0], R[0], U[0]}
    invariant_through_d16 = span_intersection(post15 + row16,
                                              invariant_symbols)
    invariant_through_d17 = span_intersection(post15 + row16 + row17,
                                              invariant_symbols)
    invariant_through_d18 = span_intersection(post15 + row16 + row17 + row18,
                                              invariant_symbols)

    k18 = {
        (B_CARRIER, R[0], R[0]): Q(1),
        (R[0], U[0], U[0]): Q(1),
    }
    through_d18 = post15 + row16 + row17 + row18
    k18_witness = linear_combination_witness(through_d18, k18)
    assert same_span(invariant_through_d18, [e15, e13, e14, k18])
    core_source_provenance = {}
    for label, poly in (("E13", e13), ("E14", e14), ("E15", e15)):
        witness = linear_combination_witness(post15, poly)
        core_source_provenance[label] = combine_source_provenance(
            post15_details, witness
        )
    through_d18_details = post15_details + details16 + details17 + details18
    assert len(through_d18_details) == len(through_d18)
    k18_source_provenance = combine_source_provenance(through_d18_details,
                                                      k18_witness)

    # Closed field branch v=R0=0.  The core gives b^3=0, while the carrier
    # reduces to c=b*s.  Lift the geometric endpoint identity without any
    # division or carrier normalization.
    v_poly = {(R[0],): Q(1)}
    r_poly = {(U[0],): Q(1)}
    b_poly = {(B_CARRIER,): Q(1)}
    s_poly_scalar = add({(CHAR4,): Q(1)}, {(V[0],): Q(-3, 4)})
    y_poly = add({(A_CARRIER,): Q(1)},
                 scale(mul(s_poly_scalar, {(D_CARRIER,): Q(1)}), -1))
    z_poly = mul(b_poly, y_poly)
    geometric = add(add({(): Q(1)}, scale(z_poly, -1)), mul(z_poly, z_poly))
    core_b3 = add(
        add(mul(scale(b_poly, 2), e13), mul(scale(b_poly, 4), e14)),
        mul(scale(r_poly, -4), e15),
    )
    # Off the v=0 branch, the difference is recorded by an exact v cofactor.
    b_cubed = {(B_CARRIER, B_CARRIER, B_CARRIER): Q(3)}
    v_remainder = add(core_b3, scale(b_cubed, -1))
    assert all(R[0] in monomial for monomial in v_remainder)
    v_cofactor = {}
    for monomial, coefficient in v_remainder.items():
        reduced_monomial = list(monomial)
        reduced_monomial.remove(R[0])
        reduced_monomial = tuple(reduced_monomial)
        v_cofactor[reduced_monomial] = (
            v_cofactor.get(reduced_monomial, Q(0)) + coefficient
        )
    assert mul(v_poly, v_cofactor) == v_remainder
    y_cubed = mul(mul(y_poly, y_poly), y_poly)
    v0_generators = [endpoint, c_relation, e13, e14, e15, v_poly]
    v0_cofactors = [
        geometric,
        mul(geometric, {(D_CARRIER,): Q(1)}),
        mul(scale(mul(b_poly, y_cubed), Q(-2, 3)), {(): Q(1)}),
        scale(mul(b_poly, y_cubed), Q(-4, 3)),
        scale(mul(r_poly, y_cubed), Q(4, 3)),
        add(
            scale(mul(v_cofactor, y_cubed), Q(1, 3)),
            mul(mul(geometric, {(D_CARRIER,): Q(1)}),
                add(scale(r_poly, Q(3, 4)), scale(v_poly, Q(3, 16)))),
        ),
    ]
    v0_unit = {}
    for generator, cofactor in zip(v0_generators, v0_cofactors):
        v0_unit = add(v0_unit, mul(generator, cofactor))
    assert v0_unit == {(): Q(1)}

    # Open branch v!=0.  Parameterize the exact E13--E15,K18 solution by
    # tau=r/v.  The old cutoff-five quadratic is absorbed by the leading
    # weight-four coordinate x; tau remains free before later rows.
    tau = {(TAU,): Q(1)}
    tau2 = mul(tau, tau)
    tau3 = mul(tau2, tau)
    tau4 = mul(tau3, tau)
    tau5 = mul(tau4, tau)
    quadratic = add(add(scale(tau2, 12), scale(tau, 6)), {(): Q(1)})
    x_open = scale(mul(tau2, quadratic), Q(1, 2))
    v_open = add(add(add(scale(tau5, -48), scale(tau4, -30)),
                     scale(tau3, Q(-15, 2))), scale(tau2, Q(-3, 4)))
    r_open = mul(tau, v_open)
    b_open = scale(mul(tau2, v_open), -1)
    h_open = scale(mul(mul(v_open, tau2), add(scale(tau, 4), {(): Q(-1)})),
                   Q(3, 8))
    char8_open = add(add(h_open, mul({(CHAR4,): Q(1)}, x_open)),
                     scale(mul(x_open, x_open), Q(-3, 4)))
    open_substitutions = {
        V[0]: x_open, R[0]: v_open, U[0]: r_open,
        B_CARRIER: b_open, CHAR8: char8_open,
    }
    for core_poly in (e13, e14, e15, k18):
        assert not substitute(core_poly, open_substitutions)
    through_d19_open = [substitute(poly, open_substitutions)
                        for poly in post15 + row16 + row17 + row18 + row19]
    through_d19_open = [poly for poly in through_d19_open if poly]
    open_tau_char4_projection = span_intersection(through_d19_open,
                                                  {TAU, CHAR4})
    through_d20_open = [substitute(poly, open_substitutions)
                        for poly in (post15 + row16 + row17 + row18 + row19 + row20)]
    through_d20_open = [poly for poly in through_d20_open if poly]
    open_tau_char4_projection_d20 = span_intersection(through_d20_open,
                                                      {TAU, CHAR4})
    p3 = add(add(add({(): Q(1)}, scale(tau, 10)), scale(tau2, 40)),
             scale(tau3, 64))
    assert v_open == scale(mul(tau2, p3), Q(-3, 4))
    target20 = mul(power(tau, 9), power(p3, 3))
    target20_witness = linear_combination_witness(through_d20_open, target20)
    target20_reconstruction = {}
    for coefficient, generator in zip(target20_witness, through_d20_open):
        target20_reconstruction = add(
            target20_reconstruction, scale(generator, coefficient)
        )
    assert target20_reconstruction == target20
    all_details_preopen = (post15_details + details16 + details17 + details18 +
                           details19 + details20)
    all_details_open = transform_details(all_details_preopen, open_substitutions)
    assert len(all_details_open) == len(through_d20_open)
    target20_source = combine_source_provenance(all_details_open,
                                                target20_witness)
    through_d19_only_open = [substitute(poly, open_substitutions)
                             for poly in (post15 + row16 + row17 + row18 + row19)]
    through_d19_only_open = [poly for poly in through_d19_only_open if poly]
    assert not span_contains(through_d19_only_open, target20)
    mutated_p3 = add(add(add({(): Q(1)}, scale(tau, 10)), scale(tau2, -40)),
                     scale(tau3, 64))
    mutated_target20 = mul(power(tau, 9), power(mutated_p3, 3))
    assert not span_contains(through_d20_open, mutated_target20)
    first_witness_index = next(index for index, coefficient
                               in enumerate(target20_witness) if coefficient)
    omitted_witness_reconstruction = add(
        target20_reconstruction,
        scale(through_d20_open[first_witness_index],
              -target20_witness[first_witness_index]),
    )
    assert omitted_witness_reconstruction != target20
    linear_factor = add({(): Q(1)}, scale(tau, 4))
    boundary_quadratic = add(add({(): Q(1)}, scale(tau, 6)),
                             scale(tau2, 16))
    assert p3 == mul(linear_factor, boundary_quadratic)
    rational_boundary = {TAU: {(): Q(-1, 4)}}
    assert not substitute(p3, rational_boundary)
    assert not substitute(v_open, rational_boundary)
    assert not substitute(target20, rational_boundary)

    v0_certificate = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL4-R0-ZERO-UNIT-v1",
        "branch": "R0=0",
        "generator_order": ["endpoint", "c_relation", "E13", "E14", "E15",
                            "R0"],
        "generators": [encode(poly) for poly in v0_generators],
        "cofactors": [encode(poly) for poly in v0_cofactors],
        "exact_reconstruction": encode(v0_unit),
        "division_used": False,
        "endpoint_carrier_normalized": False,
        "core_identity": "3*b^3=2*b*E13+4*b*E14-4*r*E15 modulo R0",
        "core_literal_source_row_provenance_after_parameterizations": (
            core_source_provenance
        ),
    }
    open_certificate = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL4-R0-NONZERO-D20-v1",
        "branch": "R0!=0",
        "tau": "U0/R0",
        "P3": encode(p3),
        "P3_factorization": {
            "linear": encode(linear_factor),
            "quadratic": encode(boundary_quadratic),
            "identity": "P3=(4*tau+1)*(16*tau^2+6*tau+1)",
        },
        "R0_formula": encode(v_open),
        "target": encode(target20),
        "target_identity": "tau^9*P3(tau)^3=0",
        "compatibility_cofactors": [str(value) for value in target20_witness],
        "compatibility_generators_after_branch_substitution": [
            encode(poly) for poly in through_d20_open
        ],
        "exact_reconstruction": encode(target20_reconstruction),
        "literal_source_row_cofactors_after_branch_substitution": target20_source,
        "K18_literal_source_row_provenance_after_parameterizations": (
            k18_source_provenance
        ),
        "field_contradiction": (
            "R0=-(3/4)*tau^2*P3 and R0!=0 imply tau!=0 and P3!=0, "
            "whereas the D20 target forces tau=0 or P3=0"
        ),
        "endpoint_used": False,
        "D19_only_contains_target": False,
        "sign_mutated_P3_target_contained": False,
        "omit_first_nonzero_serialized_cofactor": {
            "index": first_witness_index,
            "reconstructs_target": False,
            "mutated_reconstruction": encode(omitted_witness_reconstruction),
        },
        "drop_open_condition_boundary_check": {
            "tau=-1/4": {
                "P3": "0", "R0": "0", "target": "0",
            },
            "quadratic_boundary": (
                "16*tau^2+6*tau+1=0 also gives P3=R0=target=0"
            ),
            "interpretation": (
                "these are exactly R0=0 boundary points of the tau chart, "
                "not solutions of the localized R0!=0 branch"
            ),
        },
    }

    # Mutations: each one must fail in a named, nonzero way.
    deleted_pure_kernel = nullspace(pure_in_model[1:])
    assert len(deleted_pure_kernel) == 2
    wrong_half = []
    for degree in range(12):
        poly = {(F5_CONSTANT - degree,): Q(1)}
        if degree <= 4:
            poly[(V[degree],)] = Q(1, 2)
        wrong_half.append(poly)
    wrong_model10 = mod_h(dense_mul(wrong_half, wrong_half))
    assert not all(span_contains(row10, target) for target in wrong_model10)
    # The emitted compatibility list is deliberately redundant, so deletion
    # of an arbitrary single displayed row need not change its span.  Removing
    # the whole D15 block must, however, destroy at least one S-square target.
    missing_without_d15 = next(
        (degree for degree, target in enumerate(s_square_mod_c)
         if not span_contains(post14, target)), None
    )
    assert missing_without_d15 is not None
    mutated_c = dict(c_formula)
    del mutated_c[(R[0], R[0])]
    c_mutation_difference = add(c_formula, scale(mutated_c, -1))
    assert c_mutation_difference == {(R[0], R[0]): Q(3, 16)}
    wrong_endpoint = {(): Q(1), (A_CARRIER, B_CARRIER): Q(-1),
                      (C_CARRIER, D_CARRIER): Q(-1)}
    assert encode(scale(endpoint, -1)) == endpoint_source["terms"]
    assert encode(scale(wrong_endpoint, -1)) != endpoint_source["terms"]

    def stage_record(log, certificate=None):
        out = dict(log)
        if certificate is not None:
            out["remainder_inclusion_certificate"] = certificate
        return out

    analysis = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL4-DESK-ANALYSIS-v1",
        "authoritative_raw_system_sha256": RAW_SHA256,
        "raw_slot_inventory_sha256": RAW_INPUT_SHA256,
        "method": "Python Fraction exact arithmetic; no CAS",
        "prefix": {
            "retained_variables": 286,
            "generator_count_through_D7": 138,
            "rank": 76,
            "nullity": 210,
        },
        "endpoint": {
            "literal_source_record": endpoint_source,
            "equation": encode(endpoint),
            "display": "1+p32*p171-p86*p91=0",
            "carriers": {
                "p32": "G15[X^1]", "p171": "F7[X^0]",
                "p86": "G11[X^0]", "p91": "F11[X^1]",
            },
            "carrier_lifts": {f"p{index}": data["nullspace_basis"][index]
                              for index in (32, 171, 86, 91)},
        },
        "D8_pure_remainder_line": {
            "plain_log": log8_plain,
            "pure_quadratic_rank": len(pure8),
            "pure_equations": [encode(poly) for poly in pure8],
            "pure_equations_as_F4_square_remainder_cofactors": [
                [str(value) for value in witness] for witness in pure_in_model
            ],
            "remainder_kernel": [[str(value) for value in vector]
                                 for vector in remainder_kernel],
            "kernel_interpretation": "(-1,0,0,0,1,0,0,0) is X^4-1",
            "literal_source_certificates": pure8_cert,
            "field_radical_consequence": "F4=(X^4-1)*B",
            "post_parameterization_log": log8,
            "remaining_scalar": encode(scalar8_b),
        },
        "cascade": [
            stage_record(log9, cert9), stage_record(log10, cert10),
            stage_record(log11, cert11), stage_record(log12, cert12),
            stage_record(log13, cert13), stage_record(log14, cert14),
            {
                **log15,
                "uses_cumulative_D14_D15_span": True,
                "remainder_inclusion_certificate": cert15,
            },
        ],
        "parameterizations": [
            "F4=C*B", "B=C*V, hence F4=H*V",
            "F5=V/2+C*W", "W=C*R, hence F5=V/2+H*R",
            "F6=R/2+C*T", "T=C*U, hence F6=R/2+H*U",
            "F7=U/2+C*S", "S=C*Q7, hence F7=U/2+H*Q7",
        ],
        "post_D15_core": {
            "E13": encode(e13), "E14": encode(e14), "E15": encode(e15),
            "a_partner": encode(a_partner),
            "c_relation": encode(c_relation),
            "c_formula": encode(c_formula),
            "span_rank": len(post15_basis),
            "invariant_core_rank": len(invariant),
        },
        "exact_additive_gauge": {
            "coordinate": "p161=F8[X^0]",
            "charged_constraint_occurrences": 0,
            "licensed_slice": "p161=0",
            "endpoint_carrier_normalization": False,
        },
        "bounded_shifted_tail_test": {
            "D16_log": log16,
            "D17_log": log17,
            "D18_log": log18,
            "D19_log": log19,
            "D20_log": log20,
            "invariant_core_through_D16": [encode(poly)
                                           for poly in invariant_through_d16],
            "invariant_core_through_D17": [encode(poly)
                                           for poly in invariant_through_d17],
            "invariant_core_through_D18": [encode(poly)
                                           for poly in invariant_through_d18],
            "invariant_rank_through_D15": len(invariant),
            "invariant_rank_through_D16": len(invariant_through_d16),
            "invariant_rank_through_D17": len(invariant_through_d17),
            "invariant_rank_through_D18": len(invariant_through_d18),
            "K18": encode(k18),
            "K18_cumulative_compatibility_cofactors": [str(value)
                                                       for value in k18_witness],
            "closed_R0_zero_unit": {
                "generator_order": ["endpoint", "c_relation", "E13", "E14",
                                    "E15", "R0"],
                "cofactors": [encode(poly) for poly in v0_cofactors],
                "exact_reconstruction": encode(v0_unit),
                "division_used": False,
            },
            "open_R0_nonzero_parameterization": {
                "tau_definition": "tau=U0/R0",
                "V0": encode(x_open), "R0": encode(v_open),
                "U0": encode(r_open), "p171": encode(b_open),
                "p152": encode(char8_open),
                "open_condition": "R0(tau)!=0",
                "D19_tau_p196_projection": [encode(poly)
                                             for poly in open_tau_char4_projection],
                "D19_tau_p196_projection_rank": len(open_tau_char4_projection),
                "D20_tau_p196_projection": [encode(poly)
                                             for poly in open_tau_char4_projection_d20],
                "D20_tau_p196_projection_rank": len(open_tau_char4_projection_d20),
                "D20_decisive_target": encode(target20),
            },
            "scope": "Q-linear compatibility projection only; no radical conclusion",
        },
        "mutations": {
            "delete_one_D8_pure_equation_kernel_dimension": len(deleted_pure_kernel),
            "wrong_D10_half_shift_contained": False,
            "omit_D15_block_missing_remainder_degree": missing_without_d15,
            "missing_target_without_D15_contained": False,
            "delete_c_R0_square_difference": encode(c_mutation_difference),
            "endpoint_sign_mutation_matches_literal": False,
        },
        "first_genuine_residual": {
            "location": "resolved through D20",
            "description": "R0=0 endpoint unit; R0!=0 contradicted by the D20 tau target",
            "next_exact_target": "hostile replay of both branch certificates",
        },
        "scope": {
            "base": "characteristic-zero field-valued points",
            "radical_not_scheme": True,
            "endpoint_used_only_on_R0_zero_branch": True,
            "conclusion": "provisional exclusion of cutoff-four characteristic-zero field points",
        },
        "certificates": {
            "R0_zero_unit": v0_certificate,
            "R0_nonzero_D20": open_certificate,
        },
    }
    return analysis


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = compile_cutoff4()
    analysis = compile_analysis(data)
    payloads = {
        "TAIL4/TAIL_DEFORMATION_SYSTEM.json": pretty(data),
        "TAIL4_DESK_ANALYSIS.json": pretty(analysis),
        "CERTIFICATES/tail4_R0_zero_unit.json": pretty(
            analysis["certificates"]["R0_zero_unit"]
        ),
        "CERTIFICATES/tail4_R0_nonzero_D20.json": pretty(
            analysis["certificates"]["R0_nonzero_D20"]
        ),
    }
    if not args.check:
        for name, payload in payloads.items():
            path = args.output / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
    print(json.dumps({
        "status": "PASS",
        "cutoff": 4,
        "prefix_rank": data["prefix_rank"],
        "nullity": data["nullity"],
        "constraint_generators": data["constraint_generator_count"],
        "analysis_sha256": hashlib.sha256(payloads["TAIL4_DESK_ANALYSIS.json"]).hexdigest(),
        "system_sha256": hashlib.sha256(payloads["TAIL4/TAIL_DEFORMATION_SYSTEM.json"]).hexdigest(),
        "R0_zero_certificate_sha256": hashlib.sha256(
            payloads["CERTIFICATES/tail4_R0_zero_unit.json"]
        ).hexdigest(),
        "R0_nonzero_certificate_sha256": hashlib.sha256(
            payloads["CERTIFICATES/tail4_R0_nonzero_D20.json"]
        ).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
