#!/usr/bin/env python3
"""Generate factorwise formal source lifts at the corrected Q8 contacts."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
CONTACT = ROOT / "cases/max12_912_order3_nu_q8_p127_full_contact_jacobian_aws_20260825/aws_box02_v1/result.json"
CONTACT_SHA256 = "804f9fbb095832e79a4f01ad870ed87a55921b78f34ff9f83ae946da04b70549"
CANDIDATE = ROOT / "cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json"
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
P = 127
FACTORS = {
    "linear67": [60, 1],
    "linear58": [69, 1],
    "linear26": [101, 1],
    "quintic": [79, 118, 26, 38, 53, 1],
}
COORDINATES = ("c", "d2", "d4", "x1", "x3", "x5", "inv", "v")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_compiler():
    if digest(COMPILER) != COMPILER_SHA256:
        raise RuntimeError("compiler hash")
    spec = importlib.util.spec_from_file_location("q8_contact_hensel_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def polynomial(coefficients: list[int], variable: str) -> str:
    terms = []
    for exponent, coefficient in enumerate(coefficients):
        coefficient %= P
        if not coefficient:
            continue
        factors = []
        if coefficient != 1 or exponent == 0:
            factors.append(str(coefficient))
        if exponent:
            factors.append(variable if exponent == 1 else f"{variable}^{exponent}")
        terms.append("*".join(factors))
    return "+".join(terms) if terms else "0"


def candidate_string(payload: dict) -> str:
    if sorted(map(int, payload["nonzero_support"])) != list(range(191)):
        raise RuntimeError("candidate support")
    terms = []
    for raw_v_degree, entries in payload["nonzero_support"].items():
        v_degree = int(raw_v_degree)
        for w_degree, coefficient in entries:
            coefficient %= P
            if not coefficient:
                continue
            factors = []
            if coefficient != 1 or (w_degree == 0 and v_degree == 0):
                factors.append(str(coefficient))
            if w_degree:
                factors.append("w" if w_degree == 1 else f"w^{w_degree}")
            if v_degree:
                factors.append("v" if v_degree == 1 else f"v^{v_degree}")
            terms.append("*".join(factors))
    return "+".join(terms)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--factor", choices=tuple(FACTORS), required=True)
    parser.add_argument("--order", type=int, choices=(64, 256, 1024, 2048, 4096, 8192), required=True)
    args = parser.parse_args()
    if args.order & (args.order - 1):
        raise RuntimeError("order must be a power of two")
    if digest(CONTACT) != CONTACT_SHA256 or digest(CANDIDATE) != CANDIDATE_SHA256:
        raise RuntimeError("data hash")
    contact = json.loads(CONTACT.read_text())
    candidate = json.loads(CANDIDATE.read_text())
    if contact["status"] != "PASS" or candidate["status"] != "PASS":
        raise RuntimeError("data endpoint")
    product = [1]
    for factor in FACTORS.values():
        product = multiply(product, factor)
    if product != contact["q8_monic_low_to_high"]:
        raise RuntimeError(("factor product", product, contact["q8_monic_low_to_high"]))

    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    if names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError(names)
    row_strings = [Q.M.coeff_string(rows[ell], names) for ell in imposed]
    base = contact["contact_coordinates_low_to_high"]
    factor = FACTORS[args.factor]
    factor_degree = len(factor) - 1
    iterations = args.order.bit_length() - 1
    lines = [
        'LIB "linalg.lib";',
        "ring R=127,(w,c,d2,d4,x1,x3,x5,inv,v),dp;",
    ]
    for ell, expression in zip(imposed, row_strings, strict=True):
        lines.append(f"poly e{ell}={expression};")
    lines.extend([
        "poly ev=v*x5-x3+2*x5;",
        "poly eloc=inv*x5*(x3-2*x5)-1;",
        "ideal F=e1,e3,e5,e7,e2,e4,ev,eloc;",
        "matrix Jfull=jacob(F);",
        "matrix J[8][8]; int ii; int jj;",
        "for(ii=1;ii<=8;ii++){for(jj=1;jj<=8;jj++){J[ii,jj]=Jfull[ii,jj+1];}}",
        f"poly H={candidate_string(candidate)};",
        "ring B=127,(a),dp;",
        f"poly q={polynomial(factor, 'a')};",
    ])
    for name in COORDINATES:
        lines.append(f"poly {name}0={polynomial(base[name], 'a')};")
    lines.extend([
        "ideal Y0=c0,d20,d40,x10,x30,x50,inv0,v0;",
        "map phi0=R,0,c0,d20,d40,x10,x30,x50,inv0,v0;",
        "ideal F0=phi0(F); matrix J0=phi0(J); poly H0=phi0(H);",
        "ideal GBQ=std(q); int base_fail=0;",
        "for(ii=1;ii<=8;ii++){if(reduce(F0[ii],GBQ)!=0){base_fail=base_fail+1;}}",
        "if(reduce(H0,GBQ)!=0){base_fail=base_fail+1;}",
        "poly detJ0=det(J0); poly gcdJ=gcd(detJ0,q);",
        "if(deg(gcdJ)!=0){base_fail=base_fail+1;}",
        "matrix bezJ=lift(ideal(detJ0,q),ideal(1)); poly invdetJ0=bezJ[1,1];",
        "if(reduce(detJ0*invdetJ0-1,GBQ)!=0){base_fail=base_fail+1;}",
        "matrix K0=adjoint(J0)*invdetJ0;",
        "for(ii=1;ii<=8;ii++){for(jj=1;jj<=8;jj++){K0[ii,jj]=reduce(K0[ii,jj],GBQ);}}",
        "matrix checkK=J0*K0-unitmat(8);",
        "for(ii=1;ii<=8;ii++){for(jj=1;jj<=8;jj++){if(reduce(checkK[ii,jj],GBQ)!=0){base_fail=base_fail+1;}}}",
        'print("Q8-CONTACT-HENSEL-BASE");',
        f'print("factor={args.factor}");',
        f'print("factor_degree={factor_degree}");',
        'print("base_fail="+string(base_fail));',
        'print("gcd_detJ_factor_degree="+string(deg(gcdJ)));',
        "ring T=127,(s,a),dp;",
        "poly qT=imap(B,q);",
        f"ideal QT=s^{args.order},qT; ideal GQT=std(QT); qring A=GQT;",
        "ideal ZA=std(ideal(0));",
        "ideal y=imap(B,Y0);",
        "matrix K=imap(B,K0); matrix FC[8][1]; matrix DELTA[8][1];",
        "matrix I8=unitmat(8); matrix JR[8][8]; matrix JK[8][8]; matrix CORR[8][8];",
        f"int iterations={iterations}; int iteration;",
        "for(iteration=1;iteration<=iterations;iteration++)",
        "{",
        "  map evalOld=R,s,y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8];",
        "  ideal Fres=evalOld(F);",
        "  for(ii=1;ii<=8;ii++){FC[ii,1]=reduce(Fres[ii],ZA);}",
        "  DELTA=K*FC;",
        "  for(ii=1;ii<=8;ii++){y[ii]=reduce(y[ii]-DELTA[ii,1],ZA);}",
        "  kill evalOld;",
        "  map evalNew=R,s,y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8];",
        "  JR=evalNew(J); JK=JR*K; CORR=2*I8-JK; K=K*CORR;",
        "  for(ii=1;ii<=8;ii++){for(jj=1;jj<=8;jj++){K[ii,jj]=reduce(K[ii,jj],ZA);}}",
        "  kill evalNew;",
        '  print("iteration="+string(iteration));',
        "}",
        "map evalFinal=R,s,y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8];",
        "ideal Ffinal=evalFinal(F); int final_fail=0;",
        "for(ii=1;ii<=8;ii++){Ffinal[ii]=reduce(Ffinal[ii],ZA);if(Ffinal[ii]!=0){final_fail=final_fail+1;}}",
        "poly Hres=reduce(evalFinal(H),ZA); int h_contact_order=-1; poly hlead=0;",
        "if(Hres!=0)",
        "{",
        "  matrix HC=coeffs(Hres,s); int hh;",
        "  for(hh=1;hh<=nrows(HC);hh++){if((h_contact_order<0)&&(HC[hh,1]!=0)){h_contact_order=hh-1;hlead=HC[hh,1];}}",
        "}",
        'print("Q8-CONTACT-HENSEL-FINAL");',
        f'print("order={args.order}");',
        f'print("moving_vdim={args.order * factor_degree}");',
        'print("final_fail="+string(final_fail));',
        'print("h_contact_order="+string(h_contact_order));',
        'print("h_lead_coefficient="+string(hlead));',
        'if(h_contact_order<0){print("h_contact_at_least="+string(' + str(args.order) + '));}',
    ])
    print("\n".join(lines))


if __name__ == "__main__":
    main()
