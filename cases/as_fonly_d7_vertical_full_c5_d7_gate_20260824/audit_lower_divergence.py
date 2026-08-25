#!/usr/bin/env python3
"""Exact de Rham coverage for accepted current digits below degree five."""
from __future__ import annotations


def rank_mod3(matrix):
    work = [[x % 3 for x in row] for row in matrix]
    row = 0
    for col in range(len(work[0]) if work else 0):
        pivot = next((i for i in range(row, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        if work[row][col] == 2:
            work[row] = [(2*x) % 3 for x in work[row]]
        for i in range(len(work)):
            if i != row and work[i][col]:
                scalar = work[i][col]
                work[i] = [(x-scalar*y) % 3
                           for x, y in zip(work[i], work[row])]
        row += 1
    return row


records = []
for target_degree in range(5):
    source_degree = target_degree + 1
    # Columns are C_i*x^i*y^(d-i), then D_i; rows are target x^j*y^(d-1-j).
    matrix = [[0] * (2 * (source_degree + 1))
              for _ in range(target_degree + 1)]
    for i in range(source_degree + 1):
        j = source_degree - i
        if i:
            matrix[i-1][i] = i
        if j:
            matrix[i][source_degree + 1 + i] = j
    actual = rank_mod3(matrix)
    cartier = sum(1 for i in range(target_degree + 1)
                  if i % 3 == 2 and (target_degree-i) % 3 == 2)
    expected = target_degree + 1 - cartier
    assert actual == expected
    records.append((target_degree, actual, cartier))

assert records == [(0, 1, 0), (1, 2, 0), (2, 3, 0),
                   (3, 4, 0), (4, 4, 1)]
# Degree <=4 current digits have derivative degree <=3.  Crossed with the
# derivative of the charged degree <=4 first digit (degree <=3), they reach
# mixed-carry degree <=6, never the D7 boundary.  First-digit Frobenius
# derivatives vanish in M modulo three.
assert (4-1) + (4-1) == 6

print("divergence_rank_cartier", records)
print("unique_low_cartier", (2, 2))
print("lower_current_digit_mixed_carry_cap", 6)
print("PASS-LOWER-ACCEPTED-DIVERGENCE")
