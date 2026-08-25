#!/usr/bin/env python3
"""Exact integer-source audit for the full homogeneous C5,D5 D7 gate."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import runpy
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
SOURCE = (ROOT / "cases/as_fonly_d7_vertical_d7_source_license_20260824"
          / "audit_full_e1_degree7.py")
with contextlib.redirect_stdout(io.StringIO()):
    sl = runpy.run_path(str(SOURCE))

padd = sl["padd"]
pmul = sl["pmul"]
pscale = sl["pscale"]
derivative = sl["derivative"]
homogeneous = sl["homogeneous"]
degree_part = sl["degree_part"]
mod3 = sl["mod3"]
eadd = sl["eadd"]
ns = sl["ns"]


def psubstitute(poly, substitution):
    return {xy: ns["esubstitute"](e, substitution)
            for xy, e in poly.items()
            if ns["esubstitute"](e, substitution)}


def canonical_hash(rows):
    payload = []
    for row in rows:
        payload.append([[list(m), c] for m, c in sorted(row.items())])
    raw = json.dumps(payload, separators=(",", ":"), sort_keys=False).encode()
    return hashlib.sha256(raw).hexdigest()


C5 = homogeneous("c", 5)
D5 = homogeneous("d", 5)
Cfull = padd(sl["C"], C5)
Dfull = padd(sl["D"], D5)
cx, cy = derivative(Cfull, 0), derivative(Cfull, 1)
dx, dy = derivative(Dfull, 0), derivative(Dfull, 1)

# Full mixed term with all first-digit Frobenius pieces retained over Z;
# reduction happens only after construction.
Mfull = padd(pmul(sl["A"], dy), pmul(cx, sl["vy"]),
             pscale(-1, pmul(sl["uy"], dx)),
             pscale(-1, pmul(cy, sl["vx"])))
residual7 = degree_part(mod3(padd(Mfull, sl["E1_7"])), 7)

# Accepted degree-four source row E=L/3+K+div(C,D).  Degree-four of L/3 is
# empty, and C6/C7 cannot reach it, so this is K4+div(C5,D5).
assert degree_part(sl["L1"], 4) == {}
accepted4 = degree_part(mod3(padd(sl["L1"], sl["K"],
                                  derivative(C5, 0), derivative(D5, 1))), 4)
accepted_all = [accepted4.get((i, 4-i), {}) for i in range(5)]
assert accepted_all[2] == {}
assert all(accepted_all[i] for i in (0, 1, 3, 4))

# Apply only the separately registered accepted D5/D6, D8-unit-pivot, and
# triangular coordinate substitutions.  C5,D5 are untouched.
d7_rows = []
for i in range(8):
    e = residual7.get((i, 7-i), {})
    e = ns["esubstitute"](e, ns["sub_digits"])
    e = ns["esubstitute"](e, ns["normal"])
    e = ns["esubstitute"](e, ns["pivot_sub"])
    e = ns["esubstitute"](e, ns["coord"])
    d7_rows.append(e)
accepted_rows = []
for i in (0, 1, 3, 4):
    e = accepted_all[i]
    e = ns["esubstitute"](e, ns["normal"])
    e = ns["esubstitute"](e, ns["coord"])
    accepted_rows.append(e)

# Negative control: setting C5=D5=0 recovers exactly the frozen eight-row
# slice, while at least six full rows have genuine new current-digit terms.
zero5 = {f"c5_{i}": {} for i in range(6)}
zero5.update({f"d5_{i}": {} for i in range(6)})
slice_rows = [ns["esubstitute"](row, zero5) for row in d7_rows]
assert slice_rows == sl["actual"]
changed = [i for i, (full, old) in enumerate(zip(d7_rows, slice_rows))
           if full != old]
assert changed == [0, 1, 3, 4, 6, 7]

print("accepted_degree4_nonzero_rows", len(accepted_rows))
print("accepted_cartier_x2y2", ns["sexpr"](accepted_all[2]))
print("accepted_rows_sha256", canonical_hash(accepted_rows))
print("full_D7_rows_sha256", canonical_hash(d7_rows))
print("zero_C5_D5_changed_rows", changed)
for i, row in enumerate(accepted_all):
    print(f"accepted4_{i}_{4-i}", ns["sexpr"](row))
for i, row in enumerate(d7_rows):
    print(f"full_D7_{i}_{7-i}", ns["sexpr"](row))
print("PASS-FULL-C5-INTEGER-SOURCE")
