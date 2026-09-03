#!/usr/bin/env python3
"""Replay the charged K=16, t=5 heuristic normalisation from frozen inputs."""

from __future__ import annotations

import argparse
import importlib.util
import pathlib
import sys


FROZEN = pathlib.Path("/tmp/jc2-lane.80iWiG/inputs")
PIPELINE = FROZEN / "k16t56_pipeline.py"


def load_pipeline():
    spec = importlib.util.spec_from_file_location("k16t56_pipeline_frozen", PIPELINE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {PIPELINE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.LANE_INPUTS = FROZEN
    module.EXPECTED = {
        key: value
        for key, value in module.EXPECTED.items()
        if key in {"t_order_system.py", "triangular_preprocess.py"}
    }
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        type=pathlib.Path,
        default=pathlib.Path("box/k16t5gate-20260903"),
    )
    parser.add_argument("--run-singular", action="store_true")
    parser.add_argument("--singular-timeout", type=int, default=180)
    args = parser.parse_args()

    pipeline = load_pipeline()
    pipeline.run_pipeline(
        t=5,
        order="heuristic",
        out_dir=args.out_dir,
        max_q_seconds=900.0,
        max_a_seconds=2400.0,
        max_expression_bytes=80_000_000,
        max_terms=2_000_000,
        primes=tuple(pipeline.DEFAULT_PRIMES),
        run_singular=args.run_singular,
        singular_timeout=args.singular_timeout,
        skip_a=False,
    )


if __name__ == "__main__":
    main()
