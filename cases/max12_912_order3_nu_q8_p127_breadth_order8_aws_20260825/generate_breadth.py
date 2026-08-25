#!/usr/bin/env python3
"""Generate one exact moving-v order-8 lift at a selected good F_127 fibre."""

from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from hashlib import sha256
import importlib.util
import io
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PARENT = ROOT / "cases/max12_912_order3_nu_q8_p127_hensel_coordinate_lift_aws_20260825/generate.py"
PARENT_SHA256 = "4d075593a3e4e6566cb68a0fc6accc1cd6cb38e7539ed1829c2558b7e6d4bd2d"
SAMPLES_SHA256 = "0790e9f8bb6b545e742ca9e723c29b9a8dc0268a93dedd91c2f2a7b48f48f231"
GOOD_W = tuple(w for w in range(1, 127) if w not in (39, 56, 125))
ORDER = 8


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_parent():
    got = digest(PARENT)
    if got != PARENT_SHA256:
        raise RuntimeError(("parent hash", got, PARENT_SHA256))
    spec = importlib.util.spec_from_file_location("q8_breadth_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError(PARENT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def audited_sample(payload: dict, base_w: int) -> None:
    if payload.get("status") != "PASS" or payload.get("prime") != 127:
        raise RuntimeError("shape endpoint")
    if payload.get("w_values") != list(GOOD_W):
        raise RuntimeError("good-fibre list")
    if not payload.get("all_original_remainders_zero"):
        raise RuntimeError("source replay flag")
    if not payload.get("all_candidate_specializations_match"):
        raise RuntimeError("candidate-match flag")
    custody = {entry.get("w"): entry for entry in payload.get("custody", [])}
    entry = custody.get(base_w)
    if not entry or not all(entry.get(key) for key in (
        "input_sha256", "stdout_sha256", "stderr_sha256", "meta_sha256"
    )):
        raise RuntimeError(("missing fixed-fibre custody", base_w))


def fixed_prefix(parent, samples: Path, base_w: int) -> str:
    parent.W0 = base_w
    saved = sys.argv
    stream = io.StringIO()
    try:
        sys.argv = [str(PARENT), "--samples", str(samples), "--order", str(ORDER)]
        with redirect_stdout(stream):
            parent.main()
    finally:
        sys.argv = saved
    source = stream.getvalue()
    marker = "ring T=127,(s,a),dp;"
    if source.count(marker) != 1:
        raise RuntimeError("fixed-prefix marker")
    prefix, _ = source.split(marker, 1)
    literal = "map phi0=R,25,"
    if prefix.count(literal) != 1:
        raise RuntimeError("parent literal base-map marker")
    prefix = prefix.replace(literal, f"map phi0=R,{base_w},", 1)
    expected = f"map phi0=R,{base_w},c0,d20,d40,x10,x30,x50,a;"
    if expected not in prefix or "int base_fail=0;" not in prefix:
        raise RuntimeError("base fibre did not propagate")
    return prefix


def moving_suffix(base_w: int) -> str:
    lines = [
        "ring T=127,(v,s),lp;",
        f"map candidateMap=R,{base_w}+s,0,0,0,0,0,0,v;",
        "poly Hmoving=candidateMap(H);",
        f"ideal QT=Hmoving,s^{ORDER};",
        "ideal GQT=std(QT);",
        'print("Q8-P127-BREADTH-MOVING-BASIS");',
        f'print("base_w={base_w}");',
        'print("moving_leading_ideal_begin");',
        "lead(GQT);",
        'print("moving_leading_ideal_end");',
        "qring A=GQT;",
        "ideal ZA=std(ideal(0));",
        'print("moving_dimension="+string(dim(ZA)));',
        'print("moving_vdim="+string(vdim(ZA)));',
        "map baseMap=B,v;",
        "ideal y=baseMap(Y0);",
        "matrix K=baseMap(K0);",
        "poly INV=baseMap(inv0);",
        "poly INVBASE=baseMap(inv0);",
        "matrix FC[6][1]; matrix DELTA[6][1];",
        "int coefficient_order;",
        f"for (coefficient_order=1;coefficient_order<{ORDER};coefficient_order++)",
        "{",
        f"  map evalStep=R,{base_w}+s,y[1],y[2],y[3],y[4],y[5],y[6],v;",
        "  ideal Fres=evalStep(F);",
        "  for (ii=1;ii<=6;ii++)",
        "  {",
        "    Fres[ii]=reduce(Fres[ii],ZA);",
        "    matrix coeffMatrix=coeffs(Fres[ii],s);",
        "    FC[ii,1]=0;",
        "    if(nrows(coeffMatrix)>coefficient_order){FC[ii,1]=coeffMatrix[coefficient_order+1,1];}",
        "    kill coeffMatrix;",
        "  }",
        "  DELTA=K*FC;",
        "  for (ii=1;ii<=6;ii++)",
        "  {",
        "    DELTA[ii,1]=reduce(DELTA[ii,1],ZA);",
        "    matrix deltaCoeffs=coeffs(DELTA[ii,1],s);",
        "    poly delta0=deltaCoeffs[1,1];",
        "    y[ii]=reduce(y[ii]-s^coefficient_order*delta0,ZA);",
        "    kill deltaCoeffs; kill delta0;",
        "  }",
        "  kill evalStep;",
        "  poly locres=reduce(INV*y[6]*(y[5]-2*y[6])-1,ZA);",
        "  matrix locCoeffs=coeffs(locres,s);",
        "  poly locn=0;",
        "  if(nrows(locCoeffs)>coefficient_order){locn=locCoeffs[coefficient_order+1,1];}",
        "  poly locdelta=reduce(INVBASE*locn,ZA);",
        "  matrix locDeltaCoeffs=coeffs(locdelta,s);",
        "  INV=reduce(INV-s^coefficient_order*locDeltaCoeffs[1,1],ZA);",
        "  kill locres; kill locCoeffs; kill locn; kill locdelta; kill locDeltaCoeffs;",
        '  print("coefficient_order="+string(coefficient_order));',
        "}",
        f"map evalFinal=R,{base_w}+s,y[1],y[2],y[3],y[4],y[5],y[6],v;",
        "ideal Ffinal=evalFinal(F);",
        "poly Hfinal=reduce(evalFinal(H),ZA);",
        "poly evfinal=reduce(v*y[6]-y[5]+2*y[6],ZA);",
        "poly locfinal=reduce(INV*y[6]*(y[5]-2*y[6])-1,ZA);",
        "int final_fail=0;",
        "for (ii=1;ii<=6;ii++){Ffinal[ii]=reduce(Ffinal[ii],ZA);if(Ffinal[ii]!=0){final_fail=final_fail+1;}}",
        "if(Hfinal!=0){final_fail=final_fail+1;}",
        "if(evfinal!=0){final_fail=final_fail+1;}",
        "if(locfinal!=0){final_fail=final_fail+1;}",
        'print("Q8-P127-BREADTH-ORDER8");',
        f'print("order={ORDER}");',
        'print("final_fail="+string(final_fail));',
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--base-w", type=int, required=True)
    args = parser.parse_args()
    if args.base_w not in GOOD_W:
        raise RuntimeError(("not a good fibre", args.base_w))
    if digest(args.samples) != SAMPLES_SHA256:
        raise RuntimeError("shape sample hash")
    payload = json.loads(args.samples.read_text())
    audited_sample(payload, args.base_w)
    parent = load_parent()
    print(fixed_prefix(parent, args.samples, args.base_w), end="")
    print(moving_suffix(args.base_w), end="")


if __name__ == "__main__":
    main()
