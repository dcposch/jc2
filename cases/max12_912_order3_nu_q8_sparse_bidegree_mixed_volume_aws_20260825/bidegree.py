#!/usr/bin/env python3
"""Exact affine-BKK bounds for the two P1xP1 projection degrees."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PARENT = ROOT / "cases/max12_912_order3_nu_q8_sparse_mixed_volume_aws_20260825/mixed_volume.py"
PARENT_SHA256 = "a6a516d6558cdceee02e7340ad179e0e142af653506bd0f5468ee8e2027267f9"
DIMENSION = 7


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_parent():
    got = digest(PARENT)
    if got != PARENT_SHA256:
        raise RuntimeError(("parent hash", got, PARENT_SHA256))
    spec = importlib.util.spec_from_file_location("q8_bidegree_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError(PARENT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=("vertical", "horizontal"), required=True)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--controls", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.workers <= 32:
        raise RuntimeError(args.workers)
    args.work.mkdir(parents=True, exist_ok=False)

    parent = load_parent()
    compiler = parent.load_compiler()
    _, rows, imposed, names = compiler.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    if names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError(names)
    source_supports = [set(rows[ell]) for ell in imposed]
    zero = (0,) * DIMENSION
    if args.kind == "vertical":
        # w=alpha: a divisor of class (1,0), hence intersection B.
        line_support = {zero, (1, 0, 0, 0, 0, 0, 0)}
        bounds_coordinate = "B"
        provenance = "generic vertical target fibre w=alpha"
    else:
        # v=beta becomes x3-(beta+2)*x5=0: class (0,1), hence intersection A.
        line_support = {
            (0, 0, 0, 0, 0, 1, 0),
            (0, 0, 0, 0, 0, 0, 1),
        }
        bounds_coordinate = "A"
        provenance = "generic horizontal target fibre v=beta, cleared as x3-(beta+2)*x5"
    supports = source_supports + [line_support]
    augmented = [set(support) | {zero} for support in supports]
    result = parent.mixed_volume(augmented, args.work / "origin_augmented", args.workers)
    controls = parent.standard_controls(args.work / "controls", args.workers) if args.controls else {}
    payload = {
        "status": "PASS",
        "kind": args.kind,
        "bounds_bidegree_coordinate": bounds_coordinate,
        "mixed_volume_bound": result["mixed_volume"],
        "origin_augmented": result,
        "line_support": [list(point) for point in sorted(line_support)],
        "line_provenance": provenance,
        "source_support_sizes": [len(support) for support in source_supports],
        "variables": names,
        "imposed_rows": list(imposed),
        "parent_sha256": PARENT_SHA256,
        "normaliz_version": subprocess.check_output(["normaliz", "--version"], text=True).splitlines()[0],
        "controls": controls,
        "class_convention": (
            "curve class (A,B) in P1_w x P1_v; vertical class (1,0) intersects B, "
            "horizontal class (0,1) intersects A; H has class (21,190)"
        ),
        "scope": "exact affine-BKK coordinate bound; cycle and generic-isolated-intersection hypotheses remain explicit",
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("Q8-SPARSE-BIDEGREE-MIXED-VOLUME")
    print("status=PASS")
    print("kind=" + args.kind)
    print("bounds_coordinate=" + bounds_coordinate)
    print("mixed_volume_bound=" + str(result["mixed_volume"]))
    print("controls=" + json.dumps(controls, sort_keys=True))
    print("output_sha256=" + digest(args.output))


if __name__ == "__main__":
    main()
