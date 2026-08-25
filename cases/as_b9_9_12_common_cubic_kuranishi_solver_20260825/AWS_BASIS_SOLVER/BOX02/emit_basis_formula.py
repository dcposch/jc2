#!/usr/bin/env python3
"""Emit the exact 111-coordinate formula certified by structural-span replay."""

from __future__ import annotations

import gzip
import hashlib
import json
import os
import platform
import re
from pathlib import Path


assert platform.system() == "Linux", "AWS-only emitter refuses non-Linux"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_kuranishi_basis_"), job_tag

full_path = Path(os.environ["FULL_SMT"])
certificate_path = Path(os.environ["SPAN_CERTIFICATE_GZIP"])
full_bytes = full_path.read_bytes()
certificate_bytes = gzip.decompress(certificate_path.read_bytes())
assert hashlib.sha256(full_bytes).hexdigest() == (
    "108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c")
assert hashlib.sha256(certificate_path.read_bytes()).hexdigest() == (
    "45b40fd0540e060869a25683c0f5d852a0a24c39e4d04ff17d60af568453d578")
assert hashlib.sha256(certificate_bytes).hexdigest() == (
    "d363cc0c5adbf432d8f3d5287ca7fc068801535fc2b5f891511ecd5fd61c0785")

certificate = json.loads(certificate_bytes)
basis_rows = certificate["basis_coordinate_rows"]
relations = certificate["coordinate_relations"]
reduced = certificate["reduced_coordinate_matrix"]
assert len(basis_rows) == 111
assert len(relations) == len(reduced) == 176
assert all(len(row) == 111 for row in relations)

lines = full_bytes.decode().splitlines()
assert lines[-2:] == ["(check-sat)", "(get-model)"]
coordinate_assertions = lines[-178:-2]
assert len(coordinate_assertions) == 176
pattern = re.compile(r"^\(assert \(= n[0-9]+ \(_ bv0 2\)\)\)$")
assert all(pattern.fullmatch(line) for line in coordinate_assertions)

# The full emitter appends the 176 Kuranishi assertions in coordinate order.
# Replace precisely that terminal block by the certified original-row basis.
basis_assertions = [coordinate_assertions[index] for index in basis_rows]
output_lines = lines[:-178] + basis_assertions + lines[-2:]
output_bytes = ("\n".join(output_lines) + "\n").encode()
Path(os.environ["OUTPUT_SMT"]).write_bytes(output_bytes)

result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-KURANISHI-BASIS-EMIT",
    "aws_job_tag": job_tag,
    "full_smt_sha256": hashlib.sha256(full_bytes).hexdigest(),
    "span_certificate_gzip_sha256": hashlib.sha256(
        certificate_path.read_bytes()).hexdigest(),
    "span_certificate_uncompressed_sha256": hashlib.sha256(
        certificate_bytes).hexdigest(),
    "full_coordinate_count": 176,
    "basis_coordinate_count": len(basis_rows),
    "basis_coordinate_rows": basis_rows,
    "output_smt_sha256": hashlib.sha256(output_bytes).hexdigest(),
    "output_smt_size": len(output_bytes),
    "equivalence_scope": (
        "K=0 is equivalent to vanishing of these 111 original coordinate "
        "rows by the pinned exact F3 relation certificate"),
    "refusal_scope": [
        "formula emission is not a SAT or UNSAT verdict",
        "SAT still requires literal integer reconstruction/replay",
        "UNSAT still requires an independently checked certificate",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("basis_rows", len(basis_rows))
print("output_smt_sha256", result["output_smt_sha256"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
