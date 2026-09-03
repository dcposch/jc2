#!/usr/bin/env python3
"""Emit the exact Q(sqrt(15)) t=4 unit-certificate computation."""

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
OUT = HERE / "t4_exact_Qsqrt15_nfmodstd.sing"
TP_HASH = "f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    tp_path = INPUT / "triangular_preprocess.py"
    if digest(tp_path) != TP_HASH:
        raise RuntimeError("frozen triangular source hash mismatch")
    spec = importlib.util.spec_from_file_location("t4_cert_tp", tp_path)
    tp = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = tp
    spec.loader.exec_module(tp)

    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    if audit["vars"] != ["b3", "b4", "a2_0", "q3_0"]:
        raise RuntimeError("unexpected residual coordinate system")
    if [(r["source"], r["band"]) for r in audit["residual"]] != [
        (5, 0), (11, 1), (17, 2), (23, 3),
        (29, 4), (34, 5), (39, 6), (44, 7),
    ]:
        raise RuntimeError("unexpected residual rows")

    y, s = sp.symbols("q9_1 sqrt15")
    b3, b4, a2, q3 = sp.symbols("b3 b4 a2_0 q3_0")
    old_symbols = {str(z): z for z in (y, b3, b4, a2, q3)}
    target_variables = [s, b3, b4, a2, q3]
    H = 486*y**2 - 270*y + 35
    y_image = (15+s)/54
    if sp.factor(H.subs(y, y_image) - (s**2-15)/6) != 0:
        raise AssertionError("quadratic-field map identity failed")
    rows = []
    for record in audit["residual"]:
        expr = sp.sympify(record["expr"], locals=old_symbols)
        transformed = sp.expand(expr.subs(y, y_image))
        if transformed.free_symbols - set(target_variables):
            raise AssertionError("unexpected transformed symbol")
        rows.append(tp.singular_polynomial(transformed, target_variables))

    audit_hash = digest(AUDIT)
    lines = [
        'LIB "resources.lib";',
        "setcores(1);",
        'LIB "nfmodstd.lib";',
        "// exact characteristic-zero number-field computation",
        "// affine audit sha256=" + audit_hash,
        "// q9_1=(15+sqrt15)/54 and H4 maps to (sqrt15^2-15)/6",
        "ring RAC=0,(gamma,pi),dp;",
        "poly FAC=pi;",
        "poly GAC=pi-(gamma^2)/2;",
        "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
        'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
        ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
        'if (nameof(basering)=="RAC") { print("CONTROL_RAC_RING_PASS"); }'
        ' else { print("CONTROL_RAC_RING_FAIL"); }',
        "ideal RACE=gamma,pi*gamma-1;",
        "ideal RACGE=std(RACE);",
        'if (typeof(RACGE)=="ideal" && reduce(1,RACGE)==0)'
        ' { print("CONTROL_RAC_EMPTY_PASS"); }'
        ' else { print("CONTROL_RAC_EMPTY_FAIL"); }',
        "ideal RACN=gamma-1,pi*gamma-1;",
        "ideal RACGN=std(RACN);",
        'if (typeof(RACGN)=="ideal" && reduce(1,RACGN)!=0)'
        ' { print("CONTROL_RAC_NONEMPTY_PASS"); }'
        ' else { print("CONTROL_RAC_NONEMPTY_FAIL"); }',
        "ring RC=(0,sqrt15),(u,W),dp;",
        "minpoly=sqrt15^2-15;",
        "number cbar=-325*sqrt15/59049-715/19683;",
        "number cbar_inverse=1/cbar;",
        'if (cbar*cbar_inverse==1) { print("CONTROL_C_UNIT_PASS"); }'
        ' else { print("CONTROL_C_UNIT_FAIL"); }',
        'if (nameof(basering)=="RC") { print("CONTROL_RC_RING_PASS"); }'
        ' else { print("CONTROL_RC_RING_FAIL"); }',
        "ideal RCE=u,W*u-1;",
        "ideal RCGE=std(RCE);",
        'if (typeof(RCGE)=="ideal" && reduce(1,RCGE)==0)'
        ' { print("CONTROL_RC_EMPTY_PASS"); }'
        ' else { print("CONTROL_RC_EMPTY_FAIL"); }',
        "ideal RCN=u-1,W*u-1;",
        "ideal RCGN=std(RCN);",
        'if (typeof(RCGN)=="ideal" && reduce(1,RCGN)!=0)'
        ' { print("CONTROL_RC_NONEMPTY_PASS"); }'
        ' else { print("CONTROL_RC_NONEMPTY_FAIL"); }',
        "ring RK=(0,sqrt15),(b3,b4,a2_0,q3_0),dp;",
        "minpoly=sqrt15^2-15;",
        "option(redSB);",
        'if (nameof(basering)=="RK") { print("CONTROL_RK_RING_PASS"); }'
        ' else { print("CONTROL_RK_RING_FAIL"); }',
        "ideal RKE=b3,b4*b3-1;",
        "ideal RKGE=std(RKE);",
        'if (typeof(RKGE)=="ideal" && reduce(1,RKGE)==0)'
        ' { print("CONTROL_RK_EMPTY_PASS"); }'
        ' else { print("CONTROL_RK_EMPTY_FAIL"); }',
        "ideal RKN=b3-1,b4*b3-1;",
        "ideal RKGN=std(RKN);",
        'if (typeof(RKGN)=="ideal" && reduce(1,RKGN)!=0)'
        ' { print("CONTROL_RK_NONEMPTY_PASS"); }'
        ' else { print("CONTROL_RK_NONEMPTY_FAIL"); }',
        'print("MAIN_START t=4 field=Qsqrt15 rows=8 vars=4 method=nfmodStd");',
        "ideal I=" + ",\n".join(rows) + ";",
        "ideal G=nfmodStd(I);",
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (typeof(G)=="ideal" && nameof(basering)=="RK")'
        ' { print("MAIN_EXTRACT_RING_PASS"); }'
        ' else { print("MAIN_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,G)==0) { print("MAIN_EXACT_UNIT"); G; }'
        ' else { print("MAIN_NONUNIT"); G; }',
        "quit;",
    ]
    OUT.write_text("\n".join(lines)+"\n", encoding="utf-8")
    print(f"{OUT} bytes={OUT.stat().st_size} sha256={digest(OUT)}")


if __name__ == "__main__":
    main()
