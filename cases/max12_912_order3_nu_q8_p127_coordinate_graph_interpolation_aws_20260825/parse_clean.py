#!/usr/bin/env python3
"""Fail-closed audit/extraction of all 126 clean fixed-w shape bases."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re


P = 127
GOOD_EXCLUSIONS = {39, 56, 125}
COORDINATES = ("c", "d2", "d4", "x1", "x3", "x5", "inv")
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_helpers(path: Path):
    spec = importlib.util.spec_from_file_location("q8_historical_shape_helpers", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_basis(text: str, lane: Path) -> dict[int, str]:
    if text.count("shape_basis_begin\n") != 1 or text.count("shape_basis_end\n") != 1:
        raise RuntimeError(("shape markers", str(lane)))
    block = text.split("shape_basis_begin\n", 1)[1].split("shape_basis_end\n", 1)[0]
    basis: dict[int, str] = {}
    for line in block.splitlines():
        match = re.fullmatch(r"G\[(\d+)\]=(.*)", line)
        if not match:
            raise RuntimeError(("shape line", str(lane), line[:120]))
        basis[int(match.group(1))] = match.group(2)
    if sorted(basis) != list(range(1, len(basis) + 1)):
        raise RuntimeError(("basis indices", str(lane), sorted(basis)))
    return basis


def parse_good_basis(
    basis: dict[int, str], candidate: dict, w_value: int, helpers, lane: Path
) -> dict[str, list[int]]:
    if len(basis) != 8:
        raise RuntimeError(("good basis size", str(lane), len(basis)))
    eliminants: list[dict[int, int]] = []
    coordinate_values: dict[str, list[int]] = {}
    for expression in basis.values():
        hits = [name for name in COORDINATES if expression.startswith(name)]
        if not hits:
            eliminants.append(helpers.parse_univariate(expression))
            continue
        if len(hits) != 1:
            raise RuntimeError(("coordinate ambiguity", str(lane), expression[:120]))
        name = hits[0]
        tail = helpers.parse_univariate(expression[len(name) :])
        if max(tail, default=-1) >= 190:
            raise RuntimeError(("coordinate degree", str(lane), name))
        values = [0] * 190
        for degree, coefficient in tail.items():
            values[degree] = (-coefficient) % P
        coordinate_values[name] = values
    if len(eliminants) != 1 or set(coordinate_values) != set(COORDINATES):
        raise RuntimeError(("good shape structure", str(lane)))
    expected = helpers.candidate_at(candidate, w_value)
    if eliminants[0] != expected:
        raise RuntimeError(("candidate specialization", str(lane), w_value))
    return coordinate_values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean-root", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--helpers", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if digest(args.candidate) != CANDIDATE_SHA256:
        raise RuntimeError(("candidate hash", digest(args.candidate)))
    candidate = json.loads(args.candidate.read_text())
    helpers = load_helpers(args.helpers)
    samples = {name: [[] for _ in range(190)] for name in COORDINATES}
    good_values: list[int] = []
    custody: list[dict] = []
    exceptional: dict[str, dict] = {}

    for w_value in range(1, P):
        lane = args.clean_root / f"q8_p127_coordinate_shape_clean_all_v2_w{w_value}"
        required = [lane / name for name in ("input.sing", "result.out", "stderr.log", "run.meta")]
        if any(not path.is_file() for path in required):
            raise RuntimeError(("missing lane bytes", str(lane)))
        meta = (lane / "run.meta").read_text()
        if "\nrc=0\n" not in "\n" + meta:
            raise RuntimeError(("lane endpoint", str(lane)))
        text = (lane / "result.out").read_text()
        diagnostic_lines = [line for line in text.splitlines() if line.startswith("   ? ")]
        if diagnostic_lines:
            raise RuntimeError(("Singular diagnostics", str(lane), diagnostic_lines[:5]))
        if text.count("Q8-P127-LEX-COORDINATE-RECONSTRUCTION-CLEAN") != 1:
            raise RuntimeError(("clean marker", str(lane)))
        if f"w_value={w_value}" not in text:
            raise RuntimeError(("w marker", str(lane)))
        remainder_block = text.split("original_remainders_begin\n", 1)[1].split(
            "original_remainders_end\n", 1
        )[0].splitlines()
        expected_remainders = [f"original_remainders[{i}]=0" for i in range(1, 9)]
        if remainder_block != expected_remainders:
            raise RuntimeError(("source remainder", str(lane), remainder_block))
        basis = parse_basis(text, lane)
        record = {
            "w": w_value,
            "basis_size": len(basis),
            "input_sha256": digest(lane / "input.sing"),
            "stdout_sha256": digest(lane / "result.out"),
            "stderr_sha256": digest(lane / "stderr.log"),
            "meta_sha256": digest(lane / "run.meta"),
        }
        custody.append(record)
        if w_value in GOOD_EXCLUSIONS:
            expected_size = 9 if w_value == 39 else 8
            expected_vdim = 190 if w_value == 39 else 189
            for marker in (
                "fibre_dim=0",
                f"fibre_size={expected_size}",
                f"fibre_vdim={expected_vdim}",
                "v_eliminant_degree=189",
                "v_eliminant_squarefree_gcd_degree=0",
            ):
                if marker not in text:
                    raise RuntimeError(("exceptional endpoint", str(lane), marker))
            if len(basis) != expected_size:
                raise RuntimeError(("exceptional basis size", str(lane), len(basis)))
            exceptional[str(w_value)] = {
                "basis_size": len(basis),
                "fibre_vdim": expected_vdim,
                "v_eliminant_degree": 189,
            }
            continue

        for marker in (
            "fibre_dim=0",
            "fibre_size=8",
            "fibre_vdim=190",
            "v_eliminant_degree=190",
            "v_eliminant_squarefree_gcd_degree=0",
        ):
            if marker not in text:
                raise RuntimeError(("good endpoint", str(lane), marker))
        values = parse_good_basis(basis, candidate, w_value, helpers, lane)
        good_values.append(w_value)
        for name in COORDINATES:
            for v_degree, coefficient in enumerate(values[name]):
                samples[name][v_degree].append(coefficient)

    if len(custody) != 126 or len(good_values) != 123:
        raise RuntimeError((len(custody), len(good_values)))
    result = {
        "status": "PASS",
        "scope": "clean fixed-fibre shape audit; no generic graph claim",
        "prime": P,
        "candidate_sha256": CANDIDATE_SHA256,
        "all_source_remainders_zero": True,
        "singular_diagnostic_count": 0,
        "fibre_count": 126,
        "good_fibre_count": 123,
        "good_w_values": good_values,
        "exceptional": exceptional,
        "coordinate_names": list(COORDINATES),
        "samples": samples,
        "custody": custody,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("Q8-P127-CLEAN-GRAPH-SHAPE-AUDIT")
    print("status=PASS")
    print("fibre_count=126")
    print("good_fibre_count=123")
    print("exceptional=39:190/189,56:189/189,125:189/189")
    print("source_remainder_zero_count=1008")
    print("singular_diagnostic_count=0")
    print(f"output_sha256={digest(args.output)}")


if __name__ == "__main__":
    main()
