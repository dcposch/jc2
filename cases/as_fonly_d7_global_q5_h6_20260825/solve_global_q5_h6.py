#!/usr/bin/env python3
"""Source-pinned compiler for the global Q5/H6,J6 accepted-fibre gate."""
from __future__ import annotations

import hashlib
from pathlib import Path
import os


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q6_high_20260825"
          / "solve_global_q6_high.py")
EXPECTED_PARENT_SHA = (
    "c027e3f18f38539eeba72abafd181fac04dd7cce43905f5c952caa1e4ee23875")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()

marker = '''scope = {"__file__": str(PARENT), "__name__": "__global_q6_high_compiler__"}
exec(compile(source, str(PARENT), "exec"), scope)
'''
assert source.count(marker) == 1

injection = r"""
# At this point `source` is the fully expanded raw-Q7 compiler after the
# frozen Q6/high patch.  Apply the Q5 patch before executing it.
source = replace_once(
    source,
    '''rvars = [z3.BitVec(f"q7_{index}", WIDTH) for index in range(18)]
hvars = [z3.BitVec(f"q6_{index}", WIDTH) for index in range(16)]
all_input_vars = list(pred_vars.values()) + xvars + yvars + rvars + hvars
''',
    '''rvars = [z3.BitVec(f"q7_{index}", WIDTH) for index in range(18)]
hvars = [z3.BitVec(f"q6_{index}", WIDTH) for index in range(16)]
kvars = [z3.BitVec(f"q5_{index}", WIDTH) for index in range(14)]
all_input_vars = (list(pred_vars.values()) + xvars + yvars + rvars
                  + hvars + kvars)
''')

q5_start = source.index(
    '# First row not reimposed by the triangular parent: final G8 after Q7.\n')
q5_end = source.index('\nsmt2 = solver.to_smt2().encode()\n', q5_start)
q5_extended = '''# First row not reimposed by the triangular parent: final G8 after Q7.
E1_8_final = divide_three(degree_part(E, 8))
F8_final = padd(E1_8_final, degree_part(M, 8),
                 degree_part(divWZ, 8))
F1_8_final = divide_three(F8_final)
G8_final = padd(F1_8_final, degree_part(N, 8), degree_part(T, 8))
constrain_row_zero(G8_final, 8)

# Licensed homogeneous degree-seven fourth digit and all seven Q6 rows.
H7 = homogeneous(7, hvars[:8])
J7 = homogeneous(7, hvars[8:])
E1_6_final = divide_three(degree_part(E, 6))
F6_final = padd(E1_6_final, degree_part(M, 6),
                 degree_part(divWZ, 6))
F1_6_final = divide_three(F6_final)
G6_final = padd(F1_6_final, degree_part(N, 6), degree_part(T, 6),
                 pderivative(H7, 0), pderivative(J7, 1))
constrain_row_zero(G6_final, 6)

# Licensed homogeneous degree-six fourth digit and the complete Q5 row.
H6 = homogeneous(6, kvars[:7])
J6 = homogeneous(6, kvars[7:])
E1_5_final = divide_three(degree_part(E, 5))
F5_final = padd(E1_5_final, degree_part(M, 5),
                 degree_part(divWZ, 5))
F1_5_final = divide_three(F5_final)
G5_final = padd(F1_5_final, degree_part(N, 5), degree_part(T, 5),
                 pderivative(H6, 0), pderivative(J6, 1))

q5_gate_omitted = os.environ.get("OMIT_Q5_GATE", "0") == "1"
if not q5_gate_omitted:
    constrain_row_zero(G5_final, 5)

def fourth_digit_cross(H, J):
    return padd(pmul(source_data["A"], pderivative(J, 1)),
                 pmul(pderivative(H, 0), source_data["vy"]),
                 pscale(-1, pmul(source_data["uy"], pderivative(J, 0))),
                 pscale(-1, pmul(pderivative(H, 1), source_data["vx"])))

S_HJ = padd(fourth_digit_cross(H7, J7),
             fourth_digit_cross(H6, J6))
terminal_polys = {}
for degree in range(7, 13):
    E1 = divide_three(degree_part(E, degree))
    F = padd(E1, degree_part(M, degree), degree_part(divWZ, degree))
    F1 = divide_three(F)
    G = padd(F1, degree_part(N, degree), degree_part(T, degree))
    G1 = divide_three(G)
    terminal_polys[degree] = padd(G1, degree_part(S_HJ, degree),
                                   degree_part(Rmix, degree))
    if not q5_gate_omitted:
        constrain_row_zero(terminal_polys[degree], degree)

# Backwards-compatible metadata name: this switch now omits the entire new
# Q5 gate (six Q5 rows and all sixty-three terminal rows).
terminal_rows_omitted = q5_gate_omitted
'''
source = source[:q5_start] + q5_extended + source[q5_end:]

source = replace_once(
    source,
    '''    "q6_raw_variable_count": len(hvars),
    "q6_explicit_source_row_count": 7,
    "terminal_row_count": 63,
''',
    '''    "q6_raw_variable_count": len(hvars),
    "q6_explicit_source_row_count": 7,
    "q5_raw_variable_count": len(kvars),
    "q5_explicit_source_row_count": 6,
    "terminal_row_count": 63,
    "displayed_equation_count": 197,
    "q5_gate_omitted": q5_gate_omitted,
''')

source = replace_once(
    source,
    '''    "scope": ("complete aligned vertical predecessor formula with raw "
              "Q9/Q8/Q7 variables"),
''',
    '''    "scope": ("complete aligned vertical accepted-fibre formula with raw "
              "Q9/Q8/Q7/Q6/Q5 variables"),
''')

source = replace_once(
    source,
    '''    hvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in hvars]
    assert all(0 <= value <= 2
               for value in pred_values + xvalues + yvalues + rvalues + hvalues)
''',
    '''    hvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in hvars]
    kvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in kvars]
    assert all(0 <= value <= 2 for value in
               pred_values + xvalues + yvalues + rvalues + hvalues + kvalues)
''')

source = replace_once(
    source,
    '''        "q6_values": hvalues,
        "direct_integer_replay_required": True,
''',
    '''        "q6_values": hvalues,
        "q5_values": kvalues,
        "direct_integer_replay_required": True,
''')

source = replace_once(
    source,
    '''print("raw_variable_shapes", len(xvars), len(yvars), len(rvars), len(hvars))
print("explicit_source_rows", 23, 22, 19, 9, 7, 63)
''',
    '''print("raw_variable_shapes", len(xvars), len(yvars), len(rvars), len(hvars), len(kvars))
print("explicit_source_rows", 23, 22, 19, 9, 7, 6, 63)
print("displayed_equation_inventory", 20 + 5 + 12 + 11 + 23 + 22 + 19 + 9 + 7 + 6 + 63)
''')
"""

source = source.replace(marker, injection + "\n" + marker)
scope = {"__file__": str(PARENT), "__name__": "__global_q5_h6_compiler__"}
exec(compile(source, str(PARENT), "exec"), scope)
