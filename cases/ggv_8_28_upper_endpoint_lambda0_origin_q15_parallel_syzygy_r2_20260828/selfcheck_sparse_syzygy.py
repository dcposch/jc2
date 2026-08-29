#!/usr/bin/env python3
"""Small deterministic checks for the frozen sparse modular solver."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOLVER = HERE / "search_sparse_syzygy.py"


def load_solver():
    spec = importlib.util.spec_from_file_location("ggv_sparse_solver_selfcheck", SOLVER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main():
    solver = load_solver()
    prime = 65521
    columns = [
        {("x",): 1, ("y",): 1},
        {("x",): 1, ("y",): prime - 1},
    ]
    rows = {
        ("x",): {0: 1, 1: 1},
        ("y",): {0: 1, 1: prime - 1},
    }
    solution, info = solver.solve(rows, {("x",): 2}, 2, prime)
    assert solution is not None
    replay = {}
    for coefficient, column in zip(solution, columns):
        solver.add_scaled(replay, column, coefficient, prime)
    assert replay == {("x",): 2}
    inconsistent_rows = {**rows, ("z",): {}}
    impossible, inconsistent = solver.solve(inconsistent_rows, {("z",): 1}, 2, prime)
    assert impossible is None and inconsistent["inconsistent_row"] == ["z"]
    assert solver.degree({(): 1, ("x",): 2, ("x", "y"): 3}) == 2
    assert list(solver.monomials_upto(["x", "y"], 2)) == [
        (), ("x",), ("y",), ("x", "x"), ("x", "y"), ("y", "y")
    ]
    print(json.dumps({
        "status": "SPARSE_SOLVER_SELFCHECK_PASS",
        "prime": prime,
        "solution": solution,
        "rank": info["rank"],
        "replay": {"x": replay[("x",)]},
        "inconsistent_control": True,
        "inhomogeneous_total_degree_control": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
