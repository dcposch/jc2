#!/usr/bin/env python3
"""Hash-pinned wrapper for one V82Q single-q staged/current shard."""

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
EXPECTED = "792f42de85a935a7a09b799caefe6f5a0aeccec104f303dd21cfd43050116493"
assert sha256(TARGET.read_bytes()).hexdigest() == EXPECTED
assert os.environ.get("TD6_Q_EXPONENT")
print("producer_wrapper=TD6-V82QS-SINGLE-Q-CURRENT-ADJOINT")
print("inherited_V78C_banner_is_historical=true")
print("base_current_system_already_inconsistent=true")
print("no_tangent_family_TD6_SP2_or_JC2_claim=true", flush=True)
sys.argv = [str(TARGET), "staged"]
runpy.run_path(str(TARGET), run_name="__main__")
print("TD6-V82QS-SINGLE-Q-CURRENT-ADJOINT PASS")
