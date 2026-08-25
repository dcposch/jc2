#!/usr/bin/env python3
"""Portable custody and endpoint verification for the exact sparse bound."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED = {
    "mixed_volume.py": "a6a516d6558cdceee02e7340ad179e0e142af653506bd0f5468ee8e2027267f9",
    "run_remote.sh": "06c838d26242d732aac6f79bd76714ff73b3e4c188b31f4e9b38f136629b4fbf",
    "aws_box02_v1/result.json": "74685bb41f43cf796024c0c4261e24e3b304b3313f2b2d04004a441771ee06ef",
    "aws_box02_v1/result.out": "a914ca5668c091cce6a8b5fd229488260171263648368c757c8d9570de005253",
    "aws_box02_v1/run.meta": "e8717fe0406a8433948c0723be0ba46869a695eef744417dcca0962dd3fc8b25",
    "aws_box02_v1/stderr.log": "493a1a5a8e54d0746f4c7cf8f71eb849dfc4e8f816ea60d61859ec23899ada62",
    "aws_box03_affine_v1/result.json": "d9cc4829c9f0bc2fce70291c50c711e4ce0cf53b44379ef54a3e06e30c718359",
    "aws_box03_affine_v1/result.out": "e8b50151d7880883deb6f5a04f8a34ee01ba5fc151cd06c08fb560631b8c25ae",
    "aws_box03_affine_v1/run.meta": "1e538851b73f09011632fe723d29f429087d3a84b925bde15f50cc0493a10d47",
    "aws_box03_affine_v1/stderr.log": "837a5b62d7696240f768d99c955287de5e04acbc1f93a892eea7854290a0813d",
}
COMPILER_SHA = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
SUPPORT_SIZES = [10, 20, 35, 57, 16, 29]
LINE_SUPPORT = [
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1],
]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def endpoint(directory: str, independent: bool) -> dict:
    base = HERE / directory
    payload = json.loads((base / "result.json").read_text())
    assert payload["status"] == "PASS"
    assert payload["compiler_sha256"] == COMPILER_SHA
    assert payload["source_support_sizes"] == SUPPORT_SIZES
    assert payload["line_support"] == LINE_SUPPORT
    assert payload["origin_augmented_affine_candidate"]["mixed_volume"] == 658
    assert payload["origin_augmented_affine_candidate"]["factorial_divisor"] == 5040
    assert payload["origin_augmented_affine_candidate"]["polarization_normalized_volume_sum"] == "3316320"
    if independent:
        assert payload["scope"].startswith("affine-only independent shard")
    else:
        assert payload["normaliz_version"] == "Normaliz 3.10.2"
        assert payload["raw_torus"]["mixed_volume"] == 519
        assert payload["raw_torus"]["polarization_normalized_volume_sum"] == "2615760"
        assert payload["controls"] == {
            "coordinate_segments": 1,
            "repeated_standard_simplex": 1,
        }
    meta = (base / "run.meta").read_text()
    assert "\nrc=0\n" in "\n" + meta
    assert "\nendpoint=PASS\n" in "\n" + meta
    stderr = (base / "stderr.log").read_text()
    assert "Exit status: 0" in stderr and "Swaps: 0" in stderr
    return payload


def main() -> None:
    for relative, expected in EXPECTED.items():
        got = digest(HERE / relative)
        assert got == expected, (relative, got, expected)
    full = endpoint("aws_box02_v1", False)
    independent = endpoint("aws_box03_affine_v1", True)
    assert (
        full["origin_augmented_affine_candidate"]["mixed_volume"]
        == independent["origin_augmented_affine_candidate"]["mixed_volume"]
        == 658
    )
    print("Q8-SPARSE-MIXED-VOLUME-FREEZE-VERIFY PASS")
    print("raw_torus=519")
    print("origin_augmented_affine=658")
    print("independent_affine=658")


if __name__ == "__main__":
    main()
