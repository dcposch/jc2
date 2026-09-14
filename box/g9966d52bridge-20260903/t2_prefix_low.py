#!/usr/bin/env python3
"""Exact low-order T2-prefix extractor in the charged stage-7 chart.

This is deliberately filtration-bounded.  It certifies only rows through the
requested s-cap and performs only pivots whose coefficient lies in Q*.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import resource
import time
from pathlib import Path

import sympy as sp

import bridge_engine as bridge


HERE = Path(__file__).resolve().parent


def t_variables() -> set[sp.Symbol]:
    names = {"T2_a1", "T2_a0", "T2_b1", "T2_b0"}
    names.update(bridge.t3_coefficient_names())
    assert len(names) == 38
    return set(map(sp.Symbol, names))


def digest_rows(rows: list[tuple[str, sp.Expr]]) -> str:
    digest = hashlib.sha256()
    for label, expression in rows:
        digest.update(f"{label}\t{sp.srepr(sp.expand(expression))}\n".encode())
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cap", type=int, required=True)
    args = parser.parse_args()
    cap = args.cap
    if not 56 <= cap < 132:
        raise ValueError("this low-prefix driver requires 56 <= cap < 132")

    started = time.perf_counter()
    custody = bridge.verify_frozen()
    band = bridge.load_charged_module()
    _stage, free_names, joint_map, k2, outer, endpoint = bridge.load_endpoint(band)
    stats = bridge.ArithmeticStats()
    blocks = bridge.block_series(band, k2, outer, cap, joint_map, stats)
    monic, F, G, _EF, _EG = bridge.monic_t2_and_FG(blocks, cap, stats)

    # No Tschirnhausen column can occur before s^132: the earliest is
    # s^66*F*G, while min_s(F)=24 and min_s(G)=16.
    assert min(n for n, _k in F) == 24
    assert min(n for n, _k in G) == 16
    assert 66 + 24 + 16 > cap
    rows = [
        (f"T2_s{n}_pi{k}", sp.expand(expression))
        for (n, k), expression in sorted(monic.items())
        if expression != 0
    ]
    assert rows and rows[0][0] == "T2_s56_pi0"

    chart = set(map(sp.Symbol, free_names))
    ambient = chart | t_variables()
    c = sp.Symbol("c")
    residual, mapping, pivots, zero_rows = band.qstar_reduce(rows, ambient - {c})
    assert len(mapping) == len(pivots)
    assert all(p.coefficient.is_Rational and p.coefficient != 0 for p in pivots)
    assert not set(mapping).intersection(
        set().union(*(expression.free_symbols for _label, expression in residual))
        if residual else set()
    )

    ledger_path = HERE / f"t2-prefix-s{cap}-pivots.jsonl"
    ledger_lines = []
    for pivot in pivots:
        ledger_lines.append(json.dumps({
            "row": pivot.label,
            "variable": str(pivot.variable),
            "coefficient": str(pivot.coefficient),
            "rhs": str(pivot.rhs),
        }, sort_keys=True))
    ledger_path.write_text("\n".join(ledger_lines) + ("\n" if ledger_lines else ""), encoding="utf-8")

    result = {
        "type": "EXACT-Q LOW T2 PREFIX / QSTAR ONLY",
        "status": "COMPLETE[LOW-PREFIX-QSTAR]",
        "scope": {
            "cap": cap,
            "normalized_expression": "s^396*T2",
            "Tschirnhausen_columns_present": False,
            "logical_strength": "necessary prefix only",
        },
        "custody": {"count": custody["count"], "all_match": custody["all_match"]},
        "endpoint": {"stage7_free": endpoint["free_count"], "joint_all_zero": endpoint["joint_all_zero"]},
        "rows": {
            "input_count": len(rows),
            "input_sha256": digest_rows(rows),
            "first": rows[0][0],
            "last": rows[-1][0],
            "Qstar_pivots": len(pivots),
            "zero_or_dependent": zero_rows,
            "residual_count": len(residual),
            "residual_sha256": digest_rows(residual),
        },
        "pivots": {
            "ledger": str(ledger_path.relative_to(HERE.parents[1])),
            "ledger_sha256": hashlib.sha256(ledger_path.read_bytes()).hexdigest(),
            "variables": [str(p.variable) for p in pivots],
            "all_coefficients_Qstar": True,
            "localized_variable_excluded": "c",
        },
        "counting": {
            "ambient_stage7_plus_38": len(ambient),
            "dimension_upper_bound_before_J_localization": len(ambient) - len(pivots),
            "c1_slice_upper_bound_before_J_localization": len(ambient) - 1 - len(pivots),
            "warning": "A necessary-prefix bound only; localization may empty the locus and cannot increase dimension.",
        },
        "arithmetic": stats.__dict__,
        "resources": {
            "wall_seconds": round(time.perf_counter() - started, 3),
            "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        },
    }
    output = HERE / f"t2-prefix-s{cap}.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
