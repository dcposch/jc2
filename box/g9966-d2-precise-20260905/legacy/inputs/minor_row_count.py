#!/usr/bin/env python3
"""Count raw direct F99/G66 minor-leader coefficient coordinates exactly."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RECEIPT = ROOT / "xmodel/g9966-global-design-sol56-20260903.run.v2"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def verify_inputs() -> dict:
    fields = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    count = int(fields["charged_inputs"])
    frozen = Path(fields["lane_inputs_dir"])
    for index in range(1, count + 1):
        name = fields[f"charged_input_{index}_basename"]
        assert Path(name).name == name
        assert sha256(frozen / name) == fields[f"charged_input_{index}_sha256"]
    assert count == 14
    return {
        "receipt": str(RECEIPT),
        "lane_inputs_dir": str(frozen),
        "charged_inputs": count,
        "all_hashes_match": True,
    }


def delta2_rows(degree: int, pole: int) -> set[tuple[int, int]]:
    rows = set()
    # Fixed top degree=degree is omitted.  For x^i*y^j and k selected z
    # factors in y=u*t+z*t^2, the normalized coordinate is
    # (t exponent,z degree)=(pole-i+j+k,k).
    for i in range(degree):
        for j in range(degree - i):
            for k in range(j + 1):
                tag = (pole - i + j + k, k)
                if tag[0] <= 0:
                    rows.add(tag)
    return rows


def delta52_rows(degree: int, pole: int) -> set[tuple[int, int]]:
    rows = set()
    # For y=u*s^2+v*s^4+pi*s^5, let b and k count v and pi factors.
    # The normalized coordinate is
    # (s exponent,pi degree)=(pole-2i+2j+2b+3k,k).
    for i in range(degree):
        for j in range(degree - i):
            for b in range(j + 1):
                for k in range(j - b + 1):
                    tag = (pole - 2 * i + 2 * j + 2 * b + 3 * k, k)
                    if tag[0] <= 0:
                        rows.add(tag)
    return rows


def describe(rows: set[tuple[int, int]]) -> dict:
    bands = Counter(exponent for exponent, _degree in rows)
    return {
        "row_count": len(rows),
        "occupied_band_count": len(bands),
        "minimum_exponent": min(bands),
        "maximum_exponent": max(bands),
        "pole_end": {
            str(exponent): sorted(degree for exp, degree in rows if exp == exponent)
            for exponent in sorted(bands)[:7]
        },
        "face_end": {
            str(exponent): sorted(degree for exp, degree in rows if exp == exponent)
            for exponent in sorted(bands)[-6:]
        },
    }


def main() -> None:
    d2_f = delta2_rows(99, 18)
    d2_g = delta2_rows(66, 12)
    d52_f = delta52_rows(99, 9)
    d52_g = delta52_rows(66, 6)
    assert (len(d2_f), len(d2_g)) == (1134, 513)
    assert (len(d52_f), len(d52_g)) == (1316, 594)
    result = {
        "type": "RAW-DIRECT-MINOR-LEADER-ROW-COUNT / NO-RANK-CLAIM",
        "frozen_input_verification": verify_inputs(),
        "global_lower_coefficient_count": 7161,
        "delta2": {
            "substitution": "x=t^-1, y=u*t+z*t^2",
            "F99": describe(d2_f),
            "G66": describe(d2_g),
            "total_rows": len(d2_f) + len(d2_g),
            "first_coefficients": {
                "F99": "F_(98,0) at (t exponent,z degree)=(-80,0)",
                "G66": "G_(65,0) at (t exponent,z degree)=(-53,0)",
            },
        },
        "delta52": {
            "substitution": "x=s^-2, y=u*s^2+v*s^4+pi*s^5",
            "F99": describe(d52_f),
            "G66": describe(d52_g),
            "total_rows": len(d52_f) + len(d52_g),
            "first_coefficients": {
                "F99": "F_(98,0) at (s exponent,pi degree)=(-187,0)",
                "G66": "G_(65,0) at (s exponent,pi degree)=(-124,0)",
            },
        },
        "top_form_check": (
            "The only fixed-top coordinates outside these lower-support unions "
            "are the monic face terms z^27,z^18 or pi^27,pi^18; they cancel "
            "the monic target coefficients."
        ),
        "not_claimed": [
            "row independence or codimension",
            "compatibility with the major tower",
            "a Jacobian solution",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
