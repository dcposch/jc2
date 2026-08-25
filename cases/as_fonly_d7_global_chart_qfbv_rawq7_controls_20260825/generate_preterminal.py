#!/usr/bin/env python3
"""Generate the raw-Q7 predecessor formula with terminal high rows omitted."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

ROOT = Path(os.environ["JC2_ROOT"])
PRODUCER = (ROOT / "cases/as_fonly_d7_global_chart_qfbv_rawq7_20260825"
            / "solve_global_rawq7.py")
EXPECTED_PRODUCER_SHA = (
    "69b908545775f4df1e10884c867cb767b8d1e997be33e386a730a2eaed585988")
payload = PRODUCER.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PRODUCER_SHA
source = payload.decode()
marker = "\nfor degree in range(9, 13):\n"
assert source.count(marker) == 1
scope = {"__file__": str(PRODUCER), "__name__": "__raw_preterminal__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(PRODUCER), "exec"), scope)
smt2 = scope["solver"].to_smt2().encode()
Path(os.environ["SMT2_OUTPUT"]).write_bytes(smt2)
result = {
    "smt2_sha256": hashlib.sha256(smt2).hexdigest(),
    "q9_chart_dimension": 13,
    "q8_raw_variable_count": 32,
    "q7_raw_variable_count": 18,
    "explicit_source_rows": [23, 22, 19],
    "terminal_rows_omitted": True,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("smt2_sha256", result["smt2_sha256"])
print("explicit_source_rows", result["explicit_source_rows"])
print("PASS-AS-GLOBAL-RAWQ7-PRETERMINAL-GENERATOR")

