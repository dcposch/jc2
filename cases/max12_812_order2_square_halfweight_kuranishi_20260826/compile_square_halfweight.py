#!/usr/bin/env python3
"""Compile the correction-aware generic-square half-weight receiver on AWS."""

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
DESIGN = ROOT / "xmodel/max12-812-order2-generic-square-halfweight-kuranishi-design-20260826.md"
THIRD_TAIL = ROOT / "xmodel/max12-812-order2-square-third-tail-divisibility-theorem-20260826.md"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"
FIRST_NORMAL = ROOT / "xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md"
PADE = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md"
PADE_REVIEW = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md"

EXPECTED_STATIC = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    BASE_COMPILER: "77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc",
    DESIGN: "37a7234cee998a0069f33b7a36bb945123b305acd01485a771d8e6ed7dac65fd",
    THIRD_TAIL: "045b1bdc6c1429451afa34dd2d7d12da4c72d9af716e52228a869f61d0f4a4bb",
    ONEPARAM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    FIRST_NORMAL: "827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc",
    PADE: "2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5",
    PADE_REVIEW: "73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only square half-weight compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only square half-weight compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base_compiler():
    spec = importlib.util.spec_from_file_location("square_ladder_base", BASE_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot load charged base compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_coefficients() -> dict[int, str]:
    p = "p"
    c = "(sigma^2*cs)"
    r = "((p^2+sigma^2*rs)/4)"
    n3 = "(sigma^3*a1)"
    n2 = "(sigma^3*a0)"
    n1 = "(sigma^3*(p*a1+c1)/2)"
    n0 = "(sigma^3*(p*a0+c0)/2)"
    return {
        6: f"(2*({p}))",
        5: f"(2*({c}))",
        4: f"(({p})^2+2*({r}))",
        3: f"(2*({p})*({c})+sigma^2*({n3}))",
        2: f"(({c})^2+2*({p})*({r})+sigma^2*({n2}))",
        1: f"(2*({c})*({r})+sigma^2*({n1}))",
        0: f"(({r})^2+sigma^2*({n0}))",
    }


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    base = load_base_compiler()
    coeffs = source_coefficients()
    loads = {"k10": "k10", "k6": "k6", "k2": "k2"}
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    lines = [
        'LIB "elim.lib";',
        'LIB "primdec.lib";',
        f"ring Rfull={characteristic},(sigma,p,cs,rs,a0,a1,c0,c1,k10,k6,k2,mu2,mu4,mu6,J),dp;",
        "proc idealZero(ideal A, ideal G)",
        "{",
        "  int i;",
        "  for (i=1; i<=size(A); i++) { if (reduce(A[i],G)!=0) { return(0); } }",
        "  return(1);",
        "}",
        'print("SQUARE_HALFWEIGHT_SOURCE_HASHES=PASS");',
        "ideal Sigma10=std(ideal(sigma^10));",
        "int divisible=1; int identity=1; int forbidden=1;",
    ]
    for ell in range(1, 8):
        expression = base.tail_text(tails[str(ell)], ell, coeffs, loads)
        expression = expression.replace("Lambda", "(sigma^2)")
        if targets[ell] != "0":
            expression += f"-sigma^{2 * (12 + ell)}*({targets[ell]})"
        lines.extend(
            [
                f"poly Phi{ell}={expression};",
                f"if (reduce(Phi{ell},Sigma10)!=0) {{ divisible=0; }}",
                f"poly Xi{ell}=Phi{ell}/sigma^10;",
                f"if (sigma^10*Xi{ell}-Phi{ell}!=0) {{ identity=0; }}",
                f"poly e{ell}=subst(Xi{ell},sigma,0);",
                f"if (diff(e{ell},k6)!=0 || diff(e{ell},k2)!=0 || diff(e{ell},mu2)!=0 || diff(e{ell},mu4)!=0 || diff(e{ell},mu6)!=0 || diff(e{ell},J)!=0) {{ forbidden=0; }}",
            ]
        )
    lines.extend(
        [
            'print("SQUARE_HALFWEIGHT_SIGMA10_DIVISIBLE="+string(divisible));',
            'print("SQUARE_HALFWEIGHT_DIVISION_IDENTITY="+string(identity));',
            'print("SQUARE_HALFWEIGHT_FORBIDDEN="+string(forbidden));',
            'if (divisible*identity*forbidden!=1) { print("SQUARE_HALFWEIGHT_FAIL=SOURCE_GATE"); quit(81); }',
            'print("SQUARE_HALFWEIGHT_ROWS_BEGIN");',
            "print(e1); print(e2); print(e3); print(e4); print(e5); print(e6); print(e7);",
            'print("SQUARE_HALFWEIGHT_ROWS_END");',
            "ideal Efull=e1,e2,e3,e4,e5,e6,e7;",
            f"ring Rsmall={characteristic},(p,cs,rs,a0,a1,c0,c1,k10),dp;",
            "ideal E=std(imap(Rfull,Efull));",
            "ideal Ep=std(sat(E,ideal(p)));",
            "ideal Epk=std(sat(Ep,ideal(k10)));",
            "ideal Rad=std(radical(Epk));",
            "ideal Expected=std(ideal(cs,rs,c0,c1));",
            "int rad_in_expected=idealZero(Rad,Expected);",
            "int expected_in_rad=idealZero(Expected,Rad);",
            'print("SQUARE_HALFWEIGHT_RAW_BEGIN"); print(Epk); print("SQUARE_HALFWEIGHT_RAW_END");',
            'print("SQUARE_HALFWEIGHT_RADICAL_BEGIN"); print(Rad); print("SQUARE_HALFWEIGHT_RADICAL_END");',
            'print("SQUARE_HALFWEIGHT_RAD_IN_EXPECTED="+string(rad_in_expected));',
            'print("SQUARE_HALFWEIGHT_EXPECTED_IN_RAD="+string(expected_in_rad));',
            'if (rad_in_expected*expected_in_rad!=1) { print("SQUARE_HALFWEIGHT_FAIL=RADICAL_MISMATCH"); quit(82); }',
            'print("SQUARE_HALFWEIGHT_ENDPOINT=PASS_CORRECTION_AWARE_NORMALIZED_RAY");',
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
    singular = output / f"square_halfweight_{label}.sing"
    emit(singular, args.characteristic, tails)
    result = {
        "status": "PASS-SQUARE-HALFWEIGHT-COMPILER",
        "scope": "GENERIC_SQUARE_CORRECTION_AWARE_NORMALIZED_RAY_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "design_sha256": digest(DESIGN),
        "input_sha256": digest(singular),
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
