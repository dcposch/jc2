#!/usr/bin/env python3
"""Additive tag-compatibility wrapper for the frozen V43C3D diagnostic."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
V1 = HERE / "diagnose_v43c3d.py"
V1_SHA256 = "3aa423ffe751d0acfab117319d0e4d6778898f9f7e97541a270457218a2b5f8b"
COMPATIBLE_PREFIX = "max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_rebased_v43c3_diagnostic_v43c3d_"


def main() -> None:
    if sha256(V1.read_bytes()).hexdigest() != V1_SHA256:
        raise RuntimeError("V43C3D v1 source pin")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag.startswith(COMPATIBLE_PREFIX):
        raise RuntimeError("compatible V43C3/V43C3D AWS tag required")
    spec = importlib.util.spec_from_file_location("frozen_v43c3d_v1", V1)
    if spec is None or spec.loader is None:
        raise RuntimeError("V43C3D v1 import")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.TAG_PREFIX = COMPATIBLE_PREFIX
    module.main()


if __name__ == "__main__":
    main()
