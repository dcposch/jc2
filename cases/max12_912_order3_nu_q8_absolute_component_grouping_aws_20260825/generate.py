#!/usr/bin/env python3
"""Generate the exact characteristic-zero absolute Q8 component gate."""

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
CONTACT_FREEZE = ROOT / "cases/max12_912_order3_nu_q8_infinity_contact_passport_20260824/FREEZE.txt"
CONTACT_FREEZE_SHA256 = "8d695040eb73bc8719f484a724ce4d4bbda61c650e73ec617c6bbdd713d8e298"


def load_compiler():
    for path, expected in (
        (COMPILER, COMPILER_SHA256),
        (PARENT_MANIFEST, PARENT_MANIFEST_SHA256),
        (CONTACT_FREEZE, CONTACT_FREEZE_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_absolute_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(engine: str) -> str:
    Q = load_compiler()
    ring, rows, imposed, names = Q.compile_quotient("approx")
    variables = ["c", "d2", "d4", "x1", "x3", "x5", "w", "v"]
    lines = [
        'LIB "primdec.lib";',
        f"ring R=0,({','.join(variables)}),(dp(6),dp(2));",
        "option(redSB);",
    ]
    for ell in imposed:
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "ideal I=e1,e3,e5,e7,e2,e4;",
        "ideal Open=ideal(w*x5*(x3-2*x5));",
        "list Sat=sat(I,Open);",
        f"ideal Is={engine}(Sat[1]);",
        'print("Q8-ABSOLUTE-GROUPING");',
        'print("characteristic=0");',
        'print("sat_exponent="+string(Sat[2]));',
        'print("sat_dim="+string(dim(Is)));',
        'print("sat_size="+string(size(Is)));',
        "def ABS=absPrimdecGTZ(Is);",
        "setring ABS;",
        'print("absolute_class_count="+string(size(absolute_primes)));',
        'print("rational_primary_count="+string(size(primary_decomp)));',
        "poly Q8=-999*v^8-1539*v^7+1782*v^6+6498*v^5+7320*v^4+4428*v^3+1548*v^2+296*v+24;",
        "poly ev=v*x5-x3+2*x5;",
        "for (int component=1; component<=size(absolute_primes); component++)",
        "{",
        "  ideal P=std(absolute_primes[component][1]);",
        "  int conjugates=absolute_primes[component][2];",
        "  ideal Hit=std(P+ideal(w,ev,Q8));",
        "  int hit_unit=0;",
        "  if (size(Hit)>0)",
        "  {",
        "    if (deg(Hit[1])==0) { hit_unit=1; }",
        "  }",
        '  print("ABSOLUTE_COMPONENT="+string(component));',
        '  print("conjugates="+string(conjugates));',
        '  print("prime_dim="+string(dim(P)));',
        '  print("prime_size="+string(size(P)));',
        '  print("q8_hit_unit="+string(hit_unit));',
        '  print("q8_hit_dim="+string(dim(Hit)));',
        "  if (hit_unit==0)",
        "  {",
        '    print("q8_hit_vdim="+string(vdim(Hit)));',
        "    ideal EV=eliminate(Hit,c*d2*d4*x1*x3*x5*w);",
        '    print("q8_hit_elimination_size="+string(size(EV)));',
        "    EV;",
        "  }",
        "}",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="slimgb")
    args = parser.parse_args()
    print(source(args.engine))


if __name__ == "__main__":
    main()
