#!/usr/bin/env python3
"""Promote a validated V2 result only with V4 order custody."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stdout", type=Path)
    parser.add_argument("base_result", type=Path)
    parser.add_argument("compiler_result", type=Path)
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    lines = [line.strip() for line in args.stdout.read_text().splitlines()]
    marker = "K00_WEIGHT_ORDER=FABER_POSITIVE_GLOBAL_BLOCK"
    if sum(line == marker for line in lines) != 1:
        raise RuntimeError("missing or nonunique positive-block marker")
    result = json.loads(args.base_result.read_text())
    compiler = json.loads(args.compiler_result.read_text())
    if compiler.get("monomial_order") != "(wp(1,8,7,6,5,4,3,2),dp(7))":
        raise RuntimeError("wrong monomial order")
    if compiler.get("fail_fast_coded_exit_repair") is not True:
        raise RuntimeError("coded-exit repair not recorded")
    result.update({
        "status": "PASS-K00-WEIGHTED-BLOCK-ENDPOINT",
        "algorithm": compiler["algorithm"],
        "monomial_order": compiler["monomial_order"],
        "weighted_order_marker": marker,
        "compiler_result_sha256": digest(args.compiler_result),
        "base_validation_result_sha256": digest(args.base_result),
    })
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
