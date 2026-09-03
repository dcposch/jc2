#!/usr/bin/env python3
"""Hash-check and re-emit the four A2=6 numerical-census rows."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from math import gcd
from pathlib import Path


SOURCE = Path("/tmp/jc2-lane.OAeQcz/inputs/moh_skeleton_full.py")
EXPECTED = "d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2"


def load_source():
    actual = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if actual != EXPECTED:
        raise ValueError(f"moh_skeleton_full custody mismatch: {actual}")
    spec = importlib.util.spec_from_file_location("frozen_moh_a2six", SOURCE)
    if spec is None or spec.loader is None:
        raise ValueError("could not load frozen census")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def verify_member(module, t: int) -> dict[str, object]:
    P = 7 * t + 6
    n, m = 9 * P, 6 * P
    Ms = (4 * P, 9 * P - 2)
    Vs = {2: 1, 3: 6 * t + 5}
    sk = module.Skel(n, m, Ms, Vs)
    emitted = list(module.census(n, Kmin=16, full=True))
    hits = [row for row in emitted if row[0] == m and tuple(row[1]) == Ms and row[2] == Vs]
    if len(hits) != 1:
        raise AssertionError(f"t={t}: expected one target census row, got {len(hits)}")
    d4 = gcd(P, 2)
    expected_delta = {1: Fraction(7, 12), 2: Fraction(1, 6), 3: Fraction(-1)}
    assert sk.d == {1: n, 2: 3 * P, 3: P, 4: d4}
    assert sk.delta == expected_delta
    assert sk.A(2) == 6 and sk.A(1) == 2
    assert sk.div9(2) == (3 * t + 2, 3, 6, 18 * t + 15)
    assert sk.cond1011(2) == (True, True, False)
    assert sk.cond1213() == (True, False, True)
    assert sk.q() == Fraction(1, 2)
    assert sk.u == 18 * t + 15
    assert sk.windows_ok() and sk.full_ok()
    return {
        "t": t,
        "P": P,
        "D": n,
        "row": {
            "n": n,
            "m": m,
            "M": [-m, *Ms],
            "V": {"2": 1, "3": 6 * t + 5},
        },
        "d": {"2": 3 * P, "3": P, "4": d4},
        "delta_descending": ["-1", "1/6", "7/12"],
        "A2": 6,
        "A1": 2,
        "Q": 18 * t + 15,
        "TRI": 3 * t + 2,
        "SQ": 3,
        "q": "1/2",
        "u": 18 * t + 15,
        "orbit_admissible_N": list(range(3, 3 * (3 * t + 2) + 1, 3)),
        "k12_N6": True,
        "census_assignments": len(emitted),
        "target_hits": 1,
        "windows_ok": True,
        "full_ok": True,
        "cond1011": [True, True, False],
        "cond1213": [True, False, True],
    }


def main() -> int:
    try:
        module = load_source()
        result = {
            "status": "PASS",
            "typing": "implemented numerical census; geometric (3)/(4) and attainment not claimed",
            "source": str(SOURCE),
            "source_sha256": EXPECTED,
            "members": [verify_member(module, t) for t in range(4)],
        }
    except (AssertionError, OSError, TypeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
