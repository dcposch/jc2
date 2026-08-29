#!/usr/bin/env python3
"""Compile the proof-carrying normalized K00 colon/local test, AWS only."""

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
V8 = ROOT / "cases/max12_812_order2_u2_62_k00_unloaded_membership_v8_20260827/compile_unloaded_membership_v8.py"
V8_RESULT = ROOT / "cases/max12_812_order2_u2_62_k00_unloaded_membership_v8_20260827/RESULT.md"
V8_NORMALIZED = ROOT / "cases/max12_812_order2_u2_62_k00_unloaded_membership_v8_20260827/aws_normalized_q_r6d_pass/run/RESULT.json"
V8V9_REVIEW = ROOT / "xmodel/max12-812-order2-k00-v8-v9-hostile-review-grok-20260827.md"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    V8: "a1c4b18c65c053c4365a0b198aa5139206babaccbf02f37e7834583bb7714012",
    V8_RESULT: "d3adc56fdbe98e68260489a265f1bbb34a1e062c0ee1fbb4ba6e961d157d3892",
    V8_NORMALIZED: "8203925767d3fb08d73b1bebfada3c72cb6cc674b6658ccbcb1862aacc7127fc",
    V8V9_REVIEW: "6c4ebd6d61189e0f80fd9021edd509cbb323826774644d92828a0badd0943a29",
    PREREG: "144ff8f46c1d9bc2ef81d2aaa4a454ecb0d772ed345c91f3d446aa830871ea89",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only colon compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only colon compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v8():
    spec = importlib.util.spec_from_file_location("k00_v8_frozen_for_colon", V8)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V8 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]], v7) -> None:
    images = v7.coefficient_images("normalized")
    lines = [
        f"ring R={characteristic},(d0,d1,d2,d3,d4,d5),dp;",
        'print("K00_COLON_MODE=NORMALIZED_C6_1_GLOBAL_DP");',
        'print("K00_COLON_SOURCE_HASHES=PASS");',
        'ideal maximal=d0,d1,d2,d3,d4,d5;',
        'ideal toyI=(1+d0)*d1;',
        'ideal toyG=std(toyI);',
        'int toy_global_nonmember=(reduce(d1,toyG)!=0);',
        'ideal toyCp=quotient(toyI,ideal(d1));',
        'ideal toyCn=quotient(toyI,ideal(d2));',
        'int toy_local_member=(reduce(1,std(toyCp+maximal))==0);',
        'int toy_local_nonmember=(reduce(1,std(toyCn+maximal))!=0);',
        'ideal toyTarget=toyCp[1]*d1;',
        'matrix toyL=lift(toyI,toyTarget);',
        'int toy_replay=(toyTarget[1]-toyI[1]*toyL[1,1]==0);',
        'print("K00_COLON_TOY_GLOBAL_NONMEMBER="+string(toy_global_nonmember));',
        'print("K00_COLON_TOY_LOCAL_MEMBER="+string(toy_local_member));',
        'print("K00_COLON_TOY_LOCAL_NONMEMBER="+string(toy_local_nonmember));',
        'print("K00_COLON_TOY_REPLAY="+string(toy_replay));',
        'if (toy_global_nonmember*toy_local_member*toy_local_nonmember*toy_replay!=1) { print("K00_COLON_FAIL=TOY"); quit; }',
    ]
    for ell in range(1, 8):
        lines.append(f"poly r{ell}={v7.unloaded_tail(tails[str(ell)], ell, images)};")
    lines.extend([
        'ideal I=r1,r2,r3,r4,r5,r6;',
        'ideal G=std(I);',
        'int proper=(reduce(1,G)!=0);',
        'int global_nonmember=(reduce(r7,G)!=0);',
        'print("K00_COLON_SOURCE_PROPER="+string(proper));',
        'print("K00_COLON_GLOBAL_NONMEMBER="+string(global_nonmember));',
        'if (proper*global_nonmember!=1) { print("K00_COLON_FAIL=GLOBAL_CONTROL"); quit; }',
        'print("K00_COLON_QUOTIENT_START");',
        'ideal C=quotient(I,ideal(r7));',
        'ideal GC=std(C);',
        'print("K00_COLON_QUOTIENT_DONE");',
        'int colon_proper=(reduce(1,GC)!=0);',
        'print("K00_COLON_GENERATORS="+string(size(C)));',
        'print("K00_COLON_PROPER="+string(colon_proper));',
        'if ((size(C)<1)||(colon_proper!=1)) { print("K00_COLON_FAIL=COLON_PROPERNESS"); quit; }',
        'print("K00_COLON_SYZ_START");',
        'ideal A=r1,r2,r3,r4,r5,r6,r7;',
        'module S=syz(A);',
        'if (size(S)<1) { print("K00_COLON_FAIL=EMPTY_SYZ"); quit; }',
        'ideal P=S[1][7];',
        'int j; int i;',
        'for (j=2; j<=size(S); j++) { P[j]=S[j][7]; }',
        'ideal GP=std(P);',
        'int projection_equal=1;',
        'for (j=1; j<=size(C); j++) { if (reduce(C[j],GP)!=0) { projection_equal=0; } }',
        'for (j=1; j<=size(P); j++) { if (reduce(P[j],GC)!=0) { projection_equal=0; } }',
        'int syz_replay=1; poly z;',
        'for (j=1; j<=size(S); j++)',
        '{',
        '  z=0;',
        '  for (i=1; i<=7; i++) { z=z+A[i]*S[j][i]; }',
        '  if (z!=0) { syz_replay=0; }',
        '}',
        'print("K00_COLON_SYZ_DONE");',
        'print("K00_COLON_SYZ_GENERATORS="+string(size(S)));',
        'print("K00_COLON_PROJECTION_EQUAL="+string(projection_equal));',
        'print("K00_COLON_SYZ_REPLAY="+string(syz_replay));',
        'if (projection_equal*syz_replay!=1) { print("K00_COLON_FAIL=SYZ_PROJECTION"); quit; }',
        'ideal Targets=C[1]*r7;',
        'for (j=2; j<=size(C); j++) { Targets[j]=C[j]*r7; }',
        'matrix L=lift(I,Targets);',
        'int colon_lift_replay=1;',
        'for (j=1; j<=size(C); j++)',
        '{',
        '  z=-Targets[j];',
        '  for (i=1; i<=6; i++) { z=z+I[i]*L[i,j]; }',
        '  if (z!=0) { colon_lift_replay=0; }',
        '}',
        'print("K00_COLON_LIFT_REPLAY="+string(colon_lift_replay));',
        'if (colon_lift_replay!=1) { print("K00_COLON_FAIL=COLON_LIFT"); quit; }',
        'ideal Gopen=std(C+maximal);',
        'int local_member=(reduce(1,Gopen)==0);',
        'int witness_index=0; int all_constants_zero=1; poly c;',
        'for (j=1; j<=size(C); j++)',
        '{',
        '  c=C[j];',
        '  c=subst(c,d0,0); c=subst(c,d1,0); c=subst(c,d2,0);',
        '  c=subst(c,d3,0); c=subst(c,d4,0); c=subst(c,d5,0);',
        '  if ((c!=0)&&(witness_index==0)) { witness_index=j; }',
        '  if (c!=0) { all_constants_zero=0; }',
        '}',
        'int constant_consistency=((local_member==1)&&(witness_index>0))||((local_member==0)&&(all_constants_zero==1));',
        'print("K00_COLON_LOCAL_MEMBER="+string(local_member));',
        'print("K00_COLON_CONSTANT_CONSISTENCY="+string(constant_consistency));',
        'if (constant_consistency!=1) { print("K00_COLON_FAIL=CONSTANT_ATTAINABILITY"); quit; }',
        'write("COLON_GENERATORS.txt",C);',
        'write("COLON_STANDARD_BASIS.txt",GC);',
        'write("COLON_LIFTS.txt",L);',
        'write("SYZYGY_MODULE.txt",S);',
        'write("SYZYGY_PROJECTION.txt",P);',
        'if (local_member==1)',
        '{',
        '  poly h=C[witness_index];',
        '  write("LOCAL_UNIT_WITNESS.txt",h);',
        '  print("K00_COLON_WITNESS_CONSTANT_NONZERO=1");',
        '  print("K00_COLON_EVIDENCE=UNIT_COLON_WITNESS");',
        '}',
        'else',
        '{',
        '  print("K00_COLON_ALL_GENERATOR_CONSTANTS_ZERO="+string(all_constants_zero));',
        '  print("K00_COLON_EVIDENCE=COLON_CONTAINED_IN_MAXIMAL");',
        '}',
        'print("K00_COLON_ENDPOINT=PASS_LOCAL_DECISION");',
        'quit;',
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--field", choices=("Q", "65521"), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if expected == "TO_BE_FROZEN" or digest(path) != expected:
            fail(("frozen source mismatch", str(path), digest(path), expected))
    v8 = load_v8()
    for path, expected in v8.EXPECTED.items():
        if digest(path) != expected:
            fail(("V8 transitive source mismatch", str(path), digest(path), expected))
    v7 = v8.load_v7()
    tails = json.loads(v8.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v8.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    characteristic = 0 if args.field == "Q" else 65521
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"k00_colon_local_{args.field}.sing"
    emit(singular, characteristic, tails, v7)
    result = {
        "status": "PASS-K00-COLON-LOCAL-COMPILER",
        "registered_aws_lane": tag,
        "field": args.field,
        "characteristic": characteristic,
        "order": "dp",
        "v8_compiler_sha256": digest(V8),
        "v8_result_sha256": digest(V8_RESULT),
        "v8_normalized_result_sha256": digest(V8_NORMALIZED),
        "v8_v9_review_sha256": digest(V8V9_REVIEW),
        "preregistration_sha256": digest(PREREG),
        "input_sha256": digest(singular),
        "scope": "NORMALIZED_K00_UNLOADED_LOCAL_MEMBERSHIP_BY_GLOBAL_COLON_ONLY",
    }
    (output / "compiler_result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
