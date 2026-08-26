#!/usr/bin/env python3
"""AWS-only compiler for the exact one-parameter U=2 [6,2] Rees client."""

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
THEOREM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"
CLIENT = ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md"
ERRATUM = ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-client-erratum-v2-20260825.md"
SOURCE_REVIEW = ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-compiler-v2-source-review-20260825.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    THEOREM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    CLIENT: "e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7",
    ERRATUM: "5aa954cbe6396ef5de353519eaf10aed567aec55964bb197c9eb1576b131c10b",
    SOURCE_REVIEW: "b7666bb12ef454f5047074898e0384968393916d97bd06673d3a1f20ab70f50d",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
NAMES = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]
LOAD_LAMBDA_WEIGHTS = [2, 6, 10]


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


def term_text(monomial: list[int], coefficient: Fraction) -> str:
    factors: list[str] = []
    for i, exponent in enumerate(monomial[:7]):
        if exponent:
            factors.append(f"C{i}" if exponent == 1 else f"C{i}^{exponent}")
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
    variables = (
        "Lambda,C0,C1,C2,C3,C4,C5,C6,k10,k6,k2,"
        "mu2,mu4,mu6,J"
    )
    targets = {
        1: "0", 2: "mu2", 3: "0", 4: "mu4",
        5: "0", 6: "mu6", 7: "J/4",
    }
    lines = [
        'LIB "elim.lib";',
        f"ring R={characteristic},({variables}),dp;",
        'print("ONEPARAM_SOURCE_HASHES=PASS");',
        'print("ONEPARAM_LOAD_LINEARITY=PASS");',
    ]
    for ell in range(1, 8):
        expression = tail_text(tails[str(ell)], ell)
        target = targets[ell]
        if target != "0":
            expression += f"-Lambda^{12 + ell}*({target})"
        lines.append(f"poly Phi{ell}={expression};")
    lines.extend([
        "ideal I=Phi1,Phi2,Phi3,Phi4,Phi5,Phi6,Phi7;",
        'print("ONEPARAM_STAGE_LAMBDA_START");',
        "ideal KL=sat(I,ideal(Lambda));",
        'print("ONEPARAM_STAGE_LAMBDA_DONE");',
        'print("ONEPARAM_KL_SIZE="+string(size(KL)));',
        'print("ONEPARAM_KL_DIM="+string(dim(std(KL))));',
        'print("ONEPARAM_STAGE_J_START");',
        "ideal K=sat(KL,ideal(J));",
        'print("ONEPARAM_STAGE_J_DONE");',
        'print("ONEPARAM_K_SIZE="+string(size(K)));',
        'print("ONEPARAM_K_DIM="+string(dim(std(K))));',
        "ideal boundary=K,Lambda;",
        "ideal irrelevant=C0,C1,C2,C3,C4,C5,C6;",
        'print("ONEPARAM_STAGE_IRRELEVANT_START");',
        "ideal H=sat(boundary,irrelevant);",
        "H=std(H);",
        'print("ONEPARAM_STAGE_IRRELEVANT_DONE");',
        'print("ONEPARAM_H_SIZE="+string(size(H)));',
        'print("ONEPARAM_H_DIM="+string(dim(H)));',
        'print("ONEPARAM_H_IS_UNIT="+string(reduce(1,H)==0));',
        'print("ONEPARAM_REES_ENDPOINT=PASS");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 32003, 65521), default=0)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("frozen source mismatch", path))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    if sorted(tails) != [str(i) for i in range(1, 8)]:
        fail("tail key mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"oneparam_rees_char{args.characteristic}.sing"
    emit(singular, args.characteristic, tails)
    payload = {
        "status": "PASS-MAX12-812-ORDER2-U2-62-ONEPARAM-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "theorem_sha256": digest(THEOREM),
        "singular_input_sha256": digest(singular),
        "load_linearity": "EXACT",
        "finite_loads_retained": ["k10", "k6", "k2", "mu2", "mu4", "mu6", "J"],
        "scope": {
            "oneparameter_boundary_equivalence": "CONSUMED_PROVISIONALLY",
            "strict_rees_endpoint": "EMITTED_NOT_RUN",
            "taylor_x0": "NOT_COMPILED",
            "taylor_x1": "NOT_COMPILED",
            "order2_closed": False,
            "JC2": "NOT_CLAIMED",
        },
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
