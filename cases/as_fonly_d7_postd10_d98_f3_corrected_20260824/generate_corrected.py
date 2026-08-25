#!/usr/bin/env python3
"""Emit exact degree-nine/eight rows on the vertical D10 branch."""
from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
import os
import runpy
from pathlib import Path

EXPECTED_ENUM = {
    "VERTICAL-D98": {
        "total": 1594323,
        "compatible": 314127,
        "rank_pairs": {
            (0, 0): 873, (0, 1): 11520,
            (2, 2): 1404, (2, 3): 45252,
            (3, 3): 6642, (3, 4): 41472,
            (5, 5): 305208, (5, 6): 1181952,
        },
        "fiber_histogram": {0: 12, 3: 36, 9: 16, 81: 1904, 729: 219},
        "sha256": "e86fd1ec2724b5089039378c07e1a19a089042eeb4172b0342474f85d4d8b23d",
    },
    "G-ENDPOINT-D98": {
        "total": 354294,
        "compatible": 918,
        "rank_pairs": {
            (5, 5): 270, (5, 6): 117828, (6, 7): 26244,
            (8, 8): 648, (8, 9): 209304,
        },
        "fiber_histogram": {0: 360, 3: 36, 9: 90},
        "sha256": "ce421ac61d73307c3d0bd553af9e23df7f040f6e7b3e85b4d7da06f220935b67",
    },
}

EXPECTED_STRUCTURAL = {
    "VERTICAL-D98": {
        "total": 2187,
        "compatible": 314127,
        "histogram": {0: 12, 3: 36, 9: 16, 81: 1904, 729: 219},
        "rank_triples": {
            (0, 0, 0): 1, (0, 4, 4): 16, (2, 4, 4): 16,
            (2, 6, 7): 12, (2, 7, 7): 36, (3, 3, 3): 2,
            (3, 5, 5): 64, (5, 5, 5): 216, (5, 7, 7): 1824,
        },
        "zero_count": 12,
        "zero_sha256": "5b66a63af070eff410c1824a6e6f4e73fc254da13eb5445dcb9bdae4c2ece701",
    },
    "G-ENDPOINT-D98": {
        "total": 486,
        "compatible": 918,
        "histogram": {0: 360, 3: 36, 9: 90},
        "rank_triples": {
            (5, 9, 9): 18, (5, 10, 10): 36, (5, 10, 11): 108,
            (6, 10, 11): 36, (8, 12, 12): 72, (8, 12, 13): 216,
        },
        "zero_count": 360,
        "zero_sha256": "2fdb6b61e6a98e9e4b39ce8459f62774cf6dacd161b04c6752e044e87e963b2e",
    },
}

ROOT = Path(__file__).resolve().parents[2]
source = str(ROOT / "cases" / "as_fonly_d7_degree10_pointwise_20260824"
             / "generate_degree10_gate.py")
os.environ["MATRIX"] = "1"
BRANCH = os.environ.get("BRANCH", "vertical")
assert BRANCH in ("vertical", "g")
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(source)

eadd, escale, emul = ns["eadd"], ns["escale"], ns["emul"]
padd, pscale, pmul = ns["padd"], ns["pscale"], ns["pmul"]
derivative, homogeneous = ns["derivative"], ns["homogeneous"]
esubstitute, coefficient, sexpr = (
    ns["esubstitute"], ns["coefficient"], ns["sexpr"]
)


def var(name):
    return {(name,): 1}


def eval_expr(expression, assignment):
    total = 0
    for monomial, scalar in expression.items():
        term = scalar
        for name in monomial:
            term *= assignment[name]
        total += term
    return total % 3


def matrix_rank_mod3(entries):
    work = [[entry % 3 for entry in row] for row in entries]
    if not work:
        return 0
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
                work[i] = [(a-scalar*b) % 3
                           for a, b in zip(work[i], work[row])]
        row += 1
        if row == len(work):
            break
    return row


