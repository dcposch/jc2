#!/usr/bin/env python3
"""Extract and deletion-minimize an assertion core from the pinned SMT2."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import z3


source = Path(os.environ["INPUT_SMT2"])
expected = os.environ["EXPECTED_SMT2_SHA256"]
payload = source.read_bytes()
assert hashlib.sha256(payload).hexdigest() == expected
assertions = list(z3.parse_smt2_file(str(source)))
lines = payload.decode().splitlines()
assert_lines = [(number + 1, line) for number, line in enumerate(lines)
                if line.startswith("(assert ")]
assert len(assert_lines) == len(assertions)

tags = [z3.Bool(f"core_tag_{index}") for index in range(len(assertions))]
solver = z3.Solver()
solver.set(unsat_core=True)
for tag, assertion in zip(tags, assertions):
    solver.add(z3.Implies(tag, assertion))
assert solver.check(*tags) == z3.unsat
core_names = {str(tag) for tag in solver.unsat_core()}
core = [index for index, tag in enumerate(tags) if str(tag) in core_names]

# Deterministic deletion-minimality pass in assertion order.
position = 0
while position < len(core):
    trial = core[:position] + core[position + 1:]
    if solver.check(*[tags[index] for index in trial]) == z3.unsat:
        core = trial
    else:
        position += 1
assert solver.check(*[tags[index] for index in core]) == z3.unsat
for position in range(len(core)):
    trial = core[:position] + core[position + 1:]
    assert solver.check(*[tags[index] for index in trial]) != z3.unsat

core_rows = [{
    "assertion_index": index,
    "line_number": assert_lines[index][0],
    "source_line": assert_lines[index][1],
    "sexpr": assertions[index].sexpr(),
} for index in core]
result = {
    "status": "PASS-AS-B9-9-12-COMMON-CUBIC-DELETION-MINIMAL-CORE",
    "input_sha256": expected,
    "z3_version": z3.get_version_string(),
    "assertion_count": len(assertions),
    "initial_core_count": len(core_names),
    "deletion_minimal_core_count": len(core),
    "core": core_rows,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)

# Keep all declarations, but only the deletion-minimal assertions.
keep = {assert_lines[index][0] for index in core}
reduced_lines = []
for number, line in enumerate(lines, 1):
    if line.startswith("(assert ") and number not in keep:
        continue
    if line in ("(check-sat)", "(get-model)"):
        continue
    reduced_lines.append(line)
reduced_lines.extend(["(check-sat)", ""])
reduced = "\n".join(reduced_lines).encode()
Path(os.environ["OUTPUT_REDUCED_SMT2"]).write_bytes(reduced)
print("assertions_initial_minimal", len(assertions), len(core_names), len(core))
for row in core_rows:
    print("core", row["assertion_index"], row["line_number"],
          row["source_line"][:240])
print("reduced_sha256", hashlib.sha256(reduced).hexdigest())
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
