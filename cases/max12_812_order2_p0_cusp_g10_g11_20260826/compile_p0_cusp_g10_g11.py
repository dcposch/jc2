#!/usr/bin/env python3
"""Compile the correction-aware p=0 cusp grade-10/11 source client on AWS."""

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
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
BASE_COMPILER = ROOT / "cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py"
DESIGN = ROOT / "xmodel/max12-812-order2-p0-cusp-successor-design-20260826.md"
SUCCESSOR = ROOT / "xmodel/max12-812-order2-zero-load-p0-successor-design-20260826.md"
HALF_REVIEW = ROOT / "xmodel/max12-812-order2-square-halfweight-kuranishi-hostile-review-grok-20260826.md"
SHARP_PROMOTION = ROOT / "xmodel/max12-812-order2-square-third-tail-sharp-v2-promotion-20260826.md"
ODD_PROMOTION = ROOT / "xmodel/max12-812-order2-p0-odd-grade14-unit-elimination-promotion-20260826.md"

EXPECTED_STATIC = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    BASE_COMPILER: "77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc",
    DESIGN: "04ca7018ad1609dfd11839914ecbe214cf896ad78edd661cbeecc07f18614622",
    SUCCESSOR: "4e180381670c4dcd80a05e725925d3a69b85da76c84645d5a417e4fedb801216",
    HALF_REVIEW: "49744ab901f05ae6d8f0163fd195f3b0219e725f051c3aeebf31fcdaa13c4214",
    SHARP_PROMOTION: "dfc448503b1ce05a7ef0ee21d01c0c9aaf5531c0ca6bdc9bbdf82032461d784e",
    ODD_PROMOTION: "f48401b5a5635fa8212db76ac0f9f7eea44e8904e0b1aa18a4fbbc38389d56c3",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag
    ):
        fail("p0 cusp compiler is restricted to a registered AWS EC2 lane")
    return tag


