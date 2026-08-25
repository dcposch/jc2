#!/usr/bin/env python3
"""Deterministically bit-blast the pinned global SMT2 to DIMACS."""
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
parsed = z3.parse_smt2_file(str(source))
goal = z3.Goal()
goal.add(*parsed)
pipeline = z3.Then("simplify", "bit-blast", "tseitin-cnf")
answer = pipeline(goal)
assert len(answer) == 1
dimacs = (answer[0].dimacs() + "\n").encode()
output = Path(os.environ["OUTPUT_DIMACS"])
output.write_bytes(dimacs)
header = next(line for line in dimacs.decode().splitlines()
              if line.startswith("p cnf "))
_p, _cnf, variable_text, clause_text = header.split()
result = {
    "input_smt2_sha256": expected,
    "z3_version": z3.get_version_string(),
    "pipeline": ["simplify", "bit-blast", "tseitin-cnf"],
    "dimacs_variables": int(variable_text),
    "dimacs_clauses": int(clause_text),
    "dimacs_sha256": hashlib.sha256(dimacs).hexdigest(),
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("z3_version", result["z3_version"])
print("dimacs_variables", result["dimacs_variables"])
print("dimacs_clauses", result["dimacs_clauses"])
print("dimacs_sha256", result["dimacs_sha256"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-GLOBAL-CHART-BITBLAST")
