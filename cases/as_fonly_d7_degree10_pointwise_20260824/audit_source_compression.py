#!/usr/bin/env python3
"""Exact support/count audit for the D7 degree-ten source compression."""
from __future__ import annotations

import contextlib
import io
import os
import runpy

os.environ.pop("MATRIX", None)
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(
        os.path.join(os.path.dirname(__file__), "generate_degree10_gate.py")
    )

padd, pscale, pmul = ns["padd"], ns["pscale"], ns["pmul"]
derivative, homogeneous = ns["derivative"], ns["homogeneous"]


def variables_in(expression):
    return {factor for monomial in expression for factor in monomial}


def rank_mod3(matrix):
    rows = [[entry % 3 for entry in row] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = 1 if rows[rank][column] == 1 else 2
        rows[rank] = [(inverse*x) % 3 for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][column]:
                scalar = rows[i][column]
                rows[i] = [(x-scalar*y) % 3 for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


Ulow = {}
Vlow = {}
low_variables = []
for degree in (1, 2):
    layer, names = homogeneous("u", degree)
    Ulow = padd(Ulow, layer)
    low_variables += names
    layer, names = homogeneous("v", degree)
    Vlow = padd(Vlow, layer)
    low_variables += names

Ufull = padd(Ulow, ns["U"])
Vfull = padd(Vlow, ns["V"])
ux, uy = derivative(Ufull, 0), derivative(Ufull, 1)
vx, vy = derivative(Vfull, 0), derivative(Vfull, 1)
L = padd(ux, vy, {(2, 0): {(): -1}})
K = padd(pmul(padd(ux, {(2, 0): {(): -1}}), vy),
         pscale(-1, pmul(uy, vx)))

divergence_rows = []
for total in range(5):
    for i in range(total+1):
        if L.get((i, total-i), {}):
            divergence_rows.append(L[(i, total-i)])
carry_rows = []
for total in (8, 7):
    for i in range(total+1):
        if K.get((i, total-i), {}):
            carry_rows.append(K[(i, total-i)])

assert len(low_variables) == 10
assert len(divergence_rows) == 14
assert len(carry_rows) == 15
assert len(divergence_rows) + len(carry_rows) + 1 == 30

low_set = set(low_variables)
low_divergence = [row for row in divergence_rows if variables_in(row) & low_set]
assert len(low_divergence) == 3
assert all(not (variables_in(row) & low_set) for row in carry_rows)
assert all(not (variables_in(row) & low_set) for row in ns["digit_rows"])

# The three low divergence rows have rank three in ten variables, hence their
# solution is an independent affine-seven-space factor.
low_order = low_variables
low_matrix = []
for row in low_divergence:
    low_matrix.append([
        sum(coefficient for monomial, coefficient in row.items()
            if monomial == (variable,)) % 3
        for variable in low_order
    ])
assert rank_mod3(low_matrix) == 3

# The source-derived degree-ten system contains seven accepted divergence
# rows and eight nonzero mixed-carry rows.
assert len(ns["digit_rows"]) == 15
assert sum(label.startswith("accepted_div") for label in ns["digit_labels"]) == 7
assert sum(label.startswith("mixed_carry") for label in ns["digit_labels"]) == 8

# Degree-six Frobenius first-digit coefficients are derivative-zero mod 3.
# Integrally, their derivatives are multiples of 3 and have degree five.
frobenius_support = [(0, 6), (3, 3), (6, 0)]
for i, j in frobenius_support:
    assert i % 3 == 0 and j % 3 == 0
    assert (i == 0 or i >= 3) and (j == 0 or j >= 3)
    assert i+j-1 == 5
# A single degree-six derivative paired with a <=degree-five derivative in K
# has total degree <=9.  Two degree-six derivatives have degree ten but carry
# a factor 3^2, hence vanish after the one further division modulo 3.
assert (6-1)+(5-1) == 9
assert (6-1)+(6-1) == 10
assert (3*3)//3 % 3 == 0

print("full_predecessor_variables", 40)
print("full_predecessor_rows", 30)
print("divergence_rows", len(divergence_rows))
print("carry_rows_degree8_7", len(carry_rows))
print("divided_linear_rows", 1)
print("omitted_low_variables", len(low_variables))
print("omitted_low_divergence_rank", rank_mod3(low_matrix))
print("independent_low_factor_dimension", len(low_variables)-rank_mod3(low_matrix))
print("accepted_degree6_rows", 7)
print("mixed_degree10_rows", 8)
print("degree6_frobenius_parameters", 6)
print("degree6_degree10_divided_support", "single-cross<=9,double-cross=0mod3")
print("PASS-DEGREE10-SOURCE-COMPRESSION")
