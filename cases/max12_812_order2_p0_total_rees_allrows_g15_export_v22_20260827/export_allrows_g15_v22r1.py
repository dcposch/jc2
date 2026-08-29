#!/usr/bin/env python3
"""V22R1: defer serialization-only bridges to exact Singular equality."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
V1 = HERE / "export_allrows_g15_v22.py"
V1_SHA256 = "c965726d2308358bf01c533fe89f2e28551abd9e3549fc699cd3e36d40ac82a6"
PREREG_R1 = HERE / "PREREGISTRATION_R1.md"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_v1():
    if digest(V1) != V1_SHA256:
        raise RuntimeError("frozen V22 V1 exporter hash mismatch")
    spec = importlib.util.spec_from_file_location("v22_v1_frozen_for_r1", V1)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import V22 V1")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    v1 = load_v1()
    deferred: list[list[int]] = []
    original_fail = v1.fail

    def repaired_fail(message: object) -> None:
        if (
            isinstance(message, tuple)
            and len(message) == 3
            and message[0] == "old coefficient byte bridge"
            and isinstance(message[1], int)
            and isinstance(message[2], int)
        ):
            deferred.append([message[1], message[2]])
            return
        original_fail(message)

    v1.fail = repaired_fail
    v1.compile_export(args.output, args.characteristic, v1.require_aws())
    if not 1 <= len(deferred) <= 35 or len({tuple(item) for item in deferred}) != len(deferred):
        raise RuntimeError(("serialization deferral census", deferred))
    result_path = args.output.resolve() / "result.json"
    result = json.loads(result_path.read_text())
    if result.pop("old_coefficient_byte_bridges", None) != 35:
        raise RuntimeError("missing V1 bridge field")
    result["status"] = "PASS-TOTAL-REES-ALLROWS-G15-EXPORT-V22R1-COMPILER"
    result["old_coefficient_exact_polynomial_bridges"] = 35
    result["serialization_only_bridge_deferrals"] = deferred
    result["v22_v1_exporter_sha256"] = V1_SHA256
    result["preregistration_r1_sha256"] = digest(PREREG_R1)
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
