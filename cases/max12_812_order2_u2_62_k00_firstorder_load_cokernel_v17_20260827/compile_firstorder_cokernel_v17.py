#!/usr/bin/env python3
"""Compile exact K00 first-order load-deformation cokernels, AWS only."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
V7 = ROOT / "cases/max12_812_order2_u2_62_k00_unloaded_membership_v7_20260827/compile_unloaded_membership.py"
V14R1 = ROOT / "cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827"
PRELUDE = V14R1 / "aws_q_box01_pass/compiled/serialized_replay_prelude_Q.sing"
S87 = V14R1 / "aws_q_box01_pass/run/artifacts/SYZYGY_MODULE.txt"
H = V14R1 / "aws_q_box01_pass/run/artifacts/LOCAL_UNIT_WITNESS_R1.txt"
U = [V14R1 / f"aws_q_box01_pass/run/artifacts/UNIT_MULTIPLIER_{i}.txt" for i in range(1, 7)]
V14_RESULT = V14R1 / "aws_q_box01_pass/run/RESULT.json"
V16_RESULT = ROOT / "cases/max12_812_order2_u2_62_k00_syzygy_constant_projection_v16r1_20260827/aws_q_box01_pass/run/RESULT.json"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    V7: "a7f335cdbc3e5525ce641ff10d8370a52d4cbb9c84e2417b17eea64a38154f70",
    PRELUDE: "5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a",
    S87: "788a836b729d3de5e9600de07244b5d4b836c91a7538e0b1e4ef307ad86d21fb",
    H: "87ced4afe1680f11073eb62bda7c7894f297925283557b2ccf0e951daba09e04",
    U[0]: "ed096c8246ff96cb5ab621a9a74061b24e1678ff061a98137a067c387969e1e5",
    U[1]: "1f8369edbbb10bfbbb155250775399170e696e0fdbe33bb75f54bb5639f78791",
    U[2]: "ce8b51a7e9a11f0fa3a3594480fbe3e4b556e9fd0a17cf29175b273474104f0f",
    U[3]: "5d9f371cf8302502d05a56effbfe3bbbbeafd28d6dfdad8cf7f1bba3ebb60f18",
    U[4]: "135c17e36fd53a438e98c36104e350e6ed362223dfba38e7e927c6dccf65a98e",
    U[5]: "93762abdfa9b12b520a47848e55776176d9227eaca253deb80a6a9a13b4c3295",
    V14_RESULT: "28be0ddf9d12529586817e6a7e96cb3ff2bc8e84e4983f7c2f25366f81b4f7e2",
    V16_RESULT: "b6cd066a5d93fa81a4eb4217f44916969aa7b515b7e367befbe9018045a6d7ff",
    PREREG: "54916ad18f4e33c68c4ef6c9d636a40eafb7c84325f0b6d876be76cb3be462c7",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
LOADS = (("k10", 7, 2), ("k6", 8, 6), ("k2", 9, 10))


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def safe_expression(path: Path) -> str:
    text = path.read_text().strip()
    if not text or ";" in text or '"' in text or "\r" in text:
        fail(("malformed frozen polynomial", str(path)))
    return text


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V17 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V17 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v7():
    spec = importlib.util.spec_from_file_location("k00_v7_for_v17", V7)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V7 source map")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_coefficient(entries: list[list[object]], ell: int, load_index: int, images: dict[int, str], v7) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != 10 or any(value < 0 for value in monomial):
            fail(("malformed tail monomial", ell, monomial))
        if sum(a * b for a, b in zip(monomial, v7.WEIGHTS)) != 12 + ell:
            fail(("tail weight mismatch", ell, monomial))
        if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
            fail(("tail is not affine-linear in loads", ell, monomial))
        if monomial[load_index] == 1:
            terms.append(v7.term_text(monomial, Fraction(str(raw_coefficient)), images))
    return "+".join(terms).replace("+-", "-") if terms else "0"


def direction_block(label: str) -> list[str]:
    suffix = label.upper()
    rows = [f"a{suffix}{i}" for i in range(1, 8)]
    lines = [
        f'print("K00_V17_{suffix}_START");',
        f"ideal Load{suffix}={','.join(rows)};",
        f"ideal E{suffix}=0;",
        "for (j=1; j<=nt; j++)",
        "{",
        "  z=0;",
    ]
    for i in range(1, 7):
        lines.append(f"  z=z+T[j][{i}]*{rows[i-1]};")
    lines.extend([
        f"  E{suffix}[j]=z;",
        "}",
        f"ideal GE{suffix}=std(E{suffix});",
        f"poly D{suffix}=h*{rows[6]};",
    ])
    for i in range(1, 7):
        lines.append(f"D{suffix}=D{suffix}-u{i}*{rows[i-1]};")
    lines.extend([
        f"ideal J{suffix}=I,E{suffix};",
        f"ideal GJ{suffix}=std(J{suffix});",
        f"int global{suffix}=(reduce(D{suffix},GJ{suffix})==0);",
        f"int localquotientproper{suffix}=(reduce(1,std(J{suffix}+maximal))!=0);",
        f"int rep{suffix}=1; poly dalt{suffix}; poly cross{suffix};",
        "for (j=1; j<=87; j++)",
        "{",
        f"  dalt{suffix}=S87[j][7]*{rows[6]};",
    ])
    for i in range(1, 7):
        lines.append(f"  dalt{suffix}=dalt{suffix}+S87[j][{i}]*{rows[i-1]};")
    lines.extend([
        f"  cross{suffix}=h*dalt{suffix}-S87[j][7]*D{suffix};",
        f"  if (reduce(cross{suffix},GE{suffix})!=0) {{ rep{suffix}=0; }}",
        "}",
        f'print("K00_V17_{suffix}_REPRESENTATION_INVARIANCE="+string(rep{suffix}));',
        f'if (rep{suffix}!=1) {{ print("K00_V17_FAIL={suffix}_REPRESENTATION"); quit; }}',
        f"int zero{suffix}=(D{suffix}==0); int local{suffix}; int allzero{suffix}=1; int wi{suffix}=0; poly cc{suffix};",
        f"ideal C{suffix}; ideal GC{suffix};",
        f"if (zero{suffix}==1)",
        "{",
        f"  C{suffix}=ideal(1); GC{suffix}=std(C{suffix}); local{suffix}=1;",
        f'  write("BRANCH_{suffix}.txt","ZERO_TARGET");',
        f'  print("K00_V17_{suffix}_BRANCH=ZERO_TARGET");',
        "}",
        "else",
        "{",
        f"  C{suffix}=quotient(J{suffix},ideal(D{suffix})); GC{suffix}=std(C{suffix});",
        f"  local{suffix}=(reduce(1,std(C{suffix}+maximal))==0);",
        f"  for (j=1; j<=size(C{suffix}); j++)",
        "  {",
        f"    cc{suffix}=C{suffix}[j]; cc{suffix}=subst(cc{suffix},d0,0); cc{suffix}=subst(cc{suffix},d1,0); cc{suffix}=subst(cc{suffix},d2,0);",
        f"    cc{suffix}=subst(cc{suffix},d3,0); cc{suffix}=subst(cc{suffix},d4,0); cc{suffix}=subst(cc{suffix},d5,0);",
        f"    if (cc{suffix}!=0) {{ allzero{suffix}=0; if (wi{suffix}==0) {{ wi{suffix}=j; }} }}",
        "  }",
        f"  if (local{suffix}==1)",
        "  {",
        f'    write("BRANCH_{suffix}.txt","LOCAL_ZERO"); print("K00_V17_{suffix}_BRANCH=LOCAL_ZERO");',
        f'    if (wi{suffix}==0) {{ print("K00_V17_FAIL={suffix}_MISSING_UNIT_WITNESS"); quit; }}',
        f"    ideal W{suffix}=C{suffix}[wi{suffix}]*D{suffix}; matrix L{suffix}=lift(J{suffix},W{suffix}); poly replay{suffix}=-W{suffix}[1];",
        f"    for (i=1; i<=size(J{suffix}); i++) {{ replay{suffix}=replay{suffix}+J{suffix}[i]*L{suffix}[i,1]; }}",
        f'    if (replay{suffix}!=0) {{ print("K00_V17_FAIL={suffix}_LOCAL_LIFT"); quit; }}',
        f'    write("LOCAL_WITNESS_{suffix}.txt",C{suffix}[wi{suffix}]); write("LOCAL_LIFT_{suffix}.txt",L{suffix}); write("LOCAL_REPLAY_{suffix}.txt",replay{suffix});',
        "  }",
        "  else",
        "  {",
        f'    write("BRANCH_{suffix}.txt","LOCAL_NONZERO"); print("K00_V17_{suffix}_BRANCH=LOCAL_NONZERO");',
        f'    if (allzero{suffix}!=1) {{ print("K00_V17_FAIL={suffix}_NONMEMBER_CONSTANT"); quit; }}',
        "  }",
        "}",
        f'print("K00_V17_{suffix}_TARGET_ZERO="+string(zero{suffix}));',
        f'print("K00_V17_{suffix}_GLOBAL_ZERO="+string(global{suffix}));',
        f'print("K00_V17_{suffix}_LOCAL_ZERO="+string(local{suffix}));',
        f'print("K00_V17_{suffix}_LOCAL_QUOTIENT_PROPER="+string(localquotientproper{suffix}));',
        f'print("K00_V17_{suffix}_IMAGE_GENERATORS="+string(size(E{suffix})));',
        f'print("K00_V17_{suffix}_COLON_GENERATORS="+string(size(C{suffix})));',
        f'write("LOAD_ROWS_{suffix}.txt",Load{suffix});',
        f'write("IMAGE_{suffix}.txt",E{suffix}); write("IMAGE_GB_{suffix}.txt",GE{suffix});',
        f'write("TARGET_{suffix}.txt",D{suffix}); write("QUOTIENT_GB_{suffix}.txt",GJ{suffix});',
        f'write("COLON_{suffix}.txt",C{suffix}); write("COLON_GB_{suffix}.txt",GC{suffix});',
        f'print("K00_V17_{suffix}_DONE");',
    ])
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--field", choices=("Q", "65521"), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen source mismatch", str(path), actual, expected))
    v14 = json.loads(V14_RESULT.read_text())
    v16 = json.loads(V16_RESULT.read_text())
    if v14.get("local_member") is not True or v16.get("evaluation_rank") != 1:
        fail("upstream exact endpoint sentinel mismatch")
    v7 = load_v7()
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    images = v7.coefficient_images("normalized")
    prelude = PRELUDE.read_text()
    characteristic = 0 if args.field == "Q" else 65521
    if characteristic:
        prelude = prelude.replace("ring R=0,", f"ring R={characteristic},", 1)
    if prelude.count("ring R=") != 1 or sum(prelude.count(f"poly r{i}=") for i in range(1, 8)) != 7:
        fail("malformed row prelude")
    syz87 = safe_expression(S87)
    h = safe_expression(H)
    multipliers = [safe_expression(path) for path in U]
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"k00_firstorder_cokernel_v17_{args.field}.sing"
    lines = [
        prelude.rstrip(),
        f'print("K00_V17_FIELD={args.field}");',
        'print("K00_V17_SOURCE_HASHES=PASS");',
        'ideal maximal=d0,d1,d2,d3,d4,d5;',
    ]
    for ell in range(1, 8):
        unloaded = v7.unloaded_tail(tails[str(ell)], ell, images)
        lines.append(f"poly rr{ell}={unloaded};")
    lines.extend([
        "int rowaudit=1;",
        "if ((rr1-r1!=0)||(rr2-r2!=0)||(rr3-r3!=0)||(rr4-r4!=0)||(rr5-r5!=0)||(rr6-r6!=0)||(rr7-r7!=0)) { rowaudit=0; }",
        'print("K00_V17_UNLOADED_ROW_AUDIT="+string(rowaudit));',
        'if (rowaudit!=1) { print("K00_V17_FAIL=ROW_SOURCE_MAP"); quit; }',
    ])
    for label, index, _weight in LOADS:
        suffix = label.upper()
        for ell in range(1, 8):
            coefficient = load_coefficient(tails[str(ell)], ell, index, images, v7)
            lines.append(f"poly a{suffix}{ell}={coefficient};")
    lines.extend([
        f"poly h=({h});",
        *(f"poly u{i}=({value});" for i, value in enumerate(multipliers, 1)),
        "poly basereplay=-h*r7+u1*r1+u2*r2+u3*r3+u4*r4+u5*r5+u6*r6;",
        "poly h0=h; h0=subst(h0,d0,0); h0=subst(h0,d1,0); h0=subst(h0,d2,0); h0=subst(h0,d3,0); h0=subst(h0,d4,0); h0=subst(h0,d5,0);",
        'print("K00_V17_BASE_REPLAY="+string(basereplay==0));',
        'print("K00_V17_H_UNIT="+string(h0!=0));',
        'if ((basereplay!=0)||(h0==0)) { print("K00_V17_FAIL=BASE_RELATION"); quit; }',
        "ideal I=r1,r2,r3,r4,r5,r6; ideal A=r1,r2,r3,r4,r5,r6,r7;",
        'print("K00_V17_SYZ6_START");',
        "module T=syz(I); int nt=size(T); int i; int j; poly z;",
        "int treplay=1;",
        "for (j=1; j<=nt; j++) { z=0; for (i=1; i<=6; i++) { z=z+I[i]*T[j][i]; } if (z!=0) { treplay=0; } }",
        'print("K00_V17_SYZ6_DONE");',
        'print("K00_V17_SYZ6_GENERATORS="+string(nt));',
        'print("K00_V17_SYZ6_REPLAY="+string(treplay));',
        'if ((nt<1)||(treplay!=1)) { print("K00_V17_FAIL=SYZ6"); quit; }',
        f"module S87={syz87};",
        "int s87replay=1;",
        "for (j=1; j<=size(S87); j++) { z=0; for (i=1; i<=7; i++) { z=z+S87[j][i]*A[i]; } if (z!=0) { s87replay=0; } }",
        'print("K00_V17_SYZ87_GENERATORS="+string(size(S87)));',
        'print("K00_V17_SYZ87_REPLAY="+string(s87replay));',
        'if ((size(S87)!=87)||(s87replay!=1)) { print("K00_V17_FAIL=SYZ87"); quit; }',
        'write("SYZ6_MODULE.txt",T); write("SYZ87_MODULE.txt",S87);',
    ])
    for label, _index, _weight in LOADS:
        lines.extend(direction_block(label))
    lines.extend([
        'print("K00_V17_ENDPOINT=PASS_THREE_DIRECTION_LOCAL_COKERNEL");',
        "quit;",
    ])
    singular.write_text("\n".join(lines) + "\n")
    result = {
        "status": "PASS-K00-FIRSTORDER-COKERNEL-V17-COMPILER",
        "registered_aws_lane": tag,
        "field": args.field,
        "characteristic": characteristic,
        "order": "dp",
        "tails_sha256": digest(TAILS),
        "canonical_all_tails_sha256": EXPECTED_ALL_TAILS,
        "v7_source_map_sha256": digest(V7),
        "row_prelude_sha256": digest(PRELUDE),
        "syz87_sha256": digest(S87),
        "h_sha256": digest(H),
        "u_sha256": {str(i): digest(path) for i, path in enumerate(U, 1)},
        "v14_result_sha256": digest(V14_RESULT),
        "v16_result_sha256": digest(V16_RESULT),
        "preregistration_sha256": digest(PREREG),
        "input_sha256": digest(singular),
        "load_lambda_weights_deferred": {label: weight for label, _index, weight in LOADS},
        "scope": "THREE_SEPARATE_FIRSTORDER_LOAD_CLASSES_IN_NORMALIZED_LOCAL_COEFFICIENT_RING_ONLY",
    }
    (output / "compiler_result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
