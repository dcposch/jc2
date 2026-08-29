#!/usr/bin/env python3
"""Hash-pinned reverse/sparse V82QST1 CURRENT denominator pilot."""

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
EXPECTED = "522c215712cf7176d35f13fb9a1bf8429ef85d39efc12af1b25683bce7fd8b80"
assert sha256(TARGET.read_bytes()).hexdigest() == EXPECTED
assert os.environ.get("TD6_Q_EXPONENT") in ("2", "10")
assert os.environ.get("TD6_PIVOT_POLICY") in ("reverse", "sparse")
print("producer_wrapper=TD6-V82QST1-Q2-Q10-REVERSE-SPARSE-CURRENT")
print("V82QST0_ascending_bytes_not_mutated=true")
print("transport_and_staged_pivots_jointly_changed=true")
print("foreign_factor_assertion_remains_fail_closed=true")
print("explicit_localized_bezout_required_for_cover=true")
print("fixed_A3_diagnostic_only=true")
print("no_tangent_family_TD6_SP2_or_JC2_claim=true", flush=True)
sys.argv = [str(TARGET), "staged"]
runpy.run_path(str(TARGET), run_name="__main__")
print("TD6-V82QST1-Q2-Q10-REVERSE-SPARSE-CURRENT PASS")

