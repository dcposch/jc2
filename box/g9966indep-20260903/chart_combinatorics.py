#!/usr/bin/env python3
"""Independent reconstruction of the (99,66) joint-chart combinatorics.

Built ONLY from the design reports' displayed formulas (global-design 2.1-2.4,
outer-bridge 2, band 3-4).  band_engine.py was never read.
"""
from math import comb
import json

def S(D, r0):
    """homogenized slots of {A : deg A<=D, deg_y A<r0}: t^r (w-1)^q, r+q<=D, q<r0."""
    return [(r, q) for q in range(r0) for r in range(0, D - q + 1)]

BLOCKS = {  # name: (degree D, deg_y bound r0)
    'H': (10, 11), 'C2': (21, 11), 'C3': (32, 11),
    'A2': (65, 33), 'A3': (98, 33), 'B1': (32, 33), 'B2': (65, 33)}

out = {}
sizes = {k: len(S(*v)) for k, v in BLOCKS.items()}
out['block_sizes'] = sizes
out['chart_total'] = sum(sizes.values())

# ---- outer D2 support preblock: unit vanishings 3r+4q < 3(D+bound) ----
# ord bounds from Thm 1.2 with ord h2(D2) = -1 : A2>=-2, A3>=-3, B1>=-1, B2>=-2
from fractions import Fraction
OUTER = {  # name: (D, r0, D2 t-order bound, D1 t-order bound)
    'A2': (65, 33, Fraction(-2), Fraction(-2, 9)),
    'A3': (98, 33, Fraction(-3), Fraction(-1, 3)),
    'B1': (32, 33, Fraction(-1), Fraction(-1, 9)),
    'B2': (65, 33, Fraction(-2), Fraction(-2, 9))}

d2_thresh = {k: int(3 * (v[0] + v[2])) for k, v in OUTER.items()}
d1_thresh = {k: int(9 * (v[0] + v[3])) for k, v in OUTER.items()}
out['D2_thresholds'] = {k: int(v) for k, v in d2_thresh.items()}
out['D1_thresholds'] = {k: int(v) for k, v in d1_thresh.items()}

surv, deleted = {}, {}
for k, (D, r0, _, _) in OUTER.items():
    sl = S(D, r0)
    keep = [(r, q) for (r, q) in sl if 3 * r + 4 * q >= d2_thresh[k]]
    surv[k] = keep
    deleted[k] = len(sl) - len(keep)
out['outer_ambient'] = sum(len(S(*OUTER[k][:2])) for k in OUTER)
out['D2_deleted'] = deleted
out['D2_deleted_total'] = sum(deleted.values())
out['D2_remaining_total'] = sum(len(v) for v in surv.values())

# ---- outer D1 rows: t=e^9, w=1+e^12+Pi e^13 ; term c_rq e^{9r+12q}(1+Pi e)^q
# monomial Pi^j e^E with E = 3W + j,  W = 3r+4q.  Row (block,W,j) for E < thresh.
d1_rows = []   # (block, W, j, [ (col,(r,q)), coeff ])
for k in OUTER:
    W0, T = d2_thresh[k], d1_thresh[k]
    byW = {}
    for (r, q) in surv[k]:
        byW.setdefault(3 * r + 4 * q, []).append((r, q))
    for W in sorted(byW):
        if 3 * W >= T:
            continue
        for j in range(0, T - 3 * W):
            cols = [(rq, comb(rq[1], j)) for rq in byW[W] if rq[1] >= j]
            d1_rows.append((k, W - W0, W, j, cols))
from collections import defaultdict
raw = defaultdict(int); rk = defaultdict(int)
for (k, s, W, j, cols) in d1_rows:
    raw[s] += 1
per_off_cols = defaultdict(lambda: defaultdict(set))
for (k, s, W, j, cols) in d1_rows:
    per_off_cols[s][k].add(W)
# rank per (block, offset) = min(#rows, #columns) for a binomial (Vandermonde-type) matrix
rank_off = defaultdict(int)
for k in OUTER:
    W0, T = d2_thresh[k], d1_thresh[k]
    byW = defaultdict(list)
    for (r, q) in surv[k]:
        byW[3 * r + 4 * q].append((r, q))
    for W in sorted(byW):
        if 3 * W >= T:
            continue
        nrows = T - 3 * W
        ncols = len(byW[W])
        rank_off[W - W0] += min(nrows, ncols)
out['D1_raw_per_offset'] = [raw[s] for s in sorted(raw)]
out['D1_rank_per_offset'] = [rank_off[s] for s in sorted(raw)]
out['D1_raw_total'] = sum(raw.values())
out['D1_rank_total'] = sum(rank_off.values())

# ---- inner h3 (D=11 slots from H, shifted r->r+1 inside K3) : threshold 3(11-1/3)=32
h3_slots = [(r + 1, q) for (r, q) in S(10, 11)]
h3_free = [(r, q) for (r, q) in h3_slots if 3 * r + 4 * q >= 33]
out['h3_slots'] = len(h3_slots)
out['h3_killed'] = len(h3_slots) - len(h3_free)
out['h3_free'] = len(h3_free)
out['h3_equality_sites'] = sorted([(r, q) for (r, q) in h3_slots if 3 * r + 4 * q == 32])

# ---- inner h2 : K2c slots r>=1, q<=32, r+q<=33 ; D2 weight >= 96, face (pi^3-1)^8
k2_slots = [(r, q) for q in range(0, 33) for r in range(1, 34 - q)]
out['k2_slots'] = len(k2_slots)
k2_zero = [(r, q) for (r, q) in k2_slots if 3 * r + 4 * q < 96]
k2_eq = [(r, q) for (r, q) in k2_slots if 3 * r + 4 * q == 96]
k2_strict = [(r, q) for (r, q) in k2_slots if 3 * r + 4 * q >= 97]
out['k2_D2_zero'] = len(k2_zero); out['k2_D2_equality'] = len(k2_eq)
out['k2_D2_strict'] = len(k2_strict)
out['k2_D2_rows'] = len(k2_zero) + len(k2_eq)
# low-q (C2/C3-controllable, q<=21) free symbols
k2_lowq = [(r, q) for (r, q) in k2_strict if q <= 21]
out['k2_lowq_free_106'] = len(k2_lowq)
out['k2_highq_h3determined'] = len([x for x in k2_strict if x[1] >= 22])
# h2 D1 rows: threshold 9*(33-1/9) = 296, weights >= 96
h2rows = []
byW = defaultdict(list)
for (r, q) in k2_slots:
    byW[3 * r + 4 * q].append((r, q))
for W in sorted(byW):
    if 3 * W >= 296:
        continue
    nrows = 296 - 3 * W
    for j in range(nrows):
        h2rows.append((W, j, 3 * W + j))
out['h2_D1_rows_all_weights'] = len(h2rows)
unk = [(W, j, E) for (W, j, E) in h2rows if W >= 97]
out['h2_D1_rows_on_unknowns'] = len(unk)
out['h2_D1_rows_by_epower'] = dict(sorted(
    __import__('collections').Counter(E for (_, _, E) in unk).items()))
out['h2_D1_rank'] = sum(min(296 - 3 * W, len(byW[W])) for W in sorted(byW)
                        if 3 * W < 296 and W >= 97)
print(json.dumps(out, indent=1, default=str))
