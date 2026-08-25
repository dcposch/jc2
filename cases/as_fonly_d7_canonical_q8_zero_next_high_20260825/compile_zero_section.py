#!/usr/bin/env python3
"""Exhaust the Q7 fibre over one canonical Q8 zero-section predecessor."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
PARENT = (ROOT / "cases/as_fonly_d7_q8state_next_high_samples_20260825"
          / "compile_state.py")
EXPECTED_PARENT_SHA = (
    "abfd5cfa79edb87e16e2df706f7466dcf335302d889cb71bf06bcdfb9609588e")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()

start_marker = 'family = os.environ["STATE_FAMILY"]\nsample_index = int(os.environ["SAMPLE_INDEX"])\n'
end_marker = "\nassert source_rows(source_data, xvalues) == [0] * 23\n"
assert source.count(start_marker) == 1
assert source.count(end_marker) == 1
prefix, tail = source.split(start_marker, 1)
_discard, suffix = tail.split(end_marker, 1)

replacement = r'''
family = "canonical_q8_zero_section"
sample_index = int(os.environ["SAMPLE_INDEX"])
assert 0 <= sample_index < 64
predecessor_path = (ROOT /
    "cases/as_fonly_d7_canonical_q8q7_fibre_samples_20260825" /
    "results_as_canonical_q8q7_samples_20260825T041000Z" /
    f"sample_{sample_index:02d}.json")
predecessor_bytes = predecessor_path.read_bytes()
predecessor = json.loads(predecessor_bytes)
assert predecessor["sample_index"] == sample_index
assert predecessor["status"] == "q7_zero_locus_solved"
assert predecessor["q9_rows_zero"] is True
assert predecessor["q8_rank_pair"] == [13, 13]
assert predecessor["q8_fibre_dimension"] == 19
assert predecessor["q7_rank"] == 9
assert predecessor["q7_cokernel_dimension"] == 10
assert predecessor["first_witness"] == [0] * 19
assert len(predecessor["q8_particular"]) == 32
xvalues = tuple(predecessor["xvalues"])
yvalues = tuple(predecessor["q8_particular"])
state_parameters = predecessor["q9_parameters"]
rank22, augmented22 = predecessor["q8_rank_pair"]
predecessor_sha256 = hashlib.sha256(predecessor_bytes).hexdigest()
'''

instrument = r'''
result["predecessor_sample_sha256"] = predecessor_sha256
result["predecessor_q9_parameters"] = predecessor["q9_parameters"]
result["predecessor_sample_kind"] = predecessor["sample_kind"]
'''
write_marker = "\nencoded = (json.dumps(result, sort_keys=True, separators=(\",\", \":\")) + \"\\n\").encode()\n"
rebuilt = prefix + replacement + end_marker + suffix
assert rebuilt.count(write_marker) == 1
rebuilt = rebuilt.replace(write_marker, "\n" + instrument + write_marker)
exec(compile(rebuilt, str(PARENT), "exec"), {"__file__": str(PARENT),
                                             "__name__": "__main__"})
