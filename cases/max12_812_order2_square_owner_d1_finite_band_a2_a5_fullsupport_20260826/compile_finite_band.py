#!/usr/bin/env python3
"""Compile fixed-contact, complete-source D1 receivers for a=2..5.

The compiler is AWS-only.  It imports the frozen shared-Faber compiler solely
for its source substitution, exact seven-tail extraction, Laurent extraction,
and moving lower-unitriangular row-transform routines.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE_COMPILER = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/compile_r1_d1_ac.py"
BASE_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/FREEZE.sha256"
ERRATUM = ROOT / "xmodel/max12-812-order2-square-r1-d1-v12-source-support-erratum-20260826.md"
FIRST_NORMAL = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-promotion-20260826.md"
CLOSURE = ROOT / "xmodel/max12-812-order2-square-contact-raising-closure-criterion-20260826.md"

PINS = {
    BASE_COMPILER: "e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c",
    BASE_FREEZE: "34b0f3254410e39abfc9843febd3c053f965a30dfa948d9e0367c0fb094611a6",
    ERRATUM: "997dda081223d99283bff92851e7da8bc260b7b3e52ff89b97fb0a50c817a114",
    FIRST_NORMAL: "40790378bfcc7b0e0719038ef0e951712abef570b4865c0bca371409706c9f94",
    CLOSURE: "3c0a33ceddfad8ca69afb145ae5249f0d2b4866c5a8af498d257e9d4a78cfd95",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only D1 finite-band compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only D1 finite-band compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    spec = importlib.util.spec_from_file_location("d1_frozen_base", BASE_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot load frozen D1 base compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def map_images(z_image: str, a0_image: str, c0_image: str) -> list[str]:
    images = [
        z_image, "t", "sigma", "-2*rtx*rtx", "ell1", "eta",
        a0_image, "aua", "aa0", "aa1", c0_image, "cvg", "cc0", "cc1",
        "b0", "b1", "k0", "k6", "k2load", "mu2", "mu4", "mu6", "J",
        "rtx", "aua", "cvg",
    ]
    if len(images) != 26:
        fail(("map image count", len(images)))
    return images


def map_line(name: str, source: str, values: list[str]) -> str:
    return f"map {name}={source}," + ",".join(values) + ";"


def fixed_section(characteristic: int, base_module, tail_base, tails, a: int) -> list[str]:
    prefix = f"A{a}_"
    ring_name = f"Ra{a}"
    g = 11 + 2 * a
    gp = g + 1
    variables = (
        "z,t,sigma,p,ell1,eta,a0,a1,aa0,aa1,c0,c1,cc0,cc1,"
        "b0,b1,k0,k6,k2load,mu2,mu4,mu6,J,rtx,aua,cvg"
    )
    lines = [
        f"ring {ring_name}={characteristic},({variables}),dp;",
        f'print("{prefix}SOURCE_HASHES=PASS");',
        f'print("{prefix}FIXED_CONTACT={a}");',
        f'print("{prefix}GRADE_PAIR={g},{gp}");',
    ]

    pp = "(p+2*sigma*ell1)"
    az = f"(sigma^{a}*(a1+sigma*aa1))"
    ac = f"(sigma^{a}*(a0+sigma*aa0))"
    cz = f"(sigma^{a + 1}*(c1+sigma*cc1))"
    cc = f"(sigma^{a + 1}*(c0+sigma*cc0))"
    rz = f"(sigma^{a}*eta*b1)"
    rc = f"(sigma^{a}*eta*b0)"
    coeffs = base_module.source_coefficients(pp, az, ac, cz, cc, rz, rc)
    loads = {"k10": "k0", "k6": "k6", "k2": "k2load"}
    base_module.extraction(lines, prefix, tail_base, tails, coeffs, loads, g, gp)

    lines.extend([
        f"poly {prefix}sp=p/2+sigma*ell1;",
        f"poly {prefix}Inv1=1-{prefix}sp*t^2+{prefix}sp*{prefix}sp*t^4-{prefix}sp*{prefix}sp*{prefix}sp*t^6+{prefix}sp*{prefix}sp*{prefix}sp*{prefix}sp*t^8;",
        f"poly {prefix}Inv2=1-2*{prefix}sp*t^2+3*{prefix}sp*{prefix}sp*t^4-4*{prefix}sp*{prefix}sp*{prefix}sp*t^6+5*{prefix}sp*{prefix}sp*{prefix}sp*{prefix}sp*t^8;",
        f"poly {prefix}Inv3=1-3*{prefix}sp*t^2+6*{prefix}sp*{prefix}sp*t^4-10*{prefix}sp*{prefix}sp*{prefix}sp*t^6+15*{prefix}sp*{prefix}sp*{prefix}sp*{prefix}sp*t^8;",
    ])
    A = f"sigma^{a}*((a1+a0*t)+sigma*(aa1+aa0*t))"
    C = f"sigma^{a + 1}*((c1+c0*t)+sigma*(cc1+cc0*t))"
    B = f"sigma^{a}*eta*(b1+b0*t)"
    hshift = base_module.universal_hshift(A, C, B, "k0", f"{prefix}Inv1", f"{prefix}Inv2", f"{prefix}Inv3")
    base_module.analytic_extract(lines, prefix, hshift, g, gp)
    base_module.row_checks(lines, prefix, base_module.load_v1(), g, gp)

    # The first negative tail has denominator L; the second has denominator L^2.
    lines.extend([
        f"poly {prefix}L=z*z+p/2;",
        f"poly {prefix}Nfirst={prefix}h{g}_1*z+{prefix}h{g}_2;",
        f"int {prefix}recfirst=1;",
        f"if ({prefix}h{g}_3+(p/2)*{prefix}h{g}_1!=0) {{ {prefix}recfirst=0; }}",
        f"if ({prefix}h{g}_4+(p/2)*{prefix}h{g}_2!=0) {{ {prefix}recfirst=0; }}",
        f"if ({prefix}h{g}_5+(p/2)*{prefix}h{g}_3!=0) {{ {prefix}recfirst=0; }}",
        f"if ({prefix}h{g}_6+(p/2)*{prefix}h{g}_4!=0) {{ {prefix}recfirst=0; }}",
        f"if ({prefix}h{g}_7+(p/2)*{prefix}h{g}_5!=0) {{ {prefix}recfirst=0; }}",
        f"poly {prefix}Nnext={prefix}h{gp}_1*z*z*z+{prefix}h{gp}_2*z*z+({prefix}h{gp}_3+p*{prefix}h{gp}_1)*z+({prefix}h{gp}_4+p*{prefix}h{gp}_2);",
        f"int {prefix}recnext=1;",
        f"if ({prefix}h{gp}_5+p*{prefix}h{gp}_3+(p*p/4)*{prefix}h{gp}_1!=0) {{ {prefix}recnext=0; }}",
        f"if ({prefix}h{gp}_6+p*{prefix}h{gp}_4+(p*p/4)*{prefix}h{gp}_2!=0) {{ {prefix}recnext=0; }}",
        f"if ({prefix}h{gp}_7+p*{prefix}h{gp}_5+(p*p/4)*{prefix}h{gp}_3!=0) {{ {prefix}recnext=0; }}",
        f'int {prefix}bridge=({prefix}divisible*{prefix}identities*{prefix}forbidden*{prefix}analyticDiv*{prefix}row{g}*{prefix}row{gp}*{prefix}recfirst*{prefix}recnext);',
        f'print("{prefix}DENOMINATOR_RECURRENCE_FIRST="+string({prefix}recfirst));',
        f'print("{prefix}DENOMINATOR_RECURRENCE_NEXT="+string({prefix}recnext));',
        f'print("{prefix}COMPLETE_SOURCE_BRIDGE="+string({prefix}bridge));',
        f'if ({prefix}bridge!=1) {{ print("{prefix}FAIL=SOURCE_BRIDGE_OR_RECURRENCE"); quit; }}',
    ])

    eval_ring = f"Ea{a}"
    pos = map_images("z", "-aua*rtx", "cvg*rtx")
    neg = map_images("z", "aua*rtx", "-cvg*rtx")
    posroot = map_images("rtx", "-aua*rtx", "cvg*rtx")
    negroot = map_images("-rtx", "aua*rtx", "-cvg*rtx")
    lines.extend([
        f"ring {eval_ring}={characteristic},({variables}),dp;",
        map_line(f"{prefix}posmap", ring_name, pos),
        map_line(f"{prefix}negmap", ring_name, neg),
        map_line(f"{prefix}posrootmap", ring_name, posroot),
        map_line(f"{prefix}negrootmap", ring_name, negroot),
        f"poly {prefix}evalposfirst={prefix}posmap({prefix}Nfirst);",
        f"poly {prefix}evalnegfirst={prefix}negmap({prefix}Nfirst);",
        f"poly {prefix}evalposrootnext={prefix}posrootmap({prefix}Nnext);",
        f"poly {prefix}evalnegrootnext={prefix}negrootmap({prefix}Nnext);",
        f"int {prefix}allocation=({prefix}evalposfirst==0 && {prefix}evalnegfirst==0);",
        f"int {prefix}residue=({prefix}evalposrootnext-(3/2)*rtx*rtx*cvg*cvg==0 && {prefix}evalnegrootnext-(3/2)*rtx*rtx*cvg*cvg==0);",
        f'print("{prefix}BOTH_ROOT_ALLOCATIONS="+string({prefix}allocation));',
        f'print("{prefix}UNMATCHED_C2_RESIDUE="+string({prefix}residue));',
        f'if ({prefix}allocation*{prefix}residue!=1) {{ print("{prefix}FAIL=ROOT_ALLOCATION_OR_RESIDUE"); quit; }}',
        f'print("{prefix}ENDPOINT=PASS_FIXED_D1_CONTACT_A{a}");',
    ])
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen pin mismatch", str(source), actual, expected))

    base_module = load_base()
    for source, expected in base_module.PINS.items():
        if digest(source) != expected:
            fail(("frozen imported pin mismatch", str(source)))
    v1 = base_module.load_v1()
    for source, expected in v1.EXPECTED.items():
        if digest(source) != expected:
            fail(("frozen transitive source mismatch", str(source)))
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    tail_base = v1.load_base()

    output = args.output.resolve()
    if output.exists():
        fail("finite-band output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_finite_band_a2_a5_{label}.sing"
    lines: list[str] = []
    for a in range(2, 6):
        lines.extend(fixed_section(args.characteristic, base_module, tail_base, tails, a))
    lines.extend([
        'print("D1_FINITE_BAND_A2_A5_ENDPOINT=PASS");',
        "quit;",
    ])
    target.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "PASS-D1-FINITE-BAND-A2-A5-COMPILER",
        "scope": "FIXED_CONTACTS_A2_A5_COMPLETE_SEVEN_SOURCE_ROWS_NO_UNBOUNDED_D1_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "base_compiler_sha256": digest(BASE_COMPILER),
        "all_tails_sha256": v1.EXPECTED_ALL_TAILS,
        "fixed_contacts": [2, 3, 4, 5],
        "grade_pairs": [[11 + 2 * a, 12 + 2 * a] for a in range(2, 6)],
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

