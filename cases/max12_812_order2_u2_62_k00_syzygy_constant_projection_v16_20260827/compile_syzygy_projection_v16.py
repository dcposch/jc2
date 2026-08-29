#!/usr/bin/env python3
"""Compile exact K00 syzygy constant projection, on registered AWS only."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
R1 = ROOT / "cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827"
PREREG = HERE / "PREREGISTRATION.md"
R1_RESULT = R1 / "aws_q_box01_pass/run/RESULT.json"
R1_PRELUDE = R1 / "aws_q_box01_pass/compiled/serialized_replay_prelude_Q.sing"
R1_SYZ = R1 / "aws_q_box01_pass/run/artifacts/SYZYGY_MODULE.txt"
EXPECTED = {
    R1_RESULT: "28be0ddf9d12529586817e6a7e96cb3ff2bc8e84e4983f7c2f25366f81b4f7e2",
    R1_PRELUDE: "5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a",
    R1_SYZ: "788a836b729d3de5e9600de07244b5d4b836c91a7538e0b1e4ef307ad86d21fb",
    PREREG: "1bf2dc8c7acc8b004a66fa3376b04f2bc73af6031eb134963b20ff7ce9788725",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V16 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V16 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--field", choices=("Q", "65521"), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if expected == "TO_BE_FROZEN" or digest(path) != expected:
            fail(("frozen source mismatch", str(path), digest(path), expected))
    prior = json.loads(R1_RESULT.read_text())
    if prior.get("local_member") is not True or prior.get("field") != "Q":
        fail("R1 exact endpoint sentinel mismatch")
    prelude = R1_PRELUDE.read_text()
    if prelude.count("ring R=0,") != 1 or sum(prelude.count(f"poly r{i}=") for i in range(1, 8)) != 7:
        fail("malformed frozen row prelude")
    characteristic = 0 if args.field == "Q" else 65521
    if characteristic:
        prelude = prelude.replace("ring R=0,", f"ring R={characteristic},", 1)
    syz = R1_SYZ.read_text().strip()
    if not syz or ";" in syz or "gen(7)" not in syz:
        fail("malformed frozen syzygy serialization")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"k00_syzygy_projection_v16_{args.field}.sing"
    lines = [
        prelude.rstrip(),
        f'print("K00_SYZPROJ_FIELD={args.field}");',
        f"module S={syz};",
        "ideal A=r1,r2,r3,r4,r5,r6,r7;",
        "int n=size(S); int i; int j; poly z; poly e; string fn;",
        'print("K00_SYZPROJ_GENERATORS="+string(n));',
        'if (n!=87) { print("K00_SYZPROJ_FAIL=GENERATOR_COUNT"); quit; }',
        "int all_replay=1;",
        "for (j=1; j<=n; j++)",
        "{",
        "  z=0; for (i=1; i<=7; i++) { z=z+A[i]*S[j][i]; }",
        "  if (z!=0) { all_replay=0; }",
        "}",
        'print("K00_SYZPROJ_ALL_SYZ_REPLAY="+string(all_replay));',
        'if (all_replay!=1) { print("K00_SYZPROJ_FAIL=SYZ_REPLAY"); quit; }',
        "matrix E[7][87];",
        "for (j=1; j<=n; j++)",
        "{",
        "  for (i=1; i<=7; i++)",
        "  {",
        "    e=S[j][i];",
        "    e=subst(e,d0,0); e=subst(e,d1,0); e=subst(e,d2,0);",
        "    e=subst(e,d3,0); e=subst(e,d4,0); e=subst(e,d5,0);",
        "    E[i,j]=e; fn=\"SYZ_CONSTANT_\"+string(i)+\"_\"+string(j)+\".txt\"; write(fn,e);",
        "  }",
        "}",
        "int c2zero=1; int c4zero=1;",
        "for (j=1; j<=n; j++) { if (E[2,j]!=0) { c2zero=0; } if (E[4,j]!=0) { c4zero=0; } }",
        'print("K00_SYZPROJ_COORD2_ALL_ZERO="+string(c2zero));',
        'print("K00_SYZPROJ_COORD4_ALL_ZERO="+string(c4zero));',
        "int base_index=0;",
        "for (j=1; j<=n; j++) { if ((base_index==0)&&(E[7,j]!=0)) { base_index=j; } }",
        'if (base_index==0) { print("K00_SYZPROJ_FAIL=NO_UNIT_BASE"); quit; }',
        "int freedom_index=0; poly determinant;",
        "for (j=1; j<=n; j++)",
        "{",
        "  determinant=E[6,j]*E[7,base_index]-E[6,base_index]*E[7,j];",
        "  if ((freedom_index==0)&&(determinant!=0)) { freedom_index=j; }",
        "}",
        'if (freedom_index==0) { print("K00_SYZPROJ_FAIL=NO_COORD6_FREEDOM"); quit; }',
        "vector base=S[base_index];",
        "vector freedom=E[7,base_index]*S[freedom_index]-E[7,freedom_index]*S[base_index];",
        "poly base7=base[7]; poly freedom7=freedom[7]; poly freedom6=freedom[6];",
        "base7=subst(base7,d0,0); base7=subst(base7,d1,0); base7=subst(base7,d2,0); base7=subst(base7,d3,0); base7=subst(base7,d4,0); base7=subst(base7,d5,0);",
        "freedom7=subst(freedom7,d0,0); freedom7=subst(freedom7,d1,0); freedom7=subst(freedom7,d2,0); freedom7=subst(freedom7,d3,0); freedom7=subst(freedom7,d4,0); freedom7=subst(freedom7,d5,0);",
        "freedom6=subst(freedom6,d0,0); freedom6=subst(freedom6,d1,0); freedom6=subst(freedom6,d2,0); freedom6=subst(freedom6,d3,0); freedom6=subst(freedom6,d4,0); freedom6=subst(freedom6,d5,0);",
        "poly base_replay=0; poly freedom_replay=0;",
        "for (i=1; i<=7; i++)",
        "{",
        "  base_replay=base_replay+A[i]*base[i]; freedom_replay=freedom_replay+A[i]*freedom[i];",
        "  fn=\"BASE_SYZYGY_\"+string(i)+\".txt\"; write(fn,base[i]);",
        "  fn=\"FREEDOM_SYZYGY_\"+string(i)+\".txt\"; write(fn,freedom[i]);",
        "}",
        "int base_replay_ok=(base_replay==0); int freedom_replay_ok=(freedom_replay==0);",
        "int base_unit=(base7!=0); int freedom7zero=(freedom7==0); int freedom6unit=(freedom6!=0);",
        'write("BASE7_CONSTANT.txt",base7); write("FREEDOM7_CONSTANT.txt",freedom7); write("FREEDOM6_CONSTANT.txt",freedom6);',
        'print("K00_SYZPROJ_BASE_INDEX="+string(base_index));',
        'print("K00_SYZPROJ_FREEDOM_INDEX="+string(freedom_index));',
        'print("K00_SYZPROJ_BASE7_CONSTANT="+string(base7));',
        'print("K00_SYZPROJ_FREEDOM7_CONSTANT="+string(freedom7));',
        'print("K00_SYZPROJ_FREEDOM6_CONSTANT="+string(freedom6));',
        'print("K00_SYZPROJ_BASE_REPLAY="+string(base_replay_ok));',
        'print("K00_SYZPROJ_FREEDOM_REPLAY="+string(freedom_replay_ok));',
        'print("K00_SYZPROJ_BASE7_UNIT="+string(base_unit));',
        'print("K00_SYZPROJ_FREEDOM7_ZERO="+string(freedom7zero));',
        'print("K00_SYZPROJ_FREEDOM6_UNIT="+string(freedom6unit));',
        "if (base_replay_ok*freedom_replay_ok*base_unit*freedom7zero*freedom6unit!=1) { print(\"K00_SYZPROJ_FAIL=WITNESS\"); quit; }",
        'print("K00_SYZPROJ_ENDPOINT=PASS_SERIALIZED_CONSTANT_PROJECTION");',
        "quit;",
    ]
    singular.write_text("\n".join(lines) + "\n")
    replay_prelude = output / f"serialized_replay_prelude_{args.field}.sing"
    replay_prelude.write_text(prelude)
    result = {
        "status": "PASS-K00-SYZPROJ-V16-COMPILER",
        "registered_aws_lane": tag,
        "field": args.field,
        "characteristic": characteristic,
        "order": "dp",
        "r1_result_sha256": digest(R1_RESULT),
        "row_prelude_sha256": digest(R1_PRELUDE),
        "syzygy_module_sha256": digest(R1_SYZ),
        "preregistration_sha256": digest(PREREG),
        "input_sha256": digest(singular),
        "replay_prelude_sha256": digest(replay_prelude),
        "scope": "UNLOADED_K00_LOCAL_SYZYGY_CONSTANT_PROJECTION_ONLY",
    }
    (output / "compiler_result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
