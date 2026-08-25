#!/usr/bin/env python3
"""Exact corrected D7 joint-row reduction, F3 census, and controls.

This script consumes only the frozen corrected producer's displayed D8 core.
The separate ``audit_d7_source.py`` derives the eight D7 rows from the
literal integer Jacobian and proves the forced substitutions used here.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
import os
import runpy
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GEN = (ROOT / "cases" /
       "as_fonly_d7_postd10_d98_f3_corrected_20260824" /
       "generate_corrected.py")
os.environ["BRANCH"] = "vertical"
os.environ.pop("ENUMERATE", None)
os.environ.pop("STRUCTURAL", None)
with contextlib.redirect_stdout(io.StringIO()):
    NS = runpy.run_path(str(GEN))

eadd = NS["eadd"]
emul = NS["emul"]
escale = NS["escale"]
esubstitute = NS["esubstitute"]
coefficient = NS["coefficient"]
eval_expr = NS["eval_expr"]
rank = NS["matrix_rank_mod3"]
sexpr = NS["sexpr"]
var = NS["var"]


def prod(*items):
    out = {(): 1}
    for item in items:
        out = emul(out, item)
    return out


def power(item, exponent):
    return prod(*([item] * exponent))


V = var

# Rebuild the seven D8 core equations M*x+b.  The D7 integer-source rows
# force the substitutions below; X0,X1,X2 rename the three surviving source
# digits d7_1,d7_4,d7_7.
core_equations = []
for row, affine in zip(NS["core_matrix"], NS["core_rhs"]):
    equation = affine
    for entry, name in zip(row, NS["remaining_vars"]):
        equation = eadd(equation, emul(entry, V(name)))
    core_equations.append(equation)

forced = {
    "fua": {}, "fc": {}, "fd": {}, "Rr": {},
    "Tt": escale(2, eadd(V("fb"), prod(V("fvb"), V("h")))),
    "d6_1": prod(V("fa"), V("h")),
    "d6_4": prod(V("fb"), V("h")),
    "d7_1": V("X0"), "d7_4": V("X1"), "d7_7": V("X2"),
}
joint = [esubstitute(row, forced) for row in core_equations]

P, Q, s, w, h = map(V, ("Pp", "Qq", "s", "w", "h"))
fa, fb, fv = map(V, ("fa", "fb", "fvb"))
X0, X1, X2 = map(V, ("X0", "X1", "X2"))
h2, h3, h4 = power(h, 2), power(h, 3), power(h, 4)

predicted = [
    eadd(escale(2, prod(P, X0)), escale(2, prod(P, fa, s)),
         prod(h3, power(s, 3))),
    eadd(escale(2, prod(P, X1)), escale(2, prod(P, fa, w)),
         escale(2, prod(P, fb, s)), escale(2, prod(P, fv, h, s)),
         escale(2, prod(Q, X0)), escale(2, prod(Q, fa, s)),
         escale(2, prod(fv, h3, power(s, 2)))),
    eadd(escale(2, prod(P, X2)), prod(P, fb, fv),
         escale(2, prod(P, fb, w)), prod(P, power(fv, 2), h),
         escale(2, prod(P, fv, h, w)), escale(2, prod(Q, X1)),
         escale(2, prod(Q, fa, w)), escale(2, prod(Q, fb, s)),
         escale(2, prod(Q, fv, h, s)), prod(fa, power(fb, 2)),
         escale(2, prod(fa, fb, fv, h)), prod(fa, power(fv, 2), h2),
         prod(fv, h3, s, w)),
    eadd(escale(2, prod(Q, X2)), prod(Q, fb, fv),
         escale(2, prod(Q, fb, w)), prod(Q, power(fv, 2), h),
         escale(2, prod(Q, fv, h, w)),
         escale(2, prod(fv, h3, power(w, 2))), prod(h3, power(w, 3))),
    eadd(escale(2, prod(X0, h3)), prod(fa, h3, s)),
    eadd(escale(2, prod(X1, h3)), prod(fa, h3, w),
         escale(2, prod(fa, s)), prod(fb, h3, s), prod(fv, h4, s)),
    eadd(escale(2, prod(X2, h3)), escale(2, prod(fa, w)),
         escale(2, prod(fb, fv, h3)), prod(fb, h3, w),
         escale(2, prod(power(fv, 2), h4)), prod(fv, h4, w)),
]
assert joint == predicted, (joint, predicted)

XNAMES = ("X0", "X1", "X2")
matrix = [[coefficient(row, name) for name in XNAMES] for row in joint]
rhs = []
for row in joint:
    affine = row
    for name in XNAMES:
        affine = eadd(affine, escale(2, emul(coefficient(row, name), V(name))))
    rhs.append(affine)


def values_for(names, values):
    return dict(zip(names, values))


BASE = ("Pp", "Qq", "s", "w", "h", "fa", "fb", "fvb")
rank_pairs = Counter()
h_state_counts = Counter()
h_point_counts = Counter()
projection_counts = defaultdict(int)
state_count = point_count = 0
state_digest = hashlib.sha256()
point_digest = hashlib.sha256()

for base_values in itertools.product(range(3), repeat=len(BASE)):
    assignment = values_for(BASE, base_values)
    numeric = [[eval_expr(entry, assignment) for entry in row] for row in matrix]
    numeric_rhs = [eval_expr(entry, assignment) for entry in rhs]
    ra = rank(numeric)
    raug = rank([row + [b] for row, b in zip(numeric, numeric_rhs)])
    rank_pairs[(ra, raug)] += 1
    compatible = ra == raug
    state_digest.update(bytes(base_values + (ra, raug, int(compatible))))
    if compatible:
        solutions = 3 ** (3 - ra)
        state_count += 1
        point_count += solutions
        h_state_counts[base_values[4]] += 1
        h_point_counts[base_values[4]] += solutions
        projection_counts[base_values[:5]] += solutions

    # Independent literal evaluation of all X values, both as a count check
    # and as a deterministic full compatible-point stream.
    direct = 0
    for x_values in itertools.product(range(3), repeat=3):
        full = dict(assignment)
        full.update(values_for(XNAMES, x_values))
        if all(eval_expr(row, full) == 0 for row in joint):
            direct += 1
            point_digest.update(bytes(base_values + x_values))
    assert direct == (3 ** (3 - ra) if compatible else 0)

assert rank_pairs == Counter({(3, 4): 5160, (3, 3): 1158,
                             (0, 1): 156, (0, 0): 87})
assert state_count == 1245
assert point_count == 3507
assert h_state_counts == Counter({0: 831, 1: 207, 2: 207})
assert h_point_counts == Counter({0: 3093, 1: 207, 2: 207})
projection_histogram = Counter(
    projection_counts.get(key, 0)
    for key in itertools.product(range(3), repeat=5)
)
assert projection_histogram == Counter({
    0: 60, 1: 44, 2: 4, 3: 24, 5: 8, 7: 4,
    9: 64, 11: 12, 15: 10, 27: 4, 243: 8, 405: 1,
})

# At h=0 and zero X-map (P=Q=0), compatibility is exactly
# fa=0 OR (fb=s=w=0).  The two pieces have 81 and 6 points, with no overlap
# after the second piece is restricted to fa!=0, totaling 87.
hzero_rank0 = []
for values in itertools.product(range(3), repeat=7):
    names = ("Pp", "Qq", "s", "w", "fa", "fb", "fvb")
    a = values_for(names, values)
    a["h"] = 0
    numeric = [[eval_expr(entry, a) for entry in row] for row in matrix]
    numeric_rhs = [eval_expr(entry, a) for entry in rhs]
    if rank(numeric) == 0 and rank([row + [b] for row, b in
                                            zip(numeric, numeric_rhs)]) == 0:
        hzero_rank0.append(values)
        P0, Q0, s0, w0, fa0, fb0, fv0 = values
        assert P0 == Q0 == 0
        assert fa0 == 0 or (fb0 == s0 == w0 == 0)
assert len(hzero_rank0) == 87

# Old corrected-D8 representative controls.  The current D7 source row
# accepts the 3-, 9-, and 729-fibre representatives; it rejects the chosen
# 81-fibre representative before the joint equations because T+fb+fv*h=1.
controls = {
    3: ((0, 0, 0, 1, 1, 0, 0), (0, 0, 2, 0, 0, 0), (0, 0, 0)),
    9: ((0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0)),
    81: ((0, 0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 0, 1), (0, 0, 2)),
    729: ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0)),
}
control_status = {}
for fibre, (base, frob, xvals) in controls.items():
    P0, Q0, R0, T0, s0, w0, h0 = base
    fua0, fa0, fb0, fc0, fd0, fv0 = frob
    source_rows = (
        2*fua0*h0,
        fc0*h0 + 2*fua0,
        fc0,
        0 + 2*fa0*h0,  # these representatives have d6_1=0
        R0 + fd0*h0,
        2*fd0,
        0 + 2*fb0*h0,  # these representatives have d6_4=0
        T0 + fb0 + fv0*h0,
    )
    source_ok = all(value % 3 == 0 for value in source_rows)
    joint_ok = None
    if source_ok:
        assignment = values_for(BASE, (P0, Q0, s0, w0, h0,
                                       fa0, fb0, fv0))
        assignment.update(values_for(XNAMES, xvals))
        joint_ok = all(eval_expr(row, assignment) == 0 for row in joint)
        assert joint_ok
    control_status[fibre] = (source_ok, joint_ok, tuple(x % 3 for x in source_rows))
assert control_status[3][:2] == (True, True)
assert control_status[9][:2] == (True, True)
assert control_status[81][0] is False
assert control_status[81][2][-1] == 1
assert control_status[729][:2] == (True, True)

print("joint_row_count", len(joint))
for i, row in enumerate(joint):
    print(f"joint_e{i}", sexpr(row))
print("rank_pairs", sorted(rank_pairs.items()))
print("compatible_states", state_count)
print("compatible_digit_points", point_count)
print("h_state_counts", sorted(h_state_counts.items()))
print("h_point_counts", sorted(h_point_counts.items()))
print("projection_histogram", sorted(projection_histogram.items()))
print("hzero_rank0_union_count", len(hzero_rank0))
print("state_stream_sha256", state_digest.hexdigest())
print("point_stream_sha256", point_digest.hexdigest())
for fibre in sorted(control_status):
    print("control", fibre, control_status[fibre])
print("PASS-D7-JOINT-CENSUS-CONTROLS")