def enumerate_affine_system(tag, base_names, fiber_names, matrix, rhs,
                            base_filter=lambda assignment: True):
    """Exhaust the literal F3 predecessor points, with rank certificate hash."""
    rank_pairs = {}
    compatible_ranks = {}
    examples = {}
    fiber_histogram = {}
    fiber_examples = {}
    digest = hashlib.sha256()
    total = compatible = 0
    for base_values in itertools.product(range(3), repeat=len(base_names)):
        base = dict(zip(base_names, base_values))
        if not base_filter(base):
            continue
        fiber_compatible = 0
        compatible_fibers = []
        for fiber_values in itertools.product(range(3), repeat=len(fiber_names)):
            assignment = dict(base)
            assignment.update(zip(fiber_names, fiber_values))
            numeric = [[eval_expr(entry, assignment) for entry in row]
                       for row in matrix]
            numeric_rhs = [eval_expr(entry, assignment) for entry in rhs]
            rank_a = matrix_rank_mod3(numeric)
            rank_aug = matrix_rank_mod3(
                [row+[value] for row, value in zip(numeric, numeric_rhs)]
            )
            pair = (rank_a, rank_aug)
            rank_pairs[pair] = rank_pairs.get(pair, 0) + 1
            examples.setdefault(pair, tuple(base_values)+tuple(fiber_values))
            is_compatible = rank_a == rank_aug
            if is_compatible:
                compatible += 1
                fiber_compatible += 1
                compatible_fibers.append(tuple(fiber_values))
                compatible_ranks[rank_a] = compatible_ranks.get(rank_a, 0)+1
            digest.update(bytes(tuple(base_values)+tuple(fiber_values)
                                +(rank_a, rank_aug)))
            total += 1
        fiber_histogram[fiber_compatible] = (
            fiber_histogram.get(fiber_compatible, 0) + 1
        )
        fiber_examples.setdefault(
            fiber_compatible, (tuple(base_values), tuple(compatible_fibers))
        )
    actual_digest = digest.hexdigest()
    expected = EXPECTED_ENUM[tag]
    assert total == expected["total"], (tag, total)
    assert compatible == expected["compatible"], (tag, compatible)
    assert rank_pairs == expected["rank_pairs"], (tag, rank_pairs)
    assert fiber_histogram == expected["fiber_histogram"], (
        tag, fiber_histogram
    )
    assert actual_digest == expected["sha256"], (tag, actual_digest)
    print("ENUM-%s" % tag)
    print("base_names", ",".join(base_names))
    print("fiber_names", ",".join(fiber_names))
    print("total", total, "compatible", compatible)
    print("rank_pairs", sorted(rank_pairs.items()))
    print("compatible_ranks", sorted(compatible_ranks.items()))
    print("fiber_histogram", sorted(fiber_histogram.items()))
    compact_examples = [
        (count, base, len(fibers), fibers[:12])
        for count, (base, fibers) in sorted(fiber_examples.items())
    ]
    print("fiber_examples_count_and_prefix", compact_examples)
    print("examples", sorted(examples.items()))
    print("rank_stream_sha256", actual_digest)
    print("PASS-ENUM-%s" % tag)


