#!/usr/bin/env python3
"""Specialise charged Laurent/Euler diagonals (5.9)--(5.15) at t=6."""

from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import laurent_pivot_formulas as F  # noqa: E402

T = 6
y = sp.Symbol("q13_1")
q = 2 * T + 1
H = sp.expand(12 * q**2 * y**2 - 12 * q * (T + 1) * y + (T + 1) * (3 * T + 2))
Hprim = sp.Poly(H, y, domain=sp.QQ).primitive()[1].as_expr()
d = 2 * q * y - (T + 1)
cbar = T * (3 * T + 1) * y * ((T + 1) - 6 * q * y) / (6 * q**3)


def res(expr):
    return sp.resultant(H, sp.expand(expr), y)


def reduce_y(expr):
    return F.fixed_reduce(expr, T, y)


records = []
# C-family 1 <= j <= t-1
for j in range(1, T):
    Lc = F.L_c.subs({F.t: T, F.j: j, F.d: d})
    pc = F.p_c_closed.subs({F.t: T, F.j: j, F.d: d})
    Fc = F.F_c.subs({F.t: T, F.j: j})
    r = res(Lc)
    records.append({
        "family": "C", "j": j, "variable": "C%d" % j,
        "L": str(sp.expand(Lc)),
        "p": str(reduce_y(pc)),
        "F": str(sp.expand(Fc)),
        "resultant": str(r),
        "unit": r != 0,
    })
    assert r != 0, (j, r)

# Q-family t <= j <= 2t
for j in range(T, 2 * T + 1):
    Lq = F.L_q.subs({F.t: T, F.j: j, F.d: d})
    pq = F.p_q_closed.subs({F.t: T, F.j: j, F.d: d})
    Fq = F.F_q.subs({F.t: T, F.j: j})
    r = res(Lq)
    records.append({
        "family": "Q", "j": j, "variable": "q%d_0" % j,
        "L": str(sp.expand(Lq)),
        "p": str(reduce_y(pq)),
        "F": str(sp.expand(Fq)),
        "resultant": str(r),
        "unit": r != 0,
    })
    assert r != 0, (j, r)

L2 = (3 * q * d + (T + 1))
pb2 = F.p_b2.subs({F.t: T, F.j: 2 * T + 1, F.d: d})
r2 = res(L2)
records.append({
    "family": "b2", "j": 2 * T + 1, "variable": "b2",
    "L": str(sp.expand(L2)),
    "p": str(reduce_y(pb2)),
    "resultant": str(r2),
    "unit": r2 != 0,
})
assert r2 != 0

units = {
    "y": str(res(y)),
    "linear_t+1-6qy": str(res((T + 1) - 6 * q * y)),
    "cbar": str(res(cbar)),
}
assert all(sp.sympify(v) != 0 for v in units.values())

out = {
    "t": T,
    "H": str(H),
    "H_primitive": str(Hprim),
    "cbar": str(sp.together(cbar)),
    "irreducible": bool(sp.Poly(Hprim, y, domain=sp.QQ).is_irreducible),
    "disc_H": int(sp.discriminant(H, y)),
    "square_free_part_of_3_t_plus_1": 21,
    "field": "Q(sqrt(21))",
    "units": units,
    "high_pivots": records,
    "all_resultants_nonzero": True,
    "n_high_Et": 2 * T + 1,
}
path = HERE / "t6_laurent_pivot_specialization.json"
path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print("LAURENT_T6_SPECIALIZATION_PASS n=%d Hprim=%s" % (len(records), Hprim))
for rec in records:
    print("  j=%s var=%s res=%s L=%s" % (
        rec["j"], rec["variable"], rec["resultant"], rec["L"]))
print("UNITS", units)
print("WROTE", path)
