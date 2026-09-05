#!/usr/bin/env python3
"""CONTROL (a): old-radius D=108 stage-0 unit still reproduces [1].

The leading-row patch is a no-op at stage 0 (pole local power 4 << 64/96),
so the frozen-radius kill must be byte-identical in the pole rows and must
still return the unit ideal. Two witnesses of the same fact:

  1. minor_incidence at the frozen cut-43, localized groebner = [1]
     (rekill control 1; the actual stage-0 death).
  2. the full staged joint driver at wz=6, stage 0: dim = -1, UNIT.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
WORK = HERE.parent / "d108-rekill-20260905" / "work"
sys.path.insert(0, str(WORK))
from rekill_engine import (
    FRZ, SRC, minor_incidence, qstar_reduce, symbol, pole_coeff,
    raw_minor_support, stage_spec,
)
import step3_joint

t0 = time.monotonic()
out = {}

# --- (a1) frozen cut-43 groebner [1]
rows, hvars, _ = minor_incidence(FRZ, 43, False)
resid, subs, piv, zeros = qstar_reduce(rows, hvars)
c, Zc = symbol("c"), symbol("Zc")
gens = [v for _l, v in resid] + [Zc * c - 1]
rv = sorted(set().union(*(g.free_symbols for g in gens)), key=str)
G = sp.groebner(gens, *rv, order="grevlex")
unit = list(G.exprs) == [sp.Integer(1)]
out["a1_frozen_cut43_groebner"] = {
    "coords": len(hvars),
    "raw_rows": len(rows),
    "nonzero_rows": sum(1 for _l, v in rows if v != 0),
    "pivots": len(piv),
    "residual": {l: str(v) for l, v in resid},
    "localized_unit": unit,
    "groebner": [str(g) for g in G.exprs],
    "reproduces_[1]": unit and G.exprs == [sp.Integer(1)],
}

# --- identity at stage 0 (n = 4)
n0 = stage_spec(0)["pole_local_power"]
out["stage0_pole_local_power"] = n0
out["stage0_is_strictly_below_leading"] = n0 < 64
sentinel = sp.Symbol("SENTINEL")
dummy = {(n0, k): sentinel for k in range(30)}
out["stage0_pole_coeff_is_table_get"] = all(
    pole_coeff(dummy, n0, k, name) == sentinel
    for name in ("F", "G")
    for k in raw_minor_support(name, False).get(n0, ())
)

# --- (a2) full joint stage-0 at frozen radius
step3_joint.OUT = HERE
rec = step3_joint.run(0, False, FRZ, tag="ctl_a_joint_wz6_jet0pinned_stage0")
sing = rec["singular"]
out["a2_joint_frozen_stage0"] = {
    "tag": rec["tag"],
    "raw_row_count": rec["raw_row_count"],
    "Qstar_pivots": rec["Qstar_pivots"],
    "residual_row_count": rec["residual_row_count"],
    "dimension": sing.get("dimension"),
    "unit_ideal": sing.get("unit_ideal"),
    "reduce_1_in_std": sing.get("reduce_1_in_std"),
    "pipeline_can_still_kill": sing.get("unit_ideal") is True
    and str(sing.get("reduce_1_in_std")) == "0"
    and sing.get("dimension") == -1,
    "wall_seconds": rec["wall_seconds"],
}

out["wall_seconds"] = round(time.monotonic() - t0, 1)
(HERE / "ctl_a_frozen_stage0.json").write_text(json.dumps(out, indent=2) + "\n")
ok = (
    out["a1_frozen_cut43_groebner"]["reproduces_[1]"]
    and out["stage0_is_strictly_below_leading"]
    and out["stage0_pole_coeff_is_table_get"]
    and out["a2_joint_frozen_stage0"]["pipeline_can_still_kill"]
)
print(json.dumps(out, indent=2))
print("CTL_A_OK" if ok else "CTL_A_FAIL")
sys.exit(0 if ok else 1)
