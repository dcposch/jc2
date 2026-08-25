#!/usr/bin/env python3
"""Generate localized-minimal-prime Q8 grouping input."""

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
    spec = importlib.util.spec_from_file_location("q8_localized_grouping_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(prime: int, engine: str) -> str:
    Q = load_compiler()
    ring, rows, imposed, names = Q.compile_quotient("approx")
    variables = ["w", "c", "d2", "d4", "x1", "x3", "x5", "inv", "v"]
    lines = [
        'LIB "primdec.lib";',
        f"ring R={prime},({','.join(variables)}),dp;",
        "option(redSB);",
    ]
    for ell in imposed:
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "poly einv=inv*w*x5*(x3-2*x5)-1;",
        "ideal IL=e1,e3,e5,e7,e2,e4,einv;",
        f"ideal GL={engine}(IL);",
        'print("Q8-LOCALIZED-MINASS-GROUPING");',
        'print("localized_dim="+string(dim(GL)));',
        'print("localized_size="+string(size(GL)));',
        "list Components=minAssGTZ(GL);",
        'print("localized_component_count="+string(size(Components)));',
        "poly Q8=-999*v^8-1539*v^7+1782*v^6+6498*v^5+7320*v^4+4428*v^3+1548*v^2+296*v+24;",
        "poly ev=v*x5-x3+2*x5;",
        "for (int component=1; component<=size(Components); component++)",
        "{",
        "  ideal PL=std(Components[component]);",
        "  ideal P=eliminate(PL,inv);",
        "  P=std(P);",
        "  ideal Boundary=std(P+ideal(w,ev));",
        "  ideal EV=eliminate(Boundary,c*d2*d4*x1*x3*x5*w*inv);",
        '  print("LOCALIZED_COMPONENT="+string(component));',
        '  print("localized_prime_dim="+string(dim(PL)));',
        '  print("localized_prime_size="+string(size(PL)));',
        '  print("contraction_dim="+string(dim(P)));',
        '  print("contraction_size="+string(size(P)));',
        '  print("boundary_dim="+string(dim(Boundary)));',
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
    args = parser.parse_args()
    print(source(args.prime, args.engine))


if __name__ == "__main__":
    main()
