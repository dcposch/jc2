#!/usr/bin/env python3
"""Exact syntactic dependency/component analysis for the basis111 circuit."""

from __future__ import annotations

import gzip
import hashlib
import json
import os
import platform
import re
from collections import Counter
from pathlib import Path


assert platform.system() == "Linux", "AWS-only analyzer refuses non-Linux"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_kuranishi_deps_"), job_tag
formula_path = Path(os.environ["FULL_SMT"])
certificate_path = Path(os.environ["SPAN_CERTIFICATE_GZIP"])
formula_bytes = formula_path.read_bytes()
certificate_bytes = gzip.decompress(certificate_path.read_bytes())
assert hashlib.sha256(formula_bytes).hexdigest() == (
    "108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c")
assert hashlib.sha256(certificate_bytes).hexdigest() == (
    "d363cc0c5adbf432d8f3d5287ca7fc068801535fc2b5f891511ecd5fd61c0785")
certificate = json.loads(certificate_bytes)
basis_rows = certificate["basis_coordinate_rows"]
assert len(basis_rows) == 111

lines = formula_bytes.decode().splitlines()
input_pattern = re.compile(r"^\(declare-fun ([as]_[0-9]+) \(\) \(_ BitVec 2\)\)$")
definition_pattern = re.compile(r"^\(define-fun (n[0-9]+) \(\) .+\)$")
name_pattern = re.compile(r"(?<![A-Za-z0-9_])(?:n[0-9]+|[as]_[0-9]+)(?![A-Za-z0-9_])")
assertion_pattern = re.compile(r"^\(assert \(= (n[0-9]+) \(_ bv0 2\)\)\)$")

inputs = [match.group(1) for line in lines
          if (match := input_pattern.fullmatch(line))]
assert len(inputs) == 95
input_set = set(inputs)
dependencies = {name: frozenset([name]) for name in inputs}
definition_count = 0
for line in lines:
    match = definition_pattern.fullmatch(line)
    if not match:
        continue
    name = match.group(1)
    referenced = set(name_pattern.findall(line))
    referenced.discard(name)
    assert all(ref in dependencies for ref in referenced), (name, referenced)
    dependencies[name] = frozenset().union(
        *(dependencies[ref] for ref in referenced)) if referenced else frozenset()
    definition_count += 1
assert definition_count == 34555

coordinate_lines = lines[-178:-2]
coordinate_nodes = []
for line in coordinate_lines:
    match = assertion_pattern.fullmatch(line)
    assert match, line
    coordinate_nodes.append(match.group(1))
assert len(coordinate_nodes) == 176
basis_nodes = [coordinate_nodes[index] for index in basis_rows]
basis_dependencies = [sorted(dependencies[node]) for node in basis_nodes]

# Connected components in the exact syntactic incidence hypergraph.
parent = {name: name for name in inputs}


def find(name):
    while parent[name] != name:
        parent[name] = parent[parent[name]]
        name = parent[name]
    return name


def union(left, right):
    left, right = find(left), find(right)
    if left != right:
        parent[right] = left


for support in basis_dependencies:
    if not support:
        continue
    for name in support[1:]:
        union(support[0], name)
components = {}
for name in inputs:
    components.setdefault(find(name), []).append(name)
component_values = sorted((sorted(value) for value in components.values()),
                          key=lambda value: (len(value), value))

unused = sorted(input_set - set().union(*(set(row) for row in basis_dependencies)))
support_histogram = dict(sorted(Counter(
    len(row) for row in basis_dependencies).items()))
input_occurrence = Counter(name for row in basis_dependencies for name in row)
payload = {
    "basis_rows": basis_rows,
    "basis_nodes": basis_nodes,
    "basis_dependencies": basis_dependencies,
    "components": component_values,
    "unused_inputs": unused,
    "input_occurrence": dict(sorted(input_occurrence.items())),
}
payload_bytes = (json.dumps(payload, sort_keys=True, separators=(",", ":"))
                 + "\n").encode()
Path(os.environ["PAYLOAD_GZIP"]).write_bytes(
    gzip.compress(payload_bytes, compresslevel=9, mtime=0))
result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-KURANISHI-BASIS-DEPENDENCIES",
    "aws_job_tag": job_tag,
    "formula_sha256": hashlib.sha256(formula_bytes).hexdigest(),
    "certificate_uncompressed_sha256": hashlib.sha256(
        certificate_bytes).hexdigest(),
    "definition_count": definition_count,
    "input_count": len(inputs),
    "basis_coordinate_count": len(basis_rows),
    "support_size_histogram": support_histogram,
    "used_input_count": len(inputs) - len(unused),
    "unused_inputs": unused,
    "incidence_component_sizes": [len(value) for value in component_values],
    "payload_uncompressed_sha256": hashlib.sha256(payload_bytes).hexdigest(),
    "scope": (
        "exact syntactic input dependence through the pinned modular DAG; "
        "supports may overapproximate semantic dependence after cancellation"),
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("support_histogram", support_histogram)
print("used_unused", len(inputs) - len(unused), unused)
print("component_sizes", result["incidence_component_sizes"])
print("payload_sha256", result["payload_uncompressed_sha256"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
