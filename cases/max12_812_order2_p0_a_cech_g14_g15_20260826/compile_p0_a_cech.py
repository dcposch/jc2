#!/usr/bin/env python3
"""Compile the fixed-p=0 residual A-Cech source certificate (AWS only)."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OWNER = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/compile_square_a_prolongation.py"
OWNER_FREEZE = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/FREEZE.sha256"
DESIGN = ROOT / "xmodel/max12-812-order2-p0-dk0-support-exhaustion-ramified-closure-design-20260826.md"

EXPECTED = {
    OWNER: "2c7f051da265f5af3ee76007360e41af92f8492c5969846f8e529317d4dd5630",
    OWNER_FREEZE: "6dbf5b6118aac14c38facdd977e221b0e4648a9e875fe03867172c646e322f64",
    DESIGN: "3518ac6c1505098a7b9e19c7b7ca2610dce42ff741e3f39065d0618b926ddb10",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_owner():
    spec = importlib.util.spec_from_file_location("square_aprol_owner", OWNER)
    if spec is None or spec.loader is None:
        fail("cannot load frozen A-prolongation owner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def append_p0_certificate(script: Path) -> None:
    text = script.read_text()
    terminal = 'print("SQUARE_APROLONG_ENDPOINT=PASS_EXACT_SOURCE_G14_G15_A_ZERO_GATE");\nquit;\n'
    if text.count(terminal) != 1:
        fail("frozen owner endpoint anchor missing or nonunique")

    lines = [
        'print("SQUARE_APROLONG_ENDPOINT=PASS_EXACT_SOURCE_G14_G15_A_ZERO_GATE");',
        'print("P0_A_CECH_SOURCE_SPECIALIZATION=p=0_BEFORE_D(p)");',
        "int p0bridge=1;",
    ]
    for ell in range(1, 8):
        lines.extend(
            [
                f"poly p0g14_{ell}=subst(g14_{ell},p,0);",
                f"poly p0g15_{ell}=subst(g15_{ell},p,0);",
                f"poly p0h14_{ell}=subst(h14_{ell},p,0);",
                f"poly p0h15_{ell}=subst(h15_{ell},p,0);",
                f"if (p0g14_{ell}-p0h14_{ell}!=0 || p0g15_{ell}-p0h15_{ell}!=0) {{ p0bridge=0; }}",
            ]
        )
    lines.extend(
        [
            'print("P0_A_CECH_FABER_IDENTITY_AT_COLLISION="+string(p0bridge));',
            "int constchart=(p0g15_6+(1/16)*a0^3==0);",
            'print("P0_A_CECH_DA0_G15_ROW6_PURE_CUBE="+string(constchart));',
            "poly tang14_2=subst(p0g14_2,a0,0);",
            "poly tang14_1=subst(p0g14_1,a0,0);",
            "int tang14=(tang14_2+(3/32)*a1^2*br0==0) && (tang14_1-(3/8)*a1*(e0-a1*bs0)==0);",
            'print("P0_A_CECH_DA1_G14_TRIANGULAR="+string(tang14));',
            "poly tang15_3=subst(p0g15_3,a0,0);",
            "tang15_3=subst(tang15_3,br0,0);",
            "tang15_3=subst(tang15_3,e0,a1*bs0);",
            "int tang15=(tang15_3+(1/16)*a1^3==0);",
            'print("P0_A_CECH_DA1_G15_ROW3_PURE_CUBE="+string(tang15));',
            'if (p0bridge*constchart*tang14*tang15!=1) { print("P0_A_CECH_FAIL=SOURCE_OR_TRIANGULAR_IDENTITY"); quit; }',
            'print("P0_A_CECH_ENDPOINT=PASS_FIXED_P0_RAW_A_CHARTS");',
            "quit;",
        ]
    )
    script.write_text(text.replace(terminal, "\n".join(lines) + "\n"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()

    owner = load_owner()
    tag = owner.require_aws()
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen wrapper source mismatch", str(source), actual, expected))
    for source, expected in owner.EXPECTED_STATIC.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen owner transitive mismatch", str(source), actual, expected))

    tails = json.loads(owner.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != owner.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"p0_a_cech_{label}.sing"
    owner.emit(singular, args.characteristic, tails)
    append_p0_certificate(singular)

    result = {
        "status": "PASS-P0-A-CECH-COMPILER",
        "scope": "FIXED_P0_HIGH_CONTACT_A_CECH_G14_G15_ONLY_NO_TOTAL_REES_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "owner_sha256": digest(OWNER),
        "design_sha256": digest(DESIGN),
        "tails_sha256": digest(owner.TAILS),
        "input_sha256": digest(singular),
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
