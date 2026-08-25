#!/usr/bin/env python3
"""Source-pinned global Q5-locus Q4 Cartier discriminator."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q5_h6_20260825"
          / "solve_global_q5_h6.py")
EXPECTED_PARENT_SHA = (
    "2bdf4bb4743a4bf5904c87b5550df6fa7908e779e6c90645ab2e911bda87805d")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()

marker = '''scope = {"__file__": str(PARENT), "__name__": "__global_q5_h6_compiler__"}
exec(compile(source, str(PARENT), "exec"), scope)
'''
assert source.count(marker) == 1

injection = r"""
# `source` now carries the complete Q5 patch.  Preserve its original Q5
# terminal block byte-for-byte and append one Q4 coordinate immediately
# before the Q5 metadata comment.
def cartier_replace_once(text, old, new):
    assert text.count(old) == 1, (old[:80], text.count(old))
    return text.replace(old, new)

carry_start = source.index('def fourth_digit_cross(H, J):\n')
carry_end = source.index(
    '# Backwards-compatible metadata name: this switch now omits the entire new\n',
    carry_start)
original_q5_carry = source[carry_start:carry_end]
cartier_block = r'''# First Q4 Cartier-cokernel coordinate on the complete displayed Q5 locus.
E1_4_cartier = divide_three(degree_part(E, 4))
F4_cartier = padd(E1_4_cartier, degree_part(M, 4),
                   degree_part(divWZ, 4))
F1_4_cartier = divide_three(F4_cartier)
G4_cartier = padd(F1_4_cartier, degree_part(N, 4), degree_part(T, 4))
q4_cartier_omitted = os.environ.get("OMIT_Q4_CARTIER", "0") == "1"
q4_cartier_coefficient = G4_cartier.get((2, 2), bv(0))
if not q4_cartier_omitted:
    solver.add(z3.URem(q4_cartier_coefficient, BV_THREE) == bv(0))

'''
source = (source[:carry_start] + original_q5_carry + cartier_block
          + source[carry_end:])

source = cartier_replace_once(
    source,
    '''    "q5_gate_omitted": q5_gate_omitted,
''',
    '''    "q5_gate_omitted": q5_gate_omitted,
    "q4_cartier_row_count": 1,
    "q4_cartier_coordinate": [2, 2],
    "q4_cartier_omitted": q4_cartier_omitted,
    "displayed_equation_count_with_cartier": 198,
''')

source = cartier_replace_once(
    source,
    '''print("displayed_equation_inventory", 20 + 5 + 12 + 11 + 23 + 22 + 19 + 9 + 7 + 6 + 63)
''',
    '''print("displayed_equation_inventory", 20 + 5 + 12 + 11 + 23 + 22 + 19 + 9 + 7 + 6 + 63 + 1)
print("q4_cartier_coordinate", 2, 2)
''')
"""

source = source.replace(marker, injection + "\n" + marker)
scope = {"__file__": str(PARENT), "__name__": "__global_q5_q4_cartier__"}
exec(compile(source, str(PARENT), "exec"), scope)
