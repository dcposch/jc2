#!/usr/bin/env python3
"""Raw-Q7 terminal gate on all 19 Q9 directions of the first predecessor."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path

ROOT = Path(os.environ["JC2_ROOT"])
RAW = (ROOT / "cases/as_fonly_d7_global_chart_qfbv_rawq7_20260825"
       / "solve_global_rawq7.py")
EXPECTED_RAW_SHA = (
    "69b908545775f4df1e10884c867cb767b8d1e997be33e386a730a2eaed585988")
payload = RAW.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_RAW_SHA
source = payload.decode()

old_tvars = (
    'tvars = [z3.BitVec(f"t{index}", WIDTH) for index in range(13)]')
new_tvars = (
    'tvars = [z3.BitVec(f"t{index}", WIDTH) for index in range(19)]')
assert source.count(old_tvars) == 1
source = source.replace(old_tvars, new_tvars)

old_chart = '''# Reuse only V1's symbolic chart construction and exact Q8 rows.
chart_fragment = (forced_marker
                  + source.split(forced_marker, 1)[1]
                  .split(components_marker, 1)[0])
exec(compile(chart_fragment, str(V1), "exec"), globals())'''
new_chart = '''# Reuse the exact Q8 rows, but replace the 13-trit Kuranishi chart header
# by the complete 19-dimensional Q9 affine fibre.
chart_fragment = (forced_marker
                  + source.split(forced_marker, 1)[1]
                  .split(components_marker, 1)[0])
tail_marker = "\\nC2 = homogeneous(2, xvalues_symbolic[0:3])\\n"
assert chart_fragment.count(tail_marker) == 1
chart_tail = chart_fragment.split(tail_marker, 1)[1]
chart_header = r"""
forced = {}
free_q9 = tuple(range(19))
q9_parameters = list(tvars)
xvalues_symbolic = []
for column in range(32):
    expression = bv(q9_origin[column])
    for index in range(19):
        expression = badd(expression,
                          bmul(q9_kernel[index][column], q9_parameters[index]))
    xvalues_symbolic.append(z3.URem(expression, bv(3)))
"""
chart_fragment = chart_header + tail_marker + chart_tail
exec(compile(chart_fragment, str(V1), "exec"), globals())'''
assert source.count(old_chart) == 1
source = source.replace(old_chart, new_chart)

old_dimension = '"q9_chart_dimension": 13,'
new_dimension = '"q9_chart_dimension": 19,'
old_scope = ('"scope": "complete accepted 13-trit Q9 chart with raw '
             'Q8/Q7 digits",')
new_scope = ('"scope": "complete 19-trit Q9 fibre over the first '
             'corrected-Q10 predecessor, with raw Q8/Q7 digits",')
assert source.count(old_dimension) == source.count(old_scope) == 1
source = source.replace(old_dimension, new_dimension).replace(
    old_scope, new_scope)

scope = {"__file__": str(RAW), "__name__": "__full_q9_rawq7__"}
exec(compile(source, str(RAW), "exec"), scope)
print("PASS-AS-FIRST-PREDECESSOR-FULL-Q9-RAWQ7")

