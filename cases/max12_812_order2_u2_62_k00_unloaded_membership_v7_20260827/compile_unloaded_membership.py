#!/usr/bin/env python3
"""Compile exact unloaded K00 row-7 membership lanes on AWS."""

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
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"
DESIGN = ROOT / "xmodel/max12-812-order2-p0-k00-honest-source-discriminator-design-sol-20260827.md"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    ONEPARAM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    DESIGN: "9c5bf1229cf45dd7ea4d5d3907fd6033c88c0d9768934d01ea79e658f3d65a17",
    PREREG: "6f1fedfb32fc5831a908447e410cf3d6f3397b9231aff1d9b1f0a22dd362f11e",
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
        fail("AWS-only membership compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only membership compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def coefficient_images(mode: str) -> dict[int, str]:
    x = "C6" if mode == "direct" else "1"
    prefix = "d"
    return {
        6: x,
        5: f"{prefix}5",
        4: f"(3*({x})^2+{prefix}4)/8",
        3: f"{prefix}3",
        2: f"(({x})^3+{prefix}2)/16",
        1: f"{prefix}1",
        0: f"(({x})^4+{prefix}0)/256",
    }


def term_text(monomial: list[int], coefficient: Fraction, images: dict[int, str]) -> str:
    factors: list[str] = []
    for i, exponent in enumerate(monomial[:7]):
        if exponent == 1:
            factors.append(f"({images[i]})")
        elif exponent:
            factors.append(f"({images[i]})^{exponent}")
    body = "*".join(factors) or "1"
    if coefficient == 1 and factors:
        return body
    if coefficient == -1 and factors:
        return "-" + body
    return f"{rational_text(coefficient)}*{body}" if factors else rational_text(coefficient)


def unloaded_tail(entries: list[list[object]], ell: int, images: dict[int, str]) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != len(NAMES):
            fail(("monomial length", ell, monomial))
        if any(value < 0 for value in monomial):
            fail(("negative monomial exponent", ell, monomial))
        if sum(a * b for a, b in zip(monomial, WEIGHTS)) != 12 + ell:
            fail(("tail weight", ell, monomial))
        if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
            fail(("tail load nonlinearity", ell, monomial))
        if any(monomial[7:]):
            continue
        terms.append(term_text(monomial, Fraction(str(raw_coefficient)), images))
    return "+".join(terms).replace("+-", "-") if terms else "0"


def emit(path: Path, mode: str, tails: dict[str, list[list[object]]]) -> None:
    images = coefficient_images(mode)
    if mode == "direct":
        variables = "t,C6,d0,d1,d2,d3,d4,d5"
        localizer_generator = ",1-t*C6"
        label = "DIRECT_LOCALIZED"
    else:
        variables = "d0,d1,d2,d3,d4,d5"
        localizer_generator = ""
        label = "KUMMER_NORMALIZED_C6_1"
    lines = [
        'LIB "elim.lib";',
        f"ring R=0,({variables}),dp;",
        f'print("K00_UNLOADED_MODE={label}");',
        'print("K00_UNLOADED_SOURCE_HASHES=PASS");',
        'print("K00_UNLOADED_LOADS_REMOVED_BY_LITERAL_ZERO_SPECIALIZATION=PASS");',
    ]
    for ell in range(1, 8):
        lines.append(f"poly r{ell}={unloaded_tail(tails[str(ell)], ell, images)};")
    lines.extend([
        f"ideal I=r1,r2,r3,r4,r5,r6{localizer_generator};",
        'print("K00_UNLOADED_STD_START");',
        "ideal G=std(I);",
        'print("K00_UNLOADED_STD_DONE");',
        'print("K00_UNLOADED_G_SIZE="+string(size(G)));',
        'print("K00_UNLOADED_G_DIM="+string(dim(G)));',
        "int proper=(reduce(1,G)!=0);",
        'print("K00_UNLOADED_NEGATIVE_CONTROL_PROPER="+string(proper));',
        'if (proper!=1) { print("K00_UNLOADED_FAIL=SOURCE_IDEAL_UNIT"); exit(81); }',
        "poly residual=reduce(r7,G);",
        "int member=(residual==0);",
        'print("K00_UNLOADED_MEMBER="+string(member));',
        'write("STANDARD_BASIS.txt",G);',
        "if (member==1)",
        "{",
        "  matrix L=lift(I,ideal(r7));",
        "  poly replay=-r7;",
        "  int j;",
        "  for (j=1; j<=size(I); j++) { replay=replay+L[j,1]*I[j]; }",
        "  int replay_ok=(replay==0);",
        '  print("K00_UNLOADED_LIFT_REPLAY="+string(replay_ok));',
        '  if (replay_ok!=1) { print("K00_UNLOADED_FAIL=LIFT_REPLAY"); exit(82); }',
        '  write("MEMBERSHIP_LIFT.txt",L);',
        '  print("K00_UNLOADED_EVIDENCE=LIFT");',
        "}",
        "else",
        "{",
        '  write("NONMEMBERSHIP_RESIDUAL.txt",residual);',
        '  print("K00_UNLOADED_LIFT_REPLAY=NOT_APPLICABLE");',
        '  print("K00_UNLOADED_EVIDENCE=RESIDUAL");',
        "}",
        'print("K00_UNLOADED_ENDPOINT=PASS_MEMBERSHIP_DECISION");',
        "exit(0);",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--mode", choices=("direct", "normalized"), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED.items():
        if expected == "TO_BE_FROZEN" or digest(source) != expected:
            fail(("frozen source mismatch", str(source), digest(source), expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    if sorted(tails) != [str(i) for i in range(1, 8)]:
        fail("tail key mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"k00_unloaded_{args.mode}_q.sing"
    emit(singular, args.mode, tails)
    result = {
        "status": "PASS-K00-UNLOADED-MEMBERSHIP-COMPILER",
        "registered_aws_lane": tag,
        "mode": args.mode,
        "characteristic": 0,
        "tails_sha256": digest(TAILS),
        "canonical_all_tails_sha256": EXPECTED_ALL_TAILS,
        "oneparameter_sha256": digest(ONEPARAM),
        "design_sha256": digest(DESIGN),
        "preregistration_sha256": digest(PREREG),
        "input_sha256": digest(singular),
        "scope": "UNLOADED_K00_ROW7_MEMBERSHIP_ONLY_NO_CLOSURE_OR_JC2_VERDICT",
    }
    (output / "compiler_result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
