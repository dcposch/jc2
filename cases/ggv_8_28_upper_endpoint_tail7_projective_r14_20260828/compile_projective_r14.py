#!/usr/bin/env python3
"""Compile the homogeneous row-14 obstruction for the full tail-7 chart."""

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
    "TAIL7_REDUCED/TAIL_DEFORMATION_SYSTEM.json"
)
SOURCE_SHA256 = "7edd5ccd471e9eb3e27f0f163b0b337e0fb5057126ec69869f988093defba7aa"
SHARED_BLOCK = ROOT / (
    "cases/ggv_8_28_upper_endpoint_tail7_branches_20260828/"
    "BRANCHES/shared_block.json"
)
SHARED_BLOCK_SHA256 = "3e586cc283526efa9c12f51f5be5535d31eaa1b03ee0296783438acabf9feaab"
COFACTOR_EXPRESSIONS = [
    "-1/44*p80*p81-5/66*p79*p82-7/66*p78*p83+2/33*p82*p83+1/44*p81*p84-3/44*p80*p85+29/132*p84*p85-7/33*p78+13/66*p82",
    "-1/36*p80*p82-1/18*p79*p83+1/18*p83^2-1/12*p78*p84+1/9*p82*p84+1/18*p81*p85+1/6*p85^2-1/9*p79+5/18*p83+11/36",
    "-5/156*p78*p81+5/156*p81*p82-1/78*p80*p83-1/26*p79*p84+2/13*p83*p84-5/52*p78*p85+9/52*p82*p85-1/39*p80+9/26*p84",
    "-1/84*p79*p81-1/21*p78*p82+1/21*p82^2+5/84*p81*p83+2/21*p84^2-1/28*p79*p85+19/84*p83*p85+11/84*p81+41/84*p85",
    "0", "0", "0", "0", "0", "0", "0", "0",
    "1/132*p80*p81-1/66*p79*p82-1/22*p78*p83+2/11*p82*p83+5/44*p81*p84+1/44*p80*p85+49/132*p84*p85-1/11*p78+25/66*p82",
    "1/36*p81^2+1/36*p80*p82+1/9*p83^2-1/36*p78*p84+2/9*p82*p84+1/6*p81*p85+1/4*p85^2+4/9*p83+4/9",
    "-1/156*p78*p81+17/156*p81*p82+1/26*p80*p83+1/78*p79*p84+10/39*p83*p84-1/52*p78*p85+47/156*p82*p85+1/13*p80+1/2*p84",
    "1/84*p79*p81+2/21*p82^2+11/84*p81*p83+1/21*p80*p84+1/7*p84^2+1/28*p79*p85+29/84*p83*p85+1/4*p81+55/84*p85",
]


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


def parameter_weight(basis_vector):
    weights = set()
    for name, _coefficient in basis_vector:
        kind, x_degree, y_degree = name.split("_")
        offset = 8 if kind == "f" else 12
        weights.add(offset + 3 * int(x_degree) - int(y_degree))
    assert max(weights) - min(weights) <= 3
    return min(weights)


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


