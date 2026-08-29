#!/usr/bin/env python3
"""Second-order endpoint screen at the frozen deep active-c2 point.

This script is AWS-only.  It reconstructs the frozen 510x308 tangent
matrix, computes its exact 17-dimensional kernel, includes the quadratic
curvature of the reduced-prefix parametrization, and forms the 153 symmetric
quadratic columns on that kernel.  It then relaxes the Veronese monomials to
independent variables and tests the augmented linear system over three
primes and, on request, over Q.

Inconsistency of the relaxed system excludes a second-order lift at this one
base point.  Consistency is navigation only: the independent monomial values
must still come from a rank-one symmetric matrix u*u^T.
"""

from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from fractions import Fraction as Q
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import platform
import sys
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TANGENT = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_active_c2_literal_tangent_20260828"
    / "probe_tangent.py"
)
TANGENT_SHA256 = "ddcd7b5d9cc5dd37e56412f606eb4b0fb37bc976280b224ac9dcf91a04be20a1"
CERTIFICATE = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_active_c2_literal_tangent_20260828"
    / "aws_exact_q_r1/output/TANGENT_CERTIFICATE.json"
)
CERTIFICATE_SHA256 = "d21fc8538e908f9a1bc6705fd9e5cf99a2c3d0be3f3b8a82318906ef817c0a8b"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def aws_guard() -> None:
    if platform.system() != "Linux":
        raise SystemExit("AWS_ONLY: Linux required")
    dmi = Path("/sys/class/dmi/id/sys_vendor")
    value = dmi.read_text(errors="replace").strip() if dmi.exists() else ""
    if value != "Amazon EC2":
        raise SystemExit("AWS_ONLY: Amazon EC2 DMI identity required")


def clean_direction(direction):
    return {
        weight: list(direction.get(weight, []))
        for weight in range(23)
    }


def capture_frozen_tangent():
    assert sha256(TANGENT) == TANGENT_SHA256
    assert sha256(CERTIFICATE) == CERTIFICATE_SHA256
    spec = importlib.util.spec_from_file_location("frozen_tangent", TANGENT)
    assert spec and spec.loader
    tangent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tangent)

    captured = {"directions": [], "matrix": None, "rhs": None,
                "column_count": None, "F": None, "G": None, "up": None}
    original_linearized = tangent.linearized_rows
    original_modular = tangent.modular_solve

    def capture_linearized(up, F, G, dF, dG, maximum=22):
        if captured["F"] is None:
            captured["F"] = clean_direction(F)
            captured["G"] = clean_direction(G)
            captured["up"] = up
        captured["directions"].append(
            (clean_direction(dF), clean_direction(dG))
        )
        return original_linearized(up, F, G, dF, dG, maximum)

    def capture_modular(rows, rhs, column_count, modulus):
        if captured["matrix"] is None:
            captured["matrix"] = [dict(row) for row in rows]
            captured["rhs"] = list(rhs)
            captured["column_count"] = column_count
        return original_modular(rows, rhs, column_count, modulus)

    tangent.linearized_rows = capture_linearized
    tangent.modular_solve = capture_modular
    old_argv = sys.argv
    sys.argv = [str(TANGENT)]
    try:
        with redirect_stdout(io.StringIO()):
            tangent.main()
    finally:
        sys.argv = old_argv
        tangent.linearized_rows = original_linearized
        tangent.modular_solve = original_modular

    certificate = json.loads(CERTIFICATE.read_text())
    assert captured["column_count"] == 308
    assert len(captured["matrix"]) == 510
    assert len(captured["directions"]) == 308
    assert certificate["rank"] == 291
    assert certificate["matrix"]["columns"] == 308
    assert certificate["matrix"]["coefficient_rows"] == 510
    captured["labels"] = [
        tuple(label) for label in certificate["matrix"]["ordered_row_labels"]
    ]
    captured["names"] = list(certificate["matrix"]["column_names"])
    captured["tangent"] = tangent
    return captured


