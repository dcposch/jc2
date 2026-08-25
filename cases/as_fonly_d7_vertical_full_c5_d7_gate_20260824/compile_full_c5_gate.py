#!/usr/bin/env python3
"""Discovery: attach all homogeneous degree-five current digits to D7."""
from __future__ import annotations

import contextlib
import io
import itertools
import hashlib
import os
import runpy
from collections import Counter
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
GEN = ROOT / "cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/generate_corrected.py"
SOURCE_AUDIT = Path(__file__).with_name("audit_full_c5_source.py")
os.environ["BRANCH"] = "vertical"
os.environ.pop("ENUMERATE", None)
os.environ.pop("STRUCTURAL", None)
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(GEN))

eadd = ns["eadd"]
emul = ns["emul"]
escale = ns["escale"]
esubstitute = ns["esubstitute"]
coefficient = ns["coefficient"]
eval_expr = ns["eval_expr"]
rank = ns["matrix_rank_mod3"]
var = ns["var"]
padd = ns["padd"]
pmul = ns["pmul"]
pscale = ns["pscale"]
derivative = ns["derivative"]
homogeneous = ns["homogeneous"]


def psubstitute(poly, substitution):
    return {xy: esubstitute(e, substitution) for xy, e in poly.items()
            if esubstitute(e, substitution)}


# The reviewed D8 core equations in its five current-digit unknowns.
remaining = tuple(ns["remaining_vars"])
core = []
for row, affine in zip(ns["core_matrix"], ns["core_rhs"]):
    equation = affine
    for entry, name in zip(row, remaining):
        equation = eadd(equation, emul(entry, var(name)))
    core.append(equation)

# Full homogeneous degree-five current digit.
C5, c5names = homogeneous("c", 5)
D5, d5names = homogeneous("d", 5)
c5x, c5y = derivative(C5, 0), derivative(C5, 1)
d5x, d5y = derivative(D5, 0), derivative(D5, 1)

# Accepted degree-four row.  L/3 has degrees 1,3,5 in this normal form, so
# degree four is K(U0,V0)+div(C5,D5).
Knormal = psubstitute(ns["ns"]["K"], ns["normal"])
accepted4 = padd(Knormal, c5x, d5y)
accepted_all = [accepted4.get((i, 4-i), {}) for i in range(5)]
assert accepted_all[2] == {}  # universal first-carry Cartier-zero row
assert all(accepted_all[i] for i in (0, 1, 3, 4))
accepted_rows = [accepted_all[i] for i in (0, 1, 3, 4)]

# Mixed-carry degree-seven contribution from C5,D5 crossed with the degree-
# four first digit.  Frobenius derivatives vanish in M mod 3.
U0 = psubstitute(ns["ns"]["U"], ns["normal"])
V0 = psubstitute(ns["ns"]["V"], ns["normal"])
ux, uy = derivative(U0, 0), derivative(U0, 1)
vx, vy = derivative(V0, 0), derivative(V0, 1)
A = padd(ux, {(2, 0): {(): -1}})
M5 = padd(pmul(A, d5y), pmul(c5x, vy),
          pscale(-1, pmul(uy, d5x)), pscale(-1, pmul(c5y, vx)))

# Existing degree-seven residual after all accepted D5/D6 and D8 unit pivots.
old7 = {}
for i in range(8):
    e = ns["Rfull"].get((i, 7-i), {})
    e = esubstitute(e, ns["sub_digits"])
    e = esubstitute(e, ns["normal"])
    e = esubstitute(e, ns["pivot_sub"])
    e = esubstitute(e, ns["coord"])
    old7[(i, 7-i)] = e

M5 = psubstitute(M5, ns["coord"])
d7_rows = [eadd(old7[(i, 7-i)], M5.get((i, 7-i), {}))
           for i in range(8)]

# The compiler must consume the independently integer-derived rows exactly.
with contextlib.redirect_stdout(io.StringIO()):
    source_ns = runpy.run_path(str(SOURCE_AUDIT))
assert accepted_rows == source_ns["accepted_rows"]
assert d7_rows == source_ns["d7_rows"]

