#!/usr/bin/env python3
"""Reconstruct representative vertical current digits and top next carry."""
from __future__ import annotations

import contextlib
import io
import runpy
from pathlib import Path

path = str(Path(__file__).with_name("generate_corrected.py"))
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(path)


def evaluate(expr, values):
    return ns["eval_expr"](expr, values)


def solve_mod3(matrix, rhs):
    """Return the lexicographic-zero-free-variable solution of A*x=-rhs."""
    work = [[entry % 3 for entry in row] + [(-value) % 3]
            for row, value in zip(matrix, rhs)]
    ncols = len(matrix[0])
    pivots = []
    row = 0
    for col in range(ncols):
        pivot = next((i for i in range(row, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        if work[row][col] == 2:
            work[row] = [(2*x) % 3 for x in work[row]]
        for i in range(len(work)):
            if i != row and work[i][col]:
                scalar = work[i][col]
                work[i] = [(a-scalar*b) % 3
                           for a, b in zip(work[i], work[row])]
        pivots.append(col)
        row += 1
    for line in work:
        assert any(line[:ncols]) or line[-1] == 0, line
    answer = [0]*ncols
    for i, col in enumerate(pivots):
        answer[col] = work[i][-1]
    assert all((sum(a*x for a, x in zip(line, answer))+value) % 3 == 0
               for line, value in zip(matrix, rhs))
    return answer


def bracket(left, right):
    out = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            if i and ell:
                key = (i+k-1, j+ell-1)
                out[key] = (out.get(key, 0)+i*ell*a*b) % 3
            if j and k:
                key = (i+k-1, j+ell-1)
                out[key] = (out.get(key, 0)-j*k*a*b) % 3
    return {key: value for key, value in out.items() if value % 3}


representatives = {
    3: ((0, 0, 0, 1, 1, 0, 0), (0, 0, 2, 0, 0, 0)),
    9: ((0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0)),
    81: ((0, 0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 0, 1)),
    729: ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0)),
}

for fiber_count, (base_values, f_values) in representatives.items():
    P, Q, R, T, s, w, h = base_values
    fua, fa, fb, fc, fd, fvb = f_values
    values = dict(zip(("Pp", "Qq", "Rr", "Tt", "s", "w", "h"),
                      base_values))
    values.update(zip(("fua", "fa", "fb", "fc", "fd", "fvb"), f_values))
    # Inverse of the triangular coordinate change, in F3.
    values.update({
        "r": (R+s*h) % 3,
        "t": (T+w*h) % 3,
        "p": (P+R*h+2*s*h*h) % 3,
        "q": (Q+T*h+2*w*h*h) % 3,
    })
    for name in ns["ns"]["base_vars"]:
        values.setdefault(name, 0)
    for name, expression in ns["normal"].items():
        values[name] = evaluate(expression, values)
    numeric_matrix = [[evaluate(entry, values) for entry in row]
                      for row in ns["matrix"]]
    numeric_rhs = [evaluate(entry, values) for entry in ns["rhs"]]
    solution = solve_mod3(numeric_matrix, numeric_rhs)
    values.update(zip(ns["free"], solution))

    coefficients = {}
    for name in ns["c6vars"]+ns["d6vars"]+ns["ns"]["cvars"]+ns["ns"]["dvars"]:
        coefficients[name] = evaluate(ns["sub_digits"].get(name, ns["var"](name)),
                                      values)
        values[name] = coefficients[name]
    C = {}
    D = {}
    for degree, cnames, dnames in (
        (6, ns["c6vars"], ns["d6vars"]),
        (7, ns["ns"]["cvars"], ns["ns"]["dvars"]),
    ):
        for i, name in enumerate(cnames):
            if coefficients[name]:
                C[(i, degree-i)] = coefficients[name]
        for i, name in enumerate(dnames):
            if coefficients[name]:
                D[(i, degree-i)] = coefficients[name]
    N = bracket(C, D)
    N12 = {key: value for key, value in N.items() if sum(key) == 12}
    N11 = {key: value for key, value in N.items() if sum(key) == 11}
    print("FIBER-COUNT", fiber_count)
    print("base", base_values, "frobenius", f_values)
    print("free_solution", tuple(zip(ns["free"], solution)))
    print("C_support", sorted(C.items()))
    print("D_support", sorted(D.items()))
    print("N12", sorted(N12.items()))
    print("N11", sorted(N11.items()))
    print("PASS-REPRESENTATIVE", fiber_count)
