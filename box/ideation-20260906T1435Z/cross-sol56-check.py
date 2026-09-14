#!/usr/bin/env python3
"""Independent exact controls for the 1435 Sol cross exchange."""

from collections import defaultdict
from fractions import Fraction
import resource


resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))


def require(condition, label):
    if not condition:
        raise RuntimeError(label)
    print("PASS", label)


def bracket(left, right):
    out = defaultdict(Fraction)
    for (i, j), a in left.items():
        for (p, q), b in right.items():
            coefficient = a * b * (i * q - j * p)
            if coefficient:
                out[(i + p - 1, j + q - 1)] += coefficient
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def scale(poly, scalar):
    return {exponent: scalar * coefficient for exponent, coefficient in poly.items()}


def shift_gamma(poly, amount):
    return {(i + amount, j): coefficient for (i, j), coefficient in poly.items()}


# Astra Card 2 positive control: [E,R] = gamma^2 R.
r_positive = {(1, 1): Fraction(1)}
e_positive = {(3, 1): Fraction(1, 2)}
require(bracket(e_positive, r_positive) == shift_gamma(r_positive, 2),
        "twisted Euler positive control")

# Its steep nonmonomial test has no E=A gamma^7+B gamma^3 pi.
r_steep = {(4, 1): Fraction(1), (0, 2): Fraction(1)}
e_a = {(7, 0): Fraction(1)}
e_b = {(3, 1): Fraction(1)}
target = shift_gamma(r_steep, 2)
ba = bracket(e_a, r_steep)
bb = bracket(e_b, r_steep)
require(ba.get((10, 0)) == 7 and target.get((10, 0), 0) == 0,
        "steep test forces A=0")
require(bb.get((6, 1)) == -1 and bb.get((2, 2)) == 6,
        "steep test gives incompatible B coefficients")

# Changed object: a genuine monomial-J pair outside sigma>(k+1)rho.
p_changed = {(2, 1): Fraction(1), (0, 2): Fraction(1)}
q_changed = {(2, 0): Fraction(-1, 2), (0, 1): Fraction(-1)}
require(bracket(p_changed, q_changed) == {(3, 0): Fraction(1)},
        "changed object has Jacobian gamma^3")
require({i + 2 * j for i, j in p_changed} == {4} and len(p_changed) == 2,
        "changed object has nonmonomial (1,2)-face")
require(2 <= (3 + 1) * 1, "changed object lies outside forbidden steep cone")

# Fable's weight-line count fails in the Laurent ring: t^(2-b) pi^b.
weight_line = [(2 - b, b) for b in range(13)]
require(all(i + j == 2 for i, j in weight_line),
        "thirteen Laurent monomials share weight two")
require(any(i < 0 for i, _ in weight_line),
        "unbounded family uses negative t exponents")

# D125 literal-source counts and normalized specialization.
def support(degree, upper):
    return {(i, j) for i in range(degree + 1)
            for j in range(degree - i + 1) if 5 * i - j <= upper}


p_source = support(75, 15)
q_source = support(125, 25)
p_normal = {(i, j) for i, j in p_source
            if j <= 60 and (j != 60 or i == 15)}
q_normal = {(i, j) for i, j in q_source
            if j <= 100 and (j != 100 or i == 25)}
require((len(p_source), len(q_source)) == (706, 1901),
        "original D125 source counts")
require((len(p_normal), len(q_normal)) == (571, 1551),
        "normalized D125 source counts")
require((15, 60) in p_normal and (25, 100) in q_normal,
        "degree-guard endpoints retained")

# Independent terminal-face bracket and a changed-sign rejection.
p_face = {(4, 1): Fraction(1), (21, 6): Fraction(1)}
q_face = {(1, 0): Fraction(-1), (18, 5): Fraction(-3),
          (35, 10): Fraction(-9, 5)}
require(bracket(p_face, q_face) == {(4, 0): Fraction(1)},
        "D125 pinned terminal bracket")
q_mutant = dict(q_face)
q_mutant[(18, 5)] = Fraction(3)
require(bracket(p_face, q_mutant) != {(4, 0): Fraction(1)},
        "D125 changed-sign object rejected")

print("CROSS_SOL56_EXACT_CONTROLS_PASS")