def compile_localization_certificate(source):
    """Keep p32,p87 symbolic and derive a row-21 localization relation."""
    weights = {
        parameter: parameter_weight(vector)
        for parameter, vector in enumerate(source["nullspace_basis"])
    }
    assert weights[32] == 15 and weights[87] == 7
    constraints_by_row = {}
    for record in source["constraints"]:
        constraints_by_row.setdefault(int(record["row"]), []).append({
            "x_degree": int(record["x_degree"]),
            "poly": decode(record["terms"]),
        })

    substitutions = {}
    logs = []
    simple_relation = {(86, 87, 87): Q(-3, 4)}
    simple_index = None
    row21_hashes = []
    for row_number in range(14, 22):
        new_parameters = sorted(
            parameter for parameter, weight in weights.items()
            if weight == row_number
            and parameter not in substitutions
            and parameter not in (32, 87)
        )
        rows = []
        for record in constraints_by_row[row_number]:
            poly = substitute(record["poly"], substitutions)
            coefficients = [Q(0)] * len(new_parameters)
            residual = {}
            for monomial, coefficient in poly.items():
                hits = [variable for variable in monomial
                        if variable in new_parameters]
                if hits:
                    assert len(hits) == 1 and monomial == (hits[0],)
                    coefficients[new_parameters.index(hits[0])] += coefficient
                else:
                    residual[monomial] = coefficient
            rows.append((coefficients, residual))
        reduced, pivots = rref(rows, len(new_parameters))
        free_columns = [column for column in range(len(new_parameters))
                        if column not in set(pivots)]
        for pivot_row, pivot_column in enumerate(pivots):
            coefficients, residual = reduced[pivot_row]
            solution = scale(residual, -1)
            for free_column in free_columns:
                if coefficients[free_column]:
                    solution = add(solution, {
                        (new_parameters[free_column],): -coefficients[free_column]
                    })
            substitutions[new_parameters[pivot_column]] = solution
        compatibility = [residual for coefficients, residual
                         in reduced[len(pivots):] if residual]
        compatibility_hashes = [
            hashlib.sha256(compact(encode(poly))).hexdigest()
            for poly in compatibility
        ]
        if row_number == 21:
            row21_hashes = compatibility_hashes
            matches = [index for index, poly in enumerate(compatibility)
                       if poly == simple_relation]
            assert matches == [1]
            simple_index = matches[0]
        logs.append({
            "row": row_number,
            "equation_count": len(rows),
            "new_parameters": new_parameters,
            "rank": len(pivots),
            "free_parameters": [new_parameters[column]
                                for column in free_columns],
            "compatibility_count": len(compatibility),
            "compatibility_sha256s": compatibility_hashes,
        })

    endpoint = [record for record in constraints_by_row[22]
                if record["x_degree"] == 0]
    assert len(endpoint) == 1
    endpoint_poly = substitute(endpoint[0]["poly"], substitutions)
    assert endpoint_poly == {(): Q(-1), (32, 87): Q(-1)}
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL7-LOCALIZATION-CERTIFICATE-v1",
        "source_tail7_sha256": SOURCE_SHA256,
        "held_nonpivots": [32, 87],
        "row_elimination": logs,
        "row21_simple_compatibility_index": simple_index,
        "row21_simple_compatibility_terms": encode(simple_relation),
        "row21_compatibility_sha256s": row21_hashes,
        "endpoint_constant_terms": encode(endpoint_poly),
        "field_consequence": (
            "endpoint gives p32*p87=-1, hence p87!=0; "
            "row21 gives -(3/4)*p86*p87^2=0, hence p86=0"
        ),
        "scope": "field-valued tail7 endpoint stratum; no scheme claim",
    }


