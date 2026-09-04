#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from math import factorial
import importlib.util
import json
from pathlib import Path
import sys

import sympy as sp


ENGINE = Path("box/g108gate-20260903/band_engine.py")


def load_engine():
    spec = importlib.util.spec_from_file_location("g108gate_engine", ENGINE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {ENGINE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def rows_with_linear_term(engine, cutoff: int):
    h3, variables = engine.h3_template(cutoff)
    wbasis = engine.z_to_w(h3)
    jet1, jet2, c, b = sp.symbols("jet1 jet2 c b")
    collected = defaultdict(lambda: sp.Integer(0))
    for (r, j), coefficient in wbasis.items():
        for a in range(j + 1):
            for bb in range(j - a + 1):
                k = j - a - bb
                local_power = r + 2 * a + 3 * bb + 4 * k
                if local_power > 8:
                    continue
                multinomial = factorial(j) // (factorial(a) * factorial(bb) * factorial(k))
                collected[(local_power, k)] += coefficient * multinomial * jet1**a * jet2**bb
    # Equation actual - target = 0 for K3=-t^8*(pi^2+b*pi-c)+O(t^9).
    collected[(8, 0)] -= c
    collected[(8, 1)] += b
    collected[(8, 2)] += 1
    return [
        (f"minor_n{power}_pi{k}", sp.expand(value))
        for (power, k), value in sorted(collected.items())
    ], variables


def main() -> None:
    engine = load_engine()
    variants = []
    for cutoff in (43, 42):
        rows, hvars = rows_with_linear_term(engine, cutoff)
        residual, substitutions, pivots, zeros = engine.qstar_reduce(rows, hvars)
        variants.append(
            {
                "variant": f"linear_term_free_cutoff_{cutoff}",
                "target": "K3=-t^8*(pi^2+b*pi-c)+O(t^9)",
                "h3_coordinates": len(hvars),
                "qstar_pivots": len(pivots),
                "zero_rows": zeros,
                "substitutions": {str(k): str(v) for k, v in substitutions.items()},
                "residual": {label: str(sp.expand(value)) for label, value in residual},
                "residual_count": len(residual),
                "notes": [
                    "b is excluded from Q-star pivots",
                    "this weakens only the translation gauge; it still uses one common h3 polynomial",
                ],
            }
        )
    print(json.dumps({"type": "D108-HOSTILE-INCIDENCE-VARIANTS", "variants": variants}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
