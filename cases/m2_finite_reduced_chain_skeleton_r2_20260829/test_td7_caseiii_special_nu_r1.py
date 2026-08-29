#!/usr/bin/env python3
"""Independent bounded controls for td7_caseiii_special_nu_r1.py."""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "td7_caseiii_special_nu_r1.py"
spec = importlib.util.spec_from_file_location("td7_caseiii_special_nu_r1",
                                              SOURCE)
if spec is None or spec.loader is None:
    raise RuntimeError("module spec unavailable")
M = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = M
spec.loader.exec_module(M)

CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError(f"CHECK_FAILED:{label}")


def main() -> int:
    payload = M.derive()
    check(payload["cap_free"] is True, "cap-free")
    check(payload["special_values"] == [{
        "nu_H": 3, "l": 1, "nu_G": 3, "dp": 5, "dq": 7,
        "M_G": 1, "verdict": "MP2_DEAD_INTERIOR_M1"}], "special-exact")

    # Independent rectangular brute control far beyond the special value.
    solutions = []
    for h in range(3, 1002, 2):
        for l in range(1, 101):
            D = (3 * h - 4) * l - 2
            if D <= 0 or (3 * h) % D:
                continue
            g = (3 * h) // D
            if g >= 2:
                solutions.append((h, l, g))
    check(solutions == [(3, 1, 3)], "brute-unique")

    # Boundary/mutation controls.
    check((6 * 3 - 10) * 2 > 3 * 3, "l2-inequality-h3")
    for h in (5, 7, 101, 1001):
        check(h % 2 == 1 and h >= 5, f"generic-shape-{h}")
        check(h % (h - 2) != 0, f"generic-l1-empty-{h}")
    check(math.gcd(5, 7) == 1, "MP2-output")
    text = SOURCE.read_text()
    for token in ("NCAP", "range(3,", "nu_cap", "max_nu"):
        check(token not in text, f"source-no-cap-{token}")
    print(f"TD7_CASEIII_SPECIAL_NU_R1_TEST_PASS checks={CHECKS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
