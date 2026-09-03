#!/usr/bin/env python3
"""Fail closed unless every promoted finite/artifact claim is present."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def text(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


charged = text("charged_input_check.out").splitlines()
assert len(charged) == 19 and all(line.endswith(": OK") for line in charged)
assert text("denominator_audit.out").startswith("DENOMINATOR_AUDIT_PASS\n")

axis = load("residual_b3_axis_exact_audit.json")
assert all(axis["assertions"].values())

array_fixed = text("array_recurrence_t2_t6.out")
assert array_fixed.count('"status": "PASS_RECORD"') == 10
assert '"checks": 10, "status": "ALL_PASS"' in array_fixed
array_split = text("array_recurrence_t11_split.out")
assert array_split.count('"status": "PASS_FORMULA"') == 2
assert '"checks": 2, "status": "ALL_PASS"' in array_split

for branch in (0, 1):
    stem = f"terminal_t2_split-exact_branch{branch}_all"
    assert load(stem + ".json")["status"] == "PASS"
    output = text(stem + ".out")
    assert "TOP_TAIL_UNIT" in output and "B4ZERO_FULL_UNIT" in output

for t in (3, 4):
    stem = f"terminal_t{t}_exact_all"
    assert load(stem + ".json")["status"] == "PASS"
    output = text(stem + ".out")
    assert "TOP_TAIL_UNIT" in output and "B4ZERO_FULL_UNIT" in output

top5 = load("top_tail_t5_exact.json")
assert top5["run"]["status"] == "PROVED_UNIT"
assert "G[1]=1" in text("top_tail_t5_exact.out")
top6 = load("top_tail_fast_t6_exact_integral.json")
assert top6["run"]["status"] == "INCONCLUSIVE_TIMEOUT"
assert top6["run"]["exit"] == 124
top6_output = text("top_tail_fast_t6_exact_integral.out")
assert "RECURRENCE_PASS t=6" in top6_output
assert "TOP_TAIL_UNIT" not in top6_output and "TOP_TAIL_NONUNIT" not in top6_output
structure = load("top_tail_structure_audit.json")
assert structure["degree_audit"]["t5"]["rows"][-1]["degrees"] == [2, 6, 4, 3]
assert all(
    item["quotient_dimension"] > 0
    for item in structure["modular_subsystem_audit"]["t5_branch0"]["leave_one_out"]
)

for t, powers in ((5, 4), (6, 5)):
    stem = f"terminal_t{t}_exact_residual"
    assert load(stem + ".json")["status"] == "PASS"
    output = text(stem + ".out")
    assert output.count("RADICAL_POWER variable=") == powers
    assert "B4ZERO_FULL_UNIT" in output

for branch in (0, 1):
    assert load(f"terminal_t6_mod_p1009_branch{branch}_none.json")["status"] == "PASS"

t11 = load("residual_t11_p1009_status.json")
checks = t11["groebner_checks"]
assert checks[0]["status"] == "INCONCLUSIVE_TIMEOUT" and checks[0]["exit_code"] == 124
assert checks[1]["status"] == "NOT_RUN_AFTER_FIRST_FIBRE_TIMEOUT"
claims = load("claim_status.json")
assert claims["verdict"] == "PARTIAL"
assert claims["fixed_characteristic_zero"]["new_terminal_ideal_unit"] == [5]

print("CLAIM_ARTIFACT_VALIDATION_PASS")
print("charged_inputs=19 fixed_record_fibres=10 split_t11_formula_fibres=2")
print("exact_top_tail_new=t5 exact_residual_new=t5,t6")
print("exact_top_tail_t6=INCONCLUSIVE_TIMEOUT")
print("t11_residual=INCONCLUSIVE_TIMEOUT")
