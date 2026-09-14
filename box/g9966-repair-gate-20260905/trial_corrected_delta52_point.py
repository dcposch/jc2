#!/usr/bin/env python3
"""Direct rational trial of delta52, independent of any full solver endpoint."""
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
import sys
import time

import sympy as sp

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
engine = HERE / "corrected_face_engine.py"
spec = importlib.util.spec_from_file_location("corrected_delta52_trial", engine)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
started = time.monotonic()
k2, inner, inner_metadata = m.build_major_h2("delta52", 8)
outer, outer_free, outer_metadata = m.outer_state(7)
all_free = inner | outer_free
point = dict.fromkeys(all_free, sp.Integer(0))
assert sp.Symbol("jet0") in point and sp.Symbol("c") in point
point[sp.Symbol("jet0")] = point[sp.Symbol("c")] = sp.Integer(1)


def specialize(tz, assignment):
    result = {}
    for tag, expression in tz.items():
        value = sp.expand(sp.sympify(expression).xreplace(assignment))
        assert not value.free_symbols and value.is_Rational
        if value != 0:
            result[tag] = value
    return result


def images(assignment):
    numeric_k2 = specialize(k2, assignment)
    numeric_outer = {name: specialize(block, assignment) for name, block in outer.items()}
    numeric_F, numeric_G = m.build_FG(numeric_k2, numeric_outer, 8)
    rows, accounting = m.cumulative_rows("delta52", 8, numeric_F, numeric_G)
    result = [(name, sp.expand(value.xreplace(assignment))) for name, value in rows]
    assert all(not value.free_symbols and value.is_Rational for _, value in result)
    return result, accounting


rows, accounting = images(point)
assert len(rows) == 1285
nonzero = [(label, str(value)) for label, value in rows if value != 0]
full_payload = "".join(f"{variable}={point[variable]}\n" for variable in sorted(point, key=str))
image_payload = "".join(f"{label}\t{value}\n" for label, value in rows)
negative = dict(point)
assert negative[sp.Symbol("B1c_0_32")] == 0
negative[sp.Symbol("B1c_0_32")] = sp.Integer(1)
negative_rows, _ = images(negative)
negative_nonzero = [(label, str(value)) for label, value in negative_rows if value != 0]
assert negative_nonzero
assert dict(negative_rows)["stage1_J_d162_k35"] == -864
assert dict(negative_rows)["stage1_J_d162_k43"] == -864 * comb(127, 8)
result = {
    "status": "PASS_EXACT_RATIONAL_POINT" if not nonzero else "TRIAL_FAILED_NONCONCLUSIVE",
    "field": "Q", "branch": "delta52", "stage": 8,
    "scope": "corrected-face diagnostic coefficient chart, not a Keller pair",
    "no_solver_endpoint_read": True,
    "substitution_before_FG_multiplication": True,
    "engine_sha256": hashlib.sha256(engine.read_bytes()).hexdigest(),
    "inner_free_count": len(inner), "outer_free_count": len(outer_free),
    "all_free_count": len(all_free),
    "nonzero_assignment": {"jet0": "1", "c": "1"},
    "all_other_all_free_variables": "0",
    "full_assignment_sha256": hashlib.sha256(full_payload.encode()).hexdigest(),
    "row_count": len(rows), "nonzero_row_count": len(nonzero),
    "first_ten_nonzero_rows": nonzero[:10],
    "raw_images_sha256": hashlib.sha256(image_payload.encode()).hexdigest(),
    "old_unit_row": {"label": "stage8_G_local16_coord0",
                     "new_value": str(dict(rows)["stage8_G_local16_coord0"])},
    "localizer": {"c": "1", "Zc": "1", "equation_image": "0",
                  "zero_c_negative_image": "-1"},
    "negative_control": {"perturbation": "B1c_0_32: 0 -> 1",
                         "nonzero_row_count": len(negative_nonzero),
                         "first_five_nonzero_rows": negative_nonzero[:5],
                         "independently_expected_J43": str(-864 * comb(127, 8))},
    "row_accounting": accounting,
    "elapsed_seconds": round(time.monotonic() - started, 3),
}
print(json.dumps(result, indent=2, sort_keys=True))
