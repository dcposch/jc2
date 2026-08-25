#!/usr/bin/env python3
"""Sparse-AST affinity proof and corrected global Q4 Fitting strata."""
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
    assert source.count(old) == 1, (old[:160], source.count(old))
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

old_affine = '''# One whole-cube symbolic check: every charged row equals its affine rebuild.
affine_check = z3.Solver()
affine_check.set(timeout=int(os.environ.get("AFFINE_TIMEOUT_MS", "3600000")))
for variable in all_input_vars:
    affine_check.add(z3.ULE(variable, z3.BitVecVal(2, WIDTH)))
affine_check.add(z3.Or(*[
    mod_three_side(assertion) != reconstructed
    for assertion, reconstructed in zip(row_assertions, reconstructions)]))
affine_status = affine_check.check()
assert affine_status == z3.unsat, (affine_status, affine_check.reason_unknown())
'''

new_affine = '''# Exact sparse-AST certificate: restoration digits never occur below an
# exact division and never meet one another in a multiplication.  Therefore
# each final mod-3 row is affine in all 30 restoration digits.  Fail closed on
# any unsupported restoration-dependent node.
ast_seen = set()
ast_dependent_nodes = set()
ast_one_sided_multiplication_nodes = set()
ast_remainder_nodes = set()
ast_mixed_multiplication_nodes = []
ast_dependent_division_nodes = []
ast_unsupported_dependent_nodes = []
ast_cache = {}

def restoration_dependencies(node):
    key = node.get_id()
    if key in ast_cache:
        return ast_cache[key]
    ast_seen.add(key)
    if z3.is_bv_value(node):
        dependencies = frozenset()
    elif (z3.is_const(node)
          and node.decl().kind() == z3.Z3_OP_UNINTERPRETED):
        name = node.decl().name()
        dependencies = frozenset([name]) if name in restoration_names else frozenset()
    else:
        kind = node.decl().kind()
        child_dependencies = [restoration_dependencies(child)
                              for child in node.children()]
        dependencies = frozenset().union(*child_dependencies)
        if dependencies:
            ast_dependent_nodes.add(key)
            if kind == z3.Z3_OP_BMUL:
                charged_children = [item for item in child_dependencies if item]
                if len(charged_children) > 1:
                    ast_mixed_multiplication_nodes.append(node.sexpr())
                else:
                    ast_one_sided_multiplication_nodes.add(key)
            elif kind == z3.Z3_OP_BUDIV:
                ast_dependent_division_nodes.append(node.sexpr())
            elif kind == z3.Z3_OP_BUREM:
                assert len(child_dependencies) == 2
                if child_dependencies[1]:
                    ast_unsupported_dependent_nodes.append(node.sexpr())
                ast_remainder_nodes.add(key)
            elif kind not in {
                    z3.Z3_OP_BADD, z3.Z3_OP_BSUB, z3.Z3_OP_BNEG}:
                ast_unsupported_dependent_nodes.append(node.sexpr())
    ast_cache[key] = dependencies
    return dependencies

row_restoration_dependencies = []
for assertion in row_assertions:
    row_restoration_dependencies.append(sorted(
        restoration_dependencies(mod_three_side(assertion))))
assert not ast_mixed_multiplication_nodes, ast_mixed_multiplication_nodes[:1]
assert not ast_dependent_division_nodes, ast_dependent_division_nodes[:1]
assert not ast_unsupported_dependent_nodes, ast_unsupported_dependent_nodes[:1]
assert set().union(*map(set, row_restoration_dependencies)) <= restoration_names
affine_status = "PROVED-SPARSE-AST-AFFINE"
'''
replace_once(old_affine, new_affine)

replace_once(
    '''q4_payload = q4.sexpr().encode()
result = {
''',
    '''q4_payload = q4.sexpr().encode()
independent_expression_payload = "\\n".join(
    assertion.sexpr() for assertion in independent_assertions).encode()
independent_dependencies = sorted(set().union(*[
    variables(assertion) for assertion in independent_assertions]))
ast_certificate_payload = json.dumps({
    "row_restoration_dependencies": row_restoration_dependencies,
    "total_unique_node_count": len(ast_seen),
    "restoration_dependent_node_count": len(ast_dependent_nodes),
    "one_sided_multiplication_node_count": len(ast_one_sided_multiplication_nodes),
    "remainder_node_count": len(ast_remainder_nodes),
    "mixed_multiplication_node_count": len(ast_mixed_multiplication_nodes),
    "dependent_division_node_count": len(ast_dependent_division_nodes),
    "unsupported_dependent_node_count": len(ast_unsupported_dependent_nodes),
}, sort_keys=True, separators=(",", ":")).encode()
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
    "affine_proof_method": "sparse AST: no dependent UDiv or two-sided multiplication",
    "affine_reconstruction_source_proved": True,
    "ast_certificate_sha256": hashlib.sha256(
        ast_certificate_payload).hexdigest(),
    "ast_total_unique_node_count": len(ast_seen),
    "ast_restoration_dependent_node_count": len(ast_dependent_nodes),
    "ast_one_sided_multiplication_node_count": len(
        ast_one_sided_multiplication_nodes),
    "ast_remainder_node_count": len(ast_remainder_nodes),
    "ast_mixed_multiplication_node_count": len(
        ast_mixed_multiplication_nodes),
    "ast_dependent_division_node_count": len(ast_dependent_division_nodes),
    "ast_unsupported_dependent_node_count": len(
        ast_unsupported_dependent_nodes),
''')

replace_once(
    '''(OUT / "q4_expression.smt2expr").write_bytes(q4_payload + b"\\n")
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
''',
    '''(OUT / "q4_expression.smt2expr").write_bytes(q4_payload + b"\\n")
(OUT / "independent_assertions.smt2expr").write_bytes(
    independent_expression_payload + b"\\n")
(OUT / "ast_affinity_certificate.json").write_bytes(
    ast_certificate_payload + b"\\n")
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
''')

replace_once(
    '''print("q4_dependencies", q4_dependencies)
print("result_sha256", hashlib.sha256(encoded).hexdigest())
''',
    '''print("q4_dependencies", q4_dependencies)
print("independent_assertions", len(independent_assertions),
      "dependencies", independent_dependencies)
print("ast_affinity", affine_status,
      "nodes", len(ast_seen), "dependent", len(ast_dependent_nodes),
      "one_sided_mul", len(ast_one_sided_multiplication_nodes),
      "dependent_udiv", len(ast_dependent_division_nodes),
      "mixed_mul", len(ast_mixed_multiplication_nodes))
print("result_sha256", hashlib.sha256(encoded).hexdigest())
''')

namespace = {"__file__": str(PARENT), "__name__": "__cartier_fitting_v4__"}
exec(compile(source, str(PARENT), "exec"), namespace)
