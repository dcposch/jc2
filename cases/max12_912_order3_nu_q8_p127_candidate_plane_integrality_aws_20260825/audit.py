#!/usr/bin/env python3
"""Fail-closed parser and subset-sum certificate for the Singular replay."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re


def scalar(text: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}=(.*)$", text)
    if not match:
        raise RuntimeError(("missing", key))
    return match.group(1).strip()


def block(text: str, name: str) -> list[int]:
    match = re.search(
        rf"(?ms)^factor_degrees_{name}_begin\n(.*?)^factor_degrees_{name}_end$",
        text,
    )
    if not match:
        raise RuntimeError(("block", name))
    return [int(value) for value in match.group(1).split()]


def proper_subset_sums(parts: list[int]) -> list[int]:
    return sorted({
        sum(parts[index] for index in range(len(parts)) if mask >> index & 1)
        for mask in range(1, (1 << len(parts)) - 1)
    })


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    text = args.result.read_text()
    if "   ?" in text:
        raise RuntimeError("Singular diagnostic")
    if "Q8-P127-CANDIDATE-PLANE-INTEGRALITY" not in text:
        raise RuntimeError("endpoint marker")
    if scalar(text, "degree_H25") != "190" or scalar(text, "degree_H47") != "190":
        raise RuntimeError("specialization degree")
    parts25 = sorted(block(text, "25"))
    parts47 = sorted(block(text, "47"))
    if parts25 != [2, 188] or parts47 != [1, 3, 186]:
        raise RuntimeError((parts25, parts47))
    if scalar(text, "factor_count_25") != "2" or scalar(text, "factor_count_47") != "3":
        raise RuntimeError("factor count")
    if scalar(text, "squarefree_gcd_degree_25") != "0":
        raise RuntimeError("w25 squarefree")
    if scalar(text, "squarefree_gcd_degree_47") != "0":
        raise RuntimeError("w47 squarefree")
    if scalar(text, "H_71_50") != "0":
        raise RuntimeError("rational point")
    hv = int(scalar(text, "Hv_71_50")) % 127
    if hv == 0:
        raise RuntimeError("singular rational point")
    sums25 = proper_subset_sums(parts25)
    sums47 = proper_subset_sums(parts47)
    intersection = sorted(set(sums25) & set(sums47))
    if intersection:
        raise RuntimeError(intersection)
    payload = {
        "status": "PASS",
        "prime": 127,
        "degree_v": 190,
        "partition_w25": parts25,
        "partition_w47": parts47,
        "proper_subset_sums_w25": sums25,
        "proper_subset_sums_w47": sums47,
        "proper_subset_sum_intersection": intersection,
        "rational_point": [71, 50],
        "H_at_rational_point": 0,
        "Hv_at_rational_point": hv,
        "arithmetic_irreducible": True,
        "geometrically_integral": True,
        "scope": "explicit candidate plane curve only; no quotient membership or component conclusion",
        "singular_stdout_sha256": sha256(args.result.read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("Q8-P127-CANDIDATE-PLANE-INTEGRALITY-AUDIT")
    print("status=PASS")
    print(f"Hv_71_50={hv}")
    print(f"output_sha256={sha256(args.output.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()

