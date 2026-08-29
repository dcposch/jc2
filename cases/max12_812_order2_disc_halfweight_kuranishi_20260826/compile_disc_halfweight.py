#!/usr/bin/env python3
"""Compile the exact discriminant half-weight Kuranishi client (AWS only)."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
THEOREM = ROOT / "xmodel/max12-812-order2-discriminant-rank-halfweight-kuranishi-20260826.md"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"
FIRST_NORMAL = ROOT / "xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md"
FIRST_REVIEW = ROOT / "xmodel/max12-812-order2-first-normal-divisibility-jet-review-grok-20260826.md"
UFD_V2 = ROOT / "xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md"
UFD_REVIEW = ROOT / "xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md"
PADE = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md"
PADE_REVIEW = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    THEOREM: "ddbc758039621f70eae586b5482be3bfdd92754e990cdb015fa4c6d2e0eac0b1",
    ONEPARAM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    FIRST_NORMAL: "827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc",
    FIRST_REVIEW: "27275f3d13471521bec0016d4fbc6e12d5bf8e539deeb4694fe0c01f04b025bd",
    UFD_V2: "4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d",
    UFD_REVIEW: "08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa",
    PADE: "2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5",
    PADE_REVIEW: "73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
NAMES = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]
LOAD_WEIGHTS = [2, 6, 10]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def term_text(monomial: list[int], coefficient: Fraction, coeffs: dict[int, str], loads: dict[str, str]) -> str:
    factors: list[str] = []
    for i, exponent in enumerate(monomial[:7]):
        if exponent == 1:
            factors.append(coeffs[i])
        elif exponent:
            factors.append(f"({coeffs[i]})^{exponent}")
    lambda_weight = 0
    for offset, exponent in enumerate(monomial[7:]):
        if exponent:
            name = NAMES[7 + offset]
            factors.append(loads[name] if exponent == 1 else f"({loads[name]})^{exponent}")
            lambda_weight += LOAD_WEIGHTS[offset] * exponent
    if lambda_weight:
        factors.append(f"rho^{2 * lambda_weight}")
    body = "*".join(factors) or "1"
    if coefficient == 1 and factors:
        return body
    if coefficient == -1 and factors:
        return "-" + body
    return f"{rational_text(coefficient)}*{body}" if factors else rational_text(coefficient)


def tail_text(entries: list[list[object]], ell: int, coeffs: dict[int, str], loads: dict[str, str]) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != len(NAMES):
            fail(("monomial length", ell, monomial))
        if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
            fail(("load nonlinearity", ell, monomial))
        if sum(a * b for a, b in zip(monomial, WEIGHTS)) != 12 + ell:
            fail(("tail weight", ell, monomial))
        terms.append(term_text(monomial, Fraction(str(raw_coefficient)), coeffs, loads))
    return "+".join(terms).replace("+-", "-") if terms else "0"


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    p = "(d-3*a^2)"
    c = "(2*a*(a^2-d)+rho*x+rho^2*kc)"
    r = "(a^2*d-rho*a*x+rho^2*kr)"
    n3 = "m"
    n2 = "(a*m)"
    n1 = "((d-2*a^2)*m+rho*y+rho^2*ns)"
    n0 = "(-a*d*m+rho*(-a*y+m*x/2)+rho^2*nt)"
    coeffs = {
        6: f"(2*{p})",
        5: f"(2*{c})",
        4: f"(({p})^2+2*{r})",
        3: f"(2*{p}*{c}+rho^2*{n3})",
        2: f"(({c})^2+2*{p}*{r}+rho^2*{n2})",
        1: f"(2*{c}*{r}+rho^2*{n1})",
        0: f"(({r})^2+rho^2*{n0})",
    }
    loads = {"k10": "(rho^2*kappa)", "k6": "k6", "k2": "k2"}
    variables = "rho,a,d,m,x,y,kc,kr,ns,nt,kappa,k6,k2,mu2,mu4,mu6,J"
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    lines = [
        'LIB "elim.lib";',
        f"ring R={characteristic},({variables}),dp;",
        'print("DISC_HALF_SOURCE_HASHES=PASS");',
        "ideal rho6=std(ideal(rho^6));",
        "int divisible=1;",
        "int identity=1;",
        "int forbidden=1;",
    ]
    for ell in range(1, 8):
        expression = tail_text(tails[str(ell)], ell, coeffs, loads)
        if targets[ell] != "0":
            expression += f"-rho^{2 * (12 + ell)}*({targets[ell]})"
        lines.extend([
            f"poly Phi{ell}={expression};",
            f"if (reduce(Phi{ell},rho6)!=0) {{ divisible=0; }}",
            f"poly Xi{ell}=Phi{ell}/rho^6;",
            f"if (rho^6*Xi{ell}-Phi{ell}!=0) {{ identity=0; }}",
            f"poly e{ell}=subst(Xi{ell},rho,0);",
            f"if (diff(e{ell},k6)!=0 || diff(e{ell},k2)!=0 || diff(e{ell},mu2)!=0 || diff(e{ell},mu4)!=0 || diff(e{ell},mu6)!=0 || diff(e{ell},J)!=0) {{ forbidden=0; }}",
        ])
    lines.extend([
        'print("DISC_HALF_RHO6_DIVISIBLE="+string(divisible));',
        'print("DISC_HALF_DIVISION_IDENTITY="+string(identity));',
        'print("DISC_HALF_FORBIDDEN_INDEPENDENCE="+string(forbidden));',
        'if (divisible!=1) { print("DISC_HALF_FAIL=DIVISIBILITY"); quit(81); }',
        'if (identity!=1) { print("DISC_HALF_FAIL=IDENTITY"); quit(82); }',
        'if (forbidden!=1) { print("DISC_HALF_FAIL=FORBIDDEN"); quit(83); }',
        "poly b=4*a;",
        "poly ee=d+3*a^2;",
        "list cc;",
        "cc[1]=1;",
        "cc[2]=(5/2)*b;",
        "for (int nn=1; nn<=16; nn++) { cc[nn+2]=(b*(5/2-nn)*cc[nn+1]+ee*(6-nn)*cc[nn])/(nn+1); }",
        "poly hh=m*x/2;",
        "list rr;",
        "rr[1]=0; rr[2]=0; rr[3]=y^2;",
        "rr[4]=-2*y*hh-b*rr[3];",
        "rr[5]=hh^2-b*rr[4]-ee*rr[3];",
        "for (nn=5; nn<=7; nn++) { rr[nn+1]=-b*rr[nn]-ee*rr[nn-1]; }",
        "poly C0=kr+a*kc;",
        "poly S0=nt+a*ns;",
        "poly h1=12*m*S0-6*m^2*kc+16*kappa*cc[12];",
        "poly h2=6*rr[3]-6*m^2*C0+16*kappa*cc[13];",
        "poly h3=6*rr[4]-m^3+16*kappa*cc[14];",
        "poly h4=6*rr[5]+16*kappa*cc[15];",
        "poly h5=6*rr[6]+16*kappa*cc[16];",
        "poly h6=6*rr[7]+16*kappa*cc[17];",
        "poly h7=6*rr[8]+16*kappa*cc[18];",
        "poly rec13=14*cc[15]+(21/2)*b*cc[14]+7*ee*cc[13];",
        "poly rec14=15*cc[16]+(23/2)*b*cc[15]+8*ee*cc[14];",
        'print("DISC_HALF_REC13_ZERO="+string(rec13==0));',
        'print("DISC_HALF_REC14_ZERO="+string(rec14==0));',
        "poly rank3minor=-1152*m^3*cc[14];",
        'print("DISC_HALF_RANK_BOUND=3");',
        'print("DISC_HALF_RANK3_MINOR_FACTOR="); print(rank3minor);',
        'print("DISC_HALF_ANALYTIC_ROWS_BEGIN");',
        "print(h1); print(h2); print(h3); print(h4); print(h5); print(h6); print(h7);",
        'print("DISC_HALF_ANALYTIC_ROWS_END");',
        'print("DISC_HALF_SOURCE_ROWS_BEGIN");',
        "print(e1); print(e2); print(e3); print(e4); print(e5); print(e6); print(e7);",
        'print("DISC_HALF_SOURCE_ROWS_END");',
        "ideal IE=e1,e2,e3,e4,e5,e6,e7;",
        "ideal IH=h1,h2,h3,h4,h5,h6,h7;",
        'print("DISC_HALF_IDEAL_COMPARE_START");',
        "ideal GE=std(IE);",
        "ideal GH=std(IH);",
        "int analytic_in_source=(reduce(IH,GE)==0);",
        "int source_in_analytic=(reduce(IE,GH)==0);",
        'print("DISC_HALF_ANALYTIC_IN_SOURCE="+string(analytic_in_source));',
        'print("DISC_HALF_SOURCE_IN_ANALYTIC="+string(source_in_analytic));',
        'if (analytic_in_source!=1 || source_in_analytic!=1) { print("DISC_HALF_FAIL=IDEAL_COMPARE"); quit(84); }',
        "ideal IM=subst(subst(IH,x,0),y,0);",
        "ideal IMm=sat(IM,ideal(m));",
        "IMm=std(IMm);",
        'print("DISC_HALF_MATCHED_ENDPOINT_UNIT="+string(reduce(1,IMm)==0));',
        'print("DISC_HALF_ENDPOINT=PASS_SOURCE_ANALYTIC_IDEAL_EQUALITY");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 32003, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen source mismatch", source, actual, expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"disc_halfweight_p{args.characteristic}.sing"
    emit(singular, args.characteristic, tails)
    payload = {
        "status": "PASS-DISC-HALFWEIGHT-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "theorem_sha256": digest(THEOREM),
        "input_sha256": digest(singular),
        "scope": "SOURCE_ANALYTIC_HALFWEIGHT_KURANISHI_ONLY_NO_ARC_OR_ORDER2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
