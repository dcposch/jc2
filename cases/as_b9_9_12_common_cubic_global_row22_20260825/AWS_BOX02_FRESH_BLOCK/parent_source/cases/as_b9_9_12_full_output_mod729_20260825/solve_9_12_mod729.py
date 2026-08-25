#!/usr/bin/env python3
"""Complete normalized (9,12) fresh-output gate over the fixed B9 parent."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_b9_max12_full_output_mod729_20260825"
          / "solve_full_output_mod729.py")
EXPECTED_PARENT = (
    "4deb7fe07acef4f37bb14735493b0d20b6c7ac66bb10633f81b7bc1a48264bd4")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT
saved_output = os.environ["OUTPUT_JSON"]
os.environ["OUTPUT_JSON"] = os.environ["PARENT_REPLAY_JSON"]
ns = {"__file__": str(PARENT), "__name__": "__b9_full_d12_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(PARENT), "exec"), ns)
os.environ["OUTPUT_JSON"] = saved_output

support = list(ns["support"])
slots = list(ns["slots"])
matrix_full = [list(row) for row in ns["matrix"]]
rhs = [(-value) % 3 for value in ns["base"]]
rref_with_left = ns["rref_with_left"]
candidate = ns["candidate"]
add, sc, jac, modp = ns["add"], ns["sc"], ns["jac"], ns["modp"]
ONE = ns["ONE"]
coefficient = ns["coefficient"]
tdeg, dydeg = ns["tdeg"], ns["dydeg"]

allowed = ([index for index, xy in enumerate(support) if sum(xy) <= 9]
           + [91 + index for index, xy in enumerate(support)
              if sum(xy) <= 12])
assert len(allowed) == 55 + 91 == 146
matrix = [[row[index] for index in allowed] for row in matrix_full]
rank, particular, kernel, contradictions = rref_with_left(matrix, rhs)

result = {
    "status": ("PASS-AS-B9-9-12-FULL-OUTPUT-MOD729-SAT"
               if particular is not None
               else "PASS-AS-B9-9-12-FULL-OUTPUT-MOD729-UNSAT"),
    "parent_source_sha256": EXPECTED_PARENT,
    "parent_replay_sha256": hashlib.sha256(
        Path(os.environ["PARENT_REPLAY_JSON"]).read_bytes()).hexdigest(),
    "slot_count": 276,
    "variable_count": 146,
    "P_variable_count": 55,
    "Q_variable_count": 91,
    "rank": rank,
    "consistent": particular is not None,
    "kernel_dimension": len(kernel) if particular is not None else None,
    "matrix_sha256": hashlib.sha256(json.dumps(
        matrix, separators=(",", ":")).encode()).hexdigest(),
    "rhs_sha256": hashlib.sha256(json.dumps(
        rhs, separators=(",", ":")).encode()).hexdigest(),
    "scope": "complete (P<=9,Q<=12) fresh digit over one B9 mod243 point",
    "refusal_scope": [
        "not the complete earlier mod243 fibre",
        "no modulus2187 or deeper/all-depth branch",
        "no characteristic-zero point, maximum12 theorem, counterexample, or JC2",
    ],
}

if particular is not None:
    full = [0] * 182
    for index, value in zip(allowed, particular):
        full[index] = value
    P, Q = candidate(full)
    determinant = add(jac(P, Q), sc(-1, ONE))
    assert all(coefficient(determinant, xy) % 729 == 0 for xy in slots)
    assert modp(P, 3) == modp(ns["p5"], 3)
    assert modp(Q, 3) == modp(ns["q5"], 3)
    assert tdeg(P) <= 9 and dydeg(P) <= 9
    assert tdeg(Q) <= 12 and dydeg(Q) <= 12
    result.update({
        "fresh_digit_restricted": particular,
        "fresh_digit_full": full,
        "literal_integer_replay_mod729_passed": True,
        "degrees_total": [tdeg(P), tdeg(Q)],
        "degrees_y": [dydeg(P), dydeg(Q)],
        "determinant_sha256": hashlib.sha256(
            repr(sorted(jac(P, Q).items())).encode()).hexdigest(),
    })
else:
    witness = contradictions[0]
    assert all(sum(witness[row] * matrix[row][column]
                   for row in range(276)) % 3 == 0
               for column in range(146))
    assert sum(witness[row] * rhs[row] for row in range(276)) % 3 == 1
    result.update({
        "left_null_witness": witness,
        "left_null_support": [[slots[index][0], slots[index][1], value]
                              for index, value in enumerate(witness) if value],
        "left_null_pairing": 1,
    })

encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
Path(saved_output).write_bytes(encoded + b"\n")
print("rows_columns", 276, 146)
print("rank", rank)
print("consistent", particular is not None)
print("kernel_dimension", result["kernel_dimension"])
print("matrix_sha256", result["matrix_sha256"])
print("result_sha256", hashlib.sha256(encoded + b"\n").hexdigest())
print(result["status"])
