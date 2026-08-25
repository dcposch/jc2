#!/usr/bin/env python3
"""Omit terminal high rows; require and source-replay a predecessor SAT hit."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

import z3

ROOT = Path(os.environ["JC2_ROOT"])
PRODUCER = (ROOT / "cases/as_fonly_d7_global_chart_qfbv_20260825"
            / "solve_global_chart.py")
EXPECTED_PRODUCER_SHA = (
    "d4d4c17dcab32088ef0e76f618cb4fee08fd7ce3cdf44db1ea16b0226dffc3ad")
payload = PRODUCER.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PRODUCER_SHA
source = payload.decode()
marker = "\nfor degree in range(9, 13):\n"
assert source.count(marker) == 1
scope = {"__file__": str(PRODUCER), "__name__": "__preterminal_control__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(PRODUCER), "exec"), scope)

solver = scope["solver"]
smt2 = solver.to_smt2().encode()
Path(os.environ["SMT2_OUTPUT"]).write_bytes(smt2)
check = solver.check()
assert check == z3.sat
model = solver.model()
tvars, yvars, uvars = scope["tvars"], scope["yvars"], scope["uvars"]
restoration = scope["restoration"]
tvalues = [model.eval(variable, model_completion=True).as_long()
           for variable in tvars]
yvalues = [model.eval(variable, model_completion=True).as_long()
           for variable in yvars]
uvalues = [model.eval(variable, model_completion=True).as_long()
           for variable in uvars]
rvalues = [model.eval(value, model_completion=True).as_long()
           for value in restoration]
assert all(0 <= value <= 2 for value in tvalues + yvalues + uvalues + rvalues)
forced, free_q9 = scope["forced"], scope["free_q9"]
full_t = [forced.get(index, 0) for index in range(19)]
for chart_index, kernel_index in enumerate(free_q9):
    full_t[kernel_index] = tvalues[chart_index]
xvalues = scope["add_vector"](
    scope["q9_origin"], scope["q9_kernel"], full_t, reduce=True)
assert scope["source_rows"](scope["source_data"], xvalues) == [0] * 23
assert scope["transition_rows_numeric"](xvalues, yvalues) == [0] * 22
scope["parent_scope"]["xvalues"] = xvalues
scope["parent_scope"]["yvalues"] = yvalues
assert scope["q7_rows_numeric"](rvalues) == [0] * 19
_C, _D, _W, _Z, recursive = scope["recursive_high_numeric"](rvalues)
high = [value for degree in range(12, 8, -1)
        for value in recursive[degree]]
assert any(high), "full formula would otherwise have a SAT witness"
result = {
    "solver_status": "sat",
    "z3_version": z3.get_version_string(),
    "tvalues": tvalues,
    "xvalues": list(xvalues),
    "yvalues": yvalues,
    "uvalues": uvalues,
    "rvalues": rvalues,
    "q9_source_replay": "PASS",
    "q8_source_replay": "PASS",
    "q7_source_replay": "PASS",
    "terminal_high_nonzero_control": high,
    "smt2_sha256": hashlib.sha256(smt2).hexdigest(),
    "scope": "full 13-trit chart with terminal high rows omitted",
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("solver_status sat")
print("q9_q8_q7_source_replay PASS")
print("terminal_high_nonzero_count", sum(bool(value) for value in high))
print("smt2_sha256", result["smt2_sha256"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-GLOBAL-CHART-PRETERMINAL-CONTROL")

