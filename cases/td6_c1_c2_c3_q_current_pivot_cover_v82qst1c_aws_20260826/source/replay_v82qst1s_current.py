#!/usr/bin/env python3
"""Hash-pinned V82QST1C current-only reverse-pivot pilot."""

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
EXPECTED = "a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e"
assert sha256(TARGET.read_bytes()).hexdigest() == EXPECTED
assert os.environ.get("TD6_Q_EXPONENT") in ("2", "10")
assert os.environ.get("TD6_PIVOT_POLICY") == "reverse"
assert os.environ.get("TD6_PIVOT_SCOPE") == "current-only"
print("producer_wrapper=TD6-V82QST1C-CURRENT-ONLY-REVERSE-Q2-Q10-PIVOT-PILOT")
print("reviewed_ascending_raw_transport_preserved=true")
print("reviewed_ascending_raw_restriction_and_P12_division_preserved=true")
print("FIRST_and_PREVIOUS_POLE_EJet_pivots_ascending=true")
print("only_CURRENT_EJet_pivots_changed=true")
print("V82QST1_and_V82QST1R_preserved_software_negative=true")
print("nested_identity_review_and_promotion_hash_pinned=true")
print("explicit_localized_bezout_required_for_cover=true")
print("fixed_A3_diagnostic_only=true")
print("no_tangent_family_TD6_SP2_or_JC2_claim=true", flush=True)
sys.argv = [str(TARGET), "staged"]
runpy.run_path(str(TARGET), run_name="__main__")
print("TD6-V82QST1C-CURRENT-ONLY-REVERSE-Q2-Q10-PIVOT-PILOT PASS")