def classify_fiber_projection(tag, base_names, fiber_names, matrix, rhs,
                              base_filter=lambda assignment: True):
    """Exact affine projection to the Frobenius fiber, one base at a time."""
    fiber_set = set(fiber_names)
    for expression in rhs:
        assert all(sum(name in fiber_set for name in monomial) <= 1
                   for monomial in expression), expression
    for row in matrix:
        assert all(not (set(monomial) & fiber_set)
                   for expression in row for monomial in expression), row
    histogram = {}
    rank_triples = {}
    zero_bases = []
    survivor_bases = []
    zero_digest = hashlib.sha256()
    compatible_total = 0
    structural_total = 0
    zero_fiber = {name: 0 for name in fiber_names}
    for base_values in itertools.product(range(3), repeat=len(base_names)):
        base = dict(zip(base_names, base_values))
        if not base_filter(base):
            continue
        structural_total += 1
        numeric_a = [[eval_expr(entry, base) for entry in row]
                     for row in matrix]
        fiber_matrix = [
            [eval_expr(coefficient(entry, name), base) for name in fiber_names]
            for entry in rhs
        ]
        base_zero = dict(base)
        base_zero.update(zero_fiber)
        b0 = [eval_expr(entry, base_zero) for entry in rhs]
        combined = [a+f for a, f in zip(numeric_a, fiber_matrix)]
        rank_a = matrix_rank_mod3(numeric_a)
        rank_combined = matrix_rank_mod3(combined)
        rank_augmented = matrix_rank_mod3(
            [row+[value] for row, value in zip(combined, b0)]
        )
        triple = (rank_a, rank_combined, rank_augmented)
        rank_triples[triple] = rank_triples.get(triple, 0)+1
        if rank_combined != rank_augmented:
            count = 0
            zero_bases.append(tuple(base_values))
            zero_digest.update(bytes(base_values))
        else:
            exponent = len(fiber_names)+rank_a-rank_combined
            assert 0 <= exponent <= len(fiber_names), (triple, exponent)
            count = 3**exponent
            survivor_bases.append((tuple(base_values), count))
        histogram[count] = histogram.get(count, 0)+1
        compatible_total += count
    actual_zero_digest = zero_digest.hexdigest()
    expected = EXPECTED_STRUCTURAL[tag]
    assert structural_total == expected["total"], (tag, structural_total)
    assert compatible_total == expected["compatible"], (tag, compatible_total)
    assert histogram == expected["histogram"], (tag, histogram)
    assert rank_triples == expected["rank_triples"], (tag, rank_triples)
    assert len(zero_bases) == expected["zero_count"], (tag, len(zero_bases))
    assert actual_zero_digest == expected["zero_sha256"], (
        tag, actual_zero_digest
    )
    print("STRUCTURAL-%s" % tag)
    print("structural_total", structural_total)
    print("compatible_total", compatible_total)
    print("fiber_histogram", sorted(histogram.items()))
    print("rank_triples", sorted(rank_triples.items()))
    print("zero_base_count", len(zero_bases))
    print("zero_base_stream_sha256", actual_zero_digest)
    print("zero_base_prefix", zero_bases[:20])
    print("survivor_base_prefix", survivor_bases[:30])
    print("PASS-STRUCTURAL-%s" % tag)


# Source-exact L/3 contribution in total degree five from the degree-six
# Frobenius first-digit layer.
L5 = {
    (2, 3): var("fa"),       # u6_3: (3*x^2*y^3)/3
    (5, 0): escale(2, var("fb")),  # u6_6: (6*x^5)/3
    (0, 5): escale(2, var("fc")),  # v6_0: (6*y^5)/3
    (3, 2): var("fd"),       # v6_3: (3*x^3*y^2)/3
}

# Exact single-Frobenius cross term in E/3 after the accepted row is
# divided.  The six degree-six Frobenius first-digit directions are
#   U_F=fua*y^6+fa*x^3*y^3+fb*x^6,
#   V_F=fc*y^6+fd*x^3*y^3+fvb*x^6.
# The following are their integer derivatives divided by 3, reduced mod 3.
ufx3 = {(2, 3): var("fa"), (5, 0): escale(2, var("fb"))}
ufy3 = {(0, 5): escale(2, var("fua")), (3, 2): var("fa")}
vfx3 = {(2, 3): var("fd"), (5, 0): escale(2, var("fvb"))}
vfy3 = {(0, 5): escale(2, var("fc")), (3, 2): var("fd")}

C6, c6vars = homogeneous("c", 6)
D6, d6vars = homogeneous("d", 6)
c6x, c6y = derivative(C6, 0), derivative(C6, 1)
d6x, d6y = derivative(D6, 0), derivative(D6, 1)
accepted5 = padd(ns["K"], c6x, d6y, L5)

