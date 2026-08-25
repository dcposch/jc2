#!/usr/bin/env python3
"""V3: emit the coefficient-projective closure plus exact source controls."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
ORDER3 = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
ORDER3_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"


def load_compiler():
    for path, expected in ((COMPILER, COMPILER_SHA256), (ORDER3, ORDER3_SHA256)):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_rankdrop_b1_cinf_v3_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def clean(value):
    return {monomial: scalar for monomial, scalar in value.items() if scalar}


def relative_homogenize(value, c_index: int = 1):
    degree = max((monomial[c_index] for monomial in value), default=0)
    out = {}
    for monomial, scalar in value.items():
        c_power = monomial[c_index]
        # names become (w,C0,C1,d2,d4,x1,x3,x5)
        new_monomial = (
            monomial[0], c_power, degree - c_power,
            monomial[2], monomial[3], monomial[4], monomial[5], monomial[6],
        )
        out[new_monomial] = out.get(new_monomial, 0) + scalar
    return degree, clean(out)


def dehomogenize_c1_one(value):
    out = {}
    for monomial, scalar in value.items():
        # C0 -> c and C1 -> 1.
        original = (
            monomial[0], monomial[1], monomial[3], monomial[4],
            monomial[5], monomial[6], monomial[7],
        )
        out[original] = out.get(original, 0) + scalar
    return clean(out)


def scaling_lift(value, scaled: bool):
    out = {}
    for monomial, scalar in value.items():
        lam_power = monomial[1] + monomial[2] if scaled else 0
        lifted = (lam_power,) + monomial
        out[lifted] = out.get(lifted, 0) + scalar
    return clean(out)


def degree_rhs(value, degree: int):
    return {(degree,) + monomial: scalar for monomial, scalar in value.items()}


def source(engine: str, order: str) -> str:
    q = load_compiler()
    names, rows, imposed, _ = q.compile_quotient("approx")
    if tuple(names) != ("w", "c", "d2", "d4", "x1", "x3", "x5"):
        raise RuntimeError(names)
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)

    onames = ("w", "c", "d2", "d4", "x1", "x3", "x5")
    hnames = ("w", "C0", "C1", "d2", "d4", "x1", "x3", "x5")
    lnames = ("lam",) + hnames
    homogeneous = {}
    degrees = {}
    dehomogeneous = {}
    scaled = {}
    scaling_rhs = {}
    for ell in imposed:
        degrees[ell], homogeneous[ell] = relative_homogenize(rows[ell])
        dehomogeneous[ell] = dehomogenize_c1_one(homogeneous[ell])
        scaled[ell] = scaling_lift(homogeneous[ell], scaled=True)
        scaling_rhs[ell] = degree_rhs(homogeneous[ell], degrees[ell])
        if dehomogeneous[ell] != clean(rows[ell]):
            raise RuntimeError(("dehomogenization", ell))
        if scaled[ell] != scaling_rhs[ell]:
            raise RuntimeError(("scaling", ell))
        if any(monomial[1] + monomial[2] != degrees[ell] for monomial in homogeneous[ell]):
            raise RuntimeError(("homogeneity", ell))
    expected = {1: 1, 3: 2, 5: 3, 7: 3, 2: 2, 4: 2}
    if degrees != expected:
        raise RuntimeError((degrees, expected))

    lines = ["ring O=0,(w,c,d2,d4,x1,x3,x5),dp;"]
    for ell in imposed:
        lines.append(f"poly ose{ell}={q.M.coeff_string(rows[ell], onames)};")
        lines.append(f"poly odeh{ell}={q.M.coeff_string(dehomogeneous[ell], onames)};")
        lines.append(f"poly odiff{ell}=ose{ell}-odeh{ell};")
    zero_test = " || ".join(f"odiff{ell}!=0" for ell in imposed)
    lines.extend([
        f"int dehomogenization_zero=1;if({zero_test}){{dehomogenization_zero=0;}}",
        'if(dehomogenization_zero==0){print("DEHOMOGENIZATION_CONTROL_FAIL");exit;}',
        'print("dehomogenization_control=1");',
        f"ring L=0,({','.join(lnames)}),dp;",
    ])
    for ell in imposed:
        lines.append(f"poly lscaled{ell}={q.M.coeff_string(scaled[ell], lnames)};")
        lines.append(f"poly lrhs{ell}={q.M.coeff_string(scaling_rhs[ell], lnames)};")
        lines.append(f"poly ldiff{ell}=lscaled{ell}-lrhs{ell};")
    scaling_test = " || ".join(f"ldiff{ell}!=0" for ell in imposed)
    lines.extend([
        f"int scaling_zero=1;if({scaling_test}){{scaling_zero=0;}}",
        'if(scaling_zero==0){print("SCALING_CONTROL_FAIL");exit;}',
        'print("homogeneity_control=1");',
        'print("scaling_control=1");',
        "ring S=0,(w,C0,C1,d2,d4,x1,x3,x5),dp;",
    ])
    for ell in imposed:
        lines.append(f"poly he{ell}={q.M.coeff_string(homogeneous[ell], hnames)};")
    lines.append("ideal HSI=he1,he3,he5,he7,he2,he4;")
    ordering = "(dp(1),dp(8))" if order == "dp" else "(dp(1),dp(2),dp(6))"
    lines.extend([
        f"ring R=0,(zinv,C0,C1,v,w,u,x1,x3,x5),{ordering};",
        "option(redSB);",
        "map phi=S,w,C0,C1,2+v+u,1+v,x1,x3,x5;",
        "ideal I=phi(HSI);poly A=x3-2*x5;poly f=w*x5*A;",
        "ideal K=I,zinv*C1*f-1;",
        f"ideal GK={engine}(K);",
        "ideal Clos=eliminate(GK,zinv);",
        f"ideal GClos={engine}(Clos);",
        "ideal Infinity=GClos,C0-1,C1;",
        f"ideal GInf={engine}(Infinity);",
        "ideal Landing=GInf,v,w,u,x1,x3,x5;",
        f"ideal GLand={engine}(Landing);",
        "int infinity_empty=0;if(reduce(1,GInf)==0){infinity_empty=1;}",
        "int landing_empty=0;if(reduce(1,GLand)==0){landing_empty=1;}",
        'print("Q8-W0-RANKDROP-B1-C-INFINITY-V3");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("c_degrees=1,2,3,3,2,2");',
        'print("source_controls=homogeneous,dehomogenization-C1-one,projective-scaling");',
        'print("infinity_empty="+string(infinity_empty));',
        'print("landing_empty="+string(landing_empty));',
        'print("CLOSURE_BASIS_BEGIN");GClos;print("CLOSURE_BASIS_END");',
        'print("INFINITY_BASIS_BEGIN");GInf;print("INFINITY_BASIS_END");',
        'print("LANDING_BASIS_BEGIN");GLand;print("LANDING_BASIS_END");',
        'print("Q8_W0_RANKDROP_B1_C_INFINITY_V3_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), required=True)
    parser.add_argument("--order", choices=("dp", "block"), required=True)
    args = parser.parse_args()
    print(source(args.engine, args.order))
