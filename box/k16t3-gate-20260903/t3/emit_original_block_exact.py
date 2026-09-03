#!/usr/bin/env python3
"""Emit exact-Q original t=3 Rabinowitsch attempts with a block order.

This is intentionally gate-local.  It imports the frozen-hash replay driver
beside this file, rebuilds the unpreprocessed gauged t=3 equations, and only
changes the Singular monomial order/method.
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
DRIVER = HERE / "t_order_system.py"


def load_driver():
    spec = importlib.util.spec_from_file_location("gate_t_order_system", DRIVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load %s" % DRIVER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(method: str) -> str:
    if method not in {"slimgb", "modstd"}:
        raise ValueError(method)
    drv = load_driver()
    data = drv.build(t=3, gauged=True)
    params = list(data["params"])
    c = data["c"]
    T = sp.Symbol("T")

    pivot_names = [
        "a4_1", "a5_1", "a6_1", "a7_2", "a7_1", "a8_2", "a8_1",
        "a9_2", "a9_1", "a10_2", "a10_1", "a10_0", "a10_3",
    ]
    by_name = {str(v): v for v in params}
    pivots = [by_name[name] for name in pivot_names]
    rest = [v for v in params if str(v) not in set(pivot_names)]
    variables = pivots + rest + [c, T]

    lines = [
        "// gate exact-Q original t=3 Rabinowitsch attempt",
        "// equations are rebuilt from t_order_system.py; only order/method differ",
        "// variable blocks: audited high-level pivot variables, residual chart variables, c/T",
        'LIB "elim.lib";',
    ]
    if method == "modstd":
        lines.extend(['LIB "modstd.lib";', "setcores(1);"])
    lines.extend([
        "ring RAC=0,(gamma,pi),dp;",
        "poly FAC=pi;",
        "poly GAC=pi-(gamma^2)/2;",
        "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
        'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
        ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
        "ring R=0,(%s),(dp(13),dp(22),dp(2));" % ",".join(map(str, variables)),
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); }'
        ' else { print("CONTROL_RING_FAIL"); }',
        "ideal C=c;",
        "ideal CE=c;",
        "list LE=sat(CE,C);",
        "ideal SE=LE[1];",
        'if (typeof(SE)=="ideal" && nameof(basering)=="R" && reduce(1,std(SE))==0)'
        ' { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
        "ideal CN=c-1;",
        "list LN=sat(CN,C);",
        "ideal SN=LN[1];",
        'if (typeof(SN)=="ideal" && nameof(basering)=="R" && reduce(1,std(SN))!=0)'
        ' { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
        'print("MAIN_START equations=%d chart_unknowns=%d plus_T=1 order=dp13_dp22_dp2 method=%s");'
        % (len(data["equations"]), len(params) + 1, method),
    ])
    generators = [drv.singular(expr) for expr in data["equations"]]
    generators.append("T*c-1")
    lines.append("ideal I=%s;" % ",\n".join(generators))
    if method == "slimgb":
        lines.append("ideal G=slimgb(I);")
    else:
        lines.append('print("METHOD_MODSTD_EXACTNESS_1_CORES_1");')
        lines.append("ideal G=modStd(I,1);")
    lines.extend([
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); G; }'
        ' else { print("MAIN_NONTRIVIAL_SUPERSET_ONLY");'
        ' print("BASIS_OUTPUT_TRUNCATED_TO_10");'
        ' int basis_cap=size(G); if (basis_cap>10) { basis_cap=10; }'
        ' for (int basis_i=1; basis_i<=basis_cap; basis_i++) { G[basis_i]; } }',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    for method in ("slimgb", "modstd"):
        (HERE / ("t3_original_block_%s.sing" % method)).write_text(
            emit(method), encoding="utf-8"
        )


if __name__ == "__main__":
    main()
