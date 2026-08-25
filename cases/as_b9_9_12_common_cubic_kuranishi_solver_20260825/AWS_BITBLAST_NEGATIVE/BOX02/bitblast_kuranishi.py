#!/usr/bin/env python3
"""Deterministically bit-blast the pinned full Kuranishi formula."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import resource
import time
from pathlib import Path

import z3


assert platform.system() == "Linux", "AWS-only bit-blaster refuses non-Linux"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_kuranishi_bitblast_"), job_tag
source = Path(os.environ["INPUT_SMT2"])
expected = os.environ["EXPECTED_SMT2_SHA256"]
payload = source.read_bytes()
assert hashlib.sha256(payload).hexdigest() == expected
assert z3.get_version_string() == os.environ.get("EXPECTED_Z3_VERSION", "4.16.0")

start = time.monotonic()
parsed = z3.parse_smt2_file(str(source))
goal = z3.Goal()
goal.add(*parsed)
pipeline_names = ["simplify", "bit-blast", "tseitin-cnf"]
answer = z3.Then(*pipeline_names)(goal)
assert len(answer) == 1
dimacs = (answer[0].dimacs() + "\n").encode()
Path(os.environ["OUTPUT_DIMACS"]).write_bytes(dimacs)
header = next(line for line in dimacs.decode().splitlines()
              if line.startswith("p cnf "))
_p, _cnf, variable_text, clause_text = header.split()
result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-KURANISHI-BITBLAST",
    "aws_job_tag": job_tag,
    "input_smt2_sha256": expected,
    "z3_version": z3.get_version_string(),
    "pipeline": pipeline_names,
    "dimacs_variables": int(variable_text),
    "dimacs_clauses": int(clause_text),
    "dimacs_sha256": hashlib.sha256(dimacs).hexdigest(),
    "elapsed_seconds": time.monotonic() - start,
    "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    "scope": "trusted Z3 bit-blast of one pinned formula",
    "refusal_scope": [
        "CNF SAT needs mapped source-model replay",
        "CNF UNSAT needs an independently checked proof",
        "source-to-CNF translation remains part of the compiler audit",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("dimacs_variables_clauses", result["dimacs_variables"],
      result["dimacs_clauses"])
print("dimacs_sha256", result["dimacs_sha256"])
print("elapsed_rss", result["elapsed_seconds"], result["max_rss_kib"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
