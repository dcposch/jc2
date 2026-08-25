#!/usr/bin/env python3
"""Source-pinned patch compiler for the global final-G8/Q6/high gate."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_predecessor_rawq7_20260825"
          / "solve_global_predecessor.py")
EXPECTED_PARENT_SHA = (
    "96c7ea60377c43c33bc3494d57126f22a7e4f94ab3e49c0e1faf7e4a85804bf0")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()


def replace_once(text, old, new):
    assert text.count(old) == 1, (old[:80], text.count(old))
    return text.replace(old, new)


old_declarations = '''rvars = [z3.BitVec(f"q7_{index}", WIDTH) for index in range(18)]
all_input_vars = list(pred_vars.values()) + xvars + yvars + rvars
'''
new_declarations = '''rvars = [z3.BitVec(f"q7_{index}", WIDTH) for index in range(18)]
hvars = [z3.BitVec(f"q6_{index}", WIDTH) for index in range(16)]
all_input_vars = list(pred_vars.values()) + xvars + yvars + rvars + hvars
'''
source = replace_once(source, old_declarations, new_declarations)

start = source.index('terminal_rows_omitted = os.environ.get("OMIT_TERMINAL", "0") == "1"\n')
end = source.index('\nsmt2 = solver.to_smt2().encode()\n', start)
extended = '''# First row not reimposed by the triangular parent: final G8 after Q7.
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

S_HJ = padd(pmul(source_data["A"], pderivative(J7, 1)),
             pmul(pderivative(H7, 0), source_data["vy"]),
             pscale(-1, pmul(source_data["uy"], pderivative(J7, 0))),
             pscale(-1, pmul(pderivative(H7, 1), source_data["vx"])))
terminal_rows_omitted = os.environ.get("OMIT_TERMINAL", "0") == "1"
terminal_polys = {}
for degree in range(7, 13):
    E1 = divide_three(degree_part(E, degree))
    F = padd(E1, degree_part(M, degree), degree_part(divWZ, degree))
    F1 = divide_three(F)
    G = padd(F1, degree_part(N, degree), degree_part(T, degree))
    G1 = divide_three(G)
    terminal_polys[degree] = padd(G1, degree_part(S_HJ, degree),
                                   degree_part(Rmix, degree))
    if not terminal_rows_omitted:
        constrain_row_zero(terminal_polys[degree], degree)
'''
source = source[:start] + extended + source[end:]

source = replace_once(
    source,
    '    "q7_explicit_source_row_count": 19,\n    "terminal_row_count": 46,\n',
    '    "q7_explicit_source_row_count": 19,\n'
    '    "final_g8_row_count": 9,\n'
    '    "q6_raw_variable_count": len(hvars),\n'
    '    "q6_explicit_source_row_count": 7,\n'
    '    "terminal_row_count": 63,\n')

source = replace_once(
    source,
    '''    rvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in rvars]
    assert all(0 <= value <= 2
               for value in pred_values + xvalues + yvalues + rvalues)
''',
    '''    rvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in rvars]
    hvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in hvars]
    assert all(0 <= value <= 2
               for value in pred_values + xvalues + yvalues + rvalues + hvalues)
''')
source = replace_once(
    source,
    '        "q7_values": rvalues,\n        "direct_integer_replay_required": True,\n',
    '        "q7_values": rvalues,\n'
    '        "q6_values": hvalues,\n'
    '        "direct_integer_replay_required": True,\n')
source = replace_once(
    source,
    'print("raw_variable_shapes", len(xvars), len(yvars), len(rvars))\n'
    'print("explicit_source_rows", 23, 22, 19, 46)\n',
    'print("raw_variable_shapes", len(xvars), len(yvars), len(rvars), len(hvars))\n'
    'print("explicit_source_rows", 23, 22, 19, 9, 7, 63)\n')

scope = {"__file__": str(PARENT), "__name__": "__global_q6_high_compiler__"}
exec(compile(source, str(PARENT), "exec"), scope)
