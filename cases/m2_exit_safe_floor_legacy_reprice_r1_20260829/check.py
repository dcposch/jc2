#!/usr/bin/env python3
"""Exact-Q replay for the post-arity safe-floor repricing report.

This is deliberately independent of the legacy enumerators.  It reconstructs
the ten dirty td=12 frames from their closed formulas, reads the frozen LL-1
R3 book as data, and reweights its already-enumerated transition graph.
"""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict, deque
from fractions import Fraction
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LL1_REL = Path("cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json")
LL1_SHA256 = "205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def old_floor(delta: Fraction) -> int:
    require(delta > 0, "defect must be positive")
    return max(1, ceil_fraction(delta))


def safe_floor(delta: Fraction) -> int:
    """Floor for the full actual exit set, not a representative witness."""
    require(delta > 0, "defect must be positive")
    if delta.denominator == 1:
        return delta.numerator
    return ceil_fraction(2 * delta)


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def td12_frame(eps: int, k: int, nu: int) -> dict[str, object]:
    """Closed l=2, Sm=k, lex=0 dirty-frame reconstruction."""
    l = 2
    dp = eps + nu * (l + k)
    dq = 1 + nu * (1 + k)
    E = l * dq - dp
    kbar = Fraction(9 * dq, E)
    X = Fraction(9 * dp, E)
    require(kbar.denominator == 1, "td12 kbar is not integral")
    defects = [X - kbar for _ in range(k)]  # every nonzero root is simple
    old_ne = sum(old_floor(delta) for delta in defects)
    safe_ne = sum(safe_floor(delta) for delta in defects)
    zero = 0
    if eps:
        zero = old_floor((X / eps - kbar) / nu)
    return {
        "eps": eps,
        "k": k,
        "nu": nu,
        "dp": dp,
        "dq": dq,
        "E": E,
        "kbar": ftext(kbar),
        "X": ftext(X),
        "delta_each": ftext(defects[0]),
        "nonzero_old": old_ne,
        "nonzero_safe": safe_ne,
        "zero_separate": zero,
        "total_old": old_ne + zero,
        "total_safe": safe_ne + zero,
        "w_child": ftext(Fraction(9 * (1 + k), E)),
        "M_child": gcd(dp, dq),
    }


def reprice_cell(cell: dict[str, object]) -> dict[str, object]:
    X = Fraction(str(cell["X"]))
    kbar = Fraction(str(cell["kbar"]))
    defects = [X / int(mult) - kbar for mult in cell["mults"]]
    old_ne = sum(old_floor(delta) for delta in defects)
    safe_ne = sum(safe_floor(delta) for delta in defects)
    eps = int(cell["eps"])
    zero = 0
    if eps:
        zero = old_floor((X / eps - kbar) / int(cell["nu"]))
    require(old_ne + zero == int(cell["lam"]), "legacy cell price did not replay")
    return {
        "defects": tuple(defects),
        "nonzero_old": old_ne,
        "nonzero_safe": safe_ne,
        "zero_separate": zero,
        "total_old": old_ne + zero,
        "total_safe": safe_ne + zero,
    }


def cell_key(cell: dict[str, object]) -> tuple[object, ...]:
    return (
        int(cell["dp"]), int(cell["dq"]), int(cell["nu"]), int(cell["l"]),
        int(cell["eps"]), int(cell["k"]), tuple(cell["mults"]),
        str(cell["kbar"]), str(cell["X"]),
    )


def terminal_verdict(w: Fraction, M: int, charge: int) -> str:
    if not w < 1 or M < 2:
        return "TERMINAL-REJECTED"
    j = M * (1 - w)
    if j.denominator != 1 or j < 1:
        return "TERMINAL-REJECTED"
    psi = ceil_fraction(1 / (1 - w)) - 1
    budget = 6 - 1 - psi
    if charge < budget:
        return "ALIVE"
    if charge == budget:
        return "ALIVE_FRAGILE"
    return "DEAD"


def state_record(state: tuple[Fraction, int, int], verdict: str) -> list[object]:
    return [ftext(state[0]), state[1], state[2], verdict]


