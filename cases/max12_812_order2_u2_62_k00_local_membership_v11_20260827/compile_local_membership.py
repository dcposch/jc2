#!/usr/bin/env python3
"""Compile the exact normalized K00 local-ring membership test, AWS only."""

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
V7 = ROOT / "cases/max12_812_order2_u2_62_k00_unloaded_membership_v7_20260827/compile_unloaded_membership.py"
V9_RESULT = ROOT / "cases/max12_812_order2_u2_62_k00_filtered_macaulay_v9_20260827/RESULT.md"
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    V7: "a7f335cdbc3e5525ce641ff10d8370a52d4cbb9c84e2417b17eea64a38154f70",
    V9_RESULT: "bd1c636827061f1506573487618e533f34cfe413eab042be65411bfaa2eef178",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    PREREG: "4d4c9569aec1f8776c9099da9f86d0fa998ee6aace409c870efa66c9410afd6f",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only local membership compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only local membership compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v7():
    spec = importlib.util.spec_from_file_location("k00_v7_frozen", V7)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V7 source map")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path: Path, tails: dict[str, list[list[object]]], v7) -> None:
    images = v7.coefficient_images("normalized")
    lines = [
        'ring R=0,(d0,d1,d2,d3,d4,d5,h),ds;',
        'option(redSB);',
        'print("K00_LOCAL_MODE=KUMMER_NORMALIZED_C6_1_DS");',
        'print("K00_LOCAL_SOURCE_HASHES=PASS");',
        'ideal toyI=(1+d0)*d1;',
        'ideal toyG=std(toyI);',
        'int toy_positive=(reduce(d1,toyG)==0);',
        'int toy_negative=(reduce(d2,toyG)!=0);',
        'matrix toyU; matrix toyL=lift(toyI,ideal(d1),toyU);',
        'matrix toyReplay=matrix(ideal(d1))*toyU-matrix(toyI)*toyL;',
        'poly toyUnit=toyU[1,1];',
        'toyUnit=subst(toyUnit,d0,0); toyUnit=subst(toyUnit,d1,0); toyUnit=subst(toyUnit,d2,0);',
        'toyUnit=subst(toyUnit,d3,0); toyUnit=subst(toyUnit,d4,0); toyUnit=subst(toyUnit,d5,0);',
        'int toy_replay=(toyReplay==0); int toy_unit=(toyUnit!=0);',
        'print("K00_LOCAL_TOY_POSITIVE="+string(toy_positive));',
        'print("K00_LOCAL_TOY_NEGATIVE="+string(toy_negative));',
        'print("K00_LOCAL_TOY_REPLAY="+string(toy_replay));',
        'print("K00_LOCAL_TOY_UNIT="+string(toy_unit));',
        'if (toy_positive*toy_negative*toy_replay*toy_unit!=1) { print("K00_LOCAL_FAIL=TOY_SEMANTICS"); quit; }',
    ]
    for ell in range(1, 8):
        lines.append(f"poly r{ell}={v7.unloaded_tail(tails[str(ell)], ell, images)};")
    lines.extend([
        'ideal I=r1,r2,r3,r4,r5,r6;',
        'print("K00_LOCAL_STD_START");',
        'matrix T; ideal G=liftstd(I,T);',
        'print("K00_LOCAL_STD_DONE");',
        'int basis_replay=(matrix(G)-matrix(I)*T==0);',
        'int proper=(reduce(1,G)!=0);',
        'print("K00_LOCAL_G_SIZE="+string(size(G)));',
        'print("K00_LOCAL_G_DIM="+string(dim(G)));',
        'print("K00_LOCAL_BASIS_REPLAY="+string(basis_replay));',
        'print("K00_LOCAL_NEGATIVE_CONTROL_PROPER="+string(proper));',
        'if (basis_replay*proper!=1) { print("K00_LOCAL_FAIL=BASIS_OR_PROPERNESS"); quit; }',
        'write("LOCAL_STANDARD_BASIS.txt",G);',
        'write("LOCAL_BASIS_TRANSFORM.txt",T);',
        'poly residual=reduce(r7,G);',
        'int member=(residual==0);',
        'print("K00_LOCAL_MEMBER="+string(member));',
        'if (member==1)',
        '{',
        '  matrix U; matrix HG=lift(G,ideal(r7),U); matrix L=T*HG;',
        '  matrix replay=matrix(ideal(r7))*U-matrix(I)*L;',
        '  int replay_ok=(replay==0);',
        '  poly unit=U[1,1];',
        '  unit=subst(unit,d0,0); unit=subst(unit,d1,0); unit=subst(unit,d2,0);',
        '  unit=subst(unit,d3,0); unit=subst(unit,d4,0); unit=subst(unit,d5,0);',
        '  int unit_ok=(unit!=0);',
        '  print("K00_LOCAL_LIFT_REPLAY="+string(replay_ok));',
        '  print("K00_LOCAL_UNIT_CONSTANT_NONZERO="+string(unit_ok));',
        '  if (replay_ok*unit_ok!=1) { print("K00_LOCAL_FAIL=LIFT_OR_UNIT"); quit; }',
        '  write("LOCAL_MEMBERSHIP_MULTIPLIERS.txt",L);',
        '  write("LOCAL_MEMBERSHIP_UNIT.txt",U);',
        '  print("K00_LOCAL_EVIDENCE=UNIT_DENOMINATOR_LIFT");',
        '}',
        'else',
        '{',
        '  write("LOCAL_NONMEMBERSHIP_RESIDUAL.txt",residual);',
        '  poly scaled=residual;',
        '  scaled=subst(scaled,d0,h*d0); scaled=subst(scaled,d1,h*d1);',
        '  scaled=subst(scaled,d2,h*d2); scaled=subst(scaled,d3,h*d3);',
        '  scaled=subst(scaled,d4,h*d4); scaled=subst(scaled,d5,h*d5);',
        '  matrix slices=coeffs(scaled,h);',
        '  int j; int lowest=-1; poly leading=0;',
        '  for (j=1; j<=nrows(slices); j++) { if ((lowest<0)&&(slices[j,1]!=0)) { lowest=j-1; leading=slices[j,1]; } }',
        '  print("K00_LOCAL_LOWEST_TRANSVERSE_DEGREE="+string(lowest));',
        '  print("K00_LOCAL_LEADING_TERMS="+string(size(leading)));',
        '  if (lowest<0) { print("K00_LOCAL_FAIL=NONMEMBERSHIP_TELEMETRY"); quit; }',
        '  write("LOCAL_LEADING_TRANSVERSE_CLASS.txt",leading);',
        '  print("K00_LOCAL_LIFT_REPLAY=NOT_APPLICABLE");',
        '  print("K00_LOCAL_EVIDENCE=LOCAL_RESIDUAL");',
        '}',
        'print("K00_LOCAL_ENDPOINT=PASS_MEMBERSHIP_DECISION");',
        'quit;',
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if expected == "TO_BE_FROZEN" or digest(path) != expected:
            fail(("frozen source mismatch", str(path), digest(path), expected))
    v7 = load_v7()
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / "k00_local_membership_q.sing"
    emit(singular, tails, v7)
    result = {
        "status": "PASS-K00-LOCAL-MEMBERSHIP-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": 0,
        "order": "ds",
        "v7_source_map_sha256": digest(V7),
        "v9_result_sha256": digest(V9_RESULT),
        "tails_sha256": digest(TAILS),
        "canonical_all_tails_sha256": EXPECTED_ALL_TAILS,
        "preregistration_sha256": digest(PREREG),
        "input_sha256": digest(singular),
        "scope": "NORMALIZED_K00_LOCAL_RING_UNLOADED_MEMBERSHIP_ONLY",
    }
    (output / "compiler_result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
