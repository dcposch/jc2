#!/usr/bin/env python3
"""Promote a validated V2 result only with target-first custody."""

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
    marker = "K00_ORDER=TARGETS_LOWERLOADS_FABER_GLOBAL"
    if sum(line == marker for line in lines) != 1:
        raise RuntimeError("missing or nonunique target-first marker")
    result = json.loads(args.base_result.read_text())
    compiler = json.loads(args.compiler_result.read_text())
    if compiler.get("monomial_order") != "(lp(4),dp(3),wp(1,8,7,6,5,4,3,2))":
        raise RuntimeError("wrong target-first monomial order")
    if compiler.get("all_loads_retained_as_polynomial_variables") is not True:
        raise RuntimeError("load-retention assertion missing")
    result.update({
        "status": "PASS-K00-TARGETFIRST-ENDPOINT",
        "algorithm": compiler["algorithm"],
        "monomial_order": compiler["monomial_order"],
        "variable_order": compiler["variable_order"],
        "order_marker": marker,
        "compiler_result_sha256": digest(args.compiler_result),
        "base_validation_result_sha256": digest(args.base_result),
    })
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
