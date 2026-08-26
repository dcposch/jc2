#!/usr/bin/env python3
"""AWS-only compiler for a fixed-load order-two invariant quotient probe."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = (
    ROOT
    / "cases/max12_812_order2_u2_62_strict_rees_20260825"
    / "aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
)
DESIGN = ROOT / "xmodel/max12-812-order2-invariant-quotient-probe-design-20260826.md"
EXPECTED_TAILS = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
EXPECTED_DESIGN = "406d4922e2704e93af18ec1ed561784f28639558076072bb0e6a09eefe5d513e"
NAMES = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]
LOADS = {"k10": 2, "k6": 3, "k2": 5}
TARGETS = {1: 0, 2: 7, 3: 0, 4: 11, 5: 0, 6: 13}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only quotient compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only quotient compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def tail_text(entries: list[list[object]], ell: int) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != len(NAMES):
            fail(("monomial length", ell, monomial))
        if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
            fail(("nonlinear load monomial", ell, monomial))
        if sum(a * b for a, b in zip(monomial, WEIGHTS)) != 12 + ell:
            fail(("tail weight", ell, monomial))
        odd_parity = sum(monomial[i] for i in (1, 3, 5)) % 2
        if odd_parity != ell % 2:
            fail(("deck parity", ell, monomial))
        coefficient = Fraction(str(raw_coefficient))
        for offset, name in enumerate(NAMES[7:]):
            coefficient *= LOADS[name] ** monomial[7 + offset]
        factors: list[str] = []
        for i, exponent in enumerate(monomial[:7]):
            if exponent:
                factors.append(f"a{i}" if exponent == 1 else f"a{i}^{exponent}")
        body = "*".join(factors) or "1"
        if coefficient == 1 and factors:
            term = body
        elif coefficient == -1 and factors:
            term = "-" + body
        else:
            term = f"{rational_text(coefficient)}*{body}" if factors else rational_text(coefficient)
        terms.append(term)
    return "+".join(terms).replace("+-", "-") if terms else "0"


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: compile_probe.py OUTPUT_DIRECTORY")
    tag = require_aws()
    if digest(TAILS) != EXPECTED_TAILS or digest(DESIGN) != EXPECTED_DESIGN:
        fail("frozen source mismatch")
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = Path(sys.argv[1]).resolve()
    output.mkdir(parents=True, exist_ok=False)
    expressions = {ell: tail_text(tails[str(ell)], ell) for ell in range(1, 8)}
    lines = [
        'LIB "elim.lib";',
        'LIB "primdec.lib";',
        "ring R=32003,(a0,a1,a2,a3,a4,a5,a6,s,t),(dp(7),dp(2));",
        'print("ORDER2_QUOTIENT_SOURCE=PASS");',
        'print("ORDER2_QUOTIENT_LOADS=2,3,5,7,11,13");',
    ]
    for ell in range(1, 8):
        lines.append(f"poly r{ell}={expressions[ell]};")
    lines.extend([
        "ideal I=r1,r2-7,r3,r4-11,r5,r6-13;",
        "int sym_ok=1;",
    ])
    for ell in range(1, 8):
        sign = -1 if ell % 2 else 1
        lines.extend([
            f"poly sr{ell}=subst(subst(subst(r{ell},a1,-a1),a3,-a3),a5,-a5);",
            f"if (sr{ell}-({sign})*r{ell} != 0) {{ sym_ok=0; }}",
        ])
    lines.extend([
        'print("ORDER2_QUOTIENT_DECK_PARITY="+string(sym_ok));',
        'if (sym_ok!=1) { print("ORDER2_QUOTIENT_FAIL=DECK_PARITY"); quit(81); }',
        'print("ORDER2_QUOTIENT_SAT_START");',
        "ideal J=sat(I,ideal(r7));",
        "J=std(J);",
        'print("ORDER2_QUOTIENT_SAT_DONE");',
        'print("ORDER2_QUOTIENT_J_SIZE="+string(size(J)));',
        'print("ORDER2_QUOTIENT_J_DIM="+string(dim(J)));',
        "int sat_sym_ok=1;",
        "for (int ii=1; ii<=size(J); ii++) {",
        "  poly sj=subst(subst(subst(J[ii],a1,-a1),a3,-a3),a5,-a5);",
        "  if (reduce(sj,J)!=0) { sat_sym_ok=0; }",
        "}",
        'print("ORDER2_QUOTIENT_SAT_DECK_STABLE="+string(sat_sym_ok));',
        'if (sat_sym_ok!=1) { print("ORDER2_QUOTIENT_FAIL=SAT_DECK_STABILITY"); quit(82); }',
        "ideal fixed=J,a1,a3,a5;",
        "fixed=std(fixed);",
        'print("ORDER2_QUOTIENT_FIXED_SIZE="+string(size(fixed)));',
        'print("ORDER2_QUOTIENT_FIXED_DIM="+string(dim(fixed)));',
        "poly Sinv=a6+2*a4+3*a2+5*a0+a1^2+2*a1*a3+3*a1*a5+5*a3^2+7*a3*a5+11*a5^2;",
        "poly Tinv=2*a6-3*a4+5*a2-7*a0+13*a1^2-11*a1*a3+7*a1*a5+5*a3^2-3*a3*a5+2*a5^2;",
        "ideal graph=J,s-Sinv,t-Tinv;",
        'print("ORDER2_QUOTIENT_ELIM_START");',
        "ideal plane=eliminate(graph,a0*a1*a2*a3*a4*a5*a6);",
        "plane=std(plane);",
        'print("ORDER2_QUOTIENT_ELIM_DONE");',
        'print("ORDER2_QUOTIENT_PLANE_SIZE="+string(size(plane)));',
        'print("ORDER2_QUOTIENT_PLANE_DIM="+string(dim(plane)));',
        'if (size(plane)==1) {',
        '  list PF=factorize(plane[1],1);',
        '  print("ORDER2_QUOTIENT_PLANE_FACTOR_COUNT="+string(size(PF[1])));',
        '  print("ORDER2_QUOTIENT_PLANE_POLY");',
        '  print(plane[1]);',
        '}',
        'print("ORDER2_QUOTIENT_PROBE_ENDPOINT=PASS");',
        "quit;",
    ])
    singular = output / "order2_invariant_quotient_p32003.sing"
    singular.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "PASS-ORDER2-INVARIANT-QUOTIENT-PROBE-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": 32003,
        "loads": [2, 3, 5, 7, 11, 13],
        "tails_sha256": digest(TAILS),
        "design_sha256": digest(DESIGN),
        "input_sha256": digest(singular),
        "scope": "NAVIGATION_ONLY_NO_GENUS_NO_SOURCE_ELIMINATION",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