free6 = ["c6_0", "c6_3", "c6_6", "d6_0", "d6_1", "d6_3", "d6_4", "d6_6"]
sub6 = {name: var(name) for name in free6}
pivots = ["c6_1", "c6_2", "d6_2", "c6_4", "c6_5", "d6_5"]
for i, pivot in enumerate(pivots):
    row = accepted5.get((i, 5-i), {})
    coeff_expr = coefficient(row, pivot)
    assert set(coeff_expr) == {()}, (i, pivot, coeff_expr)
    scalar = coeff_expr[()] % 3
    assert scalar in (1, 2)
    rest = eadd(row, escale(2*scalar, var(pivot)))
    inverse = 1 if scalar == 1 else 2
    sub6[pivot] = escale(-inverse, rest)

Call = padd(C6, ns["C"])
Dall = padd(D6, ns["D"])
ux, uy = derivative(ns["U"], 0), derivative(ns["U"], 1)
vx, vy = derivative(ns["V"], 0), derivative(ns["V"], 1)
cx, cy = derivative(Call, 0), derivative(Call, 1)
dx, dy = derivative(Dall, 0), derivative(Dall, 1)
Mfull = padd(
    pmul(padd(ux, {(2, 0): {(): -1}}), dy),
    pmul(cx, vy), pscale(-1, pmul(uy, dx)), pscale(-1, pmul(cy, vx)),
)
KFdiv = padd(
    pmul(ufx3, vy), pmul(padd(ux, {(2, 0): {(): -1}}), vfy3),
    pscale(-1, pmul(ufy3, vx)), pscale(-1, pmul(uy, vfx3)),
)
Rfull = padd(Mfull, KFdiv)

normal = {
    "u3_1": {}, "u3_2": var("h"),
    "v3_1": escale(2, var("h")), "v3_2": {(): 1},
    "u4_0": var("p"), "u4_1": escale(2, var("r")),
    "u4_2": {}, "u4_3": var("q"), "u4_4": escale(2, var("t")),
    "v4_0": var("r"), "v4_1": var("s"), "v4_2": {},
    "v4_3": var("t"), "v4_4": var("w"),
}
for name in [f"u5_{i}" for i in range(6)]+[f"v5_{i}" for i in range(6)]:
    normal[name] = {}
if BRANCH == "g":
    normal["u4_0"] = {}
    normal["u4_3"] = {}
    normal["v5_5"] = var("g")

free = ns["free"] + free6
sub_digits = dict(ns["sub"])
sub_digits.update(sub6)
rows = []
labels = []
totals = (9, 8) if BRANCH == "vertical" else (10, 9, 8)
for total in totals:
    for i in range(total+1):
        expression = Rfull.get((i, total-i), {})
        if expression:
            expression = esubstitute(expression, sub_digits)
            expression = esubstitute(expression, normal)
            if expression:
                rows.append(expression)
                labels.append(f"M_{i}_{total-i}")

matrix = [[coefficient(row, variable) for variable in free] for row in rows]
rhs = []
for row in rows:
    affine = row
    for variable in free:
        affine = eadd(
            affine,
            escale(2, emul(coefficient(row, variable), {(variable,): 1})),
        )
    rhs.append(affine)

allowed = ({"p", "q", "r", "s", "t", "w", "h",
            "fua", "fa", "fb", "fc", "fd", "fvb"}
           if BRANCH == "vertical" else
           {"r", "s", "t", "w", "h", "g",
            "fua", "fa", "fb", "fc", "fd", "fvb"})
for expression in rhs+[entry for row in matrix for entry in row]:
    for monomial in expression:
        assert set(monomial) <= allowed, (monomial, set(monomial)-allowed)

if BRANCH == "vertical":
    print("ring R=3,(p,q,r,s,t,w,h,fua,fa,fb,fc,fd,fvb),dp;")
else:
    print("ring R=3,(r,s,t,w,h,g,fua,fa,fb,fc,fd,fvb),dp;")