equations = core + accepted_rows + d7_rows
unknowns = remaining + tuple(c5names) + tuple(d5names)
structural = ("Pp", "Qq", "Rr", "Tt", "s", "w", "h")
frob = ("fua", "fa", "fb", "fc", "fd", "fvb")
allowed = set(unknowns + structural + frob)
for equation in equations:
    assert all(set(monomial) <= allowed for monomial in equation)

matrix = [[coefficient(equation, name) for name in unknowns]
          for equation in equations]
rhs = []
for equation in equations:
    affine = equation
    for entry, name in zip(matrix[len(rhs)], unknowns):
        affine = eadd(affine, escale(2, emul(entry, var(name))))
    assert not any(set(monomial) & set(unknowns) for monomial in affine)
    rhs.append(affine)

# Coefficients may depend only on structural state, while the affine column is
# affine in the six Frobenius directions.
for row in matrix:
    for entry in row:
        assert all(set(monomial) <= set(structural) for monomial in entry)
for affine in rhs:
    assert all(sum(name in frob for name in monomial) <= 1
               for monomial in affine)

rank_triples = Counter()
fiber_hist = Counter()
compatible_frob_total = 0
compatible_digit_total = 0
empty_bases = []
literal_compatible_total = 0
literal_fiber_hist = Counter()
literal_digest = hashlib.sha256()
for values in itertools.product(range(3), repeat=len(structural)):
    assignment = dict(zip(structural, values))
    numeric_a = [[eval_expr(entry, assignment) for entry in row]
                 for row in matrix]
    fcols = [[eval_expr(coefficient(affine, name), assignment)
              for name in frob] for affine in rhs]
    zero_frob = {name: {} for name in frob}
    b0 = [eval_expr(esubstitute(affine, zero_frob), assignment)
          for affine in rhs]
    combined = [a + f for a, f in zip(numeric_a, fcols)]
    r = rank(numeric_a)
    c = rank(combined)
    d = rank([row + [value] for row, value in zip(combined, b0)])
    rank_triples[(r, c, d)] += 1
    if c == d:
        fcount = 3 ** (len(frob) + r - c)
        digit_count = 3 ** (len(frob) + len(unknowns) - c)
        compatible_frob_total += fcount
        compatible_digit_total += digit_count
    else:
        fcount = 0
        empty_bases.append(values)
    fiber_hist[fcount] += 1

    # Independent literal-F3 enumeration after one row reduction of A.  Row
    # operations are applied to [A|F|b0], but pivots are chosen only in A.
    work = [[entry % 3 for entry in a + f + [b]]
            for a, f, b in zip(numeric_a, fcols, b0)]
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
    literal_here = 0
    for fvalues in itertools.product(range(3), repeat=len(frob)):
        ok = True
        for line in work[r:]:
            value = line[-1]
            value += sum(a*b for a, b in
                         zip(line[len(unknowns):-1], fvalues))
            if value % 3:
                ok = False
                break
        if ok:
            literal_here += 1
            literal_digest.update(bytes(values + fvalues))
    assert literal_here == fcount, (values, literal_here, fcount)
    literal_fiber_hist[literal_here] += 1
    literal_compatible_total += literal_here

print("shape", len(equations), len(unknowns))
print("row_blocks", len(core), len(accepted_rows), len(d7_rows))
print("unknowns", unknowns)
print("rank_triples", sorted(rank_triples.items()))
print("frob_fiber_histogram", sorted(fiber_hist.items()))
print("compatible_frob_total", compatible_frob_total)
print("compatible_current_digit_total", compatible_digit_total)
print("literal_compatible_frob_total", literal_compatible_total)
print("literal_frob_fiber_histogram", sorted(literal_fiber_hist.items()))
print("literal_compatible_stream_sha256", literal_digest.hexdigest())
print("empty_structural_count", len(empty_bases))
print("empty_structural_prefix", empty_bases[:30])
print("accepted_cartier_row", ns["sexpr"](accepted_all[2]))
for i, row in enumerate(d7_rows):
    print(f"full_D7_{i}_{7-i}", ns["sexpr"](row))
print("PASS-DISCOVERY-FULL-C5-GATE")
