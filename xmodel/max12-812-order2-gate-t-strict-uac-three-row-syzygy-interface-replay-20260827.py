#!/usr/bin/env python3
"""Desk replay for the direct strict unique-AC three-row interface."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MINER = ROOT / "cases/max12_812_order2_square_owner_d1_unique_ac_d23_small_a_support_miner_20260826/mine_support.py"
MINER_SHA256 = "0e94e5408b8a3b5db06c8eff5c759df1c75a2e8bb4563aa4964f42c39952fe9a"


def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
            if not out[monomial]:
                del out[monomial]
    return out


def scale(value, poly):
    return {monomial: Fraction(value) * coefficient for monomial, coefficient in poly.items()}


def mul(left, right):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            powers = {}
            for name, exponent in lm + rm:
                powers[name] = powers.get(name, 0) + exponent
            monomial = tuple(sorted(powers.items()))
            out[monomial] = out.get(monomial, Fraction(0)) + lc * rc
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def var(name):
    return {((name, 1),): Fraction(1)}


def load_miner():
    if sha256(MINER.read_bytes()).hexdigest() != MINER_SHA256:
        raise RuntimeError("miner pin")
    spec = importlib.util.spec_from_file_location("three_row_miner", MINER)
    if spec is None or spec.loader is None:
        raise RuntimeError("miner import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def is_ac(item):
    return (
        item["load"] is None
        and tuple(int(item[key]) for key in ("R", "A", "C", "pole")) == (0, 1, 1, 1)
    )


def is_c2(item):
    return (
        item["load"] is None
        and tuple(int(item[key]) for key in ("R", "A", "C", "pole")) == (0, 0, 2, 2)
    )


def eligible(miner, a, d, r):
    c = a + d
    G = 10 + a + c
    T = 10 + 2 * c
    row = {
        "a": a, "d": d, "c": c, "s_min": r - a, "r": r,
        "first_ac_grade": G, "target_grade": T,
    }
    inventory = miner.enumerate_primitives(row)
    initial = [item for item in inventory if int(item["first_grade"]) <= G]
    bad_poles = [
        item for item in inventory
        if int(item["pole"]) >= 2 and not is_c2(item)
    ]
    return (
        len(initial) == 1
        and is_ac(initial[0])
        and int(initial[0]["first_grade"]) == G
        and not bad_poles
        and G < 28
        and T < 32
    ), inventory


def main():
    A1, A0, C1, C0, rho = (var(name) for name in ("A1", "A0", "C1", "C0", "rho"))
    rho2 = mul(rho, rho)
    D = add(mul(rho2, mul(C1, C1)), scale(-1, mul(C0, C0)))
    g1 = scale(Fraction(3, 8), add(mul(A0, C1), mul(A1, C0)))
    g2 = scale(Fraction(3, 8), add(mul(A0, C0), mul(rho2, mul(A1, C1))))
    g4 = scale(Fraction(3, 32), add(mul(C0, C0), mul(rho2, mul(C1, C1))))
    checks = (
        add(mul(C1, g2), scale(-1, mul(C0, g1)), scale(Fraction(-3, 8), mul(A1, D))),
        add(mul(C0, g2), scale(-1, mul(rho2, mul(C1, g1))), scale(Fraction(3, 8), mul(A0, D))),
        add(scale(Fraction(32, 3), g4), D, scale(-2, mul(rho2, mul(C1, C1)))),
        add(scale(Fraction(32, 3), g4), scale(-1, D), scale(-2, mul(C0, C0))),
    )
    if any(checks):
        raise RuntimeError(("syzygy", checks))

    miner = load_miner()
    actual = set()
    for a in range(1, 7):
        for d in (1, 2, 3):
            if a + d < 3:
                continue
            r = a + (1 if a <= d else 0)
            ok, _ = eligible(miner, a, d, r)
            if ok:
                actual.add((a, d, r))
    expected = {
        *((a, 1, a) for a in range(2, 7)),
        *((a, 2, a + (1 if a <= 2 else 0)) for a in range(2, 7)),
        (5, 3, 5), (6, 3, 6),
    }
    if actual != expected:
        raise RuntimeError(("baseline classification", actual, expected))

    recovered = {(1, 2, 3), (2, 3, 5), (3, 3, 5), (4, 3, 5)}
    if any(not eligible(miner, *cell)[0] for cell in recovered):
        raise RuntimeError("recovered subtail")
    if eligible(miner, 1, 3, 20)[0]:
        raise RuntimeError("E pole-three negative control")
    if eligible(miner, 2, 3, 3)[0] or eligible(miner, 2, 3, 4)[0]:
        raise RuntimeError("B23 RA2 negative control")
    if not eligible(miner, 2, 3, 5)[0]:
        raise RuntimeError("B23 r>=5 positive control")
    if eligible(miner, 7, 1, 7)[0]:
        raise RuntimeError("k6 tie negative control")

    print("PASS-UAC-THREE-ROW-SYZYGY-INTERFACE")
    print("SYZYGIES=4")
    print("BASELINE_CONTACTS=12")
    print("RECOVERED_SUBTAIL_BASES=4")
    print("CURRENT_B23_R3_R4=REJECT")
    print("CURRENT_B23_RGE5=ACCEPT")


if __name__ == "__main__":
    main()

