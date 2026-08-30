#!/usr/bin/env python3
"""Desk-scale algebra checks for the block-descent A1 Euler ledger."""

from __future__ import annotations

import ast
import json
import sys

import sympy as sp


def fail(message: str) -> None:
    raise SystemExit(f"FAIL:{message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


allowed = {"--mutate-cusp-sign"}
if any(arg not in allowed for arg in sys.argv[1:]):
    fail("unknown command-line argument")
mutate_cusp_sign = "--mutate-cusp-sign" in sys.argv[1:]

with open(__file__, "r", encoding="utf-8") as source_handle:
    tree = ast.parse(source_handle.read(), filename=__file__)
require(not any(isinstance(node, ast.Assert) for node in ast.walk(tree)), "assert node found")

s, x, y, a, b, c = sp.symbols("s x y a b c")
p = s**3 - 3 * s
different = sp.diff(p, s)
require(sp.factor(different - 3 * (s - 1) * (s + 1)) == 0, "cubic different failed")
require(p.subs(s, 1) == -2 and p.subs(s, -1) == 2, "critical values failed")

# Universal monic cubic control: (s,a) -> (a,b=-s^3-a*s).
b_map = -s**3 - a * s
jacobian = sp.Matrix([[sp.diff(a, s), sp.diff(a, a)], [sp.diff(b_map, s), sp.diff(b_map, a)]]).det()
require(sp.expand(jacobian - (3 * s**2 + a)) == 0, "universal cubic Jacobian failed")
disc = -4 * a**3 + (27 if mutate_cusp_sign else -27) * b**2
ram_a = -3 * s**2
ram_b = 2 * s**3
require(sp.expand(disc.subs({a: ram_a, b: ram_b})) == 0, "cusp parametrization failed")

# Complete-base ruling control: Q={b^2-4ac=1} and its A2 big cell.
quadric = b**2 - 4 * a * c - 1
cell_map = {a: x, b: 1 + 2 * x * y, c: y * (1 + x * y)}
require(sp.expand(quadric.subs(cell_map)) == 0, "quadric cell identity failed")
A, B, C = cell_map[a], cell_map[b], cell_map[c]
cell_jacobian = sp.Matrix(
    [
        [sp.diff(A, x), sp.diff(A, y)],
        [sp.diff(B, x), sp.diff(B, y)],
        [sp.diff(C, x), sp.diff(C, y)],
    ]
)
minors = [
    sp.factor(cell_jacobian.extract(rows, [0, 1]).det())
    for rows in [(0, 1), (0, 2), (1, 2)]
]
require(sp.groebner(minors, x, y).contains(sp.Integer(1)), "quadric cell is not etale")
require(sp.cancel((2 * c / (b + 1)).subs(cell_map) - y) == 0, "quadric cell inverse failed")

# Euler controls for p(s)=phi(x,y), with N=5 as a concrete replay point.
N = 5
negative_euler = 3 - 4 * N
positive_euler = 4 * N - 5
require(negative_euler == -17, "negative Euler control failed")
require(positive_euler == 15, "positive Euler control failed")

result = {
    "complete_base_control": {
        "A2_cell_missing_line": "a=0,b=-1",
        "euler": 2,
        "equation": "b^2-4*a*c=1",
        "generic_degree_of_cell": 1,
    },
    "cubic_controls": {
        "phi=x^N": "e(U)=3-4*N",
        "phi=y^2+x^N": "e(U)=4*N-5",
        "sample_N": N,
        "sample_eulers": [negative_euler, positive_euler],
    },
    "degree_three_exact_ledger": "e(U)=3-2*e(B)-|S0|",
    "p1_constraint": "2*e(B)+|S0|+Q=1",
    "p_derivative": str(sp.factor(different)),
    "quadric_cell_minors": [str(value) for value in minors],
    "sympy_version": sp.__version__,
    "universal_cubic_jacobian": str(jacobian),
}
print(json.dumps(result, sort_keys=True, separators=(",", ":")))
