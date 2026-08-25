#!/usr/bin/env python3
"""V6 wrapper: classify ternary high-bit guards before V5 row analysis."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
V5 = (ROOT / "cases/as_fonly_d7_global_q5_q4_cartier_fitting_v5_symbolic_20260825"
      / "analyze_cartier_fitting_v5.py")
EXPECTED = "35edbf45a95acede123eab65240ce35a694c5a999788772e6a42baa9658f5c97"
payload = V5.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
source = payload.decode()

marker = '''replace_once(
    "assert len(row_assertions) == 76, len(row_assertions)",
    "assert len(row_assertions) == 63, len(row_assertions)")
'''
assert source.count(marker) == 1

injection = r"""replace_once(
    '''assertions = list(solver.assertions())
independent_assertions = []
restoration_bounds = []
row_assertions = []
for assertion in assertions:
    charged = variables(assertion) & restoration_names
    if not charged:
        independent_assertions.append(assertion)
    elif assertion.decl().kind() == z3.Z3_OP_ULEQ:
        assert len(charged) == 1
        restoration_bounds.append(assertion)
    else:
        mod_three_side(assertion)
        row_assertions.append(assertion)

assert len(restoration_bounds) == 30, len(restoration_bounds)
''',
    '''assertions = list(solver.assertions())
independent_assertions = []
restoration_bounds = []
restoration_high_zero = []
row_assertions = []
for assertion in assertions:
    charged = variables(assertion) & restoration_names
    if not charged:
        independent_assertions.append(assertion)
    elif assertion.decl().kind() == z3.Z3_OP_ULEQ:
        assert len(charged) == 1
        restoration_bounds.append(assertion)
    elif z3.is_eq(assertion):
        left, right = assertion.children()
        if is_zero(right):
            candidate = left
        elif is_zero(left):
            candidate = right
        else:
            candidate = None
        if (candidate is not None
                and candidate.decl().kind() == z3.Z3_OP_EXTRACT):
            assert len(charged) == 1
            assert candidate.num_args() == 1
            assert candidate.decl().params() == [31, 2]
            restoration_high_zero.append(assertion)
        else:
            mod_three_side(assertion)
            row_assertions.append(assertion)
    else:
        mod_three_side(assertion)
        row_assertions.append(assertion)

assert len(restoration_bounds) == 30, len(restoration_bounds)
assert len(restoration_high_zero) == 30, len(restoration_high_zero)
''')

replace_once(
    '''    "restoration_bound_count": len(restoration_bounds),
    "restoration_row_count": len(row_assertions),
''',
    '''    "restoration_bound_count": len(restoration_bounds),
    "restoration_high_zero_count": len(restoration_high_zero),
    "restoration_row_count": len(row_assertions),
''')

replace_once(
    '''print("restoration_rows", len(row_assertions), "variables", len(restoration))
''',
    '''print("restoration_rows", len(row_assertions), "variables", len(restoration),
      "bounds", len(restoration_bounds), "high_zero", len(restoration_high_zero))
''')

"""
source = source.replace(marker, injection + marker)

scope = {"__file__": str(V5), "__name__": "__cartier_fitting_v6__"}
exec(compile(source, str(V5), "exec"), scope)
