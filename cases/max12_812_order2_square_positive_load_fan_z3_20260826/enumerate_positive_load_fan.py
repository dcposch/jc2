#!/usr/bin/env python3
"""Enumerate exact rational cells of the seven-form positive-load fan."""

from __future__ import annotations

import itertools
import json
import os
from fractions import Fraction

import z3


NAMES = ("AC", "C2", "RA2", "A3", "kR3", "kRC", "kA2")


def qstr(value: z3.ArithRef) -> str:
    value = z3.simplify(value)
    if z3.is_rational_value(value):
        return str(value.numerator_as_long()) + "/" + str(value.denominator_as_long())
    raise RuntimeError("non-rational model value: " + str(value))


def main() -> None:
    out_dir = os.environ.get("FAN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    a, r, c, q = z3.Reals("a r c q")
    variables = (a, r, c, q)
    forms = (
        a + c,
        2 * c,
        2 + r + 2 * a,
        5 + 3 * a,
        q + 3 * r,
        1 + q + r + c,
        4 + q + 2 * a,
    )

    cells = []
    candidate_count = 0
    unsat_count = 0
    for mask in range(1, 1 << len(NAMES)):
        active = tuple(i for i in range(len(NAMES)) if mask & (1 << i))
        inactive = tuple(i for i in range(len(NAMES)) if not mask & (1 << i))
        anchor = active[0]
        for zero_bits in itertools.product((0, 1), repeat=3):
            candidate_count += 1
            solver = z3.Solver()
            solver.set(random_seed=0)
            solver.add(a >= 0, r >= 0, c >= 0, q > 0)
            for var, is_positive in zip((a, r, c), zero_bits):
                solver.add(var > 0 if is_positive else var == 0)
            for i in active[1:]:
                solver.add(forms[i] == forms[anchor])
            for j in inactive:
                solver.add(forms[anchor] < forms[j])
            status = solver.check()
            if status == z3.unsat:
                unsat_count += 1
                continue
            if status != z3.sat:
                raise RuntimeError("solver returned " + str(status))
            model = solver.model()
            witness = {str(v): qstr(model.eval(v, model_completion=True)) for v in variables}
            cells.append(
                {
                    "active": [NAMES[i] for i in active],
                    "positive": [name for name, bit in zip(("a", "r", "c"), zero_bits) if bit],
                    "zero": [name for name, bit in zip(("a", "r", "c"), zero_bits) if not bit],
                    "witness": witness,
                }
            )

    cells.sort(key=lambda x: (len(x["active"]), x["active"], x["zero"], x["positive"]))
    payload = {
        "schema": "jc2.square.positive_load_fan.cells.v1",
        "z3_python_version": z3.get_version_string(),
        "forms": {
            "AC": "a+c",
            "C2": "2*c",
            "RA2": "2+r+2*a",
            "A3": "5+3*a",
            "kR3": "q+3*r",
            "kRC": "1+q+r+c",
            "kA2": "4+q+2*a",
        },
        "domain": ["a>=0", "r>=0", "c>=0", "q>0"],
        "candidate_count": candidate_count,
        "satisfiable_cell_count": len(cells),
        "unsat_candidate_count": unsat_count,
        "cells": cells,
    }
    path = os.path.join(out_dir, "positive_load_fan_cells.json")
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print("z3_python_version=" + z3.get_version_string())
    print("candidate_count=" + str(candidate_count))
    print("satisfiable_cell_count=" + str(len(cells)))
    print("unsat_candidate_count=" + str(unsat_count))
    print("cells_path=" + path)


if __name__ == "__main__":
    main()

