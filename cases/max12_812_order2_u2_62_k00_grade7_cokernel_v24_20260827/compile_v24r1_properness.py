#!/usr/bin/env python3
"""Narrow V24R1 modular unit-ideal/properness repair."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess


HERE = Path(__file__).resolve().parent
HARVEST = HERE / "aws_r6b_pass/output"
ORIGINAL = HARVEST / "modular_prior_reduction_v24.sing"
RESULT = HARVEST / "RESULT.json"
NF6 = HARVEST / "MODULAR_C6_NORMAL_FORM.txt"
NF7 = HARVEST / "MODULAR_C7_NORMAL_FORM.txt"
PREREG = HERE / "PREREGISTRATION_R1_PROPERNESS.md"
EXPECTED = {
    PREREG: "3e6ddcceaae46731b9fb19d8e194df065207824404c2fb620afeb442e87cbabb",
    ORIGINAL: "6f5e8fac9d8f1d06c5a06a3b3f67b1bce776418d977bf6ea80ca064c9fc5b96a",
    RESULT: "22cbd6acb79fc5788afc4b1220cc9eaa19d0a987a2126a49eace67e89ce7921b",
    NF6: "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
    NF7: "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V24R1 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V24R1 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, wanted in EXPECTED.items():
        got = digest(path)
        if got != wanted:
            fail(("frozen V24 input mismatch", str(path), got, wanted))
    if NF6.read_bytes() != b"0\n" or NF7.read_bytes() != b"0\n":
        fail("V24 modular normal-form bytes are not exact zero polynomials")
    result = json.loads(RESULT.read_text())
    if result.get("modular_reduction_status") != "F65521_C6_ZERO_1_C7_ZERO_1":
        fail("V24 modular status mismatch")

    lines = ORIGINAL.read_text().splitlines()
    if len(lines) != 11:
        fail(("unexpected original script line census", len(lines)))
    if not lines[0].startswith("ring R=65521,"):
        fail("ring declaration mismatch")
    if not lines[1].startswith("ideal P=") or not lines[1].endswith(";"):
        fail("prior ideal declaration mismatch")
    if not re.fullmatch(r"P=P,zinv\*k10_0\*\(.+\)-1;", lines[2]):
        fail("localization equation mismatch")
    if lines[3] != "ideal G=std(P);":
        fail("original standard-basis line mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    script = output / "properness_v24r1.sing"
    script.write_text("\n".join(lines[:3] + [
        "ideal G=std(P);",
        "poly N1=reduce(1,G);",
        "int D=dim(G);",
        "ideal Punit=P,1; ideal Gunit=std(Punit); poly Nunit=reduce(1,Gunit);",
        'print("K00_V24R1_ONE_NORMAL="+string(N1));',
        'print("K00_V24R1_DIM="+string(D));',
        'print("K00_V24R1_UNIT_MUTATION_ZERO="+string(Nunit==0));',
        'print("K00_V24R1_PROPER="+string((N1==1) && (D>=0)));',
        "quit;",
    ]) + "\n")
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    try:
        completed = subprocess.run([singular, "-q", str(script)], cwd=output,
                                   text=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, timeout=600)
    except subprocess.TimeoutExpired as error:
        (output / "singular.stdout").write_text(error.stdout or "")
        (output / "singular.stderr").write_text(error.stderr or "")
        payload = {
            "status": "RESOURCE_CAP_NO_VERDICT",
            "registered_aws_lane": tag,
            "timeout_seconds": 600,
            "firewall": "NO_Q_MEMBERSHIP_NO_GRADE8_NO_ARC_NO_CLOSURE_NO_JC2",
        }
        (output / "RESULT.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
        print("K00_V24R1=RESOURCE_CAP_NO_VERDICT")
        return
    (output / "singular.stdout").write_text(completed.stdout)
    (output / "singular.stderr").write_text(completed.stderr)
    if completed.returncode != 0 or completed.stderr:
        fail(("Singular failure", completed.returncode, completed.stderr[-1000:]))
    one = re.search(r"K00_V24R1_ONE_NORMAL=([^\n]+)", completed.stdout)
    dim = re.search(r"K00_V24R1_DIM=(-?\d+)", completed.stdout)
    mutation = re.search(r"K00_V24R1_UNIT_MUTATION_ZERO=([01])", completed.stdout)
    proper = re.search(r"K00_V24R1_PROPER=([01])", completed.stdout)
    if None in (one, dim, mutation, proper):
        fail("missing V24R1 markers")
    if mutation.group(1) != "1":
        fail("unit-ideal mutation did not fire")
    is_proper = proper.group(1) == "1"
    if is_proper and (one.group(1).strip() != "1" or int(dim.group(1)) < 0):
        fail("inconsistent properness markers")
    status = ("PASS_F65521_PROPER_LOCALIZED_PRIOR_IDEAL_AND_ZERO_NORMAL_FORMS"
              if is_proper else
              "F65521_LOCALIZED_PRIOR_IDEAL_IS_UNIT_NO_MEMBERSHIP_CONCLUSION")
    payload = {
        "status": status,
        "registered_aws_lane": tag,
        "field": "F_65521",
        "one_normal_form": one.group(1).strip(),
        "localized_ideal_dimension": int(dim.group(1)),
        "unit_mutation_detected": True,
        "v24_zero_normal_forms_replayed": True,
        "script_sha256": digest(script),
        "input_sha256": {str(path.relative_to(HERE.parents[1])): digest(path)
                          for path in EXPECTED},
        "scope": "MODULAR_PROPERNESS_AND_V24_ZERO_NORMAL_FORMS_ON_D_K10_0_W_ONLY",
        "firewall": "NO_EXACT_Q_MEMBERSHIP_NO_W_ZERO_NO_GRADE8_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V24R1=" + status)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
