#!/usr/bin/env python3
"""Second-layer elimination for the D43 a00pp compatibility residual.

INTERNAL / UNREVIEWED.  This driver works only with the exact, point-
specialized normal-form row banks made by :mod:`d43_nf_certificate`.  It
never sends the full 86-row verdict file to a solver.

The 52 compatibility rows are affine in the 92 level >= 53 tails.  At the
all-lower-tails-zero point their coefficient matrix has rank 44.  We use a
canonical nonzero 44 by 44 constant minor, compute the eight remaining
Schur directions to first order, and retain the first eight lower variables
that give full residual Jacobian rank.  Setting every other external
coordinate to zero gives an exact 52-equation/52-variable slice of degree at
most three.  A solution proves NONEMPTY for the literal emitted 52 by 144
compatibility presentation.  It is not, by itself, a graph-preserving D43
prolongation: coordinates eliminated at one rung can occur again later, so
``d43_lift_witness.py`` supplies the mandatory semantic lift gate.
"""

import argparse
import hashlib
import json
import os
import pickle
import re
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import d43_family2 as F
import d43_nf_certificate as NF


PRIMES = NF.PRIMES
RUNG_SIZES = (6, 6, 5, 6, 6, 6, 6, 6, 5)
RUNGS = tuple(range(26, 43, 2))


def pivot_columns(matrix, p):
    """RREF pivot columns of a numeric matrix over F_p."""
    if not matrix:
        return []
    work = [[x % p for x in row] for row in matrix]
    nr, nc = len(work), len(work[0])
    rank = 0
    pivots = []
    for col in range(nc):
        pivot = next((i for i in range(rank, nr) if work[i][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], p - 2, p)
        work[rank] = [x * inv % p for x in work[rank]]
        for i in range(nr):
            if i != rank and work[i][col]:
                scale = work[i][col]
                work[i] = [(x - scale * y) % p
                           for x, y in zip(work[i], work[rank])]
        pivots.append(col)
        rank += 1
        if rank == nr:
            break
    return pivots


def solve_square(matrix, rhs, p):
    """Solve a nonsingular square numeric system over F_p."""
    n = len(matrix)
    assert n and all(len(row) == n for row in matrix) and len(rhs) == n
    work = [[x % p for x in row] + [value % p]
            for row, value in zip(matrix, rhs)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if work[i][col]), None)
        assert pivot is not None, ("singular square system", col)
        work[col], work[pivot] = work[pivot], work[col]
        inv = pow(work[col][col], p - 2, p)
        work[col] = [x * inv % p for x in work[col]]
        for i in range(n):
            if i != col and work[i][col]:
                scale = work[i][col]
                work[i] = [(x - scale * y) % p
                           for x, y in zip(work[i], work[col])]
    return [row[-1] for row in work]


def load_rows(path, p):
    with open(path, "rb") as fh:
        bank = pickle.load(fh)
    assert bank["prime"] == p and bank["fiber"] == "a00pp"
    assert tuple(bank["rung_sizes"]) == RUNG_SIZES
    rows = bank["rows"]
    assert len(rows) == sum(RUNG_SIZES) == 52
    return bank, rows


def external_variables(rows):
    return sorted({name for row in rows for mono in row for name in mono})


def high_variables(rows):
    variables = external_variables(rows)
    return {name for name in variables
            if (NF.deep_level(name, F.X2T) or -1) >= 53}


def constant_layer(rows, p):
    """Return the canonical rank-44 constant Schur data at lower=0."""
    variables = external_variables(rows)
    high = high_variables(rows)
    high_order, columns, constants = NF.affine_split_rows(rows, high)
    A0 = [[columns[name][i].get((), 0) for name in high_order]
          for i in range(len(rows))]
    pivot_cols = pivot_columns(A0, p)
    assert len(pivot_cols) == 44
    # Pivots of the transpose select independent rows for that column basis.
    transposed = [[A0[i][j] for i in range(len(rows))]
                  for j in pivot_cols]
    pivot_rows = pivot_columns(transposed, p)
    assert len(pivot_rows) == 44
    other_rows = [i for i in range(len(rows)) if i not in pivot_rows]
    matrix = [[A0[i][j] for j in pivot_cols] for i in pivot_rows]
    y0 = solve_square(matrix,
                      [-constants[i].get((), 0) % p for i in pivot_rows], p)
    residual0 = []
    for i in other_rows:
        residual0.append((constants[i].get((), 0) +
                          sum(A0[i][j] * value
                              for j, value in zip(pivot_cols, y0))) % p)
    return {
        "variables": variables,
        "high": high,
        "high_order": high_order,
        "columns": columns,
        "constants": constants,
        "A0": A0,
        "pivot_cols": pivot_cols,
        "pivot_rows": pivot_rows,
        "other_rows": other_rows,
        "matrix": matrix,
        "y0": y0,
        "residual0": residual0,
    }


