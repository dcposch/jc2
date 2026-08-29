#!/usr/bin/env python3
"""AWS-only compiler for the g-open acceleration of K00 closure V1."""

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
V1 = (
    ROOT
    / "cases/max12_812_order2_u2_62_k00_closure_incidence_v1_20260827"
    / "compile_k00_closure.py"
)
V1_SHA = "2ab821668d6f9f9dd82476359f2c8bdcfc1f5c7b6090d33f553d5f12a41f9a62"
PROOF = HERE / "EQUIVALENCE_AND_PREREGISTRATION.md"
PROOF_SHA = "11166c81c6017d593b2b17cba8325d97f900c639999907d5eeaf269ff16dc936"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only g-open compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only g-open compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    if digest(V1) != V1_SHA:
        fail("V1 compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("k00_closure_v1", V1)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V1 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), default=65519)
    args = parser.parse_args()
    tag = require_aws()
    base = load_v1()
    for source, expected in base.INPUTS.items():
        if digest(source) != expected:
            fail(("V1 frozen source mismatch", source))
    if digest(PROOF) != PROOF_SHA:
        fail("g-open equivalence/preregistration hash mismatch")

    tails = json.loads(base.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != base.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    baseline = output / "baseline_v1.sing"
    base.emit(baseline, args.characteristic, tails)
    source = baseline.read_text()
    old = "\n".join([
        'print("K00_STAGE_CLOSURE_LAMBDA_START");',
        "ideal KL=sat(I,ideal(Lambda));",
        'print("K00_STAGE_CLOSURE_LAMBDA_DONE");',
        'print("K00_KL_SIZE="+string(size(KL)));',
        'print("K00_STAGE_CLOSURE_JDET_START");',
        "ideal K=sat(KL,ideal(Jdet));",
        'print("K00_STAGE_CLOSURE_JDET_DONE");',
        'print("K00_K_SIZE="+string(size(K)));',
        "ideal B=K+ideal(Lambda)+MK00;",
        'print("K00_STAGE_BOUNDARY_CORE_DONE");',
        'print("K00_B_SIZE="+string(size(B)));',
        "poly finalLocalizer=C6*k10*Jdet;",
        'print("K00_STAGE_FINAL_LOCALIZATION_START");',
        "list Hdata=sat_with_exp(B,ideal(finalLocalizer));",
    ])
    new = "\n".join([
        "poly finalLocalizer=C6*k10*Jdet;",
        'print("K00_GOPEN_EQUIVALENCE=SAT_G_CONTRACTION");',
        'print("K00_STAGE_GOPEN_SOURCE_START");',
        "ideal Kopen=sat(I,ideal(Lambda*finalLocalizer));",
        'print("K00_STAGE_GOPEN_SOURCE_DONE");',
        'print("K00_GOPEN_SIZE="+string(size(Kopen)));',
        "ideal B=Kopen+ideal(Lambda)+MK00;",
        'print("K00_STAGE_BOUNDARY_CORE_DONE");',
        'print("K00_B_SIZE="+string(size(B)));',
        'print("K00_STAGE_FINAL_LOCALIZATION_START");',
        "list Hdata=sat_with_exp(B,ideal(finalLocalizer));",
    ])
    if source.count(old) != 1:
        fail("V1 closure block not found uniquely")
    source = source.replace(old, new)
    source = source.replace(
        'print("K00_CLOSURE_FIRST_ORDER=PASS");',
        'print("K00_GOPEN_OPERATION_ORDER=PASS");',
    )
    singular = output / f"k00_gopen_char{args.characteristic}.sing"
    singular.write_text(source)
    baseline.unlink()

    payload = {
        "status": "PASS-K00-GOPEN-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "singular_input_sha256": digest(singular),
        "v1_compiler_sha256": digest(V1),
        "equivalence_proof_sha256": digest(PROOF),
        "algorithm": "Sat_g(Sat_(Lambda*g)(I)+(Lambda)+M_K00)",
        "g": "C6*k10*Jdet",
        "role": "EXACT_EQUIVALENT_ACCELERATION_OF_V1_H",
        "scope": {
            "same_final_H_unit_test_as_v1": True,
            "fixed_source_profile": "U=2,[6,2],ordinary-tail",
            "full_collision_receiver": "NOT_TESTED",
            "taylor_realization": "NOT_TESTED",
            "order2_closed": False,
            "JC2": "NOT_CLAIMED",
        },
    }
    (output / "compiler_result.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n"
    )
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
