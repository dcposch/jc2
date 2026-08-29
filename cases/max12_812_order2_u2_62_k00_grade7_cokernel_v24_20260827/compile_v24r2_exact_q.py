#!/usr/bin/env python3
"""Exact-Q V24 prior-chart properness and compatibility decision."""

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
V24 = HERE / "aws_r6b_pass/output"
ORIGINAL = V24 / "modular_prior_reduction_v24.sing"
V24_RESULT = V24 / "RESULT.json"
R1_RESULT = HERE / "aws_r6b_r1_unit/output/RESULT.json"
PREREG = HERE / "PREREGISTRATION_R2_EXACT_Q.md"
EXPECTED = {
    PREREG: "c45a59fba4e8af280e6b46576cd57dfaadce4831abefdcb4b5ed5e3f83e4b30d",
    ORIGINAL: "6f5e8fac9d8f1d06c5a06a3b3f67b1bce776418d977bf6ea80ca064c9fc5b96a",
    V24_RESULT: "22cbd6acb79fc5788afc4b1220cc9eaa19d0a987a2126a49eace67e89ce7921b",
    R1_RESULT: "10cfdfea0c20554d6a65bac99a009bad23fee9babcb62c80f11ed86ee8a96ea4",
}


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V24R2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V24R2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def qpath(path: Path) -> str:
    text = str(path.resolve())
    if '"' in text or "\n" in text:
        fail(("unsafe output path", text))
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("frozen input mismatch", str(path), digest(path), expected))
    r1 = json.loads(R1_RESULT.read_text())
    if r1.get("status") != "F65521_LOCALIZED_PRIOR_IDEAL_IS_UNIT_NO_MEMBERSHIP_CONCLUSION":
        fail("V24R1 vacuity result mismatch")

    original = ORIGINAL.read_text().splitlines()
    if len(original) != 11:
        fail(("unexpected V24 script line census", len(original)))
    if not original[0].startswith("ring R=65521,"):
        fail("V24 coefficient-field declaration mismatch")
    ring_q = original[0].replace("ring R=65521,", "ring R=0,", 1)
    if "65521" in ring_q or not ring_q.startswith("ring R=0,"):
        fail("exact-Q ring conversion failed")
    if not original[1].startswith("ideal P=") or not original[1].endswith(";"):
        fail("prior ideal declaration mismatch")
    if not re.fullmatch(r"P=P,zinv\*k10_0\*\(.+\)-1;", original[2]):
        fail("localization declaration mismatch")
    if original[3] != "ideal G=std(P);":
        fail("original standard-basis statement mismatch")
    if not original[4].startswith("poly C6=") or "poly C7=" not in original[4]:
        fail("compatibility declaration mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    basis_path = output / "EXACT_Q_STANDARD_BASIS.txt"
    transform_path = output / "EXACT_Q_LIFTSTD_TRANSFORM.matrix"
    unit_path = output / "EXACT_Q_UNIT_COEFFICIENTS.matrix"
    member_path = output / "EXACT_Q_COMPATIBILITY_COEFFICIENTS.matrix"
    nf6_path = output / "EXACT_Q_C6_NORMAL_FORM.txt"
    nf7_path = output / "EXACT_Q_C7_NORMAL_FORM.txt"
    script = output / "exact_q_v24r2.sing"
    lines = [ring_q, original[1], original[2],
             'if (size(P)!=36) { print("K00_V24R2_FAIL=GENERATOR_CENSUS"); quit; }',
             "matrix T; ideal G=liftstd(P,T);",
             "matrix BASISREPLAY=matrix(P)*T-matrix(G);",
             'if (BASISREPLAY!=0) { print("K00_V24R2_FAIL=LIFTSTD_REPLAY"); quit; }',
             'print("K00_V24R2_LIFTSTD_REPLAY=1");',
             "ideal Punit=P,1; ideal Gunit=std(Punit); poly Nunit=reduce(1,Gunit);",
             'if (Nunit!=0) { print("K00_V24R2_FAIL=FORCED_UNIT_MUTATION"); quit; }',
             'print("K00_V24R2_FORCED_UNIT_MUTATION=1");',
             "poly N1=reduce(1,G); int D=dim(G);",
             'print("K00_V24R2_ONE_NORMAL="+string(N1));',
             'print("K00_V24R2_DIM="+string(D));',
             "if (N1==0)",
             "{",
             "  matrix Hunit=lift(G,ideal(1)); matrix Cunit=T*Hunit;",
             "  matrix UNITREPLAY=matrix(P)*Cunit-matrix(ideal(1));",
             '  if (UNITREPLAY!=0) { print("K00_V24R2_FAIL=UNIT_IDENTITY_REPLAY"); quit; }',
             f'  write("{qpath(unit_path)}",Cunit);',
             '  print("K00_V24R2_UNIT_IDENTITY_REPLAY=1");',
             '  print("K00_V24R2_BRANCH=Q_LOCALIZED_PRIOR_IDEAL_UNIT");',
             "  quit;",
             "}",
             'if ((N1!=1)||(D<0)) { print("K00_V24R2_FAIL=PROPERNESS_MARKERS"); quit; }',
             original[4],
             "poly N6=reduce(C6,G); poly N7=reduce(C7,G);",
             f'write("{qpath(nf6_path)}",N6); write("{qpath(nf7_path)}",N7);',
             'print("K00_V24R2_C6_ZERO="+string(N6==0));',
             'print("K00_V24R2_C7_ZERO="+string(N7==0));',
             "if ((N6==0)&&(N7==0))",
             "{",
             "  ideal TARGET=C6,C7; matrix Hmember=lift(G,TARGET); matrix Cmember=T*Hmember;",
             "  matrix MEMBERREPLAY=matrix(P)*Cmember-matrix(TARGET);",
             '  if (MEMBERREPLAY!=0) { print("K00_V24R2_FAIL=MEMBERSHIP_IDENTITY_REPLAY"); quit; }',
             f'  write("{qpath(member_path)}",Cmember);',
             '  print("K00_V24R2_MEMBERSHIP_IDENTITY_REPLAY=1");',
             '  print("K00_V24R2_BRANCH=Q_PROPER_C6_C7_MEMBERS");',
             "  quit;",
             "}",
             f'write("{qpath(basis_path)}",G); write("{qpath(transform_path)}",T);',
             'print("K00_V24R2_BRANCH=Q_PROPER_COMPATIBILITY_NONMEMBERSHIP");',
             "quit;",
             ]
    script.write_text("\n".join(lines) + "\n")
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    stdout_path = output / "singular.stdout"
    stderr_path = output / "singular.stderr"
    try:
        completed = subprocess.run([singular, "-q", str(script)], cwd=output,
                                   text=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, timeout=21000)
    except subprocess.TimeoutExpired as error:
        stdout_path.write_text(error.stdout or "")
        stderr_path.write_text(error.stderr or "")
        payload = {
            "status": "RESOURCE_CAP_NO_VERDICT",
            "registered_aws_lane": tag,
            "timeout_seconds": 21000,
            "exact_q_script_sha256": digest(script),
            "scope": "NO_EXACT_Q_PROPERNESS_OR_MEMBERSHIP_VERDICT",
            "firewall": "NO_W_ZERO_NO_LATER_GRADES_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
        }
        (output / "RESULT.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
        print("K00_V24R2=RESOURCE_CAP_NO_VERDICT")
        return
    stdout_path.write_text(completed.stdout)
    stderr_path.write_text(completed.stderr)
    if completed.returncode != 0 or completed.stderr:
        fail(("exact-Q Singular failure", completed.returncode, completed.stderr[-2000:]))
    required = ("K00_V24R2_LIFTSTD_REPLAY=1", "K00_V24R2_FORCED_UNIT_MUTATION=1")
    if any(marker not in completed.stdout for marker in required) or "K00_V24R2_FAIL=" in completed.stdout:
        fail(("exact-Q replay marker failure", completed.stdout[-3000:]))

    artifacts: dict[str, dict[str, object]] = {
        script.name: {"sha256": digest(script), "bytes": script.stat().st_size},
        stdout_path.name: {"sha256": digest(stdout_path), "bytes": stdout_path.stat().st_size},
        stderr_path.name: {"sha256": digest(stderr_path), "bytes": stderr_path.stat().st_size},
    }
    if "K00_V24R2_BRANCH=Q_LOCALIZED_PRIOR_IDEAL_UNIT" in completed.stdout:
        if "K00_V24R2_UNIT_IDENTITY_REPLAY=1" not in completed.stdout or not unit_path.is_file():
            fail("missing exact-Q unit certificate")
        status = "PASS_Q_LOCALIZED_PRIOR_IDEAL_UNIT_CHART_EMPTY"
        one_normal, dimension = "0", -1
        artifacts[unit_path.name] = {"sha256": digest(unit_path), "bytes": unit_path.stat().st_size}
        compatibility = "NOT_REDUCED_BECAUSE_PRIOR_CHART_EMPTY"
    elif "K00_V24R2_BRANCH=Q_PROPER_C6_C7_MEMBERS" in completed.stdout:
        if "K00_V24R2_MEMBERSHIP_IDENTITY_REPLAY=1" not in completed.stdout or not member_path.is_file():
            fail("missing exact-Q membership certificate")
        status = "PASS_Q_PROPER_C6_C7_EXACT_MEMBERS"
        one_normal, dimension = "1", int(re.search(r"K00_V24R2_DIM=(-?\d+)", completed.stdout).group(1))
        for path in (member_path, nf6_path, nf7_path):
            artifacts[path.name] = {"sha256": digest(path), "bytes": path.stat().st_size}
        compatibility = "BOTH_EXACT_MEMBERS_WITH_REPLAYED_TWO_COLUMN_IDENTITY"
    elif "K00_V24R2_BRANCH=Q_PROPER_COMPATIBILITY_NONMEMBERSHIP" in completed.stdout:
        if not all(path.is_file() for path in (basis_path, transform_path, nf6_path, nf7_path)):
            fail("missing exact-Q nonmembership custody artifacts")
        status = "PASS_Q_PROPER_COMPATIBILITY_NONMEMBERSHIP_NORMAL_FORMS"
        one_normal, dimension = "1", int(re.search(r"K00_V24R2_DIM=(-?\d+)", completed.stdout).group(1))
        for path in (basis_path, transform_path, nf6_path, nf7_path):
            artifacts[path.name] = {"sha256": digest(path), "bytes": path.stat().st_size}
        compatibility = "AT_LEAST_ONE_EXACT_NONZERO_STANDARD_BASIS_NORMAL_FORM"
    else:
        fail(("missing exact-Q endpoint branch", completed.stdout[-3000:]))

    payload = {
        "status": status,
        "registered_aws_lane": tag,
        "field": "Q_exact",
        "generator_count_after_localization": 36,
        "one_normal_form": one_normal,
        "localized_ideal_dimension": dimension,
        "liftstd_basis_replay": True,
        "forced_unit_mutation_detected": True,
        "compatibility_outcome": compatibility,
        "artifacts": artifacts,
        "input_sha256": {str(path.relative_to(HERE.parents[1])): digest(path)
                         for path in EXPECTED},
        "scope": "EXACT_Q_V24_PRIOR_PREFIX_AND_GRADE7_COMPATIBILITY_ON_D_K10_0_W_ONLY",
        "firewall": "NO_W_ZERO_NO_OTHER_STRATA_NO_GRADES8TO19_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V24R2=" + status)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
