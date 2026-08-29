#!/usr/bin/env python3
"""Compile the thin exact-source c=3,r>=2 vertical residue certificate."""

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
BASE = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_20260826/compile_cge3_universal.py"
BASE_FREEZE = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_20260826/FREEZE.sha256"
LEMMA = ROOT / "xmodel/max12-812-order2-square-c3-vertical-residue-lemma-20260826.md"
LOW = ROOT / "xmodel/max12-812-order2-square-lowcontact-c1-c2-localized-promotion-20260826.md"
LOW_REVIEW = ROOT / "xmodel/max12-812-order2-square-lowcontact-c1-c2-localized-review-grok-20260826.md"
PTANGENT = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v5_ptangent_validator_20260826/RESULT.md"
PINS = {
    BASE: "352ad4f2d10df80e7edcc5179a8c46dfc55b4f7ce07762fb06d2109a9da1da23",
    BASE_FREEZE: "a5efc70c73fb1539086b58bc386a26815e9edb754c50eee505ab8f0918d18169",
    LEMMA: "dd4005a92440e8241807bbe3bea4f9305de06c2d08fd0e095dc5dddba4bc7707",
    LOW: "3447ce8c8da932120a785fd2a6f9ac470477fc87c395377ab54e778a4ad4e5b8",
    LOW_REVIEW: "ca1a669d718e6c7080a8ead3138ba3ecbd12a89ec120e3e821ae4dc4d043470f",
    PTANGENT: "74551fe8b2ed1e4b9b1fd1594cee54e3bd3d87e6acee8b8c29d9384f5317d5ea",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only c3 vertical compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only c3 vertical compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    spec = importlib.util.spec_from_file_location("square_cge3_base", BASE)
    if spec is None or spec.loader is None:
        fail("cannot load frozen c>=3 base compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def specialize(name: str, substitutions: list[tuple[str, str]]) -> list[str]:
    lines: list[str] = []
    for variable, value in substitutions:
        lines.append(f"{name}=subst({name},{variable},{value});")
    return lines


def certificate_block() -> str:
    lines = [
        "poly L0=z^2+p/2;",
        "poly A0z=a1*z+a0; poly A1z=aa1*z+aa0; poly A2z=aaa1*z+aaa0;",
        "poly E3z=(e31*z+e30)/2; poly E4z=(e41*z+e40)/2; poly E5z=(e51*z+e50)/2;",
        "poly B2z=bs2*z+br2/4; poly B3z=bs3*z+br3/4;",
        "poly C3h13=(3/4)*A0z*E3z;",
        "poly C3h14=(3/4)*((A1z*E3z+A0z*E4z)*L0-ell1*A0z*E3z)-(3/8)*B2z*A0z^2+(5/32)*k0*A0z^2*L0;",
        "poly C3h15=(3/4)*((A2z*E3z+A1z*E4z+A0z*E5z)*L0^2-ell1*(A1z*E3z+A0z*E4z)*L0+(ell1^2-ell2*L0)*A0z*E3z)-(3/8)*((B3z*A0z^2+2*B2z*A0z*A1z)*L0-2*ell1*B2z*A0z^2)-(1/16)*A0z^3+(5/32)*((k1*A0z^2+2*k0*A0z*A1z)*L0^2-k0*ell1*A0z^2*L0);",
        "poly C3n13=subst(subst(N13,bs1,0),br1,0);",
        "poly C3n14=subst(subst(N14,bs1,0),br1,0);",
        "poly C3n15=subst(subst(N15,bs1,0),br1,0);",
        "int C3bridge=1;",
        "if (C3n13-L0^2*C3h13!=0) { C3bridge=0; print(\"C3_BRIDGE_REMAINDER_13\"); print(C3n13-L0^2*C3h13); }",
        "if (C3n14-L0*(C3h14+3*ell1*C3h13)!=0) { C3bridge=0; print(\"C3_BRIDGE_REMAINDER_14\"); print(C3n14-L0*(C3h14+3*ell1*C3h13)); }",
        "if (C3n15-(C3h15+3*ell1*C3h14+(3*L0*ell2+3*ell1^2)*C3h13)!=0) { C3bridge=0; print(\"C3_BRIDGE_REMAINDER_15\"); print(C3n15-(C3h15+3*ell1*C3h14+(3*L0*ell2+3*ell1^2)*C3h13)); }",
        "poly C3bad14=C3h14+(3/4)*ell1*A0z*E3z;",
        "int C3negative=(C3n14-L0*(C3bad14+3*ell1*C3h13)!=0);",
        "poly C3d1a=C3h13;",
    ]
    positive = [
        ("p", "-2*rtx^2"),
        ("a1", "aua"),
        ("a0", "-aua*rtx"),
        ("e31", "2*cvg"),
        ("e30", "2*cvg*rtx"),
    ]
    lines += specialize("C3d1a", positive)
    lines += [
        "poly C3La=z^2-rtx^2; poly C3Aa=aua*(z-rtx); poly C3Ea=cvg*(z+rtx);",
        "int C3d1check=(C3d1a-(3/4)*aua*cvg*C3La==0);",
        "poly C3d2a=C3h14;",
    ]
    lines += specialize("C3d2a", positive)
    lines += [
        "poly C3B2a=bs2*z+br2/4; ideal C3GL=std(ideal(C3La));",
        "poly C3d2delta=C3d2a+(3/8)*C3B2a*C3Aa^2;",
        "int C3d2check=(reduce(C3d2delta,C3GL)==0);",
        "poly C3d2root=subst(C3d2a,z,-rtx); poly C3B2root=subst(C3B2a,z,-rtx);",
        "int C3d3check=(C3d2root+(3/8)*C3B2root*(-2*aua*rtx)^2==0);",
        "poly C3d4a=C3h15;",
    ]
    positive_d3 = positive + [("bs2", "bvb"), ("br2", "4*bvb*rtx")]
    lines += specialize("C3d4a", positive_d3)
    lines += [
        "poly C3d4root=subst(C3d4a,z,-rtx);",
        "int C3d4check=(C3d4root+(1/16)*(-2*aua*rtx)^3==0);",
        "int C3rge3=(diff(C3d4root,bs3)==0 && diff(C3d4root,br3)==0 && subst(C3d4root,bvb,0)+(1/16)*(-2*aua*rtx)^3==0);",
        "poly C3d1b=C3h13;",
    ]
    negative = [
        ("p", "-2*rtx^2"),
        ("a1", "aua"),
        ("a0", "aua*rtx"),
        ("e31", "2*cvg"),
        ("e30", "-2*cvg*rtx"),
    ]
    lines += specialize("C3d1b", negative)
    lines += [
        "poly C3Ab=aua*(z+rtx); int C3deckd1=(C3d1b-(3/4)*aua*cvg*C3La==0);",
        "poly C3d2b=C3h14;",
    ]
    lines += specialize("C3d2b", negative)
    lines += [
        "poly C3d2bdelta=C3d2b+(3/8)*C3B2a*C3Ab^2;",
        "int C3deckd2=(reduce(C3d2bdelta,C3GL)==0);",
        "poly C3d4b=C3h15;",
    ]
    negative_d3 = negative + [("bs2", "bvb"), ("br2", "-4*bvb*rtx")]
    lines += specialize("C3d4b", negative_d3)
    lines += [
        "poly C3d4broot=subst(C3d4b,z,rtx);",
        "int C3deckd4=(C3d4broot+(1/16)*(2*aua*rtx)^3==0);",
        "int C3wrong=(C3d4root+(1/15)*(-2*aua*rtx)^3!=0);",
        'print("SQUARE_C3_SOURCE_BRIDGE="+string(C3bridge));',
        'print("SQUARE_C3_OMITTED_CONNECTION_REJECTED="+string(C3negative));',
        'print("SQUARE_C3_D1_ROOT_ALLOCATION="+string(C3d1check));',
        'print("SQUARE_C3_D2_MOD_L="+string(C3d2check));',
        'print("SQUARE_C3_D3_R2_FACTOR="+string(C3d3check));',
        'print("SQUARE_C3_D4_MOD_COMPLEMENT="+string(C3d4check));',
        'print("SQUARE_C3_RGE3_SYMBOLIC="+string(C3rge3));',
        'print("SQUARE_C3_DECK_D1="+string(C3deckd1));',
        'print("SQUARE_C3_DECK_D2="+string(C3deckd2));',
        'print("SQUARE_C3_DECK_D4="+string(C3deckd4));',
        'print("SQUARE_C3_WRONG_CUBIC_REJECTED="+string(C3wrong));',
        "int C3all=C3bridge*C3negative*C3d1check*C3d2check*C3d3check*C3d4check*C3rge3*C3deckd1*C3deckd2*C3deckd4*C3wrong;",
        "if (analyticDiv*row13*row14*row15*numDiv*C3all!=1) { print(\"SQUARE_C3_FAIL=SOURCE_BRIDGE_OR_DIVISIBILITY\"); quit; }",
        'print("SQUARE_C3_ENDPOINT=PASS_VERTICAL_C3_RGE2_THIN_DIVISIBILITY");',
        "quit;",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        if digest(source) != expected:
            fail(("frozen source mismatch", str(source), digest(source), expected))
    base = load_base()
    for source, expected in base.EXPECTED.items():
        if digest(source) != expected:
            fail(("frozen transitive source mismatch", str(source)))
    tails = json.loads(base.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != base.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_c3_vertical_thin_{label}.sing"
    base.emit(target, args.characteristic, tails)
    source_text = target.read_text()
    ring_anchor = ",mu2,mu4,mu6,J),dp;"
    ring_replacement = ",mu2,mu4,mu6,J,rtx,aua,cvg,bvb),dp;"
    if source_text.count(ring_anchor) != 1:
        fail(("ring anchor missing or nonunique", source_text.count(ring_anchor)))
    source_text = source_text.replace(ring_anchor, ring_replacement)
    tail_anchor = "poly L0=z^2+p/2; poly L03=L0^3;"
    if source_text.count(tail_anchor) != 1:
        fail(("tail anchor missing or nonunique", source_text.count(tail_anchor)))
    source_text = source_text.split(tail_anchor, 1)[0] + certificate_block() + "\n"
    target.write_text(source_text)
    payload = {
        "status": "PASS-SQUARE-C3-VERTICAL-THIN-COMPILER",
        "scope": "A_ZERO_C3_RGE2_ON_DPK_ONLY_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "base_compiler_sha256": digest(BASE),
        "lemma_sha256": digest(LEMMA),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
