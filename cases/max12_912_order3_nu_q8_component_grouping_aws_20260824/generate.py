#!/usr/bin/env python3
"""Generate the exact Q8 component-grouping/projective-boundary job."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
FROZEN_MANIFEST = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/MANIFEST.sha256"
FROZEN_MANIFEST_SHA256 = "3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4"


def load():
    for path, expected in (
        (COMPILER, COMPILER_SHA256),
        (FROZEN_MANIFEST, FROZEN_MANIFEST_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_grouping_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(prime, engine, mode):
    Q = load()
    ring, rows, imposed, names = Q.compile_quotient("approx")
    internal = ["c", "d2", "d4", "x1", "x3", "x5"]
    variables = internal + ["w", "v"]
    lines = [
        'LIB "primdec.lib";',
        f"ring R={prime},({','.join(variables)}),(dp(6),dp(2));",
        "option(redSB);",
    ]
    for ell in imposed:
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "ideal I=e1,e3,e5,e7,e2,e4;",
        "ideal Open=ideal(w*x5*(x3-2*x5));",
        "list Sat=sat(I,Open);",
        f"ideal Is={engine}(Sat[1]);",
        'print("Q8-GROUPING-SATURATION");',
        'print("sat_exponent="+string(Sat[2]));',
        'print("sat_dim="+string(dim(Is)));',
        'print("sat_size="+string(size(Is)));',
    ])
    if mode == "saturation":
        return "\n".join(lines)
    lines.extend([
        "list Components=minAssGTZ(Is);",
        'print("component_count="+string(size(Components)));',
        "poly Q8=-999*v^8-1539*v^7+1782*v^6+6498*v^5+7320*v^4+4428*v^3+1548*v^2+296*v+24;",
        "poly ev=v*x5-x3+2*x5;",
        "for (int component=1; component<=size(Components); component++)",
        "{",
        "  ideal P=std(Components[component]);",
        '  print("COMPONENT="+string(component));',
        '  print("component_dim="+string(dim(P)));',
        '  print("component_size="+string(size(P)));',
        "  ideal Boundary=std(P+ideal(w,ev));",
        '  print("boundary_dim="+string(dim(Boundary)));',
        "  ideal EV=eliminate(Boundary,c*d2*d4*x1*x3*x5*w);",
        '  print("v_elimination_size="+string(size(EV)));',
        "  EV;",
        "  if (size(EV)>0)",
        "  {",
        "    poly BoundaryV=EV[1];",
        "    poly Q8gcd=gcd(BoundaryV,Q8);",
        '    print("Q8_gcd_degree="+string(deg(Q8gcd)));',
        "    Q8gcd;",
        "  }",
        "}",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="slimgb")
    parser.add_argument("--mode", choices=("saturation", "grouping"), default="grouping")
    args = parser.parse_args()
    print(source(args.prime, args.engine, args.mode))


if __name__ == "__main__":
    main()
