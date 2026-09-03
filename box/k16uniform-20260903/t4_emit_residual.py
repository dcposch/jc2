#!/usr/bin/env python3
"""Emit an exact Singular certificate job for the audited t=4 residual."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import pathlib
import sys

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
INPUT = pathlib.Path("/tmp/jc2-lane.fjoTgL/inputs")
AUDIT = HERE / "t4_affine_audit.json"
OUT = HERE / "t4_residual_Qv_slimgb.sing"
H = "486*q9_1^2-270*q9_1+35"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_tp():
    path = INPUT / "triangular_preprocess.py"
    expected = "f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93"
    if digest(path) != expected:
        raise RuntimeError("frozen triangular source hash mismatch")
    spec = importlib.util.spec_from_file_location("t4_emit_frozen_tp", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main():
    tp = load_tp()
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    if len(audit["pivots"]) != 22 or len(audit["residual"]) != 8:
        raise RuntimeError("unexpected affine audit dimensions")
    expected_vars = ["b3", "b4", "a2_0", "q3_0"]
    if audit["vars"] != expected_vars:
        raise RuntimeError("unexpected residual variables")
    names = ["q9_1"] + expected_vars
    symbols = {name: sp.Symbol(name) for name in names}
    variables = [symbols[name] for name in names]
    rows = []
    for item in audit["residual"]:
        expr = sp.sympify(item["expr"], locals=symbols)
        if expr.free_symbols - set(variables):
            raise RuntimeError("undeclared symbol in residual")
        # The charged primitive normalizer verifies g=lambda*f over Q.
        rows.append(tp.singular_polynomial(expr, variables))

    lines = [
        "// exact t=4 residual emitted from t4_affine_audit.json",
        "// audit sha256=" + digest(AUDIT),
        "// coefficient field Q(q9_1), minpoly " + H,
        "// 22 checked affine K-pivots; residual: 8 rows in 4 variables",
        "ring RAC=0,(gamma,pi),dp;",
        "poly FAC=pi;",
        "poly GAC=pi-(gamma^2)/2;",
        "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
        'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
        ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
        "ring RC=(0,q9_1),(u,W),dp;",
        "minpoly=" + H + ";",
        "number cbar=q9_1*(130-1404*q9_1)/2187;",
        "number cbar_inverse=1/cbar;",
        'if (cbar*cbar_inverse==1) { print("CONTROL_C_UNIT_PASS"); }'
        ' else { print("CONTROL_C_UNIT_FAIL"); }',
        "ideal CE=u,W*u-1;",
        "ideal GE=std(CE);",
        'if (typeof(GE)=="ideal" && nameof(basering)=="RC")'
        ' { print("CONTROL_EMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); }'
        ' else { print("CONTROL_EMPTY_FAIL"); }',
        "ideal CN=u-1,W*u-1;",
        "ideal GN=std(CN);",
        'if (typeof(GN)=="ideal" && nameof(basering)=="RC")'
        ' { print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); }'
        ' else { print("CONTROL_NONEMPTY_FAIL"); }',
        "ring RK=(0,q9_1),(b3,b4,a2_0,q3_0),dp;",
        "minpoly=" + H + ";",
        "option(redSB);",
        'if (nameof(basering)=="RK") { print("CONTROL_RING_PASS RK"); }'
        ' else { print("CONTROL_RING_FAIL"); }',
        "ideal RKE=b3,b4*b3-1;",
        "ideal RKGE=std(RKE);",
        'if (typeof(RKGE)=="ideal" && nameof(basering)=="RK")'
        ' { print("CONTROL_RK_EMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_RK_EMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,RKGE)==0) { print("CONTROL_RK_EMPTY_PASS"); }'
        ' else { print("CONTROL_RK_EMPTY_FAIL"); }',
        "ideal RKN=b3-1,b4*b3-1;",
        "ideal RKGN=std(RKN);",
        'if (typeof(RKGN)=="ideal" && nameof(basering)=="RK")'
        ' { print("CONTROL_RK_NONEMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_RK_NONEMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,RKGN)!=0) { print("CONTROL_RK_NONEMPTY_PASS"); }'
        ' else { print("CONTROL_RK_NONEMPTY_FAIL"); }',
        'print("MAIN_START t=4 field=Qv residual_equations=8 residual_unknowns=4");',
        "ideal I=" + ",\n".join(rows) + ";",
        "ideal G=slimgb(I);",
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (typeof(G)=="ideal" && nameof(basering)=="RK")'
        ' { print("MAIN_EXTRACT_RING_PASS"); }'
        ' else { print("MAIN_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,G)==0) { print("MAIN_QUADRATIC_FIELD_EMPTY"); G; }'
        ' else { print("MAIN_QUADRATIC_FIELD_NONTRIVIAL"); G; }',
        "quit;",
    ]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{OUT} bytes={OUT.stat().st_size} sha256={digest(OUT)}")


if __name__ == "__main__":
    main()
