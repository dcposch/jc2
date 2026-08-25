#!/usr/bin/env python3
"""Exact affine compiler for the first following Cartier row."""
from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
import os
import runpy
from collections import Counter
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
PARENT = (ROOT / "cases/as_fonly_d7_vertical_full_c5_d7_gate_20260824"
          / "compile_full_c5_gate.py")
SOURCE = Path(__file__).with_name("audit_next_cartier_source.py")
with contextlib.redirect_stdout(io.StringIO()):
    parent = runpy.run_path(str(PARENT))
    source = runpy.run_path(str(SOURCE))

ns = parent["ns"]
coefficient = ns["coefficient"]
eval_expr = ns["eval_expr"]
rank = ns["matrix_rank_mod3"]
eadd = ns["eadd"]
emul = ns["emul"]
escale = ns["escale"]
var = ns["var"]
esubstitute = ns["esubstitute"]

unknowns = parent["unknowns"]
structural = parent["structural"]
frob = parent["frob"]
equations = parent["equations"] + [source["F22"]]
matrix = [[coefficient(equation, name) for name in unknowns]
          for equation in equations]
rhs = []
for equation, row in zip(equations, matrix):
    affine = equation
    for entry, name in zip(row, unknowns):
        affine = eadd(affine, escale(2, emul(entry, var(name))))
    rhs.append(affine)

rank_triples = Counter()
fiber_hist = Counter()
compatible_total = 0
digit_total = 0
literal_total = 0
literal_hist = Counter()
digest = hashlib.sha256()
empty = []
for values in itertools.product(range(3), repeat=len(structural)):
    assignment = dict(zip(structural, values))
    A = [[eval_expr(entry, assignment) for entry in row] for row in matrix]
    F = [[eval_expr(coefficient(affine, name), assignment)
          for name in frob] for affine in rhs]
    zero_frob = {name: {} for name in frob}
    b0 = [eval_expr(esubstitute(affine, zero_frob), assignment)
          for affine in rhs]
    AF = [a+f for a, f in zip(A, F)]
    r = rank(A)
    c = rank(AF)
    d = rank([row+[b] for row, b in zip(AF, b0)])
    rank_triples[(r, c, d)] += 1
    if c == d:
        fcount = 3 ** (len(frob)+r-c)
        compatible_total += fcount
        digit_total += 3 ** (len(frob)+len(unknowns)-c)
    else:
        fcount = 0
        empty.append(values)
    fiber_hist[fcount] += 1

    # Independent literal enumeration from the cokernel of A.
    work = [[x % 3 for x in a+f+[b]] for a, f, b in zip(A, F, b0)]
    prow = 0
    for col in range(len(unknowns)):
        pivot = next((i for i in range(prow, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[prow], work[pivot] = work[pivot], work[prow]
        if work[prow][col] == 2:
            work[prow] = [(2*x) % 3 for x in work[prow]]
        for i in range(len(work)):
            if i != prow and work[i][col]:
                scalar = work[i][col]
                work[i] = [(x-scalar*y) % 3
                           for x, y in zip(work[i], work[prow])]
        prow += 1
    assert prow == r
    here = 0
    for fvalues in itertools.product(range(3), repeat=len(frob)):
        ok = all((line[-1] + sum(a*b for a, b in
                                 zip(line[len(unknowns):-1], fvalues))) % 3 == 0
                 for line in work[r:])
        if ok:
            here += 1
            digest.update(bytes(values+fvalues))
    assert here == fcount
    literal_total += here
    literal_hist[here] += 1

print("shape", len(equations), len(unknowns))
print("new_cartier_row", ns["sexpr"](source["F22"]))
print("rank_triples", sorted(rank_triples.items()))
print("frob_fiber_histogram", sorted(fiber_hist.items()))
print("compatible_frob_total", compatible_total)
print("visible_current_digit_total", digit_total)
print("literal_compatible_frob_total", literal_total)
print("literal_frob_fiber_histogram", sorted(literal_hist.items()))
print("literal_compatible_stream_sha256", digest.hexdigest())
print("empty_structural_count", len(empty))
print("empty_structural_prefix", empty[:30])
print("PASS-NEXT-CARTIER-COMPILER")
