#!/usr/bin/env python3
"""Compile the correction-aware order-two K3 normalized-ray client (AWS only)."""

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
DESIGN = ROOT / "xmodel/max12-812-order2-discriminant-halfweight-k3-correction-aware-design-20260826.md"
K2_V2 = ROOT / "xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-v2-20260826.md"
RANK = ROOT / "xmodel/max12-812-order2-discriminant-rank-halfweight-kuranishi-20260826.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    DESIGN: "a2c1749993807ee9f8398d99f8e8e459d56252974a9efd6196a2c0ea89aa6ae2",
    K2_V2: "f1cbb203ca26c66c3c57178460912610ba978206043b2bf22bc1b2b73aaac68b",
    RANK: "ddbc758039621f70eae586b5482be3bfdd92754e990cdb015fa4c6d2e0eac0b1",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
NAMES = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]


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


def qtext(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def binomial(alpha: Fraction, n: int) -> Fraction:
    out = Fraction(1)
    for j in range(n):
        out *= (alpha - j) / (j + 1)
    return out


def mul(left: list[Fraction], right: list[Fraction], cap: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(cap + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= cap:
                out[i + j] += a * b
    return out


def power(base: list[Fraction], exponent: int, cap: int) -> list[Fraction]:
    out = [Fraction(1)] + [Fraction(0) for _ in range(cap)]
    for _ in range(exponent):
        out = mul(out, base, cap)
    return out


def row_transform(cap: int = 7) -> dict[tuple[int, int], Fraction]:
    # q=A/w solves q^4+x*q^3=1, x=b/w.  Then A^-j=w^-j*q^-j.
    q = [Fraction(1)] + [Fraction(0) for _ in range(cap)]
    for n in range(1, cap + 1):
        q[n] = Fraction(0)
        q4 = power(q, 4, cap)
        q3 = power(q, 3, cap)
        known = q4[n] + q3[n - 1]
        q[n] = -known / 4
    inv = [Fraction(1)] + [Fraction(0) for _ in range(cap)]
    for n in range(1, cap + 1):
        inv[n] = -sum(q[j] * inv[n - j] for j in range(1, n + 1))
    ans: dict[tuple[int, int], Fraction] = {}
    for j in range(1, cap + 1):
        invj = power(inv, j, cap)
        for ell in range(j, cap + 1):
            ans[(ell, j)] = invj[ell - j]
    return ans


def term_text(monomial: list[int], coefficient: Fraction, coeffs: dict[int, str]) -> str:
    factors: list[str] = []
    for i, exponent in enumerate(monomial[:7]):
        if exponent == 1:
            factors.append(coeffs[i])
        elif exponent:
            factors.append(f"({coeffs[i]})^{exponent}")
    loads = monomial[7:]
    if sum(loads) > 1 or any(value not in (0, 1) for value in loads):
        fail(("load nonlinearity", monomial))
    if loads[0]:
        factors.append("(sig^14*chi)")
    if loads[1]:
        factors.append("(sig^24*k6)")
    if loads[2]:
        factors.append("(sig^40*k2)")
    body = "*".join(factors) or "1"
    if coefficient == 1 and factors:
        return body
    if coefficient == -1 and factors:
        return "-" + body
    return f"{qtext(coefficient)}*{body}" if factors else qtext(coefficient)


def tail_text(entries: list[list[object]], ell: int, coeffs: dict[int, str]) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != len(NAMES):
            fail(("monomial length", ell, monomial))
        if sum(a * b for a, b in zip(monomial, WEIGHTS)) != 12 + ell:
            fail(("tail weight", ell, monomial))
        terms.append(term_text(monomial, Fraction(str(raw_coefficient)), coeffs))
    return "+".join(terms).replace("+-", "-") if terms else "0"


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    cs = {n: binomial(Fraction(5, 2), n) for n in range(11, 18)}
    bb = "(b+sig*b1)"
    tt = "(t+sig*t1)"
    qq = "(q+sig*q1)"
    ss = "(ss+sig*s1)"
    a = f"({bb}/4)"
    ee = "(sig^2*eps)"
    d = f"({ee}-3*{a}^2)"
    m0 = "(6*b*t^2)"
    m1 = "(6*b1*t^2+12*b*t*t1-6*t*xi)"
    m2 = "(12*b1*t*t1+6*b*t1^2-6*t1*xi+nu)"
    mm = f"(6*{bb}*{tt}^2-6*sig*{tt}*xi+sig^2*nu)"
    xx = f"(-2*{bb}*{tt}+sig*xi+sig^2*omega)"
    yy = f"(6*{bb}*{tt}^3)"
    minv = f"(mi-sig*{m1}*mi^2+sig^2*(({m1})^2*mi^3-{m2}*mi^2))"
    minv2 = f"(mi^2-2*sig*{m1}*mi^3+sig^2*(3*({m1})^2*mi^4-2*{m2}*mi^3))"
    c11 = f"({qtext(cs[11])}*b^11)"
    c12 = f"({qtext(cs[12])}*b^12)"
    c0 = f"(({yy})^2*{minv2}+(8/3)*(sig^2*chi)*{c12}*mi^2+sig^2*gamma)"
    s0 = f"({mm}*{qq}/2-(4/3)*(sig^2*chi)*{c11}*mi+sig^2*delta)"
    kc = qq
    kr = f"({c0}-{a}*{qq})"
    ns = ss
    nt = f"({s0}-{a}*{ss})"
    p = f"({d}-3*{a}^2)"
    c = f"(2*{a}*({a}^2-{d})+sig^2*{xx}+sig^4*{kc})"
    r = f"({a}^2*{d}-sig^2*{a}*{xx}+sig^4*{kr})"
    n3 = mm
    n2 = f"({a}*{mm})"
    n1 = f"(({d}-2*{a}^2)*{mm}+sig^2*{yy}+sig^4*{ns})"
    n0 = f"(-{a}*{d}*{mm}+sig^2*(-{a}*{yy}+{mm}*{xx}/2)+sig^4*{nt})"
    coeffs = {
        6: f"(2*{p})",
        5: f"(2*{c})",
        4: f"(({p})^2+2*{r})",
        3: f"(2*{p}*{c}+sig^4*{n3})",
        2: f"(({c})^2+2*{p}*{r}+sig^4*{n2})",
        1: f"(2*{c}*{r}+sig^4*{n1})",
        0: f"(({r})^2+sig^4*{n0})",
    }
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    transform = row_transform()
    variables = "sig,b,t,q,ss,b1,t1,q1,s1,xi,nu,omega,gamma,delta,eps,chi,mi,k6,k2,mu2,mu4,mu6,J"
    lines = [
        'LIB "elim.lib";',
        f"ring R={characteristic},({variables}),dp;",
        'print("K3NR_SOURCE_HASHES=PASS");',
        f"poly m0={m0};",
        "poly y0=6*b*t^3;",
        f"poly M={mm};",
        f"poly X={xx};",
        f"poly Y={yy};",
        f"poly MINV={minv};",
        f"poly MINV2={minv2};",
        "ideal GI=std(ideal(m0*mi-1));",
        "ideal sig3=std(ideal(sig^3,m0*mi-1));",
        "ideal sig12=std(ideal(sig^12));",
        "int inverseok=(reduce(M*MINV-1,sig3)==0 && reduce(M^2*MINV2-1,sig3)==0 && reduce(MINV^2-MINV2,sig3)==0);",
        'print("K3NR_TRUNCATED_INVERSE="+string(inverseok));',
        'if (inverseok!=1) { print("K3NR_FAIL=TRUNCATED_INVERSE"); quit; }',
        "int div12=1;",
        "int basezero=1;",
        "int kernelzero=1;",
        "int forbidden=1;",
        "int tangentfreeze=1;",
        "list SR;",
    ]
    for ell in range(1, 8):
        expression = tail_text(tails[str(ell)], ell, coeffs)
        if targets[ell] != "0":
            expression += f"-sig^{4 * (12 + ell)}*({targets[ell]})"
        lines.extend([
            f"poly Phi{ell}={expression};",
            f"if (reduce(Phi{ell},sig12)!=0) {{ div12=0; }}",
            f"poly Xi{ell}=Phi{ell}/sig^12;",
            f"poly B0_{ell}=subst(Xi{ell},sig,0);",
            f"if (reduce(B0_{ell},GI)!=0) {{ basezero=0; print(\"K3NR_BASE_REMAINDER_{ell}\"); print(reduce(B0_{ell},GI)); }}",
            f"poly X1_{ell}=(Xi{ell}-B0_{ell})/sig;",
            f"poly B1_{ell}=subst(X1_{ell},sig,0);",
            f"if (reduce(B1_{ell},GI)!=0) {{ kernelzero=0; print(\"K3NR_KERNEL_REMAINDER_{ell}\"); print(reduce(B1_{ell},GI)); }}",
            f"poly X2_{ell}=(X1_{ell}-B1_{ell})/sig;",
            f"poly S{ell}=reduce(subst(X2_{ell},sig,0),GI);",
            f"SR[{ell}]=S{ell};",
            f"if (diff(S{ell},k6)!=0 || diff(S{ell},k2)!=0 || diff(S{ell},mu2)!=0 || diff(S{ell},mu4)!=0 || diff(S{ell},mu6)!=0 || diff(S{ell},J)!=0) {{ forbidden=0; }}",
            f"if (diff(S{ell},b1)!=0 || diff(S{ell},t1)!=0 || diff(S{ell},q1)!=0 || diff(S{ell},s1)!=0) {{ tangentfreeze=0; print(\"K3NR_TANGENT_REMAINDER_{ell}\"); print(diff(S{ell},b1)); print(diff(S{ell},t1)); print(diff(S{ell},q1)); print(diff(S{ell},s1)); }}",
        ])
    lines.extend([
        'print("K3NR_SIGMA12_DIVISIBLE="+string(div12));',
        'print("K3NR_SIGMA12_BASE_ZERO="+string(basezero));',
        'print("K3NR_SIGMA13_KERNEL_ZERO="+string(kernelzero));',
        'print("K3NR_FORBIDDEN_LOW_GRADES="+string(forbidden));',
        'print("K3NR_TANGENT_FREEZE_WEIGHT2="+string(tangentfreeze));',
        'if (div12!=1 || basezero!=1 || kernelzero!=1 || forbidden!=1 || tangentfreeze!=1) { print("K3NR_FAIL=SOURCE_EXTRACTION"); quit; }',
        "poly U=M*X/2+(b+sig*b1)*Y;",
        "poly U0=subst(U,sig,0);",
        "poly UX=(U-U0)/sig;",
        "poly U1=reduce(subst(UX,sig,0),GI);",
        "poly rawU1=9*b*t^2*xi;",
        "poly FF=M^3+6*M*X*Y+6*(b+sig*b1)*Y^2;",
        "poly F0=subst(FF,sig,0);",
        "poly FX=(FF-F0)/sig;",
        "poly F1=reduce(subst(FX,sig,0),GI);",
        "poly FXX=(FX-F1)/sig;",
        "poly F2=reduce(subst(FXX,sig,0),GI);",
        "poly rawF2=36*b^2*t^4*nu+216*b^2*t^5*omega+432*b*t^4*xi^2;",
        'print("K3NR_RAW_U1_MATCH="+string(reduce(U1-rawU1,GI)==0));',
        'print("K3NR_RAW_F1_ZERO="+string(reduce(F1,GI)==0));',
        'print("K3NR_RAW_F2_MATCH="+string(reduce(F2-rawF2,GI)==0));',
        'if (reduce(U1-rawU1,GI)!=0 || reduce(F1,GI)!=0 || reduce(F2-rawF2,GI)!=0) { print("K3NR_FAIL=RAW_SCHEME"); quit; }',
        "poly W=rawU1^2;",
    ])
    for n in range(13, 18):
        lines.append(f"poly c{n}={qtext(cs[n])}*b^{n};")
    lines.extend([
        "poly L1=12*m0*delta;",
        "poly L2=-6*m0^2*gamma+72*b*t^3*ss;",
        "poly L3=-rawF2-216*b^2*t^5*q+16*chi*c13;",
        "poly L4=6*W-6*y0^2*eps-432*b^2*t^7+16*chi*c14;",
        "poly L5=-6*b*W-216*b^3*t^7+16*chi*c15;",
        "poly L6=6*b^2*W+16*chi*c16;",
        "poly L7=-6*b^3*W+16*chi*c17;",
        "list LR; LR[1]=L1; LR[2]=L2; LR[3]=L3; LR[4]=L4; LR[5]=L5; LR[6]=L6; LR[7]=L7;",
        "int rowcompare=1;",
    ])
    for ell in range(1, 8):
        terms: list[str] = []
        for j in range(1, ell + 1):
            value = transform[(ell, j)]
            if not value:
                continue
            factor = qtext(value)
            power_b = ell - j
            if power_b:
                factor += f"*b^{power_b}"
            terms.append(f"({factor})*L{j}")
        predicted = "+".join(terms).replace("+-", "-") or "0"
        lines.extend([
            f"poly P{ell}={predicted};",
            f"int cmp{ell}=(reduce(16*S{ell}-P{ell},GI)==0);",
            f"print(\"K3NR_ROW_COMPARE_{ell}=\"+string(cmp{ell}));",
            f"if (cmp{ell}!=1) {{ rowcompare=0; print(\"K3NR_ROW_REMAINDER_{ell}\"); print(reduce(16*S{ell}-P{ell},GI)); }}",
        ])
    lines.extend([
        'if (rowcompare!=1) { print("K3NR_FAIL=ROW_COMPARE"); quit; }',
        "poly rec17=c17+(27/34)*b*c16;",
        'print("K3NR_C17_RECURRENCE="+string(rec17==0));',
        "poly lastcert=b*L6+L7-16*chi*(b*c16+c17);",
        'print("K3NR_LAST3_CERTIFICATE="+string(lastcert==0));',
        'if (rec17!=0 || lastcert!=0) { print("K3NR_FAIL=LAST3_IDENTITY"); quit; }',
        "ideal IA=L1,L2,L3,L4,L5,L6,L7,m0*mi-1;",
        "ideal GA=std(IA);",
        "int analyticunit=(reduce(1,GA)==0);",
        'print("K3NR_ANALYTIC_BT_UNIT="+string(analyticunit));',
        "ideal IS=S1,S2,S3,S4,S5,S6,S7,m0*mi-1;",
        "ideal GS=std(IS);",
        "int sourceunit=(reduce(1,GS)==0);",
        'print("K3NR_SOURCE_BT_UNIT="+string(sourceunit));',
        'if (analyticunit!=1 || sourceunit!=1) { print("K3NR_FAIL=UNIT"); quit; }',
        'print("K3NR_ENDPOINT=PASS_NORMALIZED_RAY_SOURCE_UNIT");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 32003), required=True)
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
    if sorted(tails) != [str(i) for i in range(1, 8)]:
        fail("tail key mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    target = output / f"disc_k3_normalized_ray_p{args.characteristic}.sing"
    emit(target, args.characteristic, tails)
    payload = {
        "status": "PASS-K3-NORMALIZED-RAY-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "design_sha256": digest(DESIGN),
        "input_sha256": digest(target),
        "raw_k2_scheme": "(kappa,e,U^2,F)_D(bm)",
        "normalized_weights": {"U": 1, "e": 2, "kappa": 2, "F": 2},
        "scope": "EXPLICIT_SOURCE_BRANCH; EXHAUSTIVE_D_COVERAGE_WAITS_EXACT_Q_K2_PROMOTION; NO_ORDER2_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
