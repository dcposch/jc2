#!/usr/bin/env python3
"""Exact D=3 identity-gauge positive control over Z/8."""
from __future__ import annotations

A = {(1, 0): 1}
B = {(0, 1): 1}
P = {(1, 0): 1, (2, 0): 7}
Q = {(0, 1): 1, (1, 1): 2, (2, 1): 4}
assert max(sum(xy) for xy in A | B) <= 3
assert max(sum(xy) for xy in P | Q) == 3
assert (1 - 2) * (1 + 2 + 4) % 8 == 1
print("A", A)
print("B", B)
print("P", P)
print("Q", Q)
print("PASS-AS-P2-DEPTH3-D3-IDENTITY-CONTROL")
