#!/usr/bin/env python3
"""Generate exact modular elimination input for the global (w,v) projection."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
PARENT_MANIFEST = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/MANIFEST.sha256"
PARENT_MANIFEST_SHA256 = "3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4"


def load_compiler():
    for path, expected in (
        (COMPILER, COMPILER_SHA256),
        (PARENT_MANIFEST, PARENT_MANIFEST_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_wv_projection_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(prime: int, engine: str) -> str:
    Q = load_compiler()
    ring, rows, imposed, names = Q.compile_quotient("approx")
    internal = ["c", "d2", "d4", "x1", "x3", "x5", "inv"]
    lines = [
        f"ring R={prime},({','.join(internal + ['w', 'v'])}),(dp(7),dp(2));",
        "option(redSB);",
    ]
    for ell in imposed:
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "poly einv=inv*w*x5*(x3-2*x5)-1;",
        "poly ev=v*x5-x3+2*x5;",
        "ideal I=e1,e3,e5,e7,e2,e4,einv,ev;",
        f"ideal G={engine}(I);",
        'print("Q8-WV-PROJECTION");',
        'print("open_dim="+string(dim(G)));',
        'print("basis_size="+string(size(G)));',
        "ideal E=eliminate(G,c*d2*d4*x1*x3*x5*inv);",
        'print("elimination_size="+string(size(E)));',
        "E;",
        "if (size(E)>0)",
        "{",
        "  ideal B=subst(E,w,0);",
        "  B=std(B);",
        '  print("w0_size="+string(size(B)));',
        "  B;",
        "  poly Q8=-999*v^8-1539*v^7+1782*v^6+6498*v^5+7320*v^4+4428*v^3+1548*v^2+296*v+24;",
        "  poly Q8gcd=Q8;",
        "  for (int i=1; i<=size(B); i++)",
        "  {",
        "    if (B[i]!=0) { Q8gcd=gcd(Q8gcd,B[i]); }",
        "  }",
        '  print("w0_Q8_gcd_degree="+string(deg(Q8gcd)));',
        "  Q8gcd;",
        "}",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="slimgb")
    args = parser.parse_args()
    print(source(args.prime, args.engine))


if __name__ == "__main__":
    main()
