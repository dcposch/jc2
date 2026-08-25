#!/usr/bin/env python3
"""Exact finite compiler for B_(2,3)(D,D), D in {2,3}."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import z3


D = int(os.environ["CAP_D"])
assert D in (2, 3)
MODULUS = 8
WIDTH = 32
BV_MOD = z3.BitVecVal(MODULUS, WIDTH)


def bv(value):
    if isinstance(value, int):
        return z3.BitVecVal(value % MODULUS, WIDTH)
    assert z3.is_bv(value) and value.size() == WIDTH
    return value


def red(value):
    return z3.URem(bv(value), BV_MOD)


def add(*values):
    result = bv(0)
    for value in values:
        result = red(result + bv(value))
    return result


def scale(scalar, value):
    return red(bv(scalar) * bv(value))


def mul(left, right):
    return red(bv(left) * bv(right))


def padd(*polys):
    support = set().union(*(poly.keys() for poly in polys))
    return {xy: add(*(poly.get(xy, bv(0)) for poly in polys))
            for xy in support}


def pscale(scalar, poly):
    return {xy: scale(scalar, value) for xy, value in poly.items()}


def pmul(left, right):
    result = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            xy = (i + k, j + ell)
            result[xy] = add(result.get(xy, bv(0)), mul(a, b))
    return result


def derivative(poly, axis):
    result = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            result[xy] = scale(exponent, value)
    return result


def determinant(left, right):
    return padd(pmul(derivative(left, 0), derivative(right, 1)),
                 pscale(-1, pmul(derivative(left, 1),
                                 derivative(right, 0))))


monomials = [(i, total - i) for total in range(D + 1)
             for i in range(total + 1)]
solver = z3.Solver()
solver.set(timeout=int(os.environ.get("SOLVER_TIMEOUT_MS", "1")))
avars = {xy: z3.BitVec(f"A_{xy[0]}_{xy[1]}", WIDTH) for xy in monomials}
bvars = {xy: z3.BitVec(f"B_{xy[0]}_{xy[1]}", WIDTH) for xy in monomials}
for xy, variable in avars.items():
    solver.add(z3.ULT(variable, z3.BitVecVal(8, WIDTH)))
    residue = 1 if xy == (1, 0) else 0
    solver.add(z3.URem(variable, bv(2)) == bv(residue))
for xy, variable in bvars.items():
    solver.add(z3.ULT(variable, z3.BitVecVal(8, WIDTH)))
    residue = 1 if xy == (0, 1) else 0
    solver.add(z3.URem(variable, bv(2)) == bv(residue))

A = dict(avars)
B = dict(bvars)
A2 = pmul(A, A)
P = padd(A, pscale(-1, A2))
S3A = padd({(0, 0): bv(1)}, pscale(2, A), pscale(4, A2))
Q = pmul(B, S3A)

equation_counts = {"gauge_det": 0, "map_det": 0, "map_overcap": 0}
for family, det in (("gauge_det", determinant(A, B)),
                    ("map_det", determinant(P, Q))):
    max_degree = max((sum(xy) for xy in det), default=0)
    for total in range(max_degree + 1):
        for i in range(total + 1):
            target = 1 if (i, total - i) == (0, 0) else 0
            solver.add(red(det.get((i, total - i), bv(0))) == bv(target))
            equation_counts[family] += 1

for poly in (P, Q):
    for xy, value in poly.items():
        if sum(xy) > D:
            solver.add(red(value) == bv(0))
            equation_counts["map_overcap"] += 1

smt2 = solver.to_smt2().encode()
Path(os.environ["SMT2_OUTPUT"]).write_bytes(smt2)
check = solver.check()
result = {
    "status": str(check),
    "prime": 2,
    "depth": 3,
    "modulus": MODULUS,
    "cap": D,
    "monomial_slots_per_coordinate": len(monomials),
    "raw_coefficient_count": 2 * len(monomials),
    "raw_binary_digit_upper_bound": 4 * len(monomials),
    "equation_counts": equation_counts,
    "smt2_sha256": hashlib.sha256(smt2).hexdigest(),
    "solver_version": z3.get_version_string(),
    "solver_timeout_ms": int(os.environ.get("SOLVER_TIMEOUT_MS", "1")),
    "unsat_without_checked_proof_is_theorem": False,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("status", check)
print("cap", D)
print("slots", len(monomials), 2 * len(monomials))
print("equation_counts", equation_counts)
print("smt2_sha256", result["smt2_sha256"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-P2-DEPTH3-EMITTER")
