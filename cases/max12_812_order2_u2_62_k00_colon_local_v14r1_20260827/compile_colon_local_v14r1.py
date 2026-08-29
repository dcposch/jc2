#!/usr/bin/env python3
"""Compile V14R1 complete lift serialization, on registered AWS only."""

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
V14 = ROOT / "cases/max12_812_order2_u2_62_k00_colon_local_v14_20260827/compile_colon_local.py"
V14_PREREG = ROOT / "cases/max12_812_order2_u2_62_k00_colon_local_v14_20260827/PREREGISTRATION.md"
V14_EXACT = ROOT / "cases/max12_812_order2_u2_62_k00_colon_local_v14_20260827/aws_q_box01_pass/run/RESULT.json"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    V14: "d801d5518704aba4e1ccc738805506057526cea1875b2c7afdd62d4e3f17b2df",
    V14_PREREG: "144ff8f46c1d9bc2ef81d2aaa4a454ecb0d772ed345c91f3d446aa830871ea89",
    V14_EXACT: "562943e3fa7ff01ecffb00161bf2f71317d0353f7d82e1628a79a47f3a47bbe1",
    PREREG: "65ee7849741bd64adbb842139f12d538e63337aa9cd3c4d6c8c89c49782bbbfd",
}
EXPECTED_BASE_INPUT = {
    "Q": "a57c05c5b0fa144dc421330cec809b8a44061960f4c98a8abe29c9870e666bfe",
    "65521": "266a85a120eca8d74ffc185688119006d529f1f2e83ae98f47f9aedb9e003a34",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V14R1 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V14R1 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v14():
    spec = importlib.util.spec_from_file_location("k00_v14_frozen_for_r1", V14)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V14 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--field", choices=("Q", "65521"), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if expected == "TO_BE_FROZEN" or digest(path) != expected:
            fail(("frozen source mismatch", str(path), digest(path), expected))
    prior = json.loads(V14_EXACT.read_text())
    if prior.get("local_member") is not True or prior.get("field") != "Q":
        fail("V14 exact positive endpoint sentinel mismatch")
    v14 = load_v14()
    for path, expected in v14.EXPECTED.items():
        if digest(path) != expected:
            fail(("V14 transitive source mismatch", str(path), digest(path), expected))
    v8 = v14.load_v8()
    for path, expected in v8.EXPECTED.items():
        if digest(path) != expected:
            fail(("V8 transitive source mismatch", str(path), digest(path), expected))
    tails = json.loads(v8.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v8.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    characteristic = 0 if args.field == "Q" else 65521
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"k00_colon_local_v14r1_{args.field}.sing"
    v14.emit(singular, characteristic, tails, v8.load_v7())
    base_text = singular.read_text()
    base_sha = sha256(base_text.encode()).hexdigest()
    if base_sha != EXPECTED_BASE_INPUT[args.field]:
        fail(("V14 base input mismatch", args.field, base_sha, EXPECTED_BASE_INPUT[args.field]))
    needle = 'write("COLON_LIFTS.txt",L);\n'
    if base_text.count(needle) != 1:
        fail(("nonunique V14 matrix-write site", base_text.count(needle)))
    addition = "\n".join([
        'write("COLON_LIFTS.txt",L);',
        'int lift_rows=nrows(L); int lift_columns=ncols(L);',
        'print("K00_COLON_R1_LIFT_ROWS="+string(lift_rows));',
        'print("K00_COLON_R1_LIFT_COLUMNS="+string(lift_columns));',
        'if ((lift_rows!=6)||(lift_columns!=6)) { print("K00_COLON_FAIL=R1_LIFT_SHAPE"); quit; }',
        'string entry_file;',
        'for (i=1; i<=6; i++)',
        '{',
        '  for (j=1; j<=6; j++)',
        '  {',
        '    entry_file="COLON_LIFT_"+string(i)+"_"+string(j)+".txt";',
        '    write(entry_file,L[i,j]);',
        '  }',
        '}',
        'if ((local_member!=1)||(witness_index<1)) { print("K00_COLON_FAIL=R1_EXPECTED_UNIT_WITNESS"); quit; }',
        'poly chosen_h=C[witness_index]; poly chosen_replay=-chosen_h*r7;',
        'for (i=1; i<=6; i++)',
        '{',
        '  chosen_replay=chosen_replay+I[i]*L[i,witness_index];',
        '  entry_file="UNIT_MULTIPLIER_"+string(i)+".txt";',
        '  write(entry_file,L[i,witness_index]);',
        '}',
        'poly chosen_constant=chosen_h;',
        'chosen_constant=subst(chosen_constant,d0,0); chosen_constant=subst(chosen_constant,d1,0);',
        'chosen_constant=subst(chosen_constant,d2,0); chosen_constant=subst(chosen_constant,d3,0);',
        'chosen_constant=subst(chosen_constant,d4,0); chosen_constant=subst(chosen_constant,d5,0);',
        'int chosen_replay_ok=(chosen_replay==0); int chosen_unit_ok=(chosen_constant!=0);',
        'write("LOCAL_UNIT_WITNESS_R1.txt",chosen_h);',
        'print("K00_COLON_R1_WITNESS_INDEX="+string(witness_index));',
        'print("K00_COLON_R1_EXPLICIT_IDENTITY_REPLAY="+string(chosen_replay_ok));',
        'print("K00_COLON_R1_EXPLICIT_UNIT="+string(chosen_unit_ok));',
        'if (chosen_replay_ok*chosen_unit_ok!=1) { print("K00_COLON_FAIL=R1_EXPLICIT_IDENTITY"); quit; }',
    ]) + "\n"
    repaired = base_text.replace(needle, addition, 1)
    singular.write_text(repaired)

    prelude_lines = [line for line in base_text.splitlines() if line.startswith("ring R=") or any(line.startswith(f"poly r{i}=") for i in range(1, 8))]
    if len(prelude_lines) != 8:
        fail(("serialized replay prelude extraction", len(prelude_lines)))
    prelude = output / f"serialized_replay_prelude_{args.field}.sing"
    prelude.write_text("\n".join(prelude_lines) + "\n")
    result = {
        "status": "PASS-K00-COLON-LOCAL-V14R1-COMPILER",
        "registered_aws_lane": tag,
        "field": args.field,
        "characteristic": characteristic,
        "order": "dp",
        "repair": "SERIALIZE_36_LIFT_ENTRIES_AND_FRESH_REPLAY",
        "v14_compiler_sha256": digest(V14),
        "v14_preregistration_sha256": digest(V14_PREREG),
        "v14_exact_result_sha256": digest(V14_EXACT),
        "v14_base_input_sha256": base_sha,
        "preregistration_sha256": digest(PREREG),
        "input_sha256": digest(singular),
        "replay_prelude_sha256": digest(prelude),
        "scope": "NORMALIZED_K00_UNLOADED_LOCAL_MEMBERSHIP_BY_GLOBAL_COLON_ONLY",
    }
    (output / "compiler_result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
