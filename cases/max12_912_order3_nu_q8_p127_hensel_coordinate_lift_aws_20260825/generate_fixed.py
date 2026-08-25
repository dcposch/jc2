#!/usr/bin/env python3
"""Generate the lower-memory fixed-Jacobian Hensel variant.

The base generator uses Newton inversion of the full six-by-six Jacobian and
doubles precision.  This wrapper keeps the certified inverse at s=0 fixed;
each correction gains at least one s-adic digit.  It therefore uses N-1
iterations but avoids dense matrix-by-matrix products in the truncated
degree-190 algebra.
"""

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
        [
            sys.executable,
            str(BASE),
            "--samples",
            str(args.samples),
            "--order",
            str(args.order),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    if completed.stderr:
        raise RuntimeError(("base generator stderr", completed.stderr))
    source = completed.stdout
    start_marker = "for (iteration=1;iteration<=iterations;iteration++)\n{\n"
    end_marker = "}\nmap evalFinal=R,25+s,y[1],y[2],y[3],y[4],y[5],y[6],V;"
    if source.count(start_marker) != 1 or source.count(end_marker) != 1:
        raise RuntimeError("Newton loop markers")
    prefix, rest = source.split(start_marker, 1)
    _, suffix = rest.split(end_marker, 1)
    old_iterations = f"int iterations={args.order.bit_length() - 1}; int iteration;"
    new_iterations = f"int iterations={args.order - 1}; int iteration;"
    if prefix.count(old_iterations) != 1:
        raise RuntimeError("iteration marker")
    prefix = prefix.replace(old_iterations, new_iterations)
    inv_marker = "poly INV=imap(B,inv0);"
    if prefix.count(inv_marker) != 1:
        raise RuntimeError("inverse marker")
    prefix = prefix.replace(inv_marker, inv_marker + "\npoly INVBASE=imap(B,inv0);")
    loop = "\n".join(
        [
            "for (iteration=1;iteration<=iterations;iteration++)",
            "{",
            "  map evalStepV=R,25+s,y[1],y[2],y[3],y[4],y[5],y[6],V;",
            "  poly Hres=reduce(evalStepV(H),ZA);",
            "  V=reduce(V-U*Hres,ZA);",
            "  kill evalStepV;",
            "  map evalStepY=R,25+s,y[1],y[2],y[3],y[4],y[5],y[6],V;",
            "  ideal Fres=evalStepY(F);",
            "  for (ii=1;ii<=6;ii++){FC[ii,1]=reduce(Fres[ii],ZA);}",
            "  DELTA=K*FC;",
            "  for (ii=1;ii<=6;ii++){y[ii]=reduce(y[ii]-DELTA[ii,1],ZA);}",
            "  kill evalStepY;",
            "  poly locden=reduce(y[6]*(y[5]-2*y[6]),ZA);",
            "  INV=reduce(INV+INVBASE*(1-locden*INV),ZA);",
            '  print("iteration="+string(iteration));',
            "}",
            "map evalFinal=R,25+s,y[1],y[2],y[3],y[4],y[5],y[6],V;",
        ]
    )
    print(prefix + loop + suffix, end="")


if __name__ == "__main__":
    main()

