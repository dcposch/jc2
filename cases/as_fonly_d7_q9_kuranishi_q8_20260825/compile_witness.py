#!/usr/bin/env python3
"""Exact Q9-witness to Q8 Lyapunov--Schmidt transition over F3."""
from __future__ import annotations

import contextlib
import hashlib
import io
import os
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
Q9 = (ROOT / "cases/as_fonly_d7_vertical_q9_state_gate_20260825"
      / "compile_shard.py")
EXPECTED_Q9_SHA = "54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2"
source_bytes = Q9.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == EXPECTED_Q9_SHA
source = source_bytes.decode()
marker = '\nshard_count = int(os.environ.get("SHARD_COUNT", "27"))\n'
assert source.count(marker) == 1
scope = {"__file__": str(Q9), "__name__": "__q9_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(Q9), "exec"), scope)

structural = scope["structural"]
frob = scope["frob"]
unknowns = scope["unknowns"]
new_names = scope["new_names"]
canonical_source = scope["canonical_source"]
new_polynomials = scope["new_polynomials"]
source_rows = scope["source_rows"]
nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
nbracket = scope["nbracket"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
homogeneous_numeric = scope["homogeneous_numeric"]
row = scope["row"]

# First witness frozen in the 27-way Q9 aggregate.
predecessor_vector = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
)
q9_vector = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0,
)
predecessor_names = structural + frob + unknowns
assert len(predecessor_names) == len(predecessor_vector) == 30
assert len(new_names) == len(q9_vector) == 32
predecessor = dict(zip(predecessor_names, predecessor_vector))
source_data = canonical_source(predecessor)
assert source_rows(source_data, q9_vector) == [0] * 23

y_names = (
    tuple(f"c3_{i}" for i in range(4))
    + tuple(f"d3_{i}" for i in range(4))
    + tuple(f"w4_{i}" for i in range(5))
    + tuple(f"z4_{i}" for i in range(5))
    + tuple(f"w6_{i}" for i in range(7))
    + tuple(f"z6_{i}" for i in range(7))
)
assert len(y_names) == 32


def y_polynomials(values):
    assignment = dict(zip(y_names, values))
    C3 = homogeneous_numeric(3, [assignment[f"c3_{i}"] for i in range(4)])
    D3 = homogeneous_numeric(3, [assignment[f"d3_{i}"] for i in range(4)])
    W4 = homogeneous_numeric(4, [assignment[f"w4_{i}"] for i in range(5)])
    Z4 = homogeneous_numeric(4, [assignment[f"z4_{i}"] for i in range(5)])
    W6 = homogeneous_numeric(6, [assignment[f"w6_{i}"] for i in range(7)])
    Z6 = homogeneous_numeric(6, [assignment[f"z6_{i}"] for i in range(7)])
    return C3, D3, W4, Z4, W6, Z6


def transition_rows(xvalues, yvalues, return_blocks=False):
    C2, D2, C4, D4, W7, Z7 = new_polynomials(xvalues)
    C3, D3, W4, Z4, W6, Z6 = y_polynomials(yvalues)
    C = nadd(source_data["Cbase"], C2, C3, C4)
    D = nadd(source_data["Dbase"], D2, D3, D4)
    W = nadd(W4, W6, W7)
    Z = nadd(Z4, Z6, Z7)

    E = nadd(source_data["L1"], source_data["K"],
             nderivative(C, 0), nderivative(D, 1))
    cx, cy = nderivative(C, 0), nderivative(C, 1)
    dx, dy = nderivative(D, 0), nderivative(D, 1)
    M = nadd(nmul(source_data["A"], dy),
             nmul(cx, source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], dx)),
             nscale(-1, nmul(cy, source_data["vx"])))

    # These quotients are independent of the new E_2 image variables.
    # Exact divisibility is asserted before any reduction modulo three.
    E1_3 = divide_exact(degree_part(E, 3), 3)
    E1_5 = divide_exact(degree_part(E, 5), 3)
    assert degree_part(E, 8) == {}
    F3 = nadd(E1_3, degree_part(M, 3),
              nderivative(W4, 0), nderivative(Z4, 1))
    F5 = nadd(E1_5, degree_part(M, 5),
              nderivative(W6, 0), nderivative(Z6, 1))

    F8 = degree_part(M, 8)
    F1_8 = divide_exact(F8, 3)
    N8 = degree_part(nbracket(C, D), 8)
    T = nadd(nmul(source_data["A"], nderivative(Z, 1)),
             nmul(nderivative(W, 0), source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], nderivative(Z, 0))),
             nscale(-1, nmul(nderivative(W, 1), source_data["vx"])))
    G8 = nadd(F1_8, N8, degree_part(T, 8))
    blocks = (row(E, 2), row(F3, 3), row(F5, 5), row(G8, 8))
    if return_blocks:
        return blocks
    return sum((list(block) for block in blocks), [])


