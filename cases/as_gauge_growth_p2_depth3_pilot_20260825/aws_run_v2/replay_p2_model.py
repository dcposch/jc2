#!/usr/bin/env python3
"""Independent integer/mod-8 replay for a Boolector B_(2,3)(D,D) model."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


D = int(os.environ["CAP_D"])
assert D in (2, 3)
model_path = Path(os.environ["MODEL_OUTPUT"])
values = {}
for line in model_path.read_text().splitlines():
    fields = line.split()
    if len(fields) == 2 and fields[0].startswith(("A_", "B_")):
        values[fields[0]] = int(fields[1])
monomials = [(i, total - i) for total in range(D + 1)
             for i in range(total + 1)]
expected = ({f"A_{i}_{j}" for i, j in monomials}
            | {f"B_{i}_{j}" for i, j in monomials})
assert set(values) == expected, (expected - set(values), set(values) - expected)
assert all(0 <= value < 8 for value in values.values())


def nadd(*polys):
    answer = {}
    for poly in polys:
        for xy, value in poly.items():
            answer[xy] = (answer.get(xy, 0) + value) % 8
    return {xy: value for xy, value in answer.items() if value}


def nscale(scalar, poly):
    return {xy: scalar * value % 8 for xy, value in poly.items()
            if scalar * value % 8}


def nmul(left, right):
    answer = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            xy = (i + k, j + ell)
            answer[xy] = (answer.get(xy, 0) + a * b) % 8
    return {xy: value for xy, value in answer.items() if value}


def derivative(poly, axis):
    answer = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            answer[xy] = exponent * value % 8
    return {xy: value for xy, value in answer.items() if value}


def det(left, right):
    return nadd(nmul(derivative(left, 0), derivative(right, 1)),
                nscale(-1, nmul(derivative(left, 1),
                                derivative(right, 0))))


A = {xy: values[f"A_{xy[0]}_{xy[1]}"] for xy in monomials
     if values[f"A_{xy[0]}_{xy[1]}"]}
B = {xy: values[f"B_{xy[0]}_{xy[1]}"] for xy in monomials
     if values[f"B_{xy[0]}_{xy[1]}"]}
assert all(value % 2 == (1 if xy == (1, 0) else 0)
           for xy, value in {slot: values[f"A_{slot[0]}_{slot[1]}"]
                             for slot in monomials}.items())
assert all(value % 2 == (1 if xy == (0, 1) else 0)
           for xy, value in {slot: values[f"B_{slot[0]}_{slot[1]}"]
                             for slot in monomials}.items())
A2 = nmul(A, A)
P = nadd(A, nscale(-1, A2))
Q = nmul(B, nadd({(0, 0): 1}, nscale(2, A), nscale(4, A2)))
expected_det = {(0, 0): 1}
assert det(A, B) == expected_det
assert det(P, Q) == expected_det
assert all(sum(xy) <= D for xy in P)
assert all(sum(xy) <= D for xy in Q)

result = {
    "status": "PASS-AS-P2-DEPTH3-DIRECT-REPLAY",
    "cap": D,
    "model_sha256": hashlib.sha256(model_path.read_bytes()).hexdigest(),
    "A": sorted(([i, j, value] for (i, j), value in A.items())),
    "B": sorted(([i, j, value] for (i, j), value in B.items())),
    "P": sorted(([i, j, value] for (i, j), value in P.items())),
    "Q": sorted(([i, j, value] for (i, j), value in Q.items())),
    "gauge_det": sorted(([i, j, value] for (i, j), value in det(A, B).items())),
    "map_det": sorted(([i, j, value] for (i, j), value in det(P, Q).items())),
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("A", result["A"])
print("B", result["B"])
print("P", result["P"])
print("Q", result["Q"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-P2-DEPTH3-DIRECT-REPLAY")

