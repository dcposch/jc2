#!/usr/bin/env python3
"""Step 7: extend the saturated schedule to local power 9, 10, ... RESTRICTED
to the stage-4/saturated surviving locus V(u,v).

Stage n imposes: the stage-0 common-h3 incidence residual, the two locus
generators, ALL F/G minor pole rows at local powers 1..n, ALL Jacobian bands
at t = 1..n with every w-power, and outer D1 offsets 0..n-1.
Each stage is exact-Q (Q*-only Gauss elimination + Singular std over Q).
"""
import argparse, json, sys, time
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deep_engine import (build_state, rows_upto, rows_hash, singular_check, OUT,
                         U_GEN, V_GEN)
from rekill_engine import symbol, GAUGE_LEDGER

def log(*a):
    print(*a, flush=True)

def witness_on_residual(residual, free, subs):
    """The section-6 rational point, expressed in the locus chart.

    Section 6 sets jet1 = jet2 = c = 1, K2c_3_26 = -8, K2c_4_25 = 20, every
    other free unknown 0.  On the locus K2c_3_26 = -8*jet2 = -8 and
    K2c_4_25 = K2c_4_26 + 20*jet1^2 = 20 are RESOLVED, so in the locus chart
    the same point is "all free unknowns 0 except jet1 = jet2 = c = 1"."""
    point = {v: sp.Integer(0) for v in sorted(free, key=str)}
    for nm in ("jet1", "jet2", "c"):
        point[symbol(nm)] = sp.Integer(1)
    bad = []
    for l, v in residual:
        img = sp.expand(sp.expand(v).subs(point))
        if img != 0: bad.append((l, str(img)[:200]))
    return point, bad

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--T", type=int, default=12)
    ap.add_argument("--start", type=int, default=8)
    ap.add_argument("--tag", default=None)
    ap.add_argument("--jet0free", action="store_true")
    ap.add_argument("--nolocus", action="store_true")
    a = ap.parse_args()
    tag = a.tag or f"deep_T{a.T}"
    t0 = time.monotonic()
    log(f"=== build_state T={a.T} locus={not a.nolocus} offsets=0..{a.T-1} ===")
    st = build_state(a.T, jet0free=a.jet0free, offsets=a.T - 1,
                     locus=not a.nolocus, log=log)
    log(f"build done in {st['build_seconds']}s")
    stages = []
    for n in range(a.start, a.T + 1):
        t1 = time.monotonic()
        rows, counts = rows_upto(st, n, jmax=n, log=log)
        residual, subs, pivots, zeros = qsr(rows, st["free"])
        sing = singular_check(residual, f"{tag}_n{n}")
        point, bad = witness_on_residual(residual, st["free"], subs)
        rec = {"stage_local_power": n, "raw_rows": len(rows), "row_counts": counts,
               "rows_sha256": rows_hash(rows), "free_unknowns": len(st["free"]),
               "Qstar_pivots": len(pivots), "dependent_zero_rows": zeros,
               "residual_row_count": len(residual),
               "residual": {l: str(v) for l, v in residual},
               "residual_factored": {l: str(sp.factor(v)) for l, v in residual},
               "residual_variables": sorted({str(s) for _l, v in residual
                                             for s in v.free_symbols}),
               "singular": sing,
               "sec6_point_survives_residual": not bad,
               "sec6_point_failures": bad,
               "wall_seconds": round(time.monotonic() - t1, 1)}
        stages.append(rec)
        log(f"[n={n}] rows={len(rows)} piv={len(pivots)} zero={zeros} "
            f"resid={len(residual)} dim={sing.get('dimension')} "
            f"UNIT={sing.get('unit_ideal')} sec6_ok={not bad} "
            f"({rec['wall_seconds']}s)")
        dump(tag, a, st, stages, t0)
        if sing.get("unit_ideal"):
            log("*** UNIT: KILL at local power", n); break
    dump(tag, a, st, stages, t0, final=True)

def qsr(rows, free):
    from rekill_engine import qstar_reduce
    return qstar_reduce(rows, free)

def dump(tag, a, st, stages, t0, final=False):
    R = st["radius"]
    rec = {"tag": tag, "truncation_depth_T": a.T, "start_local_power": a.start,
           "locus_restriction": {
               "generators": {"u": str(U_GEN), "v": str(V_GEN)},
               "licence": "rad(I_sat_T8) = <u,v> exactly (u^2 in I; v^2 = "
                          "(uL+v^2) - u*L in I; I contained in the prime <u,v>), "
                          "so V(I_sat) = V(u,v) as a SET and no point is lost",
               "imposed_as": "two extra ROWS consumed by Q* unit pivots on "
                             "K2c_3_26 and K2c_4_25; no unknown dropped by a floor",
               "active": not a.nolocus},
           "radius": {"z_s_order": R.wz, "weight": f"4*r+{R.wz}*q",
                      "K3_face": R.k3_face, "K2_face": R.k2_face,
                      "K2_D1_leading_e_exponent": R.k2_d1},
           "chart": {"jet0_free": a.jet0free},
           "gauge_ledger": GAUGE_LEDGER,
           "outer": {k: v for k, v in st["outer_meta"].items() if k != "D1_offsets"},
           "outer_D1_offset_pivots": [x["Qstar_pivots"] for x in st["outer_meta"]["D1_offsets"]],
           "k2meta": {k: v for k, v in st["k2meta"].items() if k != "K2_face_sites"},
           "build_seconds": st["build_seconds"],
           "stages": stages, "final": final,
           "wall_seconds": round(time.monotonic() - t0, 1)}
    (OUT / f"{tag}.json").write_text(json.dumps(rec, indent=2, default=str) + "\n")

if __name__ == "__main__":
    main()