def compile_objects():
    assert sha256(SOURCE) == SOURCE_SHA256
    assert sha256(SHARED_BLOCK) == SHARED_BLOCK_SHA256
    source = json.loads(SOURCE.read_text())
    row14 = [record for record in source["constraints"]
             if int(record["row"]) == 14]
    assert len(row14) == 26
    new_parameters = list(range(33, 44))
    rows = []
    for record in row14:
        coefficients = [Q(0)] * len(new_parameters)
        residual = {}
        for monomial, coefficient in decode(record["terms"]).items():
            hits = [variable for variable in monomial if variable in new_parameters]
            if hits:
                assert len(hits) == 1 and monomial == (hits[0],)
                coefficients[new_parameters.index(hits[0])] += coefficient
            else:
                residual[monomial] = coefficient
        rows.append((coefficients, residual))
    reduced, pivots = rref(rows, len(new_parameters))
    assert len(pivots) == 10
    assert [new_parameters[column] for column in range(len(new_parameters))
            if column not in set(pivots)] == [43]
    compatibility = [residual for coefficients, residual in reduced[len(pivots):]
                     if residual]
    assert len(compatibility) == 16
    assert all(all(len(monomial) == 2 for monomial in poly)
               for poly in compatibility)
    assert set(variable for poly in compatibility for monomial in poly
               for variable in monomial) == set(range(78, 88))

    homogeneous_records = []
    dehom_records = []
    localized_records = []
    for index, poly in enumerate(compatibility):
        encoded = encode(poly)
        homogeneous_records.append({
            "index": index,
            "degree": 2,
            "term_count": len(poly),
            "terms": encoded,
            "sha256": hashlib.sha256(compact(encoded)).hexdigest(),
        })
        dehom = substitute(poly, {87: {(): Q(1)}})
        encoded_dehom = encode(dehom)
        dehom_records.append({
            "index": index,
            "degree": max(len(monomial) for monomial in dehom),
            "term_count": len(dehom),
            "terms": encoded_dehom,
            "sha256": hashlib.sha256(compact(encoded_dehom)).hexdigest(),
        })
        localized = substitute(poly, {87: {(): Q(1)}, 86: {(): Q(0)}})
        encoded_localized = encode(localized)
        localized_records.append({
            "index": index,
            "degree": degree(localized),
            "term_count": len(localized),
            "terms": encoded_localized,
            "sha256": hashlib.sha256(compact(encoded_localized)).hexdigest(),
        })

    endpoint = [record for record in source["constraints"]
                if int(record["row"]) == 22 and int(record["x_degree"]) == 0]
    assert len(endpoint) == 1
    assert endpoint[0]["terms"] == [[[], "-1"], [[32, 87], "-1"]]
    homogeneous = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL7-R14-HOMOGENEOUS-v1",
        "source_tail7_sha256": SOURCE_SHA256,
        "row14_equations": 26,
        "row14_same_row_parameters": new_parameters,
        "row14_same_row_rank": len(pivots),
        "row14_free_mode": 43,
        "f7_parameters": list(range(78, 88)),
        "compatibility_count": len(homogeneous_records),
        "compatibility": homogeneous_records,
        "endpoint_constant_equation": "-1-p32*p87=0",
        "consequence": "every endpoint field point has p87 nonzero",
    }
    dehomogeneous = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL7-R14-P87-ONE-v1",
        "homogeneous_source_pending_sha256": None,
        "specialization": "p87=1 inside the homogeneous necessary row14 subsystem",
        "parameters": list(range(78, 87)),
        "parameter_count": 9,
        "constraint_count": len(dehom_records),
        "constraints": dehom_records,
        "scope": "necessary projective row14 chart; no full-system scaling claimed",
    }
    shared = json.loads(SHARED_BLOCK.read_text())
    localized_terms = [record["terms"] for record in localized_records]
    shared_terms = [record["terms"] for record in shared["constraints"]]
    assert localized_terms == shared_terms
    ordered_terms_payload = compact(localized_terms)
    localized = {
        "schema": "GGV-8_28-UPPER-ENDPOINT-TAIL7-R14-P87-ONE-P86-ZERO-v1",
        "homogeneous_source_pending_sha256": None,
        "specialization": "p87=1 and p86=0 in the necessary row14 subsystem",
        "parameters": list(range(78, 86)),
        "parameter_count": 8,
        "constraint_count": len(localized_records),
        "constraints": localized_records,
        "ordered_terms_sha256": hashlib.sha256(ordered_terms_payload).hexdigest(),
        "byte_identical_ordered_terms_to_shared_block": True,
        "shared_block_sha256": SHARED_BLOCK_SHA256,
        "scope": "necessary localized row14 block for every tail7 endpoint field point",
    }
    localization_certificate = compile_localization_certificate(source)
    return homogeneous, dehomogeneous, localized, localization_certificate


def expression(poly):
    pieces = []
    for monomial, coefficient in sorted(poly.items()):
        atom = "*".join(f"p{variable}" for variable in monomial) or "1"
        pieces.append(f"({coefficient})*{atom}")
    return "+".join(pieces) or "0"


def singular_text(dehomogeneous, characteristic=0):
    variables = [f"p{parameter}" for parameter in dehomogeneous["parameters"]]
    polys = [decode(record["terms"]) for record in dehomogeneous["constraints"]]
    return "\n".join([
        f"ring r14={characteristic},({','.join(variables)}),dp;",
        "option(redSB);",
        "ideal I=",
        ",\n".join(expression(poly) for poly in polys) + ";",
        'print("R14_P87_ONE variables="+string(nvars(basering))+" generators="+string(size(I)));',
        'print("START_SLIMGB");',
        "int start_time=timer;",
        "ideal J=slimgb(I);",
        'print("END_SLIMGB seconds="+string(timer-start_time));',
        'print("BASIS_SIZE="+string(size(J)));',
        "int is_unit=(size(J)==1 && J[1]==1);",
        'print("UNIT="+string(is_unit));',
        "J;",
        "quit;",
        "",
    ])


