#!/usr/bin/env python3
"""Stop V6 after classifying charged assertions and print exact counts."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
V6 = (ROOT / "cases/as_fonly_d7_global_q5_q4_cartier_fitting_v5_symbolic_20260825"
      / "analyze_cartier_fitting_v6.py")
EXPECTED = "f6c72654ff2be0f1dfdc78179f987c58f37c8ef469d0ce221c7f81e052956f01"
payload = V6.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
source = payload.decode()
old = "assert len(restoration_high_zero) == 30, len(restoration_high_zero)"
new = '''print("V6-COUNTS", len(independent_assertions),
      len(restoration_bounds), len(restoration_high_zero),
      len(row_assertions))
print("V6-HIGH-ZERO-SAMPLE", [item.sexpr() for item in
      restoration_high_zero[:2]])
raise SystemExit(0)'''
assert source.count(old) == 1
source = source.replace(old, new)
scope = {"__file__": str(V6), "__name__": "__diagnose_v6_counts__"}
exec(compile(source, str(V6), "exec"), scope)

