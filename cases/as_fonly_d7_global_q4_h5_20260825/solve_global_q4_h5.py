#!/usr/bin/env python3
"""Source-pinned compiler for the Q4/H5,J5 chronological successor."""
from __future__ import annotations

import hashlib
from pathlib import Path
import os


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
# At this point `source` is the expanded raw compiler after the Q5 patch.
def q4_replace_once(text, old, new):
    assert text.count(old) == 1, (old[:80], text.count(old))
    return text.replace(old, new)

source = q4_replace_once(
    source,
    '''hvars = [z3.BitVec(f"q6_{index}", WIDTH) for index in range(16)]
kvars = [z3.BitVec(f"q5_{index}", WIDTH) for index in range(14)]
all_input_vars = (list(pred_vars.values()) + xvars + yvars + rvars
                  + hvars + kvars)
''',
    '''hvars = [z3.BitVec(f"q6_{index}", WIDTH) for index in range(16)]
kvars = [z3.BitVec(f"q5_{index}", WIDTH) for index in range(14)]
mvars = [z3.BitVec(f"q4_{index}", WIDTH) for index in range(12)]
all_input_vars = (list(pred_vars.values()) + xvars + yvars + rvars
                  + hvars + kvars + mvars)
''')

carry_start = source.index('def fourth_digit_cross(H, J):\n')
carry_end = source.index(
    '# Backwards-compatible metadata name: this switch now omits the entire new\n',
    carry_start)
q4_block = '''# Licensed homogeneous degree-five fourth digit and Q4 row.
H5 = homogeneous(5, mvars[:6])
J5 = homogeneous(5, mvars[6:])
E1_4_final = divide_three(degree_part(E, 4))
F4_final = padd(E1_4_final, degree_part(M, 4),
                 degree_part(divWZ, 4))
F1_4_final = divide_three(F4_final)
G4_final = padd(F1_4_final, degree_part(N, 4), degree_part(T, 4),
                 pderivative(H5, 0), pderivative(J5, 1))

q4_gate_omitted = os.environ.get("OMIT_Q4_GATE", "0") == "1"
if not q4_gate_omitted:
    constrain_row_zero(G4_final, 4)

def fourth_digit_cross(H, J):
    return padd(pmul(source_data["A"], pderivative(J, 1)),
                 pmul(pderivative(H, 0), source_data["vy"]),
                 pscale(-1, pmul(source_data["uy"], pderivative(J, 0))),
                 pscale(-1, pmul(pderivative(H, 1), source_data["vx"])))

S_HJ = padd(fourth_digit_cross(H7, J7),
             fourth_digit_cross(H6, J6),
             fourth_digit_cross(H5, J5))
terminal_polys = {}
for degree in range(7, 13):
    E1 = divide_three(degree_part(E, degree))
    F = padd(E1, degree_part(M, degree), degree_part(divWZ, degree))
    F1 = divide_three(F)
    G = padd(F1, degree_part(N, degree), degree_part(T, degree))
    G1 = divide_three(G)
    terminal_polys[degree] = padd(G1, degree_part(S_HJ, degree),
                                   degree_part(Rmix, degree))
    if not q4_gate_omitted:
        constrain_row_zero(terminal_polys[degree], degree)

# Optional exact parent pins for witness-first continuation.
def pin_existing(name, variables):
    values = parse_pin(name, len(variables))
    if values is not None:
        for variable, value in zip(variables, values):
            solver.add(variable == bv(value))
    return values

pinned_q9 = pin_existing("PIN_Q9", xvars)
pinned_q8 = pin_existing("PIN_Q8", yvars)
pinned_q7 = pin_existing("PIN_Q7", rvars)
pinned_q6 = pin_existing("PIN_Q6", hvars)
pinned_q5 = pin_existing("PIN_Q5", kvars)
'''
source = source[:carry_start] + q4_block + source[carry_end:]

source = q4_replace_once(
    source,
    '''# Backwards-compatible metadata name: this switch now omits the entire new
# Q5 gate (six Q5 rows and all sixty-three terminal rows).
terminal_rows_omitted = q5_gate_omitted
''',
    '''# Metadata switch for the new Q4 row plus recomputed terminal rows.
terminal_rows_omitted = q4_gate_omitted
''')

source = q4_replace_once(
    source,
    '''    "q5_raw_variable_count": len(kvars),
    "q5_explicit_source_row_count": 6,
    "terminal_row_count": 63,
    "displayed_equation_count": 197,
    "q5_gate_omitted": q5_gate_omitted,
''',
    '''    "q5_raw_variable_count": len(kvars),
    "q5_explicit_source_row_count": 6,
    "q4_raw_variable_count": len(mvars),
    "q4_explicit_source_row_count": 5,
    "terminal_row_count": 63,
    "displayed_equation_count": 202,
    "q5_gate_omitted": q5_gate_omitted,
    "q4_gate_omitted": q4_gate_omitted,
    "pinned_q9": list(pinned_q9) if pinned_q9 is not None else None,
    "pinned_q8": list(pinned_q8) if pinned_q8 is not None else None,
    "pinned_q7": list(pinned_q7) if pinned_q7 is not None else None,
    "pinned_q6": list(pinned_q6) if pinned_q6 is not None else None,
    "pinned_q5": list(pinned_q5) if pinned_q5 is not None else None,
''')

source = q4_replace_once(
    source,
    '''    kvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in kvars]
    assert all(0 <= value <= 2 for value in
               pred_values + xvalues + yvalues + rvalues + hvalues + kvalues)
''',
    '''    kvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in kvars]
    mvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in mvars]
    assert all(0 <= value <= 2 for value in
               pred_values + xvalues + yvalues + rvalues + hvalues + kvalues
               + mvalues)
''')

source = q4_replace_once(
    source,
    '''        "q5_values": kvalues,
        "direct_integer_replay_required": True,
''',
    '''        "q5_values": kvalues,
        "q4_values": mvalues,
        "direct_integer_replay_required": True,
''')

source = q4_replace_once(
    source,
    '''print("raw_variable_shapes", len(xvars), len(yvars), len(rvars), len(hvars), len(kvars))
print("explicit_source_rows", 23, 22, 19, 9, 7, 6, 63)
print("displayed_equation_inventory", 20 + 5 + 12 + 11 + 23 + 22 + 19 + 9 + 7 + 6 + 63)
''',
    '''print("raw_variable_shapes", len(xvars), len(yvars), len(rvars), len(hvars), len(kvars), len(mvars))
print("explicit_source_rows", 23, 22, 19, 9, 7, 6, 5, 63)
print("displayed_equation_inventory", 20 + 5 + 12 + 11 + 23 + 22 + 19 + 9 + 7 + 6 + 5 + 63)
''')
"""

source = source.replace(marker, injection + "\n" + marker)
scope = {"__file__": str(PARENT), "__name__": "__global_q4_h5_compiler__"}
exec(compile(source, str(PARENT), "exec"), scope)
