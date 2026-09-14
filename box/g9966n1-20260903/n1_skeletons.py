#!/usr/bin/env python3
"""Enumerate and triage Moh (1)-(13) skeletons at (99,66)."""
from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from math import gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "box" / "g9966n1-20260903"
MOH = ROOT / "box" / "moh_skeleton_full.py"


def load_moh():
    spec = importlib.util.spec_from_file_location("moh_skeleton_full_live", MOH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {MOH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def detector_orders(u_s: int, v_s: int) -> list[str]:
    if u_s < 2:
        return []
    ceiling = Fraction(v_s, u_s)
    seen: set[Fraction] = set()
    for den in range(1, u_s + 1):
        for num in range(den + 1, 10 * v_s + 1):
            value = Fraction(num, den)
            if value >= ceiling:
                break
            if gcd(num, den) == 1:
                seen.add(value)
    return [qstr(value) for value in sorted(seen)]


def descended_row(S, u_s: int) -> dict:
    n1 = u_s * (S.n // S.d[S.s])
    m1 = u_s * (S.m // S.d[S.s])
    M21 = u_s * (S.M[2] // S.d[S.s])
    V21 = S.V[2]
    K1 = gcd(n1, m1)
    return {
        "n": n1,
        "m": m1,
        "K": K1,
        "M2": M21,
        "V2": V21,
        "k": n1 - M21 - 2,
        "u_prime": K1 - V21,
    }


def main() -> None:
    moh = load_moh()
    rows = []
    for m, Ms, V in moh.census(99, Kmin=2, full=True):
        if m != 66:
            continue
        S = moh.Skel(99, m, list(Ms), V)
        d_s = S.d[S.s]
        v_s = S.V[S.s]
        u_s = d_s - v_s
        row = {
            "M": [S.M[i] for i in range(1, S.s + 1)],
            "Ms": list(Ms),
            "V": {str(i): S.V[i] for i in range(2, S.s + 1)},
            "s": S.s,
            "d": [S.d[i] for i in range(1, S.s + 2)],
            "d_s": d_s,
            "v_s": v_s,
            "u_s": u_s,
            "delta": {str(i): qstr(S.delta[i]) for i in range(1, S.s + 1)},
            "A": {str(j): S.A(j) for j in range(1, S.s)},
            "L": {str(j): S.L(j) for j in range(1, S.s)},
            "cond1011": {
                str(j): {"ok": S.cond1011(j)[0], "by10": S.cond1011(j)[1], "by11": S.cond1011(j)[2]}
                for j in range(S.s - 1, 1, -1)
            },
            "cond1213": {"ok": S.cond1213()[0], "by12": S.cond1213()[1], "by13": S.cond1213()[2]},
            "windows_ok": S.windows_ok(),
            "full_ok": S.full_ok(),
            "split_window": None if u_s == 0 else f"1 < delta < {qstr(Fraction(v_s, u_s))}",
            "detector_orders_den_le_u_s": detector_orders(u_s, v_s),
            "banked_v88": S.M[2] == 77 and S.V[3] == 8 and S.V[2] == 8,
            "descended_unsplit_row": descended_row(S, u_s),
        }
        if row["banked_v88"]:
            row["triage"] = "BANKED_V88_DEAD_ALL_THREE_CONFIGURATIONS"
        elif u_s == 1:
            row["triage"] = "u_s=1_DESCENT_TO_ORDER_CHART"
        else:
            row["triage"] = "u_s>=2_SPLIT_WINDOW_PLUS_UNSPLIT_PIN_CHART_REQUIRED"
        rows.append(row)
    rows.sort(key=lambda r: (r["M"][1], r["V"]["3"], r["V"]["2"]))
    for idx, row in enumerate(rows, 1):
        row["id"] = f"S{idx}"
    payload = {
        "source": str(MOH.relative_to(ROOT)),
        "n": 99,
        "m": 66,
        "count": len(rows),
        "rows": rows,
    }
    out = HERE / "skeletons.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
