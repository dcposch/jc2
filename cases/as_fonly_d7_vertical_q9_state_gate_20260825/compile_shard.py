#!/usr/bin/env python3
"""Exact source-state gate from corrected Q10 to total degree nine.

For each corrected-Q10 visible survivor this reconstructs canonical integer
digits, proves the needed coefficientwise divisions, and solves the affine
system in the previously suppressed C2/D2, C4/D4, and W7/Z7 layers.
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
PREVIOUS = (ROOT / "cases/as_fonly_d7_vertical_next_top10_corrected_shards_20260825"
            / "compile_shard.py")
EXPECTED_PREVIOUS_SHA = "3837508e6f0ffabbcdecfdc19a9ade1e4068bbece6aba80cfdc6b9937e25a686"
source_bytes = PREVIOUS.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == EXPECTED_PREVIOUS_SHA
source = source_bytes.decode()
marker = "\nshard_count = int(os.environ.get(\"SHARD_COUNT\", \"27\"))\n"
assert source.count(marker) == 1
prefix = source.split(marker, 1)[0]
scope = {"__file__": str(PREVIOUS), "__name__": "__corrected_q10_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix, str(PREVIOUS), "exec"), scope)

top = scope["top"]
structural = scope["structural"]
frob = scope["frob"]
unknowns = scope["unknowns"]
matrix = scope["matrix"]
rhs = scope["rhs"]
N12, Q11, Q10 = scope["N12"], scope["Q11"], scope["Q10"]
spectators = scope["spectators"]
eval_expr = scope["eval_expr"]
coefficient = scope["coefficient"]
esubstitute = scope["esubstitute"]
rref_source = scope["rref_source"]
affine_solutions = scope["affine_solutions"]
transformed_coefficient = top["transformed_coefficient"]


# Numeric bivariate polynomials over Z until an explicit reduction.
def nadd(*polys):
    out = {}
    for poly in polys:
        for xy, value in poly.items():
            value2 = out.get(xy, 0) + value
            if value2:
                out[xy] = value2
            else:
                out.pop(xy, None)
    return out


def nscale(scalar, poly):
    return {xy: scalar * value for xy, value in poly.items()
            if scalar * value}


def nmul(left, right):
    out = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            xy = (i + k, j + ell)
            out[xy] = out.get(xy, 0) + a * b
    return {xy: value for xy, value in out.items() if value}


def nderivative(poly, axis):
    out = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            out[xy] = exponent * value
    return out


def nbracket(left, right):
    return nadd(nmul(nderivative(left, 0), nderivative(right, 1)),
                nscale(-1, nmul(nderivative(left, 1),
                                nderivative(right, 0))))


def degree_part(poly, total):
    return {xy: value for xy, value in poly.items()
            if sum(xy) == total and value}


def divide_exact(poly, divisor):
    assert all(value % divisor == 0 for value in poly.values())
    return {xy: value // divisor for xy, value in poly.items()
            if value // divisor}


def mod3(poly):
    return {xy: value % 3 for xy, value in poly.items() if value % 3}


def homogeneous_numeric(degree, values):
    assert len(values) == degree + 1
    return {(i, degree - i): value for i, value in enumerate(values) if value}


def row(poly, total):
    return [poly.get((i, total - i), 0) % 3 for i in range(total + 1)]


def recorded_homogeneous(prefix_name, degree, assignment):
    values = [eval_expr(transformed_coefficient(
        f"{prefix_name}{degree}_{i}"), assignment) for i in range(degree + 1)]
    return homogeneous_numeric(degree, values)


new_names = (
    tuple(f"c2_{i}" for i in range(3)) + tuple(f"d2_{i}" for i in range(3))
    + tuple(f"c4_{i}" for i in range(5)) + tuple(f"d4_{i}" for i in range(5))
    + tuple(f"w7_{i}" for i in range(8)) + tuple(f"z7_{i}" for i in range(8))
)
assert len(new_names) == 32


def canonical_source(assignment):
    """Reconstruct the charged vertical integer digits from one F3 state."""
    h, s, w = (assignment[name] % 3 for name in ("h", "s", "w"))
    Rr, Tt = (assignment[name] % 3 for name in ("Rr", "Tt"))
    Pp, Qq = (assignment[name] % 3 for name in ("Pp", "Qq"))
    r = (Rr + s * h) % 3
    t = (Tt + w * h) % 3
    p = (Pp + Rr * h + 2 * s * h * h) % 3
    q = (Qq + Tt * h + 2 * w * h * h) % 3
    U0 = {(2, 1): h, (0, 4): p, (1, 3): (2 * r) % 3,
          (3, 1): q, (4, 0): (2 * t) % 3}
    V0 = {(1, 2): (2 * h) % 3, (2, 1): 1, (0, 4): r,
          (1, 3): s, (3, 1): t, (4, 0): w}
    UF = {(0, 6): assignment["fua"] % 3,
          (3, 3): assignment["fa"] % 3,
          (6, 0): assignment["fb"] % 3}
    VF = {(0, 6): assignment["fc"] % 3,
          (3, 3): assignment["fd"] % 3,
          (6, 0): assignment["fvb"] % 3}
    U, V = nadd(U0, UF), nadd(V0, VF)

    complete = dict(assignment)
    complete.update({name: 0 for name in spectators})
    Cbase = nadd(*(recorded_homogeneous("c", degree, complete)
                   for degree in (5, 6, 7)))
    Dbase = nadd(*(recorded_homogeneous("d", degree, complete)
                   for degree in (5, 6, 7)))

    ux, uy = nderivative(U, 0), nderivative(U, 1)
    vx, vy = nderivative(V, 0), nderivative(V, 1)
    A = nadd(ux, {(2, 0): -1})
    L = nadd(A, vy)
    L1 = divide_exact(L, 3)
    K = nadd(nmul(A, vy), nscale(-1, nmul(uy, vx)))
    Ebase = nadd(L1, K, nderivative(Cbase, 0),
                 nderivative(Dbase, 1))
    E6 = degree_part(Ebase, 6)
    E1_6 = divide_exact(E6, 3)

    cx, cy = nderivative(Cbase, 0), nderivative(Cbase, 1)
    dx, dy = nderivative(Dbase, 0), nderivative(Dbase, 1)
    Mbase = nadd(nmul(A, dy), nmul(cx, vy),
                 nscale(-1, nmul(uy, dx)),
                 nscale(-1, nmul(cy, vx)))
    M9 = degree_part(Mbase, 9)
    F1_9 = divide_exact(M9, 3)

    # Source controls for the already accepted top three rows.  E has no
    # total-degree 9 or 11 part in this typed support.
    assert degree_part(Ebase, 9) == {}
    Nbase = nbracket(Cbase, Dbase)
    M11q = divide_exact(degree_part(Mbase, 11), 3)
    E10q = divide_exact(degree_part(Ebase, 10), 3)
    F10q = divide_exact(nadd(E10q, degree_part(Mbase, 10)), 3)
    assert mod3(degree_part(Nbase, 12)) == {}
    assert mod3(nadd(M11q, degree_part(Nbase, 11))) == {}
    assert mod3(nadd(F10q, degree_part(Nbase, 10))) == {}

    return {
        "U": U, "V": V, "A": A, "uy": uy, "vx": vx, "vy": vy,
        "L1": L1, "K": K, "Cbase": Cbase, "Dbase": Dbase,
        "E1_6": E1_6, "F1_9": F1_9,
    }


def new_polynomials(values):
    assignment = dict(zip(new_names, values))
    C2 = homogeneous_numeric(2, [assignment[f"c2_{i}"] for i in range(3)])
    D2 = homogeneous_numeric(2, [assignment[f"d2_{i}"] for i in range(3)])
    C4 = homogeneous_numeric(4, [assignment[f"c4_{i}"] for i in range(5)])
    D4 = homogeneous_numeric(4, [assignment[f"d4_{i}"] for i in range(5)])
    W7 = homogeneous_numeric(7, [assignment[f"w7_{i}"] for i in range(8)])
    Z7 = homogeneous_numeric(7, [assignment[f"z7_{i}"] for i in range(8)])
    return C2, D2, C4, D4, W7, Z7


def source_rows(source_data, values):
    C2, D2, C4, D4, W7, Z7 = new_polynomials(values)
    Cfull = nadd(source_data["Cbase"], C2, C4)
    Dfull = nadd(source_data["Dbase"], D2, D4)
    E = nadd(source_data["L1"], source_data["K"],
             nderivative(Cfull, 0), nderivative(Dfull, 1))

    cx, cy = nderivative(Cfull, 0), nderivative(Cfull, 1)
    dx, dy = nderivative(Dfull, 0), nderivative(Dfull, 1)
    M = nadd(nmul(source_data["A"], dy), nmul(cx, source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], dx)),
             nscale(-1, nmul(cy, source_data["vx"])))
    assert degree_part(M, 9) == degree_part(
        nscale(3, source_data["F1_9"]), 9)

    F6 = nadd(source_data["E1_6"], degree_part(M, 6),
              nderivative(W7, 0), nderivative(Z7, 1))
    N9 = degree_part(nbracket(Cfull, Dfull), 9)
    T = nadd(nmul(source_data["A"], nderivative(Z7, 1)),
             nmul(nderivative(W7, 0), source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], nderivative(Z7, 0))),
             nscale(-1, nmul(nderivative(W7, 1), source_data["vx"])))
    G9 = nadd(source_data["F1_9"], N9, degree_part(T, 9))
    return row(E, 1) + row(E, 3) + row(F6, 6) + row(G9, 9)


assert 2 + 4 + 7 + 10 == 23


def affine_rank_and_witness(source_data):
    zero = (0,) * len(new_names)
    b = source_rows(source_data, zero)
    columns = []
    for index in range(len(new_names)):
        basis = [0] * len(new_names)
        basis[index] = 1
        value = source_rows(source_data, tuple(basis))
        columns.append([(a - c) % 3 for a, c in zip(value, b)])
    A = [[columns[col][r] for col in range(len(new_names))]
         for r in range(len(b))]

    # Exhaustive symbolic-degree argument says the rows are affine.  The
    # all-ones identity is a deterministic nonlinear-term negative control.
    ones = (1,) * len(new_names)
    predicted = [(b[r] + sum(A[r])) % 3 for r in range(len(b))]
    assert source_rows(source_data, ones) == predicted

    work = [[entry % 3 for entry in row_entries] + [(-constant) % 3]
            for row_entries, constant in zip(A, b)]
    rank = 0
    pivots = []
    for col in range(len(new_names)):
        pivot = next((r for r in range(rank, len(work)) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        if work[rank][col] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
        for r in range(len(work)):
            if r != rank and work[r][col]:
                scalar = work[r][col]
                work[r] = [(x - scalar * y) % 3
                           for x, y in zip(work[r], work[rank])]
        pivots.append(col)
        rank += 1
    incompatible = any(all(value == 0 for value in line[:-1]) and line[-1]
                       for line in work)
    augmented_rank = rank + int(incompatible)
    if incompatible:
        return 0, (rank, augmented_rank), None
    witness = [0] * len(new_names)
    for r, pivot in enumerate(pivots):
        witness[pivot] = work[r][-1]
    witness = tuple(witness)
    assert source_rows(source_data, witness) == [0] * 23
    return 3 ** (len(new_names) - rank), (rank, augmented_rank), witness


shard_count = int(os.environ.get("SHARD_COUNT", "27"))
shard_index = int(os.environ["SHARD_INDEX"])
assert shard_count > 0 and 0 <= shard_index < shard_count
base_total = 3 ** len(structural)
start = base_total * shard_index // shard_count
stop = base_total * (shard_index + 1) // shard_count
assert 0 <= start < stop <= base_total

visible_total = n12_total = q11_total = q10_total = 0
q9_compatible_states = 0
q9_relevant_completion_total = 0
quotient_nonzero_states = 0
rank_pairs = Counter()
fiber_hist = Counter()
compatible_per_base = Counter()
completion_per_base = Counter()
digest = hashlib.sha256()
first_witness = None
zero_frob = {name: {} for name in frob}

for base_index, svalues in enumerate(
        itertools.product(range(3), repeat=len(structural))):
    if base_index < start:
        continue
    if base_index >= stop:
        break
    sassign = dict(zip(structural, svalues))
    Aparent = [[eval_expr(entry, sassign) for entry in row0] for row0 in matrix]
    Fparent = [[eval_expr(coefficient(affine, name), sassign)
                for name in frob] for affine in rhs]
    b0 = [eval_expr(esubstitute(affine, zero_frob), sassign) for affine in rhs]
    pivots, work = rref_source(Aparent, Fparent, b0)
    local_compatible = 0
    local_completions = 0
    for fvalues in itertools.product(range(3), repeat=len(frob)):
        for xvalues in affine_solutions(pivots, work, fvalues):
            visible_total += 1
            assignment = dict(sassign)
            assignment.update(zip(frob, fvalues))
            assignment.update(zip(unknowns, xvalues))
            if any(eval_expr(test, assignment) for test in N12):
                continue
            n12_total += 1
            if any(eval_expr(test, assignment) for test in Q11):
                continue
            q11_total += 1
            if any(eval_expr(test, assignment) for test in Q10):
                continue
            q10_total += 1
            source_data = canonical_source(assignment)
            if mod3(source_data["F1_9"]):
                quotient_nonzero_states += 1
            count, pair, witness = affine_rank_and_witness(source_data)
            rank_pairs[pair] += 1
            fiber_hist[count] += 1
            if not count:
                continue
            q9_compatible_states += 1
            q9_relevant_completion_total += count
            local_compatible += 1
            local_completions += count
            state = bytes(svalues + fvalues + xvalues)
            digest.update(state)
            digest.update(count.to_bytes(8, "little"))
            if first_witness is None:
                first_witness = (list(svalues + fvalues + xvalues),
                                 list(witness), count)
    compatible_per_base[local_compatible] += 1
    completion_per_base[local_completions] += 1

print("shard_index", shard_index)
print("shard_count", shard_count)
print("shard_range", start, stop)
print("source_shapes", len(N12), len(Q11), len(Q10), 23, 32)
print("visible_parent_total", visible_total)
print("N12_visible_survivors", n12_total)
print("Q11_visible_states", q11_total)
print("Q10_visible_states", q10_total)
print("Q10_states_with_nonzero_M9_quotient", quotient_nonzero_states)
print("Q9_compatible_predecessor_states", q9_compatible_states)
print("Q9_relevant_completion_total", q9_relevant_completion_total)
print("Q9_with_C6_spectator_factor", 729 * q9_relevant_completion_total)
print("Q9_rank_pairs", sorted(rank_pairs.items()))
print("Q9_relevant_fiber_histogram", sorted(fiber_hist.items()))
print("Q9_compatible_states_per_base", sorted(compatible_per_base.items()))
print("Q9_completion_total_per_base", sorted(completion_per_base.items()))
print("Q9_stream_sha256", digest.hexdigest())
print("Q9_first_witness", first_witness)
print("PASS-Q9-SOURCE-STATE-SHARD")
