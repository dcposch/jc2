#!/usr/bin/env python3
"""Reimpose the final Q8 source row after the Q7 restoration; AWS only."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT_REPLAY = (ROOT / "cases/as_fonly_d7_global_predecessor_rawq7_20260825"
                 / "replay_model.py")
EXPECTED_PARENT_SHA = (
    "b4acf93af94774e124502f3b6cd20be40b10197a808eb7b8ad0d7c92395b99d4")
payload = PARENT_REPLAY.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()
marker = '\nmodel_path = Path(os.environ["MODEL_OUTPUT"])\n'
assert source.count(marker) == 1
scope = {"__file__": str(PARENT_REPLAY), "__name__": "__final_g8_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(PARENT_REPLAY), "exec"), scope)

predecessor_names = tuple(scope["predecessor_names"])
canonical_source = scope["canonical_source"]
source_rows = scope["source_rows"]
transition_rows = scope["transition_rows"]
q7_rows = scope["q7_rows"]
state_polynomials = scope["state_polynomials"]
recursive_high = scope["recursive_high"]
direct_high = scope["direct_high"]
core_intermediates = scope["core_intermediates"]
nadd = scope["nadd"]
nderivative = scope["nderivative"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
row = scope["row"]

survivor_path = Path(os.environ["SURVIVOR_JSON"])
survivor = json.loads(survivor_path.read_text())
assignment = dict(zip(predecessor_names, survivor["predecessor_values"]))
source_data = canonical_source(assignment)
xvalues = survivor["q9_values"]
yvalues = survivor["q8_values"]
rvalues = survivor["q7_values"]
q9 = source_rows(source_data, xvalues)
q8_before_q7 = transition_rows(source_data, xvalues, yvalues)
q7 = q7_rows(source_data, xvalues, yvalues, rvalues)
assert q9 == [0] * 23
assert q8_before_q7 == [0] * 22
assert q7 == [0] * 19
C, D, W, Z = state_polynomials(source_data, xvalues, yvalues, rvalues)
E, M, N, T, _Rmix = core_intermediates(source_data, C, D, W, Z)
divWZ = nadd(nderivative(W, 0), nderivative(Z, 1))


def G(degree):
    E1 = divide_exact(degree_part(E, degree), 3)
    F = nadd(E1, degree_part(M, degree), degree_part(divWZ, degree))
    F1 = divide_exact(F, 3)
    return nadd(F1, degree_part(N, degree), degree_part(T, degree))


G8 = G(8)
G7 = G(7)
final_g8 = row(G8, 8)
final_g7 = row(G7, 7)
_C, _D, _W, _Z, terminal = recursive_high(
    source_data, xvalues, yvalues, rvalues)
assert terminal == direct_high(source_data, C, D, W, Z)
terminal_flat = [value for degree in range(12, 8, -1)
                 for value in terminal[degree]]
assert not any(terminal_flat)

result = {
    "status": "PASS-FINAL-G8-SOURCE-AUDIT",
    "survivor_json_sha256": hashlib.sha256(survivor_path.read_bytes()).hexdigest(),
    "q8_rows_before_q7": q8_before_q7,
    "q7_rows": q7,
    "final_reimposed_G8_rows": final_g8,
    "final_reimposed_G8_nonzero_indices": [index for index, value in enumerate(final_g8)
                                             if value],
    "final_G7_rows": final_g7,
    "terminal_R12_to_R9": terminal_flat,
    "final_G8_pass": not any(final_g8),
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("final_reimposed_G8_rows", final_g8)
print("final_reimposed_G8_nonzero_indices",
      result["final_reimposed_G8_nonzero_indices"])
print("final_G7_rows", final_g7)
print("terminal_R12_to_R9_nonzero", [i for i, value in enumerate(terminal_flat)
                                      if value])
print("final_G8_pass", result["final_G8_pass"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-SAT-SURVIVOR-FINAL-G8-AUDIT")
