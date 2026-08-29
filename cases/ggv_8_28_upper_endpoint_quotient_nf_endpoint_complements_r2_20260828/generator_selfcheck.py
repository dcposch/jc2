#!/usr/bin/env python3
"""Exact source-level negative/mutation gate for generated Singular scripts."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
from pathlib import Path


def load(path: Path):
    spec = importlib.util.spec_from_file_location("recursor", path)
    if spec is None or spec.loader is None:
        raise SystemExit("RECURSOR_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, type=Path)
    parser.add_argument("--recursor", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    module = load(args.recursor.resolve())
    base = args.base.resolve()
    label, zeros, factor, remaining, assignment, counts = module.source_inputs(
        base, "q1p03")
    delta_path = base / "output/q1p03/Q1P03_CHART_DELTA.txt"
    generators = [module.clean_poly(factor),
                  module.clean_poly(delta_path.read_text())]
    script = module.build_reduce_script(remaining, generators, 1, label,
                                        assignment)
    forbidden = ("REDUCER_PLACEHOLDER", "PLACEHOLDER", "TODO")
    if any(token in script for token in forbidden):
        raise SystemExit("GENERATED_PLACEHOLDER_SURVIVED")
    required = (
        "reduce(B[i,j],NODE_SB)",
        "NF_RATIONAL_UNIT_PIVOT_COUNT=",
        "FATAL_95_PIVOT_REPLAY",
        "NODE_REDUCE_COMPLETE=1",
    )
    if any(token not in script for token in required):
        raise SystemExit("GENERATED_REQUIRED_TOKEN_MISSING")
    mutation_rejected = False
    try:
        module.finalize_script([script, "REDUCER_PLACEHOLDER"])
    except RuntimeError as exc:
        mutation_rejected = "UNRESOLVED_GENERATOR_TOKEN" in str(exc)
    if not mutation_rejected:
        raise SystemExit("PLACEHOLDER_MUTATION_NOT_REJECTED")
    source_text = args.recursor.read_text()
    if '"NF_RATIONAL_UNIT_PIVOT_COUNT=95"' not in source_text:
        raise SystemExit("PIVOT_CERTIFICATE_MARKER_NOT_REQUIRED")
    args.output.write_text(script)
    print(f"COMPONENT=q1p03")
    print(f"GENERATED_SCRIPT_SHA256={hashlib.sha256(script.encode()).hexdigest()}")
    print("GENERATED_PLACEHOLDER_CENSUS=0")
    print("PLACEHOLDER_MUTATION_REJECTED=1")
    print("PIVOT_CERTIFICATE_MARKER_REQUIRED=1")
    print("ENDPOINT_COMPLEMENT_GENERATOR_SELFCHECK_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
