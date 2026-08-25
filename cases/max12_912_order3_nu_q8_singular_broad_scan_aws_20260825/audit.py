#!/usr/bin/env python3
"""Audit the exhaustive pure-Singular p=127 fixed-w matrix.

The script only parses exact Singular output and performs finite integer
subset-sum/cycle-type bookkeeping.  It does not run a Groebner basis.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BROAD = ROOT / "aws" / "p127_exhaustive_v1"
PRIOR = ROOT / "aws" / "p127_prior6"
INDEPENDENT = ROOT / "aws" / "independent_root_replay"
EXCLUDED = {1, 2, 63, 71, 95, 126}
RUNNER_SHA = "11084528be3c14935b4542677795240ecf9716daf4d901cd4f917557daeafcd7"
GENERATOR_SHA = "4af6f7eca198bcdf1e60151449e08099853669bd1d6965db3cddffa666032d2c"
DISPATCH_SHA = "055bb16d1595336e2bf5d6407229cbc87bda55eded4360eb1c9934fc8623bd3f"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def scalar(text: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}=(.*)$", text)
    if not match:
        raise AssertionError(f"missing {key}")
    return match.group(1).strip()


def polynomial_degree(poly: str) -> int:
    powers = [int(value) for value in re.findall(r"\bv\^(\d+)", poly)]
    if powers:
        return max(powers)
    return 1 if re.search(r"\bv\b", poly) else 0


def subset_sums(parts: list[int]) -> set[int]:
    sums = {0}
    for part in parts:
        sums |= {old + part for old in tuple(sums)}
    return sums


def audit_dispatch() -> dict[str, str | int]:
    meta_path = BROAD / "dispatch.meta"
    values_path = BROAD / "values.txt"
    meta = meta_path.read_text()
    values = [int(value) for value in values_path.read_text().split()]
    assert values == [value for value in range(1, 127) if value not in EXCLUDED]
    assert scalar(meta, "rc") == "0"
    assert scalar(meta, "expected_lane_count") == "120"
    assert scalar(meta, "prime") == "127"
    assert scalar(meta, "concurrency") == "88"
    assert scalar(meta, "values_sha256") == sha256(values_path)
    sources = re.findall(r"(?m)^source_sha256=([0-9a-f]{64})\s+(\S+)$", meta)
    found = {Path(path).name: digest for digest, path in sources}
    assert found == {
        "dispatch_p127.sh": DISPATCH_SHA,
        "run_one.sh": RUNNER_SHA,
        "generate.py": GENERATOR_SHA,
    }
    return {
        "dispatch_meta_sha256": sha256(meta_path),
        "values_sha256": sha256(values_path),
        "concurrency": 88,
    }


def audit_lane(lane: Path, expected_w: int, expected_suffix: str) -> dict:
    expected_name = f"q8_singular_p127_w{expected_w}_std_{expected_suffix}"
    assert lane.name == expected_name, (lane.name, expected_name)
    paths = {name: lane / name for name in (
        "result.out", "run.meta", "input.sing", "stderr.log", "generator.stderr"
    )}
    assert all(path.is_file() for path in paths.values())
    assert paths["generator.stderr"].stat().st_size == 0
    result = paths["result.out"].read_text()
    meta = paths["run.meta"].read_text()
    assert scalar(meta, "rc") == "0"
    assert scalar(meta, "prime") == "127"
    assert int(scalar(meta, "w_value")) == expected_w
    assert scalar(meta, "engine") == "std"
    assert scalar(meta, "input_sha256") == sha256(paths["input.sing"])
    assert scalar(meta, "stdout_sha256") == sha256(paths["result.out"])
    assert scalar(meta, "stderr_sha256") == sha256(paths["stderr.log"])
    sources = re.findall(r"(?m)^source_sha256=([0-9a-f]{64})\s+(\S+)$", meta)
    source_by_name = {}
    for digest, source_path in sources:
        name = Path(source_path).name
        if name == "generate.py" and "generic_fibre_grouping" in source_path:
            name = "generic_generate.py"
        source_by_name[name] = digest
    assert source_by_name["run_one.sh"] == RUNNER_SHA
    assert source_by_name["generate.py"] == GENERATOR_SHA

    assert scalar(result, "prime") == "127"
    assert int(scalar(result, "w_value")) == expected_w
    assert scalar(result, "fibre_dim") == "0"
    basis_size = int(scalar(result, "fibre_size"))
    assert basis_size > 0
    vector_space_dimension = int(scalar(result, "fibre_vdim"))
    assert vector_space_dimension in (189, 190)
    assert scalar(result, "v_elimination_size") == "1"
    eliminant_degree = int(scalar(result, "v_eliminant_degree"))
    assert eliminant_degree in (189, 190)
    assert scalar(result, "v_eliminant_squarefree_gcd_degree") == "0"
    factors = re.findall(r"(?m)^\s+_\[\d+\]=(.*)$", result)
    assert len(factors) == int(scalar(result, "rational_factor_entries"))
    degrees = sorted(polynomial_degree(poly) for poly in factors)
    assert all(degree > 0 for degree in degrees)
    assert sum(degrees) == eliminant_degree
    return {
        "w": expected_w,
        "factor_degrees": degrees,
        "factor_count": len(degrees),
        "groebner_basis_size": basis_size,
        "vector_space_dimension": vector_space_dimension,
        "eliminant_degree": eliminant_degree,
        "primitive_degree_190": vector_space_dimension == eliminant_degree == 190,
        "input_sha256": sha256(paths["input.sing"]),
        "result_sha256": sha256(paths["result.out"]),
        "stderr_sha256": sha256(paths["stderr.log"]),
        "lane": lane.name,
    }


def audit_independent_replay(rows_by_w: dict[int, dict]) -> list[dict]:
    replays = []
    for w_value in (25, 47):
        lane = INDEPENDENT / f"w{w_value}"
        result_path = lane / "result.out"
        input_path = lane / "input.sing"
        meta_path = lane / "run.meta"
        stderr_path = lane / "stderr.log"
        meta = meta_path.read_text()
        assert scalar(meta, "rc") == "0"
        assert scalar(meta, "prime") == "127"
        assert int(scalar(meta, "w_value")) == w_value
        assert scalar(meta, "input_sha256") == sha256(input_path)
        assert scalar(meta, "stdout_sha256") == sha256(result_path)
        assert scalar(meta, "stderr_sha256") == sha256(stderr_path)
        primary = rows_by_w[w_value]
        assert sha256(input_path) == primary["input_sha256"]
        assert sha256(result_path) == primary["result_sha256"]
        replays.append({
            "w": w_value,
            "input_sha256": sha256(input_path),
            "result_sha256": sha256(result_path),
            "stderr_sha256": sha256(stderr_path),
            "tag": scalar(meta, "tag"),
        })
    return replays


def main() -> None:
    dispatch = audit_dispatch()
    rows = []
    for w_value in range(1, 127):
        if w_value in EXCLUDED:
            lane = PRIOR / f"q8_singular_p127_w{w_value}_std_v1"
            suffix = "v1"
        else:
            lane = BROAD / f"q8_singular_p127_w{w_value}_std_v2"
            suffix = "v2"
        rows.append(audit_lane(lane, w_value, suffix))

    good_rows = [row for row in rows if row["primitive_degree_190"]]
    rows_by_w = {row["w"]: row for row in rows}
    independent_replays = audit_independent_replay(rows_by_w)
    common_sums = set(range(191))
    for row in good_rows:
        common_sums &= subset_sums(row["factor_degrees"])
    witness_25 = rows_by_w[25]["factor_degrees"]
    witness_47 = rows_by_w[47]["factor_degrees"]
    assert witness_25 == [2, 188]
    assert witness_47 == [1, 3, 186]
    proper_25 = subset_sums(witness_25) - {0, 190}
    proper_47 = subset_sums(witness_47) - {0, 190}
    assert not (proper_25 & proper_47)

    count_histogram = Counter(row["factor_count"] for row in rows)
    payload = {
        "status": "PASS",
        "scope": "all 126 nonzero p=127 fixed-w localized fibres, pure Singular std",
        "dispatch": dispatch,
        "independent_replays": independent_replays,
        "uniform_fibre_invariants": {
            "dimension": 0,
            "squarefree_gcd_degree": 0,
        },
        "primitive_degree_190_fibre_count": len(good_rows),
        "exceptional_fibres": [
            {
                "w": row["w"],
                "vector_space_dimension": row["vector_space_dimension"],
                "eliminant_degree": row["eliminant_degree"],
                "partition": row["factor_degrees"],
            }
            for row in rows if not row["primitive_degree_190"]
        ],
        "factor_count_histogram": dict(sorted(count_histogram.items())),
        "irreducible_fixed_fibres": [
            row["w"] for row in good_rows if row["factor_degrees"] == [190]
        ],
        "common_subset_sums_all_fibres": sorted(common_sums),
        "minimal_two_fibre_subset_sum_witness": {
            "w25_partition": witness_25,
            "w25_proper_subset_sums": sorted(proper_25),
            "w47_partition": witness_47,
            "w47_proper_subset_sums": sorted(proper_47),
            "proper_intersection": sorted(proper_25 & proper_47),
        },
        "large_cycle_witness": {
            "w": 63,
            "partition": next(row["factor_degrees"] for row in rows if row["w"] == 63),
            "power": 32,
            "result": "a single 157-cycle, conditional on a common generic monodromy action",
        },
        "rows": rows,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
