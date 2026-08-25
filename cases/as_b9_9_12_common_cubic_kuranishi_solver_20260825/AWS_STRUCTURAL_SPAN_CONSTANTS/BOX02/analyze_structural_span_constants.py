#!/usr/bin/env python3
"""Refine the exact structural span by evaluating constant source-DAG atoms."""

from __future__ import annotations

import contextlib
import gzip
import hashlib
import io
import json
import os
import platform
import re
from pathlib import Path


assert platform.system() == "Linux", "AWS-only analyzer refuses non-Linux"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_kuranishi_span_constants_"), job_tag
parent_path = Path(os.environ["SPAN_ANALYZER_SOURCE"])
parent_bytes = parent_path.read_bytes()
assert hashlib.sha256(parent_bytes).hexdigest() == (
    "0cbfd304c5a214b2120b024ba322986543d42d4bd09192319b71329d924eb9c3")

saved_output = os.environ["OUTPUT_JSON"]
saved_certificate = os.environ["CERTIFICATE_GZIP"]
os.environ["OUTPUT_JSON"] = os.environ["PARENT_SPAN_RESULT"]
os.environ["CERTIFICATE_GZIP"] = os.environ["PARENT_SPAN_CERTIFICATE"]
namespace = {"__file__": str(parent_path), "__name__": "__span_constants_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(parent_bytes, str(parent_path), "exec"), namespace)
os.environ["OUTPUT_JSON"] = saved_output
os.environ["CERTIFICATE_GZIP"] = saved_certificate

emitted = namespace["scope"]
next_rhs = emitted["next_rhs"]
dag = emitted["dag"]
groups = namespace["groups"]
reduced = namespace["reduced"]
assert (len(next_rhs), len(reduced), len(reduced[0])) == (299, 176, len(groups))

inputs = {ref.name for ref in dag.inputs}
definitions = {ref.name: (ref, body) for ref, body in dag.definitions}
token_pattern = re.compile(r"(?<![A-Za-z0-9_])(?:n[0-9]+|[as]_[0-9]+)(?![A-Za-z0-9_])")
dependency_cache = {name: frozenset([name]) for name in inputs}


def dependencies(name):
    if name in dependency_cache:
        return dependency_cache[name]
    _ref, body = definitions[name]
    names = set(token_pattern.findall(body))
    names.discard(name)
    answer = frozenset().union(*(dependencies(value) for value in names)) \
        if names else frozenset()
    dependency_cache[name] = answer
    return answer


constant_cache = {}
constant_pattern = re.compile(r"^\(_ bv([0-9]+) (2|20)\)$")
binary_pattern = re.compile(r"^\((fadd|fmul|madd|mmul) (n[0-9]+) (n[0-9]+)\)$")
unary_pattern = re.compile(r"^\(mneg (n[0-9]+)\)$")
embed_pattern = re.compile(r"^\(\(_ zero_extend 18\) (n[0-9]+)\)$")
digit_pattern = re.compile(
    r"^\(\(_ extract 1 0\) \(bvurem \(bvudiv (n[0-9]+) "
    r"\(_ bv([0-9]+) 20\)\) \(_ bv3 20\)\)\)$")


def constant_value(name):
    if name in constant_cache:
        return constant_cache[name]
    assert not dependencies(name), name
    ref, body = definitions[name]
    if match := constant_pattern.fullmatch(body):
        answer = (int(match.group(1)), int(match.group(2)))
    elif match := binary_pattern.fullmatch(body):
        operation, left_name, right_name = match.groups()
        left, left_width = constant_value(left_name)
        right, right_width = constant_value(right_name)
        assert left_width == right_width
        modulus = 3 if operation.startswith("f") else 531441
        value = ((left + right) if operation.endswith("add")
                 else (left * right)) % modulus
        answer = (value, left_width)
    elif match := unary_pattern.fullmatch(body):
        value, width = constant_value(match.group(1))
        assert width == 20
        answer = ((-value) % 531441, 20)
    elif match := embed_pattern.fullmatch(body):
        value, width = constant_value(match.group(1))
        assert width == 2
        answer = (value, 20)
    elif match := digit_pattern.fullmatch(body):
        value, width = constant_value(match.group(1))
        assert width == 20
        answer = ((value // int(match.group(2))) % 3, 2)
    else:
        raise AssertionError((name, body))
    constant_cache[name] = answer
    return answer


# Retain every nonconstant formal atom.  Collapse all constant F3 atoms to
# one exact constant column, and drop zero atoms.
nonconstant_groups = []
constant_group_values = {}
for group_index, group in enumerate(groups):
    representative = next_rhs[group[0]]
    if dependencies(representative.name):
        nonconstant_groups.append(group_index)
    else:
        value, width = constant_value(representative.name)
        assert width == 2
        constant_group_values[group_index] = value

refined = []
for row in reduced:
    current = [row[index] for index in nonconstant_groups]
    constant_coefficient = sum(
        row[index] * value for index, value in constant_group_values.items()) % 3
    current.append(constant_coefficient)
    refined.append(current)

rank_and_basis_rows = namespace["rank_and_basis_rows"]
solve_columns = namespace["solve_columns"]
rank, basis_rows = rank_and_basis_rows(refined)
basis = [refined[index] for index in basis_rows]
basis_transpose = [list(column) for column in zip(*basis)]
relations = []
for row in refined:
    coefficients = solve_columns(basis_transpose, row)
    assert all(sum(coefficients[k] * basis[k][column]
                   for k in range(rank)) % 3 == row[column]
               for column in range(len(refined[0])))
    relations.append(coefficients)

certificate = {
    "nonconstant_parent_group_indices": nonconstant_groups,
    "constant_parent_group_values": constant_group_values,
    "refined_coordinate_matrix": refined,
    "basis_coordinate_rows": basis_rows,
    "coordinate_relations": relations,
}
certificate_bytes = (json.dumps(
    certificate, sort_keys=True, separators=(",", ":")) + "\n").encode()
Path(saved_certificate).write_bytes(
    gzip.compress(certificate_bytes, compresslevel=9, mtime=0))
result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-KURANISHI-CONSTANT-REFINED-SPAN",
    "aws_job_tag": job_tag,
    "parent_analyzer_sha256": hashlib.sha256(parent_bytes).hexdigest(),
    "parent_formal_atom_rank": namespace["rank"],
    "parent_group_count": len(groups),
    "nonconstant_group_count": len(nonconstant_groups),
    "constant_group_values": constant_group_values,
    "refined_rank": rank,
    "basis_coordinate_rows": basis_rows,
    "certificate_uncompressed_sha256": hashlib.sha256(
        certificate_bytes).hexdigest(),
    "exactness": (
        "constant DAG atoms are evaluated with exact modular semantics; "
        "remaining distinct nonconstant digests are treated as independent"),
    "refusal_scope": [
        "does not solve the remaining basis-coordinate zero locus",
        "does not identify identities among distinct nonconstant DAG atoms",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(saved_output).write_bytes(encoded)
print("groups_nonconstant_constant", len(groups), len(nonconstant_groups),
      constant_group_values)
print("rank_basis", rank, basis_rows)
print("certificate_sha256", result["certificate_uncompressed_sha256"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
