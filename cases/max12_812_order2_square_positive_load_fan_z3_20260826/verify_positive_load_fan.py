#!/usr/bin/env python3
"""Dependency-free exact witness checker for positive_load_fan_cells.json."""

from __future__ import annotations

import json
import sys
from fractions import Fraction


NAMES = ("AC", "C2", "RA2", "A3", "kR3", "kRC", "kA2")


def parse(value: str) -> Fraction:
    return Fraction(value)


def values(w):
    a, r, c, q = (parse(w[x]) for x in ("a", "r", "c", "q"))
    return {
        "AC": a + c,
        "C2": 2 * c,
        "RA2": 2 + r + 2 * a,
        "A3": 5 + 3 * a,
        "kR3": q + 3 * r,
        "kRC": 1 + q + r + c,
        "kA2": 4 + q + 2 * a,
    }, (a, r, c, q)


def main(path: str) -> None:
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    assert data["schema"] == "jc2.square.positive_load_fan.cells.v1"
    assert data["candidate_count"] == ((1 << 7) - 1) * 8
    assert data["candidate_count"] == data["satisfiable_cell_count"] + data["unsat_candidate_count"]
    seen = set()
    for cell in data["cells"]:
        form_values, (a, r, c, q) = values(cell["witness"])
        assert a >= 0 and r >= 0 and c >= 0 and q > 0
        actual = tuple(name for name in NAMES if form_values[name] == min(form_values.values()))
        expected = tuple(cell["active"])
        assert actual == expected, (actual, expected, cell)
        for name, value in zip(("a", "r", "c"), (a, r, c)):
            assert (value == 0) == (name in cell["zero"])
            assert (value > 0) == (name in cell["positive"])
        key = (expected, tuple(cell["zero"]), tuple(cell["positive"]))
        assert key not in seen
        seen.add(key)
    assert len(seen) == data["satisfiable_cell_count"]
    print("PASS_EXACT_RATIONAL_WITNESSES")
    print("checked_cells=" + str(len(seen)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_positive_load_fan.py CELLS.json")
    main(sys.argv[1])

