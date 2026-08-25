#!/usr/bin/env python3
"""Generate coefficient-wise Hensel lifting in the moving v-basis."""

from __future__ import annotations

import argparse
from hashlib import sha256
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "generate.py"
BASE_SHA256 = "4d075593a3e4e6566cb68a0fc6accc1cd6cb38e7539ed1829c2558b7e6d4bd2d"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--order", type=int, choices=(8, 16, 32, 64, 128), required=True)
    args = parser.parse_args()
    got = sha256(BASE.read_bytes()).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError((str(BASE), got, BASE_SHA256))
    completed = subprocess.run(
        [sys.executable, str(BASE), "--samples", str(args.samples), "--order", str(args.order)],
        check=True,
        capture_output=True,
        text=True,
    )
    if completed.stderr:
        raise RuntimeError(("base generator stderr", completed.stderr))
    source = completed.stdout
    marker = "ring T=127,(s,a),dp;"
    if source.count(marker) != 1:
        raise RuntimeError("moving-basis prefix marker")
    prefix = source.split(marker, 1)[0]
    moving = [
        "ring T=127,(v,s),lp;",
        "map candidateMap=R,25+s,0,0,0,0,0,0,v;",
        "poly Hmoving=candidateMap(H);",
        f"ideal QT=Hmoving,s^{args.order};",
        "ideal GQT=std(QT);",
        'print("Q8-P127-MOVING-BASIS");',
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
        f"for (coefficient_order=1;coefficient_order<{args.order};coefficient_order++)",
        "{",
        "  map evalStep=R,25+s,y[1],y[2],y[3],y[4],y[5],y[6],v;",
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
        "map evalFinal=R,25+s,y[1],y[2],y[3],y[4],y[5],y[6],v;",
        "ideal Ffinal=evalFinal(F);",
        "poly Hfinal=reduce(evalFinal(H),ZA);",
        "poly evfinal=reduce(v*y[6]-y[5]+2*y[6],ZA);",
        "poly locfinal=reduce(INV*y[6]*(y[5]-2*y[6])-1,ZA);",
        "int final_fail=0;",
        "for (ii=1;ii<=6;ii++){Ffinal[ii]=reduce(Ffinal[ii],ZA);if(Ffinal[ii]!=0){final_fail=final_fail+1;}}",
        "if(Hfinal!=0){final_fail=final_fail+1;}",
        "if(evfinal!=0){final_fail=final_fail+1;}",
        "if(locfinal!=0){final_fail=final_fail+1;}",
        'print("Q8-P127-HENSEL-MOVING-COORDINATE-LIFT");',
        f'print("order={args.order}");',
        'print("final_fail="+string(final_fail));',
        'print("series_c="+string(y[1]));',
        'print("series_d2="+string(y[2]));',
        'print("series_d4="+string(y[3]));',
        'print("series_x1="+string(y[4]));',
        'print("series_x3="+string(y[5]));',
        'print("series_x5="+string(y[6]));',
        'print("series_inv="+string(INV));',
    ]
    print(prefix + "\n".join(moving) + "\n", end="")


if __name__ == "__main__":
    main()

