#!/usr/bin/env python3
"""Fail-closed reconstruction of the source of descended row (25,15).

The charged census module is loaded from the frozen lane input.  Arithmetic
reported below is then recomputed here, rather than copied from a prior JSON.
"""
from __future__ import annotations

import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


FROZEN = Path("/tmp/jc2-lane.QNRa2r/inputs/moh_skeleton_full.py")


def load_frozen():
    spec = importlib.util.spec_from_file_location("row2515_frozen_moh", FROZEN)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen census")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def reduced_denominator(value: Fraction) -> int:
    return value.denominator


def delta(n: int, M: dict[int, int], d: dict[int, int], V: dict[int, int], s: int, i: int) -> Fraction:
    numerator = Fraction(n - M[i], 1)
    denominator = Fraction(n - M[s] - 1, 1)
    for j in range(i + 1, s + 1):
        numerator *= Fraction(V[j] * (n - M[j]) - d[j], 1)
        denominator *= Fraction(V[j] * (n - M[j - 1]) - d[j], 1)
    return 1 - numerator / denominator


def main() -> None:
    moh = load_frozen()
    matches = []
    for m, middle, values in moh.census(125, Kmin=2, full=True):
        if m == 75 and tuple(middle) == (105, 123) and values == {2: 2, 3: 4}:
            matches.append(moh.Skel(125, m, list(middle), values))
    if len(matches) != 1:
        raise AssertionError(f"expected one exact census match, got {len(matches)}")
    source = matches[0]

    n, m, s = source.n, source.m, source.s
    M = {1: -m, 2: 105, 3: n - 2}
    d = {1: n}
    for i in range(1, s + 1):
        d[i + 1] = math.gcd(d[i], M[i])
    V = {2: 2, 3: 4, 4: d[4]}
    radii = {i: delta(n, M, d, V, s, i) for i in range(1, s + 1)}

    def L(j: int) -> int:
        value = 1
        for i in range(j + 1, s + 1):
            value = math.lcm(value, reduced_denominator(radii[i]))
        return value

    def A(j: int) -> int:
        return reduced_denominator(L(j) * radii[j])

    q2 = V[3] * d[2] // d[3]
    tri2, sq2 = divmod(q2, A(2))
    bottom12 = ((n // d[2]) * V[2]) % A(1) == 0 and (((m // d[2]) * V[2]) - 1) % A(1) == 0
    bottom13 = ((m // d[2]) * V[2]) % A(1) == 0 and (((n // d[2]) * V[2]) - 1) % A(1) == 0

    # Moh's top split uses v_s=V_s and u_s=d_s-v_s.  This is not the
    # integration quantity named ``Skel.u`` in the frozen helper.
    ds = d[s]
    vs = V[s]
    us = ds - vs
    descended = {
        "n_prime": us * n // ds,
        "m_prime": us * m // ds,
        "M2_prime": us * M[2] // ds,
        "V2_prime": V[2],
        "d2_prime": math.gcd(us * n // ds, us * m // ds),
        "u_prime": math.gcd(us * n // ds, us * m // ds) - V[2],
        "k": vs - us - 1,
    }

    checks = {
        "frozen_M": source.M == M,
        "frozen_d": source.d == d,
        "frozen_V": source.V == V,
        "frozen_delta": source.delta == radii,
        "frozen_full_ok": source.full_ok(),
        "window_ok": source.windows_ok(),
        "tower_10": V[2] <= tri2,
        "tower_11_false": (V[2] - sq2) % A(2) != 0,
        "bottom_12": bottom12,
        "bottom_13_false": not bottom13,
        "descended_tuple": descended == {
            "n_prime": 25,
            "m_prime": 15,
            "M2_prime": 21,
            "V2_prime": 2,
            "d2_prime": 5,
            "u_prime": 3,
            "k": 2,
        },
    }
    if not all(checks.values()):
        raise AssertionError({k: v for k, v in checks.items() if not v})

    payload = {
        "source": {"n": n, "m": m, "s": s, "M": M, "d": d, "V": V},
        "top_split": {
            "d_s": ds,
            "v_s": vs,
            "u_s": us,
            "note": "u_s=d_s-v_s; distinct from frozen Skel.u",
            "frozen_Skel_u": str(source.u),
        },
        "radii": {str(i): str(radii[i]) for i in radii},
        "moh_8_13_tower": {
            "level_2": {"L2": L(2), "A2": A(2), "Q2": q2, "TRI2": tri2, "SQ2": sq2,
                        "condition_10": V[2] <= tri2, "condition_11": (V[2] - sq2) % A(2) == 0},
            "bottom": {"L1": L(1), "A1": A(1), "condition_12": bottom12, "condition_13": bottom13},
        },
        "descended": descended,
        "checks": checks,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
