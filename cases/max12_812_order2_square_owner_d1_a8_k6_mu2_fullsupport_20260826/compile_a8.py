#!/usr/bin/env python3
"""Compile the two complete-source a=8 D1 k6/mu2 sections (AWS only)."""

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
PINS = {
    BASE_COMPILER: "e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c",
    BASE_FREEZE: "34b0f3254410e39abfc9843febd3c053f965a30dfa948d9e0367c0fb094611a6",
    ERRATUM: "997dda081223d99283bff92851e7da8bc260b7b3e52ff89b97fb0a50c817a114",
    FIRST_NORMAL: "40790378bfcc7b0e0719038ef0e951712abef570b4865c0bca371409706c9f94",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only a8 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only a8 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    spec = importlib.util.spec_from_file_location("a8_d1_base", BASE_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot load frozen D1 base compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def extract_source(lines, prefix, tail_base, tails, coeffs, loads,
                   minimum, maximum, allowed_by_grade):
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    charges = ("k60", "k61", "k62", "k2load", "mu2", "mu4", "mu6", "J")
    lines.extend([
        f"ideal {prefix}Sigma=std(ideal(sigma^{minimum}));",
        f"ideal {prefix}Sigma1=std(ideal(sigma));",
        f"int {prefix}divisible=1; int {prefix}identities=1; int {prefix}support=1;",
    ])
    for row in range(1, 8):
        expression = tail_base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
        if targets[row] != "0":
            expression += f"-sigma^{2 * (12 + row)}*({targets[row]})"
        lines.extend([
            f"poly {prefix}Phi{row}={expression};",
            f"if (reduce({prefix}Phi{row},{prefix}Sigma)!=0) {{ {prefix}divisible=0; }}",
            f"poly {prefix}Q{minimum}_{row}={prefix}Phi{row}/sigma^{minimum};",
            f"if (sigma^{minimum}*{prefix}Q{minimum}_{row}-{prefix}Phi{row}!=0) {{ {prefix}identities=0; }}",
        ])
        for grade in range(minimum, maximum + 1):
            qname = f"{prefix}Q{grade}_{row}"
            gname = f"{prefix}g{grade}_{row}"
            lines.append(f"poly {gname}=subst({qname},sigma,0);")
            allowed = set(allowed_by_grade[grade])
            for variable in charges:
                if variable not in allowed:
                    lines.append(f"if (diff({gname},{variable})!=0) {{ {prefix}support=0; }}")
            if grade < maximum:
                rem = f"{prefix}Rem{grade + 1}_{row}"
                nxt = f"{prefix}Q{grade + 1}_{row}"
                lines.extend([
                    f"poly {rem}={qname}-{gname};",
                    f"if (reduce({rem},{prefix}Sigma1)!=0) {{ {prefix}identities=0; }}",
                    f"poly {nxt}={rem}/sigma;",
                    f"if (sigma*{nxt}-{rem}!=0) {{ {prefix}identities=0; }}",
                ])
    lines.extend([
        f'print("{prefix}SOURCE_DIVISIBLE="+string({prefix}divisible));',
        f'print("{prefix}SOURCE_QUOTIENT_IDENTITIES="+string({prefix}identities));',
        f'print("{prefix}SOURCE_SUPPORT_FILTER="+string({prefix}support));',
        f'if ({prefix}divisible*{prefix}identities*{prefix}support!=1) {{ print("{prefix}FAIL=SOURCE_EXTRACTION_OR_SUPPORT"); quit; }}',
    ])


def inv_lines(prefix: str) -> list[str]:
    return [
        f"poly {prefix}sp=p/2+sigma*ell1;",
        f"poly {prefix}Inv1=1-{prefix}sp*t^2+{prefix}sp*{prefix}sp*t^4-{prefix}sp*{prefix}sp*{prefix}sp*t^6+{prefix}sp*{prefix}sp*{prefix}sp*{prefix}sp*t^8;",
        f"poly {prefix}Inv2=1-2*{prefix}sp*t^2+3*{prefix}sp*{prefix}sp*t^4-4*{prefix}sp*{prefix}sp*{prefix}sp*t^6+5*{prefix}sp*{prefix}sp*{prefix}sp*{prefix}sp*t^8;",
        f"poly {prefix}Inv3=1-3*{prefix}sp*t^2+6*{prefix}sp*{prefix}sp*t^4-10*{prefix}sp*{prefix}sp*{prefix}sp*t^6+15*{prefix}sp*{prefix}sp*{prefix}sp*{prefix}sp*t^8;",
    ]


def t0_prediction(v1, prefix: str, grade: int, row: int) -> str:
    terms = []
    for j in range(1, row + 1):
        t0, _, _ = v1.transform_series(row, j)
        if t0 != "0":
            terms.append(f"({t0})*{prefix}h{grade}_{j}")
    return "+".join(terms).replace("+-", "-") or "0"


def q0_section(characteristic, base_module, v1, tail_base, tails):
    prefix = "A8Q0_"
    variables = (
        "z,t,sigma,p,ell1,eta,a0,a1,aa0,aa1,c0,c1,cc0,cc1,b0,b1,"
        "k0,k60,k61,k62,k2load,mu2,mu4,mu6,J,inv"
    )
    lines = [f"ring Rq0={characteristic},({variables}),dp;", f'print("{prefix}SOURCE_HASHES=PASS");']
    pp = "(p+2*sigma*ell1)"
    coeffs = base_module.source_coefficients(
        pp,
        "(sigma^8*(a1+sigma*aa1))", "(sigma^8*(a0+sigma*aa0))",
        "(sigma^9*(c1+sigma*cc1))", "(sigma^9*(c0+sigma*cc0))",
        "(sigma^8*eta*b1)", "(sigma^8*eta*b0)",
    )
    loads = {"k10": "k0", "k6": "(k60+sigma*k61+sigma^2*k62)", "k2": "k2load"}
    extract_source(lines, prefix, tail_base, tails, coeffs, loads, 26, 26, {26: ("k60",)})
    lines.extend(inv_lines(prefix))
    C = "sigma^9*((c1+c0*t)+sigma*(cc1+cc0*t))"
    hshift = f"(3/4)*sigma^17*t*t*(k60+sigma*k61+sigma^2*k62)*({C})*({prefix}Inv1)"
    base_module.analytic_extract(lines, prefix, hshift, 26, 26)
    base_module.row_checks(lines, prefix, v1, 26, 26)
    lines.extend([
        f"poly {prefix}L=z*z+p/2;",
        f"poly {prefix}N={prefix}h26_1*z+{prefix}h26_2;",
        f"int {prefix}rec=1;",
        f"if ({prefix}h26_3+(p/2)*{prefix}h26_1!=0) {{ {prefix}rec=0; }}",
        f"if ({prefix}h26_4+(p/2)*{prefix}h26_2!=0) {{ {prefix}rec=0; }}",
        f"if ({prefix}h26_5+(p/2)*{prefix}h26_3!=0) {{ {prefix}rec=0; }}",
        f"if ({prefix}h26_6+(p/2)*{prefix}h26_4!=0) {{ {prefix}rec=0; }}",
        f"if ({prefix}h26_7+(p/2)*{prefix}h26_5!=0) {{ {prefix}rec=0; }}",
        f"int {prefix}num=({prefix}h26_1-(3/4)*k60*c1==0 && {prefix}h26_2-(3/4)*k60*c0==0);",
        f"int {prefix}unit=(reduce(c0,std(ideal({prefix}h26_1,{prefix}h26_2,inv*k60-1)))==0 && reduce(c1,std(ideal({prefix}h26_1,{prefix}h26_2,inv*k60-1)))==0);",
        f'print("{prefix}ROW_IDENTITY="+string({prefix}row26));',
        f'print("{prefix}DENOMINATOR_RECURRENCE="+string({prefix}rec));',
        f'print("{prefix}NUMERATOR_COEFFICIENTS="+string({prefix}num));',
        f'print("{prefix}DK60_FORCES_C_ZERO="+string({prefix}unit));',
        f"if ({prefix}divisible*{prefix}identities*{prefix}support*{prefix}analyticDiv*{prefix}row26*{prefix}rec*{prefix}num*{prefix}unit!=1) {{ print(\"{prefix}FAIL=Q0_SIMPLE_POLE\"); quit; }}",
        f'print("{prefix}ENDPOINT=PASS_A8_Q6_ZERO_SIMPLE_POLE");',
    ])
    return lines


def map_images(z_image: str, a0_image: str, c0_image: str) -> list[str]:
    values = [
        z_image, "t", "sigma", "-2*rtx*rtx", "ell1", "eta",
        a0_image, "aua", "aa0", "aa1", c0_image, "cvg", "cc0", "cc1",
        "b0", "b1", "k0", "k61", "k62", "k2load", "mu2", "mu4", "mu6", "J",
        "rtx", "aua", "cvg",
    ]
    if len(values) != 27:
        fail(("map image count", len(values)))
    return values


def map_line(name, source, values):
    return f"map {name}={source}," + ",".join(values) + ";"


def qplus_section(characteristic, base_module, v1, tail_base, tails):
    prefix = "A8QP_"
    variables = (
        "z,t,sigma,p,ell1,eta,a0,a1,aa0,aa1,c0,c1,cc0,cc1,b0,b1,"
        "k0,k61,k62,k2load,mu2,mu4,mu6,J,rtx,aua,cvg"
    )
    lines = [f"ring Rqp={characteristic},({variables}),dp;", f'print("{prefix}SOURCE_HASHES=PASS");']
    pp = "(p+2*sigma*ell1)"
    coeffs = base_module.source_coefficients(
        pp,
        "(sigma^8*(a1+sigma*aa1))", "(sigma^8*(a0+sigma*aa0))",
        "(sigma^9*(c1+sigma*cc1))", "(sigma^9*(c0+sigma*cc0))",
        "(sigma^8*eta*b1)", "(sigma^8*eta*b0)",
    )
    loads = {"k10": "k0", "k6": "(sigma*k61+sigma^2*k62)", "k2": "k2load"}
    allowed = {27: ("k61",), 28: ("k61", "k62", "mu2")}
    extract_source(lines, prefix, tail_base, tails, coeffs, loads, 27, 28, allowed)
    lines.extend(inv_lines(prefix))
    A = "sigma^8*((a1+a0*t)+sigma*(aa1+aa0*t))"
    C = "sigma^9*((c1+c0*t)+sigma*(cc1+cc0*t))"
    B = "sigma^8*eta*(b1+b0*t)"
    hbase = base_module.universal_hshift(A, C, B, "k0", f"{prefix}Inv1", f"{prefix}Inv2", f"{prefix}Inv3")
    hlower = f"+(3/4)*sigma^17*t*t*(sigma*k61+sigma^2*k62)*({C})*({prefix}Inv1)"
    htarget = "+sigma^28*(-mu2*t^3+(p/2)*mu2*t^5-(p*p/4)*mu2*t^7)"
    base_module.analytic_extract(lines, prefix, hbase + hlower + htarget, 27, 28)
    base_module.row_checks(lines, prefix, v1, 27, 28)
    lines.append(f"int {prefix}t1needed=0;")
    for row in range(1, 8):
        predicted = t0_prediction(v1, prefix, 28, row)
        lines.append(f"if ({prefix}g28_{row}-({predicted})!=0) {{ {prefix}t1needed=1; }}")
    lines.extend([
        f"int {prefix}k6needed=0; int {prefix}targetneeded=0;",
    ])
    for row in range(1, 8):
        lines.append(f"if (diff({prefix}g27_{row},k61)!=0 || diff({prefix}g28_{row},k62)!=0) {{ {prefix}k6needed=1; }}")
        lines.append(f"if (diff({prefix}g28_{row},mu2)!=0) {{ {prefix}targetneeded=1; }}")
    lines.extend([
        f'print("{prefix}NEGCTRL_DELETE_T1_FAILS="+string({prefix}t1needed));',
        f'print("{prefix}NEGCTRL_DELETE_K6C_FAILS="+string({prefix}k6needed));',
        f'print("{prefix}NEGCTRL_DELETE_MU2_FAILS="+string({prefix}targetneeded));',
        f"if ({prefix}t1needed*{prefix}k6needed*{prefix}targetneeded!=1) {{ print(\"{prefix}FAIL=NEGATIVE_CONTROL\"); quit; }}",
        f"poly {prefix}Nfirst={prefix}h27_1*z+{prefix}h27_2;",
        f"int {prefix}recfirst=1;",
        f"if ({prefix}h27_3+(p/2)*{prefix}h27_1!=0) {{ {prefix}recfirst=0; }}",
        f"if ({prefix}h27_4+(p/2)*{prefix}h27_2!=0) {{ {prefix}recfirst=0; }}",
        f"if ({prefix}h27_5+(p/2)*{prefix}h27_3!=0) {{ {prefix}recfirst=0; }}",
        f"if ({prefix}h27_6+(p/2)*{prefix}h27_4!=0) {{ {prefix}recfirst=0; }}",
        f"if ({prefix}h27_7+(p/2)*{prefix}h27_5!=0) {{ {prefix}recfirst=0; }}",
        f"poly {prefix}Nnext={prefix}h28_1*z*z*z+{prefix}h28_2*z*z+({prefix}h28_3+p*{prefix}h28_1)*z+({prefix}h28_4+p*{prefix}h28_2);",
        f"int {prefix}recnext=1;",
        f"if ({prefix}h28_5+p*{prefix}h28_3+(p*p/4)*{prefix}h28_1!=0) {{ {prefix}recnext=0; }}",
        f"if ({prefix}h28_6+p*{prefix}h28_4+(p*p/4)*{prefix}h28_2!=0) {{ {prefix}recnext=0; }}",
        f"if ({prefix}h28_7+p*{prefix}h28_5+(p*p/4)*{prefix}h28_3!=0) {{ {prefix}recnext=0; }}",
        f"int {prefix}bridge=({prefix}divisible*{prefix}identities*{prefix}support*{prefix}analyticDiv*{prefix}row27*{prefix}row28*{prefix}recfirst*{prefix}recnext);",
        f'print("{prefix}DENOMINATOR_RECURRENCE_FIRST="+string({prefix}recfirst));',
        f'print("{prefix}DENOMINATOR_RECURRENCE_NEXT="+string({prefix}recnext));',
        f'print("{prefix}COMPLETE_SOURCE_BRIDGE="+string({prefix}bridge));',
        f"if ({prefix}bridge!=1) {{ print(\"{prefix}FAIL=SOURCE_BRIDGE_OR_RECURRENCE\"); quit; }}",
    ])
    pos_a0 = "-aua*rtx-k61"
    neg_a0 = "aua*rtx-k61"
    pos = map_images("z", pos_a0, "cvg*rtx")
    neg = map_images("z", neg_a0, "-cvg*rtx")
    posroot = map_images("rtx", pos_a0, "cvg*rtx")
    negroot = map_images("-rtx", neg_a0, "-cvg*rtx")
    lines.extend([
        f"ring Eqp={characteristic},({variables}),dp;",
        map_line(f"{prefix}posmap", "Rqp", pos),
        map_line(f"{prefix}negmap", "Rqp", neg),
        map_line(f"{prefix}posrootmap", "Rqp", posroot),
        map_line(f"{prefix}negrootmap", "Rqp", negroot),
        f"poly {prefix}evalposfirst={prefix}posmap({prefix}Nfirst);",
        f"poly {prefix}evalnegfirst={prefix}negmap({prefix}Nfirst);",
        f"poly {prefix}evalposrootnext={prefix}posrootmap({prefix}Nnext);",
        f"poly {prefix}evalnegrootnext={prefix}negrootmap({prefix}Nnext);",
        f"int {prefix}allocation=({prefix}evalposfirst==0 && {prefix}evalnegfirst==0);",
        f"int {prefix}residue=({prefix}evalposrootnext-(3/2)*rtx*rtx*cvg*cvg==0 && {prefix}evalnegrootnext-(3/2)*rtx*rtx*cvg*cvg==0);",
        f'print("{prefix}BOTH_SHIFTED_ROOT_ALLOCATIONS="+string({prefix}allocation));',
        f'print("{prefix}MU2_L_MULTIPLE_C2_RESIDUE="+string({prefix}residue));',
        f"if ({prefix}allocation*{prefix}residue!=1) {{ print(\"{prefix}FAIL=ROOT_ALLOCATION_OR_RESIDUE\"); quit; }}",
        f'print("{prefix}ENDPOINT=PASS_A8_POSITIVE_Q6_OR_ZERO_K6");',
    ])
    return lines


def main():
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
        fail("a8 output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_a8_k6_mu2_{label}.sing"
    lines = q0_section(args.characteristic, base_module, v1, tail_base, tails)
    lines.extend(qplus_section(args.characteristic, base_module, v1, tail_base, tails))
    lines.extend(['print("D1_A8_K6_MU2_ENDPOINT=PASS");', "quit;"])
    target.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "PASS-D1-A8-K6-MU2-COMPILER",
        "scope": "TWO_EXHAUSTIVE_K6_SECTIONS_FIXED_A8_COMPLETE_SOURCE_NO_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

