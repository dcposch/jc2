#!/usr/bin/env python3
"""Compile the fixed-p0 residual-A C-contact-one certificate on AWS."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW_V2 = ROOT / "cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_v2_20260826/compile_raw_cusp_g12_cech_v2.py"
RAW_V2_FREEZE = ROOT / "cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_v2_20260826/FREEZE.sha256"
A_PROMOTION = ROOT / "xmodel/max12-812-order2-p0-a-highcontact-cech-elimination-promotion-20260826.md"
EXPECTED = {
    RAW_V2: "8abeda327a7362e0cd5bdc8b73135bc59e1883664e3824783e34c9182743686d",
    RAW_V2_FREEZE: "9616ff0af8d551a6becb482d95ea1ca7d899a3b9d04df05c7f2cc04af863de7c",
    A_PROMOTION: "4aeee7980586fc4c7c5456c04b84b02527251f6bd68e10f5a028cc5d19ef1f16",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_raw_v2():
    spec = importlib.util.spec_from_file_location("raw_cusp_cech_v2", RAW_V2)
    if spec is None or spec.loader is None:
        fail("cannot load frozen raw-cusp V2 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def append_c1_certificate(script: Path) -> None:
    text = script.read_text()
    anchor = 'print("P0_CUSP_RAW_G12_CECH_ENDPOINT=PASS_DIRECT_REGISTERED_UNIT_CERTIFICATE");\nquit;\n'
    if text.count(anchor) != 1:
        fail("raw V2 endpoint anchor missing or nonunique")
    lines = [
        'print("P0_CUSP_RAW_G12_CECH_ENDPOINT=PASS_DIRECT_REGISTERED_UNIT_CERTIFICATE");',
        "proc FixedP0A(poly P)",
        "{",
        "  P=subst(P,ell1,0); P=subst(P,ell2,0); P=subst(P,ell3,0);",
        "  P=subst(P,cs,0); P=subst(P,rs,0); P=subst(P,c0,0); P=subst(P,c1,0);",
        "  return(P);",
        "}",
        "poly C1g11_2=FixedP0A(g11_2); poly C1g11_1=FixedP0A(g11_1);",
        "int raw11=(C1g11_2==(3/8)*a0*e0 && C1g11_1==(3/8)*(a1*e0+a0*e1));",
        'print("P0_A_C1_G11_RAW_TRIANGULAR="+string(raw11));',
        "poly Da0Second=subst(C1g11_1,e0,0);",
        "int da0=(C1g11_2==(3/8)*a0*e0 && Da0Second==(3/8)*a0*e1);",
        'print("P0_A_C1_DA0_RAISES_C="+string(da0));',
        "poly Da1First=subst(C1g11_1,a0,0);",
        "poly Da1Square=FixedP0A(g12_2); Da1Square=subst(Da1Square,a0,0); Da1Square=subst(Da1Square,e0,0);",
        "int da1=(Da1First==(3/8)*a1*e0 && Da1Square==(3/32)*e1^2);",
        'print("P0_A_C1_DA1_G12_SQUARE="+string(da1));',
        "int rIndependent=(diff(C1g11_2,cs1)==0 && diff(C1g11_2,rs1)==0 && diff(C1g11_1,cs1)==0 && diff(C1g11_1,rs1)==0 && diff(Da1Square,cs1)==0 && diff(Da1Square,rs1)==0);",
        'print("P0_A_C1_ARBITRARY_R_CONTACT_GE1="+string(rIndependent));',
        "if (raw11*da0*da1*rIndependent!=1) { print(\"P0_A_C1_FAIL=RAW_CONTACT_ONE_IDENTITY\"); quit; }",
        'print("P0_A_C1_ENDPOINT=PASS_FIXED_P0_C_CONTACT_ONE_RAISED");',
        "quit;",
    ]
    script.write_text(text.replace(anchor, "\n".join(lines) + "\n"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()

    raw_v2 = load_raw_v2()
    v1 = raw_v2.load_v1()
    owner = v1.load_owner()
    tag = owner.require_aws()
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen p0-A-c1 input mismatch", str(source), actual, expected))
    for source, expected in raw_v2.EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen raw-V2 transitive mismatch", str(source), actual, expected))
    for source, expected in v1.EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen raw-V1 transitive mismatch", str(source), actual, expected))
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
    singular = output / f"p0_a_c1_{label}.sing"
    owner.emit(singular, args.characteristic, tails)
    v1.append_certificate(singular)
    raw_v2.repair_assertions(singular)
    append_c1_certificate(singular)
    source_text = singular.read_text()
    payload = {
        "status": "PASS-P0-A-C1-COMPILER",
        "scope": "FIXED_P0_A_LEADING_C_CONTACT_ONE_ONLY_NO_TOTAL_REES_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "raw_v2_sha256": digest(RAW_V2),
        "tails_sha256": digest(owner.TAILS),
        "input_sha256": digest(singular),
        "source_occurrences": {
            "k6": source_text.count("k6"), "k2": source_text.count("k2"),
            "mu2": source_text.count("mu2"), "mu4": source_text.count("mu4"),
            "mu6": source_text.count("mu6"), "J": source_text.count("J"),
        },
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
