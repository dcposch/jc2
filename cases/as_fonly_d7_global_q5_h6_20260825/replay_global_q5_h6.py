#!/usr/bin/env python3
"""Direct nested-integer replay for a global Q5/H6,J6 SAT model."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q6_high_20260825"
          / "replay_global_q6_high.py")
EXPECTED_PARENT_SHA = (
    "e8361c81609afe6365d5eba8d4fda9bdf4b3dd4a44869fbcba330c614847c77c")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()


def replace_once(text, old, new):
    assert text.count(old) == 1, (old[:80], text.count(old))
    return text.replace(old, new)


source = replace_once(
    source,
    'prefixes = ("pred_", "q9_", "q8_", "q7_", "q6_")',
    'prefixes = ("pred_", "q9_", "q8_", "q7_", "q6_", "q5_")')
source = replace_once(
    source,
    '''                | {f"q6_{index}" for index in range(16)})
''',
    '''                | {f"q6_{index}" for index in range(16)}
                | {f"q5_{index}" for index in range(14)})
''')
source = replace_once(
    source,
    '''hvalues = [model[f"q6_{index}"] for index in range(16)]
assignment = dict(zip(predecessor_names, predecessor_values))
''',
    '''hvalues = [model[f"q6_{index}"] for index in range(16)]
kvalues = [model[f"q5_{index}"] for index in range(14)]
assignment = dict(zip(predecessor_names, predecessor_values))
''')

start = source.index('S = nadd(nmul(source_data["A"], nderivative(J7, 1)),\n')
end = source.index('\nresult = {\n', start)
replacement = '''H6 = homogeneous_numeric(6, kvalues[:7])
J6 = homogeneous_numeric(6, kvalues[7:])
q5 = row(nadd(G(5), nderivative(H6, 0), nderivative(J6, 1)), 5)

def fourth_digit_cross(H, J):
    return nadd(nmul(source_data["A"], nderivative(J, 1)),
                nmul(nderivative(H, 0), source_data["vy"]),
                nscale(-1, nmul(source_data["uy"], nderivative(J, 0))),
                nscale(-1, nmul(nderivative(H, 1), source_data["vx"])))

carry = nadd(fourth_digit_cross(H7, J7),
             fourth_digit_cross(H6, J6))
recursive = {}
for degree in range(7, 13):
    recursive[degree] = row(nadd(divide_exact(G(degree), 3),
                                  degree_part(carry, degree),
                                  degree_part(Rmix, degree)), degree)

P5 = nadd(P, nscale(81, H6))
Q5 = nadd(Q, nscale(81, J6))
det_minus_one = nadd(
    nmul(nderivative(P5, 0), nderivative(Q5, 1)),
    nscale(-1, nmul(nderivative(P5, 1), nderivative(Q5, 0))),
    {(0, 0): -1})
literal = {degree: row(divide_exact(degree_part(det_minus_one, degree), 243),
                       degree) for degree in range(7, 13)}
assert literal == recursive

allow_omitted = os.environ.get("ALLOW_OMITTED_Q5_GATE", "0") == "1"
if allow_omitted:
    assert any(q5) or any(any(values) for values in recursive.values())
else:
    assert q5 == [0] * 6
    assert all(not any(values) for values in recursive.values())
    degree5 = degree_part(det_minus_one, 5)
    assert all(value % 243 == 0 for value in degree5.values())
'''
source = source[:start] + replacement + source[end:]

source = replace_once(
    source,
    '''    "q6_values": hvalues,
    "parent_rows": parent_rows,
''',
    '''    "q6_values": hvalues,
    "q5_values": kvalues,
    "parent_rows": parent_rows,
''')
source = replace_once(
    source,
    '''    "q6_rows": q6,
    "recursive_literal_div243_degrees_12_to_7_agreement": True,
''',
    '''    "q6_rows": q6,
    "q5_rows": q5,
    "q5_gate_was_omitted": allow_omitted,
    "literal_degree5_divisible_243": (not allow_omitted),
    "recursive_literal_div243_degrees_12_to_7_agreement": True,
''')
source = replace_once(
    source,
    'print("row_shapes", 20, 5, 12, 11, 23, 22, 19, 9, 7, 63)\n',
    'print("row_shapes", 20, 5, 12, 11, 23, 22, 19, 9, 7, 6, 63)\n')
source = replace_once(
    source,
    '    "status": "PASS-GLOBAL-Q6-HIGH-DIRECT-REPLAY",\n',
    '    "status": "PASS-GLOBAL-Q5-H6-DIRECT-REPLAY",\n')
source = replace_once(
    source,
    'print("PASS-AS-GLOBAL-Q6-HIGH-DIRECT-REPLAY")\n',
    'print("PASS-AS-GLOBAL-Q5-H6-DIRECT-REPLAY")\n')

scope = {"__file__": str(PARENT), "__name__": "__global_q5_h6_replay__"}
exec(compile(source, str(PARENT), "exec"), scope)
