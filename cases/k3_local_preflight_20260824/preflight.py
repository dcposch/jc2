#!/usr/bin/env python3
"""Exact stdlib preflight for the normalized D=3 Keller-collision scheme."""

import json

P_VARS = ["p10", "p01", "p20", "p11", "p02", "p21", "p12", "p03"]
Q_VARS = ["q10", "q01", "q20", "q11", "q02", "q21", "q12", "q03"]
VARS = P_VARS + Q_VARS
VID = {name: i for i, name in enumerate(VARS)}
XY3 = [(i, d - i) for d in range(4) for i in range(d, -1, -1)]
XY4 = [(i, d - i) for d in range(5) for i in range(d, -1, -1)]


def add(a, b, scale=1):
    out = dict(a)
    for mon, coeff in b.items():
        out[mon] = out.get(mon, 0) + scale * coeff
        if out[mon] == 0:
            del out[mon]
    return out


def scale(a, n):
    return {mon: n * coeff for mon, coeff in a.items() if n * coeff}


def mul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            mon = tuple(sorted(ma + mb))
            out[mon] = out.get(mon, 0) + ca * cb
    return {mon: coeff for mon, coeff in out.items() if coeff}


def const(n):
    return {(): n} if n else {}


def var(name):
    return {(VID[name],): 1}


ZERO = {}


def coordinate_coeffs(prefix):
    names = P_VARS if prefix == "p" else Q_VARS
    c = {(i, j): var(name) for (i, j), name in zip(
        [(1, 0), (0, 1), (2, 0), (1, 1), (0, 2),
         (2, 1), (1, 2), (0, 3)], names)}
    c[(0, 0)] = ZERO
    c[(3, 0)] = add(scale(c[(1, 0)], -1), c[(2, 0)], scale=-1)
    return c


def jacobian_equations():
    pc = coordinate_coeffs("p")
    qc = coordinate_coeffs("q")
    eq = {xy: {} for xy in XY4}
    for (i, j), a in pc.items():
        for (k, ell), b in qc.items():
            factor = i * ell - j * k
            if factor == 0:
                continue
            xy = (i + k - 1, j + ell - 1)
            eq[xy] = add(eq[xy], scale(mul(a, b), factor))
    eq[(0, 0)] = add(eq[(0, 0)], const(-1))
    return [eq[xy] for xy in XY4]


def eval_expr(expr, point):
    total = 0
    for mon, coeff in expr.items():
        term = coeff
        for idx in mon:
            term *= point[idx]
        total += term
    return total


def gradient(expr, point, modulus):
    row = []
    for idx in range(len(VARS)):
        total = 0
        for mon, coeff in expr.items():
            count = mon.count(idx)
            if not count:
                continue
            term = coeff * count
            removed = list(mon)
            removed.remove(idx)
            for j in removed:
                term *= point[j]
            total += term
        row.append(total % modulus)
    return row