def residual_jacobian(data, p):
    """Derivative of the eight Schur residuals at lower=0.

    This differentiates M(x)y(x)+b_R(x)=0, including dM*y.  It is an
    independent second-NF gate, not a finite-difference probe.
    """
    lower = sorted(set(data["variables"]) - data["high"])
    columns = data["columns"]
    constants = data["constants"]
    A0 = data["A0"]
    pc = data["pivot_cols"]
    pr = data["pivot_rows"]
    nr = data["other_rows"]
    matrix = data["matrix"]
    y0 = data["y0"]
    order = data["high_order"]
    jac_columns = []
    for variable in lower:
        derivative_rhs = []
        for i in pr:
            value = constants[i].get((variable,), 0)
            value += sum(columns[order[j]][i].get((variable,), 0) * y
                         for j, y in zip(pc, y0))
            derivative_rhs.append(-value % p)
        dy = solve_square(matrix, derivative_rhs, p)
        residual_derivative = []
        for i in nr:
            value = constants[i].get((variable,), 0)
            value += sum(columns[order[j]][i].get((variable,), 0) * y +
                         A0[i][j] * derivative_y
                         for j, y, derivative_y in zip(pc, y0, dy))
            residual_derivative.append(value % p)
        jac_columns.append(residual_derivative)
    jacobian = [list(row) for row in zip(*jac_columns)]
    pivots = pivot_columns(jacobian, p)
    assert len(pivots) == 8
    chosen_lower = [lower[j] for j in pivots]
    return lower, jacobian, chosen_lower


def restrict_rows(rows, keep):
    """Specialize variables outside keep to zero, exactly."""
    keep = set(keep)
    return [{mono: coeff for mono, coeff in row.items()
             if all(name in keep for name in mono)} for row in rows]


def emit_ms(path, variables, rows, p):
    NF.emit_external_ms(path, list(variables), rows, p)


def evaluate_rows(rows, assignment, p):
    values = []
    for row in rows:
        total = 0
        for mono, coeff in row.items():
            value = coeff
            for name in mono:
                value = value * assignment.get(name, 0) % p
            total = (total + value) % p
        values.append(total)
    return values


def jacobian_rank(rows, variables, assignment, p):
    matrix = []
    for row in rows:
        gradient = []
        for variable in variables:
            value = 0
            for mono, coeff in row.items():
                count = mono.count(variable)
                if not count:
                    continue
                term = coeff * count % p
                removed = False
                for name in mono:
                    if name == variable and not removed:
                        removed = True
                    else:
                        term = term * assignment.get(name, 0) % p
                value = (value + term) % p
            gradient.append(value)
        matrix.append(gradient)
    return NF.matrix_rank(matrix, p)


