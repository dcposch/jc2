#!/usr/bin/env python3
"""Append the eliminated Q2/Q1 row-8 scalar to the complete Q5 formula."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q5_h6_20260825"
          / "solve_global_q5_h6.py")
EXPECTED = "2bdf4bb4743a4bf5904c87b5550df6fa7908e779e6c90645ab2e911bda87805d"
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
source = payload.decode()
marker = '''scope = {"__file__": str(PARENT), "__name__": "__global_q5_h6_compiler__"}
exec(compile(source, str(PARENT), "exec"), scope)
'''
assert source.count(marker) == 1

injection = r"""
row8_end = source.index('\nsmt2 = solver.to_smt2().encode()\n')
row8_block = r'''# Eliminated first-carry obstruction at row 8 = x^2 y.
E1_low_degree_one = divide_three(degree_part(E, 1))
Fbase_degree_one = padd(E1_low_degree_one, degree_part(M, 1))
row8_rx = f3(Fbase_degree_one.get((1, 0), bv(0)))
row8_ry = f3(Fbase_degree_one.get((0, 1), bv(0)))
row8_omega = fadd(row8_ry,
                  fscale(2, fmul(pred_vars["h"], row8_rx)))
row8_omitted = os.environ.get("OMIT_GLOBAL_ROW8", "0") == "1"
if not row8_omitted:
    solver.add(row8_omega == bv(0))
row8_payload = row8_omega.sexpr().encode()
Path(os.environ["ROW8_EXPR_OUTPUT"]).write_bytes(row8_payload + b"\n")

'''
source = source[:row8_end] + row8_block + source[row8_end:]

def row8_replace_once(text, old, new):
    assert text.count(old) == 1, (old[:100], text.count(old))
    return text.replace(old, new)

source = row8_replace_once(
    source,
    '''    "q5_gate_omitted": q5_gate_omitted,
''',
    '''    "q5_gate_omitted": q5_gate_omitted,
    "q2q1_row8_omitted": row8_omitted,
    "q2q1_row8_coordinate": [2, 1],
    "q2q1_row8_eliminated_scalar": "ry-h*rx",
    "q2q1_row8_expression_sha256": hashlib.sha256(row8_payload).hexdigest(),
    "displayed_equation_count_with_row8": 198,
''')

source = row8_replace_once(
    source,
    '''        "q5_values": kvalues,
        "direct_integer_replay_required": True,
''',
    '''        "q5_values": kvalues,
        "q2q1_row8_value": model.eval(row8_omega,
                                      model_completion=True).as_long(),
        "direct_integer_replay_required": True,
''')

source = row8_replace_once(
    source,
    '''print("displayed_equation_inventory", 20 + 5 + 12 + 11 + 23 + 22 + 19 + 9 + 7 + 6 + 63)
''',
    '''print("displayed_equation_inventory", 20 + 5 + 12 + 11 + 23 + 22 + 19 + 9 + 7 + 6 + 63 + 1)
print("q2q1_row8_coordinate", 2, 1, "omitted", row8_omitted)
print("q2q1_row8_expression_sha256", hashlib.sha256(row8_payload).hexdigest())
''')
"""

source = source.replace(marker, injection + "\n" + marker)
scope = {"__file__": str(PARENT), "__name__": "__global_q2q1_row8__"}
exec(compile(source, str(PARENT), "exec"), scope)
