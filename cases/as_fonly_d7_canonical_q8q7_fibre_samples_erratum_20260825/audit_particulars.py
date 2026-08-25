#!/usr/bin/env python3
"""Pin the 64 zero fibre-coordinates and their affine Q8 particulars."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

root = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
source = (root / "cases/as_fonly_d7_canonical_q8q7_fibre_samples_20260825"
          / "results_as_canonical_q8q7_samples_20260825T041000Z")
records = []
for index in range(64):
    path = source / f"sample_{index:02d}.json"
    payload = path.read_bytes()
    document = json.loads(payload)
    assert document["sample_index"] == index
    assert document["status"] == "q7_zero_locus_solved"
    assert document["q9_rows_zero"] is True
    assert document["q8_rank_pair"] == [13, 13]
    assert document["q8_fibre_dimension"] == 19
    assert document["q7_rank"] == 9
    assert document["q7_cokernel_dimension"] == 10
    assert document["first_witness"] == [0] * 19
    particular = document["q8_particular"]
    assert len(particular) == 32 and set(particular) <= {0, 1, 2}
    records.append({
        "sample_index": index,
        "sample_json_sha256": hashlib.sha256(payload).hexdigest(),
        "q9_parameters": document["q9_parameters"],
        "rref_fibre_coordinate": [0] * 19,
        "q8_affine_particular": particular,
        "q8_affine_particular_sha256": hashlib.sha256(bytes(particular)).hexdigest(),
        "q8_affine_particular_nonzero_support": [
            i for i, value in enumerate(particular) if value],
    })
result = {
    "sample_count": len(records),
    "zero_particular_count": sum(not any(r["q8_affine_particular"])
                                 for r in records),
    "nonzero_particular_count": sum(any(r["q8_affine_particular"])
                                    for r in records),
    "records": records,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("sample_count", result["sample_count"])
print("zero_particular_count", result["zero_particular_count"])
print("nonzero_particular_count", result["nonzero_particular_count"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-Q8-PARTICULAR-ERRATUM-AUDIT")

