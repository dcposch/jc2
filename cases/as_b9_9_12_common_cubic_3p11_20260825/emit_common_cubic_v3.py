#!/usr/bin/env python3
"""Source-audited V3 wrapper fixing the V2 modulus-as-residue bug."""

from __future__ import annotations

import ast
import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
BASE = (ROOT / "cases/as_b9_9_12_common_cubic_3p11_20260825"
        / "emit_common_cubic.py")
EXPECTED_BASE = (
    "ab85df4824042f9919e535ad9b2d9c4213deb1aa2ed953ae6fa6aed4c66a7556")
payload = BASE.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_BASE
text = payload.decode()

old_definition = '''def bv(value):
    return f"(_ bv{value % MODULUS} {WIDTH})"
'''
new_definition = '''def bvraw(value):
    assert 0 <= value < 2 ** WIDTH
    return f"(_ bv{value} {WIDTH})"


def bv(value):
    return bvraw(value % MODULUS)
'''
assert text.count(old_definition) == 1
assert text.count("bv(MODULUS)") == 2
text = text.replace(old_definition, new_definition)
text = text.replace("bv(MODULUS)", "bvraw(MODULUS)")
assert "bv(MODULUS)" not in text
assert text.count("bvraw(MODULUS)") == 2
assert text.count("PASS-AS-B9-9-12-COMMON-CUBIC-SMT-EMITTED") == 1
text = text.replace(
    "PASS-AS-B9-9-12-COMMON-CUBIC-SMT-EMITTED",
    "PASS-AS-B9-9-12-COMMON-CUBIC-SMT-V3-EMITTED")

# Fail closed on the complete constructor-call inventory.  All `bv(...)`
# calls now denote residues; the only two raw non-residue constants are the
# positive modulus used by `bvurem` and by the strict coefficient bound.
tree = ast.parse(text)
residue_arguments = []
raw_arguments = []
for node in ast.walk(tree):
    if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
        continue
    if node.func.id == "bv":
        assert len(node.args) == 1 and not node.keywords
        residue_arguments.append(ast.get_source_segment(text, node.args[0]))
    if node.func.id == "bvraw":
        assert len(node.args) == 1 and not node.keywords
        raw_arguments.append(ast.get_source_segment(text, node.args[0]))
assert "MODULUS" not in residue_arguments
assert raw_arguments.count("MODULUS") == 2

patched = text.encode()
Path(os.environ["PATCHED_SOURCE_OUTPUT"]).write_bytes(patched)
print("v2_source_sha256", EXPECTED_BASE)
print("v3_patched_source_sha256", hashlib.sha256(patched).hexdigest())
print("bv_residue_calls", len(residue_arguments))
print("bvraw_modulus_calls", raw_arguments.count("MODULUS"))
scope = {"__file__": str(BASE), "__name__": "__main__"}
exec(compile(patched, str(BASE) + ":V3", "exec"), scope)
