#!/usr/bin/env python3
"""Independent exact-Q replay for a raw branch-P endpoint witness.

This verifier deliberately does not import the compiler or its sparse
multivariate implementation.  It reconstructs the literal univariate
F/G coefficients from a complete assignment of the 303 raw variables and
evaluates the displayed D5G recurrence with ``fractions.Fraction``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW_INPUT = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"
RAW_SYSTEM = HERE / "RAW_DIRECT_SYSTEM.json"

RAW_INPUT_SHA256 = "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876"
RAW_SYSTEM_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trim(poly):
    out = list(poly)
    while out and out[-1] == 0:
        out.pop()
    return out


def add(left, right):
    return trim([
        (left[i] if i < len(left) else Q(0))
        + (right[i] if i < len(right) else Q(0))
        for i in range(max(len(left), len(right)))
    ])


def scale(poly, scalar):
    scalar = Q(scalar)
    return trim([scalar * value for value in poly])


def mul(left, right):
    if not left or not right:
        return []
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def derivative(poly):
    return trim([Q(i) * poly[i] for i in range(1, len(poly))])


def power(poly, exponent):
    out = [Q(1)]
    base = list(poly)
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        base = mul(base, base)
        exponent //= 2
    return out


def monomial(degree, coefficient=1):
    return [Q(0)] * degree + [Q(coefficient)]


def parse_q(value):
    if isinstance(value, bool):
        raise ValueError("booleans are not rational witness values")
    if isinstance(value, int):
        return Q(value)
    if not isinstance(value, str):
        raise ValueError(f"rational value must be an integer or string, got {type(value).__name__}")
    return Q(value)


def expected_windows():
    return {
        "F": {
            1: (0, 15), 2: (0, 14), 3: (0, 13), 4: (0, 12),
            5: (0, 11), 6: (0, 10), 7: (0, 9), 8: (0, 8),
            9: (1, 7), 10: (1, 6), 11: (1, 5), 12: (2, 4),
            13: (2, 3), 14: (2, 2),
        },
        "G": {
            1: (0, 23), 2: (0, 22), 3: (0, 21), 4: (0, 20),
            5: (0, 19), 6: (0, 18), 7: (0, 17), 8: (0, 16),
            9: (0, 15), 10: (0, 14), 11: (0, 13), 12: (0, 12),
            13: (1, 11), 14: (1, 10), 15: (1, 9), 16: (2, 8),
            17: (2, 7), 18: (2, 6), 19: (3, 5), 20: (3, 4),
            21: (3, 3),
        },
    }


def audited_windows(raw_source):
    windows = {"F": {}, "G": {}}
    for kind in windows:
        for record in raw_source["raw_slots_through_weight_22"][kind]:
            weight = int(record["weight"])
            if weight <= 0:
                continue
            degree = int(record["raw_exponents"]["x"])
            windows[kind].setdefault(weight, {})[degree] = record["slot"]
    expected = expected_windows()
    for kind in ("F", "G"):
        assert set(windows[kind]) == set(expected[kind]), (kind, sorted(windows[kind]))
        for weight, (lower, upper) in expected[kind].items():
            assert sorted(windows[kind][weight]) == list(range(lower, upper + 1))
    assert 22 not in windows["G"]
    return windows


def vector_from_slots(slot_map, values):
    out = [Q(0)] * (max(slot_map) + 1)
    for degree, name in slot_map.items():
        out[degree] = values[name]
    return trim(out)


def reconstruct(values, windows):
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    H = power(A, 2)
    F = {0: power(H, 2), 1: H}
    G = {0: power(H, 3)}

    Z = [values[f"z_{degree}"] for degree in range(7)]
    T = [values[f"tt_{degree}"] for degree in range(10)]
    F[2] = scale(add([Q(1)], mul(H, Z)), Q(1, 4))
    F[3] = scale(add(Z, mul(A, T)), Q(1, 8))
    G[1] = scale(power(H, 2), Q(3, 2))
    G[2] = add(scale(mul(H, F[2]), Q(3, 2)), scale(H, Q(3, 8)))
    G[3] = add(
        add(scale(mul(H, F[3]), Q(3, 2)), scale(F[2], Q(3, 4))),
        [Q(-1, 16)],
    )

    for weight in range(4, 15):
        F[weight] = vector_from_slots(windows["F"][weight], values)
    for weight in range(4, 22):
        G[weight] = vector_from_slots(windows["G"][weight], values)
    return A, H, F, G


def recurrence_rows(F, G, maximum=22):
    rows = {}
    for n in range(maximum + 1):
        value = []
        for i in range(n + 1):
            j = n - i
            if i not in F or j not in G:
                continue
            value = add(value, scale(mul(derivative(F[i]), G[j]), 12 - j))
            value = add(value, scale(mul(F[i], derivative(G[j])), i - 8))
        rows[n] = value
    return rows


def matrix_rank(columns, row_count):
    matrix = [[columns[column][row] if row < len(columns[column]) else Q(0)
               for column in range(len(columns))] for row in range(row_count)]
    rank = 0
    for column in range(len(columns)):
        pivot = next((row for row in range(rank, row_count) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        factor = matrix[rank][column]
        matrix[rank] = [entry / factor for entry in matrix[rank]]
        for row in range(row_count):
            if row == rank or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [left - factor * right
                           for left, right in zip(matrix[row], matrix[rank])]
        rank += 1
        if rank == row_count:
            break
    return rank


def q1_audit(A, H):
    Aprime = derivative(A)

    def image(poly):
        return add(scale(mul(A, derivative(poly)), 2), scale(mul(Aprime, poly), -3))

    columns = [image(monomial(degree)) for degree in range(13)]
    base_rank = matrix_rank(columns, 16)
    with_h_rank = matrix_rank(columns + [H], 16)
    positive_mutation = image(A)
    mutation_rank = matrix_rank(columns + [positive_mutation], 16)
    assert base_rank == 13
    assert with_h_rank == 14
    assert mutation_rank == 13
    assert positive_mutation == scale(mul(A, Aprime), -1)
    return {
        "operator": "T_A(Q)=2*A*Q'-3*A'*Q, deg(Q)<=12",
        "ambient_dimension": 16,
        "image_rank": base_rank,
        "rank_with_F1_H": with_h_rank,
        "F1_H_outside_image": True,
        "positive_mutation": "T_A(A)=-A*A'",
        "rank_with_positive_mutation": mutation_rank,
    }


def endpoint_transfer_audit(A):
    # If a formal rational continuation g22=N/A^5 is adjoined, then
    # L22(g22)=-8*N'/A.  With D_raw,22=-L22(g22), target +1 requires
    # N'=A/8.  This is a diagnostic identity only: G22 is not a raw slot.
    numerator = add(scale(monomial(5), Q(1, 40)), scale(monomial(1), Q(-1, 8)))
    assert scale(derivative(numerator), 8) == A
    return {
        "status": "PASS",
        "role": "diagnostic_only_not_solver_input",
        "identity": "D_raw,22=-L22(g22)",
        "operator": "L22(R)=2*H*(-10*H'*R-4*H*R')",
        "target_particular": "g22=(X^5/40-X/8)/A^5",
        "cleared_check": "8*N'=A, hence L22(N/A^5)=-1 and D_raw,22=1",
        "kernel": "Q-constant/A^5",
        "synthetic_G22_is_not_admitted": True,
    }


def verify(witness_path: Path):
    assert sha256(RAW_INPUT) == RAW_INPUT_SHA256
    assert sha256(RAW_SYSTEM) == RAW_SYSTEM_SHA256
    raw_source = json.loads(RAW_INPUT.read_text())
    raw_system = json.loads(RAW_SYSTEM.read_text())
    windows = audited_windows(raw_source)

    witness = json.loads(witness_path.read_text())
    assert witness.get("raw_system_sha256") == RAW_SYSTEM_SHA256
    encoded_values = witness.get("values")
    assert isinstance(encoded_values, dict)
    required = set(raw_system["variables"])
    assert set(encoded_values) == required, {
        "missing": sorted(required - set(encoded_values)),
        "extra": sorted(set(encoded_values) - required),
    }
    values = {name: parse_q(encoded_values[name]) for name in required}

    A, H, F, G = reconstruct(values, windows)
    rows = recurrence_rows(F, G)
    for n in range(22):
        assert rows[n] == [], f"D{n} is nonzero: {rows[n]}"
    assert rows[22] == [Q(1)], f"D22 is not 1: {rows[22]}"

    # Frozen mutations.  These checks are intentionally expressed in the
    # independent dense model rather than by editing serialized generators.
    assert rows[22] != []                              # target D22=0 rejects
    assert add(rows[21], [Q(1)]) != []                 # D21+1 rejects
    synthetic_g22 = [Q(1)]
    synthetic_delta = add(
        scale(mul(derivative(F[0]), synthetic_g22), -10),
        scale(mul(F[0], derivative(synthetic_g22)), -8),
    )
    assert synthetic_delta and add(rows[22], synthetic_delta) != [Q(1)]

    q1 = q1_audit(A, H)
    transfer = endpoint_transfer_audit(A)
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-BRANCH-P-WITNESS-REPLAY-v1",
        "status": "PASS",
        "field": "Q",
        "raw_system_sha256": RAW_SYSTEM_SHA256,
        "variable_count": len(values),
        "raw_windows": {"F_weights": len(windows["F"]), "G_weights": len(windows["G"]),
                        "G22_present": False},
        "rows": {"D0_through_D21": "0", "D22": "1", "D23_imposed": False},
        "q1": q1,
        "endpoint_transfer": transfer,
        "mutations": {
            "D22_target_zero_rejected": True,
            "D21_constant_plus_one_rejected": True,
            "synthetic_G22_rejected": True,
            "q1_positive_F1_mutation_rejected_by_rank_separator": True,
        },
    }


def self_check():
    assert sha256(RAW_INPUT) == RAW_INPUT_SHA256
    assert sha256(RAW_SYSTEM) == RAW_SYSTEM_SHA256
    source = json.loads(RAW_INPUT.read_text())
    windows = audited_windows(source)
    system = json.loads(RAW_SYSTEM.read_text())
    # F1--F3 and G1--G3 are cascade values, not raw witness coordinates.
    expected_variables = {
        name for kind in ("F", "G") for weight in windows[kind]
        if weight >= 4 for name in windows[kind][weight].values()
    }
    expected_variables.update(f"z_{degree}" for degree in range(7))
    expected_variables.update(f"tt_{degree}" for degree in range(10))
    assert expected_variables == set(system["variables"])
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    H = power(A, 2)
    q1 = q1_audit(A, H)
    transfer = endpoint_transfer_audit(A)
    return {
        "status": "PASS",
        "variable_count": len(expected_variables),
        "raw_system_sha256": RAW_SYSTEM_SHA256,
        "q1": q1,
        "endpoint_transfer": transfer,
    }


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--witness", type=Path)
    group.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    result = self_check() if args.self_check else verify(args.witness)
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