print("matrix A[%d][%d]=%s;" % (
    len(rows), len(free), ",".join(sexpr(x) for row in matrix for x in row)
))
print("matrix bvec[%d][1]=%s;" % (len(rows), ",".join(sexpr(x) for x in rhs)))
print("matrix Aug[%d][%d]=%s;" % (
    len(rows), len(free)+1,
    ",".join(sexpr(x) for i, row in enumerate(matrix) for x in row+[rhs[i]])
))
print('print("labels");print("%s");' % ",".join(labels))
print('print("shape");print(nrows(A));print(ncols(A));')
print('print("generic_ranks_A_Aug");print(rank(A));print(rank(Aug));')
print('module MA=A;module mb=bvec;module rem=reduce(mb,std(MA));'
      'print("global_module_remainder");print(rem);')
print('if(size(rem)==0){matrix lif=lift(MA,mb);print("global_lift");print(lif);}')
print('print("PASS-VERTICAL-D98-EMIT");')

if BRANCH == "g":
    g_sub = {
        "c7_0": {}, "c7_3": {}, "c7_6": {},
    }
    drop = {"M_4_6", "M_7_3", "M_10_0"}
    g_rows = [esubstitute(row, g_sub) for label, row in zip(labels, rows)
              if label not in drop]
    g_labels = [label for label in labels if label not in drop]
    g_free = [name for name in free if name not in ("c7_0", "c7_3", "c7_6")]
    g_matrix = [[coefficient(row, variable) for variable in g_free]
                for row in g_rows]
    g_rhs = []
    for row in g_rows:
        affine = row
        for variable in g_free:
            affine = eadd(
                affine,
                escale(2, emul(coefficient(row, variable), {(variable,): 1})),
            )
        g_rhs.append(affine)
    print("ring G=3,(r,s,t,w,h,g,fua,fa,fb,fc,fd,fvb),dp;")
    print("matrix AG[%d][%d]=%s;" % (
        len(g_rows), len(g_free),
        ",".join(sexpr(x) for row in g_matrix for x in row)
    ))
    print("matrix bG[%d][1]=%s;" % (len(g_rows), ",".join(sexpr(x) for x in g_rhs)))
    print("matrix AugG[%d][%d]=%s;" % (
        len(g_rows), len(g_free)+1,
        ",".join(sexpr(x) for i, row in enumerate(g_matrix) for x in row+[g_rhs[i]])
    ))
    print('print("g_d10_pivots");print("g*c7_0,g*c7_3,g*c7_6");')
    print('print("g_reduced_labels");print("%s");' % ",".join(g_labels))
    print('print("g_reduced_shape_ranks");print(nrows(AG));print(ncols(AG));'
          'print(rank(AG));print(rank(AugG));')
    print('module MG=AG;module mG=bG;module remG=reduce(mG,std(MG));'
          'print("g_reduced_module_remainder");print(remG);')
    print('print("PASS-G-ENDPOINT-D108-REDUCED");')
    print('print("PASS-G-ENDPOINT-D108-EMIT");')
    if os.environ.get("ENUMERATE") == "1":
        enumerate_affine_system(
            "G-ENDPOINT-D98",
            ["r", "s", "t", "w", "h", "g"],
            ["fua", "fa", "fb", "fc", "fd", "fvb"],
            g_matrix, g_rhs, lambda point: point["g"] != 0,
        )
    if os.environ.get("STRUCTURAL") == "1":
        classify_fiber_projection(
            "G-ENDPOINT-D98",
            ["r", "s", "t", "w", "h", "g"],
            ["fua", "fa", "fb", "fc", "fd", "fvb"],
            g_matrix, g_rhs, lambda point: point["g"] != 0,
        )
    raise SystemExit

# A second ring block: exact constant-pivot elimination of six D8 rows.
pivot_sub = {}
for row_index, pivot in ((6, "d7_0"), (5, "c7_0"),
                         (9, "d7_3"), (8, "c7_3"),
                         (12, "d7_6"), (11, "c7_6")):
    equation = esubstitute(rows[row_index], pivot_sub)
    coeff_expr = coefficient(equation, pivot)
    assert coeff_expr == {(): 1}, (labels[row_index], pivot, coeff_expr)
    rest = eadd(equation, escale(2, var(pivot)))
    pivot_sub[pivot] = escale(2, rest)

