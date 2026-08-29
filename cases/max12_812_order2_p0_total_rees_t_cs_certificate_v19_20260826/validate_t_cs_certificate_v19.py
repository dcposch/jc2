#!/usr/bin/env python3
"""Fail-closed validator for the V19 explicit unit certificate."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compiler-result", type=Path, required=True)
    parser.add_argument("--stdout", type=Path, required=True)
    parser.add_argument("--stderr", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    compiler = json.loads(args.compiler_result.read_text())
    if (
        compiler.get("status") != "PASS-T-CS-EXPLICIT-UNIT-CERTIFICATE-V19-COMPILER"
        or compiler.get("characteristic") != args.characteristic
        or compiler.get("input_count") != 22
        or compiler.get("raw_generator_count") != 26
    ):
        raise RuntimeError("compiler result contract")
    script = Path(compiler["script"])
    text = script.read_text()
    if (
        digest(script) != compiler.get("script_sha256")
        or "qring " in text
        or "ideal E12=" in text
        or text.count("ideal Prefix12=") != 1
        or text.count("ideal RawSpecial=E+Localizers;") != 1
        or text.count("lift(RawSpecial,ONE,LiftUnit)") != 1
        or "NoG14" in text
    ):
        raise RuntimeError("script hash or transform sentinel")

    stdout = args.stdout.read_text()
    stderr = args.stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError(("resource stderr", stderr[-2000:]))
    forbidden = ("FAIL_", "?", "error occurred", "Killed", "out of memory", "Segment fault")
    if any(token in stdout or token in stderr for token in forbidden):
        raise RuntimeError(("diagnostic token", [t for t in forbidden if t in stdout or t in stderr]))
    required = (
        "V18_QRING_DISABLED=1",
        f"V18_CHARACTERISTIC={args.characteristic}",
        "V18_CHART=V_QRS_INTERSECT_DPLUS_CS_INTERSECT_DK",
        "V18_INPUT_COUNT=22",
        "V18_SPECIAL_FIBRE_UNIT=1",
        "V19_LIFT_RESIDUAL_ZERO=1",
        "V19_LIFT_SCALAR_NONZERO_CONSTANT=1",
        "V19_ARTIFACT_WRITES=3",
        "V19_RAW_GENERATOR_COUNT=26",
        "V19_SCOPE=T_CS_ORDERED_COMPLEMENT_DK_PREFIX_G10_G11_G12_G14_ONLY",
        "PASS_T_CS_EXPLICIT_UNIT_CERTIFICATE_V19",
    )
    for token in required:
        if stdout.count(token) != 1:
            raise RuntimeError(("required token", token, stdout.count(token)))

    artifacts = {}
    for raw in compiler.get("artifacts", []):
        path = Path(raw)
        if not path.is_file() or path.stat().st_size == 0:
            raise RuntimeError(("missing artifact", path))
        artifacts[path.name] = {"sha256": digest(path), "bytes": path.stat().st_size}
    expected = {"unit_certificate.matrix", "lift_unit.matrix", "raw_special.ideal"}
    if set(artifacts) != expected:
        raise RuntimeError(("artifact set", sorted(artifacts)))

    result = {
        "status": "PASS-T-CS-EXPLICIT-UNIT-CERTIFICATE-V19",
        "characteristic": args.characteristic,
        "scope": "T_CS_ORDERED_COMPLEMENT_DK_PREFIX_G10_G11_G12_G14_ONLY",
        "raw_generator_count": 26,
        "lift_residual_zero": True,
        "lift_scalar_nonzero_constant": True,
        "compiler_result_sha256": digest(args.compiler_result),
        "script_sha256": digest(script),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
        "artifacts": artifacts,
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
