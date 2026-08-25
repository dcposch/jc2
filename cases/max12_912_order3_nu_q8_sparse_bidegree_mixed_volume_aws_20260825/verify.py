#!/usr/bin/env python3
"""Verify exact AWS bidegree bounds and custody."""

from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED = {
    "bidegree.py": "a818bdbe69da12fd7b895a61348013e572288512b558c5b30250853fb131a608",
    "run_remote.sh": "c990bc5eb8748cec40214192aef926d5b16f551295de42f669564cf62aa3723d",
    "aws_box02_horizontal_v1/result.json": "2c78f62cc63578bb99ad688e8fe0a8e06e2b49bb75a2ab1006c333461101ff56",
    "aws_box02_horizontal_v1/result.out": "7b4c9d5a57d78b5d915820daa3d9bd1bf46a4c0e81306b1daec98423026c3725",
    "aws_box02_horizontal_v1/run.meta": "7a7167ff832025603a91af1923f89d2566e887ddd6e35a0e140851c320c5260e",
    "aws_box02_horizontal_v1/stderr.log": "c45a0f6573d49ce76eeb5d7cd04ed316d767099f94e238d5969f5b0c1b572e44",
    "aws_box03_vertical_v1/result.json": "ec90ca1baa563c433b49a394db49ee2feba9c52cf32add5f31c7f22fa513652c",
    "aws_box03_vertical_v1/result.out": "3b18ac0e68a51e97169f518c4c77c516dcc72d47dcb4527dfd3657802086bff5",
    "aws_box03_vertical_v1/run.meta": "e786fe1169ea225820f2a09a74f9e337728413db14b18f49d287109b0a7e92c5",
    "aws_box03_vertical_v1/stderr.log": "88634b1988eeb2216046e79054855b5f316e6e7fd5d02f8076d896669203f350",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for relative, expected in EXPECTED.items():
        got = digest(HERE / relative)
        assert got == expected, (relative, got, expected)
    horizontal = json.loads((HERE / "aws_box02_horizontal_v1/result.json").read_text())
    vertical = json.loads((HERE / "aws_box03_vertical_v1/result.json").read_text())
    assert horizontal["status"] == vertical["status"] == "PASS"
    assert horizontal["kind"] == "horizontal"
    assert horizontal["bounds_bidegree_coordinate"] == "A"
    assert horizontal["mixed_volume_bound"] == 176
    assert horizontal["origin_augmented"]["polarization_normalized_volume_sum"] == "887040"
    assert horizontal["controls"] == {
        "coordinate_segments": 1,
        "repeated_standard_simplex": 1,
    }
    assert vertical["kind"] == "vertical"
    assert vertical["bounds_bidegree_coordinate"] == "B"
    assert vertical["mixed_volume_bound"] == 550
    assert vertical["origin_augmented"]["polarization_normalized_volume_sum"] == "2772000"
    for directory in ("aws_box02_horizontal_v1", "aws_box03_vertical_v1"):
        meta = (HERE / directory / "run.meta").read_text()
        stderr = (HERE / directory / "stderr.log").read_text()
        assert "\nrc=0\n" in "\n" + meta and "\nendpoint=PASS\n" in "\n" + meta
        assert "Exit status: 0" in stderr and "Swaps: 0" in stderr
    # Combined with generic-line A+B<=658 and one H=(21,190) summand.
    best = max(
        190 * a + 21 * b
        for a in range(156)
        for b in range(361)
        if a + b <= 447
    )
    assert best == 35582
    assert 8 * 4448 > best and 8 * 4447 <= best
    print("Q8-SPARSE-BIDEGREE-VERIFY PASS")
    print("A<=176 B<=550 A+B<=658")
    print("residual_H_intersection<=35582")
    print("eight_contact_threshold=4448")


if __name__ == "__main__":
    main()
