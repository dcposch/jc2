#!/usr/bin/env python3
"""Run only the origin-augmented sparse mixed-volume calculation."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "cases/max12_912_order3_nu_q8_sparse_mixed_volume_aws_20260825/mixed_volume.py"
BASE_SHA256 = "a6a516d6558cdceee02e7340ad179e0e142af653506bd0f5468ee8e2027267f9"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_base():
    got = digest(BASE)
    if got != BASE_SHA256:
        raise RuntimeError(("base hash", got, BASE_SHA256))
    spec = importlib.util.spec_from_file_location("q8_mixed_volume_base", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.work.mkdir(parents=True, exist_ok=False)
    base = load_base()
    compiler = base.load_compiler()
    _, rows, imposed, names = compiler.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    if names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError(names)
    source_supports = [set(rows[ell]) for ell in imposed]
    line_support = {
        (1, 0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 1),
    }
    zero = (0,) * base.DIMENSION
    augmented = [support | {zero} for support in source_supports + [line_support]]
    result = base.mixed_volume(augmented, args.work / "origin_augmented", args.workers)
    payload = {
        "status": "PASS",
        "base_sha256": BASE_SHA256,
        "compiler_sha256": base.COMPILER_SHA256,
        "variables": names,
        "imposed_rows": list(imposed),
        "source_support_sizes": [len(support) for support in source_supports],
        "line_support": [list(point) for point in sorted(line_support)],
        "origin_augmented_affine_candidate": result,
        "scope": "affine-only independent shard; full controls remain in parent replay",
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("Q8-SPARSE-MIXED-VOLUME-AFFINE-SHARD")
    print("status=PASS")
    print("origin_augmented_mixed_volume=" + str(result["mixed_volume"]))
    print("output_sha256=" + digest(args.output))


if __name__ == "__main__":
    main()

