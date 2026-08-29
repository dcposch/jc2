#!/usr/bin/env python3
"""Fail closed unless the exact provisional endpoint matches frozen p cutoffs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


EXPECTED = {"K10": 4, "K6": 3, "K2": 2}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    result = json.loads(args.result.read_text())
    if result.get("status") != "PASS-K00-FILTERED-LOAD-V18R2-PROVISIONAL-Q-ENDPOINT":
        raise RuntimeError("endpoint sentinel")
    actual = {label: result.get("directions", {}).get(label, {}).get("first_incompatible_cutoff") for label in EXPECTED}
    if actual != EXPECTED:
        raise RuntimeError(("exact cutoff differs from frozen modular target", actual, EXPECTED))
    for label, cutoff in EXPECTED.items():
        rows = result["directions"][label]["cutoffs"]
        if [entry["cutoff"] for entry in rows] != list(range(2, cutoff + 1)):
            raise RuntimeError(("incomplete exact cutoff chain", label, rows))
        if any(entry["replay"] != "PASS_EXACT_LIFT" for entry in rows[:-1]) or rows[-1]["replay"] != "PASS_EXACT_DUAL":
            raise RuntimeError(("exact replay branch", label, rows))
    print("K00_V18R2_EXACT_TARGET_GATE=PASS")
    print("K00_V18R2_EXACT_PATTERN=K10_D4_K6_D3_K2_D2")


if __name__ == "__main__":
    main()