def exact_echelon(rows, column_count):
    pivots = {}
    for source_row, row in enumerate(rows):
        work = {column: Q(value) for column, value in row.items() if value}
        while work:
            pivot = min(work)
            if pivot not in pivots:
                scale = Q(1) / work[pivot]
                work = {
                    column: coefficient * scale
                    for column, coefficient in work.items()
                    if coefficient * scale
                }
                pivots[pivot] = (work, source_row)
                break
            coefficient = work[pivot]
            old_row, _ = pivots[pivot]
            for column, old_coefficient in old_row.items():
                value = work.get(column, Q(0)) - coefficient * old_coefficient
                if value:
                    work[column] = value
                else:
                    work.pop(column, None)
    free = sorted(set(range(column_count)) - set(pivots))
    basis = []
    for free_column in free:
        vector = {free_column: Q(1)}
        for pivot in sorted(pivots, reverse=True):
            row, _ = pivots[pivot]
            value = sum(
                coefficient * vector.get(column, Q(0))
                for column, coefficient in row.items()
                if column != pivot
            )
            if value:
                vector[pivot] = -value
        basis.append(vector)
    for vector in basis:
        for row in rows:
            assert sum(value * vector.get(column, Q(0))
                       for column, value in row.items()) == 0
    return pivots, basis


def direction_sum(up, directions, vector):
    dF = {weight: [] for weight in range(23)}
    dG = {weight: [] for weight in range(23)}
    for column, scalar in vector.items():
        source_F, source_G = directions[column]
        for weight in range(23):
            if source_F[weight]:
                dF[weight] = up.p_add(
                    dF[weight], up.p_scale(scalar, source_F[weight])
                )
            if source_G[weight]:
                dG[weight] = up.p_add(
                    dG[weight], up.p_scale(scalar, source_G[weight])
                )
    return dF, dG


def vector_sum(left, right):
    out = dict(left)
    for column, value in right.items():
        total = out.get(column, Q(0)) + value
        if total:
            out[column] = total
        else:
            out.pop(column, None)
    return out


def parameter_polynomial(up, vector, names, prefix):
    out = []
    for column, scalar in vector.items():
        name = names[column]
        if name.startswith(prefix):
            degree = int(name[len(prefix):])
            out = up.p_add(out, [Q(0)] * degree + [scalar])
    return out


def prefix_hessian(up, vector, names, A):
    """Coefficient of eps^2 forced by the curved reduced prefix.

    Parameter arcs are p=p0+eps*v+eps^2*w.  This returns only the fixed
    quadratic contribution depending on v; A*w is supplied separately by
    the original tangent columns.
    """
    dS = parameter_polynomial(up, vector, names, "s_")
    dZ = parameter_polynomial(up, vector, names, "z_")
    dc2 = Q(0)
    for column, scalar in vector.items():
        if names[column] == "c2":
            dc2 += scalar

    A2 = up.p_power(A, 2)
    A3 = up.p_power(A, 3)
    A4 = up.p_power(A, 4)
    dS2 = up.p_mul(dS, dS)
    dSdZ = up.p_mul(dS, dZ)
    hF = {weight: [] for weight in range(23)}
    hG = {weight: [] for weight in range(23)}
    hF[2] = up.p_scale(Q(1, 4), up.p_mul(A2, dS2))
    hF[3] = up.p_scale(Q(1, 8), up.p_mul(A, dSdZ))
    hG[2] = up.p_scale(Q(3, 4), up.p_mul(A4, dS2))
    hG[3] = up.p_add(
        up.p_scale(Q(3, 8), up.p_mul(A3, dS2)),
        up.p_scale(Q(3, 8), up.p_mul(A3, dSdZ)),
        up.p_scale(Q(5, 4) * dc2, up.p_mul(A4, dS)),
    )
    return hF, hG


def add_row_polynomials(up, *families):
    return {
        weight: up.p_add(*(family[weight] for family in families))
        for weight in range(23)
    }


def quadratic_rows(captured, vector, A):
    up = captured["up"]
    dF, dG = direction_sum(up, captured["directions"], vector)
    hF, hG = prefix_hessian(up, vector, captured["names"], A)
    bilinear = up.determinant_rows(dF, dG, 22)
    curvature = captured["tangent"].linearized_rows(
        up, captured["F"], captured["G"], hF, hG, 22
    )
    return add_row_polynomials(up, bilinear, curvature)


