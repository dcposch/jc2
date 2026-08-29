#!/usr/bin/env python3
"""Three-prime, theorem-ineligible V24 properness preflight."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
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
PREREG = HERE / "PREREGISTRATION_R3_MULTIPRIME_PREFLIGHT.md"
PRIMES = (32003, 65519, 65537)
EXPECTED = {
    PREREG: "0865e3bddbc31e8537f7167bfb08e6e6acd9612a8a6fd457011b2f118e8eef97",
    ORIGINAL: "6f5e8fac9d8f1d06c5a06a3b3f67b1bce776418d977bf6ea80ca064c9fc5b96a",
    V24_RESULT: "22cbd6acb79fc5788afc4b1220cc9eaa19d0a987a2126a49eace67e89ce7921b",
    R1_RESULT: "10cfdfea0c20554d6a65bac99a009bad23fee9babcb62c80f11ed86ee8a96ea4",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V24R3 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V24R3 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def run_prime(prime: int, base_lines: list[str], output: Path,
              singular: str) -> dict[str, object]:
    lane = output / f"p{prime}"
    lane.mkdir()
    ring = base_lines[0].replace("ring R=65521,", f"ring R={prime},", 1)
    if not ring.startswith(f"ring R={prime},"):
        fail(("field conversion failed", prime))
    script = lane / "properness.sing"
    script.write_text("\n".join([
        ring,
        base_lines[1],
        base_lines[2],
        "ideal G=std(P); poly N1=reduce(1,G); int D=dim(G);",
        "ideal Punit=P,1; ideal Gunit=std(Punit); poly Nunit=reduce(1,Gunit);",
        f'print("V24R3_P{prime}_ONE="+string(N1));',
        f'print("V24R3_P{prime}_DIM="+string(D));',
        f'print("V24R3_P{prime}_MUTATION="+string(Nunit==0));',
        "quit;",
    ]) + "\n")
    try:
        completed = subprocess.run(
            [singular, "-q", str(script)], cwd=lane, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=600)
    except subprocess.TimeoutExpired as error:
        (lane / "singular.stdout").write_text(error.stdout or "")
        (lane / "singular.stderr").write_text(error.stderr or "")
        return {"prime": prime, "status": "RESOURCE_CAP",
                "script_sha256": digest(script)}
    (lane / "singular.stdout").write_text(completed.stdout)
    (lane / "singular.stderr").write_text(completed.stderr)
    if completed.returncode != 0 or completed.stderr:
        fail(("Singular failure", prime, completed.returncode,
              completed.stderr[-1000:]))
    one = re.search(fr"V24R3_P{prime}_ONE=([^\n]+)", completed.stdout)
    dim = re.search(fr"V24R3_P{prime}_DIM=(-?\d+)", completed.stdout)
    mutation = re.search(fr"V24R3_P{prime}_MUTATION=([01])", completed.stdout)
    if None in (one, dim, mutation) or mutation.group(1) != "1":
        fail(("marker/mutation failure", prime, completed.stdout[-1000:]))
    one_text = one.group(1).strip()
    dimension = int(dim.group(1))
    if one_text == "0" and dimension == -1:
        status = "UNIT"
    elif one_text == "1" and dimension >= 0:
        status = "PROPER"
    else:
        fail(("inconsistent properness markers", prime, one_text, dimension))
    return {"prime": prime, "status": status, "one_normal_form": one_text,
            "dimension": dimension, "forced_unit_mutation": True,
            "script_sha256": digest(script)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, wanted in EXPECTED.items():
        got = digest(path)
        if got != wanted:
            fail(("frozen input mismatch", str(path), got, wanted))
    if json.loads(R1_RESULT.read_text()).get("status") != (
            "F65521_LOCALIZED_PRIOR_IDEAL_IS_UNIT_NO_MEMBERSHIP_CONCLUSION"):
        fail("V24R1 dependency mismatch")
    lines = ORIGINAL.read_text().splitlines()
    if len(lines) != 11 or not lines[0].startswith("ring R=65521,"):
        fail("V24 script shape mismatch")
    if not lines[1].startswith("ideal P=") or not re.fullmatch(
            r"P=P,zinv\*k10_0\*\(.+\)-1;", lines[2]):
        fail("V24 ideal/localization mismatch")
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    with ThreadPoolExecutor(max_workers=len(PRIMES)) as pool:
        futures = [pool.submit(run_prime, p, lines, output, singular)
                   for p in PRIMES]
        outcomes = [future.result() for future in futures]
    outcomes.sort(key=lambda item: int(item["prime"]))
    payload = {
        "status": "PASS_MULTIPRIME_PREFLIGHT",
        "registered_aws_lane": tag,
        "outcomes": outcomes,
        "input_sha256": {str(path.relative_to(HERE.parents[1])): digest(path)
                         for path in EXPECTED},
        "scope": "THEOREM_INELIGIBLE_MODULAR_PROPERNESS_PREFLIGHT_ONLY",
        "firewall": "NO_EXACT_Q_NO_COMPATIBILITY_NO_STRATUM_NO_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V24R3=PASS_MULTIPRIME_PREFLIGHT")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