def nullstellensatz_text(localized):
    variables = [f"p{parameter}" for parameter in localized["parameters"]]
    polys = [decode(record["terms"]) for record in localized["constraints"]]
    return "\n".join([
        f"ring cert=0,({','.join(variables)}),dp;",
        "option(redSB);",
        "option(redTail);",
        "ideal I=",
        ",\n".join(expression(poly) for poly in polys) + ";",
        'print("NULLSTELLENSATZ variables="+string(nvars(basering))+" generators="+string(size(I)));',
        "matrix T;",
        "int start_time=timer;",
        'ideal J=liftstd(I,T,"slimgb");',
        'print("END_LIFTSTD seconds="+string(timer-start_time));',
        'print("BASIS_SIZE="+string(size(J)));',
        "matrix delta=matrix(J)-matrix(I)*T;",
        "int unit_ok=(size(J)==1 && deg(J[1])==0 && J[1]!=0);",
        "int transform_ok=(size(ideal(delta))==0);",
        "number unit_scalar=leadcoef(J[1]);",
        "poly direct_identity=0;",
        "for (int k=1;k<=nrows(T);k++) { direct_identity=direct_identity+I[k]*(T[k,1]/unit_scalar); }",
        "int identity_ok=(unit_ok && transform_ok && direct_identity==1);",
        'print("UNIT="+string(unit_ok));',
        'print("TRANSFORM_OK="+string(transform_ok));',
        'print("DIRECT_IDENTITY_OK="+string(identity_ok));',
        'print("UNIT_SCALAR="+string(unit_scalar));',
        'print("J[1]="+string(J[1]));',
        'print("COFACTORS_BEGIN");',
        'for (int i=1;i<=nrows(T);i++) { print("H["+string(i)+"]="+string(T[i,1]/unit_scalar)); }',
        'print("COFACTORS_END");',
        "quit;",
        "",
    ])


def nullstellensatz_replay_text(localized):
    assert len(COFACTOR_EXPRESSIONS) == localized["constraint_count"] == 16
    variables = [f"p{parameter}" for parameter in localized["parameters"]]
    polys = [decode(record["terms"]) for record in localized["constraints"]]
    declarations = [f"poly h{index}={cofactor};"
                    for index, cofactor in enumerate(COFACTOR_EXPRESSIONS, 1)]
    summands = "+".join(f"h{index}*I[{index}]" for index in range(1, 17))
    return "\n".join([
        f"ring replay=0,({','.join(variables)}),dp;",
        "ideal I=",
        ",\n".join(expression(poly) for poly in polys) + ";",
        *declarations,
        f"poly lhs={summands};",
        'print("DIRECT_REPLAY_LHS="+string(lhs));',
        'print("DIRECT_REPLAY_OK="+string(lhs==1));',
        "quit;",
        "",
    ])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    homogeneous, dehomogeneous, localized, certificate = compile_objects()
    homogeneous_payload = pretty(homogeneous)
    homogeneous_sha = hashlib.sha256(homogeneous_payload).hexdigest()
    dehomogeneous["homogeneous_source_pending_sha256"] = homogeneous_sha
    localized["homogeneous_source_pending_sha256"] = homogeneous_sha
    payloads = {
        "R14_HOMOGENEOUS.json": homogeneous_payload,
        "R14_P87_ONE.json": pretty(dehomogeneous),
        "R14_P87_ONE_P86_ZERO.json": pretty(localized),
        "LOCALIZATION_CERTIFICATE.json": pretty(certificate),
        "r14_p87_one_q.sing": singular_text(dehomogeneous).encode(),
        "r14_p87_one_p65521.sing": singular_text(dehomogeneous, 65521).encode(),
        "r14_nullstellensatz_q.sing": nullstellensatz_text(localized).encode(),
        "r14_nullstellensatz_replay_q.sing":
            nullstellensatz_replay_text(localized).encode(),
    }
    for name, payload in payloads.items():
        (args.output / name).write_bytes(payload)
    print(json.dumps({
        "status": "PASS",
        "homogeneous_sha256": homogeneous_sha,
        "dehomogeneous_sha256": hashlib.sha256(payloads["R14_P87_ONE.json"]).hexdigest(),
        "q_sha256": hashlib.sha256(payloads["r14_p87_one_q.sing"]).hexdigest(),
        "modp_sha256": hashlib.sha256(payloads["r14_p87_one_p65521.sing"]).hexdigest(),
        "localized_sha256": hashlib.sha256(
            payloads["R14_P87_ONE_P86_ZERO.json"]
        ).hexdigest(),
        "certificate_sha256": hashlib.sha256(
            payloads["LOCALIZATION_CERTIFICATE.json"]
        ).hexdigest(),
        "nullstellensatz_script_sha256": hashlib.sha256(
            payloads["r14_nullstellensatz_q.sing"]
        ).hexdigest(),
        "nullstellensatz_replay_script_sha256": hashlib.sha256(
            payloads["r14_nullstellensatz_replay_q.sing"]
        ).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
