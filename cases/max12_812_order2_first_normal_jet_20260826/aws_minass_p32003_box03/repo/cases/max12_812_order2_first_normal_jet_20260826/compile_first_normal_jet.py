#!/usr/bin/env python3
"""AWS-only compiler for the exact first normal/divisibility jet."""

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
TAILS = (
    ROOT
    / "cases/max12_812_order2_u2_62_strict_rees_20260825"
    / "aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
)
THEOREM = ROOT / "xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"
SOURCE_AUDIT = ROOT / "xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md"
SOURCE_ERRATUM = ROOT / "xmodel/max12-812-order24-coefficient-infinity-source-audit-erratum-v2-20260825.md"
EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    THEOREM: "827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc",
    ONEPARAM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    SOURCE_AUDIT: "092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e",
    SOURCE_ERRATUM: "aa90155ec8a182f4f451c77fc9548cf8035889efc230afdaea622f84eb18c495",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
NAMES = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]
LOAD_LAMBDA_WEIGHTS = [2, 6, 10]
CEXPR = {
    0: "(r^2+Lambda*n0)",
    1: "(2*c*r+Lambda*n1)",
    2: "(c^2+2*p*r+Lambda*n2)",
    3: "(2*p*c+Lambda*n3)",
    4: "(p^2+2*r)",
    5: "(2*c)",
    6: "(2*p)",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only first-normal compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only first-normal compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def term_text(monomial: list[int], coefficient: Fraction) -> str:
    factors: list[str] = []
    for i, exponent in enumerate(monomial[:7]):
        if exponent == 1:
            factors.append(CEXPR[i])
        elif exponent:
            factors.append(f"{CEXPR[i]}^{exponent}")
    lambda_power = 0
    for offset, exponent in enumerate(monomial[7:]):
        if exponent:
            name = NAMES[7 + offset]
            factors.append(name if exponent == 1 else f"{name}^{exponent}")
            lambda_power += LOAD_LAMBDA_WEIGHTS[offset] * exponent
    if lambda_power:
        factors.append("Lambda" if lambda_power == 1 else f"Lambda^{lambda_power}")
    body = "*".join(factors) or "1"
    if coefficient == 1 and factors:
        return body
    if coefficient == -1 and factors:
        return "-" + body
    return f"{rational_text(coefficient)}*{body}" if factors else rational_text(coefficient)


def tail_text(entries: list[list[object]], ell: int) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != len(NAMES):
            fail(("monomial length", ell, monomial))
        if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
            fail(("tail is not affine-linear in lower loads", ell, monomial))
        actual_weight = sum(a * b for a, b in zip(monomial, WEIGHTS))
        if actual_weight != 12 + ell:
            fail(("tail weight", ell, actual_weight, monomial))
        terms.append(term_text(monomial, Fraction(str(raw_coefficient))))
    return "+".join(terms).replace("+-", "-") if terms else "0"


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    variables = "Lambda,p,c,r,n0,n1,n2,n3,k10,k6,k2,mu2,mu4,mu6,J"
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    lines = [
        'LIB "elim.lib";',
        'LIB "primdec.lib";',
        f"ring Rfull={characteristic},({variables}),dp;",
        'print("FIRST_NORMAL_SOURCE_HASHES=PASS");',
        'print("FIRST_NORMAL_LOAD_LINEARITY=PASS");',
        "ideal Lambda2=std(ideal(Lambda^2));",
        "int divisibility_ok=1;",
        "int identity_ok=1;",
        "int forbidden_ok=1;",
    ]
    for ell in range(1, 8):
        expression = tail_text(tails[str(ell)], ell)
        target = targets[ell]
        if target != "0":
            expression += f"-Lambda^{12 + ell}*({target})"
        lines.extend([
            f"poly Phi{ell}={expression};",
            f"if (reduce(Phi{ell},Lambda2)!=0) {{ divisibility_ok=0; }}",
            f"poly Theta{ell}=Phi{ell}/Lambda^2;",
            f"if (Lambda^2*Theta{ell}-Phi{ell}!=0) {{ identity_ok=0; }}",
            f"poly q{ell}=subst(Theta{ell},Lambda,0);",
            f"if (diff(q{ell},k6)!=0 || diff(q{ell},k2)!=0 || diff(q{ell},mu2)!=0 || diff(q{ell},mu4)!=0 || diff(q{ell},mu6)!=0 || diff(q{ell},J)!=0) {{ forbidden_ok=0; }}",
        ])
    lines.extend([
        'print("FIRST_NORMAL_LAMBDA2_DIVISIBLE="+string(divisibility_ok));',
        'print("FIRST_NORMAL_DIVISION_IDENTITY="+string(identity_ok));',
        'print("FIRST_NORMAL_FORBIDDEN_INDEPENDENCE="+string(forbidden_ok));',
        'if (divisibility_ok!=1) { print("FIRST_NORMAL_FAIL=DIVISIBILITY"); quit(81); }',
        'if (identity_ok!=1) { print("FIRST_NORMAL_FAIL=DIVISION_IDENTITY"); quit(82); }',
        'if (forbidden_ok!=1) { print("FIRST_NORMAL_FAIL=FORBIDDEN_VARIABLE"); quit(83); }',
        'print("FIRST_NORMAL_Q_BASIS_BEGIN");',
        "print(q1); print(q2); print(q3); print(q4); print(q5); print(q6); print(q7);",
        'print("FIRST_NORMAL_Q_BASIS_END");',
        "ideal Qraw=q1,q2,q3,q4,q5,q6,q7;",
        f"ring Rsmall={characteristic},(p,c,r,n0,n1,n2,n3,k10),dp;",
        "ideal Q=imap(Rfull,Qraw);",
        "Q=std(Q);",
        'print("FIRST_NORMAL_Q_STD_DONE");',
        'print("FIRST_NORMAL_Q_SIZE="+string(size(Q)));',
        'print("FIRST_NORMAL_Q_DIM="+string(dim(Q)));',
        'print("FIRST_NORMAL_K_SAT_START");',
        "ideal QK=sat(Q,ideal(p,c,r));",
        "QK=std(QK);",
        'print("FIRST_NORMAL_K_SAT_DONE");',
        'print("FIRST_NORMAL_NORMAL_SAT_START");',
        "ideal Qstar=sat(QK,ideal(n0,n1,n2,n3,k10));",
        "Qstar=std(Qstar);",
        'print("FIRST_NORMAL_NORMAL_SAT_DONE");',
        'print("FIRST_NORMAL_QSTAR_SIZE="+string(size(Qstar)));',
        'print("FIRST_NORMAL_QSTAR_DIM="+string(dim(Qstar)));',
        'int qstar_unit=(reduce(1,Qstar)==0);',
        'print("FIRST_NORMAL_QSTAR_IS_UNIT="+string(qstar_unit));',
        'if (qstar_unit==0) {',
        '  print("FIRST_NORMAL_MINASS_START");',
        '  list PA=minAssGTZ(Qstar);',
        '  print("FIRST_NORMAL_MINASS_DONE");',
        '  print("FIRST_NORMAL_MINASS_COUNT="+string(size(PA)));',
        '  for (int ai=1; ai<=size(PA); ai++) {',
        '    ideal Pai=std(PA[ai]);',
        '    print("FIRST_NORMAL_MINASS_COMPONENT="+string(ai)+",SIZE="+string(size(Pai))+",DIM="+string(dim(Pai)));',
        '  }',
        '}',
        'print("FIRST_NORMAL_ENDPOINT=PASS_NAVIGATION");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(32003, 65521), default=32003)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED.items():
        if digest(source) != expected:
            fail(("frozen source mismatch", source))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"first_normal_jet_p{args.characteristic}.sing"
    emit(singular, args.characteristic, tails)
    payload = {
        "status": "PASS-FIRST-NORMAL-JET-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "theorem_sha256": digest(THEOREM),
        "input_sha256": digest(singular),
        "scope": "FIRST_NORMAL_NAVIGATION_ONLY_NO_REES_OR_ORDER2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
