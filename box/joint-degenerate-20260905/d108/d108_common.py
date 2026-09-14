#!/usr/bin/env python3
"""Shared builder for the D=108 delta=3 corrected chart (imports the frozen
rekill engine read-only).  Builds h3 (after the 12 stage-0 Q* pivots) and the
symbolic K2 = t^36*h2 on the Moh Def 5.1(3) radius (SRC, W=4r+5q).

Ring map (declared): coordinates t = 1/x, w = t*y, z = w - 1.
  K3(t,z) = t^9  * h3(1/t, (1+z)/t)      top z^7 (1+z)^2
  K2(t,z) = t^36 * h2(1/t, (1+z)/t)      top z^28 (1+z)^8
  KF = K2^3 + t*KA2*K2 + t*KA3 ; KG = K2^2 + t*KB1*K2 + t*KB2   (outer blocks)
Minor arc sigma:  w = jet1*t^2 + jet2*t^3 + pi*t^4  (jet0 pinned to 0).
"""
import sys, pickle, time
from pathlib import Path
import sympy as sp
REKILL = Path("/home/ubuntu/jc2/box/d108-rekill-20260905/work")
sys.path.insert(0, str(REKILL))
from rekill_engine import (SRC, minor_incidence, qstar_reduce, symbol, build_major_h2,
                           substitute_map, local_rows, z_to_w)
HERE = Path(__file__).resolve().parent
CACHE = HERE / "k2_cache.pkl"

def build(max_t=36, force=False):
    if CACHE.exists() and not force:
        with CACHE.open("rb") as f:
            return pickle.load(f)
    t0 = time.monotonic()
    rows0, hvars, h3 = minor_incidence(SRC, SRC.k3_face, False)
    resid0, subs0, piv0, _ = qstar_reduce(rows0, hvars)
    assert not resid0, resid0
    h3r = {k: v for k, v in ((k, substitute_map(v, subs0)) for k, v in h3.items()) if v != 0}
    k2, k2free, k2meta = build_major_h2(SRC, h3r, max_t, False)
    obj = {"h3": h3r, "subs0": subs0, "hvars": hvars, "h3free": [v for v in hvars if v not in subs0],
           "k2": k2, "k2free": sorted(k2free, key=str), "k2meta": k2meta,
           "build_seconds": round(time.monotonic() - t0, 1), "max_t": max_t}
    with CACHE.open("wb") as f:
        pickle.dump(obj, f)
    return obj

if __name__ == "__main__":
    o = build(force=True)
    print("built in", o["build_seconds"], "s; K2 slots", len(o["k2"]), "K2c free", len(o["k2free"]),
          "h3 free", o["h3free"], "K2 max r", max(r for r, _ in o["k2"]))
