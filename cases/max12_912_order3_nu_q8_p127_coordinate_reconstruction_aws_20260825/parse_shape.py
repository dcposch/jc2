#!/usr/bin/env python3
"""Audit and extract the 123 exact fixed-fibre lex shape bases."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re


PRIME = 127
COORDINATES = ("c", "d2", "d4", "x1", "x3", "x5", "inv")
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def parse_univariate(expression: str) -> dict[int, int]:
    expression = expression.replace(" ", "")
    if not expression:
        return {}
    terms = re.findall(r"[+-]?[^+-]+", expression)
    if "".join(terms) != expression:
        raise RuntimeError(("unparsed polynomial", expression))
    result: dict[int, int] = {}
    for raw in terms:
        sign = 1
        if raw[0] == "+":
            raw = raw[1:]
        elif raw[0] == "-":
            sign = -1
            raw = raw[1:]
        if not raw:
            raise RuntimeError(expression)
        if "v" not in raw:
            coefficient = sign * int(raw)
            degree = 0
        else:
            if raw == "v":
                coefficient, degree = sign, 1
            elif raw.startswith("v^"):
                coefficient, degree = sign, int(raw[2:])
            elif raw.endswith("*v"):
                coefficient, degree = sign * int(raw[:-2]), 1
            elif "*v^" in raw:
                coefficient_text, degree_text = raw.split("*v^", 1)
                coefficient, degree = sign * int(coefficient_text), int(degree_text)
            else:
                raise RuntimeError(("bad v term", raw, expression))
        result[degree] = (result.get(degree, 0) + coefficient) % PRIME
    return {degree: coefficient for degree, coefficient in result.items() if coefficient}


def candidate_at(payload: dict, w_value: int) -> dict[int, int]:
    result = {}
    for raw_v_degree, entries in payload["nonzero_support"].items():
        coefficient = sum(c * pow(w_value, d, PRIME) for d, c in entries) % PRIME
        if coefficient:
            result[int(raw_v_degree)] = coefficient
    return result


def parse_lane(lane: Path, w_value: int, candidate: dict) -> tuple[dict[str, list[int]], dict]:
    meta = (lane / "run.meta").read_text()
    if "\nrc=0\n" not in "\n" + meta:
        raise RuntimeError(("nonzero or unfinished lane", str(lane)))
    text = (lane / "result.out").read_text()
    expected_error = "   ? `redSB` is not defined"
    expected_line = "   ? error occurred in or before STDIN line 14: `G=redSB(G);`"
    if text.count(expected_error) != 1 or text.count(expected_line) != 1:
        raise RuntimeError(("unexpected historical redSB diagnostic", str(lane)))
    question_lines = [line for line in text.splitlines() if line.startswith("   ? ")]
    if question_lines != [expected_error, expected_line]:
        raise RuntimeError(("additional Singular diagnostic", str(lane), question_lines))
    if text.count("shape_basis_begin\n") != 1 or text.count("shape_basis_end\n") != 1:
        raise RuntimeError(("shape marker", str(lane)))
    shape = text.split("shape_basis_begin\n", 1)[1].split("shape_basis_end\n", 1)[0]
    basis = {}
    for line in shape.splitlines():
        match = re.fullmatch(r"G\[(\d+)\]=(.*)", line)
        if not match:
            raise RuntimeError(("shape line", str(lane), line[:100]))
        basis[int(match.group(1))] = match.group(2)
    if sorted(basis) != list(range(1, 9)):
        raise RuntimeError(("basis indices", str(lane), sorted(basis)))

    eliminants = []
    coordinate_values: dict[str, list[int]] = {}
    for expression in basis.values():
        hits = [name for name in COORDINATES if expression.startswith(name)]
        if not hits:
            eliminants.append(parse_univariate(expression))
            continue
        if len(hits) != 1:
            raise RuntimeError(("coordinate ambiguity", str(lane), expression[:100]))
        name = hits[0]
        tail = expression[len(name):]
        relation_tail = parse_univariate(tail)
        if max(relation_tail, default=-1) >= 190:
            raise RuntimeError(("coordinate v degree", str(lane), name))
        values = [0] * 190
        for degree, coefficient in relation_tail.items():
            values[degree] = (-coefficient) % PRIME
        coordinate_values[name] = values
    if len(eliminants) != 1 or set(coordinate_values) != set(COORDINATES):
        raise RuntimeError(("shape structure", str(lane), len(eliminants), sorted(coordinate_values)))
    H = eliminants[0]
    if H.get(190) != 1 or max(H) != 190:
        raise RuntimeError(("nonmonic eliminant", str(lane)))
    expected_H = candidate_at(candidate, w_value)
    if H != expected_H:
        raise RuntimeError(("candidate mismatch", str(lane), w_value))

    remainders = text.split("original_remainders_begin\n", 1)[1].split(
        "original_remainders_end\n", 1
    )[0].splitlines()
    if remainders != [f"original_remainders[{i}]=0" for i in range(1, 9)]:
        raise RuntimeError(("original remainder", str(lane), remainders))
    required = {
        "fibre_dim=0",
        "fibre_size=8",
        "fibre_vdim=190",
        "v_elimination_size=1",
        "v_eliminant_degree=190",
        "v_eliminant_squarefree_gcd_degree=0",
    }
    missing = [entry for entry in required if entry not in text]
    if missing:
        raise RuntimeError(("missing endpoint", str(lane), missing))
    custody = {
        "lane": str(lane),
        "input_sha256": digest(lane / "input.sing"),
        "stdout_sha256": digest(lane / "result.out"),
        "stderr_sha256": digest(lane / "stderr.log"),
        "meta_sha256": digest(lane / "run.meta"),
    }
    return coordinate_values, custody


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sweep-root", type=Path, required=True)
    parser.add_argument("--w25-lane", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if digest(args.candidate) != CANDIDATE_SHA256:
        raise RuntimeError(("candidate hash", digest(args.candidate)))
    candidate = json.loads(args.candidate.read_text())
    expected_values = [w for w in range(1, 127) if w not in (39, 56, 125)]
    samples = {name: [[] for _ in range(190)] for name in COORDINATES}
    custody = []
    for w_value in expected_values:
        lane = (
            args.w25_lane
            if w_value == 25
            else args.sweep_root / f"q8_p127_coordinate_shape_w{w_value}_v1"
        )
        values, lane_custody = parse_lane(lane, w_value, candidate)
        custody.append({"w": w_value, **lane_custody})
        for name in COORDINATES:
            for degree, coefficient in enumerate(values[name]):
                samples[name][degree].append(coefficient)
    result = {
        "status": "PASS",
        "scope": "123 exact fixed-fibre lex shape bases; not generic membership",
        "prime": PRIME,
        "w_values": expected_values,
        "coordinate_names": list(COORDINATES),
        "v_degree_bound": 189,
        "candidate_sha256": CANDIDATE_SHA256,
        "historical_nonfatal_diagnostic": "redSB undefined after stdfglm assignment",
        "all_original_remainders_zero": True,
        "all_candidate_specializations_match": True,
        "samples": samples,
        "custody": custody,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("Q8-P127-COORDINATE-SHAPE-AUDIT")
    print("status=PASS")
    print("fibre_count=123")
    print("coordinate_count=7")
    print("shape_relation_count=861")
    print("original_remainder_zero_count=984")
    print("candidate_match_count=123")
    print(f"output_sha256={digest(args.output)}")


if __name__ == "__main__":
    main()

