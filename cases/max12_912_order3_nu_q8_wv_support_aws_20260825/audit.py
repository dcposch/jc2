#!/usr/bin/env python3
"""Lightweight custody/semantic audit of the AWS `(w,v)` support run."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent
LANE = CASE / "aws/q8_wv_support_p10007_v1"
PARENT = ROOT / "cases/max12_912_order3_nu_q8_invariant_support_20260824/modular_support.py"

EXPECTED = {
    CASE / "wv_support.py":
        "22a2c8f651032c6aa3e9720a9c5a7ae880017b7b1289bbb47e8ebad4469affd3",
    CASE / "run_remote.sh":
        "82cf839dfb3d3c8747776aa412fefafcca716fc07f52f0faccf5b3d720356edd",
    PARENT:
        "c36d6cf1ca538a39923412075fb44be77ed30023107f4eac755722b7d796dea0",
    LANE / "result.json":
        "1e3e81739f214b37bd81bad378167baafd48d51a5691ef0dcf3f5af2e4fb8c31",
    LANE / "run.meta":
        "184e8a58361f28693fe3ce27f80494cb2bd30bb67a3f711d4535debd2811bae3",
    LANE / "stderr.log":
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    CASE / "aws/q8_wv_support_p10007_v1.supervisor.out":
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    CASE / "aws/q8_wv_support_p10007_v1.supervisor.err":
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
}

RECTANGLE_SHA = "53e58cd468b83d6cc26308f659ae37085154fcbad430cfb1998257a280246f6b"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def rectangles() -> tuple[int, str]:
    tested = []
    for left_degree in range(1, 25):
        for right_degree in range(1, 17):
            columns = (left_degree + 1) * (right_degree + 1)
            if columns > 176 or columns > 176:
                continue
            tested.append({
                "left_degree": left_degree,
                "right_degree": right_degree,
                "columns": columns,
                "fit_nullity": 0,
                "holdout_pass": False,
            })
    canonical = json.dumps(tested, sort_keys=True, separators=(",", ":"))
    return len(tested), sha256(canonical.encode()).hexdigest()


def parse_meta() -> dict[str, list[str]]:
    parsed: dict[str, list[str]] = {}
    for line in (LANE / "run.meta").read_text().splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        parsed.setdefault(key, []).append(value)
    return parsed


def main() -> None:
    for path, expected in EXPECTED.items():
        check(digest(path) == expected, f"hash mismatch: {path}")

    meta = parse_meta()
    for key, expected in {
        "tag": "q8_wv_support_p10007_v1",
        "host": "ip-172-30-0-45",
        "prime": "10007",
        "root": "980",
        "order": "192",
        "holdout": "16",
        "max_degrees": "24,16",
        "max_columns": "176",
        "rc": "0",
        "stdout_sha256": EXPECTED[LANE / "result.json"],
        "stderr_sha256": EXPECTED[LANE / "stderr.log"],
    }.items():
        check(meta.get(key) == [expected], f"metadata mismatch: {key}")

    count, rectangle_sha = rectangles()
    check(count == 279, "rectangle count")
    check(rectangle_sha == RECTANGLE_SHA, "rectangle-set hash")

    data = json.loads((LANE / "result.json").read_text())
    check(data["prime"] == 10007 and data["q8_root"] == 980, "prime/root")
    good = data["good_reduction"]
    check(good == {
        "Q8_at_root": 0,
        "prime_by_trial_division": True,
        "six_by_six_jacobian_determinant": 2820,
        "v_constant_matches_root": True,
        "x5_constant_nonzero": True,
    }, "good reduction")
    check(data["parameters"] == {
        "holdout": 16,
        "max_columns": 176,
        "max_degrees": [24, 16],
        "order": 192,
    }, "parameters")
    check(set(data["relation_searches"]) == {"w,v", "theta,v"}, "pair set")
    for pair, search in data["relation_searches"].items():
        check(search["tested_rectangles"] == count, f"rectangle count: {pair}")
        check(search["full_column_rank_rectangles"] == count, f"rank count: {pair}")
        check(search["all_fit_matrices_full_column_rank"] is True, f"rank flag: {pair}")
        check(search["max_tested_columns"] == 176, f"column cap: {pair}")
        check(search["hits"] == [], f"unexpected hit: {pair}")
        check(search["nonzero_fit_nullities"] == [], f"unexpected nullity: {pair}")
        check(search["tested_rectangles_sha256"] == RECTANGLE_SHA,
              f"rectangle hash: {pair}")

    print(json.dumps({
        "status": "PASS",
        "scope": (
            "one-good-prime finite rectangular-support exclusion for rational-"
            "coefficient plane relations; not a global quotient relation"
        ),
        "prime": 10007,
        "q8_root": 980,
        "pairs": ["w,v", "theta,v"],
        "rectangles_per_pair": count,
        "total_full_column_rank_matrices": 2 * count,
        "max_columns": 176,
        "fit_rows": 176,
        "holdout_rows": 16,
        "result_sha256": EXPECTED[LANE / "result.json"],
        "stderr_sha256": EXPECTED[LANE / "stderr.log"],
        "tested_rectangles_sha256": RECTANGLE_SHA,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
