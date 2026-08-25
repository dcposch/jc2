#!/usr/bin/env python3
"""Contiguous structural-base shard of the frozen N12/N11 compiler.

The script executes only the definition prefix of the frozen monolithic
runner, then enumerates a preregistered contiguous interval of the 3^7
structural bases.  Each shard is deterministic and independent.
"""
from __future__ import annotations

import ast
import contextlib
import hashlib
import io
import itertools
import os
from collections import Counter
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
TOP = (ROOT / "cases/as_fonly_d7_vertical_next_top_carry_20260824"
       / "compile_next_top_carry.py")
EXPECTED_TOP_SHA256 = "1fc18eeb80ad3ae3b8c498fe5548e9adda423df1df60237077e0df6ef5e30d44"
source_bytes = TOP.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == EXPECTED_TOP_SHA256
source = source_bytes.decode()
marker = "\nvisible_total = 0\n"
assert source.count(marker) == 1
prefix = source.split(marker, 1)[0]
top = {"__file__": str(TOP), "__name__": "__top_definition_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix, str(TOP), "exec"), top)

gate = top["gate"]
ns = top["ns"]
structural = top["structural"]
frob = top["frob"]
unknowns = top["unknowns"]
matrix = top["matrix"]
rhs = top["rhs"]
N12 = top["N12"]
N11 = top["N11"]
spectators = top["spectators"]
eval_expr = top["eval_expr"]
coefficient = top["coefficient"]
esubstitute = ns["esubstitute"]
rref_source = top["rref_source"]
affine_solutions = top["affine_solutions"]

# Source theorem: all six advertised degree-six directions are Frobenius and
# cannot occur at N11.  A violation is a hard source mismatch.
assert all(not any(set(monomial) & set(spectators) for monomial in row)
           for row in N11)

shard_count = int(os.environ.get("SHARD_COUNT", "27"))
shard_index = int(os.environ["SHARD_INDEX"])
assert shard_count > 0 and 0 <= shard_index < shard_count
base_total = 3 ** len(structural)
start = base_total * shard_index // shard_count
stop = base_total * (shard_index + 1) // shard_count
assert 0 <= start < stop <= base_total

visible_total = 0
n12_total = 0
n11_state_count = 0
n12_digest = hashlib.sha256()
n11_digest = hashlib.sha256()
n12_base_hist = Counter()
n11_base_hist = Counter()
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
    local_n11 = 0
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
            if any(eval_expr(row, assignment) for row in N11):
                continue
            n11_state_count += 1
            local_n11 += 1
            n11_digest.update(bytes(svalues + fvalues + xvalues))
            n11_digest.update((729).to_bytes(2, "little"))
    n12_base_hist[local_n12] += 1
    n11_base_hist[local_n11] += 1

print("shard_index", shard_index)
print("shard_count", shard_count)
print("shard_range", start, stop)
print("source_shapes", len(N12), len(N11), len(spectators))
print("visible_parent_total", visible_total)
print("N12_visible_survivors", n12_total)
print("N12_stream_sha256", n12_digest.hexdigest())
print("N12_per_base_histogram", sorted(n12_base_hist.items()))
print("N11_visible_states", n11_state_count)
print("N11_full_spectator_solutions", 729 * n11_state_count)
print("N11_stream_sha256", n11_digest.hexdigest())
print("N11_per_base_histogram", sorted(n11_base_hist.items()))
print("PASS-NEXT-TOP-CARRY-SHARD")
