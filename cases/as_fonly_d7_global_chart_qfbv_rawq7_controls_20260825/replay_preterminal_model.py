#!/usr/bin/env python3
"""Replay a raw-Q7 predecessor SAT model through the integer compiler."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_q8state_next_high_samples_20260825"
          / "compile_state.py")
EXPECTED_PARENT_SHA = (
    "abfd5cfa79edb87e16e2df706f7466dcf335302d889cb71bf06bcdfb9609588e")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()
family_marker = '\nfamily = os.environ["STATE_FAMILY"]\n'
restored_marker = "\ndef restored(values):\n"
result_marker = '\nresult = {"family": family, "sample_index": sample_index,\n'
scope = {"__file__": str(PARENT), "__name__": "__raw_model_replay__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(family_marker, 1)[0], str(PARENT), "exec"), scope)
fragment = (restored_marker
            + source.split(restored_marker, 1)[1].split(result_marker, 1)[0])
exec(compile(fragment, str(PARENT), "exec"), scope)

model_path = Path(os.environ["MODEL_FILE"])
expected_model_sha = os.environ["EXPECTED_MODEL_SHA256"]
assert hashlib.sha256(model_path.read_bytes()).hexdigest() == expected_model_sha
lines = model_path.read_text().splitlines()
sat_index = lines.index("sat")
model = {}
for line in lines[sat_index + 1:]:
    fields = line.split()
    if len(fields) == 2 and set(fields[1]) <= {"0", "1"}:
        model[fields[0]] = int(fields[1], 2)
tvalues = [model[f"t{index}"] for index in range(13)]
yvalues = [model[f"y{index}"] for index in range(32)]
rvalues = [model[f"r{index}"] for index in range(18)]
assert all(0 <= value <= 2 for value in tvalues + yvalues + rvalues)
forced = {10: 0, 11: 0, 12: 0, 13: 0, 15: 0, 17: 1}
free_q9 = tuple(index for index in range(19) if index not in forced)
full_t = [forced.get(index, 0) for index in range(19)]
for chart_index, kernel_index in enumerate(free_q9):
    full_t[kernel_index] = tvalues[chart_index]
xvalues = scope["add_vector"](
    scope["q9_origin"], scope["q9_kernel"], full_t, reduce=True)
assert scope["source_rows"](scope["source_data"], xvalues) == [0] * 23
assert scope["transition_rows"](xvalues, yvalues) == [0] * 22
scope["xvalues"] = xvalues
scope["yvalues"] = yvalues
assert scope["q7_rows"](rvalues) == [0] * 19
Cn, Dn, Wn, Zn, recursive = scope["recursive_high"](rvalues)
direct = scope["direct_high"](Cn, Dn, Wn, Zn)
assert recursive == direct
high = [value for degree in range(12, 8, -1)
        for value in recursive[degree]]
assert any(high)
result = {
    "model_file_sha256": expected_model_sha,
    "tvalues": tvalues,
    "xvalues": list(xvalues),
    "yvalues": yvalues,
    "rvalues": rvalues,
    "q9_source_replay": "PASS",
    "q8_source_replay": "PASS",
    "q7_source_replay": "PASS",
    "recursive_literal_div243_agreement": "PASS",
    "terminal_high_nonzero_control": high,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("q9_q8_q7_source_replay PASS")
print("recursive_literal_div243_agreement PASS")
print("terminal_high_nonzero_count", sum(bool(value) for value in high))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-GLOBAL-RAWQ7-PRETERMINAL-REPLAY")

