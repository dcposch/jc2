#!/usr/bin/env python3
"""Compile exact-source receivers for r=1 and the symbolic d=1 AC subcone."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import math
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_20260826/compile_cge3_universal.py"
V1_FREEZE = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_20260826/FREEZE.sha256"
LOWCONTACT = ROOT / "cases/max12_812_order2_square_owner_lowcontact_c1_c2_v4_localized_delta_20260826/RESULT.md"
AC_MEMO = ROOT / "xmodel/max12-812-order2-square-small-ac-face-residue-lemma-20260826.md"
HULL = ROOT / "xmodel/max12-812-order2-square-fan-lower-hull-reduction-20260826.md"
CLOSURE = ROOT / "xmodel/max12-812-order2-square-contact-raising-closure-criterion-20260826.md"

PINS = {
    V1: "352ad4f2d10df80e7edcc5179a8c46dfc55b4f7ce07762fb06d2109a9da1da23",
    V1_FREEZE: "a5efc70c73fb1539086b58bc386a26815e9edb754c50eee505ab8f0918d18169",
    LOWCONTACT: "b8ae74e5ca69b50ee346c2a11acf3282bf68bd42522fa9a10bab537d7ab14e7d",
    AC_MEMO: "3a81fe720d278f14b17d78b088258873198584a2e39fbd496f1ee8822b2cc36e",
    HULL: "c9ecfe4000092912464e29ecc526ac5c065f950778d31cac81f58fe06622954d",
    CLOSURE: "3c0a33ceddfad8ca69afb145ae5249f0d2b4866c5a8af498d257e9d4a78cfd95",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    spec = importlib.util.spec_from_file_location("square_cge3_frozen", V1)
    if spec is None or spec.loader is None:
        fail("cannot load frozen source compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_coefficients(pp: str, az: str, ac: str, cz: str, cc: str,
                        rz: str, rc: str) -> dict[int, str]:
    """Exact coefficient substitution for K=L^2+sigma^2 R, D=LA+C.

    az/ac are the two coefficients of A, cz/cc those of C, and rz/rc
    those of R.  Unlike the older emitter, C and R use direct polynomial
    coefficients, so the factors 2 and 4 are inserted here.
    """

    kc = f"(sigma^2*({rz}))"
    kr = f"((({pp})^2)/4+sigma^2*({rc}))"
    n3 = f"(sigma^3*({az}))"
    n2 = f"(sigma^3*({ac}))"
    n1 = f"(sigma^3*((({pp})*({az}))/2+({cz})))"
    n0 = f"(sigma^3*((({pp})*({ac}))/2+({cc})))"
    return {
        6: f"(2*({pp}))",
        5: f"(2*({kc}))",
        4: f"(({pp})^2+2*({kr}))",
        3: f"(2*({pp})*({kc})+sigma^2*({n3}))",
        2: f"(({kc})^2+2*({pp})*({kr})+sigma^2*({n2}))",
        1: f"(2*({kc})*({kr})+sigma^2*({n1}))",
        0: f"(({kr})^2+sigma^2*({n0}))",
    }


def extraction(lines: list[str], prefix: str, base, tails, coeffs,
               loads, minimum: int, maximum: int) -> None:
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    lines.extend([
        f"ideal {prefix}Sigma=std(ideal(sigma^{minimum}));",
        f"ideal {prefix}Sigma1=std(ideal(sigma));",
        f"int {prefix}divisible=1; int {prefix}identities=1; int {prefix}forbidden=1;",
    ])
    for row in range(1, 8):
        expression = base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
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
            for variable in ("k6", "k2load", "mu2", "mu4", "mu6", "J"):
                lines.append(f"if (diff({gname},{variable})!=0) {{ {prefix}forbidden=0; }}")
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
        f'print("{prefix}SOURCE_FORBIDDEN="+string({prefix}forbidden));',
        f'if ({prefix}divisible*{prefix}identities*{prefix}forbidden!=1) {{ print("{prefix}FAIL=SOURCE_EXTRACTION"); quit; }}',
    ])


def analytic_extract(lines: list[str], prefix: str, hshift: str,
                     minimum: int, maximum: int) -> None:
    lines.extend([
        f"poly {prefix}Hshift={hshift};",
        f"int {prefix}analyticDiv=1;",
        f"if (reduce({prefix}Hshift,{prefix}Sigma)!=0) {{ {prefix}analyticDiv=0; }}",
        f"poly {prefix}HQ{minimum}={prefix}Hshift/sigma^{minimum};",
    ])
    for grade in range(minimum, maximum + 1):
        qname = f"{prefix}HQ{grade}"
        hname = f"{prefix}H{grade}"
        lines.append(f"poly {hname}=subst({qname},sigma,0);")
        if grade < maximum:
            rem = f"{prefix}HRem{grade + 1}"
            nxt = f"{prefix}HQ{grade + 1}"
            lines.extend([
                f"poly {rem}={qname}-{hname};",
                f"if (reduce({rem},{prefix}Sigma1)!=0) {{ {prefix}analyticDiv=0; }}",
                f"poly {nxt}={rem}/sigma;",
            ])
    for grade in range(minimum, maximum + 1):
        lines.append(f"poly {prefix}D{grade}_0={prefix}H{grade};")
    for derivative in range(1, 9):
        factorial = math.factorial(derivative)
        for grade in range(minimum, maximum + 1):
            lines.append(f"poly {prefix}D{grade}_{derivative}=diff({prefix}D{grade}_{derivative - 1},t);")
            if derivative >= 2:
                row = derivative - 1
                lines.append(
                    f"poly {prefix}h{grade}_{row}=subst({prefix}D{grade}_{derivative},t,0)/{factorial};"
                )
    lines.append(f'print("{prefix}ANALYTIC_DIVISIBLE="+string({prefix}analyticDiv));')


def row_checks(lines: list[str], prefix: str, v1, minimum: int, maximum: int) -> None:
    for grade in range(minimum, maximum + 1):
        lines.append(f"int {prefix}row{grade}=1;")
        offset = grade - minimum
        for i in range(1, 8):
            summands: list[str] = []
            for j in range(1, i + 1):
                t0, t1, t2 = v1.transform_series(i, j)
                if t0 != "0":
                    summands.append(f"({t0})*{prefix}h{grade}_{j}")
                if offset >= 1 and t1 != "0":
                    summands.append(f"({t1})*{prefix}h{grade - 1}_{j}")
                if offset >= 2 and t2 != "0":
                    summands.append(f"({t2})*{prefix}h{grade - 2}_{j}")
            predicted = "+".join(summands).replace("+-", "-") or "0"
            lines.extend([
                f"poly {prefix}Check{grade}_{i}={prefix}g{grade}_{i}-({predicted});",
                f"if ({prefix}Check{grade}_{i}!=0) {{ {prefix}row{grade}=0; print(\"{prefix}ROW_REMAINDER_{grade}_{i}\"); print({prefix}Check{grade}_{i}); }}",
            ])
        lines.append(f'print("{prefix}ROW_IDENTITIES_{grade}="+string({prefix}row{grade}));')


def universal_hshift(A: str, C: str, B: str, k: str, inv1: str,
                     inv2: str, inv3: str) -> str:
    return (
        f"(3/4)*sigma^10*t*({A})*({C})*({inv1})"
        f"+(3/8)*sigma^10*t^3*({C})^2*({inv2})"
        f"-(3/8)*sigma^12*t^2*({B})*({A})^2*({inv2})"
        f"-(1/16)*sigma^15*t^4*({A})^3*({inv3})"
        f"+(5/16)*sigma^10*({k})*({B})^3*({inv1})"
        f"+(5/8)*sigma^11*t*({k})*({B})*({C})*({inv1})"
        f"-(5/32)*sigma^13*t^2*({k})*({B})^2*({A})*({inv2})"
        f"+(5/32)*sigma^14*t*({k})*({A})^2*({inv1})"
    )


def r1_section(characteristic: int, v1, base, tails) -> list[str]:
    variables = (
        "z,t,sigma,p,a0,a1,c0,c1,b0,b1,k0,k6,k2load,mu2,mu4,mu6,J,inv"
    )
    lines = [
        f"ring Rr1={characteristic},({variables}),dp;",
        'print("R1_SOURCE_HASHES=PASS");',
    ]
    pp = "p"
    az = "sigma*a1"
    ac = "sigma*a0"
    cz = "sigma^3*c1"
    cc = "sigma^3*c0"
    rz = "sigma*b1"
    rc = "sigma*b0"
    coeffs = source_coefficients(pp, az, ac, cz, cc, rz, rc)
    loads = {"k10": "k0", "k6": "k6", "k2": "k2load"}
    extraction(lines, "R1_", base, tails, coeffs, loads, 13, 13)
    inv1 = "(1-(p/2)*t^2+(p/2)^2*t^4-(p/2)^3*t^6+(p/2)^4*t^8)"
    A = "sigma*(a1+a0*t)"
    C = "sigma^3*(c1+c0*t)"
    B = "sigma*(b1+b0*t)"
    hshift = universal_hshift(A, C, B, "k0", inv1, "1", "1")
    analytic_extract(lines, "R1_", hshift, 13, 13)
    row_checks(lines, "R1_", v1, 13, 13)
    lines.extend([
        "poly R1_L=z^2+p/2;",
        "poly R1_R=b1*z+b0;",
        "poly R1_N=R1_h13_1*z+R1_h13_2;",
        "int R1_rec=1;",
        "if (R1_h13_3+(p/2)*R1_h13_1!=0) { R1_rec=0; }",
        "if (R1_h13_4+(p/2)*R1_h13_2!=0) { R1_rec=0; }",
        "if (R1_h13_5+(p/2)*R1_h13_3!=0) { R1_rec=0; }",
        "if (R1_h13_6+(p/2)*R1_h13_4!=0) { R1_rec=0; }",
        "if (R1_h13_7+(p/2)*R1_h13_5!=0) { R1_rec=0; }",
        "ideal R1_GL=std(ideal(R1_L));",
        "int R1_num=(reduce(R1_N-(5/16)*k0*R1_R^3,R1_GL)==0);",
        'print("R1_DENOMINATOR_RECURRENCE="+string(R1_rec));',
        'print("R1_NUMERATOR_IDENTITY="+string(R1_num));',
        'LIB "primdec.lib";',
        "poly R1_rem=reduce(R1_R^3,R1_GL);",
        "poly R1_e1=diff(R1_rem,z); poly R1_e0=subst(R1_rem,z,0);",
        "ideal R1_I=std(ideal(R1_e0,R1_e1,inv*p*k0-1));",
        "ideal R1_rad=radical(R1_I);",
        "int R1_support=(reduce(b0,R1_rad)==0 && reduce(b1,R1_rad)==0 && size(R1_rad[1])>0);",
        'print("R1_LOCALIZED_REDUCED_SUPPORT_ZERO="+string(R1_support));',
        "if (R1_divisible*R1_identities*R1_forbidden*R1_analyticDiv*R1_row13*R1_rec*R1_num*R1_support!=1) { print(\"R1_FAIL=BRIDGE_OR_SUPPORT\"); quit; }",
        'print("R1_ENDPOINT=PASS_R1_LEADING_SECTION_ZERO_ON_DPK");',
    ])
    return lines


def d1_section(characteristic: int, v1, base, tails) -> list[str]:
    variables = (
        "z,t,sigma,p,ell1,theta,eta,a0,a1,aa0,aa1,c0,c1,cc0,cc1,"
        "b0,b1,k0,k6,k2load,mu2,mu4,mu6,J,lam,au,cv"
    )
    lines = [
        f"ring Rd1={characteristic},({variables}),dp;",
        'print("D1AC_SOURCE_HASHES=PASS");',
    ]
    pp = "(p+2*sigma*ell1)"
    az = "(sigma^2*theta*(a1+sigma*aa1))"
    ac = "(sigma^2*theta*(a0+sigma*aa0))"
    cz = "(sigma^3*theta*(c1+sigma*cc1))"
    cc = "(sigma^3*theta*(c0+sigma*cc0))"
    rz = "(sigma^2*theta*eta*b1)"
    rc = "(sigma^2*theta*eta*b0)"
    coeffs = source_coefficients(pp, az, ac, cz, cc, rz, rc)
    loads = {"k10": "k0", "k6": "k6", "k2": "k2load"}
    extraction(lines, "D1AC_", base, tails, coeffs, loads, 15, 16)
    lines.extend([
        "poly D1AC_sp=p/2+sigma*ell1;",
        "poly D1AC_Inv1=1-D1AC_sp*t^2+D1AC_sp^2*t^4-D1AC_sp^3*t^6+D1AC_sp^4*t^8;",
        "poly D1AC_Inv2=1-2*D1AC_sp*t^2+3*D1AC_sp^2*t^4-4*D1AC_sp^3*t^6+5*D1AC_sp^4*t^8;",
        "poly D1AC_Inv3=1-3*D1AC_sp*t^2+6*D1AC_sp^2*t^4-10*D1AC_sp^3*t^6+15*D1AC_sp^4*t^8;",
    ])
    A = "sigma^2*theta*((a1+a0*t)+sigma*(aa1+aa0*t))"
    C = "sigma^3*theta*((c1+c0*t)+sigma*(cc1+cc0*t))"
    B = "sigma^2*theta*eta*(b1+b0*t)"
    hshift = universal_hshift(A, C, B, "k0", "D1AC_Inv1", "D1AC_Inv2", "D1AC_Inv3")
    analytic_extract(lines, "D1AC_", hshift, 15, 16)
    row_checks(lines, "D1AC_", v1, 15, 16)
    lines.extend([
        "poly D1AC_H15unit=subst(D1AC_H15,theta,1);",
        "poly D1AC_H16base=subst(subst(D1AC_H16,theta,1),eta,0);",
        "poly D1AC_H16rc=subst(subst(diff(D1AC_H16,eta),eta,0),theta,1);",
        "poly D1AC_deta1=diff(D1AC_H16,eta); poly D1AC_deta2=diff(D1AC_deta1,eta); poly D1AC_deta3=diff(D1AC_deta2,eta);",
        "poly D1AC_H16r3=subst(subst(D1AC_deta3,eta,0),theta,1)/6;",
        "int D1AC_scale15=(D1AC_H15-theta^2*D1AC_H15unit==0);",
        "int D1AC_scale16=(D1AC_H16-theta^2*D1AC_H16base-theta^2*eta*D1AC_H16rc-theta^3*eta^3*D1AC_H16r3==0);",
        'print("D1AC_SYMBOLIC_SHIFT_G15="+string(D1AC_scale15));',
        'print("D1AC_SYMBOLIC_SHIFT_G16_THREE_MODULES="+string(D1AC_scale16));',
        "poly D1AC_N15=D1AC_h15_1*z+D1AC_h15_2;",
        "int D1AC_rec15=1;",
        "if (D1AC_h15_3+(p/2)*D1AC_h15_1!=0) { D1AC_rec15=0; }",
        "if (D1AC_h15_4+(p/2)*D1AC_h15_2!=0) { D1AC_rec15=0; }",
        "if (D1AC_h15_5+(p/2)*D1AC_h15_3!=0) { D1AC_rec15=0; }",
        "if (D1AC_h15_6+(p/2)*D1AC_h15_4!=0) { D1AC_rec15=0; }",
        "if (D1AC_h15_7+(p/2)*D1AC_h15_5!=0) { D1AC_rec15=0; }",
        "poly D1AC_N16=D1AC_h16_1*z^3+D1AC_h16_2*z^2+(D1AC_h16_3+p*D1AC_h16_1)*z+(D1AC_h16_4+p*D1AC_h16_2);",
        "int D1AC_rec16=1;",
        "if (D1AC_h16_5+p*D1AC_h16_3+(p^2/4)*D1AC_h16_1!=0) { D1AC_rec16=0; }",
        "if (D1AC_h16_6+p*D1AC_h16_4+(p^2/4)*D1AC_h16_2!=0) { D1AC_rec16=0; }",
        "if (D1AC_h16_7+p*D1AC_h16_5+(p^2/4)*D1AC_h16_3!=0) { D1AC_rec16=0; }",
        "poly D1AC_or15=D1AC_N15;",
        "D1AC_or15=subst(D1AC_or15,p,-2*lam^2); D1AC_or15=subst(D1AC_or15,a1,au); D1AC_or15=subst(D1AC_or15,a0,-au*lam); D1AC_or15=subst(D1AC_or15,c1,cv); D1AC_or15=subst(D1AC_or15,c0,cv*lam);",
        "poly D1AC_or16=D1AC_N16;",
        "D1AC_or16=subst(D1AC_or16,p,-2*lam^2); D1AC_or16=subst(D1AC_or16,a1,au); D1AC_or16=subst(D1AC_or16,a0,-au*lam); D1AC_or16=subst(D1AC_or16,c1,cv); D1AC_or16=subst(D1AC_or16,c0,cv*lam);",
        "poly D1AC_resplus=subst(D1AC_or16,z,lam);",
        "poly D1AC_sw15=D1AC_N15;",
        "D1AC_sw15=subst(D1AC_sw15,p,-2*lam^2); D1AC_sw15=subst(D1AC_sw15,a1,au); D1AC_sw15=subst(D1AC_sw15,a0,au*lam); D1AC_sw15=subst(D1AC_sw15,c1,cv); D1AC_sw15=subst(D1AC_sw15,c0,-cv*lam);",
        "poly D1AC_sw16=D1AC_N16;",
        "D1AC_sw16=subst(D1AC_sw16,p,-2*lam^2); D1AC_sw16=subst(D1AC_sw16,a1,au); D1AC_sw16=subst(D1AC_sw16,a0,au*lam); D1AC_sw16=subst(D1AC_sw16,c1,cv); D1AC_sw16=subst(D1AC_sw16,c0,-cv*lam);",
        "poly D1AC_resminus=subst(D1AC_sw16,z,-lam);",
        "int D1AC_orient=(D1AC_or15==0 && D1AC_sw15==0);",
        "int D1AC_residue=(D1AC_resplus-(3/2)*lam^2*cv^2*theta^2==0 && D1AC_resminus-(3/2)*lam^2*cv^2*theta^2==0);",
        'print("D1AC_DENOMINATOR_RECURRENCE_G15="+string(D1AC_rec15));',
        'print("D1AC_DENOMINATOR_RECURRENCE_G16="+string(D1AC_rec16));',
        'print("D1AC_BOTH_ROOT_ORIENTATIONS="+string(D1AC_orient));',
        'print("D1AC_UNMATCHED_DOUBLE_POLE="+string(D1AC_residue));',
        "if (D1AC_divisible*D1AC_identities*D1AC_forbidden*D1AC_analyticDiv*D1AC_row15*D1AC_row16*D1AC_scale15*D1AC_scale16*D1AC_rec15*D1AC_rec16*D1AC_orient*D1AC_residue!=1) { print(\"D1AC_FAIL=BRIDGE_SHIFT_OR_RESIDUE\"); quit; }",
        'print("D1AC_ENDPOINT=PASS_SYMBOLIC_D1_UNIQUE_AC_DOUBLE_POLE_GATE");',
        'print("R1_D1_AC_PACKAGE_ENDPOINT=PASS");',
        "quit;",
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
    v1 = load_v1()
    for source, expected in v1.EXPECTED.items():
        if digest(source) != expected:
            fail(("frozen transitive source mismatch", str(source)))
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    base = v1.load_base()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_r1_d1_ac_{label}.sing"
    lines = r1_section(args.characteristic, v1, base, tails)
    lines.extend(d1_section(args.characteristic, v1, base, tails))
    target.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "PASS-R1-D1-AC-SYMBOLIC-COMPILER",
        "scope": "R1_AND_D1_UNIQUE_AC_ONLY_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1),
        "all_tails_sha256": v1.EXPECTED_ALL_TAILS,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
