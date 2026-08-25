#!/usr/bin/env python3
"""Verify the frozen hierarchical order-16/32 Padé custody."""

from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RUN = HERE / "aws_box03_v1"
EXPECTED = {
    "high": "ed10f985d3031b1b67f2e81c028ab6bf961d26fa24fa62b312bcbb61a882a19b",
    "runner": "ebfbbcfd1b2676bb14f0d32c5bce5e8ee1462df1c221b00f1a4d3b4f463b0e70",
    "parent": "acc005c798d966297bb3b1a5a9fa64f3e83d71a164f6c2b4d7806473f841e3b5",
    "json": "b46d38770d7170518f144c12bf0e3e2bfb2c9d997921c4fe80b3bc28ea0abd17",
    "stdout": "d41f9e987256807e8c5b7291b4980d32564169ec85a93eb8047e2e62aae66c6d",
    "meta": "47149da01ce3e2016cdf1d06bacf57c187732ac76c621064629db89d909649e2",
    "stderr": "15c4c7123a6861e1ebc48b4b12a274f0c2660236ee74f56b9d8d0024577d4def",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    paths = {
        "high": ROOT / "cases/max12_912_order3_nu_q8_p127_hensel_common_pade_high_aws_20260825/common_pade_high.py",
        "runner": ROOT / "cases/max12_912_order3_nu_q8_p127_hensel_common_pade_high_aws_20260825/run_remote.sh",
        "parent": ROOT / "cases/max12_912_order3_nu_q8_p127_hensel_common_pade_aws_20260825/common_pade.py",
        "json": RUN / "reconstruction.json",
        "stdout": RUN / "result.out",
        "meta": RUN / "run.meta",
        "stderr": RUN / "stderr.log",
    }
    for name, path in paths.items():
        got = digest(path)
        if got != EXPECTED[name]:
            raise AssertionError((name, got, EXPECTED[name]))

    payload = json.loads(paths["json"].read_text())
    if payload.get("status") != "PASS" or payload.get("prefix_match") is not True:
        raise AssertionError("payload endpoint")
    if payload.get("lower_order") != 16 or payload.get("upper_order") != 32:
        raise AssertionError("orders")
    if payload.get("coordinate_lcm_candidate") is not None:
        raise AssertionError("unexpected LCM")
    expected_groups = {
        "c": 190,
        "d2": 190,
        "d4": 190,
        "x1": 190,
        "x3": 190,
        "x5": 190,
        "inv": 190,
        "normal_triple": 570,
        "invariant_triple": 570,
        "true_center_six": 1140,
        "global_seven": 1330,
    }
    groups = payload.get("group_hierarchy", {})
    if set(groups) != set(expected_groups):
        raise AssertionError((set(groups), set(expected_groups)))
    for name, count in expected_groups.items():
        item = groups[name]
        if item.get("sequence_count") != count:
            raise AssertionError((name, item.get("sequence_count"), count))
        for key in ("lower_fit", "upper_fit", "selected", "selected_source"):
            if item.get(key) is not None:
                raise AssertionError((name, key, item.get(key)))
        if item.get("lower_upper_holdout") != []:
            raise AssertionError((name, "holdout"))
    meta = paths["meta"].read_text().splitlines()
    for line in (
        "rc=0",
        "endpoint=PASS",
        "stdout_sha256=" + EXPECTED["stdout"] + "  /home/ubuntu/jc2q8-generic/out/q8_p127_hensel_common_pade_hierarchy_order16_32_box03_smoke_v1/result.out",
        "stderr_sha256=" + EXPECTED["stderr"] + "  /home/ubuntu/jc2q8-generic/out/q8_p127_hensel_common_pade_hierarchy_order16_32_box03_smoke_v1/stderr.log",
        "reconstruction_sha256=" + EXPECTED["json"] + "  /home/ubuntu/jc2q8-generic/out/q8_p127_hensel_common_pade_hierarchy_order16_32_box03_smoke_v1/reconstruction.json",
    ):
        if meta.count(line) != 1:
            raise AssertionError((line, meta.count(line)))
    print("PASS-Q8-P127-PADE-HIERARCHY-ORDER16-32-CUSTODY")


if __name__ == "__main__":
    main()

