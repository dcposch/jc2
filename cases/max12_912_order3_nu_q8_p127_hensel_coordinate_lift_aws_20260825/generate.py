#!/usr/bin/env python3
"""Generate an exact Singular Newton--Hensel lift in the w=25 shape algebra."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
CANDIDATE = ROOT / "cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json"
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
SAMPLES_SHA256 = "0790e9f8bb6b545e742ca9e723c29b9a8dc0268a93dedd91c2f2a7b48f48f231"
P = 127
W0 = 25
COORDINATES = ("c", "d2", "d4", "x1", "x3", "x5", "inv")


def load_compiler():
    got = sha256(COMPILER.read_bytes()).hexdigest()
    if got != COMPILER_SHA256:
        raise RuntimeError((str(COMPILER), got, COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("q8_hensel_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def term_string(coefficient: int, factors: list[str]) -> str:
    coefficient %= P
    if coefficient == 0:
        return ""
    pieces = []
    if coefficient != 1 or not factors:
        pieces.append(str(coefficient))
    pieces.extend(factors)
    return "*".join(pieces)


def polynomial_from_coefficients(coefficients: list[int], variable: str) -> str:
    terms = []
    for exponent, coefficient in enumerate(coefficients):
        factors = []
        if exponent:
            factors.append(variable if exponent == 1 else f"{variable}^{exponent}")
        term = term_string(coefficient, factors)
        if term:
            terms.append(term)
    return "+".join(terms) if terms else "0"


def candidate_string(payload: dict) -> str:
    support = payload["nonzero_support"]
    if sorted(map(int, support)) != list(range(191)):
        raise RuntimeError("candidate v support")
    terms = []
    for raw_v_degree, entries in support.items():
        v_degree = int(raw_v_degree)
        for w_degree, coefficient in entries:
            factors = []
            if w_degree:
                factors.append("w" if w_degree == 1 else f"w^{w_degree}")
            if v_degree:
                factors.append("v" if v_degree == 1 else f"v^{v_degree}")
            term = term_string(coefficient, factors)
            if term:
                terms.append(term)
    return "+".join(terms)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--order", type=int, choices=(8, 16, 32, 64, 128), required=True)
    args = parser.parse_args()
    if args.order & (args.order - 1):
        raise RuntimeError("order must be a power of two")

    if sha256(args.samples.read_bytes()).hexdigest() != SAMPLES_SHA256:
        raise RuntimeError("shape sample hash")
    samples = json.loads(args.samples.read_text())
    if samples["status"] != "PASS" or samples["prime"] != P:
        raise RuntimeError("shape sample endpoint")
    if samples["coordinate_names"] != list(COORDINATES):
        raise RuntimeError("shape coordinate order")
    if W0 not in samples["w_values"]:
        raise RuntimeError("missing w=25")
    w_index = samples["w_values"].index(W0)
    base_coordinates = {}
    for name in COORDINATES:
        table = samples["samples"][name]
        if len(table) != 190 or any(len(row) != 123 for row in table):
            raise RuntimeError((name, "shape dimensions"))
        base_coordinates[name] = [row[w_index] % P for row in table]

    if sha256(CANDIDATE.read_bytes()).hexdigest() != CANDIDATE_SHA256:
        raise RuntimeError("candidate hash")
    candidate = json.loads(CANDIDATE.read_text())
    if (
        candidate["status"] != "PASS"
        or candidate["prime"] != P
        or candidate["degree_v"] != 190
        or candidate["nonzero_support"]["190"] != [[0, 1]]
    ):
        raise RuntimeError("candidate endpoint")

    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if list(names) != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError("compiler variable order")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError("compiler row order")

    row_strings = [Q.M.coeff_string(rows[ell], names) for ell in imposed]
    h_string = candidate_string(candidate)
    iterations = args.order.bit_length() - 1

    lines = [
        'LIB "linalg.lib";',
        "ring R=127,(w,c,d2,d4,x1,x3,x5,v),dp;",
    ]
    for ell, expression in zip(imposed, row_strings, strict=True):
        lines.append(f"poly e{ell}={expression};")
    lines.extend(
        [
            "ideal F=e1,e3,e5,e7,e2,e4;",
            "matrix Jfull=jacob(F);",
            "matrix J[6][6];",
            "int ii; int jj;",
            "for (ii=1;ii<=6;ii++){for (jj=1;jj<=6;jj++){J[ii,jj]=Jfull[ii,jj+1];}}",
            f"poly H={h_string};",
            "poly Hv=diff(H,v);",
            "ring B=127,(a),dp;",
        ]
    )
    for name in COORDINATES:
        lines.append(
            f"poly {name}0={polynomial_from_coefficients(base_coordinates[name], 'a')};"
        )
    lines.extend(
        [
            "ideal Y0=c0,d20,d40,x10,x30,x50;",
            "map phi0=R,25,c0,d20,d40,x10,x30,x50,a;",
            "ideal F0=phi0(F);",
            "matrix J0=phi0(J);",
            "poly H0=phi0(H);",
            "poly Hv0=phi0(Hv);",
            "ideal GBH=std(H0);",
            "int base_fail=0;",
            "for (ii=1;ii<=6;ii++){if(reduce(F0[ii],GBH)!=0){base_fail=base_fail+1;}}",
            "poly ev0=a*x50-x30+2*x50;",
            "if(reduce(ev0,GBH)!=0){base_fail=base_fail+1;}",
            "poly loc0=inv0*x50*(x30-2*x50)-1;",
            "if(reduce(loc0,GBH)!=0){base_fail=base_fail+1;}",
            "poly detJ0=det(J0);",
            "poly gcdJ=gcd(detJ0,H0);",
            "poly gcdHv=gcd(Hv0,H0);",
            "if(deg(gcdJ)!=0){base_fail=base_fail+1;}",
            "if(deg(gcdHv)!=0){base_fail=base_fail+1;}",
            "matrix bezJ=lift(ideal(detJ0,H0),ideal(1));",
            "poly invdetJ0=bezJ[1,1];",
            "if(reduce(detJ0*invdetJ0-1,GBH)!=0){base_fail=base_fail+1;}",
            "matrix K0=adjoint(J0)*invdetJ0;",
            "matrix checkK0=J0*K0-unitmat(6);",
            "for (ii=1;ii<=6;ii++){for (jj=1;jj<=6;jj++){if(reduce(checkK0[ii,jj],GBH)!=0){base_fail=base_fail+1;}}}",
            "matrix bezHv=lift(ideal(Hv0,H0),ideal(1));",
            "poly U0=bezHv[1,1];",
            "if(reduce(Hv0*U0-1,GBH)!=0){base_fail=base_fail+1;}",
            'print("Q8-P127-HENSEL-BASE");',
            'print("base_fail="+string(base_fail));',
            'print("H0_degree="+string(deg(H0)));',
            'print("gcd_detJ_H0_degree="+string(deg(gcdJ)));',
            'print("gcd_Hv_H0_degree="+string(deg(gcdHv)));',
            f"ring T=127,(s,a),dp;",
            "poly H0T=imap(B,H0);",
            f"ideal QT=s^{args.order},H0T;",
            "qring A=std(QT);",
            "ideal ZA=std(ideal(0));",
            "ideal y=imap(B,Y0);",
            "matrix K=imap(B,K0);",
            "poly V=a;",
            "poly U=imap(B,U0);",
            "poly INV=imap(B,inv0);",
            "matrix FC[6][1]; matrix DELTA[6][1];",
            "matrix I6=unitmat(6);",
            "matrix JR[6][6]; matrix JK[6][6]; matrix CORR[6][6];",
            f"int iterations={iterations}; int iteration;",
            "for (iteration=1;iteration<=iterations;iteration++)",
            "{",
            "  map evalVold=R,25+s,y[1],y[2],y[3],y[4],y[5],y[6],V;",
            "  poly Hres=reduce(evalVold(H),ZA);",
            "  V=reduce(V-U*Hres,ZA);",
            "  kill evalVold;",
            "  map evalVnew=R,25+s,y[1],y[2],y[3],y[4],y[5],y[6],V;",
            "  poly Hvnew=reduce(evalVnew(Hv),ZA);",
            "  U=reduce(U*(2-Hvnew*U),ZA);",
            "  kill evalVnew;",
            "  map evalYold=R,25+s,y[1],y[2],y[3],y[4],y[5],y[6],V;",
            "  ideal Fres=evalYold(F);",
            "  for (ii=1;ii<=6;ii++){FC[ii,1]=reduce(Fres[ii],ZA);}",
            "  DELTA=K*FC;",
            "  for (ii=1;ii<=6;ii++){y[ii]=reduce(y[ii]-DELTA[ii,1],ZA);}",
            "  kill evalYold;",
            "  map evalYnew=R,25+s,y[1],y[2],y[3],y[4],y[5],y[6],V;",
            "  JR=evalYnew(J);",
            "  JK=JR*K;",
            "  CORR=2*I6-JK;",
            "  K=K*CORR;",
            "  for (ii=1;ii<=6;ii++){for (jj=1;jj<=6;jj++){K[ii,jj]=reduce(K[ii,jj],ZA);}}",
            "  kill evalYnew;",
            "  poly locden=reduce(y[6]*(y[5]-2*y[6]),ZA);",
            "  INV=reduce(INV*(2-locden*INV),ZA);",
            '  print("iteration="+string(iteration));',
            "}",
            "map evalFinal=R,25+s,y[1],y[2],y[3],y[4],y[5],y[6],V;",
            "ideal Ffinal=evalFinal(F);",
            "poly Hfinal=reduce(evalFinal(H),ZA);",
            "poly evfinal=reduce(V*y[6]-y[5]+2*y[6],ZA);",
            "poly locfinal=reduce(INV*y[6]*(y[5]-2*y[6])-1,ZA);",
            "int final_fail=0;",
            "for (ii=1;ii<=6;ii++){Ffinal[ii]=reduce(Ffinal[ii],ZA);if(Ffinal[ii]!=0){final_fail=final_fail+1;}}",
            "if(Hfinal!=0){final_fail=final_fail+1;}",
            "if(evfinal!=0){final_fail=final_fail+1;}",
            "if(locfinal!=0){final_fail=final_fail+1;}",
            'print("Q8-P127-HENSEL-COORDINATE-LIFT");',
            f'print("order={args.order}");',
            'print("final_fail="+string(final_fail));',
            'print("series_V="+string(V));',
            'print("series_c="+string(y[1]));',
            'print("series_d2="+string(y[2]));',
            'print("series_d4="+string(y[3]));',
            'print("series_x1="+string(y[4]));',
            'print("series_x3="+string(y[5]));',
            'print("series_x5="+string(y[6]));',
            'print("series_inv="+string(INV));',
        ]
    )
    print("\n".join(lines))


if __name__ == "__main__":
    main()

