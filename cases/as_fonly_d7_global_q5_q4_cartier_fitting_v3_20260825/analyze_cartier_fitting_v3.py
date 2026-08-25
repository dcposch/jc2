#!/usr/bin/env python3
"""Correct the exact restoration-row count and preserve independent rows."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q5_q4_cartier_fitting_20260825"
          / "analyze_cartier_fitting.py")
EXPECTED = "dd779edff09d5a7c17a1ac79f6b688879da4cf6993d8263a6f06b65755e864aa"
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
source = payload.decode()


def replace_once(old: str, new: str) -> None:
    global source
    assert source.count(old) == 1, (old, source.count(old))
    source = source.replace(old, new)


replace_once(
    "assert len(row_assertions) == 76, len(row_assertions)",
    "assert len(row_assertions) == 63, len(row_assertions)")
replace_once(
    "def rank_mod3(flat, rows=76, columns=30):",
    "def rank_mod3(flat, rows=63, columns=30):")
replace_once(
    '"left_cokernel_dimension": 76 - rank,',
    '"left_cokernel_dimension": 63 - rank,')
replace_once(
    '"matrix_shape": [76, 30],',
    '"matrix_shape": [63, 30],')

replace_once(
    '''q4_payload = q4.sexpr().encode()
result = {
''',
    '''q4_payload = q4.sexpr().encode()
independent_expression_payload = "\\n".join(
    assertion.sexpr() for assertion in independent_assertions).encode()
independent_dependencies = sorted(set().union(*[
    variables(assertion) for assertion in independent_assertions]))
result = {
''')

replace_once(
    '''    "independent_assertion_count": len(independent_assertions),
    "affine_whole_cube_check": str(affine_status),
''',
    '''    "independent_assertion_count": len(independent_assertions),
    "independent_assertion_expression_sha256": hashlib.sha256(
        independent_expression_payload).hexdigest(),
    "independent_assertion_dependencies": independent_dependencies,
    "independent_assertions_preserved_not_solved": True,
    "v2_expected_76_rows_scope_failure_corrected": True,
    "affine_whole_cube_check": str(affine_status),
''')

replace_once(
    '''(OUT / "q4_expression.smt2expr").write_bytes(q4_payload + b"\\n")
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
''',
    '''(OUT / "q4_expression.smt2expr").write_bytes(q4_payload + b"\\n")
(OUT / "independent_assertions.smt2expr").write_bytes(
    independent_expression_payload + b"\\n")
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
''')

replace_once(
    '''print("q4_dependencies", q4_dependencies)
print("result_sha256", hashlib.sha256(encoded).hexdigest())
''',
    '''print("q4_dependencies", q4_dependencies)
print("independent_assertions", len(independent_assertions),
      "dependencies", independent_dependencies)
print("result_sha256", hashlib.sha256(encoded).hexdigest())
''')

namespace = {"__file__": str(PARENT), "__name__": "__cartier_fitting_v3__"}
exec(compile(source, str(PARENT), "exec"), namespace)
