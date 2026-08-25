#!/usr/bin/env python3
"""Exact source for the first following Cartier row after full-C5 D7."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import runpy
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
PARENT = (ROOT / "cases/as_fonly_d7_vertical_full_c5_d7_gate_20260824"
          / "audit_full_c5_source.py")
with contextlib.redirect_stdout(io.StringIO()):
    parent = runpy.run_path(str(PARENT))

sl = parent["sl"]
ns = parent["ns"]
padd = sl["padd"]
pmul = sl["pmul"]
pscale = sl["pscale"]
derivative = sl["derivative"]
homogeneous = sl["homogeneous"]
degree_part = sl["degree_part"]
mod3 = sl["mod3"]
eadd = sl["eadd"]


def divide_expr_mod3(expression, divisor):
    assert all(value % divisor == 0 for value in expression.values())
    return {m: (value // divisor) % 3 for m, value in expression.items()
            if (value // divisor) % 3}


def canonical_hash(rows):
    payload = [[[list(m), c] for m, c in sorted(row.items())]
               for row in rows]
    return hashlib.sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


C2 = homogeneous("c", 2)
D2 = homogeneous("d", 2)
C3 = homogeneous("c", 3)
D3 = homogeneous("d", 3)
C = padd(C2, C3, parent["C5"], sl["C"])
D = padd(D2, D3, parent["D5"], sl["D"])
cx, cy = derivative(C, 0), derivative(C, 1)
dx, dy = derivative(D, 0), derivative(D, 1)

# E=L/3+K+div(C,D), constructed over Z.  Its degree-one and degree-two
# reductions are the only accepted lower rows relevant to M_(2,2).
E = padd(sl["L1"], sl["K"], cx, dy)
Emod = mod3(E)
accepted1 = [Emod.get((i, 1-i), {}) for i in range(2)]
accepted2 = [Emod.get((i, 2-i), {}) for i in range(3)]
assert all(accepted1 + accepted2)

# The Cartier coefficient E1_(2,2) is formally divisible by three: no
# quotient by an equation or canonical representative is used.
E22 = E.get((2, 2), {})
E1_22 = divide_expr_mod3(E22, 3)

M = padd(pmul(sl["A"], dy), pmul(cx, sl["vy"]),
         pscale(-1, pmul(sl["uy"], dx)),
         pscale(-1, pmul(cy, sl["vx"])))
M22 = mod3(M).get((2, 2), {})
F22 = eadd(E1_22, M22)

# Transform the charged degree-four structural coordinates exactly as in the
# parent gate; no accepted equation is divided or cleared.
accepted1 = [ns["esubstitute"](row, ns["coord"]) for row in accepted1]
accepted2 = [ns["esubstitute"](row, ns["coord"]) for row in accepted2]
F22 = ns["esubstitute"](F22, ns["coord"])

# Current digits of degrees 0/1/4 do not affect F22.  Degree-four accepted
# rows were solved in the parent; degrees 0/3 are divergence-surjective and
# can be solved independently.
lower_rows = accepted1 + accepted2 + [F22]
print("accepted_degree1_rows", [ns["sexpr"](x) for x in accepted1])
print("accepted_degree2_rows", [ns["sexpr"](x) for x in accepted2])
print("E1_x2y2", ns["sexpr"](E1_22))
print("M_x2y2", ns["sexpr"](M22))
print("F_x2y2", ns["sexpr"](F22))
print("lower_cartier_rows_sha256", canonical_hash(lower_rows))
print("PASS-NEXT-CARTIER-INTEGER-SOURCE")
