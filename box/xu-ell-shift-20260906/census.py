#!/usr/bin/env python3
"""ell-shifted child census on the 46 complete (u_s=1) rows: I'_M AND I'_m."""
from __future__ import annotations
import json, sys, time
from fractions import Fraction as Q
from pathlib import Path
ROOT = Path("/home/ubuntu/jc2"); HERE = ROOT / "box" / "xu-ell-shift-20260906"
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "box" / "exact-contact-20260906"))
sys.dont_write_bytecode = True
from child_row_close import close_row                      # noqa: E402
from exact_contact import tower, all_flat                  # noqa: E402
ROSTER = ROOT / "box" / "residual66-20260905" / "roster.jsonl"

DEPTH = int(sys.argv[1]) if len(sys.argv) > 1 else 3
rows = [json.loads(l) for l in open(ROSTER)]
complete = [r for r in rows if r["source"]["u_s"] == 1]
assert len(complete) == 46
out = []
t0 = time.monotonic()
for row in complete:
    rid = row["row_id"]
    T = tower(row["source"])
    par = [(c["IM"], c["Im"]) for c in all_flat(T)]
    par_surv = sorted({str(a) for a, b in par if a.denominator == 1 and a >= b})
    try:
        R = close_row(rid, DEPTH)
        err = None
    except Exception as e:                                   # noqa: BLE001
        R, err = None, f"{type(e).__name__}: {e}"
    rec = dict(row_id=rid, n=T["n"], m=T["m"], parent_surviving=par_surv,
               n_parent_configs=len(par), error=err)
    if R:
        alive = [c for c in R["configs"] if c["verdict"] == "ALIVE"]
        vals = sorted({s[0] for c in alive for s in c["survivors"]},
                      key=lambda x: Q(x))
        margins = sorted({str(Q(s[0]) - Q(s[1])) for c in alive for s in c["survivors"]},
                         key=lambda x: Q(x))
        rec.update(ell=R["ell"], child=R["child"], V_type=R["V_type"],
                   n_child_configs=len(R["configs"]),
                   n_child_alive=len(alive), child_surviving=vals,
                   child_margins=margins, row_verdict=R["row_verdict"],
                   flat=[dict(V=c["V_prime"], IM=c["flat_IM"], Im=c["flat_Im"],
                              sib=c["n_sibling"], verdict=c["verdict"])
                         for c in R["configs"]])
    out.append(rec)
    print(f"{rid:6} ({T['n']},{T['m']})->{tuple(rec.get('child',('?',)))} "
          f"parent{par_surv} child{rec.get('child_surviving')} "
          f"margins{rec.get('child_margins')} {rec.get('row_verdict', err)}")
    sys.stdout.flush()
json.dump(out, open(HERE / "census.json", "w"), indent=0)
print(f"\n[{time.monotonic()-t0:.1f}s] depth={DEPTH}")
dead = [r["row_id"] for r in out if r.get("row_verdict") == "DEAD"]
print("CHILD-DEAD rows:", dead)
print("parent-surviving-empty rows:", [r["row_id"] for r in out if not r["parent_surviving"]])