def load_base_compiler():
    spec = importlib.util.spec_from_file_location("p0_cusp_tail_base", BASE_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot load charged tail compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_coefficients() -> dict[int, str]:
    pp = "(2*sigma*ell1+2*sigma^2*ell2+2*sigma^3*ell3)"
    c = "(sigma^2*(cs+sigma*cs1+sigma^2*cs2))"
    r = f"((({pp})^2+sigma^2*(rs+sigma*rs1+sigma^2*rs2))/4)"
    az = "(a1+sigma*aa1+sigma^2*aaa1)"
    ac = "(a0+sigma*aa0+sigma^2*aaa0)"
    ez = "(c1+sigma*e1+sigma^2*ee1)"
    ec = "(c0+sigma*e0+sigma^2*ee0)"
    n3 = f"(sigma^3*({az}))"
    n2 = f"(sigma^3*({ac}))"
    n1 = f"(sigma^3*(({pp})*({az})+({ez}))/2)"
    n0 = f"(sigma^3*(({pp})*({ac})+({ec}))/2)"
    return {
        6: f"(2*({pp}))",
        5: f"(2*({c}))",
        4: f"(({pp})^2+2*({r}))",
        3: f"(2*({pp})*({c})+sigma^2*({n3}))",
        2: f"(({c})^2+2*({pp})*({r})+sigma^2*({n2}))",
        1: f"(2*({c})*({r})+sigma^2*({n1}))",
        0: f"(({r})^2+sigma^2*({n0}))",
    }


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    base = load_base_compiler()
    coeffs = source_coefficients()
    loads = {
        "k10": "(k+sigma*k1+sigma^2*k2c)",
        "k6": "(k6+sigma*k6_1)",
        "k2": "(k2+sigma*k2_1)",
    }
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    variables = (
        "sigma,z,ell1,ell2,ell3,cs,cs1,cs2,rs,rs1,rs2,"
        "a0,a1,aa0,aa1,aaa0,aaa1,c0,c1,e0,e1,ee0,ee1,"
        "k,k1,k2c,k6,k6_1,k2,k2_1,mu2,mu4,mu6,J,tau,d"
    )
    lines = [
        f"ring R={characteristic},({variables}),dp;",
        'print("P0_CUSP_G10_G11_SOURCE_HASHES=PASS");',
        "proc coeffAt(poly P,int n)",
        "{",
        "  int i; poly q=P; poly a;",
        "  for (i=0; i<n; i++) { a=subst(q,z,0); q=(q-a)/z; }",
        "  return(subst(q,z,0));",
        "}",
        "poly ExtractControl=7+11*z+13*z^2+17*z^3;",
        "int extractor=(coeffAt(ExtractControl,0)==7 && coeffAt(ExtractControl,1)==11 && coeffAt(ExtractControl,2)==13 && coeffAt(ExtractControl,3)==17);",
        'print("P0_CUSP_COEFFICIENT_EXTRACTOR_CONTROL="+string(extractor));',
        "ideal Sigma10=std(ideal(sigma^10)); ideal Sigma1=std(ideal(sigma));",
        "int div10=1; int div11=1; int quotientIdentity=1; int forbidden=1;",
    ]
    for ell in range(1, 8):
        expression = base.tail_text(tails[str(ell)], ell, coeffs, loads)
        expression = expression.replace("Lambda", "(sigma^2)")
        if targets[ell] != "0":
            expression += f"-sigma^{2 * (12 + ell)}*({targets[ell]})"
        lines.extend(
            [
                f"poly Phi{ell}={expression};",
                f"if (reduce(Phi{ell},Sigma10)!=0) {{ div10=0; }}",
                f"poly Q10_{ell}=Phi{ell}/sigma^10;",
                f"if (sigma^10*Q10_{ell}-Phi{ell}!=0) {{ quotientIdentity=0; }}",
                f"poly g10_{ell}=subst(Q10_{ell},sigma,0);",
                f"poly Rem11_{ell}=Q10_{ell}-g10_{ell};",
                f"if (reduce(Rem11_{ell},Sigma1)!=0) {{ div11=0; }}",
                f"poly Q11_{ell}=Rem11_{ell}/sigma;",
                f"if (sigma*Q11_{ell}-Rem11_{ell}!=0) {{ quotientIdentity=0; }}",
                f"poly g11_{ell}=subst(Q11_{ell},sigma,0);",
                f"if (diff(g10_{ell},ell1)!=0 || diff(g10_{ell},cs1)!=0 || diff(g10_{ell},rs1)!=0 || diff(g10_{ell},aa0)!=0 || diff(g10_{ell},aa1)!=0 || diff(g10_{ell},e0)!=0 || diff(g10_{ell},e1)!=0 || diff(g10_{ell},k1)!=0) {{ forbidden=0; }}",
                f"if (diff(g11_{ell},ell2)!=0 || diff(g11_{ell},ell3)!=0 || diff(g11_{ell},cs2)!=0 || diff(g11_{ell},rs2)!=0 || diff(g11_{ell},aaa0)!=0 || diff(g11_{ell},aaa1)!=0 || diff(g11_{ell},ee0)!=0 || diff(g11_{ell},ee1)!=0 || diff(g11_{ell},k2c)!=0) {{ forbidden=0; }}",
                f"if (diff(g10_{ell},k6)!=0 || diff(g10_{ell},k2)!=0 || diff(g10_{ell},mu2)!=0 || diff(g10_{ell},mu4)!=0 || diff(g10_{ell},mu6)!=0 || diff(g10_{ell},J)!=0) {{ forbidden=0; }}",
                f"if (diff(g11_{ell},k6)!=0 || diff(g11_{ell},k2)!=0 || diff(g11_{ell},mu2)!=0 || diff(g11_{ell},mu4)!=0 || diff(g11_{ell},mu6)!=0 || diff(g11_{ell},J)!=0) {{ forbidden=0; }}",
            ]
        )
    lines.extend(
        [
            'print("P0_CUSP_G10_DIVISIBLE="+string(div10));',
            'print("P0_CUSP_G11_DIVISIBLE="+string(div11));',
            'print("P0_CUSP_QUOTIENT_IDENTITIES="+string(quotientIdentity));',
            'print("P0_CUSP_FORBIDDEN_LATER_VARIABLES="+string(forbidden));',
            "if (extractor*div10*div11*quotientIdentity*forbidden!=1) { print(\"P0_CUSP_FAIL=SOURCE_EXTRACTION\"); quit; }",
            "poly A0=a1*z+a0; poly A1=aa1*z+aa0;",
            "poly C0=(c1*z+c0)/2; poly C1=(e1*z+e0)/2;",
            "poly R0=cs*z+rs/4; poly R1=cs1*z+rs1/4;",
            "poly D0=z^2*A0+C0; poly D1bar=z^2*A1+C1;",
            "poly Num10=(3/8)*D0^2+(5/16)*k*R0^3*z^2;",
            "poly Num11=(3/4)*D0*D1bar*z^2-(3/4)*ell1*D0*C0",
            " +(5/8)*k*D0*R0*z^4+(5/16)*k1*R0^3*z^4",
            " +(15/16)*k*R0^2*R1*z^4-(5/16)*k*ell1*R0^3*z^2;",
        ]
    )
    for ell in range(1, 8):
        h10 = f"coeffAt(Num10,{4 - ell})" if ell <= 4 else "0"
        h11 = f"coeffAt(Num11,{6 - ell})" if ell <= 6 else "0"
        prediction = h11
        if ell >= 3 and ell - 2 <= 4:
            prediction += f"+(({ell - 2})*ell1/2)*h10_{ell - 2}"
        lines.extend(
            [
                f"poly h10_{ell}={h10};",
                f"poly h11_{ell}={h11};",
                f"poly Check10_{ell}=g10_{ell}-h10_{ell};",
                f"poly Check11_{ell}=g11_{ell}-({prediction});",
                f"if (Check10_{ell}!=0) {{ print(\"P0_CUSP_CHECK10_{ell}\"); print(Check10_{ell}); }}",
                f"if (Check11_{ell}!=0) {{ print(\"P0_CUSP_CHECK11_{ell}\"); print(Check11_{ell}); }}",
            ]
        )
    lines.extend(
        [
            "int rows10=1; int rows11=1;",
            "if (Check10_1!=0 || Check10_2!=0 || Check10_3!=0 || Check10_4!=0 || Check10_5!=0 || Check10_6!=0 || Check10_7!=0) { rows10=0; }",
            "if (Check11_1!=0 || Check11_2!=0 || Check11_3!=0 || Check11_4!=0 || Check11_5!=0 || Check11_6!=0 || Check11_7!=0) { rows11=0; }",
            'print("P0_CUSP_G10_ANALYTIC_ROWS="+string(rows10));',
            'print("P0_CUSP_G11_ANALYTIC_ROWS="+string(rows11));',
            "poly Raw1=(15/256)*k*cs*rs^2+(3/8)*(a1*c0+a0*c1);",
            "poly Raw2=(5/1024)*k*rs^3+(3/8)*a0*c0+(3/32)*c1^2;",
            "poly Raw3=(3/16)*c0*c1; poly Raw4=(3/32)*c0^2;",
            "int rawRows=(g10_1==Raw1 && g10_2==Raw2 && g10_3==Raw3 && g10_4==Raw4 && g10_5==0 && g10_6==0 && g10_7==0);",
            'print("P0_CUSP_G10_LITERAL_RAW_ROWS="+string(rawRows));',
            "poly H2=c1^2+4*a0*c0+(5/96)*k*rs^3;",
            "poly C0Derivation=c0*H2-c1*(c0*c1)-4*a0*c0^2-(5/96)*k*rs^3*c0;",
            "int rawLocalization=(C0Derivation==0);",
            'print("P0_CUSP_RAW_C0_LOCALIZATION_IDENTITY="+string(rawLocalization));',
            "proc cuspNorm(poly P)",
            "{",
            "  P=subst(P,c0,0);",
            "  P=subst(P,rs,-(96/5)*k*tau^2);",
            "  P=subst(P,c1,(96/5)*k^2*tau^3);",
            "  P=subst(P,a0,k*tau*d);",
            "  P=subst(P,cs,-d/3);",
            "  return(P);",
            "}",
            "poly CuspH=5*k*rs^3+96*c1^2;",
            "poly CuspG=15*k*cs*rs^2+96*a0*c1;",
            "poly InvTau=c1+k*rs*tau; poly InvA=a0-k*tau*d; poly InvD=3*cs+d;",
            "int norm=(cuspNorm(CuspH)==0 && cuspNorm(CuspG)==0 && cuspNorm(InvTau)==0 && cuspNorm(InvA)==0 && cuspNorm(InvD)==0);",
            'print("P0_CUSP_NORMALIZATION_AND_INVERSE_IDENTITIES="+string(norm));',
            "int normGrade10=1;",
            "if (cuspNorm(g10_1)!=0 || cuspNorm(g10_2)!=0 || cuspNorm(g10_3)!=0 || cuspNorm(g10_4)!=0 || cuspNorm(g10_5)!=0 || cuspNorm(g10_6)!=0 || cuspNorm(g10_7)!=0) { normGrade10=0; }",
            'print("P0_CUSP_NORMALIZED_G10_ZERO="+string(normGrade10));',
            "poly N4=cuspNorm(g11_4);",
            "poly N3=subst(cuspNorm(g11_3),ell1,0);",
            "poly N2=subst(subst(cuspNorm(g11_2),ell1,0),e0,0);",
            "poly E1sol=(48/5)*k*k1*tau^3-(3/2)*k*tau*rs1;",
            "poly N1=subst(subst(subst(cuspNorm(g11_1),ell1,0),e0,0),e1,E1sol);",
            "poly Qe1=e1-E1sol;",
            "poly Qaa=tau*aa0-(1/2)*k1*tau^2*d+(5/192)*d*rs1-4*k^2*tau^3+3*k*tau^2*cs1;",
            "int pivots=(N4==-(864/25)*k^4*tau^6*ell1",
            " && N3==(18/5)*k^2*tau^3*e0",
            " && N2==(18/5)*k^2*tau^3*Qe1",
            " && N1==(36/5)*k^2*tau^2*Qaa);",
            'print("P0_CUSP_G11_FOUR_UNIT_PIVOTS="+string(pivots));',
            "int highZero=(cuspNorm(g11_5)==0 && cuspNorm(g11_6)==0 && cuspNorm(g11_7)==0);",
            'print("P0_CUSP_G11_HIGH_ROWS_ZERO="+string(highZero));',
            "if (rows10*rows11*rawRows*rawLocalization*norm*normGrade10*pivots*highZero!=1) { print(\"P0_CUSP_FAIL=ROW_OR_CHART_IDENTITY\"); quit; }",
            'print("P0_CUSP_G10_G11_ENDPOINT=PASS_EXACT_SOURCE_RAW_CHART_AND_TRIANGULAR_PROLONGATION");',
            "quit;",
        ]
    )
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED_STATIC.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen source mismatch", str(source), actual, expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"p0_cusp_g10_g11_{label}.sing"
    emit(singular, args.characteristic, tails)
    payload = {
        "status": "PASS-P0-CUSP-G10-G11-COMPILER",
        "scope": "P0_D_RS_K0_CUSP_GRADES_10_11_ONLY_NO_G12_TERMINAL_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "design_sha256": digest(DESIGN),
        "input_sha256": digest(singular),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