remaining_indices = [0, 1, 2, 3, 4, 7, 10]
remaining_vars = ["d7_1", "d7_4", "d7_7", "d6_1", "d6_4"]
reduced_rows = [esubstitute(rows[i], pivot_sub) for i in remaining_indices]
reduced_matrix = [[coefficient(row, variable) for variable in remaining_vars]
                  for row in reduced_rows]
reduced_rhs = []
for row in reduced_rows:
    affine = row
    for variable in remaining_vars:
        affine = eadd(
            affine,
            escale(2, emul(coefficient(row, variable), {(variable,): 1})),
        )
    reduced_rhs.append(affine)

print("matrix AR[7][5]=%s;" % ",".join(
    sexpr(x) for row in reduced_matrix for x in row
))
print("matrix bR[7][1]=%s;" % ",".join(sexpr(x) for x in reduced_rhs))
print("matrix AugR[7][6]=%s;" % ",".join(
    sexpr(x) for i, row in enumerate(reduced_matrix) for x in row+[reduced_rhs[i]]
))
print('print("reduced_labels");print("%s");' % ",".join(labels[i] for i in remaining_indices))
print('print("reduced_generic_ranks");print(rank(AR));print(rank(AugR));')
print('print("AR");print(AR);print("bR");print(bR);')
print('print("PASS-VERTICAL-D98-REDUCED");')

# Triangular coordinate change that exposes the Sylvester-like core.
def prod(*expressions):
    out = {(): 1}
    for expression in expressions:
        out = emul(out, expression)
    return out

coord = {
    "r": eadd(var("Rr"), prod(var("s"), var("h"))),
    "t": eadd(var("Tt"), prod(var("w"), var("h"))),
    "p": eadd(var("Pp"), prod(var("Rr"), var("h")),
              escale(2, prod(var("s"), var("h"), var("h")))),
    "q": eadd(var("Qq"), prod(var("Tt"), var("h")),
              escale(2, prod(var("w"), var("h"), var("h")))),
}
core_matrix = [[esubstitute(x, coord) for x in row] for row in reduced_matrix]
core_rhs = [esubstitute(x, coord) for x in reduced_rhs]
print("ring S=3,(Pp,Qq,Rr,Tt,s,w,h,fua,fa,fb,fc,fd,fvb),dp;")
print("matrix AC[7][5]=%s;" % ",".join(
    sexpr(x) for row in core_matrix for x in row
))
print("matrix bC[7][1]=%s;" % ",".join(sexpr(x) for x in core_rhs))
print("matrix AugC[7][6]=%s;" % ",".join(
    sexpr(x) for i, row in enumerate(core_matrix) for x in row+[core_rhs[i]]
))
print('print("core_generic_ranks");print(rank(AC));print(rank(AugC));')
print('module MC=AC;module mC=bC;module remC=reduce(mC,std(MC));'
      'print("core_module_remainder");print(remC);')
print('ideal Obs6=minor(AugC,6);'
      'print("generic_compatibility_minor_count");print(size(Obs6));')
for i in range(7):
    print('print("bC%d");print(bC[%d,1]);' % (i, i + 1))
print('print("AC");print(AC);print("bC");print(bC);')
print('print("PASS-VERTICAL-D98-CORE");')
if os.environ.get("ENUMERATE") == "1":
    enumerate_affine_system(
        "VERTICAL-D98",
        ["Pp", "Qq", "Rr", "Tt", "s", "w", "h"],
        ["fua", "fa", "fb", "fc", "fd", "fvb"], core_matrix, core_rhs,
    )
if os.environ.get("STRUCTURAL") == "1":
    classify_fiber_projection(
        "VERTICAL-D98",
        ["Pp", "Qq", "Rr", "Tt", "s", "w", "h"],
        ["fua", "fa", "fb", "fc", "fd", "fvb"],
        core_matrix, core_rhs,
    )
