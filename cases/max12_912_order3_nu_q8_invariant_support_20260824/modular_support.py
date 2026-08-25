#!/usr/bin/env python3
"""Fast modular Hensel/support learner for the corrected Q8 quotient.

This is a producer successor, not part of the frozen global-quotient case.
It specializes one Q8 contact to a rational root modulo a good prime, lifts
the exact six-row approximate-cubic branch, reconstructs the weight-zero
functions theta and Z, and searches bounded rectangular plane relations.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
FROZEN = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824"
COMPILER = FROZEN / "quotient_compiler.py"
LOCAL = FROZEN / "local_series.py"
PINS = {
    COMPILER: "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545",
    LOCAL: "5e3e3d8605999a21371dbd2aa54c82fbfec510b5e26f3801387c11d450da8957",
    FROZEN / "MANIFEST.sha256":
        "3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4",
    FROZEN / "FREEZE.txt":
        "c34fff2b838ca4803872b709857ae7becb1751a7e1ce261c9fa8c7e6d8b46c97",
}


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def check_pins():
    for path, expected in PINS.items():
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))


check_pins()
L = load("q8_modular_support_parent", LOCAL)
Q, P, M, J = L.Q, L.P, L.M, L.J
NF, ZERO, ONE = L.NF, L.ZERO, L.ONE


def fraction_mod(value, prime):
    value = Fraction(value)
    denominator = value.denominator % prime
    if not denominator:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(denominator, -1, prime) % prime


def nf_mod(value, prime, root):
    total = 0
    for coefficient in reversed(value.poly):
        total = (total * root + fraction_mod(coefficient, prime)) % prime
    return total


def q8_mod(root, prime):
    coefficients = (24, 296, 1548, 4428, 7320, 6498, 1782, -1539, -999)
    total = 0
    for coefficient in reversed(coefficients):
        total = (total * root + coefficient) % prime
    return total


def is_prime(value):
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def determinant_mod(matrix, prime):
    data = [[entry % prime for entry in row] for row in matrix]
    determinant = 1
    for column in range(len(data)):
        pivot = next((row for row in range(column, len(data))
                      if data[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            data[column], data[pivot] = data[pivot], data[column]
            determinant = -determinant
        pivot_value = data[column][column]
        determinant = determinant * pivot_value % prime
        inverse = pow(pivot_value, -1, prime)
        for row in range(column + 1, len(data)):
            if not data[row][column]:
                continue
            factor = data[row][column] * inverse % prime
            data[row] = [
                (left - factor * right) % prime
                for left, right in zip(data[row], data[column])
            ]
    return determinant % prime


def solve_mod(matrix, rhs, prime):
    rows = [
        [entry % prime for entry in row] + [right % prime]
        for row, right in zip(matrix, rhs)
    ]
    n = len(rows)
    if any(len(row) != n + 1 for row in rows):
        raise RuntimeError("non-square solve")
    for column in range(n):
        pivot = next((row for row in range(column, n) if rows[row][column]), None)
        if pivot is None:
            raise RuntimeError(("singular modular Jacobian", column, prime))
        rows[column], rows[pivot] = rows[pivot], rows[column]
        inverse = pow(rows[column][column], -1, prime)
        rows[column] = [value * inverse % prime for value in rows[column]]
        for row in range(n):
            if row == column or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                (left - factor * right) % prime
                for left, right in zip(rows[row], rows[column])
            ]
    return [row[-1] for row in rows]


def exact_q8_base():
    """Reconstruct the reviewed Q8 contact in approximate-cubic coordinates."""
    compiled = P.compile_fibre()
    tails = compiled["tails"]
    v = NF((Fraction(0), Fraction(1)))
    D0 = 3 * v ** 2 - 2
    A20 = 3 * v ** 2 + 3 * v + 1
    x5 = -36 * v ** 2 * A20 / D0
    x3 = x5 * (v + 2)
    x1 = x5 * (v + 1) + x5 ** 2 * (3 * v + 1) / (9 * v)
    raw_base = [ZERO, x1, ZERO, ONE + x3, ZERO, NF(3) + x5,
                ZERO, NF(3), ZERO]
    normals = (0, 2, 4, 6)
    odd = (3, 5, 7)
    matrix = [
        [J.nf_eval(M.cpartial(tails[ell], column), raw_base)
         for column in normals[1:]]
        for ell in odd
    ]
    rhs = [
        -J.nf_eval(M.cpartial(tails[ell], 0), raw_base)
        for ell in odd
    ]
    a2_t, a4_t, a6_t = J.solve(matrix, rhs)
    c0 = a6_t / 3
    d20 = a2_t - a6_t
    d40 = a4_t - 2 * a6_t
    return [c0, d20, d40, x1, x3, x5]


def series_add(left, right, prime):
    return [(a + b) % prime for a, b in zip(left, right)]


def series_scale(scalar, value, prime):
    return [scalar * entry % prime for entry in value]


def series_mul(left, right, prime):
    order = len(left)
    out = [0] * order
    for i, a in enumerate(left):
        if not a:
            continue
        for j in range(order - i):
            if right[j]:
                out[i + j] = (out[i + j] + a * right[j]) % prime
    return out


def series_pow(value, exponent, prime):
    order = len(value)
    out = [1] + [0] * (order - 1)
    base = value
    power = exponent
    while power:
        if power & 1:
            out = series_mul(out, base, prime)
        power >>= 1
        if power:
            base = series_mul(base, base, prime)
    return out


def series_inv(value, prime):
    if not value[0]:
        raise ZeroDivisionError("series constant")
    order = len(value)
    out = [0] * order
    out[0] = pow(value[0], -1, prime)
    for degree in range(1, order):
        correction = sum(
            value[index] * out[degree - index]
            for index in range(1, degree + 1)
        ) % prime
        out[degree] = -out[0] * correction % prime
    return out


def monomial_closure(polynomials, variable_count):
    zero = (0,) * variable_count
    monomials = {zero}
    for poly in polynomials:
        monomials.update(poly)
    queue = list(monomials)
    while queue:
        monomial = queue.pop()
        for index, exponent in enumerate(monomial):
            if exponent:
                parent = list(monomial)
                parent[index] -= 1
                parent = tuple(parent)
                if parent not in monomials:
                    monomials.add(parent)
                    queue.append(parent)
    ordered = sorted(monomials, key=lambda item: (sum(item), item))
    parents = {}
    for monomial in ordered[1:]:
        index = next(index for index, exponent in enumerate(monomial) if exponent)
        parent = list(monomial)
        parent[index] -= 1
        parents[monomial] = (tuple(parent), index)
    return ordered, parents


def row_coefficient(poly, values, degree, prime):
    return sum(
        fraction_mod(scalar, prime) * values[monomial][degree]
        for monomial, scalar in poly.items()
    ) % prime


def lift_branch(prime, root, order):
    if q8_mod(root, prime):
        raise RuntimeError(("not a Q8 root", prime, root))
    ring, rows, imposed, names = Q.compile_quotient("approx")
    if names != Q.APPROX_NAMES:
        raise RuntimeError(names)
    exact_base = exact_q8_base()
    constants = [nf_mod(value, prime, root) for value in exact_base]
    bases = [[0] * order for _ in names]
    bases[0][1] = 1
    for index, value in enumerate(constants, 1):
        bases[index][0] = value

    all_rows = [rows[ell] for ell in range(1, 9)]
    ordered, parents = monomial_closure(all_rows, len(names))
    zero_monomial = (0,) * len(names)
    values = {monomial: [0] * order for monomial in ordered}
    values[zero_monomial][0] = 1

    def recompute(degree):
        if degree:
            values[zero_monomial][degree] = 0
        for monomial in ordered[1:]:
            parent, index = parents[monomial]
            values[monomial][degree] = sum(
                values[parent][k] * bases[index][degree - k]
                for k in range(degree + 1)
            ) % prime

    recompute(0)
    equation_rows = [rows[ell] for ell in imposed]
    jacobian = []
    for row in equation_rows:
        jacobian_row = []
        for variable in range(1, len(names)):
            entry = 0
            for monomial, scalar in row.items():
                exponent = monomial[variable]
                if not exponent:
                    continue
                parent = list(monomial)
                parent[variable] -= 1
                entry += (
                    fraction_mod(scalar, prime) * exponent
                    * values[tuple(parent)][0]
                )
            jacobian_row.append(entry % prime)
        jacobian.append(jacobian_row)
    # This checks invertibility while avoiding a separate determinant routine.
    solve_mod(jacobian, [0] * 6, prime)
    jacobian_determinant = determinant_mod(jacobian, prime)
    if not jacobian_determinant:
        raise RuntimeError("zero modular Jacobian determinant")

    for degree in range(1, order):
        recompute(degree)
        origin = [
            row_coefficient(row, values, degree, prime)
            for row in equation_rows
        ]
        solution = solve_mod(jacobian, [-value for value in origin], prime)
        for index, coefficient in enumerate(solution, 1):
            bases[index][degree] = coefficient
        recompute(degree)
        residual = [
            row_coefficient(row, values, degree, prime)
            for row in equation_rows
        ]
        if any(residual):
            raise RuntimeError(("Hensel residual", degree, residual))

    def evaluate(poly):
        return [
            row_coefficient(poly, values, degree, prime)
            for degree in range(order)
        ]

    n = evaluate(rows[6])
    q = evaluate(rows[8])
    if not n[0] or not q[0]:
        raise RuntimeError(("zero output constant", n[0], q[0]))
    w = bases[0]
    c = bases[1]
    one = [1] + [0] * (order - 1)
    wc3 = series_mul(w, series_pow(c, 3, prime), prime)
    theta = series_mul(w, series_pow(series_add(one, wc3, prime), 2, prime), prime)
    Z = series_mul(
        series_pow(q, 9, prime),
        series_pow(series_inv(n, prime), 10, prime),
        prime,
    )
    return {
        "w": w,
        "theta": theta,
        "n": n,
        "q": q,
        "Z": Z,
        "coordinates": dict(zip(names[1:], bases[1:])),
        "monomial_closure_size": len(ordered),
        "jacobian_determinant": jacobian_determinant,
    }


def rref_nullvector(matrix, prime):
    if not matrix:
        return None, 0
    data = [[value % prime for value in row] for row in matrix]
    rows, columns = len(data), len(data[0])
    pivots = []
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows)
                      if data[row][column]), None)
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        inverse = pow(data[pivot_row][column], -1, prime)
        data[pivot_row] = [value * inverse % prime for value in data[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not data[row][column]:
                continue
            factor = data[row][column]
            data[row] = [
                (left - factor * right) % prime
                for left, right in zip(data[row], data[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    free = [column for column in range(columns) if column not in pivots]
    if not free:
        return None, 0
    chosen = free[-1]
    vector = [0] * columns
    vector[chosen] = 1
    for row, pivot in reversed(list(enumerate(pivots))):
        vector[pivot] = -sum(
            data[row][column] * vector[column]
            for column in free
        ) % prime
    return vector, len(free)


def relation_search(left, right, prime, max_left, max_right, max_columns,
                    holdout):
    order = len(left)
    left_powers = [[1] + [0] * (order - 1)]
    right_powers = [[1] + [0] * (order - 1)]
    for _ in range(max_left):
        left_powers.append(series_mul(left_powers[-1], left, prime))
    for _ in range(max_right):
        right_powers.append(series_mul(right_powers[-1], right, prime))
    hits = []
    tested = []
    nonzero_fit_nullities = []
    for dl in range(1, max_left + 1):
        for dr in range(1, max_right + 1):
            count = (dl + 1) * (dr + 1)
            fit_rows = order - holdout
            if count > max_columns or count > fit_rows:
                continue
            columns = [
                series_mul(left_powers[i], right_powers[j], prime)
                for i in range(dl + 1) for j in range(dr + 1)
            ]
            fit = [[column[row] for column in columns]
                   for row in range(fit_rows)]
            vector, nullity = rref_nullvector(fit, prime)
            accepted = False
            if vector is not None and nullity == 1:
                residual = [
                    sum(coefficient * column[row]
                        for coefficient, column in zip(vector, columns)) % prime
                    for row in range(fit_rows, order)
                ]
                accepted = not any(residual)
                if accepted:
                    terms = []
                    index = 0
                    for i in range(dl + 1):
                        for j in range(dr + 1):
                            if vector[index]:
                                terms.append([i, j, vector[index]])
                            index += 1
                    hits.append({
                        "left_degree": dl,
                        "right_degree": dr,
                        "columns": count,
                        "nullity_on_fit_rows": nullity,
                        "terms_mod_prime": terms,
                    })
            record = {
                "left_degree": dl,
                "right_degree": dr,
                "columns": count,
                "fit_nullity": nullity,
                "holdout_pass": accepted,
            }
            tested.append(record)
            if nullity:
                nonzero_fit_nullities.append(record)
    canonical = json.dumps(tested, sort_keys=True, separators=(",", ":"))
    return {
        "hits": hits,
        "tested_rectangles": len(tested),
        "full_column_rank_rectangles": sum(
            record["fit_nullity"] == 0 for record in tested
        ),
        "all_fit_matrices_full_column_rank": not nonzero_fit_nullities,
        "nonzero_fit_nullities": nonzero_fit_nullities,
        "max_tested_columns": max(
            (record["columns"] for record in tested), default=0
        ),
        "tested_rectangles_sha256": sha256(canonical.encode()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--root", type=int, required=True)
    parser.add_argument("--order", type=int, default=96)
    parser.add_argument("--max-left", type=int, default=16)
    parser.add_argument("--max-right", type=int, default=16)
    parser.add_argument("--max-columns", type=int, default=80)
    parser.add_argument("--holdout", type=int, default=12)
    args = parser.parse_args()
    if args.order < 4 or args.holdout < 1 or args.holdout >= args.order:
        raise RuntimeError("invalid order/holdout")
    if not is_prime(args.prime):
        raise RuntimeError(("modulus is not prime", args.prime))
    data = lift_branch(args.prime, args.root, args.order)
    pairs = {}
    for left_name, right_name in (
        ("theta", "Z"), ("w", "q"), ("n", "q"), ("theta", "q")
    ):
        pairs[f"{left_name},{right_name}"] = relation_search(
            data[left_name], data[right_name], args.prime,
            args.max_left, args.max_right, args.max_columns, args.holdout,
        )
    payload = {
        "case": "max12_912_order3_nu_q8_invariant_support_20260824",
        "prime": args.prime,
        "q8_root": args.root,
        "good_reduction": {
            "prime_by_trial_division": True,
            "Q8_at_root": q8_mod(args.root, args.prime),
            "six_by_six_jacobian_determinant": data["jacobian_determinant"],
            "all_fraction_denominators_inverted": True,
        },
        "order": args.order,
        "holdout": args.holdout,
        "max_degrees": [args.max_left, args.max_right],
        "max_columns": args.max_columns,
        "monomial_closure_size": data["monomial_closure_size"],
        "series_prefix": {
            name: values[:8]
            for name, values in data.items()
            if name in ("w", "theta", "n", "q", "Z")
        },
        "relation_searches": pairs,
        "scope": (
            "modular support learning at one Q8 specialization; a hit is not "
            "a characteristic-zero relation until lifted and substituted"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
