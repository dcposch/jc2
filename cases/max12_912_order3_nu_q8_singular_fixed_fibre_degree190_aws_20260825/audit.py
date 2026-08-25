#!/usr/bin/env python3
"""Audit the harvested pure-Singular fixed-w Q8 fibres.

This is deliberately a parser only: it performs no algebraic elimination.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AWS = ROOT / "aws"

EXPECTED = {
    23: {1, 8, 21, 22},
    67: {1, 25, 48, 66},
    89: {1, 2, 3, 7, 44, 88},
    127: {1, 2, 63, 71, 95, 126},
}
EXPECTED_SOURCE = {
    "run_one.sh": "11084528be3c14935b4542677795240ecf9716daf4d901cd4f917557daeafcd7",
    "generate.py": "4af6f7eca198bcdf1e60151449e08099853669bd1d6965db3cddffa666032d2c",
    "quotient_compiler.py": "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545",
    "generic_fibre_grouping_generate.py": "6b752b03d777c73de5d9ff729f30d01f5d81229d0ee467e9ad98a349d6234daf",
}


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
    if re.search(r"\bv\b", poly):
        return 1
    return 0


def main() -> None:
    rows = []
    seen: dict[int, set[int]] = {}
    for lane in sorted(path for path in AWS.iterdir() if path.is_dir()):
        name_match = re.fullmatch(r"q8_singular_p(\d+)_w(\d+)_std_v1", lane.name)
        assert name_match, f"unexpected lane {lane.name}"
        prime, w_value = map(int, name_match.groups())
        seen.setdefault(prime, set()).add(w_value)

        result_path = lane / "result.out"
        meta_path = lane / "run.meta"
        input_path = lane / "input.sing"
        stderr_path = lane / "stderr.log"
        for path in (result_path, meta_path, input_path, stderr_path, lane / "generator.stderr"):
            assert path.is_file(), f"missing {path}"

        result = result_path.read_text()
        meta = meta_path.read_text()
        assert scalar(meta, "rc") == "0"
        assert int(scalar(meta, "prime")) == prime
        assert int(scalar(meta, "w_value")) == w_value
        assert scalar(meta, "engine") == "std"
        assert scalar(meta, "input_sha256") == sha256(input_path)
        assert scalar(meta, "stdout_sha256") == sha256(result_path)
        assert scalar(meta, "stderr_sha256") == sha256(stderr_path)
        assert (lane / "generator.stderr").stat().st_size == 0

        source_lines = re.findall(r"(?m)^source_sha256=([0-9a-f]{64})\s+(\S+)$", meta)
        assert len(source_lines) == 4
        source_by_base = {}
        for digest, source_path in source_lines:
            base = Path(source_path).name
            if base == "generate.py" and "generic_fibre_grouping" in source_path:
                base = "generic_fibre_grouping_generate.py"
            source_by_base[base] = digest
        assert source_by_base == EXPECTED_SOURCE

        assert int(scalar(result, "prime")) == prime
        assert int(scalar(result, "w_value")) == w_value
        assert scalar(result, "fibre_dim") == "0"
        assert scalar(result, "fibre_size") == "8"
        assert scalar(result, "fibre_vdim") == "190"
        assert scalar(result, "v_elimination_size") == "1"
        assert scalar(result, "v_eliminant_degree") == "190"
        assert scalar(result, "v_eliminant_squarefree_gcd_degree") == "0"

        factors = re.findall(r"(?m)^\s+_\[\d+\]=(.*)$", result)
        claimed_count = int(scalar(result, "rational_factor_entries"))
        assert len(factors) == claimed_count
        degrees = sorted(polynomial_degree(poly) for poly in factors)
        assert all(degree > 0 for degree in degrees)
        assert sum(degrees) == 190

        rows.append(
            {
                "prime": prime,
                "w": w_value,
                "factor_degrees": degrees,
                "factor_count": len(degrees),
                "result_sha256": sha256(result_path),
                "input_sha256": sha256(input_path),
                "stderr_sha256": sha256(stderr_path),
                "lane": lane.name,
            }
        )

    assert seen == EXPECTED, f"lane matrix mismatch: {seen}"
    rows.sort(key=lambda row: (row["prime"], row["w"]))
    payload = {
        "status": "PASS",
        "scope": "20 pure-Singular fixed-w localized fibres; parser/audit only",
        "invariants": {
            "dimension": 0,
            "vector_space_dimension": 190,
            "eliminant_degree": 190,
            "squarefree_gcd_degree": 0,
        },
        "rows": rows,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