def build_one(p, rows_path, out_prefix):
    bank, rows = load_rows(rows_path, p)
    data = constant_layer(rows, p)
    lower, jacobian, chosen_lower = residual_jacobian(data, p)
    chosen_high = [data["high_order"][j] for j in data["pivot_cols"]]
    keep = chosen_lower + chosen_high
    assert len(chosen_lower) == 8 and len(chosen_high) == 44
    assert len(keep) == len(set(keep)) == 52
    restricted = restrict_rows(rows, keep)
    used = {name for row in restricted for mono in row for name in mono}
    assert used == set(keep)
    degrees = [max(map(len, row), default=0) for row in restricted]
    assert max(degrees) <= 3
    # The six-term rung-36 row becomes one nonzero linear term.  This is a
    # strong negative control against accidentally dropping all low residuals.
    assert len(restricted[34]) == 1
    (linear_mono, linear_coeff), = restricted[34].items()
    assert len(linear_mono) == 1 and linear_coeff

    ms_path = "%s_p%d.ms" % (out_prefix, p)
    emit_ms(ms_path, keep, restricted, p)
    canonical = hashlib.sha256()
    for row in restricted:
        for mono, coeff in sorted(row.items()):
            canonical.update((str(coeff) + "*" + "*".join(mono) + "\n").encode())
        canonical.update(b",\n")
    report = {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p,
        "fiber": "a00pp",
        "source_rows": rows_path,
        "source_support_sha256": hashlib.sha256(
            open(rows_path, "rb").read()).hexdigest(),
        "first_layer": {
            "rows": 52,
            "external_variables": len(data["variables"]),
            "affine_level_ge_53_variables": len(data["high"]),
            "rank_at_lower_origin": 44,
            "residual_dimension": 8,
            "pivot_rows_zero_based": data["pivot_rows"],
            "nonpivot_rows_zero_based": data["other_rows"],
            "origin_residual": data["residual0"],
        },
        "second_layer_slice": {
            "lower_variables": chosen_lower,
            "high_pivot_variables": chosen_high,
            "variables": keep,
            "rows": len(restricted),
            "terms": sum(map(len, restricted)),
            "max_degree": max(degrees),
            "degrees": degrees,
            "residual_jacobian_rank_at_origin": NF.matrix_rank(jacobian, p),
            "rung36_linear_gate": {"row_zero_based": 34,
                                    "variable": linear_mono[0],
                                    "coefficient": linear_coeff},
            "specialization": "all other 92 external variables = 0",
            "msolve_input": ms_path,
            "canonical_sha256": canonical.hexdigest(),
        },
        "gates": {
            "affine_split_exact": "PASS",
            "constant_minor_rank_44": "PASS",
            "analytic_residual_jacobian_rank_8": "PASS",
            "restriction_is_literal_zero_specialization": "PASS",
            "negative_control_rung36_row_survives": "PASS",
        },
    }
    report_path = "%s_p%d.json" % (out_prefix, p)
    with open(report_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 SECOND LAYER p=%d: 52x144 -> 52x52, %d terms, degree <= %d"
          " -> %s" % (p, sum(map(len, restricted)), max(degrees), ms_path),
          flush=True)
    return report


def verify_witness(p, rows_path, witness_path, out_path=None):
    """Verify a rational F_p witness for the specialized and parked rows."""
    bank, rows = load_rows(rows_path, p)
    witness = json.load(open(witness_path))
    assignment = {name: int(value) % p
                  for name, value in witness["external_point"].items()}
    variables = external_variables(rows)
    assert set(assignment) == set(variables)
    values = evaluate_rows(rows, assignment, p)
    assert values == [0] * 52, [(i, x) for i, x in enumerate(values) if x]

    replay_path = os.path.join(HERE, "d25_certificate_replay.json")
    parked_path = os.path.join(HERE, "d25fam_p%d_a00pp.ms" % p)
    record = json.load(open(replay_path))["parked_fibers"][str(p)]["a00pp"]
    cell = NF.build_cell_map(parked_path, replay_path,
                             int(bank["W1"]), int(bank["W2"]))
    free_values = [int(bank["free"][name]) % p for name in NF.FREE]
    parked_point = dict(zip(NF.FREE, free_values))
    parked_point.update(cell["fixed"])
    for name, poly in cell["maps"].items():
        parked_point[name] = NF.eval_free_poly(poly, free_values, p)
    parked_names, parked_prime, parked_rows = NF.parse_ms(parked_path)
    assert parked_prime == p
    parked_values = [NF.eval_named_poly(row, parked_names, parked_point, p)
                     for row in parked_rows]
    assert parked_values == [0] * 34

    compat_rank = jacobian_rank(rows, variables, assignment, p)
    parked_rank = jacobian_rank_named(parked_rows, parked_names,
                                      parked_point, p)
    assert compat_rank == 52 and parked_rank == 14
    full_point = dict(parked_point)
    assert not (set(full_point) & set(assignment))
    full_point.update(assignment)
    assert len(full_point) == 172

    result = {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p,
        "fiber": "a00pp",
        "cell": {"W1": int(bank["W1"]), "W2": int(bank["W2"]),
                 "free": dict(zip(NF.FREE, free_values))},
        "external_point": assignment,
        "parked_point": parked_point,
        "full_172_point": full_point,
        "gates": {
            "compatibility_rows_zero": "52/52",
            "parked_rows_zero": "34/34",
            "compatibility_external_jacobian_rank": compat_rank,
            "parked_jacobian_rank": parked_rank,
            "negative_control": negative_control(rows, variables,
                                                 assignment, p),
        },
        "dimension": {
            "fixed_D25_cell_point_smooth_local_dimension": 144 - compat_rank,
            "full_cell_smooth_local_dimension": 172 - compat_rank - parked_rank,
            "full_cell_component_dimension": 172 - compat_rank - parked_rank,
        },
    }
    if out_path:
        with open(out_path, "w") as fh:
            json.dump(result, fh, indent=1, sort_keys=True)
            fh.write("\n")
    print("D43 WITNESS p=%d: PASS 34/34 + 52/52; Jacobian ranks 14+52; "
          "smooth cell component dim 106" % p)
    return result


