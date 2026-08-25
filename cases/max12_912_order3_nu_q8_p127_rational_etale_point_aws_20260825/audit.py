#!/usr/bin/env python3
"""Audit the harvested p=127,w=71,v=50 etale-point replay."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
AWS = ROOT / "aws"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def scalar(text: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}=(.*)$", text)
    assert match, key
    return match.group(1).strip()


def main() -> None:
    result_path = AWS / "result.out"
    input_path = AWS / "input.sing"
    stderr_path = AWS / "stderr.log"
    meta_path = AWS / "run.meta"
    generator_stderr = AWS / "generator.stderr"
    result = result_path.read_text()
    meta = meta_path.read_text()
    assert generator_stderr.stat().st_size == 0
    assert scalar(meta, "rc") == "0"
    assert scalar(meta, "input_sha256") == digest(input_path)
    assert scalar(meta, "stdout_sha256") == digest(result_path)
    assert scalar(meta, "stderr_sha256") == digest(stderr_path)
    assert scalar(result, "point_dim") == "0"
    assert scalar(result, "point_vdim") == "1"
    expected_basis = [
        "v-50", "inv-11", "x5-39", "x3+4",
        "x1+5", "d4-27", "d2+60", "c-47",
    ]
    got_basis = re.findall(r"(?m)^GP\[\d+\]=(.*)$", result)
    assert got_basis == expected_basis
    assert scalar(result, "relative_jacobian_determinant_at_point") == "51"
    remainders = re.findall(r"(?m)^original_remainders\[\d+\]=(.*)$", result)
    assert remainders == ["0"] * 8
    payload = {
        "status": "PASS",
        "point": {
            "prime": 127,
            "w": 71,
            "c": 47,
            "d2": 67,
            "d4": 27,
            "x1": 122,
            "x3": 123,
            "x5": 39,
            "inv": 11,
            "v": 50,
        },
        "point_vector_space_dimension": 1,
        "relative_jacobian_determinant": 51,
        "all_original_generator_remainders_zero": True,
        "input_sha256": digest(input_path),
        "result_sha256": digest(result_path),
        "stderr_sha256": digest(stderr_path),
        "scope": "smooth rational etale point only; irreducibility and lifting are separate",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

