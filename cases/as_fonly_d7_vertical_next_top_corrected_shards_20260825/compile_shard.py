#!/usr/bin/env python3
"""Corrected N12/Q11 structural-base shard.

Consumes the source-frozen predecessor definition prefix, adds the divided
single-Frobenius degree-eleven term, and enumerates one contiguous block of
structural bases exactly over F3.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
import os
from collections import Counter
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
OLD_SHARD = (ROOT / "cases/as_fonly_d7_vertical_next_top_shards_20260825"
             / "compile_shard.py")
EXPECTED_OLD_SHARD_SHA = "64bbd0e15d0e10296ca81867a390338e41814ca575729e98bf2bd315a33bf893"
source_bytes = OLD_SHARD.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == EXPECTED_OLD_SHARD_SHA
source = source_bytes.decode()
marker = "\nshard_count = int(os.environ.get(\"SHARD_COUNT\", \"27\"))\n"
assert source.count(marker) == 1
prefix = source.split(marker, 1)[0]
scope = {"__file__": str(OLD_SHARD), "__name__": "__old_shard_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix, str(OLD_SHARD), "exec"), scope)

top = scope["top"]
ns = scope["ns"]
structural = scope["structural"]
frob = scope["frob"]
unknowns = scope["unknowns"]
matrix = scope["matrix"]
rhs = scope["rhs"]
N12 = scope["N12"]
spectators = scope["spectators"]
eval_expr = scope["eval_expr"]
coefficient = scope["coefficient"]
esubstitute = scope["esubstitute"]
rref_source = scope["rref_source"]
affine_solutions = scope["affine_solutions"]

var = ns["var"]
escale = ns["escale"]
padd = ns["padd"]
pmul = ns["pmul"]
pscale = ns["pscale"]
derivative = ns["derivative"]

# Integer derivatives of the homogeneous degree-six Frobenius first digit,
# divided by 3 and then reduced modulo 3.
UFx3 = {(2, 3): var("fa"), (5, 0): escale(2, var("fb"))}
UFy3 = {(0, 5): escale(2, var("fua")), (3, 2): var("fa")}
VFx3 = {(2, 3): var("fd"), (5, 0): escale(2, var("fvb"))}
VFy3 = {(0, 5): escale(2, var("fc")), (3, 2): var("fd")}

C7, D7 = top["C7"], top["D7"]
C7x, C7y = derivative(C7, 0), derivative(C7, 1)
D7x, D7y = derivative(D7, 0), derivative(D7, 1)
MF7q = padd(pmul(UFx3, D7y), pmul(C7x, VFy3),
             pscale(-1, pmul(UFy3, D7x)),
             pscale(-1, pmul(C7y, VFx3)))
Q11poly = padd(top["N11poly"], MF7q)
Q11all = [Q11poly.get((i, 11-i), {}) for i in range(12)]
Q11 = [row for row in Q11all if row]
assert len(Q11) == 12
assert all(not any(set(monomial) & set(spectators) for monomial in row)
           for row in Q11)

shard_count = int(os.environ.get("SHARD_COUNT", "27"))
shard_index = int(os.environ["SHARD_INDEX"])
assert shard_count > 0 and 0 <= shard_index < shard_count
base_total = 3 ** len(structural)
start = base_total * shard_index // shard_count
stop = base_total * (shard_index + 1) // shard_count
assert 0 <= start < stop <= base_total

visible_total = 0
n12_total = 0
q11_state_count = 0
n12_digest = hashlib.sha256()
q11_digest = hashlib.sha256()
n12_base_hist = Counter()
q11_base_hist = Counter()
zero_frob = {name: {} for name in frob}

for base_index, svalues in enumerate(
        itertools.product(range(3), repeat=len(structural))):
    if base_index < start:
        continue
    if base_index >= stop:
        break
    sassign = dict(zip(structural, svalues))
    A = [[eval_expr(entry, sassign) for entry in row] for row in matrix]
    F = [[eval_expr(coefficient(affine, name), sassign)
          for name in frob] for affine in rhs]
    b0 = [eval_expr(esubstitute(affine, zero_frob), sassign) for affine in rhs]
    pivots, work = rref_source(A, F, b0)
    local_n12 = 0
    local_q11 = 0
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
            n12_digest.update(bytes(svalues + fvalues + xvalues))
            if any(eval_expr(row, assignment) for row in Q11):
                continue
            q11_state_count += 1
            local_q11 += 1
            q11_digest.update(bytes(svalues + fvalues + xvalues))
            q11_digest.update((729).to_bytes(2, "little"))
    n12_base_hist[local_n12] += 1
    q11_base_hist[local_q11] += 1

print("shard_index", shard_index)
print("shard_count", shard_count)
print("shard_range", start, stop)
print("source_shapes", len(N12), len(Q11), len(spectators))
print("visible_parent_total", visible_total)
print("N12_visible_survivors", n12_total)
print("N12_stream_sha256", n12_digest.hexdigest())
print("N12_per_base_histogram", sorted(n12_base_hist.items()))
print("Q11_visible_states", q11_state_count)
print("Q11_full_spectator_solutions", 729 * q11_state_count)
print("Q11_stream_sha256", q11_digest.hexdigest())
print("Q11_per_base_histogram", sorted(q11_base_hist.items()))
print("PASS-NEXT-TOP-CARRY-CORRECTED-SHARD")
