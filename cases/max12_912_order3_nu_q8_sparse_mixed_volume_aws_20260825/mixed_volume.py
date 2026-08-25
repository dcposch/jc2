#!/usr/bin/env python3
"""Exact sparse mixed volumes for the selected-Q8 projection slice."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from math import factorial
from pathlib import Path
import re
import subprocess
import sys


DIMENSION = 7
ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
RANK_RE = re.compile(r"\brank = (\d+)")
VOLUME_RE = re.compile(r"volume \(lattice normalized\) = ([0-9]+(?:/[0-9]+)?)")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_compiler():
    got = digest(COMPILER)
    if got != COMPILER_SHA256:
        raise RuntimeError(("compiler hash", got, COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("q8_mixed_volume_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def point_key(point):
    return tuple(int(value) for value in point)


def write_input(path: Path, points) -> None:
    points = sorted({point_key(point) for point in points})
    if not points or any(len(point) != DIMENSION for point in points):
        raise RuntimeError((path, points[:2]))
    lines = [f"amb_space {DIMENSION + 1}", f"polytope {len(points)}"]
    lines.extend(" ".join(map(str, point)) for point in points)
    path.write_text("\n".join(lines) + "\n")


def parse_normaliz(project: Path):
    text = project.with_suffix(".out").read_text()
    ranks = [int(value) for value in RANK_RE.findall(text)]
    if not ranks:
        raise RuntimeError(("missing rank", project))
    rank = max(ranks)
    headers = list(re.finditer(r"(?m)^(\d+) extreme rays:\s*$", text))
    if not headers:
        raise RuntimeError(("missing extreme rays", project))
    header = headers[-1]
    count = int(header.group(1))
    rows = []
    for line in text[header.end():].splitlines():
        stripped = line.strip()
        if not stripped:
            if rows:
                break
            continue
        fields = stripped.split()
        if len(fields) != DIMENSION + 1:
            if rows:
                break
            continue
        try:
            values = tuple(int(field) for field in fields)
        except ValueError:
            if rows:
                break
            continue
        if values[-1] != 1:
            raise RuntimeError(("nonintegral extreme ray", project, values))
        rows.append(values[:-1])
    if len(rows) != count:
        raise RuntimeError(("extreme count", project, count, len(rows)))
    volume_matches = VOLUME_RE.findall(text)
    if rank < DIMENSION + 1:
        ambient_normalized_volume = Fraction(0)
    else:
        if len(volume_matches) != 1:
            raise RuntimeError(("volume count", project, volume_matches))
        ambient_normalized_volume = Fraction(volume_matches[0])
    return {
        "rank": rank,
        "vertices": tuple(sorted(set(rows))),
        "ambient_normalized_volume": ambient_normalized_volume,
        "out_sha256": digest(project.with_suffix(".out")),
    }


def normaliz_hull_volume(points, project: Path):
    write_input(project.with_suffix(".in"), points)
    completed = subprocess.run(
        ["normaliz", "-V", "-x=1", str(project)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    project.with_suffix(".stdout").write_text(completed.stdout)
    project.with_suffix(".stderr").write_text(completed.stderr)
    if completed.returncode != 0:
        raise RuntimeError(("Normaliz", project, completed.returncode, completed.stderr))
    return parse_normaliz(project)


def minkowski(left, right):
    return {
        tuple(a + b for a, b in zip(x, y, strict=True))
        for x in left
        for y in right
    }


def mixed_volume(supports, work: Path, workers: int):
    if len(supports) != DIMENSION:
        raise RuntimeError(len(supports))
    work.mkdir(parents=True, exist_ok=False)
    vertices = {}
    volumes = {}
    records = {}
    for cardinality in range(1, DIMENSION + 1):
        masks = [
            mask for mask in range(1, 1 << DIMENSION)
            if mask.bit_count() == cardinality
        ]

        def calculate(mask):
            bit = (mask & -mask).bit_length() - 1
            previous = mask & ~(1 << bit)
            points = supports[bit] if previous == 0 else minkowski(
                vertices[previous], supports[bit]
            )
            result = normaliz_hull_volume(points, work / f"sum_{mask:03d}")
            return mask, result

        with ThreadPoolExecutor(max_workers=workers) as pool:
            for mask, result in pool.map(calculate, masks):
                vertices[mask] = result["vertices"]
                volumes[mask] = result["ambient_normalized_volume"]
                records[str(mask)] = {
                    "cardinality": mask.bit_count(),
                    "rank": result["rank"],
                    "vertex_count": len(result["vertices"]),
                    "ambient_normalized_volume": str(result["ambient_normalized_volume"]),
                    "normaliz_out_sha256": result["out_sha256"],
                }
    polarization = sum(
        (1 if (DIMENSION - mask.bit_count()) % 2 == 0 else -1) * volume
        for mask, volume in volumes.items()
    )
    divisor = factorial(DIMENSION)
    mixed = polarization / divisor
    if mixed.denominator != 1 or mixed < 0:
        raise RuntimeError(("mixed volume integrality", polarization, mixed))
    return {
        "polarization_normalized_volume_sum": str(polarization),
        "factorial_divisor": divisor,
        "mixed_volume": mixed.numerator,
        "subset_records": records,
    }


def standard_controls(work: Path, workers: int):
    zero = (0,) * DIMENSION
    segments = []
    for index in range(DIMENSION):
        unit = [0] * DIMENSION
        unit[index] = 1
        segments.append({zero, tuple(unit)})
    simplex = {zero}
    for index in range(DIMENSION):
        unit = [0] * DIMENSION
        unit[index] = 1
        simplex.add(tuple(unit))
    segment_result = mixed_volume(segments, work / "segments", workers)
    simplex_result = mixed_volume([simplex] * DIMENSION, work / "simplex", workers)
    if segment_result["mixed_volume"] != 1 or simplex_result["mixed_volume"] != 1:
        raise AssertionError((segment_result["mixed_volume"], simplex_result["mixed_volume"]))
    return {"coordinate_segments": 1, "repeated_standard_simplex": 1}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--skip-controls", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.workers <= 32:
        raise RuntimeError(args.workers)
    args.work.mkdir(parents=True, exist_ok=False)

    compiler = load_compiler()
    _, rows, imposed, names = compiler.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    if names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError(names)
    source_supports = [set(rows[ell]) for ell in imposed]
    line_support = {
        (1, 0, 0, 0, 0, 0, 1),  # w*x5
        (0, 0, 0, 0, 0, 1, 0),  # x3
        (0, 0, 0, 0, 0, 0, 1),  # x5
    }
    supports = source_supports + [line_support]
    zero = (0,) * DIMENSION
    augmented = [set(support) | {zero} for support in supports]

    raw_result = mixed_volume(supports, args.work / "raw", args.workers)
    affine_result = mixed_volume(augmented, args.work / "origin_augmented", args.workers)
    controls = {} if args.skip_controls else standard_controls(args.work / "controls", args.workers)
    payload = {
        "status": "PASS",
        "normaliz_version": subprocess.check_output(
            ["normaliz", "--version"], text=True
        ).splitlines()[0],
        "compiler_sha256": COMPILER_SHA256,
        "variables": names,
        "imposed_rows": list(imposed),
        "source_support_sizes": [len(support) for support in source_supports],
        "line_support": [list(point) for point in sorted(line_support)],
        "line_provenance": "a*w*x5+b*(x3-2*x5)+c*x5 after v=(x3-2*x5)/x5",
        "raw_torus": raw_result,
        "origin_augmented_affine_candidate": affine_result,
        "controls": controls,
        "scope": (
            "exact support mixed volumes only; affine number is a candidate degree "
            "upper bound pending intersection-cycle, localization, infinity, and "
            "higher-dimensional-component audit"
        ),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("Q8-SPARSE-MIXED-VOLUME")
    print("status=PASS")
    print("raw_torus_mixed_volume=" + str(raw_result["mixed_volume"]))
    print("origin_augmented_mixed_volume=" + str(affine_result["mixed_volume"]))
    print("controls=" + json.dumps(controls, sort_keys=True))
    print("output_sha256=" + digest(args.output))


if __name__ == "__main__":
    main()