def encoded_rows(polynomial_rows):
    out = {}
    for weight, polynomial in polynomial_rows.items():
        for degree, coefficient in enumerate(polynomial):
            if coefficient:
                out[(weight, degree)] = coefficient
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact-output", type=Path)
    args = parser.parse_args()
    aws_guard()
    started = time.monotonic()
    captured = capture_frozen_tangent()
    up = captured["up"]
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]

    pivots, kernel = exact_echelon(captured["matrix"], 308)
    assert len(pivots) == 291
    assert len(kernel) == 17

    diagonal = [quadratic_rows(captured, vector, A) for vector in kernel]
    quadratic_columns = []
    monomial_labels = []
    for i, left in enumerate(kernel):
        for j in range(i, len(kernel)):
            if i == j:
                polynomial_rows = diagonal[i]
            else:
                together = quadratic_rows(
                    captured, vector_sum(left, kernel[j]), A
                )
                polynomial_rows = {
                    weight: up.p_add(
                        together[weight],
                        up.p_scale(-1, diagonal[i][weight]),
                        up.p_scale(-1, diagonal[j][weight]),
                    )
                    for weight in range(23)
                }
            quadratic_columns.append(encoded_rows(polynomial_rows))
            monomial_labels.append((i, j))
    assert len(quadratic_columns) == 153

    all_labels = set(captured["labels"])
    for column in quadratic_columns:
        all_labels.update(column)
    all_labels.add((22, 0))
    labels = sorted(all_labels)
    old_index = {label: index for index, label in enumerate(captured["labels"])}
    augmented_rows = []
    rhs = []
    for label in labels:
        row = dict(captured["matrix"][old_index[label]]) if label in old_index else {}
        for q_index, column in enumerate(quadratic_columns):
            if label in column:
                row[308 + q_index] = column[label]
        augmented_rows.append(row)
        rhs.append(Q(1) if label == (22, 0) else Q(0))

    modular = [
        captured["tangent"].modular_solve(
            augmented_rows, rhs, 461, prime
        )
        for prime in (65521, 65519, 65497)
    ]
    for result in modular:
        if not result["consistent"]:
            source = result["contradiction_source_row"]
            result["contradiction_label"] = list(labels[source])

    result = {
        "format": "GGV_ACTIVE_C2_LITERAL_SECOND_ORDER_RELAXED_V1",
        "base_tangent": {
            "rows": 510,
            "columns": 308,
            "rank": 291,
            "kernel_dimension": 17,
        },
        "second_order": {
            "equation_rows": len(labels),
            "correction_columns": 308,
            "symmetric_monomial_columns": 153,
            "augmented_columns": 461,
            "extra_row_labels_beyond_tangent": len(labels) - 510,
            "prefix_curvature_included": True,
            "veronese_rank_one_constraints_imposed": False,
        },
        "modular": modular,
        "pins": {
            "tangent_source_sha256": TANGENT_SHA256,
            "tangent_certificate_sha256": CERTIFICATE_SHA256,
        },
        "elapsed_seconds_before_exact": time.monotonic() - started,
    }
    print(json.dumps(result, indent=2, sort_keys=True))

    if args.exact_output:
        exact = captured["tangent"].exact_dual_certificate(
            augmented_rows, rhs, 461
        )
        if "dual" in exact:
            exact["dual"] = [
                {
                    "row_index": index,
                    "row_label": list(labels[index]),
                    "coefficient": str(coefficient),
                }
                for index, coefficient in sorted(exact["dual"].items())
            ]
        result["exact_relaxed"] = exact
        result["elapsed_seconds_total"] = time.monotonic() - started
        args.exact_output.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n"
        )
        if exact["consistent"]:
            print("SECOND_ORDER_RELAXED_CONSISTENT_NO_VERDICT")
        else:
            print("SECOND_ORDER_RELAXED_INCONSISTENT_AT_THIS_POINT")
        print("EXACT_SECOND_ORDER_OUTPUT=" + str(args.exact_output))


if __name__ == "__main__":
    main()
