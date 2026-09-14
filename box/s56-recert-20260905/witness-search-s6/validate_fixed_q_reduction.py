#!/usr/bin/env python3
"""Deterministically cross-check the fast fixed-Q recurrence against full rows."""

from __future__ import annotations

import importlib.util
import json
import random
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


RC = load("reduced_centered", "reduced_centered.py")
FULL = load("search_linear_q", "search_linear_q.py")


def main():
    prime = 32003
    seed = 20260905
    trials = 250
    rng = random.Random(seed)
    generators = [(r, e) for r in range(5) for e in range(3 * (6 - r) + 1)]
    for trial in range(trials):
        q_reduced = {6: {0: 1}}
        for r, e in rng.sample(generators, rng.randint(1, 9)):
            q_reduced.setdefault(r, {})[e] = rng.randrange(1, prime)
        reduced_rows, reduced_target, _ = RC.reduce_q(q_reduced, prime)
        reduced_ok, reduced_functional, _ = RC.solve(reduced_rows, reduced_target, prime)

        q_full = {(e, r): coefficient
                  for r, polynomial in q_reduced.items()
                  for e, coefficient in polynomial.items()}
        full_rows, full_target = FULL.system(q_full, prime)
        pivots, inconsistent = FULL.echelon(full_rows, prime)
        full_const, full_free = FULL.reduce_functional(full_target, pivots, prime)
        full_ok = not inconsistent
        full_nonzero_target = bool(full_ok and (full_const or full_free))
        reduced_nonzero_target = bool(reduced_ok and any(reduced_functional))
        if reduced_ok != full_ok or reduced_nonzero_target != full_nonzero_target:
            raise AssertionError({
                "trial": trial,
                "reduced_ok": reduced_ok,
                "full_ok": full_ok,
                "reduced_nonzero_target": reduced_nonzero_target,
                "full_nonzero_target": full_nonzero_target,
                "q": q_reduced,
            })
    print(json.dumps({
        "status": "PASS",
        "prime": prime,
        "seed": seed,
        "trials": trials,
        "comparison": "fast recurrence versus all 144 bounded P coefficients",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
