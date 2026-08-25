#!/usr/bin/env python3
"""Generate exact AWS Singular inputs for the w=0 escape boundary."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
PARENT_MANIFEST = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/MANIFEST.sha256"
PARENT_MANIFEST_SHA256 = "3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4"

FINITE_MODES = (
    "x5_open",
    "A_open",
    "overlap",
    "overlap_nu0",
    "overlap_loaded",
)
PROJECTIVE_CHARTS = ("c", "d2", "d4", "x1", "x3", "x5")


def load_compiler():
    for path, expected in ((COMPILER, COMPILER_SHA256),
                           (PARENT_MANIFEST, PARENT_MANIFEST_SHA256)):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_w0_escape_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def specialize_w0(value):
    out = {}
    for monomial, coefficient in value.items():
        if monomial[0] != 0:
            continue
        key = monomial[1:]
        out[key] = out.get(key, Fraction(0)) + coefficient
    return {m: c for m, c in out.items() if c}


def finite_source(mode: str, engine: str, order: str, print_basis: bool) -> str:
    if mode not in FINITE_MODES:
        raise RuntimeError(mode)
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    names0 = names[1:]
    extras = []
    if mode in ("x5_open", "A_open"):
        extras.append("ib")
    if mode == "overlap_loaded":
        extras.append("inu")
    variables = names0 + extras
    ordering = "dp" if order == "dp" else f"(dp({len(variables)}))"
    lines = [f"ring R=0,({','.join(variables)}),{ordering};", "option(redSB);"]
    row_names = []
    for ell in imposed:
        name = f"e{ell}"
        row_names.append(name)
        lines.append(f"poly {name}={Q.M.coeff_string(specialize_w0(rows[ell]), names0)};")
    lines.append(f"poly e6={Q.M.coeff_string(specialize_w0(rows[6]), names0)};")
    lines.append(f"poly e8={Q.M.coeff_string(specialize_w0(rows[8]), names0)};")
    lines.append("poly A=x3-2*x5;")
    generators = row_names[:]
    if mode == "x5_open":
        generators += ["x5", "ib*x3-1"]
    elif mode == "A_open":
        generators += ["A", "ib*x5-1"]
    else:
        generators += ["x5", "x3"]
        if mode == "overlap_nu0":
            generators.append("e6")
        elif mode == "overlap_loaded":
            generators.append("inu*e6-1")
    lines.extend([
        f"ideal I={','.join(generators)};",
        f"ideal G={engine}(I);",
        "int remzero=1;",
        "for(int i=1;i<=size(I);i++){if(reduce(I[i],G)!=0){remzero=0;}}",
        'print("Q8-W0-ESCAPE-FINITE");',
        f'print("mode={mode}");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("original_remainder_zero="+string(remzero));',
        'print("dim="+string(dim(G)));',
        'print("size="+string(size(G)));',
        'print("vdim="+string(vdim(G)));',
        "int unitideal=0;if(reduce(1,G)==0){unitideal=1;}",
        'print("unit_ideal="+string(unitideal));',
    ])
    if mode == "x5_open":
        lines.extend([
            "ideal E=x5,x1-x3,d2,d4,c*x3-1,ib*x3-1;",
            "ideal GE=std(E);",
            "int ItoE=1;for(int i=1;i<=size(I);i++){if(reduce(I[i],GE)!=0){ItoE=0;}}",
            "int EtoI=1;for(int i=1;i<=size(E);i++){if(reduce(E[i],G)!=0){EtoI=0;}}",
            'print("expected_I_to_E="+string(ItoE));',
            'print("expected_E_to_I="+string(EtoI));',
            "int e6identity=0;if(reduce(81*e6+4*x3^3,G)==0){e6identity=1;}",
            "int e8zero=0;if(reduce(e8,G)==0){e8zero=1;}",
            'print("e6_identity_81e6_plus_4x3cubed="+string(e6identity));',
            'print("e8_zero="+string(e8zero));',
        ])
    if mode == "A_open":
        lines.extend([
            "int e2identity=0;if(reduce(81*e2+4*x5^3,std(ideal(A)))==0){e2identity=1;}",
            'print("A_boundary_e2_identity="+string(e2identity));',
        ])
    if print_basis:
        lines.extend(['print("BASIS_BEGIN");', "G;", 'print("BASIS_END");'])
    lines.extend(['print("Q8_W0_ESCAPE_FINITE_PASS");', "exit;"])
    return "\n".join(lines)


def substitution(expr: str) -> str:
    for variable, value in (
        ("w", "0"), ("c", "1/a"), ("d2", "0"), ("d4", "0"),
        ("x1", "a"), ("x3", "a"), ("x5", "0"),
    ):
        expr = f"subst({expr},{variable},{value})"
    return expr


def tangent_source() -> str:
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    yvars = names[1:]
    lines = [
        f"ring R=(0,a),({','.join(names)}),dp;",
        "option(redSB);",
    ]
    for ell in imposed:
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    ordered = [f"e{ell}" for ell in imposed]
    lines.extend(["matrix J[6][6];", "matrix Aug[6][7];"])
    for i, row in enumerate(ordered, start=1):
        for j, variable in enumerate(yvars, start=1):
            value = substitution(f"diff({row},{variable})")
            lines.append(f"J[{i},{j}]={value};Aug[{i},{j}]={value};")
        lines.append(f"Aug[{i},7]={substitution(f'diff({row},w)')};")
    lines.extend([
        'print("Q8-W0-X5-GENERIC-TANGENT");',
        'print("rank_J="+string(rank(J)));',
        'print("rank_Aug="+string(rank(Aug)));',
    ])
    for drop_row in range(1, 7):
        for drop_col in range(1, 7):
            lines.append("matrix N[5][5];")
            rr = [i for i in range(1, 7) if i != drop_row]
            cc = [j for j in range(1, 7) if j != drop_col]
            for ii, i in enumerate(rr, start=1):
                for jj, j in enumerate(cc, start=1):
                    lines.append(f"N[{ii},{jj}]=J[{i},{j}];")
            lines.append(f'print("minor5_drop_{drop_row}_{drop_col}="+string(det(N)));')
    for drop_col in range(1, 8):
        lines.append("matrix D[6][6];")
        cc = [j for j in range(1, 8) if j != drop_col]
        for i in range(1, 7):
            for jj, j in enumerate(cc, start=1):
                lines.append(f"D[{i},{jj}]=Aug[{i},{j}];")
        lines.append(f'print("minor6_aug_drop_{drop_col}="+string(det(D)));')
    lines.extend(['print("Q8_W0_X5_GENERIC_TANGENT_PASS");', "exit;"])
    return "\n".join(lines)


def homogenize_internal(value):
    maximum = max((sum(m[1:]) for m in value), default=0)
    out = {}
    for monomial, coefficient in value.items():
        key = monomial + (maximum - sum(monomial[1:]),)
        out[key] = out.get(key, Fraction(0)) + coefficient
    return {m: c for m, c in out.items() if c}


def projective_source(chart: str, engine: str) -> str:
    if chart not in PROJECTIVE_CHARTS:
        raise RuntimeError(chart)
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    hnames = names + ["T"]
    lines = [
        'LIB "elim.lib";',
        f"ring R=0,({','.join(hnames)}),dp;",
        "option(redSB);",
    ]
    row_names = []
    for ell in imposed:
        name = f"h{ell}"
        row_names.append(name)
        lines.append(f"poly {name}={Q.M.coeff_string(homogenize_internal(rows[ell]), hnames)};")
    lines.extend([
        f"ideal Jraw={','.join(row_names)};",
        "list Sat=sat(Jraw,ideal(T));",
        "ideal C=Sat[1];",
        f"ideal B=C,w,T,{chart}-1;",
        f"ideal G={engine}(B);",
        "int remzero=1;for(int i=1;i<=size(B);i++){if(reduce(B[i],G)!=0){remzero=0;}}",
        'print("Q8-W0-ESCAPE-PROJECTIVE");',
        f'print("chart={chart}");',
        f'print("engine={engine}");',
        'print("raw_size="+string(size(Jraw)));',
        'print("saturated_size="+string(size(C)));',
        'print("original_remainder_zero="+string(remzero));',
        'print("dim="+string(dim(G)));',
        'print("size="+string(size(G)));',
        'print("vdim="+string(vdim(G)));',
        "int unitideal=0;if(reduce(1,G)==0){unitideal=1;}",
        'print("unit_ideal="+string(unitideal));',
        'print("BASIS_BEGIN");',
        "G;",
        'print("BASIS_END");',
        'print("Q8_W0_ESCAPE_PROJECTIVE_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=("finite", "tangent", "projective"), required=True)
    parser.add_argument("--mode", choices=FINITE_MODES)
    parser.add_argument("--chart", choices=PROJECTIVE_CHARTS)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    parser.add_argument("--print-basis", action="store_true")
    args = parser.parse_args()
    if args.kind == "finite":
        if args.mode is None:
            raise RuntimeError("--mode required")
        print(finite_source(args.mode, args.engine, args.order, args.print_basis))
    elif args.kind == "tangent":
        print(tangent_source())
    else:
        if args.chart is None:
            raise RuntimeError("--chart required")
        print(projective_source(args.chart, args.engine))


if __name__ == "__main__":
    main()
