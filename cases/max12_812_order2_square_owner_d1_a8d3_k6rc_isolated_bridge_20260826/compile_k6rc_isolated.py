#!/usr/bin/env python3
"""Isolate the a8d3 grade-38 k6*R*C literal/Faber bridge; AWS only."""

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
TAIL_COMPILER = ROOT / "cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py"
SOURCE_COMPILER = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/compile_r1_d1_ac.py"
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
PINS = {
    TAIL_COMPILER: "77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc",
    SOURCE_COMPILER: "e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    HERE / "PREREGISTRATION.md": "26bd59c03946a273db29408d7864a0abb008d6b6ec36e0831121386788922468",
}
PAIRS = (
    (4, "c1", "b1", "R4_C1B1"),
    (5, "c1", "b0", "R5_C1B0"),
    (5, "c0", "b1", "R5_C0B1"),
    (6, "c0", "b0", "R6_C0B0"),
    (6, "c1", "b1", "R6_C1B1"),
    (7, "c1", "b0", "R7_C1B0"),
    (7, "c0", "b1", "R7_C0B1"),
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), required=True)
    args = parser.parse_args()
    if platform.system() != "Linux":
        fail("AWS-only k6RC diagnostic refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only k6RC diagnostic refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    for path, expected in PINS.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen pin mismatch", str(path), actual, expected))

    tail = load(TAIL_COMPILER, "k6rc_tail")
    source = load(SOURCE_COMPILER, "k6rc_source")
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != tail.EXPECTED_ALL_TAILS:
        fail("canonical tails hash mismatch")

    output = args.output.resolve()
    if output.exists():
        fail("isolated output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_a8d3_k6rc_isolated_{label}.sing"

    coeffs = source.source_coefficients(
        "p", "0", "0", "sigma^11*c1", "sigma^11*c0",
        "sigma^8*eta*b1", "sigma^8*eta*b0",
    )
    loads = {"k10": "0", "k6": "k60", "k2": "0"}
    literal_rows = {
        row: tail.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
        for row in range(1, 8)
    }

    lines = [
        f"ring R={args.characteristic},(sigma,p,eta,c1,c0,b1,b0,k60,t),dp;",
        'print("K6RC_ISOLATED_SOURCE_HASHES=PASS");',
        "ideal S38=std(ideal(sigma^38)); ideal S39=std(ideal(sigma^39));",
    ]
    for row in range(1, 8):
        lines.append(f"poly Lit{row}={literal_rows[row]};")
    lines += [
        "poly p2=p*p; poly p3=p2*p; poly p4=p2*p2;",
        "poly inv3=1-(3/2)*p*t^2+(3/2)*p2*t^4-(5/4)*p3*t^6+(15/16)*p4*t^8;",
        "poly H=(-3/8)*eta*k60*(b1+b0*t)*(c1+c0*t)*t^5*inv3;",
        "poly D0=H;",
    ]
    for derivative in range(1, 9):
        lines.append(f"poly D{derivative}=diff(D{derivative-1},t);")
        if derivative >= 2:
            row = derivative - 1
            factorial = 1
            for value in range(2, derivative + 1):
                factorial *= value
            lines.append(f"poly h{row}=subst(D{derivative},t,0)/{factorial};")
    lines += [
        "poly Pred1=h1;",
        "poly Pred2=h2;",
        "poly Pred3=(p/4)*h1+h3;",
        "poly Pred4=(p/2)*h2+h4;",
        "poly Pred5=(3/32)*p2*h1+(3/4)*p*h3+h5;",
        "poly Pred6=(1/4)*p2*h2+p*h4+h6;",
        "poly Pred7=(5/128)*p3*h1+(15/32)*p2*h3+(5/4)*p*h5+h7;",
        "int binomial_coefficient=((3/4)*((3/4)-1)/2*4==-3/8);",
        'print("K6RC_BINOMIAL_COEFFICIENT_MINUS3_OVER8="+string(binomial_coefficient));',
    ]
    match_names = []
    zero_vars = ("c1", "c0", "b1", "b0", "k60")
    for row, cvar, bvar, label_name in PAIRS:
        lit = f"lit_{label_name}"
        pred = f"pred_{label_name}"
        expression = f"diff(diff(diff(Lit{row},k60),{cvar}),{bvar})"
        for variable in zero_vars:
            expression = f"subst(({expression}),{variable},0)"
        lines += [
            f"poly {lit}_raw=reduce(({expression}),S39);",
            f"int {lit}_div=(reduce({lit}_raw,S38)==0);",
            f"poly {lit}=subst(({lit}_raw/sigma^38),sigma,0);",
        ]
        expression = f"diff(diff(diff(Pred{row},k60),{cvar}),{bvar})"
        for variable in zero_vars:
            expression = f"subst(({expression}),{variable},0)"
        lines += [
            f"poly {pred}=({expression});",
            f"poly diff_{label_name}={lit}-{pred};",
            f"int match_{label_name}=({lit}_div && ({lit}=={pred}));",
            f'print("K6RC_LIT_{label_name}="+string({lit}));',
            f'print("K6RC_PRED_{label_name}="+string({pred}));',
            f'print("K6RC_DIFF_{label_name}="+string(diff_{label_name}));',
            f'print("K6RC_MATCH_{label_name}="+string(match_{label_name}));',
        ]
        match_names.append(f"match_{label_name}")
    lines += [
        "int all_match=" + "*".join(match_names) + ";",
        'print("K6RC_ALL_LITERAL_ROWS_MATCH_LAURENT="+string(all_match));',
        'print("K6RC_ISOLATED_ENDPOINT=RECORDED_NO_CELL_VERDICT");',
        "quit;",
    ]
    target.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "COMPILED-A8D3-K6RC-ISOLATED-DIAGNOSTIC",
        "scope": "A8D3_GRADE38_K6RC_LITERAL_VS_LAURENT_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target),
        "canonical_tails_sha256": digest(TAILS),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
