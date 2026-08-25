#!/usr/bin/env python3
"""Solve one pinned emitted Kuranishi QF_BV formula with Z3."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import resource
import time
from pathlib import Path

import z3


assert platform.system() == "Linux", "AWS-only solver refuses non-Linux"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_kuranishi_solver_"), job_tag
formula_path = Path(os.environ["SMT_INPUT"])
expected_formula = os.environ["EXPECTED_SMT_SHA256"]
assert hashlib.sha256(formula_path.read_bytes()).hexdigest() == expected_formula
expected_version = os.environ.get("EXPECTED_Z3_VERSION")
if expected_version:
    assert z3.get_version_string() == expected_version

solver = z3.Solver()
if os.environ.get("Z3_RANDOM_SEED"):
    solver.set(random_seed=int(os.environ["Z3_RANDOM_SEED"]))
solver.from_file(str(formula_path))
start = time.monotonic()
status = solver.check()
elapsed = time.monotonic() - start
model_text = None
if status == z3.sat:
    model_text = solver.model().sexpr()
    Path(os.environ["MODEL_OUTPUT"]).write_text(model_text + "\n")
result = {
    "status": str(status),
    "aws_job_tag": job_tag,
    "formula_sha256": expected_formula,
    "z3_version": z3.get_version_string(),
    "random_seed": (None if not os.environ.get("Z3_RANDOM_SEED")
                    else int(os.environ["Z3_RANDOM_SEED"])),
    "elapsed_seconds": elapsed,
    "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    "model_sha256": (None if model_text is None else hashlib.sha256(
        (model_text + "\n").encode()).hexdigest()),
    "scope": "solver endpoint for one pinned emitted formula",
    "refusal_scope": [
        "SAT requires original-integer source replay",
        "UNSAT requires proof production or independent exact certificate",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["RESULT_OUTPUT"]).write_bytes(encoded)
print("solver_status", status)
print("elapsed_seconds", elapsed)
print("max_rss_kib", result["max_rss_kib"])
print("model_sha256", result["model_sha256"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
