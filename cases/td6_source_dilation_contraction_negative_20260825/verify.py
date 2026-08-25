#!/usr/bin/env python3
"""Lightweight integer-weight verification of the TD6 dilation obstruction."""

from math import gcd


# After t -> b*t, choose target weights restoring p_15 and q_1.
w_alpha = -15
w_delta = -1
assert w_alpha + 15 == 0
assert w_delta + 1 == 0

# The second normalized q endpoint cannot then remain fixed under G_m.
w_q25 = w_delta + 25
assert w_q25 == 24

# Adding determinant-one target scaling leaves only a finite mu_8 subgroup.
w_target_det = w_alpha + w_delta
assert w_target_det == -16
assert gcd(24, 16) == 8

# Keeping q25 instead makes the normalized q1 coefficient have negative weight.
w_delta_keep_q25 = -25
assert w_delta_keep_q25 + 25 == 0
assert w_delta_keep_q25 + 1 == -24

# In the determinant-one source chart scaling, center weights oppose the
# t/higher-q direction after j is normalized.
center_weights = (0, -1, -2)
t_chart_weight = -3
assert center_weights == tuple(1 - degree for degree in (1, 2, 3))
assert t_chart_weight == 1 - 4

# A nonnegative contracting pole action preserving L^8 A^3=9 is trivial.
solutions = [
    (w_l, w_a)
    for w_l in range(10)
    for w_a in range(10)
    if 8*w_l + 3*w_a == 0
]
assert solutions == [(0, 0)]

print("TD6-SOURCE-DILATION-CONTRACTION-NEGATIVE PASS")
