#!/usr/bin/env python3
"""Control: the split-face screen's kills do not depend on W.

W is fitted to the charged charts (W=(3n-2*M2)/d_3), not quoted from a printed
line, so its value is the one soft input of the screen.  With t = W-k one has
t = (delta-1)/(v-u*delta), independent of W; the low branch nu=k*lam is
equivalent to t*lam integral; and W cancels from the counting bound.  This
control reruns the local-exponent test at every W in a wide range and checks
that no verdict moves.
"""
from __future__ import annotations
import importlib.util, json
from fractions import Fraction as F
from pathlib import Path

HERE = Path("/home/ubuntu/jc2/box/g9966n1b3-20260903")
spec = importlib.util.spec_from_file_location("fs", HERE / "face_screen.py")
fs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fs)

ROWS = {"S1": (2, 9), "S2": (4, 7), "S3": (4, 7), "S4": (3, 8), "S7": (4, 7), "S8": (3, 8)}
WRANGE = range(5, 60)
tested = disagreements = 0
detail = []
for name, (u, v) in ROWS.items():
    for delta in fs.detector_orders(u, v):
        X = F(u) * delta - F(v)
        for part in fs.partitions(u):
            if len(part) < 2:
                continue
            verdicts = set()
            for W in WRANGE:
                a = F(W) * X - 1 + delta
                k = a / X
                t = F(W) - k
                verdicts.add(bool(fs.local_exponent_ok(part, k, t, W, u)))
            tested += 1
            if len(verdicts) > 1:
                disagreements += 1
                detail.append({"row": name, "delta": str(delta), "partition": list(part)})
payload = {"schema": "jc2.g9966n1b3.w-independence/v1",
           "W_range": [WRANGE.start, WRANGE.stop - 1],
           "pairs_tested": tested, "W_dependent_verdicts": disagreements,
           "disagreements": detail,
           "status": "PASS" if disagreements == 0 else "FAIL",
           "identity": "t=(delta-1)/(v-u*delta); k*lam integral iff t*lam integral; "
                       "W cancels from #H <= t*a_L+1"}
(HERE / "w-independence.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps(payload, indent=1))
