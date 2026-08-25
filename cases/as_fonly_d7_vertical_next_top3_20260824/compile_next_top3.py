#!/usr/bin/env python3
"""AWS-only compiler appending the pure-N degree-ten row.

This consumes the source-frozen N12/N11 runner, checks its exact output state
internally, and re-enumerates the same visible predecessor solutions while
also imposing N10={C7,D5}+{C5,D7}.  Importing the predecessor intentionally
runs its full compiler, so this file must not be used as a lightweight local
audit.
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
TOP = (ROOT / "cases/as_fonly_d7_vertical_next_top_carry_20260824"
       / "compile_next_top_carry.py")
with contextlib.redirect_stdout(io.StringIO()):
    top = runpy.run_path(str(TOP))

gate = top["gate"]
ns = top["ns"]
structural = top["structural"]
frob = top["frob"]
unknowns = top["unknowns"]
matrix = top["matrix"]
rhs = top["rhs"]
N12 = top["N12"]
N11 = top["N11"]

eval_expr = top["eval_expr"]
coefficient = top["coefficient"]
esubstitute = ns["esubstitute"]
padd = ns["padd"]
bracket = top["bracket"]
homogeneous_from_names = top["homogeneous_from_names"]
rref_source = top["rref_source"]
affine_solutions = top["affine_solutions"]

# The source theorem says all degree-six self-brackets vanish in char 3.
# Build N10 directly from the degree-seven/degree-five cross terms.
C7 = top["C7"]
D7 = top["D7"]
C6 = top["C6"]
D6 = top["D6"]
C5 = homogeneous_from_names("c", 5)
D5 = homogeneous_from_names("d", 5)
assert bracket(C6, D6) == {}
N10poly = padd(bracket(C7, D5), bracket(C5, D7))
N10all = [N10poly.get((i, 10-i), {}) for i in range(11)]
N10 = [row for row in N10all if row]
assert [i for i, row in enumerate(N10all) if not row] == [2, 5, 8]
assert len(N10) == 8

# N11 cannot contain the six degree-six Frobenius spectators.  This turns
# the previous affine spectator check into an ordinary fixed row test.
spectators = top["spectators"]
assert all(not any(set(monomial) & set(spectators) for monomial in row)
           for row in N11)
assert set(top["n11_fiber_hist"]) <= {0, 729}
assert top["n11_total"] == 729 * top["n11_state_count"]

zero_frob = {name: {} for name in frob}
visible_total = 0
n12_visible = 0
n11_visible = 0
n10_visible = 0
n10_structural_states = set()
n10_frob_states = set()
n10_digest = hashlib.sha256()
n10_base_hist = Counter()

for svalues in itertools.product(range(3), repeat=len(structural)):
    sassign = dict(zip(structural, svalues))
    A = [[eval_expr(entry, sassign) for entry in row] for row in matrix]
    F = [[eval_expr(coefficient(affine, name), sassign)
          for name in frob] for affine in rhs]
    b0 = [eval_expr(esubstitute(affine, zero_frob), sassign) for affine in rhs]
    pivots, work = rref_source(A, F, b0)
    local_n10 = 0
    for fvalues in itertools.product(range(3), repeat=len(frob)):
        for xvalues in affine_solutions(pivots, work, fvalues):
            visible_total += 1
            assignment = dict(sassign)
            assignment.update(zip(frob, fvalues))
            assignment.update(zip(unknowns, xvalues))
            if any(eval_expr(row, assignment) for row in N12):
                continue
            n12_visible += 1
            if any(eval_expr(row, assignment) for row in N11):
                continue
            n11_visible += 1
            if any(eval_expr(row, assignment) for row in N10):
                continue
            n10_visible += 1
            local_n10 += 1
            n10_structural_states.add(svalues)
            n10_frob_states.add(svalues + fvalues)
            n10_digest.update(bytes(svalues + fvalues + xvalues))
    n10_base_hist[local_n10] += 1

assert visible_total == 1085103
assert n12_visible == top["n12_total"]
assert n11_visible == top["n11_state_count"]

print("parent_visible_total", visible_total)
print("reproduced_N12_visible", n12_visible)
print("reproduced_N11_visible", n11_visible)
print("N10_source_shape", len(N10))
print("N10_visible_survivors", n10_visible)
print("N10_structural_base_count", len(n10_structural_states))
print("N10_structural_frobenius_count", len(n10_frob_states))
print("N10_per_base_histogram", sorted(n10_base_hist.items()))
print("N10_stream_sha256", n10_digest.hexdigest())
print("PASS-NEXT-TOP3-COMPILER")