def main() -> None:
    fixtures = {
        "3/2": safe_floor(Fraction(3, 2)),
        "8": safe_floor(Fraction(8)),
        "4/3": safe_floor(Fraction(4, 3)),
    }
    require(fixtures == {"3/2": 3, "8": 8, "4/3": 3}, "fixture failure")

    td12_specs = (
        (0, 1, 7), (0, 1, 25), (0, 2, 5), (0, 2, 17),
        (0, 4, 13), (0, 8, 11),
        (1, 1, 2), (1, 1, 8), (1, 2, 4), (1, 4, 2),
    )
    td12 = [td12_frame(*spec) for spec in td12_specs]
    require(len(td12) == 10, "wrong td12 dirty-frame count")
    require(all(row["nonzero_old"] == row["nonzero_safe"] for row in td12),
            "unexpected td12 repricing")
    require([row["total_old"] for row in td12]
            == [6, 8, 6, 8, 8, 8, 9, 9, 9, 9],
            "td12 legacy totals drifted")

    # Small reviewed td7 route control: A, U, and the final epsilon suffix T.
    td7_controls = [
        {"cell": "(21,15)@nu7", "delta": Fraction(2), "zero": 0},
        {"cell": "(35,15)@nu7", "delta": Fraction(1, 2), "zero": 0},
        {"cell": "(63,9)@nu4", "delta": Fraction(1, 3), "zero": 1},
    ]
    for row in td7_controls:
        row["old_nonzero"] = old_floor(row["delta"])
        row["safe_nonzero"] = safe_floor(row["delta"])
        require(row["old_nonzero"] == row["safe_nonzero"], "td7 control changed")

    ll1_path = ROOT / LL1_REL
    blob = ll1_path.read_bytes()
    require(hashlib.sha256(blob).hexdigest() == LL1_SHA256, "LL1 input hash drift")
    book = json.loads(blob)

    unique_cells: dict[tuple[object, ...], dict[str, object]] = {}
    for row in book["sections"]["residue_steps"]:
        if "cell" in row:
            unique_cells[cell_key(row["cell"])] = row["cell"]
    require(len(unique_cells) == 16, "LL1 unique-cell count drifted")

    changed = []
    for key, cell in sorted(unique_cells.items()):
        priced = reprice_cell(cell)
        if priced["total_safe"] != priced["total_old"]:
            changed.append({
                "cell": [int(cell["dp"]), int(cell["dq"]), int(cell["nu"])],
                "l": int(cell["l"]),
                "eps": int(cell["eps"]),
                "mults": list(cell["mults"]),
                "X": str(cell["X"]),
                "kbar": str(cell["kbar"]),
                "defects": [ftext(value) for value in priced["defects"]],
                "nonzero_old": priced["nonzero_old"],
                "nonzero_safe": priced["nonzero_safe"],
                "zero_separate": priced["zero_separate"],
                "total_old": priced["total_old"],
                "total_safe": priced["total_safe"],
                "M_child": int(cell["M_child"]),
            })
    expected_changed = {
        (17, 5, 2), (51, 15, 7), (85, 25, 12), (119, 35, 17),
    }
    require({tuple(row["cell"]) for row in changed} == expected_changed,
            "LL1 changed-cell set drifted")

    # Reweight only the frozen transition graph.  Costs only increase, so an
    # edge affordable after repricing was already emitted from the same
    # reduced (w,M) source at an equal-or-lower old accumulated charge.
    templates: dict[tuple[object, ...], tuple[object, ...]] = {}
    for row in book["sections"]["residue_steps"]:
        if row.get("verdict") != "STEP":
            continue
        src = (Fraction(row["from"][0]), int(row["from"][1]))
        dst = (Fraction(row["to"][0]), int(row["to"][1]))
        old_cost = int(row["to"][2]) - int(row["from"][2])
        if "cell" in row:
            new_cost = int(reprice_cell(row["cell"])["total_safe"])
            label = ("CELL",) + cell_key(row["cell"])
        else:
            new_cost = old_cost
            label = ("OTHER", row["step"])
        key = (src, dst, label)
        value = (src, dst, old_cost, new_cost)
        if key in templates:
            require(templates[key] == value, "inconsistent transition template")
        templates[key] = value

    outgoing: dict[tuple[Fraction, int], list[tuple[object, ...]]] = defaultdict(list)
    for value in templates.values():
        outgoing[value[0]].append(value)

    start = (Fraction(3, 2), 2, 0)
    seen: set[tuple[Fraction, int, int]] = set()
    queue = deque([start])
    while queue:
        state = queue.popleft()
        if state in seen:
            continue
        seen.add(state)
        w, M, charge = state
        for _src, dst, _old_cost, new_cost in outgoing[(w, M)]:
            child = (dst[0], dst[1], charge + int(new_cost))
            if child[2] <= 4:
                queue.append(child)
    require(len(seen) == 17, "repriced LL1 state count drifted")

    old_alive = {
        (Fraction(row["state"][0]), int(row["state"][1]), int(row["state"][2]),
         row["verdict"])
        for row in book["sections"]["residue_terminals"]
        if row["verdict"] in ("ALIVE", "ALIVE_FRAGILE")
    }
    new_alive = {
        (w, M, charge, terminal_verdict(w, M, charge))
        for w, M, charge in seen
        if terminal_verdict(w, M, charge) in ("ALIVE", "ALIVE_FRAGILE")
    }
    removed = old_alive - new_alive
    require(len(old_alive) == 13 and len(new_alive) == 7 and len(removed) == 6,
            "LL1 alive-inventory count drifted")
    require(not (new_alive - old_alive), "repricing unexpectedly added an alive row")

    payload = {
        "fixtures": fixtures,
        "td12": {
            "dirty_rows": td12,
            "nonzero_floor_increases": 0,
            "other_rows": {"clean_neutral": 2, "pure_epsilon": 1},
        },
        "td7_route_controls": [
            {
                "cell": row["cell"], "delta": ftext(row["delta"]),
                "old_nonzero": row["old_nonzero"],
                "safe_nonzero": row["safe_nonzero"], "zero_separate": row["zero"],
            }
            for row in td7_controls
        ],
        "ll1": {
            "input_sha256": LL1_SHA256,
            "unique_dirty_cells": len(unique_cells),
            "changed_cells": changed,
            "old_alive_count": len(old_alive),
            "new_alive_count": len(new_alive),
            "removed_alive_rows": [
                state_record((row[0], row[1], row[2]), row[3])
                for row in sorted(removed, key=lambda item: (item[2], str(item[0]), item[1]))
            ],
            "new_alive_rows": [
                state_record((row[0], row[1], row[2]), row[3])
                for row in sorted(new_alive, key=lambda item: (item[2], str(item[0]), item[1]))
            ],
        },
        "verdict": "PASS_EXACT_REPRICE",
    }
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
