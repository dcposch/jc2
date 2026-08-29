#!/usr/bin/env python3
"""Additive output-directory idempotence shim for frozen V43C3D v2."""

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
V2 = HERE / "diagnose_v43c3d_v2.py"
V2_SHA256 = "4312ff085e502963f04f4f8e2adc896f1f10fc9f00f48f8f2a93415fc969934b"


def main() -> None:
    if len(sys.argv) != 2:
        raise RuntimeError("usage: diagnose_v43c3d_v3.py OUTPUT")
    if sha256(V2.read_bytes()).hexdigest() != V2_SHA256:
        raise RuntimeError("V43C3D v2 source pin")
    output = Path(sys.argv[1]).resolve()
    original_mkdir = Path.mkdir

    def registered_output_mkdir(path, mode=0o777, parents=False, exist_ok=False):
        resolved = path.resolve()
        if resolved == output and resolved.is_dir():
            return None
        return original_mkdir(path, mode=mode, parents=parents, exist_ok=exist_ok)

    spec = importlib.util.spec_from_file_location("frozen_v43c3d_v2", V2)
    if spec is None or spec.loader is None:
        raise RuntimeError("V43C3D v2 import")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    Path.mkdir = registered_output_mkdir
    try:
        module.main()
    finally:
        Path.mkdir = original_mkdir


if __name__ == "__main__":
    main()
