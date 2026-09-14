#!/usr/bin/env python3
"""Worker-only custody check of fresh frozen-driver certificate and graph samples."""
import csv
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
out = root / "d2-z55"
meta = json.loads((out / "99-delta2.build.json").read_text())
expected = {
    "canonical_primitive_generator_sequence_sha256": "a78c6a46e4b50dec6df51712c9c4b8d3c717b52490488d6819563cb5e18044fe",
    "singular_file_sha256": "a604ed314ced1a33ff46e43081c2222430f24bde96a10405a3a8562ec6dccbbc",
    "msolve_file_sha256": "7f593b87e40f02dbdb91f9b22aace6989f4a4d2092d9903276675b3265c7b572",
    "driver_sha256": "db7a83d6ec34c92c6c754c2b2a973da22aeac6b6c2847d2af141fc8e714add79",
    "shared_emitter_driver_sha256": "77ef23b86f655e08a11913cf838a037c82adbb89cd1bc4a7e86c6471d034be3e",
    "semantic_variable_count": 449,
    "emitted_generator_count": 466,
    "expanded_term_count": 6448959,
    "semantic_variable_order_sha256": "ee778e93b4293b9399761911d80dd71dd63b5fa95d21055cf50cd0db51428a4b",
    "solver_variable_order_sha256": "46e7a6a8bf467f6f7be994336c03fedf86bfacc139641711e4210605cd6438d5",
    "selected_T2_face_indices": [55],
    "emitted_nonzero_counts": {"T2_upper": 462, "T2_face": 1, "inverse": 3},
}
for key, value in expected.items():
    assert meta[key] == value, (key, meta.get(key), value)

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8*1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

for kind in ["singular", "msolve", "labels"]:
    assert sha(out / meta[f"{kind}_file"]) == meta[f"{kind}_file_sha256"]
assert sha(out / meta["variable_map_file"]) == meta["variable_map_sha256"]
with (out / meta["labels_file"]).open() as f:
    labels = list(csv.DictReader(f, delimiter="\t"))
assert len(labels) == 466
assert labels[462]["label"] == "T2_face_55"
assert all(row["block"] == "T2_upper" for row in labels[:462])
assert [row["label"] for row in labels[463:]] == ["inverse_T2", "inverse_T3", "inverse_separation"]
indexed = {row["label"]: row for row in labels}
samples = json.loads((root / "graph-generator-samples.json").read_text())
for sample in samples:
    row = indexed[sample["label"]]
    assert int(row["terms"]) == sample["terms"]
    assert row["primitive_sha256"] == sample["primitive_sha256"]
assert sum(int(row["terms"]) for row in labels) == 6448959
result = {
    "status": "PASS",
    "fresh_frozen_drivers": True,
    "all_expected_metadata_match": expected,
    "fresh_file_hashes_independently_recomputed": True,
    "independent_original_graph_sample_matches": samples,
    "labels_count": len(labels),
    "face_terms": int(labels[462]["terms"]),
    "build_wall_seconds": meta["build_wall_seconds"],
    "peak_RSS_KiB": meta["peak_RSS_KiB"],
    "singular_bytes": (out / meta["singular_file"]).stat().st_size,
    "msolve_bytes": (out / meta["msolve_file"]).stat().st_size,
    "audit_driver_sha256": sha(Path(__file__)),
}
(root / "subset-rebuild-check.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, indent=2, sort_keys=True), flush=True)
