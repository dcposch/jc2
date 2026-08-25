#!/usr/bin/env python3
"""Aggregate selected-state widened-BV witness searches."""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter
from pathlib import Path

results = Path(os.environ["RESULTS_DIR"])
representatives = Path(os.environ["REPRESENTATIVES_FILE"])
rows = [line.split("\t") for line in representatives.read_text().splitlines()[1:]]
documents = []
stream = hashlib.sha256()
for state_text, label, signature in rows:
    payload = (results / f"state_{int(state_text):07d}.json").read_bytes()
    document = json.loads(payload)
    assert document["state_index"] == int(state_text)
    assert document["canonical_label"] == label
    assert document["presentation_signature"] == signature
    if document["solver_status"] == "sat":
        assert document["direct_integer_div243_replay"] == "PASS"
        assert document["smooth_hensel_surjective"] is False
    stream.update(hashlib.sha256(payload).digest())
    documents.append(document)

status_histogram = Counter(document["solver_status"] for document in documents)
sat = [document for document in documents if document["solver_status"] == "sat"]
aggregate = {
    "state_count": len(documents),
    "canonical_label_histogram": dict(sorted(Counter(
        document["canonical_label"] for document in documents).items())),
    "solver_status_histogram": dict(sorted(status_histogram.items())),
    "sat_state_indices": [document["state_index"] for document in sat],
    "sat_direct_replay_count": len(sat),
    "sat_smooth_hensel_surjective_count": sum(
        bool(document["smooth_hensel_surjective"]) for document in sat),
    "ordered_result_sha_merkle_stream_sha256": stream.hexdigest(),
    "unsat_is_theorem": False,
    "scope": "selected presentation representatives only",
}
encoded = (json.dumps(aggregate, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
(results / "aggregate.json").write_bytes(encoded)
print("state_count", len(documents))
print("canonical_label_histogram",
      json.dumps(aggregate["canonical_label_histogram"], sort_keys=True))
print("solver_status_histogram",
      json.dumps(aggregate["solver_status_histogram"], sort_keys=True))
print("sat_state_indices", aggregate["sat_state_indices"])
print("sat_direct_replay_count", len(sat))
print("sat_smooth_hensel_surjective_count",
      aggregate["sat_smooth_hensel_surjective_count"])
print("aggregate_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-FULLFIBRE-QFBV-AGGREGATE")