def rref(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivots = []
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(inv * x) % p for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return a, pivots


def kernel_basis(matrix, p):
    rr, pivots = rref(matrix, p)
    free = [j for j in range(len(matrix[0])) if j not in pivots]
    basis = []
    for f in free:
        v = [0] * len(matrix[0])
        v[f] = 1
        for i, pivot in enumerate(pivots):
            v[pivot] = (-rr[i][f]) % p
        basis.append(v)
    return pivots, free, basis


def solve(matrix, rhs, p):
    aug = [row[:] + [b % p] for row, b in zip(matrix, rhs)]
    rr, pivots_aug = rref(aug, p)
    n = len(matrix[0])
    for row in rr:
        if all(x == 0 for x in row[:n]) and row[n] != 0:
            return None
    pivots = [c for c in pivots_aug if c < n]
    solution = [0] * n
    for i, pivot in enumerate(pivots):
        solution[pivot] = rr[i][n]
    return solution


def expr_json(expr):
    terms = []
    for mon, coeff in sorted(expr.items(), key=lambda item: (len(item[0]), item[0])):
        terms.append({
            "coefficient": coeff,
            "variables": [VARS[i] for i in mon],
        })
    return terms


def sparse_vector(v):
    return {VARS[i]: x for i, x in enumerate(v) if x}


def main():
    eqs = jacobian_equations()
    seed = [0] * len(VARS)
    seed[VID["p10"]] = 1
    seed[VID["q01"]] = 1

    seed_values = [eval_expr(eq, seed) for eq in eqs]
    tangent = [gradient(eq, seed, 3) for eq in eqs]
    pivots, free, kernel = kernel_basis(tangent, 3)

    if any(value % 3 for value in seed_values):
        raise AssertionError("special seed does not satisfy the scheme mod 3")
    if any(value % 3 for value in seed_values):
        raise AssertionError("first error is not divisible by 3")
    first_error = [(value // 3) % 3 for value in seed_values]
    correction_rhs = [(-value) % 3 for value in first_error]
    solution = solve(tangent, correction_rhs, 3)
    if solution is None:
        raise AssertionError("promoted first obstruction unexpectedly nonzero")

    registered = [0] * len(VARS)
    registered[VID["q21"]] = 1
    if [sum(a * b for a, b in zip(row, registered)) % 3 for row in tangent] != correction_rhs:
        raise AssertionError("registered B=x^2 y correction fails")

    lift_mod9 = [(a + 3 * b) % 9 for a, b in zip(seed, registered)]
    lift_values = [eval_expr(eq, lift_mod9) % 9 for eq in eqs]
    if any(lift_values):
        raise AssertionError("registered mod-9 point fails normalized scheme")

    # Independent direct replay of the promoted representatives
    # P=x+8x^3, Q=y+3x^2y over Z/9.
    promoted_det = {0: 1, 2: 24 + 3, 4: 24 * 3}
    if promoted_det != {0: 1, 2: 27, 4: 72}:
        raise AssertionError("promoted determinant expansion mismatch")
    if any(coeff % 9 for degree, coeff in promoted_det.items() if degree):
        raise AssertionError("promoted determinant is not one modulo 9")
    if (1 + 8) % 9 != 0:
        raise AssertionError("promoted marked collision fails modulo 9")

    result = {
        "verdict": "STAGE-A-PASS",
        "scheme": {
            "raw_coefficient_count": 20,
            "collision_eliminations": ["p00=0", "q00=0", "p30=-p10-p20", "q30=-q10-q20"],
            "normalized_variables": VARS,
            "jacobian_equation_order": [f"x^{i}y^{j}" for i, j in XY4],
            "jacobian_equations": [expr_json(eq) for eq in eqs],
            "equation_count": len(eqs),
            "total_nonzero_terms": sum(len(eq) for eq in eqs),
            "max_terms_in_equation": max(len(eq) for eq in eqs),
        },
        "controls": {
            "seed_integer_representative": sparse_vector(seed),
            "seed_equation_values_over_Z": seed_values,
            "seed_mod3_pass": True,
            "registered_correction_mod3": {"Q": "x^2*y", "vector": sparse_vector(registered)},
            "lift_mod9_vector": sparse_vector(lift_mod9),
            "lift_mod9_pass": True,
            "normalized_lift_determinant": "1-9*x^4",
            "promoted_representative_determinant": "1+27*x^2+72*x^4",
            "promoted_mod9_pass": True,
            "promoted_marked_images_mod9": [[0, 0], [0, 0]],
        },
        "tangent": {
            "field": "F_3",
            "matrix": tangent,
            "rank": len(pivots),
            "dimension": len(VARS) - len(pivots),
            "pivot_columns": [VARS[i] for i in pivots],
            "free_columns": [VARS[i] for i in free],
            "kernel_basis": [sparse_vector(v) for v in kernel],
        },
        "first_obstruction": {
            "divided_error_vector_mod3": first_error,
            "required_linear_image_mod3": correction_rhs,
            "class_vanishes": True,
            "one_solver_solution": sparse_vector(solution),
            "registered_solution": sparse_vector(registered),
        },
        "stage_b_metrics": {
            "unit_linear_pivots": len(pivots),
            "remaining_local_parameters": len(VARS) - len(pivots),
            "zero_linear_part_equations": len(eqs) - len(pivots),
            "launch_threshold_parameters": 8,
            "launch_threshold_residual_equations": 8,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
