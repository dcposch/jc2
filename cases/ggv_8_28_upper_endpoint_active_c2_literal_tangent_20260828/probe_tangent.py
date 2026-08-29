#!/usr/bin/env python3
"""First-order endpoint-lift probe at the deep active-c2 literal point.

The frozen point has D0=...=D22=0.  This probe asks whether a first-order
deformation inside the complete reduced-prefix/raw-window parameter space can
keep D0=...=D21=0 while changing D22 to the affine target 1.  It is a tangent
discriminator only, never a proof about other points or nonlinear arcs.
"""

from __future__ import annotations

from fractions import Fraction as Q
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAIL = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_active_c2_literal_d16_d22_probe_20260828"
    / "probe_literal_tail.py"
)
TAIL_SHA256 = "f3371687df3584bd1dbeac9e9ad05aca8212a6dd35b63c17209916ab9d11fb45"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_tail():
    assert sha256(TAIL) == TAIL_SHA256
    spec = importlib.util.spec_from_file_location("active_c2_tail_frozen", TAIL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def monomial(degree, coefficient=1):
    return [Q(0)] * degree + [Q(coefficient)]


def p_product(up, *items):
    out = [Q(1)]
    for item in items:
        out = up.p_mul(out, item)
    return out


def linearized_rows(up, F, G, dF, dG, maximum=22):
    rows = {}
    for n in range(maximum + 1):
        row = []
        for i in range(n + 1):
            j = n - i
            row = up.p_add(
                row,
                up.p_scale(12 - j, up.p_mul(up.p_derivative(dF[i]), G[j])),
                up.p_scale(12 - j, up.p_mul(up.p_derivative(F[i]), dG[j])),
                up.p_scale(i - 8, up.p_mul(dF[i], up.p_derivative(G[j]))),
                up.p_scale(i - 8, up.p_mul(F[i], up.p_derivative(dG[j]))),
            )
        rows[n] = row
    return rows


def invmod(value, modulus):
    return pow(value % modulus, -1, modulus)


def qmod(value, modulus):
    return (value.numerator % modulus) * invmod(value.denominator, modulus) % modulus


def modular_solve(rows, rhs, column_count, modulus):
    """Sparse row echelon; return rank and whether A*x=rhs is consistent."""
    pivots = {}
    for source_row, (row, target) in enumerate(zip(rows, rhs)):
        work = {column: qmod(value, modulus)
                for column, value in row.items() if qmod(value, modulus)}
        value = qmod(target, modulus)
        while work:
            pivot = min(work)
            if pivot not in pivots:
                scale = invmod(work[pivot], modulus)
                work = {column: coefficient * scale % modulus
                        for column, coefficient in work.items()
                        if coefficient * scale % modulus}
                value = value * scale % modulus
                pivots[pivot] = (work, value, source_row)
                break
            coefficient = work[pivot]
            old_row, old_value, _ = pivots[pivot]
            for column, old_coefficient in old_row.items():
                new_value = (work.get(column, 0) - coefficient * old_coefficient) % modulus
                if new_value:
                    work[column] = new_value
                else:
                    work.pop(column, None)
            value = (value - coefficient * old_value) % modulus
        else:
            if value:
                return {
                    "modulus": modulus,
                    "rank": len(pivots),
                    "consistent": False,
                    "contradiction_source_row": source_row,
                    "residual": value,
                    "column_count": column_count,
                }
    return {
        "modulus": modulus,
        "rank": len(pivots),
        "consistent": True,
        "nullity": column_count - len(pivots),
        "column_count": column_count,
    }


def exact_dual_certificate(rows, rhs, column_count):
    """Exact sparse Q elimination with a left-dual contradiction witness."""
    pivots = {}
    started = time.monotonic()
    for source_row, (row, target) in enumerate(zip(rows, rhs)):
        work = {column: Q(value) for column, value in row.items() if value}
        value = Q(target)
        combination = {source_row: Q(1)}
        while work:
            pivot = min(work)
            if pivot not in pivots:
                scale = Q(1) / work[pivot]
                work = {column: coefficient * scale
                        for column, coefficient in work.items()
                        if coefficient * scale}
                value *= scale
                combination = {index: coefficient * scale
                               for index, coefficient in combination.items()
                               if coefficient * scale}
                pivots[pivot] = (work, value, combination)
                break
            coefficient = work[pivot]
            old_row, old_value, old_combination = pivots[pivot]
            for column, old_coefficient in old_row.items():
                new_value = work.get(column, Q(0)) - coefficient * old_coefficient
                if new_value:
                    work[column] = new_value
                else:
                    work.pop(column, None)
            value -= coefficient * old_value
            for index, old_coefficient in old_combination.items():
                new_value = combination.get(index, Q(0)) - coefficient * old_coefficient
                if new_value:
                    combination[index] = new_value
                else:
                    combination.pop(index, None)
        else:
            if value:
                combination = {index: coefficient / value
                               for index, coefficient in combination.items()}
                assert sum(combination.get(index, Q(0)) * rhs[index]
                           for index in range(len(rows))) == 1
                for column in range(column_count):
                    assert sum(combination.get(index, Q(0))
                               * rows[index].get(column, Q(0))
                               for index in combination) == 0
                return {
                    "consistent": False,
                    "rank": len(pivots),
                    "column_count": column_count,
                    "contradiction_source_row": source_row,
                    "dual_support": len(combination),
                    "dual": combination,
                    "elapsed_seconds": time.monotonic() - started,
                }
    return {
        "consistent": True,
        "rank": len(pivots),
        "nullity": column_count - len(pivots),
        "column_count": column_count,
        "elapsed_seconds": time.monotonic() - started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact-output", type=Path)
    args = parser.parse_args()
    tail = load_tail()
    up = tail.load_upstream()

    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    A2, A3, A4, A5 = (up.p_power(A, exponent) for exponent in (2, 3, 4, 5))
    S = [Q(1)]
    Z = up.p_scale(Q(1, 2), up.p_add([Q(1)], up.p_scale(-1, A)))
    T = up.p_scale(Q(-1, 4), A)
    F4 = up.p_scale(Q(1, 64), up.p_add(up.p_mul(Z, Z), up.p_scale(-1, A)))
    F5 = up.p_scale(Q(1, 512), up.p_add(A, [Q(-1)]))

    F_laurent = {
        0: {4: [Q(1)]},
        1: {3: [Q(1)]},
        2: {2: up.p_scale(Q(1, 4), up.p_add([Q(1)], Z))},
        3: {1: up.p_scale(Q(1, 8), up.p_add(Z, up.p_scale(Q(-1, 4), A)))},
        4: {0: F4},
        5: {0: F5},
        6: {0: [Q(1, 4096)]},
        **{weight: {} for weight in range(7, 23)},
    }
    modes = {
        2: Q(1), 4: Q(0), 6: Q(1), 8: Q(0), 10: Q(0),
        12: Q(0), 14: Q(-6139, 17179869184), 16: Q(0),
        18: Q(16369, 140737488355328), 20: Q(0),
    }
    characteristic = tail.characteristic_special(up, F_laurent, modes, 21)

    F = {
        0: A4,
        1: A3,
        2: up.p_scale(Q(1, 4), up.p_mul(A2, up.p_add([Q(1)], Z))),
        3: up.p_scale(Q(1, 8), up.p_mul(A, up.p_add(Z, T))),
        4: F4,
        5: F5,
        6: [Q(1, 4096)],
        **{weight: [] for weight in range(7, 23)},
    }
    G = {}
    for weight in range(22):
        polynomial, denominator, power = tail.fraction_of_laurent(
            up, characteristic[weight], A
        )
        assert power == 0 and denominator == [Q(1)], (weight, power)
        G[weight] = polynomial
    G[22] = []
    assert all(not row for row in up.determinant_rows(F, G, 22).values())

    F_WINDOWS = {
        4: (0, 12), 5: (0, 11), 6: (0, 10), 7: (0, 9),
        8: (0, 8), 9: (1, 7), 10: (1, 6), 11: (1, 5),
        12: (2, 4), 13: (2, 3), 14: (2, 2),
    }
    G_WINDOWS = {
        4: (0, 20), 5: (0, 19), 6: (0, 18), 7: (0, 17),
        8: (0, 16), 9: (0, 15), 10: (0, 14), 11: (0, 13),
        12: (0, 12), 13: (1, 11), 14: (1, 10), 15: (1, 9),
        16: (2, 8), 17: (2, 7), 18: (2, 6), 19: (3, 5),
        20: (3, 4), 21: (3, 3),
    }

    columns = []

    def add_column(name, dF=None, dG=None):
        columns.append((name, dF or {}, dG or {}))

    # Reduced-prefix parameters S (degree <=3), Z (<=6), T (<=9), c2.
    c2 = Q(1)
    for degree in range(4):
        dS = monomial(degree)
        dF = {
            1: up.p_mul(A3, dS),
            2: up.p_scale(Q(1, 2), p_product(up, A2, S, dS)),
            3: up.p_scale(Q(1, 8), p_product(up, A, Z, dS)),
        }
        dG = {
            1: up.p_scale(Q(3, 2), up.p_mul(A5, dS)),
            2: up.p_scale(Q(3, 2), p_product(up, A4, S, dS)),
            3: up.p_add(
                up.p_scale(Q(3, 8), p_product(
                    up, A3, up.p_add(up.p_mul(S, S), Z), dS
                )),
                up.p_scale(Q(5, 4) * c2, up.p_mul(A4, dS)),
            ),
        }
        add_column(f"s_{degree}", dF, dG)

    for degree in range(7):
        dZ = monomial(degree)
        add_column(
            f"z_{degree}",
            {
                2: up.p_scale(Q(1, 4), up.p_mul(A2, dZ)),
                3: up.p_scale(Q(1, 8), p_product(up, A, S, dZ)),
            },
            {
                2: up.p_scale(Q(3, 8), up.p_mul(A4, dZ)),
                3: up.p_scale(Q(3, 8), p_product(up, A3, S, dZ)),
            },
        )

    for degree in range(10):
        dT = monomial(degree)
        add_column(
            f"tt_{degree}",
            {3: up.p_scale(Q(1, 8), up.p_mul(A, dT))},
            {3: up.p_scale(Q(3, 16), up.p_mul(A3, dT))},
        )

    add_column("c2", {}, {2: A5, 3: up.p_scale(Q(5, 4), A4)})

    for weight, (lower, upper) in F_WINDOWS.items():
        for degree in range(lower, upper + 1):
            add_column(f"F{weight}_{degree}", {weight: monomial(degree)}, {})
    for weight, (lower, upper) in G_WINDOWS.items():
        for degree in range(lower, upper + 1):
            add_column(f"G{weight}_{degree}", {}, {weight: monomial(degree)})

    zero = {weight: [] for weight in range(23)}
    images = []
    labels = set()
    for _, sparse_dF, sparse_dG in columns:
        dF = dict(zero)
        dG = dict(zero)
        dF.update(sparse_dF)
        dG.update(sparse_dG)
        image = linearized_rows(up, F, G, dF, dG)
        encoded = {}
        for weight, polynomial in image.items():
            for degree, coefficient in enumerate(polynomial):
                if coefficient:
                    encoded[(weight, degree)] = coefficient
                    labels.add((weight, degree))
        images.append(encoded)

    labels.add((22, 0))
    ordered_labels = sorted(labels)
    matrix_rows = []
    rhs = []
    for label in ordered_labels:
        row = {column: image[label]
               for column, image in enumerate(images) if label in image}
        matrix_rows.append(row)
        rhs.append(Q(1) if label == (22, 0) else Q(0))

    results = [modular_solve(matrix_rows, rhs, len(columns), prime)
               for prime in (65521, 65519, 65497)]
    for result in results:
        if not result["consistent"]:
            result["contradiction_label"] = list(
                ordered_labels[result["contradiction_source_row"]]
            )
    print(f"variables={len(columns)} coefficient_rows={len(matrix_rows)}")
    print("base=D0..D22_zero")
    for result in results:
        print(result)
    if all(not result["consistent"] for result in results):
        print("TANGENT_OBSTRUCTED_MOD_THREE_PRIMES")
    elif all(result["consistent"] for result in results):
        print("TANGENT_LIFT_EXISTS_MOD_THREE_PRIMES")
    else:
        print("TANGENT_PRIME_EXCEPTION_OR_MIXED_RESULT")

    if args.exact_output:
        exact = exact_dual_certificate(matrix_rows, rhs, len(columns))
        encoded = {key: value for key, value in exact.items() if key != "dual"}
        if "dual" in exact:
            encoded["dual"] = [
                {
                    "row_index": index,
                    "row_label": list(ordered_labels[index]),
                    "coefficient": str(coefficient),
                }
                for index, coefficient in sorted(exact["dual"].items())
            ]
        encoded["matrix"] = {
            "coefficient_rows": len(matrix_rows),
            "columns": len(columns),
            "column_names": [name for name, _, _ in columns],
            "ordered_row_labels": [list(label) for label in ordered_labels],
        }
        encoded["pins"] = {"tail_checker_sha256": TAIL_SHA256}
        args.exact_output.write_text(json.dumps(encoded, indent=2, sort_keys=True) + "\n")
        print(json.dumps({key: value for key, value in encoded.items()
                          if key not in ("dual", "matrix")}, sort_keys=True))
        print("EXACT_TANGENT_DUAL_WRITTEN=" + str(args.exact_output))


if __name__ == "__main__":
    main()
