#!/usr/bin/env python3
"""Exact AWS-oriented compiler for next carry degrees 12 and 11.

Consumes the frozen first-following-Cartier gate.  It enumerates its exact
1,085,103 visible current-digit solutions, imposes N_12={C7,D7}_12, and
solves N_11={C7,D6}+{C6,D7} linearly in the six derivative-zero degree-six
spectators.  It intentionally does not descend to degrees 10 or below.
"""
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
PARENT = (ROOT / "cases/as_fonly_d7_vertical_next_cartier_20260824"
          / "compile_next_cartier.py")
with contextlib.redirect_stdout(io.StringIO()):
    gate = runpy.run_path(str(PARENT))

parent = gate["parent"]
ns = gate["ns"]
unknowns = gate["unknowns"]
structural = gate["structural"]
frob = gate["frob"]
matrix = gate["matrix"]
rhs = gate["rhs"]

eadd = ns["eadd"]
emul = ns["emul"]
escale = ns["escale"]
esubstitute = ns["esubstitute"]
coefficient = ns["coefficient"]
eval_expr = ns["eval_expr"]
var = ns["var"]
padd = ns["padd"]
pmul = ns["pmul"]
pscale = ns["pscale"]
derivative = ns["derivative"]

spectators = ("c6_0", "c6_3", "c6_6", "d6_0", "d6_3", "d6_6")


def transformed_coefficient(name):
    expression = var(name)
    expression = esubstitute(expression, ns["sub_digits"])
    expression = esubstitute(expression, ns["normal"])
    expression = esubstitute(expression, ns["pivot_sub"])
    expression = esubstitute(expression, ns["coord"])
    return expression


def homogeneous_from_names(prefix, degree):
    return {(i, degree-i): transformed_coefficient(f"{prefix}{degree}_{i}")
            for i in range(degree+1)}


def bracket(left, right):
    return padd(pmul(derivative(left, 0), derivative(right, 1)),
                pscale(-1, pmul(derivative(left, 1), derivative(right, 0))))


C7 = homogeneous_from_names("c", 7)
D7 = homogeneous_from_names("d", 7)
C6 = homogeneous_from_names("c", 6)
D6 = homogeneous_from_names("d", 6)
N12poly = bracket(C7, D7)
N11poly = padd(bracket(C7, D6), bracket(C6, D7))
N12 = [N12poly.get((i, 12-i), {}) for i in range(13)]
N11 = [N11poly.get((i, 11-i), {}) for i in range(12)]
N12 = [row for row in N12 if row]
N11 = [row for row in N11 if row]

# Exact support/type checks.  N12 is spectator-free; N11 is affine-linear in
# the six spectators.  Lower current digits and the next digit cannot reach
# degrees 12 or 11.
for row in N12:
    assert not any(set(monomial) & set(spectators) for monomial in row)
for row in N11:
    assert all(sum(name in spectators for name in monomial) <= 1
               for monomial in row)
assert (7-1)+(7-1) == 12
assert (7-1)+(6-1) == 11
assert (4-1)+(7-1) == 9  # first-digit/next-digit cross cap


def rref_source(A, F, b0):
    """RREF [A|F|b0], pivoting only in A; return pivots and rows."""
    work = [[x % 3 for x in a+f+[b]] for a, f, b in zip(A, F, b0)]
    pivots = []
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
        pivots.append(col)
        prow += 1
    return pivots, work


def affine_solutions(pivots, work, fvalues):
    """Yield all visible solutions for a compatible Frobenius value."""
    n = len(unknowns)
    free = [col for col in range(n) if col not in pivots]
    shifted = []
    for line in work:
        value = line[-1] + sum(a*b for a, b in
                               zip(line[n:-1], fvalues))
        shifted.append(value % 3)
    if any(shifted[i] for i in range(len(pivots), len(work))):
        return
    for free_values in itertools.product(range(3), repeat=len(free)):
        solution = [0] * n
        for col, value in zip(free, free_values):
            solution[col] = value
        for i, pivot in enumerate(pivots):
            value = shifted[i]
            value += sum(work[i][col] * solution[col] for col in free)
            solution[pivot] = (-value) % 3
        yield tuple(solution)


def rank_mod3(matrix_numeric):
    if not matrix_numeric:
        return 0
    work = [[x % 3 for x in row] for row in matrix_numeric]
    row = 0
    for col in range(len(work[0])):
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


def spectator_fiber(rows, assignment):
    A = [[eval_expr(coefficient(row, name), assignment)
          for name in spectators] for row in rows]
    zero = {name: {} for name in spectators}
    b = [eval_expr(esubstitute(row, zero), assignment) for row in rows]
    r = rank_mod3(A)
    raug = rank_mod3([line+[value] for line, value in zip(A, b)])
    return 0 if r != raug else 3 ** (len(spectators)-r), (r, raug)


visible_total = 0
n12_total = 0
n12_state_count = 0
n11_total = 0
n11_state_count = 0
n11_fiber_hist = Counter()
n11_rank_pairs = Counter()
n12_digest = hashlib.sha256()
n11_digest = hashlib.sha256()
structural_survivor_hist = Counter()

zero_frob = {name: {} for name in frob}
for svalues in itertools.product(range(3), repeat=len(structural)):
    sassign = dict(zip(structural, svalues))
    A = [[eval_expr(entry, sassign) for entry in row] for row in matrix]
    F = [[eval_expr(coefficient(affine, name), sassign)
          for name in frob] for affine in rhs]
    b0 = [eval_expr(esubstitute(affine, zero_frob), sassign) for affine in rhs]
    pivots, work = rref_source(A, F, b0)
    local_n12 = 0
    for fvalues in itertools.product(range(3), repeat=len(frob)):
        for xvalues in affine_solutions(pivots, work, fvalues):
            visible_total += 1
            assignment = dict(sassign)
            assignment.update(zip(frob, fvalues))
            assignment.update(zip(unknowns, xvalues))
            if any(eval_expr(row, assignment) for row in N12):
                continue
            n12_total += 1
            local_n12 += 1
            n12_state_count += 1
            n12_digest.update(bytes(svalues+fvalues+xvalues))
            count, pair = spectator_fiber(N11, assignment)
            n11_rank_pairs[pair] += 1
            n11_fiber_hist[count] += 1
            if count:
                n11_state_count += 1
                n11_total += count
                n11_digest.update(bytes(svalues+fvalues+xvalues))
                n11_digest.update(count.to_bytes(2, "little"))
    structural_survivor_hist[local_n12] += 1

assert visible_total == 1085103, visible_total
print("source_shapes", len(N12), len(N11), len(spectators))
print("visible_parent_total", visible_total)
print("N12_visible_survivors", n12_total)
print("N12_surviving_visible_states", n12_state_count)
print("N12_stream_sha256", n12_digest.hexdigest())
print("N12_structural_survivor_histogram", sorted(structural_survivor_hist.items()))
print("N11_visible_states_with_spectator_solution", n11_state_count)
print("N11_full_spectator_solutions", n11_total)
print("N11_spectator_fiber_histogram", sorted(n11_fiber_hist.items()))
print("N11_rank_pairs", sorted(n11_rank_pairs.items()))
print("N11_stream_sha256", n11_digest.hexdigest())
print("PASS-NEXT-TOP-CARRY-COMPILER")
