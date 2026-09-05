#!/usr/bin/env python3
"""Step 4: SATURATED joint system at the corrected radius.

Instead of the frozen staged schedule this imposes, at one truncation depth T,
EVERY necessary row the chart can express:
  * all F and G minor pole rows at local powers 1..T  (stages 0..T-4),
  * all Jacobian bands at t-powers 1..T, all w-powers (beyond stage T),
  * all outer D1 offsets 0..7.
Adding rows can only shrink the locus, so a survivor here is a strictly
stronger survival statement than a survivor of the staged schedule.
"""
import argparse, json, sys, time
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rekill_engine import (SRC, FRZ, minor_incidence, qstar_reduce, symbol,
                           build_major_h2, substitute_map, outer_state, build_FG,
                           jacobian_band, local_rows, raw_minor_support, pole_coeff,
                           GAUGE_LEDGER)
from step3_joint import singular_check, rows_hash

OUT = Path(__file__).resolve().parent


def run(T, jet0free, radius=SRC, offsets=7, tag=None):
    t0 = time.monotonic()
    tag = tag or f"sat_wz{radius.wz}_jet0{'free' if jet0free else 'pinned'}_T{T}"
    rows0, hvars, h3 = minor_incidence(radius, radius.k3_face, jet0free)
    resid0, subs0, piv0, _ = qstar_reduce(rows0, hvars)
    h3r = {k: v for k, v in ((k, substitute_map(v, subs0)) for k, v in h3.items()) if v != 0}
    k2, k2free, k2meta = build_major_h2(radius, h3r, 40, jet0free)
    outer, outer_free, outer_meta = outer_state(radius, offsets)
    KF, KG = build_FG(k2, outer, T)
    f_local = local_rows(KF, T, jet0free)
    g_local = local_rows(KG, T, jet0free)
    rows, counts = [], {"F": 0, "G": 0, "J": 0}
    # The stage-0 common-h3 incidence residual is a necessary row set at
    # every stage; it is empty at the corrected radius and is the frozen kill
    # at the frozen radius, so it must be carried explicitly.
    rows += [(f"h3_incidence_{l}", v) for l, v in resid0]

    for name, table in (("F", f_local), ("G", g_local)):
        for n in range(1, T + 1):
            for k in raw_minor_support(name, jet0free).get(n, ()):
                rows.append((f"{name}_local{n}_coord{k}", pole_coeff(table, n, k, name)))
                counts[name] += 1
    for tp in range(1, T + 1):
        J = jacobian_band(KF, KG, tp)
        for k in range(179 - tp):
            rows.append((f"J_t{tp}_d{178-tp}_k{k}", J.get(k, sp.Integer(0))))
            counts["J"] += 1
    free = set(k2free) | set(outer_free) | {v for v in hvars if v not in subs0}
    residual, subs, pivots, zeros = qstar_reduce(rows, free)
    sing = singular_check(residual, tag)
    rec = {"tag": tag, "truncation_depth_T": T,
           "radius": {"z_s_order": radius.wz, "weight": f"4*r+{radius.wz}*q",
                      "K3_face": radius.k3_face, "K2_face": radius.k2_face,
                      "K2_D1_leading_e_exponent": radius.k2_d1},
           "chart": {"h3_cutoff": radius.k3_face, "jet0_free": jet0free,
                     "h3_free": [str(v) for v in hvars if v not in subs0],
                     "minor_free": (["jet0"] if jet0free else []) + ["jet1", "jet2", "c"]},
           "gauge_ledger": GAUGE_LEDGER,
           "outer_D1_offsets_imposed": offsets,
           "outer": {k: v for k, v in outer_meta.items() if k != "D1_offsets"},
           "outer_D1_offset_pivots": [x["Qstar_pivots"] for x in outer_meta["D1_offsets"]],
           "row_counts": counts, "raw_row_count": len(rows),
           "rows_sha256": rows_hash(rows), "free_unknowns": len(free),
           "Qstar_pivots": len(pivots), "dependent_zero_rows": zeros,
           "pivot_ledger": [{"row": p.label, "var": str(p.variable),
                             "coeff": str(p.coefficient)} for p in pivots],
           "residual_row_count": len(residual),
           "residual": {l: str(v) for l, v in residual},
           "residual_variables": sorted({str(s) for _l, v in residual for s in v.free_symbols}),
           "singular": sing, "wall_seconds": round(time.monotonic() - t0, 1)}
    (OUT / f"{tag}.json").write_text(json.dumps(rec, indent=2, default=str) + "\n")
    print(f"{tag}: rows={len(rows)} free={len(free)} piv={len(pivots)} zero={zeros} "
          f"resid={len(residual)} dim={sing.get('dimension')} UNIT={sing.get('unit_ideal')} "
          f"({rec['wall_seconds']}s)", flush=True)
    return rec


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--T", type=int, default=8)
    ap.add_argument("--jet0free", action="store_true")
    ap.add_argument("--frozen-radius", action="store_true")
    ap.add_argument("--offsets", type=int, default=7)
    a = ap.parse_args()
    run(a.T, a.jet0free, FRZ if a.frozen_radius else SRC, a.offsets)
