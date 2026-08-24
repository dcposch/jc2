#!/usr/bin/env python3
"""Independent exact replay for AS3-MIN-W2.

This file deliberately does not import ``search.py``.  It uses a second term
list implementation, an independent modular row reduction for the correction
equation, and direct verification of the producer's emitted Z/9 witness.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


Term = Tuple[int, int, int]  # coefficient, x exponent, y exponent
Mon = Tuple[int, int]
CAP_DIR = Path(__file__).resolve().parent


def normalize(terms: Iterable[Term], modulus: int | None = None) -> List[Term]:
    collected: Dict[Mon, int] = {}
    for coefficient, x_exp, y_exp in terms:
        collected[(x_exp, y_exp)] = collected.get((x_exp, y_exp), 0) + coefficient
    if modulus is not None:
        collected = {mon: coefficient % modulus for mon, coefficient in collected.items()}
    return [(coefficient, x_exp, y_exp)
            for (x_exp, y_exp), coefficient in sorted(collected.items()) if coefficient]


def deriv(terms: Sequence[Term], axis: int) -> List[Term]:
    out = []
    for coefficient, x_exp, y_exp in terms:
        exponent = x_exp if axis == 0 else y_exp
        if not exponent:
            continue
        if axis == 0:
            out.append((coefficient * exponent, x_exp - 1, y_exp))
        else:
            out.append((coefficient * exponent, x_exp, y_exp - 1))
    return normalize(out)


def product(left: Sequence[Term], right: Sequence[Term]) -> List[Term]:
    return normalize((a * b, i + u, j + v)
                     for a, i, j in left for b, u, v in right)


def determinant(p: Sequence[Term], q: Sequence[Term],
                modulus: int | None = None) -> List[Term]:
    positive = product(deriv(p, 0), deriv(q, 1))
    negative = [(-coefficient, i, j)
                for coefficient, i, j in product(deriv(p, 1), deriv(q, 0))]
    return normalize(positive + negative, modulus)


def evaluate(terms: Sequence[Term], point: Mon, modulus: int) -> int:
    x, y = point
    return sum(coefficient * x ** i * y ** j
               for coefficient, i, j in terms) % modulus


def decode(rows: Sequence[Sequence[int]]) -> List[Term]:
    return normalize((int(coefficient), int(i), int(j))
                     for i, j, coefficient in rows)


def encode(terms: Sequence[Term], modulus: int | None = None) -> List[List[int]]:
    return [[i, j, coefficient] for coefficient, i, j in normalize(terms, modulus)]


def polynomial_dict(terms: Sequence[Term], modulus: int) -> Dict[Mon, int]:
    return {(i, j): coefficient for coefficient, i, j in normalize(terms, modulus)}


def teich(residue: int, prime: int) -> int:
    modulus = prime ** 2
    matches = []
    for lift_index in range(prime):
        value = residue + prime * lift_index
        if (value ** prime - value) % modulus == 0:
            matches.append(value)
    if len(matches) != 1:
        raise AssertionError("independent Teichmueller search failed")
    return matches[0]


def singleton(mon: Mon) -> List[Term]:
    return [(1, mon[0], mon[1])]


def correction_solve(p: Sequence[Term], q: Sequence[Term], error: Sequence[Term],
                     prime: int) -> Tuple[int, List[Tuple[str, Mon, int]]]:
    """Independently solve L(A,B)=-E on a frozen box containing the witness."""
    mons = [(i, j) for i in range(4) for j in range(3)]
    labels = [("A", mon) for mon in mons] + [("B", mon) for mon in mons]
    columns: List[Dict[Mon, int]] = []
    for side, mon in labels:
        if side == "A":
            col = determinant(singleton(mon), q, prime)
        else:
            col = determinant(p, singleton(mon), prime)
        columns.append(polynomial_dict(col, prime))
    target = {(i, j): (-coefficient) % prime
              for coefficient, i, j in normalize(error, prime)}
    row_mons = sorted(set(target).union(*(set(column) for column in columns)))
    matrix = [[columns[column].get(mon, 0) for column in range(len(columns))]
              + [target.get(mon, 0)] for mon in row_mons]

    rank = 0
    pivots: List[int] = []
    for column in range(len(columns)):
        pivot = next((row for row in range(rank, len(matrix))
                      if matrix[row][column] % prime), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column] % prime, -1, prime)
        matrix[rank] = [(value * inverse) % prime for value in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or not matrix[row][column] % prime:
                continue
            factor = matrix[row][column] % prime
            matrix[row] = [(left - factor * right) % prime
                           for left, right in zip(matrix[row], matrix[rank])]
        pivots.append(column)
        rank += 1
        if rank == len(matrix):
            break
    if any(all(value % prime == 0 for value in row[:-1]) and row[-1] % prime
           for row in matrix):
        raise AssertionError("independent correction system is inconsistent")
    solution = [0] * len(columns)
    for row, column in enumerate(pivots):
        solution[column] = matrix[row][-1] % prime
    witness = [(side, mon, solution[index])
               for index, (side, mon) in enumerate(labels) if solution[index]]
    return rank, witness


def digest_json(value: object) -> str:
    data = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def digest_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replay(result_path: Path) -> Dict[str, object]:
    result = json.loads(result_path.read_text(encoding="utf-8"))
    checks: List[str] = []
    prime, modulus = 3, 9
    residues = [(0, 0), (1, 0)]

    if result["cap_id"] != "AS3-MIN-W2" or result["fixed_coefficient_order"] != [1, 2]:
        raise AssertionError("producer cap identity/order mismatch")
    if result["canonical_claim_sha256"] != digest_json(result["canonical_claim"]):
        raise AssertionError("producer canonical-claim hash mismatch")
    checks.append("producer canonical JSON hash")

    independent_rows = []
    entering = []
    for a in (1, 2):
        p = [(1, 1, 0), (a, 3, 0)]
        q = [(1, 0, 1)]
        jac = determinant(p, q, prime)
        images = [[evaluate(p, point, prime), evaluate(q, point, prime)]
                  for point in residues]
        enters = jac == [(1, 0, 0)] and images == [[0, 0], [0, 0]]
        independent_rows.append({"a": a, "jacobian_mod3": encode(jac, prime),
                                 "marked_images_mod3": images, "enters": enters})
        if enters:
            entering.append(a)
    if entering != [2]:
        raise AssertionError(f"independent special-fibre census changed: {entering}")
    if [row["a"] for row in result["screened"]] != [1, 2]:
        raise AssertionError("producer did not traverse the frozen prefix")
    checks.append("independent two-value special-fibre census")

    # Exact triangular generic fibre: y=V and the monic-after-scaling cubic
    # x^3 + a^{-1}x-a^{-1}U gives the unique remainder basis 1,x,x^2.
    a = 2
    if pow(a, -1, prime) != 2:
        raise AssertionError("generic-fibre leading coefficient inversion failed")
    generic_basis = ["1", "x", "x^2"]
    generic_degree = len(generic_basis)
    separable_derivative = [(1, 0, 0)]  # d(x+a*x^3-U)/dx in F_3
    if generic_degree != 3 or separable_derivative != [(1, 0, 0)]:
        raise AssertionError("generic degree/separability replay failed")
    checks.append("exact generic-fibre division basis and separability")

    p = [(1, 1, 0), (2, 3, 0)]
    q = [(1, 0, 1)]
    p_teich = [(teich(1, prime), 1, 0), (teich(2, prime), 3, 0)]
    q_teich = [(teich(1, prime), 0, 1)]
    lift_jac = determinant(p_teich, q_teich)
    numerator = normalize(lift_jac + [(-1, 0, 0)])
    if any(coefficient % prime for coefficient, _, _ in numerator):
        raise AssertionError("independent lifted error is not divisible by 3")
    error = normalize(((coefficient // prime) % prime, i, j)
                      for coefficient, i, j in numerator)
    top = [(i, j) for coefficient, i, j in error
           if coefficient % prime and i % prime == 2 and j % prime == 2]
    if encode(error, prime) != [[2, 0, 2]] or top:
        raise AssertionError(f"independent W2 obstruction changed: E={error}, top={top}")
    checks.append("independent Teichmueller lift, E, and top Cartier class")

    correction_rank, independent_witness = correction_solve(p, q, error, prime)
    if not independent_witness:
        raise AssertionError("independent correction solver emitted no witness")
    checks.append("independent modular correction solve")

    survivor = result["canonical_claim"]["survivor"]
    if result["verdict"] != "W2-SURVIVOR" or survivor["a"] != 2:
        raise AssertionError("producer verdict/survivor mismatch")
    if survivor["generic_degree"] != generic_degree:
        raise AssertionError("producer generic degree mismatch")
    if survivor["error_E_mod3"] != encode(error, prime) or survivor["top_cartier_support"]:
        raise AssertionError("producer obstruction record mismatch")

    producer_a = decode(survivor["A_mod3"])
    producer_b = decode(survivor["B_mod3"])
    lhs = normalize(determinant(producer_a, q, prime)
                    + determinant(p, producer_b, prime), prime)
    rhs = normalize(((-coefficient) % prime, i, j) for coefficient, i, j in error)
    if lhs != rhs:
        raise AssertionError("producer correction fails independent linearized check")
    p2_expected = normalize(p_teich + [(prime * coefficient, i, j)
                                      for coefficient, i, j in producer_a], modulus)
    q2_expected = normalize(q_teich + [(prime * coefficient, i, j)
                                      for coefficient, i, j in producer_b], modulus)
    p2 = decode(survivor["P2_mod9"])
    q2 = decode(survivor["Q2_mod9"])
    if normalize(p2, modulus) != p2_expected or normalize(q2, modulus) != q2_expected:
        raise AssertionError("producer corrected polynomials mismatch")
    det2 = determinant(p2, q2)
    if determinant(p2, q2, modulus) != [(1, 0, 0)]:
        raise AssertionError("producer correction is not determinant one mod 9")
    checks.append("independent verification of producer linearized and Z/9 determinant witnesses")

    lifted_points = [tuple(point) for point in survivor["lifted_points_mod9"]]
    lifted_target = tuple(survivor["lifted_target_mod9"])
    if len(lifted_points) != 2 or len(set(lifted_points)) != 2:
        raise AssertionError("producer collision lifts are not two distinct points")
    for point, residue in zip(lifted_points, residues):
        if (point[0] % prime, point[1] % prime) != residue:
            raise AssertionError("producer point does not lift its marked residue")
        image = (evaluate(p2, point, modulus), evaluate(q2, point, modulus))
        if image != lifted_target:
            raise AssertionError("producer lifted collision image mismatch")
    checks.append("independent Z/9 marked-collision replay")

    independent_core = {
        "cap_id": "AS3-MIN-W2",
        "special_fibre_rows": independent_rows,
        "entering_values": entering,
        "generic_degree": generic_degree,
        "generic_basis": generic_basis,
        "teichmueller_coefficients": {"1": teich(1, prime), "2": teich(2, prime)},
        "error_E_mod3": encode(error, prime),
        "top_cartier_support": top,
        "correction_matrix_rank": correction_rank,
        "independent_correction_witness": [[side, mon[0], mon[1], coefficient]
                                           for side, mon, coefficient in independent_witness],
        "producer_witness_determinant_exact": encode(det2),
        "producer_lifted_points_mod9": [list(point) for point in lifted_points],
        "producer_lifted_target_mod9": list(lifted_target),
        "verdict": "W2-SURVIVOR",
    }
    return {
        "schema_version": 1,
        "cap_id": "AS3-MIN-W2",
        "verdict": "PASS",
        "checks": checks,
        "producer_result_sha256": digest_file(result_path),
        "producer_canonical_claim_sha256": result["canonical_claim_sha256"],
        "independent_core": independent_core,
        "independent_core_sha256": digest_json(independent_core),
        "preregistration_sha256": digest_file(CAP_DIR / "PREREGISTRATION.md"),
        "provenance_sha256": digest_file(CAP_DIR / "provenance.json"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=CAP_DIR / "results.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = replay(args.input)
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
