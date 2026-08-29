#!/usr/bin/env python3
"""Compile repaired exact unloaded K00 membership/telemetry lanes on AWS."""

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
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"
DESIGN = ROOT / "xmodel/max12-812-order2-p0-k00-honest-source-discriminator-design-sol-20260827.md"
QUADRATIC = ROOT / "cases/max12_812_order2_u2_62_k00_normal_quadratic_v6_20260827/RESULT.md"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    V7: "a7f335cdbc3e5525ce641ff10d8370a52d4cbb9c84e2417b17eea64a38154f70",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    ONEPARAM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    DESIGN: "9c5bf1229cf45dd7ea4d5d3907fd6033c88c0d9768934d01ea79e658f3d65a17",
    QUADRATIC: "9b95409aafdd10346ca1095047bd1ea5ebbdd6ca23e2b5a7e29323e01e8e5909",
    PREREG: "fe085951e6a5a9e23f33a6af37d0ab1861221831a4c22a026f06428d55d54ea0",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V8 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V8 compiler refused non-Amazon host")
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


def emit(path: Path, mode: str, tails: dict[str, list[list[object]]], v7) -> None:
    images = v7.coefficient_images(mode)
    if mode == "direct":
        variables = "t,C6,d0,d1,d2,d3,d4,d5,h"
        localizer_generator = ",1-t*C6"
        label = "DIRECT_LOCALIZED"
    else:
        variables = "d0,d1,d2,d3,d4,d5,h"
        localizer_generator = ""
        label = "KUMMER_NORMALIZED_C6_1"
    lines = [
        'LIB "elim.lib";',
        f"ring R=0,({variables}),dp;",
        f'print("K00_UNLOADED_V8_MODE={label}");',
        'print("K00_UNLOADED_V8_SOURCE_HASHES=PASS");',
        'print("K00_UNLOADED_V8_LOADS_REMOVED_BY_LITERAL_ZERO_SPECIALIZATION=PASS");',
    ]
    for ell in range(1, 8):
        lines.append(f"poly r{ell}={v7.unloaded_tail(tails[str(ell)], ell, images)};")
    lines.extend([
        f"ideal I=r1,r2,r3,r4,r5,r6{localizer_generator};",
        'print("K00_UNLOADED_V8_STD_START");',
        "ideal G=std(I);",
        'print("K00_UNLOADED_V8_STD_DONE");',
        'print("K00_UNLOADED_V8_G_SIZE="+string(size(G)));',
        'print("K00_UNLOADED_V8_G_DIM="+string(dim(G)));',
        "int proper=(reduce(1,G)!=0);",
        'print("K00_UNLOADED_V8_NEGATIVE_CONTROL_PROPER="+string(proper));',
        'if (proper!=1) { print("K00_UNLOADED_V8_FAIL=SOURCE_IDEAL_UNIT"); quit; }',
        "poly residual=reduce(r7,G);",
        "int member=(residual==0);",
        'print("K00_UNLOADED_V8_MEMBER="+string(member));',
        'write("STANDARD_BASIS.txt",G);',
        "if (member==1)",
        "{",
        "  matrix L=lift(I,ideal(r7));",
        "  poly replay=-r7;",
        "  int j;",
        "  for (j=1; j<=size(I); j++) { replay=replay+L[j,1]*I[j]; }",
        "  int replay_ok=(replay==0);",
        '  print("K00_UNLOADED_V8_LIFT_REPLAY="+string(replay_ok));',
        '  if (replay_ok!=1) { print("K00_UNLOADED_V8_FAIL=LIFT_REPLAY"); quit; }',
        '  write("MEMBERSHIP_LIFT.txt",L);',
        '  print("K00_UNLOADED_V8_EVIDENCE=LIFT");',
        "}",
        "else",
        "{",
        '  write("NONMEMBERSHIP_RESIDUAL.txt",residual);',
        "  poly scaled=residual;",
        "  scaled=subst(scaled,d0,h*d0);",
        "  scaled=subst(scaled,d1,h*d1);",
        "  scaled=subst(scaled,d2,h*d2);",
        "  scaled=subst(scaled,d3,h*d3);",
        "  scaled=subst(scaled,d4,h*d4);",
        "  scaled=subst(scaled,d5,h*d5);",
        "  matrix slices=coeffs(scaled,h);",
        "  int j; int lowest=-1; poly leading=0; poly reconstructed=0;",
        "  for (j=1; j<=nrows(slices); j++)",
        "  {",
        "    reconstructed=reconstructed+h^(j-1)*slices[j,1];",
        "    if ((lowest<0) && (slices[j,1]!=0)) { lowest=j-1; leading=slices[j,1]; }",
        "  }",
        "  int decomposition_ok=(scaled-reconstructed==0);",
        "  poly leading_scaled=leading;",
        "  leading_scaled=subst(leading_scaled,d0,h*d0);",
        "  leading_scaled=subst(leading_scaled,d1,h*d1);",
        "  leading_scaled=subst(leading_scaled,d2,h*d2);",
        "  leading_scaled=subst(leading_scaled,d3,h*d3);",
        "  leading_scaled=subst(leading_scaled,d4,h*d4);",
        "  leading_scaled=subst(leading_scaled,d5,h*d5);",
        "  int homogeneous_ok=(leading_scaled-h^lowest*leading==0);",
        '  print("K00_UNLOADED_V8_TRANSVERSE_DECOMPOSITION="+string(decomposition_ok));',
        '  print("K00_UNLOADED_V8_LEADING_HOMOGENEOUS="+string(homogeneous_ok));',
        '  if ((lowest<0) || (decomposition_ok!=1) || (homogeneous_ok!=1)) { print("K00_UNLOADED_V8_FAIL=TRANSVERSE_TELEMETRY"); quit; }',
        '  print("K00_UNLOADED_V8_RESIDUAL_TERMS="+string(size(residual)));',
        '  print("K00_UNLOADED_V8_LOWEST_TRANSVERSE_DEGREE="+string(lowest));',
        '  print("K00_UNLOADED_V8_LEADING_TERMS="+string(size(leading)));',
        '  write("LEADING_TRANSVERSE_CLASS.txt",leading);',
        '  print("K00_UNLOADED_V8_LIFT_REPLAY=NOT_APPLICABLE");',
        '  print("K00_UNLOADED_V8_EVIDENCE=RESIDUAL_AND_LEADING_CLASS");',
        "}",
        'print("K00_UNLOADED_V8_ENDPOINT=PASS_MEMBERSHIP_DECISION");',
        "quit;",
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
    v7 = load_v7()
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    if sorted(tails) != [str(i) for i in range(1, 8)]:
        fail("tail key mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"k00_unloaded_v8_{args.mode}_q.sing"
    emit(singular, args.mode, tails, v7)
    result = {
        "status": "PASS-K00-UNLOADED-V8-COMPILER",
        "registered_aws_lane": tag,
        "mode": args.mode,
        "characteristic": 0,
        "tails_sha256": digest(TAILS),
        "canonical_all_tails_sha256": EXPECTED_ALL_TAILS,
        "v7_source_map_sha256": digest(V7),
        "oneparameter_sha256": digest(ONEPARAM),
        "design_sha256": digest(DESIGN),
        "quadratic_result_sha256": digest(QUADRATIC),
        "preregistration_sha256": digest(PREREG),
        "input_sha256": digest(singular),
        "scope": "UNLOADED_K00_ROW7_MEMBERSHIP_AND_FROZEN_NORMAL_FORM_TELEMETRY_ONLY",
    }
    (output / "compiler_result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
