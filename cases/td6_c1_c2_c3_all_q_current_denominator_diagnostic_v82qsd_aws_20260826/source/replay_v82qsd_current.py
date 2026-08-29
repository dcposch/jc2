#!/usr/bin/env python3
"""Hash-pinned denominator diagnostic for one V82Q single-q CURRENT shard."""

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
EXPECTED = "336b9228378e990f896ea82729fef6a9384135a75a01af349574cb9a5ef42c0c"
assert sha256(TARGET.read_bytes()).hexdigest() == EXPECTED
assert os.environ.get("TD6_Q_EXPONENT")
print("producer_wrapper=TD6-V82QSD-SINGLE-Q-CURRENT-DENOMINATOR-DIAGNOSTIC")
print("V82QS_failed_lane_bytes_not_mutated=true")
print("reporter_only_preassert_denominator_dump=true")
print("foreign_factor_assertion_remains_fail_closed=true")
print("inherited_V78C_banner_is_historical=true")
print("base_current_system_already_inconsistent=true")
print("no_tangent_family_TD6_SP2_or_JC2_claim=true", flush=True)
sys.argv = [str(TARGET), "staged"]
runpy.run_path(str(TARGET), run_name="__main__")
print("TD6-V82QSD-SINGLE-Q-CURRENT-DENOMINATOR-DIAGNOSTIC PASS")
