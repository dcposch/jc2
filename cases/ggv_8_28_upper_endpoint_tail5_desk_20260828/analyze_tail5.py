#!/usr/bin/env python3
"""Exact standard-library analysis of the cutoff-five square tail.

This file independently recompiles the cutoff-five nullspace from the
authoritative raw determinant JSON.  It does not import any other tail
compiler and never invokes a CAS.
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
PREREGISTRATION = HERE / "PREREGISTRATION.md"

RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
RAW_INPUT_SHA256 = "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876"

# Synthetic variables used only in the exact field-radical parameterizations.
B = tuple(range(2000, 2008))
V = tuple(range(2100, 2104))
W = tuple(range(2200, 2207))
R = tuple(range(2300, 2303))
T = tuple(range(2400, 2406))
Q7 = tuple(range(2500, 2502))
QUADRATIC_T = 2600

# Literal endpoint/core nullspace coordinates.
A_CARRIER = 32       # g_1_0 = G15[X^1]
C_CARRIER = 86       # g_0_1 = G11[X^0]
D_CARRIER = 91       # f_1_0 = F11[X^1]
CHAR8 = 120           # weight-eight characteristic coordinate
B_CARRIER = 139      # F7[X^0]
F6_CONSTANT = 150    # F6[X^0]
F5_CONSTANT = 162    # F5[X^0] = V0 after the first two radical steps


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


def rref_polynomial_rows(rows, column_count, provenance=False):
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
            other_coefficients, other_residual, other_source = tracked[row]
            other_coefficients = [left - scalar * right
                                  for left, right in zip(other_coefficients,
                                                        coefficients)]
            other_residual = add(other_residual, scale(residual, -scalar))
            if provenance:
                other_source = [left - scalar * right
                                for left, right in zip(other_source, source)]
            tracked[row] = (other_coefficients, other_residual, other_source)
        pivots.append(column)
        rank += 1
    return tracked, pivots


def span_basis_with_witness(polys):
    monomials = sorted({monomial for poly in polys for monomial in poly})
    rows = [([poly.get(monomial, Q(0)) for monomial in monomials], {})
            for poly in polys]
    reduced, pivots = rref_polynomial_rows(rows, len(monomials), provenance=True)
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


def linear_combination_witness(polys, target):
    monomials = sorted({monomial for poly in polys + [target]
                        for monomial in poly})
    rows = [([poly.get(monomial, Q(0)) for monomial in monomials], {})
            for poly in polys]
    reduced, pivots = rref_polynomial_rows(rows, len(monomials), provenance=True)
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


def same_span(left, right):
    return (len(span_basis(left)) == len(span_basis(right)) ==
            len(span_basis(left + right)))


def dense_mul(left, right):
    out = [{} for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = add(out[i + j], mul(a, b))
    return out


def mod_h(poly):
    """Remainder modulo H=X^8-2X^4+1."""
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


def compile_cutoff5():
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

    retained = [name for name in raw["variables"] if weight(name) >= 5]
    retained_index = {name: index for index, name in enumerate(retained)}
    prefix = [record for record in raw["generators"]
              if int(record["row"]) <= 9]
    matrix = []
    for record in prefix:
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
        if int(record["row"]) <= 9:
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
    values = {}
    for name in raw["variables"]:
        values[name] = encode(forms.get(name, {}))
    result = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL5-INDEPENDENT-COMPILE-v1",
        "authoritative_raw_system_sha256": RAW_SHA256,
        "raw_slot_inventory_sha256": RAW_INPUT_SHA256,
        "cutoff": 5,
        "specialization": "all raw deformation parameters of weight below five are zero",
        "linear_last_row": 9,
        "prefix_generator_count": len(prefix),
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
    }
    assert (len(retained), len(prefix), len(pivots), len(basis),
            len(constraints)) == (252, 201, 89, 163, 312)
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
    reduced, pivots = rref_polynomial_rows(rows, len(candidates), provenance=True)
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
    log = {
        "row": row_number,
        "equation_count": len(indexed),
        "candidate_count": len(candidates),
        "rank": len(pivots),
        "free_parameters": [candidates[column] for column in free],
        "displayed_compatibility_count": len(compatibility),
        "compatibility_span_rank": len(span_basis(compatibility)),
    }
    return compatibility, log, details


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


def span_inclusion_certificate(source, targets):
    return [[str(value) for value in linear_combination_witness(source, target)]
            for target in targets]


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


def evaluate(poly, point):
    total = Q(0)
    for monomial, coefficient in poly.items():
        term = coefficient
        for variable in monomial:
            term *= point.get(variable, Q(0))
        total += term
    return total


def quadratic_reduce(poly, constant=Q(1)):
    """Reduce exactly modulo 12*t^2+6*t+constant.

    ``constant=1`` is the live irreducible quadratic branch.  The optional
    argument exists solely for the sign-mutation regression below.
    """
    powers = [(Q(1), Q(0)), (Q(0), Q(1))]
    maximum = max((monomial.count(QUADRATIC_T) for monomial in poly), default=0)
    for _degree in range(2, maximum + 1):
        c0, c1 = powers[-1]
        # t*(c0+c1*t), using t^2=-(constant+6*t)/12.
        powers.append((-constant * c1 / 12, c0 - c1 / 2))
    out = {}
    for monomial, coefficient in poly.items():
        degree = monomial.count(QUADRATIC_T)
        base = tuple(variable for variable in monomial
                     if variable != QUADRATIC_T)
        c0, c1 = powers[degree]
        if c0:
            out[base] = out.get(base, Q(0)) + coefficient * c0
        if c1:
            with_t = tuple(sorted(base + (QUADRATIC_T,)))
            out[with_t] = out.get(with_t, Q(0)) + coefficient * c1
    return {monomial: coefficient for monomial, coefficient in out.items()
            if coefficient}


def variable_name(variable):
    if variable < 1000:
        return f"p{variable}"
    for variables, prefix in ((B, "baux"), (V, "v"), (W, "w"),
                              (R, "r"), (T, "t"), (Q7, "q")):
        if variable in variables:
            return f"{prefix}{variables.index(variable)}"
    if variable == QUADRATIC_T:
        return "tau"
    raise AssertionError(variable)


def singular_expression(poly):
    pieces = []
    for monomial, coefficient in sorted(poly.items()):
        atom = "*".join(variable_name(variable) for variable in monomial) or "1"
        pieces.append(f"({coefficient})*{atom}")
    return "+".join(pieces) or "0"


def singular_text(target):
    variables = [variable_name(variable) for variable in target["operative_variables"]]
    polys = [decode(record["terms"]) for record in target["constraints"]]
    return "\n".join([
        f"ring tail5=0,({','.join(variables)}),dp;",
        "option(redSB);",
        "ideal I=",
        ",\n".join(singular_expression(poly) for poly in polys) + ";",
        'print("TAIL5 variables="+string(nvars(basering))+" generators="+string(size(I)));',
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


def constraint_records(polys):
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


def compile_analysis(data):
    stages = {}
    for parameter, vector in enumerate(data["nullspace_basis"]):
        stages.setdefault(parameter_stage(vector), []).append(parameter)
    assert stages[10] == list(range(92, 113))
    assert stages[11] == list(range(73, 92))
    assert stages[12] == list(range(57, 73))
    assert stages[13] == list(range(44, 57))
    assert stages[14] == list(range(33, 44))
    assert stages[15] == list(range(24, 33))

    # D10: the compatibility space is exactly F5^2 modulo H.
    plain_substitutions = {}
    row10_plain, row10_plain_log, row10_plain_details = triangular_stage(
        data, 10, stages[10], plain_substitutions
    )
    f5 = [{(F5_CONSTANT - degree,): Q(1)} for degree in range(12)]
    row10_model = mod_h(dense_mul(f5, f5))
    assert same_span(row10_plain, row10_model)

    # Parameterize F5=C*B and replay the row before moving onward.
    substitutions = {
        F5_CONSTANT - degree: poly
        for degree, poly in c_times_parameter(B, 11).items()
    }
    row10, row10_log, row10_details = triangular_stage(
        data, 10, stages[10], substitutions
    )
    assert not row10

    # D11: preserve c=p86.  Its field-radical part contains B^2 mod C.
    row11, row11_log, row11_details = triangular_stage(
        data, 11, [parameter for parameter in stages[11]
                   if parameter != C_CARRIER], substitutions
    )
    b_poly = [{(variable,): Q(1)} for variable in B]
    row11_mod_c = mod_c(dense_mul(b_poly, b_poly))
    row11_mod_c_witness = span_inclusion_certificate(row11, row11_mod_c)

    b_to_v = {B[degree]: poly
              for degree, poly in c_times_parameter(V, 7).items()}
    substitutions = compose_substitutions(substitutions, b_to_v)
    row11_on_v = [substitute(poly, b_to_v) for poly in row11]
    row11_on_v = [poly for poly in row11_on_v if poly]
    row11_on_v_basis = span_basis(row11_on_v)
    c_initial = {
        (F6_CONSTANT, V[0]): Q(3, 4),
        (V[0], V[0]): Q(-3, 16),
    }
    g10_initial = {(V[0], V[0]): Q(3, 8)}
    expected_row11 = [
        add({(C_CARRIER,): Q(1)}, scale(c_initial, -1)),
        add({(106,): Q(1)}, scale(g10_initial, -1)),
    ]
    assert same_span(row11_on_v_basis, expected_row11)
    substitutions = compose_substitutions(substitutions, {
        C_CARRIER: c_initial,
        106: g10_initial,
    })

    # D12: compatibility is exactly (F6-V/2)^2 modulo H.
    row12, row12_log, row12_details = triangular_stage(
        data, 12, stages[12], substitutions
    )
    f6_minus_half_v = []
    for degree in range(11):
        poly = {(F6_CONSTANT - degree,): Q(1)}
        if degree <= 3:
            poly[(V[degree],)] = Q(-1, 2)
        f6_minus_half_v.append(poly)
    row12_model = mod_h(dense_mul(f6_minus_half_v, f6_minus_half_v))
    assert same_span(row12, row12_model)

    f6_to_w = {}
    c_w = c_times_parameter(W, 10)
    for degree in range(11):
        poly = dict(c_w[degree])
        if degree <= 3:
            poly = add(poly, {(V[degree],): Q(1, 2)})
        f6_to_w[F6_CONSTANT - degree] = poly
    substitutions = compose_substitutions(substitutions, f6_to_w)
    assert not [substitute(poly, f6_to_w) for poly in row12
                if substitute(poly, f6_to_w)]

    # D13: W^2 mod C is present, hence W=C*R on field points.
    row13, row13_log, row13_details = triangular_stage(
        data, 13, stages[13], substitutions
    )
    w_poly = [{(variable,): Q(1)} for variable in W]
    row13_mod_c = mod_c(dense_mul(w_poly, w_poly))
    row13_mod_c_witness = span_inclusion_certificate(row13, row13_mod_c)
    w_to_r = {W[degree]: poly
              for degree, poly in c_times_parameter(R, 6).items()}
    substitutions = compose_substitutions(substitutions, w_to_r)
    row13_on_r = [substitute(poly, w_to_r) for poly in row13]
    row13_on_r = [poly for poly in row13_on_r if poly]
    row13_on_r_basis = span_basis(row13_on_r)
    e13 = {
        (CHAR8, V[0]): Q(1),
        (B_CARRIER, V[0]): Q(-3, 4),
        (B_CARRIER, R[0]): Q(3, 2),
        (R[0], R[0]): Q(-3, 8),
    }
    assert row13_on_r_basis == [e13]

    # D14: all four coefficients of (F7-R/2)^2 mod C occur.
    row14, row14_log, row14_details = triangular_stage(
        data, 14, stages[14], substitutions
    )
    f7_minus_half_r = []
    for degree in range(10):
        poly = {(B_CARRIER - degree,): Q(1)}
        if degree <= 2:
            poly[(R[degree],)] = Q(-1, 2)
        f7_minus_half_r.append(poly)
    row14_mod_c = mod_c(dense_mul(f7_minus_half_r, f7_minus_half_r))
    row14_mod_c_witness = span_inclusion_certificate(row14, row14_mod_c)

    # F7=R/2+C*T, with T0=R0/2-b preserving b=p139 exactly.
    def t_form(degree):
        if degree == 0:
            return {(R[0],): Q(1, 2), (B_CARRIER,): Q(-1)}
        if 1 <= degree <= 5:
            return {(T[degree],): Q(1)}
        return {}

    f7_to_t = {}
    for degree in range(1, 10):
        poly = {(R[degree],): Q(1, 2)} if degree <= 2 else {}
        if 0 <= degree - 4 <= 5:
            poly = add(poly, t_form(degree - 4))
        if degree <= 5:
            poly = add(poly, scale(t_form(degree), -1))
        f7_to_t[B_CARRIER - degree] = poly
    substitutions = compose_substitutions(substitutions, f7_to_t)
    row14_on_t = [substitute(poly, f7_to_t) for poly in row14]
    row14_on_t = [poly for poly in row14_on_t if poly]
    row14_on_t_basis, row14_on_t_witness = span_basis_with_witness(row14_on_t)
    e14 = {
        (CHAR8, R[0]): Q(1),
        (B_CARRIER, B_CARRIER): Q(3, 4),
        (B_CARRIER, R[0]): Q(-3, 2),
        (R[0], R[0]): Q(3, 16),
    }
    assert row14_on_t_basis == [e13, e14]

    # D15: preserve a=p32.  This is the first compact honest later-row target.
    row15, row15_log, row15_details = triangular_stage(
        data, 15, [parameter for parameter in stages[15]
                   if parameter != A_CARRIER], substitutions
    )
    substitutions_through_d15 = dict(substitutions)
    cumulative_input = row14_on_t + row15
    cumulative_basis, cumulative_witness = span_basis_with_witness(cumulative_input)
    assert len(cumulative_basis) == 12

    # Keep c as a literal carrier.  The monic relation is exact after the
    # field-radical parameterizations; no unit normalization is used.
    c_formula = {
        (V[0], V[0]): Q(3, 16),
        (V[0], R[0]): Q(3, 4),
    }
    c_relation = add({(C_CARRIER,): Q(1)}, scale(c_formula, -1))
    endpoint = {
        (): Q(1),
        (A_CARRIER, B_CARRIER): Q(1),
        (C_CARRIER, D_CARRIER): Q(-1),
    }
    target_polys = cumulative_basis + [c_relation, endpoint]
    operative = sorted({variable for poly in target_polys
                        for monomial in poly for variable in monomial})
    assert len(operative) == 23
    assert max(len(monomial) for poly in target_polys for monomial in poly) == 3

    # Monic contraction of c is exact and retained only as a secondary target.
    contracted_polys = [substitute(poly, {C_CARRIER: c_formula})
                        for poly in cumulative_basis + [endpoint]]
    contracted_operative = sorted({variable for poly in contracted_polys
                                   for monomial in poly for variable in monomial})
    assert len(contracted_operative) == 22

    # The exact Q-linear projection onto the six-symbol invariant core is
    # proper.  A rational point rules out a spurious core-only unit claim.
    core_allowed = {A_CARRIER, B_CARRIER, CHAR8, V[0], R[0]}
    core_projection = span_intersection(cumulative_basis, core_allowed)
    assert len(core_projection) == 3
    projected_point = {
        A_CARRIER: Q(144),
        B_CARRIER: Q(-1, 144),
        CHAR8: Q(-1, 256),
        V[0]: Q(-1, 24),
        R[0]: Q(-1, 144),
        C_CARRIER: Q(5, 9216),
        D_CARRIER: Q(0),
    }
    assert all(evaluate(poly, projected_point) == 0 for poly in core_projection)
    assert evaluate(c_relation, projected_point) == 0
    assert evaluate(endpoint, projected_point) == 0

    # Regression: deleting V0^2 from c changes both the carrier relation and
    # the contracted endpoint by a named nonzero monomial.
    mutated_c_formula = {(V[0], R[0]): Q(3, 4)}
    c_formula_difference = add(c_formula, scale(mutated_c_formula, -1))
    assert c_formula_difference == {(V[0], V[0]): Q(3, 16)}
    contracted_endpoint = substitute(endpoint, {C_CARRIER: c_formula})
    mutated_endpoint = substitute(endpoint, {C_CARRIER: mutated_c_formula})
    endpoint_difference = add(contracted_endpoint, scale(mutated_endpoint, -1))
    assert endpoint_difference == {
        tuple(sorted((D_CARRIER, V[0], V[0]))): Q(-3, 16)
    }

    # D14+D15 force T^2=0 modulo C.  On field points C is squarefree, so
    # T=C*Q.  Preserve b: Q0=b-r/2, leaving q1 as the sole free coefficient.
    t_poly = [t_form(degree) for degree in range(6)]
    t_square_mod_c = mod_c(dense_mul(t_poly, t_poly))
    t_square_witness = span_inclusion_certificate(cumulative_input,
                                                   t_square_mod_c)
    t_to_q = {
        T[0]: {(R[0],): Q(1, 2), (B_CARRIER,): Q(-1)},
        T[1]: {(Q7[1],): Q(-1)},
        T[2]: {},
        T[3]: {},
        T[4]: {(B_CARRIER,): Q(1), (R[0],): Q(-1, 2)},
        T[5]: {(Q7[1],): Q(1)},
    }
    substitutions = compose_substitutions(substitutions, t_to_q)
    post_d15 = [substitute(poly, t_to_q) for poly in row15]
    post_d15 = [poly for poly in post_d15 if poly]
    post_d15_basis = span_basis(post_d15)
    e15 = {
        (CHAR8, B_CARRIER): Q(1),
        (B_CARRIER, B_CARRIER): Q(-3, 4),
        (V[0], V[0], V[0]): Q(-1, 8),
    }
    assert len(post_d15) == 9
    assert same_span(post_d15_basis, [e15, e13, e14,
                                      post_d15_basis[0]])
    assert len(post_d15_basis) == 4

    # p129=F8[X^0] is an exact additive weight-eight gauge: it is absent from
    # every literal D10,...,D22 generator.  The slice p129=0 meets every
    # additive-gauge orbit and does not touch an endpoint carrier.
    assert all(129 not in monomial
               for record in data["constraints"]
               for monomial, _coefficient in record["terms"])
    substitutions = compose_substitutions(substitutions, {129: {}})

    row16, row16_log, row16_details = triangular_stage(
        data, 16, stages[16], substitutions
    )
    row17, row17_log, row17_details = triangular_stage(
        data, 17, stages[17], substitutions
    )
    row18, row18_log, row18_details = triangular_stage(
        data, 18, stages[18], substitutions
    )

    # The first new invariant core equation is a literal cumulative
    # compatibility consequence at D17.
    k17 = {
        (B_CARRIER, V[0], V[0]): Q(1),
        (V[0], R[0], R[0]): Q(1),
    }
    through_d17 = post_d15 + row16 + row17
    k17_witness = linear_combination_witness(through_d17, k17)
    invariant_allowed = {B_CARRIER, CHAR8, V[0], R[0]}
    invariant_d17 = span_intersection(through_d17, invariant_allowed)
    assert len(invariant_d17) == 4
    assert same_span(invariant_d17, [e15, e13, e14, k17])

    # Closed field branch v=0: a completely division-free unit certificate.
    # First record the useful polynomial identity valid before taking the
    # branch, then lift the geometric-series unit through the monic c relation.
    b_poly_scalar = {(B_CARRIER,): Q(1)}
    r_poly_scalar = {(R[0],): Q(1)}
    v_poly_scalar = {(V[0],): Q(1)}
    a_cubed = {(A_CARRIER, A_CARRIER, A_CARRIER): Q(1)}
    b_cubed = {(B_CARRIER, B_CARRIER, B_CARRIER): Q(1)}
    core_b3_rhs = add(
        add(mul(scale(b_poly_scalar, 2), e13),
            mul(scale(b_poly_scalar, 4), e14)),
        add(mul(scale(add(scale(r_poly_scalar, 4),
                          scale(v_poly_scalar, 2)), -1), e15),
            scale(mul(mul(mul(v_poly_scalar, v_poly_scalar),
                              v_poly_scalar),
                      add(scale(v_poly_scalar, Q(1, 4)),
                          scale(r_poly_scalar, Q(1, 2)))), -1)),
    )
    assert core_b3_rhs == scale(b_cubed, 3)
    x_ab = {(A_CARRIER, B_CARRIER): Q(1)}
    geometric = add(add({(): Q(1)}, scale(x_ab, -1)), mul(x_ab, x_ab))
    c_multiple = add(scale(v_poly_scalar, Q(3, 16)),
                     scale(r_poly_scalar, Q(3, 4)))
    v0_generators = [endpoint, c_relation, e13, e14, e15, v_poly_scalar]
    v0_cofactors = [
        geometric,
        mul(geometric, {(D_CARRIER,): Q(1)}),
        mul(scale(a_cubed, Q(-2, 3)), b_poly_scalar),
        mul(scale(a_cubed, Q(-4, 3)), b_poly_scalar),
        mul(scale(a_cubed, Q(1, 3)),
            add(scale(r_poly_scalar, 4), scale(v_poly_scalar, 2))),
        add(
            mul(mul(geometric, {(D_CARRIER,): Q(1)}), c_multiple),
            mul(
                scale(a_cubed, Q(1, 3)),
                mul(
                    mul(v_poly_scalar, v_poly_scalar),
                    add(scale(v_poly_scalar, Q(1, 4)),
                        scale(r_poly_scalar, Q(1, 2))),
                ),
            ),
        ),
    ]
    v0_reconstruction = {}
    for generator, cofactor in zip(v0_generators, v0_cofactors):
        v0_reconstruction = add(v0_reconstruction, mul(generator, cofactor))
    assert v0_reconstruction == {(): Q(1)}

    # Open field branch v!=0.  With tau=r/v, K17 and E13--E15 reduce every
    # solution to the irreducible quadratic 12*tau^2+6*tau+1=0 and the four
    # linear forms below.  Keeping the quotient field intact covers both
    # conjugate roots without choosing either one.
    tau = {(QUADRATIC_T,): Q(1)}
    branch_substitutions = {
        V[0]: scale(tau, Q(1, 24)),
        R[0]: add(scale(tau, Q(-1, 48)), {(): Q(-1, 288)}),
        B_CARRIER: add(scale(tau, Q(-1, 144)), {(): Q(-1, 576)}),
        CHAR8: add(scale(tau, Q(-1, 192)), {(): Q(-7, 4608)}),
    }
    branch_c = add(scale(tau, Q(1, 18432)), {(): Q(1, 36864)})
    for core_poly in (e13, e14, e15, k17):
        assert not quadratic_reduce(substitute(core_poly,
                                               branch_substitutions))
    assert quadratic_reduce(substitute(c_formula, branch_substitutions)) == branch_c
    live_quadratic = {
        (QUADRATIC_T, QUADRATIC_T): Q(12),
        (QUADRATIC_T,): Q(6),
        (): Q(1),
    }
    assert not quadratic_reduce(live_quadratic)

    detail_by_row = {15: row15_details, 16: row16_details,
                     17: row17_details, 18: row18_details}
    branch_base = []
    for row_number, polys in ((15, post_d15), (16, row16),
                              (17, row17), (18, row18)):
        for local_index, poly in enumerate(polys):
            reduced_poly = quadratic_reduce(substitute(poly,
                                                       branch_substitutions))
            if reduced_poly:
                branch_base.append({
                    "row": row_number,
                    "compatibility_index": local_index,
                    "pre_branch": poly,
                    "reduced": reduced_poly,
                })

    def expanded_rows(maximum_row, constant=Q(1)):
        expanded = []
        labels = []
        for record in branch_base:
            if record["row"] > maximum_row:
                continue
            # Re-reduce from the pre-branch polynomial so the q-constant
            # mutation exercises the complete branch quotient.
            base = quadratic_reduce(substitute(record["pre_branch"],
                                               branch_substitutions), constant)
            if not base:
                continue
            expanded.append(base)
            labels.append((record["row"], record["compatibility_index"], 0))
            expanded.append(quadratic_reduce(mul(base, tau), constant))
            labels.append((record["row"], record["compatibility_index"], 1))
        return expanded, labels

    expanded16, labels16 = expanded_rows(16)
    expanded17, labels17 = expanded_rows(17)
    expanded18, labels18 = expanded_rows(18)
    assert (len(branch_base), len(expanded16), len(expanded17),
            len(expanded18)) == (56, 44, 78, 112)
    assert (len(span_basis(expanded16)), len(span_basis(expanded17)),
            len(span_basis(expanded18))) == (20, 38, 58)
    assert not span_contains(expanded16, {(): Q(1)})
    assert not span_contains(expanded17, {(): Q(1)})
    assert span_contains(expanded18, {(): Q(1)})
    d18_unit_witness = linear_combination_witness(expanded18, {(): Q(1)})
    nonzero_d18_witness = [
        (label, coefficient)
        for label, coefficient in zip(labels18, d18_unit_witness)
        if coefficient
    ]
    expected_d18_witness = [
        ((16, 4, 0), Q(1119744)),
        ((16, 12, 1), Q(5038848)),
        ((16, 16, 1), Q(10077696)),
        ((17, 1, 0), Q(-85847040, 7)),
        ((17, 1, 1), Q(-386311680, 7)),
        ((17, 5, 0), Q(-2985984)),
        ((17, 5, 1), Q(-13436928)),
        ((18, 2, 0), Q(103514112, 7)),
        ((18, 2, 1), Q(465813504, 7)),
        ((18, 6, 0), Q(7962624)),
        ((18, 6, 1), Q(35831808)),
        ((18, 10, 0), Q(23887872, 7)),
        ((18, 10, 1), Q(107495424, 7)),
    ]
    assert nonzero_d18_witness == expected_d18_witness
    d18_reconstruction = {}
    for coefficient, poly in zip(d18_unit_witness, expanded18):
        d18_reconstruction = add(d18_reconstruction, scale(poly, coefficient))
    assert d18_reconstruction == {(): Q(1)}

    # Group the 13 rational rows into eight K-linear cofactors c0+c1*tau.
    grouped = {}
    for (row_number, local_index, multiplier), coefficient in nonzero_d18_witness:
        pair = grouped.setdefault((row_number, local_index), [Q(0), Q(0)])
        pair[multiplier] += coefficient
    grouped_witness = []
    for (row_number, local_index), (c0, c1) in sorted(grouped.items()):
        base_record = next(record for record in branch_base
                           if record["row"] == row_number
                           and record["compatibility_index"] == local_index)
        assert row_number in (16, 17, 18)
        grouped_witness.append({
            "row": row_number,
            "compatibility_index": local_index,
            "K_cofactor_c0_plus_c1_tau": [str(c0), str(c1)],
            "pre_branch_terms": encode(base_record["pre_branch"]),
            "quadratic_reduced_terms": encode(base_record["reduced"]),
            "quadratic_reduced_sha256": hashlib.sha256(
                compact(encode(base_record["reduced"]))).hexdigest(),
            "literal_source_provenance": detail_by_row[row_number][local_index],
        })
    assert len(grouped_witness) == 8

    # Live mutations: omitting a charged cofactor, corrupting the quadratic's
    # constant sign, or omitting all tau multiples must destroy this replay.
    omitted_reconstruction = add(
        d18_reconstruction,
        scale(expanded18[labels18.index(nonzero_d18_witness[0][0])],
              -nonzero_d18_witness[0][1]),
    )
    assert omitted_reconstruction != {(): Q(1)}
    mutated_expanded18, mutated_labels18 = expanded_rows(18, Q(-1))
    assert mutated_labels18 == labels18
    mutated_reconstruction = {}
    for coefficient, poly in zip(d18_unit_witness, mutated_expanded18):
        mutated_reconstruction = add(mutated_reconstruction,
                                     scale(poly, coefficient))
    assert mutated_reconstruction != {(): Q(1)}
    q_only_rows = [record["reduced"] for record in branch_base]
    assert not span_contains(q_only_rows, {(): Q(1)})

    v0_certificate = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL5-V0-ZERO-UNIT-v1",
        "branch_generator": "V0=0",
        "generators_in_order": [
            "endpoint 1+a*b-c*d", "monic c reconstruction", "E13", "E14",
            "E15", "V0",
        ],
        "generator_terms": [encode(poly) for poly in v0_generators],
        "cofactor_terms": [encode(poly) for poly in v0_cofactors],
        "reconstruction": encode(v0_reconstruction),
        "core_identity": {
            "formula": "3*b^3=2*b*E13+4*b*E14-(4*r+2*v)*E15-v^3*(v/4+r/2)",
            "left": encode(scale(b_cubed, 3)),
            "right": encode(core_b3_rhs),
        },
        "normalization_or_localization": False,
    }
    d18_certificate = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL5-V-NONZERO-D18-K-UNIT-v1",
        "field": "K=Q[tau]/(12*tau^2+6*tau+1)",
        "field_semantics": "discriminant -12 is not a square in Q; K is a quadratic field and retains both conjugate roots",
        "branch_hypothesis": "V0!=0; tau=R0/V0",
        "branch_substitutions": {
            "V0": encode(branch_substitutions[V[0]]),
            "R0": encode(branch_substitutions[R[0]]),
            "b": encode(branch_substitutions[B_CARRIER]),
            "e": encode(branch_substitutions[CHAR8]),
            "c": encode(branch_c),
        },
        "quadratic": encode(live_quadratic),
        "base_compatibility_counts_through_D16_D17_D18": [22, 39, 56],
        "expanded_Q_row_counts_through_D16_D17_D18": [44, 78, 112],
        "expanded_Q_ranks_through_D16_D17_D18": [20, 38, 58],
        "unit_first_appears_at": "D18",
        "grouped_K_linear_witness": grouped_witness,
        "expanded_nonzero_Q_witness": [
            {"row": row, "compatibility_index": index,
             "tau_multiplier": multiplier, "coefficient": str(coefficient)}
            for (row, index, multiplier), coefficient in nonzero_d18_witness
        ],
        "reconstruction": encode(d18_reconstruction),
        "endpoint_used": False,
        "D19_or_later_used": False,
        "carrier_normalization_or_localization": False,
        "mutations": {
            "omit_first_nonzero_cofactor": {
                "result_terms": encode(omitted_reconstruction),
                "detected": True,
            },
            "replace_quadratic_constant_plus_one_by_minus_one": {
                "result_terms": encode(mutated_reconstruction),
                "detected": True,
            },
            "omit_all_tau_multiple_rows": {
                "unit_in_Q_span": False,
                "detected": True,
            },
        },
    }

    target = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL5-D14-D15-CARRIER-TARGET-v1",
        "scope": "necessary field-radical subsystem of the fixed cutoff-five square tail",
        "endpoint_carriers": {
            "a": "p32=G15[X^1]",
            "b": "p139=F7[X^0]",
            "c": "p86=G11[X^0]",
            "d": "p91=F11[X^1]",
            "equation": "1+a*b-c*d=0",
        },
        "operative_variables": operative,
        "operative_variable_count": len(operative),
        "constraint_count": len(target_polys),
        "maximum_degree": 3,
        "constraints": constraint_records(target_polys),
        "basis_witness_in_post_D14_then_D15_compatibilities": [
            [[index, str(value)] for index, value in enumerate(vector) if value]
            for vector in cumulative_witness
        ],
        "post_D14_displayed_count": len(row14_on_t),
        "D15_displayed_count": len(row15),
        "warning": "field-radical necessary subsystem; not a nonreduced-scheme equivalence",
    }
    contracted_target = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL5-D14-D15-MONIC-C-CONTRACTION-v1",
        "source_carrier_target": target["schema"],
        "contraction": "eliminate p86 by the monic c relation; no localization",
        "operative_variables": contracted_operative,
        "operative_variable_count": len(contracted_operative),
        "constraint_count": len(contracted_polys),
        "maximum_degree": max(len(monomial) for poly in contracted_polys
                              for monomial in poly),
        "constraints": constraint_records(contracted_polys),
    }

    raw_lifts = {}
    for parameter in (A_CARRIER, C_CARRIER, D_CARRIER, CHAR8, B_CARRIER,
                      F6_CONSTANT, F5_CONSTANT):
        raw_lifts[f"p{parameter}"] = data["nullspace_basis"][parameter]

    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL5-DESK-ANALYSIS-v2",
        "source_tail_compile_sha256": hashlib.sha256(pretty(data)).hexdigest(),
        "prefix": {
            "retained_variables": 252,
            "generator_count_through_D9": 201,
            "rank": 89,
            "nullity": 163,
            "remaining_D10_through_D22_generators": 312,
        },
        "literal_endpoint": {
            "equation": "D22[X^0]-1=-1-p32*p139+p86*p91",
            "determinant_form": "1+p32*p139-p86*p91=0",
            "individual_unit_conclusion": "none",
            "cover_consequence": "(p139,p86)=(1) and (p32,p91)=(1) pointwise",
        },
        "raw_core_lifts": raw_lifts,
        "synthetic_core_lifts": {
            "V0": "p162=F5[X^0]",
            "R0": "p150-p162/2=F6[X^0]-F5[X^0]/2",
            "p120": "weight-eight characteristic coordinate; see exact raw lift",
        },
        "stage_logs": [row10_plain_log, row10_log, row11_log, row12_log,
                       row13_log, row14_log, row15_log, row16_log, row17_log,
                       row18_log],
        "field_radical_cascade": [
            "D10: H divides F5^2, hence C divides F5 and F5=C*B",
            "D11: C divides B^2, hence B=C*V and F5=H*V",
            "D12: H divides (F6-V/2)^2, hence F6=V/2+C*W",
            "D13: C divides W^2, hence W=C*R",
            "D14: C divides (F7-R/2)^2, hence F7=R/2+C*T",
            "D14+D15: C divides T^2, hence T=C*Q",
        ],
        "structural_certificates": {
            "D10_F5_square_mod_H": {
                "model": [encode(poly) for poly in row10_model],
                "same_span": True,
            },
            "D11_B_square_mod_C": {
                "model": [encode(poly) for poly in row11_mod_c],
                "source_witness": row11_mod_c_witness,
            },
            "D11_after_B_equals_CV": [encode(poly) for poly in expected_row11],
            "D12_F6_minus_half_V_square_mod_H": {
                "model": [encode(poly) for poly in row12_model],
                "same_span": True,
            },
            "D13_W_square_mod_C": {
                "model": [encode(poly) for poly in row13_mod_c],
                "source_witness": row13_mod_c_witness,
            },
            "D13_scalar_E13": encode(e13),
            "D14_F7_minus_half_R_square_mod_C": {
                "model": [encode(poly) for poly in row14_mod_c],
                "source_witness": row14_mod_c_witness,
            },
            "D14_scalars_after_F7_parameterization": [encode(e13), encode(e14)],
            "D14_D15_T_square_mod_C": {
                "model": [encode(poly) for poly in t_square_mod_c],
                "source_witness": t_square_witness,
            },
            "D15_D17_invariant_core": {
                "basis": [encode(poly) for poly in invariant_d17],
                "expected_span": [encode(poly) for poly in
                                  (e15, e13, e14, k17)],
                "K17": encode(k17),
                "K17_witness_in_post_D15_then_D16_then_D17": [
                    [index, str(value)] for index, value
                    in enumerate(k17_witness) if value
                ],
            },
        },
        "compatibility_source_provenance": {
            "D10_plain": row10_plain_details,
            "D10_after_F5_parameterization": row10_details,
            "D11": row11_details,
            "D12": row12_details,
            "D13": row13_details,
            "D14": row14_details,
            "D15": row15_details,
            "D16": row16_details,
            "D17": row17_details,
            "D18": row18_details,
            "post_D14_basis_witness": [
                [[index, str(value)] for index, value in enumerate(vector) if value]
                for vector in row14_on_t_witness
            ],
        },
        "carrier_formula": {
            "p86": encode(c_formula),
            "formula": "p86=(3/16)*V0*(V0+4*R0)",
        },
        "mutation_regression": {
            "mutation": "drop the V0^2 term and use p86=(3/4)*V0*R0",
            "c_formula_difference": encode(c_formula_difference),
            "contracted_endpoint_difference": encode(endpoint_difference),
            "status": "PASS_MUTATION_DETECTED",
        },
        "core_projection": {
            "allowed": sorted(core_allowed),
            "rank": len(core_projection),
            "constraints": [encode(poly) for poly in core_projection],
            "exact_rational_point": {
                variable_name(variable): str(value)
                for variable, value in sorted(projected_point.items())
            },
            "conclusion": "proper; the invariant core plus endpoint alone is not a unit",
        },
        "additive_gauge": {
            "coordinate": "p129=F8[X^0]",
            "literal_occurrence_count_in_D10_through_D22": 0,
            "slice": "p129=0",
            "type": "global additive Ga quotient; not a carrier normalization",
            "regression": "reintroducing p129 leaves every literal constraint unchanged",
        },
        "field_cover_conclusion": {
            "V0_equals_zero": "exact division-free unit using endpoint, monic c reconstruction, E13--E15, and V0",
            "V0_nonzero": "K-linear literal compatibility unit at D18 after the exhaustive quadratic branch parameterization",
            "verdict": "no characteristic-zero field-valued endpoint point in the fixed cutoff-five specialization",
        },
        "v0_unit_certificate": v0_certificate,
        "v_nonzero_D18_K_unit_certificate": d18_certificate,
        "carrier_target": target,
        "contracted_target": contracted_target,
        "parameter_substitutions_through_D15": {
            f"p{variable}": encode(poly)
            for variable, poly in sorted(substitutions_through_d15.items())
        },
        "firewalls": [
            "fixed branch-P square baseline and cutoff-five tail only",
            "every divisibility step is field-radical, not a nonreduced-scheme equality",
            "no endpoint carrier is normalized",
            "D23 is not imposed and G22 is absent",
            "the older D14-D15 targets remain proper preliminary custody artifacts",
            "the final exclusion is field-valued and uses the radical cover V0=0 or V0!=0",
            "the nonzero branch unit uses D16--D18 only and no endpoint equation",
            "no branch-P family, Keller-pair, counterexample, or JC2 conclusion",
        ],
    }


def build_payloads():
    data = compile_cutoff5()
    analysis = compile_analysis(data)
    carrier_sing = singular_text(analysis["carrier_target"]).encode()
    contracted_sing = singular_text(analysis["contracted_target"]).encode()
    analysis["emitted_target_sha256"] = {
        "TARGETS/tail5_d14_d15_endpoint_carrier_q.sing": hashlib.sha256(carrier_sing).hexdigest(),
        "TARGETS/tail5_d14_d15_endpoint_contracted_q.sing": hashlib.sha256(contracted_sing).hexdigest(),
    }
    source_manifest = (
        f"{RAW_SHA256}  ../ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json\n"
        f"{RAW_INPUT_SHA256}  ../ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json\n"
        f"{sha256(PREREGISTRATION)}  PREREGISTRATION.md\n"
        f"{sha256(Path(__file__))}  analyze_tail5.py\n"
    ).encode()
    payloads = {
        "TAIL5/TAIL_DEFORMATION_SYSTEM.json": pretty(data),
        "TAIL5_DESK_ANALYSIS.json": pretty(analysis),
        "CERTIFICATES/tail5_v0_unit.json": pretty(
            analysis["v0_unit_certificate"]),
        "CERTIFICATES/tail5_v_nonzero_D18_K_unit.json": pretty(
            analysis["v_nonzero_D18_K_unit_certificate"]),
        "TARGETS/tail5_d14_d15_endpoint_carrier_q.sing": carrier_sing,
        "TARGETS/tail5_d14_d15_endpoint_contracted_q.sing": contracted_sing,
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
        "verdict": "field-valued cutoff-five endpoint stratum empty",
        "v0_certificate": "division-free unit",
        "v_nonzero_certificate": "literal D16-D18 unit over Q[tau]/(12*tau^2+6*tau+1)",
        "preliminary_carrier_target": "23 variables, 14 generators, degree at most 3",
        "preliminary_contracted_target": "22 variables, 13 generators, degree at most 3",
        "local_CAS_used": False,
        "AWS_used": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