def witness_from_linear_gb(p, rows_path, gb_path, witness_path,
                           report_path=None):
    """Decode a 52-element linear reduced GB and verify the full NF point."""
    text = open(gb_path).read()
    match = re.search(r"#variable order:\s*(.+)\n", text)
    assert match, "missing variable-order header"
    order = [name.strip() for name in match.group(1).split(",")]
    assert len(order) == 52 and len(set(order)) == 52
    match = re.search(r"\[([^\]]*)\]:\s*$", text, re.S)
    assert match, "missing printed Groebner basis"
    polynomials = [item.strip() for item in match.group(1).split(",")
                   if item.strip()]
    assert len(polynomials) == 52
    solved = {}
    pattern = re.compile(r"1\*([A-Za-z0-9_]+)\^1(?:\+([0-9]+))?$")
    for polynomial in polynomials:
        parsed = pattern.fullmatch(polynomial)
        assert parsed, ("nonlinear or nonmonic GB element", polynomial)
        name, constant = parsed.groups()
        assert name in order and name not in solved
        solved[name] = (-int(constant or 0)) % p
    assert set(solved) == set(order)

    _bank, rows = load_rows(rows_path, p)
    assignment = {name: 0 for name in external_variables(rows)}
    assignment.update(solved)
    assert evaluate_rows(rows, assignment, p) == [0] * 52
    payload = {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p,
        "source": "unique rational point decoded from 52-element linear "
                  "reduced Groebner basis of the exact second-layer slice",
        "gb_output": gb_path,
        "slice_point": solved,
        "external_point": assignment,
    }
    with open(witness_path, "w") as fh:
        json.dump(payload, fh, indent=1, sort_keys=True)
        fh.write("\n")
    return verify_witness(p, rows_path, witness_path, report_path)


def jacobian_rank_named(rows, names, assignment, p):
    matrix = []
    for row in rows:
        gradient = []
        for index, variable in enumerate(names):
            value = 0
            for mono, coeff in row.items():
                power = mono[index]
                if not power:
                    continue
                term = coeff * power % p
                for j, exponent in enumerate(mono):
                    if exponent:
                        term = term * pow(assignment[names[j]],
                                          exponent - (1 if j == index else 0),
                                          p) % p
                value = (value + term) % p
            gradient.append(value)
        matrix.append(gradient)
    return NF.matrix_rank(matrix, p)


def negative_control(rows, variables, assignment, p):
    for name in variables:
        bad = dict(assignment)
        bad[name] = (bad[name] + 1) % p
        values = evaluate_rows(rows, bad, p)
        count = sum(value != 0 for value in values)
        if count:
            return {"perturbed": name, "nonzero_compatibility_rows": count,
                    "result": "PASS"}
    raise AssertionError("negative control escaped every coordinate")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=PRIMES, required=True)
    parser.add_argument("--rows")
    parser.add_argument("--out-prefix",
                        default=os.path.join(HERE, "d43_second_layer"))
    parser.add_argument("--witness")
    parser.add_argument("--witness-report")
    parser.add_argument("--gb-out")
    parser.add_argument("--emit-witness")
    args = parser.parse_args()
    rows_path = args.rows or os.path.join(
        HERE, "d43_nf_quickshot_p%d_rows.pkl" % args.prime)
    if args.gb_out:
        if not args.emit_witness:
            parser.error("--gb-out requires --emit-witness")
        witness_from_linear_gb(args.prime, rows_path, args.gb_out,
                               args.emit_witness, args.witness_report)
    elif args.witness:
        verify_witness(args.prime, rows_path, args.witness,
                       args.witness_report)
    else:
        build_one(args.prime, rows_path, args.out_prefix)


if __name__ == "__main__":
    main()
