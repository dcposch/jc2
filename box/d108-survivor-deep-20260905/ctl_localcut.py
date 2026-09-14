#!/usr/bin/env python3
"""CONTROL E: local_rows_fast (sparse ring + the n >= r+2j cut) is identical to
the frozen sympy-Expr local_rows."""
import json, sys, time
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deep_engine import build_state, local_rows_fast, OUT
from rekill_engine import local_rows
def log(*a): print(*a, flush=True)
T = 10
st = build_state(T, locus=True, offsets=T - 1, log=log, jT=1)
res = {}
for nm, K in (("F", st["KF"]), ("G", st["KG"])):
    t0 = time.monotonic(); slow = local_rows(K, T, False); ts = time.monotonic() - t0
    t0 = time.monotonic(); fast = local_rows_fast(K, T, False); tf = time.monotonic() - t0
    keys = set(slow) | set(fast)
    bad = [k for k in keys if sp.expand(slow.get(k, 0) - fast.get(k, 0)) != 0]
    res[nm] = {"slots_slow": len(slow), "slots_fast": len(fast),
               "mismatching_slots": [str(k) for k in bad],
               "seconds_slow": round(ts, 1), "seconds_fast": round(tf, 1)}
rec = {"control": "local_rows_fast(with n>=r+2j cut) == frozen local_rows",
       "T": T, "MATCH": all(not v["mismatching_slots"] for v in res.values()),
       "detail": res}
(OUT / "ctl-localcut.json").write_text(json.dumps(rec, indent=2) + "\n")
print(json.dumps(rec, indent=2), flush=True)
