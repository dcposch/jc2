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
EXPECTED = "ccf6f89292855fa94e01f93f582ba31d454b784618d73e60b390a0d54e2f6ce0"
assert sha256(TARGET.read_bytes()).hexdigest() == EXPECTED
assert os.environ.get("TD6_Q_EXPONENT")
print("producer_wrapper=TD6-V82QST0-SINGLE-Q-CURRENT-REDUCED-COORDINATE-DIAGNOSTIC")
print("V82QS_failed_lane_bytes_not_mutated=true")
print("reporter_only_preassert_denominator_dump=true")
print("foreign_factor_assertion_remains_fail_closed=true")
print("reduced_coordinate_numerator_denominator_residue_dump_preassert=true")
print("inherited_V78C_banner_is_historical=true")
print("base_current_system_already_inconsistent=true")
print("no_tangent_family_TD6_SP2_or_JC2_claim=true", flush=True)
sys.argv = [str(TARGET), "staged"]
runpy.run_path(str(TARGET), run_name="__main__")
print("TD6-V82QST0-SINGLE-Q-CURRENT-REDUCED-COORDINATE-DIAGNOSTIC PASS")
