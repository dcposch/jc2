#!/usr/bin/env python3
"""Exact integer dimension checks for the R6 survivor parametrization."""

from __future__ import annotations

import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parent


def strata(h):
    out = []
    for b in range(h + 1):
        if (h - b) % 2:
            continue
        a = (h - b) // 2
        if b == 0:
            out.append({"b": b, "a": a, "survives_degree": True,
                        "dimension": a, "codimension": h - a, "r": None})
            continue
        r = a - b + 1
        survives = r >= 0
        out.append({"b": b, "a": a, "survives_degree": survives,
                    "dimension": a + 1 if survives else None,
                    "codimension": h - a - 1 if survives else None,
                    "r": r})
    return out


def main():
    result = json.loads((ROOT / "RESULT.json").read_text())
    for h in range(2, 65):
        live = [s for s in strata(h) if s["survives_degree"]]
        assert live
        assert min(s["codimension"] for s in live) == h // 2
        for s in live:
            b, a = s["b"], s["a"]
            if b == 0:
                assert h % 2 == 0
                assert s["codimension"] == h // 2
            else:
                assert s["r"] == (h - 3 * b + 2) // 2
                assert s["dimension"] == a + 1
                assert s["codimension"] == (h + b - 2) // 2
                assert 3 * b <= h + 2
        for s in strata(h):
            if s["b"] > 0 and not s["survives_degree"]:
                assert 3 * s["b"] > h + 2

    live8 = [s for s in strata(8) if s["survives_degree"]]
    assert [(s["b"], s["dimension"], s["codimension"]) for s in live8] == [
        (0, 4, 4), (2, 4, 4)
    ]
    assert result["degree8"]["survivor_strata"]["b0_perfect_square"] == {
        "codimension": 4, "dimension": 4
    }
    assert result["degree8"]["survivor_strata"]["b2_quadratic_squarefree_part"] == {
        "codimension": 4, "dimension": 4
    }
    print("PASS R6 endpoint survivor dimension checks")


if __name__ == "__main__":
    main()

