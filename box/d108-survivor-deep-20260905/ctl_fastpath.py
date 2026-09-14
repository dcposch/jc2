#!/usr/bin/env python3
"""CONTROL D: the sparse-ring fast path reproduces the charged saturated-T8
row set BYTE FOR BYTE (same rows_sha256 as box/d108-rekill-20260905)."""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deep_engine import build_state, rows_upto, rows_hash, OUT
EXPECT = "68201f86f8103fad3ad5b8dbe5b36a8d35a4a81ce85338a6957beb1dc5bfcc6d"
def log(*a): print(*a, flush=True)
t0 = time.monotonic()
st = build_state(8, locus=False, offsets=7, log=log, fast=True)
rows, counts = rows_upto(st, 8, jmax=8, log=log)
h = rows_hash(rows)
rec = {"control": "sparse-ring fast path == charged saturated T=8 rows",
       "T": 8, "rows": len(rows), "row_counts": counts, "rows_sha256": h,
       "charged_rows_sha256": EXPECT, "MATCH": h == EXPECT,
       "build_seconds": st["build_seconds"],
       "sympy_Expr_path_build_seconds": 45.2,
       "wall_seconds": round(time.monotonic() - t0, 1)}
(OUT / "ctl-fastpath.json").write_text(json.dumps(rec, indent=2) + "\n")
print(json.dumps(rec, indent=2), flush=True)
