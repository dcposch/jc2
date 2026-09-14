#!/usr/bin/env python3
"""Step 8: ONE-SHOT deep test at truncation depth T on the surviving locus.

Imposes, in a single exact-Q elimination, every row the chart expresses at
depth T: the stage-0 common-h3 incidence residual, ALL F/G minor pole rows at
local powers 1..T, ALL Jacobian bands at t = 0..T with every w-power (t = 0 is
the degree-178 top band, which the frozen engine asserts is identically zero;
it is imposed here rather than assumed), and outer D1 offsets 0..T-1.

At T >= 27 the A2 and B2 outer blocks become visible in KF/KG for the first
time (their surviving coordinates start at r = 26, and outer_effective_tz
shifts r -> r+1); A3 first appears at T >= 62.
"""
import argparse, json, sys, time
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deep_engine import (build_state, rows_upto, rows_hash, singular_check, OUT,
                         U_GEN, V_GEN)
from rekill_engine import qstar_reduce, symbol, GAUGE_LEDGER


def log(*a): print(*a, flush=True)


def outer_visibility(st):
    """Which outer coordinates are actually reachable at this depth."""
    import rekill_engine as E
    R = st["radius"]
    specs = E.outer_specs(R)
    out = {}
    for block, s in specs.items():
        rs = [r for r in range(s["degree"] + 1)
              for q in range(min(E.D2DEG - 1, s["degree"] - r) + 1)
              if R.W(r, q) >= s["W0"]]
        first_r = min(rs) if rs else None
        out[block] = {"kept_coords": len(rs),
                      "first_r": first_r,
                      "first_visible_t_power": None if first_r is None else first_r + 1,
                      "visible_at_this_T": first_r is not None and first_r + 1 <= st["T"],
                      "coords_visible": sum(1 for r in rs if r + 1 <= st["T"])}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--T", type=int, required=True)
    ap.add_argument("--jT", type=int, default=None)
    ap.add_argument("--tag", default=None)
    ap.add_argument("--jet0free", action="store_true")
    ap.add_argument("--nolocus", action="store_true")
    a = ap.parse_args()
    tag = a.tag or f"deepshot_T{a.T}"
    t0 = time.monotonic()
    log(f"=== one-shot T={a.T} locus={not a.nolocus} offsets=0..{a.T-1} ===")
    st = build_state(a.T, jet0free=a.jet0free, offsets=a.T - 1,
                     locus=not a.nolocus, log=log, jT=a.jT)
    rows, counts = rows_upto(st, a.T, jmax=st["jT"], log=log)
    # the degree-178 top band (t^0) is imposed explicitly, not assumed zero
    j0 = st["_jcache"][0]
    rows += [(f"J_t0_d178_k{k}", j0.get(k, sp.Integer(0))) for k in range(179)]
    counts["J"] += 179
    log(f"rows={len(rows)} (F {counts['F']}, G {counts['G']}, J {counts['J']}); "
        f"reducing ({time.monotonic()-t0:.1f}s elapsed)")
    residual, subs, pivots, zeros = qstar_reduce(rows, st["free"])
    log(f"Q* pivots={len(pivots)} zero={zeros} residual={len(residual)} "
        f"({time.monotonic()-t0:.1f}s)")
    sing = singular_check(residual, tag)
    point = {v: sp.Integer(0) for v in sorted(st["free"], key=str)}
    for nm in ("jet1", "jet2", "c"): point[symbol(nm)] = sp.Integer(1)
    bad = [(l, str(sp.expand(sp.expand(v).subs(point)))[:200])
           for l, v in residual if sp.expand(sp.expand(v).subs(point)) != 0]
    R = st["radius"]
    rec = {"tag": tag, "truncation_depth_T": a.T,
           "jacobian_depth_jT": st["jT"], "mode": "one-shot",
           "locus_restriction": {"u": str(U_GEN), "v": str(V_GEN),
                                 "active": not a.nolocus,
                                 "licence": "rad(I_sat_T8) = <u,v>, verified in "
                                            "Singular (ctl-radical.json)"},
           "radius": {"z_s_order": R.wz, "weight": f"4*r+{R.wz}*q",
                      "K3_face": R.k3_face, "K2_face": R.k2_face,
                      "K2_D1_leading_e_exponent": R.k2_d1},
           "gauge_ledger": GAUGE_LEDGER,
           "outer_visibility": outer_visibility(st),
           "outer": {k: v for k, v in st["outer_meta"].items() if k != "D1_offsets"},
           "outer_D1_offset_pivots": [x["Qstar_pivots"] for x in st["outer_meta"]["D1_offsets"]],
           "J_top_band_t0_nonzero_slots": st["J_top_band_t0_slots"],
           "row_counts": counts, "raw_row_count": len(rows),
           "rows_sha256": rows_hash(rows), "free_unknowns": len(st["free"]),
           "Qstar_pivots": len(pivots), "dependent_zero_rows": zeros,
           "residual_row_count": len(residual),
           "residual": {l: str(v) for l, v in residual},
           "residual_factored": {l: str(sp.factor(v)) for l, v in residual},
           "residual_variables": sorted({str(s) for _l, v in residual
                                         for s in v.free_symbols}),
           "singular": sing,
           "sec6_point_survives_residual": not bad, "sec6_point_failures": bad,
           "build_seconds": st["build_seconds"],
           "wall_seconds": round(time.monotonic() - t0, 1)}
    (OUT / f"{tag}.json").write_text(json.dumps(rec, indent=2, default=str) + "\n")
    log(f"[T={a.T}] rows={len(rows)} piv={len(pivots)} resid={len(residual)} "
        f"dim={sing.get('dimension')} UNIT={sing.get('unit_ideal')} "
        f"sec6_ok={not bad} ({rec['wall_seconds']}s)")


if __name__ == "__main__":
    main()
