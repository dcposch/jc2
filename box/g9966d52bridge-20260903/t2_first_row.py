#!/usr/bin/env python3
"""Certify the first nonlinear row of the delta=5/2 effective-T2 bridge."""

from __future__ import annotations

import hashlib
import json
import resource
import time
from pathlib import Path

import sympy as sp

import bridge_engine as bridge


CAP = 56
HERE = Path(__file__).resolve().parent


def t_names() -> set[sp.Symbol]:
    names = {"T2_a1", "T2_a0", "T2_b1", "T2_b0"}
    names.update(bridge.t3_coefficient_names())
    assert len(names) == 38
    return set(map(sp.Symbol, names))


def singular_text(expression: sp.Expr) -> str:
    return str(sp.expand(expression)).replace("**", "^")


def main() -> None:
    started = time.perf_counter()
    custody = bridge.verify_frozen()
    band = bridge.load_charged_module()
    _stage, free_names, joint_map, k2, outer, endpoint = bridge.load_endpoint(band)
    stats = bridge.ArithmeticStats()
    blocks = bridge.block_series(band, k2, outer, CAP, joint_map, stats)
    monic, f_series, g_series, _ef, _eg = bridge.monic_t2_and_FG(blocks, CAP, stats)
    rows = [
        (f"T2_s{n}_pi{k}", sp.expand(expression))
        for (n, k), expression in sorted(monic.items())
        if expression != 0
    ]
    assert len(rows) == 1 and rows[0][0] == "T2_s56_pi0"
    label, row = rows[0]
    assert row != 0

    chart = set(map(sp.Symbol, free_names))
    ambient = chart | t_names()
    c = sp.Symbol("c")
    assert row.free_symbols <= chart and c in chart
    residual, mapping, pivots, zero_rows = band.qstar_reduce(rows, set(ambient) - {c})
    assert zero_rows == 0
    assert len(mapping) == len(pivots)
    assert all(pivot.coefficient.is_Rational and pivot.coefficient != 0 for pivot in pivots)

    zero_point = {variable: 0 for variable in chart if variable != c}
    zero_point[c] = 1
    assert sp.expand(row.xreplace(zero_point)) == 0
    gauged = sp.expand(row.subs(c, 1))
    assert gauged != 0
    gauged_zero = {variable: 0 for variable in gauged.free_symbols}
    assert gauged.xreplace(gauged_zero) == 0

    active = sorted(row.free_symbols | {c}, key=str)
    inactive = sorted(ambient - set(active), key=str)
    script = f"""// Exact first nonlinear bridge row; all omitted variables are free.
// ambient_variables={len(ambient)} active_variables={len(active)} inactive_variables={len(inactive)}
ring R=0,({','.join(map(str, active))},Zc),dp;
poly r={singular_text(row)};
ideal I=r,Zc*c-1;
ideal G=std(I);
print(\"BEGIN_RESULT\");
print(\"unit_remainder=\"+string(reduce(1,G)));
print(\"active_localized_dimension=\"+string(dim(G)));
print(\"full_dimension_with_inactive=\"+string(dim(G)+{len(inactive)}));
print(\"END_RESULT\");
ideal Czero=c,Zc*c-1;
ideal Cone=c-1,Zc*c-1;
print(\"BEGIN_CONTROLS\");
print(reduce(1,std(Czero)));
print(reduce(1,std(Cone)));
print(\"END_CONTROLS\");
quit;
"""
    singular_path = HERE / "t2-first-row-Q.sing"
    singular_path.write_text(script, encoding="utf-8")

    digest = hashlib.sha256(f"{label}\t{sp.srepr(row)}\n".encode()).hexdigest()
    result = {
        "type": "EXACT-Q FIRST NONLINEAR T2 BRIDGE ROW",
        "status": "COMPLETE[FIRST-ROW]",
        "custody": {"count": custody["count"], "all_match": custody["all_match"]},
        "endpoint": {"free": endpoint["free_count"], "joint_all_zero": endpoint["joint_all_zero"]},
        "normalization": "U2=s^396*T2; all lower coefficients vanish",
        "row": {
            "label": label,
            "sha256_srepr": digest,
            "free_symbol_count": len(row.free_symbols),
            "total_degree": sp.Poly(row, *sorted(row.free_symbols, key=str)).total_degree(),
            "factorization": str(sp.factor(row)),
            "nonzero_over_Q": True,
            "vanishes_at_stage7_point_c1_all_other_chart0": True,
            "nonzero_after_c1_gauge": True
        },
        "Qstar": {
            "pivots": len(pivots),
            "residual_rows": len(residual),
            "coefficient_field": "Q",
            "ledger": [
                {
                    "label": pivot.label,
                    "variable": str(pivot.variable),
                    "coefficient": str(pivot.coefficient),
                    "rhs": str(pivot.rhs)
                }
                for pivot in pivots
            ]
        },
        "dimension_proof": {
            "localized_ambient_after_38_T_coefficients": len(ambient),
            "localized_principal_cut": len(ambient) - 1,
            "c1_gauged_ambient": len(ambient) - 1,
            "c1_gauged_principal_cut": len(ambient) - 2,
            "reason": "The stage7 quotient with the 38 inactive T variables is a localized polynomial domain; this row is nonzero and nonunit, so its principal ideal has height one."
        },
        "singular": {
            "path": str(singular_path.relative_to(HERE.parents[1])),
            "sha256": hashlib.sha256(singular_path.read_bytes()).hexdigest(),
            "active_variables": len(active),
            "inactive_variables": len(inactive)
        },
        "arithmetic": stats.__dict__,
        "resources": {
            "wall_seconds": round(time.perf_counter() - started, 3),
            "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        }
    }
    output = HERE / "t2-first-row.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
