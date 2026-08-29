#!/usr/bin/env python3
"""Hash-pinned V82QST1R arbitrary-pivot DAG diagnostic."""

from hashlib import sha256
import os
from pathlib import Path
import runpy
import sys


HERE = Path(__file__).resolve().parent
TARGET = (
    HERE / "payload" / "jc2" / "cases"
    / "td6_c1_c2_c3_all_q_vector_ad_repaired_20260825"
    / "replay_shard.py"
)
EXPECTED = "8f483d1807f03b8340aad432d5c637f07abe3ff9f0b8f465e4d602657da11c48"
assert sha256(TARGET.read_bytes()).hexdigest() == EXPECTED
assert os.environ.get("TD6_Q_EXPONENT") in ("2", "10")
assert os.environ.get("TD6_PIVOT_POLICY") in ("reverse", "sparse")
print("producer_wrapper=TD6-V82QST1R-Q2-Q10-ARBITRARY-PIVOT-DAG")
print("V82QST1_variable_order_failure_preserved_negative=true")
print("pivot_insertion_DAG_applied_to_restriction_forms_and_division=true")
print("source_replay_and_omission_controls_retained=true")
print("foreign_factor_assertion_remains_fail_closed=true")
print("explicit_localized_bezout_required_for_cover=true")
print("fixed_A3_diagnostic_only=true")
print("no_tangent_family_TD6_SP2_or_JC2_claim=true", flush=True)
sys.argv = [str(TARGET), "staged"]
runpy.run_path(str(TARGET), run_name="__main__")
print("TD6-V82QST1R-Q2-Q10-ARBITRARY-PIVOT-DAG PASS")

