#!/usr/bin/env python3
"""Replay the exact bounded invariant-relation falsifier."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys


CASE = Path(__file__).resolve().parent
ROOT = CASE.parents[1]
WORKER = CASE / "modular_support.py"
RESULT = CASE / "order48-p2003-v522.json"
PINS = {
    WORKER: "c36d6cf1ca538a39923412075fb44be77ed30023107f4eac755722b7d796dea0",
    RESULT: "e67c39e5394eb4ef285fcae722e318b75d5e2c02dd8638a7920d0dc4ce97841d",
}


def main():
    for path, expected in PINS.items():
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    command = [
        sys.executable, str(WORKER),
        "--prime", "2003", "--root", "522", "--order", "48",
        "--max-left", "10", "--max-right", "10",
        "--max-columns", "36", "--holdout", "8",
    ]
    result = subprocess.run(
        command, cwd=ROOT, text=True, capture_output=True,
        timeout=180, check=False,
    )
    if result.returncode:
        raise RuntimeError((result.returncode, result.stdout, result.stderr))
    if json.loads(result.stdout) != json.loads(RESULT.read_text()):
        raise RuntimeError("modular support replay mismatch")
    payload = json.loads(result.stdout)
    searches = payload["relation_searches"]
    if not all(
        value["all_fit_matrices_full_column_rank"]
        and value["tested_rectangles"] == 53
        and value["full_column_rank_rectangles"] == 53
        and not value["hits"]
        for value in searches.values()
    ):
        raise RuntimeError("bounded relation certificate mismatch")
    replay = {
        "case": payload["case"],
        "worker_sha256": PINS[WORKER],
        "result_sha256": PINS[RESULT],
        "reduction": {"prime": 2003, "q8_root": 522},
        "hensel_order": 48,
        "fit_coefficients": "w^0 through w^39",
        "holdout_coefficients": "w^40 through w^47",
        "tested_pairs": sorted(searches),
        "rectangles_per_pair": 53,
        "rectangle_rule": (
            "1<=left_degree,right_degree<=10 and "
            "(left_degree+1)*(right_degree+1)<=36"
        ),
        "all_fit_matrices_full_column_rank": True,
        "conclusion": (
            "no rational plane relation exists in any tested rectangle for "
            "the selected characteristic-zero Q8 branch"
        ),
        "scope": (
            "bounded relation exclusion only; no global equation, genus, "
            "projective boundary, or trajectory conclusion"
        ),
    }
    print(json.dumps(replay, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
