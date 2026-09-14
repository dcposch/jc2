#!/usr/bin/env python3
"""Verify a serialized corrected-face point before building F/G; no joint solver."""
import argparse
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
parser = argparse.ArgumentParser()
parser.add_argument("--branch", choices=["delta2", "delta52"], default="delta2")
args = parser.parse_args()
branch = args.branch
stage = 4 if branch == "delta2" else 8
started = time.monotonic()
engine = HERE / "corrected_face_engine.py"
spec = importlib.util.spec_from_file_location("corrected_point_audit_engine", engine)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
source = HERE / f"face-{branch}/stage{stage}.json"
record = json.loads(source.read_text())
assert record["driver_sha256"] == hashlib.sha256(engine.read_bytes()).hexdigest()
certificate = record["necessary_chart_rational_point"]
assert certificate["status"] == "FOUND"
assert certificate["omitted_all_free_default"] == "0"
k2, inner_free, metadata = m.build_major_h2(branch, 8)
outer, outer_free, outer_metadata = m.outer_state(min(stage, 7))
all_free = inner_free | outer_free
point = dict.fromkeys(all_free, sp.Integer(0))
for name, value in certificate["nonzero_assignment"].items():
    variable = sp.Symbol(name)
    assert variable in point
    point[variable] = sp.Rational(value)
assert len(all_free) == certificate["all_free_count"]
payload = "".join(f"{variable}={point[variable]}\n" for variable in sorted(point, key=str))
point_hash = hashlib.sha256(payload.encode()).hexdigest()
assert point_hash == certificate["full_assignment_sha256"]
localizer = sp.Symbol("rho" if branch == "delta2" else "c")
wrapper = sp.Rational(certificate["localization_wrapper_value"])
assert point[localizer] != 0 and point[localizer] * wrapper == 1


def specialize(tz, assignment):
    result = {}
    for position, expression in tz.items():
        image = sp.expand(sp.sympify(expression).xreplace(assignment))
        assert not image.free_symbols
        assert image.is_Rational
        if image != 0:
            result[position] = image
    return result


def row_images(assignment):
    # This is deliberately BEFORE multiplication into the large F/G system.
    numeric_k2 = specialize(k2, assignment)
    numeric_outer = {name: specialize(block, assignment) for name, block in outer.items()}
    numeric_F, numeric_G = m.build_FG(numeric_k2, numeric_outer, 8)
    rows, accounting = m.cumulative_rows(branch, stage, numeric_F, numeric_G)
    # local_rows introduces the local-series coordinates, then evaluate them.
    images = [(label, sp.expand(expression.xreplace(assignment))) for label, expression in rows]
    assert all(not expression.free_symbols and expression.is_Rational for _, expression in images)
    return images, accounting


images, accounting = row_images(point)
assert accounting == record["row_accounting"]
assert len(images) == certificate["raw_rows_verified_zero"]
assert all(value == 0 for _, value in images)
zero_payload = "".join(f"{label}\t{value}\n" for label, value in images)
zero_hash = hashlib.sha256(zero_payload.encode()).hexdigest()
assert zero_hash == certificate["raw_zero_image_sha256"]
old_label = "stage4_J_d159_k35" if branch == "delta2" else "stage8_G_local16_coord0"
assert dict(images)[old_label] == 0

# This variable is free before joint elimination, with an active mandatory row.
perturbed_variable = sp.Symbol("B1c_0_32")
assert perturbed_variable in all_free and point[perturbed_variable] == 0
perturbed = dict(point)
perturbed[perturbed_variable] = sp.Integer(1)
negative_rows, _ = row_images(perturbed)
nonzero = [(label, str(value)) for label, value in negative_rows if value != 0]
assert nonzero
active_label = "stage1_J_d162_k43"
active_value = dict(negative_rows)[active_label]
# Direct top-form differentiation gives 864*(w-1)^127*w^35.
assert active_value == -864 * comb(127, 8)
assert dict(negative_rows)["stage1_J_d162_k35"] == -864
assert 0 * wrapper - 1 == -1
print(json.dumps({
    "status": "PASS", "branch": branch, "stage": stage, "field": "Q",
    "scope": "point of corrected-face diagnostic coefficient chart; not a Keller pair",
    "engine_sha256": hashlib.sha256(engine.read_bytes()).hexdigest(),
    "input_json_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "all_free_count": len(all_free),
    "full_assignment_sha256": point_hash,
    "nonzero_assignment": certificate["nonzero_assignment"],
    "substituted_before_FG_multiplication": True,
    "rows_independently_evaluated_zero": len(images),
    "raw_zero_image_sha256": zero_hash,
    "old_unit_row": {"label": old_label, "new_value": "0"},
    "localizer": {"variable": str(localizer), "value": str(point[localizer]),
                  "wrapper": str(wrapper), "rabinowitsch_equation_image": "0"},
    "negative_control": {"perturbation": f"{perturbed_variable}: 0 -> 1",
                         "nonzero_row_count": len(nonzero),
                         "first_five_nonzero_rows": nonzero[:5],
                         "known_active_row": {"label": active_label, "value": str(active_value)},
                         "zero_localizer_wrapper_image": "-1"},
    "elapsed_seconds": round(time.monotonic() - started, 3),
}, indent=2, sort_keys=True))
