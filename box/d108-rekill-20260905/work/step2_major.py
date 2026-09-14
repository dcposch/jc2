#!/usr/bin/env python3
"""Step 2: major h2 D2 chart + h2 D1 block at the corrected radius, plus the
outer-block sizing (W0/threshold derived, then verified against the frozen
(99,66) specs by the same derivation)."""
import json, sys, time
from math import comb
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rekill_engine import (SRC, FRZ, Radius, minor_incidence, qstar_reduce, symbol,
                           build_major_h2, substitute_map, h3_template)

OUT = Path(__file__).resolve().parent


def outer_specs(R, nF, nG, degh2):
    """W0 and D1 threshold for each outer block, derived from the radius."""
    kf_w, kg_w = 3 * R.k2_face, 2 * R.k2_face
    kf_d1, kg_d1 = 3 * R.k2_d1, 2 * R.k2_d1
    sh = R.tshift                 # D2 weight cost of (r,q) -> (r+1,q)
    dsh = R.d1_mult * R.tshift    # the same shift measured in D1 e-exponent
    return {
        "A2": {"degree": nF - degh2 - 1, "W0": kf_w - R.k2_face - sh,
               "threshold": kf_d1 - R.k2_d1 - dsh, "container": "KF", "with_K2": True},
        "A3": {"degree": nF - 1, "W0": kf_w - sh,
               "threshold": kf_d1 - dsh, "container": "KF", "with_K2": False},
        "B1": {"degree": nG - degh2 - 1, "W0": kg_w - R.k2_face - sh,
               "threshold": kg_d1 - R.k2_d1 - dsh, "container": "KG", "with_K2": True},
        "B2": {"degree": nG - 1, "W0": kg_w - sh,
               "threshold": kg_d1 - dsh, "container": "KG", "with_K2": False},
    }


class R9966(Radius):
    """(99,66) delta-2 sibling radius, for the derivation control only."""
    def __init__(self):
        self.wz = 4; self.W = lambda r, q: 3 * r + 4 * q
        self.k3_face = 4 * 8; self.k2_face = 4 * 24
        self.d1_mult = 3; self.A2gal = 3; self.k2_mult = 8; self.eps = 8
        self.k2_d1 = 3 * 96 + 8; self.tshift = 3


rec = {}
# --- derivation control: reproduce the frozen (99,66) OUTER_SPECS exactly.
ctl = outer_specs(R9966(), 99, 66, 33)
frozen_9966 = {"A2": (65, 189, 583), "A3": (98, 285, 879),
               "B1": (32, 93, 287), "B2": (65, 189, 583)}
match = all((ctl[b]["degree"], ctl[b]["W0"], ctl[b]["threshold"]) == frozen_9966[b]
            for b in frozen_9966)
rec["control_outer_spec_derivation_9966"] = {
    "derived": {b: [ctl[b]["degree"], ctl[b]["W0"], ctl[b]["threshold"]] for b in ctl},
    "frozen": {b: list(v) for b, v in frozen_9966.items()}, "MATCH": match}
print(f"CONTROL outer-spec derivation vs frozen (99,66): MATCH={match}")

# --- derivation control: reproduce the frozen D108 h2-D1 row exponents.
frz = outer_specs(FRZ, 108, 72, 36)
rec["control_frozen_D108_h2D1"] = {"K2_D1_leading_e_exponent": FRZ.k2_d1,
                                   "frozen_recorded": 344, "MATCH": FRZ.k2_d1 == 344}
print(f"CONTROL frozen D108 K2 D1 leading exponent: {FRZ.k2_d1} (recorded 344)")

for name, R, nF, nG in (("frozen_wz6", FRZ, 108, 72), ("source_wz5", SRC, 108, 72)):
    sp_ = outer_specs(R, nF, nG, 36)
    counts = {}
    for b, s in sp_.items():
        allpos = [(r, q) for r in range(s["degree"] + 1)
                  for q in range(min(35, s["degree"] - r) + 1)]
        kept = [p for p in allpos if R.W(*p) >= s["W0"]]
        counts[b] = {"degree": s["degree"], "W0": s["W0"], "threshold": s["threshold"],
                     "ambient": len(allpos), "kept": len(kept),
                     "deleted_by_D2_preblock": len(allpos) - len(kept)}
    rec[f"outer_{name}"] = {"specs": sp_, "counts": counts,
                            "K2_D2_face_weight": R.k2_face, "K2_D1": R.k2_d1}
    print(f"{name}: K2face={R.k2_face} K2_D1={R.k2_d1}")
    for b, cdat in counts.items():
        print(f"   {b}: deg={cdat['degree']:3d} W0={cdat['W0']:3d} thr={cdat['threshold']:3d} "
              f"ambient={cdat['ambient']:5d} kept={cdat['kept']:5d} "
              f"deleted={cdat['deleted_by_D2_preblock']:5d}")

# --- corrected major h2 + D1 block, jet0 pinned (frozen convention) and free.
for jet0free in (False, True):
    t0 = time.monotonic()
    rows, hvars, h3 = minor_incidence(SRC, 35, jet0free)
    resid, subs, piv, zeros = qstar_reduce(rows, hvars)
    assert not resid, resid
    h3r = {k: substitute_map(v, subs) for k, v in h3.items()}
    h3r = {k: v for k, v in h3r.items() if v != 0}
    k2, free, meta = build_major_h2(SRC, h3r, 36, jet0free)
    tag = f"major_src_jet0{'free' if jet0free else 'pinned'}"
    hfree = [str(v) for v in hvars if v not in subs]
    meta.update({"h3_stage0_pivots": len(piv), "h3_free": hfree,
                 "minor_free": (["jet0"] if jet0free else []) + ["jet1", "jet2", "c"],
                 "K2c_free_count": len(free),
                 "inner_free_total": len(free) + len(hfree) + 3 + int(jet0free),
                 "seconds": round(time.monotonic() - t0, 1)})
    rec[tag] = meta
    print(f"{tag}: K2c={meta['K2c_count']} D1rows={meta['h2_D1_raw_rows']} "
          f"weights={meta['h2_D1_weights']} pivots={meta['h2_D1_pivots']} "
          f"resid={len(meta['h2_D1_residual'])} K2c_free={len(free)} "
          f"h3_free={hfree} inner={meta['inner_free_total']} ({meta['seconds']}s)")

(OUT / "step2-major.json").write_text(json.dumps(rec, indent=2, default=str) + "\n")
