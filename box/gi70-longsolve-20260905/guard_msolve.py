#!/usr/bin/env python3
"""Independent structural and 32-bit-size guard for the c=1 msolve input."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


def terms(poly: str) -> int:
    return poly.count("+") + poly.count("-") + (0 if poly.startswith("-") else 1)


def main() -> int:
    path = Path(sys.argv[1])
    expected = json.loads(Path(sys.argv[2]).read_text())
    lines = path.read_text(encoding="utf-8").splitlines()
    variables = lines[0].split(",")
    prime = int(lines[1])
    polys = [line.removesuffix(",") for line in lines[2:]]
    got_terms = sum(terms(poly) for poly in polys)
    slots = len(variables) * got_terms
    source_names = sorted(set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*", "\n".join(polys))))
    expected_names = {f"v{i}" for i in range(1, 70)}
    payload = {
        "input": str(path),
        "input_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "prime": prime,
        "variables": len(variables),
        "generators": len(polys),
        "expanded_terms": got_terms,
        "exponent_slots": slots,
        "signed_int32_max": 2_147_483_647,
        "passes_signed_int32_guard": slots <= 2_147_483_647,
        "parenthesized_subexpressions": any("(" in p or ")" in p for p in polys),
        "denominators": any("/" in p for p in polys),
        "safe_names_exact": set(source_names) == expected_names,
        "comma_termination_valid": all(line.endswith(",") for line in lines[2:-1]) and not lines[-1].endswith(","),
    }
    checks = [
        prime == 1_073_741_827,
        payload["variables"] == expected["variables"] == 69,
        payload["generators"] == expected["generators"] == 66,
        got_terms == expected["expanded_terms"] == 65_990,
        slots == expected["exponent_slots"] == 4_553_310,
        payload["passes_signed_int32_guard"],
        not payload["parenthesized_subexpressions"],
        not payload["denominators"],
        payload["safe_names_exact"],
        payload["comma_termination_valid"],
    ]
    payload["all_checks_pass"] = all(checks)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["all_checks_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
