#!/usr/bin/env python3
"""Source-corrected N12/Q11/Q10 structural-base shard.

Consumes the frozen corrected-Q11 compiler definition prefix, attaches both
degree-ten divided-Frobenius summands, and enumerates one contiguous block
of structural bases exactly over F3.
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
PREVIOUS = (ROOT / "cases/as_fonly_d7_vertical_next_top_corrected_shards_20260825"
            / "compile_shard.py")
EXPECTED_PREVIOUS_SHA = "349ea50953ba6e92d2023ff60965e484eb06e85962bded09d3bfa9b1307dcc30"
source_bytes = PREVIOUS.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == EXPECTED_PREVIOUS_SHA
source = source_bytes.decode()
marker = "\nshard_count = int(os.environ.get(\"SHARD_COUNT\", \"27\"))\n"
assert source.count(marker) == 1
prefix = source.split(marker, 1)[0]
scope = {"__file__": str(PREVIOUS), "__name__": "__corrected_q11_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix, str(PREVIOUS), "exec"), scope)

top = scope["top"]
ns = scope["ns"]
structural = scope["structural"]
frob = scope["frob"]
unknowns = scope["unknowns"]
matrix = scope["matrix"]
rhs = scope["rhs"]
N12 = scope["N12"]
Q11 = scope["Q11"]
spectators = scope["spectators"]
eval_expr = scope["eval_expr"]
coefficient = scope["coefficient"]
esubstitute = scope["esubstitute"]
rref_source = scope["rref_source"]
affine_solutions = scope["affine_solutions"]
UFx3, UFy3 = scope["UFx3"], scope["UFy3"]
VFx3, VFy3 = scope["VFx3"], scope["VFy3"]

var = ns["var"]
eadd = ns["eadd"]
emul = ns["emul"]
escale = ns["escale"]
padd = ns["padd"]
pmul = ns["pmul"]
pscale = ns["pscale"]
derivative = ns["derivative"]

C7, D7 = top["C7"], top["D7"]
C6, D6 = top["C6"], top["D6"]
homogeneous_from_names = top["homogeneous_from_names"]
bracket = top["bracket"]
C5 = homogeneous_from_names("c", 5)
D5 = homogeneous_from_names("d", 5)

# The single-Frobenius term ({UF,D6}+{C6,VF})/3.  UFx3 etc. are
# exact integer derivatives divided by three and then reduced modulo three.
C6x, C6y = derivative(C6, 0), derivative(C6, 1)
D6x, D6y = derivative(D6, 0), derivative(D6, 1)
MF6q = padd(pmul(UFx3, D6y), pmul(C6x, VFy3),
            pscale(-1, pmul(UFy3, D6x)),
            pscale(-1, pmul(C6y, VFx3)))

# The double-Frobenius term {UF,VF}/9.  Both derivatives have already
# been divided by three, so this is their ordinary bracket over F3.
Kdoubleq = padd(pmul(UFx3, VFy3),
                pscale(-1, pmul(UFy3, VFx3)))
expected_kdouble = {
    (2, 8): eadd(escale(2, emul(var("fa"), var("fc"))),
                    emul(var("fua"), var("fd"))),
    (5, 5): eadd(emul(var("fb"), var("fc")),
                    escale(2, emul(var("fua"), var("fvb")))),
    (8, 2): eadd(escale(2, emul(var("fb"), var("fd"))),
                    emul(var("fa"), var("fvb"))),
}
assert Kdoubleq == expected_kdouble

N10poly = padd(bracket(C7, D5), bracket(C6, D6), bracket(C5, D7))
Q10poly = padd(N10poly, MF6q, Kdoubleq)
assert all(sum(xy) == 10 for xy in Q10poly)
Q10all = [Q10poly.get((i, 10-i), {}) for i in range(11)]
Q10 = [row for row in Q10all if row]
assert len(Q10) == 11

# The six current-digit homogeneous degree-six Frobenius coefficients have
# derivatives still divisible by three after the licensed quotient and are
# absent from Q10, just as from corrected Q11.
assert all(not any(set(monomial) & set(spectators) for monomial in row)
           for row in Q10)

shard_count = int(os.environ.get("SHARD_COUNT", "27"))
shard_index = int(os.environ["SHARD_INDEX"])
assert shard_count > 0 and 0 <= shard_index < shard_count
base_total = 3 ** len(structural)
start = base_total * shard_index // shard_count
stop = base_total * (shard_index + 1) // shard_count
assert 0 <= start < stop <= base_total

visible_total = 0
n12_total = 0
q11_total = 0
q10_total = 0
n12_digest = hashlib.sha256()
q11_digest = hashlib.sha256()
q10_digest = hashlib.sha256()
n12_base_hist = Counter()
q11_base_hist = Counter()
q10_base_hist = Counter()
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
    local_q10 = 0
    for fvalues in itertools.product(range(3), repeat=len(frob)):
        for xvalues in affine_solutions(pivots, work, fvalues):
            visible_total += 1
            assignment = dict(sassign)
            assignment.update(zip(frob, fvalues))
            assignment.update(zip(unknowns, xvalues))
            state = bytes(svalues + fvalues + xvalues)
            if any(eval_expr(row, assignment) for row in N12):
                continue
            n12_total += 1
            local_n12 += 1
            n12_digest.update(state)
            if any(eval_expr(row, assignment) for row in Q11):
                continue
            q11_total += 1
            local_q11 += 1
            q11_digest.update(state)
            q11_digest.update((729).to_bytes(2, "little"))
            if any(eval_expr(row, assignment) for row in Q10):
                continue
            q10_total += 1
            local_q10 += 1
            q10_digest.update(state)
            q10_digest.update((729).to_bytes(2, "little"))
    n12_base_hist[local_n12] += 1
    q11_base_hist[local_q11] += 1
    q10_base_hist[local_q10] += 1

print("shard_index", shard_index)
print("shard_count", shard_count)
print("shard_range", start, stop)
print("source_shapes", len(N12), len(Q11), len(Q10), len(spectators))
print("visible_parent_total", visible_total)
print("N12_visible_survivors", n12_total)
print("N12_stream_sha256", n12_digest.hexdigest())
print("N12_per_base_histogram", sorted(n12_base_hist.items()))
print("Q11_visible_states", q11_total)
print("Q11_full_spectator_solutions", 729 * q11_total)
print("Q11_stream_sha256", q11_digest.hexdigest())
print("Q11_per_base_histogram", sorted(q11_base_hist.items()))
print("Q10_visible_states", q10_total)
print("Q10_full_spectator_solutions", 729 * q10_total)
print("Q10_stream_sha256", q10_digest.hexdigest())
print("Q10_per_base_histogram", sorted(q10_base_hist.items()))
print("PASS-NEXT-TOP10-CARRY-CORRECTED-SHARD")

