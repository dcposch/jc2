#!/usr/bin/env python3
"""CONTROL A: the max_t=T truncation is an exact identity.

Rebuild the charged saturated T=8 row set with build_major_h2(max_t=T) instead
of the frozen max_t=40 and compare rows_sha256 with the charged certificate."""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deep_engine import build_state, rows_upto, rows_hash, singular_check, OUT

EXPECT = "68201f86f8103fad3ad5b8dbe5b36a8d35a4a81ce85338a6957beb1dc5bfcc6d"
t0 = time.monotonic()
st = build_state(8, locus=False)
rows, counts = rows_upto(st, 8)
h = rows_hash(rows)
rec = {"control": "max_t=T truncation identity", "T": 8, "rows": len(rows),
       "row_counts": counts, "rows_sha256": h, "charged_rows_sha256": EXPECT,
       "MATCH": h == EXPECT, "build_seconds": st["build_seconds"],
       "wall_seconds": round(time.monotonic() - t0, 1)}
print(json.dumps(rec, indent=2), flush=True)
(OUT / "ctl-replay-T8.json").write_text(json.dumps(rec, indent=2) + "\n")
