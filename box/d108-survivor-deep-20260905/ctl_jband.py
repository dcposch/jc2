#!/usr/bin/env python3
"""CONTROL C: the single-pass Jacobian equals the frozen per-band Jacobian."""
import json, sys, time
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deep_engine import build_state, jacobian_all_bands, OUT
from rekill_engine import jacobian_band

def log(*a): print(*a, flush=True)
T = 5
st = build_state(T, locus=True, offsets=T - 1, log=log)
fast = jacobian_all_bands(st["KF"], st["KG"], T, log=log)
ok, detail = True, {}
for tp in range(0, T + 1):
    slow = jacobian_band(st["KF"], st["KG"], tp) if tp >= 1 else None
    if tp == 0:
        detail["t0_band_nonzero_slots"] = len(fast[0]); continue
    keys = set(fast[tp]) | set(slow)
    diff = [k for k in keys if sp.expand(fast[tp].get(k, 0) - slow.get(k, 0)) != 0]
    detail[f"t{tp}"] = {"slots_fast": len(fast[tp]), "slots_slow": len(slow),
                        "mismatching_w_powers": diff}
    ok = ok and not diff
rec = {"control": "single-pass Jacobian == frozen per-band Jacobian",
       "T": T, "MATCH": ok, "detail": detail}
(OUT / "ctl-jband.json").write_text(json.dumps(rec, indent=2) + "\n")
print(json.dumps(rec, indent=2))