def matrix_and_rhs(function, xvalues, variable_count):
    zero = (0,) * variable_count
    b = function(xvalues, zero)
    columns = []
    for index in range(variable_count):
        basis = [0] * variable_count
        basis[index] = 1
        value = function(xvalues, tuple(basis))
        columns.append([(a - c) % 3 for a, c in zip(value, b)])
    A = [[columns[col][r] for col in range(variable_count)]
         for r in range(len(b))]
    ones = (1,) * variable_count
    predicted = [(b[r] + sum(A[r])) % 3 for r in range(len(b))]
    assert function(xvalues, ones) == predicted
    return A, b


def rref(A, b):
    work = [[value % 3 for value in line] + [(-constant) % 3]
            for line, constant in zip(A, b)]
    rank = 0
    pivots = []
    for col in range(len(A[0])):
        pivot = next((r for r in range(rank, len(work)) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        if work[rank][col] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
        for r in range(len(work)):
            if r != rank and work[r][col]:
                scalar = work[r][col]
                work[r] = [(x - scalar * y) % 3
                           for x, y in zip(work[r], work[rank])]
        pivots.append(col)
        rank += 1
    incompatible = any(all(value == 0 for value in line[:-1]) and line[-1]
                       for line in work)
    witness = None
    if not incompatible:
        witness0 = [0] * len(A[0])
        for r, pivot in enumerate(pivots):
            witness0[pivot] = work[r][-1]
        witness = tuple(witness0)
    return rank, rank + int(incompatible), pivots, work, witness


A22, b22 = matrix_and_rhs(transition_rows, q9_vector, len(y_names))
rank22, aug22, pivots22, work22, y_witness = rref(A22, b22)
assert y_witness is not None
assert transition_rows(q9_vector, y_witness) == [0] * 22

# The first thirteen rows are the image equations.  Their kernel has the
# expected Lyapunov--Schmidt dimension 19.  The rank increment is the exact
# rank of the nine-row Kuranishi map on that kernel.
A13, b13 = A22[:13], b22[:13]
rank13, aug13, _, _, _ = rref(A13, b13)
assert aug13 == rank13
kuranishi_rank = rank22 - rank13

blocks0 = transition_rows(q9_vector, (0,) * len(y_names), True)
print("source_shapes", 23, 32, 3, 4, 6, 9, 32)
print("accepted_image_rank", rank13)
print("accepted_image_kernel_dimension", len(y_names) - rank13)
print("full_transition_rank_pair", (rank22, aug22))
print("kuranishi_rank_on_image_kernel", kuranishi_rank)
print("kuranishi_cokernel_dimension", 9 - kuranishi_rank)
print("transition_fiber_size", 3 ** (len(y_names) - rank22))
print("zero_y_block_residuals", tuple(tuple(block) for block in blocks0))
print("q8_first_witness", list(y_witness))
print("PASS-Q9-WITNESS-Q8-KURANISHI")

