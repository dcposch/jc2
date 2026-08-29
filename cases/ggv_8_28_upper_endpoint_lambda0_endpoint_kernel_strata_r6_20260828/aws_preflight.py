#!/usr/bin/env python3
"""Hash-pinned r6 tag adapter around the frozen r2 EC2 preflight."""

from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path


R2_PREFLIGHT_SHA256 = "a6cc2720e12b423cb70b5bed098bb0a8ded2bf4f58967ebddadf7a06cc4a8105"


def main() -> None:
    case_dir = Path(__file__).resolve().parent
    r2_path = case_dir.parent / "ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r2_20260828" / "aws_preflight.py"
    if hashlib.sha256(r2_path.read_bytes()).hexdigest() != R2_PREFLIGHT_SHA256:
        raise SystemExit("R2_PREFLIGHT_SOURCE_DRIFT")
    spec = importlib.util.spec_from_file_location("frozen_r2_preflight", r2_path)
    if spec is None or spec.loader is None:
        raise SystemExit("R2_PREFLIGHT_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for lane, data in module.LANES.items():
        old = data["tag"]
        new = old.replace("_r2_20260828T133400Z_", "_r6_20260828T140500Z_")
        if new == old:
            raise SystemExit(f"R6_TAG_TRANSFORM_FAILURE:{lane}")
        data["tag"] = new
    module.main()


if __name__ == "__main__":
    main()
