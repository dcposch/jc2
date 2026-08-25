#!/usr/bin/env python3
"""Replay the bounded Q8 unordered-Hurwitz support certificate."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys


CASE = Path(__file__).resolve().parent
ROOT = CASE.parents[1]
WORKER = CASE / "hurwitz_support.py"
RESULT = CASE / "order48-p2003-v522.json"
PINS = {
    WORKER: "296bcd3484893ccdf379c0f8004dbfd7d2030b87e7dc5b6b279ff1edff6bd79c",
    RESULT: "2521b23f08b3a1767f4454e0542de9db2a14e747dfa6b990ca5e22be24600b60",
}


def main():
    for path, expected in PINS.items():
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    result = subprocess.run(
        [sys.executable, str(WORKER)], cwd=ROOT, text=True,
        capture_output=True, timeout=180, check=False,
    )
    if result.returncode:
        raise RuntimeError((result.returncode, result.stdout, result.stderr))
    actual, expected = json.loads(result.stdout), json.loads(RESULT.read_text())
    if actual != expected:
        raise RuntimeError("Hurwitz support replay mismatch")
    checks = actual["hurwitz_checks"]
    if not (
        checks["all_tau_odd_t_coefficients_zero"]
        and checks["all_Delta_odd_t_coefficients_zero"]
        and checks["s_constant"]
        and checks["NormF_constant"]
        and checks["NormW_constant"]
        and checks["E_t_coefficient"]
        and checks["tau_w_coefficient"]
        and checks["Delta_w_coefficient"]
    ):
        raise RuntimeError("generic leaf/etale certificate mismatch")
    searches = actual["relation_searches"]
    if not all(
        item["all_fit_matrices_full_column_rank"]
        and item["full_column_rank_rectangles"] == 53
        and not item["hits"]
        for item in searches.values()
    ):
        raise RuntimeError("Hurwitz relation rank certificate mismatch")
    payload = {
        "case": actual["case"],
        "worker_sha256": PINS[WORKER],
        "result_sha256": PINS[RESULT],
        "reduction": {"prime": 2003, "q8_root": 522},
        "hensel_order": 48,
        "fit_coefficients": "w^0 through w^39",
        "holdout_coefficients": "w^40 through w^47",
        "Hurwitz_even_descent": "PASS",
        "generic_leaf_and_etale_units": "PASS",
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
            "bounded unordered-Hurwitz relation exclusion only; no global "
            "equation, genus, projective boundary, or trajectory conclusion"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
